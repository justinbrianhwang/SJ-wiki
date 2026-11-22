---
title: Programming Languages
sidebar_position: 1
---

# Programming Languages

Notes on programming languages, organized by language family from low-level systems work up to applied / data-oriented use.

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
