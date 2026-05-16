You are an autonomous content author for **SJ Wiki**. Populate the **Quantum Computing** area of QIS with foundational concept pages.

## Inputs

- **SOURCE_PDFs**: NONE. Write from general knowledge. Future textbook / paper drops will be merged into this area in **combine mode** — leave the structure clean so additions are easy.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-computing/`

## Pages to rewrite (5 stubs already exist)

| File | Role |
|---|---|
| `intro.md` | Area hub: scope, Mermaid showing Hardware ↔ Algorithms ↔ Error Correction ↔ Quantum ML, sub-page list |
| `hardware.md` | Physical implementations |
| `algorithms.md` | Quantum algorithms |
| `error-correction.md` | QEC |
| `quantum-ml.md` | Quantum machine learning |

## Per-page content guidance

**`hardware.md`** — superconducting transmons (Josephson junctions, transmon vs fluxonium/gmon), trapped ions (Paul traps, Mølmer-Sørensen gates), photonic (KLM scheme, measurement-based quantum computing), neutral atoms (Rydberg blockade, optical tweezer arrays), topological proposals (Majorana zero modes — note status conservatively). Include a comparison table: coherence time / gate fidelity / connectivity / scaling outlook for each platform.

**`algorithms.md`** — Deutsch-Jozsa, Bernstein-Vazirani, Simon's, Shor's factoring (modular exponentiation + QFT period finding), Grover's $O(\sqrt N)$ search and amplitude amplification, quantum phase estimation, quantum walks (discrete + continuous), HHL for linear systems. KaTeX math for the unitary structure of each algorithm.

**`error-correction.md`** — bit-flip 3-qubit, phase-flip code, Shor 9-qubit, Steane 7-qubit (CSS construction), stabilizer formalism (Pauli group, stabilizer group, normalizer), Knill-Laflamme conditions, surface codes (lattice / toric), threshold theorem (statement + rough proof intuition), fault-tolerant gates, magic state distillation overview.

**`quantum-ml.md`** — variational quantum classifiers, quantum kernels, QAOA for combinatorial optimization, quantum neural networks (parametrized circuits), barren plateau problem, expressibility / entangling capability, NISQ vs fault-tolerant QML, where the field's claims are speculative vs established (be honest).

## Format

Each page follows the depth addendum (1500-3500 words; mandatory Mermaid diagram OR comparison table OR ASCII figure; ≥2 worked examples; common pitfalls; Qiskit/Cirq Python snippets where applicable; cross-links).

Sections in order: Frontmatter → 1-paragraph elevator pitch → Definitions → Key results / formulas → Visual (mandatory) → Worked examples (≥2) → Code → Common pitfalls → Connections (cross-links) → Further reading (named canonical references — for paper deep-dives the user will drop PDFs later).

## Cross-linking

- `/physics/quantum-mechanics/` for the underlying physics
- `/math/linear-algebra/` for unitaries, tensor products
- Other QIS areas: `/quantum-information-science/quantum-communication/`, `/quantum-information-science/quantum-internet/`, `/quantum-information-science/quantum-security/`
- `/cs/cryptography/` (Shor → RSA threat), `/cs/deep-learning/`, `/cs/machine-learning/` (QML neighbors)

## Constraints

- Stay inside the OUTPUT_DIR. Do not modify `_category_.json`, files outside this area, or `docs/quantum-information-science/index.md` (the QIS hub).
- No `npm`. English. KaTeX math. Mermaid for visuals (special chars in labels wrapped in `"..."`, internal `"` → `#quot;`, `{`/`}` quoted too).
- Conservative on speculation: qubit count records, quantum advantage claims, NISQ vs fault-tolerant.
- Future-PDF policy: when textbooks / papers arrive for this area, content will be merged in combine mode — don't write the pages in a way that would conflict with that. Leave room for paper deep-dives without pre-claiming "the canonical reference is X".

Begin now.
