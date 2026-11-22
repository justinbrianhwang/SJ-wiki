---
title: Arrays and Array Operations
sidebar_position: 2
---

# Arrays and Array Operations

An array couples a simple abstract idea—a finite sequence—with a strong storage promise: equal-sized elements occupy one contiguous block. That promise gives constant-time indexing and good sequential access, but it also explains nearly every awkward array operation. Growing may require a new block. Insertion opens a gap by moving a suffix. Removing an element closes one. A raw C array carries no length at run time, so the program has to preserve that information separately.

Arrays are therefore a useful boundary between data-structure analysis and machine behavior. The index formula proves the asymptotic access cost. Element size, alignment, cache lines, and memory ownership explain the observed cost.

## The contiguous-memory contract

For an array $A$ with base address $B$, element width $w$, and zero-based index $i$,

$$
\operatorname{addr}(A[i])=B+iw.
$$

The multiplication and addition do not depend on the number of elements, so access takes $O(1)$ time in the usual random-access machine model. “Constant time” does not mean equal latency for every access. A cached element can arrive much faster than one fetched from main memory, but neither access scans the preceding elements.

In C, `a[i]` is defined in terms of pointer arithmetic as `*(a + i)`. Adding one to an `int *` advances by `sizeof(int)` bytes; the compiler incorporates the scaling. The legal indices of `int a[10]` are `0` through `9`. Forming or dereferencing an out-of-range element does not invoke a hidden bounds check. Dereferencing it has undefined behavior, which means the language places no requirement on the result.

An array type and a pointer type are still different. For a declaration `int a[10]`, `sizeof(a)` is the size of all ten integers in the scope where `a` is an actual array. In most expressions, however, `a` is converted to a pointer to its first element. A function parameter written `int a[]` is adjusted to `int *a`; `sizeof(a)` inside that function measures the pointer, not the caller's array.

That conversion is often called **array-to-pointer decay**. There are exceptions, including use as the operand of `sizeof` and unary `&`. The address `&a` and the value produced from `a` point at the same initial byte, but their types differ: one points to the whole array, the other to its first element. Pointer arithmetic on them consequently has different strides.

An array module usually tracks three quantities separately:

- `data`, the address of the allocated block;
- `size`, the number of constructed or logically valid elements;
- `capacity`, the number of element slots the block can hold.

The invariant is $0\leq\text{size}\leq\text{capacity}$. Reading `data[i]` requires $i\lt \text{size}$, not merely $i\lt \text{capacity}$. Spare capacity is allocated storage, not initialized logical content.

## Rows are linear underneath

C stores a built-in multidimensional array in row-major order. For `A[rows][cols]`, all elements of row zero come first, followed by row one. The address of $A[i][j]$ is

$$
\operatorname{addr}(A[i][j])=B+(i\cdot\mathrm{cols}+j)w.
$$

The type preserves the row width. If `A` is declared as `int A[4][5]`, then after conversion it points to an array of five integers. Incrementing that pointer skips an entire row. A callee that receives such an array must know every dimension except possibly the first so it can calculate the stride.

The formula generalizes. For a row-major three-dimensional array with extents $D_1,D_2,D_3$, element $(i,j,k)$ has linear index

$$
(iD_2+j)D_3+k.
$$

The rightmost index varies fastest. Other languages and libraries may choose column-major storage or accept explicit strides, so the source language's convention should not be assumed at an interface.

### Worked example: address of a matrix element

Suppose `int m[4][5]` begins at byte address `1000` and `sizeof(int)` is `4`. Find the address of `m[2][3]`.

The first two complete rows contain $2\cdot5=10$ elements. Moving to column three advances another three elements:

$$
\begin{aligned}
\text{linear index} &= 2\cdot5+3 \\
&=13.
\end{aligned}
$$

Convert the element offset to bytes:

$$
13\cdot4=52\ \text{bytes}.
$$

Add that displacement to the base address:

$$
1000+52=1052.
$$

The row ranges provide a check. Row zero uses linear indices $0$–$4$, row one uses $5$–$9$, and row two uses $10$–$14$. Column three of row two is indeed index $13$.

