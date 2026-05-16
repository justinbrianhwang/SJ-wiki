You are an autonomous content author for **SJ Wiki**. Populate the **Quantum Information Science** section with foundational, textbook-quality concept pages.

## Inputs

- **SOURCE_PDFs**: NONE for this run. Write from general knowledge of QIS. This is a well-established field with stable definitions and canonical results.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/`

## Current structure (do NOT delete; rewrite stub `intro.md` files in place)

```
docs/quantum-information-science/
├── index.md                          (hub — leave as-is)
├── quantum-computing/
│   ├── intro.md                      (stub → rewrite as area intro)
│   ├── hardware.md                   (stub → rewrite as full page)
│   ├── algorithms.md                 (stub → rewrite as full page)
│   ├── error-correction.md           (stub → rewrite as full page)
│   └── quantum-ml.md                 (stub → rewrite as full page)
├── quantum-communication/
│   ├── intro.md (rewrite)
│   ├── bb84.md (rewrite)
│   ├── qkd.md (rewrite)
│   └── quantum-network.md (rewrite)
├── quantum-internet/
│   ├── intro.md (rewrite)
│   ├── entanglement.md (rewrite)
│   ├── teleportation.md (rewrite)
│   └── quantum-repeater.md (rewrite)
├── quantum-sensing/
│   └── intro.md (rewrite as a full standalone page since it has no leaf pages)
└── quantum-security/
    ├── intro.md (rewrite)
    ├── pqc.md (rewrite)
    └── quantum-safe-crypto.md (rewrite)
