---
title: Summarizing Distributions
sidebar_position: 4
---

# Summarizing Distributions

Numerical summaries compress a distribution into a few interpretable quantities. The Lane text treats central tendency, variability, percentiles, and shapes of distributions as foundational because later inference depends on them. A confidence interval for a mean uses $\bar{x}$ and $s$; a z-score uses a mean and a standard deviation; an ANOVA partitions variability; regression measures how much variability is explained by a line.

Compression always loses information. A mean does not show skewness, a standard deviation does not show outliers, and a percentile does not show whether nearby values are common or rare. Good summary work therefore pairs numbers with a graph and chooses statistics whose meanings fit the distribution shape and measurement level.

![A labeled boxplot shows the median, quartiles, whiskers, and outliers of a distribution.](https://commons.wikimedia.org/wiki/Special:FilePath/Boxplot.svg)

*Figure: Components of a boxplot for summarizing a distribution. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Boxplot.svg), Jumanbar, CC BY-SA 3.0.*

## Definitions

The **mean** of $n$ observations $x_1,\dots,x_n$ is

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i.
$$

It is the balance point of the data and uses every value. The **median** is the middle value after sorting, or the average of the two middle values when $n$ is even. It is resistant to extreme values. The **mode** is the most frequent value or category. A distribution can be unimodal, bimodal, multimodal, or have no repeated value.

The **range** is $\max(x)-\min(x)$. The **interquartile range** is $IQR=Q_3-Q_1$, the width of the middle half of the data. The **sample variance** is

$$
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1},
$$

and the **sample standard deviation** is $s=\sqrt{s^2}$. The denominator $n-1$ gives the usual unbiased estimator of population variance under random sampling.

A **percentile** indicates relative standing. The 80th percentile is a value at or below which about 80% of observations fall. A **z-score** standardizes an observation:

$$
z=\frac{x-\mu}{\sigma}
$$

for a population, or approximately

$$
z=\frac{x-\bar{x}}{s}
$$

when using sample summaries descriptively. Positive z-scores are above the mean; negative z-scores are below.

**Skewness** describes asymmetry. A right-skewed distribution has a long right tail and often has mean greater than median. A left-skewed distribution has a long left tail and often has mean less than median. **Kurtosis** describes tail heaviness or peakedness relative to a reference distribution, though in introductory work it is more important to recognize outliers and tail behavior visually than to memorize a single kurtosis rule.

## Key results

The mean is sensitive to linear transformations. If every observation is transformed by $y_i=a+bx_i$, then

$$
\bar{y}=a+b\bar{x}.
$$

The standard deviation is affected by scale but not by shifts:

$$
s_y=|b|s_x.
$$

Adding 10 points to every exam score raises the mean and median by 10 but leaves standard deviation and $IQR$ unchanged. Multiplying every measurement by 2 doubles the mean, median, standard deviation, and $IQR$.

The sample variance can be computed from deviations:

$$
\sum_{i=1}^{n}(x_i-\bar{x})=0.
$$

This identity explains why squared deviations are used: simple deviations always cancel around the mean. Squaring makes distances positive and gives larger penalties to observations far from the center.

For symmetric unimodal data without strong outliers, mean and standard deviation are usually informative. For skewed data or data with outliers, the median and $IQR$ often describe typical values better. For nominal categorical data, the mode and proportions are meaningful, while means and standard deviations of arbitrary category codes are not.

The empirical rule applies approximately to bell-shaped distributions:

$$
\begin{aligned}
68\% &\text{ of values lie within } 1 \text{ standard deviation of the mean} \\
95\% &\text{ of values lie within } 2 \text{ standard deviations of the mean} \\
99.7\% &\text{ of values lie within } 3 \text{ standard deviations of the mean}.
\end{aligned}
$$

This rule is descriptive and approximate. It should not be applied blindly to strongly skewed, bounded, discrete, or multimodal distributions.

Summary choice should also follow the decision being made. If a city reports household income to describe the "typical" resident, the median is often preferred because a few very high incomes can pull the mean upward. If a factory monitors fill weights from a stable machine, the mean and standard deviation are often more useful because symmetric random variation around a target is expected. If a teacher reports class performance, the median, quartiles, and score distribution may be more informative than the mean alone. The right summary is the one that preserves the feature of the data most relevant to the question while making its limitations visible.

For any numerical summary, attach units and sample context. A standard deviation of 4 means very different things if the unit is seconds, dollars, kilograms, or points on a 5-point scale. Likewise, a median computed from 12 observations should be presented more cautiously than a median computed from 12,000 observations collected by a careful sampling design.

## Visual