Loop order affects locality. Traversing `m[i][j]` with `j` in the inner loop reads adjacent integers. Reversing the loops jumps by an entire row between accesses. Both versions are $O(\mathrm{rows}\cdot\mathrm{cols})$, but their cache behavior can differ greatly for a large matrix.

## Why insertion and deletion move data

Indexing is cheap because each logical position has a fixed offset. Inserting at index $i$ changes the offset of every element from $i$ onward, so a contiguous representation must move that suffix. If the old size is $n$, insertion moves $n-i$ elements; deletion moves $n-i-1$.

The direction of movement matters when source and destination overlap. To open a gap, copy from the old end toward $i$. Copying left to right overwrites a value before it has been moved. To close a gap after deletion, copy from $i+1$ toward the left. The C library function `memmove` handles overlapping byte ranges; `memcpy` does not promise to.

### Worked example: sorted insertion

Insert `15` into the sorted sequence `[3, 8, 12, 19, 27]`. Assume there is one spare slot.

Find the first value greater than `15`. The comparisons are `3 < 15`, `8 < 15`, `12 < 15`, then `19 > 15`, so the insertion index is `3`.

Start at the right edge:

```text
initial: [3, 8, 12, 19, 27, _]
move 27: [3, 8, 12, 19, 27, 27]
move 19: [3, 8, 12, 19, 19, 27]
write 15:[3, 8, 12, 15, 19, 27]
```

Two elements moved, matching $n-i=5-3=2$. The prefix before index three was already below `15`; the shifted suffix was already above it. The resulting sequence remains sorted.

For sorted arrays, binary search can find the insertion index in $O(\log n)$ comparisons, but the shift remains $O(n)$. Faster searching does not remove the storage cost.

| Operation | Cost | Source of cost |
|---|---:|---|
| read or write a valid index | $O(1)$ | address calculation |
| scan or unsorted search | $O(n)$ | inspect elements in sequence |
| binary search, sorted array | $O(\log n)$ | halve the candidate interval |
| insert or erase at end | $O(1)$ if capacity remains | change one element and `size` |
| insert at front | $O(n)$ | move every old element |
| erase at index $i$ | $O(n-i)$ | close the gap |

Deletion may leave capacity unchanged. Reallocating after every erase would turn ordinary removals into repeated allocation and copying. Some dynamic arrays shrink only when utilization becomes low, often using a lower threshold than the growth threshold so the buffer does not oscillate in size.

## Growing a dynamic array

A dynamic array allocates a larger contiguous block when `size == capacity`, moves or copies existing elements, releases the old block, then appends. Growing by one slot each time is a poor policy: appending $n$ elements copies roughly

$$
1+2+\cdots+(n-1)=\frac{n(n-1)}{2}
$$

elements, for $\Theta(n^2)$ total work.

Geometric growth avoids that result. If capacity doubles, the copy sizes before reaching $n$ elements are powers of two:

$$
1+2+4+\cdots+2^k=2^{k+1}-1<2n.
$$

The total number of copied elements is linear in the number appended. Adding the $n$ ordinary writes gives $O(n)$ work over $n$ appends, hence $O(1)$ **amortized** cost per append. A particular append can still cost $O(n)$; amortized analysis describes a sequence, not a latency bound for each operation.

Another way to see the bound is accounting. Charge each append a few units of work. One unit pays for its immediate write; saved units on elements inserted since the previous expansion pay for the next copy. Because doubling creates as many empty slots as occupied ones, enough cheap appends occur before the following expansion.

Growth factors below two trade less unused memory for more frequent copying. The essential property for constant amortized append is multiplicative growth by a factor greater than one. Real allocators and element types add details: moving complex objects can fail or be expensive, while a C array of integers can be copied as raw bytes.

### Worked example: capacity trace

Start with capacity `2` and size `0`; double whenever an append finds a full buffer. Append values `10`, `20`, `30`, `40`, and `50`.

1. Append `10`: size becomes `1`; capacity stays `2`.
2. Append `20`: size becomes `2`; capacity stays `2`.
3. Before appending `30`, size equals capacity. Allocate capacity `4`, copy `10` and `20`, then write `30`. There were two copied elements.
4. Append `40`: size becomes `4`; no copy is needed.
5. Before appending `50`, allocate capacity `8`, copy four elements, then write `50`.

