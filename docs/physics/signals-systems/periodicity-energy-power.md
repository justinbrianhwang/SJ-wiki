---
title: Periodicity, Energy, and Power
sidebar_position: 3
---

# Periodicity, Energy, and Power

Signals can be classified by how they repeat and by how much accumulated magnitude they contain. These classifications decide which analysis tools are natural. A finite-duration pulse is often an energy signal and is well suited to Fourier transform analysis. A sinusoid that lasts forever has infinite total energy but finite average power, so it is handled through Fourier series or generalized transform ideas.

The words energy and power are mathematical analogies unless the signal is literally voltage, current, displacement, or another physical quantity in a specified system. In signals and systems, they measure size. Energy accumulates $\vert x\vert ^2$ over all time or samples. Average power measures the long-term average of $\vert x\vert ^2$ over a growing symmetric observation window.

Units follow the signal being squared. If $x$ is a voltage, the definitions have voltage-squared units unless an impedance factor is included. Calling the result joules or watts without a physical model and reference impedance is therefore inaccurate.

## Periodicity in continuous and discrete time

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

The zero signal is a harmless exception to the usual classification language: it has zero energy and zero average power, so it satisfies neither definition requiring a strictly positive value. Some texts loosely include it in both classes by allowing zero.

Energy and power use squared magnitude because signals may be negative or complex. For a complex value, $\vert x\vert ^2=xx^*$ is real and nonnegative. Without conjugation, positive and negative or complex contributions could cancel and fail to measure signal size.

## Why periodic signals have power rather than finite energy

If a nonzero signal is periodic and has finite average squared magnitude over one period, it is a power signal rather than an energy signal. For continuous time,

$$
P_x=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|x(t)|^2\,dt
$$

for any starting time $t_0$. For discrete time,

$$
P_x=\frac{1}{N_0}\sum_{n=n_0}^{n_0+N_0-1}|x[n]|^2.
$$

The proof is based on tiling the real line or integer line by complete periods. The contribution of each complete period is the same. Boundary fragments at the ends of a large averaging interval become negligible after division by interval length.

Let the energy contained in one continuous-time period be

$$
E_0=\int_{t_0}^{t_0+T_0}|x(t)|^2\,dt.
$$

If $x$ is nonzero except perhaps on a set of zero measure, then $E_0\gt 0$. Over $M$ full periods the energy is $ME_0$, which grows without bound as $M\to\infty$. Dividing by the total duration $MT_0$ instead gives the fixed average $E_0/T_0$. The discrete-time argument replaces integrals with sums.

For any finite-energy signal,

$$
\int_{-T}^{T}|x(t)|^2dt\le E_x.
$$

Therefore

$$
0\le\frac{1}{2T}\int_{-T}^{T}|x(t)|^2dt
\le\frac{E_x}{2T}\to0.
$$

Finite energy forces zero average power. This proves that a nonzero signal cannot satisfy both strict classifications.

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

## Combining periodic components

For continuous-time sinusoids, a common period $T$ must satisfy

$$
\omega_kT=2\pi m_k
$$

for an integer $m_k$ for every component. Two nonzero frequencies therefore share a period exactly when their ratio is rational. A constant term is periodic with every positive period and does not constrain the common period.

After a common period is found, it may not be fundamental. Candidate periods should be checked for a smaller shared value, especially when phases, cancellations, or harmonically related terms are present. If two identical-frequency sinusoids cancel completely, the resulting zero signal has no unique fundamental period.

In discrete time, frequencies are equivalent modulo $2\pi$. A component with $\Omega=9\pi/4$ is the same sequence as one with $\Omega=\pi/4$. Reduce frequencies before finding periods. Once individual fundamental periods are known, their least common multiple is a period of the sum, unless cancellation creates a smaller one.

Orthogonal harmonics simplify power. If

$$
x(t)=\sum_k a_ke^{jk\omega_0t},
$$

