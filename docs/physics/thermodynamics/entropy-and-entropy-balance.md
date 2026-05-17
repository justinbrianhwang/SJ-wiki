---
title: Entropy and Entropy Balance
sidebar_position: 7
---

# Entropy and Entropy Balance

Entropy turns the second law into an accounting equation. Heat transfer carries entropy, mass flow carries entropy, and irreversibilities generate entropy. Unlike energy, entropy is not conserved. It can be transferred and generated, but never destroyed. This gives engineers a numerical way to locate losses in turbines, compressors, heat exchangers, throttles, and complete cycles.

Cengel builds entropy from the Clausius inequality, then uses it in property tables, ideal-gas relations, $T$-$s$ diagrams, isentropic efficiencies, and entropy balances. The result is a practical rule: reversible adiabatic processes are isentropic, but adiabatic does not automatically mean isentropic. If irreversibilities exist, entropy increases even without heat transfer.

## Definitions

- **Entropy** is a thermodynamic property defined through reversible heat transfer: $dS=(\delta Q/T)_{\mathrm{int\ rev}}$.
- The **Clausius inequality** states that $\oint \delta Q/T\le 0$ for any cycle, with equality for internally reversible cycles.
- The **increase of entropy principle** says $S_{\mathrm{gen}}\ge0$ for any process. Equality holds only for an ideal reversible process.
- An **isentropic process** has constant entropy. In engineering models it usually means internally reversible and adiabatic.
- **Entropy transfer by heat** occurs as $Q/T_b$, where $T_b$ is the boundary temperature at which heat crosses.
- **Entropy transfer by mass** is $ms$ or $\dot m s$ because flowing matter carries entropy with it.
- **Entropy generation** is the entropy produced by irreversibilities: friction, mixing, inelastic deformation, electrical resistance, chemical reaction, unrestrained expansion, and heat transfer through a finite temperature difference.
- The **$Tds$ relations** connect entropy to other properties: $Tds=du+Pdv$ and $Tds=dh-vdP$ for simple compressible substances.
- **Isentropic efficiencies** compare actual adiabatic devices with ideal isentropic devices between the same inlet state and exit pressure.
- **Relative pressure** and **relative specific volume** tables simplify ideal-gas isentropic calculations with variable specific heats.

Entropy is not a measure of energy amount. It measures dispersal and irreversibility in a way that constrains possible processes. A cold block warming in a room and a hot block cooling in a room may have equal and opposite heat transfers, but the entropy changes are not equal because the boundary temperatures differ.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In entropy and entropy balance, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

For a closed system,

$$
\Delta S_{\mathrm{system}}
=\sum \frac{Q_k}{T_k}+S_{\mathrm{gen}}.
$$

For a control volume, one useful sign arrangement is

$$
\dot S_{\mathrm{gen}} =
\dot S_{\mathrm{out}} - \dot S_{\mathrm{in}} + \Delta S_{\mathrm{system}}.
$$

In full rate form with heat and mass transfer,

$$
\frac{dS_{\mathrm{CV}}}{dt}
=\sum \frac{\dot Q_k}{T_k}
\sum_{in}\dot m s
-\sum_{out}\dot m s
 +\dot S_{\mathrm{gen}}.
$$

For ideal gases with constant specific heats,

$$
\Delta s=c_p\ln\left(\frac{T_2}{T_1}\right)-R\ln\left(\frac{P_2}{P_1}\right)
$$

and also

$$
\Delta s=c_v\ln\left(\frac{T_2}{T_1}\right)+R\ln\left(\frac{v_2}{v_1}\right).
$$

For incompressible substances,

$$
\Delta s \approx c\ln\left(\frac{T_2}{T_1}\right).
$$

The isentropic ideal-gas relations for constant $k$ are

$$
\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{(k-1)/k},
\qquad
\frac{P_2}{P_1}=\left(\frac{v_1}{v_2}\right)^k.
$$

These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

ASCII $T$-$s$ meaning of heat for internally reversible processes:

```text
T
|          2 *
|           /|
|          / |  area under path = q_rev
|         /  |
|    1 *-----|
|________________ s
```

| Process | Entropy change of system | Entropy generation | Comment |
|---|---:|---:|---|
| Reversible adiabatic | $0$ | $0$ | Isentropic benchmark |
| Actual adiabatic compression | $\gt 0$ often | $\gt 0$ | Work input is higher than ideal |
| Heat transfer at finite $\Delta T$ | depends on system | $\gt 0$ | Universe entropy increases |
| Throttling | often $\gt 0$ | $\gt 0$ | Enthalpy nearly constant, entropy rises |

## Worked example 1: ideal-gas entropy change

**Problem.** Air changes from $T_1=300\ \mathrm{K}$, $P_1=100\ \mathrm{kPa}$ to $T_2=600\ \mathrm{K}$, $P_2=500\ \mathrm{kPa}$. Use constant $c_p=1.005\ \mathrm{kJ/(kg\,K)}$ and $R=0.287\ \mathrm{kJ/(kg\,K)}$. Find $\Delta s$.

**Method.**

1. Use the ideal-gas entropy relation:

$$
\Delta s=c_p\ln(T_2/T_1)-R\ln(P_2/P_1).
$$

2. Temperature contribution:

$$
c_p\ln(600/300)=1.005\ln 2=0.696\ \mathrm{kJ/(kg\,K)}.
$$

3. Pressure contribution:

$$
R\ln(500/100)=0.287\ln 5=0.462\ \mathrm{kJ/(kg\,K)}.
$$

4. Combine:

$$
\Delta s=0.696-0.462=0.234\ \mathrm{kJ/(kg\,K)}.
$$

**Checked answer.** Entropy increases. Heating tends to raise entropy, while compression tends to lower it; in this case the temperature increase dominates.

## Worked example 2: entropy generation during heat transfer

**Problem.** A $600\ \mathrm{K}$ thermal reservoir transfers $100\ \mathrm{kJ}$ of heat to a $300\ \mathrm{K}$ reservoir. Find the entropy generation for the combined two-reservoir system.

**Method.**

1. The hot reservoir loses heat:

$$
\Delta S_H=-\frac{100}{600}=-0.1667\ \mathrm{kJ/K}.
$$

2. The cold reservoir gains heat:

$$
\Delta S_L=\frac{100}{300}=0.3333\ \mathrm{kJ/K}.
$$

3. The combined system is isolated, so entropy transfer across its outer boundary is zero. Thus

$$
S_{\mathrm{gen}}=\Delta S_H+\Delta S_L
=0.1666\ \mathrm{kJ/K}.
$$

**Checked answer.** Entropy generation is $0.167\ \mathrm{kJ/K}$, positive as required. The same $100\ \mathrm{kJ}$ moved across a smaller temperature difference would generate less entropy.

## Code

```python
import math

def ideal_gas_delta_s(T1, P1, T2, P2, cp=1.005, R=0.287):
    return cp * math.log(T2 / T1) - R * math.log(P2 / P1)

def heat_transfer_sgen(Q, T_hot, T_cold):
    return -Q / T_hot + Q / T_cold

print(ideal_gas_delta_s(300, 100, 600, 500))
print(heat_transfer_sgen(100, 600, 300))
```

## Common pitfalls

- Equating adiabatic with isentropic when friction, mixing, throttling, or shock waves are present.
- Using the system temperature instead of boundary temperature for entropy transfer by heat.
- Expecting entropy to be conserved like energy. Entropy generation is allowed and required for real processes.
- Applying ideal-gas constant-specific-heat formulas over a wide temperature range without checking accuracy.
- Forgetting mass-flow entropy terms in control-volume entropy balances.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [second-law heat engines and refrigerators](/physics/thermodynamics/second-law-heat-engines-and-refrigerators)
- [exergy and second-law efficiency](/physics/thermodynamics/exergy-and-second-law-efficiency)
- [thermodynamic property relations](/physics/thermodynamics/thermodynamic-property-relations)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
