---
title: Separate Compilation and Namespaces
sidebar_position: 10
---

# Separate Compilation and Namespaces

Small examples fit in one file, but real C++ programs are built from components. Separate compilation divides a program into interface files, implementation files, and application files so that classes can be reused and changes can be compiled in smaller pieces. Namespaces solve a different organization problem: they let code from different libraries use the same short names without colliding.

Savitch frames separate compilation as a practical extension of encapsulation. A class interface says what users may do. A class implementation says how the work is done. Those two ideas should be separate in the programmer's mind, and C++ lets them be separated into header and source files.

## Translation units and source boundaries

A **header file** usually has extension `.h` or `.hpp` and contains declarations: class definitions, function prototypes, constants, and comments explaining the public interface.

```cpp
// clock_time.h
#ifndef CLOCK_TIME_H
#define CLOCK_TIME_H

class ClockTime {
public:
    ClockTime();
    ClockTime(int hour, int minute);
    void advance(int minutes);
    int hour() const;
    int minute() const;

private:
    int hour_;
    int minute_;
};

#endif
```

An **implementation file** usually has extension `.cpp` and contains function definitions.

```cpp
// clock_time.cpp
#include "clock_time.h"

ClockTime::ClockTime() : hour_(0), minute_(0) {}
```

An **application file** contains `main` or other client code using the component.

```cpp
#include "clock_time.h"

int main() {
    ClockTime now(9, 30);
    now.advance(15);
}
```

An **include guard** prevents multiple inclusion of the same header.

```cpp
#ifndef CLOCK_TIME_H
#define CLOCK_TIME_H
// declarations
#endif
```

A **namespace** groups declarations under a qualified name.

```cpp
namespace calendar {
    class Date {};
}

calendar::Date due;
```

A **using directive** makes all names from a namespace available in a scope:

```cpp
using namespace std;
```

A **using declaration** makes one name available:

```cpp
using std::cout;
```

After preprocessing, one `.cpp` file together with the text of all included headers forms a **translation unit**. Compilation checks each translation unit independently. The compiler does not consult another `.cpp` file to discover a missing declaration. Object files preserve compiled code and unresolved references; the linker later resolves those references across translation units and libraries.

`#include` is textual inclusion. If two headers include the same third header, its guard ensures that its contents appear only once in that translation unit. The guard does not make the header a separately compiled unit, nor does it prevent the same declarations from appearing in other translation units where they are needed.

## What belongs in a header

Header files are included by the preprocessor before compilation. The compiler then sees the declarations in every file that includes the header. The implementation file and application file are compiled separately, then the linker connects function calls to definitions.

The usual class split is:

| File | Contains | Should avoid |
|---|---|---|
| `.h` / `.hpp` | class definition, function declarations, inline definitions, constants | ordinary non-inline function bodies |
| `.cpp` | member function definitions, helper functions, static data definitions | duplicate public declarations |
| application `.cpp` | `main`, use of public interface | depending on private representation |

Private members appear in a header because the compiler needs the full class layout. They are still implementation details because client code cannot access them directly.

A change to a `.cpp` implementation usually requires recompiling that `.cpp` file and relinking. A change to a header may require recompiling every file that includes it, directly or indirectly.

Use quotes for project headers and angle brackets for standard headers:

```cpp
#include "clock_time.h"
#include <iostream>
```

Namespaces should be used to avoid global-name pollution. A header should generally not write `using namespace std;` because that forces the directive onto every file that includes it. Prefer fully qualified names or narrow using declarations in implementation files.

Unnamed namespaces in implementation files can hide helper functions from other translation units:

```cpp
namespace {
    int digitToInt(char ch) {
        return ch - '0';
    }
}
```

The one-definition rule coordinates separately compiled code. A non-inline function or variable that is odr-used normally has one definition in the whole program. A class definition, template, or inline function may appear in several translation units when each permitted definition is equivalent. Violations are not always diagnosed; mismatched class definitions produced by inconsistent macros can compile and then behave unpredictably.

Templates generally need their full definitions visible at the point of instantiation, so template implementations commonly stay in headers or header-included implementation files. Ordinary function bodies do not need that visibility and can live in `.cpp` files. `inline` permits a function definition in multiple translation units; the keyword does not guarantee call-site substitution.

Headers should include what they use. If a public declaration contains `std::string` by value, include `<string>` rather than hoping another header happened to include it first. A forward declaration can reduce dependencies when only a pointer or reference to an incomplete class appears:

```cpp
class OutputDevice;
void writeReport(OutputDevice& device);
```

The complete definition becomes necessary when code needs the object's size, accesses members, derives from it, or destroys an owning value in a context where the destructor requires completeness. Forward declarations are dependency tools, not a way around type information.

