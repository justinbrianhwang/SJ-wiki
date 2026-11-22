---
title: Bayesian Learning
sidebar_position: 7
---

# Bayesian Learning

Bayesian learning is both an algorithmic family and an analytical lens. Mitchell uses it to describe classifiers that explicitly compute probabilities, but also to explain why some non-Bayesian procedures can be interpreted as optimizing a probabilistic objective. This chapter links prior beliefs, observed data, likelihood, posterior probability, maximum a posteriori hypotheses, maximum likelihood hypotheses, and minimum description length.

Historically, this treatment is important because it places machine learning inside probability theory rather than only symbolic search or numerical optimization. Modern probabilistic modeling, Bayesian networks, topic models, Gaussian mixtures, and calibrated classifiers all build on the same foundations, even when implemented with newer algorithms.

## Definitions

Bayes' theorem states:

$$
P(h \mid D)=\frac{P(D \mid h)P(h)}{P(D)}.
$$

Here $h$ is a hypothesis and $D$ is observed data.

| Term | Meaning |
|---|---|
| $P(h)$ | Prior probability of hypothesis before observing $D$ |
| $P(D \mid h)$ | Likelihood of observing $D$ if $h$ were true |
| $P(D)$ | Evidence or marginal likelihood |
| $P(h \mid D)$ | Posterior probability after observing $D$ |

A maximum a posteriori hypothesis is:

$$
h_{MAP}=\arg\max_{h \in H} P(h \mid D).
$$

Because $P(D)$ is constant with respect to $h$:

$$
h_{MAP}=\arg\max_{h \in H} P(D \mid h)P(h).
$$

A maximum likelihood hypothesis is:

$$
h_{ML}=\arg\max_{h \in H} P(D \mid h).
$$

Maximum likelihood is the special case of MAP when all hypotheses have equal prior probability.

The Bayes optimal classifier predicts the class with greatest posterior probability after averaging across all hypotheses:

$$
v^*=\arg\max_{v_j \in V}\sum_{h_i \in H}P(v_j \mid h_i)P(h_i \mid D).
$$

The Gibbs algorithm samples one hypothesis from the posterior and uses it to classify. Mitchell presents it because, under suitable assumptions, it has an expected error at most twice that of the Bayes optimal classifier.

## Key results

Bayesian analysis clarifies concept learning. If the learner assumes deterministic, noise-free labels and assigns equal prior probability to each hypothesis, then all consistent hypotheses have equal posterior probability and all inconsistent hypotheses have posterior probability zero. Under those assumptions, the version space is precisely the set of hypotheses with nonzero posterior probability.

MAP and ML also connect to common loss functions. Suppose examples have real-valued targets and independent Gaussian noise with constant variance:

$$
t_i = h(x_i) + \epsilon_i,
\qquad
\epsilon_i \sim \mathcal{N}(0,\sigma^2).
$$

Maximizing likelihood is equivalent to minimizing sum of squared errors:

$$
\sum_i(t_i-h(x_i))^2.
$$

This gives a probabilistic justification for the squared-error objectives used with linear units and many neural-network examples.

For classification with Bernoulli outputs, maximizing likelihood leads to cross-entropy-style objectives. Mitchell's treatment anticipates modern logistic classification, although the notation and applications are smaller in scale.

Minimum description length (MDL) is another face of Bayesian preference. It chooses the hypothesis that gives the shortest combined encoding of the hypothesis and the data given the hypothesis:

$$
h_{MDL}=\arg\min_h \left[L(h)+L(D \mid h)\right].
$$

This connects Occam's razor to probability: simpler hypotheses are preferred when they compress the data well, not simply because they are short.

Bayesian learning also clarifies what it means to combine prior knowledge with data. The prior $P(h)$ can encode a preference for simpler hypotheses, smoother functions, smaller weights, known causal structures, or expert rules. The likelihood $P(D \mid h)$ measures how well each hypothesis predicts the observed evidence. A strong prior can dominate when data are scarce; abundant data can overwhelm a weak prior when the likelihood strongly favors another hypothesis.

The difference between MAP and Bayes optimal prediction is a difference between choosing and averaging. MAP chooses the single most probable hypothesis and predicts with it. Bayes optimal prediction averages over the posterior distribution of hypotheses. Averaging accounts for uncertainty, but it is often computationally expensive because it requires summing or integrating over many hypotheses. This is why MAP and approximations such as Gibbs sampling appear in practical discussions.

Mitchell's connection between likelihood and squared error is a recurring bridge across chapters. The LMS rule from Chapter 1 and the delta rule from Chapter 4 can be interpreted as optimizing a likelihood under Gaussian noise assumptions. This does not mean squared error is always right. It means each loss function carries an implicit noise model. Choosing a loss is partly choosing a belief about how targets are generated around the ideal function.

Bayesian classifiers also invite a distinction between decision making and probability estimation. A classifier may choose the right class even if its probabilities are poorly calibrated. Conversely, a well-calibrated model may sometimes choose the wrong class because the evidence is genuinely ambiguous. Mitchell's presentation of Bayes optimal classification focuses on minimizing expected classification error, but the posterior probabilities can also support decisions with unequal costs, such as medical screening where false negatives may be more expensive than false positives.

The assumption that the hypothesis space is known is another important simplification. In practice, model structure, features, and priors are designed by the engineer. A Bayesian calculation can be exact relative to those choices and still miss the real data-generating process. That is why the Bayesian view complements, rather than replaces, evaluation on held-out data.

