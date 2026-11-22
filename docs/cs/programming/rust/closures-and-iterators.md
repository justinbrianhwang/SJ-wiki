---
title: Closures and Iterators
sidebar_position: 13
---

# Closures and Iterators

Closures and iterators let Rust describe computation as values connected by traits. A closure is an anonymous callable value that may capture bindings from its environment. An iterator is a state machine that yields one item when asked. Connecting them produces lazy pipelines without giving up ownership checking or static dispatch.

The compact syntax can hide several types at once: the closure's capture mode, its callable trait, the iterator's `Item`, and the eventual collection or scalar. Writing those types down usually resolves an opaque compiler message faster than rearranging closure punctuation.

## A closure is a value with captured state

Closure parameters appear between vertical bars; parameter and return types are often inferred from use:

```rust
let add_one = |x: i32| x + 1;
assert_eq!(add_one(4), 5);
```

Each closure expression has a unique anonymous type. Unlike a function item, that type may contain fields corresponding to captured values or references. The compiler chooses the least demanding capture for each binding according to what the body does.

Reading an outer value captures a shared borrow:

```rust
let names = vec![String::from("Ada"), String::from("Grace")];
let print_count = || println!("{}", names.len());

print_count();
println!("{names:?}");
```

Mutating a captured value requires a mutable borrow and a mutable closure binding because calling the closure changes its stored state:

```rust
let mut values = vec![1, 2];
let mut append = |value| values.push(value);

append(3);
append(4);
drop(append);
assert_eq!(values, vec![1, 2, 3, 4]);
```

The explicit `drop` ends the closure's mutable borrow before `values` is inspected. Non-lexical lifetimes often end the borrow after the closure's last use without that line, but spelling it out clarifies the ownership transition.

Moving a captured non-`Copy` value out of the closure consumes that stored value:

```rust
let message = String::from("done");
let take_message = || message;

let owned = take_message();
assert_eq!(owned, "done");
// take_message cannot be called again
```

The closure can run only once because a second call would need to move a `String` that is no longer present.

## `move` changes capture, not necessarily call count

The `move` keyword asks the closure to capture outer bindings by value rather than borrow them:

```rust
let names = vec![String::from("Ada"), String::from("Grace")];
let owns_names = move || names.len();

assert_eq!(owns_names(), 2);
assert_eq!(owns_names(), 2);
```

Although `owns_names` owns the vector, its body only borrows the vector to call `len`, so it remains callable repeatedly. `move` does not automatically make a closure `FnOnce`. Call behavior depends on what the body does with captured state.

For a `Copy` capture, “move” copies the value into the closure. The outer value remains usable:

```rust
let threshold = 10;
let above = move |value| value > threshold;

assert!(above(12));
println!("{threshold}");
```

Move closures are common at ownership boundaries. `std::thread::spawn` requires a closure that is `Send` and `'static` because the new thread may outlive the stack frame that starts it. Owning captured data is one way to satisfy the lifetime requirement; references with a sufficiently long lifetime or scoped-thread APIs are other possibilities.

## The callable trait hierarchy

Closure traits describe how the closure value must be borrowed to call it:

| Trait | Receiver model | What the body may do with captures |
|---|---|---|
| `Fn` | shared borrow | Read without mutation or consumption |
| `FnMut` | mutable borrow | Mutate captured state |
| `FnOnce` | ownership | Consume captured state |

The traits form a capability hierarchy. A closure that implements `Fn` can also be used where `FnMut` or `FnOnce` is accepted. A closure implementing only `FnOnce` cannot satisfy a caller that promises to invoke it repeatedly.

Function parameters should request the weakest capability the implementation needs. A helper that invokes a callback once can accept more closures with `FnOnce`:

```rust
fn apply_once<F, T, U>(value: T, operation: F) -> U
where
    F: FnOnce(T) -> U,
{
    operation(value)
}
```

A retry loop needs at least `FnMut` because it may call the closure several times and allow state changes:

