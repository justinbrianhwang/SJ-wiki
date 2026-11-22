---
title: Probability Distributions in R
sidebar_position: 12
---

# Probability Distributions in R

R uses one naming scheme for most probability distributions. Once the event has been translated into a density, cumulative probability, quantile, or random experiment, the corresponding function name is usually predictable. The hard part is rarely typing `pnorm` or `dbinom`; it is deciding which mathematical quantity the question asks for and checking that R's parameterization matches the model.

## One family, four views

A probability distribution assigns probabilities to possible outcomes of a random variable. For a discrete random variable, the probability mass function is

$$
P(X = x) = f(x).
$$

For a continuous random variable, $f(x)$ is a density. Probability is area under the density, so $P(X=x)=0$ at every individual point even when $f(x)$ is large. In both cases the cumulative distribution function is

$$
F(x) = P(X \le x).
$$

R combines a prefix with a distribution-family root:

| Prefix | Returned quantity | Normal example | Binomial example |
|---|---|---|---|
| `d` | Density or probability mass | `dnorm(x, mean, sd)` | `dbinom(x, size, prob)` |
| `p` | Cumulative probability | `pnorm(q, mean, sd)` | `pbinom(q, size, prob)` |
| `q` | Quantile for a cumulative probability | `qnorm(p, mean, sd)` | `qbinom(p, size, prob)` |
| `r` | Pseudo-random observations | `rnorm(n, mean, sd)` | `rbinom(n, size, prob)` |

The first argument changes meaning with the prefix. A `d` function receives possible values, a `p` function receives cutoffs, a `q` function receives probabilities, and an `r` function receives the number of observations to generate. All are vectorized.

```r
dnorm(c(-1, 0, 1))
pnorm(c(-1, 0, 1))
qnorm(c(0.025, 0.5, 0.975))
rnorm(3)
```

The same scheme covers `unif`, `exp`, `gamma`, `pois`, `t`, `chisq`, `f`, and many other families. It also encourages a useful separation: the distribution states the model, while the prefix states the question asked of that model.

## Translating words into events

Write the event before writing R code. For a discrete count $X$:

| Wording | Event | R form |
|---|---|---|
| exactly 3 | $P(X=3)$ | `d*(3, ...)` |
| at most 3 | $P(X\le3)$ | `p*(3, ...)` |
| fewer than 3 | $P(X\le2)$ | `p*(2, ...)` |
| more than 3 | $P(X\gt 3)$ | `p*(3, ..., lower.tail = FALSE)` |
| at least 3 | $P(X\ge3)=P(X\gt 2)$ | `p*(2, ..., lower.tail = FALSE)` |

The one-unit boundary shift is specific to a discrete support. For continuous $X$, strict and non-strict inequalities have the same probability. An interval comes from CDF subtraction:

$$
P(a < X \le b) = F(b) - F(a).
$$

For discrete variables the same subtraction computes $P(a\lt X\le b)$. If the desired event includes $a$, subtract $F(a-1)$ when the support advances by integer steps.

Tail arguments are preferable to manual subtraction when the requested probability is very small:

```r
pnorm(8, lower.tail = FALSE)
# better numerical route than 1 - pnorm(8)
```

The direct upper-tail calculation avoids losing significant digits when the lower-tail CDF rounds extremely close to one. Most `p` functions also accept `log.p = TRUE`, which returns a log-probability and can prevent underflow in likelihood calculations.

## Worked normal interval: standardize, then subtract

Suppose exam scores are modeled as normal with mean 75 and standard deviation 8. Let $X\sim N(75,8^2)$. The probability of a score between 70 and 90 is

$$
\begin{aligned}
P(70<X<90)
&= F(90)-F(70).
\end{aligned}
$$

The corresponding standardized values are

$$
\begin{aligned}
z_{70} &= \frac{70-75}{8} = -0.625,\\
z_{90} &= \frac{90-75}{8} = 1.875.
\end{aligned}
$$

R can work either on the original scale or on the standard-normal scale:

```r
lower <- pnorm(70, mean = 75, sd = 8)
upper <- pnorm(90, mean = 75, sd = 8)
prob <- upper - lower

c(lower = lower, upper = upper, interval = prob)
#     lower     upper  interval
# 0.2659855 0.9696036 0.7036181

pnorm(1.875) - pnorm(-0.625)
# [1] 0.7036181
```

The two routes agree because standardization transforms $X$ into $Z=(X-75)/8$, which has mean zero and standard deviation one. About 70.4% of the model's area lies in the interval. Calling `dnorm(70, 75, 8)` and `dnorm(90, 75, 8)` would produce density heights at the endpoints; subtracting those heights has no probability interpretation.

Suppose instead the question asks for the cutoff exceeded by 5% of students. If $c$ is that cutoff, then $P(X\le c)=0.95$, so

```r
cutoff <- qnorm(0.95, mean = 75, sd = 8)
cutoff
# [1] 88.15883

pnorm(cutoff, mean = 75, sd = 8)
# [1] 0.95
```

The standard-normal 95th percentile is about $1.644854$; transforming back gives $75+8(1.644854)=88.1588$. The round trip through `pnorm` checks the interpretation.

## Worked binomial count: derive the mass before summing it

A machine independently produces an acceptable part with probability $0.9$. For 12 parts, let $X$ be the number acceptable. Then $X\sim\operatorname{Binomial}(12,0.9)$ and

$$
P(X=k)=\binom{12}{k}(0.9)^k(0.1)^{12-k}.
$$

For exactly ten acceptable parts:

$$
\begin{aligned}
P(X=10)
&= \binom{12}{10}(0.9)^{10}(0.1)^2\\
&= 66(0.3486784401)(0.01)\\
&\approx 0.2301278.
\end{aligned}
$$

`dbinom` evaluates the same mass:

```r
exact_10 <- dbinom(10, size = 12, prob = 0.9)
exact_10
# [1] 0.2301278
```

"At least ten" combines three mutually exclusive outcomes:

$$
\begin{aligned}
P(X\ge10)
&=P(X=10)+P(X=11)+P(X=12)\\
&=0.2301278+0.3765727+0.2824295\\
&\approx0.8891300.
\end{aligned}
$$

There are two equivalent calls:

```r
by_sum <- sum(dbinom(10:12, size = 12, prob = 0.9))
by_tail <- pbinom(9, size = 12, prob = 0.9, lower.tail = FALSE)

c(by_sum = by_sum, by_tail = by_tail)
#    by_sum   by_tail
# 0.8891300 0.8891300
```

The tail call uses 9 because the complement of $X\ge10$ is $X\le9$. Using `pbinom(10, lower.tail = FALSE)` would compute $P(X\gt 10)$ and omit the mass at 10.

Quantiles of discrete distributions need a small qualification. The CDF is a staircase, so it usually has no ordinary inverse. R returns the smallest supported value $x$ whose CDF is at least the requested probability:

$$
Q(p)=\inf\{x:F(x)\ge p\}.
$$

Consequently, `pbinom(qbinom(p, ...), ...)` can exceed `p`; the jump at the returned count crosses the requested level.

### Why the binomial mean and variance have their familiar form

The formulas $E[X]=np$ and $\operatorname{Var}(X)=np(1-p)$ become transparent when the count is written as a sum of indicator variables. Let $I_i=1$ when trial $i$ succeeds and $I_i=0$ otherwise. Then

$$
X=I_1+I_2+\cdots+I_n.
$$

Each indicator has $E[I_i]=p$. Linearity of expectation does not require independence, so

$$
\begin{aligned}
E[X]
&=E[I_1]+\cdots+E[I_n]\\
&=np.
\end{aligned}
$$

For a Bernoulli indicator, $I_i^2=I_i$, giving

$$
\begin{aligned}
\operatorname{Var}(I_i)
&=E[I_i^2]-E[I_i]^2\\
&=p-p^2\\
&=p(1-p).
\end{aligned}
$$

Independence makes the covariance terms zero, so variances add and $\operatorname{Var}(X)=np(1-p)$. With 12 parts and success probability $0.9$, the count has mean $10.8$ and standard deviation $\sqrt{12(0.9)(0.1)}\approx1.039$. An observed count of 10 is less than one standard deviation below the mean, consistent with its sizeable probability mass.