```

Total: **18 pages to populate** (5 area intros + 13 leaf pages, with `quantum-sensing/intro.md` being a single comprehensive page).

## What to produce

Each page follows the depth addendum (1500-3500 words; mandatory Mermaid diagram OR comparison table OR ASCII figure; ≥2 worked examples; common pitfalls; Python (Qiskit/Cirq) snippets where applicable; cross-links).

### Quantum Computing area

**`intro.md`** (area hub): scope statement, sub-page list, Mermaid showing how Hardware ↔ Algorithms ↔ Error Correction ↔ Quantum ML interact.

**`hardware.md`**: superconducting transmons (Josephson junctions, gmon/fluxonium), trapped ions (Paul traps, Mølmer-Sørensen), photonic (KLM, measurement-based), neutral atoms (Rydberg, optical tweezers), topological (Majorana zero modes — be conservative on status). Comparison table of coherence times, gate fidelity, scaling outlook.

**`algorithms.md`**: Deutsch-Jozsa, Bernstein-Vazirani, Simon's algorithm (intuition: oracle structure → exponential speedup); Shor's factoring (modular exponentiation + QFT period-finding); Grover's search ($O(\sqrt{N})$ amplitude amplification); quantum phase estimation; quantum walks (continuous + discrete); HHL for linear systems. Math precise where standard.

**`error-correction.md`**: bit-flip 3-qubit, Shor 9-qubit, Steane 7-qubit, CSS construction, stabilizer formalism (Pauli group, Clifford group), surface codes (topological / lattice), threshold theorem statement, fault tolerance overview, magic state distillation intro.

**`quantum-ml.md`**: variational quantum classifiers, quantum kernels (PennyLane / Qiskit), QAOA for combinatorial optimization, quantum neural networks, barren plateau problem, expressibility / entangling capability, NISQ vs fault-tolerant ML, where claims are speculative vs established.

### Quantum Communication area

**`intro.md`**: scope, no-cloning enabling QKD, protocol families, link to Quantum Internet for distance scaling.

**`bb84.md`**: the protocol step-by-step (Alice prepares random basis/value; Bob measures random basis; sift; estimate QBER; privacy amplification), security argument via no-cloning, basis reconciliation, decoy-state extension. Worked numeric example with small key.

**`qkd.md`**: BB84, B92, E91 (entanglement-based), six-state, decoy-state BB84, MDI-QKD, twin-field QKD, device-independent QKD, side-channel attacks (photon-number-splitting, detector blinding), trusted-node networks.

**`quantum-network.md`**: network stack analogy (physical / link / network / transport), entanglement as a resource, network protocols (Wehner's Quantum Internet roadmap stages), routing entanglement.

### Quantum Internet area

**`intro.md`**: scope, entanglement-as-bandwidth, why teleportation is the routing primitive, repeater requirements, Wehner's 6 stages of quantum internet development.

**`entanglement.md`**: Bell states $|\Phi^\pm\rangle, |\Psi^\pm\rangle$, GHZ states, W states, multipartite entanglement, Schmidt decomposition, entanglement entropy, monogamy of entanglement, distillation (DEJMPS protocol).

**`teleportation.md`**: 1993 BBCJPW protocol (full math: Alice's Bell measurement on $|\psi\rangle_A \otimes |\Phi^+\rangle_{AB}$ → Bob's correction by classical 2-bit message), no-cloning consistency, fidelity, experimental demonstrations.

**`quantum-repeater.md`**: BDCZ scheme (entanglement swapping + distillation in nested levels), DLCZ protocol (atomic ensembles), all-photonic repeaters, memory requirements, swap probability, repeater rate vs distance trade-off.

### Quantum Sensing area

**`intro.md`** (single standalone page): quantum metrology, standard quantum limit (SQL = $1/\sqrt{N}$) vs Heisenberg limit ($1/N$), squeezed states, NOON states, NV centers in diamond (magnetometry), atomic clocks (Cs, optical lattice), atom interferometry (gravimetry, gyroscopes), LIGO-like quantum-enhanced detectors, Fisher information / Cramér-Rao bound, applications (GPS-denied navigation, biomedical imaging, gravity surveying).

### Quantum Security area

**`intro.md`**: PQC vs QKD distinction; the threat (Shor breaks RSA/ECDSA), but Grover only halves AES key security; migration timeline.

**`pqc.md`**: lattice-based (LWE, Module-LWE; **Kyber** KEM, **Dilithium** signature, **Falcon**), hash-based (XMSS, SPHINCS+), code-based (Classic McEliece), multivariate (Rainbow — broken; cautionary tale), isogeny-based (SIKE — broken in 2022, retrospective). NIST standardization (Round 1-4 history, finalists, FIPS 203/204/205 selection in 2024).

**`quantum-safe-crypto.md`**: migration strategies (hybrid schemes, crypto-agility, dual-stack TLS), real deployments (Cloudflare, Google, AWS hybrid Kyber), timeline considerations ("harvest now, decrypt later"), key sizes / performance trade-offs vs RSA/ECC, organizational impact (NSA CNSA 2.0).

## Cross-linking

- `/physics/quantum-mechanics/` for the underlying physics (e.g., from `algorithms.md` → measurement page; from `hardware.md` → spin-1/2 page)
- `/math/linear-algebra/` for unitaries, eigenstuff, tensor products
- `/cs/cryptography/` for classical cryptography that PQC replaces
- `/cs/deep-learning/`, `/cs/machine-learning/` for QML's classical neighbors
- Cross-link within QIS heavily (BB84 ↔ QKD ↔ quantum network ↔ repeater ↔ teleportation ↔ entanglement)

## Workflow

1. `ls -R docs/quantum-information-science/` to confirm current stubs.
2. Rewrite each of the 18 pages.
3. Print summary listing every file modified.

## Constraints

- Stay inside `docs/quantum-information-science/`.
- Do not modify `_category_.json`, `index.md` (hub), config files, sidebars, or files outside the dir.
- No `npm`.
- English. Mathematically and physically precise. KaTeX math (`$...$`, `$$...$$`, `$$\begin{aligned}...\end{aligned}$$`).
- Mermaid labels with special characters (`(`, `)`, `=`, `?`, `:`, `'`, `,`, `|`, `"`, `{`, `}`) wrapped in `"..."`; internal `"` → `#quot;`.
- Conservative on speculation: e.g., quantum advantage claims should cite the specific task, NISQ vs fault-tolerant distinction, etc.
- Don't fabricate. If unsure of a number (qubit count records, gate fidelity SOTA), give a range and date the assertion.

Begin now.
