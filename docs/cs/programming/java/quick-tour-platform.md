---
title: Quick Tour, Platform, and First Programs
sidebar_position: 2
---

# Quick Tour, Platform, and First Programs

A small Java program already exposes the language's main structure. A class contains a `main` method, the method executes statements, objects receive method calls, and the standard library supplies objects such as `System.out`. The source book moves through these ideas quickly before returning to their precise rules in later chapters.

The platform matters as much as the syntax. Java source is compiled to bytecode, a virtual machine loads and verifies that bytecode, and the runtime connects the program to class loading, memory management, threads, security checks, and standard services. Portability depends on that shared execution model as well as on the source language.

Historically, the **JDK** is the development kit: compiler, launcher, documentation tools, and the components needed to run Java programs. The **JVM** is the abstract machine that executes class files. “Java runtime” refers more broadly to the VM plus standard libraries and supporting files. Product packaging has changed across releases, but these roles remain a useful mental split when diagnosing whether a problem belongs to source compilation, launching, or execution.

## Reading the first class

```java
public class QuickTourDemo {
    private static final String GREETING = "Hello";

    public static void main(String[] args) {
        String target = args.length == 0 ? "Java" : args[0];
        for (int i = 0; i < 3; i++) {
            System.out.println(GREETING + ", " + target + " #" + (i + 1));
        }
    }
}
```

A **class** declares fields, methods, constructors, nested types, and initialization behavior. Java has no free-standing functions, so even this procedural-looking example places its behavior in a class.

The conventional application entry point is a `public static` method named `main` with a `String[]` parameter. It belongs to the class, and the virtual machine invokes it to start the application. The parameter holds references to the command-line argument strings.

Each modifier has a job. `public` permits the launcher to access the method. `static` means no `QuickTourDemo` instance is needed. `void` means the method returns no status value to its caller. Process success is normally represented by returning from `main`; `System.exit(int)` can request a particular process status but also begins virtual-machine shutdown immediately.

The parameter spelling `String... args` is also valid because a variable-arity parameter is represented as an array. Command-line parsing happens outside `main`; Java receives already separated strings. Quotes used by a shell usually group one argument and are removed before Java sees it, with details depending on the operating system and launcher environment.

The example also previews constants, local variables, arrays, a conditional expression, a loop, string concatenation, and a library call. Those features are compact here; later chapters supply the exact typing and execution rules.

## Two selections in `System.out.println`

`System.out.println("Hello")` contains ordinary field selection and method invocation:

1. `System` names a class from `java.lang`, whose types are automatically available without an explicit import.
2. `System.out` selects the static field `out`. Its value is a reference to a `PrintStream` object associated with standard output.
3. `.println` selects a method from that object, and the string literal becomes its argument.
4. The method writes the characters followed by a line separator, then control returns to the next statement.

A **reference** is a value through which a program interacts with an object. Variables of class, interface, array, and enum types hold references; they do not contain the entire object inline. `System.out` is therefore library state reached through normal Java syntax, not a special printing construct.

Tracing each dot is a useful first reading technique: ask which type or object supplies the selected field or method.

Overloading is resolved from the compile-time argument types. `PrintStream` has several `println` methods, so `println(42)` selects an integer overload while `println("42")` selects a string overload. Both display similar characters, but the calls reached different method signatures.

The `+` operator in the example also changes role. `i + 1` is integer addition. Once a string operand participates, later additions on that left-associated expression become string concatenation. Parentheses around `(i + 1)` ensure the number is computed before it is appended; without them, `" #" + i + 1` appends the two digits separately. At `i == 0`, the parenthesized form ends in `1`, while the unparenthesized form ends in `01`.

## From `Welcome.java` to a running method

Suppose `Welcome.java` declares class `Welcome` with a `main` method.

1. `javac` parses and type-checks the source, then writes bytecode and metadata to `Welcome.class`.
2. The virtual machine locates the class through a class loader.
3. Linking includes verification that the class file is structurally valid and that its bytecode obeys JVM type-safety rules.
4. The VM initializes the class when required, locates the entry method, and invokes it.
5. Execution may create objects, call library methods, load more classes, throw exceptions, and eventually terminate.

**Bytecode** is the instruction representation stored in class files. The **Java virtual machine** supplies its execution environment: class loading, linking, initialization, runtime data areas, thread coordination, interpretation or compilation, and garbage collection.

