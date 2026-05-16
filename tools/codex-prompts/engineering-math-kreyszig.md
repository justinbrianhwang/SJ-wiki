You are an autonomous content author for **SJ Wiki**. Generate **detailed**, well-structured Markdown notes from the textbook below and write them directly into the wiki.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Erwin Kreyszig _ Herbert Kreyszig_ Edward J. Norminton - Advanced engineering mathematics-Wiley (2011).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/engineering-math/`
- **SUBJECT**: Advanced Engineering Mathematics (Kreyszig, 10th ed)

## Useful commands

```bash
pdfinfo "<pdf>"
pdftotext -l 25 "<pdf>" -
pdftotext -f <start> -l <end> "<pdf>" -
```

## What to produce

1. **`intro.md`** — replace the stub. 200-400 words. Numbered list of every page you create.

2. **One Markdown file per major topic.** kebab-case filenames. Cover Kreyszig's scope:
   - First-order ODEs (separable, linear, exact, integrating factors)
   - Second-order linear ODEs (homogeneous, nonhomogeneous, applications)
   - Higher-order ODEs & systems
   - Series solutions, special functions (Legendre, Bessel)
   - Laplace transform
   - Linear algebra refresher (matrices, eigenvalues — note this is duplicated with `/math/linear-algebra/` so be brief; cross-link)
   - Vector differential calculus (gradient, divergence, curl)
   - Vector integral calculus (line/surface integrals, Green/Stokes/divergence theorems)
   - Fourier series and integrals
   - Fourier transform
   - PDEs (wave, heat, Laplace) — separation of variables
   - Complex analysis (analytic functions, Cauchy integral theorem, residues)
   - Numerical methods overview (cross-link to `/math/numerical-analysis/`)

   Aim for **18-25 pages**, each 500-1500 words.

3. **Per-page format**: frontmatter (`title`, `sidebar_position`), intuition, definitions, key theorems/methods, worked examples, code where applicable (Python/SciPy), cross-links.

4. **LaTeX math** — KaTeX-compatible. Use `$$\begin{aligned}…\end{aligned}$$` for multi-line.

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 30` → cover + full TOC.
3. For each major chapter, read page range and write 1-3 wiki pages.
4. Write `intro.md` last.
5. Print summary of all files.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/math/engineering-math/`. Do not touch other folders, `_category_.json`, `docusaurus.config.ts`, `sidebars.ts`, `package.json`.
- Do not run `npm`.
- English. Mathematically precise.
- Don't fabricate.

Begin now.
