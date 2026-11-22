---
title: Similarity and Distances
sidebar_position: 5
---

# Similarity and Distances

Similarity and distance functions define what it means for two data objects to be close. They are the hidden geometry behind nearest-neighbor search, clustering, outlier detection, information retrieval, graph mining, sequence matching, and many supervised learning methods. Aggarwal's treatment emphasizes that the right measure depends on the data type and on the analytical task, not on a universal formula.

A feature matrix alone does not specify how objects should be compared. Numeric vectors often use $L_p$ distances, text often uses cosine similarity, sets often use Jaccard similarity, strings use edit distance, time series may use dynamic time warping, and graphs use topology-aware measures.

## What a distance promises

A **distance function** $d(X,Y)$ usually satisfies nonnegativity, identity, symmetry, and sometimes the triangle inequality:

$$
d(X,Y)\ge 0,\quad d(X,Y)=0 \Leftrightarrow X=Y,\quad d(X,Y)=d(Y,X).
$$

If the triangle inequality also holds, $d(X,Z)\le d(X,Y)+d(Y,Z)$, the distance is a metric.

The axioms have algorithmic consequences. Symmetry permits storing one half of a pairwise matrix. Identity says distinct objects cannot be zero distance apart, although some useful **pseudometrics** relax it. The triangle inequality allows metric trees and branch-and-bound search to rule out candidates without comparing them directly.

A dissimilarity need not be a metric. Squared Euclidean distance violates the triangle inequality: for points $0,1,2$, the endpoints have dissimilarity $4$, larger than $1+1$. It is still useful as a loss. Conversely, a similarity is large when objects agree and generally has no fixed conversion to a metric. The transformation $1-s$ works for some normalized similarities but does not automatically satisfy the triangle inequality.

The **$L_p$ distance** between numeric vectors $X=(x_1,\dots,x_d)$ and $Y=(y_1,\dots,y_d)$ is

$$
L_p(X,Y)=\left(\sum_{j=1}^{d}|x_j-y_j|^p\right)^{1/p}.
$$

Special cases include Manhattan distance $L_1$, Euclidean distance $L_2$, and maximum distance $L_\infty=\max_j \vert x_j-y_j\vert $.

For $p\geq1$, Minkowski's inequality gives the triangle inequality. Values $0\lt p\lt 1$ emphasize sparse coordinate differences but do not define metrics. As $p$ grows, the largest coordinate difference dominates; the limit is $L_\infty$.

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

## Geometry changes in high dimension

**High dimensionality weakens raw distances.** In many high-dimensional settings, nearest and farthest neighbor distances become similar relative to their scale. This makes naive distance-based clustering and outlier detection less discriminative. Feature selection, subspace methods, normalization, or domain-specific weights can restore useful contrast.

One simple calculation shows the source of concentration. Suppose coordinates are independent with a finite mean and variance for the squared difference $Z_j=(X_j-Y_j)^2$. Then

$$
\|X-Y\|_2^2=\sum_{j=1}^d Z_j.
$$

Its mean grows like $d\operatorname{E}[Z_j]$, while its standard deviation grows like $\sqrt{d\operatorname{Var}(Z_j)}$. The coefficient of variation therefore shrinks as $1/\sqrt{d}$. Distances become large, yet their relative spread becomes small. Real features are not independent, so this is an illustration rather than a universal theorem, but it captures why adding noisy dimensions can make neighbor rankings fragile.

## Angles, sets, and sparse observations

**Cosine and Euclidean distance are connected after normalization.** If $X$ and $Y$ are unit vectors, then

$$
\|X-Y\|_2^2=(X-Y)\cdot(X-Y)=2-2X\cdot Y=2(1-\cos(X,Y)).
$$

Thus ranking by cosine similarity is equivalent to ranking by Euclidean distance among length-normalized vectors.

**Jaccard ignores joint absences.** For sparse binary data, two users who both did not buy thousands of products should not be considered similar for that reason. Jaccard uses only present items in the union.

For binary vectors, write $M_{11}$ for coordinates where both are one, and $M_{10},M_{01}$ for disagreements. Then

$$
J=\frac{M_{11}}{M_{11}+M_{10}+M_{01}}.
$$

The corresponding Jaccard distance $1-J$ is a metric on finite sets. If joint absence is meaningful, as it may be for diagnostic symptoms that were explicitly checked, simple matching or Hamming distance may be more appropriate.

Cosine similarity is undefined for the zero vector. Software libraries choose different conventions, often reporting zero similarity. That convention is operationally convenient but should not be interpreted as a measured angle.

## Covariance-aware and mixed-type distances

Standardized Euclidean distance treats each feature independently. When features are correlated, Mahalanobis distance uses a covariance matrix $\Sigma$:

$$
d_M(x,y)=\sqrt{(x-y)^\top\Sigma^{-1}(x-y)}.
$$

If $\Sigma=LL^\top$, transforming points by $L^{-1}$ whitens the covariance, and Mahalanobis distance becomes ordinary Euclidean distance in the whitened coordinates. Differences along a high-variance correlated direction count less; departures across the narrow direction of the data count more. The inverse is unstable when features are collinear or the sample is small relative to dimension. Shrinkage or a pseudoinverse may be needed.

Mixed tabular data cannot be handled honestly by assigning arbitrary integers to categories and applying Euclidean distance. Gower-style dissimilarity computes a per-feature contribution, normalizes numeric differences by a range, uses match or mismatch for nominal variables, and averages over observed comparable features. Feature weights can reflect reliability or domain importance. Range normalization remains sensitive to extreme observations, so robust ranges or fixed domain ranges may be preferable.

