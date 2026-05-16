You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/C Programming Language - 2nd Edition (OCR).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming/c/`
- **SUBJECT**: C Programming (Kernighan & Ritchie — *The C Programming Language*, 2nd ed)

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview + numbered list of all pages you create.

2. **12-18 detail pages** covering K&R's full scope:
   - A tutorial introduction (hello world, variables, expressions, control, functions, arrays, character I/O)
   - Types, operators, expressions (type conversion, bitwise, precedence, increment)
   - Control flow (if/else, switch, loops, break/continue, goto)
   - Functions and program structure (external variables, scope, header files, recursion, the preprocessor)
   - Pointers and arrays (pointers and addresses, function arguments, array of strings, pointer arithmetic, function pointers, multidimensional)
   - Structures (basic structs, structures and functions, arrays of structs, pointers to structs, self-referential structures, typedef, unions, bit-fields)
   - Input and output (standard I/O, formatted I/O, file access, error handling, line input)
   - The UNIX system interface (system calls, read/write, open/close, lseek, malloc/free, listing directories)
   - The C standard library reference (selected useful entries)
   - Modern C considerations vs K&R style (brief)

3. Per-page format: motivation → semantics → idiomatic example (in `c` code blocks) → common pitfalls.

4. Emphasize the **K&R idioms** — pointer-based array traversal, terse style, careful undefined-behavior notes.

## Workflow

1. `pdfinfo` for page count. 2. `pdftotext -l 30` for cover/TOC. 3. Iterate chapters; 1-3 wiki pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. Don't modify `_category_.json`, config files, `sidebars.ts`, `package.json`. No `npm`. English. Don't fabricate.

Begin now.
