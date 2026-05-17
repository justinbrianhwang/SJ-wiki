---
title: Z-Transform and ROC
sidebar_position: 11
---

# Z-Transform and ROC

The $z$-transform is the discrete-time counterpart of the Laplace transform. It represents sequences using the complex variable $z=re^{j\Omega}$ and provides a natural language for recursive difference equations, digital filters, poles, zeros, stability, and causality. The DTFT is obtained by evaluating the $z$-transform on the unit circle when that circle lies in the region of convergence.

As with the Laplace transform, the region of convergence is part of the answer. The same rational expression can describe a right-sided sequence, a left-sided sequence, or a two-sided sequence depending on the ROC. In digital signal processing, many system questions reduce to locating poles relative to the unit circle.

## Definitions

The bilateral $z$-transform of a sequence $x[n]$ is

$$
X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}.
$$

The unilateral $z$-transform is

$$
X_+(z)=\sum_{n=0}^{\infty}x[n]z^{-n}.
$$

The bilateral transform is used for signal and LTI system properties. The unilateral transform is useful for solving difference equations with initial conditions.

The region of convergence, or ROC, is the set of $z$ values for which the sum converges. For rational transforms, the ROC is an annulus centered at the origin:

$$
r_1<|z|<r_2,
$$

possibly with $r_1=0$ or $r_2=\infty$. The ROC never includes poles.

The DTFT is obtained on the unit circle if $\vert z\vert =1$ lies in the ROC:

$$
X(e^{j\Omega})=X(z)\bigg|_{z=e^{j\Omega}}.
$$

Important transform pairs include, for $\vert z\vert \gt \vert a\vert $,

$$
a^n u[n]\leftrightarrow \frac{1}{1-a z^{-1}},
$$

and, for $\vert z\vert \lt \vert a\vert $,

$$
-a^n u[-n-1]\leftrightarrow \frac{1}{1-a z^{-1}}.
$$

Again, the expression is identical but the ROC and sequence are different.

For an LTI system with impulse response $h[n]$, the system function is

$$
H(z)=\sum_{n=-\infty}^{\infty}h[n]z^{-n}.
$$

If $y[n]=x[n]*h[n]$, then

$$
Y(z)=X(z)H(z),
$$

with ROC at least including the intersection of the ROCs, except for possible pole-zero cancellations.

## Key results

Linearity:

$$
a x_1[n]+b x_2[n]\leftrightarrow aX_1(z)+bX_2(z).
$$

Time shifting:

$$
x[n-n_0]\leftrightarrow z^{-n_0}X(z),
$$

with possible ROC changes at $0$ or $\infty$ depending on finite-length terms.

Multiplication by $a^n$:

$$
a^n x[n]\leftrightarrow X\left(\frac{z}{a}\right).
$$

Time reversal:

$$
x[-n]\leftrightarrow X(z^{-1}).
$$

Convolution:

$$
x[n]*h[n]\leftrightarrow X(z)H(z).
$$

For rational $H(z)$,

$$
H(z)=\frac{B(z)}{A(z)}.
$$

Poles are values of $z$ where $H(z)$ becomes unbounded; zeros are values where it becomes zero. In digital filters, zeros can create frequency nulls and poles can create resonances or instability.

For a causal rational LTI system, the ROC is outside the outermost pole. For a left-sided anti-causal system, the ROC is inside the innermost pole. For a two-sided sequence, the ROC is an annulus between pole radii.

BIBO stability for a discrete-time LTI system requires absolute summability:

$$
\sum_{n=-\infty}^{\infty}|h[n]|<\infty.
$$

In $z$-transform terms, for rational systems, stability is equivalent to the unit circle being in the ROC. If the system is both causal and rational, then stability is equivalent to all poles lying strictly inside the unit circle:

$$
|p_i|<1.
$$

The frequency response of a stable system is

$$
H(e^{j\Omega})=H(z)\bigg|_{z=e^{j\Omega}}.
$$

This provides a direct bridge from pole-zero diagrams to filter magnitude and phase.

