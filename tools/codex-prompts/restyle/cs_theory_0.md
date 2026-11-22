# SJ Wiki — restyle pass (structure and voice, not length)

You are editing existing pages of SJ Wiki (Docusaurus + KaTeX + Mermaid), a personal study-notes site at `f:/coding/Web/SJ Wiki`. These pages already have enough content. They were generated from one rigid template (Definitions / Key results / Visual / Worked example / Code / Common pitfalls / Connections) and read as machine-made. Your job is to make each page read like a careful researcher's own notes **without losing substance**.

## For each file listed at the bottom

1. Read it fully.
2. **Replace generic headings with topic-specific ones.** Name sections after what they contain ("Deriving the Bode asymptotes", "Why Dijkstra fails on negative edges"), never "Definitions", "Key results", "Visual", "Code", "Common pitfalls". Reorder sections if a different order explains the topic better. Different pages should end up with different outlines.
3. **Fold the "Visual" section into the section its diagram/table explains.** Keep every Mermaid diagram and table that is correct.
4. **Code:** keep code on programming, algorithms, numerical, ML, systems and simulation pages (put it under a descriptive heading). Delete a code block that is a trivial toy unrelated to how the subject is practiced (e.g. a 5-line Python helper on a chemistry concept page).
5. **Pitfalls:** keep the useful ones, but write them naturally (prose or a list) under a descriptive heading, or fold them into the relevant section. Never use the formula "X. Avoid it by Y-ing."
6. **Ending:** finish with `## Related pages` containing the existing cross-link list (absolute links). Keep only links to pages that exist — check with `ls` under `docs/`. A link to a section root like `/physics/thermodynamics` must become `/physics/thermodynamics/intro`.
7. **Remove decorative images**: any Wikimedia image that only decorates (logos, generic photos) together with its `*Figure: …*` caption. Keep images that show the actual concept.
8. **Edit sentences** that use banned phrasing (below). Otherwise keep the author's content and math; fix anything factually wrong.

Length may change modestly; do not pad and do not cut real content.

### Banned phrasing

"This is why", "A practical …", "is not just", "is not simply", "makes … visible", "grounds …", "deserves its own", "In practice," as a paragraph opener, "Crucially", "It's worth noting", "delve", "In summary", "Key takeaway", "the snippet below", sentences about "this page" or "the wiki", paragraphs that end with a one-line moral. Prefer plain, specific, slightly terse sentences.

## Technical rules

- Keep frontmatter (`title`, `sidebar_position`) and filenames unchanged.
- Inline math `$...$`, display math `$$...$$` on their own lines; `\begin{aligned}` not `\begin{align}`.
- In prose, escape literal `{` `}` as `\{` `\}` (MDX).
- Mermaid labels containing `( ) : , = ? ' " |` must be quoted.
- Do NOT touch `_category_.json`, `intro.md`, config files, or any file not in the list. No npm, no git.
- Write each file to disk as soon as it is done, then move on.

## Files to restyle

- `f:/coding/Web/SJ Wiki/docs/cs/theory/advanced-complexity-topics.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/context-free-grammars-and-normal-forms.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/decidability-and-the-halting-problem.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/finite-automata-and-dfas.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/mathematical-preliminaries.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/non-context-free-languages.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/nondeterminism-and-closure.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/np-completeness-and-classic-reductions.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/proof-methods-and-countability.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/pushdown-automata-and-deterministic-cfls.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/reductions-and-the-recursion-theorem.md`
- `f:/coding/Web/SJ Wiki/docs/cs/theory/regular-expressions-and-nonregularity.md`
