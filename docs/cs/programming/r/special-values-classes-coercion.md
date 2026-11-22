---
title: Special Values, Classes, and Coercion
sidebar_position: 8
---

# Special Values, Classes, and Coercion

R distinguishes an unknown observation, an undefined numeric result, an infinite numeric result, and the absence of an object. Those states propagate differently. They also interact with storage type and class, two properties that answer different questions about an object. Most puzzling import and modeling failures become ordinary once values, type, class, and attributes are inspected separately.

## Four states that should not be collapsed

`NA` represents a missing or unknown value in a position. A vector can have length five even when two positions are `NA`; the missing values still occupy those positions. Arithmetic and comparisons usually propagate uncertainty:

```r
NA + 1
# [1] NA

NA == NA
# [1] NA
```

The equality result is unknown because neither missing value supplies a known quantity to compare. Use `is.na(x)` to detect missingness rather than `x == NA`.

`NaN` means “not a number” and normally arises from an undefined real-number operation. `0 / 0`, `Inf - Inf`, and `sqrt(-1)` under real arithmetic produce `NaN` or a warning followed by `NaN`. It is a numeric value with special semantics. `is.nan()` identifies it, while `is.na()` returns true for both ordinary `NA` and `NaN`.

`Inf` and `-Inf` are positive and negative infinity. They result from operations such as division of a nonzero finite number by zero or numeric overflow. They are not missing: ordering comparisons with finite values work, and `is.na(Inf)` is false. They can still invalidate a mean, model matrix, or plot scale.

`NULL` represents the absence of a value or component. It has length zero and no vector position. It is common as an optional argument default and as the result of looking up an absent list component.

| Value | Occupies a position? | Main detector | Typical origin |
|---|---:|---|---|
| `NA` | Yes | `is.na()` | Unobserved or failed conversion |
| `NaN` | Yes | `is.nan()` | Undefined numeric operation |
| `Inf`, `-Inf` | Yes | `is.infinite()` | Division by zero or overflow |
| `NULL` | No | `is.null()` | Absent component or optional value |

`is.finite(x)` is useful when an analysis accepts only observed finite numbers. It returns false for `NA`, `NaN`, `Inf`, and `-Inf`. `anyNA(x)` is an efficient yes-or-no test for missing values and also treats `NaN` as missing.

## Missing values have types

Bare `NA` has logical type, but it is coerced to the surrounding vector's type. R also supplies typed constants:

```r
typeof(NA)
# [1] "logical"

c(1L, NA_integer_)
# [1]  1 NA

c("known", NA_character_)
# [1] "known" NA
```

The typed forms include `NA_integer_`, `NA_real_`, `NA_complex_`, and `NA_character_`. They matter when a function must return a specific type, especially in `vapply`, conditional construction, or package code that promises a stable schema.

Logical summaries inherit missingness unless told what to do:

```r
x <- c(4, NA, 9)
all(x > 0)
# [1] NA

any(x < 0)
# [1] NA
```

Neither result can be decided from the observed positions alone. Adding `na.rm = TRUE` changes the question to one about observed values. On `c(NA_real_)`, `all(x > 0, na.rm = TRUE)` returns `TRUE` because no retained value violates the condition. That mathematically consistent result can be misleading in a data-quality check, so count retained observations as well.

### Three-valued logic in filters

Logical operations involving missing values follow what can be deduced. `FALSE & NA` is false because one false operand settles a conjunction. `TRUE | NA` is true because one true operand settles a disjunction. By contrast, `TRUE & NA` and `FALSE | NA` remain unknown.

This behavior reaches indexing. A logical index containing `NA` creates an unknown position in the result:

```r
score <- c(8, NA, 3, 10)
keep <- score >= 8
keep
# [1] TRUE   NA FALSE TRUE

score[keep]
# [1]  8 NA 10
```

The second output position is not silently discarded; R cannot determine whether the missing score meets the threshold. If the intended rule is “known scores of at least eight,” state both conditions:

```r
known_high <- !is.na(score) & score >= 8
score[known_high]
# [1]  8 10
```

Step by step, `!is.na(score)` is true at positions one, three, and four. The comparison is true at one and four, false at three, and unknown at two. Element-wise `&` resolves position two to false because the known-data condition is already false. The resulting selector contains no `NA`.

Short-circuit operators `&&` and `||` examine only the first element and are meant for single control-flow decisions. They should not replace `&` and `|` in a row filter.

## Worked trace: finite values after a ratio calculation

Suppose response times are divided by exposure, and the raw vectors contain both missing and zero values:

```r
response <- c(8, NA, 0, 5, -5, 9)
exposure <- c(2, 3, 0, 0, 0, 3)
ratio <- response / exposure

ratio
# [1]   4  NA NaN Inf -Inf   3
```

Trace each position:

1. $8/2=4$, a finite observed ratio.
2. `NA / 3` remains `NA` because the numerator is unknown.
3. `0 / 0` has no defined real value and becomes `NaN`.
4. `5 / 0` becomes `Inf`.
5. `-5 / 0` becomes `-Inf`.
6. $9/3=3$, another finite observed ratio.

Each detector answers a different question:

```r
is.na(ratio)
# [1] FALSE  TRUE  TRUE FALSE FALSE FALSE

is.nan(ratio)
# [1] FALSE FALSE  TRUE FALSE FALSE FALSE

is.infinite(ratio)
# [1] FALSE FALSE FALSE  TRUE  TRUE FALSE

is.finite(ratio)
# [1]  TRUE FALSE FALSE FALSE FALSE  TRUE
```

If the immediate task is a mean of valid finite ratios, retain positions one and six:

```r
keep <- is.finite(ratio)
sum(keep)
# [1] 2

mean(ratio[keep])
# [1] 3.5
```

The calculation is $(4+3)/2=3.5$. Reporting only 3.5 would conceal that four of six cases were rejected for three different reasons. A useful diagnostic keeps counts by cause:

```r
c(
  missing = sum(is.na(ratio) & !is.nan(ratio)),
  undefined = sum(is.nan(ratio)),
  infinite = sum(is.infinite(ratio)),
  finite = sum(is.finite(ratio))
)
#   missing undefined  infinite    finite
#         1         1         2         2
```

Whether to drop, repair, or retain those rows depends on why the denominators are zero and why the response is missing. `na.rm = TRUE` expresses a calculation rule, not a missing-data argument.

## `NULL` changes structure

Because `NULL` has length zero, combining it with an atomic vector contributes no element:

```r
c(1, NULL, 2)
# [1] 1 2
```

Lists can contain `NULL`, but assignment syntax matters:

```r
record <- list(id = 7, note = "check")
record$note <- NULL              # removes the component
record["note"] <- list(NULL)    # creates a named component containing NULL
```

An `NA_character_` note would mean that the component exists but its value is unknown. A `NULL` lookup may mean the component was never supplied. Keeping that distinction is useful for configuration objects and parsed data where “absent” and “present but missing” lead to different defaults.

## Storage type, class, and attributes

`typeof()` reports the object's internal storage organization. Common results include `logical`, `integer`, `double`, `complex`, `character`, `raw`, `list`, `closure`, and `environment`. `class()` reports the class vector used by generic method dispatch. `attributes()` shows metadata such as names, dimensions, levels, and class.

```r
day <- as.Date("2026-01-15")
typeof(day)
# [1] "double"

class(day)
# [1] "Date"

unclass(day)
# [1] 20468
```

The double stores a count of days relative to R's date origin. The `Date` class tells generic functions to print, compare, summarize, and plot it as a calendar date. Removing the class exposes the underlying number but also discards the intended behavior.

A factor gives the complementary example:

```r
group <- factor(c("control", "treated", "control"))
typeof(group)
# [1] "integer"

class(group)
# [1] "factor"

levels(group)
# [1] "control" "treated"
```

Its integer codes index a `levels` attribute. The codes are storage details; the levels carry the categorical labels. A data frame has class `data.frame` but is built on a list whose components usually have equal length. A fitted linear model has class `lm` and list storage. `summary()` behaves differently for each because it is a generic function that dispatches on class.

`str(x)` is usually the best first inspection because it shows dimensions, component types, classes, and representative values in one compact view. `class()` alone may hide underlying storage problems, while `typeof()` alone misses behavioral metadata.

Names and dimensions are attributes too. Adding a `dim` attribute to an atomic vector makes it behave as a matrix or higher-dimensional array without changing its underlying type. Removing dimensions with `drop` or `as.vector` can therefore change how indexing and generic functions behave even though the same stored numbers remain. Attribute loss during an operation deserves attention for dates, time zones, units, ordered factors, and custom classes.

Base arithmetic usually preserves a meaningful class only when a class-specific method defines the operation. Adding one to a `Date` advances one day because date methods interpret the numeric operand appropriately. Concatenation, coercion, or low-level manipulation may strip attributes depending on the method. Inspect the result after transformations rather than assuming class metadata survives.

## The atomic coercion ladder

An atomic vector has one element type. When `c()` combines compatible but different atomic types, R finds a common type capable of representing them. The common progression is logical to integer to double to complex to character:

```r
c(TRUE, 2L)
# [1] 1 2

c(2L, 3.5)
# [1] 2.0 3.5

c(1, "2")
# [1] "1" "2"
```

The third expression does not preserve a numeric first element and a character second element; both become character. Use a list when heterogeneous element types are intentional. Implicit coercion is convenient for arithmetic such as `sum(c(TRUE, FALSE, TRUE))`, where logical values become one and zero. It is risky at data boundaries because a single unexpected label can turn an entire numeric vector into character.

