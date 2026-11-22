---
title: Periodicity, Energy, and Power
sidebar_position: 3
---

# Periodicity, Energy, and Power

Signals can be classified by how they repeat and by how much accumulated magnitude they contain. These classifications decide which analysis tools are natural. A finite-duration pulse is often an energy signal and is well suited to Fourier transform analysis. A sinusoid that lasts forever has infinite total energy but finite average power, so it is handled through Fourier series or generalized transform ideas.

The words energy and power are mathematical analogies unless the signal is literally voltage, current, displacement, or another physical quantity in a specified system. In signals and systems, they measure size. Energy accumulates $\vert x\vert ^2$ over all time or samples. Average power measures the long-term average of $\vert x\vert ^2$ over a growing symmetric observation window.

## Definitions

A continuous-time signal $x(t)$ is periodic if there exists a positive number $T$ such that

$$
x(t+T)=x(t)
$$

for all $t$. The smallest positive such $T$, if it exists, is the fundamental period $T_0$. The fundamental angular frequency is

$$
\omega_0=\frac{2\pi}{T_0}.
$$

A discrete-time signal $x[n]$ is periodic if there exists a positive integer $N$ such that

$$
x[n+N]=x[n]
$$

for all integer $n$. The smallest positive such integer is the fundamental period $N_0$. The fundamental discrete-time radian frequency is

$$
\Omega_0=\frac{2\pi}{N_0}.
$$

Continuous-time complex exponentials

$$
e^{j\omega_0 t}
$$

are periodic for every nonzero real $\omega_0$, with fundamental period

$$
T_0=\frac{2\pi}{|\omega_0|}.
$$

Discrete-time complex exponentials

$$
e^{j\Omega_0 n}
$$

are periodic only when $\Omega_0/(2\pi)$ is rational. If

$$
\frac{\Omega_0}{2\pi}=\frac{m}{N}
$$

in lowest terms, then the fundamental period is $N_0=N$.

The continuous-time energy of $x(t)$ is

$$
E_x=\int_{-\infty}^{\infty}|x(t)|^2\,dt.
$$

The discrete-time energy is

$$
E_x=\sum_{n=-\infty}^{\infty}|x[n]|^2.
$$

The continuous-time average power is

$$
P_x=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt,
$$

when the limit exists. The discrete-time average power is

$$
P_x=\lim_{N\to\infty}\frac{1}{2N+1}\sum_{n=-N}^{N}|x[n]|^2.
$$

An energy signal has

$$
0<E_x<\infty.
$$

A power signal has

$$
0<P_x<\infty.
$$

A nonzero signal cannot be both an energy signal and a power signal under these definitions. Some signals are neither, such as $x(t)=t$ or $x[n]=n$.

## Key results

If a nonzero signal is periodic and has finite average squared magnitude over one period, it is a power signal rather than an energy signal. For continuous time,

$$
P_x=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|x(t)|^2\,dt
$$

for any starting time $t_0$. For discrete time,

$$
P_x=\frac{1}{N_0}\sum_{n=n_0}^{n_0+N_0-1}|x[n]|^2.
$$

The proof is based on tiling the real line or integer line by complete periods. The contribution of each complete period is the same. Boundary fragments at the ends of a large averaging interval become negligible after division by interval length.

For sums of continuous-time periodic signals, a common period exists if the ratio of their fundamental periods is rational. Equivalently, for sinusoids with angular frequencies $\omega_1$ and $\omega_2$, a common period exists if

$$
\frac{\omega_1}{\omega_2}
$$

is rational. If the ratio is irrational, the sum is not periodic even though each component is periodic.

For discrete-time sinusoids, each component must first be periodic by the rational-frequency condition, and then the sum's fundamental period is the least common multiple of the individual fundamental periods.

Energy and power scale predictably. If $y(t)=a x(t)$, then

$$
E_y=|a|^2E_x, \qquad P_y=|a|^2P_x.
$$

If $y(t)=x(t-t_0)$, energy and power do not change. If $y(t)=x(a t)$ in continuous time with $a\ne 0$, then

$$
E_y=\frac{1}{|a|}E_x.
$$

The average power of a periodic signal is unchanged by time scaling if the scaled signal remains periodic and the average is computed over its new period.

Classification should be done before transform selection. A finite-energy signal may still have a Fourier transform with rich frequency content, but its average power is zero because the finite energy is spread over an infinitely long averaging window. A periodic signal may have a simple formula and be bounded forever, but its total energy is infinite because the same nonzero contribution repeats over infinitely many periods. A growing signal can fail both tests: its accumulated energy is infinite and its average power may also diverge.

For sums of signals, do not classify only by appearance. The sum of two energy signals is an energy signal if both have finite energy. The sum of a nonzero power signal and an energy signal usually has the same long-term power as the power signal plus any persistent cross-term that survives averaging. The sum of periodic signals is periodic only when a common period exists. These distinctions become important when deciding whether to use Fourier series, CTFT/DTFT, or a more general transform.

Symmetry also helps with calculations. Even signals often allow energy integrals over half the domain doubled:

$$
\int_{-\infty}^{\infty}|x(t)|^2dt=2\int_{0}^{\infty}|x(t)|^2dt
$$

