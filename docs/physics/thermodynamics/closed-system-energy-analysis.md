---
title: Closed-System Energy Analysis
sidebar_position: 4
---

# Closed-System Energy Analysis

Closed-system analysis applies the first law to a fixed mass. The system may expand, compress, heat, cool, accelerate, or change elevation, but no mass crosses the boundary. This is the natural model for piston-cylinder devices, rigid tanks, sealed containers, solids and liquids being heated, and many transient steps before a valve opens.

The most distinctive closed-system term is moving boundary work. In a quasi-equilibrium piston-cylinder process, the work is the area under the $P$-$V$ curve. That geometric interpretation is simple, but it makes the answer path dependent: the same initial and final states can require different amounts of work if the pressure-volume path is different.

## Definitions

- A **closed system** or control mass contains a fixed quantity of matter. Energy may cross the boundary as heat or work, but mass does not.
- **Moving boundary work** is work associated with expansion or compression of a boundary: $W_b=\int_1^2 P\,dV$ for a quasi-equilibrium process.
- **Expansion work** is positive when the system does work on the surroundings under the convention $\Delta E=Q-W$. Compression work is negative by the same convention.
- A **polytropic process** satisfies $PV^n=C$ for constants $n$ and $C$. Many gas compression and expansion processes are approximated this way.
- **Specific heat at constant volume** is $c_v=(\partial u/\partial T)_v$ for a gas. **Specific heat at constant pressure** is $c_p=(\partial h/\partial T)_p$.
- For an **ideal gas**, internal energy is a function of temperature only, $u=u(T)$, and enthalpy is also a function of temperature only, $h=h(T)$.
- For **incompressible solids and liquids**, $c_p\approx c_v\approx c$ and $\Delta u\approx c\Delta T$. Enthalpy changes may include a pressure-volume term, but for many liquids $\Delta h\approx c\Delta T+v\Delta P$.
- A **constant-volume process** has $W_b=0$ because $dV=0$. A rigid tank can still have heat transfer, electrical work, shaft work, or changes in internal energy.
- A **constant-pressure process** has $W_b=P(V_2-V_1)$ when the pressure is uniform and the process is quasi-equilibrium.

The modeling habit is to write the most complete closed-system balance first, then remove terms only after explaining why they are negligible. For a stationary piston-cylinder without electrical or shaft work, the usual simplified form is $m(u_2-u_1)=Q-W_b$. For a rigid tank it becomes $m(u_2-u_1)=Q-W_{\mathrm{other}}$.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In closed-system energy analysis, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

The closed-system first law is

$$
\Delta U + \Delta KE + \Delta PE = Q - W.
$$

For simple compressible quasi-equilibrium boundary work,

$$
W_b = \int_1^2 P\,dV.
$$

Important special cases are

$$
\begin{aligned}
W_b &= P(V_2-V_1) && \text{constant pressure}, \\
W_b &= 0 && \text{constant volume}, \\
W_b &= mRT\ln\left(\frac{V_2}{V_1}\right) && \text{ideal gas, isothermal}, \\
W_b &= \frac{P_2V_2-P_1V_1}{1-n} && \text{polytropic, } n\ne 1.
\end{aligned}
$$

For ideal gases with constant specific heats,

$$
\Delta u=c_v(T_2-T_1), \qquad
\Delta h=c_p(T_2-T_1), \qquad
c_p-c_v=R.
$$

The ratio $k=c_p/c_v$ appears in isentropic and power-cycle formulas. Constant specific heats are convenient but approximate; at high temperatures, variable-specific-heat tables or polynomial fits should be used.

For liquids and solids,

$$
\Delta u \approx c(T_2-T_1).
$$

Because liquids are nearly incompressible, boundary work is often much smaller than heat transfer unless very large pressures or volumes are involved. Still, the sign and units of $P\Delta V$ must be checked carefully.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

ASCII $P$-$V$ interpretation of boundary work:

```text
P
|        1 *
|         /|
|        / |       area under curve = boundary work
|       /  |
|      * 2 |
|__________|____________ V
       V2  V1
```

