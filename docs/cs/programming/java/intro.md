---
title: Java
sidebar_position: 1
---

# Java

These notes follow *The Java Programming Language, Fourth Edition* by Ken Arnold, James Gosling, and David Holmes. The 2005 book is a Java 5 source: it covers the core language, virtual-machine model, object orientation, interfaces, nested classes, enums, generics, exceptions, assertions, strings, threads, annotations, reflection, garbage collection, packages, documentation comments, I/O, collections, utility classes, system programming, internationalization, and a survey of standard packages.

The language designers write in terms of contracts among source code, compiler, virtual machine, standard library, and programmer. That point of view is still useful, but the historical boundary matters. Lambda expressions, the `java.util.stream` Stream API, `CompletableFuture`, the Java Platform Module System, Maven, and Gradle arrived later or belong to the wider ecosystem. Nearby pages mark those boundaries without attributing later material to the book.

## Reading Java as a set of contracts

A **Java program** consists of source files containing classes, interfaces, enums, annotation types, packages, imports, fields, methods, constructors, statements, and expressions. Compilation produces class files containing bytecode, which a Java virtual machine executes. Portability rests on the virtual-machine and library specifications, not on a particular processor.

The **Java platform** includes the language, class libraries, virtual machine, verifier, runtime system, and standard packages. The book repeatedly separates language syntax from library and VM behavior. A declaration may promise a type, visibility boundary, exception contract, or annotation; dynamic dispatch, class loading, verification, synchronization, and garbage collection then enforce or use those promises.

Object-oriented structure supplies another set of contracts. Classes define state and behavior, constructors establish initial state, interfaces state capabilities, inheritance relates implementations, and dynamic method selection chooses behavior from the runtime object. Visibility and overriding rules determine what callers may rely on.

The standard library is part of ordinary Java literacy. Syntax alone is not enough to read programs built around `List`, `Map`, `Iterator`, `InputStream`, `StringBuilder`, `Thread`, or `Class`. The aim is not to memorize every library type, but to recognize families of abstractions and the promises they make.

Java 5 changed common idioms through generics, enums, annotations, autoboxing, varargs, enhanced `for`, `Formatter`, `Scanner`, and parts of `java.util.concurrent`. Compatibility mechanisms such as erasure and bridge methods let the newer type system coexist with older bytecode and source conventions.

When a rule feels vague, restate it as something the compiler, runtime, library, or maintainer could enforce. That usually identifies whether a bug lies in the type contract, object lifecycle, visibility boundary, exception path, or runtime mechanism.

## Mapping the source chapters to the notes

The quick tour supplies the platform model, the middle chapters build the object and type systems, and the later chapters apply those rules across the standard library.

| Source chapter area | Notes page |
|---|---|
| Chapter 1: quick tour, platform, packages | [Quick Tour, Platform, and First Programs](/cs/programming/java/quick-tour-platform) |
| Chapters 7-10: lexical elements, variables, primitives, operators, control flow | [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables), [Primitives, Operators, and Conversions](/cs/programming/java/primitives-operators-conversions), [Control Flow, Arrays, and Strings](/cs/programming/java/control-flow-arrays-strings) |
| Chapters 2-6: classes, extension, interfaces, nested types, enums | [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation), [Constructors, Methods, and Overloading](/cs/programming/java/constructors-methods-overloading), [Inheritance, Polymorphism, and Object](/cs/programming/java/inheritance-polymorphism-object), [Interfaces, Nested Classes, and Enums](/cs/programming/java/interfaces-nested-classes-enums) |
| Chapters 11-17: generics, exceptions, strings, threads, annotations, reflection, memory | [Generics, Wildcards, and Erasure](/cs/programming/java/generics-wildcards-erasure), [Exceptions and Assertions](/cs/programming/java/exceptions-assertions), [Strings, Regular Expressions, Formatter, and Scanner](/cs/programming/java/strings-regex-formatter-scanner), [Threads, Synchronization, and the Memory Model](/cs/programming/java/threads-synchronization-memory-model), [Annotations and Reflection](/cs/programming/java/annotations-reflection), [Garbage Collection, References, and Memory](/cs/programming/java/garbage-collection-references-memory) |
| Chapters 18-24 plus standard package survey | [I/O Streams, Files, Serialization, and NIO](/cs/programming/java/io-streams-files-serialization-nio), [Collections, Iteration, and Maps](/cs/programming/java/collections-iteration-maps), [Concurrent Utilities and Executors](/cs/programming/java/concurrent-utilities-executors), [Packages, Documentation, System, and Internationalization](/cs/programming/java/packages-documentation-system-i18n) |

