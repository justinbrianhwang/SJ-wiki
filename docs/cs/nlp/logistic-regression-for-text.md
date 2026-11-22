---
title: Logistic Regression for Text
sidebar_position: 5
---

# Logistic Regression for Text

Logistic regression is the standard discriminative baseline for supervised text classification. Jurafsky and Martin present it after Naive Bayes to show how a model can directly estimate $P(y\mid x)$, learn weights by gradient descent, and generalize to multiple classes through softmax. Eisenstein emphasizes the same model as a log-linear classifier, relating it to regularization, convex optimization, and the older maximum entropy name used in NLP.

For NLP, logistic regression is important because it sits between count-based classifiers and neural networks. It uses arbitrary features, produces calibrated-ish probabilities when trained carefully, handles correlated features better than Naive Bayes, and provides the softmax and cross-entropy machinery that reappears in neural language models, transformers, sequence labeling, and parsing.

## Definitions

In binary logistic regression, each input document or instance is represented by a feature vector $x\in\mathbb{R}^d$. The model learns weights $w$ and bias $b$, computes a logit

$$
z=w^\top x+b,
$$

and maps it to a probability with the sigmoid function:

$$
\sigma(z)=\frac{1}{1+\exp(-z)}.
$$

Thus

$$
P(y=1\mid x)=\sigma(w^\top x+b),\qquad P(y=0\mid x)=1-\sigma(w^\top x+b).
$$

For $K$ classes, multinomial logistic regression uses a weight matrix $W\in\mathbb{R}^{K\times d}$ and bias vector $b\in\mathbb{R}^K$. The softmax function turns class logits into probabilities:

$$
P(y=k\mid x)=\frac{\exp(W_kx+b_k)}{\sum_{j=1}^K\exp(W_jx+b_j)}.
$$

The standard loss is **cross-entropy**, which for binary classification is

$$
L(\hat{y},y)=-\left[y\log\hat{y}+(1-y)\log(1-\hat{y})\right].
$$

For multiclass classification with gold class $c$:

$$
L=-\log P(y=c\mid x).
$$

## Key results

Logistic regression is discriminative. It does not model how the document was generated; it only models the conditional probability of the label. This lets it use overlapping and correlated features, such as word counts, lexicon indicators, punctuation counts, capitalization flags, and metadata. If two features are correlated, logistic regression can share weight across them instead of double-counting evidence as Naive Bayes tends to do.

The binary cross-entropy gradient has a simple form. For one example,

$$
\frac{\partial L}{\partial w}=(\hat{y}-y)x,\qquad
\frac{\partial L}{\partial b}=\hat{y}-y.
$$

This is an error-driven update: if the model predicts too high a probability, $\hat{y}-y$ is positive and the weights on active features are decreased; if it predicts too low a probability, they are increased.

With the usual convex objective, binary and multinomial logistic regression have no bad local minima. This contrasts with multilayer neural networks, where optimization is nonconvex. Regularization controls overfitting. $L_2$ regularization adds

$$
\lambda ||w||_2^2
$$

to the loss and shrinks weights toward zero. $L_1$ regularization adds $\lambda\vert \vert w\vert \vert _1$ and encourages sparsity, which can be useful for high-dimensional bag-of-words features.

Feature scaling matters. Binary indicators, counts, TF-IDF values, and dense embeddings can have different ranges. If features are not normalized, gradient descent may learn slowly or let large-scale features dominate. For sparse text, linear models are efficient because only nonzero features need updates.

The model is also a useful interpretability baseline. A positive coefficient for a feature means that, holding the other features fixed, increasing that feature raises the log odds of the positive class. For bag-of-words sentiment, this makes it easy to inspect the most positive and most negative words. For NER or period disambiguation, feature templates can reveal whether the model relies on capitalization, suffixes, abbreviations, or neighboring words. This interpretability is not perfect, because correlated features can split weight, but it is much clearer than inspecting a deep network from scratch.

Multinomial logistic regression is the direct ancestor of the neural softmax classifier. If the input to softmax is a hidden vector rather than a hand-built feature vector, the output layer is still a log-linear classifier over classes. This is why the equations in Jurafsky and Martin's logistic regression chapter reappear in neural networks, language modeling, masked token prediction, and sequence labeling. Eisenstein's maximum-entropy perspective adds another interpretation: among distributions matching the model's feature expectations, choose the one with maximum entropy.

For text, the regularization setting should be tuned on held-out data, not chosen by habit. Too little regularization lets rare words receive extreme weights, especially in high-dimensional sparse vocabularies. Too much regularization erases useful lexical cues and makes the model behave like a class-prior baseline. Reporting the feature representation and the regularization strength is therefore part of reporting the model.

Logistic regression is also a strong calibration starting point. Because it outputs probabilities, a system can set different decision thresholds for different operational needs. A spam filter may require high precision before hiding a message; a medical triage classifier may prefer high recall before sending cases to human review. The threshold is not part of the trained weights, so it should be selected on validation data using the metric that matches the application.

