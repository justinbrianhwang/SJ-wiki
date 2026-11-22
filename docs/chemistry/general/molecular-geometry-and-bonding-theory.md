---
title: Molecular Geometry and Bonding Theory
sidebar_position: 11
---

# Molecular Geometry and Bonding Theory

A Lewis structure gives connectivity and electron-pair bookkeeping. It does not locate the nuclei in three dimensions. Geometry matters because bond dipoles add as vectors, orbitals must overlap in particular directions, and an approaching reactant encounters one face of a molecule rather than an abstract formula. Three models divide the work: VSEPR predicts many shapes, valence-bond theory describes localized overlap, and molecular-orbital theory handles delocalization and magnetism.

## From electron domains to molecular shape

Valence-shell electron-pair repulsion theory starts with the observation that regions of valence electron density around a central atom arrange themselves to reduce repulsion. An electron domain is one lone pair or one bonding region. A single, double, or triple bond counts as one domain because all of its bonding density points toward the same neighboring atom.

Electron-domain geometry names the arrangement of every domain. Molecular geometry names only the positions of atoms. The distinction matters whenever the central atom has a lone pair.

| Domains | Electron-domain geometry | Ideal angles | Molecular shapes as lone pairs are added |
|---:|---|---|---|
| 2 | linear | $180^\circ$ | linear |
| 3 | trigonal planar | $120^\circ$ | trigonal planar, bent |
| 4 | tetrahedral | $109.5^\circ$ | tetrahedral, trigonal pyramidal, bent |
| 5 | trigonal bipyramidal | $90^\circ$, $120^\circ$, $180^\circ$ | trigonal bipyramidal, seesaw, T-shaped, linear |
| 6 | octahedral | $90^\circ$, $180^\circ$ | octahedral, square pyramidal, square planar |

The procedure is short enough to use as a check:

```mermaid
flowchart LR
  A["Draw a valid Lewis structure"] --> B["Count central-atom domains"]
  B --> C["Assign electron-domain geometry"]
  C --> D["Remove lone-pair positions from the name"]
  D --> E["Name molecular geometry"]
  E --> F["Add bond dipoles as vectors"]
```

VSEPR repulsions are not all equal. A lone pair is attracted by one nucleus rather than shared between two, so its density spreads more broadly around the central atom. The rough ordering is lone pair–lone pair greater than lone pair–bonding pair greater than bonding pair–bonding pair. Water therefore has an H–O–H angle near $104.5^\circ$, smaller than the tetrahedral ideal. Ammonia, with one lone pair instead of two, has an H–N–H angle near $107^\circ$.

Multiple bonds also occupy more space than single bonds. In formaldehyde, the H–C–H angle is slightly compressed because the C=O region repels the C–H regions more strongly. VSEPR predicts directions and qualitative distortions, not high-precision bond angles.

## Worked shapes from the Lewis structure

### Water: shape, angle, and polarity

Water has

$$
6+2(1)=8
$$

valence electrons. Two O–H bonds use four; the remaining four form two lone pairs on oxygen. Oxygen therefore has four domains, giving a tetrahedral electron-domain geometry. Only two domains contain atoms, so the molecular shape is bent.

Each O–H bond dipole points toward oxygen. Because the bonds meet at an angle rather than lying opposite one another, their vector sum is nonzero. Water is polar. Calling the molecule tetrahedral without qualification confuses its electron-domain geometry with its molecular geometry.

### Carbon dioxide and formaldehyde

Carbon dioxide has the Lewis structure $\mathrm{O=C=O}$. Carbon has two domains, since each double bond counts once. The geometry is linear, and the equal C=O dipoles cancel. The molecule is nonpolar even though its bonds are polar.

For formaldehyde, $\mathrm{CH_2O}$, carbon is central with two C–H single bonds and one C=O double bond. There are three domains, no lone pairs on carbon, and a trigonal-planar arrangement. The C=O dipole is not opposed by an equivalent bond, so the molecule has a net dipole. Comparing these two molecules separates the question “Are any bonds polar?” from “Does the whole molecule have a dipole?”

### Sulfur tetrafluoride

$\mathrm{SF_4}$ contains

$$
6+4(7)=34
$$

