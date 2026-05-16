---
title: Attention and Transformers
sidebar_position: 12
---

# Attention and Transformers

Attention lets a model choose which pieces of information to use for each prediction. D2L introduces attention through queries, keys, and values, then builds scoring functions, multi-head attention, self-attention, positional encoding, and the Transformer architecture. This progression explains why attention displaced recurrence for many sequence tasks: it creates direct paths between all positions and parallelizes efficiently.

A Transformer is not just attention. It combines multi-head self-attention, positionwise feed-forward networks, residual connections, layer normalization, masking, and positional information. Each component solves a specific problem: attention mixes tokens, feed-forward layers transform each position, residual paths stabilize optimization, masks preserve causality or ignore padding, and positional encodings restore order information that pure attention does not have.

## Definitions

A **query** asks for information, a **key** describes what a value contains, and a **value** is the content to aggregate. Attention computes weights from query-key similarity and returns a weighted sum of values.

In **scaled dot-product attention**, with queries $Q$, keys $K$, and values $V$,

$$
\mathrm{Attention}(Q,K,V)
=
\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

The factor $\sqrt{d_k}$ prevents dot products from growing too large as key dimension increases.

**Additive attention** uses a learned scoring network instead of a dot product. It is useful when query and key dimensions differ.

**Multi-head attention** projects queries, keys, and values into several subspaces, applies attention in each head, concatenates the results, and projects again.

**Self-attention** uses the same sequence as the source of queries, keys, and values. Every token can attend to other tokens in the same sequence.

**Positional encoding** injects token order into the model. D2L presents sinusoidal encodings:

$$
P_{i,2j} = \sin\left(\frac{i}{10000^{2j/d}}\right),
\qquad
P_{i,2j+1} = \cos\left(\frac{i}{10000^{2j/d}}\right).
$$

A **Transformer encoder block** contains multi-head self-attention and a positionwise feed-forward network. A **Transformer decoder block** adds masked self-attention and encoder-decoder attention.

## Key results

Attention pooling generalizes weighted averaging. If a query is similar to a key, the corresponding value receives a larger weight. Since the weights are produced by softmax, they are nonnegative and sum to one along the attended dimension.

The scaled dot-product denominator matters. If entries of $q$ and $k$ have variance near $1$, their dot product has variance roughly $d_k$. Large logits push softmax into saturated regions with tiny gradients. Dividing by $\sqrt{d_k}$ keeps the scale more stable.

Self-attention has short path length between positions. In an RNN, information from token $1$ to token $T$ travels through $T-1$ recurrent steps. In self-attention, token $T$ can attend directly to token $1$ in a single layer. This makes long-range interactions easier to learn, although the $O(T^2)$ attention matrix can be expensive for long sequences.

Masking has two distinct roles. Padding masks prevent attention to artificial padding tokens. Causal masks prevent a decoder position from attending to future target tokens during autoregressive training.

Residual connections and layer normalization are not optional details. They keep deep Transformer stacks trainable by stabilizing activations and gradients.

The query-key-value view also clarifies shape discipline. If a batch has $n$ examples, $T_q$ query positions, $T_k$ key/value positions, and model width $d$, then attention scores have shape $(n,T_q,T_k)$ for each head. The output has one value vector per query position. Self-attention has $T_q=T_k$ because the same sequence supplies all three roles. Encoder-decoder attention has target positions as queries and source positions as keys and values, so target length and source length may differ.

Multi-head attention is not merely running the same attention several times. Each head has its own learned projections, so one head may focus on local syntax, another on long-distance agreement, and another on delimiter or separator tokens. After concatenation, an output projection lets the model recombine those head-specific views. In practice, each head usually has width $d_{\text{model}}/h$, keeping the total projection size comparable to single-head attention.

The positionwise feed-forward network is equally important. Attention mixes information across positions, but the feed-forward block applies a nonlinear transformation independently at each position. A Transformer layer therefore alternates "communicate across tokens" and "transform each token representation." This alternating pattern is why removing either attention or feed-forward sublayers severely weakens the architecture.

Complexity is the main tradeoff. Full self-attention over a sequence of length $T$ forms $T^2$ pairwise scores per head. For sentence-length NLP this is often acceptable, and the parallelism is excellent. For long documents, audio, videos, or high-resolution vision patches, the quadratic matrix becomes expensive in memory and time. Many later architectures modify attention sparsity, chunking, recurrence, or retrieval, but D2L's full-attention formulation is the reference point from which those variants depart.

The encoder-decoder distinction is also practical for debugging. In an encoder block, every source token can attend to every other nonpadding source token. In a decoder block, target self-attention is causal, but encoder-decoder attention is not causal with respect to the source because the full source is already known. Confusing these two masks can produce models that train with leaked future tokens or models that cannot use the full input sequence.

