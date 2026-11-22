---
title: Common Programming Concepts
sidebar_position: 4
---

# Common Programming Concepts

Rust uses familiar building blocks—bindings, scalar values, functions, branches, and loops—but gives them precise compile-time meaning. Immutability is the default, numeric widths are explicit, blocks produce values, and loop syntax distinguishes unbounded search from traversal. These rules reduce ambiguity before ownership and borrowing add further constraints.

## Bindings make change explicit

`let` introduces a pattern and binds names to the matched value. A plain binding cannot be reassigned:

```rust
let x = 5;
// x = 6; // cannot assign twice to immutable variable
```

Add `mut` when reassignment is part of the algorithm:

```rust
let mut attempts = 0;
attempts += 1;
attempts += 1;
assert_eq!(attempts, 2);
```

Immutability concerns the binding's allowed mutation through that access path; it is distinct from constants and from whether a value contains interior mutability. For ordinary local code, the useful first question is simple: does this name need to change after initialization? If not, leave it immutable so later assignment becomes a compiler-detected surprise.

### Shadowing creates a new binding

A second `let` may reuse a name. This **shadows** the earlier binding and may change type because it creates a new binding:

```rust
let count = "  15  ";
let count = count.trim();
let count: u32 = count.parse().expect("count should be an integer");
let doubled = count * 2;

assert_eq!(doubled, 30);
```

Trace the types:

1. The first `count` is `&str` containing whitespace.
2. `trim` returns another `&str`, here `"15"`, and the new binding hides the first.
3. `parse` is told to produce `u32`; the third binding is an integer.
4. Multiplication is now integer arithmetic, yielding 30.

A mutable binding cannot make the same transition:

```rust
let mut count = "15";
// count = 15; // expected &str, found integer
```

Mutation replaces a value while preserving the binding's type. Shadowing is useful for a sequence of representations of one concept. Different names are clearer when both representations remain meaningful at the same time.

Shadowing can also be scoped:

```rust
let x = 10;
{
    let x = x * 2;
    assert_eq!(x, 20);
}
assert_eq!(x, 10);
```

The inner initializer can read the outer `x`; after the block, the inner binding is out of scope and the outer value is visible again.

## Constants and static values

`const` declares a compile-time constant, requires an explicit type, and uses a constant expression:

```rust
const SECONDS_PER_HOUR: u32 = 60 * 60;
```

Constants are conventionally named in `SCREAMING_SNAKE_CASE`. They can appear where an inline constant expression could appear and do not imply one unique memory address.

A `static` item denotes one program-wide storage location and has a `'static` lifetime. Immutable statics are useful for fixed data with an address. Mutable statics require unsafe access because unsynchronized global mutation can create data races. Ordinary constants, function parameters, or synchronization primitives are usually better choices than global mutable state.

## Scalar types and literal inference

Rust has four main scalar families:

| Family | Types | Detail |
|---|---|---|
| Signed integers | `i8`, `i16`, `i32`, `i64`, `i128`, `isize` | Represent negative and nonnegative whole numbers |
| Unsigned integers | `u8`, `u16`, `u32`, `u64`, `u128`, `usize` | Represent nonnegative whole numbers |
| Floating point | `f32`, `f64` | IEEE-754 binary floating-point values |
| Boolean and character | `bool`, `char` | Truth values and Unicode scalar values |

`isize` and `usize` match the pointer width of the compilation target. Collection lengths and indices use `usize`, so converting from a possibly negative or wider external integer should be checked rather than cast blindly.

Unconstrained integer literals usually infer as `i32`; floating literals usually infer as `f64`. Suffixes and annotations override the default:

```rust
let count = 42u64;
let ratio: f32 = 0.25;
let index: usize = 3;
```

Integer literals support decimal, hexadecimal, octal, and binary notation, plus underscores for grouping:

```rust
let decimal = 98_222;
let hex = 0xff;
let octal = 0o77;
let binary = 0b1111_0000;
let byte = b'A';
```

A `char` is written with single quotes and represents one Unicode scalar value. It occupies four bytes as a Rust value, though its UTF-8 encoding may use one to four bytes. A user-perceived character can contain several scalar values, so `char` is not a full text-segmentation unit.

## Arithmetic has a type and an overflow policy

Numeric operators generally require compatible operand types; Rust does not silently promote an `i32` to `i64` or an integer to a float. Convert deliberately with `From`, `TryFrom`, or a cast after checking what truncation or range change is acceptable.

Integer division truncates toward zero:

```rust
assert_eq!(7 / 3, 2);
assert_eq!(-7 / 3, -2);
```

Division by zero panics. Floating-point division by zero follows IEEE-754 behavior and can produce infinity or NaN instead.

Fixed-width integer overflow needs an explicit mental model. Cargo's development profile normally checks overflow and panics; optimized release builds normally wrap unless overflow checks are enabled. Code whose correctness depends on one behavior should say so with a method:

