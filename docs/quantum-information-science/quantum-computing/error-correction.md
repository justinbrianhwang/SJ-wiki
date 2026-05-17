---
title: Quantum Error Correction
sidebar_position: 4
---

# Quantum Error Correction

Quantum error correction is the mechanism that makes large quantum computations plausible despite fragile physical qubits. It encodes a small logical Hilbert space into a larger physical Hilbert space, repeatedly extracts error syndromes without measuring the protected quantum data, and uses classical decoding to choose a correction or Pauli-frame update. It is the bridge between noisy [hardware](/quantum-information-science/quantum-computing/hardware) and deep [algorithms](/quantum-information-science/quantum-computing/algorithms) such as Shor's algorithm.

*This page synthesizes the wiki's earlier QEC draft with Chapters 8 and 10 of Nielsen and Chuang. The N&C treatment is canonical for the operator-sum model of noise, the Knill-Laflamme error-correction conditions, Pauli error discretization, stabilizer codes, normalizers, encoded operations, and the threshold theorem.*

## Definitions

A **quantum operation** or **channel** maps density operators to density operators. In N&C notation, a trace-preserving channel has an operator-sum representation

$$
\mathcal{E}(\rho)=\sum_k E_k\rho E_k^\dagger,
\qquad
\sum_k E_k^\dagger E_k=I.
$$

The operators $E_k$ are operation elements, often called Kraus operators. This language is essential because realistic noise is not a unitary on the data alone; it is a unitary interaction with an environment followed by discarding unobserved degrees of freedom.

The **Choi-Jamiolkowski representation** is another channel representation. With the unnormalized maximally entangled vector

$$
|\Omega\rangle=\sum_i |i\rangle|i\rangle,
$$

the Choi operator of $\mathcal{E}$ is

$$
J(\mathcal{E})=(I\otimes\mathcal{E})(|\Omega\rangle\langle\Omega|).
$$

Complete positivity is equivalent to $J(\mathcal{E})\ge 0$, and trace preservation is equivalent to $\mathrm{Tr}_{\mathrm{out}}J(\mathcal{E})=I$ under this unnormalized convention. N&C discuss closely related process-tomography and $\chi$-matrix representations in Chapter 8; modern QEC and benchmarking literature often uses the Choi form.

A **quantum error-correcting code** embeds $k$ logical qubits into $n$ physical qubits. It is commonly denoted $[[n,k,d]]$, where $d$ is the distance. A distance-$d$ code detects arbitrary errors on up to $d-1$ qubits and corrects arbitrary errors on up to

$$
t=\left\lfloor\frac{d-1}{2}\right\rfloor
$$

qubits, under the usual located-independent-error interpretation.

The **code projector** $P$ projects onto the codespace $\mathcal{C}$. The **Knill-Laflamme conditions** say that a code corrects a set of error operators $\{E_a\}$ if and only if

$$
P E_a^\dagger E_b P = c_{ab}P
$$

for all $a,b$, where $c_{ab}$ is a Hermitian matrix. Intuitively, errors must either move the codespace into distinguishable syndrome subspaces or act identically on all encoded states.

The **Pauli group** $G_n$ on $n$ qubits consists of tensor products of $I,X,Y,Z$ with phases $\pm 1,\pm i$. Pauli operators are central because arbitrary one-qubit errors can be expanded in the Pauli basis. Correcting $I,X,Y,Z$ on a qubit corrects any linear combination of them, which is N&C's discretization of quantum errors.

A **stabilizer code** is specified by an abelian subgroup $S\subset G_n$ that does not contain $-I$. The codespace is

$$
\mathcal{C}(S)=\{|\psi\rangle:g|\psi\rangle=|\psi\rangle\text{ for all }g\in S\}.
$$

If $S$ has $r$ independent generators, then the codespace dimension is $2^{n-r}$ and the code encodes

$$
k=n-r
$$

logical qubits.

The **normalizer** $N(S)$ is the set of Pauli operators that map $S$ to itself by conjugation. For the Pauli stabilizers used here, this equals the centralizer: the Pauli operators commuting with every element of $S$. Operators in $S$ act trivially on the codespace; elements of $N(S)\setminus S$ act as logical Pauli operators. A **syndrome** is the list of $\pm 1$ outcomes obtained by measuring stabilizer generators.

