---
title: Transition Metals and Coordination Compounds
sidebar_position: 23
---

# Transition Metals and Coordination Compounds

Transition-metal chemistry is unusually varied because the metal's valence $d$ orbitals lie close in energy to the outer $s$ orbital. Several oxidation states may be accessible, and the energies of the $d$ orbitals respond strongly to the surrounding ligands. Replacing water by ammonia or chloride can change a complex's geometry, color, magnetic behavior, redox potential, and substitution rate while leaving the central metal unchanged.

The useful bookkeeping has three layers: determine oxidation state and $d$ count, determine how donor atoms are arranged, then place the $d$ electrons into the resulting ligand-field levels. Skipping the first layer is the source of many later errors.

## Why the d block has variable chemistry

A transition element is commonly defined as an element whose atom has an incomplete $d$ subshell or that forms at least one cation with an incomplete $d$ subshell. Zinc has a filled $3d^{10}$ subshell in both Zn and $\mathrm{Zn^{2+}}$, so it sits in the d block but does not meet that definition. Its complexes are still studied alongside transition-metal complexes because the same coordination ideas apply.

When a first-row transition metal forms a cation, the $4s$ electrons are removed before the $3d$ electrons. The neutral-atom filling order does not give the ionization order: once the $3d$ orbitals are occupied, their relative energy falls below that of $4s$. For example,

$$
\mathrm{Fe:[Ar],4s^2 3d^6}
\qquad\longrightarrow\qquad
\mathrm{Fe^{3+}:[Ar],3d^5}.
$$

The $d$ count follows directly from the group number and oxidation state for ordinary complexes. Cobalt is in group 9, so cobalt(III) is $d^6$; nickel(II), from group 10, is $d^8$. This shortcut counts metal-centered $d$ electrons and should not be confused with the total valence-electron count used in organometallic chemistry.

Variable oxidation states arise because the $ns$ and $(n-1)d$ electrons have comparable energies. Early metals often reach high oxidation states, especially with oxygen or fluorine. Later first-row metals more often favor $+2$ and $+3$. Which state is stable depends on ligands, solvent, pH, and possible lattice or solvation energies; a bare list of “common oxidation states” cannot predict every reaction.

## Reading a coordination formula

A coordination entity contains a central metal atom or ion bound to ligands. Each ligand supplies at least one electron pair to a metal-ligand bond, so the elementary Lewis description treats the ligand as a Lewis base and the metal as a Lewis acid. The atoms directly attached to the metal form the inner coordination sphere. Counterions outside square brackets provide charge balance and can usually dissociate independently in solution.

The **coordination number** counts donor atoms, not ligand molecules. Water, ammonia, chloride, and cyanide are monodentate: each binds through one atom. Ethylenediamine, often abbreviated en, is bidentate and supplies two nitrogen donors. Ethylenediaminetetraacetate, EDTA, can bind through six donor atoms. A ligand that attaches at several sites forms chelate rings.

Common ligand charges are worth learning, but charge balance is safer than memory:

| Ligand | Formula | Charge | Typical donor atom |
|---|---|---:|---|
| aqua | $\mathrm{H_2O}$ | 0 | O |
| ammine | $\mathrm{NH_3}$ | 0 | N |
| carbonyl | $\mathrm{CO}$ | 0 | C |
| chlorido | $\mathrm{Cl^-}$ | $-1$ | Cl |
| cyanido | $\mathrm{CN^-}$ | $-1$ | usually C |
| hydroxido | $\mathrm{OH^-}$ | $-1$ | O |
| oxalato | $\mathrm{C_2O_4^{2-}}$ | $-2$ | two O atoms |

### Worked example: formula, oxidation state, and name

Consider $\mathrm{[Co(NH_3)_5Cl]Cl_2}$. The two external chloride ions require the bracketed ion to have charge $+2$. If cobalt has oxidation state $x$,

