---
title: Java
sidebar_position: 1
---

# Java

These notes are based on *The Java Programming Language, Fourth Edition* by Ken Arnold, James Gosling, and David Holmes. The book is a Java 5 era source: it explains the core language, the virtual machine model, object orientation, interfaces, nested classes, enums, generics, exceptions, assertions, strings, threads, annotations, reflection, garbage collection, packages, documentation comments, I/O, collections, utility classes, system programming, internationalization, and a survey of standard packages.

The source is historically important because it teaches Java from the language designers' point of view. It treats Java features as contracts between source code, compiler, virtual machine, standard library, and programmer. Later Java features such as lambda expressions, the `java.util.stream` Stream API, `CompletableFuture`, Java Platform Module System modules, Maven, and Gradle are outside this source. Where those topics are natural neighbors, the pages mark them as later boundaries rather than inventing coverage not present in the book.

## Definitions

The source basis for this page is the cover, table of contents, preface, and chapter map of *The Java Programming Language, Fourth Edition* by Ken Arnold, James Gosling, and David Holmes, published by Addison Wesley Professional in 2005. The terms below are written as contracts: each one tells you what the compiler can check, what the runtime must preserve, and what a reader of the program may rely on.

**Source book.** *The Java Programming Language, Fourth Edition* is the controlling source for this section of SJ Wiki. It reflects Java 5, including generics, enums, annotations, enhanced `for`, autoboxing, varargs, formatted output, scanning, and parts of `java.util.concurrent`. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Java program.** A Java program is written as source files containing classes, interfaces, enums, annotation types, packages, imports, fields, methods, constructors, statements, and expressions. The book introduces these pieces gradually, then returns to many of them in reference-style chapters. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Java platform.** The platform includes the language, the class libraries, the virtual machine, the verifier, the runtime system, and standard packages. The book repeatedly distinguishes what the language syntax says from what the library or virtual machine provides. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Compilation and execution.** A source file is compiled to class files containing bytecode, and bytecode is executed by a Java virtual machine implementation. Portability depends on the virtual machine contract and library specifications, not on assuming a particular processor. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Object orientation.** Java programs organize behavior around objects, classes, inheritance, interfaces, and dynamic method selection. The book uses object-oriented examples to show why visibility, construction, overriding, and contracts matter. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Library-centered learning.** Large parts of the book teach `java.lang`, `java.util`, `java.io`, and selected standard packages. The goal is not to memorize every class, but to recognize families of abstractions and their design contracts. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

**Historical boundary.** The source predates several now-common Java features. The notes therefore explain source-era mechanisms such as anonymous classes, `Runnable`, `Future`, and I/O streams without presenting later language features as if the book covered them. In Java, this is rarely just vocabulary. It controls which operations are legal, when a value exists, what names are visible, or which object receives a message. When reading code, ask what the term promises before asking how the implementation happens to work.

## Key results

**The book's order is intentional.** The first chapter gives a quick tour, but the later chapters revisit each idea with precise rules. Classes and objects come before inheritance and interfaces because Java's type system depends on understanding object identity, fields, methods, constructors, and access control. Generics appear only after the reader has seen class extension, interfaces, arrays, primitives, and method selection. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**Java separates source-level promises from runtime mechanisms.** A declaration may promise a type, a visibility boundary, an exception contract, or an annotation. Runtime mechanisms such as dynamic dispatch, class loading, verification, synchronization, and garbage collection then enforce or make use of those promises. This separation is why many Java bugs are best debugged by asking which contract was violated. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**The standard library is part of the language experience.** The book does not treat collections, I/O, strings, utilities, reflection, and threading as optional trivia. They are the common vocabulary of Java programs. A programmer who knows syntax but not `List`, `Map`, `Iterator`, `InputStream`, `StringBuilder`, `Thread`, or `Class` cannot read ordinary Java source effectively. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**Java 5 changed the shape of idiomatic Java.** Generics, enums, annotations, autoboxing, varargs, enhanced `for`, `Formatter`, and `Scanner` changed the way code was written. The fourth edition explicitly updates earlier Java idioms to account for those features while preserving compatibility with older code through mechanisms such as erasure and bridge methods. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

**The notes keep modern boundaries visible.** The requested syllabus includes modern areas such as lambdas, streams, modules, Maven, Gradle, and `CompletableFuture`. Because the source predates them, these notes identify them as outside the source. That is not a gap in Java itself; it is a boundary of this textbook-derived section. A good check is to rewrite the idea as a rule a compiler, library, or maintainer can enforce. If the rule cannot be stated clearly, the design is probably relying on habit instead of a contract.

A reliable way to use this section is to read from the platform and syntax pages into classes, inheritance, interfaces, and generics before jumping to libraries. The library pages assume that you already understand object references, static members, method overloading, overriding, checked exceptions, and generic type arguments. The source also rewards comparison: when you read collections, connect them to generics and iterators; when you read I/O, connect it to exceptions and final cleanup; when you read threads, connect it to object locks, `volatile`, and the memory model. That cross-linking is the main reason this wiki is organized as a network rather than as a flat list of isolated definitions.

## Visual

