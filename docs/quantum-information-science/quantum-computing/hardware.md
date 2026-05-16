---
title: Hardware
sidebar_position: 2
---

# Hardware

Quantum hardware is the engineering layer that turns abstract qubits, gates, and measurements into controlled physical systems. The same circuit drawn in [algorithms](/quantum-information-science/quantum-computing/algorithms) looks very different in an ion trap, optical cavity, nuclear magnetic resonance experiment, superconducting chip, neutral-atom array, or photonic network, so hardware comparisons must track coherence, controllability, initialization, readout, connectivity, and compatibility with [error correction](/quantum-information-science/quantum-computing/error-correction).

*This page synthesizes the wiki's earlier hardware draft with Chapter 7 of Nielsen and Chuang. N&C's central organizing idea is implementation requirements: represent quantum information robustly, perform controlled unitary transformations, prepare fiducial input states, and measure outputs. Modern superconducting, neutral-atom, and topological notes are supplementary context beyond the book's original platform emphasis.*

## Definitions

A **physical qubit** is a two-level subsystem chosen inside a real device. It may be two hyperfine states of a trapped ion, two polarization or spatial modes of a photon, two nuclear spin states in a molecule, two levels of a superconducting circuit, two clock states of a neutral atom, or a protected parity degree of freedom in a topological proposal. The computational basis is written with explicit basis labels, such as $\vert 0\rangle, \vert 1\rangle$, but the laboratory system may have many extra levels that cause leakage.

Nielsen and Chuang phrase the minimum implementation problem in four requirements:

| Requirement | Hardware meaning | Typical failure mode |
|---|---|---|
| Represent quantum information | Choose a finite, addressable Hilbert-space subspace | Leakage, uncontrolled degeneracy, excessive environmental coupling |
| Perform unitary transformations | Control Hamiltonians well enough to realize a universal gate set | Calibration error, crosstalk, slow gates, unwanted entanglement with controls |
| Prepare fiducial initial states | Repeatedly initialize states such as $\vert 0\rangle^{\otimes n}$ with high fidelity | Thermal population, imperfect cooling, residual entropy |
| Measure output results | Couple selected qubits to a classical record | Low signal-to-noise ratio, measurement back-action, slow reset |

The book's discussion predates many present devices, but its abstraction still works. A candidate platform is not judged by qubit count alone; it is judged by whether the entire prepare-control-measure loop can be made reliable enough for logical computation.

Important hardware metrics include:

| Metric | Meaning | Why it matters |
|---|---|---|
| $T_1$ | Energy relaxation time | Limits survival of excited-state population |
| $T_2$ | Dephasing time | Limits coherence of relative phases |
| $t_{\mathrm{op}}$ | Time for an elementary operation | Sets how many gates fit inside a coherence window |
| $F_1, F_2$ | Single- and two-qubit gate fidelities | Two-qubit gates usually dominate algorithmic error |
| Connectivity | Which qubits interact directly | Determines routing overhead and QEC layout |
| Readout fidelity | Probability of correct measurement record | Crucial for repeated syndrome extraction |
| Reset latency | Time to prepare a fresh state | Matters for ancilla-heavy error correction |
| Crosstalk and leakage | Unwanted response outside the intended gate | Creates correlated and non-Pauli noise |

**Optical photons** can encode qubits in dual-rail states, where $\vert 0_L\rangle=\vert 01\rangle$ and $\vert 1_L\rangle=\vert 10\rangle$ across two optical modes, or in polarization, time-bin, path, or frequency modes. Photons are natural flying qubits for [quantum communication](/quantum-information-science/quantum-communication/), but deterministic photon-photon gates are hard because ordinary optical nonlinearities are weak at the single-photon level.

**Cavity QED** couples atoms to quantized cavity modes. In the ideal strong-coupling picture, an atom and a single field mode exchange excitations through a Jaynes-Cummings interaction. The cavity can mediate interactions between photons or between atoms, but loss through cavity mirrors and spontaneous emission must be controlled.

**Trapped ions** store qubits in internal electronic or hyperfine states of charged atoms confined by electromagnetic fields. Laser pulses drive single-qubit rotations and couple internal states to shared motional modes. The shared phonon modes provide an entangling bus, making ion traps one of N&C's clearest examples of controllable microscopic quantum logic.

