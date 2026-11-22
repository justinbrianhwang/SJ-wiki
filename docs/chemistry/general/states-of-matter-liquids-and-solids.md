---
title: States of Matter, Liquids, and Solids
sidebar_position: 12
---

# States of Matter, Liquids, and Solids

Macroscopic phase behavior follows from particle motion, intermolecular attraction, and packing. Gases are highly compressible, liquids retain volume while flowing, and solids resist changes in shape through ordered lattices, networks, or other strong cohesive structures.

## Attractions behind liquid properties

Intermolecular forces act between particles; covalent and ionic bonds hold atoms together within a molecular or formula-unit description. Mixing those levels leads to bad boiling-point and phase-change arguments.

| Interaction | Where it appears | Main comparison |
|---|---|---|
| London dispersion | all atoms and molecules | grows with polarizability and contact area |
| Dipole-dipole | polar molecules | depends on molecular dipole and orientation |
| Hydrogen bonding | systems with suitable H-N, H-O, or H-F donors and lone-pair acceptors | a strong, directional dipole interaction |
| Ion-dipole | ions in polar solvents | central to solvation of many salts |

Stronger attractions generally raise boiling point, viscosity, and surface tension while lowering vapor pressure at a fixed temperature. Molecular shape matters because it changes how closely and over how much area molecules can approach one another.

## Reading a phase diagram

A phase diagram maps the stable phase at each pressure and temperature. Lines mark conditions where two phases coexist, the triple point joins all three coexistence lines, and the liquid-vapor boundary ends at the critical point. Water's solid-liquid line slopes negatively because ordinary ice is less dense than liquid water.

Boiling occurs when a liquid's vapor pressure equals the external pressure. It is therefore not fixed at $100^\circ\mathrm{C}$ for every substance or even for water at every pressure.

## Heating through a phase transition

