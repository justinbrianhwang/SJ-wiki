---
title: Closed-System Energy Analysis
sidebar_position: 4
---

# Closed-System Energy Analysis

Closed-system analysis applies the first law to a fixed mass. The system may expand, compress, heat, cool, accelerate, or change elevation, but no mass crosses the boundary. This is the natural model for piston-cylinder devices, rigid tanks, sealed containers, solids and liquids being heated, and many transient steps before a valve opens.

The most distinctive closed-system term is moving boundary work. In a quasi-equilibrium piston-cylinder process, the work is the area under the $P$-$V$ curve. That geometric interpretation is simple, but it makes the answer path dependent: the same initial and final states can require different amounts of work if the pressure-volume path is different.

## A fixed mass and its energy transfers

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
State the boundary, property model, work modes, and sign convention before substituting numbers. A rigid-tank balance and a quasi-equilibrium piston-cylinder balance may use the same end-state properties but retain different work terms. Begin with the full closed-system balance and cancel each term for a stated physical reason.

Property tables report specific quantities, while the first law may be written for the whole mass. Mark each $u$, $h$, and work term as specific or total before combining them.

## The energy balance and its process models

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
The process model should recover its limiting cases: a rigid boundary gives zero boundary work, and the polytropic expression approaches the logarithmic isothermal result as $n$ approaches 1. Keep total energy and energy per unit mass distinct throughout the calculation.

## Boundary work as area on a $P$-$V$ plot

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

## Work during polytropic compression

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

## Heating air in a rigid tank

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

## Recomputing the two cases

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

## Sign, path, and property checks

- Using $\int P\,dV$ for a non-quasi-equilibrium process without a meaningful system pressure path.
- Forgetting that compression work by the system is negative under the common engineering sign convention.
- Using $c_p$ instead of $c_v$ for ideal-gas internal-energy changes.
- Assuming a rigid tank has no energy transfer; it has no boundary work, but it may have heat or electrical work.
- Mixing total and specific quantities without multiplying or dividing by mass.

<div className="see-also">

See also: [energy, heat, work, and the first law](/physics/thermodynamics/energy-heat-work-and-first-law) · [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables) · [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance) · [microscopic foundations](/physics/statistical-mechanics/intro) · [basic thermal physics](/physics/general/intro) · [thermochemistry](/chemistry/general/thermochemistry) · [physical chemistry](/chemistry/physical-chemistry/intro) · [engineering mathematics](/math/engineering-math/intro) · [thermal systems control](/cs/control-engineering/intro)

</div>
