---
title: Chemical and Phase Equilibrium
sidebar_position: 16
---

# Chemical and Phase Equilibrium

Equilibrium tells us where a reacting or multiphase system tends after constraints are fixed. Energy balances can predict an adiabatic flame temperature only if product composition is known; at high temperature, dissociation changes that composition. Phase equilibrium determines whether species partition between liquid and vapor, dissolve in liquids, or condense from gases.

At fixed temperature and pressure, a closed reacting system reaches equilibrium by minimizing Gibbs free energy. The same principle produces equilibrium constants for reactions and equality of chemical potentials between phases.

## Constraints come before composition

- **Chemical equilibrium** occurs when a reacting mixture has no net tendency to change composition at the specified constraints.
- **Phase equilibrium** occurs when phases coexist without net mass transfer of each species between phases.
- The **Gibbs function** is $G=H-TS$. At constant temperature and pressure, equilibrium corresponds to minimum Gibbs function.
- **Chemical potential** is the partial molar Gibbs function of a species. Equality of chemical potential across phases is the phase-equilibrium condition.
- The **extent of reaction** $\xi$ tracks composition changes according to stoichiometric coefficients.
- The **equilibrium constant** relates equilibrium composition to temperature for a specified reaction written in a specified direction.
- **Reaction quotient** has the same form as the equilibrium expression but uses current, not necessarily equilibrium, composition.
- **Dissociation** is the breaking of molecules into simpler species at high temperature, such as $CO_2$ into $CO$ and $O_2$ fragments in combustion products.
- **Henry's law** relates gas solubility in a liquid to gas partial pressure for dilute solutions.
- **Raoult's law** approximates ideal liquid-vapor equilibrium: $y_iP=x_iP_{sat,i}(T)$.

Equilibrium constants depend on temperature, not on the initial amount of material. Pressure affects equilibrium composition when the number of gas moles changes because mole fractions and partial pressures enter the reaction quotient.
An equilibrium model should state the constraints, the allowed species and phases, the property model, and the composition basis before any numbers are substituted. Similar-looking formulas answer different questions: a reaction quotient determines reaction direction, an equilibrium constant fixes the equilibrium condition, and a phase relation constrains how species partition. Write the balances and equilibrium relations first, then insert property data.

Equilibrium expressions usually use mole fractions or activities, whereas equipment balances may use mass or molar flow. Convert between those bases explicitly and keep the reaction extent on the same molar basis as the stoichiometric coefficients.

Equilibrium is dynamic at the molecular scale. Forward and reverse processes continue, but their macroscopic rates are equal, so average composition no longer changes. A catalyst speeds the approach in both directions and does not change the equilibrium state at fixed constraints.

## Gibbs and chemical-potential conditions

At fixed $T$ and $P$, a reacting mixture satisfies

$$
(dG)_{T,P}\le0
$$

for spontaneous change, with equality at equilibrium. For a reaction

$$
\sum_i \nu_i A_i=0,
$$

the equilibrium condition is

$$
\sum_i \nu_i \mu_i=0.
$$

Write species changes in terms of reaction extent as

$$
dn_i=\nu_i\,d\xi,
$$

with positive stoichiometric coefficients for products and negative ones for reactants. At fixed $T$ and $P$,

$$
dG=\sum_i\mu_i\,dn_i
=\left(\sum_i\nu_i\mu_i\right)d\xi.
$$

The quantity in parentheses is the reaction Gibbs energy $\Delta_rG$. A positive forward extent lowers $G$ when $\Delta_rG\lt0$ and raises it when $\Delta_rG\gt0$. Equilibrium requires $\Delta_rG=0$ and a local minimum with respect to allowed composition changes.

For ideal gases,

$$
\mu_i=\mu_i^\circ(T)+RT\ln\left(\frac{P_i}{P^\circ}\right).
$$

Substitution gives

$$
\Delta_rG=\Delta_rG^\circ+RT\ln Q_p.
$$

At equilibrium, $Q_p=K_p$ and $\Delta_rG=0$, hence

$$
\Delta_rG^\circ=-RT\ln K_p.
$$

The normalized partial pressures make $K_p$ dimensionless. The result also explains the direction test: $Q_p\lt K_p$ makes $\Delta_rG\lt0$ for the forward reaction.

For ideal gases, an equilibrium constant can be written in terms of partial pressures:

$$
K_p(T)=\prod_i\left(\frac{P_i}{P^{\circ}}\right)^{\nu_i}.
$$

The reaction quotient $Q_p$ predicts direction: if $Q_p\lt K_p$, the reaction proceeds forward; if $Q_p\gt K_p$, it proceeds backward.

Reversing a written reaction changes $K$ to $1/K$. Multiplying every stoichiometric coefficient by a factor $a$ changes the constant to $K^a$. Tabulated constants must therefore be matched to the exact written reaction.

Temperature changes $K$. The van 't Hoff relation,

$$
\frac{d\ln K}{dT}=\frac{\Delta_rH^\circ}{RT^2},
$$

shows the trend when standard reaction enthalpy is approximately known over the interval. Raising temperature increases $K$ for an endothermic reaction and decreases it for an exothermic one. Changing total pressure does not change $K(T)$, but it can change the composition required to satisfy $Q=K$ when reaction changes the total gas moles.

For ideal liquid solutions with ideal vapor behavior, Raoult's law is

$$
y_iP=x_iP_{sat,i}(T).
$$

For dilute gas solubility, Henry's law may be written as

$$
y_iP=H_i x_i
$$

with the convention for $H_i$ depending on tables. The Gibbs phase rule gives degrees of freedom:

$$
F=C-P+2
$$

for a nonreacting system with $C$ components and $P$ phases; reactions reduce the independent composition variables. For one pure component in two phases, $F=1$: specifying temperature fixes coexistence pressure, or specifying pressure fixes saturation temperature. At a triple point, three phases give $F=0$, so both temperature and pressure are fixed.
An equilibrium composition must satisfy every element or species balance as well as the equilibrium relations, with mole fractions summing to one in each phase. State whether partial pressures, fugacities, or activities are being used; an ideal model is an assumption, not part of the equilibrium criterion.

```mermaid
flowchart LR
  A["Specify T and P"] --> B["Write species and phases"]
  B --> C["Element or species balances"]
  C --> D["Equilibrium relations"]
  D --> E["Solve composition"]
  E --> F["Check phase or reaction direction"]
```

| Equilibrium type | Criterion | Typical relation |
|---|---|---|
| Chemical reaction | $\sum \nu_i\mu_i=0$ | $K_p=\prod(P_i/P^o)^{\nu_i}$ |
| Liquid-vapor ideal solution | equal chemical potentials | $y_iP=x_iP_{sat,i}$ |
| Dilute gas in liquid | solubility proportional to partial pressure | Henry's law |
| Single-component phase coexistence | same $T$, $P$, chemical potential | saturation curve |

## Dissociation extent from an equilibrium constant

**Problem.** A gas-phase reaction $A\rightleftharpoons 2B$ starts with $1\ \mathrm{mol}$ of pure $A$ at $P=P^{\circ}$. At the specified temperature, $K_p=0.50$. Assuming ideal gases, find the equilibrium extent $\xi$.

**Method.**

1. Mole numbers at extent $\xi$:

$$
N_A=1-\xi, \qquad N_B=2\xi, \qquad N=1+\xi.
$$

2. Mole fractions:

$$
y_A=\frac{1-\xi}{1+\xi}, \qquad
y_B=\frac{2\xi}{1+\xi}.
$$

3. With $P=P^{\circ}$, the ideal-gas equilibrium expression is

$$
K_p=\frac{(y_BP/P^{\circ})^2}{y_AP/P^{\circ}}
=\frac{y_B^2}{y_A}.
$$

4. Substitute:

$$
K_p=\frac{(2\xi/(1+\xi))^2}{(1-\xi)/(1+\xi)}
=\frac{4\xi^2}{1-\xi^2}.
$$

5. Set equal to $0.50$:

$$
0.50(1-\xi^2)=4\xi^2
\Rightarrow 0.50=4.50\xi^2.
$$

6. Solve:

$$
\xi=\sqrt{0.50/4.50}=0.333.
$$

**Checked answer.** One third of the original $A$ dissociates. Product moles are $N_A=0.667$ and $N_B=0.667$, with total moles $1.333$.

## Bubble pressure from Raoult's law

**Problem.** A liquid solution at a fixed temperature contains $x_1=0.40$ of component 1 and $x_2=0.60$ of component 2. The saturation pressures are $P_{sat,1}=80\ \mathrm{kPa}$ and $P_{sat,2}=30\ \mathrm{kPa}$. Estimate the bubble pressure and vapor composition using Raoult's law.

