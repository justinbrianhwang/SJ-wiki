You are an autonomous content author for **SJ Wiki**. Populate the **Quantum Communication** area of QIS with foundational concept pages.

## Inputs

- **SOURCE_PDFs**: NONE. Write from general knowledge. Future paper / textbook drops will be merged in combine mode.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-communication/`

## Pages to rewrite (4 stubs)

| File | Role |
|---|---|
| `intro.md` | Area hub: scope, why quantum (no-cloning enables QKD), Mermaid, sub-page list |
| `bb84.md` | BB84 protocol step-by-step |
| `qkd.md` | QKD families and security |
| `quantum-network.md` | Networking architectures and the path to quantum internet |

## Per-page content guidance

**`bb84.md`** — Bennett & Brassard 1984 protocol step-by-step: Alice prepares random basis/value in $\{|0\rangle, |1\rangle, |+\rangle, |-\rangle\}$; Bob measures in random basis; classical sift; QBER estimation; error reconciliation (Cascade / LDPC); privacy amplification. Security intuition: no-cloning theorem ⇒ measurement disturbs unknown state. Worked example: small key with 12 bits, trace through sifting and error rate. Decoy-state extension for practical photon sources.

**`qkd.md`** — comparative survey: BB84, B92, six-state, E91 (entanglement-based), decoy-state BB84, MDI-QKD, twin-field QKD (TF-QKD), device-independent QKD (DI-QKD). Comparison table: security model, distance limits, key rate scaling. Side channels: photon-number splitting (PNS), detector blinding, time-shift, Trojan-horse. Trusted-node networks (China backbone, Tokyo QKD network).

**`quantum-network.md`** — network stack analogy (physical / link / network / transport / application layers), entanglement as the network resource, Wehner's roadmap (6 stages of quantum internet maturity: trusted node → prepare-and-measure → entanglement-distribution → quantum-memory → few-qubit fault-tolerant → quantum computing networks). Cross-link to `/quantum-information-science/quantum-internet/` for entanglement-distribution + repeaters.

**`intro.md`** — area scope, no-cloning ↔ QKD relationship, Mermaid showing BB84 ⊂ QKD ⊂ Network ⊂ Internet hierarchy, sub-page list.

## Format

Depth addendum (1500-3500 words per page; mandatory Mermaid diagram or comparison table; ≥2 worked examples; common pitfalls; Python sketches where useful — e.g., a numpy simulation of BB84 sifting; cross-links).

## Cross-linking

- Sister QIS areas: `/quantum-information-science/quantum-internet/` (especially entanglement, teleportation, repeaters), `/quantum-information-science/quantum-security/` (PQC alternative path), `/quantum-information-science/quantum-computing/` (no-cloning, measurement)
- `/cs/cryptography/` for classical cryptography baseline
- `/physics/quantum-mechanics/` for measurement / no-cloning

## Constraints

- Stay inside OUTPUT_DIR. No `_category_.json` or external file edits.
- English. KaTeX math. Mermaid (escape special chars).
- Conservative on QKD network status (claims about distance / rate change rapidly).
- Future-PDF policy: leave room for paper deep-dives.

Begin now.
