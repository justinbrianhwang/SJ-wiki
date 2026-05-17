---
title: Advanced Clustering Concepts
sidebar_position: 9
---

# Advanced Clustering Concepts

Advanced clustering deals with cases where the clean numeric, moderate-size, low-dimensional assumptions fail. Aggarwal discusses categorical data, scalable algorithms, high-dimensional and projected clustering, semi-supervised clustering, human or visual supervision, and cluster ensembles. The common theme is that the basic idea of grouping similar objects survives, but the representation, objective, and search strategy must change.

![A k-means animation shows centroids and cluster boundaries moving until assignments stabilize.](https://commons.wikimedia.org/wiki/Special:FilePath/K-means_convergence.gif)

*Figure: K-means alternates assignments and centroid updates until the partition stops changing. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:K-means_convergence.gif), Chire, CC BY-SA 4.0.*

This page extends the core clustering methods. It is especially important in data mining because real data often contain categorical attributes, millions of records, sparse text features, local subspace structure, partial labels, or multiple incompatible clusterings.

## Definitions

**Categorical clustering** groups records whose attributes are symbols rather than numeric values. Since arithmetic means are not defined, algorithms use modes, medoids, matching similarity, entropy, or probabilistic categorical models.

**k-modes** is the categorical analogue of k-means. It assigns objects to the nearest mode vector using a matching dissimilarity and updates each cluster representative by the most frequent category in each attribute.

**Scalable clustering** uses summaries, samples, indexes, streaming updates, or distributed computation to handle data too large for naive all-pairs methods.

**High-dimensional clustering** addresses the fact that different clusters may be visible in different feature subsets. A cluster may be tight in some dimensions and diffuse in others.

**Subspace clustering** finds clusters in subsets of dimensions. **Projected clustering** assigns each cluster its own relevant dimensions.

**Semi-supervised clustering** incorporates partial supervision such as must-link and cannot-link constraints.

A **cluster ensemble** combines multiple clusterings into a consensus clustering. The base clusterings may come from different algorithms, samples, parameters, or feature subsets.

## Key results

**Categorical representatives require different update rules.** For a cluster of categorical records, the mode in each attribute minimizes the number of mismatches within that attribute. This mirrors the way a mean minimizes squared numeric deviations.

**Scalability often comes from summarization.** BIRCH-like cluster feature summaries store counts, linear sums, and squared sums so centroids and radii can be updated without keeping all raw points. Stream clustering expands this idea with temporal summaries.

**High-dimensional clusters are often local.** A group of customers may be similar in purchase categories but not demographics; documents may cluster by politics in one term subset and by geography in another. Global distance across all features can hide these patterns.

**Semi-supervised constraints reshape the search.** A must-link constraint says two points should be in the same cluster; a cannot-link constraint says they should not. These constraints can be propagated carefully, but inconsistent constraints can make the problem impossible or force compromises.

**Cluster ensembles reduce instability.** If k-means is run many times with different initializations or feature samples, a co-association matrix can record how often each pair of objects is clustered together. Clustering that matrix can produce a more stable consensus.

**No-free-lunch principle for clustering.** There is no single best clustering definition. Compactness, separation, density, connectivity, interpretability, scalability, and constraint satisfaction can conflict.

**Advanced clustering often separates search from explanation.** A scalable or high-dimensional method may use random projections, summaries, subspace scoring, or ensemble matrices to find candidate groups. Afterward, the groups still need explanations in original terms: which categories define a k-modes cluster, which dimensions are relevant to a projected cluster, which constraints were binding in a semi-supervised solution, or which base clusterings agree in an ensemble. Without this second step, advanced methods can produce technically valid partitions that are hard to use.

**Categorical and mixed data deserve explicit distance design.** One-hot encoding lets numeric algorithms run, but it changes the geometry: a categorical attribute with many levels can dominate the distance simply because it creates many columns. Matching dissimilarity, Gower-style mixed measures, medoids, or separate treatment of numeric and categorical blocks may be more appropriate. The important test is whether the distance aligns with domain similarity, not whether it is convenient for a library call.

