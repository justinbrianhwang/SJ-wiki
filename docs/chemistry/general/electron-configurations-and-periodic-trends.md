---
title: Electron Configurations and Periodic Trends
sidebar_position: 9
---

# Electron Configurations and Periodic Trends

Electron configurations translate quantum numbers into the periodic table. They explain why elements in a group have related chemistry and why properties such as atomic radius, ionization energy, and electron affinity vary across periods and down groups.

In the Ebbing and Gammon sequence this topic sits near electron spin, Pauli exclusion, building-up principle, periodic table, orbital diagrams, Hund's rule, and periodic properties. That placement matters because general chemistry is cumulative: a later calculation usually reuses earlier ideas about measurement, atomic structure, bonding, molecular motion, or equilibrium. The aim of this page is to turn the chapter-level ideas into a working reference that can be used for problem solving without copying the textbook's wording or examples.

![A periodic table displays element names, atomic masses, electron configurations, ionization energies, and electronegativities.](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_table_large.svg/600px-Periodic_table_large.svg.png)

*Figure: Periodic table with electron configurations and trend-related data. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Periodic_table_large.svg), 2012rc, CC BY 3.0.*

## Definitions

The following definitions give the vocabulary and notation used in this page. Treat them as operational definitions: each one says what can be counted, measured, compared, or conserved in a chemical argument.

- Pauli exclusion principle states that no two electrons in an atom have the same four quantum numbers.
- Aufbau or building-up principle fills lower-energy orbitals before higher-energy orbitals for ground states.
- Hund's rule places electrons singly in degenerate orbitals with parallel spins before pairing.
- Valence electrons are outer-shell electrons most involved in bonding.
- Core electrons are inner electrons that shield valence electrons from full nuclear charge.
- Effective nuclear charge $Z_{eff}$ is the net positive attraction felt by an electron after shielding.
- Ionization energy is energy required to remove an electron from a gaseous atom or ion.
- Atomic radius reflects the size of the electron cloud and depends on shell number and nuclear attraction.

Definitions in chemistry often connect a symbolic representation to a physical sample. A formula such as $\mathrm{H_2O}$ names a substance, gives the atomic ratio inside one molecule, and supplies the molar mass used in a macroscopic calculation. A state symbol such as $\mathrm{(aq)}$ is not cosmetic; it says the species is dispersed in water and may be treated as ions when writing a net ionic equation. In the same way, constants such as $R$, $K_w$, $F$, or $N_A$ are compact definitions of the measurement system being used.

## Key results

The central results are:

- Orbital capacities: $s=2$, $p=6$, $d=10$, $f=14$ electrons.
- Common filling order begins $1s,2s,2p,3s,3p,4s,3d,4p,5s,4d,5p,6s,4f,5d,6p$.
- Across a period, $Z_{eff}$ generally increases and atomic radius decreases.
- Down a group, added shells generally increase atomic radius.
- Ionization energy generally increases across a period and decreases down a group.
- Cations are smaller than parent atoms; anions are larger than parent atoms.

Periodic trends are not memorized arrows only; they are consequences of attraction and shielding. Across a period, protons are added to the nucleus while electrons enter the same principal shell, so valence electrons feel stronger attraction. Down a group, new shells place valence electrons farther from the nucleus and increase shielding.

A good way to use these results is to state the chemical model first, then substitute numbers second. For electron configurations and periodic trends, the model usually answers questions such as what particles are present, what is conserved, which process is idealized, and which measurement is being interpreted. Once that sentence is clear, the algebra becomes a bookkeeping problem rather than a search for a memorized pattern.

Units are part of the result, not decoration. Whenever a formula contains an empirical constant, a tabulated value, or a ratio of measured quantities, the units tell you whether the expression has been used in the intended form. This is especially important in general chemistry because several equations have nearly identical algebra but different meanings: pressure can be a measured state variable, an equilibrium correction, or a colligative effect; energy can be heat flow, enthalpy, internal energy, or free energy.

The strongest check is an independent chemical interpretation. Ask whether the sign agrees with direction, whether a concentration can be negative, whether a mole ratio follows the balanced equation, whether an equilibrium shift opposes the stress, and whether a microscopic description explains the macroscopic number. These checks connect electron configurations and periodic trends to neighboring topics instead of leaving it as an isolated technique.

