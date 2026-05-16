You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from **four complementary quantum mechanics textbooks**.

## Inputs

- **SOURCE_PDFs** (four, all on the same subject — combine):
  - `f:/coding/SJ Wiki/tmp/Modern Quantum Mechanics_Sakurai.pdf` — **PRIMARY**
  - `f:/coding/SJ Wiki/tmp/Ballentine - Quantum Mechanics.pdf` (rigorous, ensemble interpretation)
  - `f:/coding/SJ Wiki/tmp/Gottfried_Quantum Mechanics.pdf` (mathematically deep)
  - `f:/coding/SJ Wiki/tmp/Schiff-QuantumMechanics.pdf` (classic, older notation)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/quantum-mechanics/`
- **SUBJECT**: Quantum Mechanics — combined from four sources

## How to combine

- Use **Sakurai** as the **primary structure** — modern, Dirac-notation-first.
- Cite alternative treatments from Ballentine, Gottfried, Schiff where they offer cleaner proofs, different interpretations, or extra examples.
- Each page should note which book(s) the section draws from and where they diverge in conceptual or notational choices.
- Do **not** make four parallel directories; merge into one set of topic pages.

## Produce

1. **`intro.md`** — overview + chapter list + note explaining the four-book synthesis.

2. **18-26 detail pages** covering:
   - Postulates of QM (states, observables, measurement, time evolution)
   - Dirac notation and Hilbert spaces
   - Spin-1/2 systems (Stern-Gerlach, Pauli matrices)
   - Quantum dynamics (Schrödinger vs Heisenberg picture, interaction picture)
   - Simple 1D systems (free particle, infinite well, finite well, harmonic oscillator with ladder ops)
   - Angular momentum (general theory, eigenstates, addition, Clebsch-Gordan)
   - Hydrogen atom
   - Identical particles (symmetrization, Pauli principle, fermions/bosons)
   - Approximation methods (time-independent perturbation, Stark, Zeeman)
   - Time-dependent perturbation theory (Fermi's golden rule)
   - Variational principle and WKB
   - Scattering theory (cross section, Born approximation, partial waves)
   - Density operator, mixed states, entanglement, decoherence (brief)
   - Path integral formulation (sketch — Feynman)
   - Measurement and interpretation (Copenhagen vs many-worlds vs ensemble, briefly)
   - Symmetries and conservation laws

3. Per-page: physical motivation → formalism (Dirac notation) → key formulas → worked example → comparison note across books where relevant.

## Workflow

1. `pdfinfo` all four. 2. `pdftotext -l 20` of each for TOC. 3. Build merged outline. 4. For each topic, read relevant chapters from Sakurai (primary) and cross-check 1-2 of the others. 5. `intro.md` last. 6. Print summary.

This is a big job — you do not need to read each book end-to-end. Focus on the chapters/sections covering the chosen topics.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Mathematically precise. Don't fabricate.

Begin now.
