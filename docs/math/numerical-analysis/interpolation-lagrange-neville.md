---
title: Lagrange Interpolation and Neville Method
sidebar_position: 6
---

# Lagrange Interpolation and Neville Method

Polynomial interpolation constructs a polynomial that passes through prescribed data points. Lagrange interpolation gives the polynomial explicitly as a weighted sum of basis polynomials, while Neville's method evaluates the same interpolating polynomial at a chosen point without first expanding all coefficients. The two views are algebraically equivalent but computationally different.

Interpolation is the local model behind numerical differentiation, Newton-Cotes integration, finite elements, and many approximation schemes. It is powerful because a polynomial is easy to evaluate, differentiate, and integrate. It is dangerous when high degree or badly spaced nodes produce oscillation that is not present in the underlying function.

## Definitions

Given distinct nodes $x_0,x_1,\ldots,x_n$ and data values $y_i=f(x_i)$, the **interpolating polynomial** $P_n$ is the unique polynomial of degree at most $n$ satisfying

$$
P_n(x_i)=y_i, \qquad i=0,1,\ldots,n.
$$

The Lagrange basis polynomial associated with node $x_i$ is

$$
L_i(x)=\prod_{\substack{0\le j\le n\\ j\ne i}}\frac{x-x_j}{x_i-x_j}.
$$

It has the cardinal property $L_i(x_j)=1$ if $i=j$ and $0$ otherwise. The Lagrange interpolant is

$$
P_n(x)=\sum_{i=0}^n y_iL_i(x).
$$

Neville's method defines recursive quantities $P_{i,j}(x)$, where $P_{i,j}$ is the value at $x$ of the interpolating polynomial through nodes $x_i,\ldots,x_j$. The recurrence is

$$
P_{i,j}(x)=\frac{(x-x_i)P_{i+1,j}(x)-(x-x_j)P_{i,j-1}(x)}{x_j-x_i}.
$$

The recurrence fills a triangular table. The left edge contains the data values, each next diagonal combines neighboring lower-degree interpolants, and the final top entry is the desired value.

## Key results

Uniqueness follows from a simple polynomial argument. If two polynomials of degree at most $n$ interpolate the same $n+1$ distinct data points, their difference has $n+1$ roots. A nonzero polynomial of degree at most $n$ cannot have that many distinct roots, so the difference must be zero.

If $f$ has $n+1$ continuous derivatives on an interval containing the nodes and $x$, then the interpolation error is

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n (x-x_i)
$$

for some $\xi$ in the interval. This formula separates the smoothness of $f$ from the geometry of the nodes. Even for a smooth function, the product term can be large near the ends of an interval when high-degree equally spaced interpolation is used.

Neville's method is best viewed as a stable organizational device for evaluation. It does not change the interpolating polynomial, but it avoids explicitly forming expanded coefficients, which can be ill-conditioned for high degree. When many evaluations are needed for the same data, barycentric Lagrange formulas are usually preferred because they precompute weights and evaluate in $O(n)$ time per point.

A practical interpolation question therefore has two parts. First, decide whether the data should be interpolated at all; noisy measurements usually call for approximation instead. Second, decide how the nodes should be used; piecewise low-degree interpolation or spline interpolation is often safer than one high-degree polynomial on a long interval.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For Lagrange interpolation and Neville's method, the input record should include nodes, data values, target evaluation points, and whether data are exact. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include node residuals, sensitivity to node placement, and comparison with lower-degree fits. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually basis construction, triangular evaluation, and reuse across many target points. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: extrapolation, high-degree oscillation, and treating noisy data as exact. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

| Feature | Lagrange form | Neville method | Practical note |
|---|---|---|---|
| Output | symbolic or evaluable polynomial form | value at one target $x$ | Neville is evaluation-focused |
| Work for one point | $O(n^2)$ if basis built directly | $O(n^2)$ recurrence | both fine for small $n$ |
| Reuse for many points | basis can be reused | recurrence repeated per point | barycentric form is better |
| Numerical risk | large basis products | triangular recurrence | node choice still dominates |

```mermaid
flowchart TB
  Data["Interpolation data<br/>nodes x_i and values y_i"] --> Need{"Need polynomial form or one value?"}

  subgraph Lagrange["Lagrange form"]
    direction TB
    Basis["build basis polynomials L_i(x)<br/>L_i(x_j)=delta_ij"] --> Sum["P(x)=sum y_i L_i(x)"]
    Sum --> EvalMany["evaluate or reuse polynomial at many x values"]
  end

  subgraph Neville["Neville evaluation"]
    direction TB
    Target["choose target x"] --> Table["triangular recurrence<br/>P#lsqb;i,j"](x) from neighboring entries"]
    Table --> EvalOne["output P#lsqb;0,n"](x)<br/>one target value"]
  end

  Need -- "symbolic or reusable" --> Basis
  Need -- "single target x" --> Target
  EvalMany --> Check["check node interpolation and endpoint oscillation"]
  EvalOne --> Check
  Check --> Result(("interpolated value or polynomial"))
```

