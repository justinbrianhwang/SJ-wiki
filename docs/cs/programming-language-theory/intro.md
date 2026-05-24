---
title: Programming Language Theory
sidebar_position: 0
---

# Programming Language Theory

Programming language theory studies the formal structure of programs: how syntax is built, how execution is defined, how types prevent bad behavior, how proofs certify correctness, and how analyses approximate large codebases. This section synthesizes four complementary sources: Pierce's *Types and Programming Languages* for lambda calculi and type systems, *Software Foundations* for mechanized metatheory and proof-assistant practice, a formal-semantics text for operational, denotational, and axiomatic methods, and Nielson-Nielson-Hankin for dataflow analysis and abstract interpretation.

The notes are organized topically rather than by textbook. Where the sources overlap, a single page combines their viewpoints: TAPL's operational type-safety style, Software Foundations' Coq-style proof discipline, denotational fixed-point semantics, Hoare logic, and static-analysis lattices. Some later material is marked as modern supplementary context, especially algebraic effects, session types, memory models, and current verification tools.

Read the pages in order if you want a coherent course path: start with lambda calculus, add semantics, prove type soundness, move to polymorphism and dependent types, then use program logic and program analysis to reason about realistic imperative and effectful programs. For compiler-oriented reading, pair the semantics and dataflow pages with the [Compilers](/cs/compilers/intro) section. For proof-oriented reading, pair type soundness, dependent types, and axiomatic semantics with [Discrete Math](/math/discrete/intro) and [Cryptography](/cs/cryptography/intro).

1. [Untyped and Typed Lambda Calculus](/cs/programming-language-theory/untyped-and-typed-lambda-calculus)
2. [Operational and Denotational Semantics](/cs/programming-language-theory/operational-and-denotational-semantics)
3. [Type Systems and Type Soundness](/cs/programming-language-theory/type-systems-and-type-soundness)
4. [Polymorphism, Subtyping, and Type Inference](/cs/programming-language-theory/polymorphism-subtyping-and-inference)
5. [Dependent Types and Proof Assistants](/cs/programming-language-theory/dependent-types-and-proof-assistants)
6. [Axiomatic Semantics and Program Logic](/cs/programming-language-theory/axiomatic-semantics-and-program-logic)
7. [Dataflow Analysis and Abstract Interpretation](/cs/programming-language-theory/dataflow-and-abstract-interpretation)
8. [Effects, Monads, and Concurrency Models](/cs/programming-language-theory/effects-monads-and-concurrency-models)
