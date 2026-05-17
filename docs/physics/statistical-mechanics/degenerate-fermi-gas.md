---
title: Degenerate Fermi Gas
sidebar_position: 9
---

# Degenerate Fermi Gas

A degenerate Fermi gas is a many-fermion system whose low-temperature behavior is dominated by the Pauli principle rather than by thermal energy. At $T=0$, all one-particle states are filled up to the Fermi energy. At small nonzero temperature, only particles within about $k_BT$ of the Fermi surface can be thermally rearranged.

Schwabl uses this model for electrons in metals and for compact astrophysical matter. The same mathematics explains why the electronic heat capacity of a metal is much smaller than the classical equipartition estimate and why degeneracy pressure can support white dwarfs against gravity.

## Definitions

For spin-$1/2$ fermions in a three-dimensional box, the occupation at $T=0$ is

$$
f(\epsilon)=
\begin{cases}
1, & \epsilon<\epsilon_F,\\
0, & \epsilon>\epsilon_F.
\end{cases}
$$

The Fermi momentum $p_F$ is defined by filling all momentum states inside a sphere:

$$
N=g{V\over h^3}{4\pi p_F^3\over 3},
$$

where $g=2$ for spin-$1/2$ particles without additional degeneracy. Thus

$$
p_F=\hbar(3\pi^2 n)^{1/3},
\qquad n={N\over V}.
$$

The nonrelativistic Fermi energy and Fermi temperature are

$$
\epsilon_F={p_F^2\over 2m},
\qquad
T_F={\epsilon_F\over k_B}.
$$

The density of one-particle states per energy is

$$
D(\epsilon)=
gV {2\pi(2m)^{3/2}\over h^3}\epsilon^{1/2}.
$$

## Key results

At zero temperature,

$$
E_0=\int_0^{\epsilon_F}\epsilon D(\epsilon)\,d\epsilon
={3\over 5}N\epsilon_F.
$$

The pressure is

$$
p=-\left({\partial E_0\over \partial V}\right)_N
={2\over 5}n\epsilon_F.
$$

This is degeneracy pressure. It exists at $T=0$ and is not caused by thermal motion in the classical sense; it is caused by the kinetic energy forced by antisymmetry.

For low but nonzero temperature, the Sommerfeld expansion states that for smooth $\phi(\epsilon)$,

$$
\int_0^\infty \phi(\epsilon)f_{\mathrm{FD}}(\epsilon)\,d\epsilon
=
\int_0^\mu \phi(\epsilon)\,d\epsilon
{\,+\,}{\pi^2\over 6}(k_BT)^2\phi'(\mu)
+O(T^4).
$$

For fixed $N$, the chemical potential is

$$
\mu(T)=\epsilon_F\left[
1-{\pi^2\over 12}\left({k_BT\over \epsilon_F}\right)^2+\cdots
\right].
$$

The electronic heat capacity is linear in $T$:

$$
C_V={\pi^2\over 2}Nk_B {T\over T_F}
$$

for a three-dimensional nonrelativistic ideal Fermi gas. This replaces the classical value $(3/2)Nk_B$ and is small when $T\ll T_F$.

The physical picture behind the Sommerfeld expansion is phase-space blocking. Deep below $\epsilon_F$, states are already occupied and cannot accept another fermion. Far above $\epsilon_F$, states are empty but thermally inaccessible. Only a shell of width about $k_BT$ around the Fermi surface changes its occupation. The fraction of active particles is therefore of order $T/T_F$, which explains the small heat capacity before any calculation is done.

The same shell structure controls magnetic response. In Pauli paramagnetism, a weak magnetic field shifts spin-up and spin-down Fermi surfaces relative to each other. Only electrons near the Fermi surface can change spin occupation, so the susceptibility is temperature independent to leading order and proportional to the density of states at $\epsilon_F$, not to $1/T$ as in Curie paramagnetism.

White-dwarf applications require a further step: at high density, electrons become relativistic. The nonrelativistic degeneracy pressure scales as $n^{5/3}$, while the ultrarelativistic pressure scales as $n^{4/3}$. This change in exponent is central to the existence of the Chandrasekhar limiting mass. The detailed stellar calculation includes gravity and charge neutrality, but the statistical-mechanical origin is already present in the ideal Fermi gas: filling momentum states costs kinetic energy even at zero temperature.

One must also distinguish the chemical potential from the Fermi energy at nonzero temperature. At $T=0$, $\mu=\epsilon_F$. At low temperature, $\mu$ decreases slightly in three dimensions for a fixed density. In many metal problems this correction is tiny because $T/T_F$ is small, but it matters in precise Sommerfeld expansions.

The density of states determines many low-temperature coefficients. In three dimensions, $D(\epsilon)\propto \sqrt{\epsilon}$, so the number of available states near the Fermi surface grows slowly with energy. In two dimensions, $D(\epsilon)$ is constant for a parabolic band, which changes some thermodynamic prefactors while preserving the idea that only a thermal shell is active. In one dimension, singular density-of-states features make fluctuations and interactions more important.

The ideal Fermi gas should not be confused with a free-electron model of every metal property. Lattices replace $p^2/(2m)$ by band dispersions, and interactions renormalize quasiparticle parameters. Nevertheless, Landau's Fermi-liquid picture keeps the Fermi surface and the low-temperature shell argument, which is why the ideal gas remains the conceptual starting point.

Pressure formulas should be derived with the constraint fixed. At $T=0$, the energy depends on volume through $n=N/V$, so differentiating $E_0=(3/5)N\epsilon_F(n)$ at fixed $N$ gives the degeneracy pressure. Differentiating at fixed density would miss the mechanical response. This is a common error because $\epsilon_F$ is often written as if it were an independent constant.

