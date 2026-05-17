---
title: Quantum Statistics and Ideal Quantum Gases
sidebar_position: 8
---

# Quantum Statistics and Ideal Quantum Gases

Quantum statistics changes the meaning of "counting states." Identical particles cannot be labeled as classical objects, and the many-body wavefunction must be symmetric for bosons or antisymmetric for fermions. This single structural fact produces Bose-Einstein condensation, blackbody radiation, the stability of metals, electron degeneracy pressure, and many other effects absent from classical gases.

Schwabl develops ideal quantum gases most cleanly in the grand canonical ensemble. The noninteracting Hamiltonian factorizes into single-particle occupations, but the allowed occupation numbers depend on statistics: $n_\alpha=0,1$ for fermions and $n_\alpha=0,1,2,\ldots$ for bosons.

## Definitions

For single-particle energies $\epsilon_\alpha$,

$$
H=\sum_\alpha \epsilon_\alpha n_\alpha,
\qquad
N=\sum_\alpha n_\alpha.
$$

The grand partition function factorizes:

$$
\mathcal Z=\prod_\alpha \mathcal Z_\alpha.
$$

For fermions,

$$
\mathcal Z_\alpha^{\mathrm F}
=\sum_{n=0}^{1}e^{-\beta(\epsilon_\alpha-\mu)n}
=1+e^{-\beta(\epsilon_\alpha-\mu)}.
$$

For bosons,

$$
\mathcal Z_\alpha^{\mathrm B}
=\sum_{n=0}^{\infty}e^{-\beta(\epsilon_\alpha-\mu)n}
={1\over 1-e^{-\beta(\epsilon_\alpha-\mu)}},
$$

valid when $e^{-\beta(\epsilon_\alpha-\mu)}\lt 1$ for every level. The mean occupations are

$$
f_{\mathrm{FD}}(\epsilon)
={1\over e^{\beta(\epsilon-\mu)}+1},
\qquad
f_{\mathrm{BE}}(\epsilon)
={1\over e^{\beta(\epsilon-\mu)}-1}.
$$

The classical Maxwell-Boltzmann limit occurs when $e^{\beta(\epsilon-\mu)}\gg 1$, giving

$$
f(\epsilon)\approx e^{-\beta(\epsilon-\mu)}=ze^{-\beta\epsilon}.
$$

## Key results

The grand potential for ideal quantum gases is

$$
\Phi_G^{\mathrm F}
=-k_BT\sum_\alpha \ln\left(1+ze^{-\beta\epsilon_\alpha}\right),
$$

and

$$
\Phi_G^{\mathrm B}
=k_BT\sum_\alpha \ln\left(1-ze^{-\beta\epsilon_\alpha}\right).
$$

The particle number is

$$
N=\sum_\alpha f(\epsilon_\alpha).
$$

For a three-dimensional box with spin degeneracy $g$, sums over states are often replaced by

$$
\sum_\alpha \to g {V\over h^3}\int d^3p
=g{V\over 2\pi^2\hbar^3}\int_0^\infty p^2\,dp.
$$

Using $\epsilon=p^2/(2m)$,

$$
\sum_\alpha \to
gV {2\pi(2m)^{3/2}\over h^3}
\int_0^\infty \epsilon^{1/2}\,d\epsilon.
$$

The degeneracy parameter is

$$
n\lambda_T^3,
\qquad n={N\over V}.
$$

Classical statistics is reliable when $n\lambda_T^3\ll 1$. Quantum statistics matters when wave packets overlap, i.e. when $n\lambda_T^3$ is not small. For fermions, Pauli exclusion creates a filled Fermi sea at low temperature. For bosons, macroscopic occupation of the ground state can occur when the excited states cannot hold all particles.

The sign difference between fermions and bosons can be traced to the symmetry of the many-particle state. For two particles in one-particle states $a$ and $b$,

