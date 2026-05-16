---
title: Molecular Geometry and Bonding Theory
sidebar_position: 11
---

# Molecular Geometry and Bonding Theory

A Lewis structure tells which atoms are connected, but molecular geometry tells how atoms are arranged in space. Shape controls polarity, reactivity, biological recognition, and many physical properties. VSEPR provides a practical first model, while valence bond and molecular orbital theories explain bonding in more electronic detail.

In the Ebbing and Gammon sequence this topic sits near VSEPR, dipole moments, valence bond theory, hybridization, multiple bonding, molecular orbital theory, and delocalized bonding. That placement matters because general chemistry is cumulative: a later calculation usually reuses earlier ideas about measurement, atomic structure, bonding, molecular motion, or equilibrium. The aim of this page is to turn the chapter-level ideas into a working reference that can be used for problem solving without copying the textbook's wording or examples.

## Definitions

The following definitions give the vocabulary and notation used in this page. Treat them as operational definitions: each one says what can be counted, measured, compared, or conserved in a chemical argument.

- Electron domain is a bonding region or lone-pair region around a central atom.
- VSEPR predicts geometry by minimizing repulsions among electron domains.
- Electron-domain geometry describes all electron domains; molecular geometry describes atom positions only.
- Dipole moment measures separation of positive and negative charge.
- Hybrid orbital is a mixed atomic orbital used in valence bond descriptions.
- Sigma bond has electron density along the internuclear axis.
- Pi bond has side-by-side orbital overlap with electron density above and below the axis.
- Molecular orbital is an orbital spread over an entire molecule.

Definitions in chemistry often connect a symbolic representation to a physical sample. A formula such as $\mathrm{H_2O}$ names a substance, gives the atomic ratio inside one molecule, and supplies the molar mass used in a macroscopic calculation. A state symbol such as $\mathrm{(aq)}$ is not cosmetic; it says the species is dispersed in water and may be treated as ions when writing a net ionic equation. In the same way, constants such as $R$, $K_w$, $F$, or $N_A$ are compact definitions of the measurement system being used.

## Key results

The central results are:

- Steric number 2 gives linear electron geometry; 3 gives trigonal planar; 4 gives tetrahedral; 5 gives trigonal bipyramidal; 6 gives octahedral.
- Lone-pair repulsions are generally stronger than bonding-pair repulsions.
- Hybridization commonly follows electron domains: 2 is $sp$, 3 is $sp^2$, 4 is $sp^3$, 5 is $sp^3d$, 6 is $sp^3d^2$.
- A double bond contains one sigma and one pi bond; a triple bond contains one sigma and two pi bonds.
- Bond order in MO theory: $(N_b-N_a)/2$.
- A molecule with polar bonds may be nonpolar if bond dipoles cancel by symmetry.

VSEPR is fast and works well for many main-group molecules, but it does not replace electronic theories. Hybridization is a localized bonding picture; molecular orbital theory is delocalized and is essential for explaining bond order, magnetism, and molecules such as oxygen. Dipole moment requires both polar bonds and asymmetric geometry.

A good way to use these results is to state the chemical model first, then substitute numbers second. For molecular geometry and bonding theory, the model usually answers questions such as what particles are present, what is conserved, which process is idealized, and which measurement is being interpreted. Once that sentence is clear, the algebra becomes a bookkeeping problem rather than a search for a memorized pattern.

Units are part of the result, not decoration. Whenever a formula contains an empirical constant, a tabulated value, or a ratio of measured quantities, the units tell you whether the expression has been used in the intended form. This is especially important in general chemistry because several equations have nearly identical algebra but different meanings: pressure can be a measured state variable, an equilibrium correction, or a colligative effect; energy can be heat flow, enthalpy, internal energy, or free energy.

The strongest check is an independent chemical interpretation. Ask whether the sign agrees with direction, whether a concentration can be negative, whether a mole ratio follows the balanced equation, whether an equilibrium shift opposes the stress, and whether a microscopic description explains the macroscopic number. These checks connect molecular geometry and bonding theory to neighboring topics instead of leaving it as an isolated technique.

A second check is to compare the limiting cases. If a reactant amount goes to zero, a product amount cannot remain large. If temperature rises in a gas sample at fixed volume, pressure should not fall in an ideal model. If an acid is diluted, hydronium concentration should normally decrease unless a coupled equilibrium supplies more. Limiting cases often reveal algebra that has been rearranged correctly but applied to the wrong chemical situation.

Finally, keep symbolic and particulate representations side by side. A balanced equation, an equilibrium expression, an orbital diagram, or a polymer repeat unit is a compact symbol for a population of particles. Translating that symbol into words forces you to say what is reacting, what is being counted, and what is being held constant. That translation is usually the difference between a calculation that can be adapted to a new problem and one that only imitates a worked example.

