---
title: Harmonic Oscillator with Ladder Operators
sidebar_position: 7
---

# Harmonic Oscillator with Ladder Operators

The harmonic oscillator is the exactly solvable model that reappears everywhere: molecular vibrations, electromagnetic field modes, phonons, small oscillations near stable equilibria, and coherent states. Its algebraic solution also shows why operators are more than a notation for differential equations.

Sakurai solves the oscillator with ladder operators after developing time evolution and the Heisenberg picture. Ballentine gives both algebraic and coordinate-representation treatments. The Gottfried-named notes include coherent states and uncertainty discussion. Schiff's classic treatment is the differential-equation counterpart, often emphasizing Hermite polynomials and wave functions.

## Definitions

The one-dimensional oscillator Hamiltonian is

$$
H={P^2\over 2m}+{1\over 2}m\omega^2X^2.
$$

Define the ladder operators

$$
a=\sqrt{m\omega\over 2\hbar}X+{i\over \sqrt{2m\hbar\omega}}P,
$$

and

$$
a^\dagger=\sqrt{m\omega\over 2\hbar}X-{i\over \sqrt{2m\hbar\omega}}P.
$$

They satisfy

$$
[a,a^\dagger]=1.
$$

The number operator is

$$
N=a^\dagger a.
$$

Solving for $X$ and $P$ gives

$$
X=\sqrt{\hbar\over 2m\omega}(a+a^\dagger),
$$

and

$$
P=-i\sqrt{m\hbar\omega\over 2}(a-a^\dagger).
$$

The Hamiltonian becomes

$$
H=\hbar\omega\left(N+{1\over 2}\right).
$$

The ground state is defined algebraically by

$$
a|0\rangle=0.
$$

## Key results

The energy eigenstates $\vert n\rangle$ obey

$$
N|n\rangle=n|n\rangle,
\qquad
H|n\rangle=\hbar\omega\left(n+{1\over 2}\right)|n\rangle,
$$

where $n=0,1,2,\ldots$.

The ladder action is

$$
a|n\rangle=\sqrt{n}|n-1\rangle,
\qquad
a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle.
$$

The zero-point energy

$$
E_0={1\over 2}\hbar\omega
$$

is not optional. If $E_0$ were zero, both kinetic and potential energy expectations would vanish, forcing $\Delta X=\Delta P=0$, which contradicts the uncertainty relation.

In the ground state,

$$
\Delta X=\sqrt{\hbar\over 2m\omega},
\qquad
\Delta P=\sqrt{m\hbar\omega\over 2},
$$

so

$$
\Delta X\Delta P={\hbar\over 2}.
$$

Thus the ground state is a minimum-uncertainty state.

A coherent state $\vert \alpha\rangle$ is an eigenstate of $a$:

$$
a|\alpha\rangle=\alpha|\alpha\rangle.
$$

It can be expanded as

$$
|\alpha\rangle=e^{-|\alpha|^2/2}\sum_{n=0}^{\infty}{\alpha^n\over \sqrt{n!}}|n\rangle.
$$

Under oscillator evolution, $\alpha$ rotates in the complex plane:

$$
\alpha(t)=\alpha(0)e^{-i\omega t}.
$$

This is why coherent states are the oscillator states closest to classical sinusoidal motion.

## Visual

```mermaid
graph TD
  N0["#quot;|#quot;0>, E0 = hbar omega / 2#quot;"] -->"|a dagger| N1["|1>, E1 = 3 hbar omega / 2"]
  N1 -->|a dagger| N2["|2>, E2 = 5 hbar omega / 2"]
  N2 -->|a dagger| N3["|3>, E3 = 7 hbar omega / 2"]
  N3 -->|a| N2
  N2 -->|a| N1
  N1 -->|a| N0
```

| Quantity | Expression | Meaning |
|---|---|---|
| Energy | $E_n=\hbar\omega(n+1/2)$ | evenly spaced spectrum |
| Raising | $a^\dagger\vert n\rangle=\sqrt{n+1}\vert n+1\rangle$ | adds one quantum |
| Lowering | $a\vert n\rangle=\sqrt n\vert n-1\rangle$ | removes one quantum |
| Position scale | $\sqrt{\hbar/(m\omega)}$ | natural width scale |
| Coherent probabilities | $P_n=e^{-\vert \alpha\vert ^2}\vert \alpha\vert ^{2n}/n!$ | Poisson number distribution |

## Worked example 1: Matrix element of position

**Problem.** Compute $\langle n+1\vert X\vert n\rangle$ for the oscillator.

**Method.**

1. Use the ladder form of $X$:

$$
X=\sqrt{\hbar\over 2m\omega}(a+a^\dagger).
$$

2. Insert between $\langle n+1\vert $ and $\vert n\rangle$:

$$
\langle n+1|X|n\rangle
=\sqrt{\hbar\over 2m\omega}
\left(\langle n+1|a|n\rangle+\langle n+1|a^\dagger|n\rangle\right).
$$

3. The lowering term gives

$$
a|n\rangle=\sqrt n|n-1\rangle,
$$

so

$$
\langle n+1|a|n\rangle=\sqrt n\langle n+1|n-1\rangle=0.
$$

4. The raising term gives

$$
a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle,
$$

so

$$
\langle n+1|a^\dagger|n\rangle=\sqrt{n+1}.
$$

5. Therefore

$$
\langle n+1|X|n\rangle
=\sqrt{\hbar\over 2m\omega}\sqrt{n+1}.
$$

**Checked answer.** $X$ only connects neighboring oscillator levels because it is linear in $a$ and $a^\dagger$.

## Worked example 2: Ground-state uncertainty product