A class file stores more than a stream of opcodes. Its constant pool contains symbolic references, literals, and names; method entries contain descriptors, bytecode, exception tables, and optional debugging attributes. References to other classes and methods can remain symbolic until linking resolves them. The format gives different JVM implementations a shared input contract.

Loading, linking, and initialization are distinct. Loading creates the VM's representation of a class from its binary form. Linking verifies it, prepares static storage, and may resolve symbolic references. Initialization executes static field initializers and static blocks in textual order when the class is first actively used. Merely having a class file on the class path does not mean its initialization code has run.

```mermaid
flowchart TD
  Source["Java source file: .java"] --> Javac["javac compiler: parse, type-check, generate bytecode"]
  Javac --> ClassFile[".class file: constant pool, fields, methods, bytecode, attributes"]
  ClassFile --> Loader["Class loader: locate, load, link, initialize classes"]
  Loader --> Verify["Bytecode verifier: stack maps, type safety, access rules"]
  Verify --> Runtime[JVM runtime data areas]

  subgraph Areas[Runtime data areas]
    direction TB
    Heap[Heap objects and arrays]
    Stacks["Per-thread Java stacks: frames, locals, operand stacks"]
    Meta[Class metadata and runtime constant pools]
    Native[Native method interface and stacks]
  end

  Runtime --> Areas
  Areas --> Main["Invoke public static void main(String#lsqb;"] args)"]
  Main --> Interpreter[Interpreter executes bytecode]
  Interpreter --> Hot{"Hot method or loop?"}
  Hot -- yes --> JIT[JIT compiler emits optimized native code]
  Hot -- no --> Interpreter
  JIT --> NativeCode[Native code runs under JVM control]
  NativeCode --> GC[Garbage collector traces reachable objects]
  Interpreter --> GC
  GC --> Heap
  Main --> Stdlib["Standard library objects: System.out, collections, I/O"]
```

The diagram separates responsibilities that otherwise blur together. A syntax or type error belongs to compilation; a malformed class-file error belongs to loading or verification; and a thrown exception belongs to execution. Reading an error by its stage narrows the search immediately.

### Following one invocation frame

When the VM invokes `main`, the main thread receives a stack frame. That frame holds local slots for `args`, `target`, and the loop index, plus an operand stack used by bytecode instructions. The literal `"Java"` and the argument strings refer to objects; the references occupy local slots while the objects live in heap-managed storage.

For the first loop iteration with no arguments, the execution can be traced as follows:

1. `args.length` evaluates to $0$, so the conditional expression selects `"Java"`.
2. `i` is initialized to $0$ and the test `i < 3` succeeds.
3. `(i + 1)` evaluates to integer $1$.
4. Concatenation constructs the displayed text `Hello, Java #1` through compiler-selected string-building operations.
5. `println` writes the text and a line separator through the current `System.out` object.
6. `i++` changes `i` to $1$, and the loop test repeats.

After three iterations, the test fails at `i == 3`; `main` returns and its frame is removed. Objects created during concatenation become eligible for collection once no reachable references remain. Eligibility does not promise immediate reclamation.

The bytecode interpreter may begin by dispatching one instruction at a time. A just-in-time compiler can later translate frequently executed methods or loops to native machine code using observed run-time information. Both routes must preserve Java's specified behavior. Optimization changes how execution is implemented, not the source-level result.

## Compile, launch, and pass arguments

Assume the source file is stored as `QuickTourDemo.java` in the current directory with no package declaration. The basic commands are:

```text
javac QuickTourDemo.java
java QuickTourDemo Ada
```

The compiler produces `QuickTourDemo.class`. The launcher argument is a binary class name, not a filename: use `QuickTourDemo`, not `QuickTourDemo.class`. The remaining token `Ada` becomes `args[0]`, so `target` is `"Ada"` and the program prints three numbered greetings.

With a declaration such as `package notes.tour;`, the class's binary name becomes `notes.tour.QuickTourDemo`. The class file normally sits below a class-path root at `notes/tour/QuickTourDemo.class`, and the launcher receives the fully qualified name:

```text
java -cp <class-path-root> notes.tour.QuickTourDemo Ada
```

