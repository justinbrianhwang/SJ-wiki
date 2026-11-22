---
title: Biochemistry and Polymer Materials
sidebar_position: 25
---

# Biochemistry and Polymer Materials

Macromolecules link small building blocks into structures whose behavior depends on far more than the repeat-unit formula. Chain length, sequence, branching, cross-links, stereochemistry, and packing all matter. Synthetic polymers exploit those variables to make materials; biological macromolecules use sequence and folding to store information, recognize partners, and catalyze reactions.

The useful common idea is constrained flexibility. A long chain has many possible conformations, but covalent geometry and interactions with neighboring groups or solvent make some conformations much more favorable than others.

## Monomers, repeat units, and polymerization routes

A **monomer** is a small molecule capable of entering a polymerization. The **repeat unit** is the structural pattern repeated in the finished chain. They are not always written identically. Ethene is $\mathrm{CH_2{=}CH_2}$, but its polyethylene repeat unit is $\mathrm{-CH_2-CH_2-}$ because the carbon-carbon double bond has been consumed.

Chain-growth polymerization commonly proceeds through initiation, propagation, and termination. In free-radical polymerization, an initiator produces a radical, the radical adds across a monomer double bond, and the new chain-end radical adds further monomers. Termination removes the active center by combination or disproportionation. Monomer disappears gradually while high-molar-mass chains can appear early.

Step-growth polymerization allows any two molecules bearing suitable functional groups to react: monomer with monomer, oligomer with monomer, or oligomer with oligomer. Polyesters can form when diols react with dicarboxylic acids, eliminating water as ester links form. High conversion is needed before very long chains become abundant because every missed functional-group reaction leaves chains shorter.

The older labels **addition polymer** and **condensation polymer** describe whether the repeat-unit formation retains all monomer atoms or eliminates a small molecule. They overlap imperfectly with the kinetic labels chain-growth and step-growth. Some step-growth reactions add without eliminating a small molecule, so it is safer to state which feature is being classified.

| Feature | Typical chain-growth case | Typical step-growth case |
|---|---|---|
| Reactive site | active chain end | functional groups on many species |
| Growth event | monomer adds to active chain | any compatible molecules join |
| High molar mass | can appear at low conversion | requires very high conversion |
| Common example | polyethylene from ethene | polyester from a diol and diacid |

## A polymer sample contains a distribution

Except for specially controlled systems, polymer molecules do not all have the same length. The number-average molar mass weights every molecule equally:

$$
M_n=\frac{\sum_i N_iM_i}{\sum_i N_i},
$$

where $N_i$ molecules have molar mass $M_i$. The weight-average molar mass gives heavier molecules more influence:

$$
M_w=\frac{\sum_i N_iM_i^2}{\sum_i N_iM_i}.
$$

The dispersity is

$$
Đ=\frac{M_w}{M_n}.
$$

For any nonnegative distribution, $M_w\ge M_n$, so $Đ\ge1$. A value of exactly 1 would mean all chains have the same molar mass. Reporting a single “molecular weight” without the averaging method can hide important differences between samples.

For a long linear chain, the number-average degree of polymerization is approximately

$$
DP_n\approx\frac{M_n}{M_{\mathrm{repeat}}}.
$$

End-group masses have been neglected. That is harmless for thousands of repeat units but significant for a short oligomer.

### Worked example: average molar masses from a distribution

Suppose a sample contains 100 chains of $10{,}000\ \mathrm{g\,mol^{-1}}$ and 50 chains of $30{,}000\ \mathrm{g\,mol^{-1}}$.

The number average is

$$
\begin{aligned}
M_n&=\frac{100(10{,}000)+50(30{,}000)}{100+50}\\
&=\frac{2{,}500{,}000}{150}\\
&=16{,}667\ \mathrm{g\,mol^{-1}}.
\end{aligned}
$$

The weight average is

