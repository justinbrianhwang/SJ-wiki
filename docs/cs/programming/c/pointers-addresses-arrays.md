---
title: Pointers, Addresses, and Arrays
sidebar_position: 7
---

# Pointers, Addresses, and Arrays

Pointers are the central C idea after functions. A pointer is a value that locates an object, and C lets programs copy, compare, increment, subtract, and dereference such values under precise conditions. K&R emphasizes that pointers can make programs smaller and clearer when they follow array and object boundaries, but they can also make errors immediate and severe.

![A C language logo marks the systems-programming pages built around C examples.](https://commons.wikimedia.org/wiki/Special:FilePath/C_Programming_Language.svg)

*Figure: C remains the reference language for low-level memory, pointers, and Unix interfaces. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:C_Programming_Language.svg), ElodinKaldwin, public domain text logo.*

Arrays and pointers are taught together because C connects them tightly. An array expression usually converts to a pointer to its first element. Pointer arithmetic moves by elements, not bytes. Function parameters declared as arrays are really pointer parameters. These rules explain much of the compact style that C inherited from early UNIX programming.

## Definitions

The address operator `&` produces the address of an object:

```c
int x = 1;
int *p = &x;
```

The indirection operator `*` accesses the object to which a pointer points:

```c
*p = 7;       /* changes x */
printf("%d", *p);
```

A pointer declaration is read by considering how the declared name is used in an expression:

```c
int *ip;
```

means `*ip` is an `int`, so `ip` is a pointer to `int`.

Arrays define contiguous storage:

```c
int a[10];
```

The elements are `a[0]` through `a[9]`. If `pa` is a pointer to `int`, then:

```c
pa = &a[0];
```

sets `pa` to point at the first element. The expression `pa + 1` points at the next `int`, not the next byte. More generally, `*(a + i)` and `a[i]` are equivalent, and `&a[i]` and `a + i` are equivalent.

An array name is not a modifiable variable. If `pa` is a pointer, `pa++` is legal. If `a` is an array, `a++` is illegal.

When an array is passed to a function, the function receives a pointer to the first element. These parameter declarations are equivalent:

```c
int strlen_kr(char s[]);
int strlen_kr(char *s);
```

`NULL` is the conventional null pointer constant. A null pointer compares unequal to any valid object pointer and is used to signal "no object" or failure.

## Key results

Pointer arguments are how C functions modify caller objects. Since scalar arguments are passed by value, `swap(a, b)` cannot exchange caller variables. The caller must pass addresses with `swap(&a, &b)`, and the function must dereference pointer parameters.

Pointer arithmetic is defined within one array object, plus one past the last element. Comparing or subtracting pointers from unrelated objects is undefined behavior. This rule matters even on machines where addresses look like integers; C's abstract machine is stricter.

Pointer subtraction returns a count of elements, not bytes. If `p` points to `s[0]` and `q` points to the terminating `'\0'`, then `q - p` is the string length. The result type is `ptrdiff_t` in the standard library, though K&R examples often use `int` for small strings.

Arrays in function parameters do not carry their length. A function that receives `char s[]` must either rely on a sentinel such as `'\0'` or receive a separate limit. K&R's `getline` passes both a buffer and a maximum length, which is the safe pattern.

`void *` is the generic object pointer type in ANSI C. It can hold any object pointer and be converted back without loss of information, but it cannot be dereferenced directly because it has no pointed-to object type.

Pointer notation should not be confused with ownership. A pointer may point to an object it owns, an object owned by its caller, a string literal with static storage duration, an element inside an array, or one-past the end of an array for traversal. The syntax alone does not tell you which case applies. K&R examples are short enough that ownership is visible nearby; in larger programs, comments, naming, and function contracts must make it explicit.

The "one past the end" rule is a deliberate convenience for loops. A pointer may be advanced to the position just after the last array element and compared with other pointers into the same array, but it must not be dereferenced there. This supports idioms such as `for (p = a; p < a + n; ++p)`. The pointer `a + n` is a boundary marker, not an object.

Arrays decay to pointers in most expressions, but not all. `sizeof a` for an actual array object gives the size of the whole array, while `sizeof p` for a pointer gives the size of the pointer itself. The address operator also differs: `&a` has type pointer to the whole array, not pointer to the first element, even though the numeric address is often the same. These distinctions explain why function parameters lose array length information while local arrays still have it available to `sizeof`.

K&R's pointer style is compact because it keeps the current position in the pointer itself. That is natural for stream-like traversal: advance through a string until the terminator, advance through an array until a boundary pointer, or advance through arguments until the count is exhausted. The cost is that the original starting address may be lost if it is not saved. When the original allocation must later be freed, keep a separate owner pointer and use another pointer for walking.

