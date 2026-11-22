---
title: Basic Concepts, Units, and Measurements
sidebar_position: 1
---

# Basic Concepts, Units, and Measurements

Engineering thermodynamics begins by deciding what portion of the world is being analyzed and how its measurable state is described. The vocabulary is deliberately strict: a system differs from its surroundings, a property differs from a path quantity, and a temperature reading is meaningful because the zeroth law makes thermometers possible. These distinctions support later energy, entropy, exergy, cycle, and flow analyses.

The emphasis is practical. Before solving for turbine power or refrigerator performance, an engineer must choose the system boundary, decide whether mass crosses it, convert units without changing physical meaning, and distinguish absolute pressure and temperature from gage readings and temperature differences. These choices look elementary, but they prevent many of the largest errors in thermodynamics homework and design calculations.

## Boundaries, states, and properties

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
Before substituting numbers, state the boundary, time basis, property model, and sign convention. Then write the defining relation or general balance and remove terms only for stated physical reasons.

Keep the basis visible: per-unit-mass, molar, total, and rate quantities are not interchangeable. Multiplying $\mathrm{kJ/kg}$ by $\dot m$ gives a power only when the mass flow rate is in $\mathrm{kg/s}$.

## Measurement relations and unit discipline

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

Dimensional homogeneity is a theorem-level habit rather than a cosmetic rule. Every term in a valid physical equation must have the same dimensions. For example, $P V$ has units of energy because $\mathrm{kPa\,m^3}=\mathrm{kJ}$. Consequently, boundary work can be computed from the area under a $P$-$V$ curve, and the ideal-gas relation $Pv=RT$ is dimensionally consistent when $R$ is chosen in matching units.

The state postulate is used most often by asking whether the substance is simple and compressible, then selecting two independent intensive properties. A piston-cylinder of water in the two-phase dome is not fixed by $T$ and $P$ alone; it also needs a quality, specific volume, or another independent property. By contrast, an ideal gas at known $T$ and $P$ has $v=RT/P$.
Use limiting cases as measurement checks: zero gage pressure must equal local atmospheric pressure, and doubling a system must double its extensive properties without changing its intensive properties. Record the phase region, property basis, and units beside every table value.

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

## Reading absolute pressure from a manometer

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

## Fixing an ideal-gas state from two properties

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

## Checks before calculation

- Using gage pressure in $Pv=RT$ or saturated-property calculations. Convert to absolute pressure first.
- Treating Celsius temperatures as absolute in ratios such as $T_L/T_H$.
- Calling heat or work a property. They are boundary interactions, not stored quantities.
- Assuming $T$ and $P$ are independent inside the saturated liquid-vapor dome.
- Forgetting that a control volume may have real and imaginary boundary segments.

<div className="see-also">

See also: [energy, heat, work, and the first law](/physics/thermodynamics/energy-heat-work-and-first-law) · [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables) · [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis) · [microscopic foundations](/physics/statistical-mechanics/intro) · [basic thermal physics](/physics/general/intro) · [thermochemistry](/chemistry/general/thermochemistry) · [physical chemistry](/chemistry/physical-chemistry/intro) · [engineering mathematics](/math/engineering-math/intro) · [thermal systems control](/cs/control-engineering/intro)

</div>
