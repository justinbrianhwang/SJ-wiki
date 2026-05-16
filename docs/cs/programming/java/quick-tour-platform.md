---
title: Quick Tour, Platform, and First Programs
sidebar_position: 2
---

# Quick Tour, Platform, and First Programs

A first Java program is small, but it already shows the major design of the language. A class contains a `main` method, the method executes statements, objects receive method invocations, and the standard library provides objects such as `System.out`. The quick tour in the source book deliberately moves fast because it wants the reader to see the whole shape before studying each rule.

The platform matters as much as the syntax. Java source is compiled to bytecode, bytecode is loaded and verified by a virtual machine, and the runtime system connects the running program to services such as standard streams, security checks, class loading, and garbage collection. That architecture is why Java can talk about portability, safety checks, and a large standard API as one platform rather than as a thin language over an operating system.

## Definitions

The source basis for this page is Chapter 1, especially the quick tour sections on getting started, variables, comments, constants, flow of control, classes, arrays, strings, exceptions, annotations, packages, and the Java platform. The terms below are written as contracts: each one tells you what the compiler can check, what the runtime must preserve, and what a reader of the program may rely on.

**Class.** A class is the basic unit that declares fields, methods, constructors, nested types, and initialization behavior. Even a minimal first program is placed inside a class declaration because Java does not have free-standing functions. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**`main` method.** The conventional application entry point is a public static method named `main` that receives a `String[]` argument. It belongs to a class, and the virtual machine invokes it to start the program. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Object reference.** A reference is a value that lets a program interact with an object. Variables of class, interface, array, enum, and annotation-related types hold references rather than containing the full object inline. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Bytecode.** Bytecode is the instruction form stored in class files after compilation. The virtual machine interprets or compiles it while enforcing class file and runtime rules. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Virtual machine.** The Java virtual machine provides the execution environment for bytecode. It loads classes, checks bytecode validity, manages memory, coordinates threads, and exposes runtime services. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Package.** A package groups related types under a name and creates a namespace. Chapter 1 introduces packages briefly, and later chapters return to naming, importing, access, and package documentation. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Standard output stream.** `System.out` is a library-provided object used by early examples to print text. It is not special syntax; it is a static field whose object has methods such as `print` and `println`. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

## Key results

**A Java program starts as a class, not as a loose script.** The first source file normally declares a class and a `main` method. That design choice reinforces the rest of Java: behavior is named through methods, methods are members of types, and type names participate in packages. Even when a program feels procedural, it is still running through class and method declarations. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**The dot operator expresses selection.** Code such as `System.out.println("Hello")` has two selections. `System.out` selects a static field from `System`, then `.println` selects a method from the object referenced by `out`. Tracing dots is one of the fastest ways to understand Java examples because it reveals which type or object supplies each operation. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**The platform enforces more than syntax.** A source program may compile, but the runtime still loads classes, verifies bytecode, initializes classes, checks access in reflective or security-sensitive operations, and manages object storage. The book stresses this platform view so that portability and safety are not treated as magical properties of source text. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**Early examples preview later chapters.** The quick tour mentions variables, constants, Unicode, control flow, classes, methods, arrays, strings, inheritance, interfaces, generics, exceptions, annotations, and packages. Each preview is shallow by design. The correct reading strategy is to notice the feature, run the example, and expect precise rules later. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**Comments and names are part of communication.** The quick tour includes comments and named constants because Java programs are read by people as well as compilers. Good names and useful comments reduce the distance between source code and the contract it is meant to express. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

When studying the quick tour, separate three layers on every line. The syntax layer asks whether the tokens form a legal declaration, statement, or expression. The type layer asks what each name denotes and what operations are permitted on that type. The platform layer asks what happens at runtime: loading, initialization, object creation, method invocation, exception propagation, output, and program termination. This three-layer habit prevents a common beginner mistake: assuming that a printed line is special because it appears in every first example. It is ordinary Java object interaction, and that ordinariness is the point.

## Visual

