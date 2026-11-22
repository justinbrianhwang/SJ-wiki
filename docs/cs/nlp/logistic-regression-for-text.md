---
title: Logistic Regression for Text
sidebar_position: 5
---

# Logistic Regression for Text

Logistic regression is the baseline I reach for when labels are available and the input can be expressed as counts or indicators. It trains quickly on millions of sparse features, gives a probability rather than only a class, and leaves behind coefficients that can be inspected. A transformer may ultimately score higher, but a linear model often exposes problems in the data long before a larger model does.

The model is also a useful bridge between count-based classifiers and neural networks. Unlike Naive Bayes, it estimates $P(y\mid x)$ directly and makes no conditional-independence claim about the features. Unlike a multilayer network, it has no hidden representation and no nonlinear feature interactions. Its sigmoid, softmax, and cross-entropy equations reappear almost unchanged in neural output layers.

## From a score to a probability

Represent a document by $x\in\mathbb{R}^d$. Its coordinates might be word indicators, TF--IDF values, character $n$-gram counts, or features supplied by an earlier system. Binary logistic regression forms one linear score,

$$
z=w^\top x+b,
$$

then sends it through the sigmoid:

$$
P(y=1\mid x)=\sigma(z)=\frac{1}{1+\exp(-z)},\qquad
P(y=0\mid x)=1-\sigma(z).
$$

The sigmoid is less arbitrary than it first appears. If $p=P(y=1\mid x)$, its odds are $p/(1-p)$. Taking logarithms and substituting the sigmoid gives

$$
\log\frac{p}{1-p}=w^\top x+b.
$$

Logistic regression is therefore linear in **log odds**, not in probability. Increasing feature $x_j$ by one, with every other feature fixed, multiplies the odds of class 1 by $\exp(w_j)$. A coefficient of $0.7$ multiplies the odds by about $2.01$; a coefficient of $-0.7$ divides them by the same factor. The bias $b$ is the log odds when all features are zero. With centered features it describes something like a baseline case; with sparse word indicators it describes an empty document, so its literal interpretation may be less interesting.

The usual decision rule predicts class 1 when $p\geq 0.5$, equivalently when $z\geq 0$. There is no requirement to use $0.5$. A moderation queue may lower the threshold to catch more harmful messages, while an automatic deletion rule should usually use a higher one. Threshold selection belongs on validation data and must follow the cost of false positives and false negatives.

## Why cross-entropy is the fitting objective

For one binary example with label $y\in\{0,1\}$ and predicted probability $\hat y$, the Bernoulli likelihood is

$$
P(y\mid x)=\hat y^y(1-\hat y)^{1-y}.
$$

Maximizing the product of these likelihoods over a training set is equivalent to minimizing the negative log-likelihood. For one example that loss is

$$
L=-\left[y\log\hat y+(1-y)\log(1-\hat y)\right].
$$

If $y=1$, only $-\log\hat y$ remains; confident wrong predictions incur a large cost. If $y=0$, the loss becomes $-\log(1-\hat y)$. Differentiating through the sigmoid yields an unusually clean result:

$$
\frac{\partial L}{\partial z}=\hat y-y,
$$

and hence

$$
\frac{\partial L}{\partial w}=(\hat y-y)x,
\qquad
\frac{\partial L}{\partial b}=\hat y-y.
$$

The update is error-driven. On a positive example predicted with probability $0.2$, the factor $\hat y-y=-0.8$ increases weights of active features under gradient descent. On a negative example predicted as $0.9$, the positive factor decreases them. Features absent from a sparse example receive no data-gradient update for that example.

For a matrix of training examples $X$ and prediction vector $p$, the unregularized gradient is $X^\top(p-y)$. The negative log-likelihood is convex in $w$ and $b$, so any local optimum is global. Perfectly separable unregularized data is an important edge case: the likelihood keeps improving as the separating weights grow without bound. Regularization supplies a finite solution.

### Regularization in a vocabulary with thousands of rare terms

$L_2$ regularization adds a quadratic penalty,

$$
J(w,b)=\sum_i L_i+\frac{\lambda}{2}\lVert w\rVert_2^2.
$$

