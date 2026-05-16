---
title: C
sidebar_position: 1
---

# C

These notes cover C through the scope of Kernighan and Ritchie's *The C Programming Language*, second edition: the tutorial core, the expression and type system, control flow, functions, pointers, structures, input/output, the UNIX interface, the ANSI standard library, and the gap between K&R-era style and modern C practice.

C is a small language with unusually direct access to representation. Arrays are contiguous storage, strings are null-terminated character arrays, pointers are typed addresses, and much of the standard library is built out of explicit buffers, status returns, and caller-managed storage. That directness is why K&R can move quickly from "hello, world" to sorting lines, parsing declarations, building hash tables, walking directories, and sketching an allocator.

The pages emphasize K&R idioms: pointer-based traversal, compact stream filters, explicit prototypes, small functions, file-scope `static` state, careful use of macros, and precise notes on undefined or implementation-defined behavior. The examples are written in modern prototype style while preserving the book's model of how C programs are shaped.

1. [Tutorial Introduction](/cs/programming/c/tutorial-introduction)
2. [Types, Operators, and Expressions](/cs/programming/c/types-operators-expressions)
3. [Control Flow](/cs/programming/c/control-flow)
4. [Functions and Program Structure](/cs/programming/c/functions-program-structure)
5. [Preprocessor and Separate Compilation](/cs/programming/c/preprocessor-separate-compilation)
6. [Pointers, Addresses, and Arrays](/cs/programming/c/pointers-addresses-arrays)
7. [Strings, Pointer Arrays, and Command-Line Arguments](/cs/programming/c/strings-pointer-arrays-command-line)
8. [Function Pointers and Complex Declarations](/cs/programming/c/function-pointers-complex-declarations)
9. [Structures, Typedef, Unions, and Bit Fields](/cs/programming/c/structures-typedef-unions-bitfields)
10. [Linked Structures and Hash Tables](/cs/programming/c/linked-structures-hash-tables)
11. [Standard I/O and Formatted I/O](/cs/programming/c/standard-io-formatted-io)
12. [File Access and Error Handling](/cs/programming/c/file-access-error-handling)
13. [Unix System Interface](/cs/programming/c/unix-system-interface)
14. [Storage Allocation](/cs/programming/c/storage-allocation)
15. [Standard Library Reference](/cs/programming/c/standard-library-reference)
16. [Modern C Considerations](/cs/programming/c/modern-c-considerations)