## Key results

The first lesson of N&C's QEC chapter is that the apparent obstacles are real but surmountable. Quantum states cannot be cloned, errors are continuous, and measurement can destroy superpositions. The solution is not to copy the state or learn the amplitudes; it is to measure only operators whose eigenvalues reveal the error class while preserving the encoded logical subspace.

The 3-qubit bit-flip code protects against one $X$ error:

$$
|0_L\rangle=|000\rangle,
\qquad
|1_L\rangle=|111\rangle.
$$

Its stabilizer generators are $Z_1Z_2$ and $Z_2Z_3$. Measuring them compares parities without distinguishing $\alpha\vert 000\rangle+\beta\vert 111\rangle$ inside the codespace.

The 3-qubit phase-flip code is the same idea in the Hadamard basis:

$$
|0_L\rangle=|+++\rangle,
\qquad
|1_L\rangle=|---\rangle.
$$

Its stabilizer generators are $X_1X_2$ and $X_2X_3$, so it corrects one $Z$ error.

The Shor 9-qubit code combines phase-flip and bit-flip protection:

$$
|0_L\rangle=
\frac{(|000\rangle+|111\rangle)(|000\rangle+|111\rangle)(|000\rangle+|111\rangle)}
{2\sqrt{2}},
$$

$$
|1_L\rangle=
\frac{(|000\rangle-|111\rangle)(|000\rangle-|111\rangle)(|000\rangle-|111\rangle)}
{2\sqrt{2}}.
$$

It corrects an arbitrary single-qubit error because any one-qubit operation element can be expanded as

$$
E=aI+bX+cY+dZ.
$$

The syndrome measurement collapses the error component into a discrete Pauli error class, and the recovery inverts that class. This is the key digital feature of quantum error correction.

The stabilizer formalism makes larger codes manageable. If $S=\langle g_1,\dots,g_{n-k}\rangle$, error detection measures the generators. If an error $E$ anticommutes with a generator $g_j$, the corresponding syndrome bit flips sign. If $E\in S$, it does not harm the logical information. If $E\in N(S)\setminus S$, it is a logical Pauli error and cannot be detected by the stabilizers. Therefore the distance of a stabilizer code is the minimum weight of an operator in $N(S)\setminus S$.

N&C's stabilizer error-correction condition can be stated compactly: a Pauli error set $\{E_j\}$ is correctable if for every pair $j,k$, either $E_j^\dagger E_k\in S$ or $E_j^\dagger E_k\notin N(S)$. If the product is in $S$, the two errors act the same on the code. If the product is outside the normalizer, some stabilizer generator distinguishes them. The dangerous case is $E_j^\dagger E_k\in N(S)\setminus S$, because then the difference between the errors is a nontrivial logical operator.

CSS codes build quantum codes from classical linear codes so that $X$-type and $Z$-type checks are separated. The Steane code is the standard $[[7,1,3]]$ example built from the classical Hamming code; it has three $X$-type and three $Z$-type stabilizer generators and corrects an arbitrary one-qubit error. The five-qubit code is the smallest code that encodes one logical qubit and corrects any one-qubit error, while the Shor code is larger but more transparent.

Encoded operations are Pauli operators in the normalizer modulo stabilizers. For example, in a stabilizer code a logical $\overline{X}$ and $\overline{Z}$ must commute with every stabilizer generator, be independent of $S$, and anticommute with each other. Multiplying a logical operator by a stabilizer gives an equivalent logical operator on the codespace, which is why the same logical Pauli can have many physical representatives with different weights.

Fault tolerance adds a propagation constraint. A recovery circuit is not enough if a single component fault can spread into several data errors in one code block. Transversal gates, verified ancillas, repeated syndrome measurement, magic-state injection, lattice surgery, and code switching are techniques for keeping the effective logical failure probability low. N&C present the threshold theorem in this spirit: under physically reasonable locality and independence assumptions, if the physical error rate is below a threshold, arbitrarily long computations can be made reliable with overhead that grows moderately with computation size.

