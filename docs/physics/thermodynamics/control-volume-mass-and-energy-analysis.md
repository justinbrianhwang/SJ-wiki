---
title: Control-Volume Mass and Energy Analysis
sidebar_position: 5
---

# Control-Volume Mass and Energy Analysis

Most engineering devices are open systems: turbines, compressors, nozzles, diffusers, pumps, boilers, condensers, throttling valves, mixing chambers, and heat exchangers all have mass crossing their boundaries. Control-volume analysis keeps the boundary fixed around the device and accounts for the energy carried with flowing matter.

The key new property is enthalpy. Flow work $Pv$ is automatically included in $h=u+Pv$, so the steady-flow energy equation can be written compactly. Cengel's method is device-oriented: after writing the general balance, simplify it using what is known about a particular device. A turbine emphasizes shaft work; a nozzle emphasizes kinetic energy; a heat exchanger emphasizes heat transfer between streams; a throttle is nearly isenthalpic.

## Definitions

- A **control volume** is a selected region in space through which mass may flow. Its boundary is the control surface.
- **Mass flow rate** is $\dot m=\rho V_n A$, where $V_n$ is the velocity component normal to the area.
- **Volume flow rate** is $\dot V=V_nA$ for uniform flow, and $\dot m=\rho\dot V=\dot V/v$.
- **Steady flow** means properties at any fixed point in the control volume do not change with time. Mass and energy stored in the control volume are then constant.
- **Flow work** is the work needed to push mass into or out of a control volume. It appears as $Pv$ per unit mass and combines with $u$ to form enthalpy.
- A **nozzle** increases velocity at the expense of enthalpy. A **diffuser** increases pressure by slowing a stream.
- A **turbine** produces shaft work from a pressure and enthalpy drop. A **compressor** or **pump** consumes shaft work to raise pressure.
- A **throttling valve** is a restriction with negligible heat transfer, work, and kinetic-potential changes; it is commonly modeled as $h_1\approx h_2$.
- A **mixing chamber** combines streams, usually with no shaft work and negligible kinetic and potential energy changes.
- A **heat exchanger** transfers heat between streams without shaft work; the outer boundary may be nearly adiabatic while heat flows internally between fluids.

The reliable sequence is mass balance first, energy balance second, device assumptions third. The mass balance may determine an unknown flow rate or mixing fraction before the energy equation can be evaluated. In transient filling and emptying problems, storage terms remain and the steady-flow simplification is not valid.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In control-volume mass and energy analysis, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

The conservation of mass for a control volume is

$$
\frac{dm_{\mathrm{CV}}}{dt}
=\sum \dot m_{\mathrm{in}}-\sum \dot m_{\mathrm{out}}.
$$

At steady state,

$$
\sum \dot m_{\mathrm{in}}=\sum \dot m_{\mathrm{out}}.
$$

The general steady-flow energy equation is

$$
\dot Q-\dot W
 +\sum_{\mathrm{in}}\dot m\left(h+\frac{V^2}{2}+gz\right)
 =
\sum_{\mathrm{out}}\dot m\left(h+\frac{V^2}{2}+gz\right).
$$

For one-inlet, one-exit steady devices, divide by $\dot m$:

$$
q-w=(h_2-h_1)+\frac{V_2^2-V_1^2}{2}+g(z_2-z_1).
$$

Common reductions are:

$$
\begin{aligned}
\text{turbine: } & w_{\mathrm{out}}\approx h_1-h_2, \\
\text{compressor: } & w_{\mathrm{in}}\approx h_2-h_1, \\
\text{nozzle: } & h_1-h_2\approx \frac{V_2^2-V_1^2}{2}, \\
\text{throttle: } & h_1\approx h_2.
\end{aligned}
$$

Remember that velocity terms in SI are in $\mathrm{m^2/s^2}$; divide by $1000$ to convert to $\mathrm{kJ/kg}$.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

