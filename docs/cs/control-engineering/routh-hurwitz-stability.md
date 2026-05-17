---
title: Routh-Hurwitz Stability
sidebar_position: 8
---

# Routh-Hurwitz Stability

Stability is the nonnegotiable requirement in feedback design. A controller that improves speed or accuracy is useless if the natural response grows without bound. Nise treats stability first through pole locations, then through the Routh-Hurwitz criterion, which determines how many roots of a polynomial lie in the right half-plane without explicitly solving for the roots.

![A feedback control block diagram shows compensators wrapped around a plant.](https://commons.wikimedia.org/wiki/Special:FilePath/Control_System.svg)

*Figure: The standard feedback loop keeps control pages tied to the plant-controller interface. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Control_System.svg), Inductiveload, public domain.*

The criterion is practical because closed-loop characteristic equations quickly become high order. For a feedback system, the denominator may include controller, plant, sensor, and load dynamics. Routh-Hurwitz lets the designer test stability and find allowable gain ranges by arithmetic on polynomial coefficients.

## Definitions

For continuous-time linear time-invariant systems, the closed-loop characteristic equation is commonly written

$$
D(s)=a_ns^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0=0.
$$

A system is **asymptotically stable** when all closed-loop poles are in the open left half-plane. It is **unstable** when any pole is in the right half-plane or when repeated poles lie on the imaginary axis. It is **marginally stable** in the classical natural-response sense when simple poles lie on the imaginary axis and all remaining poles are in the left half-plane.

The **BIBO stability** definition says that every bounded input must produce a bounded output. For rational transfer functions with no unstable hidden cancellations, BIBO stability requires all transfer-function poles to lie in the open left half-plane. Under BIBO, even simple imaginary-axis poles are not stable because sinusoidal or step-like inputs can produce unbounded output.

The **Routh array** is a table built from the coefficients of $D(s)$. The number of sign changes in the first column equals the number of right-half-plane roots, provided the standard construction is used with special cases handled correctly.

For a fourth-order polynomial

$$
a_4s^4+a_3s^3+a_2s^2+a_1s+a_0,
$$

the array begins:

| Power | Column 1 | Column 2 | Column 3 |
|---|---:|---:|---:|
| $s^4$ | $a_4$ | $a_2$ | $a_0$ |
| $s^3$ | $a_3$ | $a_1$ | $0$ |
| $s^2$ | $b_1$ | $b_2$ | $0$ |
| $s^1$ | $c_1$ | $0$ | $0$ |
| $s^0$ | $d_1$ | $0$ | $0$ |

where

$$
b_1=\frac{a_3a_2-a_4a_1}{a_3},\quad
b_2=\frac{a_3a_0-a_4(0)}{a_3}=a_0,
$$

and subsequent rows follow the same determinant-like pattern.

## Key results

A necessary condition for all roots to be in the left half-plane is that all polynomial coefficients have the same sign and none are zero. This is not sufficient for order three and above, but it is a fast first check.

The Routh-Hurwitz algorithm:

1. Fill the first two rows with alternating polynomial coefficients.
2. Compute each lower-row entry from the two rows above it.
3. Inspect the first column.
4. Count sign changes to obtain the number of right-half-plane roots.
5. For stability, require no sign changes and no special-case imaginary-axis behavior.

Two special cases require care. If the first element of a row is zero but the row is not all zero, replace that zero by a small positive $\epsilon$, complete the table, and evaluate sign changes as $\epsilon\to0^+$. This usually indicates roots near the imaginary axis or a structural difficulty in the array.

If an entire row becomes zero, the polynomial has roots symmetrically located about the origin. Construct an auxiliary polynomial from the row immediately above the zero row, differentiate it, and replace the zero row with the derivative coefficients. The auxiliary polynomial can also reveal imaginary-axis roots.

State-space stability uses the same pole-location idea. For

$$
\dot{\mathbf x}=A\mathbf x+B\mathbf u,
$$

the characteristic equation is

$$
\det(sI-A)=0.
$$

Routh-Hurwitz can be applied directly to that polynomial without converting the model to a transfer function.

Routh-Hurwitz is especially useful for gain-range problems because the entries in the first column become algebraic expressions in the gain. Instead of computing roots for many values of $K$, the designer imposes sign conditions on those expressions. The result is usually an interval such as $0\lt K\lt 20$ or a set of inequalities involving physical parameters. This matches engineering design better than a single root calculation because components have tolerances and gains may be adjusted during commissioning.

The row-of-zeros case has a concrete interpretation. It indicates that part of the polynomial is even or odd in a way that creates roots symmetric about the origin. For stability analysis, this often means imaginary-axis roots and therefore a boundary of stability. The auxiliary polynomial is not a trick for filling a table; it is the polynomial factor responsible for the symmetric roots. Differentiating it supplies the information needed to continue counting roots.

The epsilon case should also be interpreted rather than applied mechanically. A zero in the first column prevents the next row from being computed because the algorithm would divide by zero. Replacing it with $\epsilon$ asks how the sign pattern behaves for a tiny positive perturbation. If the limiting signs change, the system has right-half-plane roots. If the limiting behavior is ambiguous, direct root calculation or symbolic factoring may be appropriate.

For low-order systems, Routh-Hurwitz reduces to familiar coefficient conditions. A first-order polynomial $s+a$ is stable if $a\gt 0$. A second-order polynomial $s^2+as+b$ is stable if $a\gt 0$ and $b\gt 0$. A third-order polynomial $s^3+a_2s^2+a_1s+a_0$ requires positive coefficients and $a_2a_1\gt a_0$. This last inequality is the first point where positive coefficients alone stop being sufficient.

