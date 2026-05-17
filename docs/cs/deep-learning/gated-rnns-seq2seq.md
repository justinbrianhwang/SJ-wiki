---
title: Gated RNNs and Sequence-to-Sequence
sidebar_position: 11
---

# Gated RNNs and Sequence-to-Sequence

Basic RNNs carry hidden states through time, but they struggle to preserve useful information over long spans. D2L addresses this with gated recurrent units and long short-term memory networks, then uses recurrent encoders and decoders for machine translation. The result is the classic sequence-to-sequence pattern: one network reads an input sequence into a state representation, and another network generates an output sequence.

This page is a bridge between vanilla recurrence and attention-based models. Gating explains how neural networks can decide what to remember, what to forget, and what to expose. Encoder-decoder training introduces teacher forcing, padding masks, sequence loss, and decoding. Beam search then shows that prediction is not just a forward pass; it is a search problem over possible output sequences.

## Definitions

A **GRU** modifies the RNN hidden-state update using gates. With input $X_t$ and previous hidden state $H_{t-1}$, the reset gate $R_t$ and update gate $Z_t$ are

$$
R_t = \sigma(X_tW_{xr} + H_{t-1}W_{hr} + b_r),
$$

$$
Z_t = \sigma(X_tW_{xz} + H_{t-1}W_{hz} + b_z).
$$

The candidate hidden state is

$$
\tilde{H}_t =
\tanh(X_tW_{xh} + (R_t \odot H_{t-1})W_{hh} + b_h),
$$

and the final hidden state is

$$
H_t = Z_t \odot H_{t-1} + (1-Z_t)\odot \tilde{H}_t.
$$

An **LSTM** uses a memory cell $C_t$ and gates for input, forget, and output. The forget gate controls how much old memory survives; the input gate controls how much new content enters; the output gate controls how much cell content is exposed as hidden state.

A **deep RNN** stacks recurrent layers. A **bidirectional RNN** processes a sequence left-to-right and right-to-left, then combines both representations.

An **encoder-decoder** model maps an input sequence to an output sequence. The encoder reads the source sequence. The decoder predicts target tokens, usually conditioned on encoder state and previous target tokens.

**Teacher forcing** trains the decoder using the true previous target token as input. **Beam search** keeps the best $k$ partial sequences during decoding rather than committing to only the best next token.

## Key results

The update gate in a GRU creates a direct interpolation between old and candidate state. If $Z_t$ is close to $1$, then

$$
H_t \approx H_{t-1}.
$$

If $Z_t$ is close to $0$, then

$$
H_t \approx \tilde{H}_t.
$$

This lets the model preserve information over many time steps when needed, reducing the vanishing-gradient problem compared with a plain RNN.

The LSTM cell gives memory an additive path:

$$
C_t = F_t \odot C_{t-1} + I_t \odot \tilde{C}_t.
$$

The additive form makes it easier to carry memory forward than repeatedly applying only nonlinear transformations. This is why LSTMs became a standard sequence model before transformers became dominant.

Sequence-to-sequence training minimizes token-level cross-entropy, but padding tokens should not contribute to the loss. If a target has valid length $m$ and padded length $T$, the masked loss is

$$
\sum_{t=1}^{T} \mathbf{1}(t \le m)\ell_t.
$$

Greedy decoding chooses the best next token at each step. It is cheap but can miss the best full sequence because a locally strong token may lead to a poor continuation. Beam search approximates global sequence search by maintaining multiple candidates.

GRUs and LSTMs solve related problems with different internal structure. A GRU combines memory and hidden state in one vector, so it has fewer gates and often trains faster. An LSTM separates the cell state from the exposed hidden state, giving it a more explicit memory path. Which works better is empirical; D2L presents both because the gate equations reveal the design space.

Bidirectional RNNs are powerful encoders but not ordinary left-to-right generators. A bidirectional layer can represent a source sentence for translation because the whole source is known before decoding. It cannot be used directly to generate the next token in a causal language model because the backward direction would look at future tokens. This distinction foreshadows the difference between encoder attention and causal decoder attention in Transformers.

Machine translation also introduces vocabulary and length issues. Source and target languages usually have different vocabularies, and a target sentence may be shorter or longer than its source. Special tokens such as `<bos>`, `<eos>`, and `<pad>` define sequence boundaries and batching behavior. The decoder should learn when to stop by predicting `<eos>`, not by relying on a fixed output length.

