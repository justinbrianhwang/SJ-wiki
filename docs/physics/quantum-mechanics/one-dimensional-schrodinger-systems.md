---
title: One-Dimensional Schrodinger Systems
sidebar_position: 6
---

# One-Dimensional Schrodinger Systems

One-dimensional potentials are where the abstract postulates become wave mechanics. A free particle spreads, a particle in a box has quantized standing waves, a finite well can bind only certain states, and a barrier can transmit particles even when the classical kinetic energy would be negative inside.

Sakurai presents wave mechanics after Dirac notation and dynamics, treating wave functions as representations of kets. Ballentine uses coordinate and momentum representations early, with careful attention to probability flux and boundary conditions. The Gottfried-named notes start with wave functions and then build the formalism. Schiff's classic approach is closest to the traditional sequence: solve differential equations, then interpret the spectra.

## From the Schrödinger equation to conserved probability

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

To derive it, multiply the Schrödinger equation by $\psi^*$ and its complex conjugate by $\psi$, then subtract. For a real potential, the $V\vert \psi\vert ^2$ terms cancel:

$$
i\hbar{\partial|\psi|^2\over\partial t}
=-{\hbar^2\over2m}
\left(\psi^*{\partial^2\psi\over\partial x^2}
-\psi{\partial^2\psi^*\over\partial x^2}\right).
$$

The expression in parentheses is a total derivative. Rearranging gives the stated current and continuity equation. Integrating over an interval $[a,b]$ gives

$$
{d\over dt}\int_a^b\rho\,dx=j(a,t)-j(b,t),
$$

so probability changes only through flux across the endpoints.

For finite jumps in $V(x)$, the wave function and its first derivative are continuous. For an infinite wall, the wave function vanishes at the wall.

## Confinement, leakage, and transmission

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

For equal zero potentials on both sides of a rectangular barrier, exact matching gives

$$
T=\left[1+{V_0^2\sinh^2(\kappa a)\over4E(V_0-E)}\right]^{-1},
\qquad E<V_0.
$$

Using $\sinh(\kappa a)\sim e^{\kappa a}/2$ recovers the exponential estimate, including a prefactor that can matter when the barrier is not very thick. Above the barrier, $\kappa$ becomes imaginary and the hyperbolic sine becomes an ordinary sine; reflection still occurs because wave impedance changes at the interfaces.

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

## Four boundary-value patterns

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

## Worked example: infinite-well normalization and energy

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

## Worked example: tunneling scale through a barrier

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

## Matching rules, including a delta potential

The usual continuity of $u'$ assumes that $V(x)$ stays finite. A delta potential $V(x)=g\delta(x)$ is an important exception. Integrate the stationary equation from $-\epsilon$ to $+\epsilon$:

$$
-{\hbar^2\over2m}[u'(\epsilon)-u'(-\epsilon)]
+g u(0)=E\int_{-\epsilon}^{\epsilon}u(x)\,dx.
$$

As $\epsilon\to0$, the right-hand integral vanishes while the delta term remains. Thus

$$
u'(0^+)-u'(0^-)={2mg\over\hbar^2}u(0).
$$

The wavefunction itself remains continuous. For an attractive delta, $g\lt 0$, the ansatz $u=Ae^{-\kappa\vert x\vert }$ gives a single bound state. The jump condition gives $-2\kappa=2mg/\hbar^2$, so

$$
\kappa=-{mg\over\hbar^2},
\qquad
E=-{\hbar^2\kappa^2\over2m}=-{mg^2\over2\hbar^2}.
$$

## Errors that look plausible

- Applying infinite-wall boundary conditions to a finite well. Finite wells have exponential tails outside.
- Treating plane waves as normalizable particles. Plane waves are idealized momentum eigenstates; packets are physical states.
- Forgetting derivative continuity at finite potential jumps. Only infinite jumps allow derivative discontinuities through the limiting wall model.
- Equating $E\lt V$ with impossibility. In quantum mechanics it means local exponential behavior, not zero amplitude.
- Losing current conservation in scattering. Reflection and transmission probabilities must be computed from currents, not only from amplitude magnitudes when wave numbers differ.
- Assuming all bound-state energies can be written in elementary closed form. Finite wells generally require numerical roots.
- Ignoring parity when a potential is symmetric. Even and odd states reduce the matching work.

Boundary conditions carry physical content. In an infinite well, the wall is an idealization of an infinitely high potential, so the wave function is forced to zero at the boundary. In a finite well, the wave function penetrates into the exterior and both $\psi$ and $d\psi/dx$ are continuous. At a delta-function potential, the wave function is continuous but the derivative has a jump. Treating all boundaries the same is one of the quickest ways to get a plausible-looking but wrong spectrum.

It is also important to distinguish stationary states from general time-dependent states. A single energy eigenstate has a time-independent probability density because the phase $e^{-iEt/\hbar}$ cancels in $\vert \psi\vert ^2$. A superposition of energy eigenstates usually has time-dependent density because relative phases evolve. This is where the Dirac and wave-mechanics pictures meet: time dependence lives in phase factors attached to energy components.

