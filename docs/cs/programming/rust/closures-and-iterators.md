---
title: Closures and Iterators
sidebar_position: 13
---

# Closures and Iterators

Closures and iterators bring functional-programming style into Rust without abandoning ownership and static dispatch. A closure is an anonymous function-like value that can capture its environment. An iterator is a value that produces a sequence of items through repeated calls to `next`. Together they support expressive data processing pipelines that compile to efficient loops.

This page follows [generics, traits, and lifetimes](/cs/programming/rust/generics-traits-lifetimes) because closures are represented by traits and iterators are built around the `Iterator` trait. It also supports the command-line project style used in the Rust book's `minigrep` chapter, where iterators process arguments, lines, and search results.

## Definitions

A closure is written with vertical bars around parameters:

```rust
let add_one = |x| x + 1;
```

Closures can infer parameter and return types from use. Unlike functions, closures can capture variables from the scope where they are defined.

Closures capture environment in one of three ways: by immutable borrow, by mutable borrow, or by value. These correspond to the closure traits `Fn`, `FnMut`, and `FnOnce`. A closure that moves a captured value out of itself can be called only once.

The `move` keyword forces a closure to take ownership of captured values. This is common when spawning threads because the closure may outlive the current stack frame.

An iterator is any type implementing the `Iterator` trait:

```rust
trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}
```

Calling `next` returns `Some(item)` until the sequence is exhausted, then returns `None`.

Iterator adapters, such as `map`, `filter`, and `take`, transform iterators lazily. Consuming adapters, such as `sum`, `collect`, and `for_each`, drive iteration and produce a final value or side effect.

## Key results

The first key result is that closures capture only what they use. If a closure only reads a value, it can capture by immutable borrow. If it mutates captured state, it needs a mutable borrow. If it consumes captured state, it captures by value.

The second key result is that iterator adapters are lazy. Writing `v.iter().map(|x| x + 1);` does no work unless a consuming adapter or `for` loop pulls values from the iterator.

The third key result is that iterators often replace manual indexing. They reduce bounds errors and make intent clearer: transform, filter, fold, collect.

The fourth key result is that Rust can optimize iterator chains heavily. The book emphasizes that high-level iterator code can compile to code comparable to hand-written loops, because the abstractions are resolved statically in many common cases.

Proof sketch for laziness: `map` returns a new iterator value that stores the original iterator and the closure. It does not call the closure immediately. The closure is called only when `next` is called on the mapped iterator, or when a consumer such as `collect` repeatedly calls `next`.

## Visual

```mermaid
flowchart LR
  A[Vector] --> B[iter]
  B --> C[filter closure]
  C --> D[map closure]
  D --> E[collect or sum]
  E --> F[Final collection or value]
```

| Adapter kind | Examples | Runs immediately? | Output |
|---|---|---:|---|
| Source | `iter`, `into_iter`, `iter_mut` | no | iterator |
| Transforming adapter | `map`, `filter`, `take`, `skip` | no | iterator |
| Combining adapter | `zip`, `chain` | no | iterator |
| Consuming adapter | `sum`, `collect`, `count`, `for_each` | yes | final value or effect |
| Manual pull | `next` | one item at a time | `Option<Item>` |

## Worked example 1: closure capture modes

Problem: determine how three closures capture surrounding variables.

1. Immutable read:

```rust
let list = vec![1, 2, 3];
let only_reads = || println!("{list:?}");
only_reads();
println!("{list:?}");
```

The closure only prints `list`, so it captures by immutable borrow. The original `list` remains usable for reading after the closure call.

2. Mutable update:

```rust
let mut list = vec![1, 2, 3];
let mut adds = || list.push(4);
adds();
```

The closure mutates `list`, so the closure itself must be mutable and holds a mutable borrow while it exists. You cannot read `list` between defining `adds` and the last use of `adds` if that would overlap the mutable borrow.

3. Forced move:

```rust
let list = vec![1, 2, 3];
let owns_list = move || println!("{list:?}");
owns_list();
```

The `move` keyword transfers ownership of `list` into the closure. The outer binding cannot be used afterward.

4. Check the answer. The capture mode is determined by closure body needs, except `move` forces ownership capture. These rules are the same ownership rules applied to anonymous function values.

## Worked example 2: computing filtered squares with iterators

Problem: from `[1, 2, 3, 4, 5, 6]`, keep even numbers, square them, and sum the squares.

1. Start with a vector:

```rust
let numbers = vec![1, 2, 3, 4, 5, 6];
```

2. Borrow each element:

```rust
numbers.iter()
```

This produces `&i32` items.

3. Filter evens:

```rust
.filter(|n| *n % 2 == 0)
```

Because the closure receives references, `*n` gets the integer value for arithmetic.

4. Square:

```rust
.map(|n| n * n)
```

After filtering, `n` is still a reference in this context, but multiplication works through deref coercions for references to integers in this expression. Writing `(*n) * (*n)` would be more explicit.

5. Sum:

```rust
.sum::<i32>()
```

6. Check manually. The even numbers are `2`, `4`, and `6`. Their squares are `4`, `16`, and `36`. The sum is `56`.

The key is that `filter` and `map` define a pipeline, while `sum` actually consumes it.

## Code

```rust
#[derive(Debug, PartialEq)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes
        .into_iter()
        .filter(|shoe| shoe.size == shoe_size)
        .collect()
}

fn main() {
    let inventory = vec![
        Shoe {
            size: 10,
            style: String::from("sneaker"),
        },
        Shoe {
            size: 13,
            style: String::from("sandal"),
        },
        Shoe {
            size: 10,
            style: String::from("boot"),
        },
    ];

    let my_size = shoes_in_size(inventory, 10);
    println!("{my_size:?}");
}
```

This example consumes the input vector with `into_iter`, keeps matching shoes, and collects the owned shoes into a new vector. The original `inventory` is moved because the result owns selected shoes.

## Common pitfalls

- Creating an iterator adapter chain and forgetting a consuming adapter, resulting in no work.
- Confusing `iter`, `iter_mut`, and `into_iter`. They yield shared references, mutable references, and owned values respectively.
- Expecting a closure to have independent type annotations for multiple uses. A closure's inferred types are fixed after first use.
- Forgetting `mut` on a closure binding that mutates captured state.
- Adding `move` and then trying to use the moved variable outside the closure.
- Using manual indexing when iterator methods would avoid bounds logic.
- Calling `collect` without enough type context. Add an annotation such as `let v: Vec<_> = ...collect();`.

## Connections

- [Generics, traits, and lifetimes](/cs/programming/rust/generics-traits-lifetimes)
- [Common collections](/cs/programming/rust/common-collections)
- [Error handling](/cs/programming/rust/error-handling)
- [Cargo and crates.io workflow](/cs/programming/rust/cargo-crates-io-workflow)
- [Concurrency and shared state](/cs/programming/rust/concurrency-and-shared-state)
