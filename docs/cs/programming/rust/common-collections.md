---
title: Common Collections
sidebar_position: 9
---

# Common Collections

Rust collections combine a storage strategy with an ownership contract. `Vec<T>` owns a contiguous growable sequence, `String` owns UTF-8 text, and `HashMap<K, V>` owns key-value associations. Their method signatures expose when an operation may reallocate, when a lookup can fail, and whether inserted data is moved or merely borrowed.

Choosing a collection begins with the operations the program needs. “Several values” is not enough: order, lookup key, insertion location, text interpretation, and iteration guarantees all affect the choice.

## Choosing by access pattern

| Type | Useful when | Ordering | Typical operation cost |
|---|---|---|---|
| `Vec<T>` | Indexed sequence, append-heavy buffer | Insertion order | Index and append amortized $O(1)$; middle insert/remove $O(n)$ |
| `VecDeque<T>` | Queue or deque | Logical sequence order | Push/pop at either end amortized $O(1)$ |
| `HashMap<K, V>` | Lookup by unique key | Unspecified | Expected $O(1)$ lookup and insertion |
| `BTreeMap<K, V>` | Sorted keys or range queries | Key order | $O(\log n)$ lookup and insertion |
| `HashSet<T>` | Membership and uniqueness | Unspecified | Expected $O(1)$ membership |
| `BTreeSet<T>` | Sorted unique values | Value order | $O(\log n)$ membership |
| `BinaryHeap<T>` | Repeated access to highest-priority item | Heap order only | Peek $O(1)$; push/pop $O(\log n)$ |

The standard `BinaryHeap` is a max-heap. `LinkedList` exists, but `Vec` or `VecDeque` is often faster and simpler because contiguous or chunk-friendly storage uses caches better and carries less per-element allocation overhead. A linked list earns its cost only when its specific cursor and splice behavior matches the algorithm.

Borrowed views avoid transferring ownership. `&[T]` is a slice of a contiguous sequence, and `&str` is a borrowed region of valid UTF-8. Functions that only read should usually accept these views rather than `&Vec<T>` or `&String`; callers can then pass vectors, arrays, strings, or compatible subranges.

## A vector is a pointer, length, and capacity

A `Vec<T>` value tracks a heap allocation through three conceptual fields:

```text
stack value                         heap allocation
+---------+--------+----------+     +----+----+----+----+
| pointer | length | capacity | --> | 10 | 20 | 30 | ?? |
+---------+--------+----------+     +----+----+----+----+
                                        initialized  spare
```

Length is the number of initialized elements. Capacity is the number of elements the current allocation can hold before growing. `Vec::new()` starts empty; `Vec::with_capacity(n)` reserves space when a reliable estimate is known.

`push` writes into spare capacity when available. When length equals capacity, it may allocate a larger buffer and move all elements. The growth policy is an implementation detail, so code should depend only on the promise that repeated appends have amortized constant cost.

The possibility of relocation explains a common borrow-checker error:

```rust
let mut scores = vec![80, 90, 75];
let first = &scores[0];

// scores.push(88); // rejected if `first` is used later
println!("first score: {first}");

scores.push(88); // borrow ended after its last use
```

Trace the rejected ordering:

1. `&scores[0]` creates a reference into the vector's current allocation.
2. `push` needs mutable access to the vector and might replace that allocation.
3. If relocation occurred, `first` would point to freed storage.
4. Safe Rust rejects the overlap instead of trying to inspect run-time capacity.

Calling `reserve` first does not generally grant permission to keep an element reference across later mutable vector operations. The borrowing rule is expressed by method signatures and remains valid even if the current capacity happens to be sufficient.

## Indexing, removal, and slices

Direct indexing returns a place and panics if the index is out of bounds. `get` returns `Option<&T>`, which makes absence explicit:

```rust
let values = vec![10, 20, 30];

assert_eq!(values[1], 20);
assert_eq!(values.get(1), Some(&20));
assert_eq!(values.get(9), None);
```

Index when an invalid position is a programmer bug backed by a nearby invariant. Use `get` for input-derived positions or ordinary absence. Range indexing produces a slice but can panic for invalid bounds; `get(range)` returns an option instead.

`pop` removes from the end in constant time and returns `Option<T>`. `remove(i)` preserves order by shifting all later elements left. `swap_remove(i)` replaces the removed slot with the final element and avoids that shift, but changes order. `retain` visits the vector and keeps only elements satisfying a predicate, while `truncate` discards a suffix.

```rust
let mut jobs = vec!["a", "b", "c", "d"];
let removed = jobs.swap_remove(1);

assert_eq!(removed, "b");
assert_eq!(jobs, vec!["a", "d", "c"]);
```

The last element `"d"` moves into index one. That is a good trade when order has no meaning; it is a bug when indices or presentation order are part of the model.

A slice borrows a contiguous range:

```rust
fn average(values: &[f64]) -> Option<f64> {
    if values.is_empty() {
        None
    } else {
        Some(values.iter().sum::<f64>() / values.len() as f64)
    }
}

let readings = vec![2.0, 4.0, 8.0, 16.0];
assert_eq!(average(&readings[1..3]), Some(6.0));
```

