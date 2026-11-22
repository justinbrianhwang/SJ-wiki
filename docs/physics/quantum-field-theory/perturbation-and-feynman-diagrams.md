---
title: Perturbation Theory and Feynman Diagrams
sidebar_position: 4
---

# Perturbation Theory and Feynman Diagrams

Feynman diagrams are not cartoons added after a calculation. They are a compact notation for the terms generated when an interacting path integral or time-ordered operator expression is expanded in powers of a coupling. Lines represent propagators, vertices represent local interactions, and the graph tells you what momentum integrals and symmetry factors to write.

The physical value of the diagrammatic language is that it separates universal structure from algebra. Once the propagators and vertices are known, scattering amplitudes can be organized by the number of vertices or loops. Zee's early discussion of diagrams is meant to make this organization feel natural: forces arise because fields propagate between interaction events, and perturbation theory enumerates those events.

## Reading the ingredients of a diagram

For a theory split into free and interacting parts,

$$
\mathcal{L}=\mathcal{L}_0+\mathcal{L}_{\text{int}},
$$

the perturbative expansion is an expansion in powers of the coupling constants appearing in $\mathcal{L}_{\text{int}}$. For scalar $\phi^4$ theory,

$$
\mathcal{L}_{\text{int}}=-\frac{\lambda}{4!}\phi^4.
$$

The **propagator** is the two-point function of the free theory:

$$
\tilde{\Delta}_F(p)=\frac{i}{p^2-m^2+i\epsilon}.
$$

The **vertex factor** for $-\lambda\phi^4/4!$ is

$$
-i\lambda.
$$

An **external line** corresponds to an incoming or outgoing particle. An **internal line** is integrated over momentum. A **loop** is an independent internal momentum integral:

$$
\int \frac{d^4\ell}{(2\pi)^4}.
$$

A connected diagram contributes to a connected scattering amplitude. Vacuum bubbles cancel in normalized correlators or are absorbed into vacuum energy.

## From Feynman rules to an amplitude

The basic algorithm for scalar perturbation theory is:

1. Draw topologically distinct diagrams with the required external legs and order in $\lambda$.
2. Assign momentum to each line.
3. Write a propagator for each internal line.
4. Write a vertex factor for each vertex.
5. Enforce momentum conservation at each vertex.
6. Integrate over independent loop momenta.
7. Divide by the graph symmetry factor when the Feynman rules do not already include it.

For $2\to2$ scattering in $\phi^4$ theory at tree level, the amplitude is simply

$$
i\mathcal{M}_{\text{tree}}=-i\lambda,
\qquad \mathcal{M}_{\text{tree}}=-\lambda.
$$

At one loop, the same process receives $s$, $t$, and $u$ channel bubble corrections:

$$
i\mathcal{M}_{1\text{-loop}}
\sim
\frac{(-i\lambda)^2}{2}
\int \frac{d^4\ell}{(2\pi)^4}
\frac{i}{\ell^2-m^2+i\epsilon}
\frac{i}{(\ell+P)^2-m^2+i\epsilon},
$$

where $P$ is the momentum through the channel. The integral diverges in four dimensions and leads directly to regularization and renormalization.

Diagrams also encode conservation laws. Translational invariance gives momentum conservation. Internal symmetries impose charge flow. Gauge symmetry produces Ward identities, which are diagrammatic constraints strong enough to cancel unphysical polarizations and relate different amplitudes.

There are several layers of diagrammatic organization. Ordinary connected diagrams contribute to connected correlation functions. Amputated connected diagrams, with external propagators removed, enter scattering amplitudes through the LSZ reduction idea. One-particle-irreducible diagrams, which cannot be disconnected by cutting a single internal line, build the effective action and self-energies. Keeping these categories separate prevents confusion when the same drawing appears in different formulas with different external factors.

Power counting gives a quick estimate before any integral is evaluated. A tree diagram has no loop integral and is usually algebraic once momentum conservation is imposed. A one-loop diagram has one independent momentum integration and is the first place ultraviolet divergences, thresholds, and imaginary parts appear. Higher-loop diagrams add a consistency test: counterterms introduced at lower order must still suffice, and the renormalization scheme must be applied coherently.

External states also matter. A correlation function with fields inserted at arbitrary spacetime points is not yet an experiment. A scattering amplitude assumes asymptotic states, wavefunction normalization, and on-shell external momenta. For stable particles this is straightforward. For confined particles, unstable resonances, or finite-temperature systems, the diagrammatic expansion still exists, but its direct interpretation as a particle scattering process needs more care.

Every diagram has two readings. As a mathematical recipe it specifies denominators, numerators, integrals, and delta functions. As a physical process it identifies the quanta and charge flow, the intermediate states that can go on shell, and the applicable conservation laws.

```mermaid
flowchart TB
  Theory["QFT model<br/>fields, symmetries, Lagrangian"] --> Split["Split action or Lagrangian<br/>free quadratic part + interactions"]

  subgraph Rules["Feynman-rule lookup"]
    direction TB
    Free["quadratic kernel"] --> Prop["propagators<br/>internal line factor, pole prescription"]
    Inter["interaction monomials<br/>couplings and field content"] --> Vert["vertices<br/>coupling factor and momentum conservation"]
    External["external states<br/>on-shell momenta, spin or polarization"] --> Legs["external legs<br/>wavefunctions or LSZ factors"]
  end

  Split --> Free
  Split --> Inter
  Theory --> External
  Prop --> Enumerate["enumerate diagrams<br/>fixed external legs and order in coupling"]
  Vert --> Enumerate
  Legs --> Enumerate

  subgraph Integral["Diagram-to-integrand assembly"]
    direction TB
    Assign["assign momentum to each line"] --> Delta["apply vertex delta functions<br/>conserve momentum"]
    Delta --> Loops["choose independent loop momenta<br/>one integral per loop"]
    Loops --> Numerator["multiply vertex, propagator, and numerator factors"]
    Numerator --> Sym["divide by symmetry factor if needed"]
  end

  Enumerate --> Assign
  Sym --> Reg{"loop integral divergent?"}
  Reg -- "no" --> Amp["amplitude or correlator"]
  Reg -- "yes" --> Regularize["regularize<br/>cutoff, dimensional, lattice, etc."]
  Regularize --> Counter["add counterterms and renormalization conditions"]
  Counter --> Amp
  Amp --> Obs["observable prediction<br/>cross section, decay rate, correlation function"]
```

