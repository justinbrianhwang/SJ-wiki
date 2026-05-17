---
title: States of Matter, Liquids, and Solids
sidebar_position: 12
---

# States of Matter, Liquids, and Solids

States of matter connect molecular attractions to macroscopic properties. Gases are compressible and disordered, liquids have fixed volume but flow, and solids retain shape through strong organized or networked attractions. Phase changes show how energy changes particle arrangement without necessarily changing chemical identity.

In the Ebbing and Gammon sequence this topic sits near gases, liquids, solids, phase transitions, phase diagrams, surface tension, viscosity, intermolecular forces, crystalline solids, unit cells, and x-ray diffraction. That placement matters because general chemistry is cumulative: a later calculation usually reuses earlier ideas about measurement, atomic structure, bonding, molecular motion, or equilibrium. The aim of this page is to turn the chapter-level ideas into a working reference that can be used for problem solving without copying the textbook's wording or examples.

![A phase diagram of water maps solid, liquid, vapor, triple-point, and critical-point regions.](https://commons.wikimedia.org/wiki/Special:FilePath/Phase_diagram_of_water.svg)

*Figure: Water phase diagram connecting pressure and temperature to state of matter. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Phase_diagram_of_water.svg), Cmglee, CC BY-SA 3.0.*

## Definitions

The following definitions give the vocabulary and notation used in this page. Treat them as operational definitions: each one says what can be counted, measured, compared, or conserved in a chemical argument.

- Intermolecular forces are attractions between particles, including dispersion, dipole-dipole, and hydrogen bonding.
- Phase transition is a physical change between solid, liquid, and gas.
- Vapor pressure is the pressure exerted by vapor in equilibrium with liquid or solid.
- Boiling occurs when vapor pressure equals external pressure.
- Surface tension is resistance of a liquid surface to expansion.
- Viscosity is resistance to flow.
- Unit cell is the repeating structural unit of a crystal lattice.
- Coordination number is the number of nearest neighbors around a particle in a crystal.

Definitions in chemistry often connect a symbolic representation to a physical sample. A formula such as $\mathrm{H_2O}$ names a substance, gives the atomic ratio inside one molecule, and supplies the molar mass used in a macroscopic calculation. A state symbol such as $\mathrm{(aq)}$ is not cosmetic; it says the species is dispersed in water and may be treated as ions when writing a net ionic equation. In the same way, constants such as $R$, $K_w$, $F$, or $N_A$ are compact definitions of the measurement system being used.

## Key results

The central results are:

- Clausius-Clapeyron form: $\ln(P_2/P_1)=-\Delta H_{vap}/R(1/T_2-1/T_1)$.
- Heating curve plateaus correspond to phase change at constant temperature.
- Density from unit cell: $\rho=Z M/(N_A a^3)$ for cubic cell edge $a$.
- Stronger intermolecular forces generally increase boiling point, viscosity, and surface tension.
- Hydrogen bonding requires H bonded to N, O, or F and an acceptor lone pair.
- A phase diagram maps stable phase as a function of pressure and temperature.

Phase behavior is an energy competition. Temperature measures kinetic energy tendency to disperse particles; intermolecular forces stabilize condensed phases. Crystal structures add geometry to that competition: a solid's density and properties depend on how particles pack in a repeating lattice.

A good way to use these results is to state the chemical model first, then substitute numbers second. For states of matter, the model usually answers questions such as what particles are present, what is conserved, which process is idealized, and which measurement is being interpreted. Once that sentence is clear, the algebra becomes a bookkeeping problem rather than a search for a memorized pattern.

Units are part of the result, not decoration. Whenever a formula contains an empirical constant, a tabulated value, or a ratio of measured quantities, the units tell you whether the expression has been used in the intended form. This is especially important in general chemistry because several equations have nearly identical algebra but different meanings: pressure can be a measured state variable, an equilibrium correction, or a colligative effect; energy can be heat flow, enthalpy, internal energy, or free energy.

The strongest check is an independent chemical interpretation. Ask whether the sign agrees with direction, whether a concentration can be negative, whether a mole ratio follows the balanced equation, whether an equilibrium shift opposes the stress, and whether a microscopic description explains the macroscopic number. These checks connect states of matter to neighboring topics instead of leaving it as an isolated technique.

A second check is to compare the limiting cases. If a reactant amount goes to zero, a product amount cannot remain large. If temperature rises in a gas sample at fixed volume, pressure should not fall in an ideal model. If an acid is diluted, hydronium concentration should normally decrease unless a coupled equilibrium supplies more. Limiting cases often reveal algebra that has been rearranged correctly but applied to the wrong chemical situation.