| Source chapter area | Wiki page |
|---|---|
| Chapter 1: quick tour, platform, packages | [Quick Tour, Platform, and First Programs](/cs/programming/java/quick-tour-platform) |
| Chapters 7-10: lexical elements, variables, primitives, operators, control flow | [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables), [Primitives, Operators, and Conversions](/cs/programming/java/primitives-operators-conversions), [Control Flow, Arrays, and Strings](/cs/programming/java/control-flow-arrays-strings) |
| Chapters 2-6: classes, extension, interfaces, nested types, enums | [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation), [Constructors, Methods, and Overloading](/cs/programming/java/constructors-methods-overloading), [Inheritance, Polymorphism, and Object](/cs/programming/java/inheritance-polymorphism-object), [Interfaces, Nested Classes, and Enums](/cs/programming/java/interfaces-nested-classes-enums) |
| Chapters 11-17: generics, exceptions, strings, threads, annotations, reflection, memory | [Generics, Wildcards, and Erasure](/cs/programming/java/generics-wildcards-erasure), [Exceptions and Assertions](/cs/programming/java/exceptions-assertions), [Strings, Regular Expressions, Formatter, and Scanner](/cs/programming/java/strings-regex-formatter-scanner), [Threads, Synchronization, and the Memory Model](/cs/programming/java/threads-synchronization-memory-model), [Annotations and Reflection](/cs/programming/java/annotations-reflection), [Garbage Collection, References, and Memory](/cs/programming/java/garbage-collection-references-memory) |
| Chapters 18-24 plus standard package survey | [I/O Streams, Files, Serialization, and NIO](/cs/programming/java/io-streams-files-serialization-nio), [Collections, Iteration, and Maps](/cs/programming/java/collections-iteration-maps), [Concurrent Utilities and Executors](/cs/programming/java/concurrent-utilities-executors), [Packages, Documentation, System, and Internationalization](/cs/programming/java/packages-documentation-system-i18n) |

## Worked example 1: choosing a source-faithful reading path

Problem: A reader knows another programming language and wants the fastest path through these Java notes without skipping concepts that later pages depend on.

Method:

1. Start with the quick tour page to learn the platform model: source file, class file, bytecode, virtual machine, runtime system, verifier, and standard output.
2. Read variables, primitives, operators, control flow, arrays, and strings next. These are the building blocks inside every method body, and later examples assume the reader can trace assignments and conversions.
3. Move to classes, constructors, methods, access control, and overloading. Java library types are classes, so understanding object construction and method invocation is required before reading collections or I/O.
4. Read inheritance, interfaces, nested types, enums, and generics. These chapters explain the type relationships behind polymorphic library APIs such as `List<E>`, `Iterator<E>`, `Comparable<T>`, and `Runnable`.
5. Finish with exceptions, strings, threads, annotations, reflection, garbage collection, I/O, collections, concurrent utilities, packages, and system topics.

Checked answer: The checked path is platform -> syntax -> classes -> type relationships -> generic libraries -> runtime and standard packages. Skipping classes before collections or exceptions before I/O leaves too many later contracts unexplained.

## Worked example 2: identifying out-of-source modern features

Problem: Decide whether a page should teach lambdas, `java.util.stream.Stream`, modules, or Maven/Gradle as if they were covered by the source.

Method:

1. Check the source date and table of contents. The book is from 2005 and centers on Java 5.
2. Compare the requested feature to the source chapters. Generics, annotations, enums, `Formatter`, `Scanner`, concurrent collections, executors, and `Future` are present in the source-era scope.
3. Classify lambda expressions and the Stream API as later Java 8 features. Classify JPMS modules as later Java 9. Classify Maven and Gradle as ecosystem tools rather than topics developed by the book.
4. Record the boundary in the nearest relevant page instead of silently adding outside material. Interfaces can mention that lambdas come later; I/O can warn that source-era streams are byte and character streams; packages can mention that modules and build tools are out of scope.

Checked answer: The checked answer is to teach only the source-supported material in detail and mark later features as boundaries. That preserves the user's request not to fabricate beyond the textbook while still showing where modern Java readers may notice missing topics.

## Code

```java
public class HelloSourceBook {
    public static void main(String[] args) {
        String book = "The Java Programming Language, Fourth Edition";
        String authors = "Ken Arnold, James Gosling, David Holmes";
        int sourceYear = 2005;

        System.out.println(book);
        System.out.println(authors);
        System.out.println("Source-era Java: " + sourceYear);
    }
}
```

## Common pitfalls

- Do not read the source as a Java 21 manual. It is excellent for core language and Java 5 library contracts, but later features need other sources.
- Do not confuse I/O streams from Chapter 20 with the later `java.util.stream` API. They share a word but solve different problems.
- Do not skip the early class chapters because the examples look simple. Access control, construction, `this`, static members, and overloading are used everywhere later.
- Do not treat the standard library survey as unrelated to language learning. Java idiom is library-heavy.
- Do not assume every requested modern topic is absent from the source. `Executor`, `Callable`, `Future`, locks, and concurrent collections are at least surveyed through the standard package coverage.

## Connections

- [Quick Tour, Platform, and First Programs](/cs/programming/java/quick-tour-platform): starts the source reading path.
- [Generics, Wildcards, and Erasure](/cs/programming/java/generics-wildcards-erasure): explains the largest Java 5 type-system addition.
- [Collections, Iteration, and Maps](/cs/programming/java/collections-iteration-maps): shows how generics shape everyday library use.
- [Threads, Synchronization, and the Memory Model](/cs/programming/java/threads-synchronization-memory-model): covers the runtime behavior that most directly affects correctness.
- [Packages, Documentation, System, and Internationalization](/cs/programming/java/packages-documentation-system-i18n): records package, documentation, and ecosystem boundaries.
