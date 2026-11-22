---
title: Microcanonical Ensemble and Entropy
sidebar_position: 4
---

# Microcanonical Ensemble and Entropy

The microcanonical ensemble describes an isolated system whose energy, volume, and particle number are fixed macroscopically. It is the foundational ensemble in Schwabl's construction: equilibrium is postulated as equal weight over all accessible microstates in a narrow energy shell, and the other ensembles are derived by allowing a subsystem to exchange energy or particles with a much larger isolated environment.

Its central idea is Boltzmann's: entropy is the logarithm of accessible microscopic multiplicity. The logarithm converts multiplication of independent state counts into addition of entropies, which is exactly what thermodynamics requires for macroscopic subsystems.

## What is held fixed

For a classical isolated system with Hamiltonian $H(q,p)$, define the energy-shell density of states

$$
\Omega(E,V,N)=\int {dq\,dp\over h^{3N}N!}\,\delta(E-H(q,p)).
$$

The factor $h^{3N}$ supplies a phase-space cell, and $N!$ removes the Gibbs overcounting of identical classical particles. Because the delta function has units of inverse energy, $\Omega$ as written is a density per unit energy. A count in a narrow window is $\Omega(E)\Delta E$; the arbitrary fixed width contributes only an additive entropy constant. A related dimensionless integrated volume is

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

An observable $A(q,p)$ has microcanonical average

$$
\langle A\rangle_E
={1\over\Omega(E)}
\int {dq\,dp\over h^{3N}N!}
A(q,p)\delta(E-H).
$$

The delta function confines integration to the energy surface with the induced measure $d\Sigma/\vert \nabla H\vert $, not uniform Euclidean surface area. Regions where the Hamiltonian changes slowly normal to the surface receive more weight. For numerical work, a thin shell is often easier to sample than a literal delta function, and the shell thickness must remain small compared with the macroscopic energy resolution.

For a quantum Hamiltonian with discrete levels, the sharp analogue is a normalized projector onto an energy window,

$$
\rho_{\mathrm{mc}}={P_{[E,E+\Delta E]}\over
\operatorname{Tr}P_{[E,E+\Delta E]}}.
$$

The window is narrow on macroscopic energy scales but broad enough to contain many levels. An exact single eigenvalue is usually too restrictive for thermodynamics, especially when finite-size level spacings and degeneracies matter.

## Why equal weights lead to temperature

The equal a priori probability postulate says that all microstates compatible with the macroscopic constraints are assigned equal statistical weight. This is not a statement that all phase-space points are dynamically visited in a literal finite time; it is the equilibrium hypothesis for an isolated macrostate.

Maximizing Gibbs--Shannon entropy under normalization and an exact restriction to the allowed shell gives the same uniform distribution. That variational statement reorganizes the postulate; it does not prove that a particular Hamiltonian trajectory equilibrates. Mixing, chaos, typicality, and coupling to measuring devices belong to the dynamical justification.

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

More explicitly, use

$$
{\partial^2S\over\partial E^2}
=-{1\over T^2C_V}.
$$

Expanding $S_A(E_A)+S_B(E-E_A)$ about its maximum gives a Gaussian energy-sharing distribution with

$$
{1\over\langle(\Delta E_A)^2\rangle}
={1\over k_BT^2}\left({1\over C_A}+{1\over C_B}\right).
$$

If $B$ is an enormous bath, $C_B\to\infty$ and the variance reduces to $k_BT^2C_A$, the canonical result. If the two subsystems are comparable, conservation of total energy suppresses the fluctuations relative to that bath limit.

## Counting the ideal-gas shell

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

The phase-space volume below energy $E$ can be written explicitly:

$$
\Gamma(E,V,N)
={V^N\over N!h^{3N}}
{\pi^{3N/2}(2mE)^{3N/2}\over
\Gamma(3N/2+1)}.
$$

The $V^N$ is the configuration-space volume. The remaining factor is the volume of a $3N$-dimensional momentum sphere of radius $\sqrt{2mE}$. Taking $k_B\ln\Gamma$, then using Stirling's approximation for both $N!$ and the gamma function, gives the Sackur--Tetrode expression. Differentiating before making the large-$N$ approximation also gives

$$
{1\over T}=k_B{3N\over2E}
$$

for the volume entropy, up to the finite-$N$ convention. The energy-shell definition instead replaces $3N/2$ by $3N/2-1$ in this intermediate result. Their relative difference is of order $1/N$.

## Concavity, stability, and ensemble inequivalence

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

Negative absolute temperature should not be confused with a temperature below zero kelvin in an unbounded system. It requires entropy to decrease as energy approaches an upper spectral bound, as in the finite spin example below. Such a state is hotter than every positive-temperature state in the sense that, when coupled consistently, energy flows from the negative-temperature system to the positive-temperature one.

A final caution is that "equal probability" applies to microstates in the correct measure, not to arbitrary macroscopic variables. For an ideal gas, equal weight in phase space does not mean equal probability for each particle speed. The speed distribution includes the geometric volume of momentum shells, which is why the Maxwell speed density contains $4\pi v^2$.

