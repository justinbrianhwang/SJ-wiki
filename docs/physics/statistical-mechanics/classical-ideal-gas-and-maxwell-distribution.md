---
title: Classical Ideal Gas and Maxwell Distribution
sidebar_position: 7
---

# Classical Ideal Gas and Maxwell Distribution

The classical ideal gas is the simplest nontrivial laboratory for statistical mechanics. It has no interactions except confinement by the walls, so the partition function factorizes into a position part and a momentum part. From that factorization come the ideal-gas law, the Maxwell-Boltzmann velocity distribution, equipartition, and the density-of-states formulas used repeatedly in more complicated systems.

Schwabl treats the ideal gas in both microcanonical and canonical language. The agreement between them is a concrete example of ensemble equivalence: the microcanonical shell count and the canonical Gaussian momentum integrals produce the same macroscopic thermodynamics when $N$ is large.

## Factorizing the classical partition function

For $N$ identical classical particles of mass $m$ in volume $V$,

$$
H=\sum_{i=1}^{N}{p_i^2\over 2m}.
$$

The canonical partition function is

$$
Z_N={1\over N!h^{3N}}\int d^{3N}q\,d^{3N}p\,
e^{-\beta\sum_i p_i^2/(2m)}.
$$

The thermal de Broglie wavelength is

$$
\lambda_T={h\over \sqrt{2\pi m k_BT}}.
$$

The ideal-gas partition function is

$$
Z_N={1\over N!}\left({V\over \lambda_T^3}\right)^N.
$$

For a single particle, the velocity probability density is

$$
f(\mathbf v)=
\left({m\over 2\pi k_BT}\right)^{3/2}
\exp\left(-{m v^2\over 2k_BT}\right).
$$

The speed distribution, including the spherical velocity-space measure, is

$$
P(v)=4\pi v^2
\left({m\over 2\pi k_BT}\right)^{3/2}
\exp\left(-{m v^2\over 2k_BT}\right),
\qquad v\ge 0.
$$

The factor $V^N$ comes from integrating each position uniformly over the container. The momentum integral factors into $3N$ Gaussian integrals. Indistinguishability contributes $1/N!$, and the phase-space cell $h^{3N}$ makes the result dimensionless. The compact result

$$
Z_N={Z_1^N\over N!},
\qquad
Z_1={V\over\lambda_T^3},
$$

therefore combines free translation, Gaussian kinetic energy, and corrected counting of identical particles. Interactions would couple the position integrals; quantum degeneracy would invalidate the classical state counting.

## Thermodynamics from $Z_N$

The free energy follows from $F=-k_BT\ln Z_N$. Using Stirling's approximation,

$$
\ln N!\approx N\ln N-N,
$$

one obtains

$$
F=-Nk_BT\left[
\ln\left({V\over N\lambda_T^3}\right)+1
\right].
$$

Pressure and entropy are then

$$
p=-\left({\partial F\over \partial V}\right)_{T,N}
={Nk_BT\over V},
$$

and

$$
S=-\left({\partial F\over \partial T}\right)_{V,N}
=Nk_B\left[
\ln\left({V\over N\lambda_T^3}\right)+{5\over 2}
\right].
$$

The internal energy is

$$
E=-{\partial\over \partial\beta}\ln Z_N
={3\over 2}Nk_BT,
$$

and the heat capacity at constant volume is

$$
C_V={3\over 2}Nk_B.
$$

Equipartition explains this result: every quadratic term in the Hamiltonian contributes $(1/2)k_BT$ to the mean energy. Each particle has three quadratic momentum components, hence $(3/2)k_BT$ per particle.

The entropy formula above is the Sackur--Tetrode expression in the large-$N$ limit. It is extensive because $V/(N\lambda_T^3)$ depends on density rather than total volume. Without $N!$, the logarithm would contain $V/\lambda_T^3$ and mixing two samples of the same gas would spuriously increase the entropy. Stirling's omitted logarithmic corrections matter for very small $N$ but vanish relative to $N$ in the thermodynamic limit.

