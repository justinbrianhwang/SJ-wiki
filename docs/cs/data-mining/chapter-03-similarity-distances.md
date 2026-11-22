---
title: Similarity and Distances
sidebar_position: 5
---

# Similarity and Distances

Similarity and distance functions define what it means for two data objects to be close. They are the hidden geometry behind nearest-neighbor search, clustering, outlier detection, information retrieval, graph mining, sequence matching, and many supervised learning methods. Aggarwal's treatment emphasizes that the right measure depends on the data type and on the analytical task, not on a universal formula.

This page bridges data preparation and algorithms. A feature matrix is not enough; an algorithm also needs a comparison rule. Numeric vectors often use $L_p$ distances, text often uses cosine similarity, sets often use Jaccard similarity, strings use edit distance, time series may use dynamic time warping, and graphs use topology-aware measures.

## Definitions

A **distance function** $d(X,Y)$ usually satisfies nonnegativity, identity, symmetry, and sometimes the triangle inequality:

$$
d(X,Y)\ge 0,\quad d(X,Y)=0 \Leftrightarrow X=Y,\quad d(X,Y)=d(Y,X).
$$

If the triangle inequality also holds, $d(X,Z)\le d(X,Y)+d(Y,Z)$, the distance is a metric.

The **$L_p$ distance** between numeric vectors $X=(x_1,\dots,x_d)$ and $Y=(y_1,\dots,y_d)$ is

$$
L_p(X,Y)=\left(\sum_{j=1}^{d}|x_j-y_j|^p\right)^{1/p}.
$$

Special cases include Manhattan distance $L_1$, Euclidean distance $L_2$, and maximum distance $L_\infty=\max_j \vert x_j-y_j\vert $.

**Cosine similarity** compares the angle between vectors:

$$
\cos(X,Y)=\frac{X\cdot Y}{\|X\|_2\|Y\|_2}.
$$

It is common for text because document length should not dominate topical similarity.

**Jaccard similarity** for sets $A$ and $B$ is

$$
J(A,B)=\frac{|A\cap B|}{|A\cup B|}.
$$

**Edit distance** is the minimum number or cost of insertions, deletions, and substitutions needed to transform one string into another.

**Dynamic time warping (DTW)** aligns two time series by allowing local stretching or compression of the time axis, then finds a minimum-cost alignment path.

## Key results

**High dimensionality weakens raw distances.** In many high-dimensional settings, nearest and farthest neighbor distances become similar relative to their scale. This makes naive distance-based clustering and outlier detection less discriminative. Feature selection, subspace methods, normalization, or domain-specific weights can restore useful contrast.

**Cosine and Euclidean distance are connected after normalization.** If $X$ and $Y$ are unit vectors, then

$$
\|X-Y\|_2^2=(X-Y)\cdot(X-Y)=2-2X\cdot Y=2(1-\cos(X,Y)).
$$

Thus ranking by cosine similarity is equivalent to ranking by Euclidean distance among length-normalized vectors.

**Jaccard ignores joint absences.** For sparse binary data, two users who both did not buy thousands of products should not be considered similar for that reason. Jaccard uses only present items in the union.

**Edit distance uses dynamic programming.** Let $D[i,j]$ be the edit distance between prefixes $a_1\dots a_i$ and $b_1\dots b_j$. Then

$$
D[i,j]=\min\begin{cases}
D[i-1,j]+1,\\
D[i,j-1]+1,\\
D[i-1,j-1]+\mathbf{1}[a_i\ne b_j].
\end{cases}
$$

**DTW also uses dynamic programming but over time indices.** It replaces exact time-to-time alignment with a path through a grid. This is useful when two series have the same pattern at different speeds, but it can also over-align unrelated noise without constraints.

**A similarity measure encodes an assumption about relevance.** Weighted distances, learned metrics, and supervised similarities are useful when different dimensions have different importance. For example, in a medical record, two lab measurements may be more relevant than ten administrative fields; in a recommender system, shared rare purchases may be more informative than shared popular purchases. Choosing the measure is therefore a modeling decision. Always ask whether large coordinate differences, matching categories, shared nonzero entries, order-preserving edits, or graph connectivity are the evidence the task should use.

**Indexing and computation are tied to the metric.** Some metric distances support tree indexes, pruning by triangle inequality, or locality-sensitive hashing. Other similarities, such as unrestricted edit distance, graph edit distance, or unconstrained DTW, can be expensive enough that approximate search becomes necessary. A mathematically attractive measure is not always operationally feasible on a large data set.

**Always inspect nearest-neighbor examples.** Before trusting a similarity function in a large mining task, take several representative objects and manually inspect their nearest neighbors. This simple check reveals scaling errors, accidental identifier leakage, stop-word domination in text, bad category encodings, and time-series alignments that look mathematically cheap but semantically wrong.

## Visual

| Data type | Measure | Formula or idea | Best when | Caution |
|---|---|---|---|---|
| Numeric vectors | $L_1$ | Sum absolute deviations | Robust coordinate differences | Still scale-sensitive |
| Numeric vectors | $L_2$ | Root sum of squares | Spherical clusters | Outlier-sensitive |
| Text vectors | Cosine | Angle between vectors | Length varies | Ignores term burst patterns |
| Sets | Jaccard | Intersection over union | Sparse binary presence | Ignores repeated counts |
| Strings | Edit distance | Minimum edits | Insert/delete/substitute errors | Cost model matters |
| Time series | DTW | Minimum warped alignment | Shifted or stretched patterns | Can overfit alignment |
| Graph nodes | Random-walk similarity | Similar paths/neighborhoods | Link structure matters | Computation can be expensive |

