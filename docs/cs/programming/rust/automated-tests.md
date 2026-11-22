---
title: Automated Tests
sidebar_position: 12
---

# Automated Tests

Rust's type system rules out many invalid states, but it cannot decide whether a pricing rule, parser, or search result matches the intended behavior. Tests are ordinary Rust functions annotated for the built-in test harness. Cargo compiles them in a special test configuration, discovers the generated test cases, runs them, and reports panics or returned errors.

The useful unit of a test is an observable claim. A good name states the condition and outcome, the setup contains only data needed for that claim, and the assertion reports enough context to diagnose a failure without stepping through the test first.

## What `cargo test` builds and runs

`#[test]` marks a zero-argument function as a test case. A conventional unit-test module sits beside the implementation:

```rust
pub fn add_two(n: i32) -> i32 {
    n + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn adds_two_to_positive_input() {
        assert_eq!(add_two(3), 5);
    }
}
```

`#[cfg(test)]` includes the module only when the crate is compiled in test configuration. `use super::*` brings names from the parent module into scope. Because the test module is a child of the implementation module, it may test private items under Rust's module privacy rules.

By default, `cargo test` runs several kinds of executable checks associated with a package:

| Kind | Usual location | Boundary being checked |
|---|---|---|
| Unit test | `#[cfg(test)] mod tests` near code | Public and private behavior within the crate |
| Integration test | Files under `tests/` | Library's public API as an external crate sees it |
| Documentation test | Rust code blocks in `///` or `//!` comments | Public examples compile and behave as documented |
| Binary test | Unit tests inside binary source | Behavior local to a binary target |

Each file directly under `tests/` is compiled as a separate crate. It cannot access private library items. That apparent limitation is useful: integration tests catch accidental dependence on implementation details and often survive internal refactoring.

Test binaries run cases in parallel by default. Tests must not assume an execution order or share a fixed output filename. When diagnosing suspected interference, `cargo test -- --test-threads=1` runs harness cases serially, but serialization should not become a permanent substitute for isolated fixtures.

## Success, failure, and diagnostic assertions

An ordinary test passes by returning normally and fails by panicking. Assertion macros provide the common panic points:

- `assert!(condition)` checks a Boolean expression.
- `assert_eq!(left, right)` checks equality and prints both values on failure.
- `assert_ne!(left, right)` checks inequality and also prints both values.

`assert_eq!` and `assert_ne!` require values that implement `PartialEq` and `Debug`. For structured domain results, deriving those traits often improves production diagnostics as well as tests.

All assertion macros accept a custom message after their required arguments:

```rust
assert_eq!(
    actual_total,
    expected_total,
    "invoice {invoice_id} had the wrong total"
);
```

The message should identify the case or invariant, not repeat “assertion failed.” For setup that cannot reasonably continue, `expect("fixture should contain a header")` gives better context than bare `unwrap()`.

A test may return `Result<(), E>` when setup or the operation under test is fallible. `Ok(())` passes; `Err` fails and is reported. This form permits `?`:

```rust
#[test]
fn parses_configured_limit() -> Result<(), Box<dyn std::error::Error>> {
    let text = "42";
    let limit: u32 = text.parse()?;
    assert_eq!(limit, 42);
    Ok(())
}
```

Use `?` for failures that prevent the test from reaching its assertion. When a particular error is the behavior under test, inspect that error explicitly instead of propagating it.

## Worked boundary example: strict rectangle containment

Suppose containment requires both dimensions of the receiver to be strictly greater. Equal width or equal height must be rejected:

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

A single happy-path example would not distinguish `>` from `>=` or `&&` from a mistaken `||`. The test set should cross each boundary:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    fn rect(width: u32, height: u32) -> Rectangle {
        Rectangle { width, height }
    }

    #[test]
    fn larger_in_both_dimensions_can_hold() {
        assert!(rect(8, 7).can_hold(&rect(5, 1)));
    }

    #[test]
    fn smaller_width_cannot_hold() {
        assert!(!rect(4, 7).can_hold(&rect(5, 1)));
    }

    #[test]
    fn equal_width_is_not_strictly_larger() {
        assert!(!rect(5, 7).can_hold(&rect(5, 1)));
    }

    #[test]
    fn equal_height_is_not_strictly_larger() {
        assert!(!rect(8, 1).can_hold(&rect(5, 1)));
    }
}
```

Trace what each case excludes:

1. Width `8 > 5` and height `7 > 1` are both true, establishing the positive path.
2. Width `4 > 5` is false while height is true, so an accidental `||` would fail this test.
3. Equal widths distinguish the specified `>` from `>=`.
4. Equal heights check the second comparison independently.

These tests encode the boundary, not the implementation. Rewriting `can_hold` through a helper or a tuple comparison should leave them valid as long as the public behavior remains strict on both dimensions.

## Testing fallible code by inspecting both variants

Consider a parser that accepts a positive integer and distinguishes malformed input from zero. A typed error makes those outcomes testable without depending on display text:

```rust
#[derive(Debug, PartialEq)]
enum PositiveError {
    NotAnInteger,
    Zero,
}

