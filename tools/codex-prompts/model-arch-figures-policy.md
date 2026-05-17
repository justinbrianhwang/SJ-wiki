## MODEL ARCHITECTURE FIGURES POLICY (broad pass)

The wiki currently mentions many named models (ResNet, GoogLeNet, BERT, TransFuser, UniAD, InterFuser, ViT, U-Net, YOLO, DDPM, DQN, etc.) in deep-dive sections, but most sections have only Mermaid diagrams — no actual paper figure. The user wants the **actual paper architecture figure** embedded next to (or instead of) the Mermaid in every named-model section, especially in architecture-centric areas (deep learning, NLP, autonomous driving, generative models, RL).

### The rule

For every named-model deep-dive section across `docs/`:
- **Embed the paper's primary architecture figure** via `ar5iv.labs.arxiv.org`.
- Keep the existing Mermaid as a complementary annotated version.
- Caption format: `*Figure: <one-line description>. From [Author et al., Year](arxiv-abs-url) — embedded under educational fair use with attribution.*`
- Place the figure at the start of the model's subsection so it visually anchors the explanation.

### URL format (MANDATORY)

```
https://ar5iv.labs.arxiv.org/html/<arxiv-id>/assets/x<N>.png
```

- `<arxiv-id>` is the arxiv number (e.g., `1512.03385`).
- `<N>` is the figure number: `x1.png` for Figure 1, `x2.png` for Figure 2, etc.
- Some papers use `assets/<custom-name>.png` instead of `x<N>.png` — only use this when the custom name is clearly known.
- **Never fabricate** an arxiv ID. If not certain, skip the figure.
- The agent MUST run `python tools/check-image-urls.py docs/<target-dir>` at the end and remove (or replace) any URL returning BROKEN status.

### Curated (model → arxiv → primary figure) mappings

The agent should use these when adding figures. These are confident pairs. If a figure number turns out to be wrong (404), try `x1`, `x2`, `x3` in order, or skip.

#### Computer vision backbones (`docs/cs/deep-learning/`, `docs/cs/computer-vision/`)
| Model        | arxiv ID    | Figure |
|--------------|-------------|--------|
| ResNet (He 2015)        | `1512.03385` | `x1.png` (residual block); also try `x2.png` for full arch |
| GoogLeNet / Inception (Szegedy 2014) | `1409.4842` | `x2.png` (inception module); `x3.png` for full |
| VGG (Simonyan 2014)     | `1409.1556` | `x1.png` |
| DenseNet (Huang 2016)   | `1608.06993` | `x1.png` (dense block); `x2.png` for full |
| MobileNet (Howard 2017) | `1704.04861` | `x1.png` |
| EfficientNet (Tan 2019) | `1905.11946` | `x1.png`; also `x7.png` for compound scaling |
| U-Net (Ronneberger 2015) | `1505.04597` | `x1.png` (the iconic U) |
| Faster R-CNN (Ren 2015) | `1506.01497` | `x2.png` (RPN) |
| Mask R-CNN (He 2017)    | `1703.06870` | `x1.png` |
| YOLO v1 (Redmon 2015)   | `1506.02640` | `x2.png` (system overview); `x3.png` (architecture) |
| Vision Transformer / ViT (Dosovitskiy 2020) | `2010.11929` | `x1.png` |
| Swin Transformer (Liu 2021) | `2103.14030` | `x1.png` |
| ConvNeXt (Liu 2022)     | `2201.03545` | `x1.png` |

#### NLP & sequence models (`docs/cs/nlp/`, `docs/cs/deep-learning/`)
| Model        | arxiv ID    | Figure |
|--------------|-------------|--------|
| Transformer (Vaswani 2017) | `1706.03762` | `x1.png` |
| BERT (Devlin 2018)      | `1810.04805` | `x1.png` (pretrain/finetune); `x2.png` (input repr) |
| GPT-3 (Brown 2020)      | `2005.14165` | `x1.png` |
| T5 (Raffel 2019)        | `1910.10683` | `x1.png` |
| BART (Lewis 2019)       | `1910.13461` | `x1.png` |
| LLaMA (Touvron 2023)    | `2302.13971` | `x1.png` |
| Mamba (Gu 2023)         | `2312.00752` | `x1.png`; `x3.png` for arch |
| RWKV (Peng 2023)        | `2305.13048` | `x2.png` |
| Hyena (Poli 2023)       | `2302.10866` | `x1.png` |

#### Generative models (`docs/cs/deep-learning/generative-*`, `docs/cs/computer-vision/`)
| Model        | arxiv ID    | Figure |
|--------------|-------------|--------|
| GAN (Goodfellow 2014)   | `1406.2661`  | no ar5iv figure — use Wikimedia `Generative_adversarial_network.svg` instead |
| DCGAN (Radford 2015)    | `1511.06434` | `x1.png` or `lsun_bedrooms_generator.png` |
| VAE (Kingma 2013)       | `1312.6114`  | usually no figure — use Wikimedia `Variational-AutoEncoder.png` |
| StyleGAN (Karras 2018)  | `1812.04948` | `x1.png` |
| DDPM (Ho 2020)          | `2006.11239` | `x2.png` (diffusion forward/reverse) |
| Latent Diffusion / Stable Diffusion (Rombach 2021) | `2112.10752` | `x3.png` (architecture) |
| Imagen (Saharia 2022)   | `2205.11487` | `x1.png` |

