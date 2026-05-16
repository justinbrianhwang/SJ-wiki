---
title: Adaptive and Gaussian Quadrature
sidebar_position: 11
---

# Adaptive and Gaussian Quadrature

Composite quadrature spends evaluation points uniformly. That is reasonable when the integrand is equally easy everywhere, but wasteful when most of the interval is smooth and only a small region is difficult. Adaptive quadrature refines the interval only where an error indicator says refinement is needed.

Gaussian quadrature takes a different approach. Instead of equally spacing the nodes, it chooses both nodes and weights to maximize polynomial exactness. For smooth integrands, a small number of Gaussian nodes can outperform much denser Newton-Cotes rules. The price is that the nodes are less intuitive and basic Gauss rules are not naturally nested.

## Definitions

Adaptive Simpson quadrature compares one Simpson estimate on $[a,b]$ with two Simpson estimates on $[a,m]$ and $[m,b]$, where $m=(a+b)/2$. If

$$
|S(a,m)+S(m,b)-S(a,b)|
$$

is small enough, the refined estimate is accepted. Otherwise the interval is subdivided again. The correction

$$
S(a,m)+S(m,b)+\frac{S(a,m)+S(m,b)-S(a,b)}{15}
$$

comes from the fourth-order error model for Simpson's rule.

The $n$-point Gauss-Legendre rule on $[-1,1]$ has the form

$$
\int_{-1}^{1} f(x)\,dx\approx \sum_{i=1}^{n}w_if(x_i),
$$

where the nodes $x_i$ are roots of the Legendre polynomial $P_n$ and the weights $w_i$ are chosen for exactness. On a general interval $[a,b]$, use the change of variables

$$
t=\frac{b-a}{2}x+\frac{a+b}{2}.
$$

## Key results

An $n$-point Gauss-Legendre rule is exact for every polynomial of degree at most $2n-1$. This is much higher than what is possible with $n$ fixed equally spaced nodes. Orthogonality of Legendre polynomials is the reason: the error component orthogonal to all lower-degree polynomials is pushed to a higher degree.

Adaptive methods depend on local error estimation. The estimate is not a proof unless the smoothness assumptions behind the model are satisfied. A narrow spike, endpoint singularity, or oscillation between sample points can fool a local comparison. Therefore robust adaptive codes include recursion limits, minimum interval widths, and diagnostic failure returns.

Gaussian quadrature is excellent for smooth integrands on finite intervals. When the integrand has singular behavior, discontinuities, or strong endpoint features, a change of variables or adaptive subdivision may be needed first. Gauss-Kronrod rules extend Gauss nodes with extra nodes to produce nested pairs, which is why many production quadrature routines use adaptive Gauss-Kronrod rather than plain Gauss-Legendre alone.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For adaptive and Gaussian quadrature, the input record should include the integrand, interval, smoothness expectations, and cost of each function evaluation. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include a paired-rule difference, recursion depth, and comparison with a known special case when one is available. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually number of integrand evaluations and how they are distributed over the interval. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: hidden spikes, endpoint singularities, and non-nested Gaussian rules. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

| Method | Node placement | Error information | Strength | Weakness |
|---|---|---|---|---|
| Composite Simpson | uniform | global order estimate | simple and predictable | wastes points on easy regions |
| Adaptive Simpson | refined locally | local embedded estimate | targets difficult regions | can miss hidden features |
| Gauss-Legendre | optimal interior nodes | polynomial exactness | very efficient for smooth functions | basic rules not nested |
| Gauss-Kronrod | nested paired nodes | difference of paired rules | practical adaptive driver | tabulated rules needed |

```mermaid
flowchart TB
  Integral["Target integral<br/>I = integral_a^b f(x) dx"] --> Panel["Start panel #lsqb;a,b"]<br/>tolerance budget"]
  Panel --> Rule{"Choose paired rule"}

  subgraph Simpson["Adaptive Simpson"]
    direction TB
    S1["coarse Simpson on #lsqb;a,b"]"] --> S2["two half-panel Simpson estimates"]
    S2 --> SErr["error estimate from difference<br/>scaled by 1/15"]
  end

  subgraph Gauss["Gauss-Kronrod style"]
    direction TB
    G1["evaluate nested nodes<br/>Gauss nodes subset of Kronrod nodes"] --> G2["compute low-order and high-order estimates"]
    G2 --> GErr["error estimate from paired-rule difference"]
  end

  Rule -- "simple recursive rule" --> S1
  Rule -- "higher efficiency smooth integrand" --> G1
  SErr --> Test{"panel error within local tolerance?"}
  GErr --> Test
  Test -- "yes" --> Accept["accept panel contribution<br/>add corrected estimate"]
  Test -- "no" --> Split["split panel at midpoint<br/>halve or redistribute tolerance"]
  Split --> Panel
  Accept --> Queue{"unprocessed panels remain?"}
  Queue -- "yes" --> Panel
  Queue -- "no" --> Report["sum accepted panels<br/>report error estimate and depth"]
  Report --> Result(("integral estimate"))
```

