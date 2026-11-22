---
title: Unix System Interface
sidebar_position: 14
---

# Unix System Interface

K&R ends the main text below the standard I/O library, at the UNIX system interface. The chapter covers file descriptors, `read`, `write`, `open`, `close`, `lseek`, directory traversal, and the operating-system boundary behind an early storage allocator. These calls are system-specific; their value is in showing how directly C can express an OS interface.

The central contrast is with `<stdio.h>`. Standard I/O uses buffered `FILE *` streams and portable text conventions. UNIX low-level I/O uses integer descriptors and byte counts. A stream implementation can be built on top of that descriptor layer.

## From `FILE *` streams to descriptors

A file descriptor is a small nonnegative integer by which a process refers to an open file, device, pipe, or socket. By UNIX convention, a new process begins with three descriptors:

```text
0  standard input
1  standard output
2  standard error
```

Modern POSIX declares the basic byte operations as:

```c
ssize_t read(int fd, void *buf, size_t count);
ssize_t write(int fd, const void *buf, size_t count);
```

`read` returns the number of bytes transferred, `0` at end-of-file, or `-1` on error. `write` returns the number of bytes transferred or `-1` on error. K&R uses older declarations with `int` byte counts, but the model is the same.

Files are acquired and released with `open` and `close`:

```c
int fd = open(name, flags);
int fd = open(name, flags, mode); /* when O_CREAT is present */
int rc = close(fd);
```

Common `<fcntl.h>` flags include `O_RDONLY`, `O_WRONLY`, `O_RDWR`, `O_CREAT`, `O_TRUNC`, and `O_APPEND`.

```mermaid
flowchart LR
  A[User program] --> B["stdio FILE * streams"]
  B --> C["read()/write() system calls"]
  A --> C
  C --> D[Kernel open-file table]
  D --> E[Filesystem device or pipe]
```

| Layer | Handle | Typical operations | Buffering | Portability |
|---|---|---|---|---|
| Standard I/O | `FILE *` | `getc`, `printf`, `fgets`, `fwrite` | C library buffering | ISO C |
| UNIX descriptor I/O | `int fd` | `read`, `write`, `open`, `close`, `lseek` | kernel and device behavior | POSIX/UNIX |
| Filesystem metadata | path or descriptor plus `struct stat` | `stat`, `fstat` | not a data stream | POSIX, with system-specific fields |
| Directory traversal | `DIR *` | `opendir`, `readdir`, `closedir` | implementation-defined | POSIX |

Descriptors carry no C library buffer, formatting state, or text translation. They suit system programming, binary byte processing, and the implementation of higher-level libraries. The standard streams usually sit above descriptors 0, 1, and 2, but the standards do not require that mapping on every system.

The integer descriptor is a process-local table index. Its entry refers to an **open file description** maintained by the kernel, which contains status flags and the current file offset. The open file description in turn refers to an underlying file or other object. Two descriptors created by `dup`, or inherited across `fork`, can refer to the same open file description and therefore share its offset. Two separate calls to `open` on the same path normally create separate open file descriptions.

This distinction explains redirection. A shell can open an output file, duplicate that descriptor onto descriptor `1`, close the extra descriptor, and then execute a program. The program keeps writing to `STDOUT_FILENO`; only the table entry behind that number has changed. Pipes work similarly, replacing a standard descriptor with one end of a kernel byte channel.

The descriptor number can be reused immediately after `close`. Retaining a stale integer is dangerous because it may later name an unrelated file. Ownership rules should say which function closes a descriptor and whether a borrowed descriptor remains valid after the call.

### Opening a file is more than finding a path

When `O_CREAT` is present, `open` takes a permission mode such as `0644`. The process's file-creation mask removes requested permission bits, so the resulting mode is roughly `mode & ~umask`. Existing files keep their existing mode. `O_EXCL | O_CREAT` requests failure if the path already exists and supports atomic create-if-absent logic on filesystems that honor the POSIX semantics.

`O_TRUNC` discards an existing regular file's contents when it is opened for writing. It should appear only when replacement is intended. `O_APPEND` causes each write to position at the end as part of the write operation. Calling `lseek(fd, 0, SEEK_END)` before each write is not equivalent under concurrency: another writer may append between the seek and write.

Descriptors normally survive an `exec` operation unless marked close-on-exec. `O_CLOEXEC` asks `open` to set that property atomically, preventing a multithreaded program from briefly exposing the new descriptor to a concurrently executing child process. Leaked descriptors can keep files, pipes, or sockets alive unexpectedly.

