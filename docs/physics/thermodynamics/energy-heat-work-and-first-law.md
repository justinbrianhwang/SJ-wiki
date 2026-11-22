---
title: Energy, Heat, Work, and the First Law
sidebar_position: 2
---

# Energy, Heat, Work, and the First Law

The first law is the accounting principle of thermodynamics: energy can cross a boundary as heat, work, or mass flow, and the difference between energy entering and leaving changes the energy stored in the system. It is a modeling framework as well as an equation. The same balance can describe a battery, a human body, a motor, a turbine, a water heater, or a power plant.

The hard part is not memorizing conservation of energy. It is recognizing the mode of transfer and using a sign convention consistently. Heat is energy transfer driven by a temperature difference. Work is any other energy transfer associated with a generalized force acting through a generalized displacement, including shaft work, electrical work, spring work, boundary work, and lifting work.

## Stored energy versus boundary transfer

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
State the boundary, time basis, energy-transfer modes, and sign convention before substituting numbers. A closed-system balance and a steady-flow balance may contain similar quantities, but mass flow changes the accounting. Write the general balance first, then cancel terms with a physical reason.

Label every quantity as total, specific, or rate based. In particular, $\mathrm{kW}$ is $\mathrm{kJ/s}$; it becomes energy only after multiplication by a time interval.

## First-law balances and work modes

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

Here $N$ is the number of shaft revolutions when torque is constant.

Mechanical energy of a flowing fluid, neglecting internal energy, is often written per unit mass as

$$
e_{\mathrm{mech}}=\frac{P}{\rho}+\frac{V^2}{2}+gz.
$$

This expression foreshadows pump, turbine, and pipe-flow calculations. The first law never tells us whether a proposed process is possible by itself. A process that conserves energy may still violate the second law if it requires heat to flow from cold to hot without compensation or converts all reservoir heat into net work in a cycle.
A finished balance should identify every crossing term, reduce to $\Delta E=0$ when there is no net transfer, and preserve the chosen sign convention. Report whether each result is an energy, a specific energy, or a rate.

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

## A closed tank heated electrically

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

**Checked answer.** The tank contents gain $720\ \mathrm{kJ}$. The same value is the air's internal-energy increase once the resistor returns to its initial temperature, or when energy stored in the resistor is negligible. Including the electrical power supply inside the boundary would change the bookkeeping but not the energy delivered to the tank contents.

## Useful power from a hoist motor

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

## Boundary and sign checks

- Mixing sign conventions inside the same balance. State whether work by the system is positive and keep it throughout.
- Calling energy stored as heat. A system stores internal energy, not heat.
- Dropping kinetic or potential energy changes without checking velocities or elevation changes.
- Confusing kW with kWh. Power is a rate; energy is rate multiplied by time.
- Using efficiency without defining the desired output and required input for the chosen boundary.

<div className="see-also">

See also: [basic concepts, units, and measurements](/physics/thermodynamics/basic-concepts-units-and-measurements) · [closed-system energy analysis](/physics/thermodynamics/closed-system-energy-analysis) · [second-law heat engines and refrigerators](/physics/thermodynamics/second-law-heat-engines-and-refrigerators) · [microscopic foundations](/physics/statistical-mechanics/intro) · [basic thermal physics](/physics/general/intro) · [thermochemistry](/chemistry/general/thermochemistry) · [physical chemistry](/chemistry/physical-chemistry/intro) · [engineering mathematics](/math/engineering-math/intro) · [thermal systems control](/cs/control-engineering/intro)

</div>