```rust
fn call_twice<F>(mut operation: F)
where
    F: FnMut(),
{
    operation();
    operation();
}
```

One closure's inferred parameter and return types are fixed. Calling `let identity = |x| x;` first with a `String` constrains that closure to `String`; it cannot later accept an integer. A generic free function or a generic type implementing a callable-like trait is needed for genuinely polymorphic behavior.

Closures with no captures can coerce to ordinary function pointers such as `fn(i32) -> i32`. Capturing closures cannot, because a function pointer has nowhere to store the environment.

## Iterators are pull-based state machines

The essential `Iterator` trait has an associated item type and a `next` method:

```rust
trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // many provided methods
}
```

`&mut self` reveals that iteration advances internal state. `Some(item)` supplies the next item; `None` reports that no item is currently available. Most standard iterators continue returning `None` after exhaustion. The base trait does not require that behavior for every custom iterator; `FusedIterator` marks iterators that guarantee permanent exhaustion.

Iterator adapters such as `map`, `filter`, `take`, and `zip` are lazy. They construct new iterator values containing the previous iterator and any closure, but they do not pull items. Consumers such as `sum`, `collect`, `count`, `fold`, and `for_each` repeatedly call `next` and drive the chain.

```rust
let mapped = (1..=3).map(|n| {
    println!("mapping {n}");
    n * 2
});

println!("created"); // no mapping output yet
let values: Vec<_> = mapped.collect();
assert_eq!(values, vec![2, 4, 6]);
```

The output first contains `created`, then one mapping line for each pull during `collect`. A bare expression such as `values.iter().map(|x| x + 1);` performs no transformation if the adapter is never consumed. The compiler may warn because iterator adapters are marked as values that must be used.

## `for` loops begin with `IntoIterator`

A `for` loop accepts anything implementing `IntoIterator`, calls `into_iter`, and repeatedly matches on `next`. Conceptually,

```rust
for value in collection {
    use_value(value);
}
```

corresponds to a loop over an iterator until `None`. The chosen receiver determines item ownership:

| Expression | Typical item for `Vec<T>` | Effect on vector |
|---|---|---|
| `values.iter()` or `&values` | `&T` | Shared borrow |
| `values.iter_mut()` or `&mut values` | `&mut T` | Mutable borrow |
| `values.into_iter()` or `values` | `T` | Consumes vector |

These are not interchangeable stylistic variants. An iterator of `&T` can return views tied to the collection's lifetime. An iterator of `T` owns each item and can move it elsewhere. An iterator of `&mut T` allows in-place updates but exclusively borrows the collection for the iterator's lifetime.

```rust
let mut values = vec![1, 2, 3];
for value in &mut values {
    *value *= 10;
}
assert_eq!(values, vec![10, 20, 30]);
```

The dereference updates the integer behind each mutable reference. The loop cannot structurally modify the vector with `push` while those element borrows are active.

## Worked pipeline: filter borrowed values, then reduce

Take the even numbers from 1 through 6, square them, and add the squares:

```rust
let numbers = vec![1, 2, 3, 4, 5, 6];

let total = numbers
    .iter()
    .filter(|&&n| n % 2 == 0)
    .map(|&n| n * n)
    .sum::<i32>();

assert_eq!(total, 56);
assert_eq!(numbers.len(), 6);
```

Track the item type through each stage:

1. `numbers.iter()` has `Item = &i32` and borrows the vector.
2. `filter` tests a borrowed view of each iterator item, so its predicate receives `&&i32`. The pattern `|&&n|` obtains a copied `i32`.
3. The retained values are references to 2, 4, and 6.
4. `map` receives each `&i32`; `|&n| n * n` copies and squares it, changing the item type to `i32`.
5. The mapped items are 4, 16, and 36.
6. `sum::<i32>()` consumes the iterator and computes $4+16+36=56$.

The original vector remains available because traversal borrowed it. For `Copy` numbers, `.copied()` can make the conversion explicit:

```rust
let total: i32 = numbers
    .iter()
    .copied()
    .filter(|n| n % 2 == 0)
    .map(|n| n * n)
    .sum();
```

Now `filter` still borrows each item for its predicate, but the iterator item itself is `i32`, making the patterns easier to read.

## Worked fallible pipeline: collect results, not partial success

Suppose each input string should be a signed integer. Mapping `str::parse` produces an iterator of `Result<i32, ParseIntError>`:

```rust
fn parse_all(inputs: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError> {
    inputs.iter().map(|text| text.parse::<i32>()).collect()
}
```

`collect` is selected as `Result<Vec<i32>, _>` by the function's return type. Its behavior is:

1. Pull the first parse result.
2. If it is `Ok(value)`, place the value into the developing vector and continue.
3. On the first `Err(error)`, stop pulling and return that error.
4. If every item is `Ok`, return `Ok` containing the complete vector.

```rust
assert_eq!(parse_all(&["10", "-2", "7"]).unwrap(), vec![10, -2, 7]);

let error = parse_all(&["10", "no", "7"]);
assert!(error.is_err());
```

The second call never produces a successful partial vector containing 10. The return type promises all-or-error semantics. If partial success and a list of rejected values are required, that policy needs an explicit fold or partition rather than ordinary `collect`.

`filter_map` expresses a different choice by dropping failures or absent results and retaining successes. Using it with `.ok()` is concise, but it silently discards parse errors:

```rust
let parsed: Vec<i32> = ["10", "no", "7"]
    .into_iter()
    .filter_map(|text| text.parse().ok())
    .collect();
```

That behavior is suitable only when rejection is expected and accounted for elsewhere.

## Building a small iterator from `next`

Implementing `next` is enough to receive the trait's adapters and consumers. This counter yields 1, 2, and 3:

```rust
struct Counter {
    next: u32,
    end: u32,
}

impl Counter {
    fn new(end: u32) -> Self {
        Self { next: 1, end }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.next <= self.end {
            let current = self.next;
            self.next += 1;
            Some(current)
        } else {
            None
        }
    }
}

assert_eq!(Counter::new(3).collect::<Vec<_>>(), vec![1, 2, 3]);
```

The initial state stores `next = 1`. Each successful call copies the current value, advances state, and returns `Some`. After yielding 3, state becomes 4; the following call fails the bound and returns `None`. Methods such as `map`, `zip`, and `sum` are available through the trait's provided implementations.

For a richer iterator, `size_hint` can report lower and optional upper bounds, allowing `collect` to reserve capacity. `DoubleEndedIterator` supports pulling from both ends, and `ExactSizeIterator` promises an exact remaining length. Implement those traits only when the state machine can uphold their contracts.

## Returning a pipeline keeps its borrow alive

A function can return an unnamed adapter type with `impl Iterator`. If the iterator yields references into an argument, the returned value carries that borrow:

```rust
fn nonempty_lines(text: &str) -> impl Iterator<Item = &str> {
    text.lines().filter(|line| !line.trim().is_empty())
}
```

The elided lifetime ties output slices to `text`. Callers may consume the iterator only while the input string remains alive. No vector of lines is allocated; each call to `next` searches far enough to produce one nonempty borrowed line.

When the adapter closure must capture an additional borrowed parameter, the relationship may need an explicit lifetime and `move`:

```rust
fn containing<'a>(
    text: &'a str,
    needle: &'a str,
) -> impl Iterator<Item = &'a str> + 'a {
    text.lines().filter(move |line| line.contains(needle))
}
```

`move` stores the `&str` reference `needle` inside the closure by value. It does not copy the underlying text and does not make the result `'static`; the returned iterator still cannot outlive lifetime `'a`.

Returning `impl Iterator` hides the long concrete adapter type while preserving static dispatch. It also commits the function to one concrete hidden type. If branches would build different iterator types, options include moving the condition inside one adapter, returning a boxed trait object with an explicit lifetime, or collecting eagerly. Boxing permits run-time dispatch and a uniform type but adds allocation and indirection.

