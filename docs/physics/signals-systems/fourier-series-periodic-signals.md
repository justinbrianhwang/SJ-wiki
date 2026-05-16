---
title: Fourier Series for Periodic Signals
sidebar_position: 6
---

# Fourier Series for Periodic Signals

Fourier series represent periodic signals as weighted sums of harmonically related complex exponentials. The idea is powerful because complex exponentials are eigenfunctions of LTI systems: when a sinusoidal component passes through an LTI system, only its amplitude and phase change. A periodic signal can therefore be analyzed component by component in frequency.

Continuous-time and discrete-time Fourier series share the same conceptual structure, but their details differ. Continuous-time periodic signals generally require infinitely many harmonics. Discrete-time periodic sequences have only finitely many distinct harmonics over one period because discrete-time frequency repeats every $2\pi$.

## Definitions

For a continuous-time periodic signal with fundamental period $T_0$ and fundamental angular frequency

$$
\omega_0=\frac{2\pi}{T_0},
$$

the complex exponential Fourier series is

$$
x(t)=\sum_{k=-\infty}^{\infty}a_k e^{j k\omega_0 t}.
$$

The coefficients are

$$
a_k=\frac{1}{T_0}\int_{T_0}x(t)e^{-j k\omega_0 t}\,dt,
$$

where $\int_{T_0}$ means integration over any complete period.

For a discrete-time periodic sequence with fundamental period $N$, the discrete-time Fourier series is

$$
x[n]=\sum_{k=0}^{N-1}a_k e^{j(2\pi/N)kn}.
$$

The coefficients are

$$
a_k=\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j(2\pi/N)kn}.
$$

The coefficient sequence is periodic in $k$ with period $N$:

$$
a_{k+N}=a_k.
$$

For real continuous-time signals, the coefficients satisfy conjugate symmetry:

$$
a_{-k}=a_k^*.
$$

For real discrete-time periodic sequences,

$$
a_{N-k}=a_k^*
$$

with indices interpreted modulo $N$.

The trigonometric continuous-time series is

$$
x(t)=A_0+\sum_{k=1}^{\infty}\left(A_k\cos(k\omega_0 t)+B_k\sin(k\omega_0 t)\right).
$$

The complex form is usually cleaner for system analysis, while the trigonometric form is sometimes easier to read physically.

## Key results

The orthogonality of complex exponentials over one period is the key identity. In continuous time,

$$
\frac{1}{T_0}\int_{T_0}e^{j k\omega_0 t}e^{-j m\omega_0 t}\,dt
=
\begin{cases}
1, & k=m,\\
0, & k\ne m.
\end{cases}
$$

In discrete time,

$$
\frac{1}{N}\sum_{n=0}^{N-1}e^{j(2\pi/N)kn}e^{-j(2\pi/N)mn}
=
\begin{cases}
1, & k=m \pmod N,\\
0, & \text{otherwise}.
\end{cases}
$$

These identities isolate a single coefficient when the signal is multiplied by a conjugate harmonic and averaged over one period.

Parseval's relation connects time-domain average power to coefficient magnitudes. For continuous time,

$$
P_x=\frac{1}{T_0}\int_{T_0}|x(t)|^2\,dt
=\sum_{k=-\infty}^{\infty}|a_k|^2.
$$

For discrete time,

$$
P_x=\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2
=\sum_{k=0}^{N-1}|a_k|^2.
$$

If a periodic signal is the input to an LTI system with frequency response $H(j\omega)$, then

$$
x(t)=\sum_k a_k e^{j k\omega_0 t}
$$

produces

$$
y(t)=\sum_k a_k H(jk\omega_0)e^{j k\omega_0 t}.
$$

For discrete time, the factor is $H(e^{j2\pi k/N})$. This result is one reason Fourier series appears immediately after LTI systems.

At jump discontinuities, the Fourier series converges to the midpoint of the left and right limits under standard Dirichlet conditions:

$$
\frac{x(t_0^-)+x(t_0^+)}{2}.
$$

Near jumps, partial sums show overshoot known as the Gibbs phenomenon. Increasing the number of harmonics narrows the oscillatory region but does not remove the limiting overshoot.

Coefficient patterns reveal signal structure. A real and even continuous-time signal has real and even coefficients. A real and odd signal has purely imaginary, odd-symmetric coefficients in the complex form. Half-wave symmetry often removes even harmonics. These facts are not just shortcuts; they are checks on whether the coefficient signs and factors are plausible.

The DC coefficient is the average value over one period. In continuous time,

$$
a_0=\frac{1}{T_0}\int_{T_0}x(t)\,dt.
$$

In discrete time,

$$
a_0=\frac{1}{N}\sum_{n=0}^{N-1}x[n].
$$

If a waveform spends equal positive and negative area over a period, $a_0$ should be zero. If the signal is always nonnegative, a negative $a_0$ is a warning sign.

Fourier series also separates waveform smoothness from spectral decay. Signals with jumps have coefficients that decay slowly, typically like $1/\vert k\vert $. Signals with more smooth derivatives have faster coefficient decay. This is why sharp edges require many harmonics to approximate accurately.

## Visual

| Feature | CT Fourier series | DT Fourier series |
|---|---|---|
| Signal type | periodic $x(t)$ | periodic $x[n]$ |
| Fundamental frequency | $\omega_0=2\pi/T_0$ | $\Omega_0=2\pi/N$ |
| Synthesis | $\sum_{k=-\infty}^{\infty}a_k e^{jk\omega_0t}$ | $\sum_{k=0}^{N-1}a_k e^{j(2\pi/N)kn}$ |
| Analysis | $\frac{1}{T_0}\int_{T_0}x(t)e^{-jk\omega_0t}dt$ | $\frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-j(2\pi/N)kn}$ |
| Number of distinct harmonics | countably infinite | $N$ |
| Power relation | $P=\sum_{k=-\infty}^{\infty}\vert a_k\vert ^2$ | $P=\sum_{k=0}^{N-1}\vert a_k\vert ^2$ |

```mermaid
flowchart LR
  A[Periodic signal] --> B[Average against harmonic k]
  B --> C[Coefficient a_k]
  C --> D[Line spectrum]
  D --> E[LTI scales by H at harmonic]
  E --> F[Output periodic signal]
```

## Worked example 1: CTFS coefficients of a square wave

Problem: Let $x(t)$ be periodic with period $T_0=2\pi$ and

$$
x(t)=
\begin{cases}
1, & 0<t<\pi,\\
-1, & -\pi<t<0.
\end{cases}
$$

Find the complex Fourier series coefficients.

Method:

1. The fundamental frequency is

$$
\omega_0=\frac{2\pi}{2\pi}=1.
$$

2. Use the coefficient formula:

$$
a_k=\frac{1}{2\pi}\int_{-\pi}^{\pi}x(t)e^{-jkt}\,dt.
$$

3. Split the integral:

$$
a_k=\frac{1}{2\pi}
\left(
\int_{-\pi}^{0}(-1)e^{-jkt}\,dt
+\int_{0}^{\pi}e^{-jkt}\,dt
\right).
$$

4. For $k\ne 0$,

$$
\int e^{-jkt}\,dt=\frac{e^{-jkt}}{-jk}.
$$

Therefore

$$
a_k=\frac{1}{2\pi}
\left(
-\frac{1-e^{jk\pi}}{-jk}
+\frac{e^{-jk\pi}-1}{-jk}
\right).
$$

5. Since $e^{jk\pi}=e^{-jk\pi}=(-1)^k$,

$$
a_k=\frac{1}{2\pi}
\left(
\frac{1-(-1)^k}{jk}
+\frac{(-1)^k-1}{-jk}
\right).
$$

The two terms are equal, so

