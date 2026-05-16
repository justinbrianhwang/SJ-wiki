---
title: Quantum Models of Motion
sidebar_position: 14
---

# Quantum Models of Motion

Simple quantum models are not just textbook exercises. The particle in a box, harmonic oscillator, rigid rotor, and tunneling barrier are the reusable building blocks for electronic spectra, molecular vibrations, rotational spectroscopy, reaction rates, and nanoscience.

Atkins uses these models to show how boundary conditions and potentials shape energy levels. Each model has a characteristic spacing pattern, and those spacing patterns explain observed spectra and thermal behavior.

## Definitions

For a particle in a one-dimensional box of length $L$ with infinite walls, the allowed wavefunctions are

$$
\psi_n(x)=\left(\frac{2}{L}\right)^{1/2}\sin\frac{n\pi x}{L}
$$

with energies

$$
E_n=\frac{n^2h^2}{8mL^2},
\qquad
n=1,2,3,\dots
$$

For a harmonic oscillator,

$$
V(x)=\frac{1}{2}kx^2
$$

and

$$
E_v=\left(v+\frac{1}{2}\right)h\nu,
\qquad
v=0,1,2,\dots
$$

where

$$
\nu=\frac{1}{2\pi}\sqrt{\frac{k}{\mu}}
$$

For a rigid rotor in three dimensions,

$$
E_J=\frac{\hbar^2}{2I}J(J+1)
$$

or in spectroscopic units,

$$
\frac{E_J}{hc}=BJ(J+1)
$$

with degeneracy $2J+1$.

For a particle on a ring,

$$
E_m=\frac{m^2\hbar^2}{2I},
\qquad
m=0,\pm1,\pm2,\dots
$$

Tunneling is the penetration of a wavefunction into or through a region where classical kinetic energy would be negative.

## Key results

The particle-in-a-box model gives quantization from spatial confinement. The energy spacing increases with $n$:

$$
\Delta E_{n\to n+1}
=E_{n+1}-E_n
=\frac{(2n+1)h^2}{8mL^2}
$$

The harmonic oscillator has evenly spaced levels:

$$
\Delta E=h\nu
$$

and nonzero ground-state energy:

$$
E_0=\frac{1}{2}h\nu
$$

The rigid rotor has level spacings that increase with $J$:

$$
\Delta E_{J\to J+1}=2Bhc(J+1)
$$

The selection rules for ideal spectroscopic transitions are model-dependent. For the harmonic oscillator electric dipole transition,

$$
\Delta v=\pm1
$$

if the vibration changes the molecular dipole moment. For the rigid rotor in microwave absorption,

$$
\Delta J=\pm1
$$

and the molecule must have a permanent dipole moment.

Tunneling probability decreases sharply with barrier width and with the square root of mass. A rough barrier penetration factor is

$$
T\sim e^{-2\kappa a},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}
$$

This explains why electron tunneling is common in spectroscopy and electrochemistry, while heavy-atom tunneling is usually much weaker.

The particle in a box is the simplest model of confinement. Its wavefunctions have nodes fixed by boundary conditions at the walls, and its energies scale as $1/L^2$. This length dependence is chemically important: extending a conjugated system lowers electronic transition energies, often shifting absorption to longer wavelengths. The model is crude because real molecular potentials are not infinite square wells, but it captures the central relation between delocalization and energy spacing.

The harmonic oscillator is the local model for any smooth potential near a minimum. If a potential energy curve is expanded in a Taylor series about equilibrium,

$$
V(x)\approx V(x_e)+\frac{1}{2}
\left(\frac{d^2V}{dx^2}\right)_{x_e}(x-x_e)^2
$$

the second derivative acts as a force constant. This is why so many vibrations are approximately harmonic for low quantum numbers. The model predicts equal spacings and a zero-point energy. Real bonds are anharmonic: level spacings shrink as the bond stretches, and eventually the molecule dissociates.

The rigid rotor model connects directly to molecular geometry. The moment of inertia $I=\mu r^2$ depends on bond length, so rotational spectra can provide precise structural information. Larger moments of inertia give smaller rotational constants and more closely spaced lines. Polyatomic molecules require principal moments of inertia, leading to linear, spherical top, symmetric top, and asymmetric top classifications.