For scattering in one dimension, use current rather than amplitude alone. If the incident and transmitted regions have different wave numbers, the transmitted probability differs from $\vert A_T\vert ^2/\vert A_I\vert ^2$ by a velocity or current factor. The same flux logic returns in three-dimensional scattering and cross sections.

One-dimensional problems are also model laboratories. The infinite well teaches quantization by boundary conditions. The finite well teaches matching and tunneling tails. The barrier teaches classically forbidden transmission. The free packet teaches dispersion. These examples should not be memorized as unrelated formulas; they are variations of the same eigenvalue equation plus normalization, boundary conditions, and probability interpretation.

When an exact solution is unavailable, one-dimensional systems are also the natural testing ground for numerical methods. Finite-difference Hamiltonians should be Hermitian, eigenvectors should be orthogonal under the chosen grid inner product, and bound-state energies should converge as the grid is refined. Numerical spectra that depend strongly on box size or grid spacing are usually revealing a discretization artifact rather than new physics.

## General facts about one-dimensional bound states

Bound states of a regular one-dimensional potential are nondegenerate. Suppose two normalizable solutions have the same energy. Their Wronskian is constant because the Schrödinger equation contains no first derivative. Both functions and their derivatives decay in the asymptotic bound-state region, so the constant Wronskian is zero. The two solutions are therefore linearly dependent. Degeneracy can reappear when the configuration space is disconnected or extra internal degrees of freedom are included.

Bound eigenfunctions can be ordered by their nodes. The ground state has no internal node and can be chosen everywhere positive. The first excited state has one node, and each successive state adds one. A node raises kinetic energy by forcing additional curvature, which gives an intuitive reason for the ordering. The formal result is a version of the Sturm–Liouville oscillation theorem.

For a symmetric potential, parity commutes with the Hamiltonian. Nondegeneracy then forces each bound eigenstate to have definite parity. Even states obey a zero-derivative condition at the center, while odd states vanish there. Solving only on one half-line with the corresponding center condition cuts the numerical and analytic matching work in half.

The existence of a bound state depends strongly on dimension. In one dimension, a sufficiently well-behaved attractive potential with nonzero integrated attraction generally supports at least one bound state, even when the attraction is weak. A finite square well therefore does not need to exceed a nonzero threshold to bind its lowest state. Odd states and additional even states do appear only after the well becomes deep or wide enough.

## Wave packets and dispersion

A free wave packet is a superposition of plane waves with different wave numbers. Its group velocity is the derivative of angular frequency with respect to wave number, which equals momentum divided by mass for the nonrelativistic dispersion relation. The phase velocity differs, but the envelope carrying probability travels at the group velocity.

Because the free-particle angular frequency is quadratic in wave number, different Fourier components acquire relative phases at different rates. A localized packet spreads. A Gaussian remains Gaussian, with a width that grows on a time scale set by its initial width, mass, and Planck's constant. A heavier particle or a broader initial packet spreads more slowly.

The center of a free packet obeys the Ehrenfest equations exactly, moving at constant mean momentum. Packet spreading is compatible with that classical center motion. Confusing the trajectory of the mean with the evolution of the entire probability distribution hides one of the main quantum effects in free dynamics.

A stationary scattering state is different from a traveling packet. It extends across all space and describes steady incident, reflected, and transmitted flux. A localized incident packet gives the more literal time sequence, but the asymptotic reflection and transmission probabilities agree when the packet is narrow in momentum and the scattering amplitudes vary slowly across its bandwidth.

## Scattering coefficients and resonances

For an incident wave from the left, current conservation relates incident, reflected, and transmitted flux. When the potentials on both sides are equal, the wave numbers match and the reflection and transmission probabilities sum to one using squared amplitudes. When they differ, the transmitted amplitude must be weighted by the ratio of outgoing to incoming velocities.

A finite barrier can show nearly perfect transmission at selected energies above the barrier. Multiple reflections inside the barrier interfere, much like waves in a Fabry–Pérot cavity. Tunneling below a single barrier is exponentially suppressed, but a pair of barriers can support a quasibound state between them and produce resonant transmission. The lifetime of that temporary state is related to the width of the resonance.

Bound states and scattering states belong to one spectral problem. Bound states are square-integrable and occur at discrete energies below the asymptotic continuum. Scattering states are delta-normalized and fill the continuum. Completeness usually requires both sets. Expanding a localized state using only bound eigenfunctions fails whenever part of it can escape to infinity.

Boundary conditions also determine whether the Hamiltonian is self-adjoint. Vanishing wavefunctions at hard walls are one choice, but periodic or phase-twisted conditions describe a ring. Different self-adjoint boundary conditions define different physical systems even when the differential expression inside the interval is identical.

## Related pages

- [Dirac notation and Hilbert spaces](/physics/quantum-mechanics/dirac-notation-hilbert-spaces)
- [Quantum dynamics and pictures](/physics/quantum-mechanics/quantum-dynamics-pictures)
- [Harmonic oscillator with ladder operators](/physics/quantum-mechanics/harmonic-oscillator-ladder-operators)
- [Variational principle and WKB](/physics/quantum-mechanics/variational-principle-wkb)
- [Scattering theory](/physics/quantum-mechanics/scattering-theory)