**Method.**

1. Bubble pressure for an ideal solution is

$$
P=\sum_i x_iP_{sat,i}.
$$

2. Substitute:

$$
P=0.40(80)+0.60(30)=32+18=50\ \mathrm{kPa}.
$$

3. Vapor mole fractions:

$$
y_i=\frac{x_iP_{sat,i}}{P}.
$$

4. Component 1:

$$
y_1=\frac{0.40(80)}{50}=0.64.
$$

5. Component 2:

$$
y_2=\frac{0.60(30)}{50}=0.36.
$$

**Checked answer.** The vapor is richer in the more volatile component 1. The mole fractions sum to 1, checking the calculation.

## Dew pressure and the distinction from a bubble point

A bubble point starts from a known liquid composition and asks when the first infinitesimal vapor appears. A dew point starts from a known vapor composition and asks when the first infinitesimal liquid appears. Under ideal Raoult behavior,

$$
y_iP=x_iP_{sat,i}.
$$

At a dew pressure, $x_i=y_iP/P_{sat,i}$. Since the liquid mole fractions sum to one,

$$
\sum_i\frac{y_iP}{P_{sat,i}}=1,
$$

and therefore

$$
P_{dew}=\left(\sum_i\frac{y_i}{P_{sat,i}}\right)^{-1}.
$$

**Problem.** At the same temperature as the preceding example, a vapor has $y_1=0.50$ and $y_2=0.50$, with $P_{sat,1}=80$ kPa and $P_{sat,2}=30$ kPa. Find its dew pressure and first liquid composition.

$$
P_{dew}=\left(\frac{0.50}{80}+\frac{0.50}{30}\right)^{-1}.
$$

The sum is

$$
0.00625+0.01667=0.02292\ \text{kPa}^{-1},
$$

so

$$
P_{dew}=43.64\ \text{kPa}.
$$

The incipient liquid composition is

$$
x_1=\frac{(0.50)(43.64)}{80}=0.273,
$$

$$
x_2=\frac{(0.50)(43.64)}{30}=0.727.
$$

The values sum to one. The first liquid is richer in less volatile component 2, complementing the earlier vapor enrichment in component 1.

## Phase amounts inside a two-phase region

Equilibrium relations determine the composition of each phase, but an overall balance determines how much of each phase is present. For overall mole fraction $z_1$ between equilibrium liquid composition $x_1$ and vapor composition $y_1$, let $V$ be vapor fraction and $L=1-V$ liquid fraction. Then

$$
z_1=Lx_1+Vy_1=x_1+V(y_1-x_1).
$$

Solving gives the lever rule

$$
V=\frac{z_1-x_1}{y_1-x_1},
\qquad
L=\frac{y_1-z_1}{y_1-x_1}.
$$

The rule is a species balance rather than another equilibrium law. If $z_1$ lies outside the interval between $x_1$ and $y_1$, the assumed two-phase state and phase compositions are incompatible.

For example, take $x_1=0.30$, $y_1=0.70$, and overall $z_1=0.45$. Then

$$
V=\frac{0.45-0.30}{0.70-0.30}=0.375,
$$

$$
L=1-0.375=0.625.
$$

A direct check gives $0.625(0.30)+0.375(0.70)=0.45$.

## Activities and fugacities repair the ideal formulas

The equilibrium criterion always uses chemical potentials. Ideal-gas partial pressure and ideal-solution mole fraction are convenient special cases. For a general mixture, write

$$
\mu_i=\mu_i^\circ+RT\ln a_i,
$$

where $a_i$ is activity relative to a chosen standard state. The reaction quotient becomes

$$
Q=\prod_i a_i^{\nu_i}.
$$

For a nonideal liquid solution, $a_i=\gamma_ix_i$ under a common convention, with activity coefficient $\gamma_i$ measuring departure from ideal-solution behavior. For a real gas, fugacity replaces pressure, often written $f_i=\phi_iy_iP$. The activity or fugacity coefficients approach one in the corresponding ideal limit.

These coefficients are property-model inputs, not adjustable equilibrium constants. Changing the liquid model changes calculated activities and therefore phase composition, while $K$ at the same temperature and standard states remains tied to thermodynamic data. Consistent standard states are essential when data from different sources or models are combined.

Modified Raoult behavior is often written

$$
y_iP=x_i\gamma_iP_{sat,i}
$$

