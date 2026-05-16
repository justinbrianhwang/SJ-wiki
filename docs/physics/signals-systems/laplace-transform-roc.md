---
title: Laplace Transform and ROC
sidebar_position: 10
---

# Laplace Transform and ROC

The Laplace transform generalizes the continuous-time Fourier transform by using the complex variable $s=\sigma+j\omega$. The extra real part $\sigma$ controls exponential weighting. This makes the transform useful for signals that do not have ordinary Fourier transforms and for solving differential equations with growth, decay, and initial conditions.

For systems, the Laplace transform exposes poles, zeros, stability, causality, and transient behavior. The region of convergence is not optional. The algebraic expression $X(s)$ alone may correspond to different time-domain signals depending on where the transform converges.

## Definitions

The bilateral Laplace transform of $x(t)$ is

$$
X(s)=\int_{-\infty}^{\infty}x(t)e^{-s t}\,dt,
\qquad s=\sigma+j\omega.
$$

The unilateral Laplace transform is

$$
X_+(s)=\int_{0^-}^{\infty}x(t)e^{-s t}\,dt.
$$

The bilateral form is used most often for signal and LTI system properties. The unilateral form is useful for solving differential equations with initial conditions.

The region of convergence, or ROC, is the set of complex $s$ values for which the integral converges. For rational transforms, the ROC is a vertical strip or half-plane bounded by poles. The ROC never contains poles.

The continuous-time Fourier transform is the bilateral Laplace transform evaluated on the imaginary axis when the $j\omega$ axis lies in the ROC:

$$
X(j\omega)=X(s)\bigg|_{s=j\omega}.
$$

Important transform pairs include

$$
e^{-a t}u(t)\leftrightarrow \frac{1}{s+a},
\qquad
\operatorname{Re}(s)>-a,
$$

and

$$
-e^{-a t}u(-t)\leftrightarrow \frac{1}{s+a},
\qquad
\operatorname{Re}(s)<-a.
$$

The same algebraic expression appears, but the time-domain signals are different because the ROCs are different.

For an LTI system with impulse response $h(t)$, the system function is

$$
H(s)=\mathcal{L}\{h(t)\}.
$$

For input $x(t)$ and output $y(t)=x*h$, the bilateral transforms satisfy

$$
Y(s)=X(s)H(s),
$$

with an ROC at least including the intersection of the individual ROCs, except for possible pole-zero cancellations.

## Key results

Linearity:

$$
a x_1(t)+b x_2(t)\leftrightarrow aX_1(s)+bX_2(s).
$$

Time shifting:

$$
x(t-t_0)\leftrightarrow e^{-s t_0}X(s),
$$

with ROC unchanged for finite shifts, apart from impulse-like edge cases.

Multiplication by an exponential:

$$
e^{s_0t}x(t)\leftrightarrow X(s-s_0).
$$

Differentiation:

$$
\frac{d}{dt}x(t)\leftrightarrow sX(s)
$$

for the bilateral transform when boundary terms vanish in the transform sense. For the unilateral transform, initial-condition terms appear.

Convolution:

$$
x(t)*h(t)\leftrightarrow X(s)H(s).
$$

For rational Laplace transforms, poles determine possible exponential modes. If

$$
H(s)=\frac{B(s)}{A(s)},
$$

then roots of $A(s)$ are poles and roots of $B(s)$ are zeros. Poles are especially important because they control natural response terms such as $e^{p t}$, where $p$ is a pole.

For a causal rational LTI system, the ROC is to the right of the rightmost pole. For an anti-causal left-sided system, the ROC is to the left of the leftmost pole. For a two-sided signal, the ROC is a vertical strip between poles.

BIBO stability for a continuous-time LTI system requires the impulse response to be absolutely integrable. In Laplace terms, for rational systems, stability is equivalent to the $j\omega$ axis lying in the ROC. If the system is both causal and rational, this means all poles must lie strictly in the left half-plane:

$$
\operatorname{Re}(p_i)<0.
$$

The ROC is also a memory of time support. A right-sided signal grows or decays toward $+\infty$, so convergence is controlled by making $e^{-s t}$ decay fast enough as $t\to+\infty$. This produces a right half-plane ROC. A left-sided signal is controlled as $t\to-\infty$, producing a left half-plane ROC. A two-sided signal must satisfy both conditions, producing a vertical strip. This support interpretation is often faster than redoing the integral from scratch.

Partial fractions are the standard inverse method for rational transforms. After factoring the denominator, write $X(s)$ as a sum of terms such as $A/(s+a)$. Then use the ROC to decide whether each term is right-sided or left-sided. When the ROC is to the right of all poles, all exponential terms are right-sided. When the ROC is to the left of all poles, all are left-sided. When the ROC lies between poles, terms associated with poles left of the ROC are right-sided and terms associated with poles right of the ROC are left-sided.

For differential equations, the unilateral Laplace transform includes initial conditions explicitly. That makes it ideal for solving initial-value problems. The bilateral transform is cleaner for system functions, impulse responses, and frequency-response connections. Mixing the two conventions is possible, but the boundary terms must be handled deliberately.

