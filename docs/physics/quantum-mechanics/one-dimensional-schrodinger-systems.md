---
title: One-Dimensional Schrodinger Systems
sidebar_position: 6
---

# One-Dimensional Schrodinger Systems

One-dimensional potentials are where the abstract postulates become wave mechanics. A free particle spreads, a particle in a box has quantized standing waves, a finite well can bind only certain states, and a barrier can transmit particles even when the classical kinetic energy would be negative inside.

Sakurai presents wave mechanics after Dirac notation and dynamics, treating wave functions as representations of kets. Ballentine uses coordinate and momentum representations early, with careful attention to probability flux and boundary conditions. The Gottfried-named notes start with wave functions and then build the formalism. Schiff's classic approach is closest to the traditional sequence: solve differential equations, then interpret the spectra.

![A particle-in-a-box diagram shows standing-wave probability structure between hard walls.](https://commons.wikimedia.org/wiki/Special:FilePath/Particle_in_a_box.svg)

*Figure: The infinite square well is the simplest visual example of confinement producing discrete energy levels. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Particle_in_a_box.svg), Pieter Kuiper, public domain.*

## Definitions

For a particle of mass $m$ in one dimension,

$$
H={P^2\over 2m}+V(X).
$$

In the position representation,

$$
P=-i\hbar {d\over dx},
$$

so the time-dependent Schrodinger equation is

$$
i\hbar{\partial \psi(x,t)\over \partial t}
=-\frac{\hbar^2}{2m}{\partial^2\psi(x,t)\over \partial x^2}+V(x)\psi(x,t).
$$

For a time-independent potential, stationary states have

$$
\psi(x,t)=u(x)e^{-iEt/\hbar},
$$

where

$$
-\frac{\hbar^2}{2m}{d^2u\over dx^2}+V(x)u(x)=Eu(x).
$$

The probability density is

$$
\rho(x,t)=|\psi(x,t)|^2,
$$

and the probability current is

$$
j(x,t)={\hbar\over 2mi}\left(\psi^*{\partial\psi\over\partial x}-\psi{\partial\psi^*\over\partial x}\right).
$$

They obey the continuity equation

$$
{\partial \rho\over \partial t}+{\partial j\over \partial x}=0.
$$

For finite jumps in $V(x)$, the wave function and its first derivative are continuous. For an infinite wall, the wave function vanishes at the wall.

## Key results

For the infinite square well on $0\lt x\lt L$,

$$
V(x)=0\quad (0<x<L),\qquad V=\infty\quad \text{outside}.
$$

The normalized eigenfunctions and energies are

$$
u_n(x)=\sqrt{2\over L}\sin{n\pi x\over L},
\qquad
E_n={n^2\pi^2\hbar^2\over 2mL^2},
\qquad n=1,2,3,\ldots.
$$

The finite well differs in two crucial ways: bound-state wave functions leak into the classically forbidden region, and the number of bound states is finite for a finite-depth well. The matching conditions lead to transcendental equations rather than a simple closed-form spectrum.

For a rectangular barrier of height $V_0$ and width $a$, with $E\lt V_0$, the decay constant inside the barrier is

$$
\kappa={\sqrt{2m(V_0-E)}\over \hbar}.
$$

When the barrier is thick enough that $\kappa a\gg 1$, the transmission probability is exponentially small:

$$
T\propto e^{-2\kappa a}.
$$

The proportionality factor depends on boundary matching. The exponential dependence is the main physical point: classically forbidden does not mean quantum impossible.

A free particle energy eigenstate has the form

$$
\psi_k(x,t)=Ae^{i(kx-\omega t)},
\qquad E=\hbar\omega={\hbar^2k^2\over 2m}.
$$

Such a plane wave is not normalizable on the infinite line, so physical free particles are wave packets:

$$
\psi(x,t)=\int dk\,a(k)e^{i(kx-\omega(k)t)}.
$$

Sakurai interprets this through the position representation of kets, while Ballentine emphasizes the probability current and the distinction between normalizable packets and generalized eigenfunctions.

## Visual

```text
Infinite well on 0 < x < L

V
^     infinity          infinity
|        |                 |
|        |                 |
|        |_________________|
|        0                 L        x

u1:      /\ 
        /  \
_______/    \_______

u2:      /\    /\
        /  \  /  \
_______/    \/    \______
```

| System | Boundary condition | Spectrum | Key lesson |
|---|---|---|---|
| Free particle | scattering or packet normalization | continuous $E$ | momentum eigenstates are generalized |
| Infinite well | $u(0)=u(L)=0$ | discrete $n^2$ energies | confinement quantizes wavelength |
| Finite well | match $u$ and $u'$ | finite discrete bound states plus continuum | forbidden tails matter |
| Barrier | match incoming, reflected, transmitted waves | continuum | tunneling gives nonzero transmission |

## Worked example 1: Infinite well normalization and energy

**Problem.** A particle is in a one-dimensional infinite well $0\lt x\lt L$. Find the normalized first excited state and its energy.

**Method.**

1. Inside the well, solve

$$
-{\hbar^2\over 2m}{d^2u\over dx^2}=Eu.
$$

2. Write

$$
u(x)=A\sin(kx)+B\cos(kx).
$$

3. Apply $u(0)=0$, so $B=0$.

4. Apply $u(L)=0$, so

$$
\sin(kL)=0\Rightarrow kL=n\pi.
$$

5. The first excited state has $n=2$:

$$
u_2(x)=A\sin{2\pi x\over L}.
$$

