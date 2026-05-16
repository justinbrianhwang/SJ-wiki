## Section: Deep Learning

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/deep-learning/`

### Foundation pages (preserve and enrich)

These are the textbook chapters from the d2l-derived sequence. Do not rename or delete them.

```
intro.md, tensors-data-preprocessing.md, math-for-deep-learning.md, linear-regression-training.md,
softmax-classification-generalization.md, multilayer-perceptrons-regularization.md, pytorch-builders-guide.md,
convolutional-neural-networks.md, modern-cnns.md, sequence-modeling-rnns.md, gated-rnns-seq2seq.md,
lstm-variants.md, attention-transformers.md, pretrained-transformers-nlp.md, optimization-algorithms.md,
computational-performance.md, computer-vision-applications.md, nlp-pretraining-and-applications.md,
generative-adversarial-networks.md, recommender-systems.md, reinforcement-learning-and-bayesian-tuning.md
```

### Paper-named pages to merge then delete

```
vision-transformer.md   → merge into attention-transformers.md (vision section) OR computer-vision-applications.md
rwkv.md                 → likely a new "Efficient sequence modeling" page (see below)
mamba.md                → same
hyena.md                → same
griffin.md              → same
jamba.md                → same
```

### Recommended new topical chapter

Most of `rwkv/mamba/hyena/griffin/jamba` are linear-time / sub-quadratic alternatives to standard attention. They don't fit cleanly into any existing foundation page. **Create a new foundation chapter**:

- Filename: `efficient-sequence-modeling.md`
- `sidebar_position`: 13.5 (between attention-transformers at 13 and pretrained-transformers-nlp at 14, or wherever flows best)
- Title: `"Efficient Sequence Modeling: Linear Attention, SSMs, and Hybrids"`
- Content: textbook-chapter on why standard attention is $O(N^2)$, the families of sub-quadratic alternatives (state-space models, linear attention, gated recurrences, long convolutions, hybrids), with each paper cited inline as `[N]` and a References list at end.

`vision-transformer.md` content can either:
- Merge into `attention-transformers.md` as a "Vision Transformers" sub-section, OR
- Merge into `computer-vision-applications.md` as the "Transformer-based vision" sub-section.

Choose whichever placement makes the resulting page flow better.

### Note about Vaswani et al. 2017

The original Transformer paper was already integrated into `attention-transformers.md` earlier. **Do not change that integration.** When you produce the References list for `attention-transformers.md`, include Vaswani 2017 as one of the entries.

Apply the refactor policy above. Begin now.
