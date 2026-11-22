---
title: Vectors, Arithmetic, and Comparison
sidebar_position: 3
---

# Vectors, Arithmetic, and Comparison

R's basic computational unit is the vector. Even `7` is a vector of length one, so arithmetic, comparison, mathematical functions, and summaries naturally accept several values at once. Matrices add dimensions to an atomic vector; data-frame columns are vectors collected in a list. Understanding length, type, and attributes therefore explains a large part of ordinary R behavior.

Vectorization is most useful when the expression states a transformation directly. `scores + 10` says “add ten to every score,” while `scores >= 60` produces one logical decision per score. The output's shape can often be predicted before running the code.

## Atomic vectors and how they are built

An atomic vector contains elements of one type. The common atomic types are logical, integer, double, complex, character, and raw. The word “numeric” often covers both integer and double vectors in user-facing functions, although `typeof()` distinguishes them.

```r
typeof(c(TRUE, FALSE))
# [1] "logical"

typeof(c(1L, 2L))
# [1] "integer"

typeof(c(1, 2))
# [1] "double"

typeof(c("a", "b"))
# [1] "character"
```

Useful constructors express different patterns:

| Expression | Result | Intended pattern |
|---|---|---|
| `c(2, 4, 8)` | `2, 4, 8` | Explicit values |
| `1:5` | `1, 2, 3, 4, 5` | Unit-step sequence |
| `seq(0, 1, by = 0.25)` | `0, .25, .5, .75, 1` | Controlled sequence |
| `rep(3, times = 4)` | `3, 3, 3, 3` | Repeat a whole value or vector |
| `rep(1:2, each = 3)` | `1, 1, 1, 2, 2, 2` | Repeat each element |
| `numeric(4)` | four zeros | Preallocated double vector |

The colon operator advances by one and has high precedence. `1:n - 1` means `(1:n) - 1`, not `1:(n - 1)`. When endpoints are calculated or a zero-length result is possible, `seq_len(n)` and `seq_along(x)` are safer. For example, `1:0` yields `c(1, 0)`, whereas `seq_len(0)` yields an empty integer vector.

Combining atomic types triggers coercion to a common type:

```r
c(TRUE, 2L, 3.5)
# [1] 1.0 2.0 3.5

c(1, "2")
# [1] "1" "2"
```

The second result is character, so arithmetic requires a deliberate conversion. A list, unlike an atomic vector, can retain heterogeneous element types.

## Position-wise arithmetic

With equal-length vectors, arithmetic pairs elements by position:

$$
\begin{aligned}
(x_1,x_2,x_3)+(y_1,y_2,y_3)
&=(x_1+y_1,x_2+y_2,x_3+y_3).
\end{aligned}
$$

```text
position       1     2     3     4
x             10    20    30    40
y              1     2     3     4
x + y         11    22    33    44
x > 25     FALSE FALSE  TRUE  TRUE
```

The standard arithmetic operators are `+`, `-`, `*`, `/`, exponentiation `^`, integer division `%/%`, and remainder `%%`. Ordinary division returns a double result. Parentheses are preferable when a formula's reading might depend on remembering precedence.

Many functions are vectorized in the same sense: `sqrt`, `log`, `exp`, `sin`, `abs`, `round`, `pmin`, and `pmax` return a value for each compatible input position. Summary functions such as `sum`, `mean`, `sd`, `min`, and `max` reduce many values to one or a few results. `cumsum`, `cumprod`, `cummin`, and `cummax` retain the input length while accumulating along it.

Vectorized code may call optimized internal loops and is often faster than growing a result inside an R loop. More important, it exposes the operation's alignment. It is not a command to avoid all loops: sequential algorithms, stateful simulations, and computations that would allocate huge intermediate vectors can be clearer or cheaper with an explicit loop.

## Recycling is positional, not relational

When one operand has length one, R reuses it across every position:

```r
c(10, 20, 30) + 5
# [1] 15 25 35
```

This scalar case is central to R notation. More generally, R recycles the shorter vector. If the longer length is not a multiple of the shorter length, arithmetic emits a warning:

