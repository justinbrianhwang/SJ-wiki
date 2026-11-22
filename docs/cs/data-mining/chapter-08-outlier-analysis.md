---
title: Outlier Analysis
sidebar_position: 10
---

# Outlier Analysis

Outlier analysis finds objects that deviate strongly from the expected behavior of the data. Aggarwal treats it as a core data mining problem, parallel to clustering, classification, and association mining. The same unusual object can be a data error, a fraud signal, a rare medical case, a sensor fault, or an emerging event, so outlier analysis is tightly tied to the domain and the cost of false alarms.

The main detector families differ in their definition of normality: a central range, a probability distribution, a cluster structure, a neighborhood, or a compact description. The advanced treatment adds categorical, high-dimensional, and ensemble settings.

## Defining the reference population

An **outlier** is an object that differs significantly from most other objects under a chosen model of normality.

An **outlier score** is a numeric value where larger values usually mean more anomalous. A threshold turns scores into binary flags.

**Extreme value analysis** flags values that are unusually large or small in one or more numeric attributes.

**Probabilistic outlier detection** fits a probability model and treats low-probability objects as outliers. If $p(X)$ is small, then $X$ is surprising under the model.

**Clustering-based outlier detection** treats points far from cluster centers, in tiny clusters, or not assigned to any dense cluster as outliers.

**Distance-based outlier detection** uses nearest-neighbor distances. A common score is the distance to the $k$th nearest neighbor.

**Density-based outlier detection** compares local density around a point with local density around its neighbors. Local outlier factor (LOF) is the classic example.

**Information-theoretic outlier detection** asks which objects increase description length, entropy, or model complexity the most.

Point anomalies are individual unusual records. A **contextual anomaly** is unusual only given context, such as a temperature that is ordinary in July but remarkable in January. A **collective anomaly** is a group whose combined pattern is strange even if its members are ordinary; repeated small withdrawals or a sustained sensor oscillation are examples. Flattening context or sequence into independent rows can erase both kinds.

The reference population should also state its time and scope. Comparing a new server with all machines may flag a legitimate hardware class; comparing it only with peers of the same role may expose a real fault. Cohort definition often matters more than the scoring formula.

## Tail scores and robust scale

**Outlierness is model-relative.** There is no universal outlier without a reference population and a comparison rule. A high-income customer is normal in a luxury database and anomalous in a student-loan database.

**Global methods fail under varying density.** A point in a sparse but legitimate cluster may look far from neighbors compared with points in a dense cluster. Density-based local methods compare a point with its neighborhood rather than with the whole data set.

**Nearest-neighbor scores are simple and effective.** The $k$th nearest-neighbor distance grows when a point is isolated. However, all-pairs distance computation is expensive for large $n$, and the score depends on $k$ and the distance measure.

LOF reduces the penalty for belonging to a legitimately sparse region by comparing density locally. Let $d_k(o)$ be the distance from $o$ to its $k$th neighbor. The reachability distance from $p$ to neighbor $o$ is

$$
\operatorname{reach\_dist}_k(p,o)=\max\{d_k(o),d(p,o)\}.
$$

The maximum prevents extremely close pairs from producing arbitrarily high density. If $N_k(p)$ is the $k$-neighborhood, the local reachability density is the reciprocal of the mean reachability distance:

$$
\operatorname{lrd}_k(p)=
\left(
\frac{1}{|N_k(p)|}
\sum_{o\in N_k(p)}\operatorname{reach\_dist}_k(p,o)
\right)^{-1}.
$$

Finally,

$$
LOF_k(p)=
\frac{1}{|N_k(p)|}
\sum_{o\in N_k(p)}
\frac{\operatorname{lrd}_k(o)}{\operatorname{lrd}_k(p)}.
$$

A score near one means density comparable to neighbors. A value substantially above one means the point is locally sparser. LOF values depend on $k$ and ties, and they are not probabilities.

