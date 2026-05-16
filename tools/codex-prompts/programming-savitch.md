You are an autonomous content author for **SJ Wiki**. Generate **detailed**, well-structured Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Absolute C++ FIFTH EDITION Walter Savitch.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming/`
- **SUBJECT**: C++ programming (Savitch — *Absolute C++*, 5th ed)

## What to produce

1. **`intro.md`** — replace the stub. Overview of C++ language and the chapter list.

2. **One Markdown file per major topic.** Cover Savitch's full scope:
   - C++ basics (types, expressions, I/O, control flow)
   - Functions, scope, parameter passing (value, reference, const)
   - Arrays and strings (C-strings + `std::string`)
   - Pointers and dynamic memory
   - References & references vs pointers
   - Structures, classes, encapsulation
   - Constructors / destructors / copy semantics / move (if covered)
   - Operator overloading
   - Inheritance & polymorphism (virtual functions)
   - Templates (function + class)
   - STL containers (vector, list, map, set)
   - STL algorithms, iterators
   - Exception handling
   - File I/O
   - Recursion patterns

   Aim for **15-22 pages**, each 500-1500 words.

3. **Code-heavy**: each page should have multiple `cpp` code blocks with realistic, compilable snippets.

4. **Common pitfalls** section per page (e.g., "shallow copy in copy constructor").

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 25` → cover + TOC.
3. For each chapter, read its pages and write 1-3 wiki pages.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/programming/`. Don't touch other folders, `_category_.json`, config files.
- Don't run `npm`.
- English. Precise. Don't fabricate.

Begin now.
