---
title: Nonlinear Systems and Linearization
sidebar_position: 7
---

# Nonlinear Systems and Linearization

Nonlinear systems are the rule rather than the exception in realistic simulation. Friction changes sign, actuators saturate, valves have square-root flow laws, biological populations grow with limiting effects, and chemical reaction rates multiply concentrations. Linear tools are still valuable, but only after the modeler recognizes where the nonlinearities enter and what operating region is being studied.

Linearization builds a local linear approximation around an equilibrium or trajectory. It does not make the original system linear; it gives a model that predicts small deviations near the chosen point. This is especially useful for controller design, small-signal frequency response, and quick stability checks before running large nonlinear simulations.

## Definitions

A nonlinear state model has the form

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u}),
\qquad
\mathbf{y}=\mathbf{g}(\mathbf{x},\mathbf{u}).
$$

An equilibrium $(\bar{\mathbf{x}},\bar{\mathbf{u}})$ satisfies

$$
\mathbf{0}=\mathbf{f}(\bar{\mathbf{x}},\bar{\mathbf{u}}).
$$

Deviation variables measure small changes from the operating point:

$$
\delta\mathbf{x}=\mathbf{x}-\bar{\mathbf{x}},
\qquad
\delta\mathbf{u}=\mathbf{u}-\bar{\mathbf{u}},
\qquad
\delta\mathbf{y}=\mathbf{y}-\bar{\mathbf{y}}.
$$

The first-order Taylor approximation gives

$$
\delta\dot{\mathbf{x}}
=A\delta\mathbf{x}+B\delta\mathbf{u},
\qquad
\delta\mathbf{y}=C\delta\mathbf{x}+D\delta\mathbf{u},
$$

where the Jacobian matrices are evaluated at the operating point:

$$
A=\left.\frac{\partial \mathbf{f}}{\partial \mathbf{x}}\right|_{\bar{x},\bar{u}},
\quad
B=\left.\frac{\partial \mathbf{f}}{\partial \mathbf{u}}\right|_{\bar{x},\bar{u}},
\quad
C=\left.\frac{\partial \mathbf{g}}{\partial \mathbf{x}}\right|_{\bar{x},\bar{u}},
\quad
D=\left.\frac{\partial \mathbf{g}}{\partial \mathbf{u}}\right|_{\bar{x},\bar{u}}.
$$

Common nonlinear elements include saturation, dead zone, relay, Coulomb friction, backlash, hysteresis, quantization, square-root flow, and products of states.

## Key results

Linearization is a local approximation. For a scalar function $f(x,u)$,

$$
f(x,u)\approx f(\bar{x},\bar{u})
+\left.\frac{\partial f}{\partial x}\right|_{\bar{x},\bar{u}}(x-\bar{x})
+\left.\frac{\partial f}{\partial u}\right|_{\bar{x},\bar{u}}(u-\bar{u}).
$$

At an equilibrium, $f(\bar{x},\bar{u})=0$, so the constant term disappears in deviation coordinates. Away from equilibrium, the constant term must be retained or the system must be linearized along a trajectory.

For a nonlinear scalar first-order model

$$
\dot{x}=f(x),
$$

an equilibrium $\bar{x}$ is locally stable if

$$
f'(\bar{x})<0,
$$

unstable if $f'(\bar{x})\gt 0$, and inconclusive by first-order linearization if $f'(\bar{x})=0$.

Saturation changes effective system behavior. A commanded input $u_c$ passed through saturation is

$$
u=\operatorname{sat}(u_c)=
\begin{cases}
u_\text{max}, & u_c>u_\text{max},\\
u_c, & u_\text{min}\le u_c\le u_\text{max},\\
u_\text{min}, & u_c<u_\text{min}.
\end{cases}
$$

Inside the linear range, the slope is one; outside, the slope is zero. A linearization taken in saturation therefore may predict loss of control authority.

The operating point must be stored together with the linear model. The matrices $A$, $B$, $C$, and $D$ describe deviations, not absolute variables, unless the model has been written in absolute affine form. For example, a tank linearized at $h=4$ meters and another tank linearized at $h=1$ meter can have different outlet slopes. If their matrices are saved without the corresponding equilibrium heights and inputs, later comparisons can be misleading.

For simulation studies, a useful workflow is to run the nonlinear model and the linearized model side by side under the same small perturbation. Agreement near the operating point verifies the Jacobian and confirms that the perturbation is small enough. Disagreement under a larger perturbation is not necessarily a failure; it is often the expected evidence that nonlinear behavior is important. The time-response plot should therefore be read as an operating-range test, not only as a prediction.

