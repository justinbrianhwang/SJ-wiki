---
title: Tensors and Data Preprocessing
sidebar_position: 2
---

# Tensors and Data Preprocessing

Deep learning starts with two practical skills: representing data as tensors and making raw data numerically usable. D2L begins here because every later model, from linear regression to transformers, is ultimately a composition of tensor operations. A network can look mysterious at the architectural level, but at runtime it mostly consumes batches of arrays, applies broadcasted arithmetic, multiplies matrices, and moves intermediate results through differentiable operators.

Data preprocessing matters just as much as the model definition. Missing values, mixed numeric and categorical columns, inconsistent scales, and accidental train-test leakage can dominate the result before optimization even begins. A disciplined tensor pipeline keeps shapes explicit, keeps statistical estimates tied to the training split, and makes each minibatch look like what the model expects.

## Definitions

A **tensor** is a multidimensional array with a shape, a data type, and usually a device. In PyTorch, a scalar has shape `()`, a vector has shape `(d,)`, a matrix has shape `(m, n)`, and a minibatch of color images often has shape `(batch, channels, height, width)`.

Let $X \in \mathbb{R}^{n \times d}$ be a tabular feature matrix. The row $x_i$ is the feature vector for example $i$, and a target vector $y \in \mathbb{R}^n$ stores one label or response per row. In image tasks, one row is no longer enough to describe an example, so an input batch may be $X \in \mathbb{R}^{n \times c \times h \times w}$.

**Broadcasting** is a rule for applying elementwise operations to tensors whose shapes differ but are compatible. Starting from trailing dimensions, two dimensions are compatible when they are equal or when one of them is $1$. A dimension of size $1$ can be repeated conceptually without copying data.

**Indexing and slicing** select subtensors. A slice such as `X[:, 1:3]` means all rows and columns with indices `1` and `2`. In-place updates such as `X[:, 0] = 0` modify storage and can save memory, but they must be used carefully when autograd needs previous values.

**Data preprocessing** turns raw records into tensors. Common steps include parsing files, separating features from labels, imputing missing numeric values, encoding categorical values, standardizing numeric features, shuffling examples, and grouping them into minibatches.

**One-hot encoding** maps a categorical variable with $k$ possible categories to a vector in $\{0,1\}^k$. This lets a linear model or neural network receive category identity without imposing an artificial numeric order.

## Key results

The most important tensor result is that shape reasoning is an invariant. If an operation is valid for a single example but not for a minibatch, it is usually not written in the right vectorized form. For example, a linear model with weights $w \in \mathbb{R}^d$ and bias $b$ should compute all predictions as

$$
\hat{y} = Xw + b,
$$

where $X \in \mathbb{R}^{n \times d}$ and broadcasting expands the scalar $b$ across all $n$ rows.

Vectorization replaces Python loops with library kernels. If $X$ has $n$ rows, a loop that computes `torch.dot(X[i], w)` repeatedly launches many small operations. The expression `X @ w` launches a single optimized matrix-vector product and lets PyTorch use low-level linear algebra routines.

Broadcasting is not just syntax. It also affects memory behavior. `A + B` where `A.shape == (3, 1)` and `B.shape == (1, 4)` behaves like adding a repeated column to a repeated row, producing shape `(3, 4)`. The repeated views need not be physically materialized before the result is computed.

Preprocessing has a simple statistical rule: fit preprocessing decisions on the training set, then apply the same decisions to validation and test sets. If the mean and standard deviation of a numeric feature are estimated using the test set, information has leaked from evaluation into training. The same warning applies to vocabulary construction, category discovery, missing-value imputation, and feature selection.

For numeric standardization, use

$$
z_{ij} = \frac{x_{ij} - \mu_j}{\sigma_j + \epsilon},
$$

where $\mu_j$ and $\sigma_j$ are computed from the training column $j$, and $\epsilon$ prevents division by zero. Standardization does not make a model correct, but it makes optimization better conditioned when features have very different units.

Shape conventions should be documented at dataset boundaries. A tabular batch, image batch, and token batch all carry the batch dimension, but their remaining axes mean different things. Naming these axes in code comments, variable names, or assertions prevents subtle bugs when models are refactored. A useful habit is to check a single minibatch before training and print both feature and target shapes.

Data preprocessing should also preserve reversibility where possible. Saving category vocabularies, normalization statistics, and label mappings makes evaluation reproducible and lets predictions be interpreted later. In production systems, the preprocessing artifact is part of the model because changing it changes the numeric input seen by the network.

## Visual

| Concept | Typical PyTorch object | Shape example | Why it matters |
|---|---:|---:|---|
| Scalar loss | `torch.Tensor` | `()` | `backward()` is simplest on scalar objectives |
| Feature vector | `torch.Tensor` | `(d,)` | One example for a tabular model |
| Minibatch matrix | `torch.Tensor` | `(batch, d)` | Enables vectorized training |
| Image batch | `torch.Tensor` | `(batch, channels, height, width)` | Standard CNN layout in PyTorch |
| Token batch | `torch.Tensor` | `(batch, time)` | Standard discrete sequence layout |
| One-hot features | `torch.Tensor` | `(batch, categories)` | Converts categories to numeric inputs |