```text
DTW grid for two sequences X and Y

      Y1   Y2   Y3   Y4
X1   * -> * 
          | \ 
X2        * -> *
               |
X3             * -> *

The path is monotone: it can move right, down, or diagonal.
It may align one point in X with multiple nearby points in Y.
```

## Worked example 1: Comparing numeric and cosine distances

**Problem.** Compare $X=(1,2,0)$ and $Y=(2,1,0)$ using $L_1$, $L_2$, and cosine similarity.

**Method.**

1. Manhattan distance:

$$
L_1(X,Y)=|1-2|+|2-1|+|0-0|=1+1+0=2.
$$

2. Euclidean distance:

$$
L_2(X,Y)=\sqrt{(1-2)^2+(2-1)^2+0^2}=\sqrt{2}.
$$

3. Dot product:

$$
X\cdot Y=1\cdot2+2\cdot1+0\cdot0=4.
$$

4. Norms:

$$
\|X\|_2=\sqrt{1^2+2^2}=\sqrt{5},\quad
\|Y\|_2=\sqrt{2^2+1^2}=\sqrt{5}.
$$

5. Cosine similarity:

$$
\cos(X,Y)=\frac{4}{5}=0.8.
$$

**Checked answer.** The vectors are not identical, so $L_1=2$ and $L_2=\sqrt{2}$. They point in similar directions, so cosine similarity is high at $0.8$.

## Worked example 2: Edit distance with dynamic programming

**Problem.** Compute the edit distance between `cat` and `cut`, with insertion, deletion, and substitution cost 1.

**Method.**

1. Let rows be prefixes of `cat`: empty, `c`, `ca`, `cat`. Let columns be prefixes of `cut`: empty, `c`, `cu`, `cut`.

2. Initialize first row and column by prefix length:

   |  | empty | c | cu | cut |
   |---|---:|---:|---:|---:|
   | empty | 0 | 1 | 2 | 3 |
   | c | 1 |  |  |  |
   | ca | 2 |  |  |  |
   | cat | 3 |  |  |  |

3. Fill cells. For `c` vs `c`, substitution cost is 0, so $D[1,1]=0$.

4. For `ca` vs `cu`, compare:
   - delete: $D[1,2]+1=2$
   - insert: $D[2,1]+1=2$
   - substitute `a` to `u`: $D[1,1]+1=1$
   So $D[2,2]=1$.

5. For full `cat` vs `cut`, last characters `t` and `t` match:

$$
D[3,3]=D[2,2]+0=1.
$$

**Checked answer.** The distance is $1$, achieved by substituting `a` with `u`.

## Code

Pseudocode for edit distance:

```text
INPUT: strings a[1..m], b[1..n]
OUTPUT: edit distance D[m,n]

for i from 0 to m:
    D[i,0] = i
for j from 0 to n:
    D[0,j] = j
for i from 1 to m:
    for j from 1 to n:
        cost = 0 if a[i] == b[j] else 1
        D[i,j] = min(D[i-1,j] + 1,
                     D[i,j-1] + 1,
                     D[i-1,j-1] + cost)
return D[m,n]
```

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances

X = np.array([[1, 2, 0], [2, 1, 0], [0, 0, 5]], dtype=float)
print("euclidean")
print(np.round(pairwise_distances(X, metric="euclidean"), 3))
print("cosine similarity")
print(np.round(cosine_similarity(X), 3))

def edit_distance(a: str, b: str) -> int:
    d = np.zeros((len(a) + 1, len(b) + 1), dtype=int)
    d[:, 0] = np.arange(len(a) + 1)
    d[0, :] = np.arange(len(b) + 1)
    for i, ca in enumerate(a, start=1):
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + cost)
    return int(d[-1, -1])

print(edit_distance("cat", "cut"))
```

## Common pitfalls

- Using Euclidean distance on unscaled features with incompatible units.
- Treating cosine similarity as a metric in every setting; cosine distance variants need care.
- Counting joint zeros as evidence of similarity in sparse binary data.
- Applying DTW without a warping window and accidentally matching unrelated fluctuations.
- Using edit distance with equal operation costs when the domain has asymmetric costs.
- Forgetting that a supervised task may need a learned similarity, not a generic one.
- Assuming high-dimensional nearest neighbors are meaningful without checking distance contrast.

## Connections

- [Data Preparation](/cs/data-mining/chapter-02-data-preparation)
- [Feature Selection and Dimensionality Reduction](/cs/data-mining/chapter-02-feature-selection-dimensionality-reduction)
- [Cluster Analysis](/cs/data-mining/chapter-06-cluster-analysis)
- [Outlier Analysis](/cs/data-mining/chapter-08-outlier-analysis)
- [Mining Time Series Data](/cs/data-mining/chapter-14-mining-time-series-data)
- [Mining Graph Data](/cs/data-mining/chapter-17-mining-graph-data)
