---
title: Gases
sidebar_position: 6
---

# Gases

Gas particles occupy a container but are usually separated by distances much larger than their molecular dimensions. That separation allows a simple equation to connect pressure, volume, temperature, and amount over a wide range. Kinetic molecular theory gives the particle-level picture; deviations from it show where intermolecular attraction and finite molecular size become important.

## Pressure is momentum transfer over area

Pressure is force per area:

$$
P=\frac{F}{A}.
$$

Gas molecules strike a wall and reverse part of their momentum. The accumulated impulses from enormous numbers of collisions produce a steady macroscopic pressure. More frequent collisions or larger momentum changes increase it.

The SI pressure unit is the pascal, $1\ \mathrm{Pa}=1\ \mathrm{N\,m^{-2}}$. Several other units remain common:

$$
1\ \mathrm{atm}=101325\ \mathrm{Pa}=101.325\ \mathrm{kPa}=760\ \mathrm{torr}.
$$

The equality with $760\ \mathrm{mmHg}$ is the conventional introductory conversion; torr and millimeter of mercury are nearly identical in ordinary calculations. A bar is exactly $100\ \mathrm{kPa}$ and is not the same as one atmosphere.

A barometer compares atmospheric pressure with the weight of a liquid column. A manometer compares a gas pressure with atmosphere or vacuum. In an open-end manometer, the higher liquid level is on the lower-pressure side. Rather than memorizing a sign, follow the pressure physically from one arm to the other: moving downward through the manometer liquid increases pressure by $\rho gh$, and moving upward decreases it.

## The experimental gas laws

Several simple relationships appear when variables are held fixed.

**Boyle's law:** at constant amount and temperature,

$$
PV=\text{constant}.
$$

Reducing volume gives particles less distance between wall collisions, so pressure rises inversely. Doubling pressure halves volume for an ideal gas under these constraints.

**Charles's law:** at constant amount and pressure,

$$
\frac{V}{T}=\text{constant}.
$$

Heating increases molecular kinetic energy. To keep pressure fixed, the container volume must expand so collision frequency per area is reduced. Temperature must be in kelvin; a Celsius ratio has no physical meaning because Celsius zero is arbitrary.

**Amontons's law:** at constant amount and volume,

$$
\frac{P}{T}=\text{constant}.
$$

Heating a rigid sealed container raises pressure as collisions become more forceful.

**Avogadro's law:** at fixed pressure and temperature,

$$
\frac{V}{n}=\text{constant}.
$$

Adding particles requires greater volume to keep the wall-collision rate per area unchanged.

Combining these proportionalities gives

$$
V\propto\frac{nT}{P},
$$

or the ideal gas law,

$$
PV=nRT.
$$

The gas constant is one physical constant expressed in different unit systems. Useful values include

$$
R=0.082057\ \mathrm{L\,atm\,mol^{-1}\,K^{-1}}
$$

and

$$
R=8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}
=8.314\ \mathrm{L\,kPa\,mol^{-1}\,K^{-1}}.
$$

Because $1\ \mathrm{J}=1\ \mathrm{Pa\,m^3}$, the energy and pressure-volume forms are consistent.

For a fixed gas amount between two states, dividing two ideal-gas equations cancels $nR$:

$$
\frac{P_1V_1}{T_1}=\frac{P_2V_2}{T_2}.
$$

Use this combined relation only when the amount is unchanged. A leak, reaction, or phase change requires explicit treatment of $n$.

## Worked example: heating a flexible gas sample

A balloon contains $2.00\ \mathrm L$ of gas at $20.0\ ^\circ\mathrm C$ and $0.950\ \mathrm{atm}$. It rises to a region where the pressure is $0.700\ \mathrm{atm}$ and the temperature is $-5.0\ ^\circ\mathrm C$. Estimate its new volume, assuming the gas amount is fixed and the balloon remains flexible.

Convert temperatures:

$$
T_1=20.0+273.15=293.15\ \mathrm K,
$$

$$
T_2=-5.0+273.15=268.15\ \mathrm K.
$$

Solve the combined gas law for $V_2$:

$$
V_2=V_1\frac{P_1}{P_2}\frac{T_2}{T_1}.
$$

Substitute:

$$
V_2=(2.00\ \mathrm L)
\left(\frac{0.950}{0.700}\right)
\left(\frac{268.15}{293.15}\right)
=2.48\ \mathrm L.
$$

Lower pressure tends to expand the balloon; lower temperature tends to contract it. The pressure effect is larger here, so the net volume increases. Treating Celsius values as a ratio would predict a nonsensical negative factor.

## Using $PV=nRT$ to find amount, molar mass, or density

