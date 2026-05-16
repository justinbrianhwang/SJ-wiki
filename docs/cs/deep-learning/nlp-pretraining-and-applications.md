---
title: NLP Pretraining and Applications
sidebar_position: 17
---

# NLP Pretraining and Applications

D2L's NLP application chapters connect representation learning to downstream language tasks. Before transformers became dominant, word embeddings such as word2vec and GloVe showed that useful semantic structure could be learned from unlabeled text. Modern systems extend that idea with contextual encoders and task-specific fine-tuning for sentiment analysis, natural language inference, and sequence-to-sequence prediction.

The common thread is that text must be represented numerically while preserving enough linguistic structure to support the task. A bag of words can work for simple sentiment problems, but it loses order and context. Static embeddings represent each word type with one vector. Contextual models represent each token occurrence based on surrounding tokens. Applications differ in output structure, but they all depend on tokenization, vocabulary handling, batching, masking, and loss design.

## Definitions

A **token** is a unit of text such as a character, word, or subword. A **vocabulary** maps tokens to integer ids. An **embedding matrix** $E \in \mathbb{R}^{\vert \mathcal{V}\vert  \times d}$ maps each token id to a vector.

**Skip-gram word2vec** predicts context words from a center word. Given center word $w_c$ and context word $w_o$, the model scores them by an embedding dot product. Negative sampling trains the model to distinguish observed context pairs from sampled noise pairs.

For one positive pair and negative words $w_1,\ldots,w_K$, the negative-sampling objective is

$$
-\log \sigma(u_o^T v_c)
-\sum_{k=1}^{K}\log \sigma(-u_k^T v_c),
$$

where $v_c$ is the center embedding and $u$ vectors are output embeddings.

**GloVe** learns embeddings from global co-occurrence counts. Its objective encourages word-vector dot products to match transformed co-occurrence statistics.

**Subword embeddings** represent words through smaller units, improving coverage for rare and morphologically related words.

**Sentiment analysis** predicts polarity or rating from text. **Natural language inference** predicts whether a hypothesis is entailed by, contradicted by, or neutral with respect to a premise.

**Fine-tuning** adapts a pretrained representation model to a labeled task, often by adding a classification head and training with cross-entropy.

## Key results

Word embeddings work because distributional patterns carry meaning: words appearing in similar contexts often have related meanings. Skip-gram and GloVe optimize different objectives, but both place words in vector spaces where dot products or cosine similarity reflect contextual association.

Negative sampling avoids a full softmax over the entire vocabulary for every center-context pair. Instead of normalizing over all words, it trains a binary classifier over observed and sampled pairs. This makes word2vec scalable to large corpora.

Static embeddings have a limitation: one vector must represent every sense of a word. The word "bank" has different meanings in financial and river contexts, but a static embedding averages across uses. Contextual encoders address this by producing token representations conditioned on the sentence.

For sentiment classification, sequence encoders can use pooling, recurrent final states, convolutional features, or a special classification token. The classifier head maps a document representation to logits. Cross-entropy remains the standard loss when labels are categorical.

Natural language inference requires modeling a pair of sequences and their interaction. Simple concatenation can work as a baseline, but attention or transformer encoders give the model direct comparison paths between premise and hypothesis tokens.

Data preprocessing is unusually important in NLP. Tokenization choices change sequence lengths, vocabulary size, unknown-token rate, and evaluation comparability. Padding masks must be correct so models do not learn from artificial padding.

Subsampling frequent words is another word2vec idea. Very common tokens such as articles and punctuation appear in many contexts but carry limited semantic specificity. Downsampling them reduces training cost and lets informative context pairs have more influence. Negative samples are often drawn from a smoothed unigram distribution so common words appear often enough to be useful but not so often that they dominate.

For downstream tasks, batching text requires careful length handling. Sorting or bucketing by length can reduce padding waste. Masks should travel with the batch so encoders, attention layers, and loss functions know which positions are real. This is especially important for NLI and sentence-pair tasks where two sequences may be concatenated with separator tokens and segment ids.

