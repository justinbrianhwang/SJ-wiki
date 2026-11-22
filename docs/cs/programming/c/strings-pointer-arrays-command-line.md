---
title: Strings, Pointer Arrays, and Command-Line Arguments
sidebar_position: 8
---

# Strings, Pointer Arrays, and Command-Line Arguments

K&R's pointer chapter moves from single pointers to arrays of pointers, strings, sorting lines, multi-dimensional arrays, and command-line arguments. This is where the language becomes idiomatic UNIX C: a program reads lines into storage, keeps pointers to those lines, sorts or filters by rearranging pointers, and uses `argv` to select behavior.

The central lesson is representation. A two-dimensional character array stores fixed-width rows. An array of `char *` stores pointers to strings that may have different lengths. Both can be indexed with two subscripts in some cases, but their storage and flexibility differ dramatically.

## Definitions

A C string is a sequence of characters terminated by `'\0'`. A string literal creates an array with this terminator:

```c
"Jan"
```

has four characters in storage: `J`, `a`, `n`, `'\0'`.

A character pointer may point at the first character of a string:

```c
char *p = "January";
```

In modern C, string literals should be treated as read-only; use `const char *` unless you need a modifiable array:

```c
char month[] = "January";       /* modifiable array */
const char *name = "January";   /* pointer to literal */
```

An array of pointers stores addresses:

```c
const char *month_name[] = {
    "Illegal month",
    "January", "February", "March"
};
```

A multi-dimensional array stores all elements inline:

```c
char names[][10] = { "Jan", "Feb", "Mar" };
```

Command-line arguments are passed to `main` as an argument count and argument vector:

```c
int main(int argc, char *argv[])
```

`argc` is the number of strings. `argv[0]` is the program name by convention. `argv[1]` through `argv[argc - 1]` are the supplied arguments, and `argv[argc]` is a null pointer.

Pointer arrays are often sorted by swapping pointers instead of moving the strings they point to. This is the idea behind K&R's line-sorting example.

## Key results

`char *s` and `char s[]` are equivalent as function parameters, but not as object definitions. As a parameter, both mean "pointer to char." As definitions, `char s[] = "abc";` creates an array, while `char *s = "abc";` creates a pointer to a string literal.

An array of pointers is not a rectangular two-dimensional array. Given `int a[10][20]`, C allocates 200 integers contiguously. Given `int *b[10]`, C allocates 10 pointers; each pointer must be made to point somewhere before `b[i][j]` is valid. This distinction is the source of many C bugs and many useful representations.

Pointer-based traversal is a K&R idiom. A loop such as `while (*s++ = *t++) ;` copies a string by assigning each character, including the terminating `'\0'`, then stopping when the assigned value is zero. It is terse, but it must be read with operator precedence and side effects in mind.

Command-line option parsing often uses pointer increments. K&R's `find` example advances `argv` through option strings beginning with `-`, then walks each option character with pointer expressions. The idiom is compact, but expressions such as `(*++argv)[0]` should be used sparingly and documented by surrounding code structure.

String functions rely on the terminator, not on separately stored length. That gives C strings their simple representation, but it means every string operation must be able to find `'\0'` within valid storage. A missing terminator turns `strlen`, `strcpy`, `printf("%s")`, and many other functions into out-of-bounds reads. K&R's line-reading code explicitly writes the terminator after filling the buffer; that final assignment is not optional.

Pointer arrays are also a memory-management technique. In the line-sorting program, the text of each line is stored once, while an array of pointers records the order. Sorting swaps pointers rather than moving entire lines. This is faster, but it also means the pointers must remain valid for the whole sort. If the lines were stored in a single temporary buffer reused for every input line, all pointers would end up pointing at the same overwritten storage.

For command-line arguments, remember that the environment owns the original strings. A program may inspect them and often can modify them on hosted systems, but portable code should not depend on modifying `argv` strings unless the standard and target environment permit the intended use. It is always fine to copy an argument into program-owned storage when mutation is needed.

A useful mental model is that `argv` is already an array of strings in the same style K&R builds manually for sorted input lines. `argv` itself is a pointer to the first element of an array of `char *`; each element points at a null-terminated string. Incrementing `argv` walks the vector, while incrementing `argv[0]` walks characters inside one string. K&R shows both moves, and confusing them changes the level of traversal.

When parsing options, keep the remaining argument count and pointer position consistent. If `argc` says one argument remains, `argv` should point at it. This invariant makes it easier to detect missing operands and illegal extra arguments.

The same invariant applies to arrays of line pointers: the count says how many entries are valid, and the pointer array stores only those entries. Never sort or print uninitialized pointer slots beyond the count.

## Visual

