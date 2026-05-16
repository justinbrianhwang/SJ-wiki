---
title: Systems of ODEs and Phase Planes
sidebar_position: 7
---

# Systems of ODEs and Phase Planes

Systems of ODEs model several state variables changing together. A mass-spring system uses position and velocity, a predator-prey model uses two populations, and an electrical network may use several currents and capacitor voltages. The phase plane replaces a single graph $y(t)$ with trajectories in state space, making stability and long-term behavior visible.

Linear systems connect ODEs to eigenvalues and eigenvectors. Nonlinear systems are often understood by equilibria, linearization, nullclines, and numerical trajectories. The goal is not only to solve equations, but to classify behavior: attraction, repulsion, spiraling, saddle behavior, periodic motion, and sensitivity to initial conditions.

## Definitions

A first-order system is

$$
\mathbf{x}'=\mathbf{f}(t,\mathbf{x}).
$$

An autonomous system has no explicit $t$ dependence:

$$
\mathbf{x}'=\mathbf{f}(\mathbf{x}).
$$

For a linear homogeneous system with constant coefficients,

$$
\mathbf{x}'=A\mathbf{x},
$$

the solution can be written with the matrix exponential:

$$
\mathbf{x}(t)=e^{At}\mathbf{x}(0).
$$

An equilibrium point satisfies

$$
\mathbf{f}(\mathbf{x}_*)=\mathbf{0}.
$$

For a two-dimensional autonomous system,

$$
\begin{aligned}
x'&=f(x,y),\\
y'&=g(x,y),
\end{aligned}
$$

the $x$-nullclines are curves where $f(x,y)=0$, and the $y$-nullclines are curves where $g(x,y)=0$. Their intersections are equilibria.

Linearization at an equilibrium uses the Jacobian

$$
J(\mathbf{x}_*)=
\begin{bmatrix}
f_x & f_y\\
g_x & g_y
\end{bmatrix}_{\mathbf{x}=\mathbf{x}_*}.
$$

## Key results

If $A$ has a basis of eigenvectors $\mathbf{v}_1,\ldots,\mathbf{v}_n$ with eigenvalues $\lambda_1,\ldots,\lambda_n$, then the general solution of $\mathbf{x}'=A\mathbf{x}$ is

$$
\mathbf{x}(t)=c_1e^{\lambda_1t}\mathbf{v}_1+\cdots+c_ne^{\lambda_nt}\mathbf{v}_n.
$$

For a repeated eigenvalue with too few eigenvectors, generalized eigenvectors are needed. If $(A-\lambda I)\mathbf{w}=\mathbf{v}$, then a solution has the form

$$
e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$

For a real $2\times 2$ matrix, trace and determinant summarize the eigenvalues. The characteristic equation is

$$
\lambda^2-\operatorname{tr}(A)\lambda+\det(A)=0.
$$

The determinant gives the product of eigenvalues and the trace gives their sum. A negative determinant means eigenvalues of opposite sign, hence a saddle. A positive determinant with negative trace often indicates attraction, while a positive trace indicates repulsion, unless complex or repeated cases require closer inspection.

For nonlinear systems, linearization usually predicts local behavior when the equilibrium is hyperbolic, meaning no eigenvalue of the Jacobian has real part zero. If an eigenvalue has zero real part, linearization may be inconclusive, and nonlinear terms decide the behavior.

Phase-plane analysis combines several tools. Equilibria locate possible long-term states. Nullclines show where motion is horizontal or vertical. The vector field gives direction and speed. Eigenvectors of the linearized system show tangent directions near a saddle or node. Numerical trajectories test how local behavior extends globally.

Conservation laws can create closed orbits. For example, the undamped oscillator $x'=y$, $y'=-x$ has $x^2+y^2$ constant, so trajectories are circles. Damping changes the derivative of that energy-like quantity and turns circles into spirals. This energy viewpoint is often more robust than solving explicitly.

