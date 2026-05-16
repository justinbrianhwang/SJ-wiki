You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Python Programming.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/programming/python/`
- **SUBJECT**: Python (identify exact textbook from cover/TOC)

## Produce

1. **`intro.md`** — replace any stub. Name the source book. Overview + chapter list.

2. **15-22 detail pages** covering Python scope:
   - Setup, REPL, syntax basics, types, operators
   - Control flow (if, for, while, comprehensions)
   - Strings & text processing
   - Lists, tuples, sets, dicts (built-in containers + idioms)
   - Functions (args/kwargs, defaults, closures, decorators, lambdas)
   - Modules and packages
   - File I/O and context managers
   - Errors and exceptions
   - Classes & OOP (dunders, properties, inheritance, mixins, dataclasses)
   - Iterators, generators, `yield`
   - Functional tools (`map`, `filter`, `functools`, `itertools`)
   - Concurrency (threading, multiprocessing, asyncio overview)
   - Standard library highlights (`pathlib`, `collections`, `datetime`, `json`, `re`)
   - Testing (`unittest`, `pytest` basics)
   - Numeric / scientific stack overview (NumPy, pandas, matplotlib) — brief

3. Per-page format: motivation → idiom → `python` snippet → pitfalls → cross-links.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` to identify book + TOC. 3. Iterate chapters. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Don't fabricate.

Begin now.
