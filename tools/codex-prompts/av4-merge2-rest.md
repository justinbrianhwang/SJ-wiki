# MERGE AGENT 2 — fold V2X / planning / control / safety papers into their foundation pages

Fold each source paper's content, condensed, into the matching existing foundation page as a
cited section. **Do not create new pages.** Edit the 4 target files below.

For EACH target page:
1. Read the target page fully. **Preserve every existing section, figure, and Mermaid block.**
2. Insert ONE new `## Recent systems and papers` section immediately **before** that page's
   `## Common pitfalls` section (if a page already has such a section, append to it).
3. Write one tight paragraph per source paper (≈4–7 sentences) with inline `[N]` citations,
   drawn from the source page. Cross-link relevant siblings where natural.
4. Append a `## References` section at the END of that page (after `## Connections`) with the
   IEEE-style numbered citations, taken from each source page's own `[1]`.

## Target → source mapping

### `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/v2x-and-connected-vehicles.md`
- source: `.../cooperative-bev-fusion.md` — cooperative (infrastructure↔vehicle) camera-LiDAR BEV fusion on TUMTraf V2X. Cross-link the surviving dataset page `/cs/autonomous-driving/tumtraf-v2x-dataset`.

### `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/motion-planning.md`
- source: `.../sampling-based-motion-planning.md` — efficient on-road sampling planner.
- source: `.../urban-path-planning.md` — urban path planning + behavior decision layer.
  (Use [1], [2] for these two.)

### `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/control-pid-mpc-pure-pursuit-stanley.md`
- source: `.../mpc-for-autonomous-driving.md` — receding-horizon MPC path tracking with a vehicle model.

### `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/safety-iso26262-sotif-scenario-testing.md`
- source: `.../sensor-failure-safety-simulation.md` — fault injection / simulating sensor failures for safety evaluation. Cross-link the surviving page `/cs/autonomous-driving/shield-synthesis-runtime-enforcement`.

## Constraints

- Edit ONLY the 4 target files. Do not touch the source pages or any other file.
- Each added section condensed (≈250–500 words per source paper), NOT a full page.
- The source pages (cooperative-bev-fusion, sampling-based-motion-planning, urban-path-planning,
  mpc-for-autonomous-driving, sensor-failure-safety-simulation) will be DELETED afterward, so the
  surviving summary must live in the target foundation page.
- Mermaid/KaTeX rules as usual. No `\begin{align}`. Do not run git/npm.
- Print a summary of sections added per file.