The shape of the ROC follows from powers of $z^{-n}$. For a right-sided sequence, convergence depends on large positive $n$, so the ROC is outside the largest active pole. For a left-sided sequence, convergence depends on large negative $n$, so the ROC is inside the smallest active pole. For a two-sided sequence, both tails must converge, so the ROC is an annulus between pole radii.

Finite-length sequences are special. A finite right-sided sequence has a $z$-transform that is a polynomial in $z^{-1}$, so it has no finite poles except possibly at $z=0$ depending on how the expression is written. Such FIR systems are BIBO stable because their impulse responses are absolutely summable. Recursive IIR systems can be stable too, but only if their pole and ROC conditions satisfy the unit-circle test.

Pole-zero diagrams are qualitative frequency-response tools. A point on the unit circle near a pole usually gives a large magnitude because the denominator is small. A point on the unit circle near a zero usually gives a small magnitude because the numerator is small. Exact zeros on the unit circle create exact frequency nulls.

The $z$ variable also encodes delay naturally. A factor of $z^{-1}$ represents a one-sample delay in a transfer function. This is why digital filters are commonly written as polynomials in $z^{-1}$: the coefficients directly multiply present and delayed samples in a difference equation. Reading powers of $z^{-1}$ as delays helps connect algebraic expressions to block diagrams.

As with the Laplace transform, repeated poles produce polynomial factors in the sequence. A repeated pole at $z=a$ can create terms like $n a^n u[n]$. The pole magnitude still controls exponential decay or growth, while the polynomial factor changes the transient envelope.

## Visual

```mermaid
flowchart TB
  Seq["Discrete-time sequence x(n"]<br/>right-sided, left-sided, two-sided, or finite"] --> ZT["z-transform<br/>X(z)=sum x(n"] z^(-n)"]
  ZT --> Poles["Pole-zero expression<br/>radii and angles in z-plane"]
  ZT --> ROC{"Region of convergence"}

  subgraph Shapes["ROC shapes"]
    direction TB
    Right["right-sided sequence<br/>outside outermost active pole"] --> Causal["causal rational system candidate"]
    Left["left-sided sequence<br/>inside innermost active pole"] --> Anti["anti-causal candidate"]
    Annulus["two-sided sequence<br/>annulus between pole radii"] --> Noncausal["noncausal candidate"]
    FIR["finite-length sequence<br/>entire plane except possible 0 or infinity"] --> FIRStable["FIR stability if absolutely summable"]
  end

  ROC -- "outside radius" --> Right
  ROC -- "inside radius" --> Left
  ROC -- "between radii" --> Annulus
  ROC -- "finite support" --> FIR
  Poles --> Exclude["ROC never crosses a pole"]
  Causal --> DTFT{"unit circle inside ROC?"}
  Anti --> DTFT
  Noncausal --> DTFT
  FIRStable --> DTFT
  DTFT -- "yes" --> Freq["DTFT and H(e^jOmega) exist"]
  DTFT -- "no" --> NoFreq["no ordinary frequency response"]
```

The $z$-transform architecture mirrors the Laplace workflow but uses annular regions in the $z$-plane. The diagram shows how sidedness determines whether the ROC extends outward, inward, or between pole radii, while finite sequences occupy a special FIR branch. The unit-circle test is the discrete-time I/O contract for stability and frequency response.

| Sequence/system type | ROC shape | Stability condition | Causality clue |
|---|---|---|---|
| Right-sided $a^n u[n]$ | $\vert z\vert \gt \vert a\vert $ | stable if $\vert a\vert \lt 1$ | causal candidate |
| Left-sided $-a^n u[-n-1]$ | $\vert z\vert \lt \vert a\vert $ | stable if $\vert a\vert \gt 1$ | anti-causal candidate |
| Two-sided sequence | annulus between poles | unit circle inside annulus | noncausal |
| Causal rational LTI | outside outermost pole | all poles inside unit circle | causal |
| FIR filter | whole plane except maybe $z=0$ | always stable if finite coefficients | causal if right-sided |

## Worked example 1: same rational expression, different sequence

Problem: Interpret

