---
title: Continuous Random Variables and Uniform Laws
sidebar_position: 8
---

# Continuous Random Variables and Uniform Laws

Continuous random variables replace probability masses at individual points with probability densities spread across intervals. The conceptual shift is important: for a continuous variable, a single exact value usually has probability zero, even though intervals have positive probability. This is not a paradox; density is not probability, but probability per unit length.

![Several exponential density curves are plotted for different rates.](https://commons.wikimedia.org/wiki/Special:FilePath/Exponential_pdf.svg)

*Figure: Exponential distributions model waiting times in memoryless processes. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Exponential_pdf.svg), Skbkekas, CC BY 3.0.*

The MIT lectures first introduce general continuous random variables and then use the uniform distribution as the simplest example. Uniform random variables also explain percentiles, random arrival times modulo a schedule, and the idea that a probability law can be invariant under translations on an interval. They provide the cleanest bridge from finite equally likely outcomes to densities.

## Definitions

A random variable $X$ is **continuous with density** $f_X$ if

$$
P(X\in A)=\int_A f_X(x)\,dx
$$

for suitable sets $A$. The density must satisfy

$$
f_X(x)\ge0,
\qquad
\int_{-\infty}^{\infty}f_X(x)\,dx=1.
$$

The **cumulative distribution function** is

$$
F_X(a)=P(X\le a)=\int_{-\infty}^{a}f_X(x)\,dx.
$$

If $F_X$ is differentiable at $a$, then

$$
F_X'(a)=f_X(a).
$$

The expectation of a continuous random variable is

$$
E[X]=\int_{-\infty}^{\infty}x f_X(x)\,dx,
$$

when the integral is well-defined. More generally,

$$
E[g(X)]=\int_{-\infty}^{\infty}g(x)f_X(x)\,dx.
$$

The variance is

$$
\operatorname{Var}(X)=E[X^2]-(E[X])^2.
$$

A random variable is **uniform on $[\alpha,\beta]$** if

$$
f_X(x)=
\begin{cases}
\dfrac{1}{\beta-\alpha},& \alpha\le x\le \beta,\\
0,& \text{otherwise}.
\end{cases}
$$

## Key results

For $X\sim\operatorname{Uniform}(0,1)$,

$$
F_X(a)=
\begin{cases}
0,&a<0,\\
a,&0\le a\le1,\\
1,&a>1.
\end{cases}
$$

The mean is

$$
E[X]=\int_0^1 x\,dx=\frac12.
$$

The second moment is

$$
E[X^2]=\int_0^1 x^2\,dx=\frac13.
$$

Therefore

$$
\operatorname{Var}(X)=\frac13-\left(\frac12\right)^2=\frac1{12}.
$$

If $Y\sim\operatorname{Uniform}(0,1)$ and

$$
X=\alpha+(\beta-\alpha)Y,
$$

then $X\sim\operatorname{Uniform}(\alpha,\beta)$. Hence

$$
E[X]=\alpha+(\beta-\alpha)E[Y]
=\frac{\alpha+\beta}{2},
$$

and

$$
\operatorname{Var}(X)=(\beta-\alpha)^2\operatorname{Var}(Y)
=\frac{(\beta-\alpha)^2}{12}.
$$

For continuous random variables,

$$
P(X=a)=\int_a^a f_X(x)\,dx=0
$$

for every fixed point $a$. This does not imply that impossible events are the only events with probability zero; singletons have zero length, so density gives them zero probability.

The density-to-probability rule should always be read as an area rule. If $f_X$ is large near a point, values near that point are comparatively likely, but the probability of the exact point remains zero. For a small interval $[a,a+h]$, one has the approximation

$$
P(a\le X\le a+h)\approx f_X(a)h
$$

when $f_X$ is continuous and $h$ is small. This is the continuous analogue of a probability mass, but it only becomes a probability after multiplying by an interval length.

The CDF remains meaningful for every random variable, discrete or continuous. For continuous variables with a density, the CDF is usually smoother; for discrete variables, it jumps at atoms. This distinction matters when reading graphs. A jump of size $p$ at $a$ means $P(X=a)=p$. A continuous CDF has no such jump at a point.

Uniform distributions are invariant under translations within the interval in the sense that equal-length subintervals have equal probability. If $X\sim U(\alpha,\beta)$ and $[\ell_1,r_1]$, $[\ell_2,r_2]$ are both inside $[\alpha,\beta]$ with the same length, then the two intervals have the same probability. This property is what people usually mean informally by "all locations are equally likely".

Percentiles are a major reason uniform random variables appear everywhere. If $F$ is a continuous strictly increasing CDF and $X$ has that CDF, then $F(X)$ is uniform on $[0,1]$. Conversely, if $U$ is uniform on $[0,1]$, then $F^{-1}(U)$ has CDF $F$. The lectures use this intuition when discussing percentiles of a randomly selected person: the height itself is not uniform, but the percentile rank is approximately uniform.

For expectations, the continuum formulas mirror the discrete ones. Replace sums by integrals and mass functions by densities. The same algebraic properties hold when integrals exist: linearity of expectation, the formula $\operatorname{Var}(X)=E[X^2]-(E[X])^2$, and the transformation rule $E[g(X)]=\int g(x)f_X(x)\,dx$.

## Visual

```text
Uniform density on [alpha, beta]

height = 1/(beta-alpha)

        +--------------------+
        |                    |
        |                    |
--------+--------------------+--------
      alpha                beta

area of rectangle = base * height = (beta-alpha)/(beta-alpha) = 1
```

