---
title: Divided Differences and Hermite Interpolation
sidebar_position: 7
---

# Divided Differences and Hermite Interpolation

Divided differences reorganize polynomial interpolation so that new data can be added without rebuilding the entire polynomial. Instead of writing the interpolant in the Lagrange basis, the Newton form writes it as a nested polynomial whose coefficients are computed from a triangular table. This is especially convenient for hand computation, incremental data, and error analysis.

Hermite interpolation extends the same idea to derivative data. A Hermite polynomial can match both function values and derivative values at selected nodes, so it captures local slope as well as height. This makes it a natural bridge from ordinary interpolation to cubic splines, finite elements, and high-order initial-value methods.

## Definitions

The first divided difference through two nodes is

$$
f[x_i,x_j]=\frac{f(x_j)-f(x_i)}{x_j-x_i}.
$$

Higher divided differences are defined recursively by

$$
f[x_i,\ldots,x_{i+k}]
=\frac{f[x_{i+1},\ldots,x_{i+k}]-f[x_i,\ldots,x_{i+k-1}]}{x_{i+k}-x_i}.
$$

The Newton interpolating polynomial through distinct nodes $x_0,\ldots,x_n$ is

$$
P_n(x)=f[x_0]+f[x_0,x_1](x-x_0)+\cdots+f[x_0,\ldots,x_n]\prod_{j=0}^{n-1}(x-x_j).
$$

Hermite interpolation allows repeated nodes. If a node $x_i$ is repeated to encode derivative information, then the divided difference involving identical nodes is interpreted by a derivative, for example

$$
f[x_i,x_i]=f'(x_i).
$$

A first-derivative Hermite interpolant through $m$ nodes has $2m$ conditions: $H(x_i)=f(x_i)$ and $H'(x_i)=f'(x_i)$. The resulting polynomial has degree at most $2m-1$.

## Key results

The Newton form is algebraically the same interpolating polynomial as the Lagrange form, but it is organized for extension. If a new node $x_{n+1}$ is added, the previous polynomial $P_n$ remains intact and only one new term is appended:

$$
P_{n+1}(x)=P_n(x)+f[x_0,\ldots,x_{n+1}]\prod_{j=0}^{n}(x-x_j).
$$

The interpolation error for distinct nodes is

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{j=0}^{n}(x-x_j).
$$

For Hermite interpolation with each node repeated twice, the product has squared factors:

$$
f(x)-H(x)=\frac{f^{(2m)}(\xi)}{(2m)!}\prod_{j=0}^{m-1}(x-x_j)^2.
$$

This squared factor explains why matching slopes can give much better local behavior near a node. The polynomial is forced not only to pass through the point but also to leave the point in the correct direction. The tradeoff is that high-degree Hermite interpolation can still oscillate, and derivative data can be noisier than function data.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For divided differences and Hermite interpolation, the input record should include node order, repeated nodes, function data, and derivative data. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include table consistency, interpolation residuals at nodes, and derivative matching for Hermite data. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually triangular-table construction and nested polynomial evaluation. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: misordered nodes, noisy derivative data, and high-degree oscillation. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

| Divided-difference table | Column meaning | Used in Newton polynomial |
|---|---|---|
| $f[x_0]$ | function value | coefficient of $1$ |
| $f[x_0,x_1]$ | first divided difference | coefficient of $(x-x_0)$ |
| $f[x_0,x_1,x_2]$ | second divided difference | coefficient of $(x-x_0)(x-x_1)$ |
| $f[x_0,\ldots,x_n]$ | highest listed difference | coefficient of full product |

```mermaid
flowchart TB
  Nodes["Ordered nodes<br/>x0, x1, ..., xn"] --> Values["#quot;first column<br/>f[x_i"] = y_i"]
  Values --> Diff1["#quot;first divided differences<br/>f[x_i,x_{i+1}"]"]
  Diff1 --> Diff2["higher columns<br/>recursive quotient differences"]
  Diff2 --> Coeff["top row gives Newton coefficients<br/>c0, c1, ..., cn"]
  Coeff --> Eval["nested evaluation<br/>P(x)=c0+(x-x0)(c1+(x-x1)(...))"]

  subgraph Hermite["Hermite extension"]
    direction TB
    Repeat["repeat nodes for derivative data"] --> Deriv["use f'(x_i) for repeated divided difference"]
    Deriv --> HCoeff["Hermite Newton coefficients<br/>value and slope matching"]
  end

  Nodes --> Repeat
  HCoeff --> Eval
  Eval --> Check["check node values, derivative matches, and ordering"]
  Check --> Poly(("interpolating polynomial"))
```