## Short reads and partial writes

`read` may return fewer bytes than requested, including when more data may arrive later. `write` may accept only part of the supplied buffer. Pipes, terminals, sockets, signals, and resource limits make both cases ordinary concerns in systems code.

Suppose descriptor `0` contains the six bytes `abcdef`, and a program requests four bytes at a time. The first `read` can return `4`, producing `abcd`; the program writes those four bytes. The second read can return `2`, producing `ef`; it writes two bytes. A third read returns `0` for end-of-file. Passing the buffer's full capacity to both writes would incorrectly emit bytes that were not supplied by the corresponding read.

The copy loop below also retries calls interrupted by a signal and advances through partial writes:

```c
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

#define BUFSIZE 4096

static int copyfd(int in, int out)
{
    char buf[BUFSIZE];

    for (;;) {
        ssize_t n;

        do {
            n = read(in, buf, sizeof buf);
        } while (n < 0 && errno == EINTR);

        if (n == 0)
            return 0;
        if (n < 0)
            return -1;

        for (ssize_t done = 0; done < n;) {
            ssize_t written;

            do {
                written = write(out, buf + done, (size_t)(n - done));
            } while (written < 0 && errno == EINTR);

            if (written == 0) {
                errno = EIO;
                return -1;
            }
            if (written < 0)
                return -1;
            done += written;
        }
    }
}

int main(int argc, char *argv[])
{
    int fd;
    int status;

    if (argc == 1) {
        if (copyfd(STDIN_FILENO, STDOUT_FILENO) < 0) {
            perror("copy");
            return 1;
        }
        return 0;
    }

    fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        perror(argv[1]);
        return 1;
    }

    status = copyfd(fd, STDOUT_FILENO);
    if (status < 0)
        perror("copy");
    if (close(fd) < 0) {
        perror("close");
        status = -1;
    }

    return status == 0 ? 0 : 1;
}
```

The descriptor test must be `fd < 0`, not `!fd`: descriptor `0` is valid. Every successful `open` also needs a matching `close` along every path that has finished with the resource. Letting the integer variable leave scope does not close it.

`EINTR` means a signal interrupted the call before its normal completion. Retrying is often right, but the interface and call type still matter. A call can report a positive byte count even if a signal arrived after some transfer, and that positive result must be processed rather than discarded. Nonblocking descriptors introduce `EAGAIN` or `EWOULDBLOCK`, which means no progress is currently possible, not permanent failure. Event-driven programs wait for readiness instead of spinning in an immediate retry loop.

A successful `write` says the kernel accepted bytes; it does not promise that a storage device has committed them durably. Buffer-cache writeback, device caches, and filesystem semantics lie beyond the call. Software that needs a durability boundary uses the relevant synchronization operation and must still reason about metadata, directory entries, and hardware guarantees.

### Following four partial transfers

Suppose `copyfd` has read $10$ bytes and the output accepts only $4$, then $3$, then $3$ bytes. Initially `done = 0`, so the first call receives `buf + 0` and length $10$. It returns $4$, making `done = 4`. The second call receives `buf + 4` and length $10-4=6$; it returns $3$, making `done = 7`. The final call receives `buf + 7` and length $3$ and completes the buffer.

If the second call is interrupted before writing anything, the inner `do` loop retries with the same pointer and remaining count. If it had instead returned $3$, advancing by those $3$ bytes is mandatory even if a signal was also delivered. Restarting the full ten-byte write would duplicate the first four bytes.

## Seeking to a fixed-size record

Random access uses

```c
off_t lseek(int fd, off_t offset, int whence);
```

The `whence` argument is normally `SEEK_SET`, `SEEK_CUR`, or `SEEK_END`. File position belongs to the open file description, so descriptors that share an open file description also share the offset. Pipes and many other stream-like objects are not seekable.

For 32-byte records numbered from zero, record 5 begins at

$$
\begin{aligned}
offset &= i \times R \\
&= 5 \times 32 \\
&= 160.
\end{aligned}
$$

After

```c
if (lseek(fd, (off_t)160, SEEK_SET) == (off_t)-1)
    perror("lseek");
```

the next successful `read` or `write` begins at byte 160. The return value must be checked before assuming the position changed.

Seeking beyond the current end and then writing can create a **sparse file**. The unwritten gap reads as zero bytes but may occupy no data blocks. The logical size reported by `stat` can therefore exceed physical storage. Not every filesystem or output target supports holes in the same way.