```rust
let x = u8::MAX;

assert_eq!(x.checked_add(1), None);
assert_eq!(x.wrapping_add(1), 0);
assert_eq!(x.saturating_add(1), u8::MAX);
assert_eq!(x.overflowing_add(1), (0, true));
```

`checked_add` makes failure part of the return type. `wrapping_add` uses modular arithmetic. `saturating_add` clamps at the boundary. `overflowing_add` returns both the wrapped result and a flag. Cryptography, counters, image channels, and financial quantities often need different choices; relying on build-profile defaults makes that choice unstable.

Floating-point equality has the usual approximation issues. `0.1 + 0.2` need not equal the nearest representation written as `0.3`. Numerical comparisons generally use a tolerance chosen for the scale and error model. NaN compares unequal to every value, including itself, so use methods such as `is_nan` when classification is intended.

### Conversions should reveal possible loss

The `as` operator performs primitive casts, but its brevity does not mean every cast preserves a value. Narrowing an integer discards high bits, converting a signed negative integer to unsigned uses modular representation, and converting a float to an integer drops its fractional part subject to Rust's defined boundary behavior. Such casts are appropriate when those semantics are part of the algorithm, for example masking a known bit pattern.

Use `From` and `Into` for conversions defined as infallible, and `TryFrom` or `TryInto` when the destination may be too small:

```rust
use std::convert::TryFrom;

let small = u8::try_from(200u16);
assert_eq!(small, Ok(200));

let too_large = u8::try_from(300u16);
assert!(too_large.is_err());
```

The first value lies in the inclusive range 0 through 255, so conversion succeeds. The second exceeds `u8::MAX` and returns an error instead of wrapping to 44. At an input boundary, that distinction prevents malformed sizes or counts from becoming plausible smaller values.

Converting `usize` to a fixed-width external format deserves the same check. A length that fits on a 64-bit development machine may not fit a 32-bit field or target. Conversely, a `u64` from a file or network message may not fit `usize` for allocation. Validate before allocating and retain the fallible result in the error path.

String parsing is also a conversion with failure information. `"42".parse::<u32>()` returns `Result`, while `to_string` is infallible formatting. Calling `expect` is suitable when the text is a source-code constant whose invalidity is a programmer error; user input should normally propagate or translate the parse error.

## Tuples, arrays, and destructuring

A tuple has fixed length and may contain different types:

```rust
let record: (&str, u32, bool) = ("Ada", 36, true);
let (name, age, active) = record;

assert_eq!(name, "Ada");
assert_eq!(record.1, 36);
assert!(active);
assert_eq!(age, 36);
```

Tuple positions work well for short local groupings with an obvious convention. A struct becomes clearer when fields need durable names, documentation, or methods. The empty tuple `()` is the **unit** value and represents the absence of another meaningful result.

An array has fixed length and one element type. Its length is part of the type:

```rust
let values: [i32; 4] = [10, 20, 30, 40];
let zeros = [0u8; 16];
```

`[i32; 4]` and `[i32; 5]` are different types. Arrays suit fixed protocol fields, small lookup tables, and data whose size is known at compile time. `Vec<T>` is the ordinary growable sequence.

Array indexing checks bounds at run time when the compiler cannot prove them. An invalid index panics rather than reading unrelated memory. Iteration often avoids both manual bounds and index arithmetic:

```rust
let mut total = 0;
for value in [10, 20, 30, 40] {
    total += value;
}
assert_eq!(total, 100);
```

Patterns can destructure more than tuples. `let [first, _, third] = array;` binds selected positions of a three-element array. Refutable patterns, which might fail to match, belong in `match`, `if let`, `let else`, or similar constructs rather than an ordinary `let` without an alternative.

## Functions require explicit interface types

Function parameter types are always declared, which keeps the interface readable without searching call sites. Return types use `->`:

```rust
fn rectangle_area(width: u32, height: u32) -> u32 {
    width * height
}
```

The body is a block expression. Its final expression has no semicolon and becomes the return value. `return` can exit early:

```rust
fn absolute(value: i32) -> i32 {
    if value < 0 {
        return -value;
    }
    value
}
```

This simple implementation has an edge case: negating `i32::MIN` cannot be represented as `i32` and overflows. Depending on the contract, `checked_abs` returning `Option<i32>`, a wider return type, or an explicit panic may be more honest.

Rust infers local types from the function interface and uses, but generic calls sometimes need a target type. Parsing is the standard example:

```rust
let port: u16 = "8080".parse().expect("valid TCP port");
```

Without the annotation or another constraint, `parse` could return many types implementing `FromStr`.

## Semicolons control value flow

Rust distinguishes statements from expressions. `let` declarations are statements. Literals, arithmetic, function calls, blocks, `if`, `match`, and some loops are expressions that can yield values.

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}
```

Adding a semicolon changes the block's final value to unit:

```rust
fn broken_add_one(x: i32) -> i32 {
    x + 1;
}
```

The compiler reports an expected `i32` but found `()` mismatch. The arithmetic still executes conceptually, but its value is discarded.

Blocks can calculate local intermediate values:

```rust
let area = {
    let width = 8;
    let height = 5;
    width * height
};

