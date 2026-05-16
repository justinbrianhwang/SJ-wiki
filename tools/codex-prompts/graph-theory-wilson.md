You are an autonomous content author for **SJ Wiki**. Generate **detailed**, well-structured Markdown notes from the textbook below and write them directly into the wiki.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/wilsongraph.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/graph-theory/`
- **SUBJECT**: Graph Theory (Robin J. Wilson — *Introduction to Graph Theory*)

## What to produce

1. **`intro.md`** — replace the stub. 200-400 words. Numbered list of all pages.

2. **One Markdown file per major topic.** kebab-case. Cover Wilson's full scope:
   - Definitions & terminology (graphs, multigraphs, digraphs, walks/paths/cycles)
   - Connectedness, components
   - Trees (spanning trees, prüfer sequences, counting trees)
   - Planarity (Kuratowski's theorem, planar duality, Euler's formula)
   - Colourings (chromatic number, four-colour theorem, edge colouring)
   - Matchings (Hall's theorem, augmenting paths, König's theorem)
   - Hamiltonian and Eulerian graphs
   - Network flows (max-flow min-cut)
   - Ramsey theory (basic)
   - Algebraic graph theory (adjacency matrix, spectral)
   - Random graphs (Erdős–Rényi basics)

   Aim for **12-20 pages**, each 500-1500 words.

3. **Per-page format**: intuition → definitions → theorems with proofs → worked examples → algorithmic implementation (Python with `networkx` or vanilla) where relevant.

4. **LaTeX math**. **Diagrams** in Mermaid where simple (`graph LR; A --- B; B --- C`).

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 20` → TOC.
3. For each chapter, read its page range and write 1-3 wiki pages.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/math/graph-theory/`. Do not touch other folders, `_category_.json`, config files.
- Do not run `npm`.
- English. Mathematically precise.
- Don't fabricate.

Begin now.
