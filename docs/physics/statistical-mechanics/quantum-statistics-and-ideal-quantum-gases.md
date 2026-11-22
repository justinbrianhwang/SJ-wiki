---
title: Quantum Statistics and Ideal Quantum Gases
sidebar_position: 8
---

# Quantum Statistics and Ideal Quantum Gases

Quantum statistics changes the meaning of "counting states." Identical particles cannot be labeled as classical objects, and the many-body wavefunction must be symmetric for bosons or antisymmetric for fermions. This single structural fact produces Bose-Einstein condensation, blackbody radiation, the stability of metals, electron degeneracy pressure, and many other effects absent from classical gases.

Schwabl develops ideal quantum gases most cleanly in the grand canonical ensemble. The noninteracting Hamiltonian factorizes into single-particle occupations, but the allowed occupation numbers depend on statistics: $n_\alpha=0,1$ for fermions and $n_\alpha=0,1,2,\ldots$ for bosons.

## Occupation numbers replace particle labels

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

The mean occupations follow by differentiating a one-level partition function. With $x_\alpha=ze^{-\beta\epsilon_\alpha}$,

$$
\langle n_\alpha\rangle
=x_\alpha{\partial\over\partial x_\alpha}
\ln\mathcal Z_\alpha.
$$

For fermions $\mathcal Z_\alpha=1+x_\alpha$; for bosons it is $(1-x_\alpha)^{-1}$. The same differentiation gives the level fluctuations

$$
\operatorname{Var}n_\alpha=f_\alpha(1-f_\alpha)
$$

for fermions and $f_\alpha(1+f_\alpha)$ for bosons. Exclusion suppresses fluctuations, whereas repeated occupation enhances them.

## Grand potentials and the continuum limit

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

The last line is shorthand for inserting the density of states inside an integral over a function of energy. Explicitly,

$$
D(\epsilon)={gV\over4\pi^2}
\left({2m\over\hbar^2}\right)^{3/2}\sqrt\epsilon,
\qquad
\sum_\alpha F(\epsilon_\alpha)\to
\int_0^\infty D(\epsilon)F(\epsilon)\,d\epsilon.
$$

Boundary and ground-state contributions are subextensive for ordinary thermodynamics but can dominate a condensate occupation, so the lowest level is often separated before applying the integral.

For quadratic dispersion in three dimensions, integration by parts also gives $pV=(2/3)E$ for both ideal Fermi and Bose gases. Statistics changes the relation between density, fugacity, and energy, but the virial relation follows from the momentum scaling of the kinetic Hamiltonian.

## When Maxwell--Boltzmann statistics emerges

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

The last qualification matters for a Bose condensate. Treating the ideal ground mode independently in the grand ensemble gives

$$
\operatorname{Var}N_0=\langle N_0\rangle(1+\langle N_0\rangle),
$$

which is of order $N_0^2$ when the occupation is macroscopic. A fixed-$N$ canonical gas cannot have such total-number fluctuations. Bulk thermodynamic functions still agree in the thermodynamic limit, but condensate-number fluctuations are ensemble sensitive in the idealized model. Weak interactions and finite-size constraints change the result as well.

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

Carrying the Gaussian momentum integral through gives, for one internal component in three dimensions,

$$
{p\over k_BT}={1\over\lambda_T^3}
\left(z\mp{z^2\over2^{5/2}}+\cdots\right),
$$

$$
n={1\over\lambda_T^3}
\left(z\mp{z^2\over2^{3/2}}+\cdots\right),
$$

where the upper displayed minus applies to fermions and the plus to bosons. Eliminating $z$ yields

$$
{p\over nk_BT}=1\pm{n\lambda_T^3\over2^{5/2}}+\cdots,
$$

with plus for fermions and minus for bosons. This effective repulsion or attraction is an exchange correction; no interparticle potential has been introduced.

## Fermi surfaces, Bose accumulation, and dimension

Occupation-number language is also the bridge to second quantization. Creation and annihilation operators add or remove particles from a mode, and the many-body basis is specified by the occupation list $(n_1,n_2,\ldots)$. For bosons,

