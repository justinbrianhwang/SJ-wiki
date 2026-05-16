## EXPANSION PASS — SJ Wiki

You are running an **in-place expansion** of an existing wiki subtopic. The pages already exist; enrich them, **don't** rewrite.

## Inputs

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/math/engineering-math/`
- **SOURCE_PDF** (reference): `f:/coding/SJ Wiki/tmp/Erwin Kreyszig _ Herbert Kreyszig_ Edward J. Norminton - Advanced engineering mathematics-Wiley (2011).pdf`
- **SUBJECT**: Advanced Engineering Mathematics

## What to do

1. List all `.md` files in TARGET_DIR (skip `_category_.json` and `intro.md`).
2. For each `.md` file:
   a. Read it.
   b. Apply the depth standard: 1500-3500 words, mandatory visual, ≥2 worked examples, common-pitfalls, code where useful.
   c. **Preserve** frontmatter, filename, broad structure.
   d. **Expand**: add Visual / extra Worked example / Common pitfalls / Connections where missing.
   e. Use SOURCE_PDF for more examples (`pdftotext -f X -l Y`).

3. Do **not** modify `_category_.json`, filenames, slugs, or files outside TARGET_DIR.

4. Print a summary at the end.

## Visual ideas for engineering math pages

- **ODEs (1st-order, 2nd-order)**: direction-field ASCII or table of method-selection (separable / linear / exact / Bernoulli); Mermaid flowchart of "which method does this ODE fit".
- **Laplace transform**: comparison table of standard transforms; Mermaid showing time ↔ s-domain mapping.
- **Fourier series / transform**: pictorial table of common signals and their spectra (ASCII).
- **PDEs (wave / heat / Laplace)**: Mermaid showing separation-of-variables steps; ASCII of typical boundary conditions.
- **Complex analysis**: ASCII of contour integration paths; table of residue formulas; Mermaid showing analytic ↔ Cauchy-Riemann ↔ contour-integral connections.
- **Vector calculus**: Mermaid relating grad/div/curl/Stokes/Gauss.
- **Numerical methods overview**: comparison table of methods (Euler / RK4 / Adams) with order/stability.

Use `python` (NumPy/SciPy) snippets where they make the method concrete.

## Constraints

- Stay inside TARGET_DIR.
- No `npm`. English. Precise. Don't fabricate. Cross-links absolute.

Begin now.
