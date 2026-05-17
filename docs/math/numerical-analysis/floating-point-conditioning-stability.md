---
title: Floating Point Conditioning and Stability
sidebar_position: 3
---

# Floating Point Conditioning and Stability

Floating-point arithmetic is the working language of most numerical algorithms. It represents a real number by a sign, a finite significand, and an exponent, so almost every real result is rounded before it is stored. The resulting errors are usually tiny one operation at a time, but a poor formula can amplify them until the final answer is meaningless.

![A matrix multiplication diagram highlights row and column products.](https://commons.wikimedia.org/wiki/Special:FilePath/Matrix_multiplication_diagram.svg)

*Figure: A matrix multiplication diagram makes the row-column structure of linear algebra visible. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Matrix_multiplication_diagram.svg), Bilou, CC BY-SA 3.0.*

Conditioning and stability give two different diagnoses. Conditioning belongs to the mathematical problem: does a small perturbation in the data cause a small or large perturbation in the answer? Stability belongs to the algorithm: does the chosen computational path behave like the exact solution of a nearby problem, or does it create avoidable error?

## Definitions

A normalized floating-point number has the conceptual form

$$
x=\pm (d_0.d_1d_2\cdots d_{t-1})_\beta\,\beta^e,
$$

where $\beta$ is the base, $t$ is the precision, and $e$ is an exponent in an allowed range. A standard model for rounding a real number $x$ to floating point is

$$
fl(x)=x(1+\delta),\qquad |\delta|\le u,
$$

where $u$ is the unit roundoff. In IEEE double precision with rounding to nearest, $u=2^{-53}$. Some texts call $2u$ machine epsilon, because it is the distance from $1$ to the next larger representable number. The distinction matters when comparing published formulas, but the practical message is the same: each ordinary rounded operation introduces a very small relative perturbation.

For a scalar function $f$, the relative condition number is