#### Autonomous driving (`docs/cs/autonomous-driving/`)
| Model        | arxiv ID    | Figure |
|--------------|-------------|--------|
| PointPillars (Lang 2018) | `1812.05784` | `x2.png` (already used) |
| CenterPoint (Yin 2020)   | `2006.11275` | `x1.png`; `x2.png` |
| BEVFormer (Li 2022)      | `2203.17270` | `x2.png` |
| DETR3D (Wang 2021)       | `2110.06922` | `x2.png` |
| LSS (Lift-Splat-Shoot, Philion 2020) | `2008.05711` | `x2.png` |
| VectorNet (Gao 2020)     | `2005.04259` | `x2.png` (already used) |
| Wayformer (Nayakanti 2022) | `2207.05844` | `x1.png` |
| MultiPath (Chai 2019)    | `1910.05449` | `x2.png` |
| TransFuser (Chitta 2022) | `2205.15997` | `x2.png` (architecture) |
| InterFuser (Shao 2022)   | `2207.14024` | `x2.png` (framework) |
| UniAD (Hu 2022)          | `2212.10156` | `x1.png` (already used) |
| VAD (Jiang 2023)         | `2303.12077` | `x2.png` |
| MILE (Hu 2022)           | `2210.07729` | `x2.png` |
| ChauffeurNet (Bansal 2018) | `1812.03079` | `x1.png` |
| GAIA-1 (Hu 2023)         | `2309.17080` | `x1.png` |
| DriveDreamer (Wang 2023) | `2309.09777` | `x1.png` |

#### Adversarial attacks (`docs/cs/adversarial-attacks/`)
Most pages already have the FGSM panda figure (`1412.6572/assets/gibbon_993.png`) and patch figure (`1712.09665/assets/banana_attack_diagram.png`). Audit and add where missing:
| Model        | arxiv ID    | Figure |
|--------------|-------------|--------|
| PGD (Madry 2017)        | `1706.06083` | `x1.png` (loss landscape) |
| CW attack (Carlini 2016) | `1608.04644` | usually no good figure — skip |
| AutoAttack (Croce 2020) | `2003.01690` | `x1.png` |
| TRADES (Zhang 2019)     | `1901.08573` | `x1.png` |
| RP2 (Eykholt 2017)      | `1707.08945` | `figs/pip4.png` (already used) |

#### Reinforcement learning (`docs/cs/reinforcement-learning/`)
| Model        | arxiv ID    | Figure |
|--------------|-------------|--------|
| DQN (Mnih 2013)         | `1312.5602`  | `x1.png` if exists; otherwise use Wikimedia `Reinforcement_learning_diagram.svg` |
| A3C (Mnih 2016)         | `1602.01783` | `x1.png` |
| PPO (Schulman 2017)     | `1707.06347` | usually no architecture figure — skip |
| AlphaGo / AlphaZero     | Nature paper — no arxiv ar5iv. Use Wikimedia or skip. |
| Dreamer / DreamerV2 (Hafner 2020) | `2010.02193` | `x2.png` |
| MuZero (Schrittwieser 2019) | `1911.08265` | `x2.png` |

### Caption format

```markdown
![<one-sentence description of what the figure shows>](https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png)

*Figure: <brief explanation of the figure's role in the model>. From [Author et al., Year](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
```

### Where to place each figure

Place the figure at the **top of the named-model subsection**, right after the section heading, before any text. The reader's first impression of the model should be the canonical paper figure.

If the model already has its arch figure embedded (e.g., UniAD on the intro and end-to-end pages), don't duplicate — leave alone.

### Verification (MANDATORY)

After writing edits to all target pages, the agent MUST:

1. Run `python tools/check-image-urls.py docs/<target-area>/ 2>&1 | grep BROKEN` to list any newly broken URLs.
2. For each BROKEN URL: either try a different figure number (x1 → x2 → x3) or remove the embed entirely. Never leave a broken embed.
3. Report the final tally: how many figures added, how many pages touched, any URLs that were rejected after verification.

### Tone and scope

- Be aggressive: prefer adding a figure over leaving a section figure-less when the model is named and well-known.
- Skip if uncertain — better to leave a section without a paper figure than to introduce a broken URL.
- Don't replace existing high-quality Mermaid; both can coexist.
- Don't touch unrelated content; only insert image blocks + captions in named-model subsections.

### Output expectation

End-of-run summary table:

```
Pages touched: N
Figures embedded: M
By source: ar5iv (M-k), Wikimedia (k)
Broken URLs detected and removed: x
```
