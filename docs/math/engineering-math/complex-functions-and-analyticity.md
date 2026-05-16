---
title: Complex Functions and Analyticity
sidebar_position: 21
---

# Complex Functions and Analyticity

Complex analysis studies functions of a complex variable $z=x+iy$. The surprising feature is that complex differentiability is much stronger than real differentiability. If a function is analytic on a region, it has derivatives of all orders, local power series, and real and imaginary parts that satisfy Laplace's equation.

For engineering mathematics, analytic functions connect potential flow, electrostatics, conformal mapping, residues, Fourier and Laplace methods, and two-dimensional harmonic functions. The Cauchy-Riemann equations are the first test for analyticity, but domain and differentiability assumptions matter.

## Definitions

A complex function can be written

$$
f(z)=u(x,y)+iv(x,y),\qquad z=x+iy,
$$

where $u$ and $v$ are real-valued functions.

The complex derivative at $z_0$ is

$$
f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h},
$$

where $h$ approaches $0$ through complex values from all directions.

A function is analytic at $z_0$ if it is differentiable in a neighborhood of $z_0$. It is analytic on a domain if it is analytic at every point of that domain.

The Cauchy-Riemann equations are

$$
u_x=v_y,\qquad u_y=-v_x.
$$

If the first partial derivatives are continuous and satisfy these equations in a region, then $f=u+iv$ is analytic there.

A harmonic function satisfies

$$
u_{xx}+u_{yy}=0.
$$

If $f=u+iv$ is analytic, then both $u$ and $v$ are harmonic.

## Key results

The derivative must be independent of the direction in which $h$ approaches zero. Approaching along the real direction gives

$$
f'(z)=u_x+iv_x.
$$

Approaching along the imaginary direction gives

$$
f'(z)=v_y-iu_y.
$$

Equating real and imaginary parts yields the Cauchy-Riemann equations.

Analyticity implies harmonicity. If $u_x=v_y$ and $u_y=-v_x$, then

$$
u_{xx}+u_{yy}=v_{yx}-v_{xy}=0,
$$

assuming continuous second partial derivatives. The same argument gives $\nabla^2v=0$. Thus analytic functions generate solutions of Laplace's equation.

The converse is local: a harmonic function on a simply connected region has a harmonic conjugate, so it can become the real part of an analytic function. On regions with holes, global single-valued conjugates may fail to exist.

Elementary analytic functions include polynomials, rational functions away from poles, $e^z$, $\sin z$, and $\cos z$. Functions involving $\bar z$ are usually not analytic except in special degenerate cases. For example, $f(z)=\bar z$ satisfies no open-region Cauchy-Riemann condition.

Analytic functions preserve angles locally when $f'(z_0)\ne 0$. Such maps are conformal at $z_0$. This property supports conformal mapping methods, where complicated two-dimensional potential problems are transformed into simpler domains.

Complex differentiability should not be confused with differentiability as a function $\mathbb{R}^2\to\mathbb{R}^2$. A function can have all real partial derivatives and still fail to be complex differentiable. The Cauchy-Riemann equations impose the extra structure needed for multiplication by a complex derivative to represent the local linear map.

Branches are part of complex function definitions. The logarithm and fractional powers are multivalued unless a branch cut is chosen. A formula such as $\log z$ is not a single analytic function on all of $\mathbb{C}\setminus\{0\}$ because going around the origin changes the argument by $2\pi$.

The local linear meaning of a complex derivative is special. Multiplication by a complex number combines a scaling and a rotation. Therefore, when $f'(z_0)$ exists and is nonzero, the best linear approximation to $f$ near $z_0$ scales all small directions by the same factor and rotates them by the same angle. A general real Jacobian matrix does not have this equal-scaling structure. The Cauchy-Riemann equations are exactly the conditions that force the Jacobian into the form of complex multiplication.

Analyticity is an open-region property. A function may satisfy the Cauchy-Riemann equations at an isolated point without being analytic near that point. For example, functions involving $\bar z$ can be arranged to pass the equations at one point, but the direction-independent derivative fails nearby. This is why engineering math texts emphasize a neighborhood and continuous partial derivatives.

Power series are the local language of analytic functions. If $f$ is analytic near $z_0$, then

$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n
$$

inside some disk of convergence. This is much stronger than real differentiability. It means local behavior is determined by coefficients, and singularities control the radius of convergence. That idea later supports Taylor and Laurent series.

Harmonic conjugates are found by integrating the Cauchy-Riemann equations. If $u$ is known and one wants $v$, use $v_y=u_x$ and $v_x=-u_y$. The two integrations must be consistent; if they are not, $u$ was not harmonic or the region has a global obstruction. The conjugate is determined only up to an additive constant.

Analytic functions are rigid. If two analytic functions agree on a set with a limit point inside a connected domain, they agree everywhere on that domain. This identity principle has no direct analog for arbitrary real differentiable functions. It explains why analytic continuation can extend a function from local data when no singularity blocks the path.

Zeros of analytic functions are isolated unless the function is identically zero on a connected domain. This property supports residue calculations and contour integration. It also means that a nontrivial analytic function cannot vanish on a curve segment inside the domain without vanishing everywhere.