Seeking to the end and writing is also unsafe as an ad hoc append protocol when several processes share a pathname through separate opens. Use append mode for atomic positioning of each individual write. Even then, a logical record split across several `write` calls may interleave with another writer's record.

Fixed-size records allow direct offset arithmetic only when the on-disk record width is actually fixed. Writing a C structure with `sizeof` bakes in padding, byte order, type widths, and alignment choices from the producing implementation. An interoperable file format encodes fields explicitly and validates short input before interpreting it.

## Keeping filesystem details behind an interface

`stat` fills a structure with metadata such as file size, mode, owner, and timestamps. Directory traversal uses `opendir`, `readdir`, and `closedir` on modern POSIX systems. K&R's historical `fsize` example defines its own small `Dirent` interface and confines the machine-dependent directory layout to a few routines.

That separation is the durable part of the example. Recursive `fsize` logic consumes path names and directory entries without knowing their on-disk representation. Only the boundary layer depends on the host's directory format. POSIX later standardized a directory API, but application code still benefits from keeping platform-specific fields and assumptions localized.

A directory entry supplies a name and usually an inode reference, but it does not guarantee that the named object remains unchanged after `readdir` returns. Another process can rename or remove it. Likewise, checking `stat(path)` and later opening `path` leaves a time-of-check to time-of-use gap. When identity or security matters, operate relative to an already opened directory and use descriptor-based operations where the platform provides them.

Symbolic links add another layer. `stat` follows a link and reports the target; `lstat` reports the link itself. Recursive traversal needs an explicit policy about following links, crossing filesystem boundaries, handling cycles, and reporting entries that disappear during the walk. Treating every error as fatal makes a whole tree scan fragile, while ignoring all errors produces misleading totals.

## Buffering, errors, and ownership boundaries

Descriptor I/O is byte-oriented. `read` does not append `'\0'`, preserve line boundaries, or perform formatted conversion. A program that wants records, lines, buffering, or text conversion must provide them or use a library layer that does.

Mixing `printf` and `write` on the same underlying output can reorder bytes because the `FILE *` layer buffers data independently. Flush or otherwise synchronize the stream before crossing between APIs, and follow the standard's rules when the stream is also used for input.

Low-level calls report failure through return values and `errno`, not exceptions. Check a negative result from `open`, `read`, `write`, or `lseek` before using it; `perror` and `strerror` turn the saved error number into a diagnostic. Historical K&R declarations should also be replaced with the current POSIX headers and types: `ssize_t`, `size_t`, and `off_t`.

`errno` is meaningful only when a function has indicated failure; successful calls may leave an old value in it. Preserve it if cleanup or logging calls could overwrite the failure being reported:

```c
int saved = errno;
close(fd);              /* best-effort cleanup */
errno = saved;
perror("read input");
```

`close` itself can fail, especially for output whose delayed errors surface during finalization. Retrying `close` blindly is not portable because the descriptor may already have been released and reused. The correct response depends on the system contract; at minimum, an output-close error must not be reported as successful completion.

## A pipe connects two ownership lifetimes

`pipe` creates a read end and a write end. After `fork`, each process inherits both descriptors, so each must close the ends it does not use. End-of-file appears to a reader only after every descriptor referring to the write end has closed.

```c
int p[2];

if (pipe(p) < 0)
    /* handle error */;

/* producer */
close(p[0]);
/* write data to p[1], then */
close(p[1]);

/* consumer in another process */
close(p[1]);
/* read p[0] until read returns 0, then */
close(p[0]);
```

If the consumer accidentally keeps its inherited write end open, its final `read` waits because the kernel still sees a possible writer. The bytes may all have arrived, yet EOF cannot occur. Many apparent pipe deadlocks are ownership errors of this form rather than missing data.

K&R uses the same boundary-oriented reasoning when it sketches allocation on top of the historical `sbrk` interface. Contemporary application code should use `malloc` and `free`; the example remains useful as an account of how a library can manage larger units obtained from the operating system.

<div className="see-also">

See also: [Standard I/O and Formatted I/O](/cs/programming/c/standard-io-formatted-io) · [File Access and Error Handling](/cs/programming/c/file-access-error-handling) · [Storage Allocation](/cs/programming/c/storage-allocation) · [Structures, Typedef, Unions, and Bit Fields](/cs/programming/c/structures-typedef-unions-bitfields) · [Modern C Considerations](/cs/programming/c/modern-c-considerations)

</div>
