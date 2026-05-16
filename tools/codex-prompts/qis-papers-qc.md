You are an autonomous content author for **SJ Wiki**. Add **technique-named deep-dive pages** for the **Quantum Computing** area of QIS, based on the papers listed below.

## Inputs

- **SOURCE_PDFs** (8 papers, all believed to be QC-area; verify by reading abstract):
  - `f:/coding/SJ Wiki/tmp/s41586-024-08449-y.pdf` — Google Quantum AI 2024 *Quantum error correction below the surface code threshold* (Willow distance-7 surface code)
  - `f:/coding/SJ Wiki/tmp/s41586-025-08642-7.pdf` — *Hardware-efficient QEC via concatenated bosonic qubits* (Nature 2025)
  - `f:/coding/SJ Wiki/tmp/s41586-025-08899-y.pdf` — Brock/Devoret 2025 *QEC of qudits beyond break-even* (GKP qutrit/ququart)
  - `f:/coding/SJ Wiki/tmp/2506.08331v1.pdf` — Zhang 2025 *Correcting a noisy quantum computer using a quantum computer* (quantum decoder circuit)
  - `f:/coding/SJ Wiki/tmp/s41467-026-71773-6_reference.pdf` — *Characterising failure mechanisms of error-corrected quantum logic gates* (Nature Communications)
  - `f:/coding/SJ Wiki/tmp/s41565-026-02140-1.pdf` — *Universal logical operations in a silicon ...* (Nature Nanotechnology, likely silicon spin qubits)
  - `f:/coding/SJ Wiki/tmp/s10791-025-09807-8.pdf` — Discover Computing review (verify topic; may belong to QML/algorithms or skip if non-QC)
  - `f:/coding/SJ Wiki/tmp/s41534-025-01089-8.pdf` — npj Quantum Information article (verify topic and place accordingly)

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-computing/`

## Naming policy (CRITICAL)

Page filenames MUST be the **technique / system / device name**, NOT the paper title or author. Examples:

- ✅ `willow-surface-code-below-threshold.md`, `concatenated-bosonic-cat-qubits.md`, `gkp-qudit-error-correction.md`
- ✅ `quantum-decoder-circuit.md`, `failure-mechanisms-of-ec-gates.md`, `silicon-spin-logical-qubits.md`
- ❌ `google-willow-2024.md`, `brock-devoret-2025.md`, `s41586-024-08449-y.md`

If a paper is a review/survey, name by the topic surveyed (e.g., `qec-review-2025.md`).

If one of the unknown papers (s10791, s41534) turns out NOT to be QC-area, simply skip it — note in your summary that you skipped it.

## Existing foundational pages in this area (DO NOT REPLACE — only `intro.md` may get an appended deep-dive list)

```
intro.md          (area hub — append "## Deep-dive papers" section listing new pages)
hardware.md       (foundational; do not modify)
algorithms.md     (foundational; do not modify)
error-correction.md  (foundational; do not modify)
quantum-ml.md     (foundational; do not modify)
```

## Per-page format

Each new deep-dive page follows the depth addendum (1500-3500 words; mandatory Mermaid diagram OR comparison table OR ASCII figure; ≥2 worked examples; common pitfalls; PyTorch/Qiskit/Cirq snippet where applicable; cross-links; conservative result claims).

Sections (in order):
- Frontmatter: `title:` (technique/system name + year, e.g. `"Willow Surface Code Below Threshold (Google, 2024)"`), `sidebar_position:` starting at **20** (after foundational pages 1-5)
- 1-paragraph elevator pitch with full citation
- **Problem & motivation** — what limitation this addresses
- **Method** — architecture / algorithm with precise KaTeX math (stabilizer measurements, code distance scaling, threshold equations, lattice surgery, transversal gates as relevant)
- **Visual** (mandatory) — Mermaid diagram of the architecture / code structure / control loop
- **Hyperparameters / system details** — number of physical qubits, code distance, gate fidelities, decoder latency, etc.
- **Headline results** — conservative quotation (state metric + value + conditions)
- **Connections** — cross-link to `error-correction.md` (foundation), `hardware.md` (foundation), other QC deep-dives, `/quantum-information-science/quantum-internet/`, `/physics/quantum-mechanics/`
- **PyTorch/Qiskit sketch** — minimal code where the technique is implementable (e.g., a tiny stabilizer measurement simulation; not a full reproduction)
- **Common pitfalls / reproduction notes**
- **Further reading** — name follow-up papers / related techniques

## Update intro.md

Append a section "## Deep-dive papers" to the existing `intro.md`. Preserve the original area-hub content. List each new page with a 1-line summary.

## Workflow

1. `pdftotext -l 2 "<pdf>" -` for each paper to verify title/authors/year.
2. For unknown papers (s10791, s41534), read more to determine if they fit this area; otherwise skip and report.
3. Write each deep-dive page.
4. Update `intro.md` with appended section.
5. Print summary of created/modified files.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-computing/`.
- Do not modify `_category_.json`, config files, sidebars, or the 4 foundational pages (hardware/algorithms/error-correction/quantum-ml).
- No `npm`. English. KaTeX math. Mermaid (escape `(`, `)`, `=`, `?`, `:`, `'`, `,`, `|`, `"`, `{`, `}` in labels by wrapping in `"..."`, internal `"` → `#quot;`).
- Conservative on benchmark / fidelity claims — quote with conditions (code distance, noise model, hardware).
- Don't fabricate.

Begin now.
