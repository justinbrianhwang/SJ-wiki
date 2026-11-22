---
title: ODE Stability Stiffness and Systems
sidebar_position: 14
---

# ODE Stability Stiffness and Systems

Accuracy is only one constraint on a differential-equation solver. A method can have a small truncation error and still fail because the step size lies outside its stability region. Stiff equations make the distinction unavoidable: rapidly decaying modes force tiny explicit steps even while the visible solution changes slowly.

For systems, the eigenvalues of the Jacobian describe local modes. A large negative eigenvalue represents a rapid decay in the exact solution, yet an explicit method can turn that harmless decay into a growing numerical oscillation.

## The scalar test equation isolates stability

Start from

$$
y'=\lambda y,
\qquad y(0)=1.
$$

Applying a one-step method usually gives

$$
w_{n+1}=R(z)w_n,
\qquad z=h\lambda,
$$

where $R(z)$ is the stability function. The absolute-stability region is the set of $z$ for which

$$
|R(z)|\leq 1.
$$

An A-stable method contains the entire left half-plane $\operatorname{Re}(z)\leq0$ in this region. Such a method does not impose a stability step restriction on the scalar decays represented by that half-plane.

Absolute stability is distinct from zero-stability, consistency, and nonlinear stability. It asks one narrow but useful question: if the exact scalar mode does not grow, does repeated application of the numerical recurrence keep that mode bounded? It says nothing by itself about the size of the phase error, the local truncation error, or behavior before the linearized regime is relevant.

Stability functions are obtained by substituting the test equation into the update. The implicit trapezoidal rule gives

$$
w_{n+1}=w_n+\frac h2\left(\lambda w_n+\lambda w_{n+1}\right),
$$

so

$$
R(z)=\frac{1+z/2}{1-z/2}.
$$

For $\operatorname{Re}(z)\leq0$, its magnitude is at most one, hence it is A-stable. Yet $R(z)\to-1$ as $z\to-\infty$: an extremely fast decaying mode can survive numerically as a small alternating component. Backward Euler instead has $R(z)\to0$. An A-stable method with this stronger limiting damping is called L-stable.

No explicit Runge--Kutta method can be A-stable because its $R(z)$ is a polynomial and therefore unbounded as $\vert z\vert \to\infty$. Implicitness is not automatically sufficient either; the coefficients must place the stability region appropriately.

| Method | Stability function | A-stable? | Behavior on stiff decay |
|---|---|---|---|
| Explicit Euler | $1+z$ | no | severe step restriction |
| Backward Euler | $1/(1-z)$ | yes | robust damping; first order |
| Implicit trapezoidal rule | $(1+z/2)/(1-z/2)$ | yes | can alternate rather than damp very stiff modes |
| Classical RK4 | $1+z+z^2/2+z^3/6+z^4/24$ | no | effective for nonstiff problems |

The stability function describes the method rather than the differential equation. A decaying exact mode is reproduced only when its scaled eigenvalue $h\lambda$ lies in the method's region.

## Why explicit Euler has a hard step limit

Explicit Euler gives

$$
w_{n+1}=w_n+h\lambda w_n=(1+z)w_n,
$$

so $R(z)=1+z$. Stability requires

$$
|1+z|\leq1.
$$

Along the negative real axis, the admissible interval is

```text
unstable        stable interval         unstable
<----------|--------------------|---------------->
          -2                    0              h*lambda
```

Thus, for real $\lambda\lt 0$,

$$
-2\leq h\lambda\leq0,
\qquad\text{or equivalently}\qquad
0\leq-h\lambda\leq2.
$$

For the decay equation $y'=-10y$, take first $h=0.1$. Then

$$
z=-1,
\qquad R(-1)=0,
$$

so the step is stable. With $h=0.25$,

$$
z=-2.5,
\qquad R(-2.5)=-1.5,
$$

and $\vert R\vert =1.5\gt 1$. The numerical solution grows in magnitude and alternates in sign even though the exact solution decays.

## Backward Euler trades a solve for robust damping

Backward Euler applies the slope at the unknown next state:

$$
w_{n+1}=w_n+h\lambda w_{n+1}.
$$

Solving for the update gives

$$
R(z)=\frac{1}{1-z}.
$$

If $\operatorname{Re}(z)\leq0$, then $\vert 1-z\vert \geq1$, so backward Euler is A-stable. In fact, $R(z)\to0$ as $z\to-\infty$, giving strong damping of fast modes.

For $y'=-10y$, $h=0.25$, and $w_0=1$,

$$
(1+10h)w_{n+1}=w_n,
\qquad
w_{n+1}=\frac{w_n}{3.5}.
$$

The first two steps are

$$
w_1=0.285714\ldots,
\qquad
w_2=0.0816326\ldots.
$$

The method remains stable where explicit Euler fails, at the cost of solving an implicit equation at every step.

## Stiffness is a mismatch of time scales and stability

