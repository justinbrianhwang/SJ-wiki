---
title: Discrete-Time Fourier Transform
sidebar_position: 8
---

# Discrete-Time Fourier Transform

The discrete-time Fourier transform represents an aperiodic sequence as a continuous function of discrete-time frequency. Unlike the continuous-time Fourier transform, the DTFT is always periodic in frequency with period $2\pi$. That periodicity is not a plotting convention; it follows from $e^{j(\Omega+2\pi)n}=e^{j\Omega n}$ for every integer $n$.

The DTFT is the natural frequency-domain tool for digital filters and difference equations when signals are not necessarily periodic. It turns convolution of sequences into multiplication of spectra and makes the frequency response of a discrete-time LTI system visible.

## Definitions

The DTFT of a sequence $x[n]$ is

$$
X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}.
$$

The inverse DTFT is

$$
x[n]=\frac{1}{2\pi}\int_{2\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega,
$$

where the integral is over any interval of length $2\pi$, such as $-\pi\le \Omega\lt \pi$.

The notation $X(e^{j\Omega})$ emphasizes that the DTFT is the $z$-transform evaluated on the unit circle when the unit circle lies in the region of convergence. The same object is sometimes written as $X(\Omega)$.

The DTFT is periodic:

$$
X(e^{j(\Omega+2\pi)})=X(e^{j\Omega}).
$$

This follows directly:

$$
\sum_n x[n]e^{-j(\Omega+2\pi)n}
=\sum_n x[n]e^{-j\Omega n}e^{-j2\pi n}
=\sum_n x[n]e^{-j\Omega n}.
$$

Absolute summability,

$$
\sum_{n=-\infty}^{\infty}|x[n]|<\infty,
$$

is a common sufficient condition for the DTFT to exist as a continuous function. Many important sequences have DTFTs in a generalized or limiting sense.

Important pairs include

$$
\delta[n]\leftrightarrow 1,
$$

$$
\delta[n-n_0]\leftrightarrow e^{-j\Omega n_0},
$$

and, for $\vert a\vert \lt 1$,

$$
a^n u[n]\leftrightarrow \frac{1}{1-ae^{-j\Omega}}.
$$

For real-valued sequences,

$$
X(e^{-j\Omega})=X^*(e^{j\Omega}).
$$

Thus magnitude is even and phase is odd, with care around zeros and phase wrapping.

## Key results

Linearity:

$$
a x_1[n]+b x_2[n]\leftrightarrow aX_1(e^{j\Omega})+bX_2(e^{j\Omega}).
$$

Time shift:

$$
x[n-n_0]\leftrightarrow e^{-j\Omega n_0}X(e^{j\Omega}).
$$

Frequency shift:

$$
e^{j\Omega_0 n}x[n]\leftrightarrow X(e^{j(\Omega-\Omega_0)}).
$$

Time reversal:

$$
x[-n]\leftrightarrow X(e^{-j\Omega}).
$$

First difference:

$$
x[n]-x[n-1]\leftrightarrow (1-e^{-j\Omega})X(e^{j\Omega}).
$$

Convolution:

$$
x[n]*h[n]\leftrightarrow X(e^{j\Omega})H(e^{j\Omega}).
$$

Multiplication:

$$
x[n]h[n]\leftrightarrow \frac{1}{2\pi}\int_{2\pi}X(e^{j\theta})H(e^{j(\Omega-\theta)})\,d\theta.
$$

Parseval's relation:

$$
\sum_{n=-\infty}^{\infty}|x[n]|^2
=\frac{1}{2\pi}\int_{2\pi}|X(e^{j\Omega})|^2\,d\Omega.
$$

For a discrete-time LTI system with impulse response $h[n]$, the frequency response is

$$
H(e^{j\Omega})=\sum_{n=-\infty}^{\infty}h[n]e^{-j\Omega n}.
$$

If $y=x*h$, then

$$
Y(e^{j\Omega})=X(e^{j\Omega})H(e^{j\Omega}).
$$

For a stable LTI system, $h[n]$ is absolutely summable, so $H(e^{j\Omega})$ exists as a bounded continuous function. For recursive systems, the DTFT can often be obtained by evaluating the $z$-transform on the unit circle, but only when the unit circle is in the ROC.

The DTFT is continuous in frequency even though the signal is discrete in time. This surprises many students because finite computer calculations use the DFT, which samples the DTFT at finitely many frequency points. The DFT is not the same object as the DTFT, but it is often used to compute samples of it for finite-duration data. Zero padding interpolates the displayed frequency grid; it does not create new information about the underlying signal.

Because the frequency axis is periodic, plotting choices matter. A spectrum shown over $0\le\Omega\lt 2\pi$ and the same spectrum shown over $-\pi\le\Omega\lt \pi$ contain identical information. The second view is often easier for lowpass and highpass interpretation because zero frequency is centered. Phase plots require unwrapping if one wants to see linear phase as a straight line rather than jumps of $2\pi$.

Finite-length sequences always have DTFTs that are trigonometric polynomials:

$$
X(e^{j\Omega})=\sum_{n=n_1}^{n_2}x[n]e^{-j\Omega n}.
$$

Infinite-length sequences require convergence checks, which is where absolute summability and the $z$-transform ROC become important.

For LTI filtering, the DTFT is most useful when the input can be understood as a mixture of discrete-time complex exponentials. A component at $\Omega_0$ is multiplied by $H(e^{j\Omega_0})$, but the same component is also at $\Omega_0+2\pi k$. This means filter specifications should name a principal interval, usually $-\pi\le\Omega\lt \pi$, and should respect the wraparound behavior at the endpoints.

When checking answers, substitute a few simple frequencies. At $\Omega=0$, the DTFT is the sum of all samples when the sum converges. At $\Omega=\pi$, the factor $e^{-j\pi n}=(-1)^n$ alternates signs. These two values often reveal sign mistakes in delays and first-difference filters.

## Visual

| Concept | CTFT | DTFT |
|---|---|---|
| Time variable | real $t$ | integer $n$ |
| Frequency variable | $\omega$ on real line | $\Omega$ modulo $2\pi$ |
| Analysis | integral over time | sum over samples |
| Inverse | integral over all $\omega$ | integral over one $2\pi$ interval |
| Spectrum periodic? | no, not generally | yes, always |
| LTI action | multiply by $H(j\omega)$ | multiply by $H(e^{j\Omega})$ |

```text
DTFT frequency axis repeats:

        -2pi        -pi          0          pi         2pi
---------|-----------|-----------|-----------|-----------|----> Omega
          [ one complete spectral period can be chosen here )
```

## Worked example 1: DTFT of a right-sided exponential

Problem: Find the DTFT of

$$
x[n]=a^n u[n], \qquad |a|<1.
$$

Method:

1. Start from the definition:

$$
X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}a^n u[n]e^{-j\Omega n}.
$$

