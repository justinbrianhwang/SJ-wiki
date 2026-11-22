---
title: Descriptive Statistics
sidebar_position: 13
---

# Descriptive Statistics

Descriptive statistics summarize what is in a sample before moving to formal inference. The book's statistics section begins with elementary summaries because they are the bridge between raw vectors and statistical reasoning. A mean, median, standard deviation, table, or quantile does not prove a hypothesis, but it reveals scale, center, spread, skew, outliers, and group differences that should shape the rest of the analysis.

In R, descriptive statistics are mostly vector operations plus grouping. You compute a summary for one vector, then repeat it across columns, groups, or subsets. The same ideas support plots, confidence intervals, hypothesis tests, and models. If a summary is wrong because of missing values, bad classes, or accidental subsetting, later inference will also be wrong.

## Definitions

The **mean** is the arithmetic average:

$$
\begin{aligned}
\bar{x} &= \frac{1}{n}\sum_{i=1}^{n} x_i.
\end{aligned}
$$

The **median** is the middle value after sorting, or the average of the two middle values for an even sample size. It is more resistant to outliers than the mean.

The **variance** measures average squared deviation from the mean. R's `var()` computes the sample variance:

$$
\begin{aligned}
s^2 &= \frac{1}{n - 1}\sum_{i=1}^{n}(x_i - \bar{x})^2.
\end{aligned}
$$

The **standard deviation** is the square root of variance. It returns to the original measurement units.

The **interquartile range (IQR)** is $Q_3 - Q_1$, the distance between the 75th and 25th percentiles.

A **frequency table** counts category occurrences. `table()` is the base R tool for one-way and two-way counts.

## Key results

Different summaries answer different questions:

| Question | Summary | R function | Sensitive to outliers? |
|---|---|---|---|
| Typical arithmetic level | Mean | `mean(x)` | Yes |
| Middle observation | Median | `median(x)` | No, relatively resistant |
| Spread around mean | Standard deviation | `sd(x)` | Yes |
| Middle 50 percent spread | IQR | `IQR(x)` | Resistant |
| Five-number overview | Summary | `summary(x)` | Mixed |
| Category counts | Frequency table | `table(x)` | Not numeric |
| Quantile cutoffs | Quantiles | `quantile(x)` | Depends on quantile |

For grouped summaries in base R, common tools include `tapply`, `aggregate`, `by`, `split` plus `lapply`, and formula methods. For data frames with several numeric columns, `vapply` over selected columns is reliable.

Missing values require explicit treatment. `mean(c(1, NA, 3))` returns `NA`; `mean(c(1, NA, 3), na.rm = TRUE)` returns 2. The latter is not automatically "better"; it encodes a decision to summarize observed values only.

A descriptive statistic should be interpreted with sample size. A group mean based on 2 observations is much less stable than a group mean based on 200 observations. Include counts beside group summaries.

## Visual

```text
Sorted data:  3   4   5   7   8   9   20
              |       |       |       |
             min      Q1    median    Q3       max

Mean is pulled right by 20.
Median stays at the middle value 7.
```

| R pattern | Example | Output shape |
|---|---|---|
| One numeric vector | `mean(mtcars$mpg)` | One number |
| Several columns | `vapply(mtcars[cols], mean, numeric(1))` | Named vector |
| One grouping variable | `tapply(mtcars$mpg, mtcars$cyl, mean)` | Grouped vector |
| Data frame formula | `aggregate(mpg ~ cyl, mtcars, mean)` | Data frame |
| Two-way categories | `table(df$a, df$b)` | Contingency table |

## Worked example 1: Manual mean and standard deviation

Problem: compute the mean and sample standard deviation of `x <- c(4, 6, 8, 10)` manually and verify with R.

Method:

1. Sum the values and divide by sample size.
2. Compute deviations from the mean.
3. Square deviations.
4. Sum squared deviations.
5. Divide by `n - 1` for sample variance.
6. Take the square root for standard deviation.

Manual work:

$$
\begin{aligned}
\bar{x} &= \frac{4 + 6 + 8 + 10}{4} = 7 \\
x_i - \bar{x} &= -3, -1, 1, 3 \\
(x_i - \bar{x})^2 &= 9, 1, 1, 9 \\
s^2 &= \frac{9 + 1 + 1 + 9}{4 - 1} = \frac{20}{3} \\
s &= \sqrt{20/3} \approx 2.582.
\end{aligned}
$$

```r
x <- c(4, 6, 8, 10)
mean(x)
# [1] 7

var(x)
# [1] 6.666667

sd(x)
# [1] 2.581989
```

Checked answer: R's `var(x)` returns `6.666667`, which is `20 / 3`, and `sd(x)` returns the square root of that value. This confirms that R uses sample variance with denominator `n - 1`.

