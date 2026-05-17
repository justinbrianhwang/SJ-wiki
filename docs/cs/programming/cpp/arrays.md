---
title: Arrays
sidebar_position: 4
---

# Arrays

Arrays collect many values of the same type under one name. They are useful when a program needs indexed repetition: scores for a class, production totals for plants, characters in a word, or rows and columns in a table. Savitch uses arrays to introduce memory layout, array parameters, partially filled arrays, searching, sorting, and multidimensional data.

![The ISO C++ logo marks pages on classes, templates, containers, and modern C++ idioms.](https://commons.wikimedia.org/wiki/Special:FilePath/ISO_C%2B%2B_Logo.svg)

*Figure: C++ extends systems programming with abstraction, generic code, and deterministic resource management. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ISO_C%2B%2B_Logo.svg), Jeremy Kratz, public domain text logo.*

The key insight is that an array gives constant-time access by index, but C++ does not automatically remember or enforce every boundary in ordinary built-in arrays. The programmer must carry the size, distinguish capacity from the number of used elements, and avoid reading or writing outside the declared range.

## Definitions

An **array declaration** reserves a fixed number of elements of one base type.

```cpp
const int SIZE = 5;
int scores[SIZE];
```

If an array has size `SIZE`, valid indexes are:

$$
0, 1, 2, \ldots, SIZE - 1
$$

An **indexed variable** such as `scores[2]` behaves like a variable of the base type. Arrays are contiguous in memory, so the elements are stored one after another.

```cpp
int scores[5] = {90, 84, 72, 100, 68};
scores[2] = 75;
```

A **partially filled array** has a declared capacity and a separate count of how many elements currently hold meaningful values.

```cpp
const int CAPACITY = 100;
int values[CAPACITY];
int used = 0;
```

An **array parameter** is written with brackets, but the function does not receive the size automatically.

```cpp
void printArray(const int a[], int used) {
    for (int i = 0; i < used; ++i) {
        std::cout << a[i] << ' ';
    }
}
```

The `const` modifier prevents the function from changing the array elements through that parameter.

A **multidimensional array** uses more than one index.

```cpp
const int ROWS = 3;
const int COLS = 4;
int table[ROWS][COLS];
```

When a multidimensional array is passed to a function, all dimensions except the first must be known in the parameter type.

```cpp
void printTable(const int table[][4], int rows);
```

## Key results

Built-in arrays are efficient but low-level. Passing an array to a function passes enough information to find the first element, not a copy of all elements and not the declared size. Therefore, a function can change an array argument unless the parameter is `const`.

Searching an unsorted array is usually a sequential scan. In the worst case, the target is absent or appears at the last checked position, so the algorithm examines all `n` used elements. Its running time is $O(n)$.

Selection sort repeatedly finds the smallest remaining item and swaps it into the next sorted position. It is easy to reason about and works in-place, but it performs $O(n^2)$ comparisons.

The invariant for selection sort after `k` passes is:

$$
\begin{aligned}
&a[0], a[1], \ldots, a[k - 1]\text{ are sorted, and}\\
&\text{they are the }k\text{ smallest elements of the original array.}
\end{aligned}
$$

Array code should separate three numbers:

| Term | Meaning | Example |
|---|---|---|
| capacity | declared maximum storage | `100` in `int a[100]` |
| used size | meaningful elements now present | `used == 37` |
| last valid used index | final initialized slot | `used - 1` |

The STL `std::vector` reduces several risks by storing its current size and supporting growth. Savitch previews `vector` before the full STL because it behaves like a safer, resizable array for many beginner programs.

## Visual

```text
Declaration: int a[6] = {4, 8, 15};

capacity: 6
used:     3

index:    0    1    2    3    4    5
       +----+----+----+----+----+----+
value: |  4 |  8 | 15 | ?? | ?? | ?? |
       +----+----+----+----+----+----+
          meaningful     not meaningful yet
```

```mermaid
flowchart TD
  A[Start selection sort pass k] --> B["Assume minIndex = k"]
  B --> C[Scan indexes k+1 to used-1]
  C --> D{"a[i] < a[minIndex]?"}
  D -->|yes| E["Set minIndex = i"]
  D -->|no| F[Keep minIndex]
  E --> G{"More indexes?"}
  F --> G
  G -->|yes| C
  G -->|no| H[Swap a[k] and a[minIndex]]
  H --> I[Next pass]
```

## Worked example 1: sequential search in a partially filled array

Problem: Given `values = {12, 7, 9, 7, 30}` and `used = 5`, find the first index containing `7`. If absent, return `-1`.

Method:

1. Start at index `0`.
2. Compare `values[0]` with target `7`.

$$
12 \ne 7
$$

3. Move to index `1`.
4. Compare `values[1]` with target `7`.

$$
7 = 7
$$

5. Stop immediately because the first occurrence was found.
6. Return index `1`.

