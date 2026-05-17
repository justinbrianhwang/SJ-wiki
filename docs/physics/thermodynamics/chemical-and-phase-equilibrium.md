---
title: Chemical and Phase Equilibrium
sidebar_position: 16
---

# Chemical and Phase Equilibrium

Equilibrium tells us where a reacting or multiphase system tends after constraints are fixed. Energy balances can predict an adiabatic flame temperature only if product composition is known; at high temperature, dissociation changes that composition. Phase equilibrium determines whether species partition between liquid and vapor, dissolve in liquids, or condense from gases.

Cengel introduces equilibrium through the Gibbs function. At fixed temperature and pressure, a closed reacting system reaches equilibrium by minimizing Gibbs free energy. This principle leads to equilibrium constants for chemical reactions and equality of chemical potentials for phase equilibrium.

## Definitions

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
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In chemical and phase equilibrium, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

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

For ideal gases, an equilibrium constant can be written in terms of partial pressures:

$$
K_p(T)=\prod_i\left(\frac{P_i}{P^{\circ}}\right)^{\nu_i}.
$$

The reaction quotient $Q_p$ predicts direction: if $Q_p\lt K_p$, the reaction proceeds forward; if $Q_p\gt K_p$, it proceeds backward.

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

for a nonreacting system with $C$ components and $P$ phases; reactions reduce the independent composition variables.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

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

## Worked example 1: extent of dissociation from an equilibrium constant

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

## Worked example 2: ideal bubble pressure by Raoult's law

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

## Code

```python
import math

def dissociation_extent_A_to_2B(Kp):
    # Kp = 4*x^2/(1-x^2) at P = P_standard
    return math.sqrt(Kp / (4.0 + Kp))

def raoult_bubble(x, Psat):
    P = sum(xi * Pi for xi, Pi in zip(x, Psat))
    y = [xi * Pi / P for xi, Pi in zip(x, Psat)]
    return P, y

print(dissociation_extent_A_to_2B(0.50))
print(raoult_bubble([0.40, 0.60], [80.0, 30.0]))
```

## Common pitfalls

- Using an equilibrium constant without matching the written reaction direction.
- Forgetting pressure effects when gas mole number changes during reaction.
- Treating $K_p$ as composition independent of temperature and pressure in the wrong way: it depends on temperature, while pressure affects composition through partial pressures.
- Applying Raoult's law to strongly nonideal liquid mixtures without activity coefficients.
- Ignoring simultaneous element balances when several reactions occur.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [thermodynamic property relations](/physics/thermodynamics/thermodynamic-property-relations)
- [chemical reactions and combustion](/physics/thermodynamics/chemical-reactions-and-combustion)
- [physical chemistry](/chemistry/physical-chemistry/)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