This is also why Bayesian results in the book often serve two roles at once. They give algorithms for learners that explicitly manipulate probabilities, and they give explanations for why other algorithms behave sensibly under certain assumptions. Reading the chapter both ways helps connect symbolic consistency, squared-error training, probabilistic classification, and Occam-style simplicity.

## Visual

| Principle | Optimization form | Intuition | Mitchell connection |
|---|---|---|---|
| MAP | $\max_h P(D \mid h)P(h)$ | Fit data while respecting prior belief | Bayesian concept learning |
| ML | $\max_h P(D \mid h)$ | Choose the hypothesis that makes data most probable | Squared-error and likelihood derivations |
| Bayes optimal | Average predictions over all hypotheses | Use posterior uncertainty instead of one winner | Theoretical ideal classifier |
| Gibbs | Sample from posterior | Cheaper randomized approximation | Error bound relative to Bayes optimal |
| MDL | $\min_h L(h)+L(D \mid h)$ | Prefer concise total explanations | Occam-style bias and pruning |

## Worked example 1: Compute a MAP hypothesis

Problem: Two hypotheses can explain a dataset $D$.

| Hypothesis | Prior $P(h)$ | Likelihood $P(D \mid h)$ |
|---|---:|---:|
| $h_1$ | 0.70 | 0.20 |
| $h_2$ | 0.30 | 0.60 |

Find the MAP hypothesis and normalized posterior probabilities.

Method:

1. Compute unnormalized posterior scores.

$$
score(h_1)=P(D \mid h_1)P(h_1)=0.20(0.70)=0.14.
$$

$$
score(h_2)=P(D \mid h_2)P(h_2)=0.60(0.30)=0.18.
$$

2. Compute evidence by summing scores over the two hypotheses.

$$
P(D)=0.14+0.18=0.32.
$$

3. Normalize.

$$
P(h_1 \mid D)=0.14/0.32=0.4375.
$$

$$
P(h_2 \mid D)=0.18/0.32=0.5625.
$$

4. Choose the largest posterior.

$$
h_{MAP}=h_2.
$$

Answer: $h_2$ is the MAP hypothesis with posterior probability $0.5625$. The data favor $h_2$ enough to overcome its smaller prior.

## Worked example 2: Show why Gaussian noise gives squared error

Problem: Suppose $D=\{(x_i,t_i)\}_{i=1}^n$ and $t_i=h(x_i)+\epsilon_i$ with independent Gaussian noise $\epsilon_i \sim \mathcal{N}(0,\sigma^2)$. Show why maximizing likelihood is equivalent to minimizing squared error.

Method:

1. Write the likelihood for one example.

$$
P(t_i \mid h,x_i)=
\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\left(-\frac{(t_i-h(x_i))^2}{2\sigma^2}\right).
$$

2. Independence makes the full likelihood a product.

$$
P(D \mid h)=
\prod_{i=1}^n
\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\left(-\frac{(t_i-h(x_i))^2}{2\sigma^2}\right).
$$

3. Take log likelihood.

$$
\log P(D \mid h)
=
\sum_{i=1}^n
\left[
-\log\sqrt{2\pi\sigma^2}
-\frac{(t_i-h(x_i))^2}{2\sigma^2}
\right].
$$

4. Separate constants from the hypothesis-dependent part.

$$
\log P(D \mid h)
=
C
-
\frac{1}{2\sigma^2}
\sum_i(t_i-h(x_i))^2.
$$

5. Maximize the log likelihood.

   Since $C$ and $1/(2\sigma^2)$ do not depend on $h$, maximizing the expression is equivalent to minimizing:

$$
\sum_i(t_i-h(x_i))^2.
$$

Answer: Under independent constant-variance Gaussian noise, maximum likelihood learning is least-squares learning.

## Code

```python
import numpy as np

priors = np.array([0.70, 0.30])
likelihoods = np.array([0.20, 0.60])

scores = priors * likelihoods
posteriors = scores / scores.sum()
map_index = int(np.argmax(posteriors))

print("posterior probabilities:", posteriors)
print("MAP hypothesis:", f"h{map_index + 1}")
```

## Common pitfalls

- Confusing $P(h \mid D)$ with $P(D \mid h)$. The posterior and likelihood answer different questions.
- Dropping the prior without noticing. Maximum likelihood is not always appropriate when prior knowledge is meaningful.
- Treating the evidence $P(D)$ as irrelevant in all contexts. It is irrelevant for comparing fixed hypotheses by MAP, but important for normalized probabilities and model comparison.
- Saying "Bayesian" when only a point estimate is used. MAP is Bayesian in its objective, but it still returns one hypothesis.
- Interpreting MDL as "shortest hypothesis wins." MDL minimizes the code length of hypothesis plus remaining data, so an overly simple hypothesis can lose if it fails to explain the data.
- Assuming all posterior computations are tractable. Bayes optimal classification is often a theoretical standard rather than a practical algorithm.

## Connections

- [Concept learning](/cs/machine-learning/concept-learning-and-version-spaces)
- [Bayesian classifiers, networks, and EM](/cs/machine-learning/bayesian-classifiers-networks-and-em)
- [Evaluating hypotheses](/cs/machine-learning/evaluating-hypotheses)
- [Probability](/math/probability/)
- [Probability and random variables](/math/probability-and-random-variables/)
