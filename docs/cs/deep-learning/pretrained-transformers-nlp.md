---
title: Pretrained Transformers and BERT
sidebar_position: 13
---

# Pretrained Transformers and BERT

D2L moves from the Transformer architecture to large-scale pretraining because modern deep learning often starts from a pretrained model rather than random initialization. Broad self-supervised objectives produce reusable representations; downstream training then adapts those representations to a narrower task. The same pattern now appears in language, vision, and multimodal systems.

BERT represents the encoder-only path, building bidirectional contextual representations through masked language modeling. Sequence-to-sequence models use encoder-decoder pretraining for tasks such as translation and summarization. Decoder-only models train autoregressively and generate text one token at a time.

## Three Transformer output contracts

An **encoder-only Transformer** reads the entire input with bidirectional self-attention and returns contextual representations. BERT is the canonical example. Such models naturally score or classify complete inputs.

A **decoder-only Transformer** uses causal self-attention and predicts the next token:

$$
P(x_1,\ldots,x_T)
=
\prod_{t=1}^{T}P(x_t \mid x_1,\ldots,x_{t-1}).
$$

Its causal mask matches autoregressive generation. An **encoder-decoder Transformer** reads a source sequence bidirectionally, then generates a target through a causal decoder that attends to the encoder outputs.

| Transformer family | Attention direction | Pretraining objective | Best matched tasks |
|---|---|---|---|
| Encoder-only | Bidirectional | Masked token prediction | Classification, retrieval, tagging |
| Encoder-decoder | Source bidirectional, target causal | Denoising or seq2seq | Translation, summarization |
| Decoder-only | Causal | Next-token prediction | Generation, prompting |
| Vision Transformer | Patch self-attention | Supervised or self-supervised | Image classification and transfer |

The output interface should follow the family. Encoder-only models can use both left and right context to score an input. Decoder-only models expose next-token probabilities. Encoder-decoder models produce a transformed sequence conditioned on a source. Forcing a task through a poorly matched interface often adds complexity without improving the model.

## How BERT packs and corrupts its input

A BERT-style input sums three learned vectors at each position: a token embedding, a segment embedding that distinguishes sentence A from sentence B, and a position embedding that supplies order. A special classification token gives task heads a consistent location for reading a sequence-level representation.

