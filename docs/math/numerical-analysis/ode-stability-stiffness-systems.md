---
title: ODE Stability Stiffness and Systems
sidebar_position: 14
---

# ODE Stability Stiffness and Systems

Accuracy is not the only issue for differential equation solvers. A method can have a small truncation error formula and still fail because the step size lies outside its stability region. This becomes especially important for stiff equations, where fast-decaying modes force tiny explicit steps even when the visible solution changes slowly.

![Euler method advances along short tangent-line steps.](https://commons.wikimedia.org/wiki/Special:FilePath/Euler_method.svg)

*Figure: Euler method approximates an ODE solution by repeatedly stepping in the current slope direction. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Euler_method.svg), Oleg Alexandrov, public domain.*

Systems of ODEs make this behavior more transparent. The eigenvalues of the Jacobian describe local modes. Large negative eigenvalues may decay rapidly in the exact solution, but an explicit method can turn those harmless decays into numerical oscillations unless the step size is restricted.

## Definitions

The scalar test equation is

$$
y'=\lambda y,
\qquad y(0)=1.
$$

For a one-step method applied to this equation, the update often has the form

$$
w_{n+1}=R(z)w_n,
\qquad z=h\lambda,
$$

where $R(z)$ is the method's **stability function**. The **absolute stability region** is the set of $z$ values for which

$$
|R(z)|\le 1.
$$

A method is **A-stable** if its stability region contains the entire left half-plane $\operatorname{Re}(z)\le 0$. This is desirable for stiff decay problems.

A problem is **stiff** when stability requirements force a much smaller step size than accuracy requirements would suggest. Stiffness is not simply the presence of large derivatives; it is a mismatch between time scales and method stability.

For a system

$$
y'=F(t,y),
$$

local stiffness is often assessed using eigenvalues of the Jacobian matrix $J=\partial F/\partial y$.

## Key results

Explicit Euler applied to $y'=\lambda y$ has

$$
w_{n+1}=w_n+h\lambda w_n=(1+z)w_n,
$$

so $R(z)=1+z$ and stability requires

$$
|1+z|\le 1.
$$

For real negative $\lambda$, this means

$$
-2\le h\lambda\le 0.
$$

Backward Euler has

$$
w_{n+1}=w_n+h\lambda w_{n+1},
$$

so

$$
R(z)=\frac{1}{1-z}.
$$

If $\operatorname{Re}(z)\le 0$, then $\vert 1-z\vert \ge 1$, so backward Euler is A-stable. This explains why implicit methods are preferred for stiff systems even though each step costs more.

For nonlinear systems, stability analysis is local. Near a state $y$, the linearized equation uses the Jacobian eigenvalues. A method must treat all important modes stably. If one eigenvalue is near $-1000$ and another is near $-1$, explicit Euler is limited by the fast mode even if the slow mode is the one visible in the plot.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For ODE stability, stiffness, and systems, the input record should include the test equation or Jacobian spectrum, step size, method stability function, and stiffness scale. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include amplification factors, rejected steps, qualitative decay, and eigenvalue checks. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually implicit solves, Jacobian factorizations, and explicit step restrictions. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: accuracy-only step selection, hidden fast modes, and using nonstiff solvers on stiff systems. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

For systems, stability should be checked in the variables and scaling actually used by the code. A diagonal test equation explains the mechanism, but real Jacobians may be nonnormal, so transient growth can occur even when eigenvalues look acceptable. Pair eigenvalue checks with observed step rejection, norm growth, and qualitative knowledge of the modeled process.
 When possible, test a proposed step size on the linearized model before committing to a long nonlinear simulation.

## Visual

```text
Explicit Euler stability on the real axis:

unstable        stable interval         unstable
<----------|--------------------|---------------->
          -2                    0              h*lambda

For negative lambda, h must satisfy 0 <= -h*lambda <= 2.
```

| Method | Stability function on test equation | A-stable? | Stiff use |
|---|---|---|---|
| Explicit Euler | $1+z$ | no | poor |
| Backward Euler | $1/(1-z)$ | yes | robust but first order |
| Trapezoidal implicit | $(1+z/2)/(1-z/2)$ | yes | accurate, may oscillate for very stiff modes |
| RK4 | polynomial through $z^4/24$ | no | good nonstiff baseline |

## Worked example 1: explicit Euler stability limit

**Problem.** Apply explicit Euler to

$$
y'=-10y
$$

and determine whether $h=0.1$ and $h=0.25$ are stable.

**Method.** Here $\lambda=-10$, so $z=h\lambda$ and $R(z)=1+z$.

1. For $h=0.1$:

$$
z=-1,
\qquad
R(-1)=1-1=0.
$$

Since $\vert R\vert =0\le 1$, the step is stable.

2. For $h=0.25$:

$$
z=-2.5,
\qquad
R(-2.5)=1-2.5=-1.5.
$$

Since $\vert -1.5\vert =1.5\gt 1$, the step is unstable.

**Checked answer.** Explicit Euler is stable for $h=0.1$ and unstable for $h=0.25$. The exact solution decays in both cases, so the instability is purely numerical.

## Worked example 2: backward Euler on the same decay

**Problem.** Apply backward Euler to $y'=-10y$ with $h=0.25$ and $w_0=1$.

**Method.** Backward Euler gives

$$
w_{n+1}=w_n-10h w_{n+1}.
$$

1. Solve for $w_{n+1}$:

$$
(1+10h)w_{n+1}=w_n,
\qquad
w_{n+1}=\frac{w_n}{1+10h}.
$$

2. With $h=0.25$,

$$
w_{n+1}=\frac{w_n}{3.5}.
$$

3. Starting from $w_0=1$,

$$
w_1=0.285714\ldots,
\qquad
w_2=0.0816326\ldots.
$$

4. The numerical solution decays monotonically.

**Checked answer.** Backward Euler remains stable at $h=0.25$, while explicit Euler was unstable. The implicit method damps the fast decay mode.

## Code

```python
import numpy as np

def explicit_euler_linear(lambda_value, h, steps, y0=1.0):
    y = y0
    values = [y]
    for _ in range(steps):
        y = y + h * lambda_value * y
        values.append(y)
    return values

def backward_euler_linear(lambda_value, h, steps, y0=1.0):
    y = y0
    values = [y]
    for _ in range(steps):
        y = y / (1.0 - h * lambda_value)
        values.append(y)
    return values

def explicit_euler_stable(lambda_value, h):
    z = h * lambda_value
    return abs(1.0 + z) <= 1.0

for h in [0.1, 0.25]:
    print(h, explicit_euler_stable(-10.0, h), explicit_euler_linear(-10.0, h, 5))
print(backward_euler_linear(-10.0, 0.25, 5))
print("Jacobian eigenvalues", np.linalg.eigvals(np.diag([-1.0, -1000.0])))
```

## Common pitfalls

- Treating a stable exact decay as automatically stable numerically.
- Choosing step size only from accuracy estimates and ignoring the stability region.
- Calling every rapidly changing problem stiff. Stiffness is about restrictive stability compared with accuracy needs.
- Using explicit RK methods on stiff systems without checking rejected steps or stability warnings.
- Forgetting that nonlinear stiffness changes along the trajectory as the Jacobian changes.

## Connections

- [Euler Taylor and Runge Kutta methods](/math/numerical-analysis/euler-taylor-runge-kutta)
- [adaptive Runge Kutta and multistep methods](/math/numerical-analysis/adaptive-runge-kutta-multistep)
- [boundary value problems](/math/numerical-analysis/boundary-value-problems)
- [eigenvalue methods](/math/numerical-analysis/eigenvalue-methods)
