---
title: Sorting Algorithms
sidebar_position: 14
---

# Sorting Algorithms

Sorting rearranges records into order by key. It is one of the best ways to compare algorithmic design techniques because many algorithms solve the same problem with different tradeoffs: selection sort is simple, insertion sort adapts to nearly sorted input, quicksort partitions, merge sort divides and combines, heap sort uses a priority structure, and radix sort escapes comparison sorting by processing digits.

The source textbook has a full sorting chapter after graphs. It covers internal sorting methods such as insertion, quick, merge, heap, and radix sort, and also discusses external sorting. This page focuses on the standard in-memory algorithms from a C data-structures course, while keeping the connection to arrays, heaps, and searching visible.

## Definitions

A **sorting problem** takes a sequence of records:

$$
\langle r_0, r_1, \dots, r_{n-1}\rangle
$$

with keys $k_i$ and rearranges the records so that:

$$
k_0 \le k_1 \le \cdots \le k_{n-1}
$$

Important properties:

- **Stable sort**: records with equal keys keep their original relative order.
- **In-place sort**: uses only $O(1)$ or small auxiliary memory beyond the input array, ignoring recursion stack in some definitions.
- **Adaptive sort**: runs faster on inputs that are already nearly sorted.
- **Comparison sort**: learns order only by comparing keys. Any comparison sort has $\Omega(n \log n)$ worst-case lower bound.
- **Distribution sort**: uses key structure, such as digits or ranges, rather than only comparisons.

Core algorithms:

- **Selection sort**: repeatedly select the minimum remaining item and place it next.
- **Insertion sort**: grow a sorted prefix by inserting the next item into its correct position.
- **Bubble sort**: repeatedly swap adjacent out-of-order pairs.
- **Quicksort**: partition around a pivot, then recursively sort the sides.
- **Merge sort**: recursively sort halves, then merge two sorted sequences.
- **Heap sort**: build a heap, then repeatedly remove the maximum.
- **Radix sort**: sort by digits, often using stable counting sort for each digit.

## Key results

Selection sort always performs $\Theta(n^2)$ comparisons, regardless of input order. It performs relatively few swaps, so it can be useful when swaps are extremely expensive, but it is rarely the best general-purpose sort.

Insertion sort has worst-case $\Theta(n^2)$ time but best-case $\Theta(n)$ when the array is already sorted. It is simple, stable, and excellent for small arrays or nearly sorted data.

Quicksort has average $\Theta(n \log n)$ time and excellent cache behavior, but worst-case $\Theta(n^2)$ if pivots are consistently poor. Randomized pivots or median-of-three pivots reduce that risk.

Merge sort guarantees $\Theta(n \log n)$ time and is stable when implemented carefully, but array merge sort needs $\Theta(n)$ extra memory.

Heap sort guarantees $\Theta(n \log n)$ time and can sort in place, but it is usually not stable and often has less friendly cache behavior than quicksort.

Radix sort can run in $O(d(n + b))$, where `d` is the number of digits or passes and `b` is the base. It is not a comparison sort, so the comparison lower bound does not apply.

| Algorithm | Best | Average | Worst | Extra space | Stable? |
|---|---:|---:|---:|---:|---|
| Selection | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | no |
| Insertion | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | yes |
| Bubble | $O(n)$ with early stop | $O(n^2)$ | $O(n^2)$ | $O(1)$ | yes |
| Quicksort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ average stack | no typical |
| Merge sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | yes |
| Heap sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | no |
| Radix sort | $O(d(n+b))$ | $O(d(n+b))$ | $O(d(n+b))$ | $O(n+b)$ | yes if digit sort stable |

The right sorting algorithm depends on record size and movement cost. If records are large, it may be better to sort an array of pointers or indices rather than move entire records repeatedly. Stability matters when sorting by multiple keys: for example, sorting student records by first name and then using a stable sort by last name preserves first-name order among equal last names. If stability is not required, quicksort or heap sort may be simpler.

Sorting also changes the cost of later operations. A sorted array supports binary search in $O(\log n)$ time and makes duplicate grouping easy. But maintaining sorted order during frequent insertions can be expensive because array insertion shifts elements. This is why dictionaries with frequent updates often use search trees or hash tables instead of repeatedly sorting arrays.

For C implementations, comparison functions must impose a consistent order. A `qsort` comparator should return negative, zero, or positive according to the two records; returning only `a - b` can overflow for large integers. Careful comparator design is part of the data-structure contract.

For nearly sorted arrays, insertion sort is often used as a finishing pass inside more complex sorts because its constant factors are small.

## Visual