**Problem.** Show that the oscillator ground state saturates the uncertainty relation.

**Method.**

1. In $\vert 0\rangle$, $a\vert 0\rangle=0$.

2. Since

$$
X=\sqrt{\hbar\over 2m\omega}(a+a^\dagger),
$$

the mean position is

$$
\langle X\rangle=0
$$

because $\langle0\vert a\vert 0\rangle=\langle0\vert a^\dagger\vert 0\rangle=0$.

3. Compute $X^2$:

$$
X^2={\hbar\over 2m\omega}(a^2+aa^\dagger+a^\dagger a+(a^\dagger)^2).
$$

4. Only $aa^\dagger$ contributes:

$$
\langle0|aa^\dagger|0\rangle=\langle0|(N+1)|0\rangle=1.
$$

Thus

$$
\Delta X=\sqrt{\langle X^2\rangle}=\sqrt{\hbar\over 2m\omega}.
$$

5. Similarly,

$$
P=-i\sqrt{m\hbar\omega\over 2}(a-a^\dagger),
$$

which gives

$$
\Delta P=\sqrt{m\hbar\omega\over 2}.
$$

6. Multiply:

$$
\Delta X\Delta P={\hbar\over 2}.
$$

**Checked answer.** The result reaches the lower bound for $[X,P]=i\hbar$.

## Code

```python
import numpy as np

dim = 6
a = np.zeros((dim, dim), dtype=complex)
for n in range(1, dim):
    a[n - 1, n] = np.sqrt(n)
adag = a.conj().T
n_op = adag @ a
h = n_op + 0.5 * np.eye(dim)

print("energies:", np.diag(h).real)
print("<2|a^dagger|1> =", adag[2, 1])
```

## Common pitfalls

- Forgetting the zero-point energy. The lowest oscillator energy is not zero.
- Treating $a$ and $a^\dagger$ as commuting variables. Their commutator is the whole reason the spectrum is shifted.
- Applying $a\vert 0\rangle=\sqrt0\vert -1\rangle$ as if $\vert -1\rangle$ were a physical state. The ladder stops at the ground state.
- Losing square-root factors in ladder actions. These factors control transition strengths and normalization.
- Confusing coherent states with number states. Coherent states have uncertain number but classical-like phase-space motion.
- Assuming the oscillator is only a mechanics example. It is the template for quantized normal modes in many-body physics and fields.
- Mixing dimensionless and dimensional $X$, $P$, $a$, and $a^\dagger$ conventions.

The ladder-operator solution is a model for how algebra can replace differential equations. Once $[a,a^\dagger]=1$ is established, the spectrum follows from positivity of $a^\dagger a$, the existence of a lowest state, and repeated laddering. The Hermite-polynomial wave functions are still important, especially for coordinate-space integrals, but they are no longer the only route to the physics. This is the contrast between Sakurai's operator-first style and the older Schiff-style wave-equation path.

Selection rules are another reason the oscillator matters. Since $X$ is proportional to $a+a^\dagger$, a perturbation linear in $X$ connects only neighboring number states. Since $X^2$ contains $a^2$, $(a^\dagger)^2$, and number-conserving terms, it connects states with $\Delta n=0,\pm2$. These rules are not memorized separately; they follow from ladder algebra. Later, angular-momentum selection rules work in a similar way, with ladder operators and tensor structure controlling which matrix elements vanish.

Coherent states should be understood as superpositions, not as slightly fuzzy number states. A coherent state has a Poisson distribution over number eigenstates and a well-defined complex amplitude that rotates in time. Its expectation values follow the classical oscillator motion, while its uncertainties remain minimal. This is why coherent states are natural for quantum optics and for connecting oscillator modes to classical waves.

When checking oscillator calculations, use dimensions. $X$ should scale like $\sqrt{\hbar/(m\omega)}$, $P$ like $\sqrt{m\hbar\omega}$, and energy like $\hbar\omega$. If a matrix element of $X$ is dimensionless or an energy correction has units of length, the algebra has lost a scale factor. Dimensionless oscillator variables are convenient, but they must be declared before use.

The oscillator is also the prototype for normal-mode quantization. A complicated coupled system can often be diagonalized into independent quadratic modes, and each mode behaves like its own oscillator with its own creation and annihilation operators. This is the conceptual bridge to phonons in solids, photons in cavities, and small oscillations in quantum fields. The single-particle oscillator page therefore carries more weight than its elementary appearance suggests.

For perturbation theory, oscillator matrix elements are best computed algebraically. Expand the perturbing power of $X$ in $a$ and $a^\dagger$, commute operators until they act on number states cleanly, and use orthogonality. Coordinate-space integrals with Hermite polynomials are valid, but they are often slower and more error-prone for low-order polynomial perturbations.

As a final check, remember that number states have definite energy but not definite phase, while coherent states have a classical-like phase but uncertain number. Many conceptual errors in oscillator physics come from trying to assign both at once. The algebra makes the tradeoff explicit through noncommuting quadratures and the number-phase structure.

That tradeoff is why the oscillator remains central in quantum optics.

## Connections

- [One-dimensional Schrodinger systems](/physics/quantum-mechanics/one-dimensional-schrodinger-systems)
- [Quantum dynamics and pictures](/physics/quantum-mechanics/quantum-dynamics-pictures)
- [Time-independent perturbation theory](/physics/quantum-mechanics/time-independent-perturbation-theory)
- [Path integral formulation](/physics/quantum-mechanics/path-integral-formulation)
- [Density operator, entanglement, and decoherence](/physics/quantum-mechanics/density-operator-entanglement-decoherence)
