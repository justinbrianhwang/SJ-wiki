You are an autonomous content author for **SJ Wiki**. Add **Federated Unlearning** as a single new chapter inside the existing Federated Learning section.

## Inputs

- **OUTPUT FILE**: `f:/coding/SJ Wiki/docs/cs/federated-learning/federated-unlearning.md`
- **SUPPLIED_PAPERS**: `f:/coding/SJ Wiki/tmp/Federated Unlearning/` — three papers to anchor the chapter
- **STYLE**: Topical chapter name (NOT paper title). Inline citations `[N]` with IEEE-style References.

## Supplied papers (must reference)

| File | Paper | Key contribution |
|---|---|---|
| `2012.13891v3.pdf` | Liu et al., "Federated Unlearning" (FedEraser, 2021) | First federated unlearning method; trades server storage for unlearn time using retained historical client updates + calibration |
| `2412.20200v1.pdf` | Pan et al., "Federated Unlearning with Gradient Descent and Conflict Mitigation" (FedOSD, AAAI 2025) | Orthogonal steepest descent direction non-conflicting with retained clients' gradients |
| `Khalil_NoT_Federated_Unlearning_via_Weight_Negation_CVPR_2025_paper.pdf` | Khalil et al., "NoT: Federated Unlearning via Weight Negation" (CVPR 2025) | Weight-negation approach to FU |

Read intros + abstracts via `pdftotext -l 5 <file>` if needed.

## Page metadata

```yaml
---
title: Federated Unlearning
sidebar_position: 7
---
```

Place after `applications-and-systems.md` (sidebar 6). Do not modify other FL files.

## Content scope (~2500-3500 words)

### Definitions
- Right to be forgotten (GDPR Art. 17, CCPA), why FL motivates a distinct unlearning notion
- Unlearning request types: sample-level, client-level (most common in FU), class-level
- Centralized machine unlearning baselines: SISA (Bourtoule et al. 2021), influence-function approaches, exact retraining
- Why centralized methods fail for FL: forward coupling of parameter updates across rounds, server has no raw data

### Approaches
- **Retraining from scratch** (baseline, prohibitive)
- **Historical update reconstruction** (FedEraser): store client updates per round, reconstruct unlearned model from remaining clients' updates with calibration
- **Gradient ascent / reverse SGD** on target client's data
- **Gradient projection** (FedOSD): compute steepest descent for unlearning that is orthogonal (non-conflicting) with retained clients' gradients
- **Weight negation** (NoT, CVPR 2025): negate target client's contribution at parameter level
- **Knowledge distillation** from retained clients to new student model
- **Parameter pruning / sparsity-based** unlearning

### Evaluation
- Membership inference attack (MIA) accuracy as residual-knowledge metric
- Backdoor-trigger removal effectiveness
- Model utility preservation (accuracy on retained data)
- Unlearn speed (rounds, wall-clock vs full retraining)
- Verifiability and audit trails

### Open challenges
- Compatibility with secure aggregation (server may not see individual updates)
- Composition with differential privacy
- Cross-device FU at scale (transient clients)
- Class- and feature-level unlearning
- Federated unlearning for LLMs / FedLoRA settings
- Adversarial unlearning requests (unlearn-the-unlearner)
- Regulatory verifiability (proof of erasure)

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter
2. `# Federated Unlearning` H1
3. 1-2 opening paragraphs (motivation: RTBF, GDPR, poisoning recovery)
4. 1-2 figures (paper figures from supplied papers — see Figure policy below)
5. `## Definitions`
6. `## Key results` — algorithm families with derivations
7. `## Visual` — **MANDATORY Mermaid** comparing retraining vs FedEraser vs FedOSD vs NoT pipelines
8. `## Worked example 1` — e.g., FedEraser calibration computation on 3 clients with stored updates
9. `## Worked example 2` — e.g., FedOSD orthogonal projection: given 3 client gradients, compute the unlearn direction orthogonal to retained two
10. `## Code` — minimal NumPy / PyTorch sketch of FedEraser reconstruction or FedOSD projection
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — link to existing FL pages, [Adversarial Attacks](/cs/adversarial-attacks/intro), [Cryptography](/cs/cryptography/intro), [Privacy](/cs/federated-learning/privacy-differential-and-secure-aggregation)
13. `## References` — IEEE-style entries (15+ entries; cite the 3 supplied papers + foundational unlearning works: Bourtoule SISA, Cao & Yang 2015, Guo et al. certified data removal, Ginart et al. exact data deletion, Wang et al. federated forgetting, etc.)

## Figure policy

The 3 supplied papers are arxiv-modern; HEAD-verified figures (try ar5iv x1 first):

- `2012.13891` (FedEraser): try `https://ar5iv.labs.arxiv.org/html/2012.13891/assets/x1.png` — likely the FedEraser system diagram (Figure 2 in paper). Caption it as such.
- `2412.20200` (FedOSD): try `https://ar5iv.labs.arxiv.org/html/2412.20200/assets/x1.png` — the 3-client gradient-conflict diagram (Figure 1 in paper).
- `Khalil_NoT...` is a CVPR paper not on arxiv (or only on CVF) — skip the embed.

Verify each ar5iv URL exists and is not the 20498-byte placeholder. If placeholder, try `x2.png`, `x3.png`, etc. or skip.

Caption format:
```markdown
*Figure: <description>. From [Author et al., Year](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
```

## Constraints

- Stay inside `docs/cs/federated-learning/`.
- Only create `federated-unlearning.md`. Do not modify other FL files.
- Mermaid label special chars in `"..."`; internal `"` → `#quot;`.
- Do not fabricate arxiv IDs or figure numbers.
- English. Match depth addendum.

## Output summary

```
File: federated-unlearning.md
Word count: <N>
Figures: ar5iv=<a>, Mermaid=<m>
References: <r>
```

Begin now.