For small examples, writing the attention matrix by hand is often the fastest way to find mistakes. Rows should correspond to query positions, columns to key positions, and each row should sum to one after softmax except where masking has removed all valid keys, which should be avoided.

## Visual

```mermaid
flowchart TD
  X[Token embeddings plus positions] --> MHA[Multi-head self-attention]
  MHA --> Add1[Residual add]
  X --> Add1
  Add1 --> LN1[Layer norm]
  LN1 --> FFN[Positionwise feed-forward]
  FFN --> Add2[Residual add]
  LN1 --> Add2
  Add2 --> LN2[Layer norm]
  LN2 --> Y[Encoder block output]
```

| Mechanism | Mixes positions? | Uses order directly? | Parallel over time? | Typical use |
|---|---|---|---|---|
| CNN | Locally | Through spatial layout | Yes | Images and local patterns |
| RNN | Sequentially | Yes, by recurrence | Limited | Streaming sequences |
| Self-attention | Globally | No, needs positions | Yes | Transformers |
| Causal self-attention | Past positions only | No, needs positions | Yes during training | Autoregressive decoding |
| Encoder-decoder attention | Target queries to source keys | Source order via positions | Yes | Translation and seq2seq |

## Worked example 1: scaled dot-product attention

Problem: one query attends to two key-value pairs. Let

$$
q = [1,1],
\quad
k_1=[1,0],
\quad
k_2=[0,1],
$$

and values

$$
v_1=[10,0],
\quad
v_2=[0,20].
$$

Compute scaled dot-product attention with $d_k=2$.

Method:

1. Compute raw dot products:

$$
qk_1^T = 1(1)+1(0)=1,
\qquad
qk_2^T = 1(0)+1(1)=1.
$$

2. Scale by $\sqrt{2}$:

$$
s_1=s_2=\frac{1}{\sqrt{2}}\approx 0.707.
$$

3. Apply softmax. Since both scores are equal, the weights are equal:

$$
\alpha_1=\alpha_2=0.5.
$$

4. Compute weighted value sum:

$$
0.5[10,0] + 0.5[0,20] = [5,10].
$$

Checked answer: the attention output is $[5,10]$. Equal query-key similarity caused equal averaging of the values.

## Worked example 2: causal mask for decoding

Problem: construct the valid attention pattern for a target sequence of length $4$ in an autoregressive decoder. Position $t$ may attend only to positions $\le t$.

Method:

1. Index positions as $1,2,3,4$.
2. Position $1$ can attend to only $1$.
3. Position $2$ can attend to $1,2$.
4. Position $3$ can attend to $1,2,3$.
5. Position $4$ can attend to $1,2,3,4$.
6. Write the mask as `1` for allowed and `0` for blocked:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 1 & 1 & 0 \\
1 & 1 & 1 & 1
\end{bmatrix}.
$$

Checked answer: the matrix is lower triangular. In implementation, blocked positions are often assigned a large negative score before softmax so their attention weight becomes approximately zero.

## Code

```python
import math
import torch
from torch import nn

torch.manual_seed(5)

batch = 2
time = 4
d_model = 16
heads = 4

x = torch.randn(batch, time, d_model)
self_attn = nn.MultiheadAttention(
    embed_dim=d_model,
    num_heads=heads,
    batch_first=True,
)

causal_mask = torch.triu(
    torch.ones(time, time, dtype=torch.bool),
    diagonal=1,
)
attn_out, attn_weights = self_attn(x, x, x, attn_mask=causal_mask)

ffn = nn.Sequential(
    nn.Linear(d_model, 4 * d_model),
    nn.ReLU(),
    nn.Linear(4 * d_model, d_model),
)
norm1 = nn.LayerNorm(d_model)
norm2 = nn.LayerNorm(d_model)

y = norm1(x + attn_out)
z = norm2(y + ffn(y))

print("output shape:", z.shape)
print("attention weight shape:", attn_weights.shape)
```

## Common pitfalls

- Forgetting positional information and expecting self-attention alone to know token order.
- Using the wrong mask orientation in a decoder. Future tokens must be blocked.
- Applying softmax over the wrong dimension of the attention score matrix.
- Ignoring padding masks, which lets the model attend to artificial padding tokens.
- Treating attention weights as complete explanations. They are useful diagnostics but not proof of causal importance.
- Underestimating the memory cost of the $T \times T$ attention matrix for long sequences.

## Connections

- [Gated RNNs and sequence-to-sequence](/cs/deep-learning/gated-rnns-seq2seq)
- [Pretrained transformers and BERT](/cs/deep-learning/pretrained-transformers-nlp)
- [Natural language processing](/cs/nlp/)
- [Linear algebra](/math/linear-algebra/)
- [Machine learning](/cs/machine-learning/)
