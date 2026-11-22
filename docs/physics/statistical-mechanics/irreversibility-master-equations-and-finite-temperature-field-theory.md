---
title: Irreversibility, Master Equations, and Finite-Temperature Field Theory
sidebar_position: 21
---

# Irreversibility, Master Equations, and Finite-Temperature Field Theory

Microscopic mechanics is reversible in many basic models, but macroscopic thermodynamics is irreversible. Schwabl's final chapter examines this tension through recurrence, coarse-graining, Brownian models, master equations, phase-space volume, Gibbs and Boltzmann entropy, and the approach to equilibrium.

Finite-temperature field theory starts from the same density-matrix object, $Z=\mathrm{Tr}\,e^{-\beta H}$, rewritten as imaginary-time evolution. That connection is supplementary to Schwabl's treatment but useful for carrying the statistical-mechanical formalism into thermal field theory.

## Entropy under exact and reduced dynamics

Fine-grained Gibbs entropy for a classical density $\rho(q,p,t)$ is

$$
S_G=-k_B\int dq\,dp\,\rho\ln\rho.
$$

Under exact Liouville evolution, $S_G$ is constant. Boltzmann entropy instead assigns entropy to a macrostate $M$:

$$
S_B(M)=k_B\ln |M|,
$$

where $\vert M\vert $ is the phase-space volume compatible with the macrostate.

A continuous-time master equation for probabilities $P_i(t)$ is

$$
{dP_i\over dt}
=\sum_j\left[W_{ij}P_j-W_{ji}P_i\right],
$$

where $W_{ij}$ is the transition rate from $j$ to $i$.

Detailed balance with equilibrium distribution $P_i^{\mathrm{eq}}$ is

$$
W_{ij}P_j^{\mathrm{eq}}=W_{ji}P_i^{\mathrm{eq}}.
$$

For finite-temperature quantum systems,

$$
Z=\mathrm{Tr}\,e^{-\beta H}.
$$

In imaginary time $\tau=it$, thermal traces are represented by evolution over interval $\hbar\beta$.

## Where the arrow of time enters

Liouville's theorem preserves phase-space volume and fine-grained entropy, so irreversible entropy increase cannot be obtained merely by rewriting exact microscopic equations. It enters through coarse-graining, special initial conditions, instability to perturbations, or kinetic assumptions such as molecular chaos.

Poincare recurrence says that a finite isolated Hamiltonian system with bounded phase-space volume returns arbitrarily close to its initial state after sufficiently long times. For macroscopic systems, recurrence times are astronomically large and do not undermine practical thermodynamics. The key point is logical rather than experimental: exact microscopic reversibility and macroscopic irreversibility describe different levels of description.

For a master equation with detailed balance, the relative entropy

$$
D(P||P^{\mathrm{eq}})
=\sum_i P_i\ln{P_i\over P_i^{\mathrm{eq}}}
$$

decreases monotonically under broad conditions. This is a discrete stochastic analogue of relaxation to equilibrium.

Boltzmann's H-theorem has the same structure: entropy increases after assuming a kinetic description that discards pre-collision correlations. The apparent paradoxes, such as Loschmidt's reversibility objection, are resolved by recognizing which step introduces time-asymmetric statistical information.

Supplementary bridge to finite-temperature field theory: the canonical partition function resembles a real-time quantum evolution operator with imaginary time:

$$
e^{-\beta H}=e^{-H(\hbar\beta)/\hbar}.
$$

Bosonic fields are periodic in imaginary time,

$$
\phi(\tau+\hbar\beta)=\phi(\tau),
$$

while fermionic fields are antiperiodic,

$$
\psi(\tau+\hbar\beta)=-\psi(\tau).
$$

The corresponding Matsubara frequencies are

$$
\omega_n^{\mathrm B}={2\pi n\over \hbar\beta},
\qquad
\omega_n^{\mathrm F}={(2n+1)\pi\over \hbar\beta}.
$$

This is the field-theory version of the same Bose and Fermi statistical distinction developed in the ideal quantum gas.

The distinction between Gibbs and Boltzmann entropy is often the cleanest way to discuss irreversibility. Gibbs entropy belongs to a probability density. If that density is evolved exactly, Liouville or unitary evolution preserves its fine-grained information. Boltzmann entropy belongs to a macrostate: a large region of phase space specified by coarse variables. A system prepared in a small, low-entropy macroregion will typically move into larger macroregions simply because they occupy overwhelmingly more phase-space volume. This is a probabilistic statement about typicality, not a strict theorem forbidding fluctuations.

Large fluctuations are possible but rare. If an entropy decrease of size $\Delta S$ requires entering a macroregion whose phase volume is smaller by $e^{-\Delta S/k_B}$, the waiting time is correspondingly enormous for macroscopic $\Delta S$. The second law is therefore effectively certain in daily thermodynamics while remaining statistical at the microscopic level.

Master equations make the coarse-graining explicit by replacing microscopic trajectories with transition rates between states or macrostates. Detailed balance ensures the correct equilibrium distribution, but relaxation also depends on connectivity and spectral gaps of the rate matrix. Systems with bottlenecks, metastable states, or glassy landscapes can obey detailed balance and still equilibrate extremely slowly.

The imaginary-time field-theory bridge is a change of representation, not a new postulate. The same thermal density matrix that defines the canonical ensemble becomes a path integral on a compact Euclidean time interval. Boundary conditions encode quantum statistics, and Matsubara sums replace continuous frequency integrals. Finite-temperature QFT consequently retains partition functions, correlation functions, response, and symmetry breaking, with fields replacing particles in fixed single-particle levels.

