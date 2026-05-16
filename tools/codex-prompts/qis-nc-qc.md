You are an autonomous content author for **SJ Wiki**. Integrate **Nielsen & Chuang** into the **Quantum Computing** area of QIS using **combine mode**.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/quantum-computation-and-quantum-information-nielsen-chuang.pdf` — *Quantum Computation and Quantum Information*, 10th Anniversary Edition (Cambridge UP). The standard graduate textbook covering quantum mechanics, quantum circuits, algorithms, noise, distance measures, QEC, entropy, and quantum information theory.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-computing/`

## Existing pages (DO NOT delete; expand in place via combine mode)

```
intro.md            (area hub — append a "Primary source" note + ensure N&C is cited)
hardware.md         (foundational; enrich with N&C Ch. 7 physical implementations)
algorithms.md      (foundational; enrich with N&C Ch. 5 QFT/Shor, Ch. 6 Grover, Deutsch-Jozsa from Ch. 1)
error-correction.md (foundational; enrich with N&C Ch. 10 QEC and stabilizer formalism)
quantum-ml.md      (foundational; N&C does not cover QML directly — leave structure, optionally add an "N&C-style notation" subsection referencing entropy/channels chapters)

(plus deep-dive paper pages already added — DO NOT modify those)
```

## Combine-mode rules

- **Synthesize, do not duplicate**. The existing pages were written from general knowledge; N&C is now the primary textbook reference. Treat N&C as the canonical source where it applies and rewrite sections to match its notation, terminology, and rigor. Keep deep-dive paper pages untouched.
- **N&C-specific additions**:
  - Use N&C's notation (e.g., Dirac with explicit basis labels, `\rho` for density operators, Choi-Jamiolkowski isomorphism)
  - Add stabilizer formalism chapter content (Ch. 10) into `error-correction.md` — Pauli group, normalizer, encoded operations
  - Add quantum operations / Kraus representation (Ch. 8) — can fit in `error-correction.md` or `algorithms.md` connections
  - Add Shor's algorithm complete walkthrough (Ch. 5) in `algorithms.md` — modular exponentiation, QFT, period finding, classical post-processing, success probability
  - Add Grover with amplitude amplification math (Ch. 6) in `algorithms.md`
  - Add physical implementations comparison (Ch. 7) in `hardware.md` — ion trap detail, cavity QED, optical, nuclear magnetic resonance (historical)
- For each enriched page, **mark Nielsen & Chuang as a primary reference** in "Further reading" or a section header note, e.g., `*This page synthesizes the wiki's earlier draft with Chs. 5, 6, 10 of Nielsen & Chuang.*`
- Cross-link liberally to: `/quantum-information-science/quantum-communication/`, `/quantum-information-science/quantum-internet/`, `/physics/quantum-mechanics/`, `/math/linear-algebra/`

## Format

Each enriched page follows the depth addendum (1500-3500 words; mandatory Mermaid diagram or comparison table; ≥2 worked examples; common pitfalls; cross-links; Python snippets in Qiskit/Cirq where useful).

## Workflow

1. `pdfinfo` + `pdftotext -l 30 "<pdf>" -` to see N&C's exact TOC + chapter ranges.
2. For each of the 4 foundational pages (`hardware`, `algorithms`, `error-correction`, optionally `quantum-ml`), read the relevant N&C chapter range and **rewrite the page in place** with combine-mode synthesis.
3. Update `intro.md` to mention N&C as a primary reference (preserve the deep-dive list).
4. Print summary of files modified.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-computing/`.
- Do NOT delete or modify deep-dive paper pages (`willow-surface-code-below-threshold.md`, `concatenated-bosonic-cat-qubits.md`, etc.).
- Do not modify `_category_.json`, config files, sidebars, or files outside this area.
- No `npm`. English. KaTeX. Mermaid (escape special chars in labels).
- Conservative — preserve good content from the existing draft, replace only where N&C clearly improves rigor or completeness.

Begin now.
