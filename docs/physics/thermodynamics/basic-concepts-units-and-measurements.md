---
title: Basic Concepts, Units, and Measurements
sidebar_position: 1
---

# Basic Concepts, Units, and Measurements

Engineering thermodynamics begins by deciding what portion of the world is being analyzed and how its measurable state is described. The vocabulary is deliberately strict: a system is not the same thing as the surroundings, a property is not the same thing as a path quantity, and a temperature reading is meaningful only because the zeroth law makes thermometers possible. This page collects the foundational language used by the later energy, entropy, exergy, cycle, and flow analyses.

The emphasis is practical. Before solving for turbine power or refrigerator performance, an engineer must choose the system boundary, decide whether mass crosses it, convert units without changing physical meaning, and distinguish absolute pressure and temperature from gage readings and temperature differences. These choices look elementary, but they prevent many of the largest errors in thermodynamics homework and design calculations.

## Definitions

- A **system** is the mass or region selected for study. Everything outside it is the surroundings, and the boundary may be real or imaginary, fixed or moving. A closed system contains a fixed mass; a control volume is an open system that permits mass flow.
- A **property** is a macroscopic characteristic that has a definite value at a state. Pressure, temperature, specific volume, internal energy, enthalpy, and entropy are properties. Heat and work are not properties because they describe energy crossing a boundary during a process.
- **Extensive properties** scale with system size, such as mass, total volume, and total energy. **Intensive properties** do not scale with size, such as pressure, temperature, density, and specific volume. Specific properties, such as $u=U/m$ and $v=V/m$, convert extensive quantities to intensive form.
- A **state** is the condition of a system as specified by its properties. A process is a change from one state to another, and a cycle is a sequence of processes that returns the system to its initial state.
- The **state postulate** says that the state of a simple compressible system is fixed by two independent intensive properties. The word independent matters: at saturated liquid-vapor equilibrium, $T$ and $P$ are not independent because $T=T_{\mathrm{sat}}(P)$.
- A **quasi-equilibrium process** proceeds slowly enough that the system remains nearly uniform and can be plotted as a path on diagrams such as $P$-$v$ or $T$-$s$. Fast, highly nonuniform processes have initial and final states but no well-defined equilibrium path.
- The **zeroth law** states that if two bodies are each in thermal equilibrium with a third body, then they are in thermal equilibrium with each other. It justifies using a thermometer as the third body and gives operational meaning to temperature.
- **Absolute temperature** is required in thermodynamic ratios and ideal-gas formulas. Use kelvin or rankine, not degrees Celsius or Fahrenheit, when evaluating $PV=nRT$, Carnot efficiency, or isentropic formulas.
- **Pressure** is normal force per unit area. Absolute pressure is measured relative to vacuum; gage pressure is measured relative to the local atmosphere; vacuum pressure is the amount by which a pressure lies below atmospheric pressure.
- **Density** is $\rho=m/V$ and specific volume is $v=V/m=1/\rho$. Specific gravity compares density with a reference density, usually liquid water near standard conditions for liquids.

A disciplined setup starts by drawing the boundary and labeling what can cross it: heat, work, mass, momentum, or species. Then choose a property basis, often per unit mass for closed systems and per unit time for control volumes. Finally, check that all temperatures in ratios are absolute and that all pressure data are on the same absolute or gage basis.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In basic concepts, units, and measurements, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

The foundational formulas are mostly conversion and measurement relations, but they control later first-law and second-law work:

$$
\begin{aligned}
\rho &= \frac{m}{V}, & v &= \frac{V}{m}=\frac{1}{\rho}, \\
P &= \frac{F}{A}, & P_{\mathrm{abs}} &= P_{\mathrm{atm}}+P_{\mathrm{gage}}, \\
T(K) &= T({}^{\circ}C)+273.15, & T(R) &= T({}^{\circ}F)+459.67.
\end{aligned}
$$

For a static fluid of constant density, the hydrostatic pressure change is

$$
\Delta P = \rho g \Delta z
$$

where $\Delta z$ is the vertical depth measured downward. This relation underlies manometers, barometers, tank pressure readings, and many checks on pressure sensor data.

Dimensional homogeneity is a theorem-level habit rather than a cosmetic rule. Every term in a valid physical equation must have the same dimensions. For example, $P V$ has units of energy because $\mathrm{kPa\,m^3}=\mathrm{kJ}$. This fact is why boundary work can be computed from the area under a $P$-$V$ curve and why the ideal-gas relation $Pv=RT$ is dimensionally consistent when $R$ is chosen in matching units.

The state postulate is used most often by asking whether the substance is simple and compressible, then selecting two independent intensive properties. A piston-cylinder of water in the two-phase dome is not fixed by $T$ and $P$ alone; it also needs a quality, specific volume, or another independent property. By contrast, an ideal gas at known $T$ and $P$ has $v=RT/P$.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

