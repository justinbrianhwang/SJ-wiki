---
title: Variational Principle and WKB
sidebar_position: 14
---

# Variational Principle and WKB

The variational principle and WKB approximation are complementary tools for problems that are not exactly solvable. Variational methods estimate low-energy bound states by trying plausible wave functions. WKB estimates wave behavior when the de Broglie wavelength changes slowly compared with the scale of the potential.

Sakurai introduces WKB among elementary solutions of the Schrodinger equation and uses variational ideas in approximation methods. Ballentine gives a substantial variational-method treatment in the bound-state chapter and discusses semiclassical limits separately. The Gottfried-named notes include WKB and perturbative comparisons in approximation methods. Schiff's classic presentation is especially close to the traditional one-dimensional WKB connection-formula style.

![A particle-in-a-box diagram shows standing-wave probability structure between hard walls.](https://commons.wikimedia.org/wiki/Special:FilePath/Particle_in_a_box.svg)

*Figure: The infinite square well is the simplest visual example of confinement producing discrete energy levels. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Particle_in_a_box.svg), Pieter Kuiper, public domain.*

## Definitions

For a normalized trial state $\vert \alpha\rangle$, the variational energy is

$$
E[\alpha]={\langle \alpha|H|\alpha\rangle\over \langle \alpha|\alpha\rangle}.
$$

If $E_0$ is the exact ground-state energy, the variational principle states

$$
E[\alpha]\geq E_0.
$$

A trial family $\vert \alpha(\lambda)\rangle$ depends on one or more variational parameters $\lambda$. The best estimate inside that family is found by minimizing

$$
{dE(\lambda)\over d\lambda}=0
$$

or by solving the corresponding multivariable gradient equations.

The WKB approximation starts from the one-dimensional time-independent Schrodinger equation

$$
-{\hbar^2\over 2m}{d^2\psi\over dx^2}+V(x)\psi=E\psi.
$$

Define the local classical momentum

$$
p(x)=\sqrt{2m(E-V(x))}.
$$

In a classically allowed region $E\gt V(x)$, WKB gives

