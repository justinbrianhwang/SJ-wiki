---
title: Acids, Bases, and pH
sidebar_position: 16
---

# Acids, Bases, and pH

Acid-base chemistry classifies reactions by proton transfer, hydroxide production, or electron-pair acceptance depending on the model used. In water, pH gives a compact numerical scale for hydronium concentration and links acid-base strength to equilibrium.

In the Ebbing and Gammon sequence this topic sits near Arrhenius acids and bases, Bronsted-Lowry acids and bases, Lewis acids and bases, acid strength, molecular structure, water autoionization, strong acids and bases, and pH. That placement matters because general chemistry is cumulative: a later calculation usually reuses earlier ideas about measurement, atomic structure, bonding, molecular motion, or equilibrium. The aim of this page is to turn the chapter-level ideas into a working reference that can be used for problem solving without copying the textbook's wording or examples.

## Definitions

The following definitions give the vocabulary and notation used in this page. Treat them as operational definitions: each one says what can be counted, measured, compared, or conserved in a chemical argument.

- Arrhenius acid increases $\mathrm{H^+}$ or $\mathrm{H_3O^+}$ in water.
- Arrhenius base increases $\mathrm{OH^-}$ in water.
- Bronsted-Lowry acid donates a proton; Bronsted-Lowry base accepts a proton.
- Lewis acid accepts an electron pair; Lewis base donates an electron pair.
- Conjugate acid-base pairs differ by one proton.
- Strong acid or base reacts essentially completely in water.
- Weak acid or base reacts partially and is described by an equilibrium constant.
- pH is defined as $-\log[\mathrm{H_3O^+}]$ for dilute aqueous solutions.

Definitions in chemistry often connect a symbolic representation to a physical sample. A formula such as $\mathrm{H_2O}$ names a substance, gives the atomic ratio inside one molecule, and supplies the molar mass used in a macroscopic calculation. A state symbol such as $\mathrm{(aq)}$ is not cosmetic; it says the species is dispersed in water and may be treated as ions when writing a net ionic equation. In the same way, constants such as $R$, $K_w$, $F$, or $N_A$ are compact definitions of the measurement system being used.

## Key results

The central results are:

- Water autoionization: $K_w=[H_3O^+][OH^-]=1.0\times10^{-14}$ at $25^\circ\mathrm{C}$.
- pH: $\mathrm{pH}=-\log[H_3O^+]$.
- pOH: $\mathrm{pOH}=-\log[OH^-]$.
- At $25^\circ\mathrm{C}$, $\mathrm{pH+pOH}=14.00$.
- For strong monoprotic acid, $[H_3O^+]$ approximately equals analytical acid concentration.
- For strong group 1 hydroxide bases, $[OH^-]$ approximately equals base concentration.

Strong and weak are not the same as concentrated and dilute. Strength describes extent of reaction with water; concentration describes amount dissolved per volume. This distinction is essential because a dilute strong acid can have higher pH than a concentrated weak acid, while the weak acid still remains weak by equilibrium definition.

A good way to use these results is to state the chemical model first, then substitute numbers second. For acids, bases, and ph, the model usually answers questions such as what particles are present, what is conserved, which process is idealized, and which measurement is being interpreted. Once that sentence is clear, the algebra becomes a bookkeeping problem rather than a search for a memorized pattern.

Units are part of the result, not decoration. Whenever a formula contains an empirical constant, a tabulated value, or a ratio of measured quantities, the units tell you whether the expression has been used in the intended form. This is especially important in general chemistry because several equations have nearly identical algebra but different meanings: pressure can be a measured state variable, an equilibrium correction, or a colligative effect; energy can be heat flow, enthalpy, internal energy, or free energy.

The strongest check is an independent chemical interpretation. Ask whether the sign agrees with direction, whether a concentration can be negative, whether a mole ratio follows the balanced equation, whether an equilibrium shift opposes the stress, and whether a microscopic description explains the macroscopic number. These checks connect acids, bases, and ph to neighboring topics instead of leaving it as an isolated technique.

A second check is to compare the limiting cases. If a reactant amount goes to zero, a product amount cannot remain large. If temperature rises in a gas sample at fixed volume, pressure should not fall in an ideal model. If an acid is diluted, hydronium concentration should normally decrease unless a coupled equilibrium supplies more. Limiting cases often reveal algebra that has been rearranged correctly but applied to the wrong chemical situation.

