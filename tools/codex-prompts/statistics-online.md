You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Online_Statistics_Education.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/statistics/`
- **SUBJECT**: Statistics (David M. Lane et al. — *Online Statistics Education: A Multimedia Course of Study*, or similar open textbook)

## Produce

1. **`intro.md`** — replace the stub. Identify the source book from the cover/TOC. Overview + chapter list.

2. **15-22 detail pages** covering typical intro-stats scope:
   - Statistical literacy: descriptive vs inferential, populations vs samples, variables, levels of measurement
   - Graphing distributions (histograms, box plots, bar charts, stem-and-leaf)
   - Summarizing distributions (mean, median, mode, variance, standard deviation, percentiles, z-scores, skewness, kurtosis)
   - Describing bivariate data (scatter plots, correlation, regression intuition)
   - Probability basics (events, conditional probability, Bayes, independence)
   - Random variables and probability distributions (Binomial, Poisson, Normal, t, chi-square, F)
   - Sampling distributions, Central Limit Theorem
   - Estimation (point estimates, confidence intervals)
   - Hypothesis testing (logic, p-values, errors, power)
   - Tests for means (one-sample, two-sample, paired, t-tests)
   - ANOVA (one-way, two-way)
   - Tests for proportions and chi-square tests of independence
   - Linear regression (least squares, inference on slope, prediction intervals, residual diagnostics)
   - Effect size and meta-analytic thinking
   - Nonparametric methods (sign test, Wilcoxon, Mann-Whitney) — brief
   - Resampling: bootstrap and permutation tests

3. Per-page format: definitions → formulas (KaTeX) → worked example with real-looking numbers → Python (NumPy / SciPy / statsmodels) snippet → pitfalls.

4. Tables for distribution properties; Mermaid for hypothesis-testing decision trees.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` for TOC. 3. Iterate chapters; 1-2 wiki pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Mathematically precise. Don't fabricate.

Begin now.