## A Poisson rate must match its interval

Suppose calls arrive according to a Poisson model at an average rate of three per hour. For a 20-minute interval, the mean count is not 3 but

$$
\lambda=3\left(\frac{20}{60}\right)=1.
$$

The probability of at least two calls is

$$
\begin{aligned}
P(X\ge2)
&=1-P(X\le1)\\
&=1-\left(e^{-1}\frac{1^0}{0!}+e^{-1}\frac{1^1}{1!}\right)\\
&=1-2e^{-1}\\
&\approx0.2642411.
\end{aligned}
$$

```r
lambda_20_min <- 3 * 20 / 60
ppois(1, lambda = lambda_20_min, lower.tail = FALSE)
# [1] 0.2642411
```

Rates and exposure units must be reconciled before the distribution call. The same issue appears with events per kilometer, defects per square meter, or failures per machine-day. A correct `ppois` call with a mismatched interval still answers the wrong model.

The Poisson and exponential families describe two views of the same idealized process. Under a homogeneous Poisson process with rate $\lambda$, the count in an interval of length $t$ is Poisson with mean $\lambda t$, while the waiting time to the next event is exponential with rate $\lambda$. For three calls per hour, the probability of waiting more than 20 minutes is

$$
P(T>1/3)=e^{-3(1/3)}=e^{-1}\approx0.3678794.
$$

```r
pexp(1 / 3, rate = 3, lower.tail = FALSE)
# [1] 0.3678794
```

The process assumptions are strong: arrivals must be independent, the rate must be stable over the interval, and simultaneous arrivals must have negligible probability. A daily call-center pattern with a lunch-hour surge violates the constant-rate assumption even if its overall daily mean is estimated accurately.

## Density height and probability area

A continuous density must be nonnegative and integrate to one. It may exceed one at some points; only an area is constrained to be at most one. A uniform distribution on the narrow interval from 0 to 0.1 has density 10 throughout that interval, yet its total area is $10(0.1)=1$.

This distinction matters when drawing curves. The default `dnorm` curve is a geometric representation of density, while a histogram drawn with `freq = FALSE` estimates density on compatible vertical units. A count histogram uses frequency units and cannot be compared directly with a density curve without rescaling.

Numerical integration provides another check on a CDF difference:

```r
area <- integrate(
  dnorm,
  lower = 70,
  upper = 90,
  mean = 75,
  sd = 8
)$value

area
# [1] 0.7036181
```

`integrate` approximates the area under the density, while the earlier CDF subtraction uses a distribution-specific implementation. The CDF call is normally simpler and more accurate for a standard family; integration is useful when working with a custom density or checking a derivation.

## Matching a family to the random experiment

Distribution choice begins with the data-generating story. A binomial variable counts successes in a fixed number of comparable independent trials. A Poisson variable counts events in an exposure interval under a constant-rate idealization. An exponential variable records a nonnegative waiting time with the memoryless property. A normal variable is continuous, symmetric, and supported over the whole real line, even if negative values are implausible for the measured quantity.

Similar-looking histograms do not establish the assumptions. A bounded percentage near zero or one may be poorly represented by a normal model. Counts with variance far larger than their mean often fit a Poisson model badly. Waiting times affected by aging or recovery do not have the exponential model's constant hazard. The `d`, `p`, `q`, and `r` interface evaluates whichever family is requested; it does not diagnose whether that family is defensible.

Approximations should preserve the event boundary. When a binomial count is approximated by a continuous normal variable, a continuity correction assigns each integer count a unit-width interval. Thus $P(X\le 9)$ is approximated with a normal cutoff at $9.5$, while $P(X\ge10)$ uses the upper area beyond $9.5$. Omitting the half-unit shift can matter when the count is not very large.

For the 12-part example, the binomial mean is $10.8$ and standard deviation is about $1.039$. The continuity-corrected normal approximation to $P(X\ge10)$ is