$$
x+5(0)+(-1)=+2,
$$

so $x=+3$. Cobalt(III) is $d^6$. The complex has six donor atoms—five nitrogen atoms and one chloride—so its coordination number is 6, suggesting an octahedral arrangement.

Ligands are named before the metal and alphabetized without regard to multiplicative prefixes. Neutral $\mathrm{NH_3}$ is *ammine*, with two m's; coordinated $\mathrm{Cl^-}$ is *chlorido* in current IUPAC usage. The compound is **pentaamminechloridocobalt(III) chloride**. Many older textbooks use *chloro*, a naming difference rather than a structural one.

If the coordination entity is anionic, the metal name takes an *-ate* ending, sometimes based on a Latin name. Thus $\mathrm{K_4[Fe(CN)_6]}$ is potassium hexacyanidoferrate(II). Charge balance gives

$$
x+6(-1)=-4,
$$

so the iron oxidation state is $+2$, not $+4$.

## Geometry and the isomers it permits

Coordination number restricts geometry but does not always determine it. Two-coordinate complexes are often linear. Six-coordinate complexes are commonly octahedral. Four-coordinate complexes demand more evidence because both tetrahedral and square-planar arrangements are common.

| Coordination number | Frequent geometry | Representative ion | Structural consequence |
|---:|---|---|---|
| 2 | linear | $\mathrm{[Ag(NH_3)_2]^+}$ | ligands are $180^\circ$ apart |
| 4 | tetrahedral | $\mathrm{[ZnCl_4]^{2-}}$ | all four sites equivalent |
| 4 | square planar | $\mathrm{[PtCl_4]^{2-}}$ | adjacent and opposite sites differ |
| 6 | octahedral | $\mathrm{[Co(NH_3)_6]^{3+}}$ | six equivalent vertices in the ideal shape |

**Constitutional isomers** differ in which atoms are connected. Linkage isomers occur when an ambidentate ligand binds through different atoms, as in nitro versus nitrito coordination. Ionization isomers exchange an inner-sphere ligand with a counterion. Hydrate isomers differ in whether water lies inside or outside the coordination sphere.

**Stereoisomers** keep the same bonds but differ in spatial arrangement. A square-planar $\mathrm{MA_2B_2}$ complex has cis and trans forms. Octahedral $\mathrm{MA_4B_2}$ also has cis and trans forms. For octahedral $\mathrm{MA_3B_3}$, *fac* places three identical ligands on one triangular face, whereas *mer* places them along a meridian with two mutually trans. Some chelate complexes form non-superimposable mirror images. These optical isomers have identical ordinary chemical formulas but interact differently with plane-polarized light and with other chiral substances.

Geometry can matter biologically. Cisplatin and transplatin have the same ligand set around Pt(II), but only the cis geometry places the two labile chloride ligands suitably for the characteristic DNA cross-links associated with cisplatin's anticancer action.

## How ligands split the d orbitals

In a free gaseous metal ion, the five $d$ orbitals have the same energy. An octahedral ligand arrangement approaches along the Cartesian axes. The $d_{x^2-y^2}$ and $d_{z^2}$ orbitals point toward those ligands and are destabilized more strongly; together they form the upper $e_g$ set. The $d_{xy}$, $d_{xz}$, and $d_{yz}$ orbitals point between the axes and form the lower $t_{2g}$ set.

```text
higher energy       eg       dx2-y2, dz2
                    ──       ──────────
                     │  Δo
                     │
lower energy        t2g      dxy, dxz, dyz
                   ──────    ─────────────
```

The weighted average energy, called the barycenter, stays unchanged in the simple crystal-field model. Each $t_{2g}$ electron contributes $-0.4\Delta_o$ and each $e_g$ electron contributes $+0.6\Delta_o$. The octahedral crystal-field stabilization energy is therefore

$$
\mathrm{CFSE}=(-0.4n_{t_{2g}}+0.6n_{e_g})\Delta_o,
$$