6. Normalize:

$$
1=A^2\int_0^L\sin^2{2\pi x\over L}dx=A^2{L\over 2}.
$$

7. Therefore

$$
A=\sqrt{2\over L}.
$$

8. The energy is

$$
E_2={4\pi^2\hbar^2\over 2mL^2}={2\pi^2\hbar^2\over mL^2}.
$$

**Checked answer.** The first excited state has one internal node at $x=L/2$, and its energy is four times the ground-state energy.

## Worked example 2: Tunneling scale through a barrier

**Problem.** Estimate the exponential tunneling factor for an electron with $E=2.0\,\mathrm{eV}$ incident on a barrier with $V_0=5.0\,\mathrm{eV}$ and width $a=0.20\,\mathrm{nm}$.

**Method.**

1. The forbidden-region decay constant is

$$
\kappa={\sqrt{2m(V_0-E)}\over \hbar}.
$$

2. Convert the energy difference:

$$
V_0-E=3.0\,\mathrm{eV}=3.0(1.602\times 10^{-19})\,\mathrm{J}.
$$

3. Substitute $m=9.11\times10^{-31}\,\mathrm{kg}$ and $\hbar=1.055\times10^{-34}\,\mathrm{J\,s}$:

$$
\kappa\approx
{\sqrt{2(9.11\times10^{-31})(4.806\times10^{-19})}\over 1.055\times10^{-34}}
\approx 8.9\times10^9\,\mathrm{m^{-1}}.
$$

4. Compute

$$
2\kappa a=2(8.9\times10^9)(0.20\times10^{-9})\approx 3.6.
$$

5. The exponential factor is

$$
e^{-2\kappa a}\approx e^{-3.6}\approx 2.7\times10^{-2}.
$$

**Checked answer.** The full transmission coefficient is not exactly this number because matching prefactors matter, but the estimate correctly shows a few-percent scale rather than zero.

## Code

```python
import numpy as np

L = 1.0
n_grid = 400
x = np.linspace(0, L, n_grid)
dx = x[1] - x[0]

psi2 = np.sqrt(2 / L) * np.sin(2 * np.pi * x / L)
norm = np.trapz(abs(psi2) ** 2, x)
node_index = np.argmin(abs(x - L / 2))

print("normalization:", norm)
print("value near node:", psi2[node_index])
```

## Common pitfalls

- Applying infinite-wall boundary conditions to a finite well. Finite wells have exponential tails outside.
- Treating plane waves as normalizable particles. Plane waves are idealized momentum eigenstates; packets are physical states.
- Forgetting derivative continuity at finite potential jumps. Only infinite jumps allow derivative discontinuities through the limiting wall model.
- Equating $E\lt V$ with impossibility. In quantum mechanics it means local exponential behavior, not zero amplitude.
- Losing current conservation in scattering. Reflection and transmission probabilities must be computed from currents, not only from amplitude magnitudes when wave numbers differ.
- Assuming all bound-state energies can be written in elementary closed form. Finite wells generally require numerical roots.
- Ignoring parity when a potential is symmetric. Even and odd states reduce the matching work.

Boundary conditions carry physical content. In an infinite well, the wall is an idealization of an infinitely high potential, so the wave function is forced to zero at the boundary. In a finite well, the wave function penetrates into the exterior and both $\psi$ and $d\psi/dx$ are continuous. At a delta-function potential, the wave function is continuous but the derivative has a jump. Treating all boundaries the same is one of the quickest ways to get a plausible-looking but wrong spectrum.

It is also important to distinguish stationary states from general time-dependent states. A single energy eigenstate has a time-independent probability density because the phase $e^{-iEt/\hbar}$ cancels in $\vert \psi\vert ^2$. A superposition of energy eigenstates usually has time-dependent density because relative phases evolve. This is where the Dirac and wave-mechanics pictures meet: time dependence lives in phase factors attached to energy components.

For scattering in one dimension, use current rather than amplitude alone. If the incident and transmitted regions have different wave numbers, the transmitted probability is not simply $\vert A_T\vert ^2/\vert A_I\vert ^2$; the velocity or current factor must be included. Ballentine's emphasis on probability flux helps prevent this mistake. The same current logic returns in three-dimensional scattering as flux and cross section.

One-dimensional problems are also model laboratories. The infinite well teaches quantization by boundary conditions. The finite well teaches matching and tunneling tails. The barrier teaches classically forbidden transmission. The free packet teaches dispersion. These examples should not be memorized as unrelated formulas; they are variations of the same eigenvalue equation plus normalization, boundary conditions, and probability interpretation.

When an exact solution is unavailable, one-dimensional systems are also the natural testing ground for numerical methods. Finite-difference Hamiltonians should be Hermitian, eigenvectors should be orthogonal under the chosen grid inner product, and bound-state energies should converge as the grid is refined. Numerical spectra that depend strongly on box size or grid spacing are usually revealing a discretization artifact rather than new physics.

## Connections

- [Dirac notation and Hilbert spaces](/physics/quantum-mechanics/dirac-notation-hilbert-spaces)
- [Quantum dynamics and pictures](/physics/quantum-mechanics/quantum-dynamics-pictures)
- [Harmonic oscillator with ladder operators](/physics/quantum-mechanics/harmonic-oscillator-ladder-operators)
- [Variational principle and WKB](/physics/quantum-mechanics/variational-principle-wkb)
- [Scattering theory](/physics/quantum-mechanics/scattering-theory)
