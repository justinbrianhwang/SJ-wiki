---
title: Sampling, Aliasing, and Reconstruction
sidebar_position: 9
---

# Sampling, Aliasing, and Reconstruction

Sampling connects continuous-time signals to discrete-time sequences. A sampler records values $x(nT)$ at equally spaced times, where $T$ is the sampling period and $\omega_s=2\pi/T$ is the sampling angular frequency. The central question is whether those samples contain enough information to recover the original continuous-time signal.

The sampling theorem says exact reconstruction is possible for bandlimited signals when the sampling rate is high enough. If the sampling rate is too low, shifted copies of the spectrum overlap. That overlap is aliasing, and it is not merely a plotting artifact: different continuous-time frequencies produce the same discrete-time samples.

![Two sine waves pass through the same sampled points, illustrating aliasing.](https://commons.wikimedia.org/wiki/Special:FilePath/AliasingSines.svg)

*Figure: Aliasing shows why sampling rate is a physical constraint, not just a numerical detail. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:AliasingSines.svg), Moxfyre, CC BY-SA 3.0/GFDL.*

## Definitions

Uniform sampling of a continuous-time signal $x_c(t)$ with sampling period $T$ produces the sequence

$$
x[n]=x_c(nT).
$$

The sampling frequency in cycles per second is

$$
f_s=\frac{1}{T},
$$

and the sampling angular frequency is

$$
\omega_s=\frac{2\pi}{T}.
$$

A continuous-time signal is bandlimited to $\omega_M$ if

$$
X_c(j\omega)=0 \quad \text{for } |\omega|>\omega_M.
$$

Impulse-train sampling models the sampled continuous-time signal as

$$
x_p(t)=x_c(t)\sum_{n=-\infty}^{\infty}\delta(t-nT).
$$

Using the sifting property,

$$
x_p(t)=\sum_{n=-\infty}^{\infty}x_c(nT)\delta(t-nT).
$$

The Fourier transform of the impulse train is another impulse train:

$$
\sum_{n=-\infty}^{\infty}\delta(t-nT)
\leftrightarrow
\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_s).
$$

Therefore multiplication in time produces convolution in frequency, and the sampled spectrum is