Surface codes are a modern stabilizer-family continuation of this story. Local star and plaquette checks on a two-dimensional lattice make them attractive for hardware with local connectivity. They are not the main code family developed in N&C, but they use the same stabilizer and syndrome logic.

## Modern QEC milestones

Modern experiments and proposals test different parts of the fault-tolerant stack. A surface-code memory tests distance scaling; bosonic codes test whether one oscillator can absorb part of the redundancy; learned decoders test the latency bottleneck; and logical-gate diagnostics test whether syndrome measurements are reliable enough to drive operations, not only memory.

### Surface code memory below threshold

Google Quantum AI and collaborators [1] showed a superconducting surface-code memory whose fitted logical error per cycle decreased as the code distance increased. The contribution was a full system benchmark: ZXXZ-style rotated surface-code patches on Willow hardware, leakage removal, repeated syndrome extraction, high-accuracy offline decoding, and a separate distance-5 real-time decoding demonstration.

For a rotated distance-$d$ surface-code memory, the usual physical footprint before extra leakage-removal qubits is

$$
N_{\mathrm{surface}}=2d^2-1,
\qquad
N_{\mathrm{data}}=d^2,
\qquad
N_{\mathrm{measure}}=d^2-1.
$$

Below threshold, the idealized scaling is often summarized as

$$
\epsilon_L(d)\approx A\left(\frac{p}{p_{\mathrm{thr}}}\right)^{(d+1)/2},
$$

where $\epsilon_L(d)$ is the logical error per cycle, $p$ is a physical error proxy, and $p_{\mathrm{thr}}$ is the threshold. A practical distance-step figure of merit is

$$
\Lambda_{d,d+2}=\frac{\epsilon_L(d)}{\epsilon_L(d+2)}.
$$

The below-threshold signature is $\Lambda_{d,d+2}\gt 1$: adding physical qubits makes the logical memory better. In the Willow distance-7 run, the code used $49$ data qubits, $48$ measurement qubits, and $4$ leakage-removal qubits, so the count checks as

$$
2(7^2)-1+4=101.
$$

This is a memory milestone rather than a complete logical processor. It demonstrates distance scaling and break-even lifetime under the reported conditions, while logical gates, routing, magic-state production, and large-scale scheduling remain separate requirements.

### Concatenated bosonic codes

Putterman, Noh, Hann, and collaborators [2] demonstrated a bosonic route to hardware-efficient memory: suppress one Pauli error type inside a stabilized cat oscillator, then correct the dominant residual error with a small repetition code. The contribution is the concatenation itself in hardware: five cat data modes, four transmon syndrome ancillas, bias-preserving controlled operations, erasure-aware decoding, and an in-device distance-3 versus distance-5 comparison.

The cat-qubit basis is approximately

$$
|0\rangle_c\approx|\alpha\rangle,
\qquad
|1\rangle_c\approx|-\alpha\rangle.
$$

Increasing $\vert \alpha\vert ^2$ separates the coherent states and suppresses bit flips, but it also increases exposure to photon-loss-induced phase flips. A simplified biased-noise summary is

$$
\Gamma_X\propto e^{-c|\alpha|^2},
\qquad
\Gamma_Z\propto |\alpha|^2\kappa_1,
\qquad
\frac{\Gamma_Z}{\Gamma_X}\gg 1.
$$

The outer repetition code measures neighboring checks

$$
S_i=X_iX_{i+1},
\qquad i=1,\ldots,d-1,
$$

which detect phase flips in the cat basis. One distance-5 cycle has four checks, and each check touches two neighboring cat qubits, so it uses

$$
2(d-1)=2(5-1)=8
$$

cat-ancilla controlled interactions before measurement and reset. A compact syndrome-cycle sketch is:

```text
repeat each QEC cycle:
    stabilize each oscillator toward the cat manifold
    for each neighbor pair (i, i+1):
        entangle ancilla with X_i X_{i+1}
        measure ancilla, keeping erasure information
    compare consecutive syndromes to form detection events
    decode likely phase-flip history with matching
```

