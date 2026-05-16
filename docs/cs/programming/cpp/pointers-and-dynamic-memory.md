---
title: Pointers and Dynamic Memory
sidebar_position: 6
---

# Pointers and Dynamic Memory

Pointers expose the address-based side of C++. They make it possible to create objects whose lifetime is controlled explicitly, build dynamic arrays, share objects without copying them, and implement linked data structures. Savitch introduces pointers after arrays because array parameters already behave like addresses; pointers make that mechanism explicit.

The power of pointers is balanced by responsibility. A pointer can point to a valid object, point to nothing, point to an object that has already been destroyed, or be uninitialized. Correct pointer programs maintain ownership and lifetime invariants as carefully as numeric programs maintain arithmetic invariants.

## Definitions

A **pointer** is a value that stores the address of an object. A pointer variable has a pointer type.

```cpp
int value = 42;
int* ptr = &value;
```

The **address-of operator** `&` produces the address of an object. The **dereference operator** `*` accesses the object pointed to by a pointer.

```cpp
*ptr = 100; // changes value
```

The same symbol `*` appears in several contexts:

| Syntax | Meaning |
|---|---|
| `int* p` | declaration of pointer to `int` |
| `*p` | dereference pointer `p` |
| `a * b` | multiplication |

A **dynamic variable** is created at run time with `new`.

```cpp
int* p = new int;
*p = 17;
```

The **freestore** or **heap** is the memory area used for dynamically allocated objects. Use `delete` to destroy a single dynamic object:

```cpp
delete p;
p = nullptr;
```

A **dynamic array** is created with `new[]` and destroyed with `delete[]`.

```cpp
int* values = new int[count];
delete[] values;
```

A **dangling pointer** points to storage whose object has been destroyed. A **memory leak** occurs when dynamic storage is no longer reachable and therefore cannot be deleted.

The **arrow operator** `->` combines dereference and member access.

```cpp
struct Point {
    double x;
    double y;
};

Point* point = new Point{1.0, 2.0};
std::cout << point->x << '\n'; // same as (*point).x
delete point;
```

## Key results

Pointer assignment copies an address, not the object being pointed to. After this code, `p` and `q` point to the same dynamic integer:

```cpp
int* p = new int(10);
int* q = p;
*q = 20;
```

Now `*p` is also `20`. There is still only one dynamic integer.

Dynamic arrays connect naturally to pointer arithmetic and array indexing. If `a` points to the first element, `a[i]` means the element `i` positions after `a`. Built-in array variables act like fixed pointer values to their first elements in many expressions, but an array variable itself cannot be reassigned.

```cpp
int fixed[3] = {1, 2, 3};
int* p = fixed;    // OK
// fixed = p;      // not OK
```

When a class owns dynamic memory, the default copy behavior is usually wrong. Default memberwise copying copies pointer values, causing two objects to point to the same dynamic storage. That can cause double deletion, accidental sharing, or stale data. This is why destructors, copy constructors, and assignment operators matter.

Modern C++ often uses standard containers and smart pointers instead of raw owning pointers. Savitch's raw-pointer treatment remains essential because it explains how arrays, dynamic allocation, linked lists, and class copy semantics work underneath.

## Visual

```text
Pointer assignment copies the address:

int* p = new int(42);
int* q = p;

       +-----+
p ---> | 42  |
       +-----+
q -----^

*q = 99 changes the shared object:

       +-----+
p ---> | 99  |
       +-----+
q -----^
```

```mermaid
flowchart TD
  A[Allocate with new or new[]] --> B[Store returned pointer]
  B --> C[Use only while object is alive]
  C --> D{Single object or array?}
  D -->|single| E[delete pointer]
  D -->|array| F[delete[] pointer]
  E --> G[Set pointer to nullptr if reused]
  F --> G
  G --> H[Do not dereference after delete]
```

## Worked example 1: tracing pointer assignment

Problem: Predict the output.

```cpp
#include <iostream>

int main() {
    int* p1 = new int;
    int* p2 = new int;

    *p1 = 10;
    *p2 = 20;
    std::cout << *p1 << " " << *p2 << '\n';

    p1 = p2;
    std::cout << *p1 << " " << *p2 << '\n';

    *p1 = 30;
    std::cout << *p1 << " " << *p2 << '\n';

    delete p2;
}
```

Method:

1. Two dynamic integers are created.
2. `*p1 = 10`, `*p2 = 20`.
3. First output is `10 20`.
4. `p1 = p2` copies the address stored in `p2`.
5. Now both pointers point to the integer that contains `20`.
6. The original integer containing `10` has no pointer to it, so it is leaked.
7. Second output is `20 20`.
8. `*p1 = 30` changes the object shared by `p1` and `p2`.
9. Third output is `30 30`.

Checked answer:

```text
10 20
20 20
30 30
```

The code intentionally demonstrates a leak. A production version would delete the object pointed to by `p1` before overwriting `p1`.

## Worked example 2: dynamic array average

Problem: Read `n`, allocate an array of `n` exam scores, and compute the average.

Method:

1. Read `n`.
2. Validate `n > 0`.
3. Allocate `new double[n]`.
4. Fill indexes `0` through `n - 1`.
5. Sum all values.
6. Divide by `n`.
7. Release with `delete[]`.

```cpp
#include <iostream>

int main() {
    int n;
    std::cout << "Number of scores: ";
    std::cin >> n;

    if (n <= 0) {
        std::cerr << "Need at least one score.\n";
        return 1;
    }

    double* scores = new double[n];
    double total = 0.0;

    for (int i = 0; i < n; ++i) {
        std::cout << "Score " << i + 1 << ": ";
        std::cin >> scores[i];
        total += scores[i];
    }

    double average = total / n;
    std::cout << "Average: " << average << '\n';

    delete[] scores;
    scores = nullptr;
}
```

Checked answer: for inputs `3`, `80`, `90`, `100`, the total is:

$$
80 + 90 + 100 = 270
$$

and the average is:

$$
270 / 3 = 90
$$

The array is released with `delete[]`, matching `new[]`.

## Code

This class owns a dynamic array and follows the basic rule of three: destructor, copy constructor, and assignment operator.

```cpp
#include <algorithm>
#include <iostream>

class IntBuffer {
public:
    explicit IntBuffer(int size)
        : size_(size), data_(new int[size]) {
        std::fill(data_, data_ + size_, 0);
    }

    IntBuffer(const IntBuffer& other)
        : size_(other.size_), data_(new int[other.size_]) {
        std::copy(other.data_, other.data_ + size_, data_);
    }

    IntBuffer& operator=(const IntBuffer& rhs) {
        if (this == &rhs) {
            return *this;
        }

        int* newData = new int[rhs.size_];
        std::copy(rhs.data_, rhs.data_ + rhs.size_, newData);

        delete[] data_;
        data_ = newData;
        size_ = rhs.size_;
        return *this;
    }

    ~IntBuffer() {
        delete[] data_;
    }

    int& operator[](int index) {
        return data_[index];
    }

    int size() const {
        return size_;
    }

private:
    int size_;
    int* data_;
};

int main() {
    IntBuffer a(3);
    a[0] = 10;
    a[1] = 20;
    a[2] = 30;

    IntBuffer b = a;
    b[1] = 99;

    std::cout << a[1] << " " << b[1] << '\n';
}
```

## Common pitfalls

- Dereferencing an uninitialized pointer.
- Using a pointer after `delete`.
- Using `delete` for memory allocated with `new[]`, or `delete[]` for memory allocated with `new`.
- Losing the only pointer to dynamic memory and leaking it.
- Assuming pointer assignment copies the pointed-to object.
- Forgetting self-assignment checks in assignment operators that delete old storage.
- Returning a pointer to a local automatic variable.
- Writing outside a dynamic array because the allocated size is not tracked.

Ownership checks:

- Write down who owns each dynamically allocated object. If the answer is "several parts of the program," the design is probably ambiguous unless shared ownership is deliberately modeled.
- Initialize pointers immediately. A pointer should either hold a valid address or `nullptr`; an uninitialized pointer contains an indeterminate address and must not be dereferenced or deleted.
- After `delete`, set the pointer to `nullptr` when the pointer will remain in scope and might be tested later. This does not fix all aliasing problems, but it prevents accidental reuse through that variable.
- Prefer one allocation and one deallocation path. Functions with many early returns are safer when dynamic storage is owned by a class object rather than manually released at every exit.
- Distinguish pointer equality from value equality. `p == q` asks whether two pointers hold the same address; `*p == *q` asks whether the pointed-to values compare equal.
- For dynamic arrays, store the size next to the pointer in the owning object. A raw pointer alone does not remember how many elements were allocated.
- Use standard containers when the array size is the only dynamic feature. A `vector<int>` usually expresses a growable array more safely than `int*` plus manual capacity management.

Quick self-test: replace every raw pointer in a small program with the phrase "address of ...". If the phrase is not meaningful, the pointer probably does not have a clear role. For example, `int* scores` might be "address of the first element of a dynamic array of scores," but that sentence also reveals that the size must be stored somewhere else.

When reviewing a function, pair every allocation with the cleanup path that owns it. If the allocation happens in one function and deletion in another, document that transfer clearly or wrap the resource in an object whose destructor makes the transfer unnecessary.

A final review question is whether the pointer expresses observation or ownership. Observing pointers may point to objects owned elsewhere and must not delete them. Owning pointers are responsible for cleanup and should usually be wrapped in a class so destruction is automatic.

Extended practice: draw memory as two regions, stack objects and dynamic objects. Local pointer variables live on the stack, while objects created with `new` live in dynamic storage. Deleting the dynamic object does not remove the pointer variable; it only makes the stored address unsafe to use.

## Connections

- [arrays](/cs/programming/cpp/arrays)
- [strings](/cs/programming/cpp/strings)
- [constructors and copy semantics](/cs/programming/cpp/constructors-and-copy-semantics)
- [linked data structures](/cs/programming/cpp/linked-data-structures)
- [polymorphism](/cs/programming/cpp/polymorphism-and-virtual-functions)