The ideal gas equation can solve for any one state variable when the others are known. A $2.50\ \mathrm L$ flask contains oxygen at $0.950\ \mathrm{atm}$ and $27.0\ ^\circ\mathrm C$. Converting temperature gives $300.15\ \mathrm K$, and

$$
\begin{aligned}
n&=\frac{PV}{RT}\\
&=\frac{(0.950\ \mathrm{atm})(2.50\ \mathrm L)}
{(0.082057\ \mathrm{L\,atm\,mol^{-1}\,K^{-1}})(300.15\ \mathrm K)}\\
&=0.0965\ \mathrm{mol}.
\end{aligned}
$$

Near room temperature and one atmosphere, a mole of ideal gas occupies roughly 24 L, so about one tenth mole in 2.5 L is a useful scale check.

Substitute $n=m/M$ into the ideal gas law:

$$
PV=\frac{m}{M}RT.
$$

Solving for molar mass,

$$
M=\frac{mRT}{PV}.
$$

Since density $d=m/V$,

$$
d=\frac{PM}{RT}.
$$

At the same temperature and pressure, ideal-gas density is proportional to molar mass. At fixed composition, density rises with pressure and falls with temperature.

### Worked example: identifying a gas by molar mass

A $0.422\ \mathrm g$ gas sample occupies $250.0\ \mathrm{mL}$ at $1.00\ \mathrm{atm}$ and $25.0\ ^\circ\mathrm C$. Find its molar mass.

Convert volume and temperature:

$$
V=0.2500\ \mathrm L,
\qquad
T=298.15\ \mathrm K.
$$

Then

$$
\begin{aligned}
M&=\frac{mRT}{PV}\\
&=\frac{(0.422\ \mathrm g)(0.082057\ \mathrm{L\,atm\,mol^{-1}\,K^{-1}})(298.15\ \mathrm K)}
{(1.00\ \mathrm{atm})(0.2500\ \mathrm L)}\\
&=41.3\ \mathrm{g\,mol^{-1}}.
\end{aligned}
$$

This value narrows possible identities but does not uniquely identify the substance; several gases or mixtures could have similar average molar mass.

## Gas stoichiometry

Gas volume can be converted to moles with $PV=nRT$ and then used in a balanced reaction. At equal temperature and pressure, Avogadro's law also makes gas-volume ratios equal to mole ratios for reacting gases.

For

$$
\mathrm{2H_2(g)+O_2(g)\rightarrow2H_2O(g)},
$$

two volumes of hydrogen react with one volume of oxygen and produce two volumes of water vapor when all volumes are compared at the same temperature and pressure. If the water condenses, its liquid volume cannot be included in that gas-volume ratio.

### Worked example: hydrogen produced from a metal

Magnesium reacts with excess acid:

$$
\mathrm{Mg(s)+2H^+(aq)\rightarrow Mg^{2+}(aq)+H_2(g)}.
$$

What volume of dry hydrogen at $25.0\ ^\circ\mathrm C$ and $0.980\ \mathrm{atm}$ forms from $0.500\ \mathrm g$ Mg? Use $M_{Mg}=24.305\ \mathrm{g\,mol^{-1}}$.

Moles of magnesium are

$$
n_{Mg}=\frac{0.500\ \mathrm g}{24.305\ \mathrm{g\,mol^{-1}}}
=0.0206\ \mathrm{mol}.
$$

The reaction ratio is $1:1$, so

$$
n_{H_2}=0.0206\ \mathrm{mol}.
$$

Now solve the gas law for volume:

$$
\begin{aligned}
V&=\frac{nRT}{P}\\
&=\frac{(0.0206)(0.082057)(298.15)}{0.980}\\
&=0.514\ \mathrm L.
\end{aligned}
$$

The adjective “dry” matters. If hydrogen were collected over water, its partial pressure rather than the total pressure would enter this calculation.

## Mixtures and partial pressure

For an ideal mixture, Dalton's law is

$$
P_{\mathrm{tot}}=\sum_iP_i.
$$

Each component obeys $P_iV=n_iRT$ in the common volume. Dividing by $P_{\mathrm{tot}}V=n_{\mathrm{tot}}RT$ gives

$$
P_i=X_iP_{\mathrm{tot}},
\qquad
X_i=\frac{n_i}{n_{\mathrm{tot}}}.
$$

Partial pressure depends on component amount, temperature, and volume, not directly on molecular identity. In a mixture with $0.200$ mol He, $0.300$ mol Ne, and $0.500$ mol Ar at $1.80\ \mathrm{atm}$, total amount is $1.000$ mol. Thus

$$
X_{Ar}=\frac{0.500}{1.000}=0.500
$$

and

