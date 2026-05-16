## Domain: Deep Learning

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/cs/deep-learning/`

### Pages and what to upgrade

Walk through every `.md` in this directory and upgrade Mermaid diagrams to **real architecture level**. Specific guidance per page:

- `multilayer-perceptrons-regularization.md` — MLP with explicit layer dims, batch dim, dropout / weight decay paths.
- `convolutional-neural-networks.md` — LeNet-5 (conv-pool-conv-pool-fc-fc-fc) with channel dims, also a generic Conv-BN-ReLU-Pool block.
- `modern-cnns.md` — AlexNet, VGG-16 / 19, GoogLeNet inception module, **ResNet bottleneck block + ResNet-50 stage diagram**, DenseNet block, MobileNet depthwise-separable block. One detailed Mermaid per architecture.
- `sequence-modeling-rnns.md` — vanilla RNN cell + unrolled-over-time diagram.
- `gated-rnns-seq2seq.md` — **LSTM cell internals** (input gate, forget gate, output gate, cell state, hidden state with the exact equations on the arrows or labels). Plus a seq2seq encoder-decoder pipeline.
- `lstm-variants.md` — peephole LSTM, BiLSTM, stacked LSTM, projection LSTM (LSTMP) — each as a diagram.
- `attention-transformers.md` — **ALREADY DONE**, do not modify.
- `pretrained-transformers-nlp.md` — BERT (encoder-only with `[CLS]`/`[SEP]` tokens, MLM and NSP heads), GPT (decoder-only with causal mask), T5 (encoder-decoder seq2seq with text-to-text framing).
- `optimization-algorithms.md` — Adam optimizer state diagram (first moment, second moment, bias correction), momentum, learning-rate schedules.
- `computational-performance.md` — data parallel / model parallel / pipeline parallel / tensor parallel comparison; mixed precision flow.
- `computer-vision-applications.md` — **U-Net hourglass** with skip connections at every level, R-CNN family (R-CNN / Fast / Faster), YOLO single-shot pipeline, Mask R-CNN.
- `nlp-pretraining-and-applications.md` — pretraining → fine-tuning vs prompting; ELMo / word2vec / BERT.
- `generative-adversarial-networks.md` — Generator + Discriminator adversarial training loop with loss flows; DCGAN architecture.
- `recommender-systems.md` — matrix factorization (user × item embedding), neural CF (NeuMF), two-tower retrieval, candidate generation + ranking pipeline.
- `reinforcement-learning-and-bayesian-tuning.md` — actor-critic loop, DQN target network update, Bayesian optimization with Gaussian process surrogate.
- `efficient-sequence-modeling.md` — **Mamba SSM block** (selective scan), RWKV time-mixing + channel-mixing block, Hyena hierarchy with implicit long convolutions, Griffin gated linear recurrence + local attention block, Jamba layer-interleaving.
- `vision-transformer.md` (if still exists; otherwise skip) — ViT patch embedding + transformer encoder + MLP head.
- `tensors-data-preprocessing.md`, `math-for-deep-learning.md`, `pytorch-builders-guide.md`, `linear-regression-training.md`, `softmax-classification-generalization.md` — these are more foundational; add detailed pipeline diagrams only if they help (training loop, dataloader → forward → loss → backward → optimizer step).

### Notes

- For ResNet, use **realistic stage shapes** (e.g., stage 1: 56×56, stage 2: 28×28, stage 3: 14×14, stage 4: 7×7) and bottleneck-block expansion factor 4.
- For LSTM cell, the gate equations should appear as labels or in a textual block right next to the diagram (gates: $i, f, g, o = \sigma$ or $\tanh$ of $W \cdot [h_{t-1}, x_t] + b$).
- For U-Net, show the contracting path on one side and expanding path on the other with skip connections horizontally at each resolution.
- For Mamba, show input → selective parameters $(A, B, C, \Delta)$ → selective scan → output, with the parallel-scan trick noted as a comment.

Apply the policy above. Begin now.
