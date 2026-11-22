---
title: Threads, Synchronization, and the Memory Model
sidebar_position: 15
---

# Threads, Synchronization, and the Memory Model

A thread is a path of execution within one process. Java threads share the heap, so two threads can reach the same object while keeping separate stacks and local variables. That combination is useful and dangerous: communication can be as cheap as assigning a field, but correctness can depend on an interleaving that almost never appears during a casual test run.

Concurrency bugs fall into several different categories. **Atomicity** asks whether an operation can be observed halfway through. **Visibility** asks whether one thread is required to see another thread's write. **Ordering** asks which apparent reorderings the compiler, runtime, and processor may expose. **Liveness** asks whether useful work eventually continues. A lock can help with all four, but only when every access follows one coherent locking policy.

## A task is not a thread

`Runnable` describes work through its `run` method. `Thread` is an execution mechanism that can run that work and is scheduled by the JVM and operating system.

```java
Runnable work = () -> System.out.println(Thread.currentThread().getName());

Thread worker = new Thread(work, "worker-1");
worker.start();
```

Calling `start()` arranges for a new thread to execute `run()`. Calling `worker.run()` directly is an ordinary method call on the current thread. The distinction is observable:

```java
Thread worker = new Thread(
    () -> System.out.println(Thread.currentThread().getName()),
    "worker-1"
);

worker.run();   // prints the caller's thread name, usually "main"
worker.start(); // prints "worker-1"
```

A `Thread` can be started only once. A second call to `start()` throws `IllegalThreadStateException`, even if the first execution has already finished. Code that needs to submit many independent tasks normally uses an executor rather than repeatedly constructing and coordinating raw threads.

Thread scheduling supplies no useful default order. Starting thread A before thread B does not guarantee that A finishes first, reaches a particular statement first, or receives more CPU time. Any required order must be expressed by synchronization, `join`, a queue, a latch, or another concurrency abstraction.

## Worked race: where the missing hundred goes

Suppose an account begins with balance `0`, and two threads each execute `balance += 100`. That statement looks indivisible in source, but it is a read-modify-write operation:

1. Thread A reads `balance`, obtaining `0`.
2. A is paused before storing its result.
3. Thread B reads the same field, also obtaining `0`.
4. B adds `100` and writes `100`.
5. A resumes, adds `100` to its earlier value, and writes `100`.

Both calls returned, yet one update was lost. Declaring `balance` as `volatile` would not repair the algorithm. Each read and write would gain visibility guarantees, but the pair could still interleave exactly as above.

Every Java object has an associated monitor. A synchronized instance method locks the receiver; a synchronized static method locks the corresponding `Class` object. A synchronized block locks the object named by its expression. The account can use its own monitor as the guard:

```java
final class Account {
    private int balance; // guarded by this

    public synchronized void deposit(int amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("negative deposit");
        }
        balance += amount;
    }

    public synchronized int balance() {
        return balance;
    }
}
```

Now the two deposits proceed as follows:

1. A acquires the account monitor.
2. A reads `0`, computes `100`, and writes `100` while B cannot enter `deposit`.
3. A releases the monitor on method exit.
4. B acquires that same monitor, reads `100`, computes `200`, and writes `200`.
5. B releases the monitor. A later synchronized call to `balance()` reads `200`.

The lock covers the invariant, not merely a suspicious line. If a withdrawal must check that funds are sufficient and then subtract, the check and subtraction belong in one critical section. Splitting them into separately synchronized methods would allow another operation between the check and update.

```java
public synchronized boolean withdraw(int amount) {
    if (amount < 0) {
        throw new IllegalArgumentException("negative withdrawal");
    }
    if (balance < amount) {
        return false;
    }
    balance -= amount;
    return true;
}
```

Synchronized methods are reentrant. If a thread holding an object's monitor calls another synchronized method on the same object, it may acquire the monitor again and must release it the corresponding number of times. Reentrancy permits synchronized methods to compose without self-deadlock, though deadlock involving several different locks remains possible.

## The memory model's ordering contract

Source order alone does not define what another thread may observe. Compilers and processors may reorder operations when that reordering preserves the behavior of a single thread. Hardware caches and store buffers also mean that a write need not become promptly observable everywhere. The Java Memory Model describes allowed observations through the **happens-before** relation.

If action A happens-before action B, then A's effects are visible to B and A is ordered before B. The relation is transitive. Several rules matter frequently:

