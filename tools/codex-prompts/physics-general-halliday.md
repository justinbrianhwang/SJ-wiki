You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/David Halliday_ Robert Resnick_ Jearl Walker - Fundamentals of physics-Wiley  (2011).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/general/intro` directory
- **SUBJECT**: General Physics (Halliday, Resnick, Walker — *Fundamentals of Physics*)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **20-30 detail pages** covering HRW's scope:
   - Measurement, units, vectors
   - Kinematics 1D & 2D (projectile, circular motion)
   - Newton's laws, applications of Newton's laws (friction, drag)
   - Work, energy, conservation of energy
   - Linear momentum, collisions
   - Rotation (kinematics, dynamics, torque, angular momentum)
   - Equilibrium and elasticity
   - Gravitation (Kepler, Newton)
   - Fluids (statics, dynamics, Bernoulli)
   - Oscillations (SHM, damped, driven, resonance)
   - Waves (mechanical, sound, standing waves, Doppler)
   - Temperature & heat, kinetic theory of gases
   - First law of thermodynamics, entropy, second law
   - Coulomb's law, electric field
   - Gauss's law
   - Electric potential
   - Capacitance, current, resistance, DC circuits
   - Magnetic fields and forces
   - Ampere's law, induction (Faraday/Lenz), inductance
   - AC circuits and EM waves
   - Reflection, refraction, geometric optics
   - Interference & diffraction (Young, single slit, diffraction grating)
   - Relativity intro
   - Quantum intro (photons, matter waves)

3. Per-page: physical intuition → equations with LaTeX → worked numerical example → tips/pitfalls.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 35` for TOC. 3. Iterate chapters; 1-2 pages each. 4. `intro.md` last. 5. Print summary.

## Output dir
Write files to `f:/coding/SJ Wiki/docs/physics/general/`.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
