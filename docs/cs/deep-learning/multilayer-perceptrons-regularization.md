---
title: Multilayer Perceptrons and Regularization
sidebar_position: 6
---

# Multilayer Perceptrons and Regularization

Multilayer perceptrons extend linear models by composing affine transformations with nonlinear activation functions. This is the first point in D2L where the model can represent genuinely nonlinear relationships without manually designing nonlinear features. A linear model can only carve input space with hyperplanes; an MLP can bend those boundaries by learning hidden representations.

The same flexibility creates new training issues. Deep networks can overfit, gradients can vanish or explode, initialization can make learning slow, and regularizers can change both optimization and generalization. D2L treats these as practical engineering concerns rather than isolated theory: activation choice, initialization, dropout, weight decay, and early stopping all shape the behavior of the same training loop.

## Definitions

An **MLP** with one hidden layer maps an input $x \in \mathbb{R}^d$ to

$$
h = \phi(W_1 x + b_1),
\qquad
o = W_2 h + b_2,
$$

where $\phi$ is an elementwise activation function. For regression, $o$ may be a scalar prediction. For classification, $o$ is usually a vector of logits.

Common **activation functions** include

$$
\mathrm{ReLU}(x)=\max(x,0),
$$

$$
\sigma(x)=\frac{1}{1+\exp(-x)},
$$

and

$$
\tanh(x)=\frac{1-\exp(-2x)}{1+\exp(-2x)}.
$$

**Forward propagation** computes outputs layer by layer. **Backpropagation** applies the chain rule in reverse to compute gradients. A **computational graph** records which operations produced which tensors.

**Weight initialization** chooses initial parameter values before training. Xavier initialization aims to preserve activation variance through layers with roughly symmetric activations. Kaiming initialization is commonly paired with ReLU.

**Weight decay** adds an $L_2$ penalty to discourage large weights. **Dropout** randomly sets hidden activations to zero during training and rescales the survivors so their expectation is preserved. **Early stopping** halts training when validation performance stops improving.

## Key results

Without nonlinear activations, stacking affine layers does not increase expressive power. If

$$
h = W_1x + b_1,
\qquad
o = W_2h + b_2,
$$

then

$$
o = W_2W_1x + W_2b_1 + b_2,
$$

which is just another affine function of $x$. The activation function is what lets hidden layers learn nonlinear features.

The ReLU activation is popular because it is simple, cheap, and has derivative $1$ for positive inputs:

$$
\frac{d}{dx}\mathrm{ReLU}(x) =
\begin{cases}
1, & x > 0, \\
0, & x < 0.
\end{cases}
$$

At $x=0$ the derivative is undefined, but frameworks choose a subgradient convention. ReLU reduces the saturation problem that affects sigmoid and tanh when inputs have large magnitude.

Dropout with drop probability $p$ keeps an activation with probability $q=1-p$. In inverted dropout, the training activation is

$$
\tilde{h}_j =
\frac{m_j h_j}{q},
\qquad
m_j \sim \mathrm{Bernoulli}(q).
$$

Then

$$
\mathbb{E}[\tilde{h}_j] = h_j.
$$

This means no extra scaling is needed at evaluation time.

Weight decay for loss $L(w)$ optimizes

$$
L(w) + \frac{\lambda}{2}\|w\|_2^2.
$$

The gradient contribution from the penalty is $\lambda w$, which shrinks weights toward zero during updates.

Capacity is not determined by parameter count alone, but parameter count is still a useful warning sign. A wide MLP can memorize small datasets, especially when labels contain noise. Regularization methods do not make overfitting impossible; they bias training toward simpler or more robust solutions. D2L's generalization discussion emphasizes that modern deep networks can generalize in regimes where classical parameter-count intuition is incomplete, but validation data remains essential.

Initialization interacts with activation functions. If weights are too small, signals and gradients may shrink as they pass through layers. If weights are too large, activations may explode or saturate. Xavier-style initialization balances fan-in and fan-out for roughly symmetric activations, while Kaiming initialization accounts for ReLU zeroing roughly half of its inputs.