when vapor nonideality and pressure corrections are negligible. Positive deviation with $\gamma_i\gt1$ raises a component's escaping tendency; negative deviation lowers it. Strong nonideality can produce azeotropes, where liquid and vapor compositions coincide and ordinary distillation cannot cross the azeotropic composition at fixed pressure.

## Several reactions require independent extents

When multiple reactions occur, one extent is assigned to each independent reaction. Species amounts take the matrix form

$$
n_i=n_{i,0}+\sum_j\nu_{ij}\xi_j.
$$

Each independent reaction contributes an equilibrium relation, while element balances and nonnegative species amounts constrain the solution. A proposed reaction set containing a linear combination of the others is redundant and produces dependent equations.

Combustion equilibrium may include oxidation, water-gas shift, and dissociation reactions at once. Choosing a species list implicitly decides which chemistry is allowed. Excluding carbon monoxide forces all carbon into carbon dioxide even when high temperature or oxygen deficiency would favor CO. Including every conceivable trace species, on the other hand, may add complexity without changing engineering results. Species selection should be stated and checked against temperature, pressure, and elemental composition.

A robust numerical solution often works with element potentials or direct Gibbs minimization rather than hand-selected reaction extents. Direct minimization enforces element conservation and nonnegative mole numbers while finding the lowest Gibbs energy. Extent methods remain transparent for one or two reactions and expose how stoichiometry enters.

## Single-component phase equilibrium and Clapeyron's equation

Along a coexistence curve, the chemical potentials of two phases are equal. Differentiating that equality and using $dmu=-s\,dT+v\,dP$ gives

$$
\frac{dP_{sat}}{dT}=\frac{\Delta s}{\Delta v}
=\frac{h_{fg}}{T(v_g-v_f)}.
$$

This is Clapeyron's equation. It connects the slope of the saturation line to latent heat and the volume change. For vaporization well away from the critical point, $v_g\gg v_f$ and an ideal-gas vapor approximation gives the Clausius-Clapeyron form

$$
\frac{d\ln P_{sat}}{dT}\approx\frac{h_{fg}}{RT^2}.
$$

If latent heat is treated as constant over a modest range, integration yields

$$
\ln\frac{P_2}{P_1}
=-\frac{h_{fg}}R\left(\frac1{T_2}-\frac1{T_1}\right).
$$

The approximation explains the rapid rise of vapor pressure with temperature. Near the critical point, liquid and vapor properties converge, latent heat vanishes, and the crude constant-latent-heat approximation fails.

Solid-liquid coexistence can have either sign of slope because the volume change on melting may be positive or negative. Water is unusual in having a denser liquid than solid near ordinary melting conditions, giving its fusion curve a negative slope over the familiar range.

Metastable states require separate judgment. A supercooled liquid may persist below its equilibrium freezing temperature because forming a critical solid nucleus has an interfacial-energy barrier. Likewise, a supersaturated vapor can remain temporarily homogeneous. Equilibrium predicts the lower-Gibbs state, while nucleation kinetics determines how quickly the system reaches it. Smooth containers and lack of nucleation sites can lengthen that delay.

The distinction matters when interpreting experiments: absence of an observed phase change does not by itself establish that the present phase is the global equilibrium state. A disturbance or seed crystal can trigger rapid conversion without changing the imposed temperature and pressure appreciably.

## Where the ideal models fail

- Using an equilibrium constant without matching the written reaction direction.
- Forgetting pressure effects when gas mole number changes during reaction.
- Treating $K_p$ as composition independent of temperature and pressure in the wrong way: it depends on temperature, while pressure affects composition through partial pressures.
- Applying Raoult's law to strongly nonideal liquid mixtures without activity coefficients.
- Ignoring simultaneous element balances when several reactions occur.
- Treating a catalyst as though it changes $K$ or final composition.
- Confusing bubble and dew calculations; the known phase composition and summation condition differ.
- Using mole fractions alone for a nonideal mixture. Activities or fugacities satisfy the general chemical-potential criterion.

<div className="see-also">

See also: [thermodynamic property relations](/physics/thermodynamics/thermodynamic-property-relations) · [chemical reactions and combustion](/physics/thermodynamics/chemical-reactions-and-combustion) · [microscopic foundations](/physics/statistical-mechanics/intro) · [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables) · [thermodynamic potentials and phase equilibrium](/physics/statistical-mechanics/thermodynamic-potentials-and-phase-equilibrium)

</div>