| Summary | Formula or rule | Resistant to outliers? | Best use |
|---|---|---:|---|
| Mean | $\bar{x}=\sum x_i/n$ | No | Symmetric quantitative data |
| Median | middle sorted value | Yes | Skewed quantitative or ordinal data |
| Mode | most frequent value | Often | Categorical data, repeated values |
| Range | $\max-\min$ | No | Quick total spread |
| IQR | $Q_3-Q_1$ | Yes | Middle spread, box plots |
| Standard deviation | $s=\sqrt{\sum(x_i-\bar{x})^2/(n-1)}$ | No | Typical distance for roughly symmetric data |
| z-score | $(x-\bar{x})/s$ | No | Relative standing on a common scale |

```text
Mean vs median in a right-skewed distribution

frequency
   ^
   |      #####
   |    #########
   |  ############
   |      ##########
   |           ######
   |                ###
   |                    #
   +--------------------------------> value
          median   mean
```

## Worked example 1: Mean, median, variance, and standard deviation

Problem: A small lab records the number of minutes needed to process seven samples:

$$
9,\ 10,\ 10,\ 11,\ 12,\ 13,\ 19.
$$

Find the mean, median, sample variance, and sample standard deviation. Comment on the high value 19.

Method:

1. Add the observations:

$$
9+10+10+11+12+13+19=84.
$$

2. Divide by $n=7$:

$$
\bar{x}=84/7=12.
$$

3. The data are already sorted. With seven values, the median is the 4th value:

$$
\mathrm{median}=11.
$$

4. Compute deviations from the mean and square them:

| $x_i$ | $x_i-\bar{x}$ | $(x_i-\bar{x})^2$ |
|---:|---:|---:|
| 9 | -3 | 9 |
| 10 | -2 | 4 |
| 10 | -2 | 4 |
| 11 | -1 | 1 |
| 12 | 0 | 0 |
| 13 | 1 | 1 |
| 19 | 7 | 49 |

5. Sum squared deviations:

$$
9+4+4+1+0+1+49=68.
$$

6. Divide by $n-1=6$:

$$
s^2=68/6=11.3333.
$$

7. Take the square root:

$$
s=\sqrt{11.3333}\approx 3.37.
$$

Answer: The mean is 12 minutes, the median is 11 minutes, the sample variance is about 11.33 square minutes, and the sample standard deviation is about 3.37 minutes. The value 19 pulls the mean above the median and contributes $49$ of the $68$ squared-deviation total, so it strongly affects the standard deviation.

Checked answer: The deviations add to $-3-2-2-1+0+1+7=0$, which confirms the mean arithmetic.

## Worked example 2: Percentiles and z-scores

Problem: A student scored 86 on an exam. The class mean was 74 and the sample standard deviation was 8. Another exam in a different course had mean 62 and standard deviation 12, and the same student scored 80. On which exam was the student farther above the class average?

Method:

1. Standardize the first score:

$$
z_1=\frac{86-74}{8}=\frac{12}{8}=1.50.
$$

2. Standardize the second score:

$$
z_2=\frac{80-62}{12}=\frac{18}{12}=1.50.
$$

3. Compare the z-scores, not the raw score differences.

Answer: The student was equally far above average on both exams: 1.5 standard deviations above the mean. The first raw difference was 12 points and the second was 18 points, but the second course had more spread, so the standardized standing is the same.

Checked answer: Both standardized differences reduce to $1.50$. If the distributions are roughly bell-shaped, a score 1.5 standard deviations above the mean is around the upper tail but not extremely rare.

## Code

```python
import numpy as np
from scipy import stats

x = np.array([9, 10, 10, 11, 12, 13, 19])

mean = x.mean()
median = np.median(x)
sample_var = x.var(ddof=1)
sample_sd = x.std(ddof=1)
z_scores = (x - mean) / sample_sd

print({"mean": mean, "median": median, "variance": sample_var, "sd": sample_sd})
print("z-scores:", np.round(z_scores, 2))
print("skewness:", stats.skew(x, bias=False))
print("kurtosis excess:", stats.kurtosis(x, bias=False))
```

The argument `ddof=1` requests the sample variance denominator $n-1$. Without it, NumPy uses the population denominator $n$, which is appropriate only when the data are the whole population being summarized.

## Common pitfalls

- Reporting only the mean for a skewed distribution where the median better represents a typical case.
- Forgetting that variance is in squared units while standard deviation is in the original units.
- Mixing population and sample formulas without thinking about whether the data are a full population or a sample.
- Treating percentiles as percentages correct. A percentile is a location in a distribution, not a test score scale.
- Applying the empirical rule to a strongly skewed or multimodal distribution.
- Deleting high or low observations because they affect the mean, instead of investigating whether they are valid.

## Connections

- [Graphing distributions](/math/statistics/graphing-distributions)
- [Sampling distributions and the central limit theorem](/math/statistics/sampling-distributions-and-clt)
- [Estimation and confidence intervals](/math/statistics/estimation-and-confidence-intervals)
- [Tests for means](/math/statistics/tests-for-means)
- [Linear regression inference](/math/statistics/linear-regression-inference)