**Scalable clustering often gives approximate answers.** Sampling, summarization, and distributed updates reduce cost by discarding detail. That is acceptable when the approximation error is smaller than the noise or when the clusters are used for exploration, but it should be checked. Comparing summary-based clusters with a smaller exact run is a practical sanity test.

**Advanced clustering should preserve a route back to raw records.** Analysts usually need to inspect examples, diagnose errors, and explain why a group exists. Summary structures, subspace projections, and consensus matrices should therefore keep enough metadata to recover representative objects and important features for each discovered cluster.

## Visual

```mermaid
flowchart TB
  X["Point x_i in feature space"] --> Region["epsilon-neighborhood N_eps(x_i)"]
  Region --> Count{"|N_eps(x_i)| >= MinPts?"}
  Count -- "yes" --> Core["Core point: can expand a cluster"]
  Count -- "no, within eps of a core" --> Border["Border point: assigned but does not expand"]
  Count -- "no, not density-reachable" --> Noise["Noise/outlier"]

  Core --> Seed["Create or extend seed queue"]
  Seed --> Pop["Pop unvisited neighbor y"]
  Pop --> Visit{"Has y been visited?"}
  Visit -- "no" --> Query["Range query N_eps(y)"]
  Query --> IsCore{"|N_eps(y)| >= MinPts?"}
  IsCore -- "yes" --> Merge["Add y's neighbors to seed queue"]
  IsCore -- "no" --> Assign["Assign y as border if reachable"]
  Merge --> Pop
  Assign --> Pop
  Visit -- "yes" --> Pop
  Pop --> Done{"Seed queue empty?"}
  Done -- "no" --> Pop
  Done -- "yes" --> Cluster(("Density-connected cluster complete"))

  subgraph Scalable["Scalable and high-dimensional adaptations"]
    direction TB
    CF["BIRCH-style cluster features: N, LS, SS"]
    Subspace["Subspace/projected clustering: cluster-specific relevant dimensions"]
    Constraints["Must-link and cannot-link constraints"]
    Ensemble["Co-association matrix for cluster ensembles"]
  end

  Cluster -. "summaries or constraints can replace raw expansion in advanced settings" .-> Scalable
```