Dropout and weight decay regularize in different ways. Weight decay directly penalizes large weights in the objective. Dropout injects multiplicative noise into activations during training, making the network less dependent on exact co-adaptations among hidden units. They can be used together, but their strengths and tuning knobs are not interchangeable.

Activation distributions are worth monitoring. If most ReLU units are always negative, they output zero and receive no gradient on those examples. If sigmoid or tanh units operate in saturated regions, their derivatives are tiny. Initialization, normalization, learning rate, and input scaling all influence where activations live. This is why preprocessing and initialization are part of the MLP story rather than separate housekeeping.

Generalization controls should be evaluated on held-out data. A lower training loss after adding width may simply mean higher capacity. A lower validation loss after adding weight decay, dropout, or early stopping is stronger evidence of improved generalization. D2L's regularization sections are best read as a toolkit for changing the bias of training, not as guarantees that a model will generalize.

The MLP is also a reference model for non-image tabular features. Even when specialized architectures dominate vision and language, a well-regularized MLP remains a useful baseline for dense numeric and categorical features after appropriate preprocessing.

## Visual

```mermaid
flowchart TB
  X["Input batch X: (N, d_in"]"] --> L1["Linear 1: W1 (d_in, h1"] + b1 -> ["N, h1"]"]
  L1 --> A1["Activation phi, e.g. ReLU -> (N, h1"]"]
  A1 --> D1["Dropout train only: mask m1 ~ Bernoulli(q), h1*m1/q"]
  D1 --> L2["Linear 2: W2 (h1, h2"] + b2 -> ["N, h2"]"]
  L2 --> A2["Activation phi -> (N, h2"]"]
  A2 --> D2["Dropout train only: mask m2 ~ Bernoulli(q)"]
  D2 --> L3["Output linear: W3 (h2, K"] + b3 -> logits ["N, K"]"]
  L3 --> CE["Cross-entropy or task loss"]
  CE --> Total["Regularized objective: loss + lambda/2 * ||W||_2^2"]

  subgraph Backward["Backward/update paths"]
    direction TB
    G3["Gradients dL/dW3, dL/db3"]
    G2["Gradients dL/dW2, dL/db2"]
    G1["Gradients dL/dW1, dL/db1"]
    WD["Weight decay adds lambda * W to weight gradients"]
    Opt["Optimizer step updates trainable parameters"]
  end

  CE -. "backprop through logits" .-> G3
  G3 -. "chain rule through dropout and activation" .-> G2
  G2 -. "chain rule through dropout and activation" .-> G1
  Total -. "L2 penalty path, weights only" .-> WD
  WD --> Opt
  G1 --> Opt
  G2 --> Opt
  G3 --> Opt
  Opt -. "new W, b for next minibatch" .-> L1
```

The MLP diagram keeps the batch dimension visible from input `[N, d_in]` through hidden layers and logits `[N, K]`. Dropout is shown as a training-only activation path, while weight decay is a separate objective path that adds `lambda * W` to weight gradients rather than changing the forward pass. The backward subgraph makes clear that regularization, dropout, and affine layers affect different parts of the training loop.

| Technique | Main purpose | Training-time behavior | Evaluation-time behavior |
|---|---|---|---|
| ReLU | Nonlinear representation | Clips negative preactivations | Same as training |
| Xavier init | Stable variance | Sets scale from fan-in and fan-out | Only affects starting point |
| Kaiming init | ReLU-friendly variance | Sets scale from fan-in | Only affects starting point |
| Weight decay | Penalize large weights | Adds $\lambda w$ to gradients | No direct runtime change |
| Dropout | Reduce co-adaptation | Randomly masks activations | Uses full network |
| Early stopping | Avoid late overfitting | Stops by validation signal | Selects saved checkpoint |

## Worked example 1: forward pass through a tiny MLP

Problem: compute the output of a one-hidden-layer MLP. Let

