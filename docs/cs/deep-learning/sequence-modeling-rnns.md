---
title: Sequence Modeling and RNNs
sidebar_position: 10
---

# Sequence Modeling and RNNs

Sequence modeling handles data where order matters: text, time series, speech, click streams, and trajectories. D2L starts with autoregressive prediction and language modeling because they reveal the central issue: the prediction at one time step depends on previous observations. Recurrent neural networks address this by carrying a hidden state forward through time.

RNNs are no longer the default architecture for large-scale language modeling, but they remain conceptually important. They introduce hidden states, truncated backpropagation through time, gradient clipping, teacher-forced sequence training, and the difference between training with known histories and generating one token at a time. These ideas reappear in encoder-decoder models, attention, transformers, and reinforcement learning.

## Definitions

A **sequence** is an ordered list $(x_1,\ldots,x_T)$. In language modeling, $x_t$ may be a token. In time-series forecasting, it may be a real-valued observation.

An **autoregressive model** predicts the next value using previous values:

$$
P(x_t \mid x_{t-1},\ldots,x_1).
$$

In practice, models often use a finite context window or a hidden state that summarizes the past.

A **language model** assigns probabilities to token sequences using the chain rule:

$$
P(x_1,\ldots,x_T)
= \prod_{t=1}^T P(x_t \mid x_1,\ldots,x_{t-1}).
$$

**Perplexity** is the exponential of average cross-entropy. For a sequence with average negative log-likelihood $\bar{\ell}$,

$$
\mathrm{perplexity} = \exp(\bar{\ell}).
$$

A basic **RNN** updates a hidden state by

$$
H_t = \phi(X_t W_{xh} + H_{t-1}W_{hh} + b_h),
$$

and produces outputs by

$$
O_t = H_t W_{hq} + b_q.
$$

**Backpropagation through time** applies backpropagation to the unrolled recurrent computation graph. **Truncated BPTT** limits the number of time steps through which gradients are propagated.

**Gradient clipping** rescales gradients when their norm exceeds a threshold:

$$
g \leftarrow \min\left(1,\frac{\theta}{\|g\|}\right)g.
$$

## Key results

The language-modeling chain rule is exact, but modeling the full history is hard. RNNs use hidden states as learned summaries of the prefix. In character-level language modeling, the same recurrent cell is applied at every time step, sharing parameters across sequence positions.

Training often uses subsequences rather than entire corpora. If hidden states are carried between adjacent subsequences, the model can preserve temporal continuity. If hidden states are reset, subsequences are treated more independently. D2L discusses both random sampling and sequential partitioning because they change how hidden states should be initialized.

Perplexity has an intuitive interpretation as the effective branching factor. A perplexity of $1$ means perfect prediction. A perplexity near the vocabulary size means the model is not much better than uniform guessing. Lower perplexity usually indicates a better language model, but generated text quality also depends on decoding.

RNN gradients can vanish or explode because the same recurrent weight matrix is multiplied through many time steps. This motivates gated architectures such as GRUs and LSTMs, and it also motivates gradient clipping in basic RNN training.

During generation, the model consumes its own previous predictions. This differs from teacher-forced training, where the correct previous token is known. The mismatch can accumulate errors, especially for long sequences.

Vocabulary construction determines the model's output space. Character vocabularies are small and avoid unknown words, but sequences become long. Word vocabularies produce shorter sequences but suffer from rare and unseen words. Subword vocabularies are a compromise used by many modern NLP systems. D2L's early character-level examples are pedagogically useful because one-hot inputs and small vocabularies make the mechanics visible.

Hidden-state handling is a correctness issue. When training on independent sequences, the initial hidden state should usually be reset. When splitting a long stream into adjacent subsequences, carrying the hidden state can preserve continuity, but the state is often detached from the previous graph to limit backpropagation length. Otherwise, memory usage grows and gradients flow through far more time steps than intended.