$$
\begin{aligned}
M_w&=\frac{100(10{,}000)^2+50(30{,}000)^2}
{100(10{,}000)+50(30{,}000)}\\
&=\frac{5.50\times10^{10}}{2.50\times10^6}\\
&=22{,}000\ \mathrm{g\,mol^{-1}}.
\end{aligned}
$$

Therefore,

$$
Đ=\frac{22{,}000}{16{,}667}=1.32.
$$

The heavy chains are only one third of the molecules but contribute more strongly to $M_w$ because mass appears squared in its numerator.

### Worked example: polyethylene chain length

The polyethylene repeat-unit molar mass is

$$
M_{\mathrm{C_2H_4}}=2(12.01)+4(1.008)=28.05\ \mathrm{g\,mol^{-1}}.
$$

For $M_n=7.01\times10^4\ \mathrm{g\,mol^{-1}}$,

$$
DP_n\approx\frac{7.01\times10^4}{28.05}=2.50\times10^3.
$$

An average chain therefore contains about 2500 repeat units. Its contour length is not its ordinary end-to-end size: carbon-carbon bonds rotate, so an unconstrained chain coils rather than remaining fully extended.

## How molecular architecture becomes a material property

Linear chains can align and crystallize in ordered regions, although most common polymers are partly crystalline and partly amorphous. Branching can hinder close packing. Cross-links join chains into a network and prevent them from sliding freely past one another. A lightly cross-linked rubber can stretch and recover; a densely cross-linked thermoset is rigid and does not melt into independently flowing chains.

Thermoplastics soften on heating because their chains are held together mainly by intermolecular forces and can eventually move past one another. Thermosets contain covalent networks and generally degrade rather than melt cleanly. Elastomers combine flexible chains with enough cross-linking to restore shape after deformation.

The glass-transition temperature, $T_g$, marks a change in mobility of amorphous chain segments. Below $T_g$, segmental motion is slow and the material tends to be glassy; above it, the amorphous regions are more rubbery. $T_g$ is not the same as a crystalline melting point. A partly crystalline polymer may show both a glass transition for amorphous regions and melting of crystallites at a higher temperature.

Strong intermolecular attractions, stiff backbones, and bulky groups that restrict rotation often raise $T_g$. Flexible linkages and some plasticizers lower it by increasing segmental mobility. Molar mass matters strongly at low chain length and less once chains are sufficiently long.

Stereochemistry also changes packing. Different arrangements of side groups along a chain can make an otherwise identical repeat-unit composition crystallize differently. Copolymer sequence—random, alternating, block, or graft—can create separate nanoscale domains or distribute properties along a chain.

Conducting polymers need a conjugated backbone with overlapping orbitals, but conjugation alone is insufficient for high conductivity. Charge carriers are introduced by oxidation or reduction, often called doping in this context, and morphology controls how readily charge moves between chains.

## Biomolecules use the same chemistry with sequence control

Four broad classes recur in biochemistry:

| Class | Main building blocks | Characteristic linkage or organization | Selected roles |
|---|---|---|---|
| carbohydrates | monosaccharides | glycosidic bonds | fuel, storage, structural fibers, recognition |
| lipids | fatty acids, glycerol, sterol frameworks | ester bonds and hydrophobic assembly | membranes, energy storage, signaling |
| proteins | amino acids | peptide bonds | catalysis, transport, mechanics, signaling |
| nucleic acids | nucleotides | phosphodiester bonds | information storage and transfer |

Lipids are grouped by solubility and biological role rather than by one polymer architecture. A triacylglycerol is not a long sequence polymer like a protein. Phospholipids self-assemble into bilayers because their polar head groups interact with water while their nonpolar tails avoid it.

The hydrophobic effect is not a special bond between nonpolar groups. Water forms an organized environment around exposed nonpolar surfaces; aggregation reduces the total nonpolar surface in contact with water and releases some constrained water molecules. The resulting free-energy change helps drive membrane assembly and protein folding.

