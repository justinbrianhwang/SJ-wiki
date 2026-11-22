---
title: Atoms, Molecules, and Ions
sidebar_position: 3
---

# Atoms, Molecules, and Ions

Chemical notation compresses several levels of description into a few symbols. An element symbol identifies a nuclear charge, an isotope label adds neutron information, a superscript charge records an electron imbalance, and a chemical formula gives the relative numbers of atoms. Keeping those layers separate prevents most early notation errors.

## From composition laws to atomic theory

The atomic picture was revived in modern chemistry because it explained quantitative regularities. The law of conservation of mass says that total mass remains constant in an ordinary chemical reaction. The law of definite proportions says that a given compound has a fixed elemental mass ratio. The law of multiple proportions says that when two elements form more than one compound, the masses of one that combine with a fixed mass of the other occur in small whole-number ratios.

Dalton's early nineteenth-century theory joined these observations: matter consists of atoms; atoms of different elements differ; compounds form from atoms in whole-number ratios; reactions rearrange atoms. Parts of the original theory needed revision. Atoms have subatomic structure, atoms of one element can have different masses, and nuclear reactions can change elemental identity. The central bookkeeping idea survives: ordinary chemical reactions rearrange nuclei and electrons but do not create or destroy the nuclei involved.

A simple multiple-proportions example comes from carbon monoxide and carbon dioxide. With $12.0\ \mathrm g$ of carbon, carbon monoxide contains about $16.0\ \mathrm g$ oxygen while carbon dioxide contains about $32.0\ \mathrm g$. The oxygen masses are in the ratio $1:2$, consistent with formulas CO and $\mathrm{CO_2}$.

The electron was inferred from cathode-ray experiments; the compact positive nucleus emerged from scattering experiments; the neutron later accounted for nuclear mass without extra charge. These discoveries replaced the atom as an indivisible sphere with a small nucleus surrounded by electrons. Chemical behavior is governed mainly by the electrons, while elemental identity is fixed by the nucleus.

## Reading nuclide notation

The standard notation

$$
{}^{A}_{Z}\mathrm{X}^{q}
$$

contains four distinct pieces:

- $X$ is the element symbol.
- $Z$ is the atomic number, equal to the number of protons.
- $A$ is the mass number, equal to protons plus neutrons.
- $q$ is the net charge, determined by protons minus electrons.

The neutron count is therefore

$$
N=A-Z,
$$

and the electron count for a species with signed charge $q$ is

$$
n_e=Z-q.
$$

For a $2+$ ion, subtract two electrons; for a $1-$ ion, the negative sign means one electron has been added.

| Species | Protons | Neutrons | Electrons | What changed? |
|---|---:|---:|---:|---|
| ${}^{23}_{11}\mathrm{Na}$ | 11 | 12 | 11 | neutral atom |
| ${}^{23}_{11}\mathrm{Na^+}$ | 11 | 12 | 10 | one electron removed |
| ${}^{35}_{17}\mathrm{Cl^-}$ | 17 | 18 | 18 | one electron added |
| ${}^{37}_{17}\mathrm{Cl^-}$ | 17 | 20 | 18 | two more neutrons than the preceding ion |

Isotopes have the same $Z$ and different $A$. They are the same element because they have the same proton count. Ions have unequal proton and electron counts. Ion formation does not alter the nucleus, so $\mathrm{Na^+}$ is still sodium.

### Worked example: reconstructing the symbol

A species contains 26 protons, 30 neutrons, and 23 electrons. Identify it and write its nuclide symbol.

Atomic number 26 belongs to iron, Fe. The mass number is

$$
A=26+30=56.
$$

There are three fewer electrons than protons, so the charge is

$$
q=26-23=+3.
$$

The complete symbol is

$$
{}^{56}_{26}\mathrm{Fe^{3+}}.
$$

The order of reasoning matters. Proton count identifies the element; neutron count selects the isotope; electron count sets the charge.

## Average atomic mass is a population average

The mass number is a whole-number count for one nuclide. The atomic mass printed on a periodic table is usually a weighted mean over naturally occurring isotopes:

