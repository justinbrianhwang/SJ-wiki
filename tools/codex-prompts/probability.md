You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for a probability section.

## Inputs

- **SOURCE_PDF** (supplementary, has probability chapters 5/7/9): `f:/coding/SJ Wiki/tmp/Online_Statistics_Education.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/probability/`
- **SUBJECT**: Probability and Random Variables

## Notes on sources

There is no dedicated probability textbook in the workspace. The Lane et al. *Online Statistics Education* book covers parts of probability (events, distributions, sampling distributions) but is not a full probability-theory text. Use it for the parts it covers (chapters 5, 7, 9), and complement with standard probability content that any rigorous introductory probability course would cover. Be careful not to fabricate citations to chapters the source doesn't have — when in doubt, present the topic as a standard probability result without naming a chapter.

**Coordinate with sibling sections:**

- `/math/statistics/` (Lane et al.) covers descriptive statistics, sampling distributions, inference, regression. The probability pages here should focus on **probability theory** rather than statistical inference. Where overlap is natural (Normal distribution, CLT), reference the statistics page rather than duplicate it.
- `/math/discrete/discrete-probability` (Rosen) covers discrete probability basics — these pages can go deeper into continuous probability and more theoretical material.

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview + numbered page list.

2. **12-16 detail pages** covering:
   - Sample spaces, events, and axioms of probability (Kolmogorov axioms)
   - Conditional probability, independence, and Bayes' theorem
   - Counting principles (permutations, combinations, multinomial) — keep brief, link to discrete page
   - Random variables and probability distributions (discrete + continuous, CDF, PMF, PDF)
   - Common discrete distributions (Bernoulli, Binomial, Geometric, Poisson, Hypergeometric, Negative binomial)
   - Common continuous distributions (Uniform, Exponential, Normal, Gamma, Beta, Chi-square, t, F)
   - Expectation, variance, moments
   - Joint, marginal, and conditional distributions
   - Covariance, correlation, and independence of random variables
   - Functions of random variables (transformations, change of variables)
   - Moment generating functions and characteristic functions (brief)
   - Limit theorems: Law of Large Numbers + Central Limit Theorem (cross-link to statistics)
   - Markov chains intro (states, transition matrices, stationary distributions)
   - Common pitfalls and intuition (Monty Hall, base-rate fallacy, prosecutor's fallacy)

3. Per-page format follows the depth addendum: 1500-3500 words, Mermaid diagram or table mandatory, ≥2 worked examples with full steps, Common pitfalls section, Python code (NumPy / SciPy.stats) where useful.

## Workflow

1. `pdfinfo "<pdf>"` and `pdftotext -l 20 "<pdf>" -` to see what Lane et al. covers for probability.
2. Write the 12-16 pages.
3. Write `intro.md` last.
4. Print summary.

## Constraints

- Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`, no touching `/math/statistics/` or `/math/discrete/`.
- English. Mathematically precise. KaTeX-compatible math (inline `$..$`, display `$$..$$`, multi-line `$$\begin{aligned}...\end{aligned}$$`).
- Cross-doc links use absolute paths.
- Don't fabricate book chapter citations beyond what the source actually contains.

Begin now.
