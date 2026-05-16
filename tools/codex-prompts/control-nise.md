You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/norman nise.pdf` (Norman S. Nise — *Control Systems Engineering*, 7th ed, Wiley)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/control-engineering/`
- **SUBJECT**: Control Systems Engineering

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview + numbered list of all pages.

2. **18-25 detail pages** covering Nise's full scope (text follows the standard undergraduate sequence):

   **Modeling and analysis**
   - Introduction to control systems (open-loop vs closed-loop, configurations, design objectives)
   - Modeling in the frequency domain (Laplace transform refresher, transfer functions of electrical / mechanical / electromechanical systems, linearization)
   - Modeling in the time domain (state-space representation, conversion between TF and state-space, similarity transformations)
   - Time response (poles, zeros, first-order responses, second-order responses — overdamped / underdamped / undamped / critically damped, transient specs, time-domain spec parameters)
   - Reduction of multiple subsystems (block diagrams: series / parallel / feedback, Mason's gain formula, signal-flow graphs)

   **Stability**
   - Stability (BIBO, Routh-Hurwitz criterion, stability margins, special cases)
   - Steady-state errors (system type, static error constants, error specs)

   **Classical design**
   - Root locus techniques (sketching rules, design via root locus, cascade compensation, PI / PD / PID, lag / lead / lag-lead)
   - Frequency response (Bode plots, Nyquist criterion, gain/phase margins, design via frequency response)

   **State-space design**
   - Design via state-space (controllability, observability, pole placement, ackermann, observer/estimator design, integral control, LQR overview)

   **Digital control**
   - Digital control systems (Z-transform, sampling, stability in z-plane, digital compensator design, mapping between s and z)

   **Nonlinear / advanced**
   - Nonlinear control basics (describing functions, phase plane, Lyapunov stability — Nise's treatment is light here; respect that scope)

3. Per-page format follows the depth addendum (1500-3500 words; mandatory Mermaid block diagram OR comparison table OR ASCII figure; ≥2 worked numerical examples with full algebra; common pitfalls; Python (NumPy / SciPy / `python-control` library) code where useful).

4. **Math precision** — KaTeX:
   - Laplace: $X(s) = \int_0^\infty x(t) e^{-st}\,dt$
   - Transfer function: $G(s) = N(s)/D(s)$, pole-zero
   - Standard 2nd-order: $G(s) = \omega_n^2/(s^2 + 2\zeta\omega_n s + \omega_n^2)$
   - State-space: $\dot{\mathbf x} = A\mathbf x + B u$, $y = C\mathbf x + D u$
   - Routh array layout (use markdown table)
   - z-transform: $X(z) = \sum_{n=0}^\infty x[n] z^{-n}$
   - Bode magnitude/phase

5. **Visual** — heavy use of:
   - Mermaid block diagrams (`flowchart LR` with `R[+] --> Σ --> G --> Y; H --> Σ`)
   - Root-locus rule tables
   - s-plane / z-plane sketches (ASCII or Mermaid)
   - Bode-style asymptote tables

6. Cross-link to:
   - `/math/engineering-math/laplace-transform` and `/math/engineering-math/complex-functions-and-analyticity` (transforms, RHP)
   - `/physics/signals-systems/` (Oppenheim, related but different framing)
   - `/physics/simulation/` (Klee/Allen — Simulink-based simulation)
   - `/cs/autonomous-driving/control-pid-mpc-pure-pursuit-stanley` (applied vehicle control)
   - `/cs/embedded/` (digital controller implementation on microcontrollers)

## Workflow

1. `pdfinfo "<pdf>"` and `pdftotext -l 30 "<pdf>" -` for cover + TOC.
2. For each chapter, read the relevant page range with `pdftotext -f X -l Y "<pdf>" -` and write 1-2 wiki pages distilling the key content.
3. Write `intro.md` last.
4. Print summary listing all files.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/control-engineering/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Match the depth addendum.
- Mermaid labels with special characters (`(`, `)`, `=`, `?`, `:`, `'`, `,`, `|`, `"`, `{`, `}`) must be wrapped in `"..."`; internal `"` → `#quot;`.
- Don't fabricate beyond Nise's content.

Begin now.