Running from inside the package directory with only the simple name fails because the class loader starts from class-path roots and maps the binary name to its package path. Package name, directory layout, and class path must describe the same location.

### A failure at each stage

Consider three different messages:

- A missing semicolon is rejected by `javac`; no new valid class file is produced for that source.
- `ClassNotFoundException` or a launcher message about not finding the main class means class lookup failed before `main` began. Check the binary name and class path.
- `ArrayIndexOutOfBoundsException` from `args[0]` means the program launched and then indexed an empty array. The fix is an input check such as the conditional expression in the example.

These failures can look equally final at a terminal, but they occurred in separate systems. Changing source punctuation cannot fix a class path, and changing a class path cannot make an unsafe array access valid.

## Three layers to inspect on each line

Early examples become clearer when read at three levels:

- **Syntax:** Do the tokens form a legal declaration, statement, or expression?
- **Types:** What does each name denote, and which operations does its type permit?
- **Runtime:** Which classes load, which objects are created, which methods run, and where can an exception propagate?

Names and comments support the same reading process. A named constant records the role of a value; a useful comment explains a constraint or decision that the code cannot state directly.

One line can cross all three levels. In `String target = args.length == 0 ? "Java" : args[0];`, syntax groups a conditional expression, typing requires both alternatives to be compatible with `String`, and run time evaluates only the selected alternative. Because `args[0]` is skipped when the array is empty, the expression is safe. Replacing `?:` with a non-short-circuiting helper that evaluates both candidates could lose that property.

## What portability does and does not promise

Class files and standard APIs shield application code from many processor and operating-system differences. Primitive widths, array behavior, exception rules, and bytecode semantics do not change merely because the host CPU does. A conforming implementation can interpret or compile the same program differently while preserving those rules.

Programs still meet their host through file paths, default character encodings, locales, time zones, network configuration, native libraries, process permissions, and available memory. A program that assumes a Unix path separator or a particular default locale is using a platform detail even though its source compiles everywhere.

Native methods and the Java Native Interface deliberately cross the managed boundary. They can access operating-system facilities absent from the standard library, but they bring platform-specific binaries, manual resource ownership, and memory-safety risks. Portability is a property of the entire dependency set, not a reward granted by the `.java` extension.

Garbage collection also has a limited promise: unreachable managed objects may have storage reclaimed. It does not close files at a deterministic line, release a lock that code forgot to unlock, or guarantee a finalizer runs before process exit. External resources need explicit lifetime management.

## Where the tour continues

| Quick-tour feature | Later detailed note |
|---|---|
| Variables, primitive values, operators | [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables), [Primitives, Operators, and Conversions](/cs/programming/java/primitives-operators-conversions) |
| `if`, loops, arrays, strings | [Control Flow, Arrays, and Strings](/cs/programming/java/control-flow-arrays-strings) |
| Classes, methods, constructors | [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation), [Constructors, Methods, and Overloading](/cs/programming/java/constructors-methods-overloading) |
| Inheritance and interfaces | [Inheritance, Polymorphism, and Object](/cs/programming/java/inheritance-polymorphism-object), [Interfaces, Nested Classes, and Enums](/cs/programming/java/interfaces-nested-classes-enums) |

## Stage errors and early misconceptions

- `System.out.println` is a library method call, not Java syntax for printing.
- A source-file name, a class name, and an entry method have related but different rules. A public top-level class constrains the file name; the VM starts from the requested class's entry point.
- Compile-time type errors and runtime exceptions occur at different stages and call for different fixes.
- Even the first example depends on a package: `System` and `String` come from `java.lang`.
- Quick-tour code favors breadth and compactness. It previews features rather than defining complete style guidance.
- The `java` launcher takes a class name; handing it a `.class` path confuses the lookup model.
- JIT compilation does not create a second set of Java semantics. It optimizes under the same observable rules.
- “Runs on a JVM” does not standardize host files, locale defaults, permissions, or native dependencies.

## Next notes after the tour

- [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables): explains the names and values used in first programs.
- [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation): develops the class model behind Java source files.
- [Exceptions and Assertions](/cs/programming/java/exceptions-assertions): separates runtime failures from compile-time rejection.
- [Packages, Documentation, System, and Internationalization](/cs/programming/java/packages-documentation-system-i18n): returns to packages and system services.
