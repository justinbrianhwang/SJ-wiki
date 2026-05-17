---
title: Programming Languages
sidebar_position: 1
---

# Programming Languages

Notes on programming languages, organized by language family from low-level systems work up to applied / data-oriented use.

![A C language logo marks the systems-programming pages built around C examples.](https://commons.wikimedia.org/wiki/Special:FilePath/C_Programming_Language.svg)

*Figure: C remains the reference language for low-level memory, pointers, and Unix interfaces. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:C_Programming_Language.svg), ElodinKaldwin, public domain text logo.*

![The ISO C++ logo marks pages on classes, templates, containers, and modern C++ idioms.](https://commons.wikimedia.org/wiki/Special:FilePath/ISO_C%2B%2B_Logo.svg)

*Figure: C++ extends systems programming with abstraction, generic code, and deterministic resource management. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ISO_C%2B%2B_Logo.svg), Jeremy Kratz, public domain text logo.*

![The Python logo marks pages on scripting, testing, packaging, and scientific programming.](https://commons.wikimedia.org/wiki/Special:FilePath/Python-logo-notext.svg)

*Figure: Python provides the practical environment for many CS, ML, and data examples. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg), Python Software Foundation, GPL-compatible free license; trademark terms apply.*

![The Rust logo marks pages on ownership, borrowing, traits, and safe systems programming.](https://commons.wikimedia.org/wiki/Special:FilePath/Rust_programming_language_black_logo.svg)

*Figure: Rust connects systems control with compile-time memory-safety guarantees. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Rust_programming_language_black_logo.svg), Rust Foundation, CC BY 4.0.*

![The R logo marks pages on statistical computing, graphics, and data analysis.](https://commons.wikimedia.org/wiki/Special:FilePath/R_logo.svg)

*Figure: R connects programming examples to statistical modeling and visualization workflows. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:R_logo.svg), The R Foundation, CC BY-SA 4.0.*

## Languages

1. **[C](/cs/programming/c/intro)** — the systems language; types, pointers, memory, and the C standard library
2. **[C++](/cs/programming/cpp/intro)** — objects, templates, the STL, and modern C++ idioms *(populated from Walter Savitch, *Absolute C++*)*
3. **[Rust](/cs/programming/rust/intro)** — ownership, borrowing, lifetimes, and safe systems programming
4. **[Java](/cs/programming/java/intro)** — the JVM, classes, collections, and concurrency
5. **[Python](/cs/programming/python/intro)** — dynamic typing, idioms, the standard library, and the scientific stack
6. **[R](/cs/programming/r/intro)** — vectors, data frames, the tidyverse, and statistical visualization

## Why this order

The progression goes from systems-level to applied:

- **C** establishes the cost model — every other language is partially explained as a layer over it.
- **C++** adds abstraction (classes, templates, the STL) without giving up the cost model.
- **Rust** keeps the cost model but enforces memory safety statically.
- **Java** trades direct memory control for a managed runtime and rich libraries.
- **Python** trades performance for ergonomics and a vast ecosystem.
- **R** is specialized for statistical data analysis.

Pages within each language section have their own ordering — usually basics → types → control flow → data structures → idioms → advanced features.