**Clustering and outlier detection are linked but not identical.** Clustering tries to summarize major groups; outlier detection focuses on residual or rare behavior. A clustering algorithm that forces every point into a cluster may hide outliers unless distances, cluster sizes, or assignment probabilities are inspected.

**Statistical thresholds require assumptions.** A z-score threshold such as $\vert z\vert \gt 3$ assumes a meaningful mean and standard deviation, often a roughly normal central distribution, and enough data to estimate scale. Heavy-tailed data can produce many large z-scores without actual anomalies.

The median absolute deviation is a common robust scale estimate:

$$
MAD=\operatorname{median}_i|x_i-\operatorname{median}(x)|.
$$

For normally distributed data, $1.4826\,MAD$ estimates the standard deviation. A robust standardized score is therefore

$$
z_i^{(r)}=\frac{x_i-m}{1.4826\,MAD},
$$

where $m$ is the median. The median and MAD have a 50 percent breakdown point: fewer than half the observations can move them only so far, unlike mean and standard deviation. If $MAD=0$, which occurs with many repeated values, the formula is undefined and a domain tolerance or another quantile-based scale is needed.

Probability density and tail probability should not be confused. A value can have low density merely because units spread probability over a large region. For a well-specified univariate continuous distribution, a two-sided tail probability directly measures how extreme a value is. In several dimensions there is no unique ordering of more extreme, so likelihood level sets or model-specific scores are used.

## Neighbor and density scores

**Validity is difficult.** Labels for anomalies are often rare or delayed. Analysts may evaluate precision at top $k$, stability under parameter changes, domain review, injected anomalies, or downstream cost.

**Outlier analysis is usually a ranking problem before it is a labeling problem.** In many applications there is no natural threshold that separates normal from abnormal. Investigators review the top 10, top 100, or top 1 percent of cases subject to staffing and cost constraints. This means score calibration, ranking stability, and explanation can matter more than a binary decision. A detector that gives slightly worse global separation but clearer reasons for the top alerts may be better operationally.

**The reference set must represent normal behavior.** If the training data mix several regimes, a model may flag legitimate minority behavior. If the training data contain many anomalies, a density or clustering method may absorb them as normal. Time-based systems also need to account for drift: yesterday's unusual traffic may become today's normal pattern after a product launch or seasonal event.

**Explanation should be designed with the detector.** A z-score points to a feature, a nearest-neighbor score can point to missing neighbors, a clustering residual can point to the closest centroid, and a density method can compare local neighborhoods. If a detector only outputs a score, investigators may not know whether to trust or act on it. In applied mining, anomaly explanation is often as important as anomaly ranking.

**Outlier feedback can improve the data pipeline.** Reviewed anomalies often reveal upstream issues such as unit conversion mistakes, duplicate accounts, broken sensors, bot traffic, or changed logging formats. Those discoveries should feed back into cleaning and monitoring rules. In this sense, outlier detection is both an analysis method and a data-quality diagnostic.

Multiple anomalies can interfere with one another. **Masking** occurs when a group of unusual observations forms its own apparent cluster or inflates the estimated scale, causing its members to look normal. **Swamping** occurs when genuine normal observations are flagged because contaminated estimates shift the center or boundary. Robust fitting, iterative review, and evaluation with groups of injected anomalies are more revealing than testing only one isolated extreme point. Removing the top alert and refitting can uncover a second layer, but repeated removal also risks manufacturing anomalies from an originally coherent minority group.

The assumed contamination rate belongs to thresholding, not to the definition of truth. Asking a library for exactly one percent outliers guarantees one percent of labels even when the batch is clean or experiencing a major incident. Fixed review capacity may justify that queue size, but reports should distinguish capacity-based flags from evidence about prevalence.

**Thresholds should be revisited after review.** Once analysts label some alerts as useful or useless, the threshold can be tuned to match observed workload and precision. Static thresholds chosen before review are rarely optimal.

## From scores to an investigation queue