```r
c(10, 20, 30, 40) + c(1, 2)
# [1] 11 22 31 42

c(10, 20, 30) + c(1, 2)
# warning: longer object length is not a multiple of shorter object length
```

The first operation is mechanically well-defined, but it is readable only when the two-value pattern was intended. A warning should stop an analysis until lengths and alignment are checked.

Names do not cause arithmetic to match elements by name:

```r
x <- c(a = 1, b = 2)
y <- c(b = 10, a = 20)
x + y
#  a  b
# 11 22
```

Position one is added to position one, so the result is not `a = 21, b = 12`. If names represent keys, reorder explicitly with `y[names(x)]` or join in a data-frame operation after validating uniqueness. Silent positional alignment is one of the most expensive vector mistakes because the lengths can agree and no warning is produced.

## Worked transformation: curving scores without losing the scale

Five raw scores out of 40 are 31, 36, 28, 40, and 34. Convert each to a percentage, add three percentage points, and cap the result at 100:

```r
raw <- c(31, 36, 28, 40, 34)
percent <- raw / 40 * 100
curved <- percent + 3
final <- pmin(curved, 100)

percent
# [1]  77.5  90.0  70.0 100.0  85.0

curved
# [1]  80.5  93.0  73.0 103.0  88.0

final
# [1]  80.5  93.0  73.0 100.0  88.0
```

Each stage has length five. The division recycles the scalar 40, multiplication recycles 100, and addition recycles 3. `pmin(curved, 100)` takes the smaller value at every position, replacing only 103.

The mean can be checked from the pieces. The original percentages sum to

$$
77.5+90+70+100+85=422.5.
$$

Adding three to five scores would raise the total to $437.5$, but the cap removes the three excess points from 103. Thus

$$
\bar{x}=\frac{434.5}{5}=86.9.
$$

```r
mean(final)
# [1] 86.9
```

Using `pmin` matters. `min(curved, 100)` would reduce all inputs to the single global minimum, 73, rather than cap each score.

## Comparisons produce data

The operators `<`, `<=`, `>`, `>=`, `==`, and `!=` return logical vectors. They do not merely control `if`; their results can be counted, tabulated, indexed, and combined.

```r
mpg_high <- mtcars$mpg > 25
small_engine <- mtcars$cyl <= 4
selected <- mpg_high & small_engine

sum(selected)
# [1] 6

mtcars$mpg[selected]
# [1] 32.4 30.4 33.9 27.3 26.0 30.4
```

`selected` has one value per row. Logical values coerce to one and zero in `sum`, so the sum counts true positions. Placing the same vector inside brackets selects those positions.

`&` and `|` operate element by element. `&&` and `||` inspect only the first element of each operand and short-circuit; they belong mainly in `if` and `while` conditions that require one decision. `!` negates each logical element.

Missing comparisons propagate uncertainty. If `x[2]` is `NA`, then `x > 0` is also `NA` at position two. Logical indexing with that result includes an `NA` placeholder. To retain known positive values, use `!is.na(x) & x > 0` or another explicit missing-value policy.

The `%in%` operator asks membership and is often clearer than a chain of equality tests:

```r
group <- c("control", "treated", "other", NA)
group %in% c("control", "treated")
# [1]  TRUE  TRUE FALSE FALSE
```

Unlike `match`, `%in%` never returns `NA`; it is defined as a membership decision for each element, including missing values according to whether the table contains a matching missing value.

## Floating-point equality needs a tolerance

Most decimal fractions have no finite binary floating-point representation. Their stored values are close approximations, and separate calculation paths can round differently:

```r
0.1 + 0.2 == 0.3
# [1] FALSE

0.1 + 0.2 - 0.3
# [1] 5.551115e-17
```

For a diagnostic comparison, `all.equal` reports whether values are equal within a tolerance:

```r
all.equal(0.1 + 0.2, 0.3)
# [1] TRUE
```

For element-wise decisions, choose a tolerance meaningful on the data's scale:

```r
abs(observed - expected) <= tolerance
```

A fixed absolute tolerance can be too strict for very large numbers and too loose near zero. Numerical code often combines absolute and relative terms, for example

$$
|x-y|\le \varepsilon_{abs}+\varepsilon_{rel}\max(|x|,|y|).
$$

Exact `==` remains appropriate for integers within their exact range, categorical labels, and values deliberately produced by the same discrete representation.

## Worked filter: calibration with missing measurements

Five readings are compared with a target of 10. A reading is accepted when it is known and differs from the target by at most 1:

```r
reading <- c(10.2, 9.8, NA, 12.5, 8.9)
target <- 10
deviation <- reading - target
accepted <- !is.na(reading) & abs(deviation) <= 1

deviation
# [1]  0.2 -0.2   NA  2.5 -1.1

accepted
# [1]  TRUE  TRUE FALSE FALSE FALSE
```

The calculation proceeds position by position:

1. `10.2 - 10` is `0.2`; its absolute value is within 1.
2. `9.8 - 10` is `-0.2`; its absolute value is also within 1.
3. The missing reading produces a missing deviation, but `!is.na(reading)` is false, so the combined selector is false.
4. The deviation `2.5` exceeds the tolerance.
5. The absolute deviation `1.1` also exceeds it.

```r
sum(accepted)
# [1] 2

mean(reading[accepted])
# [1] 10
```

Two of the five readings qualify, and their mean is $(10.2+9.8)/2=10$. Reporting `sum(accepted)` alongside the mean records the effective sample size.

## Reduction, centering, and standardization

An element-wise function maps positions to positions. A reduction combines positions. The distinction explains why `x - mean(x)` has the same length as `x`: `mean(x)` first reduces the vector to one number, then scalar recycling subtracts that number from every element.

Take $x=(2,4,8)$. Its mean is

$$
\bar{x}=\frac{2+4+8}{3}=\frac{14}{3}.
$$

The centered vector is

$$
x-\bar{x}=\left(-\frac{8}{3},-\frac{2}{3},\frac{10}{3}\right).
$$

Its components sum to zero:

$$
-\frac{8}{3}-\frac{2}{3}+\frac{10}{3}=0.
$$

That cancellation follows algebraically for any complete vector because $\sum_i(x_i-\bar{x})=\sum_i x_i-n\bar{x}=0$. Small floating-point residue may remain when R evaluates the expression numerically.

```r
x <- c(2, 4, 8)
centered <- x - mean(x)

centered
# [1] -2.6666667 -0.6666667  3.3333333

sum(centered)
# [1] 0
```

R's `var(x)` uses the sample-variance denominator $n-1$:

$$
\begin{aligned}
s^2
&=\frac{\sum_i(x_i-\bar{x})^2}{n-1}\\
&=\frac{64/9+4/9+100/9}{2}\\
&=\frac{28}{3}\approx9.3333.
\end{aligned}
$$

```r
var(x)
# [1] 9.333333

sd(x)
# [1] 3.05505

z <- (x - mean(x)) / sd(x)
```

The z-score expression performs two scalar-recycling operations after computing the summaries. Its result has mean approximately zero and sample standard deviation one. If `x` contains `NA`, the mean and standard deviation are missing unless the missing-value policy is supplied consistently to both summaries. Calling `scale(x)` performs centering and optional scaling while retaining the center and scale as attributes.

Weighted summaries need explicit alignment. For values $x_i$ and nonnegative weights $w_i$, the weighted mean is

$$
\bar{x}_w=\frac{\sum_i w_i x_i}{\sum_i w_i}.
$$

Both multiplication and summation are vector operations, but equal lengths do not prove that a weight belongs to the value in the same position. When names encode identities, reorder and validate them before calling `weighted.mean`.

## Element-wise multiplication is not a matrix product

For two numeric vectors, `x * y` multiplies corresponding positions. Their dot product is the sum of those products:

```r
x <- c(1, 2, 3)
y <- c(4, 5, 6)

x * y
# [1]  4 10 18

sum(x * y)
# [1] 32

x %*% y
#      [,1]
# [1,]   32
```