| Earlier action | Later action that it happens-before |
|---|---|
| Unlock monitor M | A subsequent lock of M |
| Write volatile variable V | A subsequent read of V |
| Call `thread.start()` | Actions performed by the started thread |
| Every action in a thread | Another thread successfully returns from `join()` on it |
| Initialization of an object | Use of that object after correct publication |

Within one thread, each action also happens-before later actions according to program order. Combining rules explains the synchronized counter result:

```java
final class Counter {
    private int value;

    synchronized void increment() {
        value++;
    }

    synchronized int get() {
        return value;
    }
}

Counter counter = new Counter();
Runnable addTenThousand = () -> {
    for (int i = 0; i < 10_000; i++) {
        counter.increment();
    }
};

Thread a = new Thread(addTenThousand);
Thread b = new Thread(addTenThousand);
a.start();
b.start();
a.join();
b.join();
System.out.println(counter.get()); // 20000
```

Each increment excludes competing increments, so no update is lost. Returning from `a.join()` and `b.join()` also places both workers' actions before the main thread continues. The final synchronized getter is consistent with the counter's guard, but `join` itself already establishes visibility of completed worker actions.

A **data race** exists when two conflicting accesses to the same variable are not ordered by happens-before and at least one access is a write. Race-free programs using the synchronization rules have sequentially consistent behavior: their executions can be understood as some interleaving that respects each thread's program order. Racy programs do not earn that simple model.

Happens-before is stronger and more precise than elapsed time. A thread may write a field several seconds before another thread reads it, yet the read still lacks a visibility guarantee if no ordering edge connects them. Conversely, a volatile handoff can order ordinary field writes that precede the volatile write. A producer may fill an object, assign it to an ordinary field, and then write `ready = true` to a volatile field. A consumer that reads `ready` as true is then entitled to observe the producer's earlier writes. The volatile variable acts as the publication edge; making every field volatile would add noise without improving that protocol.

The guarantee also runs through transitivity. If A releases a monitor after preparing data, B acquires that monitor and later starts thread C, then A's preparation happens-before C's actions. Reasoning in terms of edges scales better than trying to predict cache flushes or instruction schedules, which are implementation details rather than the language contract.

## Choosing between a monitor, `volatile`, and atomics

`volatile` fits a value that can be read and written independently, with no multi-field invariant and no compound update. A shutdown flag is the standard case:

```java
final class Worker implements Runnable {
    private volatile boolean stopRequested;

    public void requestStop() {
        stopRequested = true;
    }

    @Override
    public void run() {
        while (!stopRequested) {
            doOneUnitOfWork();
        }
    }

    private void doOneUnitOfWork() {
        // bounded work: the loop must regain a chance to inspect the flag
    }
}
```

Without `volatile` or another happens-before edge, the worker is not required to observe the new value. With it, the write to `stopRequested` happens-before the read that observes `true`. Volatile access does not provide mutual exclusion, and `count++` remains a read followed by a calculation followed by a write.

Atomic classes such as `AtomicInteger` provide indivisible operations including `incrementAndGet` and compare-and-set. They are suitable for a counter or reference updated independently. A monitor is usually clearer when one operation must preserve a relationship among several fields, such as `balance`, an overdraft limit, and an audit sequence number.

| Requirement | Typical mechanism |
|---|---|
| One independently assigned flag or reference | `volatile` |
| Atomic update of one number or reference | `AtomicInteger`, `AtomicLong`, or `AtomicReference` |
| Invariant spanning several values | `synchronized` or `Lock` |
| Passing work or data between threads | Blocking queue or executor |
| Waiting for a count or phase | Latch, barrier, or phaser |

Safe publication matters even when an object is intended to be read-only. Publishing through a static initializer, a volatile field, a lock, a concurrent collection, or a thread-safe queue gives other threads a defined view of the initialized state. Final fields have additional initialization guarantees when the constructor does not leak `this`; they do not make referenced mutable objects immutable.

## Waiting for a condition, step by step

Monitors also support condition waiting. `wait()` suspends the current thread and releases the target object's monitor atomically. Before it returns, the thread must reacquire that monitor. `notify()` wakes one arbitrary waiter; `notifyAll()` wakes all waiters. The notifier keeps the lock until it leaves the synchronized region.

Consider a one-slot mailbox. A producer must wait while the slot is full, and a consumer must wait while it is empty:

