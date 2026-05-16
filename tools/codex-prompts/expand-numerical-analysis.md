## EXPANSION PASS — SJ Wiki

You are running an **in-place expansion** of an existing wiki subtopic. The pages already exist; enrich them, **don't** rewrite.

## Inputs

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/math/numerical-analysis/`
- **SOURCE_PDF** (reference): `f:/coding/SJ Wiki/tmp/numerical analysis 9th, Richard L. Burden.pdf`
- **SUBJECT**: Numerical Analysis

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

## Visual ideas for numerical analysis pages

- **Floating point / error**: number-line ASCII showing rounding gaps; table of conditioning vs stability properties.
- **Root finding (bisection / Newton / secant)**: Mermaid flowchart of iteration; convergence-rate comparison table.
- **Interpolation**: ASCII sketch of Lagrange vs spline behaviour; table of polynomial-interp error bounds.
- **Quadrature**: comparison table of Trapezoid / Simpson / Gauss with convergence orders.
- **ODE solvers (Euler / RK / multistep)**: stability-region ASCII; table of method order/stability/cost.
- **Linear systems (direct / iterative)**: Mermaid flow of LU vs Jacobi/GS/CG decision; table of complexities.
- **Approximation theory (LS / Chebyshev / FFT)**: comparison table.
- **Eigenvalue methods (power / Householder / QR)**: Mermaid pipeline showing reductions.

Heavy on **runnable Python** (NumPy/SciPy) implementations of each algorithm. Each page should have at least one full implementation, not a one-liner.

## Constraints

- Stay inside TARGET_DIR.
- No `npm`. English. Precise. Don't fabricate. Cross-links absolute.

Begin now.
