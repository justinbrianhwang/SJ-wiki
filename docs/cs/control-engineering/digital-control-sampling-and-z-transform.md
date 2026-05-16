---
title: Digital Control, Sampling, and the z-Transform
sidebar_position: 17
---

# Digital Control, Sampling, and the z-Transform

Digital controllers place a computer in the loop. Nise's final chapter shows how continuous signals, sampled data, zero-order holds, and pulse transfer functions let classical control ideas move from the $s$-plane to the $z$-plane. The practical motivation is strong: software can implement compensators, schedule multiple loops, change parameters, and integrate diagnostics more flexibly than fixed analog hardware.

Sampling also adds new design constraints. The controller sees signals only at sampling instants, the hold reconstructs an actuator command between samples, and computational delay can reduce phase margin. Digital control is not just analog control typed into a processor; it is a sampled-data system with its own transform and stability geometry.

## Definitions

The one-sided z-transform of a sequence $x[n]$ is

$$
X(z)=\sum_{n=0}^\infty x[n]z^{-n}.
$$

If a continuous signal $x(t)$ is sampled with period $T$, then

$$
x[n]=x(nT).
$$

A **sampler** converts a continuous signal into a sequence. A **zero-order hold** holds each digital output value constant over one sampling interval. Its continuous transfer function is

$$
G_{zoh}(s)=\frac{1-e^{-sT}}{s}
$$

when represented as a hold operation preceding a continuous plant in sampled-data derivations.

The mapping between continuous and discrete poles under exact sampling is

$$
z=e^{sT}.
$$

Thus $s=0$ maps to $z=1$, the left half-plane maps inside the unit circle, and the imaginary axis maps onto the unit circle.

A discrete transfer function has the form

$$
G(z)=\frac{B(z)}{A(z)}.
$$

The discrete system is stable when all poles lie inside the unit circle:

$$
|z_i|<1.
$$

## Key results

The $s$-plane and $z$-plane correspond as follows:

| Continuous-time feature | Discrete-time counterpart |
|---|---|
| Laplace transform | z-transform |
| $s$-plane imaginary-axis stability boundary | unit circle $\lvert z\rvert=1$ |
| stable LHP pole | pole inside unit circle |
| integrator pole at $s=0$ | pole at $z=1$ |
| $e^{sT}$ mapping | sampled pole location |
| Routh-Hurwitz style test | Jury test or direct root check |

The z-transform turns difference equations into algebraic equations. For example, if

$$
y[n]-0.8y[n-1]=u[n],
$$

then

$$
Y(z)-0.8z^{-1}Y(z)=U(z),
$$

so

$$
\frac{Y(z)}{U(z)}=\frac{1}{1-0.8z^{-1}}=\frac{z}{z-0.8}.
$$

Digital steady-state error parallels analog steady-state error. Poles at $z=1$ play the role of integrators. A discrete Type 1 loop has one pole at $z=1$ in the forward pulse transfer function and can track a step with zero error under the usual stability assumptions.

Sampling period matters. Very slow sampling can distort transient response, reduce stability margin, and create aliasing. Very fast sampling improves approximation to continuous control but increases computation, noise sensitivity, and hardware demands. A common engineering starting point is to sample many times faster than the desired closed-loop bandwidth, then verify with the actual implementation.

The zero-order hold is not a minor implementation detail. It makes the actuator command piecewise constant, which introduces effective delay and changes the plant seen by the digital controller. A continuous plant discretized with zero-order hold generally has a different pulse transfer function from one obtained by merely replacing $s$ with a finite-difference expression. For accurate sampled-data design, the hold and sampling assumptions should match the real hardware.

Aliasing is another sampling constraint. If unfiltered measurement noise or plant vibration exists above half the sampling frequency, it can appear as a lower-frequency signal in the sampled data. The controller may then react to a false signal. Anti-alias filtering and a sampling rate chosen with sensor bandwidth in mind are part of control design, not just data-acquisition housekeeping.