Pole locations also give qualitative time behavior before any inverse transform is computed. A pole far to the left decays quickly in a causal system. A pole close to the imaginary axis decays slowly and creates a long transient. Complex-conjugate poles create damped oscillations when their real parts are negative. These interpretations are why pole-zero plots are used so often in system design.

Repeated poles create polynomial factors multiplying exponentials in time. For example, a second-order pole at $s=-a$ produces terms involving $e^{-at}$ and $t e^{-at}$ for a right-sided signal. The exponential still controls asymptotic decay or growth, but the polynomial factor changes transient shape.

## Visual

```text
s-plane ROC examples

left-sided:          two-sided:             right-sided:

<==== ROC | pole     pole |==== ROC ====| pole     pole | ROC ====>
          a               a             b               a

The ROC is a vertical half-plane or strip and never includes poles.
```

| Signal type | Pole pattern | ROC shape | Causality clue |
|---|---|---|---|
| Right-sided exponential | pole at $-a$ | $\operatorname{Re}(s)\gt -a$ | causal candidate |
| Left-sided exponential | pole at $-a$ | $\operatorname{Re}(s)\lt -a$ | anti-causal candidate |
| Two-sided sum | multiple poles | strip between poles | noncausal |
| Stable rational LTI | poles not on ROC axis | ROC includes $j\omega$ axis | depends on ROC |
| Causal stable rational LTI | poles in left half-plane | right of rightmost pole and includes $j\omega$ | causal and stable |

## Worked example 1: same expression, different ROC

Problem: Find the inverse Laplace transform possibilities for

$$
X(s)=\frac{1}{s+2}.
$$

Method:

1. Identify the pole:

$$
s=-2.
$$

2. If the ROC is

$$
\operatorname{Re}(s)>-2,
$$

the signal is right-sided. Use the standard pair:

$$
e^{-2t}u(t)\leftrightarrow \frac{1}{s+2}.
$$

3. If the ROC is

$$
\operatorname{Re}(s)<-2,
$$

the signal is left-sided. The matching pair is

$$
-e^{-2t}u(-t)\leftrightarrow \frac{1}{s+2}.
$$

4. Check the left-sided case directly:

$$
\int_{-\infty}^{0}-e^{-2t}e^{-s t}\,dt
=-\int_{-\infty}^{0}e^{-(s+2)t}\,dt.
$$

For convergence as $t\to -\infty$, need $\operatorname{Re}(s+2)\lt 0$, so $\operatorname{Re}(s)\lt -2$. The integral is

$$
-\left[\frac{e^{-(s+2)t}}{-(s+2)}\right]_{-\infty}^{0}
=\frac{1}{s+2}.
$$

Checked answer: The algebraic expression is incomplete without the ROC. The two possible inverse transforms are $e^{-2t}u(t)$ for ROC right of $-2$, and $-e^{-2t}u(-t)$ for ROC left of $-2$.

## Worked example 2: stability and causality from poles

Problem: A causal LTI system has system function

$$
H(s)=\frac{s+1}{(s+2)(s-3)}.
$$

Determine whether it is BIBO stable.

Method:

1. Identify the poles:

$$
s=-2,\qquad s=3.
$$

2. Because the system is causal and rational, the ROC is to the right of the rightmost pole:

$$
\operatorname{Re}(s)>3.
$$

3. BIBO stability requires the $j\omega$ axis, where $\operatorname{Re}(s)=0$, to lie in the ROC.

4. The ROC $\operatorname{Re}(s)\gt 3$ does not include $\operatorname{Re}(s)=0$.

Checked answer: The system is not BIBO stable. The pole at $s=3$ corresponds to a growing right-sided exponential mode $e^{3t}u(t)$.

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

poles = np.array([-2, 3], dtype=float)
zeros = np.array([-1], dtype=float)

omega = np.linspace(-20, 20, 2000)
s = 1j * omega
H_jw = (s + 1) / ((s + 2) * (s - 3))

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].plot(np.real(zeros), np.imag(zeros), "ob", label="zero")
ax[0].plot(np.real(poles), np.imag(poles), "xr", label="poles")
ax[0].axvline(0, color="k", linewidth=0.8)
ax[0].set_title("Poles, zero, and jomega axis")
ax[0].legend()
ax[0].grid(True)

ax[1].plot(omega, np.abs(H_jw))
ax[1].set_title("Formal H(j omega)")
ax[1].set_xlabel("omega")
ax[1].grid(True)
plt.tight_layout()
plt.show()
```

## Common pitfalls

- Omitting the ROC. A rational expression without its ROC does not uniquely identify a signal.
- Assuming the Fourier transform exists just because $X(s)$ can be written. The $j\omega$ axis must lie in the ROC.
- Calling a causal rational system stable when it has a right-half-plane pole.
- Confusing unilateral and bilateral derivative properties. Initial-condition terms belong to the unilateral transform.
- Treating zeros as if they determine stability. Poles and ROC determine the natural modes and stability condition.

## Connections

- [Continuous-Time Fourier Transform](/physics/signals-systems/continuous-time-fourier-transform)
- [LTI Systems and Convolution](/physics/signals-systems/lti-systems-convolution)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
- [State-Space Introduction](/physics/signals-systems/state-space-introduction)
