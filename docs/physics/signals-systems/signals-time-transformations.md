---
title: Signals and Time Transformations
sidebar_position: 2
---

# Signals and Time Transformations

A signal is a function that carries information through variation. In this course the independent variable is usually time, but the same ideas apply to space, sample index, or any ordered coordinate. A continuous-time signal $x(t)$ is defined for real $t$, while a discrete-time signal $x[n]$ is defined only for integer $n$. The distinction is not cosmetic: continuous-time formulas use integrals and real-valued delays, while discrete-time formulas use sums and integer shifts.

Time transformations are the first language for describing how signals move, stretch, flip, or line up with other signals. They also prepare the ground for convolution, sampling, Fourier analysis, and modulation. When a problem asks for $x(2-t)$ or $x[3n+1]$, it is asking how the input graph or sequence is re-indexed before values are read.

## Definitions

A continuous-time signal is a mapping

$$
x:\mathbb{R}\to\mathbb{C}, \qquad t\mapsto x(t).
$$

A discrete-time signal is a mapping

$$
x:\mathbb{Z}\to\mathbb{C}, \qquad n\mapsto x[n].
$$

Signals may be real-valued or complex-valued. A complex signal can be written as

$$
x(t)=x_R(t)+j x_I(t),
$$

where $j^2=-1$. Its magnitude and phase are

$$
|x(t)|=\sqrt{x_R^2(t)+x_I^2(t)}, \qquad \angle x(t)=\tan^{-1}\frac{x_I(t)}{x_R(t)},
$$

with quadrant handled by an atan2 convention in computation.

The most common elementary continuous-time signals are:

$$
u(t)=
\begin{cases}
1, & t\ge 0,\\
0, & t<0,
\end{cases}
\qquad
\delta(t)
$$

where $u(t)$ is the unit step and $\delta(t)$ is the unit impulse. The impulse is not an ordinary function; it is defined by its sifting property,

$$
\int_{-\infty}^{\infty} x(t)\delta(t-t_0)\,dt=x(t_0).
$$

The analogous discrete-time signals are

$$
u[n]=
\begin{cases}
1, & n\ge 0,\\
0, & n<0,
\end{cases}
\qquad
\delta[n]=
\begin{cases}
1, & n=0,\\
0, & n\ne 0.
\end{cases}
$$

The discrete-time impulse has the exact expansion property

$$
x[n]=\sum_{k=-\infty}^{\infty}x[k]\delta[n-k].
$$

In continuous time, an analogous representation is

$$
x(t)=\int_{-\infty}^{\infty}x(\tau)\delta(t-\tau)\,d\tau.
$$

These two identities are more than notation. They say that a signal can be rebuilt from shifted impulses weighted by its own values, which is the conceptual root of convolution.

A time transformation of a continuous-time signal often has the form

$$
y(t)=x(a t+b).
$$

If $a\gt 0$, the signal is time-scaled by $1/a$ and shifted. If $a\lt 0$, it is also time-reversed. To locate features, solve the equation

$$
\tau=a t+b
$$

for $t$. A feature originally located at $\tau=\tau_0$ appears in $y(t)$ at

$$
t=\frac{\tau_0-b}{a}.
$$

For discrete time,

$$
y[n]=x[a n+b]
$$

is only directly meaningful at integer values of $a n+b$. If $a$ and $b$ are integers, the expression samples the original sequence at integer indices. When $\vert a\vert \gt 1$, values of $x[k]$ are skipped; when $a=-1$, the sequence is reversed; when $b$ changes, the sequence is shifted.

Even and odd parts are useful decompositions:

$$
x_e(t)=\frac{x(t)+x(-t)}{2}, \qquad x_o(t)=\frac{x(t)-x(-t)}{2}.
$$

They satisfy

$$
x(t)=x_e(t)+x_o(t), \qquad x_e(-t)=x_e(t), \qquad x_o(-t)=-x_o(t).
$$

The same formulas hold for $x[n]$.

## Key results

The order of visual operations matters when transforming $x(a t+b)$. A reliable method is to transform the independent variable, not the picture by memory. Set $\tau=a t+b$, map old feature locations $\tau_0$ to new locations $t=(\tau_0-b)/a$, and then copy the old value. This prevents the common left-right confusion caused by expressions such as $x(2-t)$.

The impulse scaling rule in continuous time is

$$
\delta(a t)=\frac{1}{|a|}\delta(t), \qquad a\ne 0.
$$

More generally, if $g(t)$ has simple roots $t_i$,