The phase portrait is a picture of state, not a picture of each component against time. A single point in the phase plane represents the whole current state. As time evolves, the point moves along a trajectory. If two trajectories for an autonomous system intersect in a uniqueness region, they must be the same trajectory with a different time parametrization; otherwise one initial state would have two futures. This is the system version of the noncrossing rule for scalar ODEs.

Linear systems with real eigenvectors have straight-line invariant directions. If the initial condition lies exactly on an eigenvector line, the solution stays on that line and grows or decays with the corresponding exponential. General initial conditions decompose into eigenvector components. Over time, the component with the largest real part usually dominates. This is why unstable modes can be visible even when their initial coefficient is small.

For complex eigenvalues in a real system, trajectories rotate. The sign of the real part determines whether the spiral moves inward or outward, while the imaginary part determines angular speed. The direction of rotation is not determined by the eigenvalues alone; it must be read from the vector field at a convenient point. For example, evaluating the vector field on the positive $x$-axis shows whether motion initially points upward or downward.

Nullclines are a bridge between algebra and geometry in nonlinear systems. On an $x$-nullcline, vectors are vertical because $x'=0$. On a $y$-nullcline, vectors are horizontal because $y'=0$. The signs of $x'$ and $y'$ in the regions cut out by the nullclines give a coarse phase portrait even before numerical integration. This is especially useful in population models, chemical kinetics, and competing-species systems where exact formulas are unavailable.

Linearization is a local method. It describes behavior close to an equilibrium, not necessarily far away. A nonlinear system can have one equilibrium that is locally stable and still have trajectories far away that escape, approach a different equilibrium, or enter a periodic orbit. Numerical plots should therefore use several initial conditions and should be interpreted together with invariants, nullclines, and physical constraints such as nonnegative populations.

Systems also make scaling important. Variables may have different units and magnitudes, so a phase portrait can look distorted if axes are chosen poorly. A trajectory that appears nearly horizontal may simply reflect that one variable is plotted in thousands and another in fractions. Nondimensionalization or rescaling can reveal the real geometry and improve numerical conditioning.

## Visual

```mermaid
flowchart TD
  A[System x' = f(x)] --> B[Find equilibria]
  B --> C[Compute Jacobian]
  C --> D[Eigenvalues]
  D --> E{Real parts}
  E -->|all negative| F[Local sink]
  E -->|some positive, some negative| G[Saddle]
  E -->|all positive| H[Source]
  E -->|zero real part| I[Linearization inconclusive or center]
  B --> J[Draw nullclines and trajectories]
```

| Eigenvalue pattern for $2\times2$ linear system | Phase portrait | Stability |
|---|---|---|
| Real, both negative | Sink node | Asymptotically stable |
| Real, both positive | Source node | Unstable |
| Real, opposite signs | Saddle | Unstable |
| Complex $\alpha\pm i\beta$, $\alpha\lt 0$ | Spiral sink | Asymptotically stable |
| Complex $\alpha\pm i\beta$, $\alpha\gt 0$ | Spiral source | Unstable |
| Pure imaginary | Center in linear system | Stable but not asymptotically stable |

## Worked example 1: Linear system with a source node

Problem. Solve and classify

$$
\mathbf{x}'=
\begin{bmatrix}
3&1\\
1&3
\end{bmatrix}\mathbf{x}.
$$

Method.

1. Compute the characteristic polynomial:

$$
\det(A-\lambda I)=
\begin{vmatrix}
3-\lambda&1\\
1&3-\lambda
\end{vmatrix}
=(3-\lambda)^2-1.
$$

2. Set it to zero:

$$
(3-\lambda)^2-1=0.
$$

Thus

$$
3-\lambda=\pm 1,
$$

so

$$
\lambda_1=4,\qquad \lambda_2=2.
$$

3. For $\lambda_1=4$,

$$
A-4I=
\begin{bmatrix}
-1&1\\
1&-1
\end{bmatrix},
$$

so an eigenvector is

$$
\mathbf{v}_1=\begin{bmatrix}1\\1\end{bmatrix}.
$$