**Nuclear magnetic resonance** uses nuclear spins in molecules as qubits and radio-frequency pulses for control. NMR was historically important because it demonstrated small quantum algorithms with excellent coherent control, but it uses large room-temperature ensembles and effective-pure-state preparation, so signal scaling is a serious obstacle to large-scale computation.

**Superconducting circuits** are the dominant modern solid-state gate-model platform. Transmons are nonlinear microwave oscillators made from Josephson junctions and capacitors. The transmon regime reduces charge-noise sensitivity, while resonators and tunable couplers supply readout and entangling gates. This is a modern successor to the superconducting charge and flux proposals N&C discuss in their "other implementation schemes" section.

**Silicon spin qubits** encode quantum information in electron or nuclear spin states in isotopically purified silicon, often using donors or quantum dots. Their appeal is compatibility with mature semiconductor fabrication and potentially long coherence; their scaling pressure is precise placement, addressability, exchange or hyperfine control, readout, and integration into repeated [error-correction](/quantum-information-science/quantum-computing/error-correction) cycles.

**Neutral atoms** use optically trapped atoms in tweezer arrays or lattices. Rydberg excitation creates strong controllable interactions through blockade, giving flexible geometries for simulation and gate-model experiments. N&C mention optical-lattice proposals; modern tweezer arrays are a later development.

**Topological proposals** encode information nonlocally, often using anyons or Majorana zero modes. The appeal is hardware-level protection from some local noise processes. The conservative status is that topological quantum computing remains an active research program rather than an established scalable production platform.

## Key results

The first N&C hardware figure of merit is the approximate number of coherent operations available before decoherence:

$$
n_{\mathrm{op}} \approx \frac{\tau_Q}{t_{\mathrm{op}}},
$$

where $\tau_Q$ is a characteristic coherence time and $t_{\mathrm{op}}$ is an elementary operation time. This ratio is not a full error model, but it captures the core engineering tension: strong coupling gives fast gates, while isolation gives long coherence, and a platform must balance both.

A controlled qubit is often modeled by a Hamiltonian in a rotating frame,

$$
H(t)=\frac{\hbar}{2}\left(\Delta(t)Z+\Omega_x(t)X+\Omega_y(t)Y\right),
$$

so a pulse of duration $\tau$ ideally implements

$$
U=\mathcal{T}\exp\left(-\frac{i}{\hbar}\int_0^\tau H(t)\,dt\right).
$$

Real gates deviate from this unitary description because the qubit is open to controls and environment. In the notation of [quantum error correction](/quantum-information-science/quantum-computing/error-correction), the implemented process is more accurately a quantum channel

$$
\mathcal{E}(\rho)=\sum_k E_k\rho E_k^\dagger,
$$

where leakage, relaxation, dephasing, measurement back-action, and classical control errors are folded into the operation elements $E_k$.

For optical photons, passive linear optics implements mode transformations such as beamsplitters and phase shifters. In a two-mode basis, a beamsplitter acts like a small unitary rotation of creation operators. Single-photon states are easy to transport and measure compared with many matter qubits, but two-qubit gates require either strong nonlinearities, measurement-induced gates with ancillas and feed-forward, or cluster-state methods. This explains why photonics is excellent for networking while gate-model photonic computing is resource-sensitive.

For cavity QED, a simplified resonant Jaynes-Cummings interaction has the form

$$
H_{\mathrm{JC}}=\hbar g(a^\dagger\sigma_-+a\sigma_+),
$$

where $a,a^\dagger$ act on the cavity mode and $\sigma_\pm$ act on the atom. Useful operation requires coherent coupling $g$ to dominate decay rates such as cavity loss $\kappa$ and atomic spontaneous emission $\gamma$. In that regime the atom and field can exchange quantum information before it leaks into the environment.

For ion traps, entanglement arises by coupling spin states to collective vibrational modes. A simplified modern entangling gate is often written as

$$
U_{\mathrm{MS}}(\theta)=\exp\left(-i\frac{\theta}{2}X_iX_j\right),
$$