Its gradient contributes $\lambda w$, continuously shrinking coefficients toward zero. Rare features then need enough evidence to justify a large weight. The bias is commonly left unpenalized. $L_1$ regularization adds $\lambda\lVert w\rVert_1$ and can set many coefficients exactly to zero, though its nonsmooth point at zero calls for an appropriate optimizer.

The value of $\lambda$ must be tuned together with the feature representation. Binary indicators, raw counts, and TF--IDF coordinates have different scales. A penalty that works for one does not transfer automatically to another. Some libraries expose $C$, an inverse regularization strength: larger $C$ means weaker regularization. Confusing $C$ with $\lambda$ reverses a hyperparameter search.

## Extending the model to several labels

For $K$ mutually exclusive classes, use one weight row and bias per class:

$$
z_k=W_kx+b_k,
\qquad
P(y=k\mid x)=\frac{\exp(z_k)}{\sum_{j=1}^K\exp(z_j)}.
$$

The loss for gold class $c$ is $-\log P(y=c\mid x)$. Its logit gradient is

$$
\frac{\partial L}{\partial z_k}=P(y=k\mid x)-\mathbb{1}[k=c].
$$

The gold logit is pushed up; every other logit is pushed down in proportion to its current probability. Adding the same constant to every logit leaves softmax unchanged, which means the parameterization contains a redundancy. Optimizers handle it without trouble when regularization is present, or one class can be chosen as a reference.

Numerically, softmax should be evaluated after subtracting the largest logit:

$$
P(y=k\mid x)=\frac{\exp(z_k-m)}{\sum_j\exp(z_j-m)},
\qquad m=\max_j z_j.
$$

This changes no probability and prevents overflow. Library functions such as cross-entropy-with-logits combine softmax and the logarithm more stably than a hand-written sequence of operations.

## Feature choices determine what the line can separate

A linear model cannot invent conjunctions. With unigram indicators it can learn separate weights for `not` and `good`, but cannot make the combination `not good` negative while retaining positive evidence for `good` elsewhere. Adding bigrams creates a coordinate for that phrase. Character $n$-grams help with spelling variation, productive morphology, usernames, and noisy text. Word $n$-grams preserve more local order but expand the vocabulary quickly.

Common representations have different behavior:

| Representation | What one coordinate means | Useful property | Main limitation |
|---|---|---|---|
| binary bag of words | term occurred at least once | repeated boilerplate cannot dominate | discards frequency |
| raw counts | term occurrence count | preserves repetition | long documents have larger norms |
| TF--IDF | normalized, downweighted term frequency | strong default for topical classification | values depend on fitted corpus statistics |
| word $n$-grams | phrase occurrence | captures short negation and idioms | feature space grows rapidly |
| character $n$-grams | substring occurrence | robust to variants and misspellings | harder to interpret |
| frozen embeddings | dense semantic coordinate | compact and reusable | simple pooling loses word order |

Fit the vectorizer on training data only. Computing document frequency on the full dataset leaks information from validation and test documents. Keep preprocessing identical at training and inference time; a change in Unicode normalization or tokenization silently changes the feature coordinates.

Correlated features deserve care when reading coefficients. If `excellent` and `wonderful` nearly always occur together, the optimizer can distribute evidence across them in a way that depends on regularization and sampling noise. A small coefficient need not mean a feature is useless. Coefficients describe conditional effects under the fitted representation, not causal effects of editing a sentence.

```mermaid
flowchart LR
  A[Document] --> B[Tokenizer and vectorizer]
  B --> C[Sparse feature vector]
  C --> D["Logits z = Wx + b"]
  D --> E[Sigmoid or softmax]
  E --> F[Class probabilities]
  F --> G[Cross-entropy]
  G --> H[Regularized gradient update]
  H --> D
```

## Worked example: sentiment probability and odds

Suppose the four coordinates are a constant-like feature, positive-word count, negative-word count, and exclamation-mark indicator:

$$
x=[1,2,0,1],\qquad
w=[-1.0,0.8,-1.2,0.3],\qquad b=0.
$$