## Worked example 2: Grouped summaries for `iris`

Problem: summarize sepal length by species in the `iris` data set, reporting count, mean, median, and standard deviation.

Method:

1. Split `Sepal.Length` by `Species`.
2. Write a function that returns named summaries.
3. Apply it to each group.
4. Combine results into a table.
5. Check the counts.

```r
summary_fun <- function(x) {
  c(
    n = length(x),
    mean = mean(x),
    median = median(x),
    sd = sd(x)
  )
}

pieces <- tapply(iris$Sepal.Length, iris$Species, summary_fun)
result <- do.call(rbind, pieces)
round(result, 3)
#               n  mean median    sd
# setosa       50 5.006    5.0 0.352
# versicolor   50 5.936    5.9 0.516
# virginica    50 6.588    6.5 0.636
```

Checked answer: each iris species has 50 rows, so the `n` column should be 50 for all three groups. The means increase from setosa to versicolor to virginica, matching the known pattern that virginica plants tend to have larger sepal length in this data set.

This example includes counts with summaries. Without counts, a reader cannot judge how much data supports each group statistic.

## Code

```r
# Compact descriptive report for numeric columns and one grouping variable.

describe_by <- function(df, value, group) {
  values <- df[[value]]
  groups <- df[[group]]

  if (!is.numeric(values)) stop("value column must be numeric")

  split_values <- split(values, groups)
  stats <- lapply(split_values, function(x) {
    x <- x[!is.na(x)]
    c(
      n = length(x),
      mean = mean(x),
      sd = sd(x),
      q1 = unname(quantile(x, 0.25)),
      median = median(x),
      q3 = unname(quantile(x, 0.75))
    )
  })

  data.frame(group = names(stats), do.call(rbind, stats), row.names = NULL)
}

print(describe_by(mtcars, value = "mpg", group = "cyl"))
```

The grouped summary includes both location and spread. The mean and median describe center; standard deviation and quartiles describe variability; `n` tells how many observations support the group. Reporting only a mean would hide whether the group is stable, skewed, or based on very few rows. In small data sets such as `mtcars`, the count is especially important because a single unusual observation can noticeably change a group mean.

The function removes missing values inside each group before computing summaries. That choice is visible in the code, but a production report should also report how many values were removed. One simple extension is to store `missing = sum(is.na(x))` before `x <- x[!is.na(x)]`. This avoids the common problem of comparing group means computed from different effective sample sizes without noticing it.

Descriptive statistics should usually be paired with graphics. A mean and standard deviation are compact, but they do not show multimodality, outliers, or nonlinear relationships. A histogram, boxplot, or scatterplot often reveals whether the numerical summary is appropriate. For example, if the mean and median are far apart, inspect a plot before using the mean as the main description.

Finally, choose summaries that match the measurement scale. Means and standard deviations make sense for interval-like numeric variables. Counts and proportions make sense for categories. Medians and IQRs are often better for skewed numeric variables. Factor codes should not be averaged unless the coding itself is a meaningful numeric scale.

For a complete first-pass report, combine four ingredients: sample size, missing-value count, a center summary, and a spread summary. For a numeric variable, that might be `n`, missing, mean, median, standard deviation, and IQR. For a categorical variable, it might be total count, missing count, category counts, and category proportions. This report is simple, but it catches many data-quality problems before inference begins.

Descriptive statistics also guide model choice. Strong skew may suggest a transformation or a robust method. Unequal group spreads may affect a test choice. Outliers may motivate diagnostics rather than automatic deletion. A near-zero variance predictor may be useless in a model. Treat summaries as the first conversation with the data, not as a box to check before running more impressive functions.

In coursework, show at least one manual calculation for a summary before relying on R output. Computing one mean, one variance, or one table count by hand builds trust in the function and clarifies the denominator or counting rule. After that, R can scale the same idea across groups and columns.

After summaries are computed, preserve units in labels or table names. A mean of `3.2` is ambiguous; a mean weight of `3.2 thousand pounds` is interpretable.

Clear units also prevent mixing incompatible measurements in later comparisons.

## Common pitfalls

- Reporting a mean without checking for skew or outliers. Compare mean and median.
- Forgetting `na.rm = TRUE` or using it without reporting missing counts.
- Confusing sample variance with population variance. R's `var()` uses denominator `n - 1`.
- Summarizing factor codes as if they were real numeric measurements.
- Omitting group sample sizes from grouped summaries.
- Treating correlation or group differences from descriptive summaries as causal evidence.

## Connections

- [Probability distributions](/cs/programming/r/probability-distributions)
- [Base graphics](/cs/programming/r/base-graphics)
- [Statistical inference](/cs/programming/r/statistical-inference)
- [Linear and generalized models](/cs/programming/r/linear-and-generalized-models)