Finally, keep symbolic and particulate representations side by side. A balanced equation, an equilibrium expression, an orbital diagram, or a polymer repeat unit is a compact symbol for a population of particles. Translating that symbol into words forces you to say what is reacting, what is being counted, and what is being held constant. That translation is usually the difference between a calculation that can be adapted to a new problem and one that only imitates a worked example.

## Visual

```text
Rough heating curve:

T
|                gas warming
|              /
|   boiling __/
|          /
| melting_/ liquid warming
|      /
|_____/ solid warming
+------------------------ heat added
```

| Force | Where it appears | Relative importance |
|---|---|---|
| London dispersion | all particles | grows with size and polarizability |
| Dipole-dipole | polar molecules | depends on molecular polarity |
| Hydrogen bonding | H-N, H-O, H-F systems | strong special dipole interaction |
| Ion-dipole | ions in polar solvents | important in dissolving salts |

## Worked example 1: Vapor pressure from Clausius-Clapeyron

Problem. A liquid has vapor pressure 100.0 mmHg at 300 K and $\Delta H_{vap}=35.0\ \mathrm{kJ\ mol^{-1}}$. Estimate vapor pressure at 320 K.

    Method.

    1. Use $\ln(P_2/P_1)=-\Delta H_{vap}/R(1/T_2-1/T_1)$.
2. Convert enthalpy to joules: $35.0\ \mathrm{kJ\ mol^{-1}}=35000\ \mathrm{J\ mol^{-1}}$.
3. Compute reciprocal difference: $1/320-1/300=-0.0002083\ \mathrm{K^{-1}}$.
4. Compute right side: $-(35000/8.314)(-0.0002083)=0.877$.
5. Exponentiate: $P_2/P_1=e^{0.877}=2.40$.
6. Find $P_2=2.40(100.0)=240\ \mathrm{mmHg}$.

    Checked answer. $P_2\approx 240\ \mathrm{mmHg}$. Vapor pressure increases with temperature, so the result should be greater than 100 mmHg.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Worked example 2: Density of a cubic unit cell

Problem. A metal has face-centered cubic unit cells with edge length 408 pm and molar mass $107.9\ \mathrm{g\ mol^{-1}}$. Find density.

    Method.

    1. Face-centered cubic has $Z=4$ atoms per unit cell.
2. Convert edge length: $408\ \mathrm{pm}=4.08\times10^{-8}\ \mathrm{cm}$.
3. Cell volume: $a^3=(4.08\times10^{-8})^3=6.79\times10^{-23}\ \mathrm{cm^3}$.
4. Mass per cell: $4(107.9\ \mathrm{g\ mol^{-1}})/(6.022\times10^{23})=7.17\times10^{-22}\ \mathrm{g}$.
5. Density: $7.17\times10^{-22}/6.79\times10^{-23}=10.6\ \mathrm{g\ cm^{-3}}$.

    Checked answer. $10.6\ \mathrm{g\ cm^{-3}}$. A dense metal value near 10 g/cm3 is plausible for a heavy noble metal.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Code

The snippet below is intentionally small, but it is runnable and mirrors the calculation style used in the worked examples. It keeps units visible in variable names so that the computation remains auditable.

```python
from math import exp, log

R = 8.314
def vapor_pressure(P1, T1, T2, delta_h_vap_J):
    ln_ratio = -delta_h_vap_J / R * (1 / T2 - 1 / T1)
    return P1 * exp(ln_ratio)

def cubic_density(Z, molar_mass_g, edge_pm):
    NA = 6.022e23
    edge_cm = edge_pm * 1e-10
    mass_cell = Z * molar_mass_g / NA
    volume_cell = edge_cm ** 3
    return mass_cell / volume_cell

print(vapor_pressure(100.0, 300.0, 320.0, 35000.0), cubic_density(4, 107.9, 408))
```

## Common pitfalls

- Calling intramolecular covalent bonds intermolecular forces. Avoid it by separating bonds within particles from attractions between particles.
- Assuming boiling always occurs at 100C. Avoid it by checking external pressure and substance identity.
- Forgetting phase-change plateaus in heating curves. Avoid it by distinguishing heat that raises temperature from heat that changes phase.
- Using pm directly as cm in unit-cell density. Avoid it by converting length units before cubing.
- Assuming stronger intermolecular forces always mean higher vapor pressure. Avoid it by remembering stronger attractions lower vapor pressure.
- Ignoring defect or crystal type when comparing solids. Avoid it by identifying molecular, ionic, metallic, covalent-network, or atomic solids.

## Connections

- [gases](/chemistry/general/gases)
- [solutions and colligative properties](/chemistry/general/solutions-and-colligative-properties)
- [molecular geometry and bonding theory](/chemistry/general/molecular-geometry-and-bonding-theory)
- [main-group elements](/chemistry/general/main-group-elements)
