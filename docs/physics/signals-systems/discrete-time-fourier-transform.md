---
title: Discrete-Time Fourier Transform
sidebar_position: 8
---

# Discrete-Time Fourier Transform

The discrete-time Fourier transform represents an aperiodic sequence as a continuous function of discrete-time frequency. Unlike the continuous-time Fourier transform, the DTFT is always periodic in frequency with period $2\pi$. That periodicity is not a plotting convention; it follows from $e^{j(\Omega+2\pi)n}=e^{j\Omega n}$ for every integer $n$.

The DTFT is the natural frequency-domain tool for digital filters and difference equations when signals are not necessarily periodic. It turns convolution of sequences into multiplication of spectra and exposes the frequency response of a discrete-time LTI system.

## A continuous spectrum for an integer-time sequence

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

The inverse formula follows from orthogonality over one frequency period:

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{j\Omega(n-k)}\,d\Omega
=\delta[n-k].
$$

Insert the analysis sum into the inverse integral and interchange sum and integral:

$$
\begin{aligned}
\frac{1}{2\pi}\int_{-\pi}^{\pi}
X(e^{j\Omega})e^{j\Omega n}\,d\Omega
&=\sum_kx[k]
\frac{1}{2\pi}\int_{-\pi}^{\pi}
e^{j\Omega(n-k)}\,d\Omega\\
&=\sum_kx[k]\delta[n-k]\\
&=x[n].
\end{aligned}
$$

The integral can use any interval of length $2\pi$ because the integrand is periodic. Endpoints such as $-\pi$ and $\pi$ represent the same frequency and should not be counted as two independent bins.

## Operations and their spectral effects

Linearity:

$$
a x_1[n]+b x_2[n]\leftrightarrow aX_1(e^{j\Omega})+bX_2(e^{j\Omega}).
$$

Time shift:

$$
x[n-n_0]\leftrightarrow e^{-j\Omega n_0}X(e^{j\Omega}).
$$

An integer delay adds linear phase and leaves magnitude unchanged. Fractional sample delay cannot be expressed as an ordinary shift of the input index, though an ideal frequency response $e^{-j\Omega d}$ can describe it. For noninteger $d$, that response is not $2\pi$-periodic without a phase discontinuity, and its impulse response is infinite in duration.

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

Factoring the difference response gives

$$
1-e^{-j\Omega}
=2j e^{-j\Omega/2}\sin(\Omega/2).
$$

Its magnitude vanishes at DC and grows toward the Nyquist frequency, so differencing emphasizes rapid sample-to-sample changes. The factor $e^{-j\Omega/2}$ describes the phase center between the two samples.

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

The inner-product form is

$$
\sum_nx[n]y^*[n]
=\frac{1}{2\pi}\int_{2\pi}
X(e^{j\Omega})Y^*(e^{j\Omega})\,d\Omega.
$$

It allows energy or correlation calculations in whichever domain is simpler.

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

## How sampling creates periodic frequency

Suppose a continuous-time signal $x_c(t)$ is sampled every $T_s$ seconds, giving $x[n]=x_c(nT_s)$. Represent the impulse-sampled signal as

$$
x_s(t)=\sum_{n=-\infty}^{\infty}x[n]\delta(t-nT_s).
$$

Its CTFT is

$$
X_s(j\omega)=\sum_nx[n]e^{-j\omega nT_s}
=X(e^{j\Omega})\big|_{\Omega=\omega T_s}.
$$

Since the DTFT repeats every $2\pi$, the sampled-signal spectrum repeats every $2\pi/T_s$ radians per second. Discrete-time frequencies that differ by $2\pi$ produce the same sequence:

$$
e^{j(\Omega+2\pi k)n}=e^{j\Omega n}.
$$

The dimensionless frequency $\Omega$ is radians per sample. It maps to continuous angular frequency through $\Omega=\omega T_s$, but only modulo $2\pi$. Frequencies above half the sampling rate fold into the principal interval and become aliases.

## DTFT, DFT, and Fourier series are different objects

The DTFT takes an infinite or finite aperiodic sequence and returns a continuous, periodic function of frequency. The DFT takes exactly $N$ numbers and returns $N$ numbers. Those DFT values equal samples of the finite sequence's DTFT at

$$
\Omega_k=\frac{2\pi k}{N},
\qquad k=0,1,\ldots,N-1.
$$

The DFT also treats the $N$ input samples as one period of a periodic sequence. Therefore multiplication of DFTs corresponds to circular convolution, not ordinary linear convolution, unless zero padding is long enough to prevent wraparound.

A discrete-time Fourier series represents a periodic sequence using a finite set of distinct harmonic coefficients when the period is $N$. The DTFT of that periodic sequence is an impulse train in frequency. The shared formulas can hide these domain differences, so the signal's periodicity and duration should be identified before selecting a transform.

## Comparing the continuous- and discrete-time transforms

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

## Worked example: DTFT of a right-sided exponential

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

## Worked example: frequency response of a moving average

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

## Worked example: finite rectangular sequence

Let

$$
x[n]=
\begin{cases}
1, & 0\le n\le N-1,\\
0, & \text{otherwise}.
\end{cases}
$$

The DTFT is a finite geometric sum:

$$
X(e^{j\Omega})
=\sum_{n=0}^{N-1}e^{-j\Omega n}
=\frac{1-e^{-j\Omega N}}{1-e^{-j\Omega}}.
$$

Factor numerator and denominator symmetrically:

$$
1-e^{-jN\Omega}
=2j e^{-jN\Omega/2}\sin(N\Omega/2),
$$

$$
1-e^{-j\Omega}
=2j e^{-j\Omega/2}\sin(\Omega/2).
$$

Thus

