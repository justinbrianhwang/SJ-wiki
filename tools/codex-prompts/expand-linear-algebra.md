## EXPANSION PASS — SJ Wiki

You are running an **in-place expansion** of an existing wiki subtopic. The pages already exist; your job is to enrich them, **not** rewrite from scratch.

## Inputs

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/math/linear-algebra/`
- **SOURCE_PDF** (reference): `f:/coding/SJ Wiki/tmp/Howard Anton, Anton Kaul - Elementary Linear Algebra-Wiley (2019).pdf`
- **SUBJECT**: Linear Algebra

## What to do

1. List all `.md` files in TARGET_DIR (skip `_category_.json`).
2. For each `.md` file (skip `intro.md` — it's a TOC):
   a. Read the file.
   b. Apply the depth-requirement standard from the addendum: 1500-3500 words, mandatory visual (Mermaid/table/ASCII), ≥2 worked examples, common-pitfalls section, code where appropriate.
   c. **Preserve** existing frontmatter (`title`, `sidebar_position`), filename, and broad structure. Do **not** delete existing content unless wrong.
   d. **Expand in place**: insert Visual / additional Worked example / Common pitfalls / expanded Connections where missing. Lengthen thin sections — terse definitions, proof-free theorem statements, examples skipping steps.
   e. Reference SOURCE_PDF via `pdftotext -f X -l Y` when you need more examples or motivation.

3. Do **not** modify `_category_.json`, filenames, frontmatter slugs, or files outside TARGET_DIR.

4. Print a summary at the end.

## Visual ideas for linear algebra pages

- **Systems / Gaussian elimination**: ASCII block of an augmented matrix at each row-op step; flowchart of pivot-then-eliminate in Mermaid.
- **Matrix algebra**: table of properties (commutativity, distributivity, transpose, inverse, conjugate).
- **Determinants**: ASCII expansion-by-cofactors layout; table of row-operation effects on $\det$.
- **Vector spaces / bases**: Mermaid showing subspace containment (e.g. $\{0\} \subseteq \text{span}\{v\} \subseteq \mathbb{R}^n$).
- **Eigenvalues / diagonalization**: factorization diagram ($A = PDP^{-1}$) in Mermaid; comparison table of similar/diagonalizable/orthogonally-diagonalizable.
- **Orthogonality / QR / Gram-Schmidt**: ASCII illustration of projection; Mermaid pipeline showing $A \to Q,R$.
- **SVD**: $A = U\Sigma V^T$ block-matrix diagram (ASCII or Mermaid); table comparing eigendecomp vs SVD.

Use `python` + `numpy` snippets where they sharpen the concept.

## Constraints

- Stay inside TARGET_DIR.
- Do not run `npm`.
- English. Mathematically precise. Don't fabricate.
- Cross-links use absolute paths like `/math/linear-algebra/eigenvalues-and-eigenvectors`.

Begin now.
