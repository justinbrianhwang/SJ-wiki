# Embed paper figures — final AV set (5 kept pages + sensor-fusion BEV section)

Read the **PAPER FIGURE EMBED POLICY** above. Add real paper architecture figures with full
attribution captions. **Keep every existing Mermaid diagram** — figures are ADDED, never replace Mermaid.

## Target dir

`f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`

## Pages and figure sources

1. `centerpoint.md` — CenterPoint, arXiv **2006.11275**. Architecture/overview figure (try `assets/x1.png`,
   then `assets/x2.png`, then `x1.png`, `x2.png`). Place under `## Architecture diagram`, ABOVE the Mermaid.
2. `bevfusion-mit.md` — BEVFusion (MIT), arXiv **2205.13542**. Overview figure (try x1/x2). Same placement.
3. `tumtraf-v2x-dataset.md` — TUMTraf V2X, confirm arXiv id from the PDF
   `f:/coding/Web/SJ Wiki/tmp/TUMTraf V2X Cooperative Perception Dataset.pdf` (≈2403.xxxxx); embed the
   sensor-setup / dataset-overview figure if available. If no good ar5iv image, use a relevant Wikimedia
   Commons image of roadside/cooperative perception, else leave Mermaid-only.
4. `frenet-trajectory-generation.md` — Werling 2010, NO arXiv. Use a **Wikimedia Commons** Frenet–Serret /
   road-aligned frame diagram (`Special:FilePath/...`) IF one genuinely illustrates the s–d frame; else
   leave Mermaid-only. Do NOT fabricate an ar5iv URL.
5. `shield-synthesis-runtime-enforcement.md` — Bloem 2015, NO arXiv. Leave Mermaid-only unless a clearly
   relevant Wikimedia image of a reactive-system/automaton exists. Do NOT fabricate URLs.
6. `sensor-fusion.md` — in the existing `## Recent BEV LiDAR–camera fusion systems` section ONLY, optionally
   add ONE figure: the robust BEVFusion overview (arXiv **2205.13790**, try x1/x2) near the "Robust
   two-stream BEV fusion" paragraph. Do NOT modify any other part of sensor-fusion.md.

## Format (mandatory)

```markdown
![<descriptive alt text>](<url>)

*Figure: <one-line description>. From [<FirstAuthor> et al., <Year>](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
```

For Wikimedia, caption with `[Wikimedia Commons](file-page-url), Author, License`.

## Validation (MANDATORY before finishing)

```bash
python tools/check-image-urls.py docs/cs/autonomous-driving/ 2>&1 | grep BROKEN
```

For each BROKEN url from the pages you touched: try the next candidate; if still broken, REMOVE that
embed + caption. Re-run until none of YOUR added urls are BROKEN. A missing figure is fine; a broken link is not.

## Constraints

- Only edit the 6 files listed. Do not touch other pages, configs, or any Mermaid block.
- Do not run git/npm.
- Output: figures embedded (ar5iv vs Wikimedia), pages left Mermaid-only, broken URLs removed.
