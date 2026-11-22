---
title: Time Response of First- and Second-Order Systems
sidebar_position: 6
---

# Time Response of First- and Second-Order Systems

Time response connects the algebraic model to what an engineer sees on an oscilloscope, plot, or test rig. Nise's Chapter 4 studies how poles and zeros produce first-order and second-order responses, then defines transient specifications such as time constant, peak time, percent overshoot, rise time, and settling time.

The most important habit is to read the response from pole locations. A real pole gives exponential decay. A complex conjugate pair gives oscillation under an exponential envelope. Poles near the imaginary axis decay slowly; poles far to the left decay quickly. Zeros do not determine stability by themselves, but they can strongly change shape, overshoot, and apparent speed.

## Definitions

A first-order transfer function in standard form is

$$
G(s)=\frac{K}{\tau s+1}.
$$

For a unit-step input, the response is

$$
c(t)=K\left(1-e^{-t/\tau}\right)u(t).
$$

The **time constant** $\tau$ is the time at which the response has reached about $63.2\%$ of its final value. The pole is at $s=-1/\tau$.

The standard second-order transfer function is

$$
G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2},
$$

where $\omega_n$ is the natural frequency and $\zeta$ is the damping ratio. The pole locations are

$$
s=-\zeta\omega_n\pm \omega_n\sqrt{\zeta^2-1}.
$$

For $0\lt \zeta\lt 1$, the poles are complex:

$$
s=-\zeta\omega_n\pm j\omega_d,
\qquad
\omega_d=\omega_n\sqrt{1-\zeta^2}.
$$

The underdamped unit-step specifications commonly used in Nise are

$$
T_p=\frac{\pi}{\omega_d},
\qquad
\%OS=100e^{-\zeta\pi/\sqrt{1-\zeta^2}},
$$

and the approximate $2\%$ settling time

$$
T_s\approx \frac{4}{\zeta\omega_n}.
$$

## Key results

The output response of a linear system can be decomposed into forced and natural components. In transfer-function analysis, input poles generate the forced response and system poles generate the natural response. For a stable system, the natural response decays and the forced response remains.

Pole categories for second-order systems are:

| Damping ratio | Pole type | Response character |
|---:|---|---|
| $\zeta=0$ | purely imaginary | undamped sinusoid |
| $0\lt \zeta\lt 1$ | complex conjugate LHP | underdamped oscillatory decay |
| $\zeta=1$ | repeated real pole | critically damped fastest nonoscillatory case |
| $\zeta\gt 1$ | distinct real poles | overdamped nonoscillatory case |

The $s$-plane gives geometric interpretations. For underdamped poles, the radial distance from the origin is $\omega_n$, the magnitude of the real part is $\zeta\omega_n$, and the imaginary part is $\omega_d$. Lines of constant damping ratio are rays from the origin. Vertical lines correspond to constant settling-time approximation because $T_s\approx 4/\vert \sigma\vert $ when poles are at $s=-\sigma\pm j\omega_d$.

Additional poles and zeros complicate the second-order formulas. If a higher-order system has two dominant poles much closer to the imaginary axis than the others, a second-order approximation may be reasonable. If a zero is near the dominant poles or the third pole is not far away, the approximation can be poor.

Dominance is a quantitative claim, not a drawing preference. A common rule of thumb is that nondominant poles should be at least five times farther left than the dominant real part before their transients can be ignored for rough design. Even then, residues matter. A far-left pole with a large residue can still affect the early response, while a closer pole with a tiny residue may be barely visible. The transfer function's numerator and partial-fraction coefficients decide how strongly each mode appears.

Zeros shape the step response by changing the weighted sum of modal terms. A left-half-plane zero can increase overshoot by emphasizing fast components. A right-half-plane zero creates nonminimum-phase behavior: the response may initially move in the wrong direction before eventually tracking the command. This inverse response is not captured by pole locations alone and usually limits achievable speed because forcing a nonminimum-phase plant faster demands large internal motion.

The final value should be checked separately from transient shape. A standard second-order form with numerator $\omega_n^2$ has dc gain one, so a unit step settles to one. If the numerator is different, or if extra zeros and poles change dc gain, the same pole locations can settle to a different value. Time-response specifications such as percent overshoot are normally measured relative to the final value, so computing the final value first prevents misleading percentages.

Initial conditions provide another distinction. A system can have no external input and still respond because energy is stored in masses, springs, capacitors, or inductors. The natural response seen from nonzero initial conditions uses the same poles as the transfer-function denominator. In a laboratory, tapping a structure or releasing a displaced mass is often a way to observe natural frequencies and damping without commanding a complicated input.

Nise's response formulas are design approximations, not replacements for simulation and exact inverse transforms. They are extremely useful because they connect pole geometry to performance targets. Once a controller is selected, however, the complete transfer function should be simulated, especially if the system has additional poles, zeros, actuator limits, sensor filters, or digital sampling. The dominant-pole assumption earns trust only after the complete response agrees with the approximation.

Rise time is less universal than peak time or settling time because textbooks and industries define it differently. Some use the time from $10\%$ to $90\%$ of final value; others use $0\%$ to $100\%$ for underdamped second-order systems. When comparing specifications, state the definition. Otherwise two engineers can compute different rise times from the same response and both be following a legitimate convention.

The time constant idea extends beyond first-order systems as an envelope approximation. For a complex pole pair $-\sigma\pm j\omega_d$, the oscillation amplitude decays like $e^{-\sigma t}$. The envelope time constant is $1/\sigma$. This is why vertical movement of poles in the $s$-plane changes oscillation frequency while horizontal movement changes decay rate.

