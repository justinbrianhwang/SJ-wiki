---
title: Mathematical Preliminaries and Error Analysis
sidebar_position: 2
---

# Mathematical Preliminaries and Error Analysis

Numerical analysis begins with a simple tension: calculus and linear algebra describe exact objects, while a computer stores finitely many numbers and performs finitely many operations. Error analysis does not remove that tension. It makes the size, source, and consequences of an error visible enough to decide whether an algorithm is trustworthy for the intended problem.

The same vocabulary recurs in root finding, interpolation, quadrature, differential equations, and matrix algorithms. In each setting, one must distinguish the exact object from its approximation, trace local errors into global ones, and separate mathematical convergence from practical reliability.

## Measuring error on the right scale

For an exact value $p$ and a computed approximation $\hat p$, the absolute and relative errors are

$$
E_{\mathrm{abs}}=|p-\hat p|,
\qquad
E_{\mathrm{rel}}=\frac{|p-\hat p|}{|p|}, \quad p\ne 0.
$$

Relative error is often more informative when the scale of the answer matters. An absolute error of $10^{-4}$ is excellent for a number near $10^3$ and poor for a number near $10^{-6}$. When $p=0$ or is very small, relative error is undefined or misleading, so an absolute or problem-specific scale is needed.

| Error quantity | Typical form | What it measures | Warning sign |
|---|---:|---|---|
| Absolute error | $\lvert p-\hat p\rvert$ | distance from the exact value | difficult to compare across scales |
| Relative error | $\lvert p-\hat p\rvert/\lvert p\rvert$ | error relative to answer size | unreliable when $p\approx 0$ |
| Truncation error | $O(h^q)$ | error from replacing an exact process by a finite formula | competes with roundoff as $h$ shrinks |
| Roundoff error | typically tied to unit roundoff $u$ | error from finite-precision arithmetic | cancellation, overflow, or accumulated rounding |
| Residual | $\lvert f(\hat p)\rvert$ or $\|b-A\hat x\|$ | how closely the computed value satisfies the equation | may be small despite a large forward error |

The residual and the forward error answer different questions. A small residual says that the equation is nearly satisfied. Turning that statement into a bound on the solution error requires information about conditioning.

## Convergence, rate, and stopping tests

A sequence $\{p_n\}$ converges to $p$ if, for every $\varepsilon\gt 0$, there is an index $N$ such that

$$
|p_n-p|<\varepsilon
$$

for all $n\geq N$. A computation replaces this definition with an observable stopping test such as

$$
|p_{n+1}-p_n|<\mathrm{tol},
\qquad
|f(p_n)|<\mathrm{tol},
$$

or a certified error estimate. These tests are not interchangeable. Consecutive iterates can be close because the iteration has stalled, while a small residual can coexist with a large solution error in an ill-conditioned problem.

A useful convergence claim names its hypotheses, its limiting object, and its rate. If

$$
|p_n-p|\leq C\alpha^n, \quad 0<\alpha<1,
$$

the convergence is linear. More generally, a method has order $q$ near the limit when

$$
|p_{n+1}-p|\leq C|p_n-p|^q.
$$

For $q\gt 1$, the convergence is superlinear. These are asymptotic descriptions: early iterations may instead reflect poor scaling, an unfavorable starting value, or roundoff.

## Taylor expansion as an error engine

Taylor's theorem connects exact analysis to finite formulas. If $f$ has $n+1$ continuous derivatives near $a$, then

$$
f(a+h)=f(a)+hf'(a)+\frac{h^2}{2}f''(a)+\cdots+\frac{h^n}{n!}f^{(n)}(a)+R_{n+1}(h),
$$

with the Lagrange remainder

$$
R_{n+1}(h)=\frac{h^{n+1}}{(n+1)!}f^{(n+1)}(\xi)
$$

for some $\xi$ between $a$ and $a+h$. This expansion explains, among many other results, the first-order error of a forward difference, the second-order error of a centered difference, and the exactness of Simpson's rule for cubic polynomials.