$$
|\psi_{\mathrm B}\rangle
={1\over \sqrt{2}}\left(|a\rangle|b\rangle+|b\rangle|a\rangle\right),
$$

while

$$
|\psi_{\mathrm F}\rangle
={1\over \sqrt{2}}\left(|a\rangle|b\rangle-|b\rangle|a\rangle\right).
$$

If $a=b$, the fermionic state vanishes. This is Pauli exclusion in its simplest form. In occupation-number language it becomes the rule $n_\alpha=0$ or $1$.

Quantum ideal gases also show why the grand canonical ensemble is more than a convenience. The many-body canonical partition function at fixed $N$ must enforce a global sum over occupations, $\sum_\alpha n_\alpha=N$. The grand ensemble removes that constraint with a fugacity and makes different levels independent. The fixed-$N$ answer is recovered by choosing $\mu$ so that the mean particle number matches the desired value, with relative number fluctuations vanishing for ordinary macroscopic phases.

The classical limit can be expressed as an expansion in fugacity. For small $z$,

$$
\ln(1+ze^{-\beta\epsilon})
\approx ze^{-\beta\epsilon}-{1\over 2}z^2e^{-2\beta\epsilon}+\cdots
$$

for fermions, while

$$
-\ln(1-ze^{-\beta\epsilon})
\approx ze^{-\beta\epsilon}+{1\over 2}z^2e^{-2\beta\epsilon}+\cdots
$$

for bosons. The first term is Maxwell-Boltzmann statistics. The second term is the leading quantum correction to virial behavior: fermions act as if they repel statistically, while bosons act as if they attract statistically.

Occupation-number language is also the bridge to second quantization. Creation and annihilation operators add or remove particles from a mode, and the many-body basis is specified by the occupation list $(n_1,n_2,\ldots)$. For bosons,

$$
n_\alpha=0,1,2,\ldots,
$$

while for fermions anticommutation enforces

$$
n_\alpha=0,1.
$$

The ideal-gas Hamiltonian is diagonal in this basis, making the grand partition product exact.

Interactions break the simple product over modes, but the statistical distinction remains. Perturbation theory, quasiparticles, and finite-temperature field theory all start from these noninteracting occupation factors and then add corrections. This is why mastering ideal quantum gases is not optional; it is the reference theory for much of condensed matter and many-body physics.

Exchange symmetry also creates correlations without forces. Even an ideal Fermi gas has reduced probability for two identical fermions with the same spin to be close in phase space, while an ideal Bose gas has enhanced occupation fluctuations. These are statistical correlations, not potential-energy effects. They appear in virial corrections, density correlations, and quantum optics. The word "ideal" therefore means noninteracting, not classically uncorrelated.

In the thermodynamic limit, sums over levels become integrals only when level spacing is small compared with thermal scales. Ground states, gaps, and low-dimensional densities of states must be handled separately.

Spin degeneracy is another common source of factors. A spin-$1/2$ gas with no magnetic splitting has two states for each momentum, while polarized gases or particles with internal hyperfine structure require different degeneracy counts. These factors multiply density of states and therefore shift $\mu$, $p$, and $N$ even when the occupation formula itself is unchanged.

For finite systems, discrete levels can dominate. A cold trapped gas, a quantum dot, or a small cavity may not be well approximated by a continuum density of states. In those cases the product over levels should be kept explicitly, and thermodynamic-limit intuition must be applied with care.

## Visual

| Statistics | Allowed $n_\alpha$ | Mean occupation | Low-temperature behavior |
|---|---:|---:|---|
| Maxwell-Boltzmann | effectively any, dilute | $e^{-\beta(\epsilon-\mu)}$ | classical exponential tail |
| Fermi-Dirac | $0$ or $1$ | $1/(e^{\beta(\epsilon-\mu)}+1)$ | filled states below $\mu$ |
| Bose-Einstein | $0,1,2,\ldots$ | $1/(e^{\beta(\epsilon-\mu)}-1)$ | enhanced low-energy occupation |

