---
title: First-Order ODEs
sidebar_position: 2
---

# First-Order ODEs

A first-order ordinary differential equation relates an unknown function to its first derivative. In engineering models the derivative is usually a rate: current changing in a circuit, temperature relaxing toward the surroundings, concentration changing in a mixing tank, or velocity responding to drag. The mathematical work is only one part of the task. A useful solution also records the modeling assumptions, the interval where the solution is valid, the initial condition, and the physical meaning of constants.

This page sits between qualitative ideas such as slope fields and later linear-system methods. The main theme is recognition: identify whether the equation is separable, linear, exact, Bernoulli, homogeneous in $y/x$, or best handled numerically. Many errors in first-order ODEs come from forcing an equation into a favorite method instead of checking its actual structure.

## Definitions

A first-order ODE can be written implicitly as

$$
F(x,y,y')=0
$$

or explicitly as

$$
y'=f(x,y).
$$

An initial value problem adds one condition,

$$
y(x_0)=y_0,
$$

which selects one curve from a family of solution curves. A solution on an interval $I$ is a differentiable function $y=h(x)$ such that $h'(x)=f(x,h(x))$ for all $x\in I$.

A separable equation has the form

$$
\frac{dy}{dx}=g(x)h(y).
$$

Where $h(y)\ne 0$, separate and integrate:

$$
\begin{aligned}
\frac{1}{h(y)}\,dy &= g(x)\,dx,\\
\int \frac{1}{h(y)}\,dy &= \int g(x)\,dx+C.
\end{aligned}
$$

A linear first-order equation has standard form

$$
y'+p(x)y=r(x).
$$

The integrating factor

$$
\mu(x)=e^{\int p(x)\,dx}
$$

makes the left side a product derivative:

$$
\begin{aligned}
\mu y'+\mu p y &= \mu r,\\
(\mu y)' &= \mu r.
\end{aligned}
$$

An exact equation has differential form

$$
M(x,y)\,dx+N(x,y)\,dy=0
$$

and is exact on a simply connected region when $M_y=N_x$. Then there is a potential function $u(x,y)$ with $u_x=M$ and $u_y=N$, and the implicit solution is $u(x,y)=C$.

A Bernoulli equation is

$$
y'+p(x)y=g(x)y^a,\qquad a\ne 0,1.
$$

The substitution $v=y^{1-a}$ converts it into a linear equation for $v$.

## Key results

The existence and uniqueness theorem gives the basic local guarantee. If $f(x,y)$ and $f_y(x,y)$ are continuous in a rectangle around $(x_0,y_0)$, then the initial value problem $y'=f(x,y)$, $y(x_0)=y_0$, has exactly one solution near $x_0$. The theorem is local: it does not promise that the solution exists forever, and it does not say that the formula will be elementary.

For separable equations, constant solutions can be lost by division. If $y'=y(1-y)$, separating by dividing through by $y(1-y)$ assumes $y\ne 0$ and $y\ne 1$, so the equilibrium solutions $y=0$ and $y=1$ must be added separately. These equilibria often control the long-term behavior.

For linear equations, the integrating factor formula is

$$
y(x)=\frac{1}{\mu(x)}
\left(
\int \mu(x)r(x)\,dx+C
\right).
$$

For exact equations, a reliable construction is

$$
\begin{aligned}
u(x,y)&=\int M(x,y)\,dx+\phi(y),\\
u_y(x,y)&=N(x,y).
\end{aligned}
$$

The second line determines $\phi'(y)$. If the leftover expression still contains $x$, the equation was not exact or a computation error occurred.

For autonomous equations $y'=f(y)$, the phase line gives stability without solving. An equilibrium $y_*$ satisfies $f(y_*)=0$. If $f(y)\gt 0$ below $y_*$ and $f(y)\lt 0$ above it, nearby solutions move toward $y_*$ and the equilibrium is stable. If arrows point away, it is unstable.

Most engineering uses of first-order equations start from a balance law rather than from a ready-made formula. In a mixing problem, the dependent variable is usually amount, not concentration, because the balance is most naturally written as amount per time. In a cooling problem, the dependent variable is temperature, and the proportional term must use the difference from ambient temperature, not the absolute temperature. In a circuit model, Kirchhoff's law determines whether the state variable should be charge, current, or capacitor voltage. Choosing the state variable well often makes the equation linear.

The interval of validity is part of the answer. A formula may contain a logarithm, a denominator, or a square root that restricts $x$, and the initial point must lie in the chosen interval. For example, the solution of $y'=y^2$, $y(0)=1$, is $y=1/(1-x)$, which blows up at $x=1$. The existence theorem gives local existence near $0$, but it does not contradict finite-time blow-up.

Some equations become linear only after a change of variables. Bernoulli equations are the standard example, but homogeneous equations of the form $y'=F(y/x)$ use $v=y/x$, so $y=vx$ and $y'=v+xv'$. Equations with a shifted center, such as $y'=F((y-2)/(x+1))$, may require translating coordinates before applying that idea. The point is not to memorize many named types; it is to look for algebraic structure that lowers the equation to one of the dependable forms.

Exact equations require a region condition as well as the derivative test. The equality $M_y=N_x$ is normally used on a simply connected region where the partial derivatives are continuous. Holes in the region can produce path-dependent behavior, which is why the assumptions matter. In elementary engineering ODE problems the region is usually a rectangle or half-plane, but checking the domain prevents subtle mistakes when denominators vanish.

Integrating factors beyond the linear case exist but are not automatic. For a nonexact equation $M\,dx+N\,dy=0$, a factor depending only on $x$ may be found if

$$
\frac{M_y-N_x}{N}
$$

is a function of $x$ alone. A factor depending only on $y$ may be found if

$$
\frac{N_x-M_y}{M}
$$

is a function of $y$ alone. These tests are useful, but they should be applied after the simpler classifications have been checked.

## Visual

```mermaid
flowchart TD
  A[First-order ODE] --> B{"Can write y' = g(x)h(y)?"}
  B -->|yes| C[Separate variables]
  B -->|no| D{"Linear: y' + p(x)y = r(x)?"}
  D -->|yes| E[Use integrating factor]
  D -->|no| F{"Exact: M_y = N_x?"}
  F -->|yes| G["Find potential u("x,y")"]
  F -->|no| H{"Bernoulli form?"}
  H -->|yes| I["Substitute v = y^(1-a)"]
  H -->|no| J[Use qualitative or numerical method]
```

| Form | Recognition cue | Main move | Frequent check |
|---|---|---|---|
| Separable | $y'=g(x)h(y)$ | Put $y$ terms with $dy$ and $x$ terms with $dx$ | Add lost equilibrium solutions |
| Linear | $y'+p(x)y=r(x)$ | Multiply by $\mu=e^{\int p\,dx}$ | Left side becomes $(\mu y)'$ |
| Exact | $M\,dx+N\,dy=0$, $M_y=N_x$ | Find $u_x=M$, $u_y=N$ | Final answer is implicit $u=C$ |
| Bernoulli | $y'+py=gy^a$ | Use $v=y^{1-a}$ | Exclude $a=0,1$ cases |
| Autonomous | $y'=f(y)$ | Phase line and equilibria | Arrows match sign of $f$ |

## Worked example 1: Mixing tank with a linear equation

Problem. A tank initially contains $100$ L of water with $20$ g of salt. Brine containing $0.5$ g/L enters at $4$ L/min, and the well-mixed solution leaves at $4$ L/min. Find the salt amount $A(t)$.

Method.

1. The volume stays $100$ L because inflow equals outflow.
2. Rate in is

$$
0.5\frac{\mathrm{g}}{\mathrm{L}}\cdot 4\frac{\mathrm{L}}{\mathrm{min}}=2\frac{\mathrm{g}}{\mathrm{min}}.
$$

3. Rate out uses tank concentration $A(t)/100$:

$$
\frac{A(t)}{100}\frac{\mathrm{g}}{\mathrm{L}}\cdot 4\frac{\mathrm{L}}{\mathrm{min}}=\frac{A(t)}{25}\frac{\mathrm{g}}{\mathrm{min}}.
$$

4. The balance law gives

$$
A'=2-\frac{A}{25},\qquad A(0)=20.
$$

5. Put it in linear standard form:

$$
A'+\frac{1}{25}A=2.
$$

6. The integrating factor is

$$
\mu(t)=e^{\int (1/25)\,dt}=e^{t/25}.
$$

7. Multiply and integrate:

$$
\begin{aligned}
e^{t/25}A'+\frac{1}{25}e^{t/25}A &= 2e^{t/25},\\
(e^{t/25}A)' &= 2e^{t/25},\\
e^{t/25}A &= 50e^{t/25}+C.
\end{aligned}
$$

8. Hence

$$
A(t)=50+Ce^{-t/25}.
$$

9. Use $A(0)=20$:

$$
20=50+C,\qquad C=-30.
$$

Answer.

$$
A(t)=50-30e^{-t/25}.
$$

Check. The steady amount is $50$ g because the incoming concentration $0.5$ g/L in a $100$ L tank corresponds to $50$ g. Since the initial amount is $20$ g, the solution increases toward $50$.

## Worked example 2: Bernoulli equation reduced to linear form

Problem. Solve

$$
y'+\frac{2}{x}y=x^2y^2,\qquad x>0.
$$

Method.

1. This is Bernoulli with $a=2$, $p(x)=2/x$, and $g(x)=x^2$.
2. Use

$$
v=y^{1-a}=y^{-1}.
$$

3. Differentiate:

$$
v'=-y^{-2}y'.
$$

4. Divide the original equation by $y^2$ where $y\ne 0$:

$$
y^{-2}y'+\frac{2}{x}y^{-1}=x^2.
$$

5. Substitute $y^{-2}y'=-v'$ and $y^{-1}=v$:

$$
-v'+\frac{2}{x}v=x^2.
$$

6. Multiply by $-1$:

$$
v'-\frac{2}{x}v=-x^2.
$$

7. This is linear. The integrating factor is

$$
\mu(x)=e^{\int -2/x\,dx}=e^{-2\ln x}=x^{-2}.
$$

8. Multiply:

$$
x^{-2}v'-2x^{-3}v=-1.
$$

9. Recognize the product derivative:

$$
\begin{aligned}
(x^{-2}v)'&=-1,\\
x^{-2}v&=-x+C,\\
v&=Cx^2-x^3.
\end{aligned}
$$

10. Return to $y$:

$$
\frac{1}{y}=Cx^2-x^3=x^2(C-x).
$$

Answer.

$$
y(x)=\frac{1}{x^2(C-x)},\qquad x>0,
$$

with the additional solution $y=0$ from the original equation.

Check. Substituting $v=x^2(C-x)$ into $v'-(2/x)v=-x^2$ gives

$$
2x(C-x)-x^2-\frac{2}{x}x^2(C-x)=-x^2,
$$

so the transformed equation is satisfied.

## Code

```python
import numpy as np
from scipy.integrate import solve_ivp

def tank_rhs(t, A):
    return 2.0 - A[0] / 25.0

t_eval = np.linspace(0.0, 150.0, 301)
sol = solve_ivp(tank_rhs, (0.0, 150.0), [20.0], t_eval=t_eval)
exact = 50.0 - 30.0 * np.exp(-t_eval / 25.0)
max_error = np.max(np.abs(sol.y[0] - exact))

print(f"computed final amount = {sol.y[0, -1]:.4f} g")
print(f"exact final amount    = {exact[-1]:.4f} g")
print(f"max error on grid     = {max_error:.2e}")
```

## Common pitfalls

- Dividing by $y$, $1-y$, or another factor without checking whether it gives an equilibrium solution.
- Using the integrating factor before the equation is in the normalized form $y'+p(x)y=r(x)$.
- Forgetting the constant of integration after integrating $(\mu y)'$.
- Treating an implicit solution $u(x,y)=C$ as if it must always be solved explicitly for $y$.
- Missing interval restrictions such as $x\gt 0$ when $\ln x$ or $x^{-1}$ appears.
- Ignoring units in models; a term with units of amount cannot be added to a term with units of amount per time.
- Reporting only the algebraic family and skipping the initial condition. For an initial value problem, the constant must be determined and the final curve should be checked against the starting value.
- Assuming every first-order model has a closed elementary form. Direction fields and numerical solvers are legitimate tools when recognition tests fail.

## Connections

- [Direction Fields and Existence](/math/engineering-math/direction-fields-and-existence)
- [Second-Order Linear ODEs](/math/engineering-math/second-order-linear-odes)
- [Systems of ODEs and Phase Planes](/math/engineering-math/systems-of-odes-and-phase-plane)
- [Laplace Transform](/math/engineering-math/laplace-transform)
- [Numerical Methods Overview](/math/engineering-math/numerical-methods-overview)