Sampling strategy affects generated text. Greedy decoding chooses the most likely token every time and can become repetitive. Random sampling introduces diversity but may produce incoherent output if the distribution is too flat. Temperature scaling adjusts the sharpness of token probabilities. These decoding choices do not change the trained RNN, but they strongly affect qualitative predictions.

Time-series forecasting uses the same sequence principles with different data types. Instead of token ids, inputs may be real-valued vectors containing lagged observations, calendar features, or external covariates. The model can predict one step ahead or multiple future steps. Autoregressive rollout creates the same exposure problem as text generation: once the model uses its own predictions as inputs, errors can compound.

Perplexity should be compared only under compatible preprocessing. A character-level model and a word-level model have different prediction units, so their perplexities are not directly interchangeable. The same caution applies to different vocabularies, casing rules, and token filters. D2L's language-model examples teach the metric, but fair model comparison requires a shared data pipeline.

For long streams, stateful training is a modeling choice. Carrying state between adjacent chunks can help continuity, but it also makes batch ordering part of the data pipeline. Randomly shuffling chunks while carrying state mixes unrelated histories and corrupts the sequence signal.

This is why sequence experiments should document batching, hidden-state reset rules, and truncation length.

## Visual

```mermaid
flowchart TB
  subgraph Cell["Vanilla RNN cell at time t"]
    direction TB
    Xt["#quot;Input x_t: [N, d_x"]"] --> XW["Input affine: x_t W_xh"]
    Hprev["#quot;Previous hidden h_{t-1}: [N, d_h"]"] --> HW["Recurrent affine: h_{t-1} W_hh"]
    XW --> Sum(("Add + b_h"))
    HW --> Sum
    Sum --> Phi["Nonlinearity phi, e.g. tanh or ReLU"]
    Phi --> Ht["#quot;Hidden h_t: [N, d_h"]"]
    Ht --> Readout["Output affine: h_t W_hq + b_q"]
    Readout --> Ot["#quot;Logits o_t: [N, vocab"]"]
    Ot --> Pt(("p next token from prefix through t"))
  end

  subgraph Unrolled["Same cell unrolled through time with shared weights"]
    direction LR
    H0["h_0"] --> R1["RNN cell t=1"]
    X1["x_1"] --> R1
    R1 --> H1["h_1"]
    R1 --> O1["logits for x_2"]
    H1 --> R2["RNN cell t=2"]
    X2["x_2"] --> R2
    R2 --> H2["h_2"]
    R2 --> O2["logits for x_3"]
    H2 --> R3["RNN cell t=3"]
    X3["x_3"] --> R3
    R3 --> H3["h_3"]
    R3 --> O3["logits for x_4"]
  end

  Ht -. "state passed forward" .-> H1
  R1 -. "shared W_xh, W_hh, W_hq" .-> R2
  R2 -. "shared W_xh, W_hh, W_hq" .-> R3
```

The first subgraph opens the vanilla RNN cell: input and previous hidden state are projected separately, added with bias, passed through a nonlinearity, and read out as next-token logits. The unrolled subgraph shows the same parameterized cell reused at each time step, with the hidden state carrying `[N, d_h]` information forward. Dotted arrows emphasize weight sharing across time rather than separate layers.

| Concept | Meaning in sequence models | Practical decision |
|---|---|---|
| Tokenization | Convert raw text to symbols | Character, word, or subword units |
| Vocabulary | Map tokens to integer ids | Include unknown and padding tokens |
| Context | Information used for prediction | Fixed window or hidden state |
| Perplexity | Exponential average loss | Lower is better for next-token prediction |
| Hidden state | Learned summary of past | Reset, detach, or carry between batches |
| Gradient clipping | Limit exploding gradients | Choose clipping threshold |

## Worked example 1: sequence probability and perplexity

Problem: a language model assigns the following probabilities to the correct next tokens in a three-token sequence: $0.5$, $0.25$, and $0.125$. Compute the negative log-likelihood and perplexity using natural logarithms.

Method:

1. The sequence likelihood is the product:

$$
P = 0.5 \cdot 0.25 \cdot 0.125 = 0.015625.
$$

2. The total negative log-likelihood is