Relativistic corrections are not small in compact stars, where the Fermi momentum can approach or exceed $mc$. In that regime one must replace $\epsilon=p^2/(2m)$ by the relativistic dispersion. The occupation principle is unchanged; the energy-momentum relation changes the equation of state.

The Fermi surface is therefore more fundamental than the Fermi sphere. In anisotropic crystals the surface need not be spherical, but low-temperature response is still controlled by states close to it. The ideal gas gives the spherical benchmark against which band-structure and interaction effects are measured.

This surface viewpoint also explains why scattering near the Fermi level controls transport. Filled final states are blocked, so only excitations with available states near $\epsilon_F$ contribute efficiently to electrical and thermal currents. Degeneracy changes not only equilibrium thermodynamics but also kinetic behavior.

## Visual

```text
T = 0 occupation
f
1 |###############|
  |###############|
0 +---------------+----------------> epsilon
                  epsilon_F

T > 0 occupation
f
1 |############...
  |#########....
0 +----------~~~~~---------------> epsilon
           width ~ k_B T
```

| Quantity | Formula | Scaling with density |
|---|---:|---|
| Fermi momentum | $p_F=\hbar(3\pi^2 n)^{1/3}$ | $n^{1/3}$ |
| Fermi energy | $\epsilon_F=p_F^2/(2m)$ | $n^{2/3}$ |
| Ground energy | $E_0=3N\epsilon_F/5$ | $Nn^{2/3}$ |
| Degeneracy pressure | $p=2n\epsilon_F/5$ | $n^{5/3}$ |
| Low-$T$ heat capacity | $C_V=(\pi^2/2)Nk_BT/\epsilon_F$ | $Tn^{-2/3}$ per particle |

## Worked example 1: Fermi energy of conduction electrons

Problem: Estimate the Fermi energy for an electron gas with $n=8.5\times 10^{28}\,\mathrm{m^{-3}}$.

Method:

1. Use

$$
\epsilon_F={\hbar^2\over 2m_e}(3\pi^2n)^{2/3}.
$$

2. Compute the density factor:

$$
3\pi^2n\approx 3(9.8696)(8.5\times 10^{28})
\approx 2.52\times 10^{30}.
$$

3. Raise to the $2/3$ power:

$$
(2.52\times 10^{30})^{2/3}
\approx 1.85\times 10^{20}\,\mathrm{m^{-2}}.
$$

4. Insert $\hbar=1.054\times 10^{-34}\,\mathrm{J\,s}$ and $m_e=9.11\times 10^{-31}\,\mathrm{kg}$:

$$
\epsilon_F
\approx {1.11\times 10^{-68}\over 1.822\times 10^{-30}}
(1.85\times 10^{20})
\approx 1.13\times 10^{-18}\,\mathrm J.
$$

5. Convert to electronvolts:

$$
\epsilon_F\approx {1.13\times 10^{-18}\over 1.602\times 10^{-19}}
\approx 7.1\,\mathrm{eV}.
$$

Checked answer: this is a typical metallic Fermi energy, corresponding to $T_F$ of order $10^5\,\mathrm K$.

## Worked example 2: Low-temperature electronic heat capacity

Problem: For the electron gas above, estimate $C_V/(Nk_B)$ at $T=300\,\mathrm K$ if $T_F=8.2\times 10^4\,\mathrm K$.

Method:

1. Use the Sommerfeld result:

$$
{C_V\over Nk_B}={\pi^2\over 2}{T\over T_F}.
$$

2. Insert numbers:

$$
{T\over T_F}={300\over 8.2\times 10^4}
\approx 3.66\times 10^{-3}.
$$

3. Multiply by $\pi^2/2\approx 4.935$:

$$
{C_V\over Nk_B}
\approx 4.935(3.66\times 10^{-3})
\approx 1.81\times 10^{-2}.
$$

Checked answer: only a few percent of $k_B$ per electron contributes at room temperature, far below the classical equipartition estimate.

## Code

```python
import numpy as np

hbar = 1.054_571_817e-34
me = 9.109_383_7015e-31
kB = 1.380_649e-23
eV = 1.602_176_634e-19

def fermi_energy(n, m=me):
    return hbar**2 * (3 * np.pi**2 * n)**(2 / 3) / (2 * m)

n = 8.5e28
EF = fermi_energy(n)
TF = EF / kB
print("EF eV", EF / eV)
print("TF K", TF)
for T in [10, 100, 300]:
    print(T, "Cv/NkB", 0.5 * np.pi**2 * T / TF)
```

## Common pitfalls

- Interpreting the Fermi energy as a thermal energy. It remains nonzero at $T=0$.
- Forgetting spin degeneracy when deriving $p_F$ from the momentum-space volume.
- Applying the Sommerfeld expansion when $T$ is not small compared with $T_F$.
- Assuming all electrons in a metal are thermally active. Only those near the Fermi surface respond strongly.
- Confusing degeneracy pressure with interaction pressure. The ideal Fermi gas has degeneracy pressure even without interactions.

## Connections

- [Quantum statistics and ideal quantum gases](/physics/statistical-mechanics/quantum-statistics-and-ideal-quantum-gases)
- [Grand canonical ensemble and particle exchange](/physics/statistical-mechanics/grand-canonical-ensemble-and-particle-exchange)
- [Bose gases, photons, and phonons](/physics/statistical-mechanics/bose-gases-photons-and-phonons)
- [Identical particles in quantum mechanics](/physics/quantum-mechanics/identical-particles-symmetrization)
- [Collective and condensed-matter field theory](/physics/quantum-field-theory/collective-and-condensed-matter-field-theory)