The main lesson is not that repetition codes are new; it is that strong physical noise bias changes what the outer code must do. The architecture improves hardware efficiency only while uncorrected cat bit flips remain rare enough that they do not set the logical-error floor.

### Beyond break-even with bosonic qudit codes

Brock, Singh, Eickbusch, Sivak, Ding, Frunzio, Girvin, and Devoret [3] extended bosonic error correction beyond qubits by demonstrating finite-energy GKP qutrit and ququart memories beyond break-even. The contribution is a high-dimensional logical memory in one superconducting cavity, stabilized through optimized small-big-small control rounds using a transmon ancilla.

With displacement

$$
D(\alpha)=\exp(\alpha a^\dagger-\alpha^*a),
$$

a square GKP qudit of dimension $d$ can be described by stabilizer displacements

$$
S_X=D(\ell_d),
\qquad
S_Z=D(i\ell_d),
\qquad
\ell_d=\sqrt{\pi d},
$$

and generalized logical Paulis

$$
X_d=D\left(\sqrt{\frac{\pi}{d}}\right),
\qquad
Z_d=D\left(i\sqrt{\frac{\pi}{d}}\right).
$$

They obey

$$
Z_dX_d=\omega_dX_dZ_d,
\qquad
\omega_d=e^{2\pi i/d}.
$$

For $d=3$, the phase is $\omega_3=-1/2+i\sqrt{3}/2$, so qutrit Paulis do not simply anticommute with a sign. The break-even metric compares effective memory lifetimes or decay rates:

$$
G_d=\frac{\gamma_{\mathrm{physical}}}{\gamma_{\mathrm{logical}}}
=\frac{T_{\mathrm{logical}}}{T_{\mathrm{physical}}}.
$$

For example, a qutrit logical lifetime of $886\,\mu\mathrm{s}$ with $G_3=1.82$ corresponds to a physical comparator lifetime of

$$
T_{\mathrm{physical}}\approx \frac{886}{1.82}\,\mu\mathrm{s}\approx 487\,\mu\mathrm{s}.
$$

The result shows that qudit memories can be error-corrected beyond a matched physical baseline. It does not yet supply a universal high-dimensional fault-tolerant processor, because scalable entangling logical gates and concatenation remain separate problems.

### Learned decoders for real-time error correction

Zhang [4] proposed using a trained quantum circuit as the decoder for a noisy protected quantum circuit. The contribution is conceptual and numerical rather than experimental: decoding is framed as a syndrome-conditioned quantum sampling task, with simulations on surface-code memories up to distance 7 showing performance comparable to minimum-weight perfect matching under the tested circuit-level noise model.

Let the measured syndrome be

$$
s=(s_1,\ldots,s_m)\in\{0,1\}^m,
$$

and let a code with $k$ logical qubits have a logical sector label

$$
\ell\in\{0,1\}^{2k}.
$$

Classical maximum-likelihood decoding estimates

$$
\ell^*(s)=\arg\max_\ell P(\ell\mid s).
$$

The learned quantum decoder instead implements a parameterized circuit $B_\theta(s)$ whose gates depend on syndrome bits and whose measurement samples

$$
q_\theta(\ell\mid s)\approx P(\ell\mid s).
$$

Training can use the same cross-entropy objective as a neural decoder:

$$
\mathcal{L}(\theta)
=-\frac{1}{N}\sum_{j=1}^N\log q_\theta(\ell^{(j)}\mid s^{(j)}).
$$

A deployment sketch is:

```text
offline:
    generate labeled pairs (syndrome, logical sector)
    train B_theta to maximize probability of the labeled sector

online:
    stream syndrome bits from the protected circuit
    run B_theta(s) on decoder qubits
    sample candidate logical sectors
    update the Pauli frame using the most likely sector
```

The open engineering question is whether a decoder circuit remains useful once its own noise, calibration, routing, and training cost are included. Its value in this chapter is to make the decoder latency problem explicit: QEC is only real-time if the syndrome-to-frame-update path keeps up with the hardware cycle.

### Failure modes of fault-tolerant gates

