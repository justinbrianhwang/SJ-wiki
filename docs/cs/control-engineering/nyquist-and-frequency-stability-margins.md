---
title: Nyquist and Frequency Stability Margins
sidebar_position: 14
---

# Nyquist and Frequency Stability Margins

Nyquist analysis is the frequency-domain stability test that complements Routh-Hurwitz and root locus. Instead of forming a Routh table or drawing pole paths, it studies how the open-loop transfer function maps a contour around the right half-plane. Nise uses Nyquist to connect encirclements of the critical point $-1+j0$ with closed-loop stability, then defines gain and phase margins as practical robustness measures.

The power of Nyquist is that it reasons from open-loop frequency response while accounting for open-loop unstable poles. Bode plots are easier to read for routine design, but Nyquist gives the underlying stability logic and handles cases where open-loop right-half-plane poles matter.

## Definitions

For a negative-feedback system with loop transfer function

$$
L(s)=G(s)H(s),
$$

the closed-loop characteristic equation is

$$
1+L(s)=0.
$$

The critical point is therefore

$$
-1+j0.
$$

The **Nyquist plot** is the image of a specified contour in the $s$-plane under $L(s)$. In many practical stable open-loop examples, engineers sketch $L(j\omega)$ for $\omega$ from $0$ to $\infty$ and reflect it for negative frequencies.

The Nyquist criterion relates:

$$
Z=N+P,
$$

using one common sign convention, where $Z$ is the number of right-half-plane zeros of $1+L(s)$, $P$ is the number of right-half-plane poles of $L(s)$, and $N$ is the net number of clockwise encirclements of $-1+j0$. Closed-loop stability requires $Z=0$.

The **gain margin** is the factor by which loop gain can be multiplied before the Nyquist plot passes through $-1$. On a Bode plot, it is measured at the phase crossover frequency where phase is $-180^\circ$:

$$
GM=\frac{1}{|L(j\omega_{pc})|}.
$$

In decibels,

$$
GM_{\text{dB}}=-20\log_{10}|L(j\omega_{pc})|.
$$

The **phase margin** is the additional phase lag required to reach $-180^\circ$ at the gain crossover frequency where $\vert L(j\omega_{gc})\vert =1$:

$$
PM=180^\circ+\angle L(j\omega_{gc}).
$$

## Key results

For open-loop stable systems, the Nyquist stability condition often reduces to a simple rule: the Nyquist plot should not encircle $-1+j0$. If it passes close to $-1$, the closed-loop system may be stable but fragile. Margins quantify that fragility.

Margins are not merely numerical rituals:

| Margin | Read at | Meaning |
|---|---|---|
| gain margin | phase $=-180^\circ$ | allowable loop gain increase before instability |
| phase margin | magnitude $=1$ | allowable extra lag before instability |
| crossover frequency | magnitude $=1$ | approximate closed-loop speed location |
| distance to $-1$ | Nyquist plot | combined gain-phase robustness |

Closed-loop transient behavior is related but not identical to margins. A low phase margin often corresponds to high overshoot and oscillation. A larger phase margin often gives more damping. However, exact time-domain predictions require more than margin alone, especially for high-order systems or nonminimum-phase plants.

Time delay is especially important in frequency response. A pure delay $e^{-sT}$ has magnitude $1$ but phase

$$
\angle e^{-j\omega T}=-\omega T
$$

in radians. It can destroy phase margin without changing the magnitude plot.

Nyquist plots also make clear why the point $-1+j0$ is special. The closed-loop denominator is $1+L(s)$. If the open-loop frequency response reaches $L(j\omega)=-1$, then $1+L(j\omega)=0$ and the closed-loop system has a pole on the imaginary axis. Passing near that point means the closed-loop denominator becomes small at some frequency, which usually appears as resonant amplification, oscillation, or poor damping.

For open-loop unstable plants, gain and phase margins require more care. A plant with a right-half-plane pole may need a specific encirclement of $-1$ to produce a stable closed loop. Simply asking for "no encirclements" is valid only for open-loop stable cases under the usual convention. This is where Nyquist is stronger than a casual Bode-margin reading: it keeps track of the unstable open-loop poles through $P$.

The direction of encirclement is a convention-sensitive detail, but consistency is not optional. Some texts write $N=Z-P$ with counterclockwise encirclements positive; others write $Z=N+P$ with clockwise encirclements positive. The physical conclusion is the same when the convention is used consistently. When solving problems, state the convention and define $N$, $P$, and $Z$ before counting.

Margins are local robustness summaries. A gain margin of $6$ dB says the loop gain can be doubled before reaching the marginal point, assuming phase shape and model structure remain the same. A phase margin of $45^\circ$ says an additional $45^\circ$ of phase lag at crossover would bring the loop to the stability boundary. Real uncertainty may change gain and phase across frequency simultaneously, so margins are useful but incomplete robustness measures.

Nyquist thinking is also useful for experimental data. If frequency-response data are measured point by point, the plotted curve can reveal whether the loop is close to the critical point even when a clean transfer-function model is unavailable. This is common in hardware commissioning: the engineer measures loop response at safe amplitudes, estimates margins, then decides whether the controller can be made faster or must be backed off for robustness.

The Nyquist contour includes more than the visible positive-frequency curve. For real-coefficient systems, the negative-frequency portion is the mirror image of the positive-frequency portion. If there are poles on the imaginary axis, the contour must indent around them. These details are often suppressed in introductory sketches, but they explain why integrators and marginal open-loop poles require careful handling in formal Nyquist tests.

