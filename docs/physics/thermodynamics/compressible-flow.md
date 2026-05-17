---
title: Compressible Flow
sidebar_position: 17
---

# Compressible Flow

Compressible flow appears when density changes are dynamically important, especially in high-speed gases. The Mach number compares flow speed with local speed of sound and determines whether pressure disturbances can travel upstream. This leads to choked nozzles, shock waves, expansion fans, and strong coupling between area, velocity, pressure, temperature, and entropy.

Cengel's final chapter connects thermodynamics with gas dynamics. The same steady-flow energy equation is used, but kinetic energy is no longer negligible. Isentropic nozzle relations describe ideal acceleration. Normal and oblique shocks describe thin irreversible compression regions. Fanno and Rayleigh flow add friction and heat-transfer effects in ducts.

## Definitions

- **Mach number** is $Ma=V/c$, where $c=\sqrt{kRT}$ is the ideal-gas speed of sound.
- **Subsonic flow** has $Ma\lt 1$; pressure disturbances can travel upstream. **Supersonic flow** has $Ma\gt 1$; disturbances are confined downstream within Mach waves.
- **Stagnation state** is the state reached by bringing a flow to rest adiabatically and reversibly.
- **Stagnation temperature** $T_0$ is constant in adiabatic flows with no shaft work, even across shocks for ideal gases with negligible potential energy.
- **Choked flow** occurs when Mach number reaches 1 at a minimum area, fixing the maximum mass flow for given stagnation conditions.
- A **converging nozzle** can choke at the exit. A **converging-diverging nozzle** can accelerate flow to supersonic speeds downstream of a throat.
- A **normal shock** is a nearly discontinuous compression wave perpendicular to the flow; it is adiabatic but irreversible.
- An **oblique shock** is inclined to the upstream flow and turns supersonic flow toward itself.
- A **Prandtl-Meyer expansion fan** turns supersonic flow away from itself through an isentropic expansion.
- **Fanno flow** is adiabatic flow with friction in a constant-area duct. **Rayleigh flow** is frictionless constant-area flow with heat transfer.

Compressible-flow calculations are sensitive to whether a process is isentropic. Nozzles before shocks are often modeled as isentropic; shocks never are. Across a shock, entropy rises and stagnation pressure falls, even though stagnation temperature remains constant for an adiabatic no-work ideal-gas flow.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In compressible flow, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

For an ideal gas,

$$
c=\sqrt{kRT}, \qquad Ma=\frac{V}{c}.
$$

The stagnation temperature relation for adiabatic no-work flow is

$$
T_0=T\left(1+\frac{k-1}{2}Ma^2\right).
$$

For isentropic flow,

$$
\frac{P_0}{P}
=\left(1+\frac{k-1}{2}Ma^2\right)^{k/(k-1)},
$$

$$
\frac{\rho_0}{\rho}
=\left(1+\frac{k-1}{2}Ma^2\right)^{1/(k-1)}.
$$

The choked mass flux for an ideal gas is

$$
\frac{\dot m}{A^*}
=\frac{P_0}{\sqrt{T_0}}
\sqrt{\frac{k}{R}}
\left(\frac{2}{k+1}\right)^{(k+1)/(2(k-1))}.
$$

Across a normal shock, $Ma_2\lt 1$ for upstream supersonic flow and stagnation pressure decreases. One normal-shock relation is

$$
Ma_2^2=
\frac{1+\frac{k-1}{2}Ma_1^2}{kMa_1^2-\frac{k-1}{2}}.
$$

The Mach angle for weak disturbances is

$$
\mu=\sin^{-1}\left(\frac{1}{Ma}\right).
$$

These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

ASCII nozzle behavior:

```text
converging-diverging nozzle

subsonic       throat        supersonic
Ma < 1        Ma = 1        Ma > 1
  --->       /\____/\       --->
            /      \
```