$$
a_k=\frac{1}{2\pi}\frac{2(1-(-1)^k)}{jk}
=\frac{1-(-1)^k}{j\pi k}.
$$

6. For even $k$, $1-(-1)^k=0$. For odd $k$, $1-(-1)^k=2$:

$$
a_k=
\begin{cases}
\frac{2}{j\pi k}, & k \text{ odd},\\
0, & k \text{ even}.
\end{cases}
$$

7. The DC coefficient is

$$
a_0=\frac{1}{2\pi}\left(-\pi+\pi\right)=0.
$$

Checked answer: The signal is odd, so coefficients are purely imaginary and odd-symmetric, which agrees with $a_k=2/(j\pi k)$ for odd $k$ and zero otherwise.

## Worked example 2: DTFS coefficients of a period-4 sequence

Problem: A periodic sequence has one period

$$
x[0]=1,\quad x[1]=2,\quad x[2]=1,\quad x[3]=0.
$$

Find its DTFS coefficients.

Method:

1. The period is $N=4$, so

$$
a_k=\frac{1}{4}\sum_{n=0}^{3}x[n]e^{-j(2\pi/4)kn}.
$$

2. Simplify the frequency factor:

$$
e^{-j(2\pi/4)kn}=e^{-j(\pi/2)kn}.
$$

3. Compute each coefficient.

For $k=0$:

$$
a_0=\frac{1}{4}(1+2+1+0)=1.
$$

For $k=1$:

$$
a_1=\frac{1}{4}\left(1+2e^{-j\pi/2}+e^{-j\pi}+0\right).
$$

Use $e^{-j\pi/2}=-j$ and $e^{-j\pi}=-1$:

$$
a_1=\frac{1}{4}(1-2j-1)=-\frac{j}{2}.
$$

For $k=2$:

$$
a_2=\frac{1}{4}\left(1+2e^{-j\pi}+e^{-j2\pi}\right)
=\frac{1}{4}(1-2+1)=0.
$$

For $k=3$:

$$
a_3=\frac{1}{4}\left(1+2e^{-j3\pi/2}+e^{-j3\pi}\right).
$$

Use $e^{-j3\pi/2}=j$ and $e^{-j3\pi}=-1$:

$$
a_3=\frac{1}{4}(1+2j-1)=\frac{j}{2}.
$$

Checked answer:

$$
a_0=1,\qquad a_1=-\frac{j}{2},\qquad a_2=0,\qquad a_3=\frac{j}{2}.
$$

Because $x[n]$ is real, $a_3=a_1^*$, as expected.

## Code

```python
import numpy as np

x = np.array([1, 2, 1, 0], dtype=complex)
N = len(x)
n = np.arange(N)
k = np.arange(N)

W = np.exp(-1j * 2 * np.pi / N * np.outer(k, n))
a = (W @ x) / N

print("DTFS coefficients:")
for idx, coeff in enumerate(a):
    print(idx, np.round(coeff, 6))

x_rebuilt = np.exp(1j * 2 * np.pi / N * np.outer(n, k)) @ a
print("reconstruction:", np.round(x_rebuilt.real, 6))
```

## Common pitfalls

- Using Fourier transform formulas for a periodic signal without recognizing the spectrum is made of lines.
- Forgetting the $1/T_0$ or $1/N$ factor in the analysis equation.
- Summing DTFS over infinitely many distinct harmonics. Only $N$ harmonics are distinct for period $N$.
- Assuming the Fourier series equals the original value exactly at a jump. It converges to the midpoint under standard conditions.
- Losing conjugate symmetry checks for real signals; they are useful for catching sign errors.

## Connections

- [Periodicity, Energy, and Power](/physics/signals-systems/periodicity-energy-power)
- [LTI Systems and Convolution](/physics/signals-systems/lti-systems-convolution)
- [Continuous-Time Fourier Transform](/physics/signals-systems/continuous-time-fourier-transform)
- [Discrete-Time Fourier Transform](/physics/signals-systems/discrete-time-fourier-transform)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
