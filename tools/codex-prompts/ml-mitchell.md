You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/MachineLearningTomMitchell.pdf` (Tom M. Mitchell — *Machine Learning*, McGraw-Hill 1997)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/machine-learning/`
- **SUBJECT**: Machine Learning (classic 1997 treatment by Tom Mitchell)

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview, note the historical position of Mitchell's text (pre-deep-learning era), numbered list of pages.

2. **12-16 detail pages** covering Mitchell's chapter scope:
   - Introduction to machine learning, the well-posed learning problem, design choices
   - Concept learning and the version space (FIND-S, candidate-elimination)
   - Decision tree learning (ID3, entropy, information gain, overfitting, pruning)
   - Artificial neural networks (perceptron, multilayer networks, backpropagation, hidden representations)
   - Evaluating hypotheses (sample error, confidence intervals, hypothesis comparison, paired t-test)
   - Bayesian learning (Bayes' theorem, MAP, ML, Bayes optimal classifier, Gibbs algorithm, Naive Bayes, Bayes nets, EM)
   - Computational learning theory (PAC learning, sample complexity, VC dimension, mistake bounds)
   - Instance-based learning (k-NN, locally weighted regression, radial basis functions, case-based reasoning)
   - Genetic algorithms (representation, fitness, schema theorem — brief)
   - Learning sets of rules (sequential covering, FOIL, inductive logic programming)
   - Analytical learning (explanation-based learning)
   - Combining inductive and analytical learning
   - Reinforcement learning intro (Q-learning, temporal-difference, links to MDP)

3. Per-page format (per addendum): 1500-3500 words, mandatory Mermaid diagram OR comparison table OR ASCII figure, ≥2 worked examples with full steps, common pitfalls, Python snippets where useful (with `numpy`, `scikit-learn` as appropriate — Mitchell's pseudocode is era-appropriate but you can translate).

4. **Frame the historical context** — Mitchell's book is foundational for many ideas now done very differently (decision trees still relevant; backprop is still backprop; PAC learning still teaches sample complexity rigorously). Where modern practice diverges substantially (e.g. neural network depth, GPU training), note it briefly but don't expand beyond Mitchell's scope.

5. Cross-link to:
   - `/cs/deep-learning/` (modern neural network treatment)
   - `/cs/reinforcement-learning/` (deeper RL coverage)
   - `/cs/data-mining/` (Aggarwal's pattern-mining perspective)
   - `/math/probability/` and `/math/probability-and-random-variables/` (Bayesian / probabilistic foundations)
   - `/math/statistics/` (hypothesis testing)

## Workflow

1. `pdfinfo "<pdf>"`, `pdftotext -l 25 "<pdf>" -` for cover + TOC.
2. Iterate chapters; 1 page per chapter (some chapters → 2 pages).
3. Write `intro.md` last.
4. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/machine-learning/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Match the depth addendum.
- Don't fabricate beyond Mitchell's content.

Begin now.
