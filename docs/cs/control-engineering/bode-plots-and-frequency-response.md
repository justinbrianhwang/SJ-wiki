---
title: Bode Plots and Frequency Response
sidebar_position: 13
---

# Bode Plots and Frequency Response

Frequency response studies the steady-state output of a stable linear system driven by sinusoidal inputs. Nise introduces Bode plots as a practical way to approximate and interpret magnitude and phase over many decades of frequency. The same transfer function used for time response is evaluated on the imaginary axis, $s=j\omega$.

The value of frequency response is design visibility. Low-frequency gain relates to steady-state tracking. Crossover frequency relates to speed and bandwidth. Phase lag near crossover relates to overshoot and stability margin. Bode plots show these trade-offs in a form engineers can sketch, measure, and tune.

![An asymptotic Bode plot shows magnitude and phase changing across logarithmic frequency.](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Asymptotic_Bode_plot.svg/500px-Asymptotic_Bode_plot.svg.png)

*Figure: Asymptotic Bode plot for frequency-response analysis. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Asymptotic_Bode_plot.svg), Mintz l, public domain.*

## Definitions

For a transfer function $G(s)$, the frequency response is

$$
G(j\omega).
$$

The magnitude is often expressed in decibels:

$$
|G(j\omega)|_{\text{dB}}=20\log_{10}|G(j\omega)|.
$$

The phase is

$$
\angle G(j\omega)
$$

in degrees or radians.

A **Bode magnitude plot** graphs $20\log_{10}\vert G(j\omega)\vert $ versus $\log_{10}\omega$. A **Bode phase plot** graphs phase versus $\log_{10}\omega$.

The **break frequency** or corner frequency of a factor $(1+s/\omega_b)$ is $\omega_b$. First-order factors change magnitude slope by $20$ dB/decade and phase by up to $90^\circ$. A pole contributes negative slope and phase; a zero contributes positive slope and phase.

For a sinusoidal input

$$
r(t)=A\sin(\omega t),
$$

a stable LTI system produces steady-state output

$$
c_{ss}(t)=A|G(j\omega)|\sin(\omega t+\angle G(j\omega)).
$$

## Key results

Basic Bode factors:

| Factor | Magnitude asymptote | Phase trend |
|---|---|---|
| constant $K$ | $20\log_{10}\vert K\vert $ | $0^\circ$ if $K\gt 0$, $180^\circ$ if $K\lt 0$ |
| pole at origin $1/s$ | $-20$ dB/dec | $-90^\circ$ |
| zero at origin $s$ | $+20$ dB/dec | $+90^\circ$ |
| real pole $1/(1+s/\omega_p)$ | slope changes by $-20$ dB/dec | $0^\circ$ to $-90^\circ$ |
| real zero $(1+s/\omega_z)$ | slope changes by $+20$ dB/dec | $0^\circ$ to $+90^\circ$ |
| second-order poles | possible resonant peak | up to $-180^\circ$ |

For a product of transfer-function factors, magnitudes in dB add and phases add. This is why Bode plots are convenient:

$$
20\log_{10}|G_1G_2|=20\log_{10}|G_1|+20\log_{10}|G_2|.
$$

The low-frequency magnitude of the open-loop transfer function indicates static error constants. A Type 1 system has a $-20$ dB/dec low-frequency slope because of one pole at the origin; a Type 2 system has $-40$ dB/dec.

Bandwidth is loosely associated with how fast a closed-loop system responds. Higher crossover or bandwidth often means faster response, but high bandwidth also passes more noise and may reduce robustness if phase lag is large.

Bode plots are asymptotic design tools as well as exact computational plots. Hand sketching begins with low-frequency gain and slope, then changes slope at each break frequency. The exact curve is smooth: a first-order pole is already contributing phase a decade before its break frequency and continues a decade after. The magnitude is $3$ dB away from the asymptote at the break frequency. Knowing the asymptotes helps the designer understand the exact plot rather than merely display it.