`%*%` is matrix multiplication and returns a matrix-shaped result. For matrices, `A * B` remains element-wise while `A %*% B` combines rows of A with columns of B. Confusing the operators can produce a result with plausible numbers but a completely different mathematical meaning. Conformable dimensions are required for `%*%`; element-wise operations instead follow array conformance and recycling rules.

## Indices are vectors too

Square-bracket extraction accepts several kinds of index vector. Positive integers select positions in the stated order and may repeat them. Negative integers exclude positions. Logical indices retain true positions and are recycled if shorter, though relying on that recycling hides mistakes. Character indices match names.

```r
x <- c(alpha = 10, beta = 20, gamma = 30)

x[c(3, 1, 1)]
# gamma alpha alpha
#    30    10    10

x[-2]
# alpha gamma
#    10    30

x[c("gamma", "alpha")]
# gamma alpha
#    30    10
```

Positive and negative indices cannot be mixed except that zero may appear because it selects nothing. Out-of-range positive positions yield missing values, while an unknown character name also yields `NA`. These behaviors are useful for alignment but dangerous when an index was assumed valid. `match` makes the alignment step explicit and exposes unmatched positions for checking.

`which(condition)` returns integer positions of true values and drops missing positions. Direct logical indexing preserves an `NA` result for an unknown selector. Therefore `x[condition]` and `x[which(condition)]` differ when `condition` contains `NA`; choosing `which` merely to suppress those unknowns can conceal missingness. State the known-data condition instead.

## Output shape as a debugging tool

Before evaluating an expression, predict its length and type:

| Expression | Length | Typical type |
|---|---:|---|
| `x + 1` | `length(x)` | Numeric |
| `x > 0` | `length(x)` | Logical |
| `sum(x)` | 1 | Numeric |
| `range(x)` | 2 | Numeric |
| `which(x > 0)` | Number of true positions | Integer |
| `x[x > 0]` | Number of true positions, plus possible unknowns | Same type as `x` |

`length(x)` checks the number of elements, `names(x)` checks labels, and `str(x)` shows type and structure. `identical` is strict about type and attributes; `all.equal` is designed for approximate numerical comparison. Choosing between them depends on whether representation or numerical agreement is being tested.

When a summary returns `NA`, inspect `anyNA(x)` before adding `na.rm = TRUE`. Removing missing values may be correct, but it changes both the estimand and the number of contributing observations. When arithmetic warns about recycling, compare input lengths and the intended keys. When a result becomes character, look for mixed values introduced by `c`, import, or conditional construction.

### Empty vectors have algebraic edge cases

Filtering can legitimately produce a zero-length vector. Element-wise arithmetic with it also has length zero, even when the other operand is scalar. Some reductions have identity values: `sum(numeric(0))` is zero and `prod(numeric(0))` is one. Others have no ordinary finite answer: `mean(numeric(0))` is `NaN`, while `min(numeric(0))` and `max(numeric(0))` warn and return infinities of the appropriate direction.

Those results follow the definitions used to compose reductions, but they may not fit a report. Check `length(selected)` before calculating a statistic whose interpretation requires observations. A zero count, an absent estimate, and a failed calculation communicate different states.

Vectorized conditional selection also has a shape contract. `ifelse(test, yes, no)` recycles its alternatives to the test length and chooses element by element. It may coerce types or strip class attributes, so direct logical assignment is often clearer for classed objects:

```r
result <- original
result[condition] <- replacement
```

The replacement length should either be one or match the number of selected positions. Otherwise recycling can repeat a pattern that was never intended.

<div className="see-also">

See also: [Indexing, Names, and Recycling](/cs/programming/r/indexing-names-recycling) · [Special Values, Classes, and Coercion](/cs/programming/r/special-values-classes-coercion) · [Matrices and Arrays](/cs/programming/r/matrices-and-arrays) · [Descriptive Statistics](/cs/programming/r/descriptive-statistics)

</div>