before pairing-energy terms are added.

Electrons must choose between pairing in $t_{2g}$ and occupying the higher $e_g$ level. If the splitting $\Delta_o$ is smaller than the pairing cost, the complex is **high spin**. If $\Delta_o$ is larger, it is **low spin**. The distinction matters mainly for octahedral $d^4$ through $d^7$ configurations. Strong-field ligands such as CO and $\mathrm{CN^-}$ tend to produce larger splittings than weak-field ligands such as halides, though the metal identity and oxidation state matter too.

In a tetrahedral field, no ligand lies directly on an axis. The ordering reverses: the two-orbital $e$ set lies below the three-orbital $t_2$ set. Tetrahedral splitting $\Delta_t$ is smaller than the corresponding octahedral splitting, so tetrahedral complexes are usually high spin. Square-planar splitting is more uneven and often strongly stabilizes a paired $d^8$ arrangement.

### Worked example: high-spin and low-spin iron(III)

$\mathrm{Fe^{3+}}$ is $d^5$. In a weak octahedral field, the first three electrons singly occupy $t_{2g}$ and the next two singly occupy $e_g$:

$$
(t_{2g})^3(e_g)^2.
$$

All five electrons are unpaired. The CFSE is

$$
3(-0.4\Delta_o)+2(+0.6\Delta_o)=0.
$$

In a strong field, the occupancy is

$$
(t_{2g})^5(e_g)^0.
$$

There is one unpaired electron, and the orbital contribution is $5(-0.4\Delta_o)=-2.0\Delta_o$, accompanied by two electron-pairing costs relative to five separate orbitals. The comparison between that stabilization and the pairing cost decides the spin state.

For many first-row complexes, a useful spin-only estimate of magnetic moment is

$$
\mu_{so}=\sqrt{n(n+2)}\,\mu_B,
$$

where $n$ is the number of unpaired electrons. High-spin $d^5$ gives $\sqrt{35}=5.92\,\mu_B$; low-spin $d^5$ gives $\sqrt{3}=1.73\,\mu_B$. Measured values can deviate because the formula neglects orbital contributions and magnetic coupling.

### Worked example: two nickel(II) geometries

Nickel(II) is $d^8$. In $\mathrm{[NiCl_4]^{2-}}$, chloride is weak-field and the tetrahedral splitting is modest. The ion is tetrahedral with two unpaired electrons and is paramagnetic. In $\mathrm{[Ni(CN)_4]^{2-}}$, cyanide produces a much stronger field; the complex is square planar, all electrons are paired, and it is diamagnetic.

The metal and oxidation state alone therefore do not fix magnetism. Ligand identity changes orbital splitting, which can change both occupancy and geometry.

## Color comes from selective absorption

If the energy gap between occupied and unoccupied orbitals matches a visible-light photon, absorption can promote an electron. The relation

$$
\Delta E=h\nu=\frac{hc}{\lambda}
$$

means a larger splitting corresponds to a higher-frequency, shorter-wavelength absorption. The observed color is made from wavelengths transmitted or reflected, so it is roughly complementary to the absorbed color.

This model explains trends but has limits. Selection rules make many $d$-$d$ transitions weak. Complexes with $d^0$ or $d^{10}$ configurations have no ordinary $d$-$d$ transition, yet they may still be colored. Charge-transfer transitions move electron density between ligand and metal orbitals and are often much more intense. Permanganate's strong purple color, for example, should not be described as a simple $d$-$d$ excitation of $\mathrm{Mn^{VII}}$, which is $d^0$.

## Chelation, formation equilibria, and ligand exchange

Complex formation is an equilibrium. For a metal ion $M$ and ligand $L$,

$$
M+nL\rightleftharpoons ML_n,
$$

the overall formation constant is

$$
\beta_n=\frac{[ML_n]}{[M][L]^n}
$$