Gain and phase margins should be reported with the crossover frequencies at which they occur. A phase margin at a very high crossover may be irrelevant if unmodeled dynamics begin earlier. A gain margin at a frequency far beyond actuator bandwidth may not represent the practical robustness bottleneck. The frequency location tells the engineer what physical effects might threaten the margin.

In design reviews, a Nyquist or margin calculation should identify the loop broken for analysis. Multiloop systems can have inner current loops, velocity loops, and outer position loops. Each loop has its own loop transfer and margins when opened at a specific point. Ambiguous loop-breaking leads to ambiguous stability claims.

Nyquist plots should be drawn with enough frequency labels to show direction. Encirclement count depends on how the curve is traversed as frequency increases. Without arrows or frequency markers, a plot may show shape but not the information needed for the criterion.

## Visual

```text
Nyquist idea near the critical point

Im
 ^
 |        curve L(jw)
 |       /
 |      /
 |  x  /        x = -1 + j0
 |----x----------------------> Re
 |
 |
```

| Situation | Nyquist interpretation | Closed-loop implication |
|---|---|---|
| no open-loop RHP poles and no encirclement | $P=0$, $N=0$ | stable |
| no open-loop RHP poles and one clockwise encirclement | $P=0$, $N=1$ | unstable |
| one open-loop RHP pole and one counterclockwise encirclement | sign convention cancels $P$ | can be stable |
| plot crosses $-1$ | characteristic root on $j\omega$ axis | marginal boundary |

## Worked example 1: gain and phase margins

Problem: For

$$
L(s)=\frac{10}{s(s+2)},
$$

find the gain crossover frequency and phase margin.

Method:

1. Magnitude:

$$
|L(j\omega)|=\frac{10}{|j\omega||j\omega+2|}
=\frac{10}{\omega\sqrt{\omega^2+4}}.
$$

2. Gain crossover occurs when magnitude is $1$:

$$
\frac{10}{\omega\sqrt{\omega^2+4}}=1.
$$

3. Rearrange:

$$
\omega^2(\omega^2+4)=100.
$$

Let $x=\omega^2$:

$$
x^2+4x-100=0.
$$

4. Solve:

$$
x=\frac{-4+\sqrt{16+400}}{2}
=\frac{-4+\sqrt{416}}{2}.
$$

Since $\sqrt{416}=20.396$,

$$
x=8.198,\qquad \omega_{gc}=\sqrt{8.198}=2.863\ \text{rad/s}.
$$

5. Phase:

$$
\angle L(j\omega)=-90^\circ-\tan^{-1}(\omega/2).
$$

At $\omega=2.863$,

$$
\tan^{-1}(2.863/2)=\tan^{-1}(1.4315)=55.1^\circ.
$$

Thus

$$
\angle L(j\omega_{gc})=-145.1^\circ.
$$

6. Phase margin:

$$
PM=180^\circ-145.1^\circ=34.9^\circ.
$$

Checked answer: $\omega_{gc}\approx2.86$ rad/s and $PM\approx35^\circ$.

## Worked example 2: time-delay phase loss

Problem: A loop has phase margin $50^\circ$ at crossover frequency $\omega_{gc}=4$ rad/s. A pure delay $T$ is added. What delay reduces the phase margin to $30^\circ$?

Method:

1. The allowable phase loss is

$$
50^\circ-30^\circ=20^\circ.
$$

2. Convert to radians:

$$
20^\circ=\frac{20\pi}{180}=\frac{\pi}{9}=0.3491\ \text{rad}.
$$

3. Delay phase at crossover is

$$
\omega_{gc}T.
$$

4. Set phase loss:

$$
4T=0.3491.
$$

5. Solve:

$$
T=0.0873\ \text{s}.
$$

Checked answer: a delay of about $87$ ms reduces phase margin from $50^\circ$ to $30^\circ$ at $4$ rad/s.

## Code

```python
import numpy as np
from scipy import signal

num = [10.0]
den = [1.0, 2.0, 0.0]
sys = signal.TransferFunction(num, den)

w = np.logspace(-2, 3, 5000)
w, mag_db, phase_deg = signal.bode(sys, w=w)

gc_index = np.argmin(np.abs(mag_db))
w_gc = w[gc_index]
pm = 180 + phase_deg[gc_index]
print("gain crossover:", w_gc)
print("phase margin approx:", pm)

delay = np.deg2rad(20) / 4
print("delay for 20 deg phase loss at 4 rad/s:", delay)
```

## Common pitfalls

- Using closed-loop transfer function for Nyquist margins instead of open-loop loop transfer $L(s)$.
- Forgetting open-loop right-half-plane poles in the Nyquist encirclement count.
- Mixing clockwise and counterclockwise sign conventions without consistency.
- Treating gain margin and phase margin as independent guarantees. Simultaneous gain and phase changes can be worse than either alone.
- Ignoring time delay because it has unity magnitude. Delay can remove phase margin rapidly.
- Assuming a comfortable margin fixes actuator saturation or nonlinear behavior.

## Connections

- [Bode plots](/cs/control-engineering/bode-plots-and-frequency-response) provide the magnitude and phase data used to read margins.
- [Frequency-response design](/cs/control-engineering/frequency-response-compensator-design) shapes margins with lead and lag networks.
- [Routh-Hurwitz stability](/cs/control-engineering/routh-hurwitz-stability) is the polynomial-domain stability counterpart.
- [Complex functions](/math/engineering-math/complex-functions-and-analyticity) underlies contour mapping arguments.
- [Digital control](/cs/control-engineering/digital-control-sampling-and-z-transform) maps stability from the $s$-plane to the $z$-plane.