The selected slice contains 4 and 8, whose sum 12 divided by length 2 is 6. No elements are copied, and the slice cannot outlive `readings`.

## `String` is a UTF-8 byte buffer

`String` is implemented over a byte vector while maintaining the invariant that its contents are valid UTF-8. `&str` borrows such text. `String::len()` returns bytes, not Unicode scalar values and not user-perceived grapheme clusters.

```rust
let text = String::from("é");

assert_eq!(text.len(), 2);           // UTF-8 bytes
assert_eq!(text.chars().count(), 1); // Unicode scalar values
assert_eq!(text.bytes().count(), 2);
```

Rust therefore does not implement `text[0]`. A numeric index would be ambiguous and could select the middle of a multi-byte encoding. Instead, choose the needed unit:

- `bytes()` iterates encoded bytes.
- `chars()` decodes Unicode scalar values.
- `char_indices()` yields each scalar value with its byte offset.
- `split_whitespace`, `lines`, and `split` produce borrowed textual regions.

Even `chars()` does not count displayed characters in the typographic sense. A grapheme cluster may contain a base character plus combining marks or several scalar values joined into one displayed symbol. Grapheme segmentation requires rules beyond the standard library's scalar-value iterator.

String range slicing uses byte offsets and panics when an endpoint is not a UTF-8 boundary:

```rust
let text = "Здравствуйте";
let first = text.get(0..2);
assert_eq!(first, Some("З"));
```

The first Cyrillic scalar occupies bytes 0 and 1, so the exclusive endpoint 2 is valid. `text.get(0..1)` returns `None`; direct `&text[0..1]` would panic. Byte slicing is reasonable when offsets came from `char_indices`, a parser, or another API that guarantees boundaries.

## Growing and combining strings

`push` appends one `char`, while `push_str` appends a borrowed string slice:

```rust
let mut message = String::with_capacity(32);
message.push_str("status");
message.push(':');
message.push(' ');
message.push_str("ready");

assert_eq!(message, "status: ready");
```

Repeated `push_str` is a clear way to build text incrementally. `format!` is convenient when several values and formatting rules are involved and returns a new `String`.

The `+` operator has an ownership wrinkle:

```rust
let left = String::from("hello, ");
let right = String::from("world");
let combined = left + &right;

assert_eq!(combined, "hello, world");
assert_eq!(right, "world");
// `left` was moved
```

Addition takes ownership of the left `String`, borrows the right `str`, and may reuse the left allocation. `format!("{left}{right}")` is often clearer when neither input should be consumed, though the original bindings must of course still exist at that call.

## Hash-map ownership and lookup

`HashMap<K, V>` lives in `std::collections` rather than the prelude. Keys must implement `Eq` and `Hash`; values have no such requirement.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("blue"), 10);
scores.insert(String::from("yellow"), 50);
```

Owned keys and values move into the map unless they implement `Copy`. Inserting a new value for an equal key returns the old value and leaves one entry. `get` borrows the stored value:

```rust
assert_eq!(scores.get("blue"), Some(&10));
assert_eq!(scores.get("red"), None);
```

Although the map stores `String` keys, lookup accepts `&str` because the key type supports compatible borrowed lookup. No temporary `String` allocation is required.

Iteration order is unspecified and can differ across runs or map instances. Tests should compare map contents directly, sort a collected representation, or use `BTreeMap` when sorted traversal belongs to the requirement. Never select “the first” hash-map entry as if it were stable.

Holding a reference returned by `get` blocks mutable operations that might change the map while that reference remains live. The same reasoning as vector reallocation applies: insertion may rehash and move buckets, and removal can destroy the referred value.

## Worked map update: word frequencies

The entry API performs lookup and insert-or-update through one handle:

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
```

For `"hello world wonderful world"`, the state changes are:

1. `hello` is vacant. `or_insert(0)` inserts zero and returns `&mut 0`; incrementing produces 1.
2. `world` is vacant and follows the same path, producing 1.
3. `wonderful` is vacant and produces 1.
4. The second `world` is occupied. `or_insert` returns a mutable reference to the existing 1; incrementing produces 2.

The final map associates `hello` with 1, `wonderful` with 1, and `world` with 2. The key type is `&str`, so keys borrow regions of the input and the map cannot outlive `text`. That saves allocation when the map is a short-lived analysis of one input.

An independent result should own its keys:

```rust
fn owned_word_counts(text: &str) -> HashMap<String, usize> {
    let mut counts = HashMap::new();

    for word in text.split_whitespace() {
        *counts.entry(word.to_owned()).or_insert(0) += 1;
    }

    counts
}
```

This simple version allocates a `String` for every observed word, including repeats, before the map discovers whether the key is occupied. For modest inputs that cost may be acceptable. A performance-sensitive tokenizer can use the lower-level `Entry` variants or an interning strategy to avoid repeated allocation, but that added machinery needs measurement to justify it.

`split_whitespace` does no punctuation removal or case folding. `"Rust"`, `"rust"`, and `"rust,"` are three keys. Token normalization is a separate policy and should be tested with the languages and punctuation the program expects.