```mermaid
flowchart TD
  Source["Java source file: .java"] --> Javac["javac compiler: parse, type-check, generate bytecode"]
  Javac --> ClassFile[".class file: constant pool, fields, methods, bytecode, attributes"]
  ClassFile --> Loader["Class loader: locate, load, link, initialize classes"]
  Loader --> Verify["Bytecode verifier: stack maps, type safety, access rules"]
  Verify --> Runtime["JVM runtime data areas"]

  subgraph Areas["Runtime data areas"]
    direction TB
    Heap["Heap: objects and arrays"]
    Stacks["Per-thread Java stacks: frames, locals, operand stacks"]
    Meta["Class metadata and constant pools"]
    Native["Native method interface and stacks"]
  end

  Runtime --> Areas
  Areas --> Main["Invoke public static void main(String#lsqb;"] args)"]
  Main --> Interpreter["Interpreter executes bytecode initially"]
  Interpreter --> Hot{"Hot method or loop?"}
  Hot -- "yes" --> JIT["JIT compiler emits optimized native code"]
  Hot -- "no" --> Interpreter
  JIT --> NativeCode["Native machine code runs under JVM safepoints"]
  NativeCode --> GC["Garbage collector traces reachable heap objects"]
  Interpreter --> GC
  GC --> Heap
  Main --> Stdlib["Standard library objects: System.out, collections, I/O"]
```

This Java platform diagram shows the complete path from source to execution. `javac` emits class-file bytecode, the class loader and verifier prepare it, the JVM stores class metadata, stacks, and heap objects, then interpretation and JIT compilation execute the program. The GC and standard-library edges show that memory management and library services are runtime architecture, not syntax-level conveniences.

| Quick tour feature | Later detailed page |
|---|---|
| Variables, primitive values, operators | [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables), [Primitives, Operators, and Conversions](/cs/programming/java/primitives-operators-conversions) |
| `if`, loops, arrays, strings | [Control Flow, Arrays, and Strings](/cs/programming/java/control-flow-arrays-strings) |
| Classes, methods, constructors | [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation), [Constructors, Methods, and Overloading](/cs/programming/java/constructors-methods-overloading) |
| Inheritance and interfaces | [Inheritance, Polymorphism, and Object](/cs/programming/java/inheritance-polymorphism-object), [Interfaces, Nested Classes, and Enums](/cs/programming/java/interfaces-nested-classes-enums) |

## Worked example 1: tracing a first program

Problem: Explain exactly what happens in `System.out.println("Hello")` inside a `main` method.

Method:

1. Identify `System` as a class from `java.lang`, which is automatically available without an explicit import.
2. Read `out` as a static field selected from `System`. The field value is a reference to a `PrintStream` object connected to standard output.
3. Read `println` as a method selected from that `PrintStream` object. The string literal is passed as an argument.
4. The method writes the characters and a line separator to the output destination. The call then returns to the next statement in `main`.
5. No new language rule was needed for printing. The example uses ordinary field selection, method invocation, object references, and a library class.

Checked answer: The checked answer is: class field selection produces `System.out`, object method selection invokes `println`, and the library object performs output. Printing is library behavior reached through normal Java syntax.

## Worked example 2: mapping source, bytecode, and runtime

Problem: A file `Welcome.java` contains class `Welcome` with a `main` method. Determine the path from source text to execution.

Method:

1. Compile `Welcome.java`. The compiler checks syntax and types and writes bytecode to `Welcome.class` if the source is valid.
2. Start the virtual machine with class name `Welcome`. The VM locates the class file through its class loading mechanism.
3. The bytecode verifier checks that the class file is well formed and respects safety rules, such as not treating an integer as an object reference.
4. The VM initializes the class as required, finds `public static void main(String[] args)`, and invokes it.
5. During execution, library calls may create objects, print text, throw exceptions, or load additional classes.

Checked answer: The checked path is source -> class file -> class loader -> verifier -> initialized class -> `main` invocation. Each stage has its own responsibility, so a failure message should be read in terms of the stage that produced it.

## Code

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

## Common pitfalls

- Do not treat `System.out.println` as syntax. It is a normal method call through a normal object reference stored in a static field.
- Do not assume the file name, class name, and entry point are interchangeable. A public top-level class has file-name rules, while the VM starts from a class containing an appropriate `main` method.
- Do not confuse compile-time type errors with runtime exceptions. They occur at different stages and require different fixes.
- Do not skip package thinking. Even early examples use `java.lang`, and larger programs depend on packages for naming and organization.
- Do not overread quick-tour code as complete style guidance. It is intentionally compact and is followed by precise chapters that refine the rules.

## Connections

- [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables): explains the names and values used in first programs.
- [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation): develops the class model behind every Java source file.
- [Exceptions and Assertions](/cs/programming/java/exceptions-assertions): explains runtime failures that can interrupt first programs.
- [Packages, Documentation, System, and Internationalization](/cs/programming/java/packages-documentation-system-i18n): returns to packages and system classes.
