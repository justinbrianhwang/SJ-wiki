---
title: Unix System Interface
sidebar_position: 14
---

# Unix System Interface

K&R ends the main text by going below the standard I/O library to the UNIX system interface. This chapter is deliberately system-specific: it explains file descriptors, `read`, `write`, `open`, `close`, `lseek`, directory traversal, and the low-level basis for a storage allocator. The point is not that every C program should use these calls, but that C is close enough to the operating system to express them directly.

![A C language logo marks the systems-programming pages built around C examples.](https://commons.wikimedia.org/wiki/Special:FilePath/C_Programming_Language.svg)

*Figure: C remains the reference language for low-level memory, pointers, and Unix interfaces. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:C_Programming_Language.svg), ElodinKaldwin, public domain text logo.*

The contrast with `<stdio.h>` is the main idea. Standard I/O deals in buffered `FILE *` streams and portable text conventions. UNIX low-level I/O deals in integer file descriptors and byte counts. The stream library is often implemented on top of these lower-level calls.

## Definitions

A file descriptor is a small nonnegative integer used by the kernel to identify an open file, device, pipe, or socket-like object. At process start, UNIX convention provides:

```text
0  standard input
1  standard output
2  standard error
```

Low-level input and output use:

```c
int n_read = read(int fd, char *buf, int n);
int n_written = write(int fd, char *buf, int n);
```

Modern declarations use `ssize_t` and `size_t`, but K&R presents the conceptual interface in older style. `read` returns the number of bytes read, `0` for end-of-file, and `-1` for error. `write` returns the number of bytes written, or `-1` for error.

Files are opened and closed with:

```c
int fd = open(const char *name, int flags, int mode);
int rc = close(int fd);
```

Common flags include `O_RDONLY`, `O_WRONLY`, `O_RDWR`, `O_CREAT`, `O_TRUNC`, and `O_APPEND`, declared in `<fcntl.h>` on POSIX systems.

Random access uses:

```c
long lseek(int fd, long offset, int origin);
```

Modern POSIX uses `off_t`. The `origin` is usually one of `SEEK_SET`, `SEEK_CUR`, or `SEEK_END`.

The system call `stat` fills a structure with file metadata such as size, mode, owner, and times. Directory traversal is built from system-specific directory entries; K&R wraps this behind `opendir`, `readdir`, and `closedir` to isolate non-portable details.

## Key results

Descriptors are not streams. A descriptor has no C library buffer, no formatted I/O, and no automatic text translation. It is appropriate for system programming, binary byte processing, and implementing higher-level libraries.

`read` and `write` may transfer fewer bytes than requested. A robust program loops until the desired byte count is complete, end-of-file occurs, or an error occurs. This matters especially for pipes, terminals, and interrupted calls.

The standard streams `stdin`, `stdout`, and `stderr` usually sit on top of descriptors 0, 1, and 2, but mixing stream I/O and descriptor I/O on the same underlying file requires care because buffering can reorder observations.

File position belongs to the open file description. `lseek` changes where the next `read` or `write` occurs for seekable files. Pipes and terminals are not generally seekable.

Directory formats are not portable. K&R's `fsize` example creates a small portable interface type `Dirent` and functions `opendir`, `readdir`, and `closedir`, then confines the system-dependent layout to one implementation layer. This is a classic C technique: wrap a non-portable representation behind a small interface.

System-call examples in K&R predate POSIX standardization and modern prototypes. The conceptual model remains valuable, but modern code should include the correct headers, use `ssize_t`, `size_t`, `off_t`, and check `errno` through `perror` or `strerror`.

Low-level I/O is also where C's "no hidden work" character is most obvious. A call to `read` asks for bytes and reports a count. It does not append `'\0'`, does not preserve line boundaries, and does not retry automatically in every situation. A call to `write` sends bytes and reports a count. If a program wants records, lines, buffering, or formatted conversion, it must build that behavior or use a library layer that does.

K&R's directory example is valuable because it refuses to scatter system-dependent knowledge through the whole program. The high-level `fsize` logic asks for entries one at a time and recursively processes path names. The low-level directory representation is confined to a few routines. This is the same design used in portable systems code today: make the unstable boundary small, then keep ordinary program logic on the stable side of that boundary.

The chapter also shows how C libraries are often layered. A simple version of `fopen` and `getc` can be implemented using descriptors, buffers, and calls such as `open` and `read`. Understanding that layering helps explain why stream buffering improves performance, why flushing matters, and why mixing layers can be dangerous. The standard library is not magic; it is C code plus system calls behind a cleaner interface.

Resource ownership is stricter at this layer because the operating system has finite descriptor table entries. Every successful `open` should have a matching `close` on all paths that are finished with the descriptor. This is the descriptor-level equivalent of pairing `malloc` with `free` and `fopen` with `fclose`. C will not close descriptors merely because an integer variable goes out of scope.

