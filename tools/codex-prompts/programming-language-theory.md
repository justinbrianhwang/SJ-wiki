You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for a new **Programming Language Theory** subject under `docs/cs/programming-language-theory/`.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming-language-theory/`
- **SUPPLIED_TEXTBOOKS**: `f:/coding/SJ Wiki/tmp/Programming Language Structure/`
  - `Benjamin_C._Pierce-Types_and_Programming_Languages-The_MIT_Press(2002).pdf` (Pierce, *TAPL*)
  - `Software Foundations (Benjamin C. Pierce 외 저, 시리즈물).pdf` (Pierce et al., *Software Foundations* — Coq-based)
  - `Formal Semantics of Programming Languages.pdf` (Winskel-style operational/denotational/axiomatic semantics)
  - `Principles of Program Analysis (Flemming Nielson, Hanne Riis Nielson, Chris Hankin 저).pdf` (Nielson-Nielson-Hankin, *Principles of Program Analysis*)
- **STYLE**: Topical chapter names. IEEE inline citations `[N]`.

## Workflow

1. `pdfinfo` + `pdftotext -l 30` on each book for TOC.
2. Iterate topics, synthesize across books in combine mode.
3. Replace `intro.md` last.
4. Print summary.

## Combine mode

Topics overlap (operational semantics in Winskel and TAPL, types in TAPL and Software Foundations, dataflow in Nielson). Write one chapter per topic, draw from whichever book(s) treat it best, note their angles when they differ.

## Produce

### 1. Replace `intro.md` (sidebar 0)
250-400 word overview + numbered list of all pages.

### 2. Create exactly 8 detail pages

| sidebar_position | filename | title |
|---|---|---|
| 1 | `untyped-and-typed-lambda-calculus.md` | Untyped and Typed Lambda Calculus |
| 2 | `operational-and-denotational-semantics.md` | Operational and Denotational Semantics |
| 3 | `type-systems-and-type-soundness.md` | Type Systems and Type Soundness |
| 4 | `polymorphism-subtyping-and-inference.md` | Polymorphism, Subtyping, and Type Inference |
| 5 | `dependent-types-and-proof-assistants.md` | Dependent Types and Proof Assistants |
| 6 | `axiomatic-semantics-and-program-logic.md` | Axiomatic Semantics and Program Logic |
| 7 | `dataflow-and-abstract-interpretation.md` | Dataflow Analysis and Abstract Interpretation |
| 8 | `effects-monads-and-concurrency-models.md` | Effects, Monads, and Concurrency Models |

## Content scope

### 1 Lambda calculus
- Untyped λ-calculus: terms, free/bound variables, α-conversion, β-reduction, η-reduction
- Church-Rosser confluence, Church numerals, Y combinator (fix point)
- Normal forms; call-by-value vs call-by-name reduction strategies
- Simply-typed λ-calculus (STLC): syntax, typing rules, progress + preservation
- Curry-Howard correspondence (overview)

### 2 Operational and denotational semantics
- Small-step (structural operational) vs big-step (natural) semantics
- SOS rules notation; configurations; safety
- Denotational semantics: domain theory, Scott / Plotkin CPOs, least-fixed-point construction
- Equivalence of operational and denotational semantics (Winskel)
- CEK / SECD machines

### 3 Type soundness
- Subject reduction (preservation), progress
- Type contexts, judgments, derivations
- Inversion lemmas; canonical forms
- TAPL-style proof structure
- Failure modes: stuck terms, undefined behavior

### 4 Polymorphism, subtyping, inference
- Parametric polymorphism (System F): ∀-introduction/elimination
- Let-polymorphism (ML); generalization and instantiation
- Hindley-Milner type inference; unification, principal types, Algorithm W
- Subtyping: width / depth / permutation for records; covariance / contravariance
- Bounded quantification (System F<:)
- Higher-rank polymorphism (brief), GADTs (mention)
- Rust-style trait/typeclass dispatch (brief cross-link)

### 5 Dependent types and proof assistants
- Dependent function and dependent pair types (Π, Σ)
- Calculus of Constructions; Predicative vs impredicative universes
- Coq / Lean / Agda / Idris — interaction model, tactics
- Inductive types, recursion principles
- Propositions-as-types (Curry-Howard in depth)
- Software Foundations as case study; Imp language and its semantics in Coq
- Decidability of type checking; consistency

### 6 Axiomatic semantics and program logic
- Hoare triples {P} c {Q}; assignment, sequencing, conditional, while rules
- Weakest precondition (Dijkstra)
- Loop invariants; termination via variants
- Separation logic (Reynolds, O'Hearn): * connective, frame rule
- Concurrent separation logic (CSL) brief
- Refinement types (mention)
- Verification tools: Frama-C, Dafny, F*, Why3

### 7 Dataflow analysis and abstract interpretation
- Lattice theory: complete lattices, monotone functions, fixed points, Kleene iteration
- Dataflow analyses: reaching definitions, live variables, available expressions, very busy expressions
- Forward vs backward, may vs must
- Worklist algorithm; meet-over-paths (MOP) vs maximum fixed point (MFP)
- Abstract interpretation (Cousot-Cousot 1977): Galois connections, abstract domains (intervals, polyhedra, octagons)
- Widening and narrowing operators
- Pointer/alias analysis (Andersen, Steensgaard)
- Information-flow analysis (Sabelfeld-Myers)
- Control-flow analysis (k-CFA)

### 8 Effects, monads, concurrency models
- Monads: list, maybe, state, IO, continuation — Haskell perspective
- Algebraic effects and handlers (Plotkin-Power)
- Effect systems (Lucassen-Gifford)
- Concurrency models: CCS (Milner), CSP (Hoare), π-calculus
- Linear types, session types (brief)
- Memory models for concurrency (cross-link OS/Architecture)
- Software transactional memory (STM)

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter
2. `# Title` H1
3. 1-2 opening paragraphs (motivation + scope)
4. (Optional) 1-2 contextual figures (rare for this subject; mostly Mermaid)
5. `## Definitions` — formal notation
6. `## Key results` — theorems with proofs sketched
7. `## Visual` — **MANDATORY Mermaid** (e.g., β-reduction sequence, typing-derivation tree, lattice diagram, Galois connection, separation-logic frame, Coq proof state)
8. `## Worked example 1` (e.g., type-check `λx.x x` to show failure; prove safety for a small STLC fragment)
9. `## Worked example 2` (e.g., HM inference of `let id = λx.x in id id`; abstract interpretation on intervals)
10. `## Code` — Coq / Haskell / OCaml / Python pseudocode (small snippets only)
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — links to [Theory of Computation](/cs/theory/intro), [Compilers](/cs/compilers/intro), [Discrete Math](/math/discrete/intro), [Cryptography](/cs/cryptography/intro) (verification flavor)
13. `## References` — IEEE-style (Pierce TAPL, Pierce Software Foundations, Winskel, Nielson-Nielson-Hankin, plus foundational papers: Church 1936, Curry-Howard, Plotkin SOS 1981, Milner 1978 (ML/HM), Cousot-Cousot 1977 abstract interpretation, Reynolds 2002 separation logic, Hoare 1969 Hoare logic, Dijkstra 1975 weakest precondition, Lucassen-Gifford 1988 effect system, Hindley 1969, Plotkin-Power algebraic effects)

## Word count

Each page: **2000-3500 words**.

## Visual policy

- **Mermaid mandatory** per page.
- Optional Wikimedia images: skip unless you remember a real PL-related filename. Most foundational PL papers are pre-arxiv.
- Caption: `*Figure: <desc>. Image: [Wikimedia Commons](file-url), Author, License.*`

## Constraints

- Stay inside `docs/cs/programming-language-theory/`. Do not touch `_category_.json`.
- No paper titles in filenames.
- Mermaid special chars in `"..."`; internal `"` → `#quot;`.
- English. Match depth addendum.

## Output summary

```
Pages created: 1 intro + 8 detail = 9
Word counts per page
Figures: Wikimedia=W, Mermaid=M
References per page (avg)
```

Begin now.
