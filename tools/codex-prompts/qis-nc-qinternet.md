You are an autonomous content author for **SJ Wiki**. Integrate **Nielsen & Chuang** into the **Quantum Internet** area of QIS using **combine mode**.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/quantum-computation-and-quantum-information-nielsen-chuang.pdf` — *Quantum Computation and Quantum Information*. Relevant: Chapter 1.3.7 (teleportation), Chapter 2 (postulates), Chapter 8 (quantum channels), Chapter 12 (entanglement-assisted communication, entropy of entanglement).
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-internet/`

## Existing pages (DO NOT delete; expand in place via combine mode)

```
intro.md           (append N&C reference note)
entanglement.md    (foundational; enrich with N&C Ch. 12 entropy of entanglement, Schmidt decomposition rigor, monogamy)
teleportation.md   (foundational; enrich with N&C's exact protocol derivation, fidelity bounds)
quantum-repeater.md (foundational; N&C does not cover repeaters in depth — leave structure, optionally reference channel capacity from Ch. 12)

(plus deep-dive paper pages — DO NOT modify)
```

## Combine-mode rules

- N&C is canonical. Existing general-knowledge pages get refined.
- **N&C-specific additions for QInternet**:
  - Teleportation protocol from N&C Ch. 1.3.7 — full derivation with explicit state expansion, classical 2-bit communication, Pauli correction lookup
  - Entanglement: Schmidt decomposition (Ch. 2.5), Bell-state basis, entanglement entropy $S(\rho_A) = -\mathrm{Tr}(\rho_A \log \rho_A)$ (Ch. 11), distillable entanglement / entanglement cost (Ch. 12)
  - Channels: Choi-Jamiolkowski, Kraus form (Ch. 8) — useful as background for repeater section
- Mark N&C as primary reference.
- Cross-link to QC area (QEC for memory), QCom (BB84 uses entanglement-based variant), `/physics/quantum-mechanics/density-operator-entanglement-decoherence`.

## Format

Depth addendum applies (1500-3500 words; Mermaid or table; ≥2 worked examples; common pitfalls; cross-links; Qiskit/Cirq sketch).

## Workflow

1. `pdftotext -l 30 "<pdf>" -` to find N&C's TOC for relevant chapters.
2. Read Ch. 1.3.7 (teleportation), Ch. 2.5 (Schmidt), Ch. 11 (entropy), Ch. 12 (info theory).
3. Rewrite `entanglement.md`, `teleportation.md` in place.
4. Lightly update `quantum-repeater.md` with channel references.
5. Update `intro.md` with N&C reference (preserve deep-dive list).
6. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-internet/`.
- Do NOT delete or modify deep-dive paper pages.
- Do not modify `_category_.json` or files outside this dir.
- No `npm`. English. KaTeX. Mermaid (escape special chars).
- Conservative.

Begin now.
