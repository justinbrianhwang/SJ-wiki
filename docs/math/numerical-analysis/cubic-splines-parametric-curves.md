---
title: Cubic Splines and Parametric Curves
sidebar_position: 8
---

# Cubic Splines and Parametric Curves

Cubic splines replace one high-degree interpolating polynomial by many low-degree pieces joined smoothly. This gives the local flexibility of piecewise approximation while preserving enough smoothness for plotting, differentiation, and physical modeling. The result is usually more stable and visually reasonable than forcing a single polynomial through many points.

Parametric curves use the same idea when the data describe a path rather than a single-valued function. Instead of writing $y=f(x)$, a curve is represented by $x=x(t)$ and $y=y(t)$. This is essential for loops, vertical tangents, closed curves, and computer graphics paths.

## Definitions

Given nodes

$$
a=x_0\lt x_1\lt \cdots \lt x_n=b,
$$

a cubic spline $S$ is a function such that each restriction $S_i$ on $[x_i,x_{i+1}]$ is a cubic polynomial, $S(x_i)=f(x_i)$ at every node, and the first and second derivatives match at interior nodes:

$$
S_{i-1}'(x_i)=S_i'(x_i),\qquad S_{i-1}''(x_i)=S_i''(x_i).
$$

A **natural cubic spline** additionally satisfies

$$
S''(x_0)=0,\qquad S''(x_n)=0.
$$

A **clamped cubic spline** instead prescribes endpoint slopes $S'(x_0)$ and $S'(x_n)$. Natural conditions model a relaxed curve with zero endpoint bending, while clamped conditions are better when endpoint derivatives are known.

For a parametric curve, two splines are constructed using a common parameter:

$$
x=x(t),\qquad y=y(t).
$$

The parameter may be uniform, chord length, or centripetal. Chord-length parameterization often reduces artifacts when points are unevenly spaced.

## Key results

The spline conditions lead to a tridiagonal linear system for the second derivative values $M_i=S''(x_i)$. Let $h_i=x_{i+1}-x_i$. For a natural spline, $M_0=M_n=0$, and the interior equations are

$$
h_{i-1}M_{i-1}+2(h_{i-1}+h_i)M_i+h_iM_{i+1}
=6\left(\frac{y_{i+1}-y_i}{h_i}-\frac{y_i-y_{i-1}}{h_{i-1}}\right).
$$

Once the $M_i$ are known, the spline on $[x_i,x_{i+1}]$ can be written as

$$
\begin{aligned}
S_i(x)&=\frac{M_i(x_{i+1}-x)^3}{6h_i}+\frac{M_{i+1}(x-x_i)^3}{6h_i} \\
&\quad+\left(y_i-\frac{M_i h_i^2}{6}\right)\frac{x_{i+1}-x}{h_i}
+\left(y_{i+1}-\frac{M_{i+1} h_i^2}{6}\right)\frac{x-x_i}{h_i}.
\end{aligned}
$$

The tridiagonal structure is important. A spline with many knots can be built in linear time using the Thomas algorithm, instead of using a dense linear solve. For smooth $f$ and well-spaced knots, cubic splines often achieve fourth-order accuracy in function values, but endpoint behavior depends strongly on the boundary conditions.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For cubic splines and parametric curves, the input record should include knot locations, boundary conditions, parameterization, and data reliability. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include continuity of values and derivatives, endpoint behavior, and local interpolation checks. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually tridiagonal solves and evaluation cost per segment. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: wrong boundary assumptions, uneven parameter spacing, and overinterpreting noisy derivative behavior. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

```mermaid
flowchart TB
  Knots["Data knots<br/>(x_i, y_i), i = 0..n"] --> BC{"Boundary condition"}
  BC -- "natural" --> Natural["S''(x0)=S''(xn)=0"]
  BC -- "clamped" --> Clamped["specified endpoint slopes"]
  BC -- "not-a-knot" --> Nak["third-derivative continuity near ends"]
  BC -- "periodic" --> Periodic["wrap values and derivatives"]

  Natural --> Equations
  Clamped --> Equations
  Nak --> Equations
  Periodic --> Equations
  Equations["assemble continuity equations<br/>value, first derivative, second derivative"] --> Tri["tridiagonal or cyclic system<br/>unknown second derivatives or slopes"]
  Tri --> Solve["Thomas algorithm or cyclic solve"]
  Solve --> Segments["local cubic pieces<br/>S_i(x) on #lsqb;x_i, x_{i+1}"]"]
  Segments --> Eval["evaluate only the containing segment"]

  subgraph Parametric["Parametric curve option"]
    direction TB
    Param["choose parameter t_i<br/>uniform, chord length, centripetal"] --> Xspline["spline x(t)"]
    Param --> Yspline["spline y(t)"]
    Xspline --> Curve["curve (x(t), y(t))"]
    Yspline --> Curve
  end

  Knots --> Param
  Eval --> Check["check continuity and endpoint behavior"]
  Curve --> Check
  Check --> Result(("spline or parametric curve"))
```