```mermaid
flowchart TD
  A[Data objects] --> B{Normality model}
  B -->|single feature tail| C[Extreme value]
  B -->|probability density| D[Low likelihood]
  B -->|cluster structure| E[Small cluster or far from center]
  B -->|neighbor distance| F[kNN distance]
  B -->|local density| G[LOF-style score]
  B -->|compression| H[Description length impact]
  C --> I[Rank outliers]
  D --> I
  E --> I
  F --> I
  G --> I
  H --> I
```

| Method | Score idea | Good for | Main risk |
|---|---|---|---|
| z-score | Distance from mean in standard deviations | Simple numeric tails | Heavy tails, skew |
| Gaussian likelihood | Low fitted probability | Elliptical normal data | Model misspecification |
| kNN distance | Far from $k$ neighbors | Generic metric data | Expensive and density-sensitive |
| LOF | Less dense than neighbors | Varying local density | Parameter sensitivity |
| Clustering residual | Far from centroid or tiny cluster | Clustered normal behavior | Forced assignments |
| Information-theoretic | Increases encoding cost | Pattern-based anomalies | Harder to explain simply |

If investigators can review $B$ records per day, the operational threshold is often the score of the $B$th ranked record. Precision at $B$ estimates the useful fraction of that queue:

$$
\operatorname{Precision@}B
=\frac{\text{confirmed anomalies among top }B}{B}.
$$

Recall may be unknowable because undiscovered anomalies have no labels. When delayed outcomes eventually identify cases, use a time-respecting evaluation: train on earlier data, rank later data, and wait for labels. Random splits can leak repeated entities or future regimes.

Injected anomalies test whether a detector can find the kind of corruption used for injection; they do not establish performance on unknown real anomalies. Synthetic evaluation is most informative when perturbations follow plausible failure processes, such as unit multiplication, duplicated events, or impossible transitions.

## Worked example 1: z-scores and robust suspicion

**Problem.** A sensor reports values:

$$
10,\ 11,\ 10,\ 12,\ 11,\ 100.
$$

Use mean and standard deviation to compute a z-score for 100. Then discuss the limitation.

**Method.**

1. Compute the mean:

$$
\mu=\frac{10+11+10+12+11+100}{6}=\frac{154}{6}=25.667.
$$

2. Compute squared deviations:

$$
(10-25.667)^2=245.44,\quad
(11-25.667)^2=215.11,\quad
(10-25.667)^2=245.44,
$$

$$
(12-25.667)^2=186.78,\quad
(11-25.667)^2=215.11,\quad
(100-25.667)^2=5525.44.
$$

3. Population variance:

$$
\sigma^2=\frac{6633.33}{6}=1105.56,\quad \sigma=33.25.
$$

4. z-score for 100:

$$
z=\frac{100-25.667}{33.25}=2.24.
$$

**Checked answer.** The z-score is only about 2.24 because the extreme value inflated both the mean and standard deviation. A robust median-based view would compare 100 with median 11 and identify it more clearly as unusual.

Continue the calculation with MAD. The median is $(11+11)/2=11$. Absolute deviations are $1,0,1,1,0,89$, whose median is $(1+1)/2=1$. Thus the normal-consistent robust scale is $1.4826$, and

$$
z_{100}^{(r)}=\frac{100-11}{1.4826}\approx60.03.
$$

The number should not be read as an exact Gaussian tail claim: the sample is tiny. It shows that the central five observations agree on a scale near one while the classical scale estimate is dominated by 100.

## Worked example 2: k-nearest-neighbor outlier score

**Problem.** For one-dimensional points

$$
0,\ 1,\ 2,\ 10,
$$

compute the $k=2$ nearest-neighbor distance score for each point.

**Method.**

1. Point 0 distances to others: 1, 2, 10. The 2nd nearest distance is 2.
2. Point 1 distances: 1 to 0, 1 to 2, 9 to 10. The 2nd nearest distance is 1.
3. Point 2 distances: 2 to 0, 1 to 1, 8 to 10. Sorted: 1,2,8. The 2nd nearest distance is 2.
4. Point 10 distances: 10 to 0, 9 to 1, 8 to 2. Sorted: 8,9,10. The 2nd nearest distance is 9.