$$
P_{Ar}=(0.500)(1.80)=0.900\ \mathrm{atm}.
$$

When gas is collected by displacing water, the gas above the liquid contains both product gas and water vapor:

$$
P_{\mathrm{total}}=P_{\mathrm{gas}}+P_{H_2O}.
$$

Therefore,

$$
P_{\mathrm{gas}}=P_{\mathrm{total}}-P_{H_2O}.
$$

The water vapor pressure must be taken at the collection temperature. If liquid levels inside and outside the collection vessel differ, the hydrostatic pressure difference must also be included before subtracting water vapor.

### Worked example: gas collected over water

Hydrogen is collected over water at $25.0\ ^\circ\mathrm C$. The total pressure is $755\ \mathrm{torr}$, the water vapor pressure is $23.8\ \mathrm{torr}$, and the gas volume is $315\ \mathrm{mL}$. Find dry hydrogen moles.

First remove the water contribution:

$$
P_{H_2}=755-23.8=731\ \mathrm{torr}.
$$

Convert pressure and volume:

$$
P_{H_2}=\frac{731}{760}=0.962\ \mathrm{atm},
\qquad
V=0.315\ \mathrm L.
$$

At $T=298.15\ \mathrm K$,

$$
\begin{aligned}
n_{H_2}&=\frac{PV}{RT}\\
&=\frac{(0.962)(0.315)}{(0.082057)(298.15)}\\
&=0.0124\ \mathrm{mol}.
\end{aligned}
$$

Using total pressure would overestimate hydrogen because it would assign water's share of pressure to hydrogen.

## Kinetic molecular theory

The ideal kinetic model assumes that gas particles move continuously and randomly, have negligible volume compared with the container, exert no intermolecular forces except during collisions, and collide elastically. Their mean translational kinetic energy depends only on absolute temperature:

$$
\left\langle E_{\mathrm{trans}}\right\rangle=\frac{3}{2}RT
$$

per mole, or $3k_BT/2$ per molecule.

All ideal gases at the same temperature have the same average translational kinetic energy, regardless of molar mass. Since kinetic energy contains mass times speed squared, lighter molecules must move faster on average. The root-mean-square speed is

$$
u_{\mathrm{rms}}=\sqrt{\frac{3RT}{M}},
$$

where $M$ must be in $\mathrm{kg\,mol^{-1}}$ when SI units are used.

A gas has a distribution of speeds rather than one common speed. Raising temperature shifts the distribution toward higher speeds and broadens it. At one temperature, a lighter gas has a distribution shifted toward higher speeds relative to a heavier gas.

## Effusion and diffusion

Effusion is escape through an opening small compared with the molecular mean free path. Graham's law compares ideal effusion rates at the same temperature and pressure:

$$
\frac{r_1}{r_2}=\sqrt{\frac{M_2}{M_1}}.
$$

Hydrogen effuses about four times as fast as oxygen because

$$
\frac{r_{H_2}}{r_{O_2}}
=\sqrt{\frac{32.00}{2.016}}
=3.98.
$$

For the same amount to escape, time is inversely proportional to rate, so the time ratio is reversed.

Diffusion is the net mixing that results from random molecular motion. Collisions with other molecules make diffusion through a gas much slower than bare molecular speeds might suggest. Graham's square-root relation is often used as a rough comparison, but effusion and diffusion are not the same experiment.

## Why real gases deviate

The ideal model neglects two effects. Molecules occupy finite volume, reducing the free space available for translational motion. They also attract one another at moderate separation, which can reduce the force with which they strike the wall.

At low pressure, particles are far apart and both corrections are small. At high temperature, kinetic energy weakens the relative importance of attraction. Ideal behavior is therefore best at low pressure and high temperature, especially for small, weakly interacting molecules.

The compressibility factor measures deviation:

$$
Z=\frac{PV}{nRT}.
$$

$Z=1$ for an ideal gas. Attractions can produce $Z\lt 1$ over an intermediate pressure range; excluded volume tends to produce $Z\gt 1$ at high pressure.

The van der Waals equation introduces both corrections:

$$
\left(P+a\frac{n^2}{V^2}\right)(V-nb)=nRT.
$$

The $a$ term corrects for attractions that lower observed pressure, and $b$ corrects for excluded molecular volume. The parameters depend on the gas. This equation is historically important and qualitatively useful, though more accurate equations of state are used for demanding work.

Near condensation, a gas is far from ideal because intermolecular attractions are central to phase formation. More calculator digits in $PV=nRT$ cannot repair a model failure.

## Checks before accepting a gas calculation

