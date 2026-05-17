You are adding **paper architecture figures** to the deep-learning section of SJ Wiki.

## Target

`f:/coding/SJ Wiki/docs/cs/deep-learning/`
Also: `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/` (secondary; only fill missing models)

## What to do

Read the **MODEL ARCHITECTURE FIGURES POLICY** above. For each named model in this section's pages, embed the paper's architecture figure with full caption + attribution. Place at the top of the named-model subsection.

## Models to cover (deep learning)

Confirmed mappings (use these):

### Computer vision backbones — `modern-cnns.md`, `convolutional-neural-networks.md`, `computer-vision-applications.md`
- **ResNet** (`1512.03385`, `x1.png`) — try `x2.png` if `x1` is just a teaser
- **GoogLeNet / Inception** (`1409.4842`, `x2.png` for inception module; `x3.png` for full)
- **VGG** (`1409.1556`, `x1.png`)
- **DenseNet** (`1608.06993`, `x1.png` block; `x2.png` full)
- **MobileNet** (`1704.04861`, `x1.png`)
- **EfficientNet** (`1905.11946`, `x1.png`)
- **U-Net** (`1505.04597`, `x1.png` — the iconic U shape)
- **Faster R-CNN** (`1506.01497`, `x2.png`)
- **Mask R-CNN** (`1703.06870`, `x1.png`)
- **YOLO v1** (`1506.02640`, `x2.png` or `x3.png`)
- **ViT** (`2010.11929`, `x1.png`)
- **Swin** (`2103.14030`, `x1.png`)
- **ConvNeXt** (`2201.03545`, `x1.png`)

### Sequence models — `attention-transformers.md`, `efficient-sequence-modeling.md`, `lstm-variants.md`, `sequence-modeling-rnns.md`, `pretrained-transformers-nlp.md`
- **Transformer** — already embedded in `attention-transformers.md`.
- **BERT** — already in `pretrained-transformers-nlp.md`. Confirm not duplicated elsewhere.
- **Mamba** (`2312.00752`, `x1.png` or `x3.png`)
- **RWKV** — already embedded.
- **Hyena** (`2302.10866`, `x1.png`)
- **LSTM / GRU** — usually no good arxiv figure (Hochreiter 1997). Skip or use Wikimedia `LSTM_Cell.svg`.

### Generative — `generative-adversarial-networks.md`
- **DCGAN** — already embedded.
- **StyleGAN** (`1812.04948`, `x1.png`)
- **DDPM** (`2006.11239`, `x2.png`)
- **Latent Diffusion / Stable Diffusion** (`2112.10752`, `x3.png`)
- **VAE** — use Wikimedia `Variational-AutoEncoder.png` if you remember it; else skip.

### RL in DL — `reinforcement-learning-and-bayesian-tuning.md`
- **DQN** (`1312.5602`, `x1.png` if it exists)
- **A3C** (`1602.01783`, `x1.png`)
- **Dreamer** (`2010.02193`, `x2.png`)
- **MuZero** (`1911.08265`, `x2.png`)

## Adversarial-attacks (secondary fill)

Most pages already have FGSM and patch figures. Add to `white-box-attacks.md` if missing:
- **PGD** (`1706.06083`, `x1.png` — loss landscape figure)
- **AutoAttack** (`2003.01690`, `x1.png`) — to `evaluation-and-benchmarks.md`
- **TRADES** (`1901.08573`, `x1.png`) — to `adversarial-training.md`

## Format (mandatory)

```markdown
![<descriptive alt text>](https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png)

*Figure: <one-line description>. From [Author et al., Year](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
```

## Verification (mandatory)

After all edits, run:

```bash
python tools/check-image-urls.py docs/cs/deep-learning/ docs/cs/adversarial-attacks/ 2>&1 | grep BROKEN
```

For each BROKEN URL: try `x1.png` → `x2.png` → `x3.png` in order. If none work, remove the embed. Never push a broken URL.

## Output

Final summary table:

```
Pages touched: N
Figures embedded: M (ar5iv: M-k, Wikimedia: k)
Broken URLs found and removed: x
Models skipped (no good source): list
```

## Constraints

- Stay inside `docs/cs/deep-learning/` and `docs/cs/adversarial-attacks/`.
- Don't touch existing Mermaid diagrams or other content.
- Don't duplicate already-embedded figures.
- Don't fabricate arxiv IDs or figure numbers.

Begin now.
