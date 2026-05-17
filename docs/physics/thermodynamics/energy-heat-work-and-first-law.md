---
title: Energy, Heat, Work, and the First Law
sidebar_position: 2
---

# Energy, Heat, Work, and the First Law

The first law is the accounting principle of thermodynamics: energy can cross a boundary as heat, work, or mass flow, and the difference between energy entering and leaving changes the energy stored in the system. Cengel's treatment stresses that this is not just a formula but a modeling framework. The same balance can describe a battery, a human body, a motor, a turbine, a water heater, or a power plant.

The hard part is not memorizing conservation of energy. It is recognizing the mode of transfer and using a sign convention consistently. Heat is energy transfer driven by a temperature difference. Work is any other energy transfer associated with a generalized force acting through a generalized displacement, including shaft work, electrical work, spring work, boundary work, and lifting work.

## Definitions

- **Total energy** of a system is the sum of internal, kinetic, and potential energies: $E=U+KE+PE$. Internal energy contains microscopic molecular translation, rotation, vibration, bonding, and other microscopic modes.
- **Macroscopic energy** is associated with the system as a whole relative to an external reference frame. Kinetic energy is $KE=mV^2/2$ and potential energy is $PE=mgz$.
- **Heat** is energy crossing the boundary because of a temperature difference. It is denoted $Q$ or $\dot Q$ and is path dependent.
- **Work** is energy crossing the boundary by mechanisms other than temperature difference. It is denoted $W$ or $\dot W$ and is path dependent.
- A **closed-system energy balance** has no mass crossing the boundary. The differential convention used here is $dU=\delta Q-\delta W$ when kinetic and potential energy changes are negligible.
- A **cycle** has zero net change in system properties: $\Delta E_{\mathrm{cycle}}=0$. Therefore the net heat transfer over a cycle equals the net work output over that cycle.
- **Power** is the rate of work transfer. In SI, $1\ \mathrm{kW}=1\ \mathrm{kJ/s}$, a conversion that is especially useful in steady-flow devices.
- **Efficiency** compares desired output to required input. Thermal efficiency, motor efficiency, generator efficiency, pump efficiency, and overall plant efficiency all apply this same ratio logic to different boundaries.
- **Energy quality** anticipates the second law: one kilojoule of shaft work is more useful than one kilojoule of low-temperature heat even though the first law counts both as one kilojoule.

The first-law workflow is boundary first, signs second, properties third. Draw arrows for heat and work, choose whether work by the system is positive, and only then write the balance. When mass crosses the boundary, do not use the closed-system form; use a control-volume balance with enthalpy carrying flow work.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In energy, heat, work, and the first law, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

For a closed system,

$$
\Delta E = Q - W
$$

when $Q$ is positive into the system and $W$ is positive out of the system. In differential internal-energy form,

$$
dU = \delta Q - \delta W
$$

where $\delta$ reminds us that heat and work are inexact differentials.

The total energy change is

$$
\Delta E = \Delta U + \Delta KE + \Delta PE
= m(u_2-u_1)+\frac{m(V_2^2-V_1^2)}{2}+mg(z_2-z_1).
$$

The rate form for a closed system is

$$
\frac{dE_{\mathrm{sys}}}{dt}=\dot Q-\dot W.
$$

Common work modes include

$$
W_{\mathrm{electric}}=\int VI\,dt, \qquad
W_{\mathrm{shaft}}=2\pi N\tau, \qquad
W_{\mathrm{spring}}=\frac{1}{2}k(x_2^2-x_1^2).
$$

Mechanical energy of a flowing fluid, neglecting internal energy, is often written per unit mass as

$$
e_{\mathrm{mech}}=\frac{P}{\rho}+\frac{V^2}{2}+gz.
$$

This expression foreshadows pump, turbine, and pipe-flow calculations. The first law never tells us whether a proposed process is possible by itself. A process that conserves energy may still violate the second law if it requires heat to flow from cold to hot without compensation or converts all reservoir heat into net work in a cycle.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

```mermaid
flowchart LR
  A["Choose boundary"] --> B["Label heat and work"]
  B --> C["Select sign convention"]
  C --> D["Write energy balance"]
  D --> E["Evaluate property changes"]
  E --> F["Check units and direction"]
```