Routh-Hurwitz tells how many roots are in the right half-plane, not where they are. It therefore answers the yes-or-no stability question and supports gain-boundary calculations, but it does not directly give settling time, overshoot, or damping ratio. Once a stable range is known, root locus, numerical poles, or time simulation is still needed to judge performance. A system can be stable and still unacceptable because it is slow, oscillatory, sensitive, or inaccurate.

## Visual

```text
              Im
               ^
 unstable      |      unstable
 RHP poles     |      RHP poles
               |
---------------+----------------> Re
 stable LHP    |  boundary: j-axis
 poles         |
```

| Pole location | Natural response term | Stability implication |
|---|---|---|
| $s=-a$, $a\gt 0$ | $e^{-at}$ | decays |
| $s=+a$, $a\gt 0$ | $e^{at}$ | grows without bound |
| $s=\pm j\omega$ simple | sinusoid | marginal natural response, not BIBO stable |
| repeated $s=\pm j\omega$ | $t\sin\omega t$ terms | unstable |
| $s=-\sigma\pm j\omega$ | decaying sinusoid | stable mode |

## Worked example 1: Routh test for a cubic

Problem: Determine the stability of

$$
D(s)=s^3+6s^2+11s+6.
$$

Method:

1. Build the first two rows:

| Power | Column 1 | Column 2 |
|---|---:|---:|
| $s^3$ | $1$ | $11$ |
| $s^2$ | $6$ | $6$ |

2. Compute the $s^1$ first entry:

$$
b_1=\frac{6(11)-1(6)}{6}=\frac{66-6}{6}=10.
$$

3. The $s^1$ row is:

| Power | Column 1 | Column 2 |
|---|---:|---:|
| $s^1$ | $10$ | $0$ |

4. The $s^0$ row is the constant:

| Power | Column 1 | Column 2 |
|---|---:|---:|
| $s^0$ | $6$ | $0$ |

5. Inspect the first column:

$$
1,\ 6,\ 10,\ 6.
$$

There are no sign changes.

Checked answer: all roots are in the left half-plane, so the system is stable. In fact, $D(s)=(s+1)(s+2)(s+3)$.

## Worked example 2: gain range for stability

Problem: A unity-feedback system has characteristic equation

$$
D(s)=s^3+4s^2+5s+K.
$$

Find the range of $K$ for closed-loop stability.

Method:

1. Necessary coefficient conditions require

$$
K>0.
$$

2. Build the Routh array:

| Power | Column 1 | Column 2 |
|---|---:|---:|
| $s^3$ | $1$ | $5$ |
| $s^2$ | $4$ | $K$ |
| $s^1$ | $(4\cdot5-1\cdot K)/4$ | $0$ |
| $s^0$ | $K$ | $0$ |

3. Simplify the $s^1$ entry:

$$
\frac{20-K}{4}.
$$

4. For stability, all first-column entries must have the same positive sign:

$$
1>0,\quad 4>0,\quad \frac{20-K}{4}>0,\quad K>0.
$$

5. Solve:

$$
20-K>0\Rightarrow K<20.
$$

Together,

$$
0<K<20.
$$

Checked answer: the closed-loop system is stable for $0\lt K\lt 20$. At $K=20$, the $s^1$ row becomes zero, indicating an imaginary-axis boundary case.

## Code

```python
import numpy as np

def routh_first_column(coeffs):
    n = len(coeffs) - 1
    cols = int(np.ceil((n + 1) / 2))
    table = np.zeros((n + 1, cols), dtype=float)
    table[0, :len(coeffs[0::2])] = coeffs[0::2]
    table[1, :len(coeffs[1::2])] = coeffs[1::2]
    eps = 1e-9
    for i in range(2, n + 1):
        if abs(table[i - 1, 0]) < eps:
            table[i - 1, 0] = eps
        for j in range(cols - 1):
            table[i, j] = (
                table[i - 1, 0] * table[i - 2, j + 1]
                - table[i - 2, 0] * table[i - 1, j + 1]
            ) / table[i - 1, 0]
    return table[:, 0], table

coeffs = [1, 4, 5, 10]
first_col, table = routh_first_column(coeffs)
sign_changes = np.sum(np.sign(first_col[:-1]) != np.sign(first_col[1:]))
print(table)
print("first column:", first_col)
print("right-half-plane roots:", sign_changes)
print("numeric roots:", np.roots(coeffs))
```

## Common pitfalls

- Testing open-loop poles when the question asks about closed-loop stability.
- Assuming positive coefficients are sufficient for high-order stability.
- Multiplying a Routh row by a negative number. Positive scaling is harmless; negative scaling changes sign-change counting.
- Mishandling the row-of-zeros case instead of using the auxiliary polynomial.
- Ignoring pole-zero cancellations. An unstable hidden mode may not appear in a simplified transfer function.
- Confusing marginal natural-response stability with BIBO stability.

## Connections

- [Time response](/cs/control-engineering/time-response-first-and-second-order) explains how pole locations shape decay and oscillation.
- [Root locus](/cs/control-engineering/root-locus-sketching-and-analysis) shows how poles move as gain changes.
- [Nyquist margins](/cs/control-engineering/nyquist-and-frequency-stability-margins) gives a frequency-domain stability test.
- [State-space modeling](/cs/control-engineering/state-space-modeling-and-conversions) uses $\det(sI-A)$ for stability.
- [Complex functions](/math/engineering-math/complex-functions-and-analyticity) supports the half-plane and contour ideas used later.
