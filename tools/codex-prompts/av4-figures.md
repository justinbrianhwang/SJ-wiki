# Batch-4 AV pages — embed paper architecture figures

Read the **PAPER FIGURE EMBED POLICY** above. Add real paper figures (with full attribution
captions) to the 17 new autonomous-driving pages created in batch 4. Keep every existing Mermaid
diagram — figures are ADDED alongside, never replacing Mermaid.

## Target dir

`f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`

## Page → source PDF → arXiv id (verify the id from the PDF's first page before embedding)

| page | PDF in tmp/ | arXiv id (confirm) |
|---|---|---|
| `bevfusion-mit.md` | BEVFusion Multi-Task Multi-Sensor Unified BEV.pdf | 2205.13542 |
| `bevfusion-robust.md` | BEVFusion, A Simple and Robust LiDAR-Camera Fusion Framework.pdf | 2205.13790 |
| `bevdilation.md` | BEVDilation, LiDAR-Centric Multi-Modal Fusion for 3D Object Detection.pdf | read from PDF (≈2512.xxxxx) |
| `fusion4ca.md` | Fusion4CA, Boosting 3D Object Detection via Comprehensive Image Exploitation.pdf | 2603.05305 |
| `contrastalign.md` | ContrastAlign, ... .pdf | 2405.16873 |
| `post-fusion-bev-stabilization.md` | Post Fusion BEV Feature Stabilization.pdf | 2603.05623 |
| `hybrid-attention-fusion.md` | Multi-Modal Sensor Fusion using Hybrid Attention for Autonomous Driving.pdf | read from PDF (may be none) |
| `centerpoint.md` | Center-based 3D Object Detection and Tracking.pdf | 2006.11275 |
| `weather-occlusion-robustness.md` | Evaluating the Impact of Weather-Induced Sensor Occlusion ... .pdf | 2511.04347 |
| `tumtraf-v2x-dataset.md` | TUMTraf V2X Cooperative Perception Dataset.pdf | read from PDF (≈2403.xxxxx) |
| `cooperative-bev-fusion.md` | Camera and LiDAR BEV Fusion for Cooperative 3D ... TUMTraf V2X.pdf | 2606.12981 |
| `frenet-trajectory-generation.md` | Optimal Trajectory Generation Frenet Frame.pdf | none (ICRA 2010) |
| `sampling-based-motion-planning.md` | Efficient Sampling-Based Motion Planning ... .pdf | none (T-ITS 2015) |
| `urban-path-planning.md` | Path Planning and Decision Making ... Urban Environment.pdf | none (ITSC 2015) |
| `mpc-for-autonomous-driving.md` | Model Predictive Control for Autonomous Driving Vehicles.pdf | none (MDPI Electronics 2021) |
| `sensor-failure-safety-simulation.md` | Simulating the Effects of Sensor Failures ... .pdf | none |
| `shield-synthesis-runtime-enforcement.md` | Shield Synthsis, Rntime Enforcement for Reactive Systems.pdf | none (CAV 2015) |

## How to embed (arXiv papers)

1. Confirm the arXiv id by running `pdftotext -l 1 "<pdf>" -` and reading the `arXiv:XXXX.XXXXX` line.
2. The architecture/overview figure is usually **Figure 1 or 2** → ar5iv path `x1.png` or `x2.png`.
   Try, in order: `https://ar5iv.labs.arxiv.org/html/<id>/assets/x1.png`, then `.../assets/x2.png`,
   then `.../x1.png`, `.../x2.png`. Pick the one that is the architecture/pipeline overview.
3. Place the embed right under the page's `## Architecture diagram` heading, ABOVE the existing Mermaid
   block (so reader sees canonical figure first, then the annotated Mermaid).
4. Caption format (mandatory):

   ```markdown
   ![<descriptive alt text>](<ar5iv url>)

   *Figure: <one-line description>. From [<FirstAuthor> et al., <Year>](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
   ```

## Pages with NO arXiv (frenet, sampling, urban, mpc, sensor-failure, shield)

Do NOT fabricate URLs. Options, in priority:
- A relevant **Wikimedia Commons** image (`https://commons.wikimedia.org/wiki/Special:FilePath/<Filename>`)
  that genuinely illustrates the concept (e.g. a Frenet/Frenet–Serret frame diagram, an MPC
  receding-horizon schematic, a vehicle bicycle-model diagram). Caption with Commons attribution.
- Otherwise **leave Mermaid-only**. A missing figure is fine; a broken link is not.

## Validation (MANDATORY, do this before finishing)

```bash
python tools/check-image-urls.py docs/cs/autonomous-driving/ 2>&1 | grep BROKEN
```

For each BROKEN url: try the next candidate (`x2`→`x3`, or `/assets/` vs not); if still broken, REMOVE
the embed and its caption entirely. Re-run until no BROKEN lines for these 17 pages.

## Constraints

- Only edit the 17 batch-4 pages. Do not touch other pages, `intro.md`, configs, or Mermaid blocks.
- Do not run git/npm.

## Output

Summary: figures embedded (ar5iv vs Wikimedia), pages left Mermaid-only, broken URLs removed.
