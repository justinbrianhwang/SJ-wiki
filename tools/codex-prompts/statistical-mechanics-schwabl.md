You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/통계역학.pdf` (Franz Schwabl — *Statistical Mechanics*, 2nd ed, Springer; translated by William Brewer)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/statistical-mechanics/`
- **SUBJECT**: Statistical Mechanics (graduate level, Schwabl)

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview + numbered list of all pages.

2. **18-25 detail pages** covering Schwabl's full scope:
   - Foundations: probability theory in statistical mechanics, ensembles, Liouville theorem, ergodic hypothesis
   - Equilibrium ensembles: microcanonical, canonical, grand canonical (derivations, partition functions, fluctuations)
   - Ideal gases: classical, density of states, Maxwell-Boltzmann velocity distribution, equipartition
   - Quantum statistics: identical particles, Fermi-Dirac, Bose-Einstein distributions
   - Ideal Fermi gas: degenerate fermions, Fermi energy, Sommerfeld expansion, applications (electrons in metals, white dwarfs)
   - Ideal Bose gas: photon gas, blackbody radiation, Bose-Einstein condensation, phonons, Debye model
   - Real gases: virial expansion, van der Waals, cluster expansions
   - Phase transitions (general framework): order parameters, broken symmetry, classification (Ehrenfest), Ising-style argument
   - Mean-field theory: Curie-Weiss, Landau theory, critical exponents (mean-field values)
   - Beyond mean-field: scaling, universality, renormalization group intro, critical exponents from RG
   - Ising and related models: 1D exact, 2D Onsager mention, Monte Carlo intro
   - Lattice gases, binary alloys, mean-field magnetism
   - Brownian motion and stochastic dynamics: Langevin, Fokker-Planck, master equations
   - Linear response and fluctuation-dissipation theorem
   - Boltzmann equation and transport (relaxation time approximation, conductivity, viscosity)
   - Irreversibility and the H-theorem
   - Nonequilibrium thermodynamics (entropy production, Onsager reciprocity)
   - Connection to quantum field theory (path integrals as imaginary-time, Matsubara frequencies — brief)

3. Per-page format follows the depth addendum (1500-3500 words; mandatory Mermaid diagram OR comparison table OR ASCII figure; ≥2 worked examples; common pitfalls; Python snippets where useful for distributions / Monte Carlo / RG flows).

4. **Math precision** — Schwabl is rigorous. Use proper KaTeX:
   - $Z = \mathrm{Tr}\,e^{-\beta H}$
   - $f_{\mathrm{FD}} = 1/(e^{\beta(\epsilon-\mu)}+1)$, $f_{\mathrm{BE}} = 1/(e^{\beta(\epsilon-\mu)}-1)$
   - $\langle (\Delta E)^2\rangle = k_B T^2 C_V$
   - Boltzmann equation: $\partial_t f + v\cdot\nabla_x f + F\cdot\nabla_p f = (\partial_t f)_{\mathrm{coll}}$

5. **Visual**:
   - Phase diagrams (with critical point, triple point, coexistence curves)
   - Distribution plots (Maxwell-Boltzmann, FD, BE)
   - Critical exponent tables for different universality classes
   - RG flow diagrams

6. Cross-link to:
   - `/physics/thermodynamics/` (macroscopic counterpart)
   - `/physics/quantum-mechanics/` (identical particles, second quantization)
   - `/physics/quantum-field-theory/` (path integral, finite-temperature QFT)
   - `/math/probability-and-random-variables/` (stochastic processes background)

## Workflow

1. `pdfinfo` for page count.
2. `pdftotext -l 30` for cover + TOC.
3. Iterate chapters; 1-2 wiki pages each.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/physics/statistical-mechanics/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Match the depth addendum.
- Mermaid: special chars wrapped in `"..."`, internal `"` → `#quot;`.
- For images, use `https://commons.wikimedia.org/wiki/Special:FilePath/<filename>` form only.
- Don't fabricate beyond Schwabl's content.

Begin now.
