You are an autonomous content author for **SJ Wiki**. Integrate **Nielsen & Chuang** into the **Quantum Communication** area of QIS using **combine mode**.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/quantum-computation-and-quantum-information-nielsen-chuang.pdf` — *Quantum Computation and Quantum Information*. Particularly Chapter 12 (Quantum information theory) which covers BB84 security proof and QKD foundations, plus Chapter 8 (noise/channels) for QKD analysis.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-communication/`

## Existing pages (DO NOT delete; expand in place via combine mode)

```
intro.md            (append note about N&C as primary reference)
bb84.md             (foundational; enrich with N&C Ch. 12 security proof; privacy amplification)
qkd.md              (foundational; enrich with N&C's Holevo bound / information-theoretic security framing)
quantum-network.md  (foundational; N&C touches networking only briefly; can add reference but keep existing structure)

(plus deep-dive paper pages — DO NOT modify those)
```

## Combine-mode rules

- Treat N&C as **the canonical textbook**; existing pages written from general knowledge get rewritten to match N&C's notation and rigor where applicable.
- **N&C-specific additions for QCom**:
  - BB84 security proof from N&C Ch. 12 (or 12.6 in some editions) — the privacy amplification + error correction protocol, eavesdropping bound via Holevo or Csiszár-Körner, secret key rate $r \ge I(A:B) - I(A:E)$
  - Add Holevo bound discussion (Holevo's theorem $\chi \ge I(X:Y)$ for accessible information)
  - Use N&C's notation throughout
- Mark N&C as primary reference in "Further reading" / page note.
- Cross-link to QC area (no-cloning from `algorithms.md`/`error-correction.md`), `/cs/cryptography/`, `/quantum-information-science/quantum-internet/`.

## Format

Depth addendum (1500-3500 words; mandatory Mermaid or table; ≥2 worked examples; common pitfalls; cross-links; numpy/Qiskit sketch).

## Workflow

1. `pdftotext -l 30 "<pdf>" -` to find N&C's TOC for Chapter 12.
2. `pdftotext -f X -l Y "<pdf>" -` for the QKD security proof pages.
3. Rewrite `bb84.md`, `qkd.md` in place with combine-mode synthesis.
4. Optionally lightly update `quantum-network.md`.
5. Update `intro.md` with N&C reference note (preserve deep-dive list).
6. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-communication/`.
- Do NOT delete or modify deep-dive paper pages.
- Do not modify `_category_.json` or files outside this dir.
- No `npm`. English. KaTeX. Mermaid (escape special chars).
- Conservative.

Begin now.