```r
mu <- 12 * 0.9
sigma <- sqrt(12 * 0.9 * 0.1)
pnorm(9.5, mean = mu, sd = sigma, lower.tail = FALSE)
```

This is only a check, not an improvement over the exact `pbinom` result. With a success probability near one and only 12 trials, the distribution is visibly skewed and the exact calculation is cheap. Normal approximations are more persuasive when both expected successes $np$ and expected failures $n(1-p)$ are comfortably away from zero.

## Parameterization is part of the model

Short distribution calls can conceal a parameter mismatch. Base R uses `sd`, not variance, for the normal distribution. The exponential distribution uses `rate` by default, so its mean is $1/\text{rate}$. Gamma functions also default to a rate parameter but allow `scale`; supplying both is an error. The binomial `size` is the number of trials, while negative-binomial functions use `size` as a dispersion-related parameter, not a trial count.

| Family | R root | Main parameters | Mean | Variance |
|---|---|---|---|---|
| Binomial | `binom` | `size = n`, `prob = p` | $np$ | $np(1-p)$ |
| Poisson | `pois` | `lambda` | $\lambda$ | $\lambda$ |
| Normal | `norm` | `mean = \mu`, `sd = \sigma` | $\mu$ | $\sigma^2$ |
| Uniform | `unif` | `min = a`, `max = b` | $(a+b)/2$ | $(b-a)^2/12$ |
| Exponential | `exp` | `rate = \lambda` | $1/\lambda$ | $1/\lambda^2$ |
| Student t | `t` | `df` | $0$ for $df\gt 1$ | $df/(df-2)$ for $df\gt 2$ |

The t distribution's heavy tails weaken as its degrees of freedom increase; it approaches the standard normal. Chi-squared and F distributions also depend on degrees of freedom and appear naturally in inference about variances and model comparisons. Checking `args()` or the function help before relying on memory is cheap and prevents scale-versus-rate errors.

## Simulation as a model check

The `r` functions generate pseudo-random observations. `set.seed()` fixes the initial generator state so a calculation can be reproduced. It does not make a Monte Carlo estimate exact, and inserting another random call changes all later values in that sequence.

```r
set.seed(123)
n_sim <- 100000
draws <- rbinom(n_sim, size = 12, prob = 0.9)

simulated <- mean(draws >= 10)
theoretical <- pbinom(9, size = 12, prob = 0.9, lower.tail = FALSE)
c(simulated = simulated, theoretical = theoretical)
```

The logical expression `draws >= 10` produces one indicator per simulated experiment. Its mean is the proportion of experiments satisfying the event. The Monte Carlo standard error for an estimated probability $\hat p$ based on $N$ independent simulations is approximately

$$
\sqrt{\frac{\hat p(1-\hat p)}{N}}.
$$

With $p\approx0.889$ and $N=100000$, that standard error is about $0.0010$. A discrepancy of a few thousandths is ordinary; a discrepancy of several tenths points toward a wrong event boundary, parameter, or simulation design.

Simulation is especially useful when no convenient closed form exists, but it should not replace an exact distribution function that already gives the desired probability quickly and accurately. It can still serve as an independent check on event translation.

## Checks before accepting a probability

- Confirm whether `d*` returns mass or density for the chosen family.
- Write strict and non-strict boundaries explicitly, especially for counts.
- Check the units and meaning of every parameter, including rate versus scale and standard deviation versus variance.
- Prefer `lower.tail = FALSE` and `log.p = TRUE` when extreme tails could suffer cancellation or underflow.
- Verify that probabilities lie in $[0,1]$ and that quantiles are on the measurement scale.
- Compare the result with the distribution's mean and spread. A numerically valid answer can still be implausible under the stated model.
- Treat model assumptions separately from calculation accuracy. Independence, constant event rates, and approximate normality are substantive claims, not properties checked by the R function.

<div className="see-also">

See also: [Vectors, Arithmetic, and Comparison](/cs/programming/r/vectors-arithmetic-comparison) · [Descriptive Statistics](/cs/programming/r/descriptive-statistics) · [Statistical Inference](/cs/programming/r/statistical-inference) · [Apply Family](/cs/programming/r/apply-family)

</div>
