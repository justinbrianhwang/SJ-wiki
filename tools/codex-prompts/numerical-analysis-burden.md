You are an autonomous content author for **SJ Wiki**. Generate **detailed**, well-structured Markdown notes from the textbook below and write them directly into the wiki.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/numerical analysis 9th, Richard L. Burden.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/numerical-analysis/`
- **SUBJECT**: Numerical Analysis (Burden & Faires, 9th ed)

## What to produce

1. **`intro.md`** — replace the stub. 200-400 words. Numbered list of all pages.

2. **One Markdown file per major topic.** kebab-case. Cover Burden's scope:
   - Mathematical preliminaries & error analysis (floating point, conditioning, stability)
   - Solutions of equations in one variable (bisection, fixed-point, Newton, secant, error analysis)
   - Interpolation & polynomial approximation (Lagrange, divided differences, Hermite, splines)
   - Numerical differentiation & integration (Newton-Cotes, Romberg, Gaussian quadrature, adaptive)
   - Initial-value problems for ODEs (Euler, Taylor, Runge-Kutta, multistep, stability, stiffness)
   - Direct methods for linear systems (Gaussian elimination, pivoting, LU)
   - Iterative methods for linear systems (Jacobi, Gauss-Seidel, SOR, conjugate gradient)
   - Approximation theory (least squares, Chebyshev, rational, trigonometric, FFT)
   - Eigenvalues (power method, Householder, QR algorithm)
   - Nonlinear systems
   - Boundary-value problems
   - Numerical PDEs (finite differences for parabolic/hyperbolic/elliptic)

   Aim for **18-25 pages**, each 500-1500 words.

3. **Per-page format**: intuition → algorithm → convergence/stability analysis → worked example → Python implementation.

4. **LaTeX math**, KaTeX-compatible. **Python/NumPy/SciPy code** is essential here — show actual implementations of the algorithms.

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 25` → TOC.
3. For each chapter, read its page range and write 1-3 wiki pages.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/math/numerical-analysis/`. Do not touch other folders, `_category_.json`, config files.
- Do not run `npm`.
- English. Mathematically precise.
- Don't fabricate.

Begin now.
