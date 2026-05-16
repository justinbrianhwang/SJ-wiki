---
title: Modulation and Communication Systems
sidebar_position: 13
---

# Modulation and Communication Systems

Modulation moves signal content from one frequency range to another. In communication systems, a low-frequency message can be shifted to a high-frequency carrier so it can be transmitted efficiently, separated from other users, or matched to an antenna and channel. In signals and systems language, modulation is multiplication in time, which becomes convolution or shifting in frequency.

The simplest modulation models are built from sinusoids and Fourier transform properties. Amplitude modulation shifts spectra by multiplying a message by a carrier. Frequency modulation changes the instantaneous phase derivative. Sampling can also be viewed as modulation by an impulse train, which produces repeated spectral copies.

## Definitions

Let $m(t)$ be a message signal. Complex modulation by $e^{j\omega_c t}$ produces

$$
x(t)=m(t)e^{j\omega_c t}.
$$

By the CTFT frequency-shifting property,

$$
X(j\omega)=M(j(\omega-\omega_c)).
$$

Real sinusoidal modulation by a cosine is

$$
x(t)=m(t)\cos(\omega_c t).
$$

Using

$$
\cos(\omega_c t)=\frac{1}{2}\left(e^{j\omega_c t}+e^{-j\omega_c t}\right),
$$

the spectrum is

$$
X(j\omega)=\frac{1}{2}M(j(\omega-\omega_c))+\frac{1}{2}M(j(\omega+\omega_c)).
$$

Thus a real carrier creates upper and lower shifted copies of the message spectrum.

Conventional amplitude modulation with carrier is often written

$$
s(t)=A_c\left[1+k_a m(t)\right]\cos(\omega_c t),
$$

where $A_c$ is carrier amplitude and $k_a$ is amplitude sensitivity. The term $A_c\cos(\omega_c t)$ is the transmitted carrier, and $A_c k_a m(t)\cos(\omega_c t)$ contains the message sidebands.

Double-sideband suppressed-carrier modulation is

$$
s_{\text{DSB-SC}}(t)=m(t)\cos(\omega_c t).
$$

Synchronous demodulation multiplies the modulated signal by a locally generated carrier and then lowpass filters:

$$
2s_{\text{DSB-SC}}(t)\cos(\omega_c t)
=2m(t)\cos^2(\omega_c t)
=m(t)\left[1+\cos(2\omega_c t)\right].
$$

An ideal lowpass filter removes the $2\omega_c$ term and recovers $m(t)$, assuming carrier phase and frequency match.

Angle modulation represents a carrier as

$$
s(t)=A_c\cos(\theta_i(t)),
$$

where the instantaneous angular frequency is

$$
\omega_i(t)=\frac{d\theta_i(t)}{dt}.
$$

For frequency modulation,

$$
\omega_i(t)=\omega_c+k_f m(t),
$$

so

$$
\theta_i(t)=\omega_c t+k_f\int_{-\infty}^{t}m(\tau)\,d\tau.
$$

## Key results

Multiplication in time corresponds to frequency-domain convolution:

$$
x(t)c(t)\leftrightarrow \frac{1}{2\pi}X(j\omega)*C(j\omega).
$$

When $c(t)=\cos(\omega_c t)$, its transform is

$$
C(j\omega)=\pi\delta(\omega-\omega_c)+\pi\delta(\omega+\omega_c).
$$

Convolving $M(j\omega)$ with these impulses shifts the spectrum:

$$
m(t)\cos(\omega_c t)
\leftrightarrow
\frac{1}{2}M(j(\omega-\omega_c))+\frac{1}{2}M(j(\omega+\omega_c)).
$$

For distortion-free amplitude modulation with carrier, the envelope should not cross zero. A common sufficient condition is

$$
|k_a m(t)|<1
$$

for all $t$. If this is violated, envelope detection can fail because overmodulation folds the envelope.

Frequency-division multiplexing relies on nonoverlapping shifted spectra. If messages $m_1(t)$ and $m_2(t)$ are bandlimited to $B_1$ and $B_2$, carriers should be separated enough that their sidebands do not overlap:

$$
|\omega_{c1}-\omega_{c2}|>B_1+B_2
$$

in angular-frequency units, with guard bands in practical systems.

Sampling is a special modulation process:

$$
x_p(t)=x(t)\sum_{n=-\infty}^{\infty}\delta(t-nT).
$$

Multiplication by the impulse train creates periodic spectral replicas:

