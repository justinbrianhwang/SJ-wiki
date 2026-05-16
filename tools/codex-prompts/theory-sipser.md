You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Sipser_Introduction.to.the.Theory.of.Computation.3E.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/theory/`
- **SUBJECT**: Theory of Computation (Michael Sipser — 3rd ed)

## Produce

1. **`intro.md`** — replace the stub. Overview + chapter list.

2. **15-22 detail pages** covering Sipser's full scope:
   - Mathematical preliminaries (sets, sequences, functions, graphs, strings, languages, Boolean logic, types of proof)
   - Regular languages
     - Finite automata (DFA), formal definition, examples
     - Nondeterminism (NFA), equivalence to DFA, closure constructions
     - Regular expressions, GNFA conversion, equivalence to FA
     - Nonregular languages, pumping lemma
   - Context-free languages
     - Context-free grammars, derivations, parse trees, ambiguity
     - Chomsky normal form
     - Pushdown automata, equivalence with CFGs
     - Pumping lemma for CFLs, non-CFLs
     - Deterministic CFLs (brief)
   - The Church-Turing thesis
     - Turing machines (formal definition, configurations, languages)
     - Variants (multitape, nondeterministic, enumerators) and their equivalence
     - Algorithm, decidable problems for regular and context-free languages
   - Decidability
     - The halting problem and undecidability
     - Reductions, undecidable problems from language theory
   - Reducibility
     - Mapping reducibility, undecidability proofs
     - Recursion theorem (brief)
   - Time complexity
     - Big-O, classes P and NP, NP-completeness, SAT theorem, examples
     - Reductions among NP problems (CLIQUE, HAMPATH, SUBSETSUM, etc.)
   - Space complexity
     - PSPACE, NPSPACE, Savitch's theorem
     - L, NL, NL-completeness
   - Intractability & advanced topics (brief overviews)
     - Hierarchy theorems, oracles, randomized complexity, IP, PCP

3. Per-page format: definitions → key theorems with proofs / proof sketches → worked example (small machine or reduction) → connections.

4. Use **Mermaid `stateDiagram-v2`** for finite automata, PDA, and Turing machine examples wherever it clarifies a construction.

5. Use **transition tables** in markdown for DFA/NFA where helpful.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 30` for TOC. 3. Iterate chapters; 1-3 wiki pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Mathematically precise. Don't fabricate.

Begin now.