Minimum-phase systems have a close relationship between magnitude slope and phase. A downward magnitude slope near crossover usually corresponds to phase lag. Nonminimum-phase zeros and time delays break the most comforting versions of this intuition: a right-half-plane zero may increase magnitude like a left-half-plane zero but contributes negative phase, and a pure delay contributes phase lag without magnitude change. These effects limit achievable bandwidth.

Frequency response can be measured directly. Apply sinusoids at different frequencies, wait for transients to decay, then record output amplitude ratio and phase shift. This experimental method is valuable when physical parameters are uncertain. The resulting Bode plot may be used for design even if no exact differential-equation model is available, though noise, nonlinearities, and actuator limits must be managed during testing.

Open-loop and closed-loop frequency responses answer different questions. Open-loop loop transfer $L(j\omega)$ is used for gain crossover, phase margin, Nyquist plots, and loop shaping. Closed-loop transfer $T(j\omega)$ shows how commands pass to outputs. Sensitivity $S(j\omega)=1/(1+L(j\omega))$ shows disturbance rejection and robustness. Complementary sensitivity $T(j\omega)=L(j\omega)/(1+L(j\omega))$ shows command following and noise transmission for unity feedback.

A good loop shape is usually high at low frequency, crosses over with adequate phase margin, and rolls off at high frequency. High low-frequency gain reduces tracking error and load disturbances. Moderate crossover gives speed. High-frequency rolloff avoids amplifying sensor noise and unmodeled plant dynamics. Most frequency-response design is a disciplined negotiation among those three regions.

Second-order factors add another layer of interpretation. A lightly damped pair of poles can create a resonant peak in the magnitude plot and a rapid phase transition. The peak corresponds to the same low damping that creates overshoot in step response. Increasing damping flattens the resonance and spreads the phase change over a broader frequency range. This is one reason frequency response and time response are not separate subjects; they are two views of the same poles.

The decibel scale is useful because it turns multiplication into addition, but it can hide ordinary ratios. A $20$ dB gain is a factor of $10$ in amplitude; a $40$ dB gain is a factor of $100$; a $-20$ dB attenuation is a factor of $0.1$. When checking actuator effort or sensor noise, convert back to ordinary magnitude so the physical size of signals remains clear.

For design documentation, a Bode plot should be accompanied by the transfer function, units, operating point, and whether the plotted system is open loop, closed loop, sensitivity, or complementary sensitivity. Many wrong conclusions come from looking at the correct curve for the wrong transfer function.

Phase should be unwrapped or interpreted consistently. A plot that jumps from $-179^\circ$ to $+179^\circ$ may represent a smooth continuation, not a sudden physical phase lead. Margin calculations depend on the continuous phase trend near crossover, so plotting conventions must be checked.

Always label wrapped phase plots clearly.

Units matter.

## Visual

```text
Magnitude asymptote for 10/(1+s/5)

dB
20 |---------
   |         \
   |          \
 0 |           \  slope -20 dB/dec
   +----+-------+--------> log omega
        5
```

| Quantity | How read from Bode plot | Design meaning |
|---|---|---|
| dc gain | low-frequency magnitude | step tracking and disturbance rejection |
| crossover frequency | where magnitude crosses 0 dB | approximate speed and margin location |
| phase at crossover | phase plot at gain crossover | phase margin |
| high-frequency rolloff | final magnitude slope | noise attenuation and unmodeled dynamics |
| resonant peak | magnitude bump | low damping and overshoot tendency |

## Worked example 1: magnitude and phase at one frequency

Problem: For

$$
G(s)=\frac{10}{s+2},
$$

find magnitude in dB and phase at $\omega=2$ rad/s.

Method:

1. Substitute $s=j\omega=j2$:

$$
G(j2)=\frac{10}{2+j2}.
$$

2. Denominator magnitude:

$$
|2+j2|=\sqrt{2^2+2^2}=\sqrt8=2.828.
$$

