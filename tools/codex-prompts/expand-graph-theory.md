## EXPANSION PASS — SJ Wiki

You are running an **in-place expansion** of an existing wiki subtopic. The pages already exist; enrich them, **don't** rewrite.

## Inputs

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/math/graph-theory/`
- **SOURCE_PDF** (reference): `f:/coding/SJ Wiki/tmp/wilsongraph.pdf`
- **SUBJECT**: Graph Theory

## What to do

1. List all `.md` files in TARGET_DIR (skip `_category_.json` and `intro.md`).
2. For each `.md` file:
   a. Read it.
   b. Apply the depth standard: 1500-3500 words, mandatory visual, ≥2 worked examples, common-pitfalls, code where useful.
   c. **Preserve** frontmatter, filename, broad structure.
   d. **Expand**: add Visual / extra Worked example / Common pitfalls / Connections where missing.
   e. Use SOURCE_PDF for more examples.

3. Do **not** modify `_category_.json`, filenames, slugs, or files outside TARGET_DIR.

4. Print a summary at the end.

## Visual ideas for graph-theory pages

- **Every page should include at least one explicit Mermaid graph** showing the concept on a small example. This is a subject made for diagrams.

Examples:

- **Connectivity**: Mermaid graph with cut vertex / bridge highlighted.
- **Trees / spanning trees**: Mermaid tree; table comparing rooted vs unrooted.
- **Planarity**: ASCII sketch of $K_5$ and $K_{3,3}$ embeddings; table of planar properties (Euler $V-E+F=2$).
- **Colourings**: Mermaid graph with colours indicated in node labels; table of chromatic numbers for common families.
- **Matchings**: Mermaid bipartite graph showing augmenting path.
- **Flow networks**: Mermaid directed graph with capacities; table of flow / cut values.
- **Eulerian / Hamiltonian**: Mermaid example; table comparing conditions for existence.
- **Algebraic / spectral**: matrix display with table of adjacency-matrix properties.

Use `python` with `networkx` snippets when computation matters.

## Constraints

- Stay inside TARGET_DIR.
- No `npm`. English. Precise. Don't fabricate. Cross-links absolute.

Begin now.
