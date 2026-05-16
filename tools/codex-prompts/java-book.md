You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Java.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming/java/`
- **SUBJECT**: Java (whatever textbook the PDF turns out to be — identify from cover/TOC)

## Produce

1. **`intro.md`** — replace the stub. Name the source book (after inspecting the PDF). Overview + chapter list.

2. **15-22 detail pages** covering typical Java scope:
   - Java basics (JVM, syntax, primitives, control flow, arrays)
   - Object-oriented design (classes, methods, encapsulation, this/super)
   - Inheritance, polymorphism, abstract classes
   - Interfaces and default methods
   - Generics (bounded types, wildcards, type erasure)
   - Collections framework (List, Set, Map, Queue, iterators)
   - Exception handling (checked vs unchecked, try-with-resources)
   - Functional interfaces and lambdas
   - Streams API
   - I/O (File, InputStream/OutputStream, Reader/Writer, NIO basics)
   - Concurrency (threads, Runnable, synchronized, locks, executors, Future, CompletableFuture)
   - JVM memory model and garbage collection
   - Reflection and annotations (brief)
   - Build tooling (Maven/Gradle, modules) — brief mention
   - Best practices (effective Java idioms if textbook covers them)

3. Per-page format: motivation → concept → realistic `java` example → common mistakes → cross-links.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` to find the book title + TOC. 3. Iterate chapters. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Don't fabricate beyond what's in the source.

Begin now.
