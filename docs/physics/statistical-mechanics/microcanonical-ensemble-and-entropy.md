---
title: Microcanonical Ensemble and Entropy
sidebar_position: 4
---

# Microcanonical Ensemble and Entropy

The microcanonical ensemble describes an isolated system whose energy, volume, and particle number are fixed macroscopically. It is the foundational ensemble in Schwabl's construction: equilibrium is postulated as equal weight over all accessible microstates in a narrow energy shell, and the other ensembles are derived by allowing a subsystem to exchange energy or particles with a much larger isolated environment.

Its central idea is Boltzmann's: entropy is the logarithm of accessible microscopic multiplicity. The logarithm converts multiplication of independent state counts into addition of entropies, which is exactly what thermodynamics requires for macroscopic subsystems.

## Definitions

For a classical isolated system with Hamiltonian $H(q,p)$, define the energy-shell density of states

$$
\Omega(E,V,N)=\int {dq\,dp\over h^{3N}N!}\,\delta(E-H(q,p)).
$$

The factor $h^{3N}$ makes the phase-space count dimensionless, and $N!$ removes the Gibbs overcounting of identical classical particles. A related integrated volume is

$$
\Gamma(E,V,N)=\int_{H(q,p)\le E}{dq\,dp\over h^{3N}N!}.
$$

For macroscopic systems, defining entropy using $\Omega$ or $\Gamma$ differs only by subextensive corrections:

$$
S(E,V,N)=k_B\ln \Omega(E,V,N)
\quad\text{or}\quad
S(E,V,N)=k_B\ln \Gamma(E,V,N).
$$

Thermodynamic variables are derivatives of entropy:

$$
{1\over T}=\left({\partial S\over \partial E}\right)_{V,N},
\qquad
{p\over T}=\left({\partial S\over \partial V}\right)_{E,N},
\qquad
-{\mu\over T}=\left({\partial S\over \partial N}\right)_{E,V}.
$$

The microcanonical probability density is

$$
\rho_{\mathrm{mc}}(q,p)
={\delta(E-H(q,p))\over \Omega(E,V,N)}
$$

with the same measure convention as above.

## Key results

The equal a priori probability postulate says that all microstates compatible with the macroscopic constraints are assigned equal statistical weight. This is not a statement that all phase-space points are dynamically visited in a literal finite time; it is the equilibrium hypothesis for an isolated macrostate.

If two weakly interacting isolated systems $A$ and $B$ share total energy $E$, the probability that $A$ has energy $E_A$ is proportional to

$$
P(E_A)\propto \Omega_A(E_A)\Omega_B(E-E_A).
$$

The maximum of $P$ satisfies

$$
{\partial \ln \Omega_A\over \partial E_A}
=
{\partial \ln \Omega_B\over \partial E_B},
$$

or $T_A=T_B$. Thus equality of temperature is not added from thermodynamics; it follows from maximizing multiplicity.

The width of the distribution is obtained by expanding entropy around the maximum. Since heat capacities are extensive, the standard deviation of subsystem energy scales like $\sqrt{N}$ while the energy scales like $N$. This is the microcanonical root of ensemble equivalence.

For the classical ideal gas,

$$
H=\sum_{i=1}^N {p_i^2\over 2m},
$$

the momentum-space volume is a $3N$-dimensional sphere. The entropy becomes, after Stirling's approximation, the Sackur-Tetrode form

$$
S=Nk_B\left[
\ln\left({V\over N}\left({4\pi mE\over 3Nh^2}\right)^{3/2}\right)
{+}{5\over 2}
\right],
$$

up to the usual convention about using $\Gamma$ or $\Omega$. Differentiating gives

$$
E={3\over 2}Nk_BT,\qquad pV=Nk_BT.
$$

These equations show the deductive structure Schwabl stresses: thermodynamics appears as derivatives of microscopic counting.

The choice between $\Omega(E)$ and $\Gamma(E)$ is usually harmless in the thermodynamic limit but conceptually important in small systems. $\Omega(E)$ counts states on an energy shell, while $\Gamma(E)$ counts states below an energy. Their logarithms differ by terms involving the density-of-states growth scale. For macroscopic systems with short-range interactions, entropy is extensive and such differences are negligible compared with $N$. For few-body systems or systems with unusual spectra, however, the distinction can affect definitions of temperature and heat capacity.

The concavity of entropy is the statistical statement of thermodynamic stability. If two subsystems exchange energy, the total entropy

$$
S_{\mathrm{tot}}(E_A)=S_A(E_A)+S_B(E-E_A)
$$

must have a maximum at equilibrium. The first derivative gives $T_A=T_B$. The second derivative condition gives

$$
{\partial^2 S_A\over \partial E_A^2}
+{\partial^2 S_B\over \partial E_B^2}<0.
$$

For ordinary systems this is equivalent to positive heat capacities. Long-range interacting systems can violate the usual additivity assumptions and show microcanonical features, such as negative heat capacity, that are not compatible with the canonical ensemble.

The microcanonical ensemble also clarifies adiabatic invariance. For a quasistatic change of an external parameter, an isolated system remains on an energy shell whose enclosed phase-space volume changes in a controlled way. This is the mechanical root of reversible adiabatic thermodynamics. In practice, the wall motion or parameter change must be slow compared with microscopic equilibration but fast enough to avoid heat exchange with the environment.

A final caution is that "equal probability" applies to microstates in the correct measure, not to arbitrary macroscopic variables. For an ideal gas, equal weight in phase space does not mean equal probability for each particle speed. The speed distribution includes the geometric volume of momentum shells, which is why the Maxwell speed density contains $4\pi v^2$.