There is also a mechanical route to the equation of state. A molecule with normal velocity component $v_x$ transfers momentum $2mv_x$ upon an elastic collision with a wall. Counting collisions and averaging over an isotropic distribution gives

$$
p={1\over3}nm\langle v^2\rangle,
$$

where $n=N/V$. Maxwell's distribution has $m\langle v^2\rangle=3k_BT$, hence $p=nk_BT$. The factor $1/3$ is geometric: the mean squared velocity is shared equally among the three Cartesian directions.

## The Maxwell distribution and its moments

The Maxwell distribution has several characteristic speeds:

$$
v_{\mathrm{mp}}=\sqrt{2k_BT\over m},
\qquad
\langle v\rangle=\sqrt{8k_BT\over \pi m},
\qquad
v_{\mathrm{rms}}=\sqrt{3k_BT\over m}.
$$

All speed moments can be evaluated at once. With $a=m/(2k_BT)$,

$$
\langle v^r\rangle
=4\pi\left({a\over\pi}\right)^{3/2}
\int_0^\infty v^{r+2}e^{-av^2}\,dv.
$$

Using the gamma-function integral gives

$$
\langle v^r\rangle
={2\over\sqrt\pi}
\Gamma\left({r+3\over2}\right)
\left({2k_BT\over m}\right)^{r/2}.
$$

Setting $r=1$ and $2$ yields the mean and RMS speeds. Maximizing $P(v)$ gives the most probable speed: differentiating $\ln P=2\ln v-av^2+\text{constant}$ gives $2/v-2av=0$, or $v^2=1/a$. The three characteristic speeds answer different statistical questions and should not be interchanged.

The distribution of kinetic energy $\varepsilon=mv^2/2$ follows by changing variables, $P_\varepsilon(\varepsilon)d\varepsilon=P(v)dv$:

$$
P_\varepsilon(\varepsilon)
={2\over\sqrt\pi}{\sqrt\varepsilon\over(k_BT)^{3/2}}
e^{-\varepsilon/(k_BT)},
\qquad \varepsilon\ge0.
$$

Its square-root factor is the three-dimensional one-particle density of states. The Boltzmann exponential alone is therefore not the energy distribution.

In a gravitational field, canonical weighting gives the barometric formula

$$
n(z)=n(0)e^{-mgz/(k_BT)}.
$$

This is the same Boltzmann factor applied to potential energy rather than kinetic energy.

The density of states viewpoint gives the same physics from a different angle. For fixed $N$, the number of momentum states with total kinetic energy below $E$ is proportional to the volume of a $3N$-dimensional sphere of radius $\sqrt{2mE}$:

$$
\Gamma(E)\propto V^N E^{3N/2}.
$$

Taking a logarithm and differentiating gives

$$
{1\over T}={\partial S\over \partial E}
\approx k_B{3N\over 2E},
$$

so $E=(3/2)Nk_BT$. This microcanonical derivation makes clear that the ideal-gas temperature is a measure of kinetic energy per quadratic degree of freedom, not a separate microscopic force.

The Maxwell distribution is also a useful warning about measures. The vector velocity density is largest at $\mathbf v=0$, but the speed distribution is zero at $v=0$ because there is very little velocity-space volume near exactly zero speed. The most probable speed comes from maximizing $v^2e^{-mv^2/(2k_BT)}$, not from maximizing the Gaussian factor alone.

Classical validity requires more than weak interactions. The gas must also be nondegenerate:

$$
n\lambda_T^3\ll 1.
$$

When this fails, the $N!$ correction is not enough; Bose or Fermi occupation restrictions change the thermodynamics. Conversely, a very dilute gas with complicated molecules can still be nonideal in heat capacity because internal rotational and vibrational modes contribute to $z_{\mathrm{int}}$.

## Gravity, effusion, and local equilibrium

The barometric formula illustrates local equilibrium. Each height slice is assumed to have a Maxwellian velocity distribution at the same temperature, while density changes with potential energy. This separation between fast velocity equilibration and slow spatial variation reappears in the Boltzmann equation through the local Maxwell distribution.