A problem is called stiff when stability demands a much smaller step than accuracy alone would require. Large derivatives by themselves do not define stiffness. The characteristic situation is a mixture of modes: fast transients decay quickly, but their presence continues to constrain an explicit solver long after the slow behavior dominates the plot.

For a nonlinear system

$$
y'=F(t,y),
$$

the Jacobian

$$
J=\frac{\partial F}{\partial y}
$$

provides a local linear model. If its eigenvalues include values near $-1000$ and $-1$, explicit Euler is restricted by the fast mode even when the slow mode is the quantity of interest. Because the Jacobian changes along the trajectory, stiffness can also appear or disappear during a simulation.

For the linear system $y'=Ay$, explicit Euler reads

$$
w_{n+1}=(I+hA)w_n,
$$

while backward Euler reads

$$
(I-hA)w_{n+1}=w_n.
$$

If $A=V\Lambda V^{-1}$ is diagonalizable, each eigenmode is multiplied by $R(h\lambda_j)$. The scalar stability region therefore transfers directly to the eigenvalues. A large condition number of $V$ can still cause transient amplification, and defective matrices require Jordan-block terms involving derivatives of $R$. The eigenvalue test is exact for normal matrices and a useful first approximation elsewhere.

For a nonlinear backward Euler step, the unknown $w_{n+1}$ satisfies

$$
G(z)=z-w_n-hF(t_{n+1},z)=0.
$$

Newton's method solves this algebraic system with Jacobian

$$
G'(z)=I-hJ_F(t_{n+1},z).
$$

Factorizing that matrix is often the expensive part of an implicit integrator. Reusing a Jacobian or factorization for several steps saves work, but excessive reuse can increase Newton iterations or cause failure when the dynamics change. Sparse structure matters because realistic systems may contain thousands or millions of variables.

Stiffness ratios such as $\max\vert \operatorname{Re}\lambda_j\vert /\min\vert \operatorname{Re}\lambda_j\vert $ give intuition for linear dissipative systems, but they are not universal definitions. Zero or imaginary modes, nonnormality, changing scales, and the time interval of interest all complicate a single-number diagnosis. The operational definition remains the mismatch between explicit stability steps and the steps needed for the desired accuracy.

Eigenvalues are not the whole story. A nonnormal Jacobian can produce transient norm growth even when every eigenvalue lies in an apparently safe region. Stability checks should therefore be paired with observed step rejections, norm growth, and qualitative knowledge of the modeled process. The variables and scaling used in the code also matter.

## Two time scales in one diagonal system

Consider

$$
y'=\begin{bmatrix}-1&0\\0&-1000\end{bmatrix}y,
\qquad y(0)=\begin{bmatrix}1\\1\end{bmatrix}.
$$

The exact solution is

$$
y(t)=\begin{bmatrix}e^{-t}\\e^{-1000t}\end{bmatrix}.
$$

By $t=0.01$, the second component is $e^{-10}\approx4.54\times10^{-5}$ and soon becomes negligible. Suppose an output tolerance on the slow component would allow $h=0.1$. Explicit Euler multiplies the components by

$$
1-h=0.9,
\qquad 1-1000h=-99.
$$

The slow mode is represented reasonably, but roundoff or any remaining fast component grows by a factor $99$ per step with alternating sign. Stability of the fast mode requires

$$
|1-1000h|\leq1,
$$

so $h\leq0.002$. Reaching $t=1$ then needs at least $500$ explicit Euler steps even though the visible slow solution changes on a unit time scale.

Backward Euler with $h=0.1$ uses factors

$$
\frac1{1+h}=\frac1{1.1},
\qquad
\frac1{1+1000h}=\frac1{101}.
$$

Both modes decay, and the fast one is strongly suppressed. Ten steps reach $t=1$. The slow-mode value is $(1/1.1)^{10}\approx0.3855$, compared with $e^{-1}\approx0.3679$; the discrepancy is ordinary first-order error, not instability. A smaller step can now be selected for accuracy rather than forced by the vanished fast transient.

If the initial fast component were exactly zero and arithmetic exact, explicit Euler would never excite it in this diagonal example. Coupling, input error, and roundoff make that exception fragile. A solver is expected to remain stable under small perturbations, not only along a specially chosen invariant coordinate axis.

## Nonnormal transient growth

Take

$$
A=\begin{bmatrix}-1&100\\0&-2\end{bmatrix}.
$$

Both eigenvalues are negative, yet the first component is driven by the second. With $y(0)=(0,1)^T$, direct solution gives

$$
y_2(t)=e^{-2t},
\qquad
y_1(t)=100(e^{-t}-e^{-2t}).
$$

The norm initially grows to a large value before eventually decaying. That growth belongs to the differential equation, not necessarily to numerical instability. An integrator must reproduce it rather than enforce monotone norm decay based only on eigenvalue signs. Comparing with energy estimates, pseudospectral information, or known conservation and dissipation laws separates physical transients from numerical artifacts.