$$
n_\alpha=0,1,2,\ldots,
$$

while for fermions anticommutation enforces

$$
n_\alpha=0,1.
$$

The ideal-gas Hamiltonian is diagonal in this basis, making the grand partition product exact.

Interactions break the simple product over modes, but the statistical distinction remains. Perturbation theory, quasiparticles, and finite-temperature field theory all start from these noninteracting occupation factors and then add corrections. Ideal quantum gases are the reference theory for much of condensed matter and many-body physics.

For fermions, weak interactions may preserve long-lived quasiparticles and a Fermi surface, leading to Fermi-liquid theory with renormalized effective mass and response coefficients. For bosons, repulsive interactions reorganize low-energy excitations into collective sound modes and remove some pathologies of the ideal condensate. The occupation formulas remain benchmarks, but ``ideal'' should be read as a controlled reference Hamiltonian rather than a universally accurate low-temperature material model.

Exchange effects also depend on internal state. Two fermions in orthogonal spin states are distinguishable by spin measurement and are not Pauli blocked from sharing the same spatial orbital. A balanced two-component Fermi gas therefore has different short-range correlations from a fully polarized gas. The degeneracy factor in the density of states and the symmetry of the spatial wavefunction must be treated together.

Exchange symmetry also creates correlations without forces. Even an ideal Fermi gas has reduced probability for two identical fermions with the same spin to be close in phase space, while an ideal Bose gas has enhanced occupation fluctuations. These are statistical correlations, not potential-energy effects. They appear in virial corrections, density correlations, and quantum optics. The word "ideal" therefore means noninteracting, not classically uncorrelated.

Whether excited states can saturate depends on the low-energy density of states. For dispersion $\epsilon\propto p^2$ in $d$ dimensions, $D(\epsilon)\propto\epsilon^{d/2-1}$. At the Bose limit $\mu\to\epsilon_0$, the low-energy number integral behaves as

$$
\int_0 d\epsilon\,{\epsilon^{d/2-1}\over e^{\beta\epsilon}-1}
\sim\int_0 d\epsilon\,\epsilon^{d/2-2}.
$$

It converges at zero energy only for $d\gt 2$. Thus a uniform ideal gas with quadratic dispersion has ordinary finite-temperature Bose condensation in three dimensions but not in one or two. Traps, finite size, interactions, or different dispersion can change that conclusion.

In three dimensions, choosing the ground-state energy as zero gives the maximum excited-state density

$$
n_{\mathrm{ex}}^{\max}(T)
={g\over\lambda_T^3}\zeta(3/2).
$$

The critical temperature at fixed total density is therefore determined by

$$
n={g\over\lambda_{T_c}^3}\zeta(3/2),
$$

or

$$
k_BT_c={2\pi\hbar^2\over m}
\left[{n\over g\zeta(3/2)}\right]^{2/3}.
$$

Below $T_c$, the excited density scales as $T^{3/2}$ while the remaining particles occupy the ground mode:

$$
{N_0\over N}=1-\left({T\over T_c}\right)^{3/2}.
$$

This ideal-gas result assumes the thermodynamic limit and a uniform box. It predicts macroscopic occupation of one mode, not by itself superfluidity; interactions and phase stiffness matter for that phenomenon.

Fermions have no analogous saturation. At $T=0$, all states below the Fermi energy are filled and those above are empty. Increasing density expands the occupied momentum sphere and raises its kinetic energy. At low nonzero temperature, only a shell of width roughly $k_BT$ around the Fermi surface changes occupancy, producing heat capacity linear in $T$.

## Entropy per mode

The entropy of an ideal quantum gas can be written directly in terms of mean occupations. For fermions,

$$
S_F=-k_B\sum_\alpha
\left[f_\alpha\ln f_\alpha+(1-f_\alpha)\ln(1-f_\alpha)\right],
$$

while for bosons,

$$
S_B=k_B\sum_\alpha
\left[(1+f_\alpha)\ln(1+f_\alpha)-f_\alpha\ln f_\alpha\right].
$$