Changing private data in an ordinary class changes its size and therefore the header-visible layout, requiring client recompilation. The pointer-to-implementation idiom can hide that layout behind an owning pointer, trading an allocation and indirection for a more stable binary boundary. It is useful for selected library interfaces, not a default requirement for small programs.

## From two source files to one executable

```mermaid
flowchart LR
  H[clock_time.h declarations] --> C1[clock_time.cpp compile]
  H --> C2[main.cpp compile]
  C1 --> O1[clock_time.o]
  C2 --> O2[main.o]
  O1 --> L[linker]
  O2 --> L
  L --> EXE[program executable]
```

| Namespace tool | Scope effect | Typical use |
|---|---|---|
| `std::cout` | names one entity exactly | safest in headers |
| `using std::cout;` | imports one name | convenient in `.cpp` |
| `using namespace std;` | imports many names | acceptable in small examples, risky in headers |
| `namespace app { ... }` | defines project scope | library organization |
| unnamed namespace | file-local internal names | helper functions in `.cpp` |

Linkage determines whether identical spellings in different translation units name the same entity. Names in an unnamed namespace have internal linkage, so each translation unit receives its own distinct helper. Public component functions normally have external linkage and can be referenced from other object files. `static` at namespace scope is an older way to request internal linkage; unnamed namespaces can also contain types and related helpers cleanly.

## Worked example: splitting a time class

Problem: Place a `ClockTime` class into a header, implementation, and application file.

Method:

1. Put the class declaration and include guard in `clock_time.h`.
2. Put member definitions in `clock_time.cpp`.
3. Include the header in both `.cpp` files.
4. Compile both `.cpp` files.
5. Link the resulting object files.

Header:

```cpp
// clock_time.h
#ifndef CLOCK_TIME_H
#define CLOCK_TIME_H

class ClockTime {
public:
    ClockTime();
    ClockTime(int hour, int minute);
    void advance(int minutes);
    int hour() const;
    int minute() const;

private:
    int hour_;
    int minute_;
};

#endif
```

Implementation:

```cpp
// clock_time.cpp
#include "clock_time.h"

ClockTime::ClockTime() : hour_(0), minute_(0) {}

ClockTime::ClockTime(int hour, int minute)
    : hour_(hour), minute_(minute) {}

void ClockTime::advance(int minutes) {
    int total = hour_ * 60 + minute_ + minutes;
    total %= 24 * 60;
    if (total < 0) {
        total += 24 * 60;
    }
    hour_ = total / 60;
    minute_ = total % 60;
}

int ClockTime::hour() const {
    return hour_;
}

int ClockTime::minute() const {
    return minute_;
}
```

Application:

```cpp
// main.cpp
#include <iostream>
#include "clock_time.h"

int main() {
    ClockTime time(23, 50);
    time.advance(20);
    std::cout << time.hour() << ":" << time.minute() << '\n';
}
```

Checked answer: `23:50 + 20 minutes = 24:10`, normalized to `0:10`, so output is `0:10`.

The constructor currently assumes `0 <= hour < 24` and `0 <= minute < 60`. That precondition should be documented or enforced. The `advance` calculation handles negative minute deltas by applying remainder and then adding one day when needed. It can overflow `int` for an extreme argument; a robust version would reduce the delta modulo one day before adding or use a wider checked type.

Compiling `clock_time.cpp` verifies its definitions against the declaration because it includes its own header first. If `hour()` accidentally omitted its trailing `const`, the compiler would see a definition of a different, undeclared member rather than allowing a mismatch to reach callers.

## Worked example: resolving namespace collisions

Problem: Two libraries each define a function named `greeting`. Call both without renaming either function.

Method:

1. Place each function in a different namespace.
2. Call with fully qualified names.
3. Avoid a broad `using namespace` that would make `greeting()` ambiguous.

```cpp
#include <iostream>

namespace morning {
    void greeting() {
        std::cout << "Good morning\n";
    }
}

namespace evening {
    void greeting() {
        std::cout << "Good evening\n";
    }
}

int main() {
    morning::greeting();
    evening::greeting();
}
```

Checked answer: both calls compile because `morning::greeting` and `evening::greeting` are distinct qualified names. An unqualified call to `greeting()` would be ambiguous if both namespaces were imported into the same scope.

Namespaces are open: declarations for `namespace morning` may appear in several files and all contribute to the same namespace. Nested namespace syntax such as `namespace company::payroll` organizes larger libraries. A namespace alias can shorten a long qualified name locally without importing every member.

## A component enclosed in its project namespace

