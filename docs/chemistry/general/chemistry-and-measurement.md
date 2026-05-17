---
title: Chemistry and Measurement
sidebar_position: 2
---

# Chemistry and Measurement

Measurement is the entry point into chemistry because chemical explanations must be tied to observations that can be repeated. A color change may suggest reaction, but mass, volume, temperature, pressure, and composition let the observation become evidence. This page emphasizes the measurement habits that make later chemical calculations reliable.

In the Ebbing and Gammon sequence this topic sits near the scientific method, matter classification, significant figures, SI units, derived units, and dimensional analysis. That placement matters because general chemistry is cumulative: a later calculation usually reuses earlier ideas about measurement, atomic structure, bonding, molecular motion, or equilibrium. The aim of this page is to turn the chapter-level ideas into a working reference that can be used for problem solving without copying the textbook's wording or examples.

![Four Bunsen burner flames show how controlled air flow changes the flame used for heating samples.](https://commons.wikimedia.org/wiki/Special:FilePath/Bunsen_burner_flame_types.jpg)

*Figure: Bunsen burner flame types as a laboratory context for controlled observation. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Bunsen_burner_flame_types.jpg), Arthur Jan Fijalkowski, CC BY-SA 3.0/GFDL.*

![A schematic mass spectrometer shows ionization, acceleration, magnetic deflection, and detection.](https://commons.wikimedia.org/wiki/Special:FilePath/Mass_Spectrometer_Schematic.svg)

*Figure: Mass spectrometer schematic connecting measurement to atomic and molecular mass. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Mass_Spectrometer_Schematic.svg), Devon Fyson and USGS, public domain.*

## Definitions

The following definitions give the vocabulary and notation used in this page. Treat them as operational definitions: each one says what can be counted, measured, compared, or conserved in a chemical argument.

- A hypothesis is a tentative explanation that can be tested against observations.
- A scientific law summarizes a reproducible pattern, such as conservation of mass.
- A theory explains why a broad collection of observations behaves as it does.
- A significant figure is a digit known from measurement plus one estimated digit.
- Accuracy describes closeness to an accepted or true value; precision describes reproducibility.
- An SI base unit is an agreed measurement unit such as meter, kilogram, second, kelvin, mole, and ampere.
- A derived unit combines base units, such as density in $\mathrm{g\ cm^{-3}}$ or pressure in pascals.
- Dimensional analysis uses conversion factors equal to one to transform units without changing the physical quantity.

Definitions in chemistry often connect a symbolic representation to a physical sample. A formula such as $\mathrm{H_2O}$ names a substance, gives the atomic ratio inside one molecule, and supplies the molar mass used in a macroscopic calculation. A state symbol such as $\mathrm{(aq)}$ is not cosmetic; it says the species is dispersed in water and may be treated as ions when writing a net ionic equation. In the same way, constants such as $R$, $K_w$, $F$, or $N_A$ are compact definitions of the measurement system being used.

## Key results

The central results are:

- Density: $d = m/V$.
- Percent error: $\%\ \mathrm{error}=\vert \mathrm{measured}-\mathrm{accepted}\vert /\mathrm{accepted}\times 100\%$.
- Kelvin conversion: $T_K = T_{^\circ C}+273.15$.
- Scientific notation: $a\times 10^n$ with $1 \leq a \lt  10$.
- Multiplication and division keep the least number of significant figures among measured factors.
- Addition and subtraction keep the least precise decimal place among measured terms.

Dimensional analysis is more than a unit trick. It is a disciplined way to encode what is known, what is being asked, and what relationships connect the two. If every conversion factor is written as a ratio, the units cancel in a visible chain and the remaining unit becomes a check on the answer. Significant figures then report the quality of the measurement rather than the number of digits a calculator displayed.

A good way to use these results is to state the chemical model first, then substitute numbers second. For chemistry and measurement, the model usually answers questions such as what particles are present, what is conserved, which process is idealized, and which measurement is being interpreted. Once that sentence is clear, the algebra becomes a bookkeeping problem rather than a search for a memorized pattern.

Units are part of the result, not decoration. Whenever a formula contains an empirical constant, a tabulated value, or a ratio of measured quantities, the units tell you whether the expression has been used in the intended form. This is especially important in general chemistry because several equations have nearly identical algebra but different meanings: pressure can be a measured state variable, an equilibrium correction, or a colligative effect; energy can be heat flow, enthalpy, internal energy, or free energy.

The strongest check is an independent chemical interpretation. Ask whether the sign agrees with direction, whether a concentration can be negative, whether a mole ratio follows the balanced equation, whether an equilibrium shift opposes the stress, and whether a microscopic description explains the macroscopic number. These checks connect chemistry and measurement to neighboring topics instead of leaving it as an isolated technique.