The microcanonical ensemble is therefore both narrower and stronger than the slogan "all states are equally likely." It specifies the constraint surface, the measure on that surface, and the macroscopic equivalence class being described. If a container is split by an insulating wall, the relevant constraints include the separate energies of the two sides. If the wall conducts heat, only the total energy is fixed and the most probable energy division is found by maximizing total entropy. Changing constraints changes the ensemble.

This is the statistical version of thermodynamic preparation. The same Hamiltonian can represent different experiments depending on which quantities are controlled, isolated, or allowed to fluctuate.

Additivity is the hidden assumption behind most of the familiar thermodynamic conclusions. If two weakly coupled parts have entropies that add, then maximizing total entropy gives sharp equilibrium conditions. Surface terms, long-range interactions, and small-system corrections can spoil exact additivity. Schwabl's graduate-level presentation keeps these qualifications visible because they mark the boundary between textbook thermodynamics and active statistical-mechanics problems.

The logarithm is forced by this composition rule. Independent subsystems have multiplicities $W_{AB}=W_AW_B$. If entropy is a continuous function of multiplicity and must satisfy $S(W_AW_B)=S(W_A)+S(W_B)$, its form is proportional to $\ln W$. The constant of proportionality is $k_B$, which fixes the temperature scale. This argument explains the functional form but not the equal-weight postulate or which constraints define $W$.

Extensivity is related but separate. For short-range matter, doubling $E,V,N$ at fixed densities doubles the leading entropy. Boundaries contribute more slowly than volume and disappear per particle. Gravity and other sufficiently long-range forces can keep interactions between distant pieces comparable to bulk energies, breaking the usual additive construction.

Phase coexistence appears as a nearly linear segment of entropy versus energy in the thermodynamic limit. Its slope is the common inverse temperature while added energy changes the phase fraction rather than temperature. For a finite short-range system, interface free energy can produce a convex-looking correction over a small range. One must separate that finite-size surface effect from genuine bulk nonconcavity caused by nonadditive long-range interactions.

Numerically, microcanonical molecular dynamics fixes energy only up to integration error. A symplectic method controls long-time drift better than a generic solver, but measured averages still need equilibration checks and uncertainty estimates based on correlated samples.

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

## Worked example 3: sharing a fixed number of quanta

Two Einstein solids contain $N_A$ and $N_B$ oscillators and share $q$ indistinguishable energy quanta. The multiplicity of one solid with $N$ oscillators and $q$ quanta is

$$
\Omega(N,q)={q+N-1\choose q}.
$$

If solid $A$ holds $q_A$ quanta, the combined multiplicity is

$$
\Omega_{\mathrm{tot}}(q_A)
=\Omega(N_A,q_A)\Omega(N_B,q-q_A).
$$

To locate its maximum exactly, compare adjacent terms. The ratio for one solid is

$$
{\Omega(N,q+1)\over\Omega(N,q)}={q+N\over q+1}.
$$

Moving one quantum from $B$ to $A$ changes total multiplicity by

$$
{\Omega_{\mathrm{tot}}(q_A+1)\over\Omega_{\mathrm{tot}}(q_A)}
={q_A+N_A\over q_A+1}
{q_B\over q_B+N_B-1},
\qquad q_B=q-q_A.
$$

The most probable division lies where this ratio crosses one. For large $q$ and $N$, dropping the additive ones gives

$$
{q_A+N_A\over q_A}{q_B\over q_B+N_B}\simeq1,
$$

which reduces to

$$
{q_A\over N_A}\simeq{q_B\over N_B}.
$$

Energy is shared so that the mean number of quanta per oscillator agrees. Taking logarithms and derivatives expresses the same condition as equal microcanonical temperatures. The full distribution still has a width; equilibrium selects a sharply dominant range rather than one compulsory microstate.

## What to check in a state count

- Identical classical particles require the $N!$ divisor. Without it, entropy is nonextensive and mixing identical samples produces the Gibbs paradox.
- The shell width fixes a normalization convention. A fixed, macroscopically narrow width does not affect leading derivatives, but an energy-dependent width can.
- Negative temperatures require an upper-bounded spectrum. Unbounded kinetic energy prevents them for the ordinary ideal gas.
- $\Omega(E)$ and $\Gamma(E)$ are closely related at large $N$ but yield different finite-size derivatives. The chosen entropy convention should be stated.
- Equal weight means equal weight in the invariant phase-space measure, not equal probability for a nonlinear coordinate or a coarse macrovariable.
- Quantum microcanonical states use an energy-window projector. Replacing it by one arbitrary eigenstate requires an additional typicality or eigenstate-thermalization argument.

## Related pages

- [Phase space, Liouville theorem, and ergodicity](/physics/statistical-mechanics/phase-space-liouville-ergodicity)
- [Canonical ensemble and fluctuations](/physics/statistical-mechanics/canonical-ensemble-and-fluctuations)
- [Classical ideal gas and Maxwell distribution](/physics/statistical-mechanics/classical-ideal-gas-and-maxwell-distribution)
- [Thermodynamics](/physics/thermodynamics/intro)
- [Entropy and coding](/math/probability-and-random-variables/entropy-and-coding)