| Process | Entropy | Stagnation temperature | Stagnation pressure |
|---|---:|---:|---:|
| Isentropic nozzle | constant | constant | constant |
| Normal shock | increases | approximately constant | decreases |
| Adiabatic duct with friction | increases | constant | decreases |
| Heat addition in Rayleigh flow | generally changes | changes | changes |

## Worked example 1: stagnation properties from Mach number

**Problem.** Air flows at $Ma=2.0$, $T=250\ \mathrm{K}$, and $P=50\ \mathrm{kPa}$. Use $k=1.4$. Find $T_0$ and $P_0$ if the deceleration to stagnation is isentropic.

**Method.**

1. Compute the temperature factor:

$$
1+\frac{k-1}{2}Ma^2
=1+0.2(2.0)^2
=1.8.
$$

2. Stagnation temperature:

$$
T_0=250(1.8)=450\ \mathrm{K}.
$$

3. Stagnation pressure ratio:

$$
\frac{P_0}{P}=1.8^{k/(k-1)}=1.8^{3.5}=7.82.
$$

4. Stagnation pressure:

$$
P_0=50(7.82)=391\ \mathrm{kPa}.
$$

**Checked answer.** The stagnation temperature is $450\ \mathrm{K}$ and stagnation pressure is $391\ \mathrm{kPa}$. The large pressure ratio reflects supersonic kinetic energy and isentropic compression.

## Worked example 2: choked mass flow through a throat

**Problem.** Air with $k=1.4$ and $R=287\ \mathrm{J/(kg\,K)}$ enters a nozzle with stagnation conditions $P_0=500\ \mathrm{kPa}$ and $T_0=300\ \mathrm{K}$. The throat area is $A^*=0.010\ \mathrm{m^2}$. Find the choked mass flow rate.

**Method.**

1. Use the ideal-gas choked-flow formula:

$$
\dot m=A^*\frac{P_0}{\sqrt{T_0}}
\sqrt{\frac{k}{R}}
\left(\frac{2}{k+1}\right)^{(k+1)/(2(k-1))}.
$$

2. Evaluate the pressure-temperature factor:

$$
\frac{P_0}{\sqrt{T_0}}=\frac{500000}{\sqrt{300}}=28867\ \mathrm{Pa/K^{1/2}}.
$$

3. Gas factor:

$$
\sqrt{k/R}=\sqrt{1.4/287}=0.06985.
$$

4. Critical factor:

$$
\left(\frac{2}{2.4}\right)^3=0.5787.
$$

5. Mass flux:

$$
G^*=28867(0.06985)(0.5787)=1167\ \mathrm{kg/(m^2\,s)}.
$$

6. Mass flow:

$$
\dot m=0.010(1167)=11.7\ \mathrm{kg/s}.
$$

**Checked answer.** The choked mass flow is about $11.7\ \mathrm{kg/s}$. Lowering downstream pressure further will not increase mass flow unless upstream stagnation conditions or throat area change.

## Code

```python
import math

def stagnation_from_mach(T, P, Ma, k=1.4):
    factor = 1.0 + (k - 1.0) / 2.0 * Ma**2
    T0 = T * factor
    P0 = P * factor ** (k / (k - 1.0))
    return T0, P0

def choked_mdot(P0, T0, area, k=1.4, R=287.0):
    factor = (2.0 / (k + 1.0)) ** ((k + 1.0) / (2.0 * (k - 1.0)))
    flux = P0 / math.sqrt(T0) * math.sqrt(k / R) * factor
    return area * flux

print(stagnation_from_mach(250.0, 50.0, 2.0))
print(choked_mdot(500000.0, 300.0, 0.010))
```

## Common pitfalls

- Using incompressible Bernoulli equations at high Mach number without checking density changes.
- Treating shocks as isentropic. They are adiabatic but irreversible.
- Forgetting that stagnation pressure drops across shocks and frictional ducts.
- Expecting a converging nozzle to produce supersonic flow without a diverging section downstream of a choked throat.
- Using Celsius temperature in speed-of-sound or stagnation formulas.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis)
- [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance)
- [gas power cycles](/physics/thermodynamics/gas-power-cycles)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