The real and imaginary parts of analytic functions form orthogonal families of level curves where the derivative is nonzero. If $u=\text{constant}$ and $v=\text{constant}$ curves intersect, they do so at right angles. This is the geometric basis of potential-flow diagrams and conformal grids.

## Visual

```mermaid
flowchart TD
  A["f(z) = u("#quot;x,y#quot;") + i v("#quot;x,y#quot;")"] --> B{"Cauchy-Riemann equations?"}
  B -->|with smooth partials| C[Analytic]
  C --> D[u and v harmonic]
  C --> E[Local power series]
  C --> F["Conformal where f' != 0"]
  B -->|fail| G[Not analytic on open region]
  D --> H[Potential theory]
```

| Function | Analytic where? | Reason |
|---|---|---|
| $z^n$ | All complex plane | Polynomial |
| $1/z$ | $z\ne 0$ | Pole at origin |
| $e^z$ | All complex plane | Entire function |
| $\bar z$ | Nowhere on an open region | Fails Cauchy-Riemann |
| $\log z$ | Chosen branch domain | Multivalued without branch cut |

## Worked example 1: Testing Cauchy-Riemann equations

Problem. Determine where

$$
f(z)=z^2
$$

is analytic using $u$ and $v$.

Method.

1. Write

$$
z^2=(x+iy)^2=x^2-y^2+2ixy.
$$

2. Thus

$$
u=x^2-y^2,\qquad v=2xy.
$$

3. Compute partial derivatives:

$$
u_x=2x,\qquad u_y=-2y,
$$

and

$$
v_x=2y,\qquad v_y=2x.
$$

4. Check Cauchy-Riemann:

$$
u_x=v_y \quad \Rightarrow \quad 2x=2x,
$$

and

$$
u_y=-v_x \quad \Rightarrow \quad -2y=-2y.
$$

Answer. The equations hold everywhere, and the partial derivatives are continuous, so $z^2$ is analytic on all of $\mathbb{C}$.

Check. The derivative is $f'(z)=2z$, matching the polynomial rule.

At $z=0$, the derivative is zero, so the map is analytic but not conformal there. Near other points, small angles are preserved. This distinction is important: analyticity alone does not guarantee local angle preservation at critical points where the derivative vanishes.

## Worked example 2: Showing $\bar z$ is not analytic

Problem. Test

$$
f(z)=\bar z.
$$

Method.

1. Write

$$
\bar z=x-iy.
$$

2. Thus

$$
u=x,\qquad v=-y.
$$

3. Compute partials:

$$
u_x=1,\qquad u_y=0,
$$

and

$$
v_x=0,\qquad v_y=-1.
$$

4. Check the first Cauchy-Riemann equation:

$$
u_x=v_y
$$

would require

$$
1=-1,
$$

which is false.

Answer. The function $\bar z$ is not analytic at any point in an open region.

Check. The difference quotient also depends on direction: along real $h$, the quotient is $1$; along imaginary $h$, it is $-1$.

The example is useful because $\bar z$ is perfectly smooth as a real two-variable function. Its failure is specifically complex differentiability. This demonstrates why complex analysis cannot be reduced to ordinary partial derivatives without the Cauchy-Riemann structure.

## Code

```python
import sympy as sp

x, y = sp.symbols("x y", real=True)
u = x**2 - y**2
v = 2*x*y

cr1 = sp.simplify(sp.diff(u, x) - sp.diff(v, y))
cr2 = sp.simplify(sp.diff(u, y) + sp.diff(v, x))
lap_u = sp.diff(u, x, 2) + sp.diff(u, y, 2)
lap_v = sp.diff(v, x, 2) + sp.diff(v, y, 2)

print(cr1, cr2)
print(lap_u, lap_v)
```

The code verifies the Cauchy-Riemann equations and harmonicity for $z^2$. Symbolic checks are useful, but they do not replace domain analysis. A formula can satisfy local equations away from a branch cut or singularity and still fail to be analytic on a larger requested domain.

For branch-dependent functions, code usually follows a principal branch convention. That convention may introduce a discontinuity along a cut, often the negative real axis for logarithms. Mathematical work must state the branch domain explicitly.

## Common pitfalls

- Checking Cauchy-Riemann equations at a single point and claiming analyticity on a region.
- Forgetting the need for continuity of partial derivatives in the common sufficient test.
- Treating $\bar z$ as if it behaved like $z$ under complex differentiation.
- Ignoring branch cuts for $\log z$ and fractional powers.
- Assuming harmonic real part automatically gives a global analytic function on a region with holes.
- Confusing "complex differentiable at a point" with "analytic in a neighborhood."
- Forgetting that conformality can fail where $f'(z)=0$.
- Applying real-variable intuition about differentiability without checking direction independence.
- Treating a branch formula as globally single-valued without tracking changes in argument.
- Forgetting that harmonic conjugates are unique only up to an additive real constant.
- Assuming a harmonic function on a multiply connected domain always has a single-valued conjugate.
- Ignoring singular points when naming an analytic domain.

## Connections

- [Complex Integration and Residues](/math/engineering-math/complex-integration-and-residues)
- [Laplace Equation and Potential](/math/engineering-math/laplace-equation-and-potential)
- [Vector Differential Calculus](/math/engineering-math/vector-differential-calculus)
- [Fourier Integrals and Transforms](/math/engineering-math/fourier-integrals-and-transforms)