The order reflects real dependencies. Classes and objects precede inheritance and interfaces because the type system assumes object identity, fields, methods, constructors, and access control. Generics become clearer after class extension, interfaces, arrays, primitives, and method selection. Library chapters in turn assume references, static members, overloading, overriding, checked exceptions, and generic type arguments.

## A source-faithful route through Java

For a reader who already knows another language, the shortest path that preserves those dependencies is:

1. Start with the quick tour and its platform model: source file, class file, bytecode, virtual machine, runtime system, verifier, and standard output.
2. Read variables, primitives, operators, control flow, arrays, and strings. Later examples assume assignments and conversions can be traced without interruption.
3. Move to classes, constructors, methods, access control, and overloading. Library types are classes, so object construction and method invocation must come before collections or I/O.
4. Continue through inheritance, interfaces, nested types, enums, and generics. These topics explain polymorphic APIs such as `List<E>`, `Iterator<E>`, `Comparable<T>`, and `Runnable`.
5. Finish with exceptions, strings, threads, annotations, reflection, garbage collection, I/O, collections, concurrent utilities, packages, and system topics.

The compressed order is platform → syntax → classes → type relationships → generic libraries → runtime and standard packages. Collections become easier when tied back to generics and iterators; I/O depends on exceptions and cleanup; threads depend on object locks, `volatile`, and the memory model.

## Where the 2005 source stops

The publication date and table of contents provide a clean test for borderline material:

| Feature | Treatment here | Reason |
|---|---|---|
| Generics, annotations, enums, enhanced `for`, autoboxing, varargs | Covered | Java 5 language features developed in the source |
| `Formatter`, `Scanner`, executors, `Callable`, `Future`, locks, concurrent collections | Covered or surveyed | Present in the source-era library scope |
| Lambda expressions and `java.util.stream.Stream` | Later boundary | Java 8 features |
| Java Platform Module System | Later boundary | Java 9 feature |
| Maven and Gradle | Ecosystem boundary | Build tools rather than subjects developed by the book |
| `CompletableFuture` | Later boundary | Added after the source era |

The closest relevant chapter may point forward without pretending the source covered the feature. The interfaces material can mention lambdas; I/O can distinguish byte and character streams from the later Stream API; packages can identify modules and build tools as later concerns.

## Reading errors to avoid

- Do not use the source as a Java 21 manual. Its account of core language and Java 5 library contracts remains valuable, but later features require later documentation.
- I/O streams and `java.util.stream` share a word, not a purpose. The former move bytes or characters; the latter process element pipelines.
- The early class examples look small, yet access control, construction, `this`, static members, and overloading recur throughout the library chapters.
- The standard-library survey belongs to language learning because idiomatic Java is library-heavy.
- Source-era concurrency is broader than `Thread`: executors, `Callable`, `Future`, locks, and concurrent collections are already represented.

<div className="see-also">

See also: [Quick Tour, Platform, and First Programs](/cs/programming/java/quick-tour-platform) · [Generics, Wildcards, and Erasure](/cs/programming/java/generics-wildcards-erasure) · [Collections, Iteration, and Maps](/cs/programming/java/collections-iteration-maps) · [Threads, Synchronization, and the Memory Model](/cs/programming/java/threads-synchronization-memory-model) · [Packages, Documentation, System, and Internationalization](/cs/programming/java/packages-documentation-system-i18n)

</div>
