---
title: Gas Power Cycles
sidebar_position: 9
---

# Gas Power Cycles

Gas power cycles model engines and gas turbines by replacing combustion and exhaust with heat addition and rejection under air-standard assumptions. The real working fluid changes composition in an internal combustion engine, but the ideal cycles reveal how compression ratio, pressure ratio, specific heat ratio, regeneration, intercooling, and reheat affect performance.

Cengel covers reciprocating-engine cycles such as Otto and Diesel, externally heated Stirling and Ericsson cycles, and Brayton cycles for gas turbines and jet propulsion. The diagrams are idealizations, but they guide design tradeoffs: higher compression ratio improves Otto efficiency, higher pressure ratio improves ideal Brayton efficiency, regeneration helps when turbine exhaust is hotter than compressor discharge, and intercooling/reheat mainly increase net work when combined with regeneration.

## Definitions

- A **power cycle** is a thermodynamic cycle whose net effect is work output.
- The **air-standard assumptions** treat the working fluid as air circulating in a closed loop, model combustion as external heat addition, model exhaust as heat rejection, and often use constant specific heats at room temperature.
- The **Otto cycle** is the ideal cycle for spark-ignition engines: isentropic compression, constant-volume heat addition, isentropic expansion, and constant-volume heat rejection.
- The **Diesel cycle** is the ideal cycle for compression-ignition engines: isentropic compression, constant-pressure heat addition, isentropic expansion, and constant-volume heat rejection.
- **Compression ratio** is $r=V_{max}/V_{min}$ for reciprocating engines.
- **Cutoff ratio** in the Diesel cycle is the volume ratio during constant-pressure heat addition.
- The **Brayton cycle** is the ideal cycle for gas turbines: isentropic compression, constant-pressure heat addition, isentropic expansion, and constant-pressure heat rejection.
- **Regeneration** preheats compressed air using turbine exhaust, reducing required external heat input.
- **Intercooling** reduces compressor work by cooling between compression stages. **Reheat** increases turbine work by heating between expansion stages.
- A **jet-propulsion cycle** uses a gas turbine to produce a high-speed exhaust jet; thrust depends strongly on momentum change, not just shaft work.

These ideal cycles should be compared at the same assumptions. Variable specific heats, pressure drops, combustion irreversibility, mechanical losses, and non-isentropic turbomachinery all move actual engines away from ideal predictions.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In gas power cycles, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

For the ideal Otto cycle with constant $k$,

$$
\eta_{Otto}=1-\frac{1}{r^{k-1}}.
$$

The Diesel-cycle efficiency with cutoff ratio $r_c$ is

$$
\eta_{Diesel}
=1-\frac{1}{r^{k-1}}
\left[\frac{r_c^k-1}{k(r_c-1)}\right].
$$

For the ideal Brayton cycle with pressure ratio $r_p=P_2/P_1$,

$$
\eta_{Brayton}=1-\frac{1}{r_p^{(k-1)/k}}.
$$

Isentropic compressor and turbine temperature relations are

$$
\frac{T_2}{T_1}=r_p^{(k-1)/k},
\qquad
\frac{T_4}{T_3}=\frac{1}{r_p^{(k-1)/k}}.
$$

For a simple ideal Brayton cycle,

$$
w_{net}=c_p[(T_3-T_4)-(T_2-T_1)], \qquad
q_{in}=c_p(T_3-T_2).
$$

Regeneration is useful only if $T_4\gt T_2$. If the compressor exit is already hotter than the turbine exhaust, a regenerator cannot preheat the air and would only add pressure losses.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

ASCII ideal Otto cycle on $P$-$v$ coordinates:

```text
P
|      3 *
|       /|
|      / |  heat addition at constant volume
|  2 *  |
|    |  * 4
|    | /
|  1 *
|________________ v
```

