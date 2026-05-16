You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Statics and Dynamics.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/mechanics/`
- **SUBJECT**: Engineering Mechanics — Statics & Dynamics

## Produce

1. **`intro.md`** — overview + chapter list.

2. **12-20 detail pages** covering:
   - Force vectors, resultants, components
   - Particle equilibrium (2D, 3D)
   - Rigid-body equilibrium (FBD, moments, support reactions)
   - Trusses (method of joints, method of sections), frames, machines
   - Internal forces in beams, shear & bending moment diagrams
   - Friction (dry, belt, screws)
   - Centroids, moments of inertia, second moments
   - Kinematics of particles (rectilinear, curvilinear, n-t coords, cylindrical)
   - Kinetics: Newton's second law for particles
   - Work-energy methods (work, kinetic energy, potential energy)
   - Impulse & momentum (linear, angular, impact)
   - Planar kinematics of rigid bodies (rotation, relative motion)
   - Planar kinetics of rigid bodies
   - Vibrations (free, damped, forced — single DOF)

3. Per-page: setup with FBD/diagram (Mermaid where simple) → equilibrium/EOM equations → worked example with numbers.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` for TOC. 3. Iterate. 4. `intro.md` last.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
