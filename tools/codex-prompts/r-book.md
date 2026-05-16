You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/The_Book_of_R.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming/r/`
- **SUBJECT**: R (Tilman M. Davies — *The Book of R*)

## Produce

1. **`intro.md`** — replace the stub. Overview + chapter list.

2. **15-22 detail pages** covering The Book of R's scope:
   - R basics (interpreter, RStudio, packages, help, scripts)
   - Numeric and character vectors; arithmetic and comparison
   - Indexing, named vectors, recycling
   - Matrices and arrays
   - Lists and data frames
   - Factors and categorical data
   - Reading and writing data (CSV, Excel, RData)
   - Programming structures (if/else, for/while, functions, scoping)
   - Apply family (`apply`, `lapply`, `sapply`, `mapply`, `vapply`)
   - Probability distributions in R
   - Descriptive statistics
   - Plotting with base graphics
   - Plotting with `ggplot2`
   - Statistical inference (hypothesis tests, confidence intervals)
   - Linear models (`lm`)
   - Generalized linear models (`glm`) — brief
   - Object-oriented R (S3, S4 — brief)
   - The tidyverse overview (dplyr, tidyr, magrittr) — if covered

3. Per-page format: motivation → R code example with output → idiom notes → connections.

4. Use `r` language tag in fenced code blocks. Include realistic small datasets in examples (mtcars, iris, etc.).

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` for TOC. 3. Iterate chapters. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Don't fabricate.

Begin now.