then averaging cross terms over a period removes all terms with different harmonic indices, leaving

$$
P_x=\sum_k|a_k|^2.
$$

For real sinusoids at distinct harmonics, powers add. Two components at the same frequency must first be combined as phasors because their cross term need not average to zero.

## Classification at a glance

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

## Worked example: energy and power of a finite pulse

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

## Worked example: periodicity of a discrete-time sinusoid

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

## Worked example: energy of a two-sided exponential

Let

$$
x(t)=Ae^{-a|t|},
\qquad a>0.
$$

Its squared magnitude is even:

$$
|x(t)|^2=|A|^2e^{-2a|t|}.
$$

Therefore

$$
\begin{aligned}
E_x
&=2|A|^2\int_0^\infty e^{-2at}\,dt\\
&=2|A|^2\left[\frac{-e^{-2at}}{2a}\right]_0^\infty\\
&=\frac{|A|^2}{a}.
\end{aligned}
$$

Since the energy is finite and positive for $A\ne0$, average power is zero. Increasing $a$ shortens the decay and reduces energy in inverse proportion; multiplying $A$ scales energy by $\vert A\vert ^2$.

## Worked example: period and power of a multisine

Consider

$$
x(t)=2+3\cos(4t)+4\sin(6t).
$$

The component periods are

$$
T_1=\frac{2\pi}{4}=\frac{\pi}{2},
\qquad
T_2=\frac{2\pi}{6}=\frac{\pi}{3}.
$$

The smallest common period is $\pi$: it contains two periods of the cosine and three periods of the sine. To compute power, square and average over $[0,\pi]$. Each nonconstant sinusoid has zero mean, its squared mean is $1/2$, and cross terms between distinct harmonics average to zero. Hence

$$
\begin{aligned}
P_x
&=|2|^2+\frac{|3|^2}{2}+\frac{|4|^2}{2}\\
&=4+\frac92+8\\
&=16.5.
\end{aligned}
$$

The total energy is infinite because this positive amount of energy repeats every period. If the sine also had angular frequency $4$, its phase relative to the cosine would matter and the two terms would need to be combined before applying the amplitude-squared rule.

## Edge cases outside the two main classes

A signal can have infinite energy and zero average power. For example, a slowly decaying signal may fail square integrability while its accumulated energy grows sublinearly with observation duration. Such a signal is neither an energy signal nor a positive-power signal.

A signal can also have no average-power limit. One can construct alternating blocks of zeros and ones whose block lengths grow so rapidly that averages along different observation sizes approach different values. Boundedness alone does not guarantee that the limit defining average power exists.

Finite-duration bounded signals are energy signals, but finite duration alone is insufficient if the signal has a non-square-integrable singularity. Likewise, a periodic signal has finite power only when its squared magnitude is integrable or summable over one period.

Random signals are usually classified using expected power or autocorrelation rather than the deterministic limits above. A particular realization may not possess a convenient time average unless ergodic assumptions connect time averages to ensemble averages.

## Classification mistakes

- Calling every sinusoid periodic in discrete time. $e^{j\Omega n}$ is periodic only when $\Omega/(2\pi)$ is rational.
- Reporting average power of an energy signal as a positive number. Finite-energy signals have zero average power.
- Forgetting absolute value squared for complex signals. Use $\vert x\vert ^2$, not $x^2$.
- Averaging a periodic signal over a non-integer piece of a period and treating that as the long-term power.
- Assuming a finite number of nonzero samples has nonzero average power. Its energy may be finite, but its average power is zero.

<div className="see-also">

See also: [Signals and Time Transformations](/physics/signals-systems/signals-time-transformations) · [Fourier Series for Periodic Signals](/physics/signals-systems/fourier-series-periodic-signals) · [Continuous-Time Fourier Transform](/physics/signals-systems/continuous-time-fourier-transform) · [Discrete-Time Fourier Transform](/physics/signals-systems/discrete-time-fourier-transform)

</div>