```mermaid
flowchart TD
  Input["Input array A(0..n-1"]"] --> Choice{"Algorithm structure"}

  subgraph Merge["Merge sort recursion"]
    direction TB
    M0["Split A(lo..hi"] at mid"]
    M1["Recursively sort left half"]
    M2["Recursively sort right half"]
    M3["Merge two sorted runs into auxiliary array"]
    M4["Copy merged run back to A(lo..hi"]"]
    M0 --> M1
    M0 --> M2
    M1 --> M3
    M2 --> M3
    M3 --> M4
  end

  subgraph Quick["Quicksort partition"]
    direction TB
    Q0["Choose pivot, e.g. 6"]
    Q1["Scan and swap so elements < pivot move left"]
    Q2["Place pivot in final position"]
    Q3["Recurse on left and right partitions"]
    Q0 --> Q1
    Q1 --> Q2
    Q2 --> Q3
  end

  subgraph Heap["Heap sort"]
    direction TB
    H0["Build max heap bottom-up in array"]
    H1["Swap root max with last unsorted slot"]
    H2["Shrink heap size by one"]
    H3["Sift down new root"]
    H0 --> H1
    H1 --> H2
    H2 --> H3
    H3 --> H1
  end

  subgraph Radix["Radix sort"]
    direction TB
    R0["For each digit from least to most significant"]
    R1["Stable counting sort by current digit"]
    R0 --> R1
    R1 --> R0
  end

  Choice -- "stable comparison sort" --> Merge
  Choice -- "cache-friendly average fast comparison sort" --> Quick
  Choice -- "in-place worst-case n log n" --> Heap
  Choice -- "fixed-width digit keys" --> Radix
  Merge --> Output(("Sorted records"))
  Quick --> Output
  Heap --> Output
  Radix --> Output
```

This sorting diagram compares the internal state machines of the major sorting families rather than only choosing among names. Merge sort labels the split-sort-merge-copy recursion, quicksort labels pivot partitioning and recursive subarrays, heap sort labels build-heap and repeated root removal, and radix sort labels stable digit passes. The output node is shared because all paths satisfy the same sorting contract while using different invariants, memory, and stability trade-offs.

## Worked example 1: insertion sort trace

Problem: Sort `[8, 3, 5, 2, 9]` using insertion sort.

Method: maintain a sorted prefix. At step `i`, insert `a[i]` into `a[0..i-1]`.

1. Start with prefix `[8]` sorted.
2. Insert `3` into `[8]`:
   - Compare `8 > 3`, shift `8` right.
   - Place `3` at index `0`.
   - Array: `[3, 8, 5, 2, 9]`.
3. Insert `5` into `[3, 8]`:
   - Compare `8 > 5`, shift `8` right.
   - Compare `3 <= 5`, stop.
   - Place `5` after `3`.
   - Array: `[3, 5, 8, 2, 9]`.
4. Insert `2` into `[3, 5, 8]`:
   - Shift `8`, shift `5`, shift `3`.
   - Place `2` at index `0`.
   - Array: `[2, 3, 5, 8, 9]`.
5. Insert `9` into `[2, 3, 5, 8]`:
   - `8 <= 9`, no shift.
   - Array remains `[2, 3, 5, 8, 9]`.

Checked answer: final array is sorted. The trace also shows adaptiveness: inserting `9` into an already-correct position took one comparison and no shifts.

## Worked example 2: merge step

Problem: Merge sorted arrays `L = [2, 5, 8]` and `R = [1, 3, 9]`.

Method: keep one pointer into each array and repeatedly copy the smaller current item.

1. Compare `2` and `1`. Copy `1` from `R`. Output: `[1]`.
2. Compare `2` and `3`. Copy `2` from `L`. Output: `[1, 2]`.
3. Compare `5` and `3`. Copy `3` from `R`. Output: `[1, 2, 3]`.
4. Compare `5` and `9`. Copy `5` from `L`. Output: `[1, 2, 3, 5]`.
5. Compare `8` and `9`. Copy `8` from `L`. Output: `[1, 2, 3, 5, 8]`.
6. `L` is exhausted. Copy remaining `9` from `R`.

Checked answer: merged output is `[1, 2, 3, 5, 8, 9]`. Each step chose the smallest not-yet-copied item among the two sorted prefixes, so the result is sorted.

## Code

This C program implements quicksort using Lomuto partitioning for a compact runnable example. Production quicksorts often use better pivot selection and switch to insertion sort for small partitions.

```c
#include <stdio.h>
#include <stdlib.h>

static void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

static int partition(int a[], int lo, int hi) {
    int pivot = a[hi];
    int i = lo;
    for (int j = lo; j < hi; ++j) {
        if (a[j] <= pivot) {
            swap(&a[i], &a[j]);
            i++;
        }
    }
    swap(&a[i], &a[hi]);
    return i;
}

static void quicksort(int a[], int lo, int hi) {
    if (lo >= hi) return;
    int p = partition(a, lo, hi);
    quicksort(a, lo, p - 1);
    quicksort(a, p + 1, hi);
}

static void print_array(const int a[], int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d%s", a[i], i + 1 == n ? "\n" : " ");
    }
}

int main(void) {
    int a[] = {9, 3, 7, 1, 6, 2, 8};
    int n = (int)(sizeof(a) / sizeof(a[0]));
    quicksort(a, 0, n - 1);
    print_array(a, n);
    return EXIT_SUCCESS;
}
```

## Common pitfalls

- Calling every $O(n \log n)$ algorithm "the same." Stability, memory, worst-case behavior, and constant factors matter.
- Implementing quicksort partition so the pivot is not moved into its final position.
- Forgetting that merge sort needs auxiliary storage for array merging.
- Using bubble sort by default. It is mainly pedagogical; insertion sort is usually better for simple small-array sorting.
- Assuming radix sort applies to arbitrary comparison keys. It needs key structure and a stable digit-level sort.
- Breaking stability by swapping equal keys across each other.

## Connections

- [arrays and array operations](/cs/data-structures/arrays)
- [heaps and priority queues](/cs/data-structures/heaps-priority-queues)
- [searching algorithms](/cs/data-structures/searching-algorithms)
- [binary search trees](/cs/data-structures/binary-search-trees)
- [minimum spanning trees](/cs/data-structures/minimum-spanning-trees)