The trace is:

| append | size after | capacity after | elements copied |
|---:|---:|---:|---:|
| `10` | 1 | 2 | 0 |
| `20` | 2 | 2 | 0 |
| `30` | 3 | 4 | 2 |
| `40` | 4 | 4 | 0 |
| `50` | 5 | 8 | 4 |

Five appends perform five destination writes and six expansion copies. The expensive steps are visible, yet the accumulated copies stay proportional to the number of values.

## A checked C implementation

The useful parts of a small implementation are ownership, overflow checks, and overlap-safe movement. Callers receive success or failure for invalid indices; allocation failure is kept distinct.

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntArray;

static int reserve(IntArray *a, size_t needed) {
    if (needed <= a->capacity) return 1;

    size_t next = a->capacity == 0 ? 4 : a->capacity;
    while (next < needed) {
        if (next > SIZE_MAX / 2) return 0;
        next *= 2;
    }
    if (next > SIZE_MAX / sizeof(*a->data)) return 0;

    int *p = realloc(a->data, next * sizeof(*a->data));
    if (p == NULL) return 0;
    a->data = p;
    a->capacity = next;
    return 1;
}

static int insert_at(IntArray *a, size_t index, int value) {
    if (index > a->size || a->size == SIZE_MAX) return 0;
    if (!reserve(a, a->size + 1)) return 0;

    memmove(&a->data[index + 1],
            &a->data[index],
            (a->size - index) * sizeof(*a->data));
    a->data[index] = value;
    a->size++;
    return 1;
}

static int erase_at(IntArray *a, size_t index) {
    if (index >= a->size) return 0;
    memmove(&a->data[index],
            &a->data[index + 1],
            (a->size - index - 1) * sizeof(*a->data));
    a->size--;
    return 1;
}