**Checked answer.** The kNN outlier scores are:

| point | score |
|---:|---:|
| 0 | 2 |
| 1 | 1 |
| 2 | 2 |
| 10 | 9 |

Point 10 is the strongest outlier by this score.

## Worked example 3: a local density ratio

**Problem.** Suppose point $p$ has two neighbors $a,b$. Their local reachability densities are $2.0$ and $2.4$, while $p$ has density $0.8$. Compute $LOF_2(p)$.

**Method.** Compare each neighbor density with that of $p$:

$$
\frac{\operatorname{lrd}(a)}{\operatorname{lrd}(p)}
=\frac{2.0}{0.8}=2.5,
$$

$$
\frac{\operatorname{lrd}(b)}{\operatorname{lrd}(p)}
=\frac{2.4}{0.8}=3.0.
$$

Average the ratios:

$$
LOF_2(p)=\frac{2.5+3.0}{2}=2.75.
$$

**Checked answer.** Point $p$ is about 2.75 times less dense than its local comparison neighborhood under these supplied density estimates. The value supports ranking $p$ highly, but it does not supply a calibrated probability or universal cutoff.

## Computing neighbor scores

Pseudocode for kNN outlier scoring:

```text
INPUT: data X, neighbor count k
OUTPUT: outlier scores s

for each point Xi:
    distances = empty list
    for each point Xj where j != i:
        add distance(Xi, Xj) to distances
    sort distances
    s[i] = distances[k]
rank points by descending s
return s
```

```python
import numpy as np
from sklearn.neighbors import NearestNeighbors, LocalOutlierFactor

X = np.array([[0.0], [1.0], [2.0], [10.0]])

nn = NearestNeighbors(n_neighbors=3)  # includes the point itself
nn.fit(X)
distances, indices = nn.kneighbors(X)
k2_scores = distances[:, 2]
print("2NN distance scores:", k2_scores)

lof = LocalOutlierFactor(n_neighbors=2)
labels = lof.fit_predict(X)
scores = -lof.negative_outlier_factor_
print("LOF labels:", labels)
print("LOF-style scores:", np.round(scores, 3))
```

The `NearestNeighbors` call requests three returned neighbors because a training point is its own nearest neighbor at distance zero. In novelty detection on new points, self-inclusion does not occur, so the requested count and indexing change. LOF also has separate modes for labeling the training sample and scoring genuinely new observations; mixing them leads to off-by-one neighborhoods or unsupported method calls.

## Failure modes

- Calling every rare point an error rather than checking domain meaning.
- Using z-scores blindly on skewed or heavy-tailed data.
- Choosing a distance measure that is inappropriate for mixed, categorical, text, or graph data.
- Evaluating outlier methods only by how many points they flag, not by precision or usefulness.
- Letting a clustering algorithm force anomalous points into normal clusters without inspecting residuals.
- Ignoring parameter sensitivity in $k$, $\epsilon$, or contamination rate.
- Training an outlier detector on data that already contains many anomalies without robust methods.
- Reporting an anomaly rate chosen by a library's default contamination setting as if it were discovered from the data.
- Letting the same entity appear many times in a reference set. Its duplicates create an artificial dense neighborhood and can mask coordinated abuse.
- Ignoring exposure. A customer with ten failed requests may be unusual at ten total requests and ordinary at a million.

<div className="see-also">

See also: [Advanced Outlier Analysis](/cs/data-mining/chapter-09-advanced-outlier-analysis) · [Similarity and Distances](/cs/data-mining/chapter-03-similarity-distances) · [Cluster Analysis](/cs/data-mining/chapter-06-cluster-analysis) · [Mining Data Streams and Big Data](/cs/data-mining/chapter-12-mining-data-streams) · [Mining Time Series Data](/cs/data-mining/chapter-14-mining-time-series-data)

</div>