| Device | Dominant conversion | Usual simplifications | Core result |
|---|---|---|---|
| Nozzle | enthalpy to kinetic energy | $q\approx0$, $w=0$, $\Delta z\approx0$ | $V_2$ rises as $h$ falls |
| Diffuser | kinetic energy to pressure/enthalpy | $q\approx0$, $w=0$ | velocity falls |
| Turbine | enthalpy to shaft work | adiabatic, small $\Delta KE$, $\Delta PE$ | $\dot W\approx\dot m(h_1-h_2)$ |
| Compressor | shaft work to enthalpy | adiabatic, small $\Delta KE$ | $\dot W_{in}\approx\dot m(h_2-h_1)$ |
| Throttle | pressure drop at nearly constant enthalpy | $q\approx0$, $w=0$ | $h_1\approx h_2$ |
| Heat exchanger | heat between streams | outer boundary adiabatic | enthalpy lost by hot stream equals gained by cold stream |

## Worked example 1: adiabatic turbine power

**Problem.** Steam enters an adiabatic turbine at $h_1=3200\ \mathrm{kJ/kg}$ and exits at $h_2=2500\ \mathrm{kJ/kg}$. The mass flow rate is $2.0\ \mathrm{kg/s}$. Kinetic and potential energy changes are negligible. Find the turbine power output.

**Method.**

1. Steady mass balance gives the same mass flow rate at inlet and exit.
2. For an adiabatic turbine with negligible kinetic and potential changes:

$$
\dot W_{\mathrm{out}}=\dot m(h_1-h_2).
$$

3. Substitute:

$$
\dot W_{\mathrm{out}}
=(2.0)(3200-2500)
=1400\ \mathrm{kJ/s}.
$$

4. Convert $\mathrm{kJ/s}$ to $\mathrm{kW}$:

$$
\dot W_{\mathrm{out}}=1400\ \mathrm{kW}=1.4\ \mathrm{MW}.
$$

**Checked answer.** The positive output is expected because the steam enthalpy drops through the turbine.

## Worked example 2: exit velocity from an adiabatic nozzle

**Problem.** Air enters a nozzle with $h_1=430\ \mathrm{kJ/kg}$ and $V_1=40\ \mathrm{m/s}$. It exits with $h_2=390\ \mathrm{kJ/kg}$. Heat transfer, work, and elevation change are negligible. Find the exit velocity.

**Method.**

1. The nozzle energy balance is

$$
h_1+\frac{V_1^2}{2}=h_2+\frac{V_2^2}{2}
$$

when both kinetic terms are in the same units as enthalpy.

2. Convert the inlet kinetic energy:

$$
\frac{V_1^2}{2}=\frac{40^2}{2}=800\ \mathrm{m^2/s^2}=0.800\ \mathrm{kJ/kg}.
$$

3. Solve for exit kinetic energy:

$$
\frac{V_2^2}{2}
=(h_1-h_2)+0.800
=40.8\ \mathrm{kJ/kg}.
$$

4. Convert back to $\mathrm{m^2/s^2}$ and solve:

$$
V_2=\sqrt{2(40.8)(1000)}=286\ \mathrm{m/s}.
$$

**Checked answer.** The exit velocity is about $286\ \mathrm{m/s}$. The velocity increase is large because a $40\ \mathrm{kJ/kg}$ enthalpy drop is a large kinetic-energy change.

## Code

```python
import math

def turbine_power(mdot, h1, h2):
    return mdot * (h1 - h2)  # kW

def nozzle_exit_velocity(h1, h2, V1):
    ke2_kJkg = (h1 - h2) + V1**2 / 2000.0
    return math.sqrt(2.0 * ke2_kJkg * 1000.0)

print(turbine_power(2.0, 3200.0, 2500.0))
print(nozzle_exit_velocity(430.0, 390.0, 40.0))
```

## Common pitfalls

- Using internal energy instead of enthalpy for steady-flow devices with flow work.
- Forgetting the factor of $1000$ when converting $V^2/2$ to $\mathrm{kJ/kg}$.
- Applying steady-flow equations to startup, shutdown, filling, or emptying without storage terms.
- Assuming every valve or nozzle is adiabatic without checking heat transfer or residence time.
- Dropping mass balance in heat exchangers and mixing chambers before determining flow rates.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [energy, heat, work, and the first law](/physics/thermodynamics/energy-heat-work-and-first-law)
- [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance)
- [compressible flow](/physics/thermodynamics/compressible-flow)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