$$
-\log P =
-\log(0.015625).
$$

Since $0.015625 = \frac{1}{64}$,

$$
-\log P = \log 64.
$$

3. The average negative log-likelihood over three tokens is

$$
\bar{\ell} = \frac{\log 64}{3}.
$$

Because $64=4^3$,

$$
\bar{\ell} = \log 4.
$$

4. Perplexity is

$$
\exp(\bar{\ell}) = \exp(\log 4)=4.
$$

Checked answer: the perplexity is $4$. On average, the model is as uncertain as choosing among four equally likely options at each step.

## Worked example 2: one RNN hidden-state update

Problem: compute a one-step RNN hidden state with ReLU. Let

$$
x_t =
\begin{bmatrix}
1 & 2
\end{bmatrix},
\quad
h_{t-1} =
\begin{bmatrix}
0 & 1
\end{bmatrix},
$$

$$
W_{xh} =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix},
\quad
W_{hh} =
\begin{bmatrix}
1 & -1 \\
2 & 0
\end{bmatrix},
\quad
b_h =
\begin{bmatrix}
-1 & 1
\end{bmatrix}.
$$

Method:

1. Compute input contribution:

$$
x_t W_{xh} =
\begin{bmatrix}
1 & 2
\end{bmatrix}.
$$

2. Compute recurrent contribution:

$$
h_{t-1}W_{hh} =
\begin{bmatrix}
0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & -1 \\
2 & 0
\end{bmatrix}
=
\begin{bmatrix}
2 & 0
\end{bmatrix}.
$$

3. Add bias:

$$
z_t =
\begin{bmatrix}
1 & 2
\end{bmatrix}
+
\begin{bmatrix}
2 & 0
\end{bmatrix}
+
\begin{bmatrix}
-1 & 1
\end{bmatrix}
=
\begin{bmatrix}
2 & 3
\end{bmatrix}.
$$

4. Apply ReLU:

$$
h_t = \mathrm{ReLU}(z_t)=
\begin{bmatrix}
2 & 3
\end{bmatrix}.
$$

Checked answer: the next hidden state is $[2,3]$. Both units are active because both preactivations are positive.

## Code

```python
import torch
from torch import nn

torch.manual_seed(3)

vocab_size = 20
batch_size = 4
time_steps = 6
hidden_size = 16

tokens = torch.randint(0, vocab_size, (batch_size, time_steps))
inputs = tokens[:, :-1]
targets = tokens[:, 1:]

model = nn.RNN(input_size=vocab_size, hidden_size=hidden_size, batch_first=True)
classifier = nn.Linear(hidden_size, vocab_size)
loss_fn = nn.CrossEntropyLoss()

one_hot = torch.nn.functional.one_hot(inputs, num_classes=vocab_size).float()
states, h_last = model(one_hot)
logits = classifier(states)

loss = loss_fn(logits.reshape(-1, vocab_size), targets.reshape(-1))
loss.backward()

torch.nn.utils.clip_grad_norm_(
    list(model.parameters()) + list(classifier.parameters()),
    max_norm=1.0,
)
print("loss:", loss.item())
print("last hidden shape:", h_last.shape)
```

## Common pitfalls

- Feeding class indices directly into an RNN that expects one-hot or embedded vectors.
- Forgetting to detach hidden states between subsequences when truncated BPTT is intended.
- Comparing perplexity values computed with different tokenization schemes.
- Generating text with teacher forcing instead of feeding predictions back into the model.
- Ignoring exploding gradients in long sequences.
- Treating hidden state shape as batch-first. PyTorch recurrent modules use `(num_layers * directions, batch, hidden_size)` for hidden states.

## Connections

- [Gated RNNs and sequence-to-sequence](/cs/deep-learning/gated-rnns-seq2seq)
- [Attention and transformers](/cs/deep-learning/attention-transformers)
- [Natural language processing](/cs/nlp/)
- [Probability and random variables](/math/probability-and-random-variables/)
- [Reinforcement learning](/cs/reinforcement-learning/)