$$
X_p(j\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X_c(j(\omega-k\omega_s)).
$$

The discrete-time frequency $\Omega$ corresponding to continuous-time frequency $\omega$ under sampling is

$$
\Omega=\omega T.
$$

Because DT frequency is periodic with period $2\pi$, continuous-time frequencies separated by integer multiples of $\omega_s$ map to the same discrete-time frequency.

## Key results

The Nyquist sampling condition for a bandlimited signal is

$$
\omega_s>2\omega_M.
$$

Equivalently,

$$
f_s>2f_M.
$$

The number $2f_M$ is the Nyquist rate. The frequency $f_s/2$ is often called the Nyquist frequency. The distinction matters: one is a minimum sampling rate, the other is the highest frequency representable without aliasing at a given sampling rate.

If $\omega_s\gt 2\omega_M$, the shifted copies of $X_c(j\omega)$ in $X_p(j\omega)$ do not overlap. An ideal lowpass reconstruction filter can isolate the central copy and undo the scale factor $1/T$. One ideal reconstruction response is

$$
H_r(j\omega)=
\begin{cases}
T, & |\omega|\le \omega_M,\\
0, & |\omega|>\omega_M,
\end{cases}
$$

with transition band allowed if $\omega_M\lt \vert \omega\vert \lt \omega_s-\omega_M$.

The time-domain interpolation formula for ideal reconstruction is

$$
x_c(t)=\sum_{n=-\infty}^{\infty}x_c(nT)\operatorname{sinc}\left(\frac{t-nT}{T}\right),
$$

where the normalized sinc is

$$
\operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
$$

Aliasing occurs when the spectral copies overlap:

$$
\omega_s\le 2\omega_M.
$$

A continuous-time sinusoid

$$
x_c(t)=\cos(\omega_0 t)
$$

sampled at period $T$ gives

$$
x[n]=\cos(\omega_0 nT).
$$

The sampled sequence cannot distinguish $\omega_0$ from

$$
\omega_0+k\omega_s
$$

or from sign-reflected equivalents created by cosine symmetry. That is why antialiasing filters are placed before analog-to-digital conversion: information lost to aliasing cannot be recovered by later digital processing.

The practical sampling workflow has three stages. First, limit the analog input bandwidth with an antialiasing filter. Second, sample at a rate high enough that the remaining spectral copies do not overlap. Third, if a continuous-time output is needed, use a reconstruction filter to isolate the baseband copy. Each stage has a different job. The sampler creates copies; it does not decide which copy is the original. The reconstruction filter can select a copy only if the copies are separated.

The strict inequality $\omega_s\gt 2\omega_M$ is the clean textbook condition. At exactly $\omega_s=2\omega_M$, edge cases depend on whether the spectrum is zero at the band edge and on the realizability of the reconstruction filter. In engineering practice, sampling rates are chosen with guard bands because real filters have transition regions and cannot switch from passband to stopband instantly.

Downsampling and upsampling in discrete time mirror the same ideas. Downsampling by an integer factor compresses the effective frequency axis and can create aliasing unless a digital lowpass filter removes high-frequency content first. Upsampling by inserting zeros creates spectral images that must be removed by an interpolation filter. These operations are discrete-time versions of the same spectral-copy logic.

Aliasing can sometimes be used intentionally, as in bandpass sampling, but only when the spectral bands and sampling rate are chosen so that shifted copies land without overlap. Accidental aliasing is destructive; intentional aliasing is controlled frequency translation.

A final check in sampling problems is to compare pictures in both units. On the continuous-time axis, copies are spaced by $\omega_s$ rad/s. On the discrete-time axis, all frequencies are folded into a $2\pi$-periodic interval. A continuous-time frequency near $\omega_s$ may appear near zero after sampling, while a frequency just above $\omega_s/2$ may appear as a lower-frequency sinusoid with reversed sign convention. Drawing both axes prevents the mistaken belief that high sampled frequencies always remain high in the sequence.

The sample values alone do not contain the sampling rate. The same numerical sequence can represent different analog frequencies if it is played back or interpreted with a different $T$. Always keep the sampling period attached to the data when moving between continuous-time and discrete-time descriptions.

## Visual

```mermaid
flowchart TB
  Analog["Continuous-time signal x_c(t)<br/>bandlimit omega_M if ideal"] --> AntiAlias["Anti-alias filter<br/>remove content above omega_s/2"]
  AntiAlias --> Sampler["Uniform sampler<br/>x(n) = x_c(nT), omega_s = 2pi/T"]
  Sampler --> Sequence["Discrete-time sequence x(n)<br/>DT frequency Omega = omega T"]

  subgraph Spectrum["Sampling spectrum architecture"]
    direction TB
    CTSpec["original spectrum X_c(j omega)"] --> Replicas["impulse-train sampling creates replicas<br/>copies spaced by omega_s"]
    Replicas --> Alias{"copies overlap?"}
    Alias -- "no, omega_s greater than 2 omega_M" --> Safe["samples preserve bandlimited information"]
    Alias -- "yes" --> Fold["aliasing<br/>different CT frequencies map to same DT frequency"]
  end

  AntiAlias --> CTSpec
  Sequence --> Recon{"Reconstruction requested?"}
  Safe --> Recon
  Fold --> Loss["lost information cannot be recovered by ideal interpolation"]
  Recon -- "yes" --> IdealLP["ideal lowpass interpolation<br/>sinc reconstruction for bandlimited signal"]
  Recon -- "practical" --> Practical["hold, interpolation, or reconstruction filter<br/>adds distortion or delay"]
  IdealLP --> Output("(reconstructed x_c(t")"))
  Practical --> Output
  Loss --> Output
```

The sampling diagram shows the full continuous-to-discrete-to-continuous contract. An anti-alias filter and sampler create spectral replicas spaced by $\omega_s$; if those replicas overlap, the aliasing branch records irreversible information loss. The reconstruction branch distinguishes ideal sinc/lowpass recovery from practical holds and filters that trade accuracy for realizability.

| Quantity | Meaning | Formula |
|---|---|---|
| Sampling period | seconds per sample | $T$ |
| Sampling angular frequency | radians per second | $\omega_s=2\pi/T$ |
| Bandlimit | largest nonzero CT frequency | $\omega_M$ |
| Nyquist rate | minimum ideal sampling rate | $2\omega_M$ |
| DT frequency mapping | CT to DT frequency | $\Omega=\omega T$ |
| Spectrum copies | sampled CT spectrum | $\frac{1}{T}\sum_k X_c(j(\omega-k\omega_s))$ |

## Worked example 1: checking the sampling theorem

Problem: A continuous-time signal is bandlimited to

$$
\omega_M=4000\pi \ \text{rad/s}.
$$

It is sampled at

$$
f_s=3000 \ \text{samples/s}.
$$

Determine whether ideal reconstruction is possible.

Method:

1. Convert the bandlimit to hertz:

$$
f_M=\frac{\omega_M}{2\pi}
=\frac{4000\pi}{2\pi}
=2000 \ \text{Hz}.
$$

2. Compute the Nyquist rate:

$$
2f_M=4000 \ \text{samples/s}.
$$

3. Compare with the actual sampling rate:

$$
f_s=3000<4000.
$$

4. Since the sampling rate is below the Nyquist rate, shifted copies of the spectrum overlap.

Checked answer: Ideal reconstruction is not possible from these samples alone. Aliasing occurs. An antialiasing filter would need to reduce the analog bandwidth to below

$$
\frac{f_s}{2}=1500 \ \text{Hz}
$$

before sampling.

## Worked example 2: finding an aliased sinusoid

Problem: The signal

$$
x_c(t)=\cos(1400\pi t)
$$

is sampled at

$$
f_s=1000 \ \text{Hz}.
$$

Find the discrete-time frequency and an equivalent aliased continuous-time frequency in the baseband interval $[-f_s/2,f_s/2]$.

Method:

1. Convert the sinusoid frequency to hertz:

$$
f_0=\frac{1400\pi}{2\pi}=700 \ \text{Hz}.
$$

2. The sampling period is

$$
T=\frac{1}{1000}.
$$

3. The discrete-time radian frequency is

$$
\Omega_0=\omega_0T=(1400\pi)\frac{1}{1000}=1.4\pi.
$$

4. Discrete-time frequency is periodic modulo $2\pi$. Bring $1.4\pi$ into $[-\pi,\pi]$:

$$
1.4\pi-2\pi=-0.6\pi.
$$

5. A cosine is even, so

$$
\cos(-0.6\pi n)=\cos(0.6\pi n).
$$

6. Convert $0.6\pi$ back to hertz:

$$
f_a=\frac{\Omega}{2\pi}f_s
=\frac{0.6\pi}{2\pi}(1000)
=300 \ \text{Hz}.
$$

Checked answer: The 700 Hz sinusoid sampled at 1000 Hz aliases to a 300 Hz cosine in the sampled data. The sequence is

$$
x[n]=\cos(1.4\pi n)=\cos(0.6\pi n).
$$

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 1000.0
f0 = 700.0
T = 1 / fs
n = np.arange(0, 40)

x_samples = np.cos(2 * np.pi * f0 * n * T)
x_alias = np.cos(2 * np.pi * 300.0 * n * T)

print("samples match aliased 300 Hz:", np.allclose(x_samples, x_alias))

t = np.linspace(0, 0.01, 2000)
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t, np.cos(2 * np.pi * f0 * t), label="700 Hz analog")
ax.plot(t, np.cos(2 * np.pi * 300.0 * t), label="300 Hz alias", alpha=0.7)
ax.stem(n * T, x_samples, linefmt="k-", markerfmt="ko", basefmt=" ")
ax.set_xlim(0, 0.01)
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()
```

## Common pitfalls

- Confusing Nyquist rate with Nyquist frequency. The Nyquist rate is $2f_M$; the Nyquist frequency for a sampler is $f_s/2$.
- Forgetting that an ideal reconstruction theorem requires bandlimiting before sampling.
- Assuming a high digital sampling rate fixes aliasing after it has already occurred. Aliasing is created at the sampling operation.
- Mixing angular frequency $\omega$ in rad/s with ordinary frequency $f$ in Hz without the factor $2\pi$.
- Thinking sample values remember the original continuous-time frequency. Frequencies separated by multiples of $f_s$ produce identical samples.

## Connections

- [Continuous-Time Fourier Transform](/physics/signals-systems/continuous-time-fourier-transform)
- [Discrete-Time Fourier Transform](/physics/signals-systems/discrete-time-fourier-transform)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
- [Modulation and Communication Systems](/physics/signals-systems/modulation-communication-systems)