valence electrons. Four S–F bonds use eight electrons, the four fluorine octets require twenty-four more, and the final pair remains on sulfur. Five domains imply trigonal-bipyramidal electron geometry.

In a trigonal bipyramid, an axial site has three $90^\circ$ relationships, while an equatorial site has only two. The bulky lone pair therefore occupies an equatorial site. Removing that position from the molecular name leaves a seesaw shape. Its S–F dipoles do not cancel, so $\mathrm{SF_4}$ is polar.

### Xenon tetrafluoride

$\mathrm{XeF_4}$ has four bonding domains and two lone-pair domains around xenon. Six domains give an octahedral arrangement. The lone pairs take opposite positions to minimize their mutual repulsion; the four fluorine atoms remain in one plane as a square. The molecular geometry is square planar. With four equivalent Xe–F bonds, opposing dipoles cancel pairwise and the molecule is nonpolar.

These expanded-valence Lewis structures are useful bookkeeping. They should not be read as proof that sulfur or xenon forms six equivalent hybrid orbitals by promoting electrons into low-energy $d$ orbitals.

## Localized bonds: sigma, pi, and hybrid orbitals

Valence-bond theory treats a bond as overlap between occupied atomic or hybrid orbitals. Head-on overlap along the internuclear axis gives a sigma bond, written $\sigma$. Side-by-side overlap of parallel $p$ orbitals gives a pi bond, $\pi$, with density above and below the axis.

| Bond multiplicity | Components | Consequence for rotation |
|---|---|---|
| single | one $\sigma$ | rotation often possible without destroying overlap |
| double | one $\sigma$ and one $\pi$ | rotation would break the $\pi$ overlap |
| triple | one $\sigma$ and two perpendicular $\pi$ | short, strong bond with cylindrical overall symmetry |

The sigma framework establishes connectivity. Pi bonding explains why an alkene cannot freely rotate without crossing a substantial energy barrier: twisting the carbons makes the parallel $p$ orbitals perpendicular, eliminating their side-by-side overlap. Restricted rotation then permits distinct geometric isomers when each alkene carbon carries two different substituents.

Hybridization is a localized orbital construction that matches equivalent bond directions. Mixing one $s$ and one $p$ orbital gives two $sp$ hybrids directed $180^\circ$ apart. One $s$ plus two $p$ orbitals gives three coplanar $sp^2$ hybrids. One $s$ plus three $p$ orbitals gives four tetrahedral $sp^3$ hybrids.

In ethene, each carbon is $sp^2$ in this model. Three hybrids make sigma bonds—two C–H and one C–C—while the remaining unhybridized $p$ orbital on each carbon forms the pi bond. In ethyne, each carbon is $sp$; two unhybridized $p$ orbitals remain and form two perpendicular pi bonds.

Hybridization is inferred from geometry and bonding, not an extra experimental measurement placed before the Lewis structure. Labels such as $sp^3d$ reproduce five-domain arrangements in elementary treatments, but modern descriptions of hypervalent bonding generally do not require large central-atom $d$-orbital participation. VSEPR geometry can be retained without attaching a literal hybrid set.

## Delocalized orbitals and bond order

Molecular-orbital theory combines atomic orbitals into orbitals that can extend over an entire molecule. Constructive combination produces a bonding orbital with density between nuclei; destructive combination produces an antibonding orbital with a node between them. Antibonding orbitals are marked with an asterisk.

Bond order is estimated by

$$
\text{bond order}=\frac{N_b-N_a}{2},
$$

where $N_b$ and $N_a$ count electrons in bonding and antibonding molecular orbitals. Adding an electron to a bonding orbital raises bond order by one half; adding it to an antibonding orbital lowers bond order by one half.

### Hydrogen species as a minimal example

$\mathrm{H_2}$ places two electrons in the $\sigma_{1s}$ bonding orbital and none in $\sigma_{1s}^*$:

$$
\text{bond order}(\mathrm{H_2})=\frac{2-0}{2}=1.
$$

Ionizing it gives $\mathrm{H_2^+}$ with one bonding electron:

$$
\text{bond order}(\mathrm{H_2^+})=\frac{1-0}{2}=\frac{1}{2}.
$$

