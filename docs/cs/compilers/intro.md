---
title: Compilers and Interpreters
sidebar_position: 0
---

# Compilers and Interpreters

Compilers and interpreters are the machinery that turns programming languages from text into behavior. This section follows the concrete route of Nystrom's *Crafting Interpreters* while cross-referencing the broader compiler tradition from Aho, Lam, Sethi, and Ullman; Appel; Cooper and Torczon; and Muchnick. The emphasis is practical: each page explains the abstraction, the implementation technique, the common failure modes, and the connection to neighboring computer-science topics.

The organization mirrors the life of a program. Source text is first scanned into tokens, parsed into syntax trees, checked for semantic meaning, and either interpreted directly or lowered to bytecode and intermediate representations. Runtime systems then support execution with environments, call frames, heap objects, native services, and garbage collection. Nystrom's Lox interpreters provide the running case study: jlox shows tree walking and lexical resolution, while clox shows bytecode, virtual-machine dispatch, closures, hash tables, and a compact mark-and-sweep collector. The supplementary material adds standard compiler topics that Crafting Interpreters mentions only briefly, including LR parsing, Hindley-Milner inference, SSA, dataflow analysis, register allocation, generational garbage collection, and modern VM/JIT context. Read the pages as a linked path, not as isolated notes.

Pages in this section:

1. [Lexical Analysis and Scanning](/cs/compilers/lexical-analysis-and-scanning)
2. [Parsing and Syntax Trees](/cs/compilers/parsing-and-syntax-trees)
3. [Tree-Walking Interpreters](/cs/compilers/tree-walking-interpreters)
4. [Bytecode Compilation and Virtual Machines](/cs/compilers/bytecode-compilation-and-virtual-machines)
5. [Semantic Analysis and Type Checking](/cs/compilers/semantic-analysis-and-type-checking)
6. [Intermediate Representations and Optimization](/cs/compilers/intermediate-representations-and-optimization)
7. [Garbage Collection and Runtime Systems](/cs/compilers/garbage-collection-and-runtime-systems)