![DBSCAN core, border, and noise points — the figure shows core points around A, density-reachable border points B and C, and noise point N.](https://commons.wikimedia.org/wiki/Special:FilePath/DBSCAN-Illustration.svg)

*Figure: DBSCAN classifies points as core, border, or noise according to epsilon-neighborhood density and reachability. From [Chire, 2011](https://commons.wikimedia.org/wiki/File:DBSCAN-Illustration.svg) — CC BY-SA 3.0.*

This DBSCAN-centered diagram makes density reachability explicit. A point becomes core, border, or noise from the `epsilon` range query and `MinPts` count, and clusters grow by repeatedly expanding core-neighborhood seed queues. The scalable/high-dimensional side branch connects the same clustering problem to summaries, subspaces, constraints, and ensembles that the advanced chapter discusses.

| Challenge | Why basic k-means struggles | Typical adaptation |
|---|---|---|
| Categorical attributes | Mean is undefined | Modes, medoids, matching distance |
| Millions of points | Repeated full scans costly | Samples, summaries, distributed passes |
| High dimensions | Distances lose contrast | Feature selection, subspaces, projections |
| Partial supervision | Purely unsupervised objective ignores hints | Must-link/cannot-link constraints |
| Unstable results | Random starts produce different partitions | Ensembles and consensus clustering |
| Analyst knowledge | Objective misses semantic structure | Interactive or visual supervision |

## Worked example 1: One k-modes update

**Problem.** Cluster four categorical records by product preference and region:

| object | product | region |
|---:|---|---|
| 1 | phone | East |
| 2 | phone | East |
| 3 | laptop | West |
| 4 | phone | West |

Suppose cluster A contains objects 1, 2, and 4. Find its mode vector.

**Method.**

1. For the `product` attribute in cluster A:
   - phone appears in objects 1, 2, and 4 -> count 3.
   - laptop appears 0 times.
   The mode is phone.

2. For the `region` attribute:
   - East appears in objects 1 and 2 -> count 2.
   - West appears in object 4 -> count 1.
   The mode is East.

3. The cluster representative is therefore (phone, East).

4. Compute mismatches to the mode:
   - object 1: (phone, East) -> 0 mismatches.
   - object 2: (phone, East) -> 0 mismatches.
   - object 4: (phone, West) -> 1 mismatch.

5. Total within-cluster mismatch cost is 1.

**Checked answer.** The k-modes representative for cluster A is (phone, East). It minimizes the number of attribute mismatches within this cluster.

## Worked example 2: Consensus from two clusterings

**Problem.** Four objects A, B, C, D have two base clusterings:

$$
\Pi_1=\{\{A,B\},\{C,D\}\},\quad
\Pi_2=\{\{A,B,C\},\{D\}\}.
$$

Build the pairwise co-association scores.

**Method.**

1. List all unordered pairs: AB, AC, AD, BC, BD, CD.

2. In $\Pi_1$:
   - AB together -> 1
   - CD together -> 1
   - all other pairs -> 0

3. In $\Pi_2$:
   - AB together -> 1
   - AC together -> 1
   - BC together -> 1
   - pairs with D -> 0

4. Average over two clusterings:

   | pair | score |
   |---|---:|
   | AB | $(1+1)/2=1.0$ |
   | AC | $(0+1)/2=0.5$ |
   | AD | 0 |
   | BC | $(0+1)/2=0.5$ |
   | BD | 0 |
   | CD | $(1+0)/2=0.5$ |

5. A consensus method can treat $1-\text{score}$ as a distance and cluster this matrix.

**Checked answer.** AB is the most stable pair because it appears together in both base clusterings. Other positive pairs are less stable, and pairs involving A-D or B-D never co-occur.

## Code

Pseudocode for a cluster ensemble:

```text
INPUT: data X, base clustering procedure A, number of runs R
OUTPUT: consensus clustering

initialize co-association matrix M with zeros
for r from 1 to R:
    run A with a different sample, feature subset, or random seed
    for every pair of objects i, j:
        if i and j are in the same cluster:
            M[i,j] = M[i,j] + 1
divide M by R
cluster objects using distance 1 - M
return consensus clustering
```

```python
import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans

X = np.array([[0, 0], [0, 1], [4, 4], [4, 5], [8, 0]], dtype=float)
n = len(X)
runs = 10
coassoc = np.zeros((n, n))

for seed in range(runs):
    labels = KMeans(n_clusters=2, n_init=1, random_state=seed).fit_predict(X)
    for i in range(n):
        for j in range(n):
            coassoc[i, j] += labels[i] == labels[j]

coassoc /= runs
distance = 1 - coassoc
consensus = AgglomerativeClustering(
    n_clusters=2,
    metric="precomputed",
    linkage="average",
).fit_predict(distance)

print(np.round(coassoc, 2))
print(consensus)
```

## Common pitfalls

- Forcing categorical data into arbitrary integer codes and then using Euclidean distance.
- Believing a scalable summary is lossless; summaries are approximations unless proven otherwise.
- Searching all feature subspaces naively in high dimensions, which can become combinatorial.
- Treating must-link and cannot-link constraints as always correct; supervision can be noisy.
- Combining clusterings in an ensemble without diversity; identical base clusterings add little.
- Evaluating high-dimensional clusters only in full-dimensional distance.
- Assuming the most compact clustering is the most interpretable or useful one.

## Connections

- [Cluster Analysis](/cs/data-mining/chapter-06-cluster-analysis)
- [Feature Selection and Dimensionality Reduction](/cs/data-mining/chapter-02-feature-selection-dimensionality-reduction)
- [Mining Data Streams and Big Data](/cs/data-mining/chapter-12-mining-data-streams)
- [Mining Text Data](/cs/data-mining/chapter-13-mining-text-data)
- [Social Network Analysis](/cs/data-mining/chapter-19-social-network-analysis)
