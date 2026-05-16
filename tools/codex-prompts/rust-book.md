You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/rust_book.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming/rust/`
- **SUBJECT**: Rust (likely *The Rust Programming Language* — Klabnik & Nichols)

## Produce

1. **`intro.md`** — replace the stub. Overview + chapter list.

2. **15-22 detail pages** covering the standard Rust book scope:
   - Hello, Cargo, the toolchain
   - Common programming concepts (variables, types, functions, control flow)
   - Ownership, references, slices
   - Structs and enums
   - Pattern matching
   - Modules, packages, crates, the path system
   - Common collections (Vec, String, HashMap)
   - Error handling (panic, Result, `?`)
   - Generics, traits, lifetimes
   - Writing automated tests
   - Closures and iterators
   - Cargo and crates.io workflow
   - Smart pointers (Box, Rc, RefCell, Weak)
   - Concurrency (threads, message passing, shared state, Send/Sync)
   - Object-oriented patterns in Rust
   - Advanced traits & types
   - Macros and metaprogramming basics
   - Unsafe Rust (brief)
   - Async/await (if covered)

3. Per-page format: motivation → concept → small `rust` code example → pitfalls / borrow-checker notes → cross-links.

4. Use the **ownership / borrowing diagrams** in Mermaid where they clarify lifetime relationships.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 30` for TOC. 3. Iterate chapters; 1-2 wiki pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Don't fabricate.

Begin now.
