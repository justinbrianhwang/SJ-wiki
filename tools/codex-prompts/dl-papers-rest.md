You are an autonomous content author for **SJ Wiki**. Continue and finish a paper-deep-dive series in the deep learning section.

## Context

The earlier agent already wrote:
- `f:/coding/SJ Wiki/docs/cs/deep-learning/vision-transformer.md`
- `f:/coding/SJ Wiki/docs/cs/deep-learning/rwkv.md`
- `f:/coding/SJ Wiki/docs/cs/deep-learning/mamba.md`

Do **not** overwrite or duplicate those.

## Inputs

- **SOURCE_PDFs**:
  - `f:/coding/SJ Wiki/tmp/attention is all you need.pdf` — Vaswani et al., *Attention Is All You Need*, NeurIPS 2017
  - `f:/coding/SJ Wiki/tmp/Hyena.pdf` — Poli et al., *Hyena Hierarchy*, ICML 2023
  - `f:/coding/SJ Wiki/tmp/Griffin.pdf` — Botev et al., *Griffin: Mixing Gated Linear Recurrences with Local Attention*, 2024
  - `f:/coding/SJ Wiki/tmp/Jamba.pdf` — Lieber et al., *Jamba*, 2024

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/deep-learning/`

## What to produce

### 1. Three new paper pages (flat in deep-learning/)

| Filename | sidebar_position | Paper |
|---|---:|---|
| `hyena.md` | 23 | Poli et al. 2023 |
| `griffin.md` | 26 | Botev et al. 2024 |
| `jamba.md` | 27 | Lieber et al. 2024 |

Each page follows the depth addendum (1500-3500 words, mandatory Mermaid block diagram, ≥2 worked examples, precise KaTeX math, PyTorch sketch, common pitfalls, conservative result claims). Sections:

- Frontmatter (`title:` with author + year, `sidebar_position:` per table)
- 1-paragraph elevator pitch with full citation
- Problem & motivation
- Method (with formulas)
- Visual (mandatory Mermaid)
- Architecture details / hyperparameters
- Key results (conservative)
- Connections (cross-link to other wiki pages including the existing `attention-transformers`, `mamba`, `rwkv`, `vision-transformer` pages)
- PyTorch sketch
- Common pitfalls
- Further reading

### 2. Integrate Vaswani 2017 into existing `attention-transformers.md`

**Do NOT create a separate `attention-is-all-you-need.md` file.** Instead, read the existing
`f:/coding/SJ Wiki/docs/cs/deep-learning/attention-transformers.md` and **expand it in place** with a comprehensive section dedicated to the original Vaswani et al. 2017 paper. Suggested structure:

- Keep all existing content from the d2l-derived page intact.
- Add a new top-level section titled something like **"The Vaswani et al. 2017 paper"** (or "Original Transformer: Attention Is All You Need") near the end, before "Connections" / "Common pitfalls".
- That section should be ~600-1200 words covering:
  - Citation and historical placement (June 2017, neural machine translation context, ousting RNN-based seq2seq)
  - Architecture summary (encoder-decoder with $N=6$ stacks, multi-head attention, position-wise FFN, sinusoidal positional encodings, residual + layer norm)
  - The three attention variants used (encoder self-attention, decoder masked self-attention, encoder-decoder cross-attention)
  - Key formulas: scaled dot-product attention $\mathrm{softmax}(QK^T/\sqrt{d_k})V$, multi-head concatenation, sinusoidal PE $PE_{(pos,2i)} = \sin(pos / 10000^{2i/d_{\mathrm{model}}})$
  - Training setup: WMT 14 EN-DE and EN-FR, label smoothing, Adam with warmup schedule
  - Headline results (BLEU 28.4 EN-DE / 41.0 EN-FR — conservatively cite, note "as reported in the paper")
  - Mermaid block diagram of the encoder-decoder
  - Why this paper became a landmark (eliminated recurrence, parallel training, scaled to enormous models, kicked off the transformer revolution)
- Add cross-links FROM that section TO the modern variants (`vision-transformer`, `rwkv`, `mamba`, `hyena`, `griffin`, `jamba`).

### 3. Lightly update existing `intro.md` (optional)

If the existing `intro.md` has a chapter list, you may **append** entries for `hyena`, `griffin`, `jamba` at the end of the list (positions 23, 26, 27 respectively — note positions 22, 24, 25 for ViT/RWKV/Mamba should already be there from the earlier agent run; if missing, add them too). Preserve existing content.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/deep-learning/`.
- Do not modify any other already-existing page except `attention-transformers.md` (Vaswani section) and `intro.md` (optional listing update).
- Specifically do not touch: `vision-transformer.md`, `rwkv.md`, `mamba.md`, `lstm-variants.md`, the d2l-derived pages.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Don't fabricate numbers.

## Workflow

1. `pdfinfo` and read first 20-30 pages of each of the 4 papers.
2. Read the current `attention-transformers.md` so you know what's already there.
3. Write `hyena.md`, `griffin.md`, `jamba.md`.
4. Edit `attention-transformers.md` to insert the Vaswani section.
5. Optionally update `intro.md`.
6. Print summary listing exactly which files you created / modified.

Begin now.
