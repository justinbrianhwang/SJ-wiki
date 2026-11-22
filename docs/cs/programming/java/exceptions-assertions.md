---
title: Exceptions and Assertions
sidebar_position: 11
---

# Exceptions and Assertions

Exceptions separate ordinary control flow from unexpected failure. A method can throw an exception when it cannot complete its contract, and callers either handle that exception or allow it to propagate. The source book treats exception design as a clarity tool: code should not be buried under error checks, but exceptions should not be abused for expected situations such as normal end-of-input.

Assertions serve a different purpose. An assertion checks a condition that should be true if the program logic is correct, such as an invariant, precondition, or postcondition. Assertions can be enabled or disabled, so they are a debugging and validation aid rather than a substitute for required argument checks in public APIs.

## Four kinds of failure signal

Chapter 12 covers exception types, `throw`, `throws`, `try`, `catch`, `finally`, chaining, stack traces, and assertions. The central question is whether a condition belongs to ordinary control flow, a recoverable API failure, a programming error, or an internal invariant check.

**Exception.** An object representing an abnormal condition that interrupts normal control flow. It is thrown and may be caught by a matching handler.

**Checked exception.** An exception that must be declared or caught. The compiler prevents callers from accidentally ignoring declared recoverable failures.

**Unchecked exception.** A `RuntimeException` or `Error` subclass, usually representing a programming error or a condition not intended for ordinary recovery.

**`throw`.** A transfer of control using an exception object. Execution resumes only if stack unwinding finds a matching handler.

**`throws` clause.** The checked exceptions that a method or constructor may let escape; part of its contract.

**`try`, `catch`, `finally`.** `try` protects a block, `catch` handles selected exceptions, and `finally` runs cleanup after normal completion, exception, or most control transfers.

**Exception chaining.** Recording an underlying cause when translating one exception into another, preserving diagnostic information across abstraction boundaries.

**Assertion.** A boolean check that throws `AssertionError` when assertions are enabled and the condition is false.

## Choosing between returns, exceptions, and assertions

**Use exceptions for exceptional contract failure, not ordinary loop endings.** The source contrasts a return flag for expected end-of-input with an exception for reading past the end. If a condition is normal and easy to test, a direct condition is clearer than exception-driven looping.

**Checked exceptions document recoverable obligations.** A checked exception in a `throws` clause tells the caller to address or propagate a possible failure. The API should not force callers to catch failures they cannot meaningfully handle.

**`finally` preserves cleanup across exits.** A `finally` block runs when the `try` block completes normally, throws, returns, breaks, or continues, unless the VM terminates. The source-era cleanup idiom is therefore `try` plus `finally`; try-with-resources came later.

**Do not let `finally` hide the original reason for exit.** If a `finally` block throws or returns, it can replace the original exception or return reason. Cleanup should avoid a new control transfer unless that replacement is intended.

**Assertions are for internal truth, not user input validation.** A public method must reject invalid arguments even when assertions are disabled. Assertions suit conditions that should be impossible in correct code, such as an internal postcondition.

When designing error handling, classify each condition before writing code. Is it expected and common, like reaching the end of a token stream? Use a normal condition or return value. Is it a recoverable failure that the caller can address, like an I/O problem? A checked exception may make the contract explicit. Is it a programming error, like passing `null` where the contract forbids it? An unchecked exception may be appropriate. Is it an invariant that should never fail inside correct code? Use an assertion during development. This classification is more important than memorizing exception class names.

```mermaid
flowchart TD
  A[Method starts] --> B{"Can complete contract?"}
  B -->|yes| C[Return normally]
  B -->|no| D{"Expected condition?"}
  D -->|yes| E[Return status or value]
  D -->|recoverable failure| F[Throw checked exception]
  D -->|programming error| G[Throw unchecked exception]
  F --> H[Caller catches or declares]
  G --> I[Usually fix code]
```

| Mechanism | Use for | Avoid for |
|---|---|---|
| Return value | Expected alternatives | Hidden serious failure |
| Checked exception | Recoverable failure callers must see | Routine loop termination |
| Unchecked exception | Programming errors or contract violations | Normal user choices |
| `finally` | Cleanup after any exit | Returning over an existing exception |
| Assertion | Internal invariant checks | Required public validation |

## End-of-input belongs in the loop condition

Problem: A token reader reaches the end of input. Should `next()` throw an exception to end a loop?

Method:

1. Classify end-of-input. In a reader, reaching the end is expected and common.
2. If `next()` throws to signal the normal end, the loop may look infinite and the exit condition is hidden in a `catch` block.
3. Provide a test such as `hasNext()` or an end marker if a marker value is unambiguous.
4. Use an exception for reading past the end after the caller failed to check, because that violates the reader's contract.
5. Write the loop with the normal condition visible: `while (reader.hasNext()) process(reader.next());`.

Checked answer: Normal end-of-input should not be exception-driven. A visible condition is clearer; an exception is appropriate for misuse such as reading after the end.

## Closing a stream through every exit

Problem: Open a stream, read data, and ensure the stream is closed if reading succeeds, fails, or returns early.

Method:

1. Declare the stream reference outside the `try` so the `finally` block can see it.
2. Assign the stream after opening. If opening fails, the reference remains `null` and there is nothing to close.
3. Perform reading inside the `try`. The read code may return normally, return early, or throw an exception.
4. In `finally`, check whether the stream is non-null before closing it.
5. Avoid allowing a close failure to hide the more important read failure unless that is the intended API behavior.

Checked answer: The checked source-era idiom is `try` plus `finally` with a null check. Later Java try-with-resources automates this pattern, but it is not covered by the source book.

## Source-era cleanup with `finally`

```java
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

public class ExceptionDemo {
    static int firstByte(byte[] data) throws IOException {
        InputStream in = null;
        try {
            in = new ByteArrayInputStream(data);
            int value = in.read();
            if (value < 0) {
                throw new IOException("empty input");
            }
            assert value >= 0 && value <= 255;
            return value;
        } finally {
            if (in != null) {
                in.close();
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.println(firstByte(new byte[] { 65, 66 }));
    }
}
```

## Lost causes and hidden exits

- Do not use exceptions to hide ordinary control flow such as an expected loop ending.
- Do not catch an exception and discard it silently unless the contract explicitly says the failure is irrelevant.
- Do not let a `finally` block return or throw accidentally, because it can replace the original reason for leaving the `try` block.
- Do not use assertions to validate public method arguments that must be checked in production.
- Do not translate exceptions without preserving the cause when the lower-level failure is diagnostically important.

<div className="see-also">

See also:

- [I/O Streams, Files, Serialization, and NIO](/cs/programming/java/io-streams-files-serialization-nio): uses checked `IOException` and cleanup idioms.
- [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation): uses exceptions to enforce object contracts.
- [Control Flow, Arrays, and Strings](/cs/programming/java/control-flow-arrays-strings): contrasts normal branch/loop control with exceptional transfer.
- [Threads, Synchronization, and the Memory Model](/cs/programming/java/threads-synchronization-memory-model): explains exceptions crossing thread boundaries and synchronization cleanup.

</div>