Missing features complicate pairwise comparison. Averaging only over coordinates observed for both objects keeps a score computable, but two pairs may then be judged on different evidence. A pair sharing one ordinary field can appear closer than a pair sharing twenty nearly matching fields. Recording the number and identity of comparable features alongside the distance helps, and a minimum-overlap rule can reject unsupported comparisons. Learned missingness penalties are appropriate only when absence itself carries stable meaning.

Asymmetric consequences can also make a symmetric metric inappropriate. Substituting a dangerous drug for a harmless one may have a different cost from the reverse decision, and recommending an already purchased item differs from failing to recommend a desired one. Such costs belong in a task loss or directed dissimilarity; forcing them into a metric can erase the direction the application cares about.

### Learning a distance from examples

When labeled pairs or triplets are available, metric learning can estimate which directions matter. A common linear form applies a positive semidefinite matrix to coordinate differences. Factoring that matrix produces a learned linear transformation followed by Euclidean distance. Similar pairs are pulled closer and dissimilar pairs are pushed apart according to a loss.

The supervision defines the geometry. If pairs are generated from product clicks, the learned space reflects exposure and clicking behavior, not an abstract notion of product similarity. False negative pairs are especially harmful: two relevant items may never have been observed together. Evaluation should use held-out entities or time periods so the transformation cannot memorize repeated objects.

Metric learning also does not repair a weak representation automatically. No coordinate weighting can recover word order after it was discarded or road barriers from bare latitude and longitude. Learned distances work best when the input retains the distinctions the task may need and the pair labels express the intended comparison.

## Alignment costs are models too

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

## Choosing the comparison rule

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

## Worked example 3: DTW by hand

**Problem.** Align $X=(1,2,2)$ and $Y=(1,1,2)$ with local cost $c(i,j)=\vert x_i-y_j\vert $. Use cumulative recurrence

$$
D[i,j]=c(i,j)+\min\{D[i-1,j],D[i,j-1],D[i-1,j-1]\},
$$

with $D[1,1]=c(1,1)$ and inaccessible cells outside the grid assigned infinity.

**Method.** The local-cost matrix is

| | $y_1=1$ | $y_2=1$ | $y_3=2$ |
|---|---:|---:|---:|
| $x_1=1$ | 0 | 0 | 1 |
| $x_2=2$ | 1 | 1 | 0 |
| $x_3=2$ | 1 | 1 | 0 |

Fill the cumulative matrix from the upper left:

1. First row: $D[1,1]=0$, $D[1,2]=0$, and $D[1,3]=1$.
2. First column: $D[2,1]=1$ and $D[3,1]=2$.
3. Interior entries are $D[2,2]=1+\min(0,1,0)=1$ and $D[2,3]=0+\min(1,1,0)=0$.
4. The last row gives $D[3,2]=1+\min(1,2,1)=2$ and $D[3,3]=0+\min(0,2,1)=0$.

The path $(1,1)\rightarrow(1,2)\rightarrow(2,3)\rightarrow(3,3)$ has total cost zero. It aligns the first value of $X$ with two ones in $Y$, then the two twos in $X$ with the final two in $Y$. Equal values at slightly different durations match exactly under this cost. A narrow warping window could forbid such a path if timing itself carries meaning.

## Implementing and checking distances

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

The edit-distance implementation stores the full matrix, using $O(mn)$ memory. If only the final distance is needed, the recurrence needs only the previous and current rows, reducing memory to $O(\min(m,n))$. Recovering the edit script requires backpointers or recomputation.

## Failure modes

- Using Euclidean distance on unscaled features with incompatible units.
- Treating cosine similarity as a metric in every setting; cosine distance variants need care.
- Counting joint zeros as evidence of similarity in sparse binary data.
- Applying DTW without a warping window and accidentally matching unrelated fluctuations.
- Using edit distance with equal operation costs when the domain has asymmetric costs.
- Forgetting that a supervised task may need a learned similarity, not a generic one.
- Assuming high-dimensional nearest neighbors are meaningful without checking distance contrast.
- Feeding missing values into a distance after replacing them with zero. Zero may be a real value, and pairs with more missing coordinates can appear spuriously close.
- Estimating a Mahalanobis covariance from the same tiny neighborhood being ranked. The inverse can amplify sampling noise and reorder neighbors arbitrarily.
- Comparing DTW totals across series of very different lengths without deciding whether total cost or path-normalized cost matches the task.

Distance choice should be evaluated through judgments the application actually needs. Retrieval can use labeled relevant pairs and metrics such as recall at $k$. Clustering can compare stability across resamples and inspect representatives. When labels are unavailable, controlled perturbations are useful: a small translation, harmless spelling variation, or time shift should change distance only if the task considers that change important.

<div className="see-also">

See also: [Data Preparation](/cs/data-mining/chapter-02-data-preparation) · [Feature Selection and Dimensionality Reduction](/cs/data-mining/chapter-02-feature-selection-dimensionality-reduction) · [Cluster Analysis](/cs/data-mining/chapter-06-cluster-analysis) · [Outlier Analysis](/cs/data-mining/chapter-08-outlier-analysis) · [Mining Time Series Data](/cs/data-mining/chapter-14-mining-time-series-data) · [Mining Graph Data](/cs/data-mining/chapter-17-mining-graph-data)

</div>
