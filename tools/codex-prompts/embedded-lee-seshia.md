You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/LeeSeshia_DigitalV2_2.pdf` (Edward A. Lee & Sanjit A. Seshia — *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*, 2nd ed, MIT Press 2017)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/embedded/`
- **SUBJECT**: Embedded Systems — cyber-physical systems perspective (supplementary)

## Existing content note

The `embedded/` folder already contains pages based on **Godse & Godse**'s *Microprocessors & Microcontroller Systems* — those pages cover 8085, 8051, 8255, AVR, PIC, and hardware interfacing. **Do not delete, modify, or duplicate** those pages. The Godse coverage is hardware-and-assembly-oriented; Lee & Seshia is system-modeling-and-analysis-oriented. The two are complementary.

**Existing Godse pages** (do NOT overwrite — list them by reading the directory):

```bash
ls "f:/coding/SJ Wiki/docs/cs/embedded/"
```

Add your new pages with **distinct, non-colliding filenames**. Recommended naming prefix or grouping (your choice — keep names self-explanatory):
- `cps-introduction.md`
- `continuous-dynamics.md`
- `discrete-dynamics.md`
- `hybrid-systems.md`
- `composition-of-state-machines.md`
- `concurrent-models-of-computation.md`
- `embedded-processors-architecture.md`
- `memory-architectures.md`
- `input-output-interfacing.md`
- `sensors-and-actuators.md`
- `multitasking-and-threads.md`
- `scheduling-and-real-time.md`
- `invariants-and-temporal-logic.md`
- `equivalence-and-refinement.md`
- `reachability-and-model-checking.md`
- `quantitative-analysis.md`
- `security-and-privacy.md`

Use `sidebar_position` values in the range **50-70** so your pages sort AFTER the Godse pages (which use 2-14). The first new page should have `sidebar_position: 50`, the next 51, etc.

## Produce

1. **`intro.md`** — **DO NOT REPLACE**. The existing `intro.md` is for the Godse-sourced material. **Append** a new section to it (or create `intro-cps.md` if you prefer) that mentions the Lee & Seshia supplementary coverage with a numbered list of the new pages.

   Actually — **safer alternative**: leave `intro.md` alone, and create `intro-cyber-physical-systems.md` (with `sidebar_position: 50`) that serves as a sub-hub for your new content.

2. **14-18 detail pages** covering Lee & Seshia's full scope (the topics listed above). Each page should follow the depth addendum (1500-3500 words, mandatory Mermaid diagram OR comparison table OR ASCII figure, ≥2 worked examples with full steps, common pitfalls, runnable Python or pseudocode where useful).

3. **Math notation** — Lee & Seshia uses continuous-time dynamics (ODEs), discrete-time systems, state machines, finite automata, temporal logic (LTL, CTL), and timing analysis. Use KaTeX for math. Use Mermaid `stateDiagram-v2` for FSMs and `flowchart` for hybrid systems.

4. Cross-link to:
   - existing `cs/embedded/` Godse pages where the topics relate
   - `/cs/theory/finite-automata-and-dfas` (FSMs)
   - `/cs/theory/turing-machines-and-the-church-turing-thesis` (computation models)
   - `/cs/operating-systems/cpu-scheduling` (real-time scheduling overlap)
   - `/cs/operating-systems/process-synchronization` (concurrency)
   - `/physics/signals-systems/` (signals view)
   - `/physics/simulation/` (continuous-time simulation)
   - `/math/engineering-math/first-order-odes` and `/math/engineering-math/laplace-transform` (continuous dynamics)

## Workflow

1. `pdfinfo "<pdf>"`, `pdftotext -l 30 "<pdf>" -` for cover + TOC + preface.
2. `ls "f:/coding/SJ Wiki/docs/cs/embedded/"` to see existing filenames — make sure your new names don't collide.
3. For each new topic, read its source pages with `pdftotext -f X -l Y` and write a wiki page.
4. Write `intro-cyber-physical-systems.md` last with links to all new pages you created.
5. Print summary listing all new files (only new ones — confirm you did not touch existing files).

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/embedded/`.
- **Do NOT modify or delete existing Godse pages.** Verify by listing the directory before and after — the old file count should still be present.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Match the depth addendum.
- Don't fabricate beyond Lee & Seshia's content.

Begin now.