This quadrature diagram shows adaptive integration as a queue of panels with paired estimates and local error tests. Simpson and Gauss-Kronrod style rules differ in node placement and efficiency, but both route through the same accept-or-split controller. The output includes not only the integral estimate but also the accumulated error and recursion depth diagnostics.

## Worked example 1: three-point Gauss rule for $x^4$

**Problem.** Use the three-point Gauss-Legendre rule on $[-1,1]$ to integrate $f(x)=x^4$.

**Method.** The three-point nodes and weights are

$$
x_1=-\sqrt{3/5},\quad x_2=0,\quad x_3=\sqrt{3/5},
$$

$$
w_1=\frac59,\quad w_2=\frac89,\quad w_3=\frac59.
$$

1. Evaluate the function values:

$$
f(0)=0,
\qquad
f\left(\pm\sqrt{3/5}\right)=\left(\frac35\right)^2=\frac{9}{25}.
$$

2. Apply the rule:

$$
Q=\frac59\frac{9}{25}+\frac89(0)+\frac59\frac{9}{25}.
$$

3. Simplify:

$$
Q=2\cdot\frac{5}{9}\cdot\frac{9}{25}=\frac{2}{5}.
$$

4. The exact integral is

$$
\int_{-1}^{1}x^4\,dx=2\int_0^1x^4\,dx=\frac25.
$$

**Checked answer.** The three-point Gauss rule gives the exact value $2/5$ because it is exact through degree five.

## Worked example 2: adaptive Simpson decision

**Problem.** For $f(x)=\sqrt{x}$ on $[0,1]$, compare one Simpson panel with two half panels.

**Method.** The exact integral is $2/3$, but the endpoint derivative is singular, so adaptation is useful.

1. One Simpson panel gives

$$
S(0,1)=\frac16\left[f(0)+4f(0.5)+f(1)\right]
=\frac16(0+4\sqrt{0.5}+1).
$$

Numerically, $S(0,1)=0.638071187\ldots$.

2. On $[0,0.5]$,

$$
S(0,0.5)=\frac{0.5}{6}\left[0+4\sqrt{0.25}+\sqrt{0.5}\right]
=0.225592231\ldots.
$$

3. On $[0.5,1]$,

$$
S(0.5,1)=\frac{0.5}{6}\left[\sqrt{0.5}+4\sqrt{0.75}+1\right]
=0.430964406\ldots.
$$

4. The refined sum is $0.656556637\ldots$, so the difference from the coarse panel is about $0.01848545$.

**Checked answer.** The large difference signals that the interval should be subdivided, especially near $0$ where the derivative is unbounded.

## Code

```python
import numpy as np
from numpy.polynomial.legendre import leggauss

def simpson_panel(f, a, b):
    m = 0.5 * (a + b)
    return (b - a) * (f(a) + 4.0 * f(m) + f(b)) / 6.0

def adaptive_simpson(f, a, b, tol=1e-10, max_depth=20):
    whole = simpson_panel(f, a, b)

    def recurse(left, right, whole_value, local_tol, depth):
        mid = 0.5 * (left + right)
        s_left = simpson_panel(f, left, mid)
        s_right = simpson_panel(f, mid, right)
        delta = s_left + s_right - whole_value
        if depth == 0 or abs(delta) <= 15.0 * local_tol:
            return s_left + s_right + delta / 15.0
        return (recurse(left, mid, s_left, local_tol / 2.0, depth - 1)
                + recurse(mid, right, s_right, local_tol / 2.0, depth - 1))

    return recurse(a, b, whole, tol, max_depth)

def gauss_legendre(f, a, b, n):
    nodes, weights = leggauss(n)
    mapped = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    return 0.5 * (b - a) * np.dot(weights, f(mapped))

print(gauss_legendre(lambda x: x**4, -1.0, 1.0, 3))
print(adaptive_simpson(np.sqrt, 0.0, 1.0), 2.0 / 3.0)
```

## Common pitfalls

- Assuming an adaptive error estimate is a rigorous bound. It is a model-based indicator.
- Allowing unbounded recursion near singularities without reporting failure.
- Using Gaussian quadrature on a nonsmooth integrand without subdivision or transformation.
- Forgetting the interval change-of-variables factor $(b-a)/2$.
- Comparing Gaussian rules only by node count. Smoothness, cost per function evaluation, and nesting also matter.

## Connections

- [Newton Cotes and Romberg integration](/math/numerical-analysis/newton-cotes-romberg-integration)
- [numerical differentiation and Richardson extrapolation](/math/numerical-analysis/numerical-differentiation-richardson)
- [finite difference methods for PDEs](/math/numerical-analysis/finite-difference-pdes)
- [least squares and Chebyshev approximation](/math/numerical-analysis/least-squares-chebyshev-approximation)
