You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for a new **Federated Learning** subject under `docs/cs/federated-learning/`.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/federated-learning/`
- **SUPPLIED_PAPERS_DIR**: `f:/coding/SJ Wiki/tmp/Federated Learning/` (read these to anchor the content; consult them via `pdftotext` as needed)
- **SUBJECT**: Federated Learning (graduate-level survey, book-style)
- **STYLE**: Topical chapter names (NOT paper titles). Inline paper citations as `[N]` with a References section at the end of each page (IEEE style).

## REQUIRED PAPERS (uploaded — must be referenced)

Read these from `tmp/Federated Learning/` (already on disk). Every page that touches the relevant topic must cite the relevant paper(s) below. Filenames → identity:

| File | Paper | Where it fits |
|---|---|---|
| `1602.05629v4.pdf` | McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized Data" (FedAvg, AISTATS 2017) | Ch.1 foundations |
| `MLSys-2020-federated-optimization-in-heterogeneous-networks-Paper.pdf` | Li et al., "Federated Optimization in Heterogeneous Networks" (FedProx, MLSys 2020) | Ch.2 heterogeneity |
| `1910.06378v4.pdf` | Karimireddy et al., "SCAFFOLD: Stochastic Controlled Averaging" (ICML 2020) | Ch.2 heterogeneity |
| `NeurIPS-2020-tackling-the-objective-inconsistency-problem-in-heterogeneous-federated-optimization-Paper.pdf` | Wang et al., "Tackling the Objective Inconsistency Problem" (FedNova, NeurIPS 2020) | Ch.2 heterogeneity |
| `288_fedbn_federated_learning_on_no.pdf` | Li et al., "FedBN: Federated Learning on Non-IID Features via Local Batch Normalization" (ICLR 2021) | Ch.2 / Ch.3 |
| `Li_Model-Contrastive_Federated_Learning_CVPR_2021_paper.pdf` | Li et al., "Model-Contrastive Federated Learning" (MOON, CVPR 2021) | Ch.2 heterogeneity |
| `NeurIPS-2020-personalized-federated-learning-with-moreau-envelopes-Paper.pdf` | Dinh et al., "Personalized Federated Learning with Moreau Envelopes" (pFedMe, NeurIPS 2020) | Ch.3 personalization |
| `2012.04221v3.pdf` | Li et al., "Ditto: Fair and Robust Federated Learning Through Personalization" (ICML 2021) | Ch.3 personalization + Ch.5 robustness |
| `2017-281.pdf` | Bonawitz et al., "Practical Secure Aggregation for Privacy-Preserving Machine Learning" (CCS 2017) | Ch.4 privacy |
| `1906.08935v2.pdf` | Zhu et al., "Deep Leakage from Gradients" (DLG, NeurIPS 2019) | Ch.4 privacy (attacks) |
| `1807.00459v3.pdf` | Bagdasaryan et al., "How To Backdoor Federated Learning" (AISTATS 2020) | Ch.5 robustness (attacks) |
| `2409.15723v2.pdf` | Yao et al., "Federated Large Language Models: Current Progress and Future Directions" (2024 survey) | Ch.6 applications + LLM section |
| `2505.13502v1.pdf` | Yang et al., "Federated Low-Rank Adaptation for Foundation Models: A Survey" (FedLoRA, 2025) | Ch.6 applications + LLM section |

Use these papers as the **anchor** for each topic. Each citation must reflect what is actually in the paper (read it via `pdftotext -l 30 <file>` for an intro + abstract pass; longer reads on demand). Other classical references (Bonawitz federated summary 2019, Kairouz "Advances and Open Problems in FL", Krum, etc.) may be added beyond these but the supplied 13 papers MUST appear in the References.

## Produce

### 1. Replace `intro.md` (sidebar_position: 0)

A 250-400 word overview of what Federated Learning is (training models across decentralized data without centralizing it), the threat models it addresses (privacy, regulation, communication, edge compute), the canonical setting (cross-silo vs cross-device), and the chapter map. End with a numbered list of all pages.

### 2. Create exactly 6 detail pages

| sidebar_position | filename | title |
|---|---|---|
| 1 | `foundations-and-fedavg.md` | Foundations and FedAvg |
| 2 | `heterogeneity-and-optimization.md` | Heterogeneity and Federated Optimization |
| 3 | `personalization-in-federated-learning.md` | Personalization in Federated Learning |
| 4 | `privacy-differential-and-secure-aggregation.md` | Privacy: Differential Privacy and Secure Aggregation |
| 5 | `communication-efficiency-and-robustness.md` | Communication Efficiency and Robustness |
| 6 | `applications-and-systems.md` | Applications and Systems |

These are the ONLY 6 detail files to create. Do not split into more sub-chapters.

## Content scope per page

### 1 — `foundations-and-fedavg.md` (sidebar 1)

- Definition, motivation (privacy regulation GDPR/HIPAA, data sovereignty, edge data, communication cost)
- Cross-silo (hospitals, banks) vs cross-device (phones, IoT) settings — characteristics: client count, availability, stake, data scale
- System architecture: server, clients, communication rounds; synchronous vs asynchronous
- FedSGD as a baseline; FedAvg algorithm (McMahan et al., 2017) — pseudocode with local epochs $E$, batch size $B$, learning rate $\eta$, client fraction $C$
- Communication-computation tradeoff (why local epochs > 1)
- Convergence intuition: under IID data FedAvg ≈ SGD on aggregate; non-IID introduces client drift
- Basic notation: $w_t^k$, $w_t$, $n_k$, $K$, $T$
- Two worked examples: (a) one round of FedAvg by hand with 3 clients and scalar weights, (b) compute communication cost vs uplinks for given $T,K,d,B$

### 2 — `heterogeneity-and-optimization.md` (sidebar 2)

- Two heterogeneities: **statistical** (non-IID label/feature distributions) and **system** (compute speed, network, dropout, stragglers)
- Why FedAvg degrades under non-IID: client drift, objective inconsistency (Wang et al., FedNova)
- **FedProx** [Li et al. 2018]: proximal term $\frac{\mu}{2}\|w-w_t\|^2$ in local objective
- **SCAFFOLD** [Karimireddy et al. 2020]: control variates correcting client drift; client and server variates $c_k, c$
- **FedNova** [Wang et al. 2020]: normalized averaging to handle uneven local steps
- **MOON** [Li et al. 2021]: model-contrastive learning to align local with global features
- **q-FedAvg / q-FFL** [Li et al. 2020]: fairness via tilted objectives
- System heterogeneity: client sampling, asynchronous FL (FedBuff), partial participation, deadline-based aggregation
- Worked examples: (a) FedProx update step on one client, (b) SCAFFOLD correction term computation

### 3 — `personalization-in-federated-learning.md` (sidebar 3)

- Why personalization: when client distributions differ enough that one global model is poor
- Approaches:
  - Local fine-tuning after global training
  - **Per-FedAvg** [Fallah et al. 2020]: MAML-style meta-learning
  - **pFedMe** [Dinh et al. 2020]: Moreau envelope objective $\min_w F_k(w)+\frac{\lambda}{2}\|w-\theta\|^2$
  - **FedRep / FedBABU**: shared representation + personalized head
  - **Clustered FL** [Sattler et al., Ghosh et al.]: cluster clients with similar distributions
  - **Ditto** [Li et al. 2021]: personalized + robust dual objective
  - Multi-task FL [Smith et al. MOCHA] and **FedFomo** (model selection)
- Tradeoffs: storage, server-side coordination, when personalization helps vs hurts
- Evaluation: per-client accuracy, worst-client accuracy, mean+std across clients
- Worked examples: (a) pFedMe inner-loop update, (b) clustered FL assignment based on gradient similarity

### 4 — `privacy-differential-and-secure-aggregation.md` (sidebar 4)

- Threat models: honest-but-curious server, malicious clients, malicious server, network adversary, membership inference
- **Local DP**: each client perturbs locally; high noise, weak utility
- **Central DP** (DP-FedAvg / DP-SGD style): server clips and adds noise to aggregate; Gaussian or Laplace mechanisms
- Privacy accounting: $(\varepsilon,\delta)$-DP, moments accountant, RDP composition
- **Secure aggregation** [Bonawitz et al. 2017]: pairwise masks via Diffie-Hellman, sums cancel at server; supports dropouts via Shamir secret sharing
- Trusted execution environments (TEE) as an alternative
- Homomorphic encryption (CKKS, BFV) for federated aggregation — partial use due to overhead
- Multi-party computation (MPC) for cross-silo collaborations
- Gradient inversion attacks — **Deep Leakage from Gradients** (DLG, Zhu et al.): given shared gradients $\nabla_\theta\mathcal{L}(x,y;\theta)$ recover $(x,y)$ via optimization of "dummy" $(x^*,y^*)$ minimizing $\|\nabla\mathcal{L}(x^*,y^*;\theta)-\nabla\mathcal{L}(x,y;\theta)\|^2$. iDLG label recovery from final-layer gradients. Mitigations: gradient clipping, large batch, DP noise, secure aggregation.
- Membership inference; defense composition: noise + secure aggregation + clipping stacked
- Worked examples: (a) compute $(\varepsilon,\delta)$ noise scale for DP-FedAvg with given clip norm and rounds, (b) secure aggregation pairwise mask example with 3 clients

### 5 — `communication-efficiency-and-robustness.md` (sidebar 5)

**Communication efficiency**
- Bottleneck: uplink ≪ downlink; rounds dominate convergence wall-time
- Gradient compression: top-k sparsification, signSGD, quantization (QSGD, TernGrad, 1-bit SGD)
- Model compression: structured / unstructured pruning before sending, low-rank updates, **LoRA / adapter** style federated updates
- **FedPAQ**, **FedDist** for distillation-based communication reduction
- Federated distillation: communicate logits instead of weights (FedMD, FedAUX)
- Lazy / event-triggered communication
- Worked example: bandwidth and round count under top-k vs full transmission

**Robustness / Byzantine defenses**
- Threat: malicious clients submitting poisoned or arbitrary updates
- **Coordinate-wise median** / **trimmed mean** [Yin et al. 2018]
- **Krum / Multi-Krum** [Blanchard et al. 2017]: select update closest to its $K-f-2$ nearest neighbors
- **Bulyan**, **FoolsGold**, **FLTrust** [Cao et al. 2020]
- Targeted backdoor attacks: **model replacement** (Bagdasaryan et al., "How To Backdoor FL") — constrain-and-scale technique to evade defenses, semantic backdoors, DBA distributed backdoor variant; defenses: norm clipping, anomaly detection, certified bounds, FLTrust trust scores
- Trade-off between Byzantine robustness and privacy (DP+secure aggregation complicate detection)
- Worked example: apply Krum to 5 client updates with one malicious

### 6 — `applications-and-systems.md` (sidebar 6)

- **Mobile keyboards**: Google Gboard next-word prediction, emoji prediction
- **Healthcare**: cross-hospital model training (NVIDIA FLARE deployments), MELLODDY drug discovery consortium
- **Finance**: cross-bank fraud detection, AML modeling under regulatory constraints
- **Autonomous driving**: cross-vehicle perception model updates (NVIDIA, BMW)
- **Internet of Things**: edge device training, federated TinyML
- **Cross-silo science**: federated genomics, multi-site clinical trials
- **Recommendation**: federated content / item models for privacy-preserving recsys
- **LLM era**: federated fine-tuning, **FedLLM** (Yao et al. 2024 survey — challenges in heterogeneous device compute, model size, prompt vs parameter tuning, privacy-utility tradeoffs at LLM scale), **FedLoRA** (Yang et al. 2025 survey — combining LoRA low-rank updates with FL to minimize communication and memory; per-client low-rank adapters $A_k,B_k$, aggregation strategies including stacking, averaging, full-rank approximation; heterogeneous LoRA ranks). Include a small diagram or table comparing full-model FL vs adapter / LoRA FL on parameters transmitted per round.
- **Frameworks and tools**:
  - **TensorFlow Federated** (TFF)
  - **PySyft / OpenMined**
  - **FATE** (WeBank)
  - **Flower** (general)
  - **NVIDIA FLARE**
  - **OpenFL** (Intel)
- **Open challenges**: incentives and mechanism design, label scarcity, certified robustness, foundation models in FL, regulatory and audit trails, fairness, energy

## Per-page format (mandatory — depth addendum applies)

Each page MUST include in this order:

1. Frontmatter: `title:`, `sidebar_position:`
2. `# Title` (H1)
3. Opening 1-2 paragraphs (motivation + scope)
4. (Strongly recommended) 1-2 contextual or paper figures with attribution
5. `## Definitions` — formal setup, notation
6. `## Key results` — main algorithms / theorems / model families
7. `## Visual` — **MANDATORY Mermaid diagram** showing the chapter's architecture / flow. Match the level of `attention-transformers.md` (subgraphs, residuals, dimensions where applicable). Special-char labels in `"..."`; internal `"` → `#quot;`.
8. `## Worked example 1: ...` (numerical / by-hand)
9. `## Worked example 2: ...`
10. `## Code` — minimal PyTorch / NumPy / pseudocode (Flower-style or plain NumPy)
11. `## Common pitfalls` — 10-15 bulleted items
12. `## Connections` — links to other DL/CS pages (deep-learning, adversarial-attacks, cryptography, privacy, optimization)
13. `## References` — IEEE-style numbered list with arxiv links (15-25 entries per page is appropriate)

