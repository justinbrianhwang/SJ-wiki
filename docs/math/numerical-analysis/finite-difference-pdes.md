---
title: Finite Difference Methods for PDEs
sidebar_position: 24
---

# Finite Difference Methods for PDEs

Finite difference methods approximate partial derivatives on a grid. They turn differential equations into algebraic equations that can be solved step by step or as large linear systems. The method is conceptually simple, but accuracy, stability, boundary handling, and matrix structure must all be managed carefully.

PDE type matters. Elliptic problems such as Laplace's equation usually produce coupled spatial systems. Parabolic problems such as the heat equation involve time stepping with smoothing. Hyperbolic problems such as wave and advection equations require special attention to propagation speed and numerical dispersion.

## Definitions

For a grid point $x_i=x_0+i\Delta x$, centered differences include

$$
u_x(x_i)\approx \frac{u_{i+1}-u_{i-1}}{2\Delta x},
$$

and

$$
u_{xx}(x_i)\approx \frac{u_{i-1}-2u_i+u_{i+1}}{\Delta x^2}.
$$

For the heat equation

$$
u_t=\alpha u_{xx},
$$

the forward-time centered-space scheme is

$$
u_i^{n+1}=u_i^n+r(u_{i-1}^n-2u_i^n+u_{i+1}^n),
\qquad
r=\frac{\alpha\Delta t}{\Delta x^2}.
$$

For Laplace's equation

$$
u_{xx}+u_{yy}=0,
$$

the five-point stencil on a square grid is

$$
4u_{i,j}=u_{i-1,j}+u_{i+1,j}+u_{i,j-1}+u_{i,j+1}.
$$

## Key results

Consistency means the finite difference formula approaches the PDE as the mesh spacings go to zero. Stability means errors do not grow uncontrollably under the numerical update. Convergence follows when a consistent scheme is stable for a well-posed linear problem; this is the practical message of the Lax equivalence theorem.

The explicit heat scheme is stable in one spatial dimension under the condition

$$
r=\frac{\alpha\Delta t}{\Delta x^2}\le \frac12.
$$

This restriction can be severe on fine grids because halving $\Delta x$ requires roughly quartering $\Delta t$. Implicit methods remove this parabolic time-step restriction but require solving a linear system each step.

Finite difference matrices are sparse. A one-dimensional second derivative gives a tridiagonal matrix; a two-dimensional five-point Laplacian gives a sparse block structure. Preserving sparsity is essential for large grids.

Boundary conditions are not afterthoughts. Dirichlet values enter the right-hand side, Neumann values require derivative approximations, and mixed conditions can change both the matrix and the accuracy near the boundary.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For finite difference PDE methods, the input record should include the PDE type, mesh spacings, boundary conditions, and stencil. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include discrete residuals, conservation or maximum-principle checks, and grid refinement. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually sparse matrix storage, time-step restrictions, and solver complexity. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: CFL violations, boundary-condition mistakes, and dense treatment of sparse grids. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

Grid refinement is the most important practical audit. Run the same PDE with half the mesh spacing, adjust the time step consistently, and compare the solutions in a common norm. If the observed order is far below the stencil order, boundary conditions, nonsmooth data, solver tolerance, or stability limits are usually responsible.

## Visual

```text
Five-point Laplace stencil:

        u(i,j+1)
            |
u(i-1,j) - u(i,j) - u(i+1,j)
            |
        u(i,j-1)

4*u(i,j) equals the sum of the four neighbors for Laplace's equation.
```

| PDE type | Example | Common finite difference issue | Matrix/update pattern |
|---|---|---|---|
| Elliptic | Laplace, Poisson | boundary coupling | sparse linear system |
| Parabolic | heat equation | time-step stability | marching plus smoothing |
| Hyperbolic | wave, advection | CFL and dispersion | propagation-sensitive update |
| Nonlinear | reaction-diffusion | nonlinear solves | Newton or splitting |

## Worked example 1: one explicit heat step

**Problem.** Use the explicit heat scheme with $r=0.25$ for one interior value $u_1^0=1$ and boundary values $u_0^0=u_2^0=0$.

**Method.** Apply

$$
u_1^{1}=u_1^0+r(u_0^0-2u_1^0+u_2^0).
$$

1. Substitute the values:

$$
u_1^{1}=1+0.25(0-2(1)+0).
$$

2. Simplify the second-difference term:

$$
0-2+0=-2.
$$

3. Update:

$$
u_1^{1}=1+0.25(-2)=0.5.
$$

4. Check stability condition:

$$
r=0.25\le 0.5.
$$

**Checked answer.** The new interior value is $0.5$. The scheme is stable for this $r$ in the one-dimensional heat equation.

## Worked example 2: one-point Laplace solve

**Problem.** A square has boundary values $100$ on the top side and $0$ on the other three sides. With one interior grid point, approximate the steady temperature.

**Method.** The five-point formula says the interior value equals the average of its four neighbors.

1. Let the interior value be $u$.

2. The four neighboring boundary values are

$$
0,\quad 0,\quad 0,\quad 100.
$$

3. The Laplace equation gives

$$
4u=0+0+0+100.
$$

4. Therefore

$$
u=25.
$$

**Checked answer.** The one-point finite difference approximation gives temperature $25$ at the center.

## Code

```python
import numpy as np

def heat_explicit(u0, alpha, dx, dt, steps):
    r = alpha * dt / (dx * dx)
    if r > 0.5:
        raise ValueError("explicit heat scheme unstable for r > 1/2")
    u = np.array(u0, dtype=float)
    history = [u.copy()]
    for _ in range(steps):
        new = u.copy()
        new[1:-1] = u[1:-1] + r * (u[:-2] - 2*u[1:-1] + u[2:])
        u = new
        history.append(u.copy())
    return history

def laplace_jacobi(top, bottom, left, right, n, iterations=5000, tol=1e-10):
    u = np.zeros((n + 2, n + 2))
    u[0, :] = top
    u[-1, :] = bottom
    u[:, 0] = left
    u[:, -1] = right
    for _ in range(iterations):
        old = u.copy()
        u[1:-1, 1:-1] = 0.25 * (old[:-2, 1:-1] + old[2:, 1:-1]
                                  + old[1:-1, :-2] + old[1:-1, 2:])
        if np.linalg.norm(u - old, ord=np.inf) < tol:
            break
    return u

print(heat_explicit([0.0, 1.0, 0.0], alpha=1.0, dx=1.0, dt=0.25, steps=1)[-1])
print(laplace_jacobi(100.0, 0.0, 0.0, 0.0, n=1))
```

## Common pitfalls

- Choosing $\Delta t$ for accuracy but violating the CFL or heat stability condition.
- Treating boundary conditions as values to patch in after solving instead of building them into the scheme.
- Converting sparse PDE matrices into dense arrays for large grids.
- Using centered differences for advection-dominated hyperbolic problems without stabilization.
- Refining space without refining time consistently for transient problems.

## Connections

- [boundary value problems](/math/numerical-analysis/boundary-value-problems)
- [matrix factorizations and special systems](/math/numerical-analysis/matrix-factorizations-special-systems)
- [iterative linear systems](/math/numerical-analysis/iterative-linear-systems)
- [ODE stability stiffness and systems](/math/numerical-analysis/ode-stability-stiffness-systems)
