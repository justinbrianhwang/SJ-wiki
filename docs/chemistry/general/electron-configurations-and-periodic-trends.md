---
title: Electron Configurations and Periodic Trends
sidebar_position: 9
---

# Electron Configurations and Periodic Trends

An electron configuration records how electrons occupy atomic orbitals in a chosen state, usually the isolated ground state. The periodic table is arranged so that recurring valence configurations appear in columns. Trends in size and energy then follow from a competition between nuclear attraction, shielding, distance, and electron-electron repulsion.

The trend arrows are summaries rather than causes. Reliable explanations start with which shell and subshell contain the relevant electrons.

## From quantum numbers to subshell capacity

Each one-electron orbital is labeled by quantum numbers. The principal quantum number $n=1,2,3,\ldots$ describes the main shell and is related to size and energy. The angular-momentum quantum number $l$ ranges from 0 to $n-1$ and identifies the subshell: $l=0,1,2,3$ correspond to $s,p,d,f$.

For a given $l$, the magnetic quantum number $m_l$ takes integer values from $-l$ through $+l$, giving $2l+1$ orbitals. The spin quantum number $m_s$ is $+1/2$ or $-1/2$. Each orbital can therefore hold two electrons of opposite spin.

| Subshell | $l$ | Number of orbitals $2l+1$ | Maximum electrons |
|---|---:|---:|---:|
| $s$ | 0 | 1 | 2 |
| $p$ | 1 | 3 | 6 |
| $d$ | 2 | 5 | 10 |
| $f$ | 3 | 7 | 14 |

The shell with principal number $n$ contains $n^2$ orbitals and can hold at most $2n^2$ electrons. This capacity does not mean all orbitals of a shell fill consecutively; orbital energies in many-electron atoms overlap between shells.

## Three rules for a ground-state configuration

The **Pauli exclusion principle** states that no two electrons in an atom have the same four quantum numbers. An orbital holds at most two electrons, and if two occupy it their spins are opposite.

**Hund's rule** says that electrons occupy degenerate orbitals singly with parallel spins before pairing. For a $p^3$ subshell, the three $p$ orbitals each receive one electron. Pairing earlier would add repulsion without an orbital-energy benefit.

The **Aufbau procedure** fills available orbitals from lower to higher energy. A common approximate order is

```text
1s
2s  2p
3s  3p
4s  3d  4p
5s  4d  5p
6s  4f  5d  6p
7s  5f  6d  7p
```

The Madelung ordering by increasing $n+l$, with lower $n$ first on a tie, reproduces much of this sequence. It is a useful mnemonic, not a fundamental theorem that predicts every neutral-atom ground state. Subshell energies depend on occupation, shielding, and electron correlation.

Orbital notation exposes Hund's rule. Nitrogen, with $1s^22s^22p^3$, has

```text
2p:  [↑] [↑] [↑]
```

whereas oxygen, $1s^22s^22p^4$, has

```text
2p:  [↑↓] [↑] [↑]
```

The precise choice of which box pairs first is arbitrary because the three isolated-atom $p$ orbitals are degenerate.

## Building configurations and checking the count

The full ground-state configuration of chlorine, $Z=17$, is

$$
\mathrm{1s^2\,2s^2\,2p^6\,3s^2\,3p^5}.
$$

The superscripts sum to 17. Noble-gas notation replaces the filled core:

$$
\mathrm{Cl:[Ne]3s^2\,3p^5}.
$$

This notation highlights the seven valence electrons responsible for chlorine's similarity to other group 17 elements.

The table's blocks correspond to the subshell being filled. The $s$ block spans two columns, the $p$ block six, the transition-metal $d$ block ten, and the inner-transition $f$ block fourteen. Helium is placed with the noble gases because its filled $1s^2$ shell gives noble-gas chemistry even though its configuration belongs formally to the $s$ block.

For main-group elements, valence electrons usually occupy the highest-$n$ $s$ and $p$ subshells. Transition-metal chemistry also involves nearby $(n-1)d$ electrons, so a simple highest-shell definition is less adequate there.

### Worked example: selenium and its common ion

Selenium has $Z=34$. Starting from the argon core with 18 electrons, fill $4s^2$, $3d^{10}$, then $4p^4$:

$$
\mathrm{Se:[Ar]4s^2\,3d^{10}\,4p^4}.
$$

The count is

$$
18+2+10+4=34.
$$

For $\mathrm{Se^{2-}}$, add two electrons to the partly filled $4p$ subshell:

$$
\mathrm{Se^{2-}:[Ar]4s^2\,3d^{10}\,4p^6=[Kr]}.
$$

The ion has 36 electrons and a filled valence shell. The configuration describes an isolated ion; in a solid or molecule, bonding changes the orbital picture, though the electron count remains essential.

## Exceptions near half-filled and filled $d$ subshells

The simplest filling prediction for chromium is $\mathrm{[Ar]4s^23d^4}$, but its observed ground-state configuration is commonly written

$$
\mathrm{Cr:[Ar]4s^1\,3d^5}.
$$

Copper is