The particle on a ring is a bridge between rotational motion and delocalized electronic motion. It is useful for cyclic conjugated molecules because periodic boundary conditions require the wavefunction to match after a full circuit. The allowed angular momentum quantum numbers include positive and negative values corresponding to opposite circulation. Magnetic fields can split or shift such states, linking the model to aromaticity and ring currents in more advanced contexts.

Tunneling shows that quantum probability can cross classically forbidden regions. The wavefunction does not abruptly vanish when $E\lt V(x)$; it decays exponentially. A barrier that is thin enough or a particle that is light enough can have measurable transmission. This affects scanning tunneling microscopy, inversion in ammonia, proton transfer, alpha decay, and low-temperature reaction rates. The exponential dependence on mass and barrier width explains why isotope substitution can strongly change tunneling contributions.

Approximation methods become necessary quickly. Perturbation theory handles small changes to a solvable Hamiltonian; variation theory estimates ground-state energies by optimizing trial wavefunctions; time-dependent perturbation theory describes transitions caused by oscillating fields. These methods are introduced after the exact models because real molecules rarely match exactly solvable potentials.

Selection rules arise from both model algebra and physical coupling. The harmonic oscillator has $\Delta v=\pm1$ in the ideal electric-dipole approximation, but anharmonicity allows overtones. The rigid rotor has $\Delta J=\pm1$ for microwave absorption, but only if the molecule has a permanent dipole. The particle in a box has transition restrictions based on parity-like integrals. In every case, an energy difference is necessary but not sufficient for spectral intensity.

These models also feed statistical thermodynamics. The translational partition function comes from particle-in-a-box levels in the limit of extremely dense spacing. The vibrational partition function comes from harmonic oscillator spacings. Rotational partition functions come from rotor levels and degeneracies. Thus the simple quantum models are not isolated; they are the molecular foundation of heat capacities, entropies, and equilibrium constants.

## Visual

```text
Energy patterns

Particle in a box:     E_n proportional to n^2
                       n=4  ----------------
                       n=3  ---------
                       n=2  ----
                       n=1  -

Harmonic oscillator:   equal spacing
                       v=3  -----------
                       v=2  -------
                       v=1  ---
                       v=0  -

Rigid rotor:           E_J proportional to J(J+1)
                       J=3  ----------------
                       J=2  --------
                       J=1  ---
                       J=0  _
```

| Model | Energy formula | Spacing pattern | Chemical use |
|---|---:|---|---|
| Particle in a box | $n^2h^2/(8mL^2)$ | increases with $n$ | conjugated molecules, quantum dots |
| Harmonic oscillator | $(v+1/2)h\nu$ | constant | vibrations, IR spectra, heat capacity |
| Rigid rotor | $BhcJ(J+1)$ | increases linearly in transitions | microwave spectra, bond lengths |
| Tunneling barrier | $T\sim e^{-2\kappa a}$ | not discrete by itself | reaction rates, STM, electron transfer |

## Worked example 1: Particle-in-a-box transition energy

**Problem.** Estimate the $n=1\to2$ transition wavelength for an electron in a one-dimensional box of length $1.00\ \mathrm{nm}$.

**Method.** Use

$$
\Delta E=E_2-E_1=\frac{(4-1)h^2}{8mL^2}
=\frac{3h^2}{8mL^2}
$$

and $\lambda=hc/\Delta E$.

1. Substitute:

$$
\Delta E=\frac{3(6.626\times10^{-34})^2}
{8(9.109\times10^{-31})(1.00\times10^{-9})^2}
$$

2. Calculate:

$$
\Delta E=1.81\times10^{-19}\ \mathrm{J}
$$

3. Wavelength:

$$
\lambda=\frac{(6.626\times10^{-34})(2.998\times10^8)}
{1.81\times10^{-19}}
$$

$$
\lambda=1.10\times10^{-6}\ \mathrm{m}
=1100\ \mathrm{nm}
$$

**Checked answer.** A nanometer-scale box gives near-infrared energy spacing. Shorter boxes would shift transitions to higher energy.

## Worked example 2: Bond force constant from vibrational wavenumber

**Problem.** A diatomic molecule has reduced mass $\mu=1.63\times10^{-27}\ \mathrm{kg}$ and vibrational wavenumber $2886\ \mathrm{cm^{-1}}$. Estimate the force constant.

**Method.** Convert wavenumber to frequency:

$$
\nu=c\tilde\nu
$$