assert_eq!(area, 40);
```

The inner `let` lines are statements; `width * height` is the block's final expression. A semicolon after the closing brace ends the outer `let` statement and does not change the value already produced inside.

## `if` chooses one value of one type

Rust conditions must have type `bool`; there is no integer or pointer truthiness. Because `if` is an expression, it can initialize a binding:

```rust
let score = 74;
let label = if score >= 60 { "pass" } else { "retry" };
```

Every reachable branch must produce compatible types. `if condition { 5 } else { "five" }` cannot assign one statically typed result. A branch that always returns, panics, or otherwise diverges has the never type `!` and can coexist with another branch's value:

```rust
let value = if input_is_valid {
    10
} else {
    panic!("invalid input")
};
```

An `if` without `else` has unit value, so it cannot directly initialize a non-unit result. Use `if let` or `match` when the condition is fundamentally about the shape of an enum or pattern rather than a Boolean formula.

Boolean operators `&&` and `||` short-circuit. In `left && right`, `right` is evaluated only when `left` is true; in `left || right`, it is evaluated only when `left` is false. Besides avoiding unnecessary work, this permits a guard to establish a precondition for the second expression:

```rust
let values = [10, 20, 30];
let index = 2;

if index < values.len() && values[index] > 0 {
    println!("positive value");
}
```

Reversing the operands would index before checking the bound and could panic. Bitwise `&` and `|` do not short-circuit and operate on integer bits as well as booleans; they should not be substituted casually in control-flow conditions.

## `loop`, `while`, and `for` state different intent

`loop` repeats until an explicit exit and can yield a value carried by `break`. `while` repeats while a Boolean remains true. `for` traverses an `IntoIterator` and handles progression and termination.

### Worked search with a loop value

Find the first square greater than 50:

```rust
let mut n = 1;

let answer = loop {
    let square = n * n;
    if square > 50 {
        break square;
    }
    n += 1;
};

assert_eq!(answer, 64);
```

The candidates are $1,4,9,16,25,36,49,64$. For values one through seven, the condition is false and the loop increments `n`. At `n = 8`, the square is 64, so `break square` both terminates the loop and supplies the value assigned to `answer`.

Only `loop` supports a non-unit `break` value. `while` and `for` always evaluate to unit. When nested loops need a targeted exit, labels identify the destination:

```rust
'rows: for row in 0..3 {
    for column in 0..3 {
        if row == 1 && column == 2 {
            break 'rows;
        }
    }
}
```

Ranges make bounds visible. `0..3` yields 0, 1, and 2; `0..=3` also yields 3. Iterating a collection directly is preferable when the index itself is irrelevant. Use `.enumerate()` when both position and item are needed.

### Worked conversion and classification

```rust
fn fahrenheit_to_celsius(fahrenheit: f64) -> f64 {
    (fahrenheit - 32.0) * 5.0 / 9.0
}

fn classify_temperature(celsius: f64) -> &'static str {
    if celsius <= 0.0 {
        "freezing"
    } else if celsius < 20.0 {
        "cold"
    } else if celsius < 30.0 {
        "mild"
    } else {
        "hot"
    }
}

let readings = [32.0, 68.0, 86.0, 104.0];
for fahrenheit in readings {
    let celsius = fahrenheit_to_celsius(fahrenheit);
    println!("{fahrenheit:>5.1} F -> {celsius:>5.1} C: {}",
             classify_temperature(celsius));
}
```

For 68°F, subtracting 32 gives 36, multiplying by 5 gives 180, and dividing by 9 gives 20°C. The first two classification conditions are false at exactly 20, while `20 < 30` is true, so the label is `"mild"`. At 32°F the result is 0°C and the inclusive first boundary classifies it as `"freezing"`. Boundary examples document the choice between `<` and `<=` more effectively than a middle value.

## Compiler messages to read literally

- “cannot assign twice to immutable variable” asks whether reassignment is needed or a new shadowing binding is clearer.
- “mismatched types” at a function's closing brace often points to a trailing semicolon or incompatible `if` branches.
- “type annotations needed” means local uses do not constrain a generic result such as `parse` or `collect`.
- An out-of-bounds panic means the code compiled but violated a run-time indexing precondition; iteration or `get` may express the intended behavior better.
- Overflow behavior should come from an explicit method when wrapping, saturation, or rejection is part of the domain rule.

<div className="see-also">

See also: [Ownership, References, and Slices](/cs/programming/rust/ownership-references-slices) · [Structs, Methods, and Enums](/cs/programming/rust/structs-methods-enums) · [Pattern Matching](/cs/programming/rust/pattern-matching) · [Common Collections](/cs/programming/rust/common-collections)

</div>
