---
title: Degenerate Fermi Gas
sidebar_position: 9
---

# Degenerate Fermi Gas

A degenerate Fermi gas is a many-fermion system whose low-temperature behavior is dominated by the Pauli principle rather than by thermal energy. At $T=0$, all one-particle states are filled up to the Fermi energy. At small nonzero temperature, only particles within about $k_BT$ of the Fermi surface can be thermally rearranged.

Schwabl uses this model for electrons in metals and for compact astrophysical matter. The same mathematics explains why the electronic heat capacity of a metal is much smaller than the classical equipartition estimate and why degeneracy pressure can support white dwarfs against gravity.

## Filling momentum space at zero temperature

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

The counting can be done either with cells of volume $h^3$ in $\mathbf p$ space or $(2\pi)^3$ in $\mathbf k$ space. With periodic boundary conditions, one state per spin occupies $(2\pi/L)^3$ in $\mathbf k$ space. Hence

$$
N=g{V\over(2\pi)^3}{4\pi k_F^3\over3},
$$

which gives $k_F=(3\pi^2n)^{1/3}$ for $g=2$ and $p_F=\hbar k_F$. Differentiating the integrated state count

$$
\mathcal N(\epsilon)
={gV\over6\pi^2}\left({2m\epsilon\over\hbar^2}\right)^{3/2}
$$

produces $D(\epsilon)$. These formulas count one-particle orbitals; the many-body ground state is the Slater determinant in which all orbitals below $\epsilon_F$ are occupied.

## Ground-state energy and degeneracy pressure

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

The factor $3/5$ follows directly from the power-law density of states:

$$
{E_0\over N}
={\int_0^{\epsilon_F}\epsilon^{3/2}\,d\epsilon
\over\int_0^{\epsilon_F}\epsilon^{1/2}\,d\epsilon}
={3\over5}\epsilon_F.
$$

Since $\epsilon_F\propto(N/V)^{2/3}$, the total energy scales as $E_0\propto N^{5/3}V^{-2/3}$. Differentiating at fixed $N$ gives $p=(2/3)E_0/V$, the same relation between pressure and kinetic-energy density as for any nonrelativistic gas with quadratic dispersion. Here the energy scale is set by density rather than temperature.

## The narrow thermal shell

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

To see where the shift in $\mu$ comes from, apply the Sommerfeld formula to the number equation:

$$
N=\int_0^\infty D(\epsilon)f_{\mathrm{FD}}(\epsilon)\,d\epsilon.
$$

With $D(\epsilon)=A\sqrt\epsilon$,

$$
N=A\left[{2\over3}\mu^{3/2}
+{\pi^2\over12}(k_BT)^2\mu^{-1/2}+\cdots\right].
$$

At zero temperature $N=(2A/3)\epsilon_F^{3/2}$. Write $\mu=\epsilon_F(1+\delta)$ and retain terms through $T^2$. The number constraint gives

$$
\delta=-{\pi^2\over12}\left({k_BT\over\epsilon_F}\right)^2.
$$

Applying the expansion again with $\phi(\epsilon)=\epsilon D(\epsilon)$ and inserting this shift yields

$$
E(T)=E_0+{\pi^2\over4}N{(k_BT)^2\over\epsilon_F}+O(T^4).
$$

Differentiation gives the linear heat capacity. Holding $\mu$ fixed during this calculation would give a different coefficient because particles could enter or leave; the fixed-$N$ correction is essential.

The physical picture behind the Sommerfeld expansion is phase-space blocking. Deep below $\epsilon_F$, states are already occupied and cannot accept another fermion. Far above $\epsilon_F$, states are empty but thermally inaccessible. Only a shell of width about $k_BT$ around the Fermi surface changes its occupation. The fraction of active particles is therefore of order $T/T_F$, which explains the small heat capacity before any calculation is done.

The same shell structure controls magnetic response. In Pauli paramagnetism, a weak magnetic field shifts spin-up and spin-down Fermi surfaces relative to each other. Only electrons near the Fermi surface can change spin occupation, so the susceptibility is temperature independent to leading order and proportional to the density of states at $\epsilon_F$, not to $1/T$ as in Curie paramagnetism.

At $T=0$, a weak field lowers one spin energy by $\mu_BB$ and raises the other by the same amount. To first order, the population difference is the number of states in an energy slice of width $2\mu_BB$ at the Fermi surface:

$$
N_\uparrow-N_\downarrow\simeq D(\epsilon_F)\mu_BB,
$$

where $D$ includes both spin directions. The magnetization is therefore