Adding an electron gives $\mathrm{H_2^-}$, with two bonding and one antibonding electron, also giving bond order one half. Filling both orbitals in hypothetical neutral $\mathrm{He_2}$ gives $(2-2)/2=0$, so the simple model predicts no ordinary covalent bond.

## Oxygen's magnetism: where the localized picture fails

A Lewis structure draws $\mathrm{O_2}$ with a double bond and paired electrons. It predicts bond order but misses a central observation: gaseous oxygen is paramagnetic and is attracted into a magnetic field.

In the valence MO description, $\mathrm{O_2}$ has eight electrons in bonding orbitals and four in antibonding orbitals:

$$
\text{bond order}=\frac{8-4}{2}=2.
$$

The two highest-energy electrons occupy separate degenerate $\pi^*$ orbitals with parallel spins under Hund's rule. These two unpaired electrons account for paramagnetism. The model also predicts useful trends. Removing one antibonding electron to form $\mathrm{O_2^+}$ raises bond order to $2.5$ and shortens the bond. Adding one to form superoxide, $\mathrm{O_2^-}$, lowers bond order to $1.5$ and lengthens it. Peroxide, $\mathrm{O_2^{2-}}$, has bond order $1$.

MO theory is more demanding than Lewis or VSEPR, but it answers questions those models were never built to answer. The models are complementary approximations rather than competitors from which one universal winner must be chosen.

## Failure modes in shape assignments

- Counting lines instead of domains gives a false tetrahedral carbon in $\mathrm{CO_2}$. Each multiple bond points toward one atom and counts as one domain.
- Omitting lone pairs changes both the geometry name and predicted angles. Recount total valence electrons before assigning a shape.
- Symmetry must be assessed after identifying all substituents. A tetrahedral molecule cancels its bond dipoles only when their magnitudes and arrangement permit cancellation; $\mathrm{CH_3Cl}$ is polar.
- A flat Lewis drawing does not mean a planar molecule. Methane is tetrahedral, and ammonia is trigonal pyramidal.
- Hybridization cannot repair an invalid Lewis structure. Establish electron count, connectivity, and domains first.
- VSEPR is least reliable for transition-metal complexes, highly delocalized species, and fine bond-angle predictions. Other electronic-structure models are better suited there.

## Geometry beyond a single central atom

Large molecules are assembled from local geometries, but local shape does not fix the whole conformation. In ethane each carbon is tetrahedral, yet rotation around the C–C sigma bond produces many conformations. In a peptide, repeated planar amide groups are joined by rotatable bonds, and the resulting three-dimensional fold depends on steric contacts and noncovalent interactions. Assigning VSEPR at every center is therefore a starting map, not a complete molecular structure.

Resonance can also alter the local picture. In an amide, nitrogen's lone pair overlaps with the adjacent carbonyl pi system. The C–N bond gains partial double-bond character, the nitrogen approaches planarity, and rotation becomes restricted. A simple domain count that treats the nitrogen as an isolated amine misses this delocalization. Experimental geometry often reveals where the localized model needs refinement.

Molecular symmetry gives a systematic dipole check. If a molecule has a symmetry operation that reverses a proposed permanent dipole while leaving the molecule unchanged, that dipole component must vanish. Equivalent bond dipoles cancel in $\mathrm{BF_3}$, $\mathrm{CO_2}$, $\mathrm{CF_4}$, and $\mathrm{SF_6}$. Substitution removes symmetry: replacing one F in $\mathrm{CF_4}$ with Cl generally leaves a net dipole even though the central geometry remains tetrahedral.

Bond angle, bond length, and bond energy answer different questions. Lone pairs mainly distort angles; bond order strongly affects length and strength; electronegativity and atomic size alter all three. No single VSEPR label supplies numerical values. Spectroscopy and diffraction provide the measurements against which the models are judged.

<div className="see-also">

See also: [ionic and covalent bonding](/chemistry/general/ionic-and-covalent-bonding) · [states of matter: liquids and solids](/chemistry/general/states-of-matter-liquids-and-solids) · [organic chemistry](/chemistry/general/organic-chemistry) · [transition metals and coordination compounds](/chemistry/general/transition-metals-and-coordination-compounds)

</div>