A related measurement samples a different distribution. Molecules escaping through a small hole are weighted by their speed toward the hole, because faster molecules strike it more often. An effusive beam therefore has a flux distribution proportional to $vP(v)$ rather than $P(v)$. Using an ordinary Maxwell speed distribution for such a beam underestimates its mean kinetic energy. The gas inside the vessel remains Maxwellian if the aperture is small enough that escape does not appreciably disturb equilibrium.

For gravity, hydrostatic balance supplies an independent derivation. With mass density $mn(z)$,

$$
{dp\over dz}=-mgn,
\qquad p=nk_BT.
$$

At constant temperature this becomes $d\ln n/dz=-mg/(k_BT)$ and integrates to the barometric law. If temperature varies with height, the simple exponential no longer follows; both $n(z)$ and $T(z)$ enter the pressure gradient.

## Counting states and the classical limit

The ideal gas also sets a baseline for interacting systems. Virial coefficients, transport coefficients, and phase-transition models are often stated as deviations from ideal behavior. When an equation of state is written as $pV=Nk_BT$ times a correction factor, the correction has meaning only because the ideal gas has already fixed the natural scale of pressure. Similarly, heat capacities of molecular gases are interpreted by asking which degrees of freedom have been added to the translational ideal-gas value.

The chemical potential follows by differentiating the free energy at fixed $T,V$:

$$
\mu=\left({\partial F\over\partial N}\right)_{T,V}
=k_BT\ln(n\lambda_T^3)
$$

in the classical large-$N$ limit. Since $n\lambda_T^3\ll1$, the ideal-gas chemical potential is negative relative to the chosen zero of single-particle energy. Adding a particle is entropically favorable because many translational states are available. Equality of chemical potentials, rather than equality of densities, controls diffusive equilibrium between regions or species.

For two different ideal gases, removing a partition increases entropy because each species gains accessible volume. If the species are identical, the $N!$ counting cancels that apparent gain. The distinction is physical: a semipermeable membrane can sort distinct species but cannot sort molecules that differ only by an arbitrary label.

Finally, the ideal gas is one of the best examples of ensemble equivalence. Microcanonical counting, canonical Gaussian integration, and grand-canonical Poisson statistics all produce the same thermodynamic equation of state in the macroscopic limit. Their fluctuations differ because their constraints differ, but the leading thermodynamic functions agree.

It is also a model of what interactions do not affect. In an ideal gas, the internal energy is independent of volume because there is no potential energy. Therefore a free expansion at fixed internal energy leaves the temperature unchanged for a classical monatomic ideal gas. Real gases do not obey this exactly because intermolecular attractions and repulsions make internal energy depend on density. The contrast is a useful diagnostic when studying Joule expansion and virial corrections.

For a quasistatic adiabatic change, the first law gives $dE=-p\,dV$. With $E=C_VT$ and $p=Nk_BT/V$,

$$
C_V{dT\over T}=-Nk_B{dV\over V}.
$$

For a monatomic gas $C_V=3Nk_B/2$, so integration gives $TV^{2/3}=\text{constant}$. Since $pV=Nk_BT$, this is equivalent to

$$
pV^{5/3}=\text{constant}.
$$

More generally $pV^\gamma$ is constant with $\gamma=C_P/C_V$, provided the heat capacities are effectively constant over the temperature range. For a monatomic ideal gas, $C_P=C_V+Nk_B=5Nk_B/2$ and $\gamma=5/3$. These relations concern a reversible adiabatic path; they do not describe a free expansion, which is irreversible even though no heat enters.

The same ratio controls the adiabatic sound speed,

$$
c_s=\sqrt{\gamma p\over\rho}
=\sqrt{\gamma k_BT\over m}.
$$

It is comparable to the thermal molecular speed but not equal to any one of $v_{\mathrm{mp}}$, $\langle v\rangle$, or $v_{\mathrm{rms}}$. Sound is a collective pressure disturbance whose coefficient depends on the thermodynamic constraint during compression.

