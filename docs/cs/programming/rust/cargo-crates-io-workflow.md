---
title: Cargo and Crates.io Workflow
sidebar_position: 15
---

# Cargo and Crates.io Workflow

Cargo coordinates more than compilation. It resolves dependencies, selects targets and profiles, runs tests, builds documentation, assembles publishable archives, and manages groups of related packages. The manifest records the range of builds a package supports; the lockfile records one resolved dependency graph. Confusing those two roles leads either to unreproducible applications or libraries with needlessly rigid dependency requirements.

## Package, crate, target, and workspace

Cargo terminology separates several layers that casual speech often calls “a crate”:

| Term | Meaning |
|---|---|
| Package | A `Cargo.toml` plus the source and metadata it describes |
| Crate | One Rust compilation unit, rooted at a source file |
| Target | A library, binary, example, test, benchmark, or build script Cargo can build |
| Workspace | Packages managed together under a shared lockfile and target directory |
| Registry | An index and download service for published packages; crates.io is the default public registry |

A package may contain at most one library target and any number of binary targets. The conventional roots are `src/lib.rs` and `src/main.rs`; additional binaries can live under `src/bin/`. Integration-test files under `tests/` are separate crate targets. Cargo infers these layouts, while explicit `[[bin]]`, `[lib]`, and related tables handle nonstandard paths or settings.

The distinction matters during design. Moving logic from a binary target into the package's library target does not require a second package. It creates a reusable crate boundary inside the same package, which integration tests and the binary can both import. A workspace becomes useful when components need separate manifests, dependency sets, versions, or publication decisions.

## Reading a manifest as a build contract

The `[package]` table identifies a package and states metadata used for compilation and publication:

```toml
[package]
name = "line-count"
version = "0.1.0"
edition = "2024"
description = "Counts matching lines in UTF-8 text"
license = "MIT OR Apache-2.0"
```

The name and version identify a published release. The edition selects language and Cargo conventions without changing the compiler version by itself. Description and license metadata matter to registry users and packaging tools. Other metadata can identify documentation, source repository, categories, included files, and the minimum supported Rust version.

Dependency sections describe why a package needs another package:

```toml
[dependencies]
serde = { version = "1.0.210", features = ["derive"] }

[dev-dependencies]
pretty_assertions = "1.4.1"

[build-dependencies]
cc = "1.1.21"
```

Normal dependencies are available to library and binary code. Development dependencies are used for tests, examples, and benchmarks and are not propagated to downstream packages. Build dependencies are compiled for, and visible to, `build.rs`; ordinary crate code cannot use them unless they are also declared as normal dependencies. Target-specific dependency tables can restrict a dependency to an operating system, architecture, or other target configuration.

The version numbers above illustrate syntax rather than a recommendation to select those releases. Dependency choice also requires reviewing maintenance, license, platform support, transitive cost, and the public types it introduces.

## Worked resolution: requirement versus selected version

A plain version string is Cargo's default caret requirement. Suppose the manifest contains:

```toml
[dependencies]
example-lib = "1.2.3"
```

The requirement means

```text
>= 1.2.3, < 2.0.0
```

Now trace a first resolution when the registry contains versions `1.2.2`, `1.2.3`, `1.4.0`, and `2.0.0`:

1. `1.2.2` is rejected because it is below the stated minimum.
2. `1.2.3` and `1.4.0` satisfy the compatible range.
3. `2.0.0` is rejected because it crosses the upper bound.
4. Subject to the rest of the dependency graph and resolver policy, Cargo generally prefers the highest acceptable version, so it selects `1.4.0`.
5. The exact selected package, checksum, source, and transitive graph are recorded in `Cargo.lock`.

On a later build, the lockfile keeps `1.4.0` even if `1.5.0` has appeared. `cargo update -p example-lib` asks Cargo to find a newer version within the manifest's allowed range. Changing the manifest to `"2.0.0"` is required before the resolver may choose the incompatible major line.

Pre-1.0 caret compatibility follows Cargo's leftmost-nonzero rule:

| Requirement | Effective range |
|---|---|
| `"1.2.3"` | `>=1.2.3, <2.0.0` |
| `"0.2.3"` | `>=0.2.3, <0.3.0` |
| `"0.0.3"` | `>=0.0.3, <0.0.4` |

Tilde requirements such as `~1.2.3` restrict updates to versions below `1.3.0`. An exact requirement such as `=1.2.3` admits only that release. Exact pins can make a shared graph harder to resolve and are rarely the right response to a broken update; the lockfile is the normal place to stabilize one application's selected versions.

The minimum in the manifest should match the oldest dependency release whose API the code actually uses. If code begins using an API added in `1.4.0`, leaving the requirement at `1.2.3` gives fresh downstream resolution permission to choose a version that cannot compile the crate.

## `Cargo.toml` permits; `Cargo.lock` records

The manifest describes acceptable dependency sources, versions, features, and target conditions. The lockfile captures a concrete solution for the entire graph. Commands that need the graph reuse locked versions when they still satisfy the manifests.

Applications normally commit `Cargo.lock` so development, continuous integration, and deployment begin from the same graph. A library's published package does not force its lockfile on downstream users; their top-level package resolves the library together with the rest of their graph. A library repository may still keep its lockfile to stabilize its own tests and tooling.

`cargo build --locked` fails rather than changing the lockfile. It is useful in CI when an unnoticed resolution change should be treated as an error. `--frozen` additionally prevents network access. Neither flag proves that cached sources or the compiler environment are identical, so a lockfile is one part of reproducibility rather than a complete environment capture.

Several commands help inspect resolution:

```text
cargo tree                    # dependency tree and duplicate versions
cargo tree -i package-name    # packages that depend on a selected package
cargo update -p package-name  # update one package within allowed requirements
cargo metadata                # machine-readable package and graph metadata
```

Two incompatible versions of the same package may coexist in a graph. Their types are distinct even when they have the same Rust names. Exposing dependency-owned types in a public API therefore makes that dependency part of the compatibility surface and can complicate downstream resolution.

## The edit loop and the measurement build

Cargo profiles choose compiler settings for a kind of build. The default `dev` profile favors fast compilation and useful debugging. The default `release` profile enables optimization and usually takes longer to compile.

| Command | Main purpose |
|---|---|
| `cargo check` | Type-check and borrow-check without producing final linked artifacts |
| `cargo build` | Build development artifacts |
| `cargo test` | Build and run test targets and doc tests |
| `cargo clippy --all-targets` | Run available Clippy lints across targets |
| `cargo doc --no-deps` | Build documentation for local packages |
| `cargo build --release` | Build optimized artifacts |

`cargo check` is usually the fastest feedback after an edit, but it does not exercise linking, tests, build-script behavior for every target, or run-time behavior. A successful release build also says nothing about algorithmic correctness. Each command answers a narrower question.

Performance measurements should use the profile and feature set intended for deployment. Debug timing can be dominated by missing optimization, particularly in iterator-heavy numeric code. Conversely, a release-only check can hide useful debug assertions. Record the command, target, feature flags, input, and compiler version beside a benchmark result.

Profile settings can be customized in root manifest tables such as `[profile.release]`. Increasing optimization, enabling link-time optimization, changing panic strategy, or reducing code-generation units trades compilation time, binary size, debugging behavior, and sometimes run time. Change those settings from measurements rather than copying a generic “fastest” profile.

## Features are additive configuration

Cargo features conditionally enable code or optional dependencies. A package might keep JSON support optional:

```toml
[dependencies]
serde_json = { version = "1.0.128", optional = true }

[features]
default = []
json = ["dep:serde_json"]
```

Source code then uses `#[cfg(feature = "json")]` around the corresponding implementation. The `dep:` prefix enables the optional dependency without exposing an additional implicit feature of the dependency's name.

Features unify additively across a dependency graph. If one path requests feature A and another requests feature B on the same resolved package, that package is generally built with both. Features should therefore enable capabilities, not select mutually exclusive modes. Code must remain valid when several features are enabled together.

A compact test matrix covers the configurations users are most likely to build:

```text
cargo test
cargo test --no-default-features
cargo test --all-features
cargo test --features json
```

The full power set grows exponentially, so supported combinations should stay small and documented. A default feature is easy to add and difficult to remove without affecting users who relied on an unqualified dependency.

## Worked workspace split: core logic and CLI shell

Suppose a command-line search tool has reusable matching logic and process-specific argument handling. A workspace can hold two packages:

```toml
[workspace]
resolver = "3"
members = ["search-core", "search-cli"]

[workspace.package]
edition = "2024"
license = "MIT OR Apache-2.0"
```

`search-cli/Cargo.toml` depends on the core package:

```toml
[package]
name = "search-cli"
version = "0.1.0"
edition.workspace = true
license.workspace = true

[dependencies]
search-core = { path = "../search-core" }
```

The design trace is:

1. `search-core/src/lib.rs` owns search functions and their unit tests; it does not know about command-line arguments or standard output.
2. `search-cli/src/main.rs` parses arguments, reads files, calls `search_core`, and selects exit status and presentation.
3. The CLI's path dependency tells Cargo where to find the local package.
4. The workspace root supplies one `Cargo.lock` and shared `target` directory for both members.
5. `cargo test --workspace` checks both packages; `cargo test -p search-core` narrows the run to the library package.

If the core package is later published, a path-only normal dependency cannot be used by registry consumers. Local development can pair `path` with a compatible registry `version`, or the CLI and library can be published in dependency order with valid registry metadata.

A workspace is not automatically better than one package. If components always share a release, dependency set, and audience, modules plus library and binary targets are simpler. Split packages where the boundary changes reuse, compilation dependencies, ownership, or publication.

## Documentation is part of the artifact

`///` documents the following item, while `//!` documents the enclosing module or crate. Rust code blocks in documentation comments are compiled as doc tests by `cargo test --doc`.

```rust
/// Adds one to an integer.
///
/// ```
/// use line_count::add_one;
/// assert_eq!(add_one(2), 3);
/// ```
pub fn add_one(value: i32) -> i32 {
    value + 1
}
```

`cargo doc --no-deps --open` builds local HTML and opens it without spending time documenting every dependency. Read the rendered result: correct Markdown source can still produce awkward navigation, broken intra-doc links, or an example that lacks enough context.

Public names, re-exports, trait implementations, feature flags, error behavior, and documented panics all form the usable API. A `pub use` can provide a stable short path, but re-exporting an internal module wholesale ties compatibility to the current directory structure.

## Inspecting the exact package before publication

Publication is an artifact review, not merely an upload command. `cargo package --list` shows files selected for the archive. `cargo package` creates and verifies the package locally. It catches missing metadata, disallowed dependency forms, files omitted by include/exclude rules, and code that works only because untracked local files are present.

A careful release sequence is:

1. Review public API and decide whether the version change matches compatibility impact.
2. Run tests, documentation tests, lints used by the project, and a release build with supported feature sets.
3. Check `cargo package --list` for secrets, generated bulk, missing readme or license files, and required test fixtures.
4. Run `cargo package` and inspect or test the packaged artifact rather than only the source tree.
5. Run `cargo publish --dry-run` to exercise publication checks without uploading.
6. Publish only after registry ownership, metadata, and credentials point to the intended package.

A published version cannot be overwritten with different contents. A release can be yanked to discourage new resolution, but existing lockfiles may still refer to it. Version numbers and package names therefore need a final check before upload.

Crates.io treats SemVer as a compatibility promise between releases, but determining whether a Rust change is breaking requires judgment. Removing or renaming public items is clearly breaking. Adding a required trait method, changing feature defaults, tightening generic bounds, or exposing a different dependency type can also break users even if local tests pass.

<div className="see-also">

See also: [Getting Started, Toolchain, and Cargo](/cs/programming/rust/getting-started-toolchain-cargo) · [Packages, Crates, and Modules](/cs/programming/rust/packages-crates-modules) · [Automated Tests](/cs/programming/rust/automated-tests) · [I/O Project with minigrep](/cs/programming/rust/io-project-minigrep)

</div>