$$
\delta(g(t))=\sum_i \frac{\delta(t-t_i)}{|g'(t_i)|}.
$$

This rule has no direct counterpart for the discrete-time impulse, because a discrete impulse is an ordinary sequence value rather than a distribution spread over a real axis.

Step and impulse are connected by differentiation and integration:

$$
\frac{d}{dt}u(t)=\delta(t), \qquad \int_{-\infty}^{t}\delta(\tau)\,d\tau=u(t).
$$

In discrete time the corresponding relation is a first difference:

$$
u[n]-u[n-1]=\delta[n].
$$

For complex exponentials, continuous-time and discrete-time signals again differ in an important way:

$$
x(t)=e^{s t}, \qquad x[n]=z^n.
$$

Continuous-time complex exponentials have distinct frequencies for all distinct real $\omega$ in $e^{j\omega t}$. Discrete-time complex exponentials satisfy

$$
e^{j(\omega+2\pi k)n}=e^{j\omega n}
$$

for every integer $k$, so discrete-time frequency is periodic with period $2\pi$.

## Visual

| Operation | Continuous-time form | Effect on feature at $t=t_0$ or $n=n_0$ | Discrete-time caution |
|---|---|---|---|
| Delay | $x(t-t_d)$ | feature moves to $t_0+t_d$ | $x[n-n_d]$ needs integer $n_d$ |
| Advance | $x(t+t_d)$ | feature moves to $t_0-t_d$ | finite stored sequences may lose samples |
| Reversal | $x(-t)$ | feature moves to $-t_0$ | $x[-n]$ reverses around $n=0$ |
| Scaling | $x(a t)$ | feature moves to $t_0/a$ | $x[a n]$ skips samples if $\vert a\vert \gt 1$ |
| Affine transform | $x(a t+b)$ | feature moves to $(t_0-b)/a$ | integer indexing is required |

```mermaid
flowchart TD
  A[Given y(t)=x(a t+b)] --> B[List landmarks of x at tau0]
  B --> C[Solve tau0=a t+b]
  C --> D[Place each landmark at t=(tau0-b)/a]
  D --> E[Copy amplitudes from x]
  E --> F[Connect intervals with correct reversal and scaling]
```

## Worked example 1: transforming a rectangular pulse

Problem: Let

$$
x(t)=
\begin{cases}
2, & -1\le t\le 3,\\
0, & \text{otherwise}.
\end{cases}
$$

Find and describe $y(t)=x(2-t)$.

Method:

1. Introduce the old variable $\tau=2-t$.
2. The nonzero part of $x(\tau)$ occurs when

$$
-1\le \tau\le 3.
$$

3. Substitute $\tau=2-t$:

$$
-1\le 2-t\le 3.
$$

4. Solve both sides carefully. From $-1\le 2-t$,

$$
-3\le -t \quad \Rightarrow \quad t\le 3.
$$

From $2-t\le 3$,

$$
-t\le 1 \quad \Rightarrow \quad t\ge -1.
$$

5. Combine the inequalities:

$$
-1\le t\le 3.
$$

Therefore

$$
y(t)=
\begin{cases}
2, & -1\le t\le 3,\\
0, & \text{otherwise}.
\end{cases}
$$

Check: The endpoints of the original pulse are $\tau=-1$ and $\tau=3$. They map to

$$
t=\frac{\tau-2}{-1}=2-\tau.
$$

So $\tau=-1$ maps to $t=3$, and $\tau=3$ maps to $t=-1$. The interval is reversed but has the same endpoints. Since the pulse is constant over that interval, the reversal is not visually obvious. A nonconstant ramp would show the flip.

## Worked example 2: decomposing a sequence into shifted impulses

Problem: Write the finite sequence

$$
x[-1]=4,\qquad x[0]=-2,\qquad x[2]=3,
$$

with all other samples equal to zero, as a sum of shifted impulses.

Method:

1. Start from the discrete-time expansion

$$
x[n]=\sum_{k=-\infty}^{\infty}x[k]\delta[n-k].
$$

2. Keep only the nonzero samples:

$$
x[n]=x[-1]\delta[n-(-1)]+x[0]\delta[n-0]+x[2]\delta[n-2].
$$

3. Substitute the sample values:

$$
x[n]=4\delta[n+1]-2\delta[n]+3\delta[n-2].
$$

Check each index:

- At $n=-1$, $\delta[0]=1$ in the first term and the others are zero, so $x[-1]=4$.
- At $n=0$, the middle term gives $-2$.
- At $n=2$, the last term gives $3$.
- At all other integer $n$, every impulse term is zero.

The answer is

$$
x[n]=4\delta[n+1]-2\delta[n]+3\delta[n-2].
$$

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

def x_ct(t):
    return np.where((-1 <= t) & (t <= 3), 2.0, 0.0)

t = np.linspace(-4, 6, 1001)
y = x_ct(2 - t)

n = np.arange(-4, 5)
x_dt = np.zeros_like(n, dtype=float)
x_dt[n == -1] = 4
x_dt[n == 0] = -2
x_dt[n == 2] = 3

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].plot(t, y)
ax[0].set_title("y(t)=x(2-t)")
ax[0].grid(True)

ax[1].stem(n, x_dt)
ax[1].set_title("Discrete impulse expansion samples")
ax[1].grid(True)
plt.tight_layout()
plt.show()
```

## Common pitfalls

- Shifting in the wrong direction. $x(t-t_0)$ is delayed by $t_0$, while $x(t+t_0)$ is advanced by $t_0$.
- Reversing before locating the new origin. For $x(a t+b)$, solve $\tau=a t+b$ rather than relying on a memorized picture operation.
- Treating $\delta(t)$ as a tall narrow ordinary function in algebra. The continuous-time impulse is defined by integration behavior.
- Forgetting that $x[2n]$ is not a compressed version containing every sample. It reads only even-indexed samples of $x[n]$.
- Assuming discrete-time frequencies are unique. Frequencies separated by $2\pi$ produce the same sequence.

## Connections

- [Periodicity, Energy, and Power](/physics/signals-systems/periodicity-energy-power)
- [System Properties](/physics/signals-systems/system-properties)
- [LTI Systems and Convolution](/physics/signals-systems/lti-systems-convolution)
- [Discrete-Time Fourier Transform](/physics/signals-systems/discrete-time-fourier-transform)