2. The unit step restricts the sum to $n\ge 0$:

$$
X(e^{j\Omega})=\sum_{n=0}^{\infty}a^n e^{-j\Omega n}.
$$

3. Combine the factors:

$$
X(e^{j\Omega})=\sum_{n=0}^{\infty}(a e^{-j\Omega})^n.
$$

4. Since $\vert a\vert \lt 1$ and $\vert e^{-j\Omega}\vert =1$, the geometric series converges:

$$
\sum_{n=0}^{\infty}r^n=\frac{1}{1-r}.
$$

5. Set $r=a e^{-j\Omega}$:

$$
X(e^{j\Omega})=\frac{1}{1-ae^{-j\Omega}}.
$$

Checked answer:

$$
a^n u[n]\leftrightarrow \frac{1}{1-ae^{-j\Omega}}, \qquad |a|<1.
$$

The result is periodic in $\Omega$ because replacing $\Omega$ by $\Omega+2\pi$ leaves $e^{-j\Omega}$ unchanged.

## Worked example 2: frequency response of a moving average

Problem: Find the frequency response of the three-point moving average

$$
y[n]=\frac{1}{3}\left(x[n]+x[n-1]+x[n-2]\right).
$$

Method:

1. Identify the impulse response by setting $x[n]=\delta[n]$:

$$
h[n]=\frac{1}{3}\left(\delta[n]+\delta[n-1]+\delta[n-2]\right).
$$

2. Take the DTFT:

$$
H(e^{j\Omega})=\frac{1}{3}\left(1+e^{-j\Omega}+e^{-j2\Omega}\right).
$$

3. Factor out the linear phase term $e^{-j\Omega}$:

$$
H(e^{j\Omega})=\frac{1}{3}e^{-j\Omega}\left(e^{j\Omega}+1+e^{-j\Omega}\right).
$$

4. Use $e^{j\Omega}+e^{-j\Omega}=2\cos\Omega$:

$$
H(e^{j\Omega})=\frac{1}{3}e^{-j\Omega}\left(1+2\cos\Omega\right).
$$

5. The magnitude is

$$
|H(e^{j\Omega})|=\frac{1}{3}|1+2\cos\Omega|.
$$

At $\Omega=0$:

$$
H(e^{j0})=\frac{1}{3}(1+1+1)=1.
$$

At $\Omega=\pi$:

$$
H(e^{j\pi})=\frac{1}{3}(1-1+1)=\frac{1}{3}.
$$

Checked answer: The moving average passes DC with gain $1$ and attenuates higher frequencies. It is a simple lowpass-like FIR filter, although it does not completely remove $\Omega=\pi$.

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

Omega = np.linspace(-np.pi, np.pi, 1000)
H = (1 + np.exp(-1j * Omega) + np.exp(-2j * Omega)) / 3

a = 0.7
X = 1 / (1 - a * np.exp(-1j * Omega))

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].plot(Omega, np.abs(X))
ax[0].set_title(r"$\vert 1/(1-ae^{-j\Omega})\vert $")
ax[0].grid(True)

ax[1].plot(Omega, np.abs(H))
ax[1].set_title("Three-point moving average magnitude")
ax[1].grid(True)
plt.tight_layout()
plt.show()
```

## Common pitfalls

- Forgetting that the DTFT is periodic with period $2\pi$.
- Integrating over the whole real frequency line in the inverse DTFT instead of one $2\pi$ interval.
- Evaluating a $z$-transform on the unit circle without checking whether the unit circle lies in the ROC.
- Treating $\Omega=\pi$ and $\Omega=-\pi$ as unrelated points. They represent the same discrete-time frequency.
- Assuming a moving average is an ideal lowpass filter. It attenuates bands according to its exact frequency response.

## Connections

- [Fourier Series for Periodic Signals](/physics/signals-systems/fourier-series-periodic-signals)
- [LTI Systems and Convolution](/physics/signals-systems/lti-systems-convolution)
- [Sampling, Aliasing, and Reconstruction](/physics/signals-systems/sampling-aliasing-reconstruction)
- [Z-Transform and ROC](/physics/signals-systems/z-transform-roc)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