```mermaid
flowchart LR
  A[Raw files or tables] --> B[Parse records]
  B --> C[Split train validation test]
  C --> D[Fit preprocessing on train only]
  D --> E[Transform every split]
  E --> F[TensorDataset]
  F --> G[DataLoader minibatches]
  G --> H[Model input tensors]
```

## Worked example 1: broadcasting a minibatch

Problem: compute $Y = X + r$ where

$$
X =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix},
\qquad
r =
\begin{bmatrix}
10 & 20 & 30
\end{bmatrix}.
$$

Method:

1. Write the shapes. $X$ has shape $(2,3)$ and $r$ has shape $(1,3)$.
2. Compare trailing dimensions. The last dimensions are both $3$, so they match.
3. Compare the first dimensions. They are $2$ and $1$, so broadcasting can repeat the single row of $r$ across the two rows of $X$.
4. Conceptually expand $r$ to

$$
\begin{bmatrix}
10 & 20 & 30 \\
10 & 20 & 30
\end{bmatrix}.
$$

5. Add elementwise:

$$
Y =
\begin{bmatrix}
1+10 & 2+20 & 3+30 \\
4+10 & 5+20 & 6+30
\end{bmatrix}
=
\begin{bmatrix}
11 & 22 & 33 \\
14 & 25 & 36
\end{bmatrix}.
$$

Checked answer: the output shape is $(2,3)$, matching the broadcasted common shape. Each row of $X$ received the same offset vector $r$.

## Worked example 2: preprocessing a small table

Problem: convert the following raw data into model-ready numeric features. The target is `price`.

| row | rooms | age | city | price |
|---:|---:|---:|---|---:|
| 1 | 2 | 10 | Seoul | 220 |
| 2 | 4 | missing | Busan | 310 |
| 3 | 3 | 20 | Seoul | 280 |

Method:

1. Separate the target:

$$
y = [220, 310, 280]^T.
$$

2. Impute the missing numeric value using the training-column mean. The observed ages are $10$ and $20$, so

$$
\mu_{\text{age}} = \frac{10 + 20}{2} = 15.
$$

The imputed age column is $[10, 15, 20]^T$.

3. Standardize `rooms`. Its mean is

$$
\mu_{\text{rooms}} = \frac{2 + 4 + 3}{3} = 3.
$$

Its population standard deviation is

$$
\sigma_{\text{rooms}} =
\sqrt{\frac{(2-3)^2 + (4-3)^2 + (3-3)^2}{3}}
= \sqrt{\frac{2}{3}}
\approx 0.816.
$$

So the standardized `rooms` values are approximately

$$
\left[
\frac{2-3}{0.816},
\frac{4-3}{0.816},
\frac{3-3}{0.816}
\right]
= [-1.225, 1.225, 0].
$$

4. Standardize `age`. The imputed age mean is $15$ and the population standard deviation is

$$
\sigma_{\text{age}} =
\sqrt{\frac{(10-15)^2 + (15-15)^2 + (20-15)^2}{3}}
= \sqrt{\frac{50}{3}}
\approx 4.083.
$$

The standardized age values are approximately $[-1.225, 0, 1.225]$.

5. One-hot encode `city` with columns `[Busan, Seoul]`. The rows become `[0,1]`, `[1,0]`, and `[0,1]`.

Checked answer: one valid feature matrix is

$$
X \approx
\begin{bmatrix}
-1.225 & -1.225 & 0 & 1 \\
1.225 & 0 & 1 & 0 \\
0 & 1.225 & 0 & 1
\end{bmatrix}.
$$

The first two columns are standardized numeric features, and the final two are categorical indicators.

## Code

```python
import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset

raw = pd.DataFrame(
    {
        "rooms": [2.0, 4.0, 3.0],
        "age": [10.0, None, 20.0],
        "city": ["Seoul", "Busan", "Seoul"],
        "price": [220.0, 310.0, 280.0],
    }
)

y = torch.tensor(raw.pop("price").values, dtype=torch.float32).reshape(-1, 1)
numeric = raw[["rooms", "age"]].copy()
numeric = numeric.fillna(numeric.mean())
numeric = (numeric - numeric.mean()) / numeric.std(ddof=0)

categorical = pd.get_dummies(raw["city"], dtype=float)
features = pd.concat([numeric, categorical], axis=1)
X = torch.tensor(features.values, dtype=torch.float32)

dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=2, shuffle=True)

for xb, yb in loader:
    print("features:", xb)
    print("targets:", yb)
```

## Common pitfalls

- Treating tensor shape errors as incidental. Shape mismatches usually reveal an incorrect mental model of the batch dimension.
- Computing standardization statistics on the full dataset before splitting. This leaks information from validation or test examples.
- Encoding categories independently in each split. The column order and category set must be learned once from the training data.
- Assuming broadcasting always copies data. It often uses views, but the final result still has the broadcasted shape.
- Using integer tensors for model inputs that should participate in floating-point arithmetic.
- Forgetting that PyTorch image tensors usually use channels-first layout, while many image files and plotting libraries use channels-last layout.

## Connections

- [Linear algebra foundations](/math/linear-algebra/)
- [Probability and random variables](/math/probability-and-random-variables/)
- [Classical machine learning data preparation](/cs/machine-learning/)
- [Linear regression training](/cs/deep-learning/linear-regression-training)
- [Computer vision applications](/cs/deep-learning/computer-vision-applications)
