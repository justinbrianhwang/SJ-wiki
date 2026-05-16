You are an autonomous content author for **SJ Wiki**. Generate **system/component deep-dive pages** for the Autonomous Driving section from a folder of 53 papers.

## Inputs

- **SOURCE_FOLDER**: `f:/coding/SJ Wiki/tmp/ad/` — 53 PDFs on autonomous driving. Mixed filenames: descriptive (`Gao_VectorNet_...`, `Lang_PointPillars_...`), arxiv IDs (`YYMM.NNNNN`), conference DOIs, surveys.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/autonomous-driving/`

## Existing foundational pages (do NOT overwrite — leave as conceptual scaffolding)

```
intro.md
sae-levels-and-operational-design-domain.md
sensors-cameras-lidar-radar-imu.md
perception-object-detection-and-segmentation.md
depth-estimation-and-stereo-vision.md
sensor-fusion.md
localization-and-hd-maps.md
prediction-and-motion-forecasting.md
motion-planning.md
decision-making-and-behavior-planning.md
control-pid-mpc-pure-pursuit-stanley.md
end-to-end-driving.md
simulation-and-data.md
safety-iso26262-sotif-scenario-testing.md
v2x-and-connected-vehicles.md
adversarial-and-physical-attacks-on-av.md
```

Run `ls docs/cs/autonomous-driving/` first to confirm.

## CRITICAL NAMING POLICY

Page filenames MUST be the **system / model / component name**, NOT the paper title or author. Examples:

- ✅ `pointpillars.md`, `centerpoint.md`, `vectornet.md`, `hivt.md`, `pnpnet.md`
- ✅ `chauffeurnet.md`, `mv3d.md`, `leapvad.md`, `limsim.md`, `autovla.md`
- ✅ `darpa-urban-challenge.md`, `vla-for-driving-survey.md`, `mllm-for-driving-survey.md`
- ✅ `dynamic-conditional-imitation-learning.md` (if a unique technique without short name)
- ❌ `lang-cvpr2019.md`, `1812-03079.md`, `gao-vectornet-2020.md`

If a paper introduces a named system, use that. Survey papers should be named by topic (e.g. `vla-for-driving-survey.md`).

## Workflow

1. **Survey phase**: for each PDF in `tmp/ad/`, run `pdftotext -l 2 "<pdf>" -` to get title + authors + venue. Build a mapping: `<filename> → <system name> + <year> + <venue>`.

2. **Group phase**: target **15-25 wiki pages**. Use judgment:
   - Landmark systems deserve standalone pages (PointPillars, CenterPoint, VectorNet, HiVT, PnPNet, ChauffeurNet, MV3D).
   - Surveys → one page each, named by topic (`vla-for-driving-survey.md`, `mllm-for-driving-survey.md`).
   - Closely related variants may share a page (e.g., multiple VLA papers can each have their own page if they introduce distinct ideas).
   - Niche / domain-specific papers (drones, sonar 3D reconstruction, etc.) may be grouped into a "domain-specific or non-road AV" page if you don't want a standalone.
   - Historical papers (DARPA Urban Challenge) get a `darpa-urban-challenge.md` page.

3. **Write phase**: each page follows the depth addendum (1500-3500 words, mandatory Mermaid block diagram or comparison table, ≥2 worked examples, conservative result claims, PyTorch sketch where applicable, common pitfalls).

   Per-page sections:
   - Frontmatter: `title:` (system name + year, e.g. `"PointPillars (Lang et al., 2019)"`), `sidebar_position:` (integers starting at **20** — sort by topic cluster: perception → fusion → prediction → planning → end-to-end / VLA → safety / simulation)
   - 1-paragraph elevator pitch with full citation
   - **Problem & motivation** — what gap in AV stack this addresses
   - **Method** — architecture / algorithm with KaTeX math (pillar/voxel encoding, attention over agents, BEV transforms, vector representations, imitation losses, VLA token interfaces, etc.)
   - **Visual** (mandatory) — Mermaid block diagram of the architecture
   - **Architecture details / hyperparameters**
   - **Datasets and headline results** — conservatively quoted (KITTI, nuScenes, Waymo Open, Argoverse — state metric + value, don't fabricate)
   - **Connections** — cross-link to foundational AV pages (`/cs/autonomous-driving/perception-...`, etc.), neighboring system pages, and `/cs/deep-learning/`, `/cs/reinforcement-learning/`, `/cs/adversarial-attacks/`
   - **PyTorch sketch** — minimal `torch` snippet of the core idea (pillar feature net, vector encoder, attention block)
   - **Common pitfalls / where this is used today**
   - **Further reading** — name follow-up papers / extensions

4. **Update `intro.md`**: append a new section "## System and paper deep-dives" listing every new page you produce. **Preserve** the existing 16-foundation page list.

5. **Print summary**: list every file you created / modified.

## Suggested groupings (you may revise)

**Perception / 3D detection cluster** (positions 20-25): pointpillars, centerpoint, mv3d, voxelnet (if covered), pillar-or-voxel-survey

**Motion forecasting / interaction cluster** (positions 26-31): vectornet, hivt, trajectron (if covered), social-lstm (if covered), pnpnet

**End-to-end / classical pipelines cluster** (positions 32-37): chauffeurnet, dynamic-conditional-imitation, alvinn-revisit (if covered), classical-pipeline-darpa, vla-models-survey

**VLA / LLM for driving cluster** (positions 38-44): autovla, pointvla, leapvad, limsim, mllm-for-driving-survey, vla-for-driving-survey, dolphins-or-similar

**Domain / niche** (positions 45+): drone-papers, sonar-mv3d, journal-of-field-robotics-darpa, etc.

These are SUGGESTED — your final clustering should reflect what the papers actually contain.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/autonomous-driving/`.
- Do NOT overwrite or modify the 16 existing foundational pages (other than `intro.md` for the appended listing).
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Don't fabricate numbers.
- Mermaid labels with special characters wrapped in `"..."`; internal `"` → `#quot;`; `{` and `}` are hazardous and need the same treatment.
- Be conservative on post-2024 papers — if the paper introduces something specific to a single system or benchmark, note that scope.

## Time budget

~40-60 minutes. If you fall behind, prefer **finishing fewer pages well** over starting many incompletely.

Begin now.