## Proteins: sequence becomes a folded chemical environment

An amino acid contains an amino group, a carboxyl group, and a side chain attached to the alpha carbon. Near neutral pH, free amino acids commonly exist as zwitterions with a protonated amino group and deprotonated carboxyl group.

A peptide bond forms between the carboxyl group of one amino acid and the amino group of another. The backbone has direction: sequences are conventionally written from the amino, or N, terminus to the carboxyl, or C, terminus. Because resonance gives the peptide C–N bond partial double-bond character, the peptide unit is approximately planar and rotation is restricted.

Protein structure is described at several levels. Primary structure is amino-acid sequence. Secondary structures such as alpha helices and beta sheets arise largely from backbone hydrogen bonding. Tertiary structure is the three-dimensional arrangement of one polypeptide chain. Quaternary structure describes the association of multiple chains.

No single force “causes” folding. Hydrophobic burial, hydrogen bonds, ionic interactions, dispersion forces, disulfide bonds, and metal coordination can all contribute. Folding is a free-energy balance that includes the protein and solvent. The native structure is dynamic rather than a rigid model.

Enzymes accelerate reactions by lowering the activation free energy. Binding positions reacting groups, stabilizes charge distributions, and can supply acidic, basic, nucleophilic, or metal-ion chemistry. An enzyme changes the rates of forward and reverse reactions but does not change the reaction's equilibrium constant.

Denaturation disrupts higher-order structure without necessarily cleaving peptide bonds. Heat, extreme pH, or solvents can disturb the interactions maintaining the fold. Loss of structure often means loss of activity, even though the amino-acid sequence remains intact.

## Carbohydrates and lipids

Monosaccharides contain several hydroxyl groups and a carbonyl group in their open-chain form. In water, many cyclize to hemiacetals or hemiketals. Glycosidic bonds join sugar units, and their stereochemistry changes biological properties. Starch and cellulose are both glucose polymers, but their different glycosidic linkages produce different shapes and digestibility.

Fatty acids contain a carboxyl group and hydrocarbon chain. Double bonds, especially cis double bonds, introduce bends that disrupt tight packing and often lower melting temperature. Saturated chains pack more regularly. In phospholipid bilayers, tail composition helps tune membrane fluidity along with sterols and temperature.

Hydrolysis reverses many biological condensation linkages by adding the elements of water. The reaction may be thermodynamically favorable yet slow without acid, base, or an enzyme. Favorability and rate remain separate questions.

## DNA and RNA: direction, complementarity, and information

A nucleotide contains a sugar, phosphate, and nitrogenous base. Phosphodiester bonds connect the $3'$ hydroxyl of one sugar to the $5'$ phosphate of the next, giving every nucleic-acid strand a $5'\rightarrow3'$ direction. Standard double-stranded DNA uses antiparallel strands: one runs $5'\rightarrow3'$ while its partner runs $3'\rightarrow5'$.

Watson–Crick pairing places A with T and G with C in DNA. RNA generally uses U in place of T. For

$$
5'\text{-ATGCCGA-}3',
$$

the aligned DNA complement is

$$
3'\text{-TACGGCT-}5'.
$$

If the complement must also be written $5'\rightarrow3'$, reverse the aligned sequence:

$$
5'\text{-TCGGCAT-}3'.
$$

There are three A–T pairs and four G–C pairs. Counting two hydrogen bonds for each A–T pair and three for each G–C pair gives

$$
3(2)+4(3)=18
$$

hydrogen bonds in the idealized pairing picture. Duplex stability cannot be inferred from that count alone. Base stacking, neighboring sequence, salt concentration, strand length, mismatches, and temperature all contribute.

Replication and transcription depend on complementarity, but base pairing does not copy information by itself. Enzymes select substrates, catalyze phosphodiester-bond formation, and proofread to varying degrees. The sequence is stored in covalent structure; hydrogen bonding allows the strands to recognize complementary partners reversibly.