The low-level interface also reports errors through return values, not exceptions. A negative return from `open`, `read`, `write`, or `lseek` must be checked before the result is used. K&R's examples keep this visible, and modern POSIX code normally adds `errno`-based diagnostics.

Descriptor I/O is byte-oriented, so text conventions belong above it. If a program needs to count lines, it must look for newline bytes itself or use a stream function that already presents text lines. This distinction is why K&R can implement higher-level routines on top of descriptors: the descriptor layer is intentionally simple.

## Visual

```mermaid
flowchart LR
  A[User program] --> B[stdio FILE streams]
  B --> C[read/write system calls]
  A --> C
  C --> D[Kernel open file table]
  D --> E[Filesystem/device/pipe]
```

| Layer | Handle type | Operations | Buffering | Portability |
|---|---|---|---|---|
| Standard I/O | `FILE *` | `getc`, `printf`, `fgets`, `fwrite` | C library buffering | ISO C |
| UNIX descriptor I/O | `int fd` | `read`, `write`, `open`, `close`, `lseek` | kernel and device behavior | POSIX/UNIX |
| Filesystem metadata | path plus `struct stat` | `stat`, `fstat` | not a data stream | system-specific fields |
| Directory traversal | `DIR *` or K&R wrapper | `opendir`, `readdir`, `closedir` | implementation-defined | POSIX for modern API |

## Worked example 1: Copying with `read` and `write`

Problem: copy input descriptor `0` to output descriptor `1` using a buffer of 4 bytes. Suppose input bytes are:

```text
abcdef
```

Method:

1. First call:

   ```c
   n = read(0, buf, 4);
   ```

   It may return `4` with buffer:

   ```text
   a b c d
   ```

2. Write exactly those 4 bytes:

   ```c
   write(1, buf, 4);
   ```

3. Second read requests 4 bytes but only 2 remain:

   ```text
   e f
   ```

   `read` returns `2`.

4. Write exactly 2 bytes.
5. Third read reaches end-of-file and returns `0`.
6. Stop.

Checked answer: the output byte sequence is `abcdef`. The loop must use the actual `n` returned by `read`, not the full buffer size.

## Worked example 2: Seeking to overwrite a record

Problem: a binary file stores fixed-size records of 32 bytes. Compute the byte offset of record number 5 if records are numbered from 0, then seek there.

Method:

1. Record size:

   $$R = 32.$$

2. Record index:

   $$i = 5.$$

3. Offset from beginning:

$$
\begin{aligned}
   offset &= i \times R \\
   &= 5 \times 32 \\
   &= 160
   \end{aligned}
$$

4. Call:

   ```c
   lseek(fd, 160L, SEEK_SET);
   ```

5. The next `read` or `write` begins at byte 160.

Checked answer: record 5 starts at byte offset 160 when record 0 starts at byte 0 and every record is exactly 32 bytes.

## Code

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFSIZE 4096

static int copyfd(int in, int out)
{
    char buf[BUFSIZE];
    ssize_t n;

    while ((n = read(in, buf, sizeof buf)) > 0) {
        char *p = buf;
        ssize_t left = n;

        while (left > 0) {
            ssize_t written = write(out, p, (size_t)left);
            if (written < 0)
                return -1;
            p += written;
            left -= written;
        }
    }

    return n < 0 ? -1 : 0;
}

int main(int argc, char *argv[])
{
    int fd;
    int status;

    if (argc == 1)
        return copyfd(STDIN_FILENO, STDOUT_FILENO) == 0 ? 0 : 1;

    fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        perror(argv[1]);
        return 1;
    }

    status = copyfd(fd, STDOUT_FILENO);
    close(fd);
    return status == 0 ? 0 : 1;
}
```

## Common pitfalls

- Assuming `read` fills the whole buffer. It returns the byte count actually read.
- Assuming `write` writes every requested byte. Robust descriptor code handles partial writes.
- Treating descriptor `0` as false in tests. Descriptor `0` is valid; failure from `open` is `-1`.
- Mixing `printf` and `write` to the same output without flushing, causing surprising ordering.
- Using `lseek` on pipes or terminals and expecting it to work.
- Embedding historical directory-entry layouts directly in application code.
- Forgetting that K&R's prototypes are historical; modern systems require the correct POSIX headers and types.

## Connections

- [Standard I/O and Formatted I/O](/cs/programming/c/standard-io-formatted-io)
- [File Access and Error Handling](/cs/programming/c/file-access-error-handling)
- [Storage Allocation](/cs/programming/c/storage-allocation)
- [Structures, Typedef, Unions, and Bit Fields](/cs/programming/c/structures-typedef-unions-bitfields)
- [Modern C Considerations](/cs/programming/c/modern-c-considerations)