First compute the logit:

$$
\begin{aligned}
z
&=w^\top x+b\\
&=(-1.0)(1)+(0.8)(2)+(-1.2)(0)+(0.3)(1)\\
&=-1.0+1.6+0+0.3\\
&=0.9.
\end{aligned}
$$

Then

$$
\hat y=\sigma(0.9)=\frac{1}{1+e^{-0.9}}
\approx\frac{1}{1+0.4066}
\approx0.711.
$$

The positive-class odds are $0.711/(1-0.711)\approx2.46$, which also equals $e^{0.9}$. At a $0.5$ threshold the prediction is positive. At a high-precision threshold of $0.8$, the same item remains unclassified or goes to the negative/default action, depending on the system.

Now suppose the gold label is $y=1$ and the learning rate is $\eta=0.1$. The error term is

$$
\hat y-y=0.711-1=-0.289.
$$

For the positive-word coordinate $x_2=2$,

$$
\frac{\partial L}{\partial w_2}=(-0.289)(2)=-0.578.
$$

One unregularized gradient step gives

$$
w_2'=w_2-\eta\frac{\partial L}{\partial w_2}
=0.8-0.1(-0.578)=0.8578.
$$

Because the model underpredicted a positive example, the active positive-word coefficient rises.

## Worked example: a stable three-class softmax

Consider labels `sports`, `politics`, and `technology`, with logits

$$
z=[2.0,1.0,-1.0].
$$

Subtract the maximum $m=2.0$ before exponentiating:

$$
z-m=[0,-1,-3].
$$

The unnormalized values are

$$
[e^0,e^{-1},e^{-3}]\approx[1,0.3679,0.0498],
$$

whose sum is $1.4177$. The probabilities are therefore approximately

$$
[0.7054,0.2595,0.0351].
$$

If the gold class is `politics`, the loss is

$$
-\log(0.2595)\approx1.349.
$$

The gradient with respect to the three logits is

$$
[0.7054,0.2595-1,0.0351]
=[0.7054,-0.7405,0.0351].
$$

Thus the incorrect high `sports` score receives the largest downward pressure, while the gold score receives upward pressure of magnitude $0.7405$.

## A sparse baseline worth keeping

The following uses a vectorizer and a library loss that accepts logits. Real experiments should split data before fitting the vectorizer and should tune regularization on a validation set.

```python
import torch
from sklearn.feature_extraction.text import CountVectorizer

train_texts = ["good fun", "good moving", "boring dull", "bad boring"]
targets = torch.tensor([1, 1, 0, 0], dtype=torch.float32)

vectorizer = CountVectorizer(binary=True, ngram_range=(1, 2))
X = torch.tensor(
    vectorizer.fit_transform(train_texts).toarray(), dtype=torch.float32
)

w = torch.zeros(X.shape[1], requires_grad=True)
b = torch.zeros((), requires_grad=True)
optimizer = torch.optim.SGD([w, b], lr=0.5, weight_decay=0.01)

for _ in range(100):
    logits = X @ w + b
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, targets)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

test_X = torch.tensor(
    vectorizer.transform(["good but boring"]).toarray(), dtype=torch.float32
)
probability = torch.sigmoid(test_X @ w + b).item()
print(probability)
```

For large corpora, converting a sparse matrix with `.toarray()` wastes memory; scikit-learn's linear estimators consume sparse matrices directly. The dense conversion here is tolerable only because the example has a handful of documents.

## Diagnosing a disappointing classifier

Start with the representation. Inspect tokenized errors and the highest-weighted features. Spurious names, HTML fragments, or dataset-source markers often reveal leakage. If negation errors dominate, try word bigrams rather than changing the optimizer. If rare terms carry extreme coefficients, strengthen regularization or require a minimum document frequency.

Then separate ranking from thresholding. A reasonable precision--recall curve with bad accuracy may only need a different threshold. Poor ranking suggests missing features, label noise, or a train/test shift. Probability calibration is a separate question again: logistic loss encourages calibrated probabilities, but regularization, class weighting, sampling, and distribution shift can distort them. Reliability plots and held-out calibration are more informative than assuming the raw sigmoid is trustworthy.