The microcanonical ensemble is therefore both narrower and stronger than the slogan "all states are equally likely." It specifies the constraint surface, the measure on that surface, and the macroscopic equivalence class being described. If a container is split by an insulating wall, the relevant constraints include the separate energies of the two sides. If the wall conducts heat, only the total energy is fixed and the most probable energy division is found by maximizing total entropy. Changing constraints changes the ensemble.

This is the statistical version of thermodynamic preparation. The same Hamiltonian can represent different experiments depending on which quantities are controlled, isolated, or allowed to fluctuate.

Additivity is the hidden assumption behind most of the familiar thermodynamic conclusions. If two weakly coupled parts have entropies that add, then maximizing total entropy gives sharp equilibrium conditions. Surface terms, long-range interactions, and small-system corrections can spoil exact additivity. Schwabl's graduate-level presentation keeps these qualifications visible because they mark the boundary between textbook thermodynamics and active statistical-mechanics problems.

## Visual

```mermaid
graph LR
  A["Fixed E,V,N"] --> B["Accessible energy shell"]
  B --> C["Equal weights"]
  C --> D["Omega(E,V,N)"]
  D --> E["S = k_B ln Omega"]
  E --> F["T, p, mu from derivatives"]
```

| Entropy derivative | Thermodynamic variable | Meaning |
|---|---:|---|
| $(\partial S/\partial E)_{V,N}$ | $1/T$ | energy sharing at equilibrium |
| $(\partial S/\partial V)_{E,N}$ | $p/T$ | response to boundary displacement |
| $(\partial S/\partial N)_{E,V}$ | $-\mu/T$ | cost of adding particles |
| second derivatives of $S$ | stability conditions | positive heat capacity, concavity |

## Worked example 1: Temperature of a two-level spin system

Problem: $N$ independent spins in a magnetic field have energies $-\epsilon$ and $+\epsilon$. If $n$ spins are in the upper level, find the microcanonical temperature.

Method:

1. The total energy is

$$
E=n\epsilon+(N-n)(-\epsilon)
=\epsilon(2n-N),
$$

so

$$
n={N\over 2}+{E\over 2\epsilon}.
$$

2. The multiplicity is

$$
\Omega(E)=\binom{N}{n}.
$$

3. Stirling's approximation gives

$$
\ln\Omega
\approx N\ln N-n\ln n-(N-n)\ln(N-n).
$$

4. Differentiate with respect to $n$:

$$
{\partial \ln\Omega\over \partial n}
=\ln{N-n\over n}.
$$

Since $dn/dE=1/(2\epsilon)$,

$$
{1\over T}
=k_B{\partial \ln\Omega\over \partial E}
={k_B\over 2\epsilon}\ln{N-n\over n}.
$$

Checked answer: if $n\lt N/2$, then $T\gt 0$. If $n\gt N/2$, the logarithm is negative and the spin system has negative absolute temperature, possible because the spectrum is bounded above.

## Worked example 2: Ideal gas pressure from entropy

Problem: Use the entropy dependence $S=Nk_B[\ln V+\text{terms independent of }V]$ to derive the ideal-gas law.

Method:

1. Start from the microcanonical pressure definition:

$$
{p\over T}=\left({\partial S\over \partial V}\right)_{E,N}.
$$

2. Differentiate:

$$
\left({\partial S\over \partial V}\right)_{E,N}
=Nk_B {1\over V}.
$$

3. Therefore

$$
{p\over T}={Nk_B\over V}.
$$

4. Multiply by $VT$:

$$
pV=Nk_BT.
$$

Checked answer: no kinetic-theory wall-collision argument was needed. The pressure is the entropy gain available when volume increases.

## Code

```python
import math

def spin_entropy(N, n, kB=1.0):
    return kB * (math.lgamma(N + 1) - math.lgamma(n + 1) - math.lgamma(N - n + 1))

N = 200
eps = 1.0
for n in [60, 100, 140]:
    E = eps * (2 * n - N)
    # central difference in energy using n +/- 1
    dS_dE = (spin_entropy(N, n + 1) - spin_entropy(N, n - 1)) / (4 * eps)
    T = 1.0 / dS_dE if dS_dE != 0 else float("inf")
    print(n, E, T)
```

## Common pitfalls

- Omitting the $N!$ factor for identical classical particles, which leads to the Gibbs paradox and nonextensive entropy.
- Treating the energy shell width as physically important for macroscopic thermodynamics. It affects normalization but not leading thermodynamic derivatives.
- Forgetting that negative temperatures require an upper-bounded spectrum; they do not occur for an ideal gas with unbounded kinetic energy.
- Confusing $\Omega(E)$ with $\Gamma(E)$. They are closely related for large systems but not identical in small-system calculations.
- Assuming the microcanonical ensemble is only classical. Quantum mechanically, it is a normalized projector onto an energy window.

## Connections

- [Phase space, Liouville theorem, and ergodicity](/physics/statistical-mechanics/phase-space-liouville-ergodicity)
- [Canonical ensemble and fluctuations](/physics/statistical-mechanics/canonical-ensemble-and-fluctuations)
- [Classical ideal gas and Maxwell distribution](/physics/statistical-mechanics/classical-ideal-gas-and-maxwell-distribution)
- [Thermodynamics](/physics/thermodynamics/)
- [Entropy and coding](/math/probability-and-random-variables/entropy-and-coding)
