You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/EM1-book-(7th-ed).pdf` (Fawwaz T. Ulaby & Umberto Ravaioli — *Fundamentals of Applied Electromagnetics*, 7th ed, Pearson)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/electromagnetics/`
- **SUBJECT**: Applied Electromagnetics

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview + numbered list of pages.

2. **15-22 detail pages** covering Ulaby's full scope. Typical organization:
   - Introduction: waves, EM spectrum, complex numbers and phasors, units, vectors review
   - Vector analysis (gradient, divergence, curl; cartesian / cylindrical / spherical; line/surface/volume integrals; divergence theorem; Stokes' theorem)
   - Transmission lines (lumped vs distributed model, telegraph equations, characteristic impedance, reflection, Smith chart, impedance matching)
   - Vector analysis applied to electrostatics (Coulomb's law, electric field, Gauss's law, electric potential, capacitance, electrostatic energy, dielectrics, boundary conditions)
   - Magnetostatics (Biot-Savart, Ampère's law, magnetic flux, vector potential, inductance, magnetic energy, magnetic materials, boundary conditions)
   - Maxwell's equations for time-varying fields (Faraday's law, motional EMF, displacement current, full Maxwell set, boundary conditions)
   - Plane wave propagation (uniform plane waves in lossless / lossy media, polarization, Poynting vector, normal incidence, oblique incidence, total reflection, total transmission, Brewster's angle)
   - Reflection, transmission, and waveguides (rectangular waveguide modes, TE/TM, cavity resonators, optical fibers — brief)
   - Antennas and radiation (short dipole, half-wave dipole, antenna patterns, directivity, Friis equation, antenna arrays)
   - Wave-matter interaction and applications (radar equation, remote sensing, microwave systems — selected highlights)

3. Per-page format (per addendum): 1500-3500 words, mandatory Mermaid diagram OR comparison table OR ASCII figure, ≥2 worked examples with full steps, common pitfalls, Python (NumPy / matplotlib) code where useful.

4. **Heavy use of vector calculus notation** (KaTeX). Frequent objects: $\vec E$, $\vec H$, $\vec D$, $\vec B$, $\vec J$, $\rho$, $\epsilon$, $\mu$, $\sigma$, $\omega$, $k$. Use `$$\begin{aligned} \nabla\times\vec E &= -\partial_t\vec B \\\\ \nabla\cdot\vec D &= \rho \end{aligned}$$` for grouped Maxwell equations.

5. Cross-link to:
   - `/math/engineering-math/vector-differential-calculus` (gradient/div/curl)
   - `/math/engineering-math/vector-integral-calculus` (Stokes / divergence theorem)
   - `/math/engineering-math/complex-functions-and-analyticity` (phasors)
   - `/physics/signals-systems/` (frequency-domain views)
   - `/physics/general/` (intro-level E&M)

## Workflow

1. `pdfinfo "<pdf>"` for page count.
2. `pdftotext -l 30 "<pdf>" -` for cover + TOC + preface.
3. For each chapter, `pdftotext -f X -l Y "<pdf>" -` and write 1-2 wiki pages.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/physics/electromagnetics/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Physically and mathematically precise. Match the depth addendum.
- Don't fabricate beyond what Ulaby covers.

Begin now.
