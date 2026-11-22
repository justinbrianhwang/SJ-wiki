---
title: Advanced Outlier Analysis
sidebar_position: 11
---

# Advanced Outlier Analysis

Advanced outlier analysis studies cases where ordinary numeric, full-dimensional, single-model anomaly detection is inadequate. Aggarwal's advanced chapter focuses on categorical data, high-dimensional outlier detection, ensembles, and applications. These settings are common in data mining: fraud records mix category codes, text vectors have thousands of sparse dimensions, and operational systems often need robust rankings rather than one brittle detector.

An anomaly may be hidden in a subspace, in an unusual categorical combination, or in disagreement among several detectors. Each case changes both the search problem and the explanation owed to a reviewer.

## Where full-dimensional numeric scores fail

**Categorical outlier detection** finds unusual combinations of symbolic attribute values. It often uses frequency, entropy, pattern rarity, or deviations from expected co-occurrence.

**High-dimensional outlier detection** seeks anomalies when the number of dimensions is large and raw distances lose contrast. Outliers may be visible only in a subset of dimensions.

**Subspace outlier** refers to an object that is anomalous in some feature subset even if it does not look anomalous in all dimensions together.

**Angle-based outlier detection** uses angles among points rather than distances, because angles can be more stable than distances in some high-dimensional settings.

**Outlier ensembles** combine multiple anomaly scores. Base detectors may vary by algorithm, feature subset, sample, parameter, or random seed.

**Isolation-based detection** ranks objects by how quickly random splits isolate them. Isolation forest builds an ensemble of such random trees; anomalies tend to require shorter paths.

## Categorical rarity needs a model

**Categorical rarity is combinatorial.** A single category value may be common, but its combination with other values may be rare. For example, country = US and device = desktop may both be common, but a specific browser-language-payment combination may be unusual.

Using the frequency of a complete tuple quickly becomes useless: with many attributes, nearly every tuple may occur once. A factorized model estimates

$$
P(x_1,\ldots,x_d)\approx\prod_{j=1}^dP(x_j),
$$

but misses dependencies. A conditional or graphical model can preserve selected dependencies, such as $P(\text{payment}\mid\text{country})$, without requiring counts for every complete combination. Association-rule approaches instead ask whether a record violates a frequent implication.

For a categorical variable with $m$ possible values, additive smoothing estimates

$$
\widehat{P}(x=v)=\frac{n_v+\alpha}{n+\alpha m}.
$$

With $\alpha\gt 0$, an unseen value no longer receives zero probability and infinite negative log score. The category universe must still be defined: a malformed code should not be silently accepted as an ordinary unseen category.

## Searching subspaces without manufacturing anomalies

**High-dimensional distance concentration hurts global detectors.** If all pairwise distances become similar, nearest-neighbor scores lose contrast. Subspace methods search for projections in which contrast reappears.

**Subspace search must be controlled.** The number of feature subsets is exponential in dimension. Practical methods use random subspaces, feature bagging, evolutionary search, sparse models, or domain-restricted subsets.

If all nonempty subsets were searched, there would be $2^d-1$ candidates. At $d=40$, that exceeds one trillion. Restricting subspace size reduces cost but also encodes a hypothesis about interaction order. Random subspaces trade exhaustive coverage for diversity; domain groups such as “network,” “billing,” and “device” features give more interpretable tests.

Angle-based methods exploit a different high-dimensional signal. For candidate $x$ and two other observations $y,z$, consider

$$
\cos\theta=
\frac{(y-x)^\top(z-x)}{\|y-x\|\,\|z-x\|}.
$$

An isolated point far outside a cloud sees most other points in similar directions, producing relatively consistent angles. A point inside the cloud sees points in many directions. Angle-based outlier factor formalizes this through a weighted variance of such angles. Computing all triples is expensive, so sampling or approximations are needed at scale.

Subspace scores also create a comparability problem. A two-dimensional score and a twenty-dimensional score need not have the same null distribution. Rank or empirical-tail normalization within each subspace is safer than taking a raw maximum.

## Isolation depth and its normalization

**Ensembles improve robustness when detectors fail differently.** A distance detector, density detector, isolation detector, and subspace detector may rank different objects highly. Combining normalized scores can reduce dependence on one fragile assumption.

**Isolation forest intuition.** Randomly choose a feature and a split value. Points in sparse or extreme regions are separated by fewer random splits. Average path length across many trees becomes an anomaly score.

Raw path length depends on sample size. Isolation forest compares the mean path $E[h(x)]$ with the expected unsuccessful-search depth of a random binary search tree. A standard normalizer is

$$
c(n)=2H_{n-1}-\frac{2(n-1)}{n},
$$

where $H_j=\sum_{i=1}^j1/i$ is a harmonic number. The score is commonly written

$$
s(x,n)=2^{-E[h(x)]/c(n)}.
$$