int main(void) {
    IntArray a = {0};
    int values[] = {3, 8, 12, 19, 27};

    for (size_t i = 0; i < sizeof(values) / sizeof(values[0]); ++i) {
        if (!insert_at(&a, a.size, values[i])) return EXIT_FAILURE;
    }
    if (!insert_at(&a, 3, 15)) return EXIT_FAILURE;
    if (!erase_at(&a, 1)) return EXIT_FAILURE;

    for (size_t i = 0; i < a.size; ++i) printf("%d ", a.data[i]);
    printf("\n");
    free(a.data);
    return EXIT_SUCCESS;
}
```

Assigning `realloc` directly to `a->data` would lose the old allocation if reallocation failed. The temporary pointer preserves ownership until success. Any successful reallocation may move the block, so pointers into the old array become invalid. Indices survive relocation and are often safer to retain across a call that may grow the buffer.

For element types that own resources, raw `memmove` may be the wrong operation. C requires an explicit move protocol; C++ containers invoke constructors and destructors. The contiguous layout remains, but object lifetime rules add work beyond byte copying.

## Array parameters need shape information

Because conversion to a pointer drops the outer array extent, a C function normally receives the length as a separate argument:

```c
long sum(const int *data, size_t length);
```

The pair forms a non-owning **view** of the elements. The function may read the range from `data[0]` through `data[length - 1]`, but it does not own the allocation and must not free it. This convention also represents a slice without copying: to pass elements beginning at index `first`, supply `data + first` and a length no greater than `size - first`.

Both halves of the pair are required. A pointer does not carry the allocation size, and a length is meaningless without a pointer and element type. Sentinel-terminated arrays, such as C strings, encode the end with a special element instead. They avoid an explicit length for some operations but require a scan to discover it, and the sentinel value cannot be used as ordinary data without an escaping convention.

For a rectangular matrix, the function also needs its stride. With a true C two-dimensional array whose column count is `cols`, a parameter can describe rows of that width. Libraries often accept a pointer plus row count, column count, and leading dimension. The leading dimension can exceed the logical column count when a matrix is a view into a larger padded buffer. Addressing then uses the physical stride rather than assuming tightly packed rows.

A jagged array has a different representation. It is commonly an array of row pointers, and each row may have a different length or allocation. That flexibility costs an extra pointer lookup and loses the guarantee that the end of one row is adjacent to the start of the next. Passing a contiguous matrix where a function expects row pointers, or the reverse, is a type and layout error rather than a harmless cast.

Ownership should be stated at the API boundary. “Borrowed for the duration of the call” permits stack arrays and subarrays. “Takes ownership” requires a dynamically allocated block that the callee will eventually release. An output function may instead ask the caller for a destination and capacity, then return the number of elements written or required. These contracts prevent double frees and buffer overruns more reliably than naming conventions alone.

## Aliasing changes what bulk operations are legal

Two pointers **alias** when they refer to overlapping storage. Aliasing matters for both correctness and optimization. If a function adds one array into another, the behavior may change when the source and destination are the same array or partially overlap. The interface should either support that case explicitly or state that the ranges must not overlap.

`memcpy` is intended for nonoverlapping ranges. It can copy in any order, so overlap makes its behavior undefined. `memmove` behaves as though the source bytes were first copied to a temporary array, which preserves the result for overlap. An implementation need not allocate that temporary block; it can choose a safe direction based on the addresses.

Consider shifting the range `[20, 30, 40]` one place to the right within the same array. A left-to-right element loop writes `20` over the old `30`, then reads that overwritten slot and produces repeated `20`s. A right-to-left loop reads each source before its destination can replace it. The earlier insertion trace depends on exactly that ordering.

The C `restrict` qualifier lets a function promise that, for the relevant execution, accesses through one restricted pointer are not also made through an unrelated pointer to the same objects. The compiler can then optimize more aggressively. Supplying overlapping arrays to a function whose contract uses `restrict` violates the promise. It is an API condition, not a run-time overlap check.

## Stable addresses versus stable indices

An ordinary fixed array gives every element a stable address for the array's lifetime. A resizable dynamic array gives stable indices only until insertions or deletions change logical positions. Growth may invalidate every address, pointer, and iterator into the block even though indices of existing elements remain numerically unchanged.

Insertion near the front has two independent effects. Reallocation may move the whole buffer, and shifting changes the address and index of the suffix. Erasure similarly moves later elements left. Code that stores internal element pointers in another structure must account for both effects. Reserving enough capacity prevents relocation but does not prevent shifting.

Some workloads need pointer stability more than locality. A linked structure, chunked sequence, or indirection table may then be a better representation. Another option is to store objects separately and keep pointers in the dynamic array; array growth moves the pointers, not the objects, at the cost of extra allocations and indirection. The choice depends on which identity must survive an update: position, object address, or an external handle.

## Choosing arrays, and recognizing their limits

Arrays fit workloads dominated by indexed lookup, scans, sorting, and compact storage. Their locality lets hardware prefetch sequential elements and places several small elements in one cache line. Linked structures can offer cheaper local splicing when a node is already known, but each node carries links and may require a separate, poorly localized allocation.

Large arrays also require one contiguous virtual address range. Total free memory may be sufficient while no suitable contiguous range is available, especially in constrained systems. Very large automatic arrays can exhaust the thread stack; dynamic allocation or static storage is usually more appropriate for data whose size depends on input.

Several recurring errors follow directly from the representation:

- `size` and `capacity` are interchangeable only when the buffer is full. Iterating to capacity reads slots outside the logical sequence.
- A pointer into a dynamic array cannot be kept across an operation that may reallocate.
- Signed and unsigned index arithmetic needs care. Subtracting from zero in `size_t` wraps to a very large value.
- The middle index in binary search should be formed without overflowing the sum of endpoints.
- A two-dimensional array is not generally compatible with an `int **`. The former is one contiguous block with fixed row stride; the latter usually points to separately located rows.
- Zero-length allocation has implementation-defined details at the library boundary. A container can avoid ambiguity by representing the empty state with a null pointer and zero capacity.

<div className="see-also">

See also: [Searching algorithms](/cs/data-structures/searching-algorithms) · [Sorting algorithms](/cs/data-structures/sorting-algorithms) · [Stacks](/cs/data-structures/stacks) · [Queues](/cs/data-structures/queues) · [Hashing](/cs/data-structures/hashing)

</div>
