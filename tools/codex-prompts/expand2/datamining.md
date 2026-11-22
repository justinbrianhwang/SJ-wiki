# SJ Wiki — expand thin pages (style-aware pass)

You are expanding existing pages of SJ Wiki (Docusaurus + KaTeX + Mermaid), a personal study-notes site at `f:/coding/Web/SJ Wiki`. The owner wants the site to read like a careful researcher's own notebook, NOT like AI-generated template output. Depth AND voice both matter.

## Task

Expand **only the files listed at the bottom** of this prompt, in place. Each is currently too thin. Read each file fully, then rewrite/extend it so it becomes a genuinely useful reference page.

- Target: **1800–3000 words of prose** per page (math and code blocks do not count toward this).
- Keep the frontmatter (`title`, `sidebar_position`) unchanged. Keep the filename.
- Keep correct existing content (definitions, math, Mermaid diagrams, tables) unless you are improving it. Fix anything that is wrong.
- Add real substance: derivations and proof sketches, the *why* behind results, edge cases, historical/standard-textbook context, 2+ worked examples with every step shown, comparison tables where they actually help.
- Do not invent facts, citations, paper numbers, or URLs. If unsure, leave it out.

## Voice and structure (important — this is why the pass exists)

The old pages all used the same six headings (Definitions / Key results / Visual / Code / Common pitfalls / Connections). That uniformity is what makes the site look machine-made. For each page:

1. **Choose headings that fit the topic.** A probability page might go: motivation → the definition → derivation of the mean and variance → examples → where it shows up. A C++ page might go: syntax → what the compiler actually does → pitfalls with real error messages. Name sections after their content ("Deriving the partition function", "Why the bias term matters"), not generic labels like "Key results" or "Visual".
2. **Rename or merge the existing generic headings** accordingly. A diagram goes inside the section it explains; it does not need its own "Visual" heading.
3. **Code only when it earns its place.** Remove a `## Code` section that is a trivial toy unrelated to how the subject is practiced. Keep/expand code on programming, algorithms, numerical, ML, and simulation pages.
4. **No decorative images.** Do not add Wikimedia/stock images. Mermaid diagrams, tables, and ASCII sketches are fine when they explain something.
5. Pitfalls may stay as a list, but write each item naturally — do NOT use the formula "X. Avoid it by Y-ing."
6. Keep a short related-pages list at the end (absolute links like `/math/probability/expectation`), but only link pages that actually exist — check with `ls`.

### Banned phrasing

Do not use: "This is why", "A practical …", "is not just", "is not simply", "makes … visible", "grounds …", "deserves its own", "In practice," as a paragraph opener, "Crucially", "It's worth noting", "delve", "In summary", "Key takeaway", "the snippet below is intentionally small", sentences that talk about "this page" or "the wiki". Avoid rule-of-three lists in every sentence, and avoid ending paragraphs with a one-line moral. Prefer plain, specific, slightly terse sentences, the way a person writes notes for themselves.

## Technical rules

- Inline math `$...$`, display math `$$...$$` on their own lines. Use `\begin{aligned}` not `\begin{align}`.
- In prose (outside math/code), escape literal `{` `}` as `\{` `\}` (MDX).
- Mermaid labels containing `( ) : , = ? ' " |` must be quoted: `A["f(x) = 0"]`.
- Do NOT touch `_category_.json`, `intro.md`, `docusaurus.config.ts`, `sidebars.ts`, `package.json`, or any file not in the list.
- Do not run `npm` builds or git commands; the orchestrator does that.
- Work through the files one by one and write each file to disk as soon as it is done.

## Files to expand

- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-02-data-preparation.md` (currently ~1141 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-02-feature-selection-dimensionality-reduction.md` (currently ~1116 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-03-similarity-distances.md` (currently ~1062 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-06-cluster-analysis.md` (currently ~1191 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-08-outlier-analysis.md` (currently ~1193 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-09-advanced-outlier-analysis.md` (currently ~1197 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-10-data-classification.md` (currently ~1138 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-12-mining-data-streams.md` (currently ~1131 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-13-mining-text-data.md` (currently ~1126 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-14-mining-time-series-data.md` (currently ~1063 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-15-mining-discrete-sequences.md` (currently ~1119 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-16-mining-spatial-data.md` (currently ~1179 prose words)
- `f:/coding/Web/SJ Wiki/docs/cs/data-mining/chapter-18-mining-web-data.md` (currently ~1131 prose words)