### Entry handles express conditional insertion

`entry` supports more than a zero default. `or_insert_with` computes a value only when the key is absent, which matters when construction allocates or performs other expensive work. `and_modify` updates an occupied entry before supplying an insertion fallback:

```rust
use std::collections::HashMap;

let mut totals = HashMap::new();
for (name, amount) in [("tea", 3), ("coffee", 5), ("tea", 4)] {
    totals
        .entry(name)
        .and_modify(|total| *total += amount)
        .or_insert(amount);
}

assert_eq!(totals.get("tea"), Some(&7));
assert_eq!(totals.get("coffee"), Some(&5));
```

The first `tea` is vacant, so `and_modify` does nothing and `or_insert` stores 3. `coffee` follows the same path with 5. The second `tea` is occupied, so the modification adds 4 to the existing 3; because the entry is now occupied, `or_insert` leaves it unchanged. The chain performs one entry lookup per input and keeps the occupied and vacant policies adjacent.

Matching on `std::collections::hash_map::Entry` exposes the two cases directly when insertion needs access to the key, removal, or several operations. It is often clearer than a separate `contains_key` followed by `get_mut` or `insert`; that two-step form repeats lookup and can accidentally separate a check from the update it was meant to govern.

## Determinism may justify an ordered collection

Switching from `HashMap` to `BTreeMap` changes more than asymptotic lookup. A tree map requires `Ord` rather than `Hash + Eq`, iterates in key order, and supports bounded range traversal. That can remove a sort step from reports and make serialized output reproducible.

```rust
use std::collections::BTreeMap;

let prices = BTreeMap::from([
    ("apple", 120),
    ("banana", 80),
    ("pear", 100),
]);

let middle: Vec<_> = prices.range("banana"..="pear").collect();
```

The range visits `banana` and `pear` in lexical key order. A hash map would need to inspect every entry for a range-like query and then sort the retained keys if order mattered. The tree's logarithmic operations may be the better fit even when hash lookup has a lower expected complexity.

Deterministic iteration alone does not require changing the storage type when output is rare. Collecting borrowed entries and sorting just before presentation preserves hash-map lookup behavior elsewhere. The choice depends on which operation dominates and whether order is an invariant or merely formatting.

## Iteration states the ownership transfer

Collections expose three recurring traversal forms:

| Form | Item | Collection afterward |
|---|---|---|
| `collection.iter()` | shared references | remains usable after borrow ends |
| `collection.iter_mut()` | mutable references | remains usable after exclusive borrow ends |
| `collection.into_iter()` | owned elements | collection is consumed |

For maps the item is a key-value pair in the corresponding reference form. Consuming a map yields owned keys and values, which can be moved into another collection without cloning. Borrowing a map yields references tied to the map's lifetime.

`collect` needs a destination type because many collections can be built from the same iterator:

```rust
use std::collections::{BTreeSet, HashSet};

let words = ["red", "blue", "red"];
let hash: HashSet<_> = words.into_iter().collect();
let sorted: BTreeSet<_> = words.into_iter().collect();
```

Both remove duplicates. The hash set optimizes membership lookup and has unspecified iteration order; the tree set iterates as `blue`, then `red`.

## Clearing values and releasing capacity are separate operations

`clear` drops every element but normally retains the collection's allocation for reuse. For a vector or string that repeatedly fills to a similar size, retaining capacity avoids another allocation on the next cycle. `truncate` drops only a suffix, while `drain` removes a selected range and yields the removed items.

```rust
let mut buffer = Vec::with_capacity(1024);
buffer.extend(0..100);
buffer.clear();

assert_eq!(buffer.len(), 0);
assert!(buffer.capacity() >= 1024);
```

An empty collection can therefore still reserve substantial memory. `shrink_to_fit` asks the collection to reduce excess capacity, but it is not a promise to reach one exact allocation size. Repeatedly shrinking and regrowing a hot buffer trades memory for allocation work and is often counterproductive.

Dropping the collection releases its owned allocation and drops remaining elements. Draining, removing, or replacing an element also runs that element's destructor at the corresponding point. When values manage files, sockets, or locks, the mutation method chosen can determine when those resources are released.

## Review notes for collection code

- Accept slices when a function needs only a borrowed sequence, and `&str` when it needs only borrowed text.
- Use `get` when absence is part of normal control flow; use indexing when invalid bounds indicate a broken invariant.
- Treat capacity as an optimization detail, never as permission to bypass borrowing rules.
- State whether text logic operates on bytes, Unicode scalar values, or grapheme clusters.
- Do not build tests or output protocols around hash-map iteration order.
- Decide whether a result should borrow from its input or own independent data; the return type should make that lifetime choice apparent.
- Choose `remove`, `swap_remove`, `retain`, or a queue structure according to whether order and removal position matter.

<div className="see-also">

See also: [Ownership, References, and Slices](/cs/programming/rust/ownership-references-slices) · [Closures and Iterators](/cs/programming/rust/closures-and-iterators) · [Pattern Matching](/cs/programming/rust/pattern-matching) · [Smart Pointers](/cs/programming/rust/smart-pointers)

</div>