The spline diagram shows why cubic splines are local rather than one global high-degree polynomial. Boundary choices feed a structured continuity system, usually tridiagonal, whose solution defines one cubic per knot interval. The parametric branch makes clear that curves are built by splining coordinates against a chosen parameter, so spacing choices affect the resulting geometry.

| Boundary condition | Extra information | Best use | Risk |
|---|---|---|---|
| Natural | $S''(x_0)=S''(x_n)=0$ | relaxed interpolation | endpoint curvature may be wrong |
| Clamped | endpoint slopes | known derivative data | bad slopes distort the curve |
| Not-a-knot | third derivative continuity near ends | general-purpose libraries | less intuitive physically |
| Periodic | values and derivatives wrap | closed curves | requires compatible endpoints |

## Worked example 1: natural spline through three points

**Problem.** Find the natural spline second derivatives for

$$
(0,0),\quad (1,1),\quad (2,0).
$$

**Method.** Here $h_0=h_1=1$ and the natural conditions are $M_0=M_2=0$.

1. The single interior equation is

$$
h_0M_0+2(h_0+h_1)M_1+h_1M_2
=6\left(\frac{0-1}{1}-\frac{1-0}{1}\right).
$$

2. Substitute $M_0=M_2=0$:

$$
4M_1=6(-1-1)=-12.
$$

3. Therefore

$$
M_1=-3.
$$

**Checked answer.** The second derivative values are

$$
M_0=0,\qquad M_1=-3,\qquad M_2=0.
$$

The negative middle value matches the visual shape: the data rise to a peak at $x=1$ and bend downward there.

## Worked example 2: first spline segment formula

**Problem.** Use the result above to write the spline on $[0,1]$.

**Method.** Use $x_0=0$, $x_1=1$, $h_0=1$, $y_0=0$, $y_1=1$, $M_0=0$, and $M_1=-3$.

1. Substitute into the cubic spline formula:

$$
S_0(x)=\frac{0(1-x)^3}{6}+\frac{-3x^3}{6}
+\left(0-0\right)(1-x)+\left(1-\frac{-3}{6}\right)x.
$$

2. Simplify:

$$
S_0(x)=-\frac{x^3}{2}+\frac{3x}{2}.
$$

3. Check the endpoints:

$$
S_0(0)=0,
\qquad
S_0(1)=-\frac12+\frac32=1.
$$

4. Check the second derivatives:

$$
S_0''(x)=-3x,
\qquad
S_0''(0)=0,
\qquad
S_0''(1)=-3.
$$

**Checked answer.** The first segment is $S_0(x)=3x/2-x^3/2$. It matches the data and the computed second derivative values.

## Code

```python
import numpy as np

def natural_spline_second_derivatives(xs, ys):
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    n = len(xs) - 1
    h = np.diff(xs)
    A = np.zeros((n + 1, n + 1))
    rhs = np.zeros(n + 1)
    A[0, 0] = 1.0
    A[n, n] = 1.0
    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2.0 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        rhs[i] = 6.0 * ((ys[i + 1] - ys[i]) / h[i]
                        - (ys[i] - ys[i - 1]) / h[i - 1])
    return np.linalg.solve(A, rhs)

def spline_eval(xs, ys, M, x):
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    i = np.searchsorted(xs, x) - 1
    i = min(max(i, 0), len(xs) - 2)
    h = xs[i + 1] - xs[i]
    left = xs[i + 1] - x
    right = x - xs[i]
    return (M[i] * left**3 / (6 * h) + M[i + 1] * right**3 / (6 * h)
            + (ys[i] - M[i] * h * h / 6) * left / h
            + (ys[i + 1] - M[i + 1] * h * h / 6) * right / h)

xs = [0.0, 1.0, 2.0]
ys = [0.0, 1.0, 0.0]
M = natural_spline_second_derivatives(xs, ys)
print(M)
print(spline_eval(xs, ys, M, 0.5))
```

## Common pitfalls

- Using a single high-degree polynomial where a spline is intended. The local nature of splines is the main benefit.
- Forgetting boundary conditions. Function values and smooth joining are not enough to determine a unique cubic spline.
- Assuming natural endpoints are always best. If endpoint slopes are known, clamped conditions may be more accurate.
- Parameterizing a curve uniformly when points are very unevenly spaced. Chord-length parameters often behave better.
- Solving the tridiagonal spline system as a dense system for large data sets.

## Connections

- [divided differences and Hermite interpolation](/math/numerical-analysis/divided-differences-hermite)
- [Lagrange interpolation and Neville method](/math/numerical-analysis/interpolation-lagrange-neville)
- [matrix factorizations and special systems](/math/numerical-analysis/matrix-factorizations-special-systems)
- [finite difference methods for PDEs](/math/numerical-analysis/finite-difference-pdes)
