---
title: Linear Systems, Transfer Functions, and Modes
sidebar_position: 6
---

# Linear Systems, Transfer Functions, and Modes

Linear system analysis gives simulation a set of benchmarks. When a model is linear and time invariant, its response can be studied through poles, zeros, transfer functions, eigenvalues, and frequency response. These tools explain what a time plot should look like before the simulation is run: exponential decay, oscillation, overshoot, resonance, filtering, or instability.

In a simulation workflow, linear analysis is useful in two directions. First, a known transfer function or state model can be simulated and checked against analytical results. Second, a nonlinear model can be linearized around an operating point so its local modes and frequency response can be understood. This page connects the simulation notes to the broader signals-and-systems material.

## Definitions

A continuous-time LTI state-space model is

$$
\dot{x}=Ax+Bu,\qquad y=Cx+Du.
$$

For zero initial conditions, its transfer function is

$$
G(s)=\frac{Y(s)}{U(s)}=C(sI-A)^{-1}B+D
$$

for single-input single-output systems, or a transfer matrix for multi-input multi-output systems.

A pole is a value of $s$ where the transfer function becomes unbounded, after cancellations. Poles determine natural response terms. A zero is a value of $s$ where the transfer function is zero. Zeros shape forced response and can create undershoot or phase lag.

The impulse response $g(t)$ is the output due to a unit impulse input under zero initial conditions. The step response is the output due to $u(t)=1$ for $t\ge0$. The frequency response is

$$
G(j\omega),
$$

obtained by evaluating the transfer function on the imaginary axis when the system is stable.

For a second-order denominator

$$
s^2+2\zeta\omega_n s+\omega_n^2,
$$

$\omega_n$ is the natural frequency and $\zeta$ is the damping ratio. These parameters directly predict the shape of the time response.

## Key results

The modes of an LTI state model are associated with eigenvalues of $A$. If $A$ has an eigenvalue $\lambda$, the natural response includes a term like $e^{\lambda t}$, possibly multiplied by polynomials if repeated eigenvalues are defective. Stability for a continuous-time LTI system requires all internal modes to have negative real parts:

$$
\operatorname{Re}(\lambda_i)<0
\quad\text{for all }i.
$$

For a standard underdamped second-order system with $0\lt \zeta\lt 1$, poles are

$$
s=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}.
$$

The damped natural frequency is

$$
\omega_d=\omega_n\sqrt{1-\zeta^2}.
$$

The percent overshoot for a unit step in the standard form is

$$
M_p=100\exp\left(\frac{-\zeta\pi}{\sqrt{1-\zeta^2}}\right)\%.
$$

Frequency response connects sinusoidal input to steady-state sinusoidal output. If

$$
u(t)=A\cos(\omega t),
$$

then after transients decay,

$$
y_\text{ss}(t)=A|G(j\omega)|\cos(\omega t+\angle G(j\omega)).
$$

This result is essential when interpreting simulated filters, mechanical resonance, aircraft modes, or electrical circuits.

Linear results are also useful as regression tests for simulation software. If a Simulink block diagram built from integrators does not match the `step` response of the equivalent transfer function, the problem is usually not subtle mathematics; it is a sign error, an initial condition mismatch, a parameter typo, or a solver setting difference. Before adding nonlinearities, limits, or controllers, it is good practice to verify the underlying linear plant against a compact analytical or Control System Toolbox representation.

Modes should be interpreted with the output in mind. A state matrix may contain several eigenvalues, but not every mode is equally visible in every output. Some modes are weakly excited by a given input, and some are weakly observed by a given sensor. This is why a simulation report should state both the internal mode analysis and the specific time response being plotted. A mode that is invisible in one output can still matter for actuator limits, internal stress, or later nonlinear coupling.

Frequency-domain checks give another way to detect time-domain mistakes. If a simulated sinusoidal input at frequency $\omega$ produces a steady output amplitude that does not match $\vert G(j\omega)\vert $, then the input amplitude, transient removal, sample rate, or model implementation should be questioned. Likewise, a step response with an unexpected final value should be compared with the DC gain $G(0)$. These comparisons are quick and often catch errors before a large nonlinear or hybrid model is built on top of a faulty linear subsystem.

In Simulink, linear subsystems can be represented at different levels of abstraction. A Transfer Fcn block is compact and convenient for response checks. A State-Space block makes multi-input and multi-output systems straightforward. An integrator-level realization is longer but exposes internal variables and lets the modeler insert nonlinearities, saturations, limits, and sensors at physically meaningful points. Choosing the right representation depends on what must be inspected or modified during the simulation study.

Initial conditions are the other reason state-space form remains important. A transfer function describes zero-state input-output behavior by default; a physical simulation often starts with stored energy already present. A charged capacitor, moving mass, warm object, or nonzero aircraft attitude can produce output before any new input is applied. If that initial condition is part of the problem, the state model gives the cleanest way to specify it and to separate forced response from natural response.

## Visual

```mermaid
flowchart LR
  A[State model A,B,C,D] --> B[Eigenvalues of A]
  A --> C[Transfer function G(s)]
  B --> D[Modes and stability]
  C --> E[Poles and zeros]
  C --> F[Step and impulse response]
  C --> G[Frequency response G(jw)]
  D --> H[Expected time plot]
  E --> H
  F --> H
  G --> I[Expected sinusoidal gain and phase]
```

