---
title: Normal, t, Chi-Square, and F Distributions
sidebar_position: 8
---

# Normal, t, Chi-Square, and F Distributions

Several continuous distributions appear repeatedly in introductory inference. The normal distribution models many measurements and approximates many sampling distributions. The $t$ distribution appears when estimating a mean with an unknown population standard deviation. The chi-square distribution appears in variance inference and categorical-data tests. The $F$ distribution appears in ANOVA and regression model comparisons. The Lane text treats these distributions across several chapters, but they form one connected family in practice.

These distributions are not just named curves. Each one describes the behavior of a particular statistic under assumptions. Understanding the statistic behind the curve prevents mechanical table lookup. For example, a $t$ statistic compares an estimated effect to its estimated standard error, while an $F$ statistic compares variance explained by a model to variance left unexplained.

## Definitions

A **normal distribution** with mean $\mu$ and standard deviation $\sigma$ is written

$$
X\sim N(\mu,\sigma^2).
$$

Its density is bell-shaped, symmetric around $\mu$, and controlled by $\sigma$. The **standard normal distribution** is $Z\sim N(0,1)$. Standardization converts a normal variable to standard normal:

$$
Z=\frac{X-\mu}{\sigma}.
$$

If $Z$ is standard normal, probabilities are areas under the standard normal curve.

The **$t$ distribution** with $\nu$ degrees of freedom is symmetric around 0 and has heavier tails than the standard normal distribution. It is commonly used for

$$
t=\frac{\bar{X}-\mu_0}{S/\sqrt{n}},
$$

when sampling from a normal population and estimating $\sigma$ by $S$. The degrees of freedom for a one-sample $t$ statistic are $\nu=n-1$.

The **chi-square distribution** with $\nu$ degrees of freedom is written $\chi^2_\nu$. If $Z_1,\dots,Z_\nu$ are independent standard normal variables, then

$$
X=Z_1^2+\cdots+Z_\nu^2
$$

has a chi-square distribution with $\nu$ degrees of freedom. The distribution is nonnegative and right-skewed, especially for small $\nu$.

The **$F$ distribution** has two degrees of freedom parameters, $\nu_1$ and $\nu_2$. If $U\sim\chi^2_{\nu_1}$ and $V\sim\chi^2_{\nu_2}$ are independent, then

$$
F=\frac{U/\nu_1}{V/\nu_2}
$$

has an $F_{\nu_1,\nu_2}$ distribution. It is nonnegative and right-skewed.

## Key results

For a normal distribution, the empirical rule says that about 68% of values lie within one standard deviation of the mean, 95% within two, and 99.7% within three. Exact probabilities come from the standard normal cumulative distribution function $\Phi(z)=P(Z\le z)$.

The normal distribution approximates the binomial distribution when $np$ and $n(1-p)$ are sufficiently large. If $X\sim\mathrm{Binomial}(n,p)$, then

$$
X\approx N(np,\ np(1-p)).
$$

Because the binomial is discrete and the normal is continuous, a continuity correction often improves approximation:

$$
P(X\le k)\approx P(Y\le k+0.5),
$$

where $Y$ is the approximating normal random variable.

The $t$ distribution approaches the standard normal as degrees of freedom increase. Small samples have more uncertainty in the estimated standard deviation, so the $t$ distribution has heavier tails. This produces wider confidence intervals and larger critical values.

Chi-square and $F$ distributions are built from squared standardized quantities. That is why they are nonnegative and skewed. In categorical tests, a chi-square statistic accumulates squared discrepancies between observed and expected counts:

$$
\chi^2=\sum \frac{(O-E)^2}{E}.
$$

In ANOVA, an $F$ statistic compares mean squares:

$$
F=\frac{MS_{\text{between}}}{MS_{\text{within}}}.
$$

Large chi-square or $F$ statistics often indicate evidence against a null model, but "large" must be judged relative to the appropriate degrees of freedom.

These distributions also differ in how their tails are used. Normal and $t$ tests for means often use one or two tails depending on the alternative hypothesis. Chi-square goodness-of-fit and independence tests use the upper tail because larger squared discrepancies are more inconsistent with the null; a statistic near zero means observed counts are unusually close to expected counts, not evidence against the model in the usual test. ANOVA $F$ tests also use the upper tail because the statistic is a ratio of explained to unexplained variance. Remembering the statistic's construction is more reliable than memorizing tail directions.

Degrees of freedom can be read as the amount of independent information left after estimating constraints. In a one-sample $t$ test, estimating the sample mean uses one constraint, leaving $n-1$ degrees of freedom for variability. In a chi-square table, fixed totals reduce how many cells can vary freely. This interpretation helps explain why larger samples make $t$ distributions look more normal and why changing the number of categories changes the chi-square reference curve.

## Visual

| Distribution | Support | Shape | Key parameters | Common statistic |
|---|---|---|---|---|
| Normal | all real numbers | symmetric bell | $\mu,\sigma$ | $Z=(X-\mu)/\sigma$ |
| $t$ | all real numbers | symmetric, heavy tails | degrees of freedom $\nu$ | $t=(\bar{X}-\mu_0)/(S/\sqrt{n})$ |
| Chi-square | $[0,\infty)$ | right-skewed | degrees of freedom $\nu$ | $\sum (O-E)^2/E$ |
| $F$ | $[0,\infty)$ | right-skewed | numerator and denominator df | ratio of mean squares |