The fermion expression is the binary entropy of an empty-or-occupied level. The boson expression comes from the geometric occupation distribution. In the dilute limit $f\ll1$, both reduce to the Maxwell--Boltzmann entropy per mode to leading order. These formulas concern the equilibrium ensemble over occupation numbers, not entanglement entropy between arbitrary spatial regions.

In the thermodynamic limit, sums over levels become integrals only when level spacing is small compared with thermal scales. Ground states, gaps, and low-dimensional densities of states must be handled separately.

Spin degeneracy is another common source of factors. A spin-$1/2$ gas with no magnetic splitting has two states for each momentum, while polarized gases or particles with internal hyperfine structure require different degeneracy counts. These factors multiply density of states and therefore shift $\mu$, $p$, and $N$ even when the occupation formula itself is unchanged.

For finite systems, discrete levels can dominate. A cold trapped gas, a quantum dot, or a small cavity may not be well approximated by a continuum density of states. In those cases the product over levels should be kept explicitly, and thermodynamic-limit intuition must be applied with care.

The semiclassical replacement of sums by phase-space integrals has its own condition: the potential and thermal occupation should vary slowly on the scale of a wavelength. In a trap one often writes a local energy $p^2/(2m)+U(\mathbf r)$ and integrates over both position and momentum. This local-density approximation fails near abrupt boundaries or when only a few trap levels are populated.

Particle number conservation differs between material gases and quasiparticles. Atoms and electrons ordinarily have a chemical potential fixed by their conserved number. Photons and phonons can be created or destroyed in thermal equilibrium, so their equilibrium chemical potential is zero unless an external constraint maintains their number. The Bose occupation formula is the same, but the reservoir condition determining $\mu$ is different.

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

Checked answer: the value is not small, so quantum statistics is essential near a few kelvin. Liquid helium is also strongly interacting, so the ideal-gas model diagnoses degeneracy but does not give its full thermodynamics.

## Worked example 3: first exchange correction

Take a one-component gas with $n\lambda_T^3=0.10$. The leading virial correction gives

$$
{p\over nk_BT}=1\pm{0.10\over2^{5/2}}.
$$

Since $2^{5/2}=\sqrt{32}\approx5.657$,

$$
{0.10\over2^{5/2}}\approx0.0177.
$$

Therefore

$$
{p_F\over nk_BT}\approx1.0177,
\qquad
{p_B\over nk_BT}\approx0.9823.
$$

At equal density and temperature, exchange raises the ideal Fermi pressure and lowers the ideal Bose pressure relative to Maxwell--Boltzmann statistics. The calculation is controlled only while the degeneracy parameter is small enough that higher fugacity terms remain negligible.

## Checks before taking a continuum limit

- Identical particles cannot be assigned persistent classical labels. Occupation states already contain the required symmetrization or antisymmetrization.
- The Bose chemical potential must lie below the lowest single-particle energy in the normal phase. Equality is approached at condensation.
- Maxwell--Boltzmann behavior requires small phase-space density. High temperature and low density are two routes to $n\lambda_T^3\ll1$.
- A mean level occupation is not the probability that the entire many-body system contains one particle. Many levels fluctuate simultaneously in the grand ensemble.
- Replacing a sum by an integral can erase a macroscopically occupied ground state or discrete finite-size structure.
- Spin degeneracy changes the density per momentum state. A quoted degeneracy parameter should specify whether $n$ is total density and which $g$ is used.

<div className="see-also">

See also: [Grand canonical ensemble and particle exchange](/physics/statistical-mechanics/grand-canonical-ensemble-and-particle-exchange) · [Degenerate Fermi gas](/physics/statistical-mechanics/degenerate-fermi-gas) · [Bose gases, photons, and phonons](/physics/statistical-mechanics/bose-gases-photons-and-phonons) · [Identical particles and symmetrization](/physics/quantum-mechanics/identical-particles-symmetrization) · [Quantum field theory motivation](/physics/quantum-field-theory/motivation-fields-and-quanta)

</div>
