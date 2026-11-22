---
title: Exception Handling
sidebar_position: 17
---

# Exception Handling

Exception handling gives C++ a structured way to report and respond to unusual errors without forcing every function to return a special error code. Savitch presents exceptions after classes and dynamic memory because exceptions interact with control flow, object lifetime, and resource cleanup.

The central pattern is `try`, `throw`, and `catch`. Code that may detect an exceptional condition throws an exception object. Code that knows how to recover catches it. Functions in between do not need to pass the error manually, but they must still be written so local objects clean themselves up correctly during stack unwinding.

## Throwing changes the ordinary return path

A **throw expression** raises an exception:

```cpp
throw DivideByZero();
```

A **try block** encloses code that may throw:

```cpp
try {
    result = quotient(numerator, denominator);
}
```

A **catch block** handles exceptions of a matching type:

```cpp
catch (const DivideByZero& e) {
    cout << "division by zero" << endl;
}
```

An **exception class** is a class used as an exception type. It may be empty when the type alone communicates the error, or it may store a message and related values.

```cpp
class NegativeNumber {
public:
    explicit NegativeNumber(double value) : value(value) {}
    double getValue() const { return value; }
private:
    double value;
};
```

**Stack unwinding** is the process of leaving functions between the throw point and the catch point. Local objects in those functions are destroyed as the stack unwinds, which is why destructors and RAII are so important.

**RAII** means Resource Acquisition Is Initialization: a resource is owned by an object whose destructor releases it. If an exception leaves a scope, destructors still run for fully constructed local objects.

A handler is considered only for a dynamically enclosing `try` block. The search begins in the current function and continues through callers. Once a matching handler is found, control does not return to the throw point; after the handler finishes, execution continues after the handler sequence. Retrying an operation therefore requires an explicit loop around the `try`, not an assumption that `catch` resumes the failed statement.

Exception objects are copied or moved into storage managed by the runtime, so throwing a local exception object does not leave a dangling object by itself. Data stored inside it can still dangle if it is a pointer or reference into a local variable. Standard exception types own their diagnostic message and expose it through `what()`.

## Matching, unwinding, and recovery boundaries

The nearest matching catch block handles the exception. Matching is based on type, so catch blocks should be ordered from more specific to more general:

```cpp
try {
    // work
} catch (const FileOpenError& e) {
    // specific
} catch (const std::exception& e) {
    // general
}
```

Catch exception objects by `const` reference unless there is a clear reason not to. This avoids copying and preserves derived exception information:

```cpp
catch (const runtime_error& e) {
    cout << e.what() << endl;
}
```

Exceptions are best for exceptional conditions, not ordinary loop decisions. A missing optional value, a normal end-of-file state, or a user choosing "quit" is often better represented by ordinary control flow.

When a function cannot handle an exception, it should usually let the exception continue to a caller that can handle it. A catch block can rethrow the same exception with `throw;`.

Historically, older C++ books discuss exception specifications such as `throw(Type)`. Modern C++ has deprecated and removed dynamic exception specifications, so new code should not use them. The durable ideas are still the same: document what can fail, use precise exception types, and write resource-owning classes so cleanup is automatic.

A useful correctness rule is this: after any exception, every object that was fully constructed before the throw must be in a valid destroyed or still-usable state. Raw `new` followed by later throwing code is therefore fragile unless ownership is transferred to a class object.

Exception matching does not perform arbitrary conversions. A handler for a base class can catch an object of a publicly derived type, and a catch-all handler written `catch (...)` matches anything. Otherwise the handler needs the same type apart from limited qualification adjustments. Standard exceptions derive from `std::exception`, so an outer application boundary can log `what()` for many library failures while inner layers still catch specific types when they know a recovery.

Three exception guarantees are common vocabulary for library operations:

| Guarantee | State after failure |
|---|---|
| no-throw | the operation will not emit an exception |
| strong | visible state is unchanged |
| basic | invariants hold and resources do not leak, but values may change |

No guarantee means even validity may be uncertain. The strong guarantee often uses a temporary result followed by a non-throwing commit. The basic guarantee is still useful for operations that update several elements incrementally, provided the object remains usable and cleanup is complete.

`noexcept` is part of a function's contract. If an exception escapes a `noexcept` function, the program calls `std::terminate`; callers do not get a chance to catch it. Destructors are normally non-throwing, and move operations often declare `noexcept` so containers can move elements safely during reallocation. Marking a function `noexcept` merely for speed is unsound unless every called operation also satisfies the promise.