## Word count

Each detail page: **2000-3500 words**. Dense pages (privacy, optimization) lean toward upper end.

## Math precision (KaTeX)

- FedAvg: $w_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}w_{t+1}^k$
- FedProx local: $\min_w F_k(w)+\frac{\mu}{2}\|w-w_t\|^2$
- DP guarantee: $(\varepsilon,\delta)$-DP, $\sigma=\frac{C\sqrt{2\log(1.25/\delta)}}{\varepsilon}$ for Gaussian mechanism
- Secure-agg mask: $z_k=x_k+\sum_{u<k}s_{k,u}-\sum_{u>k}s_{u,k}$
- Krum score: $\mathrm{score}(i)=\sum_{j\in\mathcal{N}(i)}\|g_i-g_j\|^2$ over $K-f-2$ nearest

## Visual policy

- Mermaid mandatory per page.
- Optional: paper figures via `https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png`. Verified candidates:
  - FedAvg (`1602.05629`, `x1.png` if exists) — McMahan et al.
  - FedProx (`1812.06127`, `x1.png`)
  - SCAFFOLD (`1910.06378`, `x1.png`)
  - Secure aggregation (`1611.04482`, `x1.png`)
  - DP-FedAvg / Learning Differentially Private (`1710.06963`, `x1.png`)
  - Personalization survey (`2003.13461`, `x1.png`)
