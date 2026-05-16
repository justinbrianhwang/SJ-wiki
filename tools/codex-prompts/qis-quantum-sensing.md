You are an autonomous content author for **SJ Wiki**. Populate the **Quantum Sensing** area of QIS with a single comprehensive foundational page.

## Inputs

- **SOURCE_PDFs**: NONE. Write from general knowledge.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-sensing/`
- **Pages**: Just `intro.md` (rewrite the stub as a full-length standalone page; this area has no sub-pages yet — future textbook drops can add them).

## Page content

A single comprehensive **Quantum Sensing** page (2500-4000 words because it covers a whole area). Sections:

1. **Intuition** — sensing as parameter estimation: a quantum probe interacts with an unknown parameter and the goal is precise estimation under physical constraints.

2. **Definitions** — quantum metrology, probe state, signal Hamiltonian, measurement, Fisher information $F_\theta$, classical Cramér-Rao bound $\Delta\theta \ge 1/\sqrt{F_\theta}$, quantum Fisher information, quantum Cramér-Rao bound.

3. **Standard Quantum Limit vs Heisenberg Limit** — for $N$ classical probes, $\Delta\theta \sim 1/\sqrt N$ (SQL). For entangled / squeezed quantum probes, can achieve $1/N$ (Heisenberg). Show the math for the simplest case (Ramsey interferometry, NOON states).

4. **Physical platforms**:
   - **NV centers in diamond** — for magnetometry, biology, MRI; nitrogen-vacancy color centers as 3-level systems; optically detected magnetic resonance.
   - **Atomic clocks** — Cs fountain, optical lattice clocks (Sr, Yb, Hg); fractional frequency stability $\sim 10^{-18}$; clock comparisons.
   - **Atom interferometry** — Mach-Zehnder analog with cold atoms; gravimetry, gyroscopy, fundamental constant measurement; gradiometers.
   - **Squeezed light** — LIGO and ground-based GW detection using squeezed vacuum injection.
   - **Spin-squeezed BECs** — for compact accelerometers, gravimeters.
   - **Photon-counting sensors** — for low-light astronomy and biological imaging.

5. **Visual** (mandatory) — comparison table of platforms (parameter sensed, sensitivity, frequency range, maturity).

6. **Worked example 1**: Compute the Heisenberg-limit improvement for $N=10$ entangled probes vs SQL. Show factor-of-$\sqrt{10}$ ≈ 3.16x improvement.

7. **Worked example 2**: NV-center magnetometry — given a Ramsey contrast and integration time, estimate the achievable magnetic field sensitivity.

8. **Code**: Python (numpy) sketch computing Fisher information for a simple two-level probe undergoing phase accumulation $\theta$.

9. **Common pitfalls** — decoherence kills the Heisenberg scaling; preparing many-body entangled states is fragile; sensitivity numbers in papers depend heavily on assumptions; "quantum advantage" in sensing requires careful baseline comparison.

10. **Applications** — GPS-denied navigation (Defense applications, conservatively framed), biomedical imaging (NV-MRI), gravity surveying (mineral / hydrocarbon exploration), dark matter searches, tests of fundamental physics.

11. **Connections**:
    - `/quantum-information-science/quantum-computing/` (some qubit platforms double as sensors)
    - `/physics/quantum-mechanics/` (measurement theory)
    - `/math/probability-and-random-variables/` (Fisher information, Cramér-Rao)
    - `/math/statistics/estimation-and-confidence-intervals` (CRB connection)

12. **Further reading** — Degen, Reinhard, Cappellaro 2017 review *Quantum Sensing*; Pezzè et al. *Quantum metrology with non-classical states of atomic ensembles*; Giovannetti, Lloyd, Maccone *Quantum-enhanced measurements* and follow-ups. (Reference by name; future paper drops can deep-dive.)

## Format

Single page following the depth addendum (longer than usual: 2500-4000 words because this is a one-page area). Mandatory Mermaid diagram or comparison table. ≥2 worked examples. Common pitfalls. Python code.

## Constraints

- Only modify `intro.md`. Do not create new files (that's for future paper drops).
- No external file edits, no `npm`.
- English. KaTeX math. Mermaid (escape special chars).
- Conservative on numbers (state ranges and dates).

Begin now.
