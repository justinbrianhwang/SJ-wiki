You are adding **paper architecture figures** to the autonomous-driving section of SJ Wiki.

## Target

`f:/coding/SJ Wiki/docs/cs/autonomous-driving/`

## What to do

Read the **MODEL ARCHITECTURE FIGURES POLICY** above. For each named model in this section's pages, embed the paper's architecture figure with full caption + attribution. Place it at the top of the named-model subsection (right after the section heading).

## Models to cover in this directory

Use the AV table in the policy above. Confirmed mappings:

- **TransFuser** (`2205.15997`, `x2.png`) — in `end-to-end-driving.md` § "Transformer fusion"
- **InterFuser** (`2207.14024`, `x2.png`) — in `end-to-end-driving.md` § "Transformer fusion"
- **ChauffeurNet** (`1812.03079`, `x1.png`) — in `end-to-end-driving.md` § "Mid-level and privileged imitation"
- **VAD** (`2303.12077`, `x2.png`) — in `end-to-end-driving.md` § "Planning-oriented full-stack learning"
- **MILE** (`2210.07729`, `x2.png`) — in `end-to-end-driving.md` § "Generative planning and world models"
- **DriveDreamer** (`2309.09777`, `x1.png`) — same section
- **GAIA-1** (`2309.17080`, `x1.png`) — same section
- **PilotNet** (Bojarski 2016, no ar5iv — use Wikimedia `PilotNet_architecture.svg` if known, else skip)
- **BEVFormer** (`2203.17270`, `x2.png`) — `perception-object-detection-and-segmentation.md`
- **CenterPoint** (`2006.11275`, `x1.png`) — same page
- **DETR3D** (`2110.06922`, `x2.png`) — same page
- **LSS / Lift-Splat-Shoot** (`2008.05711`, `x2.png`) — same page or `sensor-fusion.md`
- **HiVT / Wayformer / MultiPath** — `prediction-and-motion-forecasting.md`:
  - Wayformer (`2207.05844`, `x1.png`)
  - MultiPath (`1910.05449`, `x2.png`)
- **UniAD** already embedded in `intro.md`, `foundation-models-for-driving.md`, `end-to-end-driving.md` — don't duplicate.
- **PointPillars**, **VectorNet**, **RP2** already embedded — don't duplicate.

## Format (mandatory)

```markdown
![<descriptive alt text>](https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png)

*Figure: <one-line description of what this figure shows>. From [Author et al., Year](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
```

## Verification (mandatory)

After all edits, run:

```bash
python tools/check-image-urls.py docs/cs/autonomous-driving/ 2>&1 | grep BROKEN
```

For each BROKEN URL: try `x1.png` → `x2.png` → `x3.png` in order. If none work, remove the embed entirely. Never push a broken URL.

## Output

Final summary:

```
Pages touched: N
Figures embedded: M (ar5iv: M-k, Wikimedia: k)
Broken URLs found and removed: x
Models skipped (no good source): list
```

## Constraints

- Stay inside `docs/cs/autonomous-driving/`.
- Don't touch existing Mermaid diagrams or other content.
- Don't duplicate already-embedded figures.
- Don't add captions without source attribution.
- Don't fabricate arxiv IDs or figure numbers.

Begin now.