In error analysis, separate feature errors from decision errors. If a document is tokenized badly or a negation cue is missing, the classifier may be blameless. If the features are present but the learned weights point the wrong way, the issue is data, regularization, or optimization. This separation keeps linear baselines useful even in projects that later move to transformer models.

## Visual

```mermaid
flowchart LR
  A[Document] --> B[Feature vector x]
  B --> C["Linear score z = Wx + b"]
  C --> D[Sigmoid or softmax]
  D --> E[Class probabilities]
  E --> F[Cross-entropy loss]
  F --> G[Gradient update]
  G --> C
```

| Model | Learns | Handles correlated features | Training style | Typical NLP role |
|---|---|---:|---|---|
| Naive Bayes | $P(y)$ and $P(x\mid y)$ | weakly | counting | tiny-data baseline |
| Logistic regression | $P(y\mid x)$ | better | gradient descent | strong sparse baseline |
| Feedforward net | nonlinear $P(y\mid x)$ | better | backpropagation | learned feature interactions |
| Transformer fine-tune | contextual $P(y\mid x)$ | best with data | backpropagation | modern high-accuracy model |

## Worked example 1: binary sentiment probability

Problem: a binary logistic sentiment model has features:

$$
x=[1,\;2,\;0,\;1]
$$

for bias-like constant, positive word count, negative word count, and exclamation mark. Let

$$
w=[-1.0,\;0.8,\;-1.2,\;0.3],\qquad b=0.
$$

Compute $P(\mathrm{positive}\mid x)$.

1. Compute the logit:

$$
\begin{aligned}
z &= w^\top x+b\\
&=(-1.0)(1)+(0.8)(2)+(-1.2)(0)+(0.3)(1)+0\\
&=-1.0+1.6+0+0.3\\
&=0.9.
\end{aligned}
$$

2. Apply sigmoid:

$$
\sigma(0.9)=\frac{1}{1+\exp(-0.9)}.
$$

3. Approximate $\exp(-0.9)\approx0.4066$:

$$
\sigma(0.9)\approx \frac{1}{1.4066}\approx0.711.
$$

Checked answer: the model predicts positive sentiment with probability about $0.711$, so a $0.5$ decision threshold gives the positive class.

## Worked example 2: one gradient step

Problem: use the same example, but suppose the gold label is $y=1$ and learning rate $\eta=0.1$. Compute the update for the positive word weight $w_2=0.8$.

1. From the previous example, $\hat{y}=0.711$.
2. The error term is

$$
\hat{y}-y=0.711-1=-0.289.
$$

3. The positive word feature value is $x_2=2$.
4. The gradient for $w_2$ is

$$
\frac{\partial L}{\partial w_2}=(\hat{y}-y)x_2=(-0.289)(2)=-0.578.
$$

5. Gradient descent subtracts the gradient:

$$
w_2' = w_2-\eta\frac{\partial L}{\partial w_2}
=0.8-0.1(-0.578)
=0.8578.
$$

Checked answer: because the model underpredicted a positive example, the weight for the active positive-word feature increases from $0.8$ to about $0.858$.

## Code

```python
import torch
from sklearn.feature_extraction.text import CountVectorizer

texts = ["good fun", "good moving", "boring dull", "bad boring"]
y = torch.tensor([1, 1, 0, 0], dtype=torch.float32)

vec = CountVectorizer(binary=True)
X_np = vec.fit_transform(texts).toarray()
X = torch.tensor(X_np, dtype=torch.float32)

w = torch.zeros(X.shape[1], requires_grad=True)
b = torch.zeros((), requires_grad=True)
opt = torch.optim.SGD([w, b], lr=0.5, weight_decay=0.01)

for _ in range(100):
    logits = X @ w + b
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, y)
    opt.zero_grad()
    loss.backward()
    opt.step()

test = torch.tensor(vec.transform(["good boring"]).toarray(), dtype=torch.float32)
prob = torch.sigmoid(test @ w + b)
print(vec.get_feature_names_out())
print(prob.item())
```

## Common pitfalls

- Applying sigmoid before `binary_cross_entropy_with_logits`; most libraries expect raw logits for numerical stability.
- Interpreting weights without checking feature scaling and correlations.
- Forgetting the bias term, which represents the base log odds.
- Using accuracy when the decision threshold should be tuned for precision or recall.
- Assuming logistic regression automatically learns phrase interactions; a bag-of-words model needs explicit features for `not_good`.
- Over-regularizing and shrinking all useful lexical evidence toward zero.
- Comparing to Naive Bayes without matching tokenization, vocabulary, and train/test splits.

## Connections

- [Naive Bayes and sentiment classification](/cs/nlp/naive-bayes-sentiment-classification)
- [Neural networks for NLP](/cs/nlp/neural-networks-for-nlp)
- [Sequence labeling with HMMs and CRFs](/cs/nlp/sequence-labeling-hmms-crfs)
- [Pretrained language models](/cs/nlp/pretrained-language-models)