The task head should match the prediction target. Sentiment analysis usually uses a sequence-level head. Token tagging uses a per-token head. Sequence-to-sequence tasks use a decoder that predicts a distribution at every target time step. Many implementation errors come from using a representation with the wrong granularity for the label structure.

Static embeddings can also encode corpus biases. If the training text reflects social stereotypes or domain-specific associations, vector similarities can reproduce them. This matters when embeddings are reused in downstream classifiers. D2L's focus is technical, but practical NLP systems should treat pretrained representations as learned artifacts of their data, not neutral dictionaries.

Natural language inference is a useful stress test because lexical overlap is not enough. A premise and hypothesis may share many words while contradicting each other, or use different words while expressing entailment. Models need mechanisms for alignment, negation, quantifiers, and sentence-pair interaction. Transformer encoders handle this by letting tokens in both segments attend to one another after concatenation with segment markers.

For applied NLP, error analysis should include actual text examples. Aggregate accuracy can hide failures on negation, rare words, long inputs, domain-specific terms, or mislabeled examples. Inspecting mistakes often suggests whether the bottleneck is tokenization, representation, model capacity, or data quality.

## Visual

```mermaid
flowchart TB
  Raw["Raw corpus or task text"] --> Tok["Tokenize: word, character, or subword units"]
  Tok --> IDs["Vocabulary ids + padding mask"]

  subgraph Static["Static embedding pretraining"]
    direction TB
    IDs --> W2V["word2vec skip-gram: center id -> embedding v_c"]
    W2V --> Dot["Dot with context embeddings u_o and negatives u_k"]
    Dot --> NSLoss["Negative-sampling binary loss"]
    NSLoss --> StaticEmb["#quot;Static word vector table E: [|V|, d"]"]
  end

  subgraph ELMo["ELMo-style contextual features"]
    direction TB
    IDs --> CharCNN["Character CNN or token embedding"]
    CharCNN --> FwdLM["Forward LM LSTM"]
    CharCNN --> BwdLM["Backward LM LSTM"]
    FwdLM --> ELMoCat["Layer-weighted concat of forward/backward states"]
    BwdLM --> ELMoCat
    ELMoCat --> ELMoFeat["#quot;Contextual token features [N, T, d_ctx"]"]
  end

  subgraph BERTFlow["BERT-style contextual encoder"]
    direction TB
    IDs --> BEmb["Token + segment + position embeddings"]
    BEmb --> BEnc["Bidirectional Transformer encoder"]
    BEnc --> MLM["Pretraining head: masked token logits"]
    BEnc --> CLS["#quot;[CLS"] sequence representation"]
  end

  subgraph Adapt["Using pretrained representations"]
    direction TB
    StaticEmb --> FT["Fine-tuning path: add task head and update selected parameters"]
    ELMoFeat --> FT
    CLS --> FT
    CLS --> Prompt["Prompting path: format task as text and read model output"]
    FT --> Head["Task head: sentiment, NLI, tagging, or seq2seq"]
    Prompt --> Head
    Head --> Out(("Task predictions"))
  end
```

The diagram separates static embedding training, ELMo-style bidirectional recurrent features, and BERT-style bidirectional transformer pretraining. The adaptation subgraph shows the two main downstream patterns: fine-tuning with a task head versus prompting by formatting the task as text. Shape labels distinguish vocabulary tables, contextual token sequences, and sequence-level `[CLS]` representations.

| Representation | Contextual? | Handles rare words | Typical use |
|---|---|---|---|
| One-hot token | No | Poorly | Input to embedding lookup |
| word2vec | No | Depends on vocabulary | Static semantic features |
| GloVe | No | Depends on co-occurrence data | Static semantic features |
| Subword embedding | Partly | Better | Open-vocabulary modeling |
| RNN hidden states | Yes | With embeddings | Sequence classification/generation |
| Transformer states | Yes | With subword tokenization | Modern NLP fine-tuning |

