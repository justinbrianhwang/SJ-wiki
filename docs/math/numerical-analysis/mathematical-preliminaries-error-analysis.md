---
title: Mathematical Preliminaries and Error Analysis
sidebar_position: 2
---

# Mathematical Preliminaries and Error Analysis

Numerical analysis begins with a simple tension: calculus and linear algebra describe exact objects, while a computer stores finitely many numbers and performs finitely many operations. The purpose of error analysis is not to make this tension disappear. It is to make the size, direction, and consequences of the error visible enough that an algorithm can be trusted for the intended problem.

![Carl Friedrich Gauss is shown in a formal painted portrait.](https://commons.wikimedia.org/wiki/Special:FilePath/Carl_Friedrich_Gauss.jpg)

*Figure: Carl Friedrich Gauss is central to number theory, linear algebra, statistics, and numerical methods. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Carl_Friedrich_Gauss.jpg), Gottlieb Biermann after Christian Albrecht Jensen, public domain.*

This page sits before root finding, interpolation, quadrature, differential equations, and matrix algorithms because every later method uses the same vocabulary. We compare exact and approximate quantities, track how local truncation errors become global errors, and distinguish mathematical convergence from practical reliability.

## Definitions

An **exact value** is the mathematical quantity being approximated, usually denoted $p$, $y(t)$, $I$, or $x$. An **approximation** is a computed value such as $p_n$, $w_i$, $Q_h$, or $\hat{x}$. The **absolute error** and **relative error** are

$$
E_{abs}=|p-\hat p|,
\qquad
E_{rel}=\frac{|p-\hat p|}{|p|}, \quad p\ne 0.
$$

Relative error is usually more meaningful when the scale of the exact answer matters. An absolute error of $10^{-4}$ is excellent for a number near $10^3$ and poor for a number near $10^{-6}$. When $p=0$ or is very small, relative error can be undefined or misleading, so the absolute scale must be reported.

A sequence $\{p_n\}$ **converges** to $p$ if for every tolerance $\varepsilon\gt 0$ there is an index $N$ such that $\vert p_n-p\vert \lt\varepsilon$ for all $n\ge N$. In computations, this definition is turned into a stopping rule such as $\vert p_{n+1}-p_n\vert \lt\mathrm{tol}$, $\vert f(p_n)\vert \lt\mathrm{tol}$, or an estimated error bound. These tests are not equivalent, so the chosen test should match the question being answered.

The notation $O(h^q)$ means that, as $h\to 0$, the magnitude of the term is bounded by a constant times $h^q$. More precisely, $R(h)=O(h^q)$ if there are constants $C$ and $h_0$ such that $\vert R(h)\vert \le C\vert h\vert ^q$ whenever $0\lt \vert h\vert \lt h_0$. This notation is central to Taylor formulas, finite differences, interpolation remainders, and quadrature error estimates.

## Key results

Taylor's theorem is the main bridge between exact analysis and numerical formulas. If $f$ has $n+1$ continuous derivatives near $a$, then

$$
f(a+h)=f(a)+hf'(a)+\frac{h^2}{2}f''(a)+\cdots+\frac{h^n}{n!}f^{(n)}(a)+R_{n+1}(h),
$$

where one common form of the remainder is

$$
R_{n+1}(h)=\frac{h^{n+1}}{(n+1)!}f^{(n+1)}(\xi)
$$

for some $\xi$ between $a$ and $a+h$. The theorem explains why the forward difference has first-order truncation error, the centered difference has second-order truncation error, and Simpson's rule is exact for cubic polynomials.

A typical convergence statement has three parts: the hypotheses under which the result is true, the limiting object, and the rate. If

$$
|p_n-p|\le C\alpha^n, \quad 0\lt\alpha\lt 1,
$$

then convergence is linear. If

$$
|p_{n+1}-p|\le C|p_n-p|^q, \quad q\gt 1,
$$

then the method has order $q$ near the limit. These asymptotic rates describe late-stage behavior; early iterations can be dominated by poor scaling, bad starting values, or roundoff.

Error analysis also separates **truncation error** from **roundoff error**. Truncation error is caused by replacing an infinite or exact mathematical process with a finite one, such as replacing a derivative by a difference quotient. Roundoff error is caused by storing and operating on finite precision numbers. Reducing the step size $h$ often lowers truncation error but can increase roundoff amplification, so the best step is frequently a balance rather than the smallest representable number.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For mathematical preliminaries and error analysis, the input record should include the exact quantity, approximation, norm, scale, and stopping criterion. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include absolute error, relative error, residuals, and observed convergence rates. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually iterations, function evaluations, and the balance between truncation and roundoff. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: using the wrong error scale, overreading asymptotic notation, and ignoring roundoff. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

