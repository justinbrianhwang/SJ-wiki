---
title: Compressible Flow
sidebar_position: 17
---

# Compressible Flow

Compressible flow appears when density changes are dynamically important, especially in high-speed gases. The Mach number compares flow speed with local speed of sound and determines whether pressure disturbances can travel upstream. This leads to choked nozzles, shock waves, expansion fans, and strong coupling between area, velocity, pressure, temperature, and entropy.

The steady-flow energy equation still applies, but kinetic energy is now comparable to enthalpy change. Isentropic nozzle relations describe ideal acceleration. Normal and oblique shocks describe thin irreversible compression regions. Fanno and Rayleigh models isolate friction and heat-transfer effects in constant-area ducts.

## Mach number and stagnation state

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
Specify the duct or nozzle geometry, stagnation conditions, gas model, and irreversibilities before substituting numbers. Isentropic relations apply only between states connected without shocks, friction, or heat transfer. The steady-flow balance must retain kinetic energy because it is often comparable to the enthalpy change.

Stagnation enthalpy and kinetic energy are normally compared per unit mass; mass flux adds the per-area, per-time basis. Unit conversions between $\mathrm{J/kg}$ and $\mathrm{kJ/kg}$ therefore belong in the written calculation.

## Isentropic acceleration, choking, and shocks

For steady adiabatic flow with no shaft work and negligible potential-energy change,

$$
h+\frac{V^2}{2}=h_0.
$$

For a calorically perfect ideal gas, $h=c_pT$, so bringing the flow to rest reversibly gives

$$
c_pT+\frac{V^2}{2}=c_pT_0.
$$

Using $V=Ma\sqrt{kRT}$ and $c_p=kR/(k-1)$ leads to

$$
\frac{T_0}{T}=1+\frac{k-1}{2}Ma^2.
$$

The stagnation temperature relation comes from energy conservation and remains valid across an adiabatic shock under the stated gas model. The stagnation pressure relation additionally requires an isentropic path, so stagnation pressure falls across a shock.

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

## Why a diverging passage accelerates supersonic flow

Steady one-dimensional continuity gives

$$
\rho AV=\text{constant}.
$$

In differential form,

$$
\frac{d\rho}{\rho}+\frac{dA}{A}+\frac{dV}{V}=0.
$$

For isentropic flow, $dP=c^2d\rho$. The momentum equation along a streamline is $dP+\rho VdV=0$, so

$$
\frac{d\rho}{\rho}=-\frac{V^2}{c^2}\frac{dV}{V}
=-Ma^2\frac{dV}{V}.
$$

Substitution into continuity yields the area-velocity relation

$$
\frac{dA}{A}=(Ma^2-1)\frac{dV}{V}.
$$

For $Ma\lt1$, acceleration requires decreasing area. For $Ma\gt1$, acceleration requires increasing area. At $Ma=1$, a smooth acceleration through sonic conditions requires an area extremum, normally the minimum throat of a converging-diverging nozzle.

Choking does not mean velocity stops responding everywhere. It means the mass flow can no longer increase in response to lower downstream pressure while upstream stagnation conditions and throat area remain fixed. Once a converging nozzle is choked, its exit is sonic. A converging-diverging nozzle can sustain a supersonic region only for a compatible back pressure; other back pressures place a shock inside or outside the nozzle, or leave the entire flow subsonic.

Check the low-Mach limit against incompressible behavior and the throat state against $Ma=1$. Relations based on constant $k$ and isentropic flow should be labeled as such, especially when shocks, friction, or high temperatures are present.

## Reading a converging-diverging nozzle

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
| Normal shock | increases | constant | decreases |
| Adiabatic duct with friction | increases | constant | decreases |
| Heat addition in Rayleigh flow | generally changes | changes | changes |

## Stagnation properties at Mach 2

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

## Choked mass flow through a throat

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

## A normal shock at Mach 2

**Problem.** Air with $k=1.4$ enters a normal shock at $Ma_1=2.0$, $P_1=100$ kPa, and $T_1=300$ K. Find downstream Mach number, pressure, density, and temperature ratios.

