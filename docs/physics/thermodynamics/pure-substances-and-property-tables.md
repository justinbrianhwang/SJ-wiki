---
title: Pure Substances and Property Tables
sidebar_position: 3
---

# Pure Substances and Property Tables

Pure substances are the bridge between abstract balances and real fluids. Water, refrigerants, carbon dioxide, nitrogen, and many other substances cannot always be modeled as ideal gases, especially near phase change or near the critical point. Engineering thermodynamics therefore relies heavily on property tables and diagrams: $T$-$v$, $P$-$v$, $P$-$T$, $T$-$s$, and $h$-$s$ views of the same state surface.

The central skill is locating the state. Once the phase region is identified, the table entries provide $v$, $u$, $h$, and $s$ values that can be inserted into energy and entropy balances. Cengel emphasizes saturation temperature-pressure dependence, quality in the two-phase region, ideal-gas limits, and the compressibility factor as a correction when ideal-gas behavior is questionable.

## Definitions

- A **pure substance** has a fixed chemical composition throughout. It may be a single chemical species or a uniform mixture such as air treated as a mixture of gases, provided the composition does not vary spatially.
- A **phase** is a physically distinct, homogeneous form of matter. Solid, liquid, and vapor are phases; liquid water and water vapor can coexist during boiling or condensation.
- A **saturated liquid** is about to vaporize. A **saturated vapor** is about to condense. A **compressed** or **subcooled liquid** has a temperature below the saturation temperature at its pressure.
- A **superheated vapor** has a temperature above saturation temperature at its pressure. In this region, $T$ and $P$ are independent.
- **Quality** is the mass fraction of vapor in a saturated liquid-vapor mixture: $x=m_g/(m_f+m_g)$. It is defined only in the two-phase region.
- **Enthalpy** is $h=u+Pv$. It packages internal energy and flow work and is especially useful for control volumes.
- The **critical point** is the end of the liquid-vapor saturation curve. Above the critical temperature, a distinct liquid-vapor phase change does not occur.
- The **ideal-gas equation of state** is $Pv=RT$ or $PV=nR_uT$. It works best at low density and far from the saturation dome.
- The **compressibility factor** is $Z=Pv/(RT)$. When $Z$ is close to 1, ideal-gas behavior is accurate; when it departs significantly, real-gas tables, charts, or equations of state should be used.
- **Reduced properties** are $T_R=T/T_c$ and $P_R=P/P_c$. The corresponding-states idea uses them to estimate real-gas departures with generalized charts.

The state-location sequence is: identify the substance, list known intensive properties, compare $T$ with $T_{\mathrm{sat}}(P)$ or $P$ with $P_{\mathrm{sat}}(T)$, then choose the correct table. If the state is saturated mixture, use quality formulas. If it is superheated or compressed, interpolate in the appropriate table or use a justified approximation.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In pure substances and property tables, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

For a saturated mixture, any specific property $y$ among $v$, $u$, $h$, or $s$ is

$$
y = y_f + x y_{fg}, \qquad y_{fg}=y_g-y_f.
$$

Quality can therefore be recovered from any mixture property:

$$
x=\frac{y-y_f}{y_{fg}}.
$$

The ideal-gas equation is

$$
PV=nR_uT, \qquad Pv=RT,
$$

with $R=R_u/M$. For real gases,

$$
Z=\frac{Pv}{RT}, \qquad Pv=ZRT.
$$

Near the critical region or saturation dome, small changes in $P$ or $T$ can produce large density changes, so ideal-gas estimates become unreliable. For compressed liquids, Cengel often uses the approximation

$$
y(T,P)\approx y_f(T)
$$

for $v$ and $u$ when pressure effects are small, while enthalpy may be corrected as

$$
h(T,P)\approx h_f(T)+v_f(T)\left[P-P_{\mathrm{sat}}(T)\right].
$$

This correction is small for many liquid-water problems but useful when pressures are high. Tables use arbitrary reference states for $u$, $h$, and $s$; absolute values matter less than differences within a consistent table set.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

ASCII $T$-$v$ map of water-like phase behavior:

```text
T
|                         superheated vapor
|                        /
|                       /
|          critical *  /
|                  ___/ 
|                 /   \
| compressed     /     \     saturated mixture
| liquid        /       \    0 < x < 1
|______________/_________\________________ v
              sat. liq.  sat. vapor
```

