# SJ Wiki — Autonomous Driving paper deep-dives (Batch 4)

You are an autonomous content author for **SJ Wiki**, a Docusaurus study wiki. You are writing
**paper / system deep-dive pages** for the Autonomous Driving section.

## Fixed paths (project moved — use these EXACTLY)

- **PROJECT ROOT**: `f:/coding/Web/SJ Wiki/`
- **OUTPUT_DIR**: `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`
- **SOURCE PDFs**: `f:/coding/Web/SJ Wiki/tmp/` (filenames given per paper below)

First run `ls "f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/"` to see the 16 existing
foundational pages. **Do NOT overwrite or modify any existing page**, and do NOT touch
`intro.md`, `_category_.json`, `sidebars.ts`, `docusaurus.config.ts`, or `package.json`.
(The orchestrator updates `intro.md` and positions afterward.) You ONLY create the new
`.md` files assigned to you in the agent-specific section that follows.

## How to read each PDF

Use `pdftotext "<absolute pdf path>" -` (whole document) and read it. For figures, note the
figure numbers you reference. Quote results conservatively — never fabricate numbers; if unsure,
state the metric qualitatively.

## Per-page format (this OVERRIDES the generic template in the depth addendum)

These are paper deep-dives, so use these sections instead of the math-style template, but keep
the addendum's depth (1500–3500 words), mandatory-visual, and KaTeX rules.

```
---
title: "<System/Topic Name> (<FirstAuthor> et al., <Year>)"
sidebar_position: <integer given per paper>
---

# <System/Topic Name>

<1–2 paragraph elevator pitch with the full citation inline (authors, venue, year).>

## Problem & motivation
<What gap in the AV stack this addresses.>

## Method
<Architecture / algorithm in depth, with KaTeX math. Define notation. This is the core.>

## Architecture diagram
<MANDATORY visual: a Mermaid block diagram of the pipeline/architecture. Follow Mermaid hazards below.>

## Architecture details
<Backbones, BEV grid sizes, heads, losses, hyperparameters as reported.>

## Datasets & results
<Benchmarks used (KITTI / nuScenes / Waymo / Argoverse / TUMTraf etc.) with metric names
(mAP, NDS, AMOTA, ADE/FDE, etc.) and reported values — conservatively quoted. A comparison
table is strongly encouraged.>

## Worked example  (or step-by-step walkthrough)
<At least one concrete walkthrough: e.g. trace a point through the BEV transform, compute a
cost-functional term, expand the kinematic model, work an IoU/NDS calc, etc.>

## Code
<A minimal, meaningful PyTorch/Python/MATLAB sketch of the core idea — not a one-liner.>

## Common pitfalls
<Bullets: failure modes, where it breaks, deployment caveats.>

## Connections
<Bullet cross-links (ABSOLUTE paths) to foundation pages and sibling system pages, e.g.
/cs/autonomous-driving/sensor-fusion, /cs/autonomous-driving/perception-object-detection-and-segmentation,
/cs/autonomous-driving/motion-planning, /cs/deep-learning/..., /cs/adversarial-attacks/...>

## References
<IEEE-style numbered list. The paper itself is [1]; add key cited works as [2], [3], ...>
```

## Citation style

- Topical headings only — NEVER name a section after the paper title.
- Use inline numeric citations `[1]`, `[2]` in the prose, with the numbered **References** list at the page end.

## Mermaid hazards (Docusaurus build will FAIL otherwise)

- Wrap any label containing `(` `)` `=` `?` `:` `,` `|` `{` `}` `'` `"` `[` `]` in double quotes: `A["BEV grid (200x200)"]`.
- Internal `"` inside a label → `#quot;`.
- Edge labels with special chars: `A -->|"label, with comma"| B`.
- Do NOT use `#lsqb;`/`#rsqb;`.

## KaTeX

- Inline `$...$`, display `$$...$$`. Multi-line: `$$\begin{aligned} ... \end{aligned}$$` (NOT `align`).

## When done

Print the list of every file you created. Do not run `npm`, git, or the sanitizers — the
orchestrator does that.

---
The agent-specific paper list follows below.
---