$$
\psi(x)\approx {C\over \sqrt{p(x)}}
\exp\left(\pm {i\over\hbar}\int^x p(x')\,dx'\right).
$$

In a forbidden region $E\lt V(x)$, define

$$
\kappa(x)=\sqrt{2m(V(x)-E)}.
$$

Then

$$
\psi(x)\approx {C\over \sqrt{\kappa(x)}}
\exp\left(\pm {1\over\hbar}\int^x \kappa(x')\,dx'\right).
$$

## Key results

The variational principle proof is short. Expand a normalized trial state in exact energy eigenstates:

$$
|\alpha\rangle=\sum_n c_n|n\rangle.
$$

Then

$$
\langle H\rangle=\sum_n |c_n|^2E_n.
$$

Since $E_n\geq E_0$ for every $n$,

$$
\langle H\rangle\geq E_0\sum_n |c_n|^2=E_0.
$$

This is why a bad trial state still gives an upper bound for the ground energy, assuming the Hamiltonian is bounded below and the trial state is in the domain of $H$.

For one-dimensional bound states with two classical turning points $x_1,x_2$, WKB quantization gives

$$
\int_{x_1}^{x_2}p(x)\,dx=\left(n+{1\over2}\right)\pi\hbar.
$$

The half-integer shift is the Maslov correction from the turning points. For tunneling through a barrier between $x_1$ and $x_2$, the leading exponential factor is

$$
T\sim \exp\left[-{2\over\hbar}\int_{x_1}^{x_2}\sqrt{2m(V(x)-E)}\,dx\right].
$$

Variational methods are global and energy-focused; WKB is local and phase-focused. Ballentine's treatment highlights variational control for bound-state estimates, while Sakurai's path from WKB to propagators helps connect semiclassical phases with action.

## Visual

```text
WKB regions for a barrier

V(x)
 ^
 |              forbidden
 |              _________
 |             /         \
 |____________/           \____________
 |      allowed     E      allowed
 +----x1-----------------x2-----------> x

allowed:    oscillatory phase exp(+- i integral p dx / hbar)
forbidden:  exponential decay/growth exp(+- integral kappa dx / hbar)
```

| Method | Input | Output | Reliability check |
|---|---|---|---|
| Variational | trial wave function | upper bound to $E_0$ | improve trial family and compare |
| WKB bound states | slowly varying $p(x)$ | approximate quantization | fails near turning points without connection formulas |
| WKB tunneling | forbidden-region action | exponential transmission scale | best when action is large vs $\hbar$ |
| Perturbation | small operator change | series corrections | fails near degeneracy or large coupling |

## Worked example 1: Variational estimate for hydrogen ground energy

**Problem.** Use the trial wave function

$$
\psi_\alpha(r)=\left({\alpha^3\over \pi}\right)^{1/2}e^{-\alpha r}
$$

for hydrogen. Find the minimizing $\alpha$ and energy.

**Method.**

1. For this normalized trial state, the needed expectation values are

$$
\langle T\rangle={\hbar^2\alpha^2\over 2\mu},
\qquad
\left\langle {1\over r}\right\rangle=\alpha.
$$

2. The energy functional is

$$
E(\alpha)={\hbar^2\alpha^2\over 2\mu}
-{e^2\over 4\pi\epsilon_0}\alpha.
$$

3. Differentiate:

$$
{dE\over d\alpha}={\hbar^2\alpha\over\mu}
-{e^2\over 4\pi\epsilon_0}.
$$

4. Set to zero:

$$
\alpha={\mu e^2\over 4\pi\epsilon_0\hbar^2}={1\over a_0}.
$$

5. Substitute back:

$$
E_{\min}={\hbar^2\over 2\mu a_0^2}
-{e^2\over 4\pi\epsilon_0a_0}
=-{\hbar^2\over 2\mu a_0^2}.
$$

6. This equals

$$
-{13.6\,\mathrm{eV}}
$$

for hydrogen to standard precision.

**Checked answer.** The chosen trial family contains the exact ground-state shape, so the variational estimate reaches the exact nonrelativistic ground energy.

## Worked example 2: WKB quantization of the harmonic oscillator

**Problem.** Use WKB quantization for

$$
V(x)={1\over2}m\omega^2x^2.
$$

Find the approximate energies.

**Method.**

1. Turning points satisfy

$$
E={1\over2}m\omega^2x_0^2,
$$

so

$$
x_0=\sqrt{2E\over m\omega^2}.
$$

2. The WKB condition is

$$
\int_{-x_0}^{x_0}\sqrt{2m\left(E-{1\over2}m\omega^2x^2\right)}\,dx
=\left(n+{1\over2}\right)\pi\hbar.
$$

3. The integral is the area of an ellipse in phase space divided by two in the usual $x$-$p$ projection:

$$
\int_{-x_0}^{x_0}p(x)\,dx={\pi E\over \omega}.
$$

4. Therefore

$$
{\pi E\over \omega}=\left(n+{1\over2}\right)\pi\hbar.
$$

5. Solve:

$$
E_n=\hbar\omega\left(n+{1\over2}\right).
$$

**Checked answer.** WKB gives the exact oscillator spectrum because the quadratic potential is unusually friendly to the semiclassical quantization rule.

## Code

```python
import numpy as np

def variational_hydrogen(alpha, hbar=1.0, mu=1.0, k=1.0):
    return hbar**2 * alpha**2 / (2 * mu) - k * alpha

alphas = np.linspace(0.1, 2.0, 200)
energies = variational_hydrogen(alphas)
best = np.argmin(energies)

print("best alpha:", alphas[best])
print("best energy:", energies[best])
```

## Common pitfalls

- Forgetting that the variational estimate is an upper bound only for the ground state, not automatically for excited states without extra orthogonality constraints.
- Minimizing an unnormalized expectation $\langle\psi\vert H\vert \psi\rangle$ without dividing by $\langle\psi\vert \psi\rangle$.
- Choosing a trial wave function outside the Hamiltonian's domain.
- Trusting WKB at a turning point without connection formulas. The naive amplitude diverges as $p(x)\to0$.
- Treating the WKB exponential prefactor as more reliable than the action exponent when the barrier is thick.
- Ignoring symmetry in trial functions. A trial state with the wrong parity cannot approximate the intended state well.
- Mixing variational and perturbative logic. Variational estimates do not require a small parameter, but they depend strongly on trial-family quality.

Variational work is only as good as the trial family. A one-parameter exponential works beautifully for hydrogen because it has the exact functional shape available. The same one-parameter family would be poor for a double well because it cannot represent two separated lobes or tunneling splitting. Before differentiating, inspect whether the trial function has the right symmetry, boundary behavior, number of nodes, and asymptotic decay. These qualitative features often matter more than adding another parameter blindly.

For excited states, the simple ground-state upper-bound statement needs refinement. If a trial state is constrained to be orthogonal to all lower exact states, a similar variational bound applies to the corresponding excited energy. In practical calculations, one often chooses trial functions with different parity or angular momentum so orthogonality follows from symmetry. This is another reason symmetry labels are not bookkeeping decoration; they make variational estimates meaningful for more than just the ground state.

WKB should be read as an expansion in slowly varying phase. The approximation is good when the local wavelength changes little over one wavelength. It is bad near turning points because $p(x)$ vanishes and the naive amplitude $1/\sqrt{p(x)}$ diverges. Connection formulas repair this by matching WKB waves to Airy-function behavior near the turning point. Schiff-style treatments often dwell on these connection formulas because they are essential for reliable one-dimensional spectra and tunneling factors.

The two methods can also check each other. Variational estimates give upper bounds for bound-state energies, while WKB often gives accurate high-quantum-number spectra and tunneling exponents. If both methods are applicable and disagree strongly, examine whether the trial family is too restrictive or whether the WKB action is too small for semiclassical reasoning. Ballentine's separation of variational and classical-limit topics helps keep these domains distinct.

For multidimensional systems, variational thinking often generalizes more directly than elementary WKB. A trial wave function can include correlations, anisotropic widths, or basis expansions, and the same Rayleigh quotient applies. WKB in several dimensions requires more geometric machinery because classical trajectories, caustics, and phases replace a single one-dimensional action integral. This is why introductory courses usually teach WKB in one dimension but use variational estimates broadly.

Numerically, variational methods become the Rayleigh-Ritz method: choose a finite basis, build the Hamiltonian matrix, and diagonalize it. The lowest eigenvalue in the chosen subspace is an upper bound to the true ground energy. Enlarging the basis can only improve or leave unchanged that variational estimate. This connects hand trial functions to practical computational quantum mechanics.

## Connections

- [One-dimensional Schrodinger systems](/physics/quantum-mechanics/one-dimensional-schrodinger-systems)
- [Central potentials and the hydrogen atom](/physics/quantum-mechanics/central-potentials-hydrogen-atom)
- [Time-independent perturbation theory](/physics/quantum-mechanics/time-independent-perturbation-theory)
- [Path integral formulation](/physics/quantum-mechanics/path-integral-formulation)
- [Scattering theory](/physics/quantum-mechanics/scattering-theory)