fn parse_positive(input: &str) -> Result<u32, PositiveError> {
    let value = input
        .parse::<u32>()
        .map_err(|_| PositiveError::NotAnInteger)?;

    if value == 0 {
        Err(PositiveError::Zero)
    } else {
        Ok(value)
    }
}
```

Three cases cover the success and both error branches:

```rust
#[test]
fn parses_positive_integer() {
    assert_eq!(parse_positive("42"), Ok(42));
}

#[test]
fn reports_zero_separately() {
    assert_eq!(parse_positive("0"), Err(PositiveError::Zero));
}

#[test]
fn rejects_non_integer_text() {
    assert_eq!(
        parse_positive("forty-two"),
        Err(PositiveError::NotAnInteger)
    );
}
```

For `"42"`, parsing yields `Ok(42)` and the zero branch is skipped. For `"0"`, parsing succeeds first, then the domain check returns `Zero`. For `"forty-two"`, parsing fails and `?` returns `NotAnInteger` before the domain check. Comparing the complete `Result` proves which stage rejected the input.

A less precise `assert!(parse_positive("0").is_err())` would allow the two error cases to be swapped without detection. Exact error assertions are valuable when the distinction is part of the API contract; they are brittle when they inspect incidental wording that callers were never promised.

## Panics are for invariants, not ordinary errors

`#[should_panic]` passes only when the test panics. Add an expected message substring so an unrelated panic does not satisfy the case:

```rust
fn percentage(part: u32, whole: u32) -> u32 {
    assert!(whole != 0, "whole must be nonzero");
    part * 100 / whole
}

#[test]
#[should_panic(expected = "whole must be nonzero")]
fn percentage_rejects_zero_whole() {
    percentage(3, 0);
}
```

The assertion panics before division, and the expected substring ties success to the intended invariant. If zero is a normal input that callers should handle, returning `Result` would be a better API and the test should compare the error instead. Panic tests suit programmer errors, violated internal invariants, and interfaces explicitly documented to panic.

When more detail matters, `std::panic::catch_unwind` can inspect whether a closure panicked, but it introduces unwind-safety constraints and rarely improves an ordinary unit test. Prefer testing the returned error whenever the production API offers one.

## Integration tests at the public boundary

Assume a library crate named `text_tools` exports `count_matches`. A minimal integration test lives in `tests/search.rs`:

```rust
use text_tools::count_matches;

#[test]
fn counts_matching_lines() {
    let text = "Rust:\nsafe, fast, productive.\nPick three.";
    assert_eq!(count_matches("duct", text), 1);
}
```

The test imports the crate exactly as a downstream user would. If the function was forgotten behind a private module or not re-exported from the public API, this test fails to compile even if a nearby unit test can call it.

Shared integration-test support should normally go in a submodule such as `tests/common/mod.rs`, then be declared with `mod common;` from each integration test crate. A standalone `tests/common.rs` is itself treated as an integration-test crate, which creates an extra empty test target.

Integration tests can also execute a compiled binary, but the standard library alone does not provide a high-level assertion framework for process output. Keep command-line parsing and core behavior in library functions where possible, then leave a small number of end-to-end tests for process status, standard output, and standard error.

## Documentation examples as executable contracts

Rust code blocks in documentation comments are compiled as doc tests. A public example can therefore teach usage and detect API drift:

```rust
/// Returns the larger of two values.
///
/// ```
/// use text_tools::larger;
///
/// assert_eq!(larger(4, 9), 9);
/// ```
pub fn larger(a: i32, b: i32) -> i32 {
    a.max(b)
}
```

Lines prefixed with `#` inside a doc-test code block are compiled but hidden from rendered documentation, which is useful for setup that would distract from the example. Blocks that should compile but not run can use `no_run`; blocks demonstrating an intentional compiler error can use `compile_fail`. Marking a block as plain text disables the check entirely and should be reserved for pseudocode or incomplete fragments.

Doc tests favor short public examples. Complex edge cases belong in unit or integration tests where fixtures and failure messages are easier to maintain.

## Table-driven cases without hiding the failure

Several inputs that exercise one rule can share a test body. Keep the case data small and include it in the assertion message:

```rust
fn clamp_percentage(value: i32) -> i32 {
    value.clamp(0, 100)
}

#[test]
fn clamps_percentages_to_closed_interval() {
    let cases = [
        (-20, 0),
        (0, 0),
        (37, 37),
        (100, 100),
        (140, 100),
    ];

    for (input, expected) in cases {
        assert_eq!(
            clamp_percentage(input),
            expected,
            "unexpected result for input {input}"
        );
    }
}
```