Harper, Laine, Hockings, McLauchlan, Nixon, Brown, and Bartlett [5] separated two failure mechanisms that are easy to conflate: logical-memory decay and measurement-driven logical-gate failure. The contribution is a diagnostic framework on a heavy-hex subsystem-code patch, showing that faster syndrome extraction and reset removal can improve memory while repeated-measurement stability tests reveal the measurement faults that would limit lattice-surgery-style gates.

A memory experiment fits the logical success probability over syndrome rounds as

$$
P_{\mathrm{success}}(t)=A p^t+\frac{1}{2},
$$

with a per-round logical fidelity convention

$$
F_{\mathrm{round}}=\frac{1+p}{2}.
$$

Thus a fitted $p=0.92$ means

$$
F_{\mathrm{round}}=\frac{1+0.92}{2}=0.96.
$$

But a logical gate driven by repeated stabilizer measurements can fail even when the memory survives, because time-like strings of measurement errors can flip the inferred logical measurement. A stability experiment probes that class of failure by checking whether repeated stabilizer products remain self-consistent. The same hardware can therefore have two different optimization targets:

| Diagnostic | Main error direction | Design lever |
|---|---|---|
| Memory experiment | Space-like data-error chains | Better gates, less idle time, better placement |
| Stability experiment | Time-like measurement-error chains | Better mid-circuit measurement and enough repetitions |
| Lattice surgery | Both together | Balance code distance $d$ and measurement rounds $t$ |

The practical lesson is that "a good logical memory" is not the same statement as "a good fault-tolerant logical gate." Mid-circuit measurement time, assignment error, reset noise, and decoder timing enter the gate budget directly.

## Visual

```mermaid
flowchart TB
  subgraph BitFlip["3-qubit bit-flip code"]
    direction LR
    BFIn["input qubit<br/>|psi> = alpha|0> + beta|1>"] --> BFC1["CNOT<br/>q0 -> q1"]
    BFC1 --> BFC2["CNOT<br/>q0 -> q2"]
    BFC2 --> BFEnc["encoded block<br/>alpha|000> + beta|111>"]
    BFEnc --> BFNoise["single-X error channel<br/>I, X1, X2, or X3"]
    BFNoise --> BFS1["measure stabilizer<br/>Z1 Z2 -> syndrome bit s12"]
    BFNoise --> BFS2["measure stabilizer<br/>Z2 Z3 -> syndrome bit s23"]
    BFS1 --> BFSyn["syndrome pair<br/>#lsqb;s12, s23"]"]
    BFS2 --> BFSyn
    BFSyn --> BFDec{"decoder table<br/>which bit flipped?"}
    BFDec -->|"["+,+"]"| BFI["do nothing"]
    BFDec -->|"["-,+"]"| BFX1["apply X1"]
    BFDec -->|"["-,-"]"| BFX2["apply X2"]
    BFDec -->|"["+,-"]"| BFX3["apply X3"]
    BFI --> BFOut["logical state restored<br/>up to correctable error"]
    BFX1 --> BFOut
    BFX2 --> BFOut
    BFX3 --> BFOut
  end

  subgraph Shor9["9-qubit Shor code"]
    direction LR
    SHIn["input qubit<br/>alpha|0> + beta|1>"] --> SHPhase["phase-flip repetition<br/>alpha|+++> + beta|--->"]
    SHPhase --> SHBit["bit-flip repetition inside each block<br/>3 blocks x 3 qubits"]
    SHBit --> SHCode["codewords<br/>alpha(|000>+|111>)^3 + beta(|000>-|111>)^3"]
    SHCode --> SHZ["within-block Z checks<br/>Z1Z2, Z2Z3, Z4Z5, Z5Z6, Z7Z8, Z8Z9"]
    SHCode --> SHX["between-block X checks<br/>X1...X6 and X4...X9"]
    SHZ --> SHSyn["bit-flip and phase-flip syndromes"]
    SHX --> SHSyn
    SHSyn --> SHRec["recovery<br/>correct one arbitrary single-qubit Pauli error"]
  end

  subgraph Steane7["7-qubit Steane CSS code"]
    direction LR
    STIn["logical input<br/>|psi_L>"] --> STEnc["Hamming-code CSS encoder<br/>#lsqb;#lsqb;7,1,3"]]"]
    STEnc --> STData["7 data qubits<br/>distance 3, one logical qubit"]
    STData --> STX["X stabilizers<br/>X1X3X5X7, X2X3X6X7, X4X5X6X7"]
    STData --> STZ["Z stabilizers<br/>Z1Z3Z5Z7, Z2Z3Z6Z7, Z4Z5Z6Z7"]
    STX --> STSyn["6 syndrome bits<br/>3 X-type + 3 Z-type"]
    STZ --> STSyn
    STSyn --> STCSS["CSS decoder<br/>separate bit-flip and phase-flip decoding"]
    STCSS --> STOut["logical qubit preserved<br/>corrects any weight-1 Pauli"]
  end

  subgraph Surface["Surface-code patch and repeated rounds"]
    direction TB
    SD11(("data d11")) --- SX12["X-check ancilla"]
    SX12 --- SD13(("data d13"))
    SD11 --- SZ21["Z-check ancilla"]
    SZ21 --- SD31(("data d31"))
    SD13 --- SZ23["Z-check ancilla"]
    SZ23 --- SD33(("data d33"))
    SD31 --- SX32["X-check ancilla"]
    SX32 --- SD33
    SX12 --> SCRound["one stabilizer round<br/>prepare ancillas, CNOT schedule, measure, reset"]
    SZ21 --> SCRound
    SZ23 --> SCRound
    SX32 --> SCRound
    SCRound --> SCBits["syndrome differences<br/>space-time detection events"]
    SCBits --> SCDec["classical decoder<br/>matching, union-find, or neural decoder"]
    SCDec --> SCFrame["Pauli-frame update<br/>no immediate physical correction required"]
    SCFrame -. "repeat for d or more rounds" .-> SCRound
  end

  Noise["physical noise model<br/>Kraus, Pauli, leakage, measurement error"] --> BFNoise
  Noise --> SCRound
  BFOut --> Goal["fault-tolerant goal<br/>logical information survives below threshold"]
  SHRec --> Goal
  STOut --> Goal
  SCFrame --> Goal
```

