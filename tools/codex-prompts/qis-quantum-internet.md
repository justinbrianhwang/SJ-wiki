You are an autonomous content author for **SJ Wiki**. Populate the **Quantum Internet** area of QIS with foundational concept pages.

## Inputs

- **SOURCE_PDFs**: NONE. Write from general knowledge. Future paper drops will merge in combine mode.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-internet/`

## Pages to rewrite (4 stubs)

| File | Role |
|---|---|
| `intro.md` | Area hub |
| `entanglement.md` | Entanglement as a network resource |
| `teleportation.md` | Quantum teleportation as the routing primitive |
| `quantum-repeater.md` | Repeaters and long-distance entanglement |

## Per-page content guidance

**`entanglement.md`** — Bell states $|\Phi^\pm\rangle, |\Psi^\pm\rangle$ with explicit matrix forms; GHZ ($|000\rangle + |111\rangle$); W state; Schmidt decomposition; entanglement entropy $S(\rho_A) = -\mathrm{Tr}(\rho_A \log \rho_A)$; monogamy of entanglement; distillation protocols (DEJMPS, hashing); LOCC restrictions; entanglement as a resource (cost / rate). Worked example: compute Schmidt decomp for a 2-qubit state.

**`teleportation.md`** — Bennett-Brassard-Crepeau-Jozsa-Peres-Wootters 1993 protocol. Full math: Alice has $|\psi\rangle_A = \alpha|0\rangle + \beta|1\rangle$ and shares $|\Phi^+\rangle_{BC}$ with Bob. Joint state expansion. Alice's Bell measurement on $(A,B)$ collapses Bob's $C$ to one of four Pauli-transformed copies of $|\psi\rangle$. Alice sends 2 classical bits; Bob applies $I/X/Z/XZ$. Result: $|\psi\rangle$ now at Bob, $A$ and $B$ destroyed (consistent with no-cloning). Fidelity, experimental demonstrations (Innsbruck, Rome, satellite-based by Pan Jianwei).

**`quantum-repeater.md`** — long-distance entanglement problem (channel loss exponential in distance). BDCZ scheme (Briegel-Dür-Cirac-Zoller): nested swapping + distillation. DLCZ (Duan-Lukin-Cirac-Zoller) with atomic ensembles. All-photonic repeaters. Quantum memory requirements. Repeater rate vs distance trade-off (square-root scaling under BDCZ vs linear in classical). Concrete examples of small-scale demonstrations (Delft NV-center node-to-node).

**`intro.md`** — scope statement, Wehner's 6 stages of quantum internet, why teleportation is the routing primitive (vs forwarding), Mermaid showing entanglement distribution as the resource, sub-page list.

## Format

Depth addendum (1500-3500 words; mandatory Mermaid diagram or comparison table; ≥2 worked examples; common pitfalls; Python (numpy / Qiskit) sketches; cross-links).

## Cross-linking

- `/quantum-information-science/quantum-communication/` (BB84, QKD, network)
- `/quantum-information-science/quantum-computing/error-correction` (memory needs FT)
- `/physics/quantum-mechanics/density-operator-entanglement-decoherence`
- `/math/linear-algebra/inner-product-spaces` (Schmidt decomposition / SVD)

## Constraints

- Stay inside OUTPUT_DIR. No external edits.
- English. KaTeX math. Mermaid (escape special chars).
- Conservative on experimental progress.

Begin now.