Explicit conversion functions include `as.integer`, `as.double`, `as.numeric`, `as.logical`, and `as.character`. A conversion may lose information: decimals are truncated toward zero by `as.integer`, unrecognized numeric text becomes `NA` with a warning, and large values may be beyond an integer type's range. The result should be checked rather than assumed.

## Worked cleaning trace: numeric text and factor codes

Suppose an imported count column contains three numeric strings, a missing field, and a label:

```r
raw_counts <- c("10", "12", NA, "missing", "15")
counts <- suppressWarnings(as.numeric(raw_counts))

counts
# [1] 10 12 NA NA 15
```

The output contains two missing values with different origins. One was already missing; the other was introduced by conversion. Preserve that difference:

```r
introduced <- is.na(counts) & !is.na(raw_counts)
already_missing <- is.na(raw_counts)

raw_counts[introduced]
# [1] "missing"

c(
  converted = sum(!is.na(counts)),
  already_missing = sum(already_missing),
  failed = sum(introduced)
)
#         converted already_missing          failed
#                 3               1               1
```

Now the observed total can be stated with its denominator:

```r
sum(counts, na.rm = TRUE)
# [1] 37

mean(counts, na.rm = TRUE)
# [1] 12.33333
```

The warning was suppressed only because failure positions were immediately recorded. Silencing a warning without an equivalent audit turns malformed labels into indistinguishable missing values.

Factors require another step. Direct numeric conversion returns internal level codes:

```r
f <- factor(c("10", "20", "10"))
as.numeric(f)
# [1] 1 2 1

as.numeric(as.character(f))
# [1] 10 20 10
```

The second route converts labels rather than codes. It is appropriate only when those labels genuinely represent quantities. A factor containing ordered categories such as `"low"`, `"medium"`, and `"high"` has no automatic numerical spacing; assigning scores is a modeling decision.

Dates need similar discipline. `as.Date("03/04/2026")` is ambiguous without a format. Supplying `format = "%d/%m/%Y"` or `format = "%m/%d/%Y"` records the intended interpretation, after which newly introduced `NA` values should be counted.

## Auditing a frame before analysis

A compact audit keeps structural and value checks together:

```r
audit_frame <- function(df) {
  data.frame(
    variable = names(df),
    class = vapply(df, function(x) paste(class(x), collapse = "/"), character(1)),
    type = vapply(df, typeof, character(1)),
    missing = vapply(df, function(x) sum(is.na(x)), integer(1)),
    infinite = vapply(df, function(x) {
      if (is.numeric(x)) sum(is.infinite(x)) else NA_integer_
    }, integer(1)),
    row.names = NULL
  )
}
```

`complete.cases(df)` identifies rows with no missing values across the selected columns, but it applies one all-or-nothing rule. A model using three columns may have more complete cases than the entire imported frame. Audit the variables used by the analysis, and record how many rows each filtering step removes.

Missing-data policy belongs beside the audit. Complete-case analysis changes the analyzed population whenever missingness is related to a measured variable. Filling every missing value with a column mean understates variation and can distort relationships. A sentinel such as `-99` is worse if it is left numeric: summaries treat it as an extreme observed value. Convert documented sentinels to `NA` during import, preserve the original data, and record the conversion count.

Different functions also choose different defaults. `mean(c(1, NA))` returns `NA`, while many modeling functions omit or fail on incomplete rows according to an `na.action` setting. A result can therefore use fewer rows than the input without an obvious error. Checking `nobs(model)`, residual lengths, or the model frame identifies the sample that actually contributed.

There is no universal “clean” subset. A ratio analysis may require finite numerator and denominator-derived values; a categorical table may legitimately retain an explicit missing category; a diagnostic report may need every malformed row. Define validity in terms of the operation being performed, then encode that rule in a named logical vector whose counts can be reported.

For numeric transformations, check finite values after the transformation rather than only before it. Positive raw measurements can still produce `-Inf` under `log(0)`, and a denominator created by subtraction can become zero even when both input columns were finite.

## Checks before trusting an object's printed form

- Use `is.na`, `is.nan`, `is.infinite`, and `is.finite` according to the question; they are not interchangeable.
- Distinguish an absent component (`NULL`) from a present unknown value (`NA`).
- Inspect both `typeof()` and `class()` when generic behavior or imported columns look surprising.
- After coercion, compare missing-value positions before and after and inspect the original labels that failed.
- Treat factor codes as implementation details unless the codes themselves were deliberately defined as data.
- Report the number of retained observations whenever `na.rm`, `complete.cases`, or a finite-value filter changes the sample.

<div className="see-also">

See also: [Factors and Categorical Data](/cs/programming/r/factors-and-categorical-data) · [Reading and Writing Data](/cs/programming/r/reading-and-writing-data) · [Descriptive Statistics](/cs/programming/r/descriptive-statistics) · [Object-Oriented R](/cs/programming/r/object-oriented-r)

</div>
