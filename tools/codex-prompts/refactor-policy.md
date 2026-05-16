## REFACTOR POLICY — paper-named pages into topical foundation pages

You are restructuring a wiki section that currently has two kinds of pages:

1. **Foundation pages** — topical, textbook-style (e.g., `white-box-attacks.md`, `perception-object-detection-and-segmentation.md`, `error-correction.md`)
2. **Paper-named pages** — one-paper-per-page deep dives (e.g., `pgd.md`, `pointpillars.md`, `willow-surface-code-below-threshold.md`)

The user wants the wiki to read like a textbook: **topical chapters with papers cited inline**, not paper-by-paper deep dives.

### What you must do

For each paper-named page in the section:

1. **Read** the paper page in full.
2. **Decide** the best home: an existing foundation page whose topic naturally contains this paper's contribution. If no existing foundation page fits, **create a new topical foundation page** (textbook-style filename, e.g. `efficient-sequence-modeling.md`, `foundation-models-for-driving.md`) and put it at a reasonable `sidebar_position` after the existing foundation pages but before any remaining paper pages.
3. **Merge** the paper's content into the target foundation page as a focused sub-section. The sub-section should:
   - Have a topical heading (not the paper title; e.g., `### Single-step sign attack`, not `### FGSM (Goodfellow et al., 2014)`)
   - Briefly state what the paper contributed (1-3 sentences)
   - Include the method, key formulas, and 1 worked example or pseudo-code where it adds value
   - **Cite the paper inline as `[N]`** the first time and subsequent times
   - DO NOT duplicate full content. Be tight; preserve the textbook flow of the host page.
4. **Delete** the paper-named page after merging.
5. Append/maintain a **References** section at the END of each foundation page that received merged content:

   ```
   ## References

   [1] I. J. Goodfellow, J. Shlens, C. Szegedy. *Explaining and Harnessing Adversarial Examples*. ICLR 2015.
   [2] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, A. Vladu. *Towards Deep Learning Models Resistant to Adversarial Attacks*. ICLR 2018.
   ```

   Number references in order of first appearance within the page. Each foundation page maintains its own independent numbering.

### Update `intro.md`

The existing `intro.md` may have a "## Deep-dive papers" section listing the paper-named pages. **Remove** that section (papers are now inline in foundation pages). Preserve the rest of `intro.md`.

### What to preserve

- Existing foundation pages: keep their structure and existing content. Add merged paper material **into** them — don't replace.
- Mermaid diagrams, worked examples, code snippets in foundation pages — keep them.
- `_category_.json` — DO NOT modify.

### What to delete

- Every paper-named page in the section, after merging.

### Quality bar

- The resulting foundation pages must read as **textbook chapters with cited papers**, not as paper-by-paper deep dives.
- No paper-named filename should survive.
- Inline citations should be `[N]` with the References list at page bottom.
- Author/year mentions in prose are OK ("Goodfellow et al. [1] introduced…") but the section heading must be topical.

### Format reminders

- Depth addendum applies (Mermaid where useful, KaTeX math, common pitfalls, cross-links).
- After merging, the host foundation page may grow to 4000-6000 words — that's fine, it's a textbook chapter now.
- Cross-doc links use absolute paths.

---

The section-specific instructions follow below. Apply this policy to that section.

---

