You are an autonomous content author for **SJ Wiki**. Generate **detailed**, well-structured Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/C로 쓴 자료구조.pdf` (Korean-language data structures textbook in C)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/data-structures/`
- **SUBJECT**: Data Structures in C

## What to produce

1. **`intro.md`** — replace the stub. Overview + chapter list.

2. **One Markdown file per major topic.** Cover the full scope (typical Korean DS-in-C curriculum):
   - Arrays and array operations
   - Stacks (array-based and linked-list-based) + applications (expression evaluation)
   - Queues (linear, circular, deque) + applications
   - Linked lists (singly, doubly, circular)
   - Trees (binary tree representation, traversals)
   - Binary search trees (insert / delete / search)
   - Heaps and priority queues
   - Hashing (open addressing, chaining)
   - Graphs (representation: adjacency matrix / list)
   - Graph traversals (BFS, DFS)
   - Minimum spanning trees (Prim, Kruskal)
   - Shortest paths (Dijkstra, Floyd-Warshall)
   - Sorting algorithms (selection, insertion, bubble, quick, merge, heap, radix)
   - Searching algorithms (linear, binary)

   Aim for **15-22 pages**, each 500-1500 words.

3. **Per-page format**: intuition → ADT definition → C implementation → time/space complexity → example trace.

4. **Code in C** — actual compilable snippets. Use `c` language tag in fenced code blocks.

5. **Diagrams** in Mermaid for trees/graphs where simple.

## Language note

The source is Korean. **Write the wiki pages in English** (translate concepts), but quote original Korean terms in parentheses where they help (e.g., "stack (스택)"). Math/CS terminology in English.

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 25` → cover + TOC. Korean text will be cp949/UTF-8 — handle it.
3. Iterate chapters; write 1-3 wiki pages each.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/data-structures/`. Don't touch other folders, `_category_.json`, config files.
- Don't run `npm`.
- Don't fabricate.

Begin now.