```text
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

Within a single phase, added heat raises temperature according to the relevant heat capacity. Along an idealized plateau, energy changes the phase while temperature remains constant. A phase transition changes particle arrangement without changing chemical identity.

The flat segments should not be read as “no energy change.” The energy is latent heat used to overcome or establish intermolecular attractions rather than to raise the average kinetic energy.

## Estimating vapor pressure at a second temperature

For a liquid over a modest temperature range, the integrated Clausius-Clapeyron equation is

$$
\ln\left(\frac{P_2}{P_1}\right)
=-\frac{\Delta H_{vap}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right).
$$

Suppose $P_1=100.0\ \mathrm{mmHg}$ at 300 K and $\Delta H_{vap}=35.0\ \mathrm{kJ\,mol^{-1}}$. At 320 K,

$$
\ln\left(\frac{P_2}{100.0}\right)
=-\frac{35000}{8.314}\left(\frac{1}{320}-\frac{1}{300}\right)
=0.877.
$$

Therefore $P_2/P_1=e^{0.877}=2.40$ and $P_2\approx240\ \mathrm{mmHg}$. The increased vapor pressure agrees with the higher temperature.

## From a unit cell to bulk density

A unit cell is the repeating unit of a crystal lattice, and the coordination number counts nearest neighbors around a lattice site. For a cubic unit cell,

$$
\rho=\frac{ZM}{N_Aa^3},
$$

where $Z$ is the number of formula units or atoms per cell, $M$ is molar mass, and $a$ is the cell edge.

For a face-centered cubic metal, $Z=4$. With $a=408\ \mathrm{pm}=4.08\times10^{-8}\ \mathrm{cm}$ and $M=107.9\ \mathrm{g\,mol^{-1}}$,

$$
V_{cell}=a^3=6.79\times10^{-23}\ \mathrm{cm^3},
$$

$$
m_{cell}=\frac{4(107.9)}{6.022\times10^{23}}
=7.17\times10^{-22}\ \mathrm{g},
$$

so

$$
\rho=10.6\ \mathrm{g\,cm^{-3}}.
$$

The length conversion must occur before cubing. An error of ten in the edge becomes an error of one thousand in the volume.

## Vapor pressure is a dynamic equilibrium

Molecules in a liquid have a distribution of kinetic energies. Some surface molecules have enough energy and a favorable direction to escape. In a closed container, vapor molecules also collide with the surface and condense. Equilibrium vapor pressure is reached when evaporation and condensation rates are equal, not when molecular motion stops.

Raising temperature shifts the energy distribution so that more molecules can escape, increasing vapor pressure. Stronger intermolecular attraction raises the energy cost of escape and lowers vapor pressure at the same temperature. A liquid with high vapor pressure is described as volatile and normally has a lower normal boiling point than a less volatile liquid under the same comparison.

Surface area changes the rate at which equilibrium is approached but not the equilibrium vapor pressure at a fixed temperature. An open container may never establish equilibrium because vapor is continually removed. Evaporation then cools the remaining liquid because escaping molecules carry above-average kinetic energy.

### Comparing boiling points without a single-factor slogan

Compare propane, dimethyl ether, and ethanol, which have similar molar masses. Propane is nonpolar and relies on dispersion forces. Dimethyl ether is polar, so it adds dipole–dipole attraction. Ethanol can both donate and accept hydrogen bonds, producing the strongest cohesive interactions of the three and the highest boiling point. Similar size makes the interaction-type comparison informative.

Within a homologous nonpolar series, polarizability and contact area become more important. A longer electron cloud is more easily distorted, strengthening dispersion. Branching often lowers boiling point among isomers by reducing surface contact. Molecular mass alone is therefore an incomplete explanation.

Hydrogen bonding requires a donor hydrogen directly attached to N, O, or F and a suitable acceptor. An ether oxygen accepts hydrogen bonds from water but an ether molecule has no O–H bond and cannot donate one to another ether. Merely containing hydrogen and an electronegative atom elsewhere in the formula is insufficient.

## Reading phase boundaries thermodynamically

Crossing a coexistence line changes the stable phase. Moving horizontally changes temperature at fixed pressure; moving vertically changes pressure at fixed temperature. Below the triple-point pressure, a liquid phase is unavailable and heating a solid produces sublimation. Beyond the critical point, liquid and gas merge continuously into a supercritical fluid, so there is no liquid–vapor boundary to cross.

The slope of a coexistence line follows the Clapeyron relation

$$
\frac{dP}{dT}=\frac{\Delta H}{T\Delta V}.
$$

For melting, $\Delta H$ is positive. Most substances expand on melting, giving a positive solid–liquid slope. Ice Ih contracts on melting, so $\Delta V$ is negative and the line slopes downward. Increasing pressure near the ordinary melting point then favors the denser liquid and lowers the melting temperature slightly.

The integrated Clausius–Clapeyron expression assumes $\Delta H_{vap}$ is roughly constant and vapor behaves ideally over the interval. It is best used over modest temperature ranges. Temperatures must be absolute because reciprocals of Celsius temperatures have no thermodynamic meaning.

## What added heat does

Within one phase,

$$
q=mc\Delta T.
$$

At a transition,

$$
q=n\Delta H_{trans}.
$$

To heat ice below zero to steam above $100^\circ\mathrm{C}$ at one atmosphere, split the path into warming ice, melting, warming liquid, vaporizing, and warming vapor. Each segment uses its own heat capacity or transition enthalpy. Combining the whole temperature change with one heat capacity omits the latent heat terms, commonly the largest contribution.

During an ideal constant-pressure transition, temperature remains fixed while potential energy and molecular arrangement change. The original text's flat segments represent energy absorption, not “no energy change.” Real heating curves can slope or broaden because of heat loss, mixtures, or nonuniform temperature.

## Solid structure and the forces that hold it

| Solid type | Structural particles | Dominant cohesion | Typical behavior |
|---|---|---|---|
| molecular | molecules | intermolecular forces | often soft with relatively low melting point |
| ionic | cations and anions | electrostatic attraction | brittle, high-melting, conducting when ions move |
| metallic | metal atoms/ions and delocalized electrons | metallic bonding | conducting, malleable, ductile |
| covalent network | atoms joined throughout a network | covalent bonds | hard or high-melting; properties vary with topology |
| atomic | individual atoms | usually dispersion | low melting for noble-gas solids |

The categories predict broad behavior, not exact rankings. Graphite is a covalent-network solid that conducts along its sheets and cleaves readily between them. Some molecular solids have extensive hydrogen bonding. Crystal defects also matter: vacancies, substituted atoms, and dislocations can control conductivity and mechanical strength without changing the ideal lattice name.

## Counting particles in cubic cells

An atom at a cube corner is shared by eight cells and contributes $1/8$; a face-centered atom is shared by two and contributes $1/2$; a body-centered atom lies wholly inside one cell. Simple cubic, body-centered cubic, and face-centered cubic cells therefore contain 1, 2, and 4 net atoms respectively.

Their coordination numbers are 6, 8, and 12. Coordination and packing efficiency rise from simple cubic to the close-packed FCC structure, but a material's actual structure depends on electronic energetics as well as geometrical density. The unit-cell edge also relates to atomic radius differently in each lattice, so a formula must be derived from the direction along which atoms touch rather than memorized without its geometry.

Crystalline solids possess long-range repeating order. Amorphous solids lack that periodic order over long distances, though they can retain local structure. Glass softens over a range rather than melting sharply like an ideal pure crystal; calling it a very slow room-temperature liquid is misleading.

## Comparisons that need a stated model

- Identify molecular, ionic, metallic, covalent-network, or atomic solids before comparing their properties.
- Do not infer a higher vapor pressure from stronger intermolecular forces; the direction is lower at fixed temperature.
- Distinguish heat that changes temperature from latent heat that changes phase.
- Include the external pressure when discussing boiling.
- Real crystals contain defects, and measured densities may differ slightly from an ideal unit-cell calculation.

## Metastable phases and nucleation

A phase diagram identifies the lowest-free-energy bulk phase, but a system can remain metastable when conversion requires forming a new interface. Supercooled water remains liquid below its freezing point until a sufficiently large ice nucleus forms. Once nucleation begins, growth can be rapid. Scratching a container, adding a seed crystal, or introducing dust can lower the nucleation barrier without changing the equilibrium melting temperature.

The same distinction appears in vapor condensation and crystal polymorphs. A less stable crystal form may appear first because it nucleates more easily, then transform later. Cooling rate affects particle size and order: rapid cooling can trap an amorphous structure, while slow cooling gives particles time to arrange into a crystal. Equilibrium and kinetics must therefore be stated separately when discussing observed phase.

Capillary action combines adhesion to a surface, cohesion within a liquid, and surface tension. Water rises in clean glass when attraction to the wall favors wetting; mercury is depressed because cohesion dominates. The curved meniscus creates a pressure difference whose magnitude grows as radius decreases, explaining why narrow pores show stronger capillary effects.

Pressure has little effect on condensed-phase volume because liquids and solids are far less compressible than gases. It can still shift phase equilibria when the competing phases have different molar volumes. The denser phase is favored by increased pressure, as expressed by the $P\Delta V$ contribution to free energy.

Viscosity measures resistance to flow and generally falls as a liquid is heated because molecules escape local attractive cages more readily. Surface tension measures the free-energy cost of creating surface area. Both respond to intermolecular forces, but they are distinct properties and need not rank every substance identically.

At the critical point, the liquid and vapor densities converge and the surface between them disappears. Above it, “gas” and “liquid” are no longer separate equilibrium phases. A supercritical fluid can combine gas-like transport with liquid-like density, with properties tuned continuously by pressure and temperature.

<div className="see-also">

See also: [gases](/chemistry/general/gases) · [solutions and colligative properties](/chemistry/general/solutions-and-colligative-properties) · [molecular geometry and bonding theory](/chemistry/general/molecular-geometry-and-bonding-theory) · [main-group elements](/chemistry/general/main-group-elements)

</div>
