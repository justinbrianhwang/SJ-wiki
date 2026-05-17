---
title: Big-O Notation
sidebar_position: 2
---

# Big-O Notation

**Big-O notation** describes the asymptotic upper bound of a function's growth rate. It's how we compare algorithm efficiency without caring about constants or hardware.

![A square Kufic algorithms mark introduces the study of designed procedures.](https://commons.wikimedia.org/wiki/Special:FilePath/Algorithms.svg)

*Figure: The algorithms mark gives the abstract algorithms pages a concrete visual anchor. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Algorithms.svg), Jeff Erickson, CC BY 4.0.*

## Formal definition

We say $f(n) = O(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$
0 \le f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0
$$

In plain English: $f$ grows at most as fast as $g$, up to a constant factor, for sufficiently large $n$.

## Common complexity classes

| Notation        | Name              | Example                          |
| --------------- | ----------------- | -------------------------------- |
| $O(1)$          | Constant          | Array index access               |
| $O(\log n)$     | Logarithmic       | Binary search                    |
| $O(n)$          | Linear            | Linear search                    |
| $O(n \log n)$   | Linearithmic      | Merge sort, heap sort            |
| $O(n^2)$        | Quadratic         | Bubble sort, naive matrix mult.  |
| $O(n^3)$        | Cubic             | Standard matrix multiplication   |
| $O(2^n)$        | Exponential       | Brute-force subset enumeration   |
| $O(n!)$         | Factorial         | Naive traveling salesman         |

## Example: linear search

```python
def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
```

The loop runs at most $n$ times, so this is $O(n)$.

## Example: binary search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Each iteration halves the search space, so it takes $O(\log n)$ time.

:::warning
Big-O describes the **worst case**. Big-Θ (theta) describes a tight bound; Big-Ω (omega) describes a lower bound. Don't conflate them.
:::

## Related

- [Vectors](../../math/linear-algebra/vectors) — linear algebra cost analysis often uses these bounds.