in the concentration approximation. Large formation constants explain why adding a ligand can dissolve a sparingly soluble salt or shift a redox potential. Conditional values may depend strongly on pH because protonation can remove ligand donor sites from availability.

Multidentate ligands often form more stable complexes than comparable monodentate ligands. The chelate effect has a substantial entropy contribution: replacing several bound solvent or monodentate molecules with one multidentate ligand can release more independent particles into solution. Ring size, donor-metal matching, and strain also affect stability, so denticity alone is not a complete predictor.

Thermodynamic stability must be separated from kinetic lability. A complex may have a large formation constant yet exchange ligands rapidly, or it may be thermodynamically vulnerable but react slowly. Terms such as *labile* and *inert* describe rates; *stable* and *unstable* describe equilibrium.

## Substitution and redox can change different layers

A ligand-substitution reaction replaces one donor without necessarily changing the metal oxidation state. When water in a hydrated metal ion is replaced by ammonia, charge balance may remain the same while ligand-field splitting and color change. A redox reaction changes electron count and may then trigger a geometry or ligand change because the new oxidation state has different preferences.

Substitution pathways are often described as dissociative, associative, or interchange. In a dissociative limit, a ligand leaves before the entering ligand binds, temporarily lowering coordination number. In an associative limit, the incoming ligand begins bonding first and temporarily raises coordination number. Steric crowding, electron count, and geometry influence which route is accessible. Square-planar substitution is especially sensitive to ligands already attached to the metal; the trans effect describes how one ligand can accelerate replacement opposite itself.

Oxidation state, coordination number, and overall complex charge answer different questions. In hexacyanidoferrate(II), iron is formally $+2$, six donor atoms give coordination number 6, and the coordination entity has charge $-4$. None can be inferred from either of the others alone.

## Limits of the crystal-field picture

Crystal-field theory treats ligands as point charges or dipoles and explains splitting patterns with little machinery. It does not describe metal-ligand covalency explicitly. Ligand-field and molecular-orbital treatments allow ligand orbitals to mix with metal orbitals, explaining why pi-donor and pi-acceptor ligands alter splitting and bonding.

Carbon monoxide is a useful case. It donates electron density from a carbon lone pair into the metal and can accept electron density back into ligand antibonding orbitals. That back-bonding strengthens the metal-carbon bond while weakening the internal carbon-oxygen bond. The simple label “strong-field ligand” records the observed splitting tendency but omits the bonding mechanism.

Real complexes also depart from ideal geometry. Uneven orbital occupancy can drive a Jahn-Teller distortion that removes degeneracy and lowers electronic energy. Octahedral copper(II), a $d^9$ case, commonly shows elongated or compressed metal-ligand distances rather than six identical bonds. Such distortion affects spectra and reactivity and warns against reading an ideal polyhedron too literally.

## Bookkeeping checks

- Counterions outside brackets affect total charge but not coordination number.
- Oxidation state is a formal charge assignment; it need not equal the measured charge localized on the metal.
- Remove $ns$ electrons before $(n-1)d$ electrons when forming transition-metal cations.
- Four-coordinate does not automatically mean tetrahedral. A $d^8$ ion with strong-field ligands may be square planar.
- Count unpaired electrons only after choosing geometry, splitting pattern, and, where relevant, spin state.
- A compound's observed color is not the wavelength it absorbs, and an intense color may arise from charge transfer rather than a $d$-$d$ transition.

<div className="see-also">

See also: [electron configurations and periodic trends](/chemistry/general/electron-configurations-and-periodic-trends) · [molecular geometry and bonding theory](/chemistry/general/molecular-geometry-and-bonding-theory) · [solubility and complex-ion equilibria](/chemistry/general/solubility-and-complex-ion-equilibria) · [electrochemistry](/chemistry/general/electrochemistry) · [molecular symmetry and group theory](/chemistry/physical-chemistry/molecular-symmetry-and-group-theory)

</div>