Class weighting changes the effective training objective and often helps when the desired error costs are asymmetric. It does not create information for a rare class, and it can worsen probability calibration. For multilabel tasks, where several labels may be true at once, use one sigmoid per label rather than a single softmax; softmax incorrectly forces the labels to compete for total probability one.

Finally, compare models under identical splits and preprocessing. Naive Bayes can outperform logistic regression with extremely little data because its generative estimates settle quickly. Logistic regression usually catches up as labeled data grows and correlated evidence becomes important. A neural model earns its added cost when nonlinear interactions or contextual meaning improve held-out results, not merely because it is newer.

## Calibration, class imbalance, and what a probability means

The sigmoid number is a conditional estimate under the training setup. If examples were deliberately balanced by undersampling the majority class, the fitted intercept reflects that artificial class prior. A score of $0.7$ need not mean that seven of ten comparable production items are positive. The same warning applies when positive examples are selected for annotation more aggressively than ordinary negatives.

Prior shift can sometimes be corrected by adjusting the intercept when class-conditional feature distributions remain stable and only the prevalence changes. More general distribution shift needs fresh labeled data. A reliability diagram groups predictions into probability bins and compares mean confidence with empirical frequency. Brier score measures squared probability error; log loss penalizes confident mistakes more sharply. Both examine information that accuracy discards.

Post-hoc calibration fits a mapping on held-out predictions. Platt-style scaling fits another sigmoid to logits, while isotonic regression learns a monotone stepwise mapping. The calibration set must not be the same data used to fit the classifier. With few calibration examples, a flexible isotonic map can overfit badly. Calibration also does not repair ranking: if positives tend to score below negatives, remapping scores monotonically cannot reverse them.

Class weighting is often introduced as a response to imbalance, but the desired metric should come first. If the classes overlap and only a different operating point is needed, training an ordinary model and choosing a threshold may be enough. Weighting changes the fitted boundary by making some errors more expensive. It can help when minority regions would otherwise be neglected, yet its output probabilities now correspond to a modified loss rather than the original population frequencies.

Macro-averaged metrics give every class equal weight; micro-averaged metrics pool decisions and are dominated by frequent classes. For multiclass news classification, reporting both can reveal a model that performs well on common topics and poorly on rare ones. For multilabel classification, thresholds may differ by label because prevalence and costs differ. A single global threshold is convenient, not inherently correct.

## Reading coefficients without telling a causal story

For a binary feature, $e^{w_j}$ is an odds multiplier conditional on every other coordinate being held fixed. Text edits rarely hold the others fixed. Adding a phrase changes several unigram, bigram, character, length, and normalization features at once. A coefficient is a property of the fitted coordinate system, not the isolated semantic effect of a word.

Regularization makes interpretation still more conditional. Two duplicate features can split a useful weight, making each look modest. Removing one lets the other grow without changing predictions much. Standard errors from classical low-dimensional logistic regression are also a poor fit for a vocabulary chosen from the same corpus with heavy regularization. Bootstrap stability of top features is more honest when interpretation matters.

Inspecting errors by subgroup or source often teaches more than a ranked coefficient list. A strong publisher-name feature may be valid on a random split and useless on a future publisher. Temporal, author-level, or source-level splits test the generalization actually needed. Near-duplicate documents must remain in one split; otherwise the model can appear to understand text while matching repeated templates.

The linear decision can be decomposed for one document by listing $w_jx_j$ contributions. That local accounting is exact for the logit and useful for debugging. It still says what raised the fitted score, not what would happen in the world if the phrase were changed. Keeping those two claims separate avoids most overinterpretation.

<div className="see-also">

See also: [Naive Bayes sentiment classification](/cs/nlp/naive-bayes-sentiment-classification) · [Neural networks for NLP](/cs/nlp/neural-networks-for-nlp) · [Sequence labeling with HMMs and CRFs](/cs/nlp/sequence-labeling-hmms-crfs) · [Pretrained language models](/cs/nlp/pretrained-language-models)

</div>