Linearization can also be performed numerically when symbolic derivatives are inconvenient, but the perturbation size must be chosen carefully. Too large a perturbation measures curvature rather than local slope; too small a perturbation can be dominated by roundoff or solver noise. MATLAB and Simulink linearization tools automate much of this process, yet the resulting matrices still need physical review: signs, units, equilibrium values, and expected mode locations should all be checked.

## Visual

```mermaid
flowchart TD
  A["Nonlinear model xdot=f("#quot;x,u#quot;")"] --> B[Find operating point]
  B --> C{"Equilibrium?"}
  C -->|yes| D[Use deviation variables]
  C -->|no| E[Linearize along trajectory or keep affine term]
  D --> F["Compute Jacobians A,B,C,D"]
  E --> F
  F --> G[Analyze local modes and response]
  G --> H[Compare with nonlinear simulation]
  H -->|small deviations agree| I[Use linear model locally]
  H -->|large deviations differ| J[Use nonlinear model]
```

| Nonlinearity | Mathematical feature | Simulation effect | Linearization warning |
|---|---|---|---|
| Saturation | Clipped input/output | Limited response and windup risk | Slope may become zero |
| Dead zone | No output near zero | Delayed response | Linear slope depends on operating point |
| Coulomb friction | Sign function | Stick-slip and discontinuity | Not differentiable at zero velocity |
| Square-root flow | $\sqrt{h}$ | State-dependent time constant | Derivative large near zero |
| Product term | $xy$ or $xu$ | Coupled gain changes | Jacobian depends on both variables |

## Worked example 1: Linearize a nonlinear tank outlet

Problem: A tank obeys

$$
A\dot{h}=q_\text{in}-k\sqrt{h}
$$

with $A=2$, $k=0.6$, and nominal inflow $\bar{q}_\text{in}=1.2$. Find the equilibrium height and the linearized model in deviation variables.

1. Write the scalar state equation:

$$
\dot{h}=f(h,q)=\frac{1}{A}(q-k\sqrt{h}).
$$

2. Find equilibrium by setting $\dot{h}=0$:

$$
0=\bar{q}-k\sqrt{\bar{h}}.
$$

3. Solve for $\bar{h}$:

$$
\sqrt{\bar{h}}=\frac{\bar{q}}{k}=\frac{1.2}{0.6}=2,
\qquad
\bar{h}=4.
$$

4. Compute the Jacobian with respect to $h$:

$$
\frac{\partial f}{\partial h}
=\frac{1}{A}\left(-k\frac{1}{2\sqrt{h}}\right)
=-\frac{k}{2A\sqrt{h}}.
$$

At $\bar{h}=4$,

$$
A_\ell=-\frac{0.6}{2(2)(2)}=-0.075.
$$

5. Compute the input Jacobian:

$$
B_\ell=\frac{\partial f}{\partial q}=\frac{1}{A}=0.5.
$$

6. Write deviation model:

$$
\delta\dot{h}=-0.075\delta h+0.5\delta q.
$$

Checked answer: the local time constant is $1/0.075\approx13.33\ \mathrm{s}$. The time-response plot for a small inflow step should resemble a first-order exponential around $h=4$. For a large step, the nonlinear square-root law changes the effective slope and the linear approximation becomes less accurate.

Simulink description: the nonlinear model uses a Sqrt block in the outlet feedback. The linearized model uses a Sum, Gain $0.5$ on $\delta q$, Gain $-0.075$ on $\delta h$, and an Integrator for $\delta h$. Plot both absolute height responses using $h=\bar{h}+\delta h$.

## Worked example 2: Linearize a pendulum near downward equilibrium

Problem: A damped pendulum satisfies

$$
\ddot{\theta}+\frac{b}{m\ell^2}\dot{\theta}+\frac{g}{\ell}\sin\theta=\frac{1}{m\ell^2}\tau.
$$

Let $x_1=\theta$, $x_2=\dot{\theta}$, and input $u=\tau$. Linearize about $\bar{\theta}=0$, $\bar{\dot{\theta}}=0$, $\bar{u}=0$.

1. Write the state equations:

$$
\begin{aligned}
\dot{x}_1 &= x_2,\\
\dot{x}_2 &= -\frac{b}{m\ell^2}x_2-\frac{g}{\ell}\sin x_1+\frac{1}{m\ell^2}u.
\end{aligned}
$$