The return type is an API choice. `Vec<T>` performs all work before return, owns its results, supports repeated traversal, and can report length directly. `impl Iterator<Item = T>` defers work, can short-circuit, and is normally single-pass. Neither is universally superior; callers need to know whether errors, I/O, or expensive calculation occur during function call or later during iteration.

## Selecting the adapter that states the policy

| Need | Adapter or consumer |
|---|---|
| Transform every item | `map` |
| Retain items satisfying a predicate | `filter` |
| Transform and possibly omit | `filter_map` |
| Map one item to many, then flatten | `flat_map` |
| Pair two sequences until either ends | `zip` |
| Append one sequence after another | `chain` |
| Keep a prefix | `take`, `take_while` |
| Maintain an accumulator and produce one result | `fold` |
| Stop a fold on an error or other residual | `try_fold` |
| Find one item without collecting | `find`, `position` |

Prefer a direct consumer when only one result is needed. `iter.filter(...).count()` need not allocate a vector; `iter.any(...)` can stop at the first true predicate; `find` can return at the first match. Laziness permits such short-circuiting.

`fold` makes ownership of an accumulator explicit. To concatenate words with a separator:

```rust
let sentence = ["ownership", "guides", "design"]
    .into_iter()
    .fold(String::new(), |mut output, word| {
        if !output.is_empty() {
            output.push(' ');
        }
        output.push_str(word);
        output
    });
```

The initial accumulator is an empty owned `String`. Each call receives ownership of the current string, mutates it, and returns it for the next item. After three items the result is `"ownership guides design"`. Because the same allocation can be returned between steps, the fold need not allocate a new string for every word, although growth may still reallocate when capacity is exhausted.

A loop with `push_str` may communicate this particular construction more directly. `fold` is strongest when the accumulator and transition form a compact expression or when it is one stage in a larger iterator operation. `reduce` differs by using the first item as the initial accumulator and therefore returns `Option` for an empty iterator.

Fallible accumulation calls for `try_fold`. It short-circuits on the first residual such as `Err` while allowing the accumulator to stay in its native type. That avoids building a partial collection only to discover an error later.

Iterator chains often optimize to loops with no intermediate collections, but allocation and performance still depend on the adapters, closure bodies, optimizer, and target. Readability and ownership should choose the first implementation; profiles and benchmarks settle a performance question.

`inspect` is useful for temporary observation without changing items:

```rust
let total: i32 = (1..=3)
    .inspect(|value| eprintln!("before square: {value}"))
    .map(|value| value * value)
    .sum();
```

Because it is lazy, the diagnostic runs only when `sum` pulls an item. Leaving `inspect` in a library can couple behavior to a consumer's traversal pattern, so structured logging at a clearer boundary is preferable for lasting diagnostics.

## When a loop communicates more clearly

A pipeline works well when each stage has one recognizable role and item types flow cleanly. A `for` loop is often clearer for several mutable accumulators, complex branching, early exits with cleanup, or side effects that would be hidden inside `map`.

Naming intermediate iterators can split a long type error and document a phase without allocating:

```rust
let valid = records.iter().filter(|record| record.is_valid());
let ids = valid.map(|record| record.id);
let unique_ids = ids.collect::<std::collections::HashSet<_>>();
```

If `collect` cannot infer its destination, supply the variable type or a turbofish such as `collect::<Vec<_>>()`. If a closure unexpectedly moves a value, inspect what its body returns or consumes before adding clones. If a chain appears to do nothing, find the consumer that drives it.

<div className="see-also">

See also: [Generics, Traits, and Lifetimes](/cs/programming/rust/generics-traits-lifetimes) · [Common Collections](/cs/programming/rust/common-collections) · [Error Handling](/cs/programming/rust/error-handling) · [Concurrency and Shared State](/cs/programming/rust/concurrency-and-shared-state)

</div>
