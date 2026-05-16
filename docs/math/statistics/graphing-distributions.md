---
title: Graphing Distributions
sidebar_position: 3
---

# Graphing Distributions

A distribution describes how the values of a variable are arranged. Before computing sophisticated summaries, a statistician should look. Graphs reveal shape, center, spread, clusters, gaps, possible data-entry errors, and outliers. The Lane text devotes an early chapter to graphing because most later methods silently assume something about the shape of the data: whether values are symmetric, skewed, roughly normal, grouped by category, or separated into distinct subpopulations.

Different variables require different displays. A bar chart is natural for categories, while a histogram or stem-and-leaf plot is natural for quantitative values. A box plot compresses a distribution into a five-number summary and is especially useful for comparing several groups. The goal is not decoration; the goal is to choose a display that lets the structure of the data answer the statistical question.

## Definitions

A **frequency distribution** lists the number of observations in each category or interval. A **relative frequency distribution** divides each frequency by the total sample size, giving proportions that add to 1. A **percentage distribution** multiplies relative frequencies by 100.

For a categorical variable, a **bar chart** uses separated bars whose heights represent counts or proportions. The separation between bars is important because the categories are distinct rather than intervals on a continuous scale. A **Pareto chart** is a bar chart ordered from largest category to smallest, often with a cumulative percentage line.

For a quantitative variable, a **histogram** divides the number line into adjacent bins. The height or area of each bar represents how many observations fall in that interval. Because the bins are adjacent, histograms emphasize continuity and distribution shape. Bin width matters: bins that are too wide hide features, while bins that are too narrow create noise.

A **stem-and-leaf display** splits each observation into a stem and a leaf, preserving the original data values while creating a rough histogram. For example, the values 42, 44, and 49 might appear as stem 4 with leaves 2, 4, 9. It works best for small to moderate data sets.

A **box plot** displays the median, first quartile $Q_1$, third quartile $Q_3$, interquartile range $IQR=Q_3-Q_1$, and potential outliers. A common rule marks observations below $Q_1-1.5IQR$ or above $Q_3+1.5IQR$ as possible outliers. The whiskers usually extend to the most extreme non-outlying data values.

A **dot plot** places one dot for each observation on a number line. Dot plots are excellent for small samples because they show every value. A **frequency polygon** connects points plotted at class midpoints. It can be useful when comparing several quantitative distributions on the same axes.

## Key results

The most important graphical result is that the same data can tell a different visual story under different choices of scale, bin width, ordering, and grouping. A histogram of exam scores using bins of width 20 may show only "low, middle, high," while bins of width 5 may reveal two clusters, one near 70 and another near 90. Therefore, a responsible analysis often checks more than one graph.

For quantitative data, common visual features include:

- **Center**: where typical values lie.
- **Spread**: how far values vary from each other.
- **Shape**: whether the distribution is symmetric, left-skewed, right-skewed, uniform, bell-shaped, or multimodal.
- **Outliers**: observations separated from the main pattern.
- **Gaps and clusters**: signs of subgroups, measurement thresholds, or unusual processes.

For categorical data, the main features are category ordering, dominance, balance, and rare categories. Since category names are not numbers, the axis order should be chosen for interpretation: natural order if the categories are ordinal, frequency order if the question is ranking, or a meaningful domain order if the categories have a conventional sequence.

The five-number summary behind a box plot is

$$
\min,\ Q_1,\ \mathrm{median},\ Q_3,\ \max.
$$

The interquartile range is

$$
IQR = Q_3 - Q_1.
$$

The standard outlier fences are

$$
\begin{aligned}
\mathrm{lower\ fence} &= Q_1 - 1.5IQR \\
\mathrm{upper\ fence} &= Q_3 + 1.5IQR.
\end{aligned}
$$

These fences are screening rules, not automatic deletion rules. An outlier may be a data-entry error, a rare but valid value, or the most scientifically interesting case in the data.

## Visual

| Display | Best for | Shows individual values? | Common mistake |
|---|---|---:|---|
| Bar chart | Nominal or ordinal categories | No | Using connected bars for categories |
| Histogram | Quantitative distributions | No | Choosing a misleading bin width |
| Stem-and-leaf | Small quantitative samples | Yes | Using it for very large data sets |
| Box plot | Comparing distributions | No | Treating outlier marks as automatic errors |
| Dot plot | Small samples, repeated values | Yes | Overplotting without stacking or jitter |
| Frequency polygon | Comparing quantitative shapes | No | Forgetting class midpoints |

```text
Right-skewed distribution

frequency
   ^
   |      ####
   |    ########
   |  ############
   | ################
   |        ###########
   |             #######
   |                  ###
   +--------------------------> value
        center       long tail
```

## Worked example 1: Building a histogram by hand

Problem: A teacher records the following quiz scores out of 20:

$$
8,\ 9,\ 10,\ 12,\ 12,\ 13,\ 14,\ 14,\ 15,\ 15,\ 16,\ 17,\ 18,\ 18,\ 19.
$$

Construct a frequency table using bins $8$-$10$, $11$-$13$, $14$-$16$, and $17$-$19. Then describe the shape.

Method:

1. Count values from 8 to 10: 8, 9, 10. Frequency is 3.
2. Count values from 11 to 13: 12, 12, 13. Frequency is 3.
3. Count values from 14 to 16: 14, 14, 15, 15, 16. Frequency is 5.
4. Count values from 17 to 19: 17, 18, 18, 19. Frequency is 4.
5. Compute relative frequencies by dividing by $n=15$:

$$
\begin{aligned}
3/15 &= 0.200 \\
3/15 &= 0.200 \\
5/15 &= 0.333 \\
4/15 &= 0.267.
\end{aligned}
$$

Answer:

| Score bin | Frequency | Relative frequency |
|---:|---:|---:|
| 8-10 | 3 | 0.200 |
| 11-13 | 3 | 0.200 |
| 14-16 | 5 | 0.333 |
| 17-19 | 4 | 0.267 |

The distribution is concentrated in the upper half of the scale, with the tallest bin at 14-16 and no extreme isolated value. It is slightly left-skewed because the lower scores stretch farther from the main group than the upper scores do. However, the sample is small, so this description should be cautious.

Checked answer: The frequencies add to $3+3+5+4=15$, matching the number of scores. The relative frequencies add to $1.000$ after rounding.

## Worked example 2: Box plot fences and interpretation

Problem: Delivery times in minutes for 13 orders are:

$$
21,\ 22,\ 23,\ 24,\ 25,\ 25,\ 26,\ 27,\ 29,\ 31,\ 32,\ 33,\ 48.
$$

Find the five-number summary, $IQR$, outlier fences, and interpret the possible outlier.

Method:

1. The data are already sorted.
2. With $n=13$, the median is the 7th value: $26$.
3. The lower half excluding the median is $21,22,23,24,25,25$. Its median is the average of the 3rd and 4th values:

$$
Q_1=\frac{23+24}{2}=23.5.
$$

4. The upper half excluding the median is $27,29,31,32,33,48$. Its median is

$$
Q_3=\frac{31+32}{2}=31.5.
$$

5. Compute the interquartile range:

$$
IQR=31.5-23.5=8.
$$

6. Compute fences:

$$
\begin{aligned}
\mathrm{lower\ fence} &= 23.5 - 1.5(8)=11.5 \\
\mathrm{upper\ fence} &= 31.5 + 1.5(8)=43.5.
\end{aligned}
$$

Answer: The five-number summary is $21, 23.5, 26, 31.5, 48$. The value 48 is above the upper fence 43.5, so it is a possible outlier. It should not be deleted automatically. It might represent a traffic delay, a weather event, a wrong address, or a data-entry error. Each possibility has a different implication for operations.

Checked answer: All values except 48 lie between the fences. The middle 50% of delivery times lie between 23.5 and 31.5 minutes, so a typical order is much closer to 26 minutes than to 48 minutes.

## Code

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([8, 9, 10, 12, 12, 13, 14, 14, 15, 15, 16, 17, 18, 18, 19])
bins = [8, 11, 14, 17, 20]
labels = ["8-10", "11-13", "14-16", "17-19"]

table = pd.cut(scores, bins=bins, right=False, labels=labels).value_counts().sort_index()
print(pd.DataFrame({"frequency": table, "relative": table / len(scores)}))

plt.hist(scores, bins=bins, edgecolor="black")
plt.xlabel("quiz score")
plt.ylabel("frequency")
plt.title("Quiz-score histogram")
plt.show()
```

The code uses left-closed bins: $[8,11)$ contains 8, 9, and 10. Explicit bin edges make the display reproducible and prevent the plotting library from silently choosing a different grouping than the one described in the analysis.

## Common pitfalls

- Using a pie chart or bar chart for a quantitative variable when the order and spacing of values matter.
- Forgetting that histogram bars touch because bins represent intervals on a number line.
- Changing the vertical axis or bin width until the graph "looks right" for a preferred story.
- Reporting a box plot outlier as an error without checking the original record.
- Comparing group histograms with different bin widths or different axis scales.
- Treating a graph as a final analysis. Graphs guide questions and reveal structure, but numerical summaries and study design still matter.

## Connections

- [Statistical literacy and data](/math/statistics/statistical-literacy-and-data)
- [Summarizing distributions](/math/statistics/summarizing-distributions)
- [Bivariate data and correlation](/math/statistics/bivariate-data-and-correlation)
- [Normal, t, chi-square, and F distributions](/math/statistics/normal-t-chi-square-and-f-distributions)
- [Linear regression inference](/math/statistics/linear-regression-inference)