Finally, keep symbolic and particulate representations side by side. A balanced equation, an equilibrium expression, an orbital diagram, or a polymer repeat unit is a compact symbol for a population of particles. Translating that symbol into words forces you to say what is reacting, what is being counted, and what is being held constant. That translation is usually the difference between a calculation that can be adapted to a new problem and one that only imitates a worked example.

## Visual

```text
Acidic                 Neutral                Basic
pH 0      3      6      7      8      11      14
|---------|------|------|------|------|-------|
high [H3O+]                         high [OH-]
```

| Model | Acid | Base | Example |
|---|---|---|---|
| Arrhenius | increases $H_3O^+$ in water | increases $OH^-$ in water | HCl, NaOH |
| Bronsted-Lowry | proton donor | proton acceptor | $NH_4^+$, $NH_3$ |
| Lewis | electron-pair acceptor | electron-pair donor | $BF_3$, $NH_3$ |

## Worked example 1: pH of a strong acid

Problem. Find the pH of $2.5\times10^{-3}\ \mathrm{M}$ HCl at $25^\circ\mathrm{C}$.

    Method.

    1. Classify HCl as a strong monoprotic acid.
2. Assume complete reaction in water, so $[H_3O^+]=2.5\times10^{-3}\ \mathrm{M}$.
3. Use $\mathrm{pH}=-\log[H_3O^+]$.
4. Substitute: $\mathrm{pH}=-\log(2.5\times10^{-3})$.
5. Calculate: pH $=2.60$.

    Checked answer. The pH is 2.60. A millimolar strong acid should have pH around 3, and $2.5$ millimolar is somewhat below 3.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Worked example 2: pH after strong acid-base mixing

Problem. Mix 40.0 mL of 0.100 M HNO3 with 25.0 mL of 0.120 M KOH. Find final pH.

    Method.

    1. Write the net ionic reaction: $\mathrm{H^+ + OH^-\to H_2O}$.
2. Moles acid: $0.0400\times0.100=0.00400\ \mathrm{mol}$.
3. Moles base: $0.0250\times0.120=0.00300\ \mathrm{mol}$.
4. Hydroxide is limiting; excess acid moles are $0.00400-0.00300=0.00100\ \mathrm{mol}$.
5. Total volume is $0.0400+0.0250=0.0650\ \mathrm{L}$.
6. $[H^+]=0.00100/0.0650=0.0154\ \mathrm{M}$.
7. pH $=-\log(0.0154)=1.81$.

    Checked answer. Final pH is 1.81. Acid remains after neutralization, so pH below 7 is required.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Code

The snippet below is intentionally small, but it is runnable and mirrors the calculation style used in the worked examples. It keeps units visible in variable names so that the computation remains auditable.

```python
from math import log10

def pH_from_h(h):
    return -log10(h)

def strong_mix_pH(acid_M, acid_mL, base_M, base_mL):
    h_mol = acid_M * acid_mL / 1000.0
    oh_mol = base_M * base_mL / 1000.0
    volume_L = (acid_mL + base_mL) / 1000.0
    excess_h = h_mol - oh_mol
    return pH_from_h(excess_h / volume_L)

print(pH_from_h(2.5e-3))
print(strong_mix_pH(0.100, 40.0, 0.120, 25.0))
```

## Common pitfalls

- Equating strong with concentrated. Avoid it by separating equilibrium extent from molarity.
- Taking pH before neutralization stoichiometry. Avoid it by reacting strong acid and base moles first.
- Forgetting that some strong bases provide two hydroxides per formula unit. Avoid it by using formula stoichiometry for $[OH^-]$.
- Using $14$ for pH + pOH at all temperatures. Avoid it by noting that 14.00 is specific to $25^\circ\mathrm{C}$.
- Confusing conjugate acid with original acid. Avoid it by checking the species differs by exactly one proton.
- Reporting impossible pH from a negative concentration. Avoid it by checking limiting reagent signs before logarithms.

## Connections

- [aqueous reactions and solution stoichiometry](/chemistry/general/aqueous-reactions-and-solution-stoichiometry)
- [acid-base equilibria, buffers, and titrations](/chemistry/general/acid-base-equilibria-buffers-and-titrations)
- [chemical equilibrium](/chemistry/general/chemical-equilibrium)
- [solubility and complex-ion equilibria](/chemistry/general/solubility-and-complex-ion-equilibria)