The Maxwell distribution should be interpreted component by component and speed by speed. Each Cartesian component is Gaussian with variance $k_BT/m$, while the speed has a skewed distribution because many velocity vectors share the same magnitude.

The center-of-mass constraint supplies a small finite-system correction. If the total momentum is fixed at zero, only $3N-3$ independent quadratic momentum coordinates remain rather than $3N$. The mean kinetic energy is then $3(N-1)k_BT/2$. Ordinary canonical formulas allow the center of mass to move and recover $3Nk_BT/2$; the difference is negligible per particle at large $N$ but matters when comparing small simulations with different momentum constraints.

Mixtures retain a Maxwell distribution for each species at the common temperature. A heavier species has a narrower component distribution and smaller characteristic speed, since all species share mean translational energy rather than mean speed. Collisions exchange momentum and energy until the temperature agrees; they do not force molecular speeds to agree. This distinction is useful when interpreting diffusion, effusion, or time-of-flight measurements in mixed gases.

The ideal model assumes equilibrium, not merely the absence of interactions. A collisionless collection can keep a non-Maxwellian velocity distribution indefinitely. Even weak interactions are dynamically important because they redistribute energy among directions and species. Statistical equilibrium supplies the Maxwell form after thermalization; the ideal Hamiltonian then supplies the thermodynamics once that state has been reached.

| Result | Formula | Comment |
|---|---:|---|
| Partition function | $Z_N=(V/\lambda_T^3)^N/N!$ | classical, noninteracting, identical |
| Equation of state | $pV=Nk_BT$ | pressure from $F$ |
| Internal energy | $E=3Nk_BT/2$ | kinetic energy only |
| Heat capacity | $C_V=3Nk_B/2$ | temperature independent |
| Most probable speed | $\sqrt{2k_BT/m}$ | maximum of $P(v)$ |
| RMS speed | $\sqrt{3k_BT/m}$ | from $\langle v^2\rangle$ |

```text
P(v)
 ^
 |          .
 |        .   .
 |      .       .
 |    .           .
 |  .               .
 +----------------------> v
      v_mp    <v>   v_rms
```

## Worked example 1: Deriving the one-particle momentum integral

Problem: Evaluate the one-particle canonical momentum integral

$$
I_p=\int_{\mathbb R^3} d^3p\,e^{-\beta p^2/(2m)}.
$$

Method:

1. Factor the integral into Cartesian components:

$$
I_p=
\left(\int_{-\infty}^{\infty} dp_x\,e^{-\beta p_x^2/(2m)}\right)^3.
$$

2. Use the Gaussian integral

$$
\int_{-\infty}^{\infty} e^{-a x^2}\,dx=\sqrt{\pi\over a}.
$$

Here $a=\beta/(2m)$, so

$$
\int dp_x\,e^{-\beta p_x^2/(2m)}
=\sqrt{2\pi m\over \beta}.
$$

3. Cube the result:

$$
I_p=\left({2\pi m\over \beta}\right)^{3/2}
=(2\pi m k_BT)^{3/2}.
$$

4. Divide by $h^3$ and multiply by $V$:

$$
Z_1={V\over h^3}(2\pi m k_BT)^{3/2}
={V\over \lambda_T^3}.
$$

Checked answer: this is the single-particle factor whose $N$th power gives the ideal-gas partition function.

## Worked example 2: Characteristic speeds of nitrogen at room temperature

Problem: Estimate $v_{\mathrm{mp}}$, $\langle v\rangle$, and $v_{\mathrm{rms}}$ for nitrogen molecules at $T=300\,\mathrm K$. Take $m=4.65\times 10^{-26}\,\mathrm{kg}$.

Method:

1. Compute $k_BT$:

$$
k_BT=(1.380649\times 10^{-23})(300)
=4.141947\times 10^{-21}\,\mathrm J.
$$

2. Most probable speed:

$$
v_{\mathrm{mp}}
=\sqrt{2k_BT\over m}
=\sqrt{8.283894\times 10^{-21}\over 4.65\times 10^{-26}}
\approx 422\,\mathrm{m/s}.
$$

3. Mean speed:

$$
\langle v\rangle
=\sqrt{8k_BT\over \pi m}
=\sqrt{3.313558\times 10^{-20}\over 1.4608\times 10^{-25}}
\approx 476\,\mathrm{m/s}.
$$

4. RMS speed:

$$
v_{\mathrm{rms}}
=\sqrt{3k_BT\over m}
=\sqrt{1.242584\times 10^{-20}\over 4.65\times 10^{-26}}
\approx 517\,\mathrm{m/s}.
$$

Checked answer: the ordering $v_{\mathrm{mp}}\lt \langle v\rangle\lt v_{\mathrm{rms}}$ is required by the right-skewed speed distribution.

## Worked example 3: atmospheric scale height

For an isothermal dilute gas, define the scale height

$$
H={k_BT\over mg},
$$

so $n(z)=n(0)e^{-z/H}$. For nitrogen near $T=300\,\mathrm K$, using $m=4.65\times10^{-26}\,\mathrm{kg}$ and $g=9.81\,\mathrm{m/s^2}$ gives

$$
H={4.141947\times10^{-21}\,\mathrm J
\over(4.65\times10^{-26}\,\mathrm{kg})(9.81\,\mathrm{m/s^2})}
\approx9.08\times10^3\,\mathrm m.
$$

At one scale height, the density ratio is

$$
{n(H)\over n(0)}=e^{-1}\approx0.368.
$$

At $z=5.0\,\mathrm{km}$,

$$
{n(z)\over n(0)}
=\exp\left(-{5000\over9080}\right)
\approx0.576.
$$

The numerical value is only an isothermal estimate for the real atmosphere, where temperature, composition, and gravity vary. The calculation does show how molecular mass enters: at a common temperature, a heavier species has a smaller scale height and its concentration decreases more rapidly with altitude.

## Numerical check of the speed moments

```python
import numpy as np

kB = 1.380649e-23
T = 300.0
m = 4.65e-26

v = np.linspace(0.0, 1500.0, 5000)
P = 4 * np.pi * v**2 * (m / (2 * np.pi * kB * T))**1.5 * np.exp(-m * v**2 / (2 * kB * T))
dv = v[1] - v[0]

print("normalization", np.trapz(P, v))
print("mean speed", np.trapz(v * P, v))
print("rms speed", np.sqrt(np.trapz(v**2 * P, v)))
print("most probable grid speed", v[np.argmax(P)])
```

## Diagnostic checks

- The vector density $f(\mathbf v)$ and speed density $P(v)$ have different measures. The latter needs the spherical-shell factor $4\pi v^2$.
- Maxwell statistics assume a dilute, equilibrated classical gas. Dense fluids require correlations; degenerate gases require Bose or Fermi statistics.
- Omitting $N!$ produces a nonextensive entropy and an artificial entropy of mixing for identical gases.
- Translational equipartition can hold while rotational or vibrational modes remain quantum mechanically frozen. Molecular heat capacity must be assessed mode by mode.
- The thermal wavelength is a quantum overlap scale, not a molecular diameter. Interaction diluteness and quantum nondegeneracy are separate conditions.
- A velocity-selected or flux-selected sample is not distributed like molecules chosen uniformly from the volume. Effusion is the standard counterexample.

## Related pages

- [Canonical ensemble and fluctuations](/physics/statistical-mechanics/canonical-ensemble-and-fluctuations)
- [Microcanonical ensemble and entropy](/physics/statistical-mechanics/microcanonical-ensemble-and-entropy)
- [Molecular gases, mixtures, and solutions](/physics/statistical-mechanics/molecular-gases-mixtures-and-solutions)
- [Boltzmann equation and transport](/physics/statistical-mechanics/boltzmann-equation-and-transport)
- [Thermodynamics](/physics/thermodynamics/intro)