- Wikimedia context: `Federated_learning_process_central_case.png` (if exists), generic distributed-computing diagrams.
- Do NOT fabricate arxiv IDs. Skip figure if unsure.
- Caption format: `*Figure: <description>. From [Author et al., Year](arxiv-abs-url) — embedded under educational fair use with attribution.*` or `*Figure: <description>. Image: [Wikimedia Commons](file-page-url), Author, License.*`

## Citation format

Inline as `[N]` matched to a References section at end. Example:

> FedAvg [1] reduces communication rounds by allowing multiple local SGD epochs before aggregation.

> ## References
> [1] H. B. McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized Data," AISTATS, 2017. https://arxiv.org/abs/1602.05629
> [2] T. Li et al., "Federated Optimization in Heterogeneous Networks," MLSys, 2020. https://arxiv.org/abs/1812.06127
> ...

## Constraints

- Stay inside `docs/cs/federated-learning/`.
- Replace the existing `intro.md` stub. Do not touch `_category_.json`.
- Do NOT use paper titles or author names in filenames.
- Mermaid label special chars in `"..."`; internal `"` → `#quot;`.
- For images, use `https://commons.wikimedia.org/wiki/Special:FilePath/<filename>` (Wikimedia) or `https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png` (paper figures). Skip if uncertain.
- English. Match the depth addendum.

## Output summary

End with:

```
Pages created: 1 intro + 6 detail = 7
Total word count: <X>
Figures embedded: <N> (ar5iv: a, Wikimedia: w, Mermaid: m)
References per page (avg): <Y>
```

Begin now.