$$
\bar m=\sum_i f_i m_i,
$$

where each $f_i$ is a fractional abundance and the fractions sum to 1. Isotope masses are not exact integers because nuclear binding energy changes the mass and because the atomic mass unit is defined relative to carbon-12.

For chlorine, using isotope mass $34.969\ \mathrm u$ at fractional abundance $0.7578$ and isotope mass $36.966\ \mathrm u$ at abundance $0.2422$ gives

$$
\begin{aligned}
\bar m&=(0.7578)(34.969\ \mathrm u)+(0.2422)(36.966\ \mathrm u)\\
&=35.45\ \mathrm u.
\end{aligned}
$$

The mean lies between the isotope masses and nearer the more abundant isotope. If a calculated average lies outside the range of component masses, the fractions or arithmetic are wrong.

### Worked example: finding an unknown isotope abundance

Suppose an element has two isotopes of mass $62.93\ \mathrm u$ and $64.93\ \mathrm u$, and its average atomic mass is $63.55\ \mathrm u$. Let $x$ be the fraction of the lighter isotope. The heavier fraction is $1-x$:

$$
63.55=x(62.93)+(1-x)(64.93).
$$

Expand and collect terms:

$$
\begin{aligned}
63.55&=62.93x+64.93-64.93x,\\
63.55-64.93&=-2.00x,\\
x&=0.690.
\end{aligned}
$$

Thus the abundances are $69.0\%$ light isotope and $31.0\%$ heavy isotope. Substitution checks the result:

$$
(0.690)(62.93)+(0.310)(64.93)=63.55\ \mathrm u.
$$

Mass spectrometry measures isotope mass-to-charge ratios and relative signal intensities, supplying the data from which such averages are formed. Natural abundances can vary for some elements and samples, so tabulated atomic weights may be given as intervals in high-precision work.

## Molecules, formula units, and ions

A molecule is a discrete, electrically neutral group of atoms held together by covalent bonds. Water and methane exist as $\mathrm{H_2O}$ and $\mathrm{CH_4}$ molecules. A molecular formula states the actual number of each atom in one molecule, but it does not fully specify connectivity or three-dimensional shape. Ethanol and dimethyl ether share $\mathrm{C_2H_6O}$ yet have different structures and properties.

An ionic solid is an extended lattice rather than a collection of discrete molecules. The formula $\mathrm{NaCl}$ gives the lowest whole-number ratio of sodium ions to chloride ions in the crystal. Calling one “NaCl molecule” obscures that structure; **formula unit** is the usual counting term.

Ions may be monatomic, such as $\mathrm{Mg^{2+}}$, or polyatomic, such as nitrate, $\mathrm{NO_3^-}$. A polyatomic ion behaves as a charged unit in many reactions, although its internal atoms are covalently bonded. Parentheses in a formula show that a subscript applies to the whole group: $\mathrm{Ca(NO_3)_2}$ contains two nitrate ions and therefore two nitrogen atoms and six oxygen atoms.

Several elements occur as diatomic molecules in their standard elemental forms:

$$
\mathrm{H_2,\ N_2,\ O_2,\ F_2,\ Cl_2,\ Br_2,\ I_2}.
$$

Their compounds are not automatically diatomic. Oxygen in water is written O, not $\mathrm{O_2}$, because the subscript belongs to the elemental substance rather than to every appearance of that element.

## Constructing neutral ionic formulas

An ionic compound must have zero total charge. Use the smallest whole-number ratio of ions that satisfies that condition. For $\mathrm{Ca^{2+}}$ and $\mathrm{NO_3^-}$, two nitrates balance one calcium:

$$
(+2)+2(-1)=0,
$$

so the formula is $\mathrm{Ca(NO_3)_2}$.

For aluminum and oxide, let the numbers of ions be $a$ and $b$:

$$
3a-2b=0.
$$

The smallest solution is $a=2$ and $b=3$, giving $\mathrm{Al_2O_3}$. Simply copying charge magnitudes as subscripts often works as a shortcut, but the result must be reduced. Calcium oxide is $\mathrm{CaO}$, not $\mathrm{Ca_2O_2}$.

