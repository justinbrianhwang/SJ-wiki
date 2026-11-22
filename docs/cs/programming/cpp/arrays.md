---
title: Arrays
sidebar_position: 4
---

# Arrays

Arrays collect many values of the same type under one name. They are useful when a program needs indexed repetition: scores for a class, production totals for plants, characters in a word, or rows and columns in a table. Savitch uses arrays to introduce memory layout, array parameters, partially filled arrays, searching, sorting, and multidimensional data.

The key insight is that an array gives constant-time access by index, but C++ does not automatically remember or enforce every boundary in ordinary built-in arrays. The programmer must carry the size, distinguish capacity from the number of used elements, and avoid reading or writing outside the declared range.

## Storage, indices, and the size contract

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

Contiguity gives array indexing its usual constant-time cost. If the address of the first element is $B$ and one element occupies $s$ bytes, the address calculation is

$$
\operatorname{address}(a[i]) = B + i s.
$$

No scan through elements $0$ to $i-1$ occurs. The compiler scales the index by the element size and adds it to the base address. The same calculation also explains why an out-of-range subscript is dangerous: the machine can still form an address, but that address does not designate an element of the array. Reading or writing through it has undefined behavior. C++ does not promise a clean error, and an apparently successful run supplies no evidence that the program is correct.

An initializer may determine the bound:

```cpp
int primes[] = {2, 3, 5, 7}; // exactly four elements
```

When fewer initializers than the declared bound are supplied, the remaining elements are value-initialized. For an `int` array, that means zero:

```cpp
int counts[5] = {3, 1}; // {3, 1, 0, 0, 0}
int zeros[5] = {};      // all zero
```

That rule applies only when initialization occurs. A local declaration such as `int counts[5];` leaves its elements with indeterminate values. Reading one before assigning it is undefined behavior.

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

The brackets in that parameter are misleading if read as “an array value.” In a function parameter, `const int a[]` is adjusted to `const int* a`. Only a pointer to the first element arrives. These two declarations therefore describe the same function type:

```cpp
void printArray(const int a[], int used);
void printArray(const int* a, int used);
```

Consequently, `sizeof(a)` inside `printArray` is the size of a pointer, not the byte size of the caller's array. Dividing it by `sizeof(a[0])` cannot recover the element count. The caller and callee need an explicit size contract, or the function should accept a type that retains its size.

For a genuinely fixed bound, a reference-to-array parameter preserves the extent:

```cpp
template <std::size_t N>
void printFixed(const int (&a)[N]) {
    for (std::size_t i = 0; i < N; ++i) {
        std::cout << a[i] << ' ';
    }
}
```

Modern interfaces more often use `std::array<T, N>` for a fixed-size value or `std::span<T>` for a non-owning view whose length travels with it. `std::vector<T>` owns a variable-size sequence. Built-in arrays remain important at language boundaries, in embedded code, and for understanding the storage model beneath those abstractions.

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

C++ stores a built-in two-dimensional array in row-major order: every element of row zero comes first, followed by every element of row one, and so on. For `int table[ROWS][COLS]`, the logical entry `table[r][c]` lies at flat offset

$$
r\,COLS + c.
$$

The compiler needs `COLS` to compute that offset, which is the reason the later dimension cannot be omitted from the parameter type. The rows themselves have no padding requirement between them beyond whatever is already implied by the element type; a row is an array of `COLS` integers.

## Capacity, used length, and algorithm invariants

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

The distinction between capacity and used length is a small data-structure invariant. It can be written as

$$
0 \le used \le capacity.
$$

Every insertion must preserve it. The correct order is to check room, write at index `used`, and then increment `used`. Incrementing first skips index zero and can eventually write one element beyond the allocation. Removal from the end moves in the opposite order: first decrement `used`, then treat the old last element as outside the meaningful prefix. Nothing has to be erased for an `int` array; the count decides which slots belong to the sequence.

Selection sort is a useful first exercise in invariants because each outer iteration enlarges a settled prefix. Suppose the invariant holds before pass $k$. Scanning the suffix finds its least value, and swapping that value into position $k$ places the next-smallest original element immediately after the already settled prefix. The prefix remains sorted because every old prefix element is no larger than the new element. Induction then proves the claim for every pass. After $n-1$ passes, only one value remains, so the whole used portion is sorted.

The number of comparisons does not depend on the original order:

$$
(n-1)+(n-2)+\cdots+1 = \frac{n(n-1)}{2}.
$$

Selection sort therefore takes quadratic time even on an already sorted array. Its compensating property is a low number of swaps: at most $n-1$. That can matter when moving an element is much more expensive than comparing two elements, though library sorting algorithms are normally the better choice.

## Reading the memory sketch

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

The question marks mean “not part of the logical sequence,” not necessarily “physically uninitialized.” With the initializer shown, the last three integers are actually zero because aggregate initialization fills omitted entries. In a general partially filled array, unused slots may contain old values or indeterminate values. Algorithms should ignore them either way. Logical membership is controlled by `used`.

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

## Worked example: sequential search in a partially filled array

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

The loop invariant is: before testing index $i$, none of the indexes from $0$ through $i-1$ contains the target. It is true initially because that range is empty. A failed comparison extends the known-absent range by one. A successful comparison returns the first match, while reaching `i == used` proves that the entire meaningful prefix was checked. This argument covers an empty prefix too: the loop body runs zero times and the function returns `-1`.

## Worked example: two passes of selection sort

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

Continuing the trace gives pass 2 over `{10, 8, 16}`. The least value is `8` at index `3`, so indexes `2` and `3` are swapped, producing `{2, 6, 8, 10, 16}`. Pass 3 scans `{10, 16}`, finds that `10` is already least, and changes nothing. The final one-element suffix needs no pass.

## A complete fixed-capacity example

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

## Boundary failures and misleading syntax

- Using index `size` as if it were valid. The last valid index is `size - 1`.
- Forgetting that array indexes start at zero.
- Passing an array without passing its used size or capacity.
- Writing past the end of a partially filled array when `used == capacity`.
- Omitting `const` on array parameters that should not modify the array.
- Returning a built-in local array from a function. The local array disappears when the function returns.
- Confusing capacity with used size in loops.
- Assuming assignment copies built-in arrays. Built-in arrays are not assigned as whole values.

For array code:

- Write the loop bounds in words before coding them. For a used portion of length `used`, the valid indexes are `0` through `used - 1`; a loop that visits every used element should test `i < used`, not `i <= used`.
- Keep capacity tests close to insertion. A partially filled array changes state when `used` is incremented, so the safest pattern is check `used < capacity`, assign into `a[used]`, then increment `used`.
- Decide whether a function is allowed to change the array. If the answer is no, the parameter should be `const int a[]`; if the answer is yes, the function name should make the mutation clear, such as `sort`, `read`, or `replace`.
- Test three cases for every array algorithm: an empty used portion, a one-element used portion, and a full used portion. These cases expose most off-by-one and capacity mistakes.
- Separate searching from reporting. A search function should usually return an index or `-1`; printing "not found" inside the search makes the function harder to reuse in a larger program.
- Remember that a two-dimensional array parameter must know the second dimension at compile time in ordinary C++ array syntax. If the dimensions need to vary freely, a `vector` of `vector` objects or a flat dynamic representation is often cleaner.

If an array function receives `int a[]`, `int capacity`, and `int& used`, identify which parameter represents storage, which prevents overflow, and which reports how many values are meaningful. Then ask whether the function should change `used`; searching should not, reading usually should, and sorting should not change it even though it changes element order.

One more distinction matters when choosing an interface:

| Type | Owns elements | Size stored at run time | Can grow | Copies as a value |
|---|---:|---:|---:|---:|
| built-in `T[N]` | yes, in its enclosing object | no | no | no whole-array assignment |
| `std::array<T, N>` | yes | fixed in the type | no | yes |
| `std::span<T>` | no | yes | no | copies the view only |
| `std::vector<T>` | yes | yes | yes | yes |

`std::array` has essentially the same contiguous fixed-size storage model as a built-in array but participates in assignment, return-by-value, and standard algorithms more smoothly. `std::span` is useful for parameters because it can refer to an array, an `std::array`, or a `std::vector` without owning any of them. Its lifetime cannot exceed the storage it views.

<div className="see-also">

See also: [C++ basics and control flow](/cs/programming/cpp/cpp-basics-and-control-flow) · [functions and parameters](/cs/programming/cpp/functions-parameters-and-scope) · [strings](/cs/programming/cpp/strings) · [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory) · [STL containers](/cs/programming/cpp/stl-containers)

</div>