| Transfer mode | Driving idea | Typical symbol | Stored in system? |
|---|---|---:|---|
| Heat | Temperature difference | $Q$ | No, heat is boundary crossing. |
| Boundary work | Moving boundary under pressure | $\int P\,dV$ | No, work is boundary crossing. |
| Shaft work | Torque through rotation | $2\pi N\tau$ | No. |
| Electrical work | Charge moved through potential | $\int VI\,dt$ | No. |
| Internal energy | Molecular storage | $U$ | Yes, it is a property. |

## Worked example 1: closed tank heated by an electric resistor

**Problem.** A rigid, insulated tank contains air. A $1.2\ \mathrm{kW}$ electric resistor operates inside the tank for $10\ \mathrm{min}$. The tank has no shaft crossing and no moving boundary. Find the increase in internal energy of the air.

**Method.**

1. Choose the air plus resistor interior as the closed system. No mass crosses the tank boundary.
2. The tank is insulated, so $Q=0$ through the outer boundary. The electrical energy crosses as work input to the system.
3. With the convention $\Delta E=Q-W$ and work positive when done by the system, electrical work done on the system is negative:

$$
W=-W_{\mathrm{elec,in}}.
$$

4. Compute the electrical input:

$$
W_{\mathrm{elec,in}}=(1.2\ \mathrm{kJ/s})(10\times 60\ \mathrm{s})=720\ \mathrm{kJ}.
$$

5. Kinetic and potential energy changes are negligible, so

$$
\Delta U=0-(-720)=720\ \mathrm{kJ}.
$$

**Checked answer.** The air internal energy increases by $720\ \mathrm{kJ}$. If the same boundary had included the electrical power supply, the bookkeeping would change, but the tank air would still receive $720\ \mathrm{kJ}$ before losses.

## Worked example 2: energy balance for a hoist motor

**Problem.** A motor lifts a $400\ \mathrm{kg}$ elevator car through $12\ \mathrm{m}$ in $20\ \mathrm{s}$. The motor draws $3.0\ \mathrm{kW}$ of electrical power. Neglect kinetic energy changes and find the useful lifting power and the motor efficiency during the lift.

**Method.**

1. The useful energy output is the increase in gravitational potential energy:

$$
\Delta PE=mg\Delta z=(400)(9.81)(12)=47,088\ \mathrm{J}=47.1\ \mathrm{kJ}.
$$

2. Divide by the lift time:

$$
\dot W_{\mathrm{useful}}=\frac{47.1\ \mathrm{kJ}}{20\ \mathrm{s}}=2.35\ \mathrm{kW}.
$$

3. The electrical input during the same interval is $3.0\ \mathrm{kW}$. Efficiency is desired output over required input:

$$
\eta=\frac{2.35}{3.0}=0.785.
$$

4. Express as a percentage:

$$
\eta=78.5\%.
$$

**Checked answer.** The useful lifting power is $2.35\ \mathrm{kW}$ and the efficiency is about $79\%$. The remaining power is converted to internal energy of the motor, cables, and surroundings through losses.

## Code

```python
def resistor_energy(power_kW, minutes):
    return power_kW * minutes * 60.0  # kJ

def hoist_efficiency(mass, height, time_s, electric_power_kW, g=9.81):
    useful_kJ = mass * g * height / 1000.0
    useful_kW = useful_kJ / time_s
    return useful_kW, useful_kW / electric_power_kW

print(resistor_energy(1.2, 10))
print(hoist_efficiency(400, 12, 20, 3.0))
```

## Common pitfalls

- Mixing sign conventions inside the same balance. State whether work by the system is positive and keep it throughout.
- Calling energy stored as heat. A system stores internal energy, not heat.
- Dropping kinetic or potential energy changes without checking velocities or elevation changes.
- Confusing kW with kWh. Power is a rate; energy is rate multiplied by time.
- Using efficiency without defining the desired output and required input for the chosen boundary.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [basic concepts, units, and measurements](/physics/thermodynamics/basic-concepts-units-and-measurements)
- [closed-system energy analysis](/physics/thermodynamics/closed-system-energy-analysis)
- [second-law heat engines and refrigerators](/physics/thermodynamics/second-law-heat-engines-and-refrigerators)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