Quantization affects both measurement and actuation. An ADC maps a continuous voltage into finite counts, and a PWM or DAC maps the computed command into finite output resolution. Quantization can create limit cycles, especially when the plant has friction or the controller has integral action. Linear analysis usually ignores quantization, so embedded implementations need simulation or testing with realistic numeric limits.

Computational delay is often modeled as one or more factors of $z^{-1}$. Even if the sampling period is fixed, the controller may read sensors, compute the law, and update actuators later in the cycle. That delay adds phase lag and can reduce stability margin. Real-time scheduling and interrupt jitter therefore have direct control consequences.

Digital control preserves many classical ideas but changes their geometry. Stable continuous poles lie in the left half-plane; stable discrete poles lie inside the unit circle. Continuous integrators sit at $s=0$; digital integrators sit at $z=1$. Continuous oscillation frequency maps to angle around the unit circle. Keeping these translations visible prevents most early mistakes in sampled-data analysis.

The inverse z-transform also differs in flavor from inverse Laplace work. Long division of $C(z)$ by powers of $z^{-1}$ immediately produces the output samples $c[0],c[1],c[2],\ldots$. Partial fractions can produce a closed-form expression for $c[n]$. In control design, the sample sequence is often more useful than a continuous-looking formula because the controller only updates at those instants.

Discrete transfer functions depend on where sampling occurs. Cascading two continuous subsystems and then sampling the final output is not generally equivalent to multiplying two separately sampled pulse transfer functions unless a sampler and hold separate the subsystems in the required way. This is a major sampled-data modeling issue. Block-diagram reduction in the $z$-domain is valid only when the signals between blocks are discrete sequences at the same sampling instants.

Sampling also affects what "overshoot" means. The true continuous output between samples may peak higher than the sampled values show, especially with a slow sampling period or lightly damped plant. A digital simulation that plots only sample points can therefore underreport intersample overshoot. For physical plants, check the continuous response reconstructed through the zero-order hold and plant dynamics, not only the discrete sequence.

Finally, the sampling period is part of the controller design. Changing $T$ moves every mapped pole $z=e^{sT}$ and changes the discrete equivalent of the plant. A controller tuned for $T=0.01$ s is not the same controller at $T=0.05$ s, even if the difference equation looks similar. Timing must be treated as a specified design parameter.

The discrete model should also state whether signals are indexed before or after the control update. Some texts use $u[n]$ as the command computed from $e[n]$ and held immediately; real processors may apply that value one sample later. A single indexing convention prevents hidden delays.

That convention should match the firmware timing diagram and test logs.

Otherwise analysis and implementation silently diverge.

Record it explicitly.

Then test it.

## Visual

```mermaid
flowchart LR
  R["Continuous reference r(t)"] --> SamplerR["#quot;Sampler: r[n"] = r(nT)"]
  SamplerR --> Sum(("Σ"))
  Yfb["#quot;Digital feedback y[n"]"] -->|"negative input"| Sum
  Sum --> E["#quot;Error sequence e[n"]"]
  E --> Delay["Computation / scheduling delay: z^-d"]
  Delay --> Dz["Digital controller D(z): difference equation"]
  Dz --> QuantU["DAC/PWM quantization"]
  QuantU --> ZOH["Zero-order hold: u(t) held over [nT, (n+1)T)"]
  ZOH --> Plant["Continuous plant G_p(s)"]
  Dist["Disturbance d(t)"] --> Plant
  Plant --> Y["Continuous output y(t)"]
  Y --> AntiAlias["Anti-alias filter"]
  AntiAlias --> ADC["ADC sampler + quantizer"]
  ADC --> Yfb
  Clock["Sampling clock period T"] -. "sets update instants" .-> SamplerR
  Clock -. "sets update instants" .-> ADC
  Clock -. "sets hold interval" .-> ZOH
  Dz --> ZPlane["z-plane model: poles must lie inside the unit circle"]
  Plant --> Mapping["Exact pole mapping for sampled modes: z = exp(sT)"]
  ZPlane --> Output(("Sampled-data closed-loop response"))
  Mapping --> Output
```