3. Magnitude:

$$
|G(j2)|=\frac{10}{2.828}=3.536.
$$

4. Convert to dB:

$$
20\log_{10}(3.536)=10.97\ \text{dB}.
$$

5. Denominator angle:

$$
\angle(2+j2)=\tan^{-1}(2/2)=45^\circ.
$$

6. Numerator is positive real, so phase is

$$
\angle G(j2)=0^\circ-45^\circ=-45^\circ.
$$

Checked answer: magnitude is about $11.0$ dB and phase is $-45^\circ$.

## Worked example 2: asymptotic Bode sketch

Problem: Sketch the asymptotic magnitude slopes for

$$
G(s)=\frac{100(s+1)}{s(s+10)}.
$$

Method:

1. Put factors in Bode form:

$$
s+1=1(1+s/1),
$$

$$
s+10=10(1+s/10).
$$

Thus

$$
G(s)=\frac{100(1+s)}{s\cdot10(1+s/10)}
=\frac{10(1+s/1)}{s(1+s/10)}.
$$

2. Constant magnitude contribution:

$$
20\log_{10}(10)=20\ \text{dB}.
$$

3. Pole at origin contributes slope $-20$ dB/dec from the start.

4. Zero at $\omega=1$ contributes $+20$ dB/dec after $\omega=1$, changing slope from $-20$ to $0$ dB/dec.

5. Pole at $\omega=10$ contributes $-20$ dB/dec after $\omega=10$, changing slope from $0$ to $-20$ dB/dec.

6. Magnitude at $\omega=1$ from the initial asymptote:

Since $20$ dB at $\omega=1$ after the origin pole expression $20-20\log_{10}\omega$, at $\omega=1$ it is $20$ dB.

7. From $\omega=1$ to $10$, slope is $0$, so magnitude remains $20$ dB. After $10$, it falls at $-20$ dB/dec.

Checked answer: slopes are $-20$ dB/dec for $\omega\lt 1$, $0$ dB/dec for $1\lt \omega\lt 10$, and $-20$ dB/dec for $\omega\gt 10$.

## Code

```python
import numpy as np
from scipy import signal

num = [100, 100]      # 100(s + 1)
den = [1, 10, 0]      # s(s + 10)
sys = signal.TransferFunction(num, den)

w = np.logspace(-2, 3, 500)
w, mag, phase = signal.bode(sys, w=w)

idx = np.argmin(np.abs(w - 2.0))
print("magnitude at 2 rad/s:", mag[idx], "dB")
print("phase at 2 rad/s:", phase[idx], "deg")
print("approx gain crossover rad/s:", w[np.argmin(np.abs(mag))])
```

## Common pitfalls

- Using $10\log_{10}$ for voltage-like transfer-function magnitude instead of $20\log_{10}$.
- Forgetting that phases add algebraically, with poles contributing negative phase and zeros positive phase.
- Treating asymptotes as exact near break frequencies. First-order factors differ by about $3$ dB at the corner.
- Evaluating frequency response at $s=\omega$ instead of $s=j\omega$.
- Ignoring units of $\omega$. Bode formulas use rad/s unless explicitly converted.
- Assuming higher bandwidth is always better. Noise, actuator limits, and unmodeled dynamics constrain useful bandwidth.

## Connections

- [Nyquist and margins](/cs/control-engineering/nyquist-and-frequency-stability-margins) uses the same open-loop frequency response for stability.
- [Frequency-response design](/cs/control-engineering/frequency-response-compensator-design) shapes Bode plots with lag, lead, and lag-lead compensation.
- [Steady-state errors](/cs/control-engineering/steady-state-errors-and-sensitivity) connect low-frequency gain to tracking error.
- [Time response](/cs/control-engineering/time-response-first-and-second-order) relates bandwidth and damping to transient behavior.
- [Signals and systems](/physics/signals-systems/) studies sinusoidal steady state in a broader setting.
