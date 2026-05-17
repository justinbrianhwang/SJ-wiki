---
title: Common Collections
sidebar_position: 9
---

# Common Collections

Collections store multiple values on the heap. The book focuses on three standard library collections because they appear constantly in real Rust programs: `Vec<T>`, `String`, and `HashMap<K, V>`. A vector is a growable sequence. A string is a growable UTF-8 text buffer. A hash map associates keys with values. Each collection interacts with ownership, borrowing, and error handling in visible ways.

![The Rust logo marks pages on ownership, borrowing, traits, and safe systems programming.](https://commons.wikimedia.org/wiki/Special:FilePath/Rust_programming_language_black_logo.svg)

*Figure: Rust connects systems control with compile-time memory-safety guarantees. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Rust_programming_language_black_logo.svg), Rust Foundation, CC BY 4.0.*

This page follows [ownership](/cs/programming/rust/ownership-references-slices) because collections own their contents and may reallocate as they grow. It also prepares for [iterators](/cs/programming/rust/closures-and-iterators), because collections are often processed through iterator adapters rather than manual indexing.

## Definitions

`Vec<T>` is a growable array stored on the heap. All elements have the same type `T`. A vector keeps its elements contiguous, so indexing is fast, but inserting in the middle may require shifting later elements.

`String` is a growable UTF-8 encoded text type. It owns its bytes. A string slice `&str` is a borrowed view into UTF-8 data. Rust strings are not indexed by character position because Unicode scalar values and grapheme clusters do not correspond to one byte each.

`HashMap<K, V>` stores key-value pairs using a hashing function. Keys must implement `Eq` and `Hash`. The standard `HashMap` is not automatically in the prelude, so it is normally imported with `use std::collections::HashMap;`.

Indexing a vector with `v[i]` returns a reference and panics if `i` is out of bounds. Calling `v.get(i)` returns `Option<&T>`, which makes absence explicit.

Pushing into a vector may reallocate its buffer. If references to elements were allowed to survive a reallocation, they could point to old memory. The borrow checker prevents that by forbidding mutation while element references are still used.

The `entry` API for hash maps supports update-or-insert logic. `or_insert` returns a mutable reference to the value for a key, inserting a default if the key is missing.

## Key results

The first key result is that vector element borrows restrict mutation. If `let first = &v[0];` is later used, `v.push(...)` cannot happen before the last use of `first`, because `push` could move the vector's buffer.

The second key result is that strings require UTF-8 awareness. `String::len()` returns bytes, not human-perceived characters. Slicing strings by range is allowed only at valid UTF-8 boundaries. Iteration can be by bytes with `bytes()` or by Unicode scalar values with `chars()`.

The third key result is that collections take ownership of inserted owned values. Inserting `String` keys or values into a `HashMap` moves them unless they are cloned or borrowed data is used with appropriate lifetimes.

The fourth key result is that `get`, `match`, and `Option` are preferred when absence is normal. Panicking index access is acceptable only when out-of-bounds access represents a programmer bug rather than expected control flow.

Proof sketch for vector reallocation safety: a vector's elements are contiguous. If capacity is full and `push` needs more space, the vector may allocate a new buffer and copy or move elements there. Any old element reference would then point at invalid memory. Rust rejects simultaneous element reference use and mutation that could reallocate, so the invalid pointer cannot be created in safe Rust.

Another result is that collection APIs reveal whether they consume, borrow, or mutate. `into_iter` on a vector consumes the vector and yields owned elements. `iter` borrows the vector and yields shared references. `iter_mut` mutably borrows the vector and yields mutable references. The same names appear throughout Rust because they encode ownership policy directly in the method call. Choosing among them is not just a performance choice. It decides whether the original collection remains usable, whether elements can be changed, and whether output values borrow from the input.

For strings, the comparable lesson is that text APIs force a choice of interpretation. `bytes()` sees raw UTF-8 bytes. `chars()` sees Unicode scalar values. Methods such as `split_whitespace` or `lines` produce string slices that respect textual boundaries. This is why many Rust string programs avoid indexing entirely. They ask the library for the kind of textual unit they actually mean.

Hash maps add one more ownership lesson. Inserting a key-value pair moves owned keys and values into the map, because the map must keep them alive independently of the caller's stack frame. If the caller needs to keep using the same owned strings, it can clone them, store references with suitable lifetimes, or restructure the program so the map becomes the owner. Each choice says something different about who is responsible for the data.

Capacity is the performance side of the same model. `Vec`, `String`, and `HashMap` can reserve space ahead of time when the program has a good size estimate. Reserving is not required for correctness, but it can reduce reallocations and rehashing in tight loops.

