## ⚠️ CONTENT DEPTH REQUIREMENTS (override the per-page length below)

These requirements **override** any shorter targets in the subject-specific prompt that follows. The user has reviewed earlier output and wants longer pages with more visual content.

### Combine mode (DEFAULT for multi-book subjects)

If the OUTPUT_DIR already contains pages from another textbook on the same subject, treat this as a **combined / synthesized** treatment, not a parallel set of separate pages.

- Scan the existing pages first (`ls` + read a few).
- For each topic that BOTH books cover: write **one** wiki page that draws from both, noting where they differ in emphasis, notation, or proof style. Do NOT duplicate.
- For topics covered by only one book: add the page under the standard naming, marked with a brief note about which book is the source.
- Cross-link generously between the merged pages so the reader sees the synthesis.
- Existing pages may be **rewritten** (preserve `_category_.json`). Keep the better content from the existing page where the new book doesn't surpass it.

Examples of subjects already done in combine mode for reference: QM (4 books — Sakurai/Ballentine/Gottfried/Schiff), NLP (Eisenstein + Jurafsky&Martin), Cryptography (Katz-Lindell + Smart).

### Extra chapters (encouraged)

You are encouraged to add chapters beyond what the source book(s) literally cover, in three categories:

1. **Modern context**: topics the source omits because of its era (e.g., adding ARM/RISC-V to an 8085 book; adding async/await to a pre-2015 language book; adding diffusion models to a pre-2020 deep-learning book). Mark these clearly as supplementary; keep them short and well-cited.
2. **Completeness fillers**: book covers a topic but very briefly — write a fuller page if it earns its place in the subject's wiki.
3. **Cross-section bridges**: a page that explicitly connects two SJ Wiki sections (e.g., "MDPs and probability" linking RL and probability sections; "vector calculus for E&M" linking engineering-math and electromagnetics). These pages should sit in whichever section is the primary owner, with prominent cross-links.

Do not invent facts. If you're not sure of a modern topic's standard treatment, omit it.

### Word count target

- **Each page: 1500-3500 words** (NOT 500-1500). For dense topics (proofs, derivations, multi-method algorithms) lean toward the upper end.

### Visual content (MANDATORY per page)

Every page MUST include at least one of the following. Pages without any visual anchor are not acceptable.

1. **Mermaid diagram** — Docusaurus has `@docusaurus/theme-mermaid` configured. Use a fenced code block with `mermaid` language tag. Examples of when to use Mermaid:
   - State machines, finite automata
   - Flowcharts of algorithms / decision processes
   - Simple graphs (graph theory, dependency, ER, class hierarchy)
   - Trees (BST, B+, decision, derivation, parse)
   - Sequence diagrams (protocols, message-passing)
   - Block diagrams (control systems, system architecture)

   ```mermaid
   graph LR
     A[Input] --> B{Choice}
     B -->|yes| C[Path 1]
     B -->|no| D[Path 2]
   ```

2. **Comparison or reference table** — markdown tables. Examples:
   - Complexity classes ($O(1), O(\log n), \dots$)
   - Properties of distributions / transforms / operations
   - Algorithm comparison (time / space / stability)
   - Differentiation / integration rules cheat sheets
   - Cipher modes, mode-of-operation properties

3. **ASCII art** — for geometric or numerical concepts that Mermaid cannot express. Examples:
   - Number lines, intervals
   - Sketches of function graphs ("rough shape" diagrams)
   - Matrix block structure
   - Memory layout, stack frames

Aim for **2+ visuals on dense pages** (one diagram AND one table, etc.).

### Worked examples

- **At least TWO worked examples per page**, not one. Show every intermediate step. Numbered substeps are encouraged.
- Each example: state the problem → show the method → arrive at a checked answer.

### Page-structure template (use exactly these sections, in order)

```
---
title: <Human Title>
sidebar_position: <integer>
---

# <Human Title>

<1-2 paragraphs of intuition: what is this, why does it matter, where it sits among neighbouring topics>

## Definitions

<formal definitions, notation, basic facts>

## Key results

<theorems, lemmas, key formulas — with proofs or proof sketches where reasonable>

## Visual

<MANDATORY: Mermaid diagram, comparison table, or ASCII figure that anchors the concept>

## Worked example 1: <descriptive name>

<full work with intermediate steps>

## Worked example 2: <descriptive name>

<full work with intermediate steps>

## Code

<runnable, meaningful snippet — Python / C++ / MATLAB / etc. as appropriate. Tag the language. Multiple lines, not a one-liner.>

## Common pitfalls

<bullet list of mistakes students typically make and how to avoid them>

## Connections

<bullet list of cross-links to related wiki pages, using absolute paths like /math/calculus/limits>
```

If a section genuinely has no content for a particular topic, you may omit it — but **Visual, Worked example 1, and Common pitfalls are mandatory on every page**.

### LaTeX / KaTeX

- Inline math: `$...$`
- Display math: `$$...$$`
- Multi-line aligned equations: `$$\begin{aligned} a &= b \\ &= c \end{aligned}$$` (do NOT use `\begin{align}` — KaTeX rejects it).
- Reactions: `$$\mathrm{2H_2 + O_2 \to 2H_2O}$$` for chemistry-style notation.

### Cross-references

- Cross-doc links inside the wiki use **absolute** paths from the docs root, e.g. `[derivatives](/math/calculus/derivatives-and-rates)` — relative `./` paths break under slug rewriting.

---

The subject-specific prompt follows below. Read it and obey both this addendum and that.

---