and use

$$
k=(2\pi\nu)^2\mu
$$

1. Convert wavenumber to $\mathrm{m^{-1}}$:

$$
2886\ \mathrm{cm^{-1}}=2.886\times10^5\ \mathrm{m^{-1}}
$$

2. Frequency:

$$
\nu=(2.998\times10^8)(2.886\times10^5)
=8.65\times10^{13}\ \mathrm{s^{-1}}
$$

3. Angular frequency:

$$
2\pi\nu=5.43\times10^{14}\ \mathrm{s^{-1}}
$$

4. Force constant:

$$
k=(5.43\times10^{14})^2(1.63\times10^{-27})
=4.81\times10^2\ \mathrm{N\ m^{-1}}
$$

**Checked answer.** A force constant near $480\ \mathrm{N\ m^{-1}}$ is reasonable for a strong diatomic bond such as HCl.

## Code

```python
import numpy as np

h = 6.62607015e-34
c = 2.99792458e8
me = 9.1093837015e-31

def box_transition_wavelength(L, n1, n2, m=me):
    dE = (n2**2 - n1**2) * h**2 / (8 * m * L**2)
    return h * c / dE

def force_constant(wavenumber_cm, reduced_mass_kg):
    nu = c * (wavenumber_cm * 100.0)
    return (2 * np.pi * nu)**2 * reduced_mass_kg

print("box wavelength nm:", box_transition_wavelength(1e-9, 1, 2) * 1e9)
print("force constant N/m:", force_constant(2886.0, 1.63e-27))
```

## Common pitfalls

- Forgetting that the particle in a box has no $n=0$ state.
- Ignoring zero-point energy in the harmonic oscillator.
- Treating the harmonic oscillator as exact for highly excited vibrations; real bonds are anharmonic and can dissociate.
- Applying rotational microwave selection rules to molecules without permanent dipole moments.
- Underestimating mass effects in tunneling; replacing H by D can strongly change rates.

When using a model, identify what physical feature it preserves and what it discards. The particle in a box preserves confinement but discards realistic potential shape. The harmonic oscillator preserves curvature near a minimum but discards dissociation. The rigid rotor preserves rotational quantization but discards bond stretching. A model can be useful even when obviously idealized if the retained feature controls the observation.

Scaling relations are often more valuable than exact numbers. Box energies scale as $1/mL^2$, vibrational frequencies as $(k/\mu)^{1/2}$, and rotational constants as $1/I$. These scalings predict isotope effects, size effects, and bond-strength trends quickly. They also provide checks on numerical answers: heavier isotopes lower vibrational frequencies and rotational constants; stronger bonds raise vibrational frequencies.

For tunneling, remember that probability depends exponentially on parameters. A small increase in barrier width or particle mass can reduce tunneling by orders of magnitude. This is why electron transfer can occur through barriers that would be impossible for heavy atoms, and why hydrogen-transfer reactions can show unusually large kinetic isotope effects at low temperature.

It is also worth checking the classical limit. At large quantum numbers, particle-in-a-box and rotor level spacings become small compared with the total energy, and quantum predictions begin to resemble classical continuous motion. At low quantum numbers, zero-point energy, nodes, and selection rules dominate. Many chemical phenomena sit between these limits, which is why simple models remain useful but need corrections.

In spectroscopy problems, connect each model parameter to an observable: $L$ to confinement energy, $k$ to vibrational frequency, $I$ to rotational spacing, and barrier width to tunneling probability. This keeps the model physical.

When numerical answers are unreasonable, inspect powers of ten first. Nanometers, picometers, $\mathrm{cm^{-1}}$, and SI base units are frequently mixed in these models.

Also verify whether a frequency is ordinary frequency $\nu$ or angular frequency $\omega=2\pi\nu$; the missing $2\pi$ is a common source of force-constant errors.

Write the defining equation before substituting constants.

Then check units.

## Connections

- [Quantum foundations](/chemistry/physical-chemistry/quantum-foundations)
- [Rotational, vibrational, and Raman spectroscopy](/chemistry/physical-chemistry/rotational-vibrational-and-raman-spectroscopy)
- [Temperature dependence and reaction dynamics](/chemistry/physical-chemistry/temperature-dependence-and-reaction-dynamics)
- [Physics quantum mechanics](/physics/quantum-mechanics/)