The five rows distinguish lower saturation, both inclusive boundaries, an unchanged interior value, and upper saturation. If input 140 fails, the custom message identifies the row even though all cases share one harness test name.

Table-driven form works when setup and assertion are genuinely identical. Separate tests are better when cases represent different requirements or need different fixtures. One failing assertion stops the loop, so a single table test may report only the first broken case. Independent test functions let the harness run and report every case, at the cost of more repeated setup.

Generated case names from a third-party test framework can combine both benefits, but a dependency is unnecessary for a handful of rows. The standard loop is transparent and debuggable.

## Compile-time contracts need compile-time tests

Some Rust behavior is the refusal to compile: a type must not be `Send`, a borrowed result must not outlive its input, or a macro must reject invalid syntax. A run-time unit test cannot assert a compiler error because invalid source never becomes a test binary.

Documentation blocks marked `compile_fail` are suitable for small public examples. The harness succeeds when the example fails to compile, but compiler diagnostics are not a stable string contract, so the example should isolate the intended error. Larger compile-pass and compile-fail suites usually use a dedicated test harness that invokes the compiler on fixture crates.

Do not turn every type error into such a test. The compiler already checks ordinary implementation code. Compile-fail coverage earns its maintenance cost when rejection is part of a public API's design, particularly for macros, unsafe abstractions, typestate, and lifetime-sensitive interfaces.

## Regression tests preserve the smallest reproducer

When fixing a bug, first reduce the report to the smallest input that still fails. The regression test should call the public boundary that exposed the bug and assert the corrected outcome. Extra production objects, timestamps, or network setup make the test harder to understand and can hide the actual condition.

Name the test after the failed behavior rather than an issue number alone. An external number may disappear or require context; `empty_header_does_not_consume_first_record` tells a future maintainer what must remain true. A short comment may record a nonobvious historical cause, but the fixture and assertion should carry most of the explanation.

## Files, clocks, and other sources of flaky tests

Tests should own the state they mutate. A test that writes `output.txt` in the working directory can collide with another parallel case or overwrite a developer's file. Use a uniquely named directory under `std::env::temp_dir()`, include a process or test-specific component, and remove it after the assertion. For nontrivial projects, a dedicated temporary-directory helper crate can guarantee cleanup on drop.

Environment variables and the process working directory are global to the process. Changing them in one test can affect another running concurrently. Prefer passing configuration and paths as arguments. If a global mutation is unavoidable, isolate it behind synchronization and restore the previous value even when assertions fail.

Real time, network services, random input, and iteration order from hash-based collections can also make tests intermittent. Inject a clock or deterministic input at the design boundary, compare unordered results as sets or sorted collections, and reserve live-service checks for an explicitly controlled test environment.

## Running the smallest useful slice

Cargo forwards arguments after `--` to the test harness:

```text
cargo test                         # all ordinary tests for the package
cargo test parse_positive          # names containing this filter
cargo test --test search           # one integration-test target
cargo test --doc                   # documentation tests
cargo test -- --show-output        # include output from passing tests
cargo test -- --ignored            # only ignored tests
cargo test -- --include-ignored    # ordinary and ignored tests
```

Mark a slow or environment-dependent case with `#[ignore = "reason"]`; do not ignore a nondeterministic failure merely to make the default suite green. While debugging, run the narrow failing case. Before handing off a change, run the full relevant suite so shared state and integration boundaries are exercised.

Test filters match substrings, which can select more cases than expected. The harness option `--exact` requests one full test name once that name is known. `--nocapture` streams output as tests run; `--show-output` retains captured output for successful tests in the final report. Assertions remain preferable to reading logs because Cargo can evaluate their success automatically.

## Review notes for tests that must last

- Assert public outcomes and domain errors rather than private call sequences.
- Include boundaries that distinguish nearby implementations: empty, equal, one below, one above, and overflow limits where relevant.
- Keep cases independent of order, fixed filenames, global configuration, and wall-clock timing.
- Use typed errors when callers care which failure occurred; avoid locking tests to decorative error wording.
- Let unit tests cover intricate helpers and integration tests cover the promised API.
- A bug fix should usually add a test that fails before the fix and passes after it. The case records the regression more precisely than a comment.
- Avoid asserting several unrelated behaviors in one long test. Once the first assertion panics, later claims are not evaluated.

<div className="see-also">

See also: [Error Handling](/cs/programming/rust/error-handling) · [Cargo and crates.io Workflow](/cs/programming/rust/cargo-crates-io-workflow) · [Structs, Methods, and Enums](/cs/programming/rust/structs-methods-enums) · [Closures and Iterators](/cs/programming/rust/closures-and-iterators)

</div>