$$
X_p(j\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(j(\omega-k\omega_s)).
$$

This is the same equation used in the sampling theorem. In communication terms, the impulse train is a carrier with infinitely many spectral lines.

Carrier placement is a bandwidth allocation problem. For DSB-SC or conventional AM with a message bandwidth $B$, the transmitted positive-frequency band extends roughly from $\omega_c-B$ to $\omega_c+B$. If $\omega_c$ is too small, the lower sideband can overlap baseband or cross zero frequency. If multiple users share a channel, guard bands are inserted because practical filters do not have infinitely sharp edges.

Coherent demodulation assumes the receiver oscillator has the same frequency and phase as the transmitter carrier. A phase error changes the recovered amplitude and can mix message components into an unwanted quadrature channel. A frequency error creates a slowly rotating phase term that may sound like beating in audio or produce symbol rotation in digital communication. These effects are system issues, but they are predicted by the same multiplication and frequency-shift properties.

Angle modulation is different from ordinary multiplication. FM does not simply shift the message spectrum by a carrier. The instantaneous frequency varies with the message, and the resulting spectrum can contain many sidebands. Narrowband FM can be approximated with a small number of terms, but wideband FM requires bandwidth rules such as Carson's rule in communication courses.

In baseband-equivalent analysis, engineers often use complex envelopes to avoid carrying both positive and negative carrier bands explicitly. The real transmitted waveform is recovered by taking the real part after multiplication by $e^{j\omega_c t}$. This notation is compact, but the underlying frequency-shift rules are the same ones shown here.

## Visual

```mermaid
flowchart LR
  A[Message m(t)] --> B[Multiply by carrier]
  C[cos omega_c t] --> B
  B --> D[Shifted sidebands]
  D --> E[Channel]
  E --> F[Multiply by synchronized carrier]
  G[local oscillator] --> F
  F --> H[Lowpass filter]
  H --> I[Recovered message]
```

| Modulation type | Time-domain form | Spectrum effect | Typical recovery |
|---|---|---|---|
| Complex modulation | $m(t)e^{j\omega_c t}$ | one-sided shift by $\omega_c$ | multiply by $e^{-j\omega_c t}$ |
| DSB-SC AM | $m(t)\cos\omega_c t$ | upper and lower sidebands | synchronous demodulation |
| Conventional AM | $A_c[1+k_am(t)]\cos\omega_c t$ | carrier plus sidebands | envelope detector if not overmodulated |
| Sampling | $x(t)\sum_n\delta(t-nT)$ | repeated spectral copies | ideal lowpass if no aliasing |
| FM | $A_c\cos(\omega_ct+k_f\int m)$ | bandwidth depends on deviation | frequency discriminator or PLL |

## Worked example 1: spectrum of DSB-SC modulation

Problem: A message $m(t)$ has spectrum

$$
M(j\omega)=0 \quad \text{for } |\omega|>1000\pi.
$$

The transmitted signal is

$$
s(t)=m(t)\cos(10000\pi t).
$$

Find the occupied positive-frequency sideband intervals.

Method:

1. The message is bandlimited to

$$
\omega_M=1000\pi.
$$

2. The carrier angular frequency is

$$
\omega_c=10000\pi.
$$

3. Cosine modulation creates two shifted copies:

$$
S(j\omega)=\frac{1}{2}M(j(\omega-\omega_c))
+\frac{1}{2}M(j(\omega+\omega_c)).
$$

4. The positive-frequency copy centered at $+\omega_c$ occupies

$$
\omega_c-\omega_M\le \omega\le \omega_c+\omega_M.
$$

5. Substitute values:

$$
10000\pi-1000\pi\le \omega\le 10000\pi+1000\pi.
$$

Thus

$$
9000\pi\le \omega\le 11000\pi.
$$

6. In hertz, divide by $2\pi$:

$$
4500\le f\le 5500 \ \text{Hz}.
$$

Checked answer: The positive-frequency sideband occupies $4500$ Hz to $5500$ Hz. A symmetric negative-frequency copy occupies $-5500$ Hz to $-4500$ Hz.

## Worked example 2: synchronous demodulation scale

Problem: Let

$$
s(t)=m(t)\cos(\omega_c t).
$$

The receiver multiplies by $2\cos(\omega_c t)$ and then applies an ideal lowpass filter that passes the message band and rejects frequencies around $2\omega_c$. Show the recovered signal.

Method:

1. Multiply:

$$
v(t)=2s(t)\cos(\omega_c t)
=2m(t)\cos^2(\omega_c t).
$$

2. Use the identity

$$
\cos^2(\omega_c t)=\frac{1+\cos(2\omega_c t)}{2}.
$$

3. Substitute:

$$
v(t)=2m(t)\frac{1+\cos(2\omega_c t)}{2}.
$$

4. Simplify:

$$
v(t)=m(t)+m(t)\cos(2\omega_c t).
$$

5. The first term is the baseband message. The second term is a copy shifted around $\pm 2\omega_c$.

6. The ideal lowpass filter passes $m(t)$ and rejects $m(t)\cos(2\omega_c t)$, assuming the carrier is high enough that the shifted term does not overlap the message band.

Checked answer:

$$
y(t)=m(t).
$$

If the receiver had multiplied by only $\cos(\omega_c t)$ instead of $2\cos(\omega_c t)$, the recovered baseband would be $m(t)/2$.

## Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

fs = 20_000
t = np.arange(0, 0.05, 1 / fs)
message = np.cos(2 * np.pi * 200 * t) + 0.5 * np.cos(2 * np.pi * 500 * t)
fc = 3_000

s = message * np.cos(2 * np.pi * fc * t)
mixed = 2 * s * np.cos(2 * np.pi * fc * t)

b, a = butter(6, 800 / (fs / 2), btype="low")
recovered = filtfilt(b, a, mixed)

plt.figure(figsize=(9, 4))
plt.plot(t, message, label="message")
plt.plot(t, recovered, "--", label="recovered")
plt.xlim(0, 0.02)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```

## Common pitfalls

- Forgetting the factor $1/2$ introduced by cosine modulation.
- Expecting envelope detection to work for DSB-SC. A suppressed-carrier signal needs coherent recovery or another carrier-recovery method.
- Letting sidebands overlap when choosing carrier frequencies for multiplexing.
- Treating FM bandwidth as just the message bandwidth. Frequency deviation also matters.
- Missing the connection between sampling and modulation by an impulse train.

## Connections

- [Continuous-Time Fourier Transform](/physics/signals-systems/continuous-time-fourier-transform)
- [Sampling, Aliasing, and Reconstruction](/physics/signals-systems/sampling-aliasing-reconstruction)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
- [Fourier Series for Periodic Signals](/physics/signals-systems/fourier-series-periodic-signals)
