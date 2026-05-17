---
title: Indexing, Names, and Recycling
sidebar_position: 4
---

# Indexing, Names, and Recycling

Once values are in a vector, the next task is choosing the right values. R gives several indexing styles: positive positions, negative omissions, logical filters, character names, and empty selections. The book introduces these early because subsetting is not a side topic in R; it is how you inspect data, clean data, replace values, and pass selected observations into statistical functions.

![The R logo marks pages on statistical computing, graphics, and data analysis.](https://commons.wikimedia.org/wiki/Special:FilePath/R_logo.svg)

*Figure: R connects programming examples to statistical modeling and visualization workflows. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:R_logo.svg), The R Foundation, CC BY-SA 4.0.*

Names and recycling make indexing more expressive but also more dangerous. Names let you ask for `"height"` or `"control"` rather than position 3. Recycling lets short vectors align with long vectors, making scalar operations easy, but accidental recycling can silently produce wrong answers. Good R code makes the intended shape clear before it subsets or combines objects.

## Definitions

An **index** is an instruction inside square brackets. For a vector `x`, `x[1]` requests the first element, `x[c(1, 3)]` requests the first and third elements, and `x[-2]` requests all but the second element. R uses one-based indexing, so the first element is position 1, not position 0.

A **logical index** is a logical vector used to keep values where the index is `TRUE`. If `x <- c(4, 9, 12)`, then `x[x > 8]` returns `9` and `12`.

A **named vector** is a vector with a `names` attribute. Names can be set during construction with `c(a = 10, b = 20)` or afterward with `names(x) <- c("a", "b")`.

**Recycling** is R's rule for repeating a shorter vector to match a longer vector in element-wise operations. `c(10, 20, 30) + 1` recycles `1` three times. `c(10, 20, 30, 40) + c(1, 2)` recycles `1, 2` to `1, 2, 1, 2`. Recycling is safest when the longer length is an exact multiple of the shorter length.

**Replacement indexing** assigns into a subset. For example, `x[x < 0] <- 0` replaces all negative values with zero.

## Key results

Subsetting in R follows a small set of rules that appear everywhere:

| Index type | Example | Meaning | Typical use |
|---|---|---|---|
| Positive integer | `x[c(1, 4)]` | Keep listed positions | Select known positions |
| Negative integer | `x[-2]` | Drop listed positions | Remove an element |
| Logical | `x[x > 0]` | Keep `TRUE` positions | Filter observations |
| Character | `x[c("a", "b")]` | Keep named elements | Stable named lookup |
| Empty | `x[]` | Select all positions | Replace while preserving attributes |

Do not mix positive and negative positions in the same index, except for zero. `x[c(1, -2)]` is an error because it asks R to keep and drop at the same time. Decide whether the index is a keep-list or a drop-list.

Logical filters must have the right length. If the logical vector is shorter, R may recycle it. Sometimes this is intended, as in alternating selection, but most analysis filters should be exactly as long as the object being filtered. Check with `length(filter) == length(x)` when in doubt.

Named indexing is more robust than positional indexing when data may be reordered. If you store model coefficients named `"intercept"` and `"slope"`, `coef["slope"]` still works after reordering; `coef[2]` only works if the slope remains in position 2.

Replacement indexing keeps the original vector length unless the replacement itself changes the structure. This makes cleaning concise: build a condition, then assign into the positions flagged by the condition.

## Visual

```text
x:        12    5    9   18    7
pos:       1    2    3    4    5
name:    Mon  Tue  Wed  Thu  Fri

x[c(1,4)]       -> 12, 18
x[-2]           -> 12, 9, 18, 7
x[x >= 10]      -> 12, 18
x[c("Mon","Fri")] -> 12, 7
```

| Recycling case | Example | Result | Risk |
|---|---|---|---|
| Scalar | `1:4 + 10` | `11, 12, 13, 14` | Low |
| Exact repeat | `1:4 + c(0, 100)` | `1, 102, 3, 104` | Medium; document intent |
| Non-exact repeat | `1:5 + c(0, 100)` | Warning, uneven pattern | High |
| Logical scalar | `x[TRUE]` | All values | Often accidental |

## Worked example 1: Cleaning impossible measurements

Problem: a sensor reports temperatures in degrees Celsius: `21.4`, `22.0`, `-99`, `20.8`, `200`, and `21.9`. The value `-99` is a missing-data code, and `200` is outside the plausible range. Replace both with `NA`, then compute the mean of valid readings.

Method:

1. Store the readings.
2. Build one logical condition for the missing-data code.
3. Build another logical condition for implausible high values.
4. Combine the conditions with `|`.
5. Replace flagged values with `NA`.
6. Summarize with `na.rm = TRUE`.

```r
temp <- c(21.4, 22.0, -99, 20.8, 200, 21.9)
bad_code <- temp == -99
too_high <- temp > 60
bad <- bad_code | too_high

bad
# [1] FALSE FALSE  TRUE FALSE  TRUE FALSE

temp[bad] <- NA
temp
# [1] 21.4 22.0   NA 20.8   NA 21.9

mean(temp, na.rm = TRUE)
# [1] 21.525
```