up to single-qubit rotations and convention choices. N&C present the older Cirac-Zoller style logic in terms of sideband transitions and phonon-mediated gates; the enduring idea is the same: internal states are good memories, and shared motion supplies a controllable interaction.

For NMR, the thermal state at temperature $T$ is a density operator close to maximally mixed:

$$
\rho \approx \frac{I}{2^n}+\epsilon\Delta\rho,
\qquad
\epsilon \approx \frac{hf}{2k_BT}
$$

for a spin transition of frequency $f$ with $\epsilon\ll 1$. The useful signal is carried by the small deviation term $\Delta\rho$, not by a pure ensemble of identical $\vert 0\rangle^{\otimes n}$ systems. This is why NMR was a powerful control testbed but not a clean route to scalable fault-tolerant quantum computing.

Finally, hardware must be evaluated through the QEC cycle:

$$
\text{prepare} \rightarrow \text{entangle} \rightarrow \text{measure syndrome} \rightarrow \text{decode} \rightarrow \text{update Pauli frame}.
$$

A device with beautiful isolated qubits but slow, noisy, or destructive measurement may be poor for fault tolerance. Conversely, a platform with modest coherence can still be competitive if its gates and measurements are fast, parallel, and repeatable.

### Encoded logical operations in silicon spin hardware

Zhang, Xu, Zhang, Duan, and collaborators [1] demonstrated an encoded logical workflow in a phosphorus-donor silicon processor. The contribution was not long-distance error correction; it was a compact logical-control stack: prepare states in a $[[4,2,2]]$ detection code, perform logical Clifford operations, inject a non-Clifford $T$ gate by measurement using an extra nuclear-spin ancilla, and run a two-logical-qubit VQE-style chemistry demonstration.

The $[[4,2,2]]$ code encodes two logical qubits in four physical spin qubits and detects, rather than corrects, arbitrary single-qubit errors. Its stabilizers can be written as

$$
S_X=X_1X_2X_3X_4,
\qquad
S_Z=Z_1Z_2Z_3Z_4.
$$

A convenient logical basis is

$$
\begin{aligned}
|00\rangle_L &= \frac{|0000\rangle+|1111\rangle}{\sqrt{2}},\\
|01\rangle_L &= \frac{|0011\rangle+|1100\rangle}{\sqrt{2}},\\
|10\rangle_L &= \frac{|0101\rangle+|1010\rangle}{\sqrt{2}},\\
|11\rangle_L &= \frac{|0110\rangle+|1001\rangle}{\sqrt{2}}.
\end{aligned}
$$

Each codeword is a $+1$ eigenstate of both stabilizers. For example,

$$
S_X|10\rangle_L
=\frac{|1010\rangle+|0101\rangle}{\sqrt{2}}
=|10\rangle_L,
$$

and both computational-basis components of $\vert 10\rangle_L$ have even parity, so $S_Z\vert 10\rangle_L=\vert 10\rangle_L$. A single physical $X$ or $Z$ error flips at least one stabilizer parity, which lets the experiment project data back into the logical subspace during postprocessing.

Logical Pauli operators are represented by multi-spin physical operators such as

$$
X_LI_L \leftrightarrow X_1X_3,
\qquad
I_LX_L \leftrightarrow X_1X_2,
$$

and

$$
Z_LI_L \leftrightarrow Z_1Z_2,
\qquad
I_LZ_L \leftrightarrow Z_1Z_3.
$$

The hardware point is that a donor cluster can provide high connectivity through shared electron-mediated control, making these multi-qubit logical operations accessible in a small device. The limitation is equally important: postprocessed parity projection and distance-2 detection are not substitutes for repeated real-time syndrome correction. Scaling this direction requires arrays of donor clusters, better readout, and a path from detected errors to corrected logical operation.

The two-logical-qubit application used expectation values of a Hamiltonian of the form

$$
H=g_0+g_1Z_LI_L+g_2I_LZ_L+g_3Z_LZ_L+g_4X_LX_L+g_5Y_LY_L.
$$

Given coefficients $g_i$ and measured logical observables, the energy estimate is the ordinary linear combination

$$
\langle H\rangle
=g_0+g_1\langle ZI\rangle+g_2\langle IZ\rangle+g_3\langle ZZ\rangle
+g_4\langle XX\rangle+g_5\langle YY\rangle.
$$

