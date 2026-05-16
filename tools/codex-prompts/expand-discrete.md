## EXPANSION PASS — SJ Wiki

You are running an **in-place expansion** of an existing wiki subtopic. The pages already exist; enrich them, **don't** rewrite.

## Inputs

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/math/discrete/`
- **SOURCE_PDF** (reference): `f:/coding/SJ Wiki/tmp/Kenneth Rosen - Discrete Mathematics and Its Applications-McGraw-Hill Higher Education (2018).pdf`
- **SUBJECT**: Discrete Mathematics

## What to do

1. List all `.md` files in TARGET_DIR (skip `_category_.json` and `intro.md`).
2. For each `.md` file:
   a. Read it.
   b. Apply the depth standard from the addendum: 1500-3500 words, mandatory visual, ≥2 worked examples, common-pitfalls, code where useful.
   c. **Preserve** frontmatter, filename, broad structure. Don't delete content unless wrong.
   d. **Expand**: add Visual / extra Worked example / Common pitfalls / Connections where missing. Lengthen thin sections.
   e. Use SOURCE_PDF for more examples (`pdftotext -f X -l Y`).

3. Do **not** modify `_category_.json`, filenames, slugs, or files outside TARGET_DIR.

4. Print a summary at the end.

## Visual ideas for discrete math pages

- **Propositional logic / Predicates**: truth tables (markdown table), Mermaid showing implication chains.
- **Proof techniques**: Mermaid decision tree (which proof method fits which goal).
- **Sets**: Venn-diagram-style ASCII, table of set-operation identities.
- **Functions / sequences / sums**: Mermaid showing function composition / injection / surjection.
- **Cardinality**: ASCII bijection sketch (e.g. $\mathbb{Z} \leftrightarrow \mathbb{N}$).
- **Algorithms / complexity**: complexity-class table; Mermaid flowchart of typical algorithm structures.
- **Number theory**: tables of GCD / modular arithmetic properties; Mermaid showing $a \bmod n$ partitioning.
- **Induction / Recursion**: Mermaid showing base case → inductive step → conclusion.
- **Recurrences**: comparison table of solution methods (characteristic eq, generating fn, master thm).
- **Counting**: comparison table (perm with/without rep, combinations, multinomial).
- **Probability**: tree diagrams in Mermaid for conditional probability / Bayes.
- **Relations / partial orders / equivalence**: Mermaid Hasse diagram example.
- **Graphs**: Mermaid actual graph examples (vertices + edges); adjacency-matrix table.
- **Trees**: Mermaid tree example; table of binary-tree traversal orders.
- **Boolean algebra / circuits**: Mermaid wiring diagrams for AND/OR/NOT, truth tables.
- **Finite-state machines**: Mermaid state diagram (`stateDiagram-v2`).

Use `python` for combinatorics, modular exponentiation, GCD, BFS/DFS, etc.

## Constraints

- Stay inside TARGET_DIR.
- No `npm`. English. Precise. Don't fabricate. Cross-links absolute.

Begin now.