The downstream Mach number is

$$
Ma_2^2=
\frac{1+\frac{k-1}{2}Ma_1^2}
{kMa_1^2-\frac{k-1}{2}}.
$$

Substitution gives

$$
Ma_2^2=\frac{1+0.2(4)}{1.4(4)-0.2}
=\frac{1.8}{5.4}=0.3333,
$$

so $Ma_2=0.577$. The pressure ratio is

$$
\frac{P_2}{P_1}
=1+\frac{2k}{k+1}(Ma_1^2-1)
=1+\frac{2(1.4)}{2.4}(4-1)
=4.50.
$$

Hence $P_2=450$ kPa. The density ratio is

$$
\frac{\rho_2}{\rho_1}
=\frac{(k+1)Ma_1^2}{(k-1)Ma_1^2+2}
=\frac{(2.4)(4)}{(0.4)(4)+2}
=2.667.
$$

For an ideal gas,

$$
\frac{T_2}{T_1}
=\frac{P_2/P_1}{\rho_2/\rho_1}
=\frac{4.50}{2.667}=1.6875,
$$

so $T_2=506$ K. The shock converts directed kinetic energy into internal energy: static pressure, density, temperature, and entropy rise, while Mach number becomes subsonic. Stagnation temperature remains unchanged, but stagnation pressure falls because the process is irreversible.

## Fanno and Rayleigh limits

Fanno flow models an adiabatic constant-area duct with wall friction. Friction raises entropy and drives Mach number toward one: subsonic flow accelerates toward sonic conditions, while supersonic flow decelerates toward them. For a fixed inlet state and diameter, there is a maximum duct length before the model reaches a sonic limit.

Rayleigh flow models a frictionless constant-area duct with heat transfer. Heat addition drives both subsonic and supersonic branches toward a sonic state, though temperature and stagnation-property trends differ across the branches. Stagnation temperature changes because heat crosses the boundary. Real combustors and heated pipes may involve both heat transfer and friction, outside either isolated model.

| Model | Area | Heat transfer | Friction | Role of sonic state |
|---|---:|---:|---:|---|
| Isentropic nozzle | variable | none | none | throat condition |
| Fanno duct | constant | none | present | limiting duct length |
| Rayleigh duct | constant | present | none | limiting heat interaction |
| Normal shock | nearly constant locally | none | irreversible compression | supersonic to subsonic transition |

## Calculating stagnation state and choked flow

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

## Area ratio and nozzle branches

Combining continuity with the isentropic stagnation relations gives the area-Mach relation

$$
\frac{A}{A^*}
=\frac1{Ma}
\left[
\frac{2}{k+1}
\left(1+\frac{k-1}{2}Ma^2\right)
\right]^{\frac{k+1}{2(k-1)}}.
$$

For every area ratio greater than one, the equation has one subsonic and one supersonic solution. Geometry alone does not choose the branch. Upstream stagnation conditions, back pressure, starting history, and any shocks determine which state occurs.

For air with $k=1.4$ at $Ma=2$, the exponent is $3$. The bracket is

$$
\frac{2}{2.4}[1+0.2(4)]=(0.8333)(1.8)=1.5.
$$

Thus

$$
\frac{A}{A^*}=\frac1{2}(1.5)^3=1.6875.
$$

A nozzle section with area $1.6875A^*$ can also support a subsonic isentropic Mach number. Selecting the supersonic value assumes the flow has passed through a choked throat onto the supersonic branch without an intervening shock.

Mass flow can be expressed at any isentropic section as

$$
\dot m
=A\frac{P_0}{\sqrt{T_0}}
\sqrt{\frac{k}{R}}
Ma
\left(1+\frac{k-1}{2}Ma^2\right)^{-\frac{k+1}{2(k-1)}}.
$$

For fixed $A$, $P_0$, and $T_0$, the Mach-dependent factor is greatest at $Ma=1$. That maximum yields the choked-flow formula. The mass flux maximum is a calculus result, not an assertion that every minimum-area section must be sonic.