This makes the experiment a useful hardware milestone for encoded control and mitigation, not evidence of a chemistry speedup.

## Visual

```mermaid
flowchart TD
  subgraph Transmon["Superconducting transmon module"]
    direction TB
    TCtrl["Room-temperature control rack<br/>AWG, DAC, microwave sources"] --> TXY["XY microwave drive<br/>X/Y rotations"]
    TCtrl --> TZ["Flux or coupler bias<br/>frequency and ZZ tuning"]
    TJ["Josephson junction<br/>nonlinear inductance E_J"] --- TCap["Shunt capacitor<br/>charging energy E_C"]
    TJ --- TQ["Transmon qubit<br/>|0>, |1>, leakage |2>"]
    TCap --- TQ
    TXY --> TQ
    TZ --> TQ
    TQ --> TG["Entangling operation<br/>cross-resonance, iSWAP, CZ, or tunable coupler"]
    TQ --> TRes["Readout resonator<br/>state-dependent frequency shift"]
    TRes --> TPurcell["Purcell/filter chain<br/>protect qubit from readout loss"]
    TPurcell --> TADC["Amplifier + ADC<br/>I/Q samples -> bit #lsqb;0 or 1"]"]
  end

  subgraph IonTrap["Trapped-ion processor"]
    direction TB
    RF["RF electrodes<br/>radial confinement"] --> Trap["Linear Paul trap<br/>pseudopotential well"]
    DC["Segmented DC electrodes<br/>axial confinement and shuttling"] --> Trap
    Trap --> Chain["Ion chain<br/>N addressable qubits + shared motional modes"]
    Cool["Doppler and sideband cooling lasers"] --> Chain
    Raman["Raman or quadrupole beams<br/>1q gates and MS entangling gates"] --> Chain
    Chain --> Motion["Motional bus<br/>collective modes mediate 2q gates"]
    Motion --> IEnt["Mølmer-Sørensen gate<br/>XX(theta) on selected ions"]
    Chain --> IDet["State-dependent fluorescence<br/>PMT/CCD camera -> bits #lsqb;N"]"]
  end

  subgraph Photonic["Linear-optical photonic block"]
    direction TB
    Src["Single-photon or weak-coherent sources<br/>time-bin, polarization, or dual-rail"] --> Enc["Mode encoding<br/>logical |0>, |1> across optical modes"]
    Enc --> Mesh["Interferometer mesh<br/>beamsplitters + phase shifters"]
    Mesh --> NL["Optional nonlinear or measurement-induced gate<br/>KLM-style ancillas"]
    NL --> FF["Fast feed-forward switch<br/>condition on detector clicks"]
    FF --> Det["SNSPD/APD detectors<br/>click pattern -> sample bit string"]
  end

  subgraph Stack["Hardware-to-algorithm stack"]
    direction TB
    Spec["Circuit specification<br/>logical qubits #lsqb;k"], depth [D], measurements"] --> Compile["Compiler and scheduler<br/>map gates to native operations"]
    Compile --> Cal["Calibration loop<br/>Rabi, Ramsey, crosstalk, readout assignment"]
    Cal --> Run["Execution batch<br/>shots #lsqb;S"] with timing and reset"]
    Run --> Noise["Noise model<br/>T1/T2, leakage, loss, SPAM, crosstalk"]
    Noise --> QEC["QEC cycle<br/>syndrome measurement + decoder + Pauli frame"]
    QEC --> Result["Algorithm result<br/>samples, expectation values, logical outcomes"]
    QEC -. "decoder and calibration feedback" .-> Cal
  end

  TADC --> Cal
  IDet --> Cal
  Det --> Cal
  Compile --> TXY
  Compile --> Raman
  Compile --> Mesh
```

This diagram decomposes hardware into three concrete implementations rather than treating "qubit" as a black box. The transmon block shows the Josephson-junction-plus-capacitor circuit and dispersive readout chain, the ion-trap block separates RF/DC confinement from laser gates and fluorescence, and the photonic block shows source, interferometer, feed-forward, and detectors. The shared stack at the bottom makes the I/O contract explicit: a logical circuit is compiled to native controls, executed as shots, modeled as noise, and fed into QEC and calibration loops.