$$
\mathrm{Cu:[Ar]4s^1\,3d^{10}}
$$

rather than $\mathrm{[Ar]4s^23d^9}$. The $4s$ and $3d$ energies are close, and the balance of electron correlation and subshell occupation favors the observed arrangements. Saying only that “half-filled and filled subshells are stable” is a mnemonic, not a general quantitative explanation. Several heavier transition elements have additional exceptions.

Known configurations should be consulted when exact spectroscopy or transition-metal chemistry depends on them. The Aufbau sequence remains effective for locating the relevant subshells and counting electrons.

## Forming ions: remove from the outer shell first

Main-group cations lose electrons from the highest occupied principal shell. Sodium, $\mathrm{[Ne]3s^1}$, becomes $\mathrm{Na^+:[Ne]}$. Anions fill the valence subshell: chlorine gains one electron to reach $\mathrm{[Ar]}$.

Transition-metal ions cause a common reversal. Neutral iron is conventionally written

$$
\mathrm{Fe:[Ar]4s^2\,3d^6},
$$

but the $4s$ electrons are removed before $3d$ electrons when cations form:

$$
\begin{aligned}
\mathrm{Fe^{2+}}&:\mathrm{[Ar]3d^6},\\
\mathrm{Fe^{3+}}&:\mathrm{[Ar]3d^5}.
\end{aligned}
$$

Although $4s$ fills before $3d$ in the neutral-atom construction, the relative orbital energies change after $3d$ occupation. “Last written, first removed” is unsafe because configurations may be written in different orders; remove from the highest principal quantum number first for these common cations.

### Worked example: cobalt(III) and unpaired electrons

Neutral cobalt, $Z=27$, is

$$
\mathrm{Co:[Ar]4s^2\,3d^7}.
$$

To form $\mathrm{Co^{3+}}$, remove two $4s$ electrons and one $3d$ electron:

$$
\mathrm{Co^{3+}:[Ar]3d^6}.
$$

For a free $d^6$ ion, Hund filling across five degenerate $d$ orbitals gives

```text
3d:  [↑↓] [↑] [↑] [↑] [↑]
```

so four electrons are unpaired in that isolated-ion model. In a coordination complex, ligand-field splitting can instead favor a low-spin arrangement with fewer unpaired electrons. Electron count alone is not enough to assign magnetism in transition-metal complexes.

Species with one or more unpaired electrons are paramagnetic and attracted into a magnetic field. Species with all electrons paired are diamagnetic and weakly repelled. This connection provides experimental evidence about configurations, although molecules and solids may require molecular-orbital or band descriptions.

## Effective nuclear charge and shielding

Every electron is attracted to the nucleus and repelled by other electrons. A rough one-electron summary is the effective nuclear charge

$$
Z_{\mathrm{eff}}=Z-S,
$$

where $S$ represents shielding. This is a model quantity rather than one universal integer. Core electrons shield valence electrons strongly; electrons in the same shell shield one another less completely. Penetrating orbitals spend more time near the nucleus and experience greater attraction. For a fixed $n$, penetration generally follows $s\gt p\gt d\gt f$.

Across a period, $Z$ increases one unit at a time while added valence electrons enter roughly the same shell. Shielding does not rise enough to cancel the added nuclear charge, so $Z_{\mathrm{eff}}$ generally increases. Down a group, the valence shell has higher $n$, is farther from the nucleus, and is screened by additional core shells.

These two comparisons—effective attraction across a period and shell number down a group—account for many broad periodic patterns.

## Atomic and ionic radii

An atom has no sharp outer boundary, so atomic radius depends on its operational definition: covalent radius, metallic radius, or van der Waals radius. Trend comparisons should use compatible definitions.

Across a period, atomic radius generally decreases as increasing effective nuclear charge contracts the valence cloud. Down a group, radius increases because a new occupied shell outweighs the greater nuclear charge.

Cations are smaller than their parent atoms. Electron loss reduces repulsion and may remove the outer shell entirely. Anions are larger because added electrons increase repulsion within the valence shell while nuclear charge is unchanged.

For an isoelectronic series, all species have the same electron count, so proton count decides the attraction. Consider

$$
\mathrm{O^{2-},\ F^-,\ Ne,\ Na^+,\ Mg^{2+}}.
$$

Each has ten electrons, but nuclear charge rises from 8 to 12. Radius therefore decreases in the order

$$
\mathrm{O^{2-}>F^->Ne>Na^+>Mg^{2+}}.
$$

Applying the ordinary left-to-right neutral-atom trend without first noticing equal electron counts often reverses this reasoning.

## Ionization energy and its local exceptions

The first ionization energy is the energy required to remove an electron from a gaseous ground-state atom:

$$
\mathrm{X(g)\rightarrow X^+(g)+e^-}.
$$

It generally rises across a period because valence electrons experience increasing attraction, and falls down a group because the removed electron occupies a larger, more shielded shell. Successive ionization energies always increase because an electron is removed from an increasingly positive species.