```text
Relative shape sketch

normal and t:              chi-square and F:

   ^                            ^
   |        normal              |\
   |       /\                   | \
   |  t   /  \                  |  \___
   |  ___/    \___              |      \____
   +---------------->           +---------------->
        0                            0
```

## Worked example 1: Normal probability with standardization

Problem: Suppose adult commute times in a region are approximately normal with mean $\mu=31$ minutes and standard deviation $\sigma=8$ minutes. What proportion of commuters take longer than 45 minutes? What commute time marks the 90th percentile?

Method:

1. Standardize 45 minutes:

$$
z=\frac{45-31}{8}=\frac{14}{8}=1.75.
$$

2. Convert to an upper-tail probability:

$$
P(X>45)=P(Z>1.75)=1-\Phi(1.75).
$$

3. From a standard normal table or software, $\Phi(1.75)\approx0.9599$.

$$
P(X>45)\approx1-0.9599=0.0401.
$$

4. For the 90th percentile, find $z_{0.90}$ such that $\Phi(z_{0.90})=0.90$. The value is about 1.2816.
5. Transform back:

$$
x=\mu+z\sigma=31+1.2816(8)=31+10.2528=41.2528.
$$

Answer: About 4.0% of commuters take longer than 45 minutes. The 90th percentile is about 41.3 minutes.

Checked answer: The 90th percentile should be above the mean, and 41.3 is about 1.28 standard deviations above 31, which matches the standard normal percentile.

## Worked example 2: Choosing $t$, chi-square, or $F$

Problem: For each study, identify the appropriate reference distribution and degrees of freedom where possible.

1. A sample of 16 batteries has mean lifetime 52.1 hours and sample standard deviation 4.8 hours. Test whether the population mean differs from 50 hours.
2. A genetics activity compares observed counts of four phenotype categories with expected Mendelian proportions.
3. A one-way ANOVA compares mean exam scores across three teaching methods with 10 students per method.

Method:

1. The battery problem involves one sample mean and unknown population standard deviation. Use a one-sample $t$ distribution with

$$
\nu=n-1=16-1=15.
$$

The statistic is

$$
t=\frac{52.1-50}{4.8/\sqrt{16}}
=\frac{2.1}{1.2}
=1.75.
$$

2. The phenotype problem compares observed and expected categorical counts. Use a chi-square goodness-of-fit statistic. With four categories and no estimated parameters, the degrees of freedom are

$$
\nu=4-1=3.
$$

3. The ANOVA problem compares three group means. There are $k=3$ groups and $N=30$ total observations. Use an $F$ distribution with

$$
\nu_1=k-1=2,
$$

$$
\nu_2=N-k=27.
$$

Answer: The correct reference distributions are $t_{15}$ for the one-sample mean, $\chi^2_3$ for the four-category goodness-of-fit test, and $F_{2,27}$ for the one-way ANOVA.

Checked answer: The chosen distributions match the statistic types: standardized mean with estimated standard error, squared categorical discrepancies, and ratio of between-group to within-group mean squares.

## Code

```python
from scipy import stats

# Normal probability and percentile
mu, sigma = 31, 8
p_long = 1 - stats.norm.cdf(45, loc=mu, scale=sigma)
p90 = stats.norm.ppf(0.90, loc=mu, scale=sigma)
print(f"P(commute > 45) = {p_long:.4f}")
print(f"90th percentile = {p90:.2f}")

# t statistic and two-sided p-value for battery example
t_stat = (52.1 - 50) / (4.8 / (16 ** 0.5))
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=15))
print(f"t = {t_stat:.3f}, p = {p_value:.4f}")

# Critical F value for alpha = 0.05, df1 = 2, df2 = 27
print("F critical:", stats.f.ppf(0.95, dfn=2, dfd=27))
```

The code uses cumulative distribution functions for probabilities and percent point functions for percentiles or critical values. This is safer than copying table entries by hand, especially for nonstandard degrees of freedom.

## Common pitfalls

- Using a normal critical value for a small-sample mean when the population standard deviation is unknown.
- Forgetting that chi-square and $F$ statistics cannot be negative.
- Treating degrees of freedom as decoration rather than part of the distribution.
- Applying a normal approximation to a binomial problem when expected successes or failures are too small.
- Forgetting a continuity correction when a more accurate normal approximation to a discrete count is needed.
- Comparing a statistic to the wrong tail of the reference distribution.

## Connections

- [Random variables and probability distributions](/math/statistics/random-variables-and-distributions)
- [Sampling distributions and the central limit theorem](/math/statistics/sampling-distributions-and-clt)
- [Estimation and confidence intervals](/math/statistics/estimation-and-confidence-intervals)
- [Tests for means](/math/statistics/tests-for-means)
- [ANOVA](/math/statistics/anova)
- [Proportions and chi-square tests](/math/statistics/proportions-and-chi-square-tests)