$$
M={\mu_B(N_\uparrow-N_\downarrow)\over V},
\qquad
\chi_P=\mu_0\mu_B^2{D(\epsilon_F)\over V}
$$

in SI units. The result depends only on states at the boundary of the filled sea. Orbital Landau diamagnetism and band effects must be included when comparing with a real metal.

White-dwarf applications require a further step: at high density, electrons become relativistic. The nonrelativistic degeneracy pressure scales as $n^{5/3}$, while the ultrarelativistic pressure scales as $n^{4/3}$. This change in exponent is central to the existence of the Chandrasekhar limiting mass. The detailed stellar calculation includes gravity and charge neutrality, but the statistical-mechanical origin is already present in the ideal Fermi gas: filling momentum states costs kinetic energy even at zero temperature.

One must also distinguish the chemical potential from the Fermi energy at nonzero temperature. At $T=0$, $\mu=\epsilon_F$. At low temperature, $\mu$ decreases slightly in three dimensions for a fixed density. In many metal problems this correction is tiny because $T/T_F$ is small, but it matters in precise Sommerfeld expansions.

## What survives beyond the spherical free-electron model

The density of states determines many low-temperature coefficients. In three dimensions, $D(\epsilon)\propto \sqrt{\epsilon}$, so the number of available states near the Fermi surface grows slowly with energy. In two dimensions, $D(\epsilon)$ is constant for a parabolic band, which changes some thermodynamic prefactors while preserving the idea that only a thermal shell is active. In one dimension, singular density-of-states features make fluctuations and interactions more important.

The ideal Fermi gas should not be confused with a free-electron model of every metal property. Lattices replace $p^2/(2m)$ by band dispersions, and interactions renormalize quasiparticle parameters. Nevertheless, Landau's Fermi-liquid picture keeps the Fermi surface and the low-temperature shell argument, which is why the ideal gas remains the conceptual starting point.

Pressure formulas should be derived with the constraint fixed. At $T=0$, the energy depends on volume through $n=N/V$, so differentiating $E_0=(3/5)N\epsilon_F(n)$ at fixed $N$ gives the degeneracy pressure. Differentiating at fixed density would miss the mechanical response. This is a common error because $\epsilon_F$ is often written as if it were an independent constant.

The same density dependence fixes the compressibility. For $p=An^{5/3}$,

$$
{\partial p\over\partial n}={5\over3}{p\over n}
={2\over3}\epsilon_F.
$$

The zero-temperature isothermal compressibility is therefore

$$
\kappa_T={1\over n}\left({\partial n\over\partial p}\right)
={3\over2n\epsilon_F}.
$$

It is finite even without interactions because compressing the gas forces particles into higher momentum states. For particles of mass $m$, the corresponding hydrodynamic sound scale satisfies

$$
c^2={1\over m}{\partial p\over\partial n}
={v_F^2\over3},
\qquad v_F={p_F\over m}.
$$

Whether an actual collisionless Fermi system supports ordinary hydrodynamic sound depends on its collision rate and interactions, but the derivative still measures the stiffness of the equation of state.

Relativistic corrections are not small in compact stars, where the Fermi momentum can approach or exceed $mc$. In that regime one must replace $\epsilon=p^2/(2m)$ by the relativistic dispersion. The occupation principle is unchanged; the energy-momentum relation changes the equation of state.

The Fermi surface is therefore more fundamental than the Fermi sphere. In anisotropic crystals the surface need not be spherical, but low-temperature response is still controlled by states close to it. The ideal gas gives the spherical benchmark against which band-structure and interaction effects are measured.

For a general band dispersion, the Fermi velocity is the gradient $\mathbf v_F=\hbar^{-1}\nabla_{\mathbf k}\epsilon(\mathbf k)$ evaluated on that surface. Heat capacity weights the density of states, while transport also weights velocity components and scattering lifetimes. Two metals can therefore have similar carrier density but quite different conductivity or electronic heat capacity. Replacing the bare mass by one fitted effective mass captures only the simplest nearly parabolic case.

This surface viewpoint also explains why scattering near the Fermi level controls transport. Filled final states are blocked, so only excitations with available states near $\epsilon_F$ contribute efficiently to electrical and thermal currents. Degeneracy changes not only equilibrium thermodynamics but also kinetic behavior.

The zero-temperature step is an ideal limit. Disorder and finite quasiparticle lifetime can broaden spectral features even when thermal broadening is negligible, while interactions can reduce the discontinuity in the momentum distribution below one. A Fermi liquid still has a sharply defined Fermi surface in the appropriate sense; the occupation need not remain the exact free-gas step.