| Concept | Mathematical cue | Engineering consequence |
|---|---:|---|
| Closed system | $m=\mathrm{constant}$ | Boundary work and heat may cross, but no mass crosses. |
| Control volume | $\dot m_{\mathrm{in}}$ and $\dot m_{\mathrm{out}}$ may exist | Flow work is included through enthalpy. |
| Intensive property | independent of mass | Two independent intensive properties can fix a simple compressible state. |
| Extensive property | doubles when the system is doubled | Use specific quantities for table lookup and comparison. |
| Absolute pressure | $P_{\mathrm{abs}}=P_{\mathrm{atm}}+P_g$ | Required in ideal-gas and property calculations. |
| Temperature difference | $\Delta T(K)=\Delta T({}^{\circ}C)$ | Temperature differences may use Celsius increments, but temperature ratios may not. |

ASCII sketch of common pressure references:

```text
absolute vacuum:        P = 0
                         |
                         |---- vacuum pressure ----|---- gage pressure ----|
local atmosphere:        P_atm --------------------- measured pressure
```

## Worked example 1: absolute pressure from a manometer

**Problem.** A gas tank is connected to a U-tube manometer containing mercury. The mercury level on the open-atmosphere side is $0.180\ \mathrm{m}$ higher than on the tank side. Local atmospheric pressure is $99.0\ \mathrm{kPa}$. Estimate the absolute tank pressure using $\rho_{\mathrm{Hg}}=13,600\ \mathrm{kg/m^3}$.

**Method.**

1. The higher mercury level is on the atmosphere side, so the tank pressure exceeds atmospheric pressure.
2. The gage pressure equals the hydrostatic head:

$$
\begin{aligned}
\Delta P &= \rho g h \\
&=(13,600\ \mathrm{kg/m^3})(9.81\ \mathrm{m/s^2})(0.180\ \mathrm{m}) \\
&=24,010\ \mathrm{Pa}=24.0\ \mathrm{kPa}.
\end{aligned}
$$

3. Convert to absolute pressure:

$$
P_{\mathrm{abs}}=P_{\mathrm{atm}}+P_g=99.0+24.0=123.0\ \mathrm{kPa}.
$$

**Checked answer.** The tank pressure is about $123\ \mathrm{kPa}$ absolute. The sign is reasonable because the tank-side mercury column is depressed, which requires a gas pressure above atmospheric.

## Worked example 2: using the state postulate with an ideal gas

**Problem.** A rigid tank contains $0.75\ \mathrm{kg}$ of air at $25{}^{\circ}C$ and $150\ \mathrm{kPa}$ absolute. Treat air as an ideal gas with $R=0.287\ \mathrm{kJ/(kg\,K)}$. Find the tank volume and explain why the state is fixed.

**Method.**

1. Convert temperature to kelvin:

$$
T=25+273.15=298.15\ \mathrm{K}.
$$

2. The two independent intensive properties are $T$ and $P$; for an ideal gas they fix $v$ through $Pv=RT$.

$$
\begin{aligned}
v &= \frac{RT}{P} \\
&=\frac{(0.287\ \mathrm{kJ/(kg\,K)})(298.15\ \mathrm{K})}{150\ \mathrm{kPa}}.
\end{aligned}
$$

3. Since $1\ \mathrm{kPa\,m^3}=1\ \mathrm{kJ}$,

$$
v=0.570\ \mathrm{m^3/kg}.
$$

4. Multiply by mass:

$$
V=mv=(0.75)(0.570)=0.428\ \mathrm{m^3}.
$$

**Checked answer.** The tank volume is $0.428\ \mathrm{m^3}$. The result is physically plausible: air at pressure above atmospheric has a specific volume smaller than roughly $0.85\ \mathrm{m^3/kg}$ at room temperature and $1\ \mathrm{atm}$.

## Code

```python
def tank_volume_air(m_kg, T_C, P_kPa, R=0.287):
    T_K = T_C + 273.15
    v = R * T_K / P_kPa  # kJ/kg divided by kPa = m^3/kg
    return m_kg * v

def hydrostatic_head_pressure(rho, h, g=9.81):
    return rho * g * h / 1000.0  # kPa

print(round(tank_volume_air(0.75, 25.0, 150.0), 3))
print(round(99.0 + hydrostatic_head_pressure(13600.0, 0.180), 1))
```

## Common pitfalls

- Using gage pressure in $Pv=RT$ or saturated-property calculations. Convert to absolute pressure first.
- Treating Celsius temperatures as absolute in ratios such as $T_L/T_H$.
- Calling heat or work a property. They are boundary interactions, not stored quantities.
- Assuming $T$ and $P$ are independent inside the saturated liquid-vapor dome.
- Forgetting that a control volume may have real and imaginary boundary segments.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [energy, heat, work, and the first law](/physics/thermodynamics/energy-heat-work-and-first-law)
- [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables)
- [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