This diagram shows the sampled-data loop with the sampler, digital controller, computation delay, DAC/PWM quantization, zero-order hold, continuous plant, anti-alias filter, and ADC feedback all in the signal path. The shape transition is explicit: continuous signals `r(t)` and `y(t)` become sequences `r[n]`, `e[n]`, and `y[n]`, while the hold converts the digital command back into a piecewise-constant continuous input.

## Worked example 1: mapping continuous poles to the z-plane

Problem: Continuous closed-loop poles are

$$
s=-2\pm j3.
$$

With sampling period $T=0.1$ s, find the corresponding $z$-plane poles.

Method:

1. Use

$$
z=e^{sT}.
$$

2. Substitute:

$$
z=e^{(-2\pm j3)(0.1)}
=e^{-0.2}e^{\pm j0.3}.
$$

3. Magnitude:

$$
e^{-0.2}=0.8187.
$$

4. Rectangular form:

$$
z=0.8187(\cos0.3\pm j\sin0.3).
$$

5. Evaluate:

$$
\cos0.3=0.9553,\qquad \sin0.3=0.2955.
$$

Therefore

$$
z=0.782\pm j0.242.
$$

Checked answer: the poles are approximately $0.782\pm j0.242$, inside the unit circle.

## Worked example 2: z-transform of a difference equation

Problem: Find the transfer function for

$$
y[n]=0.6y[n-1]+2u[n]-u[n-1].
$$

Method:

1. Move all output terms to the left:

$$
y[n]-0.6y[n-1]=2u[n]-u[n-1].
$$

2. Apply the z-transform with zero initial conditions:

$$
Y(z)-0.6z^{-1}Y(z)=2U(z)-z^{-1}U(z).
$$

3. Factor:

$$
Y(z)(1-0.6z^{-1})=U(z)(2-z^{-1}).
$$

4. Divide:

$$
G(z)=\frac{Y(z)}{U(z)}=\frac{2-z^{-1}}{1-0.6z^{-1}}.
$$

5. Multiply numerator and denominator by $z$:

$$
G(z)=\frac{2z-1}{z-0.6}.
$$

Checked answer: $G(z)=(2z-1)/(z-0.6)$ with a stable pole at $z=0.6$.

## Code

```python
import numpy as np
from scipy import signal

T = 0.1
s_poles = np.array([-2 + 3j, -2 - 3j])
z_poles = np.exp(s_poles * T)
print("mapped z poles:", z_poles)
print("magnitudes:", np.abs(z_poles))

# Discrete transfer function G(z) = (2z - 1)/(z - 0.6)
num = [2.0, -1.0]
den = [1.0, -0.6]
system = signal.dlti(num, den, dt=T)
t, y = signal.dstep(system, n=20)
print("first step samples:", np.squeeze(y)[:8])
```

## Common pitfalls

- Checking digital stability with left-half-plane rules instead of the unit circle.
- Forgetting that $s=0$ maps to $z=1$, not $z=0$.
- Ignoring computational delay. One sample of delay can meaningfully reduce phase margin.
- Choosing sampling period without reference to bandwidth and transient requirements.
- Confusing $z^{-1}$ notation with $z$ polynomial notation.
- Assuming a discrete simulation exactly represents intersample continuous behavior.

## Connections

- [Digital compensator implementation](/cs/control-engineering/z-plane-design-and-digital-compensators) continues into gain design and software realization.
- [Laplace transfer functions](/cs/control-engineering/laplace-transfer-functions-and-linearization) are the continuous-domain counterpart.
- [Frequency-response design](/cs/control-engineering/frequency-response-compensator-design) motivates sampling-rate and delay checks.
- [Embedded systems](/cs/embedded/) covers the hardware context for real digital controllers.
- [Signals and systems](/physics/signals-systems/) includes sampling and transform theory.
