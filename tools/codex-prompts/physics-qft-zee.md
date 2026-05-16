You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Quantum Field Theory in a NutshellZee.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/quantum-field-theory/`
- **SUBJECT**: Quantum Field Theory (A. Zee — *QFT in a Nutshell*)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **12-20 detail pages** covering Zee's scope (he organizes by "I.x", "II.x" etc):
   - Motivation (why fields, classical-to-quantum)
   - Path integral formulation
   - Feynman diagrams and perturbation theory
   - $\phi^4$ theory as a worked-through example
   - Renormalization (divergences, regularization, counterterms, running coupling)
   - Gauge invariance, QED
   - Symmetry breaking (spontaneous, Goldstone, Higgs)
   - Non-Abelian gauge theory (Yang–Mills, QCD)
   - Renormalization group
   - Anomalies (chiral)
   - Effective field theory
   - Condensed-matter applications (BEC, superconductivity, fractional Hall — whatever Zee includes)
   - Gravity & cosmology overview (final chapters)

3. Per-page: physical motivation → key Lagrangian → derivation sketch → Feynman rules where applicable → worked example.

4. LaTeX heavily. Diagrams in ASCII (`A——⌫——B`) or describe Feynman diagrams in text.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 30` for TOC. 3. Iterate sections; 1-2 pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