when $\vert x(t)\vert ^2$ is even. For discrete-time sequences with symmetric samples, pair positive and negative indices to reduce arithmetic, but keep the $n=0$ sample only once.

## Visual

| Signal type | Continuous-time test | Discrete-time test | Typical analysis tool |
|---|---|---|---|
| Finite-duration pulse | finite $\int \vert x(t)\vert ^2dt$ | finite $\sum \vert x[n]\vert ^2$ | Fourier transform |
| Decaying exponential | finite if decay is strong enough | finite if $\vert a\vert \lt 1$ for right-sided $a^n u[n]$ | Laplace or $z$ transform |
| Nonzero sinusoid | infinite energy, finite power | finite power if periodic or bounded tone | Fourier series / spectral lines |
| Constant nonzero signal | $P=\vert c\vert ^2$ | $P=\vert c\vert ^2$ | DC component |
| Growing ramp | usually neither | usually neither | local or generalized analysis |

```text
energy signal: accumulated area is finite

|x(t)|^2
  ^
  |        /\
  |       /  \       small tails
  |______/____\________________> t

power signal: average level persists forever

|x(t)|^2
  ^
  |   _   _   _   _   _
  |__/ \_/ \_/ \_/ \_/ \____> t
```

## Worked example 1: energy and power of a finite pulse

Problem: Let

$$
x(t)=
\begin{cases}
3, & -2\le t\le 1,\\
0, & \text{otherwise}.
\end{cases}
$$

Determine its energy and average power.

Method:

1. Compute energy:

$$
E_x=\int_{-\infty}^{\infty}|x(t)|^2\,dt.
$$

2. The signal is nonzero only on $[-2,1]$, so

$$
E_x=\int_{-2}^{1}9\,dt.
$$

3. The interval length is $1-(-2)=3$, hence

$$
E_x=9(3)=27.
$$

4. Compute average power:

$$
P_x=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt.
$$

5. For all large enough $T$, the integral over $[-T,T]$ includes the whole pulse and equals $27$:

$$
P_x=\lim_{T\to\infty}\frac{27}{2T}=0.
$$

Checked answer: The signal is an energy signal with $E_x=27$ and average power $P_x=0$. It is not a power signal because the required power classification has $0\lt P_x\lt \infty$.

## Worked example 2: periodicity of a discrete-time sinusoid

Problem: Determine whether

$$
x[n]=\cos\left(\frac{3\pi}{7}n+\frac{\pi}{5}\right)
$$

is periodic, and find its fundamental period if it is.

Method:

1. A phase shift does not affect periodicity. Check the angular frequency

$$
\Omega_0=\frac{3\pi}{7}.
$$

2. A discrete-time complex exponential or sinusoid is periodic when

$$
\frac{\Omega_0}{2\pi}
$$

is rational:

$$
\frac{\Omega_0}{2\pi}
=\frac{3\pi/7}{2\pi}
=\frac{3}{14}.
$$

3. The fraction $3/14$ is in lowest terms. Therefore the fundamental period of the complex exponential $e^{j(3\pi/7)n}$ is $14$.

4. For a cosine, one must check whether a smaller period is possible because cosine is even. Require

$$
\frac{3\pi}{7}N=2\pi k
$$

for some integer $k$. This gives

$$
3N=14k.
$$

The smallest positive integer $N$ satisfying this is $N=14$.

Checked answer:

$$
N_0=14.
$$

A quick check is

$$
\cos\left(\frac{3\pi}{7}(n+14)+\frac{\pi}{5}\right)
=\cos\left(\frac{3\pi}{7}n+6\pi+\frac{\pi}{5}\right)
=x[n].
$$

## Code

```python
import math
import numpy as np
from fractions import Fraction

def discrete_period_from_frequency(omega):
    ratio = omega / (2 * math.pi)
    frac = Fraction(ratio).limit_denominator(10_000)
    return frac.denominator, frac

omega = 3 * math.pi / 7
N0, ratio = discrete_period_from_frequency(omega)
print("Omega/(2*pi) =", ratio)
print("fundamental period candidate =", N0)

n = np.arange(0, 2 * N0)
x = np.cos(omega * n + math.pi / 5)
print("one-period repeat:", np.allclose(x[:N0], x[N0:]))
```

## Common pitfalls

- Calling every sinusoid periodic in discrete time. $e^{j\Omega n}$ is periodic only when $\Omega/(2\pi)$ is rational.
- Reporting average power of an energy signal as a positive number. Finite-energy signals have zero average power.
- Forgetting absolute value squared for complex signals. Use $\vert x\vert ^2$, not $x^2$.
- Averaging a periodic signal over a non-integer piece of a period and treating that as the long-term power.
- Assuming a finite number of nonzero samples has nonzero average power. Its energy may be finite, but its average power is zero.

## Connections

- [Signals and Time Transformations](/physics/signals-systems/signals-time-transformations)
- [Fourier Series for Periodic Signals](/physics/signals-systems/fourier-series-periodic-signals)
- [Continuous-Time Fourier Transform](/physics/signals-systems/continuous-time-fourier-transform)
- [Discrete-Time Fourier Transform](/physics/signals-systems/discrete-time-fourier-transform)
