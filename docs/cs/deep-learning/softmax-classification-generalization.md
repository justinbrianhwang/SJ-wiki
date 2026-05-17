---
title: Softmax Classification and Generalization
sidebar_position: 5
---

# Softmax Classification and Generalization

Classification changes the target from a real number to a discrete class. D2L introduces softmax regression as the linear neural network for this setting: it is still a single affine transformation, but its outputs are interpreted as class probabilities. This makes it the natural baseline for image classification, text classification, and any problem where the model must choose among mutually exclusive labels.

The chapter also introduces a more careful view of generalization. Good training accuracy is not the goal; good performance on future data from the intended environment is the goal. Classification makes this distinction visible because accuracy, cross-entropy, class imbalance, distribution shift, and repeated test-set use can all tell different stories about the same model.

## Definitions

For $K$ classes, a classifier produces **logits** $o \in \mathbb{R}^K$. Logits are unconstrained scores, not probabilities. The **softmax** function maps logits to probabilities:

$$
\hat{y}_k =
\frac{\exp(o_k)}{\sum_{j=1}^K \exp(o_j)}.
$$

The probabilities are nonnegative and sum to $1$. The predicted class is often

$$
\arg\max_k \hat{y}_k,
$$

which is the same as $\arg\max_k o_k$ because softmax preserves score order.

For a one-hot label vector $y \in \{0,1\}^K$, the **cross-entropy loss** is

$$
\ell(y,\hat{y}) = -\sum_{k=1}^K y_k \log \hat{y}_k.
$$

If the true class is $c$, this reduces to $-\log \hat{y}_c$.

**Accuracy** is the fraction of examples whose predicted class equals the true class. **Top-k accuracy** counts a prediction as correct when the true class appears among the $k$ highest-scoring classes.

**Generalization error** is expected error on new data from the target distribution. **Training error** is measured on the examples used for fitting. A gap between them indicates overfitting, underspecified evaluation, distribution shift, or both.

**Distribution shift** occurs when training and deployment data differ. D2L distinguishes covariate shift $P(x)$ changes, label shift $P(y)$ changes, and concept shift $P(y \mid x)$ changes.

## Key results

Softmax is invariant to adding the same constant to every logit:

$$
\mathrm{softmax}(o)_k =
\mathrm{softmax}(o - c\mathbf{1})_k.
$$

In practice, one chooses $c = \max_j o_j$ before exponentiating to avoid overflow. This numerical detail is important enough that PyTorch combines softmax and cross-entropy in `nn.CrossEntropyLoss`, which expects raw logits and applies a stable log-softmax internally.

Softmax regression is a linear classifier. With input $x \in \mathbb{R}^d$, weights $W \in \mathbb{R}^{d \times K}$, and bias $b \in \mathbb{R}^K$, the logits are

$$
o = W^T x + b.
$$

The decision boundaries are linear in input space because class changes occur where two logits are equal:

$$
w_a^T x + b_a = w_b^T x + b_b.
$$

For cross-entropy with softmax, the gradient with respect to logits has a compact form:

$$
\frac{\partial \ell}{\partial o_k} = \hat{y}_k - y_k.
$$

This explains the behavior of classification training. The model pushes down probabilities assigned to wrong classes and pushes up the probability assigned to the true class.

The test set should be used sparingly. If many models are trained and repeatedly selected by test-set performance, the test set becomes part of the model-selection process. A separate validation set is used for selection; the test set is reserved for final reporting.

Cross-entropy also rewards calibrated confidence more than accuracy does. If two classifiers both predict the correct class, the one assigning probability $0.9$ to that class receives lower loss than the one assigning $0.55$. This is useful during training because gradients remain informative before the argmax decision changes. It is also why a model can improve cross-entropy while accuracy stays flat.

Distribution shift should be considered before deployment, not only after failure. A clothing classifier trained on catalog photos may fail on user-uploaded images because lighting, pose, background, and camera quality differ. The labels may be the same, but the input distribution has changed. D2L's taxonomy gives names to these failures so they can be tested and mitigated deliberately.

The information-theoretic view is useful beyond terminology. Cross-entropy can be read as the expected code length when using the model's predicted distribution to encode labels from the true distribution. Minimizing it encourages the predicted distribution to place mass where the data distribution places mass. KL divergence then measures the extra cost of using one distribution when another is correct. This connects classification loss to probability modeling rather than only to decision accuracy.

Softmax temperature changes confidence without changing logit order when applied uniformly. Dividing logits by a temperature greater than $1$ softens probabilities; using a temperature below $1$ sharpens them. Temperature scaling is often used after training for calibration, while training-time label smoothing changes targets to reduce overconfidence. These tools are separate from the linear softmax-regression model, but they address the same probability-output interpretation.

## Visual

```mermaid
flowchart TB
  X["Input batch X: (N, d"]"] --> Affine["Affine classifier: logits O = XW + b -> (N, K"]"]
  Affine --> Stable["Stable log-softmax: subtract row max before exponentials"]
  Stable --> Prob["Probabilities p_hat: (N, K"], rows sum to 1"]
  Y["True class ids y: (N"]"] --> Gather["Gather log probability of true class"]
  Prob --> Gather
  Gather --> CE["Cross-entropy loss = mean(-log p_hat_y)"]
  Affine --> Argmax["argmax over logits"]
  Argmax --> Acc["Accuracy, top-k, per-class metrics"]
  CE --> Grad["Gradient wrt logits: p_hat - one_hot(y)"]
  Grad --> Update["Backprop to W and b"]

  subgraph Generalization["Generalization control"]
    direction TB
    Train["Training split fits W and b"]
    Val["Validation split selects hyperparameters"]
    Test["Test split used once for final estimate"]
    Shift["Deployment shift checks: covariate, label, concept"]
  end

  Update --> Train
  Train --> Val
  Val --> Test
  Test --> Shift
```