## Visual

| Steric number | Electron-domain geometry | Common molecular geometries |
|---:|---|---|
| 2 | linear | linear |
| 3 | trigonal planar | trigonal planar, bent |
| 4 | tetrahedral | tetrahedral, trigonal pyramidal, bent |
| 5 | trigonal bipyramidal | seesaw, T-shaped, linear |
| 6 | octahedral | square pyramidal, square planar |

```mermaid
flowchart LR
  A[Lewis structure] --> B[Count electron domains]
  B --> C[Electron-domain geometry]
  C --> D[Remove lone pairs from name]
  D --> E[Molecular geometry]
  E --> F[Dipole analysis]
```

## Worked example 1: VSEPR shape and polarity of sulfur tetrafluoride

Problem. Predict the electron geometry, molecular geometry, and polarity of $\mathrm{SF_4}$.

    Method.

    1. Count valence electrons: S has 6 and four F atoms contribute 28, total 34.
2. Connect S to four F atoms with single bonds, using 8 electrons.
3. Complete four fluorine octets with 24 more electrons; total 32 used.
4. Place the remaining 2 electrons as one lone pair on sulfur.
5. Sulfur has five electron domains: four bonds and one lone pair, so electron geometry is trigonal bipyramidal.
6. With one equatorial lone pair, molecular geometry is seesaw.
7. The seesaw shape is asymmetric, so bond dipoles do not cancel.

    Checked answer. $\mathrm{SF_4}$ is trigonal-bipyramidal in electron geometry, seesaw in molecular geometry, and polar. A lone pair on a five-domain center usually breaks symmetry.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Worked example 2: Bond order and magnetism of oxygen

Problem. Use a simple MO count to find bond order for $\mathrm{O_2}$ and decide whether it is paramagnetic.

    Method.

    1. Oxygen has 12 valence electrons total.
2. For $\mathrm{O_2}$, the valence MO filling gives 8 electrons in bonding MOs and 4 in antibonding MOs.
3. Bond order is $(N_b-N_a)/2=(8-4)/2=2$.
4. The highest occupied antibonding $\pi^*$ orbitals contain two unpaired electrons.
5. Unpaired electrons imply paramagnetism.

    Checked answer. $\mathrm{O_2}$ has bond order 2 and is paramagnetic. Lewis structures show a double bond but do not explain paramagnetism; MO theory does.

    The important habit is to identify the conserved quantity before reaching for an equation. In this example the units, coefficients, charges, or particles chosen in the first step control every later step. The final numerical answer is not accepted merely because it came from a formula; it is checked against the chemical picture. If the magnitude, sign, units, or limiting condition contradicts that picture, the calculation has to be restarted from the definition rather than patched at the end.

## Code

The snippet below is intentionally small, but it is runnable and mirrors the calculation style used in the worked examples. It keeps units visible in variable names so that the computation remains auditable.

```python
def vsepr_label(steric_number, lone_pairs):
    table = {
        (2, 0): "linear",
        (3, 0): "trigonal planar", (3, 1): "bent",
        (4, 0): "tetrahedral", (4, 1): "trigonal pyramidal", (4, 2): "bent",
        (5, 1): "seesaw", (5, 2): "T-shaped", (5, 3): "linear",
        (6, 2): "square planar",
    }
    return table.get((steric_number, lone_pairs), "geometry requires a fuller table")

def bond_order(bonding, antibonding):
    return (bonding - antibonding) / 2

print(vsepr_label(5, 1), bond_order(8, 4))
```

## Common pitfalls

- Naming electron geometry when asked for molecular geometry. Avoid it by removing lone pairs from the molecular shape name.
- Assuming polar bonds guarantee a polar molecule. Avoid it by checking vector cancellation by geometry.
- Counting multiple bonds as multiple VSEPR domains. Avoid it by counting each multiple bond as one electron domain.
- Using hybridization before drawing a Lewis structure. Avoid it by deriving hybridization from electron domains.
- Expecting Lewis theory to explain oxygen magnetism. Avoid it by using MO theory when unpaired electrons are observed.
- Ignoring lone-pair placement in trigonal bipyramidal geometries. Avoid it by placing lone pairs equatorial when minimizing repulsion.

## Connections

- [ionic and covalent bonding](/chemistry/general/ionic-and-covalent-bonding)
- [states of matter, liquids, and solids](/chemistry/general/states-of-matter-liquids-and-solids)
- [organic chemistry](/chemistry/general/organic-chemistry)
- [biochemistry and polymer materials](/chemistry/general/biochemistry-and-polymer-materials)
