---
title: Classical Ideal Gas and Maxwell Distribution
sidebar_position: 7
---

# Classical Ideal Gas and Maxwell Distribution

The classical ideal gas is the simplest nontrivial laboratory for statistical mechanics. It has no interactions except confinement by the walls, so the partition function factorizes into a position part and a momentum part. From that factorization come the ideal-gas law, the Maxwell-Boltzmann velocity distribution, equipartition, and the density-of-states formulas used repeatedly in more complicated systems.

Schwabl treats the ideal gas in both microcanonical and canonical language. The agreement between them is a concrete example of ensemble equivalence: the microcanonical shell count and the canonical Gaussian momentum integrals produce the same macroscopic thermodynamics when $N$ is large.

## Definitions

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

## Key results

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

The Maxwell distribution has several characteristic speeds:

$$
v_{\mathrm{mp}}=\sqrt{2k_BT\over m},
\qquad
\langle v\rangle=\sqrt{8k_BT\over \pi m},
\qquad
v_{\mathrm{rms}}=\sqrt{3k_BT\over m}.
$$

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

The barometric formula illustrates local equilibrium. Each height slice is assumed to have a Maxwellian velocity distribution at the same temperature, while density changes with potential energy. This separation between fast velocity equilibration and slow spatial variation reappears in the Boltzmann equation through the local Maxwell distribution.

The ideal gas also sets a baseline for interacting systems. Virial coefficients, transport coefficients, and phase-transition models are often stated as deviations from ideal behavior. When an equation of state is written as $pV=Nk_BT$ times a correction factor, the correction has meaning only because the ideal gas has already fixed the natural scale of pressure. Similarly, heat capacities of molecular gases are interpreted by asking which degrees of freedom have been added to the translational ideal-gas value.

Finally, the ideal gas is one of the best examples of ensemble equivalence. Microcanonical counting, canonical Gaussian integration, and grand-canonical Poisson statistics all produce the same thermodynamic equation of state in the macroscopic limit. Their fluctuations differ because their constraints differ, but the leading thermodynamic functions agree.

It is also a model of what interactions do not affect. In an ideal gas, the internal energy is independent of volume because there is no potential energy. Therefore a free expansion at fixed internal energy leaves the temperature unchanged for a classical monatomic ideal gas. Real gases do not obey this exactly because intermolecular attractions and repulsions make internal energy depend on density. The contrast is a useful diagnostic when studying Joule expansion and virial corrections.

The Maxwell distribution should be interpreted component by component and speed by speed. Each Cartesian component is Gaussian with variance $k_BT/m$, while the speed has a skewed distribution because many velocity vectors share the same magnitude.

## Visual

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

## Code

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

## Common pitfalls

- Forgetting the $4\pi v^2$ factor when moving from velocity density to speed density.
- Treating the Maxwell distribution as valid for dense or strongly interacting gases without corrections.
- Dropping $N!$ in $Z_N$ and producing nonextensive entropy.
- Applying classical equipartition to frozen rotational, vibrational, or electronic modes at low temperature.
- Confusing $\lambda_T$ with a literal molecular size. It is a quantum length scale controlling the validity of the classical approximation.

## Connections

- [Canonical ensemble and fluctuations](/physics/statistical-mechanics/canonical-ensemble-and-fluctuations)
- [Microcanonical ensemble and entropy](/physics/statistical-mechanics/microcanonical-ensemble-and-entropy)
- [Molecular gases, mixtures, and solutions](/physics/statistical-mechanics/molecular-gases-mixtures-and-solutions)
- [Boltzmann equation and transport](/physics/statistical-mechanics/boltzmann-equation-and-transport)
- [Thermodynamics](/physics/thermodynamics/)