| Error idea | Typical symbol | What it measures | Common control knob | Warning sign |
|---|---:|---|---|---|
| Absolute error | $\vert p-\hat p\vert $ | Physical distance from exact value | More iterations, smaller step | Misleading across scales |
| Relative error | $\vert p-\hat p\vert /\vert p\vert $ | Error compared with answer size | Scaling and normalization | Bad when $p\approx 0$ |
| Truncation error | $O(h^q)$ | Error from a finite formula | Decrease $h$ or raise order | Competes with roundoff |
| Roundoff error | about $u$ per rounded operation | Error from finite precision | Stable formula, rescaling | Cancellation, overflow |
| Residual | $\vert f(\hat p)\vert $ or $\|b-A\hat x\|$ | Equation mismatch | Iteration refinement | Small residual can hide ill-conditioning |

## Worked example 1: absolute and relative error

**Problem.** A computation gives $\hat p=3.1416$ for $p=\pi$. Find the absolute and relative error, and interpret the result.

**Method.** Use the definitions directly.

1. Compute the absolute error:

$$
|p-\hat p|=|3.141592653589793-3.1416|=0.000007346410207\ldots.
$$

2. Compute the relative error:

$$
\frac{|p-\hat p|}{|p|}
=\frac{0.000007346410207\ldots}{3.141592653589793}
=2.338434996\times 10^{-6}\ldots.
$$

3. Convert to a percent if desired:

$$
100E_{rel}\approx 0.0002338435\%.
$$

**Checked answer.** The approximation has absolute error about $7.35\times 10^{-6}$ and relative error about $2.34\times 10^{-6}$. The final digit is not exact, but the first five significant digits are reliable for ordinary reporting.

## Worked example 2: Taylor order check

**Problem.** Show that

$$
\cos h+\frac{h^2}{2}=1+O(h^4)
$$

as $h\to 0$.

**Method.** Expand $\cos h$ about $0$ through the fourth-degree term.

1. Taylor's theorem gives

$$
\cos h=1-\frac{h^2}{2}+\frac{h^4}{24}\cos(\xi)
$$

for some $\xi$ between $0$ and $h$.

2. Add $h^2/2$ to both sides:

$$
\cos h+\frac{h^2}{2}=1+\frac{h^4}{24}\cos(\xi).
$$

3. Since $\vert \cos(\xi)\vert \le 1$,

$$
\left|\frac{h^4}{24}\cos(\xi)\right|\le \frac{|h|^4}{24}.
$$

**Checked answer.** The remainder is bounded by a constant times $h^4$, so $\cos h+h^2/2=1+O(h^4)$. This check is typical: identify the first nonzero neglected Taylor term, then bound its coefficient.

## Code

```python
import math

def absolute_error(true_value, approx):
    return abs(true_value - approx)

def relative_error(true_value, approx):
    if true_value == 0:
        raise ValueError("relative error is undefined when the exact value is zero")
    return abs(true_value - approx) / abs(true_value)

def observed_order(errors, hs):
    """Estimate q from error ~= C h**q using consecutive data."""
    orders = []
    for e1, e2, h1, h2 in zip(errors, errors[1:], hs, hs[1:]):
        orders.append(math.log(e2 / e1) / math.log(h2 / h1))
    return orders

p = math.pi
p_hat = 3.1416
print("absolute", absolute_error(p, p_hat))
print("relative", relative_error(p, p_hat))

hs = [0.2, 0.1, 0.05, 0.025]
errors = [abs((math.cos(h) + 0.5 * h * h) - 1.0) for h in hs]
print("errors", errors)
print("observed orders", observed_order(errors, hs))
```

## Common pitfalls

- Reporting a residual as if it were automatically a forward error. A small residual only says the equation is nearly satisfied; conditioning determines how far the computed answer may be from the exact answer.
- Using relative error when the exact value is zero or close to zero. In that case, report absolute error or use a problem-specific scale.
- Treating $O(h^q)$ as an equality. It describes an asymptotic bound, not the exact leading constant.
- Decreasing $h$ without considering roundoff. Difference formulas often get worse after $h$ becomes too small.
- Stopping an iteration because consecutive iterates are close even though the residual is still large. A stalled sequence can pass an increment test.

## Connections

- [floating point conditioning and stability](/math/numerical-analysis/floating-point-conditioning-stability)
- [bisection and fixed point iteration](/math/numerical-analysis/bisection-fixed-point)
- [numerical differentiation and Richardson extrapolation](/math/numerical-analysis/numerical-differentiation-richardson)
- [Newton Cotes and Romberg integration](/math/numerical-analysis/newton-cotes-romberg-integration)