```text
Array of pointers:

name[0] --> "Illegal month\0"
name[1] --> "January\0"
name[2] --> "Feb\0"

Two-dimensional array:

aname[0]  I l l e g a l ... fixed row width
aname[1]  J a n u a r y \0 padding...
aname[2]  F e b \0 padding...
```

| Representation | Declaration | Storage | Strength | Risk |
|---|---|---|---|---|
| Modifiable string array | `char s[] = "abc";` | characters inline | can edit contents | fixed size |
| Pointer to literal | `const char *s = "abc";` | pointer plus literal elsewhere | cheap, shareable | do not modify literal |
| Rectangular table | `char a[12][10]` | fixed rows inline | simple indexing | wasted space, fixed width |
| Pointer array | `char *a[12]` | pointers inline, strings elsewhere | variable-length rows | pointers must be valid |
| Argument vector | `char *argv[]` | array of pointers from environment | natural command input | option parsing can get dense |

## Worked example 1: Echoing command-line arguments by pointer movement

Problem: for a program invoked as

```text
echo hello world
```

show how K&R's pointer version prints `hello world`.

Method:

Initial state:

```text
argc = 3
argv[0] -> "echo"
argv[1] -> "hello"
argv[2] -> "world"
argv[3] -> NULL
```

Loop:

```c
while (--argc > 0)
    printf("%s%s", *++argv, (argc > 1) ? " " : "");
```

1. First test decrements `argc` from `3` to `2`; condition is true.
2. `++argv` moves from `argv[0]` to `argv[1]`.
3. `*argv` is `"hello"`.
4. Since `argc > 1`, print a space after it.
5. Second test decrements `argc` from `2` to `1`; condition is true.
6. `++argv` moves to `argv[2]`.
7. `*argv` is `"world"`.
8. Since `argc > 1` is false, print no trailing space.
9. Third test decrements `argc` from `1` to `0`; stop.

Checked answer: output is exactly `hello world`.

## Worked example 2: Choosing pointer array over two-dimensional array

Problem: store the month names `May`, `September`, and `December`. Compare storage if a fixed row width of 10 characters is used.

Method:

1. Two-dimensional array:

   ```c
   char m[3][10] = { "May", "September", "December" };
   ```

   Storage is:

   $$3 \times 10 = 30\text{ chars}.$$

2. Actual characters needed including terminators:

   - `"May"` needs `4`.
   - `"September"` needs `10`.
   - `"December"` needs `9`.

   Total:

   $$4 + 10 + 9 = 23\text{ chars}.$$

3. Pointer array:

   ```c
   const char *m[] = { "May", "September", "December" };
   ```

   It stores 3 pointers plus 23 characters for literals, ignoring implementation details such as literal pooling.

4. Interpretation: the pointer array may use more total memory on a machine with large pointers, but it avoids fixed row limits and represents variable-length strings naturally.

Checked answer: the two-dimensional array reserves exactly 30 character slots and can modify each row. The pointer array represents variable strings naturally but should treat literals as read-only.

## Code

```c
#include <stdio.h>
#include <string.h>

static const char *month_name(int n)
{
    static const char *name[] = {
        "Illegal month",
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    };

    return (n < 1 || n > 12) ? name[0] : name[n];
}

int main(int argc, char *argv[])
{
    if (argc == 1) {
        for (int i = 1; i <= 12; ++i)
            puts(month_name(i));
        return 0;
    }

    while (--argc > 0) {
        int n = 0;
        const char *s = *++argv;

        while (*s >= '0' && *s <= '9')
            n = 10 * n + (*s++ - '0');

        puts(month_name(n));
    }

    return 0;
}
```

## Common pitfalls

- Trying to modify a string literal through `char *`. Modern compilers may warn; the behavior is undefined.
- Assuming `char **` is interchangeable with `char a[][N]`. A pointer to pointer and a pointer to an array are different types and layouts.
- Forgetting that `argv[argc]` is `NULL`, but `argv[argc - 1]` is the last real argument.
- Writing overly clever pointer expressions in option parsing. Split them when the precedence is not obvious.
- Losing the original pointer returned by an allocator while incrementing through a string.
- Copying strings without room for the terminating `'\0'`.
- Sorting full lines when swapping pointers would be simpler and cheaper.

## Connections

- [Pointers, Addresses, and Arrays](/cs/programming/c/pointers-addresses-arrays)
- [Function Pointers and Complex Declarations](/cs/programming/c/function-pointers-complex-declarations)
- [Standard I/O and Formatted I/O](/cs/programming/c/standard-io-formatted-io)
- [Storage Allocation](/cs/programming/c/storage-allocation)
- [Unix System Interface](/cs/programming/c/unix-system-interface)
