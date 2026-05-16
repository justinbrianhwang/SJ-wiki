You are an autonomous content author for **SJ Wiki**. Generate **attack/defense deep-dive pages** for the Adversarial Attacks section from a folder of 41 papers.

## Inputs

- **SOURCE_FOLDER**: `f:/coding/SJ Wiki/tmp/` — 41 PDFs covering adversarial ML attacks and defenses. Filenames are mixed: some descriptive (e.g. `FGSM.pdf`), most are arxiv IDs (`YYMM.NNNNN`) or conference DOIs.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/`

## Existing foundational pages (do NOT overwrite — they're conceptual scaffolding)

```
intro.md
threat-models-and-attack-taxonomy.md
mathematical-formulation.md
white-box-attacks.md
black-box-and-transfer-attacks.md
physical-world-and-patch-attacks.md
adversarial-training.md
certified-defenses-and-randomized-smoothing.md
gradient-masking-and-obfuscation.md
evaluation-and-benchmarks.md
robustness-accuracy-tradeoff.md
attacks-on-llms-and-other-modalities.md
```

Run `ls docs/cs/adversarial-attacks/` first to confirm.

## CRITICAL NAMING POLICY

Page filenames MUST be the **attack name** or **defense name**, NOT the paper title or author. Examples:

- ✅ `fgsm.md`, `pgd.md`, `bim.md`, `deepfool.md`, `carlini-wagner-attack.md`
- ✅ `universal-adversarial-perturbations.md`, `one-pixel-attack.md`, `physical-stop-sign-attack.md`
- ✅ `badnets-backdoor.md`, `adaptive-autoattack.md`, `lidar-spoofing.md`
- ✅ `textfooler.md`, `audio-adversarial.md`, `gcg-jailbreak.md`
- ❌ `goodfellow-2014.md`, `1706-06083-madry.md`, `attention-is-all-you-need-but-for-attacks.md`

If a paper introduces a named attack/defense, use that name. If not, use the technique it represents.

## Workflow

1. **Survey phase**: for every PDF in tmp/, run `pdftotext -l 2 "<pdf>" -` to get title + authors + venue. Build an internal mapping: `<filename> → <attack/defense name> + <year>`.

2. **Group phase**: decide a target set of **15-25 wiki pages**. Use your judgment:
   - Closely related variants of one attack may share a page (e.g. BIM is so close to FGSM iterated that it can sit on `bim.md` or even share `fgsm.md` if better).
   - A landmark paper that introduces something distinctive deserves its own page (FGSM, PGD, C&W, DeepFool, UAP, BadNets, etc.).
   - Several minor or domain-specific papers (radio modulation, specific LiDAR exploit) may be grouped into a "domain-specific attacks" page if you don't want a separate page per niche.
   - If a paper is more naturally a **defense** than an attack, use a defense-name page.

3. **Write phase**: produce each page following the depth addendum (1500-3500 words, mandatory Mermaid block diagram or comparison table, ≥2 worked examples with full steps, common pitfalls, PyTorch sketch where the attack/defense is implementable, conservative result claims).

   Per-page sections (in order):
   - Frontmatter: `title:` (attack/defense name + year of original paper in parens, e.g. `"FGSM (Goodfellow et al., 2014)"`), `sidebar_position:` (assign integers starting from **20** so they sort after the 12 foundational pages; use chronological / logical order)
   - 1-paragraph elevator pitch
   - **Threat model** — explicit white/grey/black-box, targeted/untargeted, norm, attacker knowledge
   - **Method** — algorithm with KaTeX math (gradient formulas, update rules, optimization objectives)
   - **Visual** — mandatory Mermaid diagram of the attack pipeline OR comparison table
   - **Worked example** — at least one concrete instance (e.g. trace one PGD iteration; sketch a stop-sign attack's optimization steps)
   - **Implementation** — minimal PyTorch (or Foolbox-style pseudocode) when applicable
   - **Original paper results** — conservative quotation: state the model, dataset, $\epsilon$/budget, headline number
   - **Connections** — cross-link to foundational pages (`/cs/adversarial-attacks/white-box-attacks` etc.), neighboring attack pages, and relevant `/cs/deep-learning/` pages
   - **Common pitfalls / when this attack is used today**
   - **Further reading** — name the original paper + key follow-ups without writing the deep-dive elsewhere

4. **Update `intro.md`**: append a new section titled "## Attack and defense deep-dives" listing every paper-deep-dive page you produce. **Preserve** the existing 12-foundational-page list.

5. **Print summary**: list every file you created/modified.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/`.
- Do NOT overwrite or modify the 12 existing foundational pages (other than `intro.md` for the appended listing).
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Don't fabricate numbers.
- Mermaid labels with special characters must be wrapped in `"..."`; internal `"` must be `#quot;`; `{` and `}` inside labels are hazardous and need the same treatment.
- Be **conservative about coverage of post-2024 papers** — if a 2025 paper introduces something specific, treat it as a "frontier" entry without overclaiming.

## Time budget

This is a big run. You have ~40-60 minutes. If you fall behind, prefer **finishing fewer pages well** over starting many pages incompletely. The wiki can be expanded in follow-up runs.

Begin now.