Pointer types also document scale. An `int *` says that `p + 1` moves by one `int`; a `struct node *` says it moves by one node if it is part of an array of nodes. Casting everything to `char *` may be useful for byte-level work, but it discards that scaling information and should signal a low-level operation.

The safest pointer loops have an explicit boundary or sentinel. A string loop uses `'\0'` as its sentinel. An array loop should use a count or an end pointer computed from the same array. Avoid loops whose stopping condition depends on memory outside the object; C will not detect that mistake before the program has already executed undefined behavior.

## Visual

```text
int a[5] = { 10, 20, 30, 40, 50 };

Index:    0    1    2    3    4
        +----+----+----+----+----+
a ----> | 10 | 20 | 30 | 40 | 50 |
        +----+----+----+----+----+
          ^
          |
        pa = a

pa + 2 points to a[2]
*(pa + 2) is 30
```

| Expression | Meaning when `pa = a` | Legal? |
|---|---|---|
| `a[2]` | third element | yes |
| `*(a + 2)` | third element | yes |
| `pa[2]` | third element | yes |
| `*(pa + 2)` | third element | yes |
| `pa++` | advance pointer to next element | yes |
| `a++` | attempt to modify array name | no |
| `pa - a` | element distance from first element | yes, same array |
| `pa < other_array` | compare unrelated arrays | undefined behavior |

## Worked example 1: Swapping through pointer arguments

Problem: exchange two caller variables `a = 3` and `b = 9` using a function.

Method:

1. A wrong function receives copies:

   ```c
   void swap_bad(int x, int y)
   {
       int temp = x;
       x = y;
       y = temp;
   }
   ```

   Calling `swap_bad(a, b)` copies `3` into `x` and `9` into `y`. The copies are swapped, then discarded.

2. Correct call passes addresses:

   ```c
   swap(&a, &b);
   ```

3. Correct function:

   ```c
   void swap(int *px, int *py)
   {
       int temp = *px;
       *px = *py;
       *py = temp;
   }
   ```

4. Trace:

   - `px` points to `a`; `py` points to `b`.
   - `temp = *px` stores `3`.
   - `*px = *py` stores `9` into `a`.
   - `*py = temp` stores `3` into `b`.

Checked answer: after the call, `a = 9` and `b = 3`.

## Worked example 2: Computing string length by pointer subtraction

Problem: compute the length of `"cat"` using a pointer-walking version of `strlen`.

Method:

```c
int strlen_kr(char *s)
{
    char *p = s;
    while (*p != '\0')
        ++p;
    return p - s;
}
```

1. The string storage is:

   ```text
   c  a  t  \0
   ```

2. Initially `p = s`, pointing at `'c'`.
3. Test `*p != '\0'`: true. Increment `p`; now points at `'a'`.
4. Test true. Increment `p`; now points at `'t'`.
5. Test true. Increment `p`; now points at `'\0'`.
6. Test false. Stop.
7. Pointer difference:

   $$p - s = 3.$$

Checked answer: the length is `3`, excluding the terminating null character.

## Code

```c
#include <stdio.h>

void reverse(char *s)
{
    char *left = s;
    char *right = s;

    while (*right != '\0')
        ++right;
    if (right != s)
        --right;

    while (left < right) {
        char temp = *left;
        *left++ = *right;
        *right-- = temp;
    }
}

int main(void)
{
    char word[] = "pointer";

    reverse(word);
    printf("%s\n", word);
    return 0;
}
```

## Common pitfalls

- Dereferencing an uninitialized pointer. A pointer must point to a valid object or be a null pointer before meaningful use.
- Treating arrays as assignable. You can copy elements, but not assign one array object to another with `=`.
- Comparing pointers from different arrays. Equality with `NULL` is fine; ordering comparisons across unrelated objects are not.
- Returning a pointer to an automatic local array. The array ceases to exist when the function returns.
- Forgetting bounds when walking with pointers. Pointer notation does not make overrun safer than subscript notation.
- Assuming `sizeof parameter_array` gives the original array size. In a function parameter, the array has already become a pointer.
- Casting arbitrary integers to pointers. Except for the null pointer constant, pointers and integers are not interchangeable.

## Connections

- [Types, Operators, and Expressions](/cs/programming/c/types-operators-expressions)
- [Functions and Program Structure](/cs/programming/c/functions-program-structure)
- [Strings, Pointer Arrays, and Command-Line Arguments](/cs/programming/c/strings-pointer-arrays-command-line)
- [Function Pointers and Complex Declarations](/cs/programming/c/function-pointers-complex-declarations)
- [Storage Allocation](/cs/programming/c/storage-allocation)
