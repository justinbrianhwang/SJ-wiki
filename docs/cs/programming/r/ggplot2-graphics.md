---
title: ggplot2 Graphics
sidebar_position: 15
---

# ggplot2 Graphics

The book introduces `ggplot2` as a grammar-of-graphics alternative to base plotting. Instead of drawing a figure procedurally, `ggplot2` builds a plot from a data frame, aesthetic mappings, geometric layers, scales, facets, coordinates, and themes. This structure is especially strong when a plot should encode multiple variables consistently or produce a family of related panels.

The central shift is from "draw points, then add a line" to "declare the data, map variables to visual properties, and add layers that use those mappings." Once that grammar is understood, scatterplots, histograms, smoothers, facets, and density plots become variations on the same template.

## Definitions

`ggplot(data, aes(...))` starts a plot with a data frame and default aesthetic mappings. Aesthetic mappings connect variables to visual properties such as `x`, `y`, `color`, `fill`, `shape`, and `size`.

A **geom** is a geometric layer that draws something. Common examples include `geom_point`, `geom_line`, `geom_smooth`, `geom_histogram`, `geom_boxplot`, `geom_bar`, and `geom_density`.

A **mapping** is data-driven and belongs inside `aes()`. A **setting** is a constant and belongs outside `aes()`. For example, `aes(color = Species)` maps color to a variable, while `color = "steelblue"` sets every point to the same color.

A **facet** splits a plot into panels by one or more variables. `facet_wrap(~ Species)` creates one panel per species.

A **theme** controls non-data display elements such as grid lines, text size, background, and legend position. A **scale** controls how data values become visual values.

## Key results

The common `ggplot2` build pattern is:

```r
ggplot(data, aes(x = ..., y = ...)) +
  geom_...() +
  scale_...() +
  facet_...() +
  labs(...) +
  theme_...()
```

Not every plot needs every part. The minimum useful plot is usually data, mapping, and one geom.

| Component | Example | Role |
|---|---|---|
| Data | `ggplot(iris, ...)` | Source data frame |
| Mapping | `aes(Sepal.Length, Petal.Length)` | Variables to visual properties |
| Geom | `geom_point()` | What gets drawn |
| Statistical transformation | `geom_smooth(method = "lm")` | Compute then draw |
| Scale | `scale_color_brewer()` | Control visual encoding |
| Facet | `facet_wrap(~ Species)` | Split into panels |
| Labels | `labs(title = ..., x = ...)` | Human-readable text |
| Theme | `theme_minimal()` | Non-data styling |

The mapping-vs-setting distinction is the most common beginner issue. If you write `aes(color = "red")`, ggplot treats `"red"` as a data category and creates a legend. If you write `color = "red"` outside `aes()`, all points are red.

`ggplot2` expects tidy-ish rectangular data: one row per observation, variables in columns, and grouping variables stored explicitly. It can plot wide data, but many multi-series plots become easier after reshaping to long format.

## Visual

```mermaid
flowchart TD
  A[Data frame] --> B[ggplot data and aes mappings]
  B --> C[Geometric layers]
  C --> D[Scales]
  D --> E[Facets]
  E --> F[Coordinates]
  F --> G[Theme and labels]
  G --> H[Rendered plot]
```

| Mapping or setting | Code | Meaning |
|---|---|---|
| Mapped color | `aes(color = Species)` | Color varies by data |
| Constant color | `color = "steelblue"` | Every layer item uses same color |
| Mapped size | `aes(size = Sepal.Width)` | Size encodes numeric variable |
| Constant alpha | `alpha = 0.6` | Every item is partly transparent |

## Worked example 1: Scatterplot with linear smooth by group

Problem: create a scatterplot of petal length against sepal length in `iris`, color by species, and add a separate linear trend for each species.

Method:

1. Load `ggplot2`.
2. Start with `iris` as the data frame.
3. Map sepal length to x, petal length to y, and species to color.
4. Add points.
5. Add a linear smoother with `method = "lm"` and no standard-error ribbon.
6. Add labels.

```r
library(ggplot2)

p <- ggplot(
  iris,
  aes(x = Sepal.Length, y = Petal.Length, color = Species)
) +
  geom_point(size = 2, alpha = 0.8) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(
    title = "Petal length increases with sepal length",
    x = "Sepal length",
    y = "Petal length",
    color = "Species"
  ) +
  theme_minimal()

print(p)
```

Checked answer: because `color = Species` is inside the initial `aes()`, both `geom_point()` and `geom_smooth()` inherit the grouping. The result is one color per species and a separate fitted line per species. If the color mapping were removed from `aes()`, the smoother would fit one overall line unless grouping were supplied separately.

This is the grammar in action: data and mappings are declared once, then layers use them consistently.

## Worked example 2: Faceted histogram with constant fill

Problem: show the distribution of `mpg` in `mtcars` separately for 4-, 6-, and 8-cylinder cars, using facets and a constant fill color.

Method:

1. Copy `mtcars` and convert `cyl` to a factor for categorical display.
2. Start `ggplot` with `mpg` mapped to x.
3. Add `geom_histogram` with a constant fill outside `aes()`.
4. Facet by cylinder group.
5. Check that fill is not mapped to a variable.

```r
library(ggplot2)

cars <- mtcars
cars$cyl <- factor(cars$cyl)

ggplot(cars, aes(x = mpg)) +
  geom_histogram(binwidth = 3, fill = "gray70", color = "white") +
  facet_wrap(~ cyl, nrow = 1) +
  labs(
    title = "Fuel economy distribution by cylinder count",
    x = "Miles per gallon",
    y = "Number of cars"
  ) +
  theme_minimal()
```

Checked answer: `facet_wrap(~ cyl)` creates one panel for each cylinder level. The fill is constant because `fill = "gray70"` is outside `aes()`. No fill legend is needed because fill does not encode data.

The plot answers a different question than a single histogram: it shows how the distribution shifts across cylinder groups rather than mixing all cars in one panel.

## Code

```r
# Reusable ggplot function for a scatterplot with optional faceting.

library(ggplot2)

scatter_by_group <- function(df, x, y, color, facet = NULL) {
  mapping <- aes(
    x = .data[[x]],
    y = .data[[y]],
    color = .data[[color]]
  )

  p <- ggplot(df, mapping) +
    geom_point(size = 2, alpha = 0.75) +
    geom_smooth(method = "lm", se = FALSE) +
    labs(x = x, y = y, color = color) +
    theme_minimal()

  if (!is.null(facet)) {
    p <- p + facet_wrap(vars(.data[[facet]]))
  }

  p
}

scatter_by_group(iris, "Sepal.Length", "Petal.Length", "Species")
```

## Common pitfalls

- Putting constants inside `aes()`, such as `aes(color = "red")`, and accidentally creating a legend.
- Forgetting to convert numeric codes such as cylinder count to factors when they should be categories.
- Adding too many aesthetics to one plot. Color, shape, size, alpha, and facets can overload a reader.
- Expecting `ggplot2` to modify data. It visualizes the data supplied; cleaning and reshaping should be explicit.
- Forgetting `print(p)` when creating ggplot objects inside functions or non-interactive scripts.
- Using a smoother without understanding the method. LOESS and linear model smoothers answer different questions.

## Connections

- [Base graphics](/cs/programming/r/base-graphics)
- [Descriptive statistics](/cs/programming/r/descriptive-statistics)
- [Advanced graphics and 3D plots](/cs/programming/r/advanced-graphics-3d)
- [Linear and generalized models](/cs/programming/r/linear-and-generalized-models)