Transient specifications should be tied to the actual output variable. A motor position response, current response, and control effort response may have different peaks and settling behavior. A design that gives acceptable output overshoot may still require an unacceptable actuator pulse. Complete time-response analysis often checks several signals, not only $c(t)$.

Always state whether settling time uses a $2\%$ or $5\%$ band.

The numeric difference can change design acceptance.

## Visual

```text
Imaginary axis
      ^
      |        x  pole: -zeta*wn + j*wd
      |       /|
      |      / | wd
      |     /  |
      |    /theta
------+---x------------------> Real axis
      |  -zeta*wn
      |
```

| Specification | Formula for $0\lt \zeta\lt 1$ | Mainly controlled by |
|---|---|---|
| Damped frequency | $\omega_d=\omega_n\sqrt{1-\zeta^2}$ | imaginary part |
| Peak time | $T_p=\pi/\omega_d$ | imaginary part |
| Percent overshoot | $100e^{-\zeta\pi/\sqrt{1-\zeta^2}}$ | damping ratio |
| Settling time | $T_s\approx 4/(\zeta\omega_n)$ | real part |
| Time constant envelope | $1/(\zeta\omega_n)$ | real part |

## Worked example 1: first-order step response

Problem: A system has

$$
G(s)=\frac{5}{2s+1}.
$$

Find the time constant, pole, final value for a unit-step input, and output at $t=4$ s.

Method:

1. Match to $K/(\tau s+1)$:

$$
K=5,\qquad \tau=2.
$$

2. The pole is

$$
s=-\frac{1}{\tau}=-0.5.
$$

3. For a unit step,

$$
c(t)=5(1-e^{-t/2}).
$$

4. The final value is

$$
c(\infty)=5.
$$

5. Evaluate at $t=4$:

$$
c(4)=5(1-e^{-2}).
$$

Since $e^{-2}\approx 0.1353$,

$$
c(4)=5(0.8647)=4.3235.
$$

Checked answer: $\tau=2$ s, pole $-0.5$, final value $5$, and $c(4)\approx 4.32$.

## Worked example 2: second-order transient specifications

Problem: A closed-loop system has dominant poles at

$$
s=-3\pm j4.
$$

Find $\omega_n$, $\zeta$, $\omega_d$, $T_p$, $\%OS$, and the approximate $2\%$ settling time.

Method:

1. The real part gives

$$
\zeta\omega_n=3.
$$

2. The imaginary part is the damped frequency:

$$
\omega_d=4.
$$

3. Natural frequency is radial distance:

$$
\omega_n=\sqrt{3^2+4^2}=5\ \text{rad/s}.
$$

4. Damping ratio:

$$
\zeta=\frac{3}{5}=0.6.
$$

5. Peak time:

$$
T_p=\frac{\pi}{\omega_d}=\frac{\pi}{4}=0.785\ \text{s}.
$$

6. Percent overshoot:

$$
\%OS=100e^{-\zeta\pi/\sqrt{1-\zeta^2}}
=100e^{-0.6\pi/\sqrt{1-0.36}}.
$$

Since $\sqrt{0.64}=0.8$,

$$
\%OS=100e^{-0.75\pi}\approx 9.48\%.
$$

7. Settling time:

$$
T_s\approx \frac{4}{\zeta\omega_n}=\frac{4}{3}=1.33\ \text{s}.
$$

Checked answer: $\omega_n=5$, $\zeta=0.6$, $\omega_d=4$, $T_p=0.785$ s, $\%OS\approx9.5\%$, $T_s\approx1.33$ s.

## Code

```python
import numpy as np
from scipy import signal

zeta = 0.6
wn = 5.0
num = [wn**2]
den = [1.0, 2*zeta*wn, wn**2]
sys = signal.TransferFunction(num, den)

t = np.linspace(0, 5, 1000)
t, y = signal.step(sys, T=t)
final = y[-1]
peak = np.max(y)
tp = t[np.argmax(y)]
overshoot = (peak - final) / final * 100

print("poles:", np.roots(den))
print(f"peak time approx: {tp:.3f} s")
print(f"overshoot approx: {overshoot:.2f}%")
print(f"settling estimate: {4/(zeta*wn):.3f} s")
```

## Common pitfalls

- Applying underdamped formulas when $\zeta\ge 1$. Peak time and overshoot formulas assume complex poles.
- Using $\omega_n$ where $\omega_d$ is required. The sinusoidal oscillation frequency is $\omega_d$, not $\omega_n$, for damped systems.
- Assuming zeros do not matter. A zero can add overshoot or undershoot even with stable poles.
- Trusting a second-order approximation without checking nondominant poles and nearby zeros.
- Confusing $T_s\approx4/(\zeta\omega_n)$ with an exact theorem. It is a common $2\%$ rule of thumb.
- Reading final value from numerator gain alone without applying the final value theorem or evaluating dc gain.

## Connections

- [Physical system modeling](/cs/control-engineering/physical-system-modeling-frequency-domain) produces the poles analyzed here.
- [Root locus](/cs/control-engineering/root-locus-sketching-and-analysis) moves closed-loop poles to meet these specifications.
- [Frequency response](/cs/control-engineering/bode-plots-and-frequency-response) links bandwidth and resonant peak to time response.
- [Steady-state error](/cs/control-engineering/steady-state-errors-and-sensitivity) covers the final-value accuracy side of performance.
- [Signals and systems](/physics/signals-systems/) gives broader response decomposition tools.
