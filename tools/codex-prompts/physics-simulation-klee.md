You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/326.pdf` (Klee & Allen — *Simulation of Dynamic Systems with MATLAB & Simulink*, 2nd ed)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/simulation/`
- **SUBJECT**: Simulation of Dynamic Systems with MATLAB & Simulink

## Produce

1. **`intro.md`** — overview + chapter list.

2. **10-15 detail pages** covering:
   - Mathematical modeling of continuous-time dynamical systems
   - State-space representation
   - Numerical integration methods (Euler, RK4, adaptive) for simulation
   - Step size, accuracy, stability
   - Linear systems (transfer functions, modes, time/freq response) — cross-link to `/physics/signals-systems/`
   - Nonlinear systems and linearization
   - MATLAB scripting for simulation
   - Simulink block diagrams
   - Discrete-time models and sampled-data systems
   - Hybrid systems (continuous + discrete events)
   - Examples: mechanical, electrical, thermal, chemical, biological systems
   - Validation and verification of simulations

3. Per-page: model derivation → MATLAB code (`matlab` blocks) and Simulink description → time-response plot description → discussion.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 20` for TOC. 3. Iterate. 4. `intro.md` last.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