$$
X(z)=\frac{1}{1-\frac{1}{2}z^{-1}}
$$

for two possible ROCs.

Method:

1. Identify the pole. The denominator is zero when

$$
1-\frac{1}{2}z^{-1}=0.
$$

Multiply by $z$:

$$
z-\frac{1}{2}=0,
$$

so the pole is

$$
z=\frac{1}{2}.
$$

2. If the ROC is

$$
|z|>\frac{1}{2},
$$

the sequence is right-sided:

$$
x[n]=\left(\frac{1}{2}\right)^n u[n].
$$

3. If the ROC is

$$
|z|<\frac{1}{2},
$$

the sequence is left-sided:

$$
x[n]=-\left(\frac{1}{2}\right)^n u[-n-1].
$$

4. Check the right-sided case:

$$
\sum_{n=0}^{\infty}\left(\frac{1}{2}\right)^n z^{-n}
=\sum_{n=0}^{\infty}\left(\frac{1}{2}z^{-1}\right)^n
=\frac{1}{1-\frac{1}{2}z^{-1}},
$$

which converges when

$$
\left|\frac{1}{2}z^{-1}\right|<1
\quad \Rightarrow \quad
|z|>\frac{1}{2}.
$$

Checked answer: Both sequences share the same rational expression. The ROC determines whether the sequence is right-sided or left-sided.

## Worked example 2: stability of a causal digital filter

Problem: A causal LTI system has

$$
H(z)=\frac{1}{1-1.2z^{-1}+0.32z^{-2}}.
$$

Determine whether it is stable.

Method:

1. Find the poles by solving

$$
1-1.2z^{-1}+0.32z^{-2}=0.
$$

2. Multiply by $z^2$:

$$
z^2-1.2z+0.32=0.
$$

3. Factor:

$$
z^2-1.2z+0.32=(z-0.8)(z-0.4).
$$

4. The poles are

$$
z=0.8,\qquad z=0.4.
$$

5. Because the system is causal, the ROC is outside the outermost pole:

$$
|z|>0.8.
$$

6. The unit circle $\vert z\vert =1$ lies in this ROC.

Checked answer: The system is BIBO stable. For a causal rational system, the same conclusion follows from the pole magnitudes:

$$
0.8<1,\qquad 0.4<1.
$$

Both poles are inside the unit circle.

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

# H(z)=1/(1 - 1.2 z^-1 + 0.32 z^-2)
den = np.array([1.0, -1.2, 0.32])
poles = np.roots(den)
print("poles:", poles)
print("causal stable:", np.all(np.abs(poles) < 1))

Omega = np.linspace(-np.pi, np.pi, 1000)
z = np.exp(1j * Omega)
H = 1 / (1 - 1.2 * z**-1 + 0.32 * z**-2)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
circle = plt.Circle((0, 0), 1, fill=False, color="gray")
ax[0].add_artist(circle)
ax[0].plot(poles.real, poles.imag, "xr", markersize=10)
ax[0].set_aspect("equal", adjustable="box")
ax[0].set_title("Pole-zero view")
ax[0].grid(True)

ax[1].plot(Omega, np.abs(H))
ax[1].set_title("Frequency response magnitude")
ax[1].grid(True)
plt.tight_layout()
plt.show()
```

## Common pitfalls

- Giving a $z$-transform without its ROC when the inverse sequence is requested.
- Assuming right-sided and causal always mean stable. A causal pole outside the unit circle is unstable.
- Evaluating $H(e^{j\Omega})$ when the unit circle is not in the ROC.
- Forgetting that the ROC of a rational transform cannot include poles.
- Mixing powers of $z$ and $z^{-1}$ when finding poles. Clear denominators before solving.

## Connections

- [Discrete-Time Fourier Transform](/physics/signals-systems/discrete-time-fourier-transform)
- [LTI Systems and Convolution](/physics/signals-systems/lti-systems-convolution)
- [Frequency Response and Filtering](/physics/signals-systems/frequency-response-filtering)
- [State-Space Introduction](/physics/signals-systems/state-space-introduction)