$$
x =
\begin{bmatrix}
1 \\
-2
\end{bmatrix},
\quad
W_1 =
\begin{bmatrix}
1 & 1 \\
2 & -1
\end{bmatrix},
\quad
b_1 =
\begin{bmatrix}
0 \\
1
\end{bmatrix},
$$

use ReLU activation, and let

$$
W_2 =
\begin{bmatrix}
1 & -2
\end{bmatrix},
\quad
b_2 = 0.5.
$$

Method:

1. Compute the hidden preactivation:

$$
z_1 = W_1x+b_1 =
\begin{bmatrix}
1(1)+1(-2) \\
2(1)+(-1)(-2)
\end{bmatrix}
+
\begin{bmatrix}
0 \\
1
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
4
\end{bmatrix}
+
\begin{bmatrix}
0 \\
1
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
5
\end{bmatrix}.
$$

2. Apply ReLU:

$$
h = \mathrm{ReLU}(z_1) =
\begin{bmatrix}
0 \\
5
\end{bmatrix}.
$$

3. Compute output:

$$
o = W_2h+b_2 =
\begin{bmatrix}
1 & -2
\end{bmatrix}
\begin{bmatrix}
0 \\
5
\end{bmatrix}
+0.5
= -10 + 0.5
= -9.5.
$$

Checked answer: the MLP output is $-9.5$. The first hidden unit is inactive because its preactivation is negative.

## Worked example 2: dropout preserves expectation

Problem: a hidden activation is $h=[2,4]^T$. Apply inverted dropout with drop probability $p=0.5$. List all possible masked outputs and show that the expected output equals $h$.

Method:

1. The keep probability is $q=1-p=0.5$.
2. Each unit is kept independently. If kept, it is scaled by $1/q=2$.
3. The four possible masks are $[0,0]$, $[1,0]$, $[0,1]$, and $[1,1]$, each with probability $0.25$.
4. The corresponding outputs are

$$
[0,0],
\quad
[4,0],
\quad
[0,8],
\quad
[4,8].
$$

5. Compute the expectation:

$$
\mathbb{E}[\tilde{h}]
=0.25[0,0]+0.25[4,0]+0.25[0,8]+0.25[4,8]
=[2,4].
$$

Checked answer: inverted dropout changes individual training passes but preserves the activation expectation. This is why PyTorch dropout layers automatically disable masking in `eval()` mode rather than rescaling outputs again.

## Code

```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(2)

n = 1000
X = 4 * torch.rand(n, 2) - 2
y = ((X[:, 0] ** 2 + X[:, 1] ** 2) > 1.5).long()
loader = DataLoader(TensorDataset(X, y), batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Linear(2, 32),
    nn.ReLU(),
    nn.Dropout(p=0.2),
    nn.Linear(32, 16),
    nn.ReLU(),
    nn.Linear(16, 2),
)

for module in model:
    if isinstance(module, nn.Linear):
        nn.init.kaiming_uniform_(module.weight, nonlinearity="relu")
        nn.init.zeros_(module.bias)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=1e-4)

model.train()
for epoch in range(30):
    for xb, yb in loader:
        loss = loss_fn(model(xb), yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

model.eval()
with torch.no_grad():
    accuracy = (model(X).argmax(dim=1) == y).float().mean().item()
print(f"training accuracy: {accuracy:.3f}")
```

## Common pitfalls

- Stacking linear layers without nonlinear activations and expecting a deeper model.
- Leaving dropout active during evaluation by forgetting `model.eval()`.
- Applying dropout to logits in a simple classifier unless there is a specific reason.
- Using sigmoid in deep hidden layers without considering saturation and vanishing gradients.
- Initializing all weights to zero, which makes hidden units learn identical features.
- Assuming lower training loss always means a better model. Validation behavior is the relevant generalization signal.

## Connections

- [Softmax classification and generalization](/cs/deep-learning/softmax-classification-generalization)
- [Optimization algorithms](/cs/deep-learning/optimization-algorithms)
- [PyTorch builders guide](/cs/deep-learning/pytorch-builders-guide)
- [Classical machine learning](/cs/machine-learning/)
- [Calculus](/math/calculus/)