## Worked example 1: negative sampling loss

Problem: a skip-gram model has center vector $v_c=[1,2]$, positive output vector $u_o=[2,0]$, and one negative output vector $u_n=[0,1]$. Compute the negative-sampling loss.

Method:

1. Compute positive score:

$$
u_o^T v_c = [2,0]\cdot[1,2] = 2.
$$

2. Positive loss:

$$
-\log\sigma(2).
$$

Since $\sigma(2)=\frac{1}{1+e^{-2}}\approx 0.881$,

$$
-\log(0.881)\approx 0.127.
$$

3. Compute negative score:

$$
u_n^T v_c = [0,1]\cdot[1,2] = 2.
$$

4. Negative loss uses $-\log \sigma(-u_n^Tv_c)$:

$$
-\log\sigma(-2).
$$

Since $\sigma(-2)\approx 0.119$,

$$
-\log(0.119)\approx 2.127.
$$

5. Total loss:

$$
0.127 + 2.127 = 2.254.
$$

Checked answer: the loss is about $2.254$. The negative pair is costly because the model currently gives it a high dot-product score.

## Worked example 2: sentiment classifier dimensions

Problem: a sentiment model embeds a padded review of length $50$ with embedding size $100$, mean-pools over valid tokens, and predicts $2$ classes. For a batch of $32$, find the main tensor shapes and classifier parameter count.

Method:

1. Token ids have shape `(32, 50)`.
2. The embedding lookup returns shape `(32, 50, 100)`.
3. A padding-aware mean over the time dimension returns one vector per review:

$$
(32,50,100) \rightarrow (32,100).
$$

4. A linear classifier maps $100$ features to $2$ logits. Its weight shape is `(2, 100)` and bias shape is `(2)`.
5. Parameter count:

$$
2 \cdot 100 + 2 = 202.
$$

6. Batch logits have shape `(32, 2)`.

Checked answer: the pooled review representation is `(32, 100)`, the logits are `(32, 2)`, and the classifier has $202$ parameters.

## Code

```python
import torch
from torch import nn
from torch.nn import functional as F

torch.manual_seed(8)

vocab_size = 50
embed_size = 16
batch = 4
negatives = 3

center = torch.randint(0, vocab_size, (batch,))
positive = torch.randint(0, vocab_size, (batch,))
negative = torch.randint(0, vocab_size, (batch, negatives))

center_embed = nn.Embedding(vocab_size, embed_size)
context_embed = nn.Embedding(vocab_size, embed_size)

v = center_embed(center)
u_pos = context_embed(positive)
u_neg = context_embed(negative)

pos_score = (v * u_pos).sum(dim=1)
neg_score = torch.bmm(u_neg, v.unsqueeze(2)).squeeze(2)

loss = -F.logsigmoid(pos_score).mean() - F.logsigmoid(-neg_score).mean()
loss.backward()

print("negative sampling loss:", loss.item())
print("center embedding gradient shape:", center_embed.weight.grad.shape)
```

## Common pitfalls

- Comparing NLP model results without matching tokenization and preprocessing.
- Averaging padded token embeddings as if padding were real text.
- Treating static word embeddings as context-sensitive.
- Using a full vocabulary softmax for word2vec-style training when negative sampling is intended.
- Fine-tuning a large encoder with too high a learning rate on a small labeled dataset.
- Assuming sentiment analysis, NLI, and translation need the same output head.

## Connections

- [Pretrained transformers and BERT](/cs/deep-learning/pretrained-transformers-nlp)
- [Attention and transformers](/cs/deep-learning/attention-transformers)
- [Sequence modeling and RNNs](/cs/deep-learning/sequence-modeling-rnns)
- [Natural language processing](/cs/nlp/)
- [Probability and random variables](/math/probability-and-random-variables/)