The arrow of time in statistical mechanics is therefore not a new microscopic force. It is a statement about preparation, typicality, coarse variables, and the overwhelming phase-space dominance of equilibrium macrostates. Low-entropy initial conditions are special; once prepared, their typical microscopic representatives evolve toward macrostates with larger volume. Time-reversed trajectories exist, but selecting them would require extraordinarily precise correlations.

Ensembles describe what is typical under constraints, kinetic equations describe how selected coarse variables relax, and field-theory methods repackage the thermal trace for systems with infinitely many modes.

Open systems sharpen the distinction further. Coupling to reservoirs can make the subsystem dynamics dissipative even when the combined system plus reservoirs evolves reversibly. Master equations, Langevin equations, and linear response theory are all reduced descriptions of this kind. Their success depends on identifying the right slow variables and the right reservoir assumptions.

Detailed finite-temperature QFT calculations add regularization, interactions, analytic continuation, and real-time response formalisms. Their statistical core is already present in $Z=\mathrm{Tr}\,e^{-\beta H}$.

```mermaid
flowchart LR
  A["Reversible microscopic dynamics"] --> B["Liouville theorem"]
  B --> C["Fine-grained entropy constant"]
  A --> D["Coarse variables"]
  D --> E["Loss of correlations"]
  E --> F["Master/Boltzmann equations"]
  F --> G["Macroscopic entropy increase"]
  H["Thermal trace"] --> I["Imaginary-time path integral"]
```

| Entropy concept | Formula | Time behavior |
|---|---:|---|
| Gibbs fine-grained | $-k_B\int\rho\ln\rho$ | constant under Liouville flow |
| Coarse-grained Gibbs | cells replace exact density | can increase after smoothing |
| Boltzmann | $k_B\ln \vert M\vert $ | increases for typical macrostates |
| Relative entropy | $\sum_i P_i\ln(P_i/P_i^{eq})$ | decreases in detailed-balance Markov relaxation |

## Relaxation rate of a two-state process

A system jumps between states $0$ and $1$ with rates $W_{10}=a$ and $W_{01}=b$. Both the equilibrium probability and relaxation rate follow from one linear equation.

1. The master equation for $P_1$ is

$$
{dP_1\over dt}=aP_0-bP_1.
$$

2. Since $P_0=1-P_1$,

$$
{dP_1\over dt}=a(1-P_1)-bP_1
=a-(a+b)P_1.
$$

3. At equilibrium, set the derivative to zero:

$$
0=a-(a+b)P_1^{\mathrm{eq}}.
$$

4. Therefore

$$
P_1^{\mathrm{eq}}={a\over a+b},
\qquad
P_0^{\mathrm{eq}}={b\over a+b}.
$$

5. Solve the linear equation:

$$
P_1(t)-P_1^{\mathrm{eq}}
=\left[P_1(0)-P_1^{\mathrm{eq}}\right]e^{-(a+b)t}.
$$

The relaxation time is $\tau=1/(a+b)$, and detailed balance is $aP_0^{\mathrm{eq}}=bP_1^{\mathrm{eq}}$.

## Matsubara frequencies from thermal boundary conditions

Bosonic and fermionic Matsubara frequencies follow directly from their boundary conditions on an imaginary-time interval of length $\hbar\beta$.

1. A Fourier mode has form

$$
e^{-i\omega_n\tau}.
$$

2. Bosonic periodicity requires

$$
e^{-i\omega_n(\tau+\hbar\beta)}
=e^{-i\omega_n\tau}.
$$

3. Cancel the common factor:

$$
e^{-i\omega_n\hbar\beta}=1.
$$

Thus

$$
\omega_n\hbar\beta=2\pi n,
\qquad
\omega_n^{\mathrm B}={2\pi n\over \hbar\beta}.
$$

4. Fermionic antiperiodicity requires

$$
e^{-i\omega_n\hbar\beta}=-1=e^{-i(2n+1)\pi}.
$$

5. Therefore

$$
\omega_n^{\mathrm F}={(2n+1)\pi\over \hbar\beta}.
$$

Integer multiples appear for bosons and half-odd-integer multiples for fermions.

## Assumptions carried by each description

- Claiming microscopic reversibility is false because macroscopic entropy increases. The point is the change of description and assumptions.
- Confusing fine-grained Gibbs entropy with coarse-grained or Boltzmann entropy.
- Forgetting that recurrence times can be finite in principle but physically irrelevant for macroscopic systems.
- Using a master equation without checking probability conservation and nonnegative transition rates.
- Treating the finite-temperature QFT bridge as a different ensemble; it is the same thermal trace written in imaginary-time language.

<div className="see-also">

See also: [Phase space, Liouville theorem, and ergodicity](/physics/statistical-mechanics/phase-space-liouville-ergodicity) · [Boltzmann equation and transport](/physics/statistical-mechanics/boltzmann-equation-and-transport) · [Brownian motion, Langevin, and Fokker-Planck dynamics](/physics/statistical-mechanics/brownian-motion-langevin-and-fokker-planck-dynamics) · [Path integrals in quantum mechanics](/physics/quantum-mechanics/path-integral-formulation) · [Path integral formulation in QFT](/physics/quantum-field-theory/path-integral-formulation)

</div>