## A small experiment with amplification factors

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
    print(h, explicit_euler_stable(-10.0, h))
    print(explicit_euler_linear(-10.0, h, 5))

print(backward_euler_linear(-10.0, 0.25, 5))
print("Jacobian eigenvalues", np.linalg.eigvals(np.diag([-1.0, -1000.0])))
```

For a proposed step size, examining $R(h\lambda)$ on a linearized model can expose an unstable choice before a long nonlinear simulation begins.

## Accuracy control on an implicit step

Implicitness enlarges the stability region but does not choose an accurate step automatically. Backward Euler can take a huge stable step across a slow transient and return a poor value without blowing up. Adaptive implicit solvers pair a stable formula with an error estimate, often by comparing formulas of adjacent orders or using an embedded construction. A step must pass both the nonlinear-solve test and the local-error test.

The nonlinear tolerance should be tighter than the requested time-discretization error. If Newton stops too early, algebraic error contaminates the local error estimate. Solving far more accurately than the discretization warrants wastes linear solves. Codes commonly scale the Newton residual and state correction with the same absolute and relative component tolerances used for time stepping.

When Newton fails, reducing $h$ helps because $I-hJ$ becomes closer to the identity and the initial guess lies nearer the next solution. Failure may also indicate a poor Jacobian, a discontinuity, or an inconsistent model rather than stiffness alone. Recording Newton iteration counts distinguishes these cases from ordinary error-based rejection.

## Order reduction and startup transients

An A-stable high-order method can exhibit lower observed order on a stiff problem. Rapid boundary or initial layers, time-dependent constraints, and insufficient smoothness may prevent the derivatives assumed by the formal truncation expansion from staying uniformly bounded as stiffness increases. This phenomenon is called stiff order reduction. Refinement studies should therefore measure the observed slope on the actual system rather than infer it solely from the method's advertised order.

Initial conditions may also be inconsistent with algebraic constraints in differential-algebraic systems. The solver then sees an artificial fast adjustment or fails its first implicit solve. Projecting onto the constraint manifold is a modeling and initialization step, not something absolute stability repairs.

## Stability beyond decay

Oscillatory modes have nearly imaginary eigenvalues. Explicit Euler satisfies $\vert 1+ih\omega\vert \gt 1$ for every nonzero step, so it adds energy to the undamped oscillator. RK4 has a useful interval along the imaginary axis but still accumulates phase and amplitude error. Trapezoidal rule maps the imaginary axis to the unit circle, preserving amplitude for the scalar test mode while altering phase.

Monotonicity can be stricter than absolute stability. Explicit Euler applied to $y'=-ay$ is absolutely stable for $0\leq ah\leq2$, yet it stays nonnegative and decays without sign alternation only for $0\leq ah\leq1$. If negative concentrations are unacceptable, the smaller bound is the relevant one.

Some systems possess a Lyapunov function or conserved quantity that supplies a stronger diagnostic than eigenvalues. A chemically reacting system may preserve total mass and require nonnegative species; a mechanical system may conserve or dissipate energy at a known rate. Monitoring these quantities can reveal a stable-looking but physically wrong trajectory.

Method selection follows the spectrum and structure. Moderately stiff smooth problems often suit backward differentiation formulas; systems requiring strong damping may suit L-stable Runge--Kutta methods; large problems may need Jacobian-free Krylov solves and preconditioning. The linear algebra inside the step can determine the feasible method as much as the stability region does.

## Evidence worth recording from a stiff solve

- Record the accepted and rejected step sizes, method, tolerances, and relevant Jacobian scales. A final curve alone hides whether the solver struggled with stability.
- An accuracy estimator cannot rescue an explicit method outside its stability region. Many adaptive codes will discover the restriction through repeated rejections, but the resulting tiny steps are still expensive.
- Decaying physical modes should not become persistent numerical oscillations. Trapezoidal-rule ringing on very stiff components is bounded yet may still be undesirable; an L-stable method damps it.
- Cost comparisons must use a verified tolerance. Implicit steps pay for nonlinear solves and factorizations, while explicit methods may pay for far more right-hand-side evaluations.
- Poor variable scaling can make Newton convergence and error control uneven across components. Nondimensionalization or componentwise tolerances are often needed for systems with different physical units.
- Separate model behavior, time-discretization error, algebraic-solver error, and stopping diagnostics. A failure at any layer can look like a bad ODE method from the outside.

<div className="see-also">

See also: [Euler Taylor and Runge Kutta methods](/math/numerical-analysis/euler-taylor-runge-kutta) · [adaptive Runge Kutta and multistep methods](/math/numerical-analysis/adaptive-runge-kutta-multistep) · [boundary value problems](/math/numerical-analysis/boundary-value-problems) · [eigenvalue methods](/math/numerical-analysis/eigenvalue-methods)

</div>