The rule-lookup subgraph separates propagators, vertices, and external legs. The integrand subgraph then tracks momentum assignment, delta functions, loop integration, numerator factors, and symmetry factors. Ultraviolet-sensitive loop integrals take the regularization and counterterm branch.

ASCII sketch of common scalar diagrams:

```text
tree 2->2:

 p1 ----\
         X---- p3
 p2 ----/ \
          \--- p4

one-loop bubble:

 p1 ----\      /---- p3
         X====X
 p2 ----/      \---- p4
```

| Diagram feature | Mathematical object | Physical reading |
|---|---|---|
| External leg | asymptotic particle | prepared or detected quantum |
| Internal line | propagator | virtual propagation between events |
| Vertex | coupling and local product of fields | interaction at one spacetime point |
| Loop | unconstrained momentum integral | quantum fluctuation summed over |
| Symmetry factor | combinatorial division | avoids overcounting identical contractions |

## The tree-level contact amplitude

For $\phi(p_1)+\phi(p_2)\to\phi(p_3)+\phi(p_4)$ in real scalar $\phi^4$ theory, the interaction is

$$
\mathcal{L}_{\text{int}}=-\frac{\lambda}{4!}\phi^4.
$$

The factor $4!$ cancels the number of contractions of the four identical fields with the external particles, leaving the four-point vertex

$$
\text{vertex}=-i\lambda.
$$

There is one tree diagram, with one four-leg vertex and no internal propagator. Momentum conservation supplies

$$
(2\pi)^4\delta^{(4)}(p_1+p_2-p_3-p_4).
$$

The $S$-matrix convention writes the connected contribution as

$$
i\mathcal{M}(2\pi)^4\delta^{(4)}(\sum p_{\text{in}}-\sum p_{\text{out}})
$$

for the connected amplitude.

Therefore

$$
i\mathcal{M}_{\text{tree}}=-i\lambda,
\qquad
\mathcal{M}_{\text{tree}}=-\lambda.
$$

There is no momentum dependence at this order because the interaction is local and contains no derivatives.

## Counting internal lines and loops

A connected scalar diagram has $V=3$ quartic vertices and $E=4$ external legs. Each quartic vertex has four field ends, so the vertices supply

$$
4V=12
$$

line ends.

The external lines consume one end each:

$$
E=4.
$$

Internal lines consume two ends each. Therefore

$$
4V=E+2I.
$$

Insert $V=3$ and $E=4$:

$$
12=4+2I.
$$

Solving gives

$$
2I=8,\qquad I=4.
$$

For a connected graph, the number of independent loops is

$$
L=I-V+1.
$$

Thus

$$
L=4-3+1=2.
$$

Thus $I=4$ and $L=2$: a third-order four-point diagram in $\phi^4$ theory is a two-loop correction.

## Checking $\phi^4$ graph counts

```python
def phi4_graph_counts(vertices, external_legs):
    ends = 4 * vertices
    if external_legs > ends:
        raise ValueError("more external legs than available line ends")
    if (ends - external_legs) % 2 != 0:
        raise ValueError("line ends do not pair into internal lines")
    internal_lines = (ends - external_legs) // 2
    loops = internal_lines - vertices + 1
    return internal_lines, loops

for vertices in range(1, 5):
    internal, loops = phi4_graph_counts(vertices, external_legs=4)
    print(f"V={vertices}: I={internal}, L={loops}")
```

## What the drawings do—and do not—mean

- Reading diagrams as literal particle trajectories. Internal lines represent terms in an amplitude, not directly observed paths.
- Omitting the momentum-conserving delta function and then double-counting momentum constraints.
- Forgetting symmetry factors in diagrammatic expansions derived directly from Wick contractions.
- Confusing the amplitude $\mathcal{M}$ with $i\mathcal{M}$; conventions differ, so track factors of $i$ consistently.
- Treating loop divergences as mistakes. Divergences are signals that parameters must be defined with a regulator and physical renormalization condition.
- Mixing correlation functions with scattering amplitudes. A correlator still has external propagators and off-shell positions; an $S$-matrix element requires amputation, on-shell limits, and normalization of external states.
- Counting only the number of vertices when estimating difficulty. The number of loops controls independent momentum integrations, ultraviolet behavior, and the appearance of imaginary parts from physical thresholds.
- Forgetting that diagrams are constrained by every symmetry of the Lagrangian. Charge flow, momentum conservation, spinor structure, and gauge identities are as much a part of the diagram as its topology.
- Drawing all topologies but forgetting permutations of external assignments. For identical particles this may be hidden in symmetry factors; for distinct particles it can change the channel structure.

<div className="see-also">

See also: [Path Integral Formulation](/physics/quantum-field-theory/path-integral-formulation) · [Scalar Phi-Four Theory](/physics/quantum-field-theory/scalar-phi-four-theory) · [Renormalization and Counterterms](/physics/quantum-field-theory/renormalization-and-counterterms) · [Gauge Invariance and QED](/physics/quantum-field-theory/gauge-invariance-and-qed)

</div>
