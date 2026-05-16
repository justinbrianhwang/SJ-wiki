You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/1621583343.pdf` (*Atkins' Physical Chemistry* — Peter Atkins, Julio de Paula; identify the exact edition from cover/preface)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/chemistry/physical-chemistry/`
- **SUBJECT**: Physical Chemistry

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview, identify the edition you read, numbered list of all pages.

2. **18-26 detail pages** covering Atkins' full scope. Typical organization:
   - **Thermodynamics**
     - Properties of gases (perfect gas, real gases, virial equation, van der Waals, critical phenomena)
     - First law of thermodynamics (work, heat, enthalpy, $C_p$/$C_V$, adiabatic processes, thermochemistry, Hess's law, Kirchhoff's law)
     - Second law and entropy (Carnot cycle, Clausius inequality, entropy changes, statistical interpretation)
     - Free energy (Helmholtz $A$, Gibbs $G$; $\Delta G^\circ$ and equilibrium; Maxwell relations; chemical potential)
     - Phase diagrams and phase transitions (Clapeyron, Clausius-Clapeyron; phase rule; binary and ternary mixtures)
     - Mixtures and solutions (partial molar quantities; Raoult's law; Henry's law; activity; ideal vs real solutions; colligative properties)
     - Chemical equilibrium (extent of reaction, equilibrium constant, response to conditions, activity)
     - Electrochemistry (electrolyte thermodynamics; ion activity; Debye-Hückel; cells; Nernst equation; standard potentials)
   - **Statistical thermodynamics**
     - Boltzmann distribution and the molecular partition function
     - Translational, rotational, vibrational, electronic partition functions
     - Statistical thermodynamics of ensembles and ideal gases
     - Connection to thermodynamic functions (U, H, S, A, G)
   - **Quantum chemistry**
     - Foundations: wave-particle duality, Schrödinger equation, postulates
     - Translational, rotational, and vibrational motion
     - Atomic structure (hydrogen, multi-electron atoms, term symbols, periodic trends)
     - Molecular structure (Born-Oppenheimer, VB, MO, HF, computational quantum chemistry overview)
     - Group theory and molecular symmetry (point groups, character tables)
   - **Spectroscopy**
     - Rotational, vibrational, vibrational-rotational, Raman, electronic spectra
     - Laser action, NMR, EPR (brief)
   - **Kinetics and dynamics**
     - Rate laws (orders, integrated rate laws)
     - Reaction mechanisms (elementary steps, steady state, pre-equilibrium)
     - Temperature dependence (Arrhenius, transition-state theory)
     - Reaction dynamics (collision theory, RRKM — brief)
     - Catalysis (homogeneous, heterogeneous, enzyme kinetics — Michaelis-Menten)
   - **Macromolecules and condensed matter** (selected highlights as Atkins covers them)

3. Per-page format (per addendum): 1500-3500 words, mandatory Mermaid diagram OR comparison table OR ASCII figure, ≥2 worked examples with full numerical steps, common pitfalls, runnable Python (NumPy / SciPy where useful, e.g. fitting rate data, plotting partition functions).

4. **KaTeX math** — heavy use. Chemistry-style reactions in `\mathrm{}`: `$$\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$$`. Thermodynamic state functions, derivatives, and Maxwell relations. Quantum operators with Dirac notation.

5. Cross-link to:
   - `/chemistry/general/` (Ebbing for intro-level overlap)
   - `/physics/quantum-mechanics/` (deeper QM)
   - `/physics/general/` (basic thermodynamics)
   - `/math/engineering-math/` (PDEs for Schrödinger equation; complex analysis for spectroscopy)
   - `/math/calculus/multiple-integrals` (statistical thermodynamics integrals)

## Workflow

1. `pdfinfo "<pdf>"` for page count.
2. `pdftotext -l 30 "<pdf>" -` for cover + TOC + preface; identify edition.
3. For each chapter, read its page range with `pdftotext -f X -l Y` and write 1-2 wiki pages.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/chemistry/physical-chemistry/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically and chemically precise. Match the depth addendum.
- Don't fabricate beyond what Atkins covers.

Begin now.
