---
title: Concurrency and Shared State
sidebar_position: 17
---

# Concurrency and Shared State

Rust cannot decide a scheduling policy or prove that every concurrent protocol makes progress. It can enforce who owns data crossing a thread boundary and whether a shared type permits safe access. Spawned closures, channels, `Arc`, locks, atomics, and the marker traits `Send` and `Sync` express different parts of that contract.

Memory safety is only the first threshold. A program can be free of data races and still deadlock, starve a worker, process messages in an unintended order, or spend all its time contending for one lock. The ownership model narrows the failure space; protocol design still matters.

## A spawned thread owns a unit of work

`std::thread::spawn` starts a new thread and returns a `JoinHandle<T>`, where `T` is the closure's return type. Calling `join` waits for completion and returns `std::thread::Result<T>`. The error side carries the payload of a worker panic.

```rust
use std::thread;

let handle = thread::spawn(|| {
    let mut total = 0;
    for n in 1..=4 {
        total += n;
    }
    total
});

let total = handle.join().expect("worker panicked");
assert_eq!(total, 10);
```

The worker computes $1+2+3+4=10$ and returns the integer. `join` does two jobs: it prevents the caller from continuing past that point before the worker finishes, and it transfers the return value or panic outcome back to the caller.

Dropping a `JoinHandle` detaches the thread; it does not cancel or join it. A short-lived process may exit before detached work finishes, and a detached panic can be easy to miss. Retain and join handles when completion is part of correctness.

### Why unscoped threads often need `move`

The closure passed to `spawn` may outlive the stack frame that created it. A borrow of an ordinary local therefore cannot satisfy the required `'static` bound:

```rust
use std::thread;

let values = vec![1, 2, 3];
let handle = thread::spawn(move || values.iter().sum::<i32>());
let sum = handle.join().unwrap();

assert_eq!(sum, 6);
// `values` was moved into the closure
```

`move` transfers the vector into the closure object, so the worker owns valid data for its entire lifetime. The keyword does not necessarily make the closure callable only once; here the thread API itself consumes and calls the closure once.

`thread::scope` provides another shape. Scoped threads are guaranteed to join before the scope returns, so they may borrow local data whose lifetime covers the scope:

```rust
use std::thread;

let values = [2, 4, 6, 8];
let (left, right) = values.split_at(2);

let total = thread::scope(|scope| {
    let a = scope.spawn(|| left.iter().sum::<i32>());
    let b = scope.spawn(|| right.iter().sum::<i32>());
    a.join().unwrap() + b.join().unwrap()
});

assert_eq!(total, 20);
```

The two immutable slices borrow disjoint parts of `values`. The scope cannot finish while either child remains running, which proves that both borrows end before the array leaves scope.

## Channels transfer ownership with a protocol

`std::sync::mpsc::channel` creates a multi-producer, single-consumer channel. `Sender<T>` values can be cloned; one `Receiver<T>` owns the receiving side. Sending moves a non-`Copy` value into the channel, and receiving moves it out.

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();

let worker = thread::spawn(move || {
    let message = String::from("finished");
    tx.send(message).expect("receiver dropped");
    // `message` has moved into the channel
});

assert_eq!(rx.recv().unwrap(), "finished");
worker.join().unwrap();
```

An unbounded channel's `send` queues without waiting for capacity, though allocation can still fail by aborting the process. `sync_channel(capacity)` creates a bounded channel whose sends can block until space is available. A zero-capacity synchronous channel forms a rendezvous: sender and receiver meet for each message.

`recv` blocks until a value arrives or every sender is dropped. `try_recv` returns immediately. Iterating a receiver repeatedly calls `recv` and ends only after disconnection, so retaining an unused sender can make the loop wait forever.

### Worked fan-in: two producers, one receiver

Two workers can calculate squares and send `(input, square)` pairs to one receiver:

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();
let mut handles = Vec::new();

for inputs in [vec![1, 3, 5], vec![2, 4, 6]] {
    let tx = tx.clone();
    handles.push(thread::spawn(move || {
        for input in inputs {
            tx.send((input, input * input)).unwrap();
        }
    }));
}

drop(tx);

let mut results: Vec<_> = rx.into_iter().collect();
results.sort_unstable_by_key(|(input, _)| *input);

for handle in handles {
    handle.join().unwrap();
}

assert_eq!(
    results,
    vec![(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
);
```

The ownership and termination steps are:

