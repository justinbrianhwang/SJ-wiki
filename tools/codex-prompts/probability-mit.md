You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for the probability section using **MIT 18.440 Probability and Random Variables** lecture notes.

## Inputs

- **SOURCE_FOLDER**: `f:/coding/SJ Wiki/tmp/tandom variable/` (33 MIT 18.440 lecture PDFs, Scott Sheffield, Spring 2014). The filenames hash-prefix the lecture number, e.g. `..._MIT18_440S14_LectureN.pdf` for N = 1..36 (some numbers missing).
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/math/probability-and-random-variables/`
- **SUBJECT**: Probability and Random Variables — MIT 18.440 scope

## Useful commands

```bash
# Survey all lectures: get title pages
for f in "f:/coding/SJ Wiki/tmp/tandom variable/"*.pdf; do
  echo "=== $f ==="
  pdftotext -l 2 "$f" -
done

# Read a specific lecture
pdftotext "f:/coding/SJ Wiki/tmp/tandom variable/<filename>.pdf" -
```

## Workflow

1. **Survey phase**: extract first 1-2 pages of each lecture (use bash loop). Build a map: `LectureN → topic`. Sort by lecture number — the filenames are content-hashed so you must read them to learn the order.

2. **Outline phase**: group lectures into 15-22 wiki pages. The MIT 18.440 syllabus typically covers:
   - Counting, combinatorics, basic axioms
   - Conditional probability, independence, Bayes
   - Discrete random variables (Bernoulli, Binomial, Geometric, Poisson, Negative binomial, Hypergeometric)
   - Continuous random variables (Uniform, Exponential, Normal, Gamma, Beta, Cauchy)
   - Joint distributions, marginals, conditional distributions
   - Independence and uncorrelatedness
   - Expectation, variance, covariance, correlation
   - Moment generating functions, characteristic functions
   - Transformations / change of variables
   - Sums of random variables, convolutions
   - Law of Large Numbers (weak / strong)
   - Central Limit Theorem
   - Markov inequalities, Chebyshev, Chernoff bounds
   - Markov chains (intro)
   - Entropy / information theory basics (if covered)
   - Brownian motion / random walks (if covered in late lectures)
   - Martingales (if covered)

3. **Write phase**: for each wiki topic, read the relevant lecture PDF(s) and write a wiki page. Multiple lectures may feed one page; one lecture may split across two pages.

4. **Wrap-up**: write `intro.md` last with a numbered list of all pages and a short note that the section follows MIT 18.440 (Sheffield, Spring 2014) lecture notes. Print a final summary of files created.

## Format requirements

(Inherited from the depth addendum — 1500-3500 words, mandatory Mermaid diagram or comparison table, ≥2 worked examples with full steps, common pitfalls, runnable Python where useful.)

Per-page sections in this order:
- Frontmatter (`title:`, `sidebar_position:` — use the lecture order for `sidebar_position`)
- Heading
- 1-2 paragraph intuition
- Definitions
- Key results (with proofs or proof sketches)
- Visual (Mermaid diagram, comparison table, or ASCII figure — MANDATORY)
- Worked example 1
- Worked example 2
- Code (Python with `numpy` / `scipy.stats` where appropriate)
- Common pitfalls
- Connections (cross-links to other wiki pages — use absolute paths)

## Cross-references

- This is a **rigorous, theory-oriented** treatment of probability.
- The sibling `/math/probability/` section is a shorter introduction sourced from Lane et al.'s online statistics textbook. Link rather than duplicate when natural.
- `/math/statistics/` covers data analysis, inference, regression — link for applied statistics.
- `/math/discrete/discrete-probability` covers discrete-probability basics from Rosen.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/math/probability-and-random-variables/`.
- Do not modify `_category_.json`, config files, `sidebars.ts`, `package.json`, or files outside OUTPUT_DIR.
- Do not run `npm`.
- English. Mathematically precise. KaTeX-compatible math (`$..$`, `$$..$$`, `$$\begin{aligned}...\end{aligned}$$`).
- Mermaid labels with special characters (`(`, `)`, `=`, `?`, `:`, `'`, `,`, `|`, `"`) must be wrapped in double quotes — internal `"` should be `#quot;`.
- Don't fabricate content beyond what the MIT lectures cover. Sheffield is rigorous; respect the level.

Begin now.