The notation $R(h)=O(h^q)$ means that constants $C$ and $h_0$ exist such that

$$
|R(h)|\leq C|h|^q
$$

whenever $0\lt \vert h\vert \lt h_0$. It is an asymptotic bound, not an equality and not a statement of the leading constant.

## Truncation and roundoff pull in opposite directions

Truncation error comes from replacing an exact or infinite process by a finite one, such as replacing a derivative with a difference quotient. Roundoff error comes from representing numbers and operations in finite precision. Decreasing a step size often reduces truncation error while amplifying roundoff, so the best step is generally a balance rather than the smallest representable number.

For a credible computation, record the exact quantity or mathematical target, the approximation, its norm and scale, and the stopping criterion. The main cost may be iterations, function evaluations, or extra stages in a higher-order method. Compare methods by the work required to reach a verified tolerance, not by asymptotic order alone.

It also helps to keep four layers distinct:

1. the continuous mathematical problem;
2. the discrete approximation;
3. the algebraic or iterative algorithm;
4. the diagnostic used to judge the result.

A high-order discretization can still be undermined by noisy data or unstable arithmetic, and a small algebraic residual does not measure modeling error.

## Error in the approximation $3.1416\approx\pi$

Taking $p=\pi$ and $\hat p=3.1416$, the absolute error is

$$
|p-\hat p|=|3.141592653589793-3.1416|
=0.000007346410207\ldots.
$$

The relative error is

$$
\frac{|p-\hat p|}{|p|}
=\frac{0.000007346410207\ldots}{3.141592653589793}
=2.338434996\times 10^{-6}\ldots,
$$

or about $0.0002338435\%$. Thus the absolute error is about $7.35\times 10^{-6}$ and the relative error is about $2.34\times 10^{-6}$; reporting $3.1416$ to five significant digits is justified.

## Reading the first neglected Taylor term

To show that

$$
\cos h+\frac{h^2}{2}=1+O(h^4),
$$

expand $\cos h$ about zero with a fourth-order remainder:

$$
\cos h=1-\frac{h^2}{2}+\frac{h^4}{24}\cos(\xi)
$$

for some $\xi$ between $0$ and $h$. Therefore

$$
\cos h+\frac{h^2}{2}=1+\frac{h^4}{24}\cos(\xi).
$$

Since $\vert \cos(\xi)\vert \leq 1$,

$$
\left|\frac{h^4}{24}\cos(\xi)\right|\leq \frac{|h|^4}{24}.
$$

The remainder is bounded by a constant times $h^4$, which proves the claim. The first nonzero neglected term usually identifies the expected order; bounding its coefficient completes the argument.

## Estimating error and observed order in Python

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

The ratio estimate is meaningful only while the errors are in the asymptotic regime and still above the roundoff floor. If the observed orders drift, refine the test carefully rather than forcing a single rate onto the data.

## Checks that catch misleading answers

- Use absolute error or a problem-specific scale when the exact value is zero or nearly zero.
- Treat $O(h^q)$ as a bound on asymptotic behavior, not as the exact error.
- Do not decrease $h$ indefinitely; difference formulas eventually lose accuracy to roundoff and cancellation.
- Pair an increment test with a residual or error estimate, since close iterates can merely indicate stagnation.
- When the exact answer is unavailable, compare independent approximations, refine the mesh or tolerance, and test the method on a nearby problem with a known result.
- If diagnostics disagree, investigate conditioning, stability, and implementation rather than averaging the evidence away.

<div className="see-also">

See also: [floating point conditioning and stability](/math/numerical-analysis/floating-point-conditioning-stability) · [bisection and fixed point iteration](/math/numerical-analysis/bisection-fixed-point) · [numerical differentiation and Richardson extrapolation](/math/numerical-analysis/numerical-differentiation-richardson) · [Newton Cotes and Romberg integration](/math/numerical-analysis/newton-cotes-romberg-integration)

</div>