```text
occupation
 ^
1| FD:  ______
 |          \
 |           \
0|------------\----------> epsilon
 | BE: rises sharply near mu from above
```

## Worked example 1: Fermion and boson occupation of the same level

Problem: Let $T$ be such that $\beta(\epsilon-\mu)=2$. Compute $f_{\mathrm{FD}}$ and $f_{\mathrm{BE}}$.

Method:

1. Evaluate the exponential:

$$
e^{\beta(\epsilon-\mu)}=e^2\approx 7.389.
$$

2. Fermion occupation:

$$
f_{\mathrm{FD}}
={1\over e^2+1}
={1\over 8.389}
\approx 0.119.
$$

3. Boson occupation:

$$
f_{\mathrm{BE}}
={1\over e^2-1}
={1\over 6.389}
\approx 0.157.
$$

4. Classical approximation:

$$
f_{\mathrm{MB}}=e^{-2}\approx 0.135.
$$

Checked answer: for this moderately dilute level, the classical value lies between FD and BE. Fermions are suppressed by exclusion; bosons are enhanced by stimulated occupation.

## Worked example 2: Degeneracy parameter for helium gas

Problem: Estimate $n\lambda_T^3$ for helium atoms at $T=4\,\mathrm K$ and number density $n=2.2\times 10^{28}\,\mathrm{m^{-3}}$. Use $m=6.64\times 10^{-27}\,\mathrm{kg}$.

Method:

1. Compute the thermal wavelength:

$$
\lambda_T={h\over \sqrt{2\pi m k_BT}}.
$$

2. Insert values:

$$
2\pi m k_BT
=2\pi(6.64\times 10^{-27})(1.380649\times 10^{-23})(4)
\approx 2.31\times 10^{-48}.
$$

3. Its square root is approximately $1.52\times 10^{-24}$, so

$$
\lambda_T\approx {6.626\times 10^{-34}\over 1.52\times 10^{-24}}
\approx 4.36\times 10^{-10}\,\mathrm m.
$$

4. The degeneracy parameter is

$$
n\lambda_T^3
=(2.2\times 10^{28})(4.36\times 10^{-10})^3
\approx 1.8.
$$

Checked answer: the value is not small, so quantum statistics is essential for liquid helium near a few kelvin.

## Code

```python
import numpy as np

def fermi(eps, mu, T, kB=1.0):
    return 1.0 / (np.exp((eps - mu) / (kB * T)) + 1.0)

def bose(eps, mu, T, kB=1.0):
    x = np.exp((eps - mu) / (kB * T))
    return 1.0 / (x - 1.0)

eps = np.linspace(0.1, 5.0, 10)
mu = 0.0
T = 0.5
for e in eps:
    print(f"{e:.2f}", f"{fermi(e, mu, T):.4f}", f"{bose(e, mu, T):.4f}")
```

## Common pitfalls

- Labeling identical quantum particles as if they were distinguishable classical particles.
- Forgetting that the Bose formula requires $\mu$ below the lowest single-particle energy.
- Assuming the Maxwell-Boltzmann limit is high temperature only. Low density is equally important through $n\lambda_T^3$.
- Confusing occupation of a single-particle level with the probability that the many-body system has one particle total.
- Replacing sums by integrals without checking whether the ground state must be separated, especially near Bose-Einstein condensation.

## Connections

- [Grand canonical ensemble and particle exchange](/physics/statistical-mechanics/grand-canonical-ensemble-and-particle-exchange)
- [Degenerate Fermi gas](/physics/statistical-mechanics/degenerate-fermi-gas)
- [Bose gases, photons, and phonons](/physics/statistical-mechanics/bose-gases-photons-and-phonons)
- [Identical particles and symmetrization](/physics/quantum-mechanics/identical-particles-symmetrization)
- [Quantum field theory motivation](/physics/quantum-field-theory/motivation-fields-and-quanta)