2. Compute partial derivatives for the first equation:

$$
\frac{\partial \dot{x}_1}{\partial x_1}=0,\qquad
\frac{\partial \dot{x}_1}{\partial x_2}=1,\qquad
\frac{\partial \dot{x}_1}{\partial u}=0.
$$

3. Compute partial derivatives for the second equation:

$$
\frac{\partial \dot{x}_2}{\partial x_1}
=-\frac{g}{\ell}\cos x_1,
\qquad
\frac{\partial \dot{x}_2}{\partial x_2}
=-\frac{b}{m\ell^2},
\qquad
\frac{\partial \dot{x}_2}{\partial u}
=\frac{1}{m\ell^2}.
$$

4. Evaluate at $x_1=0$:

$$
\cos 0=1.
$$

5. Assemble matrices:

$$
A=
\begin{bmatrix}
0 & 1\\
-g/\ell & -b/(m\ell^2)
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
0\\
1/(m\ell^2)
\end{bmatrix}.
$$

Checked answer: the small-angle approximation $\sin\theta\approx\theta$ gives the same result. The nonlinear and linear time-response plots should agree for small initial angles such as $5^\circ$, but diverge for large angles such as $60^\circ$ because the sine curve is no longer close to its tangent.

Simulink description: create the nonlinear pendulum with a Trigonometric Function block for `sin`, damping feedback, torque input, and two integrators. The linear model can use a State-Space block. Scope both angles on the same plot.

## Code

```matlab
clear; clc; close all;

% Nonlinear tank versus local linear model
A = 2; k = 0.6; qbar = 1.2; hbar = (qbar/k)^2;
dfdh = -k/(2*A*sqrt(hbar));
dfdq = 1/A;

qstep = 0.1;
nonlinear_tank = @(t,h) (qbar + qstep - k*sqrt(max(h,0)))/A;
linear_tank = @(t,dh) dfdh*dh + dfdq*qstep;
[tn, hn] = ode45(nonlinear_tank, [0 80], hbar);
[tl, dhl] = ode45(linear_tank, [0 80], 0);

figure;
plot(tn, hn, 'b-', tl, hbar + dhl, 'r--', 'LineWidth', 1.4);
grid on; xlabel('Time (s)'); ylabel('Height (m)');
legend('Nonlinear', 'Linearized', 'Location', 'best');
title('Nonlinear tank and local linear approximation');

% Pendulum nonlinear versus linear for small initial angle
m = 1; ell = 1; b = 0.1; g = 9.81;
x0 = [5*pi/180; 0];
pend_nl = @(t,x) [x(2); -(b/(m*ell^2))*x(2) - (g/ell)*sin(x(1))];
Apend = [0 1; -g/ell -b/(m*ell^2)];
pend_lin = @(t,x) Apend*x;
[t1, xnl] = ode45(pend_nl, [0 10], x0);
[t2, xlin] = ode45(pend_lin, [0 10], x0);

figure;
plot(t1, xnl(:,1), 'b-', t2, xlin(:,1), 'r--', 'LineWidth', 1.4);
grid on; xlabel('Time (s)'); ylabel('\theta (rad)');
legend('Nonlinear', 'Linearized', 'Location', 'best');
title('Small-angle pendulum comparison');
```

The tank plot should show close agreement for the small inflow perturbation. The pendulum plot should show nearly identical small-angle motion; increasing the initial angle reveals the limits of linearization. These comparisons are stronger than simply deriving a Jacobian because they show the operating range over which the approximation is useful.

## Common pitfalls

- Linearizing before finding a valid operating point. The constant term will not vanish unless the point is an equilibrium.
- Applying a small-signal model to a large transient, especially through saturation or dead-zone regions.
- Differentiating discontinuous nonlinearities as if they were smooth. Friction, relays, and quantizers need special treatment.
- Forgetting to convert deviation outputs back to physical variables before comparing with nonlinear simulation.
- Assuming stability of the linearized model proves global nonlinear stability. It only gives local information under appropriate conditions.
- Ignoring units in Jacobians. Each matrix entry has units determined by the derivative it represents.

## Connections

- [State-Space Representation](/physics/simulation/state-space-representation)
- [Simulink Block Diagrams](/physics/simulation/simulink-block-diagrams)
- [Linear Systems, Transfer Functions, and Modes](/physics/simulation/linear-systems-transfer-functions-modes)
- [System Properties](/physics/signals-systems/system-properties)