The softmax diagram distinguishes logits, probabilities, cross-entropy, and argmax metrics. The loss path uses the true-class log probability and produces the compact `p_hat - one_hot(y)` gradient, while the metric path reads decisions from logits. The generalization subgraph shows where validation, test, and distribution-shift checks belong in the classifier workflow.

| Evaluation idea | Measures | Strength | Weakness |
|---|---|---|---|
| Cross-entropy | Probability assigned to true class | Sensitive to confidence | Harder to interpret than accuracy |
| Accuracy | Correct class decisions | Simple and task-facing | Ignores confidence and class imbalance |
| Validation error | Model-selection performance | Helps tune hyperparameters | Can be overused too |
| Test error | Final held-out estimate | Best report of chosen model | Invalid if used repeatedly for selection |
| Calibration | Probability reliability | Important for risk decisions | Not guaranteed by high accuracy |
| Shift analysis | Train-deploy mismatch | Explains failures beyond overfitting | Requires knowledge of deployment data |

## Worked example 1: cross-entropy from logits

Problem: a three-class model outputs logits $o=[2,1,0]$, and the true class is class $0$. Compute the softmax probabilities and cross-entropy loss.

Method:

1. Exponentiate logits:

$$
\exp(2) \approx 7.389,\quad
\exp(1) \approx 2.718,\quad
\exp(0)=1.
$$

2. Sum exponentials:

$$
Z = 7.389 + 2.718 + 1 = 11.107.
$$

3. Divide by the sum:

$$
\hat{y}_0 = \frac{7.389}{11.107} \approx 0.665,
\quad
\hat{y}_1 = \frac{2.718}{11.107} \approx 0.245,
\quad
\hat{y}_2 = \frac{1}{11.107} \approx 0.090.
$$

4. Since the true class is $0$, the cross-entropy is

$$
\ell = -\log(0.665) \approx 0.408.
$$

5. Compute the logit gradient:

$$
\nabla_o \ell = \hat{y} - y =
[0.665, 0.245, 0.090] - [1,0,0]
= [-0.335, 0.245, 0.090].
$$

Checked answer: the loss is about $0.408$. The gradient increases the true-class logit and decreases the two wrong-class logits under gradient descent.

## Worked example 2: accuracy under class imbalance

Problem: a dataset has $90$ examples of class `A` and $10$ examples of class `B`. Classifier 1 predicts `A` for every example. Classifier 2 correctly predicts $80$ of the `A` examples and $8$ of the `B` examples. Compare accuracy and balanced accuracy.

Method:

1. Classifier 1 correct predictions:

$$
90 + 0 = 90.
$$

Accuracy is

$$
\frac{90}{100} = 0.90.
$$

2. Classifier 1 recall by class:

$$
\mathrm{recall}_A = \frac{90}{90}=1,
\qquad
\mathrm{recall}_B = \frac{0}{10}=0.
$$

Balanced accuracy is

$$
\frac{1 + 0}{2}=0.50.
$$

3. Classifier 2 correct predictions:

$$
80 + 8 = 88.
$$

Accuracy is

$$
\frac{88}{100}=0.88.
$$

4. Classifier 2 recall by class:

$$
\mathrm{recall}_A = \frac{80}{90} \approx 0.889,
\qquad
\mathrm{recall}_B = \frac{8}{10}=0.8.
$$

Balanced accuracy is

$$
\frac{0.889 + 0.8}{2} \approx 0.8445.
$$

Checked answer: classifier 1 has higher raw accuracy, but classifier 2 is much better when both classes matter. This is why D2L treats metrics as part of problem formulation, not decoration after training.

## Code

```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(1)

n = 600
X0 = torch.randn(n // 3, 2) + torch.tensor([-2.0, 0.0])
X1 = torch.randn(n // 3, 2) + torch.tensor([2.0, 0.0])
X2 = torch.randn(n // 3, 2) + torch.tensor([0.0, 2.5])
X = torch.cat([X0, X1, X2], dim=0)
y = torch.cat(
    [
        torch.zeros(n // 3, dtype=torch.long),
        torch.ones(n // 3, dtype=torch.long),
        2 * torch.ones(n // 3, dtype=torch.long),
    ]
)

loader = DataLoader(TensorDataset(X, y), batch_size=64, shuffle=True)
model = nn.Linear(2, 3)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(20):
    for xb, yb in loader:
        logits = model(xb)
        loss = loss_fn(logits, yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

with torch.no_grad():
    pred = model(X).argmax(dim=1)
    accuracy = (pred == y).float().mean().item()
print(f"training accuracy: {accuracy:.3f}")
```

## Common pitfalls

- Applying `softmax` before `nn.CrossEntropyLoss`. The PyTorch loss expects logits and applies a stable log-softmax internally.
- Reporting accuracy alone on imbalanced data. Per-class recall, macro averages, or task-specific costs may matter more.
- Treating logits as probabilities. Logits can be any real numbers and do not sum to one.
- Reusing the test set for model selection. This produces an optimistic estimate of future performance.
- Forgetting that high softmax confidence does not guarantee calibrated probabilities.
- Assuming a classifier trained under one data distribution will remain reliable after covariate, label, or concept shift.

## Connections

- [Linear regression and training loops](/cs/deep-learning/linear-regression-training)
- [Multilayer perceptrons and regularization](/cs/deep-learning/multilayer-perceptrons-regularization)
- [Classical machine learning](/cs/machine-learning/)
- [Probability and random variables](/math/probability-and-random-variables/)
- [Natural language processing](/cs/nlp/)