4. For $\lambda_2=2$,

$$
A-2I=
\begin{bmatrix}
1&1\\
1&1
\end{bmatrix},
$$

so an eigenvector is

$$
\mathbf{v}_2=\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Answer.

$$
\mathbf{x}(t)=c_1e^{4t}
\begin{bmatrix}1\\1\end{bmatrix}
+c_2e^{2t}
\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Check. Both eigenvalues are positive, so this is a source node, not a saddle. Every nonzero trajectory moves away from the origin as $t$ increases.

The eigenvector directions give the shape of that departure. Initial data on the line $y=x$ stay on that line and grow like $e^{4t}$. Initial data on the line $y=-x$ stay on that line and grow like $e^{2t}$. For most other initial data, the $e^{4t}$ component eventually dominates, so trajectories become tangent to the faster eigenvector direction as they move outward.

## Worked example 2: Linearization of a predator-prey equilibrium

Problem. For

$$
\begin{aligned}
x'&=x(2-y),\\
y'&=y(x-3),
\end{aligned}
$$

find equilibria and classify the positive equilibrium by linearization.

Method.

1. Set $x'=0$:

$$
x(2-y)=0,
$$

so $x=0$ or $y=2$.

2. Set $y'=0$:

$$
y(x-3)=0,
$$

so $y=0$ or $x=3$.

3. Intersections give equilibria

$$
(0,0)\quad \text{and}\quad (3,2).
$$

4. Compute the Jacobian:

$$
J(x,y)=
\begin{bmatrix}
2-y&-x\\
y&x-3
\end{bmatrix}.
$$

5. At $(3,2)$,

$$
J(3,2)=
\begin{bmatrix}
0&-3\\
2&0
\end{bmatrix}.
$$

6. Characteristic equation:

$$
\lambda^2+6=0.
$$

Thus

$$
\lambda=\pm i\sqrt{6}.
$$

Answer. The linearization has a center. Because the eigenvalues are pure imaginary, the equilibrium is nonhyperbolic, so linearization alone does not prove asymptotic stability or instability.

Check. This system is the undamped Lotka-Volterra form and has closed level curves around the positive equilibrium, consistent with center-like behavior.

The conclusion should be stated carefully. The linearized matrix predicts rotation but has no decay. It does not prove attraction. In a damped ecological model, extra terms could turn the same equilibrium into a spiral sink or spiral source, so the nonlinear equations must be considered.

## Code

```python
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, z):
    x, y = z
    return [x * (2.0 - y), y * (x - 3.0)]

t_eval = np.linspace(0.0, 20.0, 1000)
sol = solve_ivp(rhs, (0.0, 20.0), [4.0, 1.0], t_eval=t_eval, rtol=1e-9, atol=1e-11)

print(sol.y[:, -1])
print(np.min(sol.y[0]), np.max(sol.y[0]))
```

## Common pitfalls

- Calling every pair of pure imaginary eigenvalues a stable nonlinear center. Linearization is inconclusive when eigenvalues have zero real part.
- Forgetting that a negative determinant in a $2\times2$ linear system forces a saddle.
- Drawing nullclines as trajectories. They are places where one component of velocity is zero, not necessarily solution curves.
- Ignoring eigenvectors when sketching a saddle or node; they determine approach and departure directions.
- Treating numerical phase portraits as proof without checking step size, tolerances, and invariants.
- Classifying a system from trace alone. Determinant and discriminant are also needed.
- Losing variables when converting a higher-order scalar ODE into a first-order system.
- Forgetting to keep only physically meaningful regions, such as nonnegative populations.

## Connections

- [Eigenvalues and Diagonalization](/math/engineering-math/eigenvalues-and-diagonalization)
- [Second-Order Linear ODEs](/math/engineering-math/second-order-linear-odes)
- [Direction Fields and Existence](/math/engineering-math/direction-fields-and-existence)
- [Numerical Methods Overview](/math/engineering-math/numerical-methods-overview)