1. Each loop iteration moves one input vector and one cloned transmitter into a worker.
2. A tuple is created for each number and moved into the channel.
3. Messages from one sender preserve that sender's order, but scheduling can interleave the two producers differently on each run.
4. The original transmitter is dropped in main. When both workers finish, their transmitter clones also drop.
5. Only then can receiver iteration observe disconnection and end.
6. Sorting makes the final assertion independent of cross-producer arrival order.

The message type describes the protocol. A domain enum can make several message variants explicit and require the receiver to handle each. Channels avoid shared mutable payload state, but they do not remove backpressure, shutdown, error propagation, or ordering decisions.

## Shared mutation needs ownership and exclusion

`Mutex<T>` protects a value by allowing one guard at a time. It does not provide multiple ownership. `Arc<T>` provides atomic reference-counted ownership across threads. It does not allow arbitrary mutation through shared references. `Arc<Mutex<T>>` combines the two independent requirements.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0u64));
let mut handles = Vec::new();

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    handles.push(thread::spawn(move || {
        let mut value = counter.lock().expect("counter mutex poisoned");
        *value += 1;
    }));
}

for handle in handles {
    handle.join().expect("worker panicked");
}

assert_eq!(*counter.lock().unwrap(), 10);
```

Trace one iteration and the final read:

1. `Arc::clone` creates another owning pointer to the same mutex; it does not copy the integer.
2. The cloned pointer moves into the worker closure.
3. `lock` waits until it can return a `MutexGuard<u64>`.
4. Dereferencing the guard reaches the protected counter, and `+= 1` performs the update while exclusion is held.
5. The guard drops at the end of the closure and unlocks the mutex.
6. The worker's `Arc` clone drops. The allocation remains because main and other workers still own clones.
7. After all joins, every successful increment has completed, so main reads 10 under the lock.

Replacing `Arc` with `Rc` fails to compile because `Rc` updates a non-atomic reference count and is not `Send`. Replacing the mutex with `RefCell` also fails across threads; its borrow checks are run-time checks for single-threaded interior mutability, not cross-thread synchronization.

## The guard's scope is the critical section

A mutex unlocks when its guard is dropped. Keep the guard only while protected invariants are being read or changed:

```rust
let snapshot = {
    let mut state = shared.lock().unwrap();
    state.update();
    state.clone_for_report()
}; // guard drops here

write_slow_report(snapshot);
```

The slow operation runs after unlocking. Holding a guard during file I/O, sleep, user callbacks, or channel communication can serialize unrelated work and create dependency cycles. A narrow critical section should still be logically complete: reading, checking, and updating a shared invariant may need one uninterrupted lock acquisition.

Standard-library mutexes are poisoned when a thread panics while holding the guard. A later `lock` returns `PoisonError` because the protected value may have been left between invariant-preserving steps. Calling `unwrap` or `expect` chooses to propagate failure as another panic. Recovery can call `into_inner` on the poison error, but only code that understands and repairs the invariant should do so.

Poisoning is advisory, not a universal proof that state is corrupt or sound. Some panic paths occur before mutation; some invariant violations may occur without a panic. The application still defines what recovery means.

## Picking a synchronization primitive

| Need | Standard tool | Main constraint |
|---|---|---|
| One owner sends values to one receiver | `mpsc` channel | Receiver is single; ordering across producers is unspecified |
| Shared mutable compound state | `Mutex<T>` | One guard at a time |
| Many readers or one writer | `RwLock<T>` | Workload and implementation determine whether it beats a mutex |
| Wait until a protected predicate changes | `Condvar` with `Mutex<T>` | Predicate must be checked in a loop |
| Atomic counter or flag | `Atomic*` types | Memory ordering and single-value invariants |
| Shared read-only data | `Arc<T>` | Inner type must be safe to share |

`RwLock` permits several readers or one writer. It helps when read sections are frequent and long enough to offset its overhead; it can perform worse than a mutex for tiny sections or write-heavy workloads. It also does not guarantee a particular fairness policy.

A condition variable lets a thread sleep while a mutex-protected predicate is false. Waiting atomically releases the mutex and later reacquires it. The predicate belongs in a `while` loop because notifications can be spurious and another thread may change state before the awakened thread gets the lock.

Atomics are appropriate when the invariant fits one atomic value or a carefully designed lock-free protocol. A simple statistics counter can use `AtomicUsize`:

```rust
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;

let count = Arc::new(AtomicUsize::new(0));
let mut handles = Vec::new();

