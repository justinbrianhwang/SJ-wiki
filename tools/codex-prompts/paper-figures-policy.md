## PAPER FIGURE EMBED POLICY for SJ Wiki

The user wants real paper figures embedded directly (with attribution) where they would help readers understand the topic. PyTorch tutorials, distill.pub, course slides, and Wikipedia all routinely do this under educational fair use. We follow the same practice: **embed publicly hosted figures with full attribution and a source link**.

### Allowed sources

Embed only from publicly reachable, reasonably stable hosts:

1. **Wikimedia Commons** — already used; safe and explicitly CC-licensed.
2. **arxiv ar5iv HTML renders** — `https://ar5iv.labs.arxiv.org/html/<arxiv-id>` exposes images at paths like `https://ar5iv.labs.arxiv.org/html/<id>/<x><number>.png`. arxiv provides perpetual distribution rights; reuse with attribution is widely practiced for educational sites.
3. **Paper companion GitHub repos** when the authors host figures publicly (e.g., `https://github.com/<authors>/<repo>/blob/main/figures/<name>.png?raw=1`).
4. **Author homepages / project websites** with explicit public/educational sharing.
5. **PyTorch / TensorFlow / Hugging Face tutorial figures** — typically Apache 2.0 / MIT licensed and explicitly intended for reuse.
6. **distill.pub** — published under CC BY 4.0.

**Do NOT** embed from:
- Random blog posts.
- Journal publisher CDNs (Nature, Science, IEEE) — copyrighted.
- Slideshare / personal slide decks — copyright unclear.

### Required format

```markdown
![Descriptive alt text — full sentence describing what the figure shows.](IMAGE_URL)

*Figure: Brief description. From [Author et al., Year](paper-url) — embedded under educational fair use with attribution.*
```

The caption MUST include:
- The author(s) and year
- A link to the original paper / source page
- "embedded under educational fair use with attribution" (or "CC BY ..." if the source is explicitly licensed)

### Where to add figures (priority pages)

Focus on pages where a real figure dramatically helps:

#### Adversarial Attacks (high priority — user's example)
- `white-box-attacks.md`: **Goodfellow et al. 2014 "panda + perturbation = gibbon"** figure from FGSM paper. arxiv:1412.6572. Use ar5iv link.
- `physical-world-and-patch-attacks.md`: Eykholt et al. stop-sign with sticker patches (arxiv:1707.08945). Brown et al. adversarial patch (arxiv:1712.09665).
- `attacks-on-llms-and-other-modalities.md`: example jailbreak prompts (with care).
- `evaluation-and-benchmarks.md`: AutoAttack ensemble diagram if the paper has one.

#### Deep Learning architectures (high priority)
- `attention-transformers.md`: Vaswani et al. 2017 original Transformer figure (arxiv:1706.03762, ar5iv-hosted). Keep our detailed Mermaid too.
- `modern-cnns.md`: ResNet residual block (He et al. 2015, arxiv:1512.03385); DenseNet block (arxiv:1608.06993); VGG, GoogLeNet inception, MobileNet depthwise figures.
- `convolutional-neural-networks.md`: LeNet-5 figure (LeCun classic, often hosted on author homepage).
- `gated-rnns-seq2seq.md`: Olah's LSTM cell figure (his blog is CC BY).
- `vision-transformer.md` (if exists) / inside attention-transformers vision section: ViT patch figure from Dosovitskiy 2020 (arxiv:2010.11929).
- `efficient-sequence-modeling.md`: Mamba selective SSM diagram (arxiv:2312.00752); RWKV time-mix (arxiv:2305.13048); Hyena hierarchy (arxiv:2302.10866).
- `pretrained-transformers-nlp.md`: BERT input representation (Devlin 2018); GPT pretrain/finetune.
- `generative-adversarial-networks.md`: GAN architecture from Goodfellow 2014; DCGAN figure (Radford 2016).
- `computer-vision-applications.md`: U-Net figure (Ronneberger 2015); R-CNN family figure; YOLO figure (Redmon 2016).

#### Autonomous Driving (high priority)
- `perception-object-detection-and-segmentation.md`: PointPillars architecture (arxiv:1812.05784); CenterPoint (arxiv:2006.11275).
- `prediction-and-motion-forecasting.md`: VectorNet (arxiv:2005.04259); HiVT (CVPR 2022).
- `end-to-end-driving.md`: ChauffeurNet (Bansal 2018), TransFuser, UniAD architectures.
- `safety-iso26262-sotif-scenario-testing.md`: Mobileye RSS figure if publicly available.

#### QIS (medium priority)
- `quantum-computing/algorithms.md`: Shor circuit, Grover circuit — typically have Wikimedia versions but paper versions are richer.
- `quantum-computing/error-correction.md`: Google Willow surface-code figure (Nature 2024, may need to use arxiv version).
- `quantum-information-science/quantum-internet/teleportation.md`: standard teleportation circuit (Wikimedia version is fine).

#### Reinforcement Learning
- `reinforcement-learning-and-bayesian-tuning.md`: Sutton & Barto agent-environment loop (open access edition images).
- DQN architecture (Mnih 2015).
- AlphaGo MCTS diagram (Silver 2016).

#### Reinforcement Learning section in `cs/reinforcement-learning/`
- Same coverage but page-specific.

### Mermaid stays alongside

When you embed a paper figure, **keep the existing Mermaid diagram** as a complementary "labeled, color-blind-safe" version. The two together give: (a) the canonical visual from the paper for instant recognition, (b) our Mermaid annotated version for detail study.

### Validation

For each embed, you should be confident the URL exists. Specifically:

- For arxiv ar5iv: the URL is `https://ar5iv.labs.arxiv.org/html/<id>/<filename>` where filename is something like `x1.png`, `x2.png`. Only use this when you're confident the figure number maps correctly (figure 1, 2, 3 in the paper usually are x1, x2, x3).
- If you're not confident, prefer Wikimedia Commons (which you've used safely already).
- **Do not invent URLs**.

### Skipping is OK

If a section has no good public figure source, leave it as Mermaid-only. Better than a broken link.

### Output expectation

End-of-run summary: list how many figures you embedded across how many pages, separated by source (arxiv ar5iv / Wikimedia / GitHub / etc.).

---

The section-specific instructions follow.

---