| Platform | N&C emphasis | Strength | Main scaling pressure |
|---|---|---|---|
| Optical photons | Dual-rail photons, beamsplitters, nonlinear optical media | Excellent transmission and room-temperature propagation | Loss, source quality, detector efficiency, feed-forward, weak deterministic interactions |
| Cavity QED | Strong atom-photon coupling | Mediated interactions between flying and stationary qubits | Cavity loss, spontaneous emission, mode matching |
| Trapped ions | Internal states plus motional bus | Long coherence and high-fidelity control | Gate speed, motional heating, large-chain crowding, modular interconnects |
| NMR | Ensemble nuclear-spin control | Historically important pulse control and small algorithms | Exponential signal loss in effective-pure-state schemes |
| Superconducting circuits | Mentioned as charge/flux proposals; modern transmons extend this line | Fast gates, lithographic scaling, strong control stack | Cryogenic wiring, crosstalk, leakage, calibration drift |
| Silicon spin qubits | Mostly beyond N&C's main platform treatment | Long spin coherence and semiconductor manufacturing path | Placement, readout, donor or dot integration, repeated syndrome extraction |
| Neutral atoms | Optical-lattice proposals; modern tweezers are supplementary | Large flexible arrays and Rydberg interactions | Atom loss, loading, uniformity, mid-circuit measurement |
| Topological proposals | Mostly beyond N&C's main treatment | Possible passive protection from local noise | Experimental maturity and controllable logical gates |

## Worked example 1: Operation budget from coherence and gate time

**Problem.** Compare two simplified platforms. Platform A has coherence time $\tau_Q=1$ s and two-qubit gate time $t_{\mathrm{op}}=100$ microseconds. Platform B has $\tau_Q=100$ microseconds and $t_{\mathrm{op}}=200$ ns. Estimate $n_{\mathrm{op}}=\tau_Q/t_{\mathrm{op}}$ for each.

**Method.**

1. Convert Platform A's gate time:

$$
100\ \mu\mathrm{s}=100\times 10^{-6}\ \mathrm{s}=10^{-4}\ \mathrm{s}.
$$

2. Compute Platform A's operation budget:

$$
n_{\mathrm{op},A}=\frac{1}{10^{-4}}=10^4.
$$

3. Convert Platform B's values:

$$
\tau_Q=100\times 10^{-6}\ \mathrm{s}=10^{-4}\ \mathrm{s},
\qquad
t_{\mathrm{op}}=200\times 10^{-9}\ \mathrm{s}=2\times 10^{-7}\ \mathrm{s}.
$$

4. Compute Platform B's operation budget:

$$
n_{\mathrm{op},B}=\frac{10^{-4}}{2\times 10^{-7}}=5\times 10^2.
$$

**Answer.** Platform A permits roughly $10{,}000$ elementary gate times per coherence time, while Platform B permits roughly $500$. The checked interpretation is limited: a real error budget also includes gate calibration, measurement, leakage, idle noise, and correlated errors, so this ratio is a first screening metric, not a threshold estimate.

## Worked example 2: Thermal polarization in an NMR-style qubit

**Problem.** A nuclear spin transition has frequency $f=500$ MHz at room temperature $T=300$ K. Use the high-temperature estimate

$$
\epsilon \approx \frac{hf}{2k_BT}
$$

to estimate the population polarization.

**Method.**

1. Use constants

$$
h=6.626\times 10^{-34}\ \mathrm{J\,s},
\qquad
k_B=1.381\times 10^{-23}\ \mathrm{J/K}.
$$

2. Convert frequency:

$$
f=500\ \mathrm{MHz}=5.00\times 10^8\ \mathrm{s}^{-1}.
$$

3. Compute the numerator:

$$
hf=(6.626\times 10^{-34})(5.00\times 10^8)
=3.313\times 10^{-25}\ \mathrm{J}.
$$

4. Compute the denominator:

$$
2k_BT=2(1.381\times 10^{-23})(300)
=8.286\times 10^{-21}\ \mathrm{J}.
$$

5. Divide:

$$
\epsilon \approx \frac{3.313\times 10^{-25}}{8.286\times 10^{-21}}
\approx 4.0\times 10^{-5}.
$$

**Answer.** The polarization is about $4\times 10^{-5}$. This explains the NMR ensemble issue: the density operator is extremely close to maximally mixed, so many molecules are needed to obtain a macroscopic signal, and effective-pure-state signal shrinks as the number of qubits grows.

## Code

The following Python snippet computes the two N&C-style screening quantities used above: coherent operation budget and NMR thermal polarization.

```python
from dataclasses import dataclass

H = 6.62607015e-34
KB = 1.380649e-23

@dataclass
class Platform:
    name: str
    coherence_s: float
    gate_s: float

def operation_budget(platform):
    return platform.coherence_s / platform.gate_s

def nmr_polarization(frequency_hz, temperature_k):
    return H * frequency_hz / (2 * KB * temperature_k)

platforms = [
    Platform("ion-like memory", coherence_s=1.0, gate_s=100e-6),
    Platform("fast solid-state gate", coherence_s=100e-6, gate_s=200e-9),
    Platform("photonic feed-forward step", coherence_s=1e-3, gate_s=10e-9),
]

for platform in platforms:
    print(f"{platform.name:24s} n_op={operation_budget(platform):.1f}")

epsilon = nmr_polarization(frequency_hz=500e6, temperature_k=300)
print(f"NMR polarization at 500 MHz and 300 K: {epsilon:.2e}")
```

## Common pitfalls

- Comparing platforms by physical qubit count alone. Coherence, gate quality, measurement, reset, connectivity, and crosstalk determine computational value.
- Treating $T_1$ or $T_2$ as a complete error model. Gate errors can be dominated by control imperfections, leakage, and correlated noise.
- Forgetting initialization. N&C emphasize that a device must prepare a fiducial input state, not merely preserve arbitrary states for a while.
- Ignoring measurement. Fault-tolerant machines need repeated, selective, high-fidelity syndrome measurements, not just final readout.
- Assuming photons are always easy because they travel well. Photonic qubits are excellent carriers, but deterministic two-qubit gates and loss management are difficult.
- Treating NMR demonstrations as scalable fault-tolerant blueprints. They were important control demonstrations, but ensemble signal scaling is the bottleneck.
- Reading N&C's platform list as current market ranking. The book's criteria remain central, but the leading experimental platforms have evolved since the original edition.
- Treating topological protection as already solved hardware engineering. Protected encodings and protected gates are distinct experimental challenges.

## Connections

- [Quantum algorithms](/quantum-information-science/quantum-computing/algorithms) translates hardware constraints into depth, gate set, connectivity, and oracle cost.
- [Quantum error correction](/quantum-information-science/quantum-computing/error-correction) explains why physical noise channels, stabilizer measurement, and fresh ancillas dominate scaling.
- [Quantum machine learning](/quantum-information-science/quantum-computing/quantum-ml) is strongly constrained by NISQ noise, shot budgets, and trainability.
- [Quantum communication](/quantum-information-science/quantum-communication/) is especially close to photonic hardware and quantum memories.
- [Quantum internet](/quantum-information-science/quantum-internet/) connects stationary qubits, flying photons, entanglement distribution, and repeaters.
- [Linear algebra](/math/linear-algebra/) supplies the unitary, spectral, and tensor-product language used to model gates.
- [Quantum mechanics](/physics/quantum-mechanics/) supplies Hamiltonians, measurement theory, perturbation ideas, spin, and oscillator physics.

## Further reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, Chapter 7.
- David DiVincenzo, articles on criteria for physical implementation of quantum computation.
- Rainer Blatt and David Wineland, reviews on trapped-ion quantum information.
- H. Jeff Kimble and collaborators, cavity-QED and quantum-network experiments.
- Emanuel Knill, Raymond Laflamme, and Gerald Milburn, linear-optics quantum computation.
- Michel Devoret, Robert Schoelkopf, and collaborators, reviews on superconducting circuits and circuit QED.

## References

[1] C. Zhang, F. Xu, S. Zhang, M. Duan, et al. *Universal logical operations in a silicon quantum processor*. Nature Nanotechnology (2026).