A second check is to compare the limiting cases. If a reactant amount goes to zero, a product amount cannot remain large. If temperature rises in a gas sample at fixed volume, pressure should not fall in an ideal model. If an acid is diluted, hydronium concentration should normally decrease unless a coupled equilibrium supplies more. Limiting cases often reveal algebra that has been rearranged correctly but applied to the wrong chemical situation.

Finally, keep symbolic and particulate representations side by side. A balanced equation, an equilibrium expression, an orbital diagram, or a polymer repeat unit is a compact symbol for a population of particles. Translating that symbol into words forces you to say what is reacting, what is being counted, and what is being held constant. That translation is usually the difference between a calculation that can be adapted to a new problem and one that only imitates a worked example.

## Visual

```text
Energy filling sketch:

1s
2s  2p
3s  3p
4s  3d  4p
5s  4d  5p
6s  4f  5d  6p

Read roughly left to right by increasing energy for ground-state filling.
```

| Trend | Across a period | Down a group | Main reason |
|---|---|---|---|
| Atomic radius | decreases | increases | $Z_{eff}$ versus shell number |
| First ionization energy | increases | decreases | attraction to valence electron |
| Metallic character | decreases | increases | ease of losing electrons |
| Ionic radius | depends on charge | increases | electron count and shell size |

## Worked example 1: Electron configuration of iron(III)

Problem. Write the electron configuration of $\mathrm{Fe^{3+}}$.

    Method.

    1. Neutral iron has atomic number 26, so it has 26 electrons.
2. Ground-state neutral Fe is $\mathrm{[Ar]4s^2 3d^6}$.
3. For transition-metal cations, remove electrons from the highest principal quantum number first; remove $4s$ before $3d$.
4. Remove two $4s$ electrons to get $\mathrm{Fe^{2+}:[Ar]3d^6}$.
5. Remove one more electron from $3d$ to get $\mathrm{Fe^{3+}:[Ar]3d^5}$.

    Checked answer. $\mathrm{Fe^{3+}}$ has configuration $\mathrm{[Ar]3d^5}$. The ion has 23 electrons total: argon core 18 plus five d electrons.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Worked example 2: Ranking atomic radii

Problem. Rank $\mathrm{Na}$, $\mathrm{Mg}$, and $\mathrm{K}$ from smallest to largest atomic radius.

    Method.

    1. Locate the elements: Na and Mg are in period 3; K is below Na in group 1.
2. Across period 3 from Na to Mg, nuclear charge increases while electrons enter the same shell, so radius decreases.
3. Therefore Mg is smaller than Na.
4. Down group 1 from Na to K, a new shell is added, so K is larger than Na.
5. Combine the comparisons: Mg < Na < K.

    Checked answer. Smallest to largest: $\mathrm{Mg \lt  Na \lt  K}$. The largest atom should be the one with the highest occupied shell among the three, potassium.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Code

The snippet below is intentionally small, but it is runnable and mirrors the calculation style used in the worked examples. It keeps units visible in variable names so that the computation remains auditable.

```python
capacities = {"s": 2, "p": 6, "d": 10, "f": 14}
filling = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2),
           ("3p", 6), ("4s", 2), ("3d", 6)]

electrons_fe = sum(count for _, count in filling)
fe3_electrons = electrons_fe - 3

def period_radius_rule(a_period, b_period, same_period_left_to_right):
    if a_period != b_period:
        return "larger shell usually means larger radius"
    return "radius decreases left to right" if same_period_left_to_right else "compare positions"

print(electrons_fe, fe3_electrons, period_radius_rule(3, 3, True))
```

## Common pitfalls

- Removing $3d$ electrons before $4s$ for transition-metal cations. Avoid it by removing electrons from the highest principal quantum number first.
- Memorizing trend arrows without explaining shielding. Avoid it by using shell number and effective nuclear charge.
- Pairing p electrons too early in orbital diagrams. Avoid it by applying Hund's rule to degenerate orbitals.
- Counting valence electrons incorrectly for main-group ions. Avoid it by using group number and charge together.
- Assuming every configuration has no exceptions. Avoid it by checking known stability exceptions such as chromium and copper when needed.
- Comparing ionic radii without checking electron count. Avoid it by identifying isoelectronic series and nuclear charge.

## Connections

- [quantum theory of atoms](/chemistry/general/quantum-theory-of-atoms)
- [ionic and covalent bonding](/chemistry/general/ionic-and-covalent-bonding)
- [main-group elements](/chemistry/general/main-group-elements)
- [transition metals and coordination compounds](/chemistry/general/transition-metals-and-coordination-compounds)