Short paths give scores nearer one; paths near the average normal depth give scores around one half. This normalization supports comparison within a fitted forest, not a universal probability of fraud or failure.

Feature subsampling helps diversify the trees, but irrelevant dimensions can still delay isolation because random splits waste chances on them. Categorical variables require a meaningful split representation; arbitrary integer codes impose false order.

## Combining detectors that fail differently

**Score normalization matters.** Combining raw scores from different detectors is meaningless if one detector outputs distances, another outputs negative log-likelihoods, and another outputs path lengths. Convert scores to ranks, quantiles, z-scores, or calibrated probabilities before aggregation.

**Subspace anomalies require evidence control.** In high dimensions, it is easy to find some projection where a point looks strange by chance. This is the anomaly-detection version of multiple testing. Candidate subspaces can be limited with domain knowledge, random feature bagging, minimum support requirements, or validation on known anomalies. The final explanation should name the feature subset that made the point unusual; otherwise reviewers cannot distinguish a meaningful subspace anomaly from a search artifact.

**Categorical anomaly scores need smoothing.** A combination not seen in historical data may have empirical probability zero, but that does not always mean impossible. New products, new countries, and new device types appear over time. Smoothing, hierarchical category grouping, and recency-aware baselines help avoid turning every new legitimate category into a severe alert.

**Ensemble disagreement is diagnostic.** If every detector ranks the same point highly, the anomaly is probably strong under several assumptions. If only one detector does, the point may reveal a specific structure: isolation forests like marginal separation, LOF likes local-density dips, and subspace detectors like feature-specific deviations. Reviewing the pattern of detector scores can therefore help explain why a case was flagged.

**Advanced anomaly detection should report why the case is reviewable now.** For streaming or operational data, a point may be unusual because it is new, because its frequency changed, because its combination of categories is rare, or because a local peer group shifted. The explanation should distinguish persistent rare behavior from sudden change; the response may be different.

**Maintenance matters.** Advanced detectors often depend on background frequencies, subspace samples, or ensemble components. These baselines should be refreshed on a controlled schedule so the model adapts without immediately normalizing every suspicious burst.

Average rank is robust to score units but loses information about the size of gaps. Quantile averaging retains only empirical position. Standardizing scores keeps magnitude but is sensitive to heavy tails. A maximum-rank ensemble catches anything any detector considers extreme and therefore raises false positives. The aggregation rule should match whether consensus or coverage is preferred.

Base diversity must be real. Ten isolation forests with adjacent random seeds may be less diverse than one isolation forest, one local-density method, and one categorical model. Pairwise rank correlation among component scores is a simple diagnostic. High agreement can be reassuring, but it also means the ensemble adds little robustness.

## A map of the advanced methods

```mermaid
flowchart TD
  A[Candidate anomaly] --> B{"Why hard?"}
  B -->|symbolic values| C[Categorical rarity and pattern deviation]
  B -->|many dimensions| D[Subspace or angle-based scoring]
  B -->|detector instability| E[Outlier ensemble]
  B -->|large mixed data| F[Isolation forest]
  C --> G[Normalized anomaly score]
  D --> G
  E --> G
  F --> G
  G --> H[Rank and review]
```

| Advanced setting | Useful idea | Example score | Main danger |
|---|---|---|---|
| Categorical | Rare combinations | Negative log frequency | Sparse data overflags rare but valid cases |
| High-dimensional | Subspace contrast | Max score over sampled subspaces | Multiple testing |
| Angle-based | Directional isolation | Variance of angles | Costly for large data |
| Ensemble | Combine detectors | Average rank | Poor normalization |
| Isolation | Random partition depth | Short path length | Needs enough trees |

## Worked example 1: Categorical combination rarity

**Problem.** A login table has three categorical attributes:

| record | country | device | hour_bucket |
|---:|---|---|---|
| 1 | US | desktop | day |
| 2 | US | desktop | day |
| 3 | US | mobile | day |
| 4 | US | desktop | night |
| 5 | FR | desktop | day |
| 6 | FR | mobile | night |

Score each record by negative log frequency of the full combination, using empirical probability.

**Method.**

1. Count full combinations:
   - (US, desktop, day): records 1 and 2 -> count 2.
   - (US, mobile, day): count 1.
   - (US, desktop, night): count 1.
   - (FR, desktop, day): count 1.
   - (FR, mobile, night): count 1.

2. Total records $n=6$. Probability for (US, desktop, day) is $2/6=1/3$.

3. Probability for each singleton combination is $1/6$.

4. Negative log score with natural log:

$$
-\log(1/3)=1.099,\quad -\log(1/6)=1.792.
$$

5. Records 3, 4, 5, and 6 tie as more unusual by full-combination frequency.

**Checked answer.** The rare full combinations receive higher scores. This does not prove they are malicious; it only says they are less frequent under this simple categorical model.

## Worked example 2: Isolation depth intuition

**Problem.** In one dimension, points are

$$
0.0,\ 0.1,\ 0.2,\ 0.3,\ 9.0.
$$