## Following an exception through the call stack

```mermaid
flowchart TD
  A[Call function] --> B[Enter try block]
  B --> C{"Error detected?"}
  C -->|no| D[Continue normally]
  C -->|yes| E[throw exception object]
  E --> F[Unwind stack]
  F --> G{"Matching catch?"}
  G -->|yes| H[Run handler]
  G -->|no| I[Continue unwinding]
  H --> J[Program resumes after catch]
```

| Strategy | How error is reported | Strength | Risk |
|---|---|---|---|
| Return code | Return special value | Simple and explicit | Caller may ignore it |
| Output parameter | Fill status variable | Works with normal return value | Clutters interfaces |
| Exception | `throw` object | Separates error path from main path | Can hide control flow if overused |
| Program exit | Call `exit` or terminate | Stops unsafe continuation | Prevents caller recovery |

Calling `std::exit` is different from returning from `main` or throwing to a handler: automatic local objects on the abandoned stack are not destroyed. Static-storage objects are handled separately. Code that relies on RAII cleanup should prefer normal scope exit or controlled exception propagation.

## Worked example: division by zero

Problem: Write a function `safeDivide(10, 0)` that reports division by zero with an exception, then trace the control flow.

Method:

1. Define an exception type:

   ```cpp
   class DivideByZero {};
   ```

2. Define the function:

   ```cpp
   double safeDivide(double numerator, double denominator) {
       if (denominator == 0.0) {
           throw DivideByZero();
       }
       return numerator / denominator;
   }
   ```

3. Call it inside a try block:

   ```cpp
   try {
       cout << safeDivide(10.0, 0.0) << endl;
   } catch (const DivideByZero&) {
       cout << "cannot divide by zero" << endl;
   }
   ```

4. Trace the evaluation:

   - `safeDivide(10.0, 0.0)` starts.
   - The test `denominator == 0.0` is true.
   - The function throws `DivideByZero()`.
   - The return statement is skipped.
   - Control jumps to the matching catch block.

Checked answer: the program prints `cannot divide by zero`. It does not attempt to compute `10.0 / 0.0`.

For floating-point arithmetic, the language and hardware may produce an infinity for division by zero rather than raising a C++ exception. `safeDivide` creates its own domain policy by testing first. The exact comparison is appropriate when rejecting a literal zero denominator; deciding whether a very small nonzero value is numerically acceptable is a separate, application-dependent condition.

## Worked example: preserving diagnostic values

Problem: A square-root function should reject negative inputs and report the offending value. What does `checkedSqrt(-9.0)` do?

Method:

1. Define an exception class that stores the invalid value:

   ```cpp
   class NegativeNumber {
   public:
       explicit NegativeNumber(double value) : value(value) {}
       double getValue() const { return value; }
   private:
       double value;
   };
   ```

2. Define the function:

   ```cpp
   double checkedSqrt(double value) {
       if (value < 0.0) {
           throw NegativeNumber(value);
       }
       return sqrt(value);
   }
   ```

3. Evaluate `checkedSqrt(-9.0)`:

   - `value` is `-9.0`.
   - The condition `value < 0.0` is true.
   - The function constructs `NegativeNumber(-9.0)`.
   - The function throws that object.

4. Catch it:

   ```cpp
   catch (const NegativeNumber& e) {
       cout << "negative input: " << e.getValue() << endl;
   }
   ```

Checked answer: the handler can print `negative input: -9`, so the exception carries both the error category and the data needed to explain it.

For `-0.0`, the comparison `value < 0.0` is false and `std::sqrt` returns negative zero on usual IEEE-754 implementations. For a NaN input, the comparison is also false and the NaN propagates. If the function's contract accepts only finite real values, it should test `std::isfinite(value)` as well as the sign. “Negative” and “outside the accepted domain” are not always identical predicates in floating-point code.

## Two small handler designs

```cpp
#include <cmath>
#include <iostream>
#include <stdexcept>
using namespace std;

double checkedSqrt(double value) {
    if (value < 0.0) {
        throw invalid_argument("square root of a negative number");
    }
    return sqrt(value);
}

int main() {
    double values[] = {25.0, -4.0, 9.0};

    for (int i = 0; i < 3; ++i) {
        try {
            cout << "sqrt(" << values[i] << ") = "
                 << checkedSqrt(values[i]) << endl;
        } catch (const invalid_argument& e) {
            cout << "error for " << values[i] << ": "
                 << e.what() << endl;
        }
    }
}
```