| Pole location | Time-domain behavior | Simulation clue |
|---|---|---|
| Negative real pole | Decaying exponential | Monotone approach if dominant |
| Positive real pole | Growing exponential | Divergence even without sustained input |
| Complex pair with negative real part | Decaying oscillation | Ringing with envelope decay |
| Pure imaginary pair | Sustained oscillation | No decay in ideal linear model |
| Complex pair with positive real part | Growing oscillation | Oscillatory instability |

## Worked example 1: Predict a step response from poles

Problem: Analyze

$$
G(s)=\frac{9}{s^2+3s+9}.
$$

Find $\omega_n$, $\zeta$, damped frequency, percent overshoot, steady-state step value, and the expected time-response plot.

1. Compare with standard form:

$$
s^2+2\zeta\omega_n s+\omega_n^2.
$$

Thus

$$
\omega_n^2=9,\qquad \omega_n=3.
$$

2. Match the $s$ coefficient:

$$
2\zeta\omega_n=3.
$$

Substitute $\omega_n=3$:

$$
6\zeta=3,\qquad \zeta=0.5.
$$

3. Damped natural frequency:

$$
\omega_d=3\sqrt{1-0.5^2}
=3\sqrt{0.75}
\approx2.598\ \mathrm{rad/s}.
$$

4. Percent overshoot:

$$
M_p=100\exp\left(\frac{-0.5\pi}{\sqrt{0.75}}\right)
\approx100e^{-1.814}
\approx16.3\%.
$$

5. Step steady state:

$$
G(0)=\frac{9}{9}=1.
$$

Checked answer: a unit-step response should rise toward $1$, overshoot to about $1.163$, oscillate with damped frequency about $2.6\ \mathrm{rad/s}$, and settle as the real part $-\zeta\omega_n=-1.5$ damps the response.

Simulink description: use a Step block feeding a Transfer Fcn block with numerator `[9]` and denominator `[1 3 9]`. A Scope should show the underdamped response. A To Workspace block can export the response for measuring peak time and overshoot.

## Worked example 2: State matrix modes and transfer function

Problem: The state model is

$$
A=\begin{bmatrix}0&1\\-4&-4\end{bmatrix},
\qquad
B=\begin{bmatrix}0\\1\end{bmatrix},
\qquad
C=\begin{bmatrix}1&0\end{bmatrix},
\qquad
D=0.
$$

Find the transfer function and determine stability.

1. Compute $sI-A$:

$$
sI-A=
\begin{bmatrix}
s & -1\\
4 & s+4
\end{bmatrix}.
$$

2. Compute the determinant:

$$
\det(sI-A)=s(s+4)-(-1)(4)=s^2+4s+4=(s+2)^2.
$$

3. Invert the matrix:

$$
(sI-A)^{-1}
=\frac{1}{(s+2)^2}
\begin{bmatrix}
s+4 & 1\\
-4 & s
\end{bmatrix}.
$$

4. Multiply by $B$:

$$
(sI-A)^{-1}B
=\frac{1}{(s+2)^2}
\begin{bmatrix}
1\\
s
\end{bmatrix}.
$$

5. Multiply by $C$:

$$
G(s)=C(sI-A)^{-1}B
=\frac{1}{(s+2)^2}.
$$

6. Determine stability. The pole is repeated at $s=-2$, so all poles have negative real parts.

Checked answer: the system is stable and critically damped. A unit-step response should approach $G(0)=1/4$ without oscillation, with a shape containing terms $e^{-2t}$ and $te^{-2t}$.

Simulink description: a State-Space block with these matrices or a Transfer Fcn block with denominator `[1 4 4]` and numerator `[1]` should give the same zero-initial-condition output. If the state initial condition is nonzero, the State-Space block exposes natural response effects that a simple transfer-function step comparison may not show.

## Code

```matlab
clear; clc; close all;

% Second-order transfer function
G = tf(9, [1 3 9]);
figure;
subplot(2,1,1);
step(G); grid on;
title('Underdamped step response');

subplot(2,1,2);
bode(G); grid on;
title('Frequency response');

% State-space model and conversion
A = [0 1; -4 -4];
B = [0; 1];
C = [1 0];
D = 0;
sys = ss(A, B, C, D);
G_from_state = tf(sys);
disp(G_from_state);

figure;
step(sys); grid on;
title('Critically damped state-space step response');
```

The Bode plot for the first system should show a resonance-like rise because $\zeta=0.5$ is underdamped, but the peak is moderate. The state-space step response should approach $0.25$ monotonically. These analytical predictions are useful before trusting any Simulink output.

## Common pitfalls

- Treating transfer function stability as the whole story when a state realization may contain hidden unstable canceled modes.
- Forgetting that `step` assumes zero initial conditions unless told otherwise.
- Reading frequency response from a transient time plot before transients have decayed.
- Confusing natural frequency $\omega_n$ with damped frequency $\omega_d$.
- Comparing continuous-time pole locations to discrete-time pole criteria. Continuous-time stability uses the left half-plane; discrete-time stability uses the unit circle.
- Ignoring units on frequency. MATLAB often reports rad/s, while experimental data may be in Hz.

## Connections

- [Laplace Transform and ROC](/physics/signals-systems/laplace-transform-roc)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
- [State-Space Representation](/physics/simulation/state-space-representation)
- [Discrete-Time and Sampled-Data Systems](/physics/simulation/discrete-time-sampled-data-systems)