| Uniform law | Density | Mean | Variance | CDF inside interval |
|---|---|---:|---:|---|
| $U(0,1)$ | $1$ on $[0,1]$ | $1/2$ | $1/12$ | $F(a)=a$ |
| $U(\alpha,\beta)$ | $1/(\beta-\alpha)$ on $[\alpha,\beta]$ | $(\alpha+\beta)/2$ | $(\beta-\alpha)^2/12$ | $(a-\alpha)/(\beta-\alpha)$ |

The rectangle picture is more than a mnemonic. It explains normalization, interval probabilities, and scaling at the same time. If the base interval becomes twice as long, the height must become half as large so the total area stays $1$. This is why stretching a uniform random variable spreads probability out rather than creating more probability. It also explains why the CDF inside the interval is linear: as the endpoint $a$ moves to the right, the accumulated area grows at a constant rate.

Uniform models should still be justified from the story. Arriving at a train platform at a "random time" gives a uniform wait modulo a fixed schedule only if arrivals are not synchronized with the schedule and the train spacing is deterministic. If trains themselves arrive randomly according to a Poisson process, the waiting-time distribution is exponential, not uniform. The same word "random" can therefore lead to different continuous laws depending on the mechanism.

One last check is dimensional: density has units inverse to the variable. If $X$ is measured in hours, $f_X(x)$ is per hour; multiplying by an interval length in hours gives a unitless probability. This helps explain why density values themselves are not probabilities.

## Worked example 1: interval probabilities under a density

Problem: Let $X$ be uniform on $[0,2]$. Compute $P(X\lt 3/2)$, $P(X=3/2)$, and $P(1/2\lt X\lt 3/2)$.

Method:

1. The density is

$$
f_X(x)=\frac12,\qquad 0\le x\le2.
$$

2. For $P(X\lt 3/2)$, integrate:

$$
P(X<3/2)=\int_0^{3/2}\frac12\,dx
=\frac12\cdot\frac32
=\frac34.
$$

3. For a single point,

$$
P(X=3/2)=\int_{3/2}^{3/2}\frac12\,dx=0.
$$

4. For the interval:

$$
P(1/2<X<3/2)=\int_{1/2}^{3/2}\frac12\,dx.
$$

5. The interval length is $1$, so

$$
P(1/2<X<3/2)=\frac12.
$$

Checked answer: all probabilities are interval length divided by total length $2$, except the single point, which has length $0$.

## Worked example 2: transforming a standard uniform variable

Problem: Let $Y\sim U(0,1)$ and define $X=10+6Y$. Find the distribution, mean, variance, and $P(12\le X\le 15)$.

Method:

1. Since $X=10+6Y$, the minimum value is $10$ and the maximum is $16$.
2. Therefore

$$
X\sim U(10,16).
$$

3. The mean is

$$
E[X]=\frac{10+16}{2}=13.
$$

4. The variance is

$$
\operatorname{Var}(X)=\frac{(16-10)^2}{12}
=\frac{36}{12}
=3.
$$

5. The probability of $12\le X\le15$ is interval length over total length:

$$
P(12\le X\le15)=\frac{15-12}{16-10}
=\frac36
=\frac12.
$$

Checked answer: using $Y$, the event $12\le10+6Y\le15$ is

$$
\frac{2}{6}\le Y\le\frac{5}{6},
$$

whose probability is $5/6-1/3=1/2$.

## Code

```python
def uniform_cdf(a, left=0.0, right=1.0):
    if a <= left:
        return 0.0
    if a >= right:
        return 1.0
    return (a - left) / (right - left)

def uniform_interval_prob(a, b, left=0.0, right=1.0):
    return max(0.0, uniform_cdf(b, left, right) - uniform_cdf(a, left, right))

print("P(X < 1.5) for U(0,2):", uniform_cdf(1.5, 0, 2))
print("P(0.5 < X < 1.5) for U(0,2):", uniform_interval_prob(0.5, 1.5, 0, 2))

left, right = 10, 16
mean = (left + right) / 2
variance = (right - left) ** 2 / 12
print("U(10,16) mean and variance:", mean, variance)
```

## Common pitfalls

- Treating a density value as a probability. A density can exceed $1$; probabilities are areas under the density.
- Forgetting that $P(X=a)=0$ for a continuous density, even when $a$ is a very typical value.
- Using strict versus non-strict inequalities as if they matter for continuous variables. They do not change probabilities when endpoints are single points.
- Failing to rescale variance by the square of the stretch factor. If $X=\alpha+cY$, then variance is multiplied by $c^2$.
- Assuming every subset of $[0,1]$ behaves nicely under uniform probability. The lectures mention measurable-set subtleties; ordinary probability computations stay with measurable events.

## Connections

- [Discrete random variables, expectation, and variance](/math/probability-and-random-variables/discrete-random-variables-expectation-variance)
- [Normal, exponential, gamma, beta, and Cauchy laws](/math/probability-and-random-variables/normal-exponential-gamma-beta-cauchy)
- [Joint distributions, transformations, and independence](/math/probability-and-random-variables/joint-distributions-transformations-independence)
- [Sums, convolutions, and order statistics](/math/probability-and-random-variables/sums-convolutions-order-statistics)
- [Common continuous distributions](/math/probability/common-continuous-distributions)