The fixed-context encoder-decoder is limited because the entire source sequence must be compressed into a small set of final states. For short sentences this can work, but long sentences strain the bottleneck. Attention was originally introduced for neural machine translation to let the decoder consult encoder states at every output step. Thus D2L's progression from seq2seq to attention is not arbitrary; it fixes a concrete weakness of the basic encoder-decoder.

Loss masking is part of the model objective. Padding lets variable-length sequences share a batch, but padded positions do not represent target tokens. If they contribute loss, the model can learn to predict padding too strongly or distort perplexity. Correct valid lengths, masks, and target shifting are therefore as important as the recurrent cell equations.

## Visual

```mermaid
flowchart TB
  subgraph LSTM["LSTM cell internals at time t"]
    direction TB
    X["Input x_t: #lsqb;N, d_x"]"] --> Cat["Concatenate #lsqb;h_{t-1}, x_t"]"]
    Hprev["Previous hidden h_{t-1}: #lsqb;N, d_h"]"] --> Cat
    Cprev["Previous cell C_{t-1}: #lsqb;N, d_h"]"] -. "linear memory path" .-> ForgetMul(("Elementwise multiply"))

    Cat --> F["Forget gate f_t = sigmoid(W_f #lsqb;h_{t-1}, x_t"] + b_f)"]
    Cat --> I["Input gate i_t = sigmoid(W_i #lsqb;h_{t-1}, x_t"] + b_i)"]
    Cat --> G["Candidate g_t = tanh(W_g #lsqb;h_{t-1}, x_t"] + b_g)"]
    Cat --> O["Output gate o_t = sigmoid(W_o #lsqb;h_{t-1}, x_t"] + b_o)"]

    F --> ForgetMul
    Cprev --> ForgetMul
    I --> InMul(("Elementwise multiply"))
    G --> InMul
    ForgetMul --> Cadd(("Add cell contributions"))
    InMul --> Cadd
    Cadd --> Ct["Cell C_t = f_t*C_{t-1} + i_t*g_t"]
    Ct --> TanhC["tanh(C_t)"]
    O --> OutMul(("Elementwise multiply"))
    TanhC --> OutMul
    OutMul --> Ht["Hidden h_t = o_t*tanh(C_t)"]
  end

  subgraph Seq2Seq["Encoder-decoder sequence-to-sequence pipeline"]
    direction LR
    Src["Source tokens: #lsqb;x_1 ... x_n"]"] --> SrcEmb["Source embedding + mask"]
    SrcEmb --> Enc["Encoder RNN/LSTM unrolled over source"]
    Enc --> Context["Final encoder state(s): h_n and C_n"]
    Context --> DecInit["Initialize decoder state"]
    Bos["BOS token then previous target tokens"] --> TgtEmb["Target embedding"]
    TgtEmb --> Dec["Decoder RNN/LSTM unrolled over target"]
    DecInit --> Dec
    Dec --> Proj["Linear vocabulary projection"]
    Proj --> Pred(("Predicted y_1 ... EOS"))
  end
```

![An LSTM chain diagram shows repeating cells with gates controlling memory update, forgetting, and hidden-state output over time.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png)