This single-file demonstration mimics a namespace-wrapped component. In a real project, place declarations in a header and definitions in a `.cpp`.

```cpp
#include <iostream>
#include <string>

namespace payroll {
    class Employee {
    public:
        Employee(std::string name, int id)
            : name_(name), id_(id) {}

        std::string name() const {
            return name_;
        }

        int id() const {
            return id_;
        }

    private:
        std::string name_;
        int id_;
    };

    void printBadge(const Employee& employee) {
        std::cout << employee.id() << " - " << employee.name() << '\n';
    }
}

int main() {
    payroll::Employee employee("Ada", 1001);
    payroll::printBadge(employee);
}
```

Argument-dependent lookup also consults namespaces associated with argument types. In `printBadge(employee)`, an unqualified call can find `payroll::printBadge` because `employee` has a type from `payroll`. This rule supports nonmember operators and customization functions near their types, but broad using directives can add candidates and create ambiguities that appear far from the directive.

## Compile errors, link errors, and stale boundaries

- Putting non-inline function definitions in headers and causing multiple-definition linker errors.
- Forgetting include guards or `#pragma once`.
- Writing `using namespace std;` in a header file.
- Including `.cpp` files instead of compiling and linking them, except in special template-only patterns.
- Changing a header and recompiling only one dependent file.
- Letting application code depend on private representation.
- Confusing the global namespace with an unnamed namespace.
- Assuming namespace qualification changes object lifetime or storage. It only qualifies names.

At the build boundary:

- Put declarations needed by clients in the header and implementation details in the `.cpp` file. A header is a contract; it should not expose helper functions or private representation that clients do not need.
- Include the header in its own `.cpp` implementation file. This lets the compiler verify that declarations and definitions match.
- Use include guards or `#pragma once` to prevent repeated inclusion from producing duplicate declarations during preprocessing.
- Avoid `using namespace std;` in header files. It forces every file that includes the header to inherit the namespace decision.
- Keep namespace names meaningful and stable. A namespace is part of the name clients write, so casual renaming can break many files.
- Remember that separate compilation does not mean separate type systems. All translation units must agree on class definitions, function declarations, constants, and template definitions.
- When debugging linker errors, distinguish "not declared" from "declared but not defined." The first is usually a header or include problem; the second is usually a missing `.cpp` file in the build or a signature mismatch.

A useful isolation test includes the header first in a file that does nothing else. It should compile without hidden prior includes or using-directives. A self-sufficient header includes what it needs, declares only the public interface, and can be read as the contract for that module.

For linker errors, compare the exact spelling of the declaration and definition: namespace, class scope, parameter types, `const` qualifiers, and return type context. `void f(int)` and `void f(double)` are different functions; `int Account::balance() const` and `int Account::balance()` are different member function signatures for linking and overload resolution.

Changing an implementation file should not force unnecessary recompilation of clients. If clients include only the stable header and the header avoids needless implementation details, separate compilation gives both clearer boundaries and faster rebuilds in larger programs.

Splitting a one-file class program into `Type.h`, `Type.cpp`, and `main.cpp` is easiest in stages. First move only the declaration, then the member definitions, then remove unnecessary includes from `main.cpp`. Compiling after each move exposes each header's responsibility without one large confusing break.

Also inspect object-file boundaries conceptually. The compiler checks each `.cpp` file using the headers it includes; the linker later connects calls to definitions. Many build errors become easier once those two phases are kept separate.

A header should compile cleanly when included first.

Circular inclusion usually indicates that two headers know too much about one another. Include guards stop infinite textual recursion, but one class may still be incomplete where a by-value member requires its full definition. Replacing one by-value dependency with a pointer or reference and a forward declaration can break the cycle; often the clearer repair is extracting the genuinely shared concept into a third header.

Macros cross namespace boundaries because the preprocessor runs before C++ name lookup. A macro named `min` can interfere with `std::min` despite the qualification. Constants, inline functions, and templates obey scope and type rules and should replace macros for most ordinary language-level facilities.

Binary compatibility is stricter than source compatibility. Changing class layout, virtual function order, calling conventions, or inline definitions can require rebuilding consumers even when their source still compiles. Within a single project, a clean dependency-aware rebuild handles this. Distributed binary libraries need explicit ABI policy beyond the basic header/source split.

## Related pages

- [classes and encapsulation](/cs/programming/cpp/classes-and-encapsulation)
- [constructors and copy semantics](/cs/programming/cpp/constructors-and-copy-semantics)
- [streams and file I/O](/cs/programming/cpp/streams-and-file-io)
- [templates](/cs/programming/cpp/templates)
- [STL containers](/cs/programming/cpp/stl-containers)