```cpp
#include <iostream>

int search(const int values[], int used, int target) {
    for (int i = 0; i < used; ++i) {
        if (values[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    int values[] = {12, 7, 9, 7, 30};
    int index = search(values, 5, 7);
    std::cout << index << '\n';
}
```

Checked answer: the output is `1`. The later `7` at index `3` is not returned because the algorithm stops at the first match.

## Worked example 2: one pass of selection sort

Problem: Sort the array prefix `{8, 6, 10, 2, 16}`. Show the first two passes of selection sort.

Method:

Initial state:

```text
index: 0  1   2   3   4
value: 8  6  10   2  16
```

Pass 0:

1. Search indexes `0..4` for the smallest value.
2. Current minimum starts at index `0`, value `8`.
3. Index `1`: `6 < 8`, so minimum becomes index `1`.
4. Index `2`: `10 < 6` is false.
5. Index `3`: `2 < 6`, so minimum becomes index `3`.
6. Index `4`: `16 < 2` is false.
7. Swap index `0` and index `3`.

After pass 0:

```text
2  6  10  8  16
```

Pass 1:

1. The sorted prefix is `{2}`.
2. Search indexes `1..4`.
3. Current minimum starts at index `1`, value `6`.
4. Values `10`, `8`, and `16` are all greater than `6`.
5. Minimum remains index `1`, so the swap keeps the array unchanged.

After pass 1:

```text
2  6  10  8  16
```

Checked answer: after two passes, the two smallest values are in their final positions: `2` and `6`.

## Code

This program reads a partially filled array, prints it, sorts it, and searches it.

```cpp
#include <iostream>

const int CAPACITY = 20;

void readValues(int a[], int capacity, int& used) {
    used = 0;
    int next;
    while (used < capacity && std::cin >> next && next >= 0) {
        a[used] = next;
        ++used;
    }
}

int indexOfSmallest(const int a[], int start, int used) {
    int minIndex = start;
    for (int i = start + 1; i < used; ++i) {
        if (a[i] < a[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

void swapValues(int& left, int& right) {
    int temp = left;
    left = right;
    right = temp;
}

void selectionSort(int a[], int used) {
    for (int i = 0; i < used - 1; ++i) {
        int minIndex = indexOfSmallest(a, i, used);
        swapValues(a[i], a[minIndex]);
    }
}

void printArray(const int a[], int used) {
    for (int i = 0; i < used; ++i) {
        std::cout << a[i] << ' ';
    }
    std::cout << '\n';
}

int main() {
    int values[CAPACITY];
    int used;

    std::cout << "Enter nonnegative integers, end with a negative value:\n";
    readValues(values, CAPACITY, used);
    selectionSort(values, used);
    printArray(values, used);
}
```

## Common pitfalls

- Using index `size` as if it were valid. The last valid index is `size - 1`.
- Forgetting that array indexes start at zero.
- Passing an array without passing its used size or capacity.
- Writing past the end of a partially filled array when `used == capacity`.
- Omitting `const` on array parameters that should not modify the array.
- Returning a built-in local array from a function. The local array disappears when the function returns.
- Confusing capacity with used size in loops.
- Assuming assignment copies built-in arrays. Built-in arrays are not assigned as whole values.

Diagnostic checks for array code:

- Write the loop bounds in words before coding them. For a used portion of length `used`, the valid indexes are `0` through `used - 1`; a loop that visits every used element should test `i < used`, not `i <= used`.
- Keep capacity tests close to insertion. A partially filled array changes state when `used` is incremented, so the safest pattern is check `used < capacity`, assign into `a[used]`, then increment `used`.
- Decide whether a function is allowed to change the array. If the answer is no, the parameter should be `const int a[]`; if the answer is yes, the function name should make the mutation clear, such as `sort`, `read`, or `replace`.
- Test three cases for every array algorithm: an empty used portion, a one-element used portion, and a full used portion. These cases expose most off-by-one and capacity mistakes.
- Separate searching from reporting. A search function should usually return an index or `-1`; printing "not found" inside the search makes the function harder to reuse in a larger program.
- Remember that a two-dimensional array parameter must know the second dimension at compile time in ordinary C++ array syntax. If the dimensions need to vary freely, a `vector` of `vector` objects or a flat dynamic representation is often cleaner.

Quick self-test: if an array function receives `int a[]`, `int capacity`, and `int& used`, identify which parameter represents storage, which prevents overflow, and which reports how many values are meaningful. Then ask whether the function should change `used`; searching should not, reading usually should, and sorting should not change it even though it changes element order.

## Connections

- [C++ basics and control flow](/cs/programming/cpp/cpp-basics-and-control-flow)
- [functions and parameters](/cs/programming/cpp/functions-parameters-and-scope)
- [strings](/cs/programming/cpp/strings)
- [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory)
- [STL containers](/cs/programming/cpp/stl-containers)