This diagram turns the divided-difference table into a dataflow: ordered nodes fill the value column, recursive differences fill higher columns, and the top row becomes Newton-form coefficients. The Hermite subgraph shows how repeated nodes and derivative data enter the same table architecture. The final check is important because node ordering and repeated-node handling control the polynomial actually being built.

## Worked example 1: Newton polynomial from divided differences

**Problem.** Construct the interpolating polynomial for

$$
(1,0),\quad (2,1),\quad (4,3).
$$

**Method.** Build the divided-difference table.

1. Zeroth differences are the function values:

$$
f[1]=0,\qquad f[2]=1,\qquad f[4]=3.
$$

2. First differences:

$$
f[1,2]=\frac{1-0}{2-1}=1,
\qquad
f[2,4]=\frac{3-1}{4-2}=1.
$$

3. Second difference:

$$
f[1,2,4]=\frac{f[2,4]-f[1,2]}{4-1}=\frac{1-1}{3}=0.
$$

4. Newton form:

$$
P_2(x)=0+1(x-1)+0(x-1)(x-2)=x-1.
$$

**Checked answer.** The three points all lie on the line $y=x-1$, so the second divided difference is zero and the interpolant is $P_2(x)=x-1$.

## Worked example 2: a cubic Hermite interpolant

**Problem.** Find the cubic $H(x)=a+bx+cx^2+dx^3$ satisfying

$$
H(0)=1,\quad H'(0)=0,\quad H(1)=2,\quad H'(1)=3.
$$

**Method.** Translate the four Hermite conditions into equations for the coefficients.

1. From $H(0)=1$, get $a=1$.

2. Since $H'(x)=b+2cx+3dx^2$, the condition $H'(0)=0$ gives $b=0$.

3. Use $H(1)=2$:

$$
1+0+c+d=2,\qquad c+d=1.
$$

4. Use $H'(1)=3$:

$$
0+2c+3d=3.
$$

5. Solve the two-by-two system. From $c=1-d$,

$$
2(1-d)+3d=3 \quad \Rightarrow \quad d=1,
$$

and therefore $c=0$.

**Checked answer.** The Hermite interpolant is

$$
H(x)=1+x^3.
$$

It satisfies $H(0)=1$, $H'(0)=0$, $H(1)=2$, and $H'(1)=3$ exactly.

## Code

```python
import numpy as np

def divided_difference_coefficients(xs, ys):
    xs = np.asarray(xs, dtype=float)
    coeffs = np.asarray(ys, dtype=float).copy()
    n = len(xs)
    for level in range(1, n):
        for i in range(n - 1, level - 1, -1):
            coeffs[i] = (coeffs[i] - coeffs[i - 1]) / (xs[i] - xs[i - level])
    return coeffs

def newton_eval(xs, coeffs, x):
    value = coeffs[-1]
    for k in range(len(coeffs) - 2, -1, -1):
        value = value * (x - xs[k]) + coeffs[k]
    return value

def cubic_hermite_coefficients(f0, fp0, f1, fp1):
    # H(x)=a+b*x+c*x**2+d*x**3 on [0,1]
    a = f0
    b = fp0
    rhs1 = f1 - a - b
    rhs2 = fp1 - b
    d = rhs2 - 2 * rhs1
    c = rhs1 - d
    return np.array([a, b, c, d], dtype=float)

xs = [1.0, 2.0, 4.0]
ys = [0.0, 1.0, 3.0]
coeffs = divided_difference_coefficients(xs, ys)
print(coeffs)
print(newton_eval(xs, coeffs, 3.0))
print(cubic_hermite_coefficients(1.0, 0.0, 2.0, 3.0))
```

## Common pitfalls

- Mixing the order of nodes after building the divided-difference table. The coefficients depend on the listed order.
- Treating repeated Hermite nodes like ordinary distinct nodes. Repeated-node entries require derivative values.
- Expanding the Newton polynomial too early. Nested evaluation is usually more stable and cheaper.
- Assuming derivative data are exact. Measured slopes can amplify noise more than measured function values.
- Using a high-degree Hermite polynomial over a wide interval when piecewise Hermite or splines would be safer.

## Connections

- [Lagrange interpolation and Neville method](/math/numerical-analysis/interpolation-lagrange-neville)
- [cubic splines and parametric curves](/math/numerical-analysis/cubic-splines-parametric-curves)
- [numerical differentiation and Richardson extrapolation](/math/numerical-analysis/numerical-differentiation-richardson)
- [least squares and Chebyshev approximation](/math/numerical-analysis/least-squares-chebyshev-approximation)