Checked answer: the valid readings are `21.4`, `22.0`, `20.8`, and `21.9`. Their sum is `86.1`, and `86.1 / 4 = 21.525`. The logical index selected exactly positions 3 and 5 for replacement.

This is a standard R cleaning pattern. You do not need to loop through values one by one; you write a logical statement describing invalid values and assign into those locations.

## Worked example 2: Named lookup for grouped totals

Problem: a small shop records weekly sales by product. Use names to retrieve sales for `"tea"` and `"coffee"`, then compute their combined share of total sales.

Method:

1. Build a named numeric vector.
2. Select by character names.
3. Sum the selected products.
4. Divide by total sales.
5. Check the arithmetic manually.

```r
sales <- c(coffee = 42, tea = 35, cocoa = 18, juice = 25)
hot_drinks <- sales[c("coffee", "tea", "cocoa")]

hot_drinks
# coffee    tea  cocoa
#     42     35     18

sum(hot_drinks)
# [1] 95

sum(hot_drinks) / sum(sales)
# [1] 0.7916667
```

Checked answer: total sales are `42 + 35 + 18 + 25 = 120`. Hot drink sales are `42 + 35 + 18 = 95`. The share is `95 / 120 = 0.7916667`, or about 79.2 percent.

The name-based index is safer than `sales[c(1, 2, 3)]` because it records intent. If the vector is later reordered alphabetically or by sales volume, `sales[c("coffee", "tea", "cocoa")]` still selects the intended products.

## Code

```r
# Robust named-vector helper: select required names and fail clearly if missing.

select_named <- function(x, required) {
  missing <- setdiff(required, names(x))
  if (length(missing) > 0) {
    stop("Missing required names: ", paste(missing, collapse = ", "))
  }
  x[required]
}

sales <- c(coffee = 42, tea = 35, cocoa = 18, juice = 25)
chosen <- select_named(sales, c("tea", "coffee"))

share <- sum(chosen) / sum(sales)
result <- data.frame(
  group_total = sum(chosen),
  all_total = sum(sales),
  share = share
)

print(result)
```

The helper function is intentionally defensive. It does not let a missing name silently turn into `NA`; it checks the requested names first and stops with a clear message if any are absent. This is especially useful in analysis scripts that depend on column names or named summary vectors. A typo such as `"cofee"` should be caught at the lookup step, not several calculations later after an `NA` has contaminated a result.

Indexing code is easiest to debug when the index object has a name and can be inspected. Instead of writing one dense expression, split it into `bad <- temp == -99 | temp > 60`, then inspect `bad`, then assign `temp[bad] <- NA`. For named extraction, create `required <- c("tea", "coffee")`, check `setdiff(required, names(sales))`, and only then extract. These intermediate objects document intent and make it clear whether the index is positional, logical, or character.

Recycling deserves the same explicitness. Scalar recycling is idiomatic and safe in expressions like `x + 1`; the scalar is meant to apply to every element. Longer recycling should be rare in analysis code unless the repeating pattern is part of the design, such as alternating treatment labels. If you do intend a pattern, create it with `rep(..., length.out = length(x))` so the code says the pattern is deliberate.

One reliable way to study indexing is to write the index object separately and print it. For example, create `keep <- names(sales) %in% c("tea", "coffee")`, inspect `keep`, and then run `sales[keep]`. This makes the relationship between names, logical values, and extracted elements visible. The same method works for data-frame rows: build `rows <- df$score >= 80`, check `table(rows)`, and then subset.

When replacing values, verify both the number of target positions and the replacement length. Replacing five positions with one value is normal because the one value is recycled intentionally. Replacing five positions with two values is suspicious because the pattern will recycle unevenly or fail. If a replacement expresses a rule, consider computing the replacement vector explicitly so the operation can be checked before assignment.

## Common pitfalls

- Forgetting that R indexes from 1. `x[0]` returns an empty vector; it does not return the first value.
- Mixing positive and negative positions, such as `x[c(1, -3)]`.
- Treating a logical filter of the wrong length as harmless. It may recycle and select a repeating pattern.
- Using `x["missing_name"]` without checking the result. R returns `NA` for a missing name in an atomic vector.
- Dropping names accidentally with operations that rebuild vectors. Check `names(x)` after transformations where names matter.
- Confusing `[` and `[[` when lists become involved. Vectors usually use `[`, while lists often need `[[` to extract the component itself.

## Connections

- [Vectors, arithmetic, and comparison](/cs/programming/r/vectors-arithmetic-comparison)
- [Lists and data frames](/cs/programming/r/lists-and-data-frames)
- [Factors and categorical data](/cs/programming/r/factors-and-categorical-data)
- [Apply family](/cs/programming/r/apply-family)