*Figure: LSTM cell chain visualization from [Christopher Olah, 2015](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — embedded under educational fair use with attribution.*

The LSTM cell diagram shows all four gate computations from the concatenated `[h_{t-1}, x_t]` input and the additive memory update `C_t = f_t*C_{t-1} + i_t*g_t`. The dotted path highlights the cell state's nearly direct route through time, while the output gate controls what part of `tanh(C_t)` becomes the exposed hidden state. The seq2seq subgraph then shows how encoder final states initialize the decoder, with teacher-forced target tokens feeding the decoder during training.

| Model | Extra state or gates | Strength | Limitation |
|---|---|---|---|
| Plain RNN | Hidden state only | Simple recurrent baseline | Vanishing/exploding gradients |
| GRU | Reset and update gates | Fewer gates than LSTM | Less explicit memory cell |
| LSTM | Cell plus input/forget/output gates | Strong long-range memory | More parameters |
| Deep RNN | Multiple recurrent layers | Hierarchical sequence features | Slower and harder to train |
| Bidirectional RNN | Forward and backward states | Uses both contexts | Not causal for generation |
| Encoder-decoder | Separate reader and writer | Variable-length translation | Fixed context bottleneck without attention |

## Worked example 1: GRU update gate interpolation

Problem: a one-dimensional GRU has previous hidden state $H_{t-1}=10$, candidate state $\tilde{H}_t=2$, and update gate $Z_t=0.75$. Compute $H_t$.

Method:

1. Use the GRU interpolation formula:

$$
H_t = Z_tH_{t-1} + (1-Z_t)\tilde{H}_t.
$$

2. Substitute values:

$$
H_t = 0.75(10) + (1-0.75)(2).
$$

3. Compute the old-state contribution:

$$
0.75(10)=7.5.
$$

4. Compute the candidate contribution:

$$
0.25(2)=0.5.
$$

5. Add:

$$
H_t = 7.5 + 0.5 = 8.
$$

Checked answer: the new hidden state is $8$. Since the update gate is close to $1$, the GRU mostly preserves the old state.

## Worked example 2: beam search with width two

Problem: decode two time steps with beam width $2$. At step 1, candidate log probabilities are `A: -0.1`, `B: -0.7`, `C: -1.2`. At step 2, extensions have log probabilities:

| prefix | next X | next Y |
|---|---:|---:|
| A | -0.6 | -1.0 |
| B | -0.2 | -0.4 |

Find the top two length-two sequences.

Method:

1. Keep the top two prefixes after step 1: `A` with score $-0.1$ and `B` with score $-0.7$. Drop `C`.
2. Extend `A`:

$$
\mathrm{score}(AX) = -0.1 + (-0.6) = -0.7,
$$

$$
\mathrm{score}(AY) = -0.1 + (-1.0) = -1.1.
$$

3. Extend `B`:

$$
\mathrm{score}(BX) = -0.7 + (-0.2) = -0.9,
$$

$$
\mathrm{score}(BY) = -0.7 + (-0.4) = -1.1.
$$

4. Rank all length-two candidates by log score. Higher is better because log probabilities are negative:

$$
AX:-0.7,\quad
BX:-0.9,\quad
AY:-1.1,\quad
BY:-1.1.
$$

Checked answer: the beam keeps `AX` and `BX`. Greedy search would also start with `A`, but beam search preserves `B` as an alternate path because it could lead to a stronger continuation.

## Code

```python
import torch
from torch import nn

torch.manual_seed(4)

src_vocab = 30
tgt_vocab = 35
batch_size = 3
src_len = 5
tgt_len = 6
embed_size = 8
hidden_size = 16

encoder = nn.GRU(embed_size, hidden_size, batch_first=True)
decoder = nn.GRU(embed_size, hidden_size, batch_first=True)
src_embed = nn.Embedding(src_vocab, embed_size)
tgt_embed = nn.Embedding(tgt_vocab, embed_size)
classifier = nn.Linear(hidden_size, tgt_vocab)

src = torch.randint(0, src_vocab, (batch_size, src_len))
tgt = torch.randint(0, tgt_vocab, (batch_size, tgt_len))

_, enc_state = encoder(src_embed(src))
dec_inputs = tgt[:, :-1]
dec_targets = tgt[:, 1:]
dec_outputs, _ = decoder(tgt_embed(dec_inputs), enc_state)
logits = classifier(dec_outputs)

loss = nn.CrossEntropyLoss()(
    logits.reshape(-1, tgt_vocab),
    dec_targets.reshape(-1),
)
loss.backward()
print("sequence loss:", loss.item())
print("logits shape:", logits.shape)
```

## Common pitfalls

- Using bidirectional encoder states in a decoder without correctly combining directions.
- Computing loss on padded positions instead of masking them.
- Forgetting that teacher forcing uses true previous tokens during training but generated previous tokens during inference.
- Comparing beam-search scores across different lengths without length normalization when appropriate.
- Treating GRU and LSTM hidden states as interchangeable; LSTM returns both hidden state and cell state.
- Carrying hidden states across unrelated sequences in a shuffled batch.

## Connections

- [Sequence modeling and RNNs](/cs/deep-learning/sequence-modeling-rnns)
- [Attention and transformers](/cs/deep-learning/attention-transformers)
- [Natural language processing](/cs/nlp/)
- [Reinforcement learning](/cs/reinforcement-learning/)
- [Probability and random variables](/math/probability-and-random-variables/)