This interpolation diagram shows the two computational contracts separately. Lagrange builds reusable basis polynomials that exactly select node values, while Neville builds a triangular table aimed at one target value. The shared check calls out the main structural risk: high-degree interpolation can oscillate strongly near endpoints even when it matches every node.

## Worked example 1: quadratic Lagrange interpolation

**Problem.** Interpolate the data

$$
(1,1),\quad (2,4),\quad (3,9)
$$

and evaluate the polynomial at $x=2.5$.

**Method.** Build the three Lagrange basis polynomials.

1. The basis polynomial for $x_0=1$ is

$$
L_0(x)=\frac{x-2}{1-2}\frac{x-3}{1-3}=\frac{(x-2)(x-3)}{2}.
$$

2. For $x_1=2$,

$$
L_1(x)=\frac{x-1}{2-1}\frac{x-3}{2-3}=-(x-1)(x-3).
$$

3. For $x_2=3$,

$$
L_2(x)=\frac{x-1}{3-1}\frac{x-2}{3-2}=\frac{(x-1)(x-2)}{2}.
$$

4. The interpolant is

$$
P_2(x)=1L_0(x)+4L_1(x)+9L_2(x).
$$

Since the data come from $f(x)=x^2$, simplification gives $P_2(x)=x^2$.

5. Therefore

$$
P_2(2.5)=2.5^2=6.25.
$$

**Checked answer.** The interpolating polynomial is exactly $x^2$, so the value at $2.5$ is $6.25$.

## Worked example 2: Neville evaluation at one point

**Problem.** Use Neville's method on the same data to compute $P(2.5)$ without expanding the polynomial.

**Method.** Let $x=2.5$ and start with

$$
P_{0,0}=1,\quad P_{1,1}=4,\quad P_{2,2}=9.
$$

1. First linear interpolation:

$$
P_{0,1}=\frac{(2.5-1)P_{1,1}-(2.5-2)P_{0,0}}{2-1}
=\frac{1.5(4)-0.5(1)}{1}=5.5.
$$

2. Second linear interpolation:

$$
P_{1,2}=\frac{(2.5-2)P_{2,2}-(2.5-3)P_{1,1}}{3-2}
=0.5(9)+0.5(4)=6.5.
$$

3. Quadratic interpolation:

$$
P_{0,2}=\frac{(2.5-1)P_{1,2}-(2.5-3)P_{0,1}}{3-1}
=\frac{1.5(6.5)+0.5(5.5)}{2}=6.25.
$$

**Checked answer.** Neville's recurrence gives the same value, $P(2.5)=6.25$, while keeping the computation focused on the target point.

## Code

```python
import numpy as np

def lagrange_eval(xs, ys, x):
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    total = 0.0
    n = len(xs)
    for i in range(n):
        basis = 1.0
        for j in range(n):
            if i != j:
                basis *= (x - xs[j]) / (xs[i] - xs[j])
        total += ys[i] * basis
    return total

def neville(xs, ys, x):
    xs = np.asarray(xs, dtype=float)
    table = np.asarray(ys, dtype=float).copy()
    n = len(xs)
    for width in range(1, n):
        for i in range(n - width):
            j = i + width
            table[i] = ((x - xs[i]) * table[i + 1]
                        - (x - xs[j]) * table[i]) / (xs[j] - xs[i])
    return table[0]

xs = [1.0, 2.0, 3.0]
ys = [1.0, 4.0, 9.0]
print(lagrange_eval(xs, ys, 2.5))
print(neville(xs, ys, 2.5))
```

## Common pitfalls

- Using high-degree equally spaced interpolation on a wide interval and expecting uniform accuracy.
- Forgetting that interpolation matches the data at the nodes but may behave poorly between or outside them.
- Expanding polynomial coefficients unnecessarily when only values are needed.
- Reusing formulas with repeated nodes; ordinary Lagrange interpolation requires distinct nodes.
- Treating the error formula as computable when $f^{(n+1)}(\xi)$ is unknown. It is often a bound, not an exact estimate.
- Extrapolating far outside the node interval. Polynomial interpolation is usually much less reliable outside the data range.

## Connections

- [divided differences and Hermite interpolation](/math/numerical-analysis/divided-differences-hermite)
- [cubic splines and parametric curves](/math/numerical-analysis/cubic-splines-parametric-curves)
- [numerical differentiation and Richardson extrapolation](/math/numerical-analysis/numerical-differentiation-richardson)
- [Newton Cotes and Romberg integration](/math/numerical-analysis/newton-cotes-romberg-integration)