Explain why 9.0 is likely isolated quickly by random splits.

**Method.**

1. The data range is from 0.0 to 9.0.

2. A random split threshold between 0.3 and 9.0 immediately separates 9.0 from the four compact points.

3. The length of this interval is $9.0-0.3=8.7$, while the full split range is $9.0-0.0=9.0$.

4. The probability that a uniformly random threshold falls in $(0.3,9.0)$ is

$$
\frac{8.7}{9.0}=0.967.
$$

5. Therefore a single split isolates 9.0 with high probability. By contrast, isolating 0.1 from nearby points requires thresholds in narrow intervals such as $(0.0,0.1)$ and $(0.1,0.2)$ across multiple branches.

**Checked answer.** The point 9.0 has a short expected isolation path because it is separated by a large empty gap from the rest of the data.

## Worked example 3: rank aggregation

**Problem.** Three records $A,B,C$ receive anomaly scores from two detectors. Larger means more anomalous.

| record | detector 1 | detector 2 |
|---|---:|---:|
| A | 100 | 0.60 |
| B | 20 | 0.95 |
| C | 10 | 0.20 |

Average raw scores are meaningless because the scales differ. Convert each column to ascending quantile ranks using rank divided by three.

**Method.** Detector 1 orders $C\lt B\lt A$, so its quantiles are $1/3,2/3,1$. Detector 2 orders $C\lt A\lt B$, giving $1/3,2/3,1$ to $C,A,B$ respectively.

The ensemble values are

$$
q_A=\frac{1+2/3}{2}=\frac{5}{6},
$$

$$
q_B=\frac{2/3+1}{2}=\frac{5}{6},
\qquad
q_C=\frac{1/3+1/3}{2}=\frac{1}{3}.
$$

**Checked answer.** $A$ and $B$ tie at $5/6$, while $C$ ranks lower. The aggregation records that each of $A$ and $B$ is strongly supported by one detector and moderately supported by the other. With only three records, the quantiles are coarse; larger reference samples give finer ranks.

## Building a rank ensemble

Pseudocode for an outlier ensemble:

```text
INPUT: data X, base detectors A1..Am
OUTPUT: combined anomaly ranking

for each detector Aj:
    fit Aj on X
    compute raw anomaly scores sj
    convert sj to ranks or quantiles qj
combined_score = average of q1..qm
rank objects by combined_score descending
return ranking
```

```python
import numpy as np
from scipy.stats import rankdata
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

X = np.array(
    [
        [0.0, 0.0],
        [0.1, 0.0],
        [0.0, 0.2],
        [0.2, 0.1],
        [4.0, 4.0],
    ]
)

iso = IsolationForest(random_state=0, contamination=0.2)
iso_score = -iso.fit(X).score_samples(X)

lof = LocalOutlierFactor(n_neighbors=2)
lof.fit_predict(X)
lof_score = -lof.negative_outlier_factor_

def quantile_scores(scores):
    return rankdata(scores, method="average") / len(scores)

ensemble = (quantile_scores(iso_score) + quantile_scores(lof_score)) / 2
print("isolation:", np.round(iso_score, 3))
print("lof:", np.round(lof_score, 3))
print("ensemble:", np.round(ensemble, 3))
```

The example fits and scores the same five observations, which is suitable for illustrating unsupervised detection. For novelty detection, component estimators must support scoring new records, and the empirical rank transform must be defined against stored training-score distributions rather than reranking every incoming batch. Batch reranking would make a record's score depend on which other records happened to arrive beside it.

## Failure modes

- Treating rare categorical values as automatically anomalous without accounting for legitimate class imbalance.
- Searching many subspaces and reporting the best anomaly without correcting for chance discoveries.
- Averaging raw outlier scores from incompatible detectors.
- Assuming an ensemble is better when all base detectors use the same flawed distance measure.
- Using isolation forest contamination settings as ground truth rather than threshold choices.
- Ignoring explainability; anomaly reviewers often need the features or patterns that caused the flag.
- Evaluating only top-ranked examples and missing systematic false positives in protected or operationally sensitive groups.
- Taking the maximum over thousands of subspace scores without recording how many opportunities each record had to look unusual.
- Treating unseen categories caused by a schema change as behavioral anomalies rather than pipeline failures.
- Refreshing the baseline during an attack or outage so quickly that the abnormal regime becomes the new normal.

## Related pages

- [Outlier Analysis](/cs/data-mining/chapter-08-outlier-analysis)
- [Feature Selection and Dimensionality Reduction](/cs/data-mining/chapter-02-feature-selection-dimensionality-reduction)
- [Advanced Clustering Concepts](/cs/data-mining/chapter-07-advanced-clustering)
- [Mining Data Streams and Big Data](/cs/data-mining/chapter-12-mining-data-streams)
- [Mining Web Data and Recommenders](/cs/data-mining/chapter-18-mining-web-data)
