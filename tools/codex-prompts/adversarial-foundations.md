You are an autonomous content author for **SJ Wiki**. Generate **foundational** Markdown notes for the Adversarial Attacks subtopic.

## Inputs

- **SOURCE_PDFs**: NONE for this run. There is no textbook in tmp/ yet. The user is collecting papers in parallel. **You must write from general knowledge of the field** — adversarial robustness is a well-established area with stable definitions, threat models, canonical algorithms, and standard defenses.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/`

## What to produce

A **foundational page set** that gives the wiki reader the vocabulary, formulations, and canonical algorithms of adversarial ML. Specific papers (FGSM/PGD/C&W/randomized smoothing/jailbreaks) will be deep-dived as separate pages in a later batch — your job is the conceptual scaffolding.

The existing `intro.md` already exists as a stub. **Rewrite it** with a real overview + full numbered page list.

### Pages to create (suggested 9-12 pages)

| Position | Filename | Topic |
|---:|---|---|
| 1 | `intro.md` (rewrite) | Hub: definitions, scope, threat models overview, page list |
| 2 | `threat-models-and-attack-taxonomy.md` | White/grey/black-box, targeted/untargeted, norm balls, query budgets, transferability, attacker knowledge |
| 3 | `mathematical-formulation.md` | Adversarial example as constrained optimization; min-max / Lagrangian formulations; perturbation budget $\epsilon$; loss surfaces |
| 4 | `white-box-attacks.md` | FGSM, BIM/I-FGSM, PGD, MIM, C&W, DeepFool — algorithms, gradients, pseudocode, complexity, when to use each |
| 5 | `black-box-and-transfer-attacks.md` | Transfer-based (no queries), query-based (ZOO, NES, SPSA, square attack), substitute models, surrogate gradients |
| 6 | `physical-world-and-patch-attacks.md` | Real-world robustness: stop signs (Eykholt et al.), patches, eyeglasses, audio, 3D printed objects, expectation over transformations |
| 7 | `adversarial-training.md` | Min-max training, Madry-style PGD-AT, TRADES, free / fast AT, robust overfitting, computational cost |
| 8 | `certified-defenses-and-randomized-smoothing.md` | What "certified" means; randomized smoothing (Cohen et al.); interval bound propagation; CROWN; convex relaxations |
| 9 | `gradient-masking-and-obfuscation.md` | Why broken defenses look strong: gradient masking, obfuscated gradients (Athalye et al.); evaluation pitfalls |
| 10 | `evaluation-and-benchmarks.md` | RobustBench, AutoAttack, adaptive attacks, common methodological errors, FAQ-style "is this defense real?" |
| 11 | `robustness-accuracy-tradeoff.md` | Why robust models lose clean accuracy; theoretical analyses; data scaling laws under robust loss |
| 12 | `attacks-on-llms-and-other-modalities.md` | Beyond image classifiers: text adversarial (TextFooler, HotFlip), audio, RL policies, LLM jailbreaks and prompt injection (overview only — specific papers later) |

If you prefer fewer pages, group adjacent topics, but cover the same conceptual territory.

## Per-page format (depth addendum applies)

- Frontmatter: `title:`, `sidebar_position:` (per table above)
- 1-paragraph elevator pitch
- **Definitions** — formal where they exist (e.g., adversarial example: $x' = x + \delta$ with $\|\delta\|_p \le \epsilon$ such that $f(x') \ne f(x)$ or $f(x') = y_t$)
- **Key results / formulas** — with KaTeX math
- **Visual** (mandatory) — Mermaid diagram, threat-model decision tree, or comparison table
- **Worked example** — at least one concrete example (e.g., trace one FGSM step on MNIST; compute $\epsilon$ for $\ell_\infty$ vs $\ell_2$ on the same image)
- **PyTorch sketch** — minimal `torch` snippet illustrating the attack/defense (e.g., FGSM in 5 lines, PGD in ~15)
- **Common pitfalls** — gradient masking signs, evaluation errors, threat-model confusion
- **Connections** — cross-links to other foundational pages + existing wiki pages (`/cs/deep-learning/`, `/cs/machine-learning/`, `/cs/cryptography/`)
- **Further reading** — name the canonical paper for the topic (e.g., "Goodfellow et al. 2014" for FGSM) without writing a full paper deep dive — those come later as separate pages

## Critical guidelines

- **Be honest about scope**: this is a foundational layer. Don't claim to deep-dive specific papers; mark those as forthcoming.
- **Use stable, peer-reviewed definitions**. Threat models from Biggio & Roli's "Wild Patterns" survey are widely cited; cite them where natural.
- **Stay current to ~2023-2024 understanding** of the field. Mention LLM jailbreaks, multimodal attacks, alignment-adjacent concerns at the level a 2024 graduate-level course would.
- **Math precision**: use $\ell_p$ norms consistently, define $\epsilon$, distinguish targeted ($y_t$) vs untargeted, use $\nabla_x \mathcal{L}$ for the loss gradient.
- **Code precision**: PyTorch snippets must be syntactically correct; use `torch.clamp` for projection, `torch.sign` for FGSM, `loss.backward()` and `x.grad.data` correctly.

## Workflow

1. List the OUTPUT_DIR (`ls`) and read the existing `intro.md` so you know the stated scope.
2. Plan the 9-12 pages (see table).
3. Write each detail page (positions 2-12).
4. Rewrite `intro.md` last with a numbered list of every page you produced.
5. Print a summary listing all files.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/`.
- Do not modify `_category_.json`, config files, `sidebars.ts`, `package.json`, or files outside OUTPUT_DIR.
- No `npm`. English. Mathematically and conceptually precise. Don't fabricate paper results — at this stage you are giving CONCEPTUAL coverage; specific paper numbers and tables come in later deep-dive pages.
- KaTeX-compatible math (`$..$`, `$$..$$`, `$$\begin{aligned}…\end{aligned}$$`).
- Mermaid for visuals.
- Cross-doc links use absolute paths (`/cs/deep-learning/...`).

Begin now.
