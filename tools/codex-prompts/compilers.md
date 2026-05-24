You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for a new **Compilers and Interpreters** subject under `docs/cs/compilers/`.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/compilers/`
- **SUPPLIED_TEXTBOOK**: `f:/coding/SJ Wiki/tmp/Complier/Crafting Interpreters - Robert Nystrom.pdf` (Nystrom, *Crafting Interpreters*)
- Cross-reference standard texts: Aho-Lam-Sethi-Ullman *Dragon Book* (Compilers: Principles, Techniques, and Tools), Appel *Modern Compiler Implementation*, Cooper-Torczon *Engineering a Compiler*, Muchnick *Advanced Compiler Design*
- **STYLE**: Topical chapter names. IEEE inline citations `[N]`.

## Workflow

1. `pdfinfo` + `pdftotext -l 30` on Crafting Interpreters for cover + TOC.
2. Iterate, write topical pages.
3. Replace `intro.md` last.
4. Print summary.

## Produce

### 1. Replace `intro.md` (sidebar_position 0)
250-400 word overview + numbered list of all pages.

### 2. Create exactly 7 detail pages

| sidebar_position | filename | title |
|---|---|---|
| 1 | `lexical-analysis-and-scanning.md` | Lexical Analysis and Scanning |
| 2 | `parsing-and-syntax-trees.md` | Parsing and Syntax Trees |
| 3 | `tree-walking-interpreters.md` | Tree-Walking Interpreters |
| 4 | `bytecode-compilation-and-virtual-machines.md` | Bytecode Compilation and Virtual Machines |
| 5 | `semantic-analysis-and-type-checking.md` | Semantic Analysis and Type Checking |
| 6 | `intermediate-representations-and-optimization.md` | Intermediate Representations and Optimization |
| 7 | `garbage-collection-and-runtime-systems.md` | Garbage Collection and Runtime Systems |

## Content scope

### 1 Lexical Analysis
- Lexemes, tokens, regular expressions, finite automata (NFA → DFA conversion, subset construction)
- Hand-written scanner vs generated (lex/flex)
- Lookahead, longest match rule
- Lexical error reporting; line tracking; UTF-8 handling

### 2 Parsing
- Context-free grammars, ambiguity, leftmost/rightmost derivations
- Top-down: recursive descent, predictive (LL(1)), Pratt parsing for operator precedence (Crafting Interpreters style)
- Bottom-up: LR(0), SLR(1), LALR(1), LR(1); shift-reduce, reduce-reduce conflicts
- Parser generators (yacc/bison, ANTLR)
- AST design vs parse tree; visitor pattern

### 3 Tree-Walking Interpreters
- AST evaluation, environments, scope chains
- First-class functions, closures, lexical scoping
- Statements vs expressions
- Resolving (variable binding pass)
- Native functions, host interop

### 4 Bytecode VMs
- Stack-based vs register-based VMs
- Bytecode design: opcodes, immediate operands, constant pool
- Compilation pass: AST → bytecode
- Dispatch loops (switch, computed goto, direct threading)
- Crafting Interpreters' clox VM as case study
- JIT compilation overview (template, tracing, method JIT)

### 5 Semantic Analysis and Types
- Symbol tables, scope resolution
- Type systems: static vs dynamic, strong vs weak, structural vs nominal
- Hindley-Milner type inference (mention)
- Subtyping, generics, parametric polymorphism (brief)
- Type checking pass; error reporting
- Definite assignment, ownership/borrow check briefly (Rust)

### 6 IR and Optimization
- Three-address code, SSA form
- LLVM IR overview
- Basic blocks, control-flow graph (CFG)
- Local optimizations: constant folding, common subexpression elimination, dead code elimination, strength reduction
- Loop optimizations: invariant code motion, unrolling, vectorization
- Global / dataflow: reaching definitions, liveness, available expressions
- Register allocation: graph coloring (Chaitin), linear scan
- Instruction scheduling

### 7 GC and Runtime
- Memory layout: stack, heap, text, data, BSS
- Reference counting (Python, Swift, ARC) vs tracing
- Tracing GC: mark-and-sweep, copying (Cheney), mark-compact
- Generational hypothesis; minor/major GC, nurseries
- Incremental and concurrent GC; tri-color invariant
- Read/write barriers; GC roots
- JVM HotSpot G1/ZGC, Go GC, Crafting Interpreters' simple GC

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter (`title:`, `sidebar_position:`)
2. `# Title` H1
3. 1-2 opening paragraphs
4. (Optional) 1-2 Wikimedia / book figures with attribution (verified only)
5. `## Definitions`
6. `## Key results` — algorithms/theorems
7. `## Visual` — **MANDATORY Mermaid** (compiler pipeline, NFA→DFA conversion, AST tree, SSA CFG, GC heap diagram, etc.)
8. `## Worked example 1`
9. `## Worked example 2`
10. `## Code` — Python: minimal scanner / Pratt parser / tree-walker / bytecode dispatch / liveness analysis / mark-sweep GC
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — links to [Theory of Computation](/cs/theory/intro), [Programming Language Theory](/cs/programming-language-theory/intro), [Operating Systems](/cs/operating-systems/intro), [Computer Architecture](/cs/computer-architecture/intro)
13. `## References` — IEEE-style (Nystrom *Crafting Interpreters*, Aho-Lam-Sethi-Ullman Dragon Book, Appel, Cooper-Torczon, plus foundational papers: Knuth 1965 LR parsing, Hindley 1969 / Milner 1978 type inference, Chaitin 1981 register allocation graph coloring, Cytron et al. 1991 SSA, Cheney 1970 copying GC, Dijkstra et al. tri-color GC)

## Word count

Each page: **2000-3500 words**.

## Visual policy

- **Mermaid mandatory** per page.
- Optional Wikimedia images: be conservative. Try only if you remember a real filename.
- Skip ar5iv figures (mostly pre-arxiv classics).
- Caption: `*Figure: <desc>. Image: [Wikimedia Commons](file-url), Author, License.*`

## Constraints

- Stay inside `docs/cs/compilers/`. Do not touch `_category_.json`.
- No paper titles in filenames.
- Mermaid special chars in `"..."`; internal `"` → `#quot;`.
- English. Match depth addendum.

## Output summary

```
Pages created: 1 intro + 7 detail = 8
Word counts per page
Figures: Wikimedia=W, Mermaid=M
References per page (avg)
```

Begin now.