A large jump in successive ionization energies signals that all valence electrons have been removed and the next electron belongs to a core shell. For magnesium, the large jump occurs after the second ionization, consistent with $\mathrm{[Ne]3s^2}$ and a common $2+$ ion.

The across-period rise has instructive exceptions. Boron's first removed electron is in $2p$, which is higher in energy and less penetrating than beryllium's $2s$ electron, so boron has a lower first ionization energy than a naive monotonic trend predicts. Oxygen has one paired $2p$ orbital, and repulsion within that pair makes electron removal easier than from nitrogen's half-filled $2p^3$ arrangement. These exceptions support the subshell model rather than overturning it.

## Electron affinity and electronegativity

Electron affinity describes the energy change when a gaseous atom gains an electron. Sign conventions vary among texts: some report the energy released as a positive magnitude, while thermodynamic conventions report an exothermic energy change as negative. The convention must be checked before ranking numerical values.

Halogens generally have strongly favorable first electron affinities because one added electron completes a $p$ subshell. Noble gases resist addition into a new shell. Second electron addition to an already negative ion is unfavorable in the gas phase because of electrostatic repulsion, even when a $2-$ ion is stabilized in an ionic lattice.

Electronegativity is a relative measure of an atom's attraction for shared electrons in a bond. It is not an energy measured for an isolated atom in exactly the same way as ionization energy. Electronegativity generally rises across a period and falls down a group; fluorine is highest on the common Pauling scale. Bond polarity depends on the difference between bonded atoms, while molecular polarity also depends on geometry.

## Metallic character and periodic reactivity

Metals tend to lose electrons and form cations, so metallic character increases as ionization energy falls: generally down a group and toward the left. Nonmetallic behavior increases toward the upper right. Metalloids occupy a broad boundary and show intermediate or context-dependent properties.

Reactivity does not follow one arrow for every family. Alkali metals become more reactive down the group because electron loss becomes easier. Halogen oxidizing strength generally decreases down the group because gaining an electron becomes less favorable and bond and solvation effects change. A periodic trend must be tied to the particular reaction rather than used as a universal ranking of “reactivity.”

| Property | General trend across a period | General trend down a group | Main reason |
|---|---|---|---|
| atomic radius | decreases | increases | increasing $Z_{\mathrm{eff}}$ versus added shells |
| first ionization energy | increases | decreases | attraction and distance of removed electron |
| electronegativity | increases | decreases | attraction for bonding electron density |
| metallic character | decreases | increases | ease of electron loss |

## A disciplined way to rank species

1. Count electrons and identify charge. Isoelectronic species should be compared by proton count.
2. Locate the highest occupied shell. An added shell usually dominates a down-group comparison.
3. For species in the same shell, compare effective nuclear charge.
4. Check subshell occupation and pairing when ranking ionization energies or electron affinities near known exceptions.
5. State whether the comparison concerns atoms, free ions, or ions in a bonded environment.

For Na, Mg, and K, potassium has an additional occupied shell and is largest. Sodium and magnesium share period 3, but magnesium has greater nuclear charge with similar core shielding, so it is smaller:

$$
\mathrm{Mg<Na<K}.
$$

The explanation is more durable than memorizing the direction of an arrow.

## Configuration checks

- Sum every superscript and compare with the required electron count after charge is included.
- Apply Hund's rule within one set of degenerate orbitals; it does not mean filling a higher-energy subshell before pairing in a lower one.
- Remove transition-metal electrons from the highest principal shell before the lower-$n$ $d$ subshell.
- Treat the Aufbau sequence as a strong working rule with known exceptions, not an infallible energy law.
- Explain periodic comparisons with shell number, shielding, penetration, and nuclear attraction. “Because it is farther right” only restates the table position.
- Do not transfer isolated-atom unpaired-electron counts directly to coordination complexes without considering ligand-field splitting.

## Spectra as evidence for discrete energies

Electron configurations are supported by spectroscopy rather than inferred only from table shape. When an atom absorbs or emits light, photon energy matches a difference between allowed states:

$$
\Delta E=h\nu=\frac{hc}{\lambda}.
$$

Discrete spectral lines show that atomic energy changes are quantized. Many-electron spectra are complicated by electron repulsion, spin-orbit coupling, and multiple possible terms, so a configuration does not specify one energy by itself.

Photoelectron spectroscopy removes electrons with known photon energy and measures their kinetic energy. The binding-energy pattern separates shells and subshells; peak areas approximately reflect electron counts after sensitivity factors are considered. Sudden changes in binding energy across a series give experimental support to shell structure and effective nuclear charge.

Configurations are therefore compact assignments within a model tested by spectra, magnetism, and chemical behavior. They are not little planetary paths. An orbital is a quantum state whose squared wavefunction gives a probability distribution.

<div className="see-also">

See also: [quantum theory of atoms](/chemistry/general/quantum-theory-of-atoms) · [ionic and covalent bonding](/chemistry/general/ionic-and-covalent-bonding) · [main-group elements](/chemistry/general/main-group-elements) · [transition metals and coordination compounds](/chemistry/general/transition-metals-and-coordination-compounds)

</div>
