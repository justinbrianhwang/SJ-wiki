# MERGE AGENT 1 — fold BEV-fusion papers into sensor-fusion.md

The project decided NOT to keep these as standalone pages. Fold their content, condensed, into
the existing foundation page as a cited section. **Do not create new pages.**

## Target (edit ONLY this file)

`f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/sensor-fusion.md`

## Source material (already written — read these for the content; they will be DELETED afterward by the orchestrator, so the surviving summary must live in sensor-fusion.md)

- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/bevfusion-robust.md`
- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/bevdilation.md`
- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/fusion4ca.md`
- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/contrastalign.md`
- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/post-fusion-bev-stabilization.md`
- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/hybrid-attention-fusion.md`
- `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/weather-occlusion-robustness.md`

(Note: BEVFusion-MIT and CenterPoint REMAIN standalone — you may cross-link them but do not summarize them here.)

## What to do — exact, conservative edit

1. Read `sensor-fusion.md` fully. **Preserve every existing section, figure, and Mermaid block unchanged.**
2. Insert ONE new section titled `## Recent BEV LiDAR–camera fusion systems` immediately **before** the existing `## Common pitfalls` section.
3. In it, write **one tight paragraph per paper** (≈4–7 sentences) capturing the key idea, the mechanism, and what problem it solves, drawn from the corresponding source page. Use inline numeric citations `[1]`–`[7]`. Group sensibly:
   - Robust two-stream BEV fusion [1] (bevfusion-robust)
   - LiDAR-centric dilation fusion [2] (bevdilation)
   - Comprehensive image exploitation [3] (fusion4ca)
   - Contrastive BEV feature alignment [4] (contrastalign)
   - Post-fusion BEV stabilization [5] (post-fusion-bev-stabilization)
   - Hybrid (self+cross) attention fusion [6] (hybrid-attention-fusion)
   - Weather-occlusion robustness study [7] (weather-occlusion-robustness)
   You may add a 2–3 sentence intro framing these as the modern BEV-fusion family, and cross-link the two surviving pages `/cs/autonomous-driving/bevfusion-mit` and `/cs/autonomous-driving/centerpoint`.
4. Optionally include ONE compact comparison table (system | core idea | modality emphasis | benchmark) if it reads well. Keep it conservative on numbers.
5. Append a new `## References` section at the very END of the file (after `## Connections`) with the IEEE-style numbered list `[1]`–`[7]`. Pull the exact citation strings from each source page's own References `[1]`.

## Constraints

- Edit ONLY `sensor-fusion.md`. Do not touch the 7 source pages or any other file.
- Keep total added length reasonable (a condensed section, NOT 7 full pages). Target ≈600–1100 words added.
- Mermaid hazards / KaTeX rules as usual. No `\begin{align}`.
- Do not run git/npm. Print a short summary of what you added.