| Process model | Constraint | Boundary work |
|---|---|---:|
| Constant volume | $V_2=V_1$ | $0$ |
| Constant pressure | $P=\mathrm{constant}$ | $P(V_2-V_1)$ |
| Isothermal ideal gas | $T=\mathrm{constant}$ | $mRT\ln(V_2/V_1)$ |
| Polytropic | $PV^n=C$ | $(P_2V_2-P_1V_1)/(1-n)$ |

## Worked example 1: polytropic compression work

**Problem.** A gas in a piston-cylinder is compressed quasi-equilibrium from $P_1=100\ \mathrm{kPa}$, $V_1=0.100\ \mathrm{m^3}$ to $P_2=500\ \mathrm{kPa}$, $V_2=0.030\ \mathrm{m^3}$ along $PV^n=C$. Find $n$ and the boundary work by the gas.

**Method.**

1. Use the polytropic relation:

$$
P_1V_1^n=P_2V_2^n
\quad\Rightarrow\quad
n=\frac{\ln(P_2/P_1)}{\ln(V_1/V_2)}.
$$

2. Substitute:

$$
n=\frac{\ln(500/100)}{\ln(0.100/0.030)}
=\frac{1.609}{1.204}=1.34.
$$

3. Use the polytropic work formula:

$$
W_b=\frac{P_2V_2-P_1V_1}{1-n}.
$$

4. Since $\mathrm{kPa\,m^3}=\mathrm{kJ}$,

$$
W_b=\frac{(500)(0.030)-(100)(0.100)}{1-1.34}
=\frac{15.0-10.0}{-0.34}
=-14.7\ \mathrm{kJ}.
$$

**Checked answer.** The boundary work by the gas is $-14.7\ \mathrm{kJ}$, meaning $14.7\ \mathrm{kJ}$ of work is done on the gas during compression.

## Worked example 2: rigid-tank heating of air

**Problem.** A rigid tank contains $2.0\ \mathrm{kg}$ of air initially at $300\ \mathrm{K}$. Heat is added until the air reaches $500\ \mathrm{K}$. Treat air as an ideal gas with constant $c_v=0.718\ \mathrm{kJ/(kg\,K)}$. Find the heat transfer.

**Method.**

1. The tank is rigid, so $W_b=0$.
2. The tank is stationary and has no other work mode, so $\Delta KE=\Delta PE=0$ and $Q=\Delta U$.
3. For an ideal gas with constant specific heat:

$$
\Delta U=m c_v(T_2-T_1).
$$

4. Substitute values:

$$
\begin{aligned}
Q&=(2.0\ \mathrm{kg})(0.718\ \mathrm{kJ/(kg\,K)})(500-300)\ \mathrm{K} \\
&=287.2\ \mathrm{kJ}.
\end{aligned}
$$

**Checked answer.** Heat transfer into the tank is $287\ \mathrm{kJ}$. Pressure rises during the process, but boundary work remains zero because volume is fixed.

## Code

```python
import math

def polytropic_exponent(P1, V1, P2, V2):
    return math.log(P2 / P1) / math.log(V1 / V2)

def polytropic_work(P1, V1, P2, V2):
    n = polytropic_exponent(P1, V1, P2, V2)
    return (P2 * V2 - P1 * V1) / (1.0 - n)

def rigid_tank_heat(m, cv, T1, T2):
    return m * cv * (T2 - T1)

print(polytropic_exponent(100, 0.100, 500, 0.030))
print(polytropic_work(100, 0.100, 500, 0.030))
print(rigid_tank_heat(2.0, 0.718, 300, 500))
```

## Common pitfalls

- Using $\int P\,dV$ for a non-quasi-equilibrium process without a meaningful system pressure path.
- Forgetting that compression work by the system is negative under the common engineering sign convention.
- Using $c_p$ instead of $c_v$ for ideal-gas internal-energy changes.
- Assuming a rigid tank has no energy transfer; it has no boundary work, but it may have heat or electrical work.
- Mixing total and specific quantities without multiplying or dividing by mass.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [energy, heat, work, and the first law](/physics/thermodynamics/energy-heat-work-and-first-law)
- [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables)
- [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
