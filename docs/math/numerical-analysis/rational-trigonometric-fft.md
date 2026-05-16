---
title: Rational Trigonometric Approximation and FFT
sidebar_position: 20
---

# Rational Trigonometric Approximation and FFT

Polynomial approximation is not the only useful approximation model. Rational functions can represent poles, saturation, and sharp transitions with lower degree than polynomials. Trigonometric approximations represent periodic behavior, and the fast Fourier transform makes them computationally practical for large data sets.

This page connects approximation theory with algorithms. A rational approximant changes the function class; a trigonometric approximant changes the basis; the FFT changes the cost of computing coefficients. All three are used in scientific computing, signal processing, spectral methods, and data analysis.

## Definitions

A rational approximation has the form

$$
R(x)=\frac{P_m(x)}{Q_n(x)},
$$

where $P_m$ and $Q_n$ are polynomials and $Q_n(x)\ne 0$ on the interval of interest. Pade approximants are rational functions whose Taylor series matches a target function to high order near an expansion point.

A trigonometric polynomial of degree $N$ can be written as

$$
T_N(x)=a_0+\sum_{k=1}^{N}\left(a_k\cos(kx)+b_k\sin(kx)\right).
$$

For complex notation, the discrete Fourier transform (DFT) of data $x_0,\ldots,x_{n-1}$ is

$$
X_k=\sum_{j=0}^{n-1}x_j e^{-2\pi i jk/n},
\qquad k=0,1,\ldots,n-1.
$$

The inverse transform is

$$
x_j=\frac1n\sum_{k=0}^{n-1}X_k e^{2\pi i jk/n}.
$$

## Key results

Rational approximations can outperform polynomials when the target has nearby singularities or behavior that resembles a quotient. For example, a low-order rational function can approximate exponential or logarithmic behavior well over a wider interval than a same-degree polynomial, but poles in the denominator must be monitored carefully.

The DFT converts between sample values and frequency coefficients. Direct computation costs $O(n^2)$ complex operations. The FFT reduces the cost to $O(n\log n)$ when $n$ has suitable factors, especially powers of two. The Cooley-Tukey idea splits even and odd indexed samples, recursively transforms the two halves, and combines them with twiddle factors.

Sampling introduces aliasing. Frequencies above the Nyquist limit can appear as lower frequencies in sampled data. Therefore trigonometric approximation is inseparable from sampling rate, periodic extension, and windowing. A spectral method can be extremely accurate for smooth periodic functions and disappointing for nonsmooth or nonperiodic data.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For rational and trigonometric approximation with FFT, the input record should include the approximation class, sampling rate, interval mapping, and periodicity assumptions. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include coefficient decay, reconstruction error, denominator checks, and aliasing diagnostics. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually direct DFT cost, FFT cost, and evaluation of rational denominators. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: poles in the interval, endpoint jumps, and interpreting aliased frequencies as real features. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

A final verification step is to reconstruct from the computed coefficients and compare against the original samples or target function. For rational approximations, evaluate the denominator on a fine grid before trusting the quotient. For Fourier approximations, plot or inspect the magnitude of high-frequency coefficients; slow decay usually warns about nonsmoothness, endpoint jumps, or insufficient sampling.
 Always state whether coefficients use normalized or unnormalized DFT conventions, since scaling differs across libraries.

## Visual

```mermaid
graph TD
  A[Sampled data x_j] --> B[DFT]
  B --> C[Frequency coefficients X_k]
  C --> D{Need speed?}
  D -->|small n| E[Direct O(n^2)]
  D -->|large n| F[FFT O(n log n)]
  F --> G[Filter, analyze, or reconstruct]
  E --> G
```

| Approximation | Basis or form | Strength | Risk |
|---|---|---|---|
| Polynomial | powers or orthogonal polynomials | smooth nonperiodic functions | high-degree oscillation |
| Rational | quotient $P/Q$ | poles and sharp transitions | denominator zeros |
| Trigonometric | sine, cosine, complex exponentials | periodic smooth data | aliasing and endpoint jumps |
| FFT | algorithm for DFT | fast coefficient computation | assumes sampled periodic structure |

## Worked example 1: a simple Pade approximant

**Problem.** Show that

$$
R(x)=\frac{1+x/2}{1-x/2}
$$

matches $e^x$ through the $x^2$ term in its Taylor series.

**Method.** Expand the denominator as a geometric series.

1. For small $x$,

$$
\frac{1}{1-x/2}=1+\frac{x}{2}+\frac{x^2}{4}+O(x^3).
$$

2. Multiply by $1+x/2$:

$$
R(x)=\left(1+\frac{x}{2}\right)\left(1+\frac{x}{2}+\frac{x^2}{4}+O(x^3)\right).
$$

3. Collect terms through $x^2$:

$$
R(x)=1+x+\frac{x^2}{2}+O(x^3).
$$

4. The Taylor series for $e^x$ is

$$
e^x=1+x+\frac{x^2}{2}+O(x^3).
$$

**Checked answer.** The rational function agrees with $e^x$ through degree two. At $x=0.1$, it gives $1.105263\ldots$, while $e^{0.1}=1.105170\ldots$.

## Worked example 2: four-point DFT

**Problem.** Compute the DFT of

$$
x=[1,0,-1,0].
$$

**Method.** Since only $x_0$ and $x_2$ are nonzero,

$$
X_k=1- e^{-2\pi i(2)k/4}=1-e^{-\pi i k}.
$$

1. Use $e^{-\pi i k}=(-1)^k$.

2. Therefore

$$
X_k=1-(-1)^k.
$$

3. For even $k$, $X_k=0$. For odd $k$, $X_k=2$.

4. Thus

$$
X=[0,2,0,2].
$$

**Checked answer.** The nonzero coefficients occur at the odd frequency indices, matching the alternating structure of the data.

## Code

```python
import cmath
import numpy as np

def fft_recursive(x):
    x = list(map(complex, x))
    n = len(x)
    if n == 1:
        return x
    if n % 2:
        raise ValueError("recursive radix-2 FFT requires even length")
    even = fft_recursive(x[0::2])
    odd = fft_recursive(x[1::2])
    out = [0j] * n
    for k in range(n // 2):
        twiddle = cmath.exp(-2j * cmath.pi * k / n) * odd[k]
        out[k] = even[k] + twiddle
        out[k + n // 2] = even[k] - twiddle
    return out

def pade_exp_11(x):
    return (1.0 + 0.5 * x) / (1.0 - 0.5 * x)

data = [1.0, 0.0, -1.0, 0.0]
print(fft_recursive(data))
print(np.fft.fft(data))
print(pade_exp_11(0.1), np.exp(0.1))
```

## Common pitfalls

- Using rational approximations without checking for denominator zeros on the interval.
- Treating FFT coefficients as meaningful frequencies without knowing the sampling rate.
- Forgetting that the DFT assumes periodic extension of the sampled data.
- Ignoring aliasing when sampling a high-frequency signal.
- Comparing an $O(n\log n)$ FFT with a direct DFT at very small $n$ where overhead can dominate.

## Connections

- [least squares and Chebyshev approximation](/math/numerical-analysis/least-squares-chebyshev-approximation)
- [interpolation Lagrange and Neville method](/math/numerical-analysis/interpolation-lagrange-neville)
- [finite difference methods for PDEs](/math/numerical-analysis/finite-difference-pdes)
- [floating point conditioning and stability](/math/numerical-analysis/floating-point-conditioning-stability)