The first program places the `try` inside the loop. A bad element reports one error and the next element is still processed. Moving the `try` outside the loop would abandon the remaining iterations after the first throw. Handler placement therefore expresses whether failure belongs to one item or to the whole batch.

```cpp
#include <iostream>
#include <string>
using namespace std;

class BadInput {
public:
    explicit BadInput(string message) : message(message) {}
    string getMessage() const { return message; }
private:
    string message;
};

int readAge(int age) {
    if (age < 0) {
        throw BadInput("age cannot be negative");
    }
    if (age > 150) {
        throw BadInput("age is unrealistically large");
    }
    return age;
}

int main() {
    try {
        cout << readAge(42) << endl;
        cout << readAge(-3) << endl;
    } catch (const BadInput& e) {
        cout << e.getMessage() << endl;
    }
}
```

The second program has one `try` around both calls. Once `readAge(-3)` throws, the handler runs and no later statement in that try block would execute. A standard `std::out_of_range` or `std::invalid_argument` would integrate with the standard exception hierarchy; a custom type is most useful when callers need a distinct category or structured fields beyond a message.

## Failure modes in exception-using code

- Catching a general exception type before a specific one. The specific handler may become unreachable.
- Throwing raw string literals everywhere instead of using meaningful exception classes or standard exception types.
- Catching by value and accidentally slicing derived exception objects.
- Using exceptions for normal loop control or ordinary input validation that can be handled locally.
- Allocating memory with `new` and then throwing before ownership is protected by a class object. Prefer standard containers or resource-owning classes.
- Assuming code after `throw` in the same block will run. A throw transfers control immediately.

During an exception-safety review:

- Decide where recovery belongs. A low-level function can detect that a file failed to open, but the caller may be the only code that knows whether to ask for another filename, use a default file, or stop the program.
- Keep thrown objects informative but small. A type and a short message are often enough; storing large buffers or references to local variables inside an exception object creates new lifetime risks.
- Do not catch an exception just to print a message and continue as if the failed operation succeeded. After a catch block, the program state should be known and valid.
- Use destructors for cleanup, not catch blocks scattered throughout the program. If a resource is owned by an object, stack unwinding will call the destructor automatically.
- Make catch blocks narrow. Catching every exception at a deep level with `catch (...)` can hide programming errors and make debugging much harder.
- Check whether a function can provide the strong guarantee: either it completes successfully, or the visible state is unchanged. Copy-then-swap assignment is a common way to reach this behavior for resource-owning classes.
- Treat exceptions and file streams carefully together. Opening a stream, reading data, and validating the result are separate steps; exceptions can report invalid states, but the program still needs to check what recovery is sensible.

For each exception a function can throw, complete the sentence "the caller can recover by ...". If no reasonable recovery exists at that level, do not catch it there. Let it travel to a part of the program that can choose a fallback, ask the user for new input, roll back a transaction, or end the program with a useful diagnostic.

An exception should leave enough context to diagnose the failure. "Bad input" is less useful than "negative radius" or "could not open scores.txt." Precise exceptions help the caller recover and help the programmer find the failing assumption during testing.

Translating one return-code example to exceptions and back is a useful design test. If every caller must handle the failure immediately in the same way, a return value may be simpler. If failure must travel through several layers to a meaningful recovery point, exceptions usually express the control flow more cleanly.

Rethrowing has two spellings with different effects. `throw;` inside a handler preserves the currently handled exception object and its dynamic type. `throw e;` throws a new object from the handler variable; if `e` has a base type, that can slice derived information. The bare form is the normal choice after adding context or rolling back local work.

Constructors have no failure return value, so exceptions fit failed construction well. If a constructor throws, the object never comes into existence, but already initialized members and bases are destroyed. A raw resource acquired in the constructor body before a later throwing operation can leak because the class destructor will not run. Acquiring it directly into a smart pointer, container, or member wrapper closes that gap.

Catch-all handlers belong mainly at boundaries such as a thread entry function or `main`, where no exception may safely escape. They can perform logging and controlled shutdown, but they cannot inspect an unknown exception through `what()`. Swallowing one and continuing with uncertain state converts a diagnosable failure into later corruption.

## Related pages

- [constructors and copy semantics](/cs/programming/cpp/constructors-and-copy-semantics)
- [file I/O](/cs/programming/cpp/streams-and-file-io)
- [classes and encapsulation](/cs/programming/cpp/classes-and-encapsulation)
- [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory)
- [stl containers](/cs/programming/cpp/stl-containers)