## Back pressure sets the nozzle pattern

Begin with a converging-diverging nozzle connected to a large reservoir and let back pressure fall. With a high back pressure, flow remains subsonic throughout: it accelerates in the converging part and decelerates in the diverging part. At one critical back pressure the throat reaches Mach one.

Lowering back pressure further cannot communicate through the sonic throat in the same way. A supersonic region forms downstream, often followed by a normal shock inside the diverging section. Across that shock the flow becomes subsonic and then adjusts to the exit pressure. As back pressure falls, the shock moves downstream and weakens relative to the expanding upstream state.

At the design back pressure, flow is isentropic to the exit and exit static pressure matches the surroundings. If exit pressure exceeds ambient, the jet is underexpanded and continues expanding outside. If exit pressure is below ambient, it is overexpanded and external compression waves or shocks adjust it. Real nozzle separation can occur under strong adverse pressure gradients.

The terms underexpanded and overexpanded refer to static-pressure mismatch, not to whether geometric area is too small or large in isolation. Rocket nozzles face changing ambient pressure during ascent, so one fixed geometry is perfectly expanded at only a limited condition.

## Oblique shocks and expansion fans

A supersonic stream turned into itself by a compression corner cannot adjust through smooth upstream communication. It forms an oblique shock. The velocity component normal to the shock obeys normal-shock relations, while the tangential component is unchanged in the inviscid model. The flow slows, pressure and temperature rise, and the direction turns toward the surface.

For a given upstream Mach number and modest turning angle, weak and strong oblique-shock solutions may exist. The weak branch is more commonly observed because it produces a smaller pressure rise and often leaves downstream flow supersonic. Beyond a maximum turning angle no attached solution exists, and a detached bow shock forms.

Turning a supersonic flow away from itself produces a Prandtl-Meyer expansion fan. The fan consists of a continuous spread of Mach waves; the ideal process is isentropic. Mach number rises while static pressure and temperature fall. Replacing an expansion fan with a single “expansion shock” would violate the entropy condition for ordinary gases.

Shock-expansion methods piece these elements together around wedges and nozzles. They depend on inviscid, steady, often constant-$k$ assumptions. Boundary layers introduce displacement thickness, friction, separation, and shock-boundary-layer interaction that can dominate real hardware.

## When the low-Mach approximation is acceptable

Density change rather than speed alone decides whether incompressible modeling is accurate enough. For isentropic ideal-gas flow, pressure and density variations scale roughly with Mach number squared at low Mach. A conventional guideline often treats flows below about Mach $0.3$ as weakly compressible, but accuracy requirements and temperature changes can move the useful boundary.

Heating can create significant density change even at low velocity. Conversely, liquids may be modeled incompressibly at large speeds until pressure transients, cavitation, or acoustic propagation become important. Mach number is a strong first diagnostic for gases, not a substitute for examining the governing property changes.

## Where incompressible intuition breaks

- Using incompressible Bernoulli equations at high Mach number without checking density changes.
- Treating shocks as isentropic. They are adiabatic but irreversible.
- Forgetting that stagnation pressure drops across shocks and frictional ducts.
- Expecting a converging nozzle to produce supersonic flow without a diverging section downstream of a choked throat.
- Using Celsius temperature in speed-of-sound or stagnation formulas.
- Using stagnation-pressure ratios across a shock as though the shock were isentropic. Static pressure rises while stagnation pressure falls.
- Assuming a lower back pressure always increases nozzle mass flow. Once the throat is choked, downstream changes alter the wave pattern before they alter the fixed upstream-controlled mass flux.
- Applying constant-$k$ air relations at temperatures where heat capacities or chemical composition vary strongly.

<div className="see-also">

See also: [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis) · [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance) · [gas power cycles](/physics/thermodynamics/gas-power-cycles) · [microscopic foundations](/physics/statistical-mechanics/intro) · [gas mixtures](/physics/thermodynamics/gas-mixtures) · [plane waves in lossless and lossy media](/physics/electromagnetics/plane-waves-lossless-lossy-polarization)

</div>
