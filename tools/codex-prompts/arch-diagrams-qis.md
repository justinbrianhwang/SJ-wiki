## Domain: QIS (Quantum Computing / Communication / Internet / Sensing / Security)

- **TARGET_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/`

### Guidance

- **Quantum Computing**:
  - `intro.md`, `hardware.md`: transmon qubit equivalent circuit (Josephson junction + capacitor + readout resonator); ion trap setup (RF electrodes + DC electrodes + ion chain + lasers); photonic linear-optical block.
  - `algorithms.md`: **detailed quantum circuits** for
    - Deutsch-Jozsa (n+1 qubits, H ⊗ X|1⟩, oracle $U_f$, H, measure)
    - Bernstein-Vazirani (similar but recover hidden string)
    - Grover (oracle $U_f$, diffusion $2|s⟩⟨s| - I$, repeat $\sqrt N$ times)
    - QFT (Hadamards + controlled-phase ladder)
    - QPE (controlled-$U^{2^k}$ + inverse QFT)
    - Shor (modular exponentiation register + QFT)
    - HHL (block of phase estimation + controlled rotations + inverse phase estimation)
  - `error-correction.md`: 3-qubit bit-flip code circuit (encoding + syndrome measurement + correction); 9-qubit Shor code; 7-qubit Steane code stabilizer generators; surface code lattice with data qubits and X/Z stabilizers.
  - `quantum-ml.md`: VQE / QAOA parametrized circuit ansatz + classical optimizer loop; quantum kernel circuit.

- **Quantum Communication**:
  - `bb84.md`: BB84 protocol sequence diagram (Alice prepare → quantum channel → Bob measure → sift → estimate QBER → privacy amplification + reconciliation) with bases and bit values illustrated.
  - `qkd.md`: E91 entanglement-based variant; MDI-QKD with untrusted measurement; TF-QKD setup.
  - `quantum-network.md`: trusted-node network topology; layered stack (physical / link / network / transport / application).

- **Quantum Internet**:
  - `entanglement.md`: Bell pair generation circuits (CNOT + Hadamard); GHZ generation.
  - `teleportation.md`: full teleportation circuit (Alice's Bell measurement on |ψ⟩A and her half of |Φ⁺⟩AB, classical 2-bit channel, Bob's X / Z corrections).
  - `quantum-repeater.md`: BDCZ nested swapping + distillation tree; DLCZ memory-based repeater; all-photonic repeater.

- **Quantum Sensing**:
  - `intro.md`: Ramsey interferometry sequence; NV-center magnetometry block diagram (microwave + green pump + red fluorescence); atomic clock feedback (laser → atomic transition → error signal → AOM correction).

- **Quantum Security**:
  - `pqc.md`: lattice LWE problem geometric illustration; Kyber KEM encapsulate / decapsulate flow; SPHINCS+ hash-tree signature structure; Falcon NTRU lattice signing.
  - `quantum-safe-crypto.md`: hybrid TLS 1.3 handshake with classical + PQ KEX in parallel; crypto-agility migration sequence.

### Notes

- Quantum circuits in Mermaid: use `flowchart LR` with wires as labeled rectangles and gates as nodes. Example for teleportation:

  ```
  q0_psi[ |ψ⟩ ] --> H{H}
  H --> CX1((⊕))
  q1_phi_plus_a[ |Φ⁺⟩ qubit A ] --> CX1
  CX1 --> M0[ measure → c0 ]
  CX1 --> M1[ measure → c1 ]
  q2_phi_plus_b[ |Φ⁺⟩ qubit B ] --> X_c1[ X if c1=1 ]
  X_c1 --> Z_c0[ Z if c0=1 ]
  Z_c0 --> Out[ ≈ |ψ⟩ at Bob ]
  ```

Adapt as needed. The point is **a circuit diagram, not a hand-wave**.

Apply the policy. Begin now.
