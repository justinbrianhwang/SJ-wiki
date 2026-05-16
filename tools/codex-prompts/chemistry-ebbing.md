You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/General_Chemistry_9th_Edition_Ebbing_Gammon.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/chemistry/general/`
- **SUBJECT**: General Chemistry (Ebbing & Gammon — *General Chemistry*, 9th ed)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **20-28 detail pages** covering Ebbing's full scope:
   - Chemistry overview, scientific method, units, measurement
   - Atoms, molecules, ions (atomic theory, nuclear atom, periodic table intro)
   - Stoichiometry (moles, balanced equations, limiting reagent, percent yield)
   - Reactions in aqueous solution (precipitation, acid-base, redox; molarity)
   - Gases (ideal gas law, Dalton, kinetic theory, real gases)
   - Thermochemistry (heat, enthalpy, Hess's law, calorimetry)
   - Quantum theory of atoms (Bohr → quantum, orbitals, electron configurations)
   - Electron configurations & periodic trends
   - Ionic & covalent bonding (Lewis structures, electronegativity)
   - Molecular geometry (VSEPR, hybridization, MO theory)
   - States of matter (liquids, solids, phase diagrams, intermolecular forces)
   - Solutions (concentration, colligative properties, solubility)
   - Chemical kinetics (rate laws, integrated rate laws, mechanisms, catalysis, Arrhenius)
   - Chemical equilibrium ($K_c$, $K_p$, Le Châtelier, ICE tables)
   - Acid-base equilibria (Brønsted, $K_a$, $K_b$, pH, buffers, titration)
   - Solubility & complex-ion equilibria
   - Thermodynamics (entropy, Gibbs, $\Delta G$, free energy & equilibrium)
   - Electrochemistry (galvanic cells, $E°$, Nernst, electrolysis)
   - Nuclear chemistry (radioactivity, fission/fusion)
   - Coordination compounds + transition metals (brief)
   - Organic chemistry intro (functional groups, isomerism)
   - Biochemistry intro (carbs, lipids, proteins, nucleic acids)

3. Per-page: concept → equations/diagrams → worked example with numbers → common pitfalls.

4. Use LaTeX for equations and reactions, e.g. `$$\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$$`.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 35` for TOC. 3. Iterate chapters; 1-2 pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