- Convert temperature to kelvin before using a ratio or the ideal gas law.
- Match pressure and volume units to the chosen value of $R$; do not mix kPa with an atmosphere-based constant.
- Confirm that the gas amount stays fixed before using a combined gas-law equation that cancels $n$.
- For collection over water, subtract water vapor pressure and account for unequal liquid levels if present.
- Distinguish partial pressure from total pressure. Each component uses its own $P_i$ in a single shared volume.
- Use gas stoichiometry through moles unless every gas volume is measured at the same temperature and pressure.
- Expect ideal behavior to worsen at high pressure, low temperature, and near a phase transition.

## Mean free path and collision frequency

Although molecular speeds are hundreds of meters per second, a molecule in an ordinary-pressure gas does not travel across a room without interruption. It collides repeatedly with other molecules. The mean free path is the average distance between collisions and grows as pressure falls.

For a hard-sphere model,

$$
\lambda=\frac{k_BT}{\sqrt{2}\pi d^2P},
$$

where $d$ is an effective molecular diameter. The inverse pressure dependence explains why low-pressure systems can enter a molecular-flow regime in which molecules collide with walls more often than with one another. Vacuum technology, effusion, and gas transport depend on which collision regime applies.

At higher pressure, diffusion is slowed by frequent intermolecular collisions even though individual thermal speeds remain high. Odor spreading across a room is governed by diffusion and air currents, not by one molecule flying ballistically from source to observer.

## Stoichiometry when temperature and pressure are not shared

Gas-volume coefficients equal mole coefficients only when the compared volumes refer to the same temperature and pressure. If conditions differ, each volume must first be converted to amount.

Suppose $1.00\ \mathrm L$ hydrogen at $300\ \mathrm K$ and $1.00\ \mathrm{atm}$ reacts with $1.00\ \mathrm L$ oxygen at $600\ \mathrm K$ and $1.00\ \mathrm{atm}$. Equal volumes do not contain equal amounts because their temperatures differ:

$$
n_{H_2}=\frac{(1.00)(1.00)}{(0.082057)(300)}
=0.0406\ \mathrm{mol},
$$

$$
n_{O_2}=\frac{(1.00)(1.00)}{(0.082057)(600)}
=0.0203\ \mathrm{mol}.
$$

The amounts are exactly in the required $2:1$ ratio for water formation. Comparing the raw one-liter volumes would incorrectly suggest a $1:1$ mixture and excess oxygen.

Standard molar volume also needs stated conditions. At $0\ ^\circ\mathrm C$ and $1\ \mathrm{atm}$, the ideal value is about $22.414\ \mathrm{L\,mol^{-1}}$. At $25\ ^\circ\mathrm C$ and $1\ \mathrm{bar}$ it is about $24.79\ \mathrm{L\,mol^{-1}}$. Quoting “22.4 liters per mole” without temperature and pressure hides the condition.

## Critical behavior and liquefaction

Compression can liquefy a gas only below its critical temperature. Above that temperature, thermal motion prevents a distinct liquid-gas phase boundary no matter how much pressure is applied. At the critical point, liquid and gas densities converge and the interface disappears.

A substance above its critical temperature and pressure is a supercritical fluid. It has no liquid-gas boundary and can combine liquid-like density with gas-like transport properties. Density can be tuned strongly with pressure near the critical region, which is useful in extraction and processing.

The ideal gas law cannot represent condensation because it contains no attractive forces and predicts one smooth gas state. Van der Waals-type models introduce a loop related to phase separation, but actual coexistence requires equal temperature, pressure, and chemical potential between phases. Phase behavior therefore needs thermodynamics beyond a corrected gas-volume calculation.

## Buoyancy and gas density

A gas parcel rises when its average density is lower than that of the surrounding fluid. From

$$
d=\frac{PM}{RT},
$$

lower molar mass or higher temperature lowers ideal-gas density at a shared pressure. Helium balloons rise because helium's molar mass is far below that of air. Hot-air balloons rise because heating lowers the density of the enclosed air while the flexible envelope remains near atmospheric pressure.

Humidity also lowers air density at fixed temperature and pressure. Water vapor has molar mass about $18\ \mathrm{g\,mol^{-1}}$, lower than the average molar mass of dry air near $29\ \mathrm{g\,mol^{-1}}$. Replacing some nitrogen and oxygen with water vapor therefore reduces average molar mass. The effect is modest but opposite to the intuition that humid air must be heavier because it “contains water.”

<div className="see-also">

See also: [stoichiometry](/chemistry/general/stoichiometry) · [states of matter, liquids, and solids](/chemistry/general/states-of-matter-liquids-and-solids) · [solutions and colligative properties](/chemistry/general/solutions-and-colligative-properties) · [thermodynamics and free energy](/chemistry/general/thermodynamics-and-free-energy)

</div>