### Worked example: formula and name with a variable-charge metal

Find the iron charge in $\mathrm{Fe_2(SO_4)_3}$ and name the compound.

Each sulfate ion has charge $2-$, so three sulfates contribute

$$
3(-2)=-6.
$$

The two iron ions must contribute $+6$ total. Each iron ion therefore has charge

$$
\frac{+6}{2}=+3.
$$

The name is **iron(III) sulfate**. The Roman numeral records the cation charge, not the number of iron atoms. By contrast, metals with a predictable single common charge, such as sodium or aluminum in elementary nomenclature, do not need a Roman numeral.

## Naming patterns and what they encode

Binary ionic compounds name the cation first and change the monatomic anion ending to *-ide*: $\mathrm{MgCl_2}$ is magnesium chloride. Compounds containing polyatomic ions retain the ion's established name: $\mathrm{Na_2CO_3}$ is sodium carbonate.

Binary molecular compounds use prefixes to state atom counts: $\mathrm{CO}$ is carbon monoxide and $\mathrm{N_2O_4}$ is dinitrogen tetroxide. The first element usually omits *mono-*; vowel combinations are often contracted in pronunciation and spelling. These prefixes belong to molecular nomenclature, not ordinary ionic naming.

An empirical formula gives the smallest whole-number atom ratio. A molecular formula gives the actual count and is an integer multiple of the empirical formula. Hydrogen peroxide has molecular formula $\mathrm{H_2O_2}$ but empirical formula HO. Ionic formulas are already expressed as simplest charge-balanced ratios unless structural conventions state otherwise.

## Coefficients and subscripts do different jobs

In

$$
\mathrm{2H_2+O_2\rightarrow2H_2O},
$$

the coefficient 2 before $\mathrm{H_2}$ means two molecules or two moles of hydrogen. The subscript 2 is part of the hydrogen molecule. Changing a coefficient changes the amount; changing a subscript changes the identity. Balancing an equation may alter coefficients only.

The product coefficient 2 multiplies the whole water formula, giving four hydrogen atoms and two oxygen atoms on the product side. Reading coefficients distributively is essential when parentheses and polyatomic groups appear.

## Notation checks

- Atomic number identifies an element and cannot change during ordinary ion formation. If the proton count changes, the species is a different element.
- Mass number belongs to one isotope; average atomic mass describes a sample's isotope population. They should not be used interchangeably in neutron calculations.
- A positive ion has fewer electrons than protons. The plus sign records missing negative charge, not added protons in an ordinary chemical process.
- Ionic formulas use the lowest charge-balanced ratio. Coefficients in an equation cannot repair a formula whose charges do not balance.
- Parentheses are used only when more than one copy of a polyatomic group is present. $\mathrm{NaNO_3}$ needs none; $\mathrm{Ca(NO_3)_2}$ does.
- A formula gives composition but may not give structure. Structural formulas, Lewis structures, and molecular geometry add information that a molecular formula leaves open.

## From percent composition to a formula

An empirical formula is obtained by turning elemental masses into mole ratios. Percentages may be treated as grams in a hypothetical $100\ \mathrm g$ sample. Divide each mass by its atomic mass, then divide all mole amounts by the smallest. The resulting ratios may need multiplication to reach whole numbers.

Suppose a compound is $40.00\%$ carbon, $6.71\%$ hydrogen, and $53.29\%$ oxygen. In $100.00\ \mathrm g$, the mole amounts are

$$
\begin{aligned}
n_C&=\frac{40.00}{12.01}=3.331,\\
n_H&=\frac{6.71}{1.008}=6.657,\\
n_O&=\frac{53.29}{16.00}=3.331.
\end{aligned}
$$

Divide by $3.331$:

$$
C:H:O=1.000:1.998:1.000.
$$

Rounding within experimental uncertainty gives the empirical formula $\mathrm{CH_2O}$. That formula could represent formaldehyde, glucose after reduction to the simplest ratio, or another compound. If the measured molar mass is $180.2\ \mathrm{g\,mol^{-1}}$, compare it with the empirical-formula mass:

$$
M_{CH_2O}=30.03\ \mathrm{g\,mol^{-1}}.
$$

The multiplier is

$$
\frac{180.2}{30.03}=6.00,
$$

so the molecular formula is $\mathrm{C_6H_{12}O_6}$. Composition and molar mass still do not establish connectivity; structural evidence is needed to distinguish isomers.

Ratios near $1.5$, $1.33$, or $1.25$ often indicate halves, thirds, or quarters rather than measurement failure. Multiply all ratios by 2, 3, or 4 respectively. Arbitrary aggressive rounding can create a formula unsupported by the data.

## The mole connects formulas to laboratory amounts

Atomic mass in unified atomic mass units and molar mass in grams per mole have the same numerical value because of how the mole and mass scale are linked. One carbon-12 atom has a mass of exactly 12 u by the historical definition of the atomic mass unit, while a mole of carbon-12 atoms has a mass very close to 12 g under the current SI definition.

A formula gives the count ratio within one entity and therefore the mole ratio within any amount. One mole of $\mathrm{Ca(NO_3)_2}$ contains one mole of calcium atoms, two moles of nitrogen atoms, and six moles of oxygen atoms. It also contains two moles of nitrate ions conceptually, although those ions are part of the solid lattice before dissolution.

For $0.250\ \mathrm{mol}$ calcium nitrate, the oxygen amount is

$$
0.250\ \mathrm{mol\ formula\ units}
\left(\frac{6\ \mathrm{mol\ O}}{1\ \mathrm{mol\ formula\ units}}\right)
=1.50\ \mathrm{mol\ O}.
$$

The particle count follows from Avogadro's constant. Counting “particles” without naming atoms, molecules, ions, or formula units is ambiguous, so the entity should accompany the numerical answer.

## Nuclear notation and chemical behavior

Isotopes of an element usually have very similar chemical behavior because they share an electron count and valence structure. They differ in mass, which can change vibrational frequencies, diffusion rates, and reaction rates slightly. Such isotope effects can reveal which bonds are changing in a reaction mechanism.

Radioactivity is a nuclear property, not a consequence of ordinary ion charge. A radioactive neutral atom and its ion remain the same radionuclide because their proton and neutron counts match. Nuclear decay can change $Z$ and therefore elemental identity; chemical ionization changes only electron count.

Isotope labels are valuable tracers because a labeled atom can be followed through a reaction without greatly changing the chemistry. Mass spectrometry distinguishes labels by mass, and radioactive isotopes can be detected by their emissions. A tracer experiment still needs atom conservation: the labeled nucleus must appear in one of the products unless a nuclear process occurs.

Average atomic masses used for molar-mass calculations assume a stated isotope composition. Enriched material can have a different molar mass from the standard tabulated value. For ordinary natural samples the table value is appropriate, but isotope-labeling experiments require the actual isotopic composition.

## Formula writing as charge conservation

Charge balance can be expressed as a small integer problem. If a cation has charge $+m$ and an anion has charge $-n$, the numbers $a$ and $b$ in a neutral formula satisfy

$$
am=bn.
$$

The smallest solution comes from the least common multiple of $m$ and $n$. For $\mathrm{Al^{3+}}$ and $\mathrm{SO_4^{2-}}$, the least common charge is 6, requiring two aluminum ions and three sulfate ions:

$$
\mathrm{Al_2(SO_4)_3}.
$$

This method is safer than crossing charge numerals mechanically because it forces reduction and keeps polyatomic ions intact. It also exposes impossible interpretations. A proposed $\mathrm{AlSO_4}$ formula would have net charge $+1$ and cannot represent a neutral simple salt.

<div className="see-also">

See also: [chemistry and measurement](/chemistry/general/chemistry-and-measurement) · [stoichiometry](/chemistry/general/stoichiometry) · [electron configurations and periodic trends](/chemistry/general/electron-configurations-and-periodic-trends) · [ionic and covalent bonding](/chemistry/general/ionic-and-covalent-bonding)

</div>