![Google surface-code memory result — the figure shows the Willow surface-code experiment and logical error behavior across code distances.](https://ar5iv.labs.arxiv.org/html/2408.13687/assets/x1.png)

*Figure: Google Quantum AI's Willow experiment reports below-threshold surface-code memory scaling across increasing code distance. From [Google Quantum AI and Collaborators, 2024](https://arxiv.org/abs/2408.13687) — embedded under educational fair use with attribution.*

The diagram shows QEC at four scales: a full 3-qubit bit-flip encoding/syndrome/correction circuit, the nested structure of Shor's 9-qubit code, the CSS stabilizer split of the Steane code, and a surface-code patch with repeated ancilla rounds. The labeled syndrome paths make clear that the measurement reveals error information, not the encoded amplitudes. The dotted surface-code feedback arrow shows the ongoing decoder and Pauli-frame loop used in fault-tolerant operation.

| Object | N&C notation | Role in QEC | Common mistake |
|---|---|---|---|
| Density operator | $\rho$ | Represents pure, mixed, and encoded states | Treating all states as state vectors |
| Quantum operation | $\mathcal{E}(\rho)=\sum_k E_k\rho E_k^\dagger$ | Models noise and recovery | Assuming every process is unitary on data |
| Code projector | $P$ | Defines the protected subspace | Forgetting to restrict equations to the codespace |
| Stabilizer | $S$ | Operators with eigenvalue $+1$ on code states | Measuring logical information instead of syndrome |
| Normalizer | $N(S)$ | Pauli operators preserving the codespace | Confusing stabilizers with logical Paulis |
| Syndrome | $\pm 1$ outcomes | Identifies an error class | Assuming syndrome reveals amplitudes |

## Worked example 1: Syndrome table for the 3-qubit bit-flip code

**Problem.** For the code $\vert 0_L\rangle=\vert 000\rangle$, $\vert 1_L\rangle=\vert 111\rangle$, compute the syndrome for no error and for $X_1$, $X_2$, and $X_3$ using stabilizers $g_1=Z_1Z_2$ and $g_2=Z_2Z_3$.

**Method.**

1. No error. Both $\vert 000\rangle$ and $\vert 111\rangle$ have equal $Z$ parity on adjacent pairs:

$$
g_1=+1,
\qquad
g_2=+1.
$$

2. Error $X_1$ flips the first bit. The basis states become $\vert 100\rangle$ and $\vert 011\rangle$. Qubits 1 and 2 now differ, while qubits 2 and 3 match:

$$
g_1=-1,
\qquad
g_2=+1.
$$

3. Error $X_2$ flips the middle bit. Both adjacent parities change:

$$
g_1=-1,
\qquad
g_2=-1.
$$

4. Error $X_3$ flips the last bit. Qubits 1 and 2 match, while qubits 2 and 3 differ:

$$
g_1=+1,
\qquad
g_2=-1.
$$

**Answer.**

| Error | $Z_1Z_2$ | $Z_2Z_3$ | Recovery |
|---|---:|---:|---|
| $I$ | $+1$ | $+1$ | Do nothing |
| $X_1$ | $-1$ | $+1$ | Apply $X_1$ |
| $X_2$ | $-1$ | $-1$ | Apply $X_2$ |
| $X_3$ | $+1$ | $-1$ | Apply $X_3$ |

Each allowed single-bit-flip error has a unique syndrome, and the syndrome measurement does not distinguish $\alpha\vert 000\rangle+\beta\vert 111\rangle$ from another state in the same logical qubit.

## Worked example 2: Checking Knill-Laflamme for the bit-flip error set

**Problem.** Let $P=\vert 000\rangle\langle000\vert +\vert 111\rangle\langle111\vert $ be the projector for the 3-qubit bit-flip code. Verify the Knill-Laflamme condition for the restricted error set $\{I,X_1,X_2,X_3\}$.

**Method.**

1. Start with identical errors. For $E_a=E_b=X_i$,

$$
P X_i^\dagger X_i P = P I P=P.
$$

The same is true for $E_a=E_b=I$.

2. Compare $I$ with a single flip. For example,

$$
X_1|000\rangle=|100\rangle,
\qquad
X_1|111\rangle=|011\rangle.
$$

Both $\vert 100\rangle$ and $\vert 011\rangle$ are orthogonal to the codespace, so

$$
P X_1 P=0.
$$

The same argument gives $P X_i P=0$ for $i=1,2,3$.

3. Compare two distinct flips. For example,

$$
X_1X_2|000\rangle=|110\rangle,
\qquad
X_1X_2|111\rangle=|001\rangle.
$$

Again these states are orthogonal to $\vert 000\rangle$ and $\vert 111\rangle$, so

$$
P X_1^\dagger X_2 P=P X_1X_2 P=0.
$$

The same holds for any $i\ne j$.

4. Assemble the matrix $c_{ab}$. The diagonal entries are $1$ and the off-diagonal entries are $0$, so

$$
P E_a^\dagger E_b P=\delta_{ab}P
$$

for $E_a,E_b\in\{I,X_1,X_2,X_3\}$.

**Answer.** The restricted bit-flip code satisfies the Knill-Laflamme conditions for no error and one $X$ error. The check also explains what the code does not do: $Z_1$ commutes with the $Z$-parity stabilizers and acts as a logical phase error, so this 3-qubit code is not a full arbitrary-error code.

## Code

This small script computes stabilizer syndromes for Pauli-string errors. It mirrors N&C's stabilizer rule: a syndrome bit is $-1$ exactly when the error anticommutes with the measured generator.

```python
ANTI = {
    ("X", "Z"), ("Z", "X"),
    ("X", "Y"), ("Y", "X"),
    ("Y", "Z"), ("Z", "Y"),
}

def anticommutes(pauli_a, pauli_b):
    count = 0
    for a, b in zip(pauli_a, pauli_b):
        if a == "I" or b == "I" or a == b:
            continue
        if (a, b) in ANTI:
            count += 1
    return count % 2 == 1

def syndrome(error, generators):
    return tuple(-1 if anticommutes(error, g) else 1 for g in generators)

generators = ["ZZI", "IZZ"]
errors = {
    "I": "III",
    "X1": "XII",
    "X2": "IXI",
    "X3": "IIX",
    "Z1": "ZII",
}

for name, pauli in errors.items():
    print(f"{name:2s} {pauli} syndrome={syndrome(pauli, generators)}")
```

## Common pitfalls

- Measuring the data instead of the syndrome. Stabilizer checks must reveal error information without revealing the logical amplitudes.
- Assuming the 3-qubit repetition code corrects arbitrary quantum errors. It corrects one Pauli type unless combined with phase protection.
- Forgetting the density-operator viewpoint. QEC corrects channels and operation elements, not just state-vector mistakes.
- Confusing stabilizers with logical operators. Stabilizers act as identity on the codespace; normalizer elements outside the stabilizer are logical Paulis.
- Treating every distinct physical error as needing a distinct syndrome. Degenerate codes allow different errors to act identically on the codespace.
- Ignoring measurement errors. Surface-code and fault-tolerant protocols require repeated syndrome rounds because the syndrome record is noisy.
- Applying a correction physically when a Pauli-frame update would suffice. Tracking corrections classically often avoids extra gates.
- Treating the threshold theorem as a practical qubit-count estimate. It is an asymptotic statement whose constants depend on architecture and noise.
- Ignoring leakage and correlated noise. Pauli error models are analytically powerful, but hardware can leave the computational subspace or produce correlated faults.
- Assuming transversal gates are universal for one fixed stabilizer code. Non-Clifford operations require additional machinery such as magic states or code switching.

## Connections

- [Quantum hardware](/quantum-information-science/quantum-computing/hardware) determines the physical noise channel, measurement cycle, reset method, and geometry.
- [Quantum algorithms](/quantum-information-science/quantum-computing/algorithms) determines the logical gate counts and target failure probabilities that QEC must support.
- [Quantum machine learning](/quantum-information-science/quantum-computing/quantum-ml) mostly studies NISQ circuits today, but fault-tolerant QML would need these tools.
- [Quantum communication](/quantum-information-science/quantum-communication/) shares ideas with entanglement purification, quantum repeaters, and channel correction.
- [Quantum internet](/quantum-information-science/quantum-internet/) uses error correction and purification to protect distributed entanglement.
- [Linear algebra](/math/linear-algebra/) supplies projectors, eigenspaces, tensor products, matrix algebras, and operator decompositions.
- [Quantum mechanics](/physics/quantum-mechanics/) supplies measurement, spin operators, open systems, and the density-operator formalism.

## Further reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, Chapters 8 and 10.
- Peter Shor, scheme for reducing decoherence in quantum computer memory.
- Andrew Steane, multiple-particle interference and quantum error correction.
- Daniel Gottesman, stabilizer codes and fault-tolerant quantum computation.
- A. Robert Calderbank and Peter Shor; Andrew Steane, CSS code constructions.
- Alexei Kitaev, toric code and fault-tolerant quantum computation by anyons.
- John Preskill, lecture notes on fault-tolerant quantum computation.

## References

[1] Google Quantum AI and Collaborators. *Quantum error correction below the surface code threshold*. Nature 638, 920-926 (2025).
[2] H. Putterman, K. Noh, C. T. Hann, et al. *Hardware-efficient quantum error correction via concatenated bosonic qubits*. Nature 638, 927-934 (2025).
[3] B. L. Brock, S. Singh, A. Eickbusch, V. V. Sivak, A. Z. Ding, L. Frunzio, S. M. Girvin, M. H. Devoret. *Quantum error correction of qudits beyond break-even*. Nature 641, 612-617 (2025).
[4] P. Zhang. *Correcting a noisy quantum computer using a quantum computer*. arXiv:2506.08331 (2025).
[5] R. Harper, C. Laine, E. T. Hockings, C. McLauchlan, G. M. Nixon, B. J. Brown, S. D. Bartlett. *Characterising the failure mechanisms of error-corrected quantum logic gates*. Nature Communications (2026).