A second check is to compare the limiting cases. If a reactant amount goes to zero, a product amount cannot remain large. If temperature rises in a gas sample at fixed volume, pressure should not fall in an ideal model. If an acid is diluted, hydronium concentration should normally decrease unless a coupled equilibrium supplies more. Limiting cases often reveal algebra that has been rearranged correctly but applied to the wrong chemical situation.

Finally, keep symbolic and particulate representations side by side. A balanced equation, an equilibrium expression, an orbital diagram, or a polymer repeat unit is a compact symbol for a population of particles. Translating that symbol into words forces you to say what is reacting, what is being counted, and what is being held constant. That translation is usually the difference between a calculation that can be adapted to a new problem and one that only imitates a worked example.

## Visual

| Quantity | Common unit | SI or derived unit | Typical chemistry use |
|---|---:|---:|---|
| Mass | g | kg | sample amount, conservation checks |
| Length | cm, nm | m | atomic scale, lab apparatus dimensions |
| Volume | mL, L | $\mathrm{m^3}$ | solutions and gases |
| Temperature | $^\circ\mathrm{C}$ | K | gas laws and thermodynamics |
| Amount | mol | mol | particle counting and stoichiometry |
| Density | $\mathrm{g\ mL^{-1}}$ | $\mathrm{kg\ m^{-3}}$ | identifying substances |

```mermaid
flowchart LR
  A[Question] --> B[Known measured values]
  B --> C[Conversion factors]
  C --> D[Unit cancellation]
  D --> E[Significant figures]
  E --> F[Chemical reasonableness check]
```

## Worked example 1: Density with significant figures

Problem. A metal sample has mass 37.50 g and displaces water from 21.30 mL to 26.06 mL. Find its density.

    Method.

    1. Find the sample volume by subtraction: $26.06-21.30=4.76\ \mathrm{mL}$.
2. The subtraction result has two decimal places because both readings were recorded to hundredths of a milliliter.
3. Use density: $d=m/V=37.50\ \mathrm{g}/4.76\ \mathrm{mL}$.
4. Calculate: $37.50/4.76=7.878...\ \mathrm{g\ mL^{-1}}$.
5. The limiting measured factor has three significant figures, so round to $7.88\ \mathrm{g\ mL^{-1}}$.

    Checked answer. $d=7.88\ \mathrm{g\ mL^{-1}}$. The density is metal-like and greater than water, so a sinking metal sample is plausible.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Worked example 2: Dimensional analysis across unit systems

Problem. A medicine solution contains 25.0 mg of solute per 5.00 mL. Convert the concentration to grams per liter.

    Method.

    1. Write the given concentration as $25.0\ \mathrm{mg}/5.00\ \mathrm{mL}$.
2. Convert milligrams to grams: $1\ \mathrm{g}/1000\ \mathrm{mg}$.
3. Convert milliliters to liters by multiplying by $1000\ \mathrm{mL}/1\ \mathrm{L}$ because milliliters are in the denominator.
4. Combine: $(25.0/5.00)(1/1000)(1000)=5.00\ \mathrm{g\ L^{-1}}$.
5. All measured values have three significant figures, so keep three.

    Checked answer. $5.00\ \mathrm{g\ L^{-1}}$. The factors of 1000 cancel, so 5 mg/mL equals 5 g/L.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Code

The snippet below is intentionally small, but it is runnable and mirrors the calculation style used in the worked examples. It keeps units visible in variable names so that the computation remains auditable.

```python
def density_from_displacement(mass_g, initial_ml, final_ml):
    volume_ml = final_ml - initial_ml
    return mass_g / volume_ml

def mg_per_ml_to_g_per_l(mg, ml):
    return (mg / ml) * (1e-3) * 1000.0

rho = density_from_displacement(37.50, 21.30, 26.06)
conc = mg_per_ml_to_g_per_l(25.0, 5.00)
print(round(rho, 3), round(conc, 3))
```

## Common pitfalls

- Rounding after every intermediate step. Avoid it by keeping guard digits until the final answer.
- Confusing accuracy with precision. Avoid it by separating closeness to true value from repeatability.
- Using Celsius directly in gas or thermodynamic equations. Avoid it by converting to kelvin before substitution.
- Writing conversion factors in the wrong direction. Avoid it by checking unit cancellation line by line.
- Counting exact conversion factors as limiting significant figures. Avoid it by identifying counted and defined quantities separately.
- Forgetting that density changes with temperature for many substances. Avoid it by recording experimental conditions with measured values.

## Connections

- [atoms, molecules, and ions](/chemistry/general/atoms-molecules-and-ions)
- [stoichiometry](/chemistry/general/stoichiometry)
- [gases](/chemistry/general/gases)
- [thermochemistry](/chemistry/general/thermochemistry)