## Boundaries of the simplified models

- A repeat unit is not automatically identical to the monomer. Check which bonds were broken or formed during polymerization.
- Molar mass is an average over a distribution. State whether it is $M_n$, $M_w$, or another measured average.
- Similar molar mass does not guarantee similar material behavior. Branching, crystallinity, tacticity, additives, and processing history can dominate.
- Condensation and step-growth are related terms but not exact synonyms. One refers to atom balance; the other refers to the growth mechanism.
- Biomolecular shape cannot be predicted from covalent connectivity alone. Solvent and many weak interactions contribute to the favored ensemble.
- Nucleic-acid complements need direction labels. An aligned antiparallel complement and a reverse complement contain the same bases in opposite written order.
- Enzymes affect rate, not the equilibrium position. More product at a fixed early time does not imply a changed equilibrium constant.

## Degradation, recycling, and lifetime

Polymer lifetime depends on which bonds are vulnerable and whether water, oxygen, light, heat, or mechanical stress can reach them. Polyesters and polyamides contain hydrolyzable links, though useful degradation may still be slow in a dry or cool environment. Carbon-carbon backbones resist hydrolysis but can undergo oxidation or photochemical chain scission.

Chain scission lowers molar mass and often weakens a material before much mass is lost. Cross-linking during aging can instead make a polymer harder and more brittle. Additives such as antioxidants and ultraviolet absorbers slow selected pathways but may migrate or be consumed.

Mechanical recycling melts and reshapes suitable thermoplastics, but mixed polymers, pigments, fillers, and prior degradation reduce product quality. Chemical recycling aims to recover monomers or other feedstocks by depolymerization or conversion. Its feasibility depends on separation, energy use, reaction selectivity, and product value; a polymer being chemically degradable does not guarantee an efficient recycling process.

Biodegradation requires organisms or enzymes able to attack the material under the disposal conditions. A polymer that degrades in an industrial composting facility may persist in cold soil or seawater. Labels such as biodegradable therefore need a specified environment and time scale.

## Free energy links self-assembly and folding

Macromolecular organization is governed by Gibbs energy,

$$
\Delta G=\Delta H-T\Delta S.
$$

Folding a chain reduces its conformational entropy, which opposes a unique compact structure. Favorable interactions within the chain and changes in solvent organization compensate. The resulting folded state is favored only when the total free-energy balance is negative under the given conditions.

Self-assembly remains dynamic. Lipids exchange, protein conformations fluctuate, and nucleic-acid base pairs open transiently. Cooperative behavior can make a transition appear sharp even though individual molecular events remain reversible. Heating a protein or DNA duplex shifts the ensemble rather than flipping every molecule at one identical temperature.

Crowding, salt, pH, and cosolvents alter the balance by changing electrostatic screening, solvent activity, or exposed surface. A sequence that folds in one buffer may aggregate or unfold in another. Structural claims therefore belong with conditions.

## Sequence errors have different consequences

A substitution in a protein sequence may change little if it preserves size and chemical character at an exposed position, or it may destroy function if it disrupts an active site or buried packing. Insertions and deletions can be more disruptive because they alter every downstream position in a translated reading frame when the nucleotide count is not a multiple of three.

For synthetic copolymers, sequence is usually less exact but still consequential. A block copolymer can segregate into domains because long runs of unlike units avoid one another, whereas a random copolymer distributes the same compositions along each chain. Composition alone cannot predict morphology without sequence architecture.

<div className="see-also">

See also: [organic chemistry](/chemistry/general/organic-chemistry) · [molecular geometry and bonding theory](/chemistry/general/molecular-geometry-and-bonding-theory) · [chemical kinetics](/chemistry/general/chemical-kinetics) · [thermodynamics and free energy](/chemistry/general/thermodynamics-and-free-energy)

</div>