![The BERT input representation sums token embeddings, segment embeddings, and position embeddings for a packed sentence-pair sequence.](https://ar5iv.labs.arxiv.org/html/1810.04805/assets/x2.png)

*BERT input representation from [Devlin et al., 2018](https://arxiv.org/abs/1810.04805), reproduced with attribution for study.*

**Masked language modeling** selects input positions, corrupts them, and trains the encoder to recover the original tokens from both left and right context. The original BERT recipe mixes mask-token replacements, random-token replacements, and unchanged selected tokens. Always replacing a selected token with a visible mask symbol would create an easy cue and a mismatch with fine-tuning inputs, where masks usually do not occur.

**Next sentence prediction**, used in the original BERT formulation, asks whether two segments appeared consecutively. Later models often modify or remove the objective, but it remains a useful example of paired-sequence pretraining.

MLM does not factor a sequence probability from left to right, so a BERT-style model is not directly an autoregressive generator. Its bidirectional context instead suits classification, retrieval, tagging, and natural language inference.

## Information flow in BERT, GPT, and T5

```mermaid
flowchart TB
  subgraph BERT["BERT encoder-only pretraining and fine-tuning"]
    direction TB
    BTok["Input tokens: #lsqb;CLS"] sentence A [SEP] sentence B [SEP]"]
    BTok --> BEmb["Token + segment + position embeddings -> (N, T, d_model)"]
    BEmb --> BMask["Bidirectional self-attention mask: padding only"]
    BMask --> BEnc["Transformer encoder stack: e.g. 12 or 24 layers"]
    BEnc --> BCLS["#lsqb;CLS"] representation -> ("N, d_model")"]
    BEnc --> BMasked["Hidden states at masked token positions"]
    BCLS --> NSP["NSP or sentence-pair classification head -> (N, 2)"]
    BMasked --> MLM["MLM head: dense + activation + layer norm + tied vocab projection"]
    MLM --> MLMOut(("Masked-token logits: (M, |V|)"))
    NSP --> NSPOut(("Sentence or task logits"))
  end

  subgraph GPT["GPT decoder-only language model"]
    direction TB
    GTok["Prompt tokens: x_1 ... x_T"] --> GEmb["Token + position embeddings -> (N, T, d_model)"]
    GEmb --> GMask["Causal mask: token t attends only through position t"]
    GMask --> GDec["Transformer decoder blocks: masked self-attention + MLP"]
    GDec --> GHead["Tied linear vocabulary head"]
    GHead --> GOut(("Next-token logits: (N, T, |V|)"))
    GOut -. "sampled token T+1 becomes the next input" .-> GTok
  end

  subgraph T5["T5 text-to-text encoder-decoder"]
    direction TB
    Task["Text prefix + source tokens: e.g. summarize ..."] --> TEncEmb["Encoder token embeddings + relative position bias"]
    TEncEmb --> TEnc["Encoder stack with bidirectional self-attention"]
    TEnc --> Memory["Encoder memory keys and values: (N, S, d_model)"]
    Target["Decoder input: shifted target tokens"] --> TDecEmb["Decoder embeddings"]
    TDecEmb --> TSelf["Masked decoder self-attention"]
    TSelf --> TCross["Cross-attention reads encoder memory"]
    Memory --> TCross
    TCross --> TMLP["Decoder MLP and final normalization"]
    TMLP --> THead["Vocabulary projection"]
    THead --> TOut(("Generated text tokens"))
  end
```

BERT splits its encoder states into token-level MLM predictions and sequence-level heads. GPT feeds causal next-token predictions back into the prompt during generation. T5 gives a causal decoder access to bidirectional source memory through cross-attention. Their masks and output heads define the tasks each family handles most directly.

## Two shape checks for BERT training

### Masked-language-model loss

Suppose an MLM assigns probabilities $0.20$ and $0.50$ to the correct tokens at two selected positions. Cross-entropy is computed over those positions only:

$$
\ell_1 = -\log(0.20) \approx 1.609,
$$

$$
\ell_2 = -\log(0.50) \approx 0.693,
$$

and

$$
\bar{\ell}
=
\frac{1.609 + 0.693}{2}
= 1.151.
$$

Unmasked tokens supply context but usually make no direct contribution to the prediction loss.

### Classification-head dimensions

Let $h_{\mathrm{CLS}} \in \mathbb{R}^{768}$ feed a three-class sentiment head. In PyTorch, `nn.Linear(768, 3)` stores a weight of shape `(3, 768)` and a bias of shape `(3)`. For a batch representation of shape `(32, 768)`, the mathematical multiplication is

$$
(32,768) \times (768,3) \rightarrow (32,3).
$$

The head has

$$
3 \cdot 768 + 3 = 2307
$$

trainable parameters, and each row of the output contains one logit per sentiment class.

## Reusing a pretrained representation

**Fine-tuning** continues training the pretrained model on task-specific data. **Feature extraction** freezes the base and trains only a smaller head. Full fine-tuning can adapt more strongly, but it uses more memory and can overfit or forget useful features on a tiny, narrow dataset. A frozen encoder is cheaper and more stable, though it may under-adapt.

For classification, a BERT-style head commonly computes

$$
o = W h_{\mathrm{CLS}} + b.
$$

Cross-entropy trains the head; during full fine-tuning, its gradients also reshape the encoder's internal features. Parameter-efficient methods occupy the middle ground by updating a small subset of added or selected parameters.

Transfer depends on the relation between pretraining and downstream data. Broad web text may transfer well to general sentiment analysis and poorly to biomedical, legal, or code tasks. Continued pretraining on unlabeled in-domain text can help, but a narrow corpus may over-specialize the model.

Scaling also involves more than layer count. Dataset composition, tokenizer, context length, optimizer schedule, batch size, and evaluation protocol all affect the result. Larger models do not automatically transfer better under fixed data and compute budgets.

## A small encoder classifier in PyTorch

```python
import torch
from torch import nn

torch.manual_seed(6)

batch = 4
time = 8
vocab_size = 100
d_model = 32
classes = 3

tokens = torch.randint(0, vocab_size, (batch, time))
positions = torch.arange(time).unsqueeze(0).expand(batch, time)
segments = torch.zeros_like(tokens)

token_embed = nn.Embedding(vocab_size, d_model)
pos_embed = nn.Embedding(time, d_model)
seg_embed = nn.Embedding(2, d_model)

encoder_layer = nn.TransformerEncoderLayer(
    d_model=d_model,
    nhead=4,
    dim_feedforward=128,
    batch_first=True,
)
encoder = nn.TransformerEncoder(encoder_layer, num_layers=2)
classifier = nn.Linear(d_model, classes)

x = token_embed(tokens) + pos_embed(positions) + seg_embed(segments)
encoded = encoder(x)
cls_rep = encoded[:, 0, :]
logits = classifier(cls_rep)

labels = torch.randint(0, classes, (batch,))
loss = nn.CrossEntropyLoss()(logits, labels)
loss.backward()
print("logits:", logits.shape)
print("loss:", loss.item())
```

## Where reproductions usually diverge

Tokenization must match pretraining; changing the vocabulary or segmentation scheme invalidates the learned embedding interface. Paired-input encoders also need the intended segment and position information. MLM loss belongs only on selected prediction positions, not every token.

A BERT-style masked model should not be evaluated as though it were a left-to-right generator. Small-data fine-tuning needs validation monitoring and regularization, especially when every encoder parameter is updated. These checks matter more than copying the nominal layer count while changing the data path or loss.

<div className="see-also">

See also: [Attention and transformers](/cs/deep-learning/attention-transformers) · [NLP pretraining and applications](/cs/deep-learning/nlp-pretraining-and-applications) · [Natural language processing](/cs/nlp/intro) · [Machine learning](/cs/machine-learning/intro) · [Probability and random variables](/math/probability-and-random-variables/intro)

</div>