When quoting a Fermi temperature, the mass and degeneracy convention belong with it. Semiconductor carriers may have an effective mass far from the electron mass, and valleys provide additional degeneracy. The density alone is therefore insufficient to compare degeneracy scales across materials.

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

## Relativistic change of the equation of state

For an arbitrary isotropic dispersion $\epsilon(p)$ at zero temperature, the occupation is still a filled momentum sphere. What changes is the energy assigned to each shell. In the ultrarelativistic limit, kinetic energy is approximately $pc$, so $E/V\propto p_F^4/\hbar^3\propto n^{4/3}$. The pressure becomes

$$
p={1\over3}{E\over V}
={1\over4}n p_Fc,
$$

whereas the nonrelativistic relation is $p=(2/3)E/V=(2/5)n\epsilon_F$. The softer density exponent $4/3$ is the feature needed in the white-dwarf argument; quoting a limiting stellar mass requires the gravitational calculation and composition, not merely this gas formula.

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

## Worked example 3: zero-temperature pressure of a metal-density gas

Use the density and Fermi energy from the first example: $n=8.5\times10^{28}\,\mathrm{m^{-3}}$ and $\epsilon_F=1.13\times10^{-18}\,\mathrm J$. The nonrelativistic degeneracy pressure is

$$
p={2\over5}n\epsilon_F.
$$

Substitution gives

$$
\begin{aligned}
p&={2\over5}(8.5\times10^{28})(1.13\times10^{-18})\\
&={2\over5}(9.605\times10^{10})\,\mathrm{Pa}\\
&\approx3.84\times10^{10}\,\mathrm{Pa}.
\end{aligned}
$$

This is about $3.8\times10^5$ atmospheres. It does not mean an ordinary metal explodes: positive ionic charge, Coulomb binding, and the lattice supply the other parts of the mechanical equilibrium. The calculation isolates the kinetic contribution of the conduction-electron model.

As a consistency check, use the energy density $u=E_0/V=(3/5)n\epsilon_F$:

$$
{2\over3}u
={2\over3}{3\over5}n\epsilon_F
={2\over5}n\epsilon_F=p.
$$

The same numerical pressure follows. At fixed particle number, lowering the density by a factor of eight lowers $p$ by $8^{5/3}=32$, illustrating the steep nonrelativistic density dependence.

## Excitations are particles and holes

Heating does not lift the entire Fermi sea. It creates particle--hole pairs: an occupied state just below $\mu$ becomes a hole, and a state just above $\mu$ becomes occupied. Both objects carry energy measured relative to the chemical potential. The total particle number can remain fixed while the number of excitations grows with temperature.

This language helps with transport. An applied field changes the distribution only near the Fermi surface, and collisions must find unoccupied final states. At low temperature Pauli blocking restricts the available final-state phase space. The ideal equilibrium gas does not predict a resistivity by itself, but it identifies which electrons can participate once impurity, phonon, or electron--electron scattering is added.

## Numerical scale for conduction electrons

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

## Checks before using the formulas

- The Fermi energy is fixed primarily by density and remains nonzero at $T=0$; it is not thermal energy.
- Spin or other internal degeneracy changes the relation between density and $p_F$. The value $3\pi^2n$ assumes $g=2$.
- The Sommerfeld expansion is asymptotic for $T/T_F\ll1$. Near the classical crossover, the full Fermi--Dirac integrals are required.
- Most electrons lie deep in the sea and cannot be thermally rearranged. Counting all $N$ as active gives the wrong heat capacity and susceptibility.
- Degeneracy pressure needs no interparticle force. Coulomb and lattice effects in real matter add corrections rather than creating the ideal-gas pressure.
- At nonzero temperature, distinguish $\mu(T)$ from the zero-temperature $\epsilon_F$ and state whether density or chemical potential is held fixed.

## Related pages

- [Quantum statistics and ideal quantum gases](/physics/statistical-mechanics/quantum-statistics-and-ideal-quantum-gases)
- [Grand canonical ensemble and particle exchange](/physics/statistical-mechanics/grand-canonical-ensemble-and-particle-exchange)
- [Bose gases, photons, and phonons](/physics/statistical-mechanics/bose-gases-photons-and-phonons)
- [Identical particles in quantum mechanics](/physics/quantum-mechanics/identical-particles-symmetrization)
- [Collective and condensed-matter field theory](/physics/quantum-field-theory/collective-and-condensed-matter-field-theory)
