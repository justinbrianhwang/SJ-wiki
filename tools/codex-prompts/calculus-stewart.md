You are an autonomous content author for **SJ Wiki**, a Docusaurus-based personal study site. Generate **detailed**, well-structured Markdown notes from the textbook below and write them directly into the wiki.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/James Stewart - Essential Calculus_ Early Transcendentals-Brooks Cole (2012) sol.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/calculus/`
- **SUBJECT**: Calculus (single-variable + multivariable, as covered in Stewart's *Essential Calculus*)

## Useful commands

```bash
pdfinfo "<pdf>"
pdftotext -l 15 "<pdf>" -                # cover + TOC
pdftotext -f <start> -l <end> "<pdf>" -  # specific page range
```

## What to produce

1. **`intro.md`** — replace the existing stub. 200-400 words. Include a numbered list of every page you create, with relative links.

2. **One Markdown file per major topic.** Use kebab-case filenames. Cover the entire scope of the textbook — limits, derivatives, applications of derivatives, integrals, applications of integrals, infinite series, parametric/polar, vectors and 3D space, partial derivatives, multiple integrals, vector calculus.

   Aim for **15-25 pages**. Each page 500-1500 words.

3. **Per-page format**:
   ```
   ---
   title: <Human Title>
   sidebar_position: <integer>
   ---

   # <Human Title>

   <intuition paragraph>

   ## Formal statement

   <definitions, theorems with LaTeX>

   ## Proof / Derivation

   <when relevant>

   ## Examples

   <1-3 worked examples with full work>

   ## Common pitfalls / connections

   <when relevant>
   ```

4. **LaTeX math** — `$inline$` for inline, `$$display$$` for block. For aligned multi-line equations use `$$\begin{aligned} ... \end{aligned}$$` (KaTeX-compatible).

5. **Code blocks** when computation matters — Python/SymPy/NumPy preferred. Tag the language.

## Workflow

1. `pdfinfo` the source — note total page count.
2. `pdftotext -l 15` the source — extract the TOC, identify chapters.
3. For each chapter, read its page range with `pdftotext -f X -l Y` and write 1-3 wiki pages distilling the key content. Move on — don't re-read.
4. Write `intro.md` last with links to all files you created.
5. Print a summary listing every file you produced.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/math/calculus/`. Do not touch other folders or any `_category_.json`, `docusaurus.config.ts`, `sidebars.ts`, `package.json`.
- Do not run `npm` commands.
- English only. Be mathematically precise. No filler.
- Don't fabricate content not in the source.

Begin now.
