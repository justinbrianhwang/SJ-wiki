You are an autonomous content author for **SJ Wiki**. Add a **technique-named deep-dive page** for the **Quantum Internet** area of QIS, based on the paper below.

## Inputs

- **SOURCE_PDF**:
  - `f:/coding/SJ Wiki/tmp/Entanglement_swapping_systems_toward_a_quantum_int.pdf` — Davis et al. 2025 *Entanglement swapping systems toward a quantum internet* (Caltech/Fermilab/JPL; time-bin qubits at 1536.4 nm; conditional entanglement swapping with 87% fidelity; deployable system)

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-internet/`

## Naming policy

Page filename MUST be the **technique / system** name, NOT the paper title or author. Suggested:

- `entanglement-swapping-time-bin-telecom.md`
- or `deployable-entanglement-swapping-1536nm.md`

Pick one (your judgment). Use the technique-specific name, not the institution/author.

## Existing foundational pages (DO NOT REPLACE)

```
intro.md             (only append "## Deep-dive papers" section)
entanglement.md      (foundational; do not modify)
teleportation.md     (foundational; do not modify)
quantum-repeater.md  (foundational; do not modify)
```

## Per-page format

Depth addendum (1500-3500 words; Mermaid diagram or table; ≥2 worked examples; common pitfalls; cross-links). Sections:

- Frontmatter: `title:` (technique name + year, e.g. `"Deployable Entanglement Swapping at Telecom Band (Davis et al., 2025)"`), `sidebar_position:` starting at **20**
- 1-paragraph pitch with citation
- Problem & motivation — why telecom-band entanglement swapping with off-the-shelf components matters for the quantum internet roadmap
- Method
  - Time-bin qubit encoding (KaTeX: $|\psi\rangle = \alpha|\text{early}\rangle + \beta|\text{late}\rangle$, basis interferometer)
  - Electro-optic modulator preparation
  - Bell-state measurement projecting onto $|\Psi^-\rangle$
  - Superconducting nanowire single-photon detectors (SNSPDs) and their timing resolution
  - Characteristic function modeling of imperfections
- Visual (mandatory) — Mermaid block diagram of the swap setup (sources, BSM, SNSPDs, classical heralding)
- Experimental parameters — wavelength 1536.4 nm, fidelity 87%, estimated source-independent QKD secret key rate ~0.5 bits/sifted bit, modular components
- Results & comparison to prior demonstrations
- Connections — cross-link to foundational `entanglement.md` (Bell states, swapping), `teleportation.md` (related primitive), `quantum-repeater.md` (this is a repeater building block), `/quantum-information-science/quantum-communication/qkd.md` (source-independent QKD)
- Python/numpy sketch — characteristic function representation or fidelity-from-coincidence calculation
- Common pitfalls / reproduction notes (mode matching, indistinguishability, detector dead time)
- Further reading — name DLCZ protocol, photonic repeater papers, Pan Jianwei's satellite work

## Update intro.md

Append "## Deep-dive papers" with a 1-line summary of the new page. Preserve original content.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-internet/`.
- Do not modify `_category_.json`, config files, sidebars, or foundational pages.
- No `npm`. English. KaTeX. Mermaid (escape special chars).
- Conservative on fidelity / rate claims — quote conditions.
- Don't fabricate.

Begin now.