$$
X(e^{j\Omega})
=e^{-j\Omega(N-1)/2}
\frac{\sin(N\Omega/2)}{\sin(\Omega/2)}.
$$

At multiples of $2\pi$, numerator and denominator both vanish. Returning to the original sum gives the limiting value $N$. The phase factor centers the length-$N$ block at $(N-1)/2$, while the sine ratio controls magnitude.

The first zeros around DC occur at $\Omega=\pm2\pi/N$. Increasing $N$ narrows the main lobe but adds more closely spaced sidelobes. This is the discrete-time rectangular-window spectrum, also called the Dirichlet kernel up to shifts and normalization.

Parseval gives an immediate check. The time-domain energy is $N$, so

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}
\left|
\frac{\sin(N\Omega/2)}{\sin(\Omega/2)}
\right|^2d\Omega=N.
$$

## Convergence and the unit circle

For $x[n]=a^nu[n]$, the associated $z$-transform is

$$
X(z)=\frac{1}{1-az^{-1}},
\qquad |z|>|a|.
$$

The DTFT is obtained by setting $z=e^{j\Omega}$ only if the unit circle lies in this region, requiring $\vert a\vert \lt 1$. The algebraic expression alone does not determine whether a DTFT exists. For $\vert a\vert \gt 1$, the same right-sided sequence grows and its unit-circle sum diverges.

A left-sided sequence can share the same rational expression with a different ROC. For example, $-a^nu[-n-1]$ has ROC $\vert z\vert \lt \vert a\vert $. Its DTFT exists when $\vert a\vert \gt 1$, again because the unit circle must lie in the ROC. Time support and convergence are encoded by the ROC, not by pole locations alone.

## Symmetry and linear phase in finite impulse responses

For a real sequence, conjugate symmetry means that only one half of a spectral period is independent. Additional time symmetry gives stronger constraints. A real even sequence has a real, even DTFT. A real odd sequence has an imaginary, odd DTFT. A shifted symmetric sequence acquires a linear phase factor.

Suppose a real length-$N$ impulse response satisfies

$$
h[n]=h[N-1-n].
$$

Pairing terms equidistant from the midpoint factors the response as

$$
H(e^{j\Omega})
=e^{-j\Omega(N-1)/2}A(\Omega),
$$

where $A(\Omega)$ is real. Away from its sign changes, the phase is a straight line with slope $-(N-1)/2$. The group delay is therefore constant:

$$
\tau_g=-\frac{d}{d\Omega}\angle H(e^{j\Omega})
=\frac{N-1}{2}
$$

samples. A constant group delay preserves the shape of a signal whose spectrum lies in the passband, apart from the magnitude response and an overall delay. Zeros of $A(\Omega)$ can introduce phase jumps of $\pi$ without changing the underlying linear-phase property.

Antisymmetric FIR sequences produce a similar factorization with an imaginary amplitude function. These symmetry conditions are widely used because exact linear phase is possible with finite impulse responses. A causal stable rational IIR filter cannot generally have exact linear phase over the full frequency interval unless its response is essentially a pure delay times a constant.

## Reading normalized frequency

Discrete-time frequency has no physical unit until a sampling rate is supplied. If the sampling frequency is $f_s$, then

$$
\Omega=2\pi\frac{f}{f_s}.
$$

Thus $\Omega=\pi/2$ corresponds to $f_s/4$, while $\Omega=\pi$ corresponds to the Nyquist frequency $f_s/2$. Values outside the principal interval wrap: $3\pi/2$ is equivalent to $-\pi/2$.

Specifications sometimes use cycles per sample, denoted $\nu=f/f_s$, rather than radians per sample. Then one period has length one and the complex exponential is $e^{j2\pi\nu n}$. Mixing $\nu$ with $\Omega$ produces a factor-of-$2\pi$ error analogous to mixing hertz and radians per second in the CTFT.

For real sampled sinusoids, frequencies $\Omega_0$ and $-\Omega_0$ appear as a conjugate pair. At DC and Nyquist, the positive- and negative-frequency representatives coincide modulo $2\pi$. A Nyquist-frequency cosine is simply $(-1)^n$; a sine at exactly that frequency samples to zero for zero initial phase.

## Finite records and leakage

Taking $N$ observed samples multiplies an underlying sequence by a finite window. Multiplication in time becomes periodic convolution in DTFT frequency, spreading each spectral component by the window spectrum. If a sinusoid completes an integer number of cycles in the record, its frequency aligns with a DFT grid point and the rectangular-window zeros fall on the other bins. Otherwise its energy appears across many bins.

Zero padding samples the same windowed DTFT more densely. Peaks look smoother and their displayed locations can be estimated more finely, but the main-lobe width and ability to separate close components remain governed by the nonzero observation length. A longer record supplies the narrower window transform needed for genuinely better resolution.

## Checks for periodic-frequency mistakes

- Forgetting that the DTFT is periodic with period $2\pi$.
- Integrating over the whole real frequency line in the inverse DTFT instead of one $2\pi$ interval.
- Evaluating a $z$-transform on the unit circle without checking whether the unit circle lies in the ROC.
- Treating $\Omega=\pi$ and $\Omega=-\pi$ as unrelated points. They represent the same discrete-time frequency.
- Assuming a moving average is an ideal lowpass filter. It attenuates bands according to its exact frequency response.

## Related pages

- [Fourier Series for Periodic Signals](/physics/signals-systems/fourier-series-periodic-signals)
- [LTI Systems and Convolution](/physics/signals-systems/lti-systems-convolution)
- [Sampling, Aliasing, and Reconstruction](/physics/signals-systems/sampling-aliasing-reconstruction)
- [Z-Transform and ROC](/physics/signals-systems/z-transform-roc)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