for _ in 0..10 {
    let count = Arc::clone(&count);
    handles.push(thread::spawn(move || {
        count.fetch_add(1, Ordering::Relaxed);
    }));
}

for handle in handles {
    handle.join().unwrap();
}

assert_eq!(count.load(Ordering::Relaxed), 10);
```

Relaxed ordering is sufficient here because only atomicity of the counter updates is needed, and `join` separately establishes that workers have completed before the final observation. If the counter publishes or guards access to other memory, stronger ordering or a lock may be required. Guessing at atomic orderings is unsafe design even when the code type-checks.

## Deadlock remains possible in safe Rust

Two threads can deadlock if each holds one mutex and waits for the other. The type system prevents unsynchronized access, not cyclic waiting. Establish a global lock order and acquire multiple locks only in that order. Avoid calling unknown code while holding a lock because the callback may try to acquire another lock or re-enter the same state.

Channels can deadlock too. Two workers using bounded channels may each block sending while neither reaches its receive. A coordinator can wait forever because an extra sender was never dropped. Liveness analysis must include blocking sends, receives, joins, locks, and shutdown signals as one protocol.

Lock-free does not mean wait-free, fair, or fast. Under contention, repeated compare-and-swap retries can starve. Conversely, a well-scoped mutex may be easier to audit and faster than a complicated atomic design.

## `Send` and `Sync` express thread-safety composition

`Send` means ownership of a value may be transferred to another thread. `Sync` means a shared reference `&T` may be used from several threads; equivalently, `&T` is `Send`. Most standard and user-defined types receive these marker traits automatically when their components permit it.

`Rc<T>` is not `Send` or `Sync`; `Arc<T>` uses atomic count updates and can cross threads when its inner type satisfies the required bounds. A raw pointer does not gain a thread-safety story merely because it sits inside a struct.

Manual `unsafe impl Send` or `unsafe impl Sync` asserts that all hidden invariants make cross-thread use sound. The compiler cannot verify that assertion. Such implementations need the same audit as other unsafe code and should never be added solely to silence a trait-bound error.

These traits concern memory safety, not application semantics. A type can be `Send + Sync` while its methods permit deadlock or a logically inconsistent sequence of calls. Document protocol constraints separately.

## Shutdown is part of the protocol

Threads have no safe general-purpose “kill” operation. Cancellation is cooperative: a worker receives a stop message, observes an atomic flag, notices channel disconnection, or reaches another defined cancellation point. It then leaves its current invariant valid, drops guards and resources, and returns.

Channel ownership often supplies a clean shutdown signal. A worker looping over `Receiver<T>` exits when every sender has been dropped. The coordinator must therefore drop its own sender before joining the worker; joining first can deadlock because the worker is still waiting for a message from a sender held by the joining thread.

An explicit message enum can distinguish work from orderly shutdown:

```rust
enum Command {
    Run(Job),
    Stop,
}
```

One `Stop` message is enough only for a single receiver that owns the work loop. A pool with several workers needs a protocol that wakes each worker or closes the shared queue. The design must also decide whether queued jobs finish, are returned, or are abandoned after cancellation.

Error paths need the same lifecycle. If one worker fails, the coordinator may have to stop producing, notify peers, drain or close channels, and still join every handle so panics and resources are accounted for. Returning early with live handles and senders can leave background work running longer than the caller expects.

Timeouts bound waiting but do not repair the underlying operation. `recv_timeout` can let a coordinator recheck cancellation or health, while a timed lock can avoid an indefinite wait in APIs that provide one. Repeated short timeouts create polling overhead and still require a rule for what happens when the deadline expires.

## Questions to settle before adding threads

- Is the workload large enough to offset thread creation, coordination, and cache costs?
- Can ownership be transferred through tasks or messages instead of shared mutation?
- How are worker errors and panics returned to the coordinator?
- What closes the protocol, drops senders, and joins workers during normal shutdown and early error paths?
- Which invariant does each lock protect, and in what order may locks be acquired?
- Does any critical section perform blocking I/O, wait on a channel, or call user code?
- Are result order and message order specified, or should tests normalize them?

<div className="see-also">

See also: [Ownership, References, and Slices](/cs/programming/rust/ownership-references-slices) · [Closures and Iterators](/cs/programming/rust/closures-and-iterators) · [Smart Pointers](/cs/programming/rust/smart-pointers) · [Multithreaded Web Server](/cs/programming/rust/multithreaded-web-server)

</div>