| Cycle | Heat addition | Main control parameter | Efficiency trend |
|---|---|---|---|
| Otto | constant volume | compression ratio $r$ | increases with $r$ and $k$ |
| Diesel | constant pressure | $r$ and cutoff ratio | increases with $r$, decreases with large cutoff |
| Brayton | constant pressure | pressure ratio $r_p$ | increases with $r_p$ in ideal simple cycle |
| Stirling/Ericsson | isothermal with regeneration | regenerator effectiveness | can reach Carnot ideal if fully reversible |

## Worked example 1: Otto-cycle efficiency

**Problem.** Estimate the air-standard Otto-cycle efficiency for a spark-ignition engine with compression ratio $r=8.0$ and $k=1.4$.

**Method.**

1. Use the ideal Otto relation:

$$
\eta=1-\frac{1}{r^{k-1}}.
$$

2. Compute the exponent:

$$
k-1=0.4.
$$

3. Evaluate:

$$
r^{k-1}=8^{0.4}=2.297.
$$

4. Efficiency:

$$
\eta=1-\frac{1}{2.297}=0.565.
$$

**Checked answer.** The ideal efficiency is $56.5\%$. A real engine has lower brake efficiency because of heat losses, combustion irreversibility, friction, pumping work, and finite-rate processes.

## Worked example 2: simple ideal Brayton-cycle temperatures

**Problem.** Air enters an ideal Brayton-cycle compressor at $T_1=300\ \mathrm{K}$. The pressure ratio is $r_p=10$, the turbine inlet temperature is $T_3=1400\ \mathrm{K}$, and $k=1.4$. Use $c_p=1.004\ \mathrm{kJ/(kg\,K)}$. Find $T_2$, $T_4$, net work, and thermal efficiency.

**Method.**

1. The isentropic temperature ratio is

$$
a=r_p^{(k-1)/k}=10^{0.4/1.4}=1.931.
$$

2. Compressor exit:

$$
T_2=aT_1=1.931(300)=579\ \mathrm{K}.
$$

3. Turbine exit:

$$
T_4=\frac{T_3}{a}=\frac{1400}{1.931}=725\ \mathrm{K}.
$$

4. Net work:

$$
w_{net}=c_p[(T_3-T_4)-(T_2-T_1)]
=1.004[(1400-725)-(579-300)]
=397\ \mathrm{kJ/kg}.
$$

5. Heat input:

$$
q_{in}=c_p(T_3-T_2)=1.004(821)=824\ \mathrm{kJ/kg}.
$$

6. Efficiency:

$$
\eta=397/824=0.482.
$$

**Checked answer.** The ideal thermal efficiency is about $48\%$, matching $1-1/a=0.482$.

## Code

```python
import math

def otto_efficiency(r, k=1.4):
    return 1.0 - 1.0 / (r ** (k - 1.0))

def brayton_ideal(T1, T3, rp, k=1.4, cp=1.004):
    a = rp ** ((k - 1.0) / k)
    T2 = T1 * a
    T4 = T3 / a
    wnet = cp * ((T3 - T4) - (T2 - T1))
    qin = cp * (T3 - T2)
    return T2, T4, wnet, wnet / qin

print(otto_efficiency(8.0))
print(brayton_ideal(300.0, 1400.0, 10.0))
```

## Common pitfalls

- Using air-standard efficiency formulas for actual engine brake efficiency without accounting for losses.
- Increasing compression ratio without considering knock, material limits, or actual-cycle constraints.
- Assuming regeneration always helps; it requires turbine exhaust hotter than compressor discharge.
- Using constant specific heats at very high turbine inlet temperatures without estimating the error.
- Confusing pressure ratio in a Brayton cycle with compression ratio in a piston engine.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [exergy and second-law efficiency](/physics/thermodynamics/exergy-and-second-law-efficiency)
- [compressible flow](/physics/thermodynamics/compressible-flow)
- [vapor and combined power cycles](/physics/thermodynamics/vapor-and-combined-power-cycles)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