| Region | How to identify | Main table or model | Typical unknown recovery |
|---|---|---|---|
| Compressed liquid | $T\lt T_{\mathrm{sat}}(P)$ | compressed-liquid table or saturated liquid approximation | use $y\approx y_f(T)$ |
| Saturated mixture | $T=T_{\mathrm{sat}}(P)$ and $0\lt x\lt 1$ | saturation table | $y=y_f+xy_{fg}$ |
| Superheated vapor | $T\gt T_{\mathrm{sat}}(P)$ | superheated table | interpolate in $P$ and $T$ |
| Ideal gas | low density, far from dome | $Pv=RT$ | compute $v$, $P$, or $T$ directly |

## Worked example 1: saturated water mixture at 200 kPa

**Problem.** Water is a saturated liquid-vapor mixture at $200\ \mathrm{kPa}$ with quality $x=0.80$. Estimate $v$, $u$, and $h$ using common saturated-water table values at $200\ \mathrm{kPa}$: $v_f=0.001061\ \mathrm{m^3/kg}$, $v_g=0.8857\ \mathrm{m^3/kg}$, $u_f=504.5\ \mathrm{kJ/kg}$, $u_{fg}=2024.6\ \mathrm{kJ/kg}$, $h_f=504.7\ \mathrm{kJ/kg}$, and $h_{fg}=2201.9\ \mathrm{kJ/kg}$.

**Method.**

1. In the saturated mixture region, use $y=y_f+xy_{fg}$.
2. Specific volume:

$$
\begin{aligned}
v &= v_f+x(v_g-v_f) \\
&=0.001061+0.80(0.8857-0.001061) \\
&=0.7088\ \mathrm{m^3/kg}.
\end{aligned}
$$

3. Internal energy:

$$
u=504.5+0.80(2024.6)=2124.2\ \mathrm{kJ/kg}.
$$

4. Enthalpy:

$$
h=504.7+0.80(2201.9)=2266.2\ \mathrm{kJ/kg}.
$$

**Checked answer.** The values lie between the saturated liquid and saturated vapor entries. The large specific volume shows that vapor dominates the volume even though liquid is $20\%$ of the mass.

## Worked example 2: ideal-gas estimate and compressibility check

**Problem.** Nitrogen is at $300\ \mathrm{K}$ and $2.0\ \mathrm{MPa}$. Estimate $v$ from the ideal-gas equation using $R=0.2968\ \mathrm{kJ/(kg\,K)}$. If a generalized compressibility chart suggested $Z=0.98$, correct the result.

**Method.**

1. Use pressure in kPa so that $\mathrm{kPa\,m^3}=\mathrm{kJ}$:

$$
P=2.0\ \mathrm{MPa}=2000\ \mathrm{kPa}.
$$

2. Ideal-gas specific volume:

$$
v_{\mathrm{ideal}}=\frac{RT}{P}
=\frac{(0.2968)(300)}{2000}
=0.04452\ \mathrm{m^3/kg}.
$$

3. Apply $Pv=ZRT$:

$$
v_{\mathrm{real}}=Z\frac{RT}{P}=0.98(0.04452)=0.04363\ \mathrm{m^3/kg}.
$$

4. Percent departure from ideal-gas estimate:

$$
\frac{0.04452-0.04363}{0.04452}\times 100=2.0\%.
$$

**Checked answer.** The corrected specific volume is $0.0436\ \mathrm{m^3/kg}$. A $2\%$ departure is small for many engineering estimates, but not negligible for precision mass inventory.

## Code

```python
def saturated_mixture(y_f, y_g=None, y_fg=None, x=0.0):
    if y_fg is None:
        y_fg = y_g - y_f
    return y_f + x * y_fg

v = saturated_mixture(0.001061, y_g=0.8857, x=0.80)
u = saturated_mixture(504.5, y_fg=2024.6, x=0.80)
h = saturated_mixture(504.7, y_fg=2201.9, x=0.80)

R_N2 = 0.2968
v_ideal = R_N2 * 300.0 / 2000.0
v_real = 0.98 * v_ideal
print(v, u, h)
print(v_ideal, v_real)
```

## Common pitfalls

- Using quality outside the saturated liquid-vapor mixture region.
- Interpolating in the wrong table after identifying only one property.
- Treating saturated $T$ and saturated $P$ as independent properties.
- Using ideal-gas behavior for steam near condensation or for dense gases near the critical region.
- Mixing property values from tables with different reference states.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [property-table workflows and software](/physics/thermodynamics/property-table-workflows-and-software)
- [closed-system energy analysis](/physics/thermodynamics/closed-system-energy-analysis)
- [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
