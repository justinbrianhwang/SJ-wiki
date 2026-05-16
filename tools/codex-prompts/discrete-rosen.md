You are an autonomous content author for **SJ Wiki**, a Docusaurus-based personal study site. Generate **detailed**, well-structured Markdown notes from the textbook below and write them directly into the wiki.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Kenneth Rosen - Discrete Mathematics and Its Applications-McGraw-Hill Higher Education (2018).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/discrete/`
- **SUBJECT**: Discrete Mathematics (from Rosen's *Discrete Mathematics and Its Applications*, 8th ed)

## Useful commands

```bash
pdfinfo "<pdf>"
pdftotext -l 20 "<pdf>" -
pdftotext -f <start> -l <end> "<pdf>" -
```

## What to produce

1. **`intro.md`** — replace the existing stub. 200-400 words. Numbered list of every page you create.

2. **One Markdown file per major topic.** kebab-case filenames. Cover Rosen's full scope:
   - Propositional logic & predicates
   - Proof techniques (direct, contrapositive, contradiction, induction)
   - Sets, relations, functions
   - Cardinality (countable / uncountable)
   - Algorithms & asymptotic complexity (basic)
   - Number theory (divisibility, modular arithmetic, primes, GCD, RSA)
   - Mathematical induction & recurrence relations
   - Counting (permutations, combinations, pigeonhole, inclusion-exclusion)
   - Discrete probability
   - Recurrences & generating functions
   - Relations (equivalence, partial orders)
   - Graphs (definitions, paths, connectivity, Euler/Hamilton)
   - Trees (spanning trees, traversals)
   - Boolean algebra & combinational logic

   Aim for **18-25 pages**, each 500-1500 words.

3. **Per-page format**:
   ```
   ---
   title: <Human Title>
   sidebar_position: <integer>
   ---

   # <Human Title>

   <intuition>

   ## Definitions

   ## Theorems & proofs

   ## Examples / problems

   ## Code

   <Python where useful — combinatorics, number theory, graph traversal>
   ```

4. **LaTeX math** — KaTeX-compatible. `$inline$`, `$$display$$`, `$$\begin{aligned}…\end{aligned}$$`.

5. **Code blocks** — Python preferred for algorithmic concepts (GCD, modexp, combinations, BFS/DFS).

## Workflow

1. `pdfinfo` to get page count.
2. `pdftotext -l 25` to read cover + TOC.
3. Iterate through chapters, reading page ranges and writing 1-3 wiki pages each.
4. Write `intro.md` last.
5. Print summary listing all files.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/math/discrete/`. Do not touch other folders, `_category_.json`, `docusaurus.config.ts`, `sidebars.ts`, `package.json`.
- Do not run `npm`.
- English. Mathematically precise.
- Don't fabricate.

Begin now.
