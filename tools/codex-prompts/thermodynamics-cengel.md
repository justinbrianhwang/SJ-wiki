You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/열역학.pdf` (Yunus A. Çengel & Michael A. Boles — *Thermodynamics: An Engineering Approach*, 9th ed, McGraw-Hill)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/thermodynamics/`
- **SUBJECT**: Engineering Thermodynamics

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview + numbered list of all pages.

2. **18-25 detail pages** covering Çengel's full scope:
   - Introduction and basic concepts (system, state, properties, processes, cycle, T/P/V, zeroth law)
   - Energy, energy transfer, and general energy analysis (work, heat, conservation)
   - Properties of pure substances (phase changes, property tables, ideal-gas equation, compressibility factor)
   - Energy analysis of closed systems (boundary work, PdV, first law for closed systems)
   - Mass and energy analysis of control volumes (steady-flow, nozzles, diffusers, turbines, compressors, throttling, heat exchangers, pipe flow)
   - Second law of thermodynamics (heat engines, refrigerators, heat pumps, Kelvin-Planck, Clausius, Carnot)
   - Entropy (Clausius inequality, T-ds relations, isentropic processes, entropy balance)
   - Exergy (reversible work, irreversibility, second-law efficiency)
   - Gas power cycles (Otto, Diesel, Stirling, Ericsson, Brayton, regeneration, reheat, intercool)
   - Vapor and combined power cycles (Rankine, reheat, regeneration, supercritical, combined cycle)
   - Refrigeration cycles (vapor-compression, absorption, gas refrigeration, cascade)
   - Thermodynamic property relations (Maxwell relations, Clapeyron, Joule-Thomson)
   - Gas mixtures (Dalton, Amagat, properties of mixtures)
   - Gas-vapor mixtures and air conditioning (humidity, psychrometric chart, AC processes)
   - Chemical reactions (combustion, fuels, theoretical air, dew point of combustion gases, adiabatic flame temperature)
   - Chemical and phase equilibrium (Gibbs function, equilibrium constant, simultaneous reactions)
   - Compressible flow (stagnation, Mach number, choked flow, normal shocks, oblique shocks, nozzles)

3. Per-page format follows the depth addendum (1500-3500 words; mandatory Mermaid diagram OR comparison table OR ASCII figure; ≥2 worked numerical examples with property-table lookups where relevant; common pitfalls; Python (numpy / iapws / coolprop sketches) where useful).

4. **Math precision**:
   - State postulate, property relations
   - First law: $dU = \delta Q - \delta W$
   - Entropy balance: $\dot S_{\mathrm{gen}} = \dot S_{\mathrm{out}} - \dot S_{\mathrm{in}} + \Delta S_{\mathrm{system}}$
   - Carnot efficiency: $\eta_{\mathrm{Carnot}} = 1 - T_L/T_H$
   - Ideal gas: $PV = nRT$ or $Pv = RT$
   - Maxwell relations using cyclic-rule notation

5. **Visual** — heavy use of:
   - PV / Ts / hs diagrams (ASCII or Mermaid where representable)
   - Cycle diagrams (Otto/Diesel/Brayton/Rankine schematics)
   - Property tables (steam, R-134a, ideal-gas constants)
   - Comparison tables (cycle efficiencies, working fluids)

6. Cross-link to:
   - `/physics/statistical-mechanics/` (microscopic foundations)
   - `/physics/general/` (basic thermal physics intro)
   - `/chemistry/general/thermochemistry`, `/chemistry/physical-chemistry/` (thermo overlap)
   - `/math/engineering-math/` (PDEs / calculus background)
   - `/cs/control-engineering/` (thermal systems control)

## Workflow

1. `pdfinfo "<pdf>"` for page count.
2. `pdftotext -l 30 "<pdf>" -` for cover + TOC.
3. For each chapter, read its page range with `pdftotext -f X -l Y "<pdf>" -` and write 1-2 wiki pages.
4. Write `intro.md` last.
5. Print summary listing all files.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/physics/thermodynamics/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically and physically precise. Match the depth addendum.
- Mermaid labels with special characters (`(`, `)`, `=`, `?`, `:`, `'`, `,`, `|`, `"`, `{`, `}`) wrapped in `"..."`; internal `"` → `#quot;`.
- For images, use `https://commons.wikimedia.org/wiki/Special:FilePath/<filename>` form only.
- Don't fabricate beyond Çengel's content.

Begin now.