```java
final class Mailbox<T> {
    private T item;
    private boolean full;

    public synchronized void put(T value) throws InterruptedException {
        while (full) {
            wait();
        }
        item = value;
        full = true;
        notifyAll();
    }

    public synchronized T take() throws InterruptedException {
        while (!full) {
            wait();
        }
        T value = item;
        item = null;
        full = false;
        notifyAll();
        return value;
    }
}
```

For a consumer arriving first, the sequence is:

1. The consumer acquires the mailbox monitor and finds `full == false`.
2. `wait()` releases the monitor and suspends the consumer.
3. The producer acquires the monitor, stores the item, sets `full` to `true`, and calls `notifyAll()`.
4. The producer still owns the monitor until `put` returns.
5. The consumer competes to reacquire the monitor, then evaluates `!full` again.
6. With the predicate now false, it removes the item and restores the empty-state invariant.

```mermaid
sequenceDiagram
  participant Producer
  participant Mailbox
  participant Consumer
  Consumer->>Mailbox: "take() acquires monitor"
  Mailbox-->>Consumer: "empty: wait and release monitor"
  Producer->>Mailbox: "put(item) acquires monitor"
  Producer->>Mailbox: "store item; notifyAll()"
  Note over Producer,Mailbox: Producer releases monitor on return
  Consumer->>Mailbox: "reacquire and retest predicate"
  Mailbox-->>Consumer: "remove and return item"
```

The test must be a `while`, not an `if`. A wakeup is permission to compete for the lock, not evidence that the predicate is true. Another consumer may take the item first, unrelated conditions may share the wait set, and spurious wakeups are permitted. Both the predicate and the state changes that can satisfy it must use the same monitor.

`wait`, `notify`, and `notifyAll` throw `IllegalMonitorStateException` when called without owning the target monitor. Calling `other.wait()` while synchronized on `this` is therefore wrong unless `other` and `this` are the same object.

## Interruption and orderly shutdown

Interruption is a cooperative request, not forced termination. Blocking methods such as `sleep`, `wait`, and `join` respond by throwing `InterruptedException` and clearing the interrupted status. Code that cannot complete the requested operation should normally propagate the exception. Code at a boundary that cannot throw it should restore the status so an outer layer can observe it:

```java
try {
    queue.put(result);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    return;
}
```

For nonblocking loops, `Thread.currentThread().isInterrupted()` checks the status without clearing it. `Thread.interrupted()` checks and clears the current thread's status, a difference that can silently consume a cancellation request.

Deprecated abrupt termination operations are unsafe because a thread can be stopped while it owns locks or while an invariant is temporarily broken. A worker should finish or roll back its current consistency-preserving unit, release resources, and return from `run`.

## Deadlock is a design error, not a slow lock

Two transfers can deadlock if each thread locks its source account and then tries to lock its destination. One holds A and waits for B; the other holds B and waits for A. Neither can proceed.

The usual repair is a global lock order. Assign each account a stable ordering key, acquire the lower one first, then the higher one. Equal keys need a tie-breaking lock or a key guaranteed to be unique. Keeping critical sections bounded and avoiding calls into unknown code while holding a monitor also limits lock dependencies.

Deadlock differs from starvation, where a runnable thread repeatedly loses access to a needed resource, and livelock, where threads keep reacting to each other but make no progress. Adding retries may replace a deadlock with livelock unless backoff or ownership rules ensure progress. Thread dumps are the first useful artifact for a suspected deadlock because they show monitor ownership and waiting relationships.

## Review notes for shared state

- Write down which lock guards each mutable field. All reads count, including `toString`, logging, and diagnostic getters.
- Do not synchronize writers while leaving readers unsynchronized. The reader needs the same happens-before relation.
- Keep check-then-act sequences under one lock, or use a single atomic library operation designed for them.
- Never assume a wakeup means a condition is satisfied. Retest under the lock.
- Avoid holding a lock during blocking I/O or callbacks unless the ownership design specifically requires it.
- Define cancellation and failure handling along with startup. A thread that cannot stop can keep the JVM or a service shutdown hanging.
- Prefer higher-level concurrency utilities once the problem resembles task scheduling, message passing, or phase coordination. Their contracts encode policies that are easy to get subtly wrong with raw monitors.

<div className="see-also">

See also: [Concurrent Utilities and Executors](/cs/programming/java/concurrent-utilities-executors) · [Interfaces, Nested Classes, and Enums](/cs/programming/java/interfaces-nested-classes-enums) · [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation) · [Exceptions and Assertions](/cs/programming/java/exceptions-assertions)

</div>