The best collection choice starts with access pattern, not habit. Ask whether the program needs order, key lookup, text mutation, borrowed views, or ownership transfer, then choose the type that states that need.

The type should make the common operation obvious.

That choice is part of the design.

It shapes later APIs.

## Visual

```text
Vec<i32>
stack fields                  heap buffer
+------+-----+----------+     +----+----+----+----+
| ptr  | len | capacity | --> | 10 | 20 | 30 | ?? |
+------+-----+----------+     +----+----+----+----+
                                  elements     spare capacity
```

| Collection | Best for | Access pattern | Common ownership note |
|---|---|---|---|
| `Vec<T>` | Ordered growable list | index, iterate, push, pop | owns elements contiguously |
| `String` | Owned mutable UTF-8 text | append, slice, iterate chars | byte length differs from character count |
| `HashMap<K, V>` | Lookup by key | `insert`, `get`, `entry` | owned keys and values move in |
| `&[T]` | Borrowed sequence view | iterate, read by index | no ownership of elements |
| `&str` | Borrowed text view | read, split, search | must remain valid UTF-8 |

## Worked example 1: safe vector access and mutation

Problem: read the first score from a vector, then add another score without creating an invalid reference.

1. Create the vector:

```rust
let mut scores = vec![80, 90, 75];
```

The vector owns three `i32` values.

2. Use safe access:

```rust
let first = scores.get(0);
```

The type is `Option<&i32>`. For this vector, the value is `Some(&80)`.

3. Consume the option before mutation:

```rust
match first {
    Some(score) => println!("first score: {score}"),
    None => println!("no scores yet"),
}
```

After the last use of `first`, the immutable borrow ends.

4. Mutate the vector:

```rust
scores.push(88);
```

This is allowed because no active element reference is used afterward.

5. Check the answer. The final vector is `[80, 90, 75, 88]`. No reference into the old buffer survives the push.

If the code tried to push before printing `first`, Rust could reject it because `push` requires mutable access to the vector while an immutable borrow of an element is still live.

## Worked example 2: counting words with `HashMap`

Problem: count how often each word occurs in `"hello world wonderful world"`.

1. Import the collection:

```rust
use std::collections::HashMap;
```

2. Create an empty map:

```rust
let mut counts = HashMap::new();
```

Rust can infer the key and value types from later insertion.

3. Iterate through words:

```rust
for word in text.split_whitespace() {
    let count = counts.entry(word).or_insert(0);
    *count += 1;
}
```

Here `word` has type `&str`, borrowed from `text`. The map stores keys that are valid as long as `text` is valid. For a longer-lived map, owned `String` keys would be safer.

4. Trace the updates:

| Word | Previous map state | Operation | New count |
|---|---|---|---:|
| `hello` | missing | insert `0`, add `1` | 1 |
| `world` | missing | insert `0`, add `1` | 1 |
| `wonderful` | missing | insert `0`, add `1` | 1 |
| `world` | present | add `1` | 2 |

5. Check the answer. The map contains `hello -> 1`, `world -> 2`, and `wonderful -> 1`.

## Code

```rust
use std::collections::HashMap;

fn word_counts(text: &str) -> HashMap<&str, usize> {
    let mut counts = HashMap::new();

    for word in text.split_whitespace() {
        let count = counts.entry(word).or_insert(0);
        *count += 1;
    }

    counts
}

fn main() {
    let text = "rust makes systems programming safer and rust tools help";
    let counts = word_counts(text);

    for (word, count) in &counts {
        println!("{word}: {count}");
    }

    let letters: Vec<char> = String::from("Rust").chars().collect();
    println!("letters: {letters:?}");
}
```

The map borrows words from `text`, so it cannot outlive that input. The final lines demonstrate string character iteration, which is different from byte indexing.

## Common pitfalls

- Indexing with `v[i]` when missing elements are expected. Prefer `get`.
- Holding a reference to a vector element and then pushing into the vector before the reference is no longer used.
- Assuming `String::len()` counts characters. It counts bytes.
- Slicing a string at arbitrary numeric positions without checking UTF-8 boundaries.
- Moving a `String` into a `HashMap` and then trying to use the original binding.
- Forgetting to import `HashMap`.
- Using a hash map when order matters. Standard `HashMap` iteration order is not a stable sorted order.

## Connections

- [Ownership, references, and slices](/cs/programming/rust/ownership-references-slices)
- [Pattern matching](/cs/programming/rust/pattern-matching)
- [Error handling](/cs/programming/rust/error-handling)
- [Closures and iterators](/cs/programming/rust/closures-and-iterators)
- [Smart pointers](/cs/programming/rust/smart-pointers)