$$
\kappa_f(x)=\left|\frac{x f'(x)}{f(x)}\right|,
$$

provided $x\ne 0$ and $f(x)\ne 0$. It estimates the relative output change caused by a small relative input change:

$$
\frac{|\Delta f|}{|f(x)|}\approx \kappa_f(x)\frac{|\Delta x|}{|x|}.
$$

An algorithm is **forward stable** if its computed answer has a small forward error for the problem class of interest. It is **backward stable** if the computed answer is the exact solution of a nearby problem. Backward stability is often stronger and more useful because it separates the algorithm from the conditioning of the original problem.

## Key results

The central first-order model is that each basic operation satisfies

$$
fl(x\circ y)=(x\circ y)(1+\delta),\qquad |\delta|\le u,
$$

for $\circ\in\{+,-,\times,/\}$, assuming no overflow, underflow, or exceptional operation. This model lets an error analysis replace a long floating-point calculation by an exact calculation with many tiny perturbations. Products of several factors $(1+\delta_i)$ are often summarized by a single factor $1+\theta_n$, where $\vert \theta_n\vert $ is roughly bounded by a small multiple of $nu$ when $nu$ is small.

Subtractive cancellation is the most common local source of accuracy loss. If $x$ and $y$ are nearly equal, then $x-y$ may be small even though $x$ and $y$ each contain rounding errors of ordinary size. The absolute error in the subtraction may be moderate, but the relative error in the small difference can be huge. Cancellation is not always avoidable, but formulas should avoid subtracting nearly equal quantities when an algebraically equivalent stable form is available.

Conditioning sets a limit on what any algorithm can promise. If $\kappa(A)$ is large for a linear system $Ax=b$, even a backward-stable solver can have large forward error. A useful rule of thumb is

$$
\frac{\|x-\hat{x}\|}{\|x\|}\lesssim \kappa(A)\cdot \text{relative backward error}.
$$

Thus a stable algorithm does not make an ill-conditioned problem well-conditioned. It only avoids adding unnecessary instability. When a result looks suspicious, the disciplined workflow is to check scale, residual, backward error, condition number, and then the algorithmic formula. Skipping directly to more precision can hide a bad formulation without explaining it.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For floating-point conditioning and stability, the input record should include the mathematical problem, data scale, arithmetic precision, and algorithmic formula. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include forward error, backward error, residuals, and condition estimates. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually operation count, cancellation exposure, and precision requirements. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: ill-conditioning mistaken for instability and stable-looking formulas with hidden cancellation. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

```text
Floating-point numbers are dense near zero and sparse at large magnitudes.

small scale:     0     .     .     .     .     .
                 |-----|-----|-----|-----|-----|

large scale:     1e6          1e6+gap          1e6+2gap
                 |------------|----------------|

A real result between two adjacent machine numbers must be rounded to one of them.
```

| Concept | Belongs to | Good sign | Bad sign |
|---|---|---|---|
| Conditioning | Problem | small condition number | output changes wildly after tiny data changes |
| Stability | Algorithm | computed answer solves nearby problem | algebraically equivalent stable formula disagrees |
| Forward error | Result | $\|x-\hat x\|$ small | many correct residual digits but few answer digits |
| Backward error | Algorithm-data pair | small perturbation explains result | large perturbation needed to justify result |

## Worked example 1: stable evaluation of a small difference

**Problem.** Evaluate

$$
q(x)=\frac{1-\cos x}{x^2}
$$

for small $x$, and explain why the direct formula can fail.

**Method.** Rewrite the numerator with the identity $1-\cos x=2\sin^2(x/2)$.

1. Direct evaluation computes $\cos x$ first. When $x=10^{-8}$, $\cos x$ is so close to $1$ that subtracting it from $1$ loses most significant digits.

2. Use the identity:

$$
q(x)=\frac{2\sin^2(x/2)}{x^2}.
$$

3. For small $x$, $\sin(x/2)\approx x/2$, so

$$
\frac{2\sin^2(x/2)}{x^2}\approx \frac{2(x/2)^2}{x^2}=\frac12.
$$

4. The stable expression avoids forming a difference of two numbers that both round to values extremely close to $1$.

**Checked answer.** Both formulas are mathematically equal, and the limit is $1/2$. The sine-squared form preserves the small quantity directly, so it remains accurate for much smaller $x$ than the direct subtraction.

## Worked example 2: condition number of a square root

**Problem.** Find the relative condition number of $f(x)=\sqrt{x}$ at $x=4$ and interpret it.

**Method.** Use the scalar formula.

1. Compute the derivative:

$$
f'(x)=\frac{1}{2\sqrt{x}}.
$$

2. Substitute into the condition number:

$$
\kappa_f(x)=\left|\frac{x f'(x)}{f(x)}\right|
=\left|\frac{x}{2\sqrt{x}\sqrt{x}}\right|=\frac12.
$$

3. At $x=4$, the same value holds:

$$
\kappa_f(4)=\frac12.
$$

4. If the input has relative error about $10^{-8}$, the output should have relative error about $5\times 10^{-9}$, before accounting for arithmetic inside the algorithm.

**Checked answer.** A small relative input error is roughly halved in the output. The square-root problem is well-conditioned away from zero. If a computed square root at $x=4$ is inaccurate, the cause is more likely the algorithm or implementation than the conditioning of the mathematical problem.

## Code

```python
import numpy as np

def naive_ratio(x):
    return (1.0 - np.cos(x)) / (x * x)

def stable_ratio(x):
    return 2.0 * np.sin(0.5 * x) ** 2 / (x * x)

def scalar_condition(f, fp, x):
    y = f(x)
    if x == 0 or y == 0:
        raise ValueError("relative condition number is not defined here")
    return abs(x * fp(x) / y)

xs = np.array([1e-2, 1e-6, 1e-8, 1e-10], dtype=float)
for x in xs:
    print(f"x={x:8.1e} direct={naive_ratio(x): .16e} stable={stable_ratio(x): .16e}")

kappa_sqrt_4 = scalar_condition(np.sqrt, lambda t: 0.5 / np.sqrt(t), 4.0)
print("condition number for sqrt at 4:", kappa_sqrt_4)
```

## Common pitfalls

- Calling an algorithm unstable just because the problem is ill-conditioned. First estimate the problem sensitivity.
- Trusting algebraic equivalence in floating-point arithmetic. Equivalent exact formulas can have very different cancellation behavior.
- Ignoring overflow and underflow in the standard model. The simple $fl(x)=x(1+\delta)$ model assumes ordinary rounded operations.
- Reporting only a residual for an ill-conditioned linear system. Pair residuals with a condition estimate.
- Comparing floating-point numbers with exact equality when the values came from rounded computations.
- Increasing precision before checking the formula. Higher precision may postpone cancellation without fixing the algorithmic cause.

## Connections

- [mathematical preliminaries and error analysis](/math/numerical-analysis/mathematical-preliminaries-error-analysis)
- [Gaussian elimination pivoting and LU](/math/numerical-analysis/gaussian-elimination-pivoting-lu)
- [matrix factorizations and special systems](/math/numerical-analysis/matrix-factorizations-special-systems)
- [conjugate gradient and iterative refinement](/math/numerical-analysis/conjugate-gradient-iterative-refinement)
