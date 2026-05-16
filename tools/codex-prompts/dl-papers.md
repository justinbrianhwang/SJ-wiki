You are an autonomous content author for **SJ Wiki**. Generate **detailed** paper-deep-dive pages for the deep learning section.

## Inputs

- **SOURCE_PDFs** (7 papers on efficient sequence modeling / attention):
  1. `f:/coding/SJ Wiki/tmp/attention is all you need.pdf` — Vaswani et al., *Attention Is All You Need*, NeurIPS 2017 (Transformer)
  2. `f:/coding/SJ Wiki/tmp/ViT.pdf` — Dosovitskiy et al., *An Image is Worth 16x16 Words* (ViT), ICLR 2021 (preprint Oct 2020)
  3. `f:/coding/SJ Wiki/tmp/Hyena.pdf` — Poli et al., *Hyena Hierarchy*, ICML 2023 (preprint Feb 2023)
  4. `f:/coding/SJ Wiki/tmp/RWKV.pdf` — Peng et al., *RWKV: Reinventing RNNs for the Transformer Era*, EMNLP 2023 (preprint May 2023)
  5. `f:/coding/SJ Wiki/tmp/Mamba.pdf` — Gu & Dao, *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*, 2023 (Dec 2023)
  6. `f:/coding/SJ Wiki/tmp/Griffin.pdf` — Botev et al., *Griffin: Mixing Gated Linear Recurrences with Local Attention*, 2024 (Feb)
  7. `f:/coding/SJ Wiki/tmp/Jamba.pdf` — Lieber et al., *Jamba: A Hybrid Transformer-Mamba Language Model*, 2024 (Mar)

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/deep-learning/` (flat — same directory as existing d2l-derived pages; do NOT use a `papers/` subfolder)

## Output filenames + sidebar_position

These are continuations of the existing d2l chapter sequence. Use **publication order** for `sidebar_position`, starting at **21** (just after the last existing d2l page which is at 20):

| Position | Filename | Paper |
|---:|---|---|
| 21 | `attention-is-all-you-need.md` | Vaswani 2017 Transformer |
| 22 | `vision-transformer.md` | Dosovitskiy 2020 ViT |
| 23 | `hyena.md` | Poli Feb 2023 |
| 24 | `rwkv.md` | Peng May 2023 |
| 25 | `mamba.md` | Gu Dec 2023 |
| 26 | `griffin.md` | Botev Feb 2024 |
| 27 | `jamba.md` | Lieber Mar 2024 |

Do NOT create a separate "Papers" hub page. These pages flow naturally from the existing d2l content (which ends at position 20). The existing `intro.md` already lists d2l chapters; you may **optionally** append a short "## Papers and modern architectures" section to that intro that lists the 7 new pages — but only if you preserve the existing 19-item d2l list intact.

## Per-page format

For each paper page:

- Frontmatter: `title:` (e.g. `"Attention Is All You Need (Vaswani et al., 2017)"`), `sidebar_position:` (per table above)
- 1-paragraph elevator pitch with full citation
- **Problem & motivation** — what limitation of prior work this addresses
- **Method** — the core contribution with precise KaTeX math (attention formulas, recurrence equations, SSM state-space form, gating, scan, etc.)
- **Visual** — Mermaid block diagram of the architecture (mandatory)
- **Architecture details / hyperparameters** — what the paper actually configures
- **Key results** — datasets, baselines, headline numbers (quote conservatively — give ranges, don't fabricate, cite which task)
- **Connections** — explicit cross-links to:
  - Earlier papers in this sequence (e.g. Mamba → Hyena, SSM background)
  - Existing d2l pages: `/cs/deep-learning/attention-transformers`, `/cs/deep-learning/sequence-modeling-rnns`, `/cs/deep-learning/gated-rnns-seq2seq`, `/cs/deep-learning/modern-cnns` (for ViT)
- **PyTorch sketch** — minimal `torch` snippet of the key forward pass (e.g., scaled dot-product attention, ViT patch embed, Mamba selective scan). Pedagogical, not copy-pasted.
- **Common pitfalls / what to watch for when reproducing**
- **Further reading** — concrete follow-up references the paper cites or natural sequels

## Format requirements (depth addendum applies)

- 1500-3500 words per page. Foundational papers (Transformer, Mamba) lean toward the upper end.
- Mermaid diagrams mandatory.
- Math precision: scaled dot-product attention $\mathrm{softmax}(QK^T/\sqrt{d_k})V$, multi-head, positional encoding; ViT patch embedding $x \mapsto \mathrm{Linear}(x_{\mathrm{patches}}) + \mathrm{PE}$; RWKV time-mixing with $\mu_*$ tokens and decay $w$; Mamba selective SSM with input-dependent $A, B, C, \Delta$ and the parallel selective scan; Hyena's implicit long convolution and order-N hierarchy; Griffin's RG-LRU gated recurrence; Jamba's MoE + Transformer/Mamba layer interleaving.
- Conservative on benchmark claims. State the year and task.

## Workflow

1. `pdfinfo` each paper. Confirm exact title, authors, year.
2. `pdftotext -l 5 "<pdf>" -` for abstract + intro.
3. `pdftotext -f 1 -l 30 "<pdf>" -` for full body (most papers ~10-20 pages).
4. Write one wiki page per paper.
5. Optionally append a short "Papers" section to existing `intro.md` (preserve original content) listing the 7 pages.
6. Print summary listing all files created.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/deep-learning/`.
- Do NOT modify any existing d2l-derived page (positions 1-20). Only `intro.md` may receive a short appended section.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Don't fabricate.

Begin now.
