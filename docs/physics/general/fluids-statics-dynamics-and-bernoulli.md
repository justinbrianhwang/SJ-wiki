---
title: "Fluids: Statics, Dynamics, and Bernoulli"
sidebar_position: 11
---

# Fluids: Statics, Dynamics, and Bernoulli

Fluid statics follows from force balance; ideal fluid dynamics follows from conservation of mass and mechanical energy. The equations look compact, but pressure reference, displaced volume, and flow assumptions determine whether they apply.

## Pressure below a free surface

Pressure is normal force per area:

$$
P=\frac{F_\perp}{A}.
$$

Pressure is a scalar field even though the force it produces on a surface is normal. At a point in a stationary fluid, pressure is the same in every direction; otherwise a small element would have an unbalanced shear or torque.

In a stationary fluid of constant density,

$$
P=P_0+\rho gh,
$$

where $P_0$ is the pressure at the surface and $h$ is depth below it. The gauge pressure is $P_g=P-P_0=\rho gh$; absolute pressure includes $P_0$.

Balancing a thin horizontal slab gives

$$
\frac{dP}{dy}=-\rho g,
$$

with $y$ upward. If density varies, retain it in the integral:

$$
P(y_2)-P(y_1)=-\int_{y_1}^{y_2}\rho(y)g\,dy.
$$

The pressure at equal elevations in a connected stationary fluid is equal. A hydraulic lift therefore satisfies $F_1/A_1=F_2/A_2$. The force gain is paid for by distance: incompressibility gives $A_1d_1=A_2d_2$, hence $F_1d_1=F_2d_2$ ideally.

A hatch of area $0.80\,\mathrm{m^2}$ lies $5.0\,\mathrm m$ below the surface of fresh water. Its gauge pressure is

$$
P_g=(1000)(9.8)(5.0)=4.90\times10^4\,\mathrm{Pa}.
$$

If the other side is at atmospheric pressure and the hatch is small enough that its depth is effectively uniform, the net force is

$$
F=P_gA=(4.90\times10^4)(0.80)
=3.92\times10^4\,\mathrm N.
$$

Using absolute pressure for only one side would incorrectly include the atmospheric force that is already balanced on the other side.

For a large vertical gate, pressure is not uniform. On a rectangle of width $b$ extending from the surface to depth $H$,

$$
F=\int_0^H\rho gy\,b\,dy
=\frac12\rho gbH^2.
$$

The resultant acts at depth $2H/3$, below the geometric center, because the pressure distribution is triangular.

## Buoyancy is the resultant pressure force

Pressure increases with depth, so the upward pressure force on a submerged object's lower surface exceeds the downward force on its upper surface. The net buoyant force is

$$
F_B=\rho_f gV_{\mathrm{disp}},
$$

equal to the weight of displaced fluid. The density is the fluid's density, and the volume is the displaced volume. For a floating object, equilibrium gives $F_B=mg$, so the submerged fraction is $\rho_{\mathrm{object}}/\rho_f$ when densities are uniform.

Archimedes' principle follows by replacing the object mentally with the fluid that occupied the same volume. That fluid parcel was in equilibrium, so surrounding pressure forces had a resultant equal and opposite to its weight. The same surface pressures act on the object.

### Worked example: a submerged block and tether

A block has density $800\,\mathrm{kg/m^3}$ and volume $2.0\times10^{-3}\,\mathrm{m^3}$. It is submerged in water and held by a string attached to the bottom. Its weight is

$$
W=(800)(2.0\times10^{-3})(9.8)=15.68\,\mathrm N,
$$

while buoyancy is

$$
F_B=(1000)(2.0\times10^{-3})(9.8)=19.60\,\mathrm N.
$$

The tether must pull downward:

$$
T=F_B-W=3.92\,\mathrm N.
$$

If cut, the initial acceleration is

$$
a=\frac{F_B-W}{m}
=\frac{3.92}{(800)(2.0\times10^{-3})}
=2.45\,\mathrm{m/s^2},
$$

before drag and partial emergence change the forces.

Floating equilibrium also needs rotational stability. A small tilt shifts the center of buoyancy. If the shifted buoyant force produces a restoring torque about the center of mass, the orientation is stable; equal vertical forces alone do not settle that question.

## Following a parcel through a flow tube

For steady incompressible flow, conservation of mass gives

$$
A_1v_1=A_2v_2=Q,
$$

where $Q$ is volume flow rate. A narrower cross section therefore has a greater speed.

The general steady mass-flow relation is

$$
\dot m=\rho Av.
$$

Only constant density reduces it to $Av=\text{constant}$. Gas flow through a large pressure change may be compressible.

```mermaid
graph LR
  A[Choose two cross sections] --> B[Apply continuity]
  B --> C[Relate the speeds]
  C --> D[Apply Bernoulli along a streamline]
  D --> E[Compare pressure and height]
```

| Effect | Relation | Condition |
|---|---|---|
| Hydrostatic pressure | $P=P_0+\rho gh$ | fluid at rest, constant density |
| Buoyant force | $F_B=\rho_f gV_{\mathrm{disp}}$ | displaced-fluid weight |
| Continuity | $A_1v_1=A_2v_2$ | steady incompressible flow |
| Bernoulli balance | $P+\tfrac12\rho v^2+\rho gy=\text{constant}$ | steady, incompressible, nonviscous flow along a streamline |

Water moves at $1.5\,\mathrm{m/s}$ where a horizontal pipe has radius $4.0\,\mathrm{cm}$. Where the radius narrows to $2.0\,\mathrm{cm}$,

$$
v_2=v_1\frac{A_1}{A_2}
=v_1\left(\frac{r_1}{r_2}\right)^2
=1.5\left(\frac{4.0}{2.0}\right)^2
=6.0\,\mathrm{m/s}.
$$

The square appears because area scales as radius squared.

The volume flow rate is

$$
Q=\pi(0.040)^2(1.5)
=7.54\times10^{-3}\,\mathrm{m^3/s}.
$$

The narrow section gives the same value, providing an arithmetic check.

## Bernoulli as mechanical energy density

Along a streamline in steady, incompressible, nonviscous flow with no pump or turbine work,

$$
P+\frac12\rho v^2+\rho gy=\text{constant}.
$$

Each term has units of energy per volume. A pressure decrease can accompany increased speed, increased height, or both, but the equation does not say that high speed universally causes low pressure.

Follow a fluid volume $\Delta V$ from section 1 to section 2. Pressure forces do work

$$
W_P=P_1\Delta V-P_2\Delta V.
$$

The kinetic and gravitational energy changes are

$$
\Delta K=\frac12\rho\Delta V(v_2^2-v_1^2),
\qquad
\Delta U_g=\rho\Delta Vg(y_2-y_1).
$$

Set pressure work equal to the mechanical-energy change, divide by $\Delta V$, and rearrange to recover Bernoulli's equation.

For the horizontal pipe above, $y_1=y_2$, so Bernoulli predicts

$$
P_1-P_2=\frac12\rho\left(v_2^2-v_1^2\right)>0.
$$

The narrower, faster section has lower static pressure under the ideal-flow assumptions.

For the water speeds above,

$$
P_1-P_2
=\frac12(1000)(6.0^2-1.5^2)
=1.69\times10^4\,\mathrm{Pa}.
$$

This is the basis of a Venturi meter: measure pressure between known areas, then combine Bernoulli with continuity to infer flow rate.

### Worked example: efflux from a tank

A large open tank has a small hole $1.25\,\mathrm m$ below its free surface. Apply Bernoulli between the free surface and the jet. Both points are at atmospheric pressure, and the surface speed is negligible. Hence

$$
v=\sqrt{2gh}
=\sqrt{2(9.8)(1.25)}
=4.95\,\mathrm{m/s}.
$$

If the hole area is $1.0\,\mathrm{cm^2}=1.0\times10^{-4}\,\mathrm{m^2}$, the ideal rate is

$$
Q=Av=(1.0\times10^{-4})(4.95)
=4.95\times10^{-4}\,\mathrm{m^3/s}.
$$

This is Torricelli's law. A real sharp-edged opening gives a smaller flow, summarized by a discharge coefficient.

## Viscosity and flow regime

For a Newtonian fluid, shear stress is

$$
\tau=\eta\frac{dv}{dy},
$$

where $\eta$ is dynamic viscosity. No-slip at a wall produces a velocity gradient and dissipates mechanical energy.

Steady laminar flow through a long circular pipe obeys Poiseuille's law:

$$
Q=\frac{\pi R^4}{8\eta L}\Delta P.
$$

Doubling radius at fixed pressure drop increases this ideal laminar flow rate by sixteen. The strong radius dependence is one reason vessel constriction matters in biological flow.

The Reynolds number

$$
\mathrm{Re}=\frac{\rho vD}{\eta}
$$

compares inertial and viscous effects. Low values favor laminar flow; high values permit turbulence. Transition depends on geometry and disturbances, so one threshold does not cover every flow.

An extended energy equation uses head:

$$
\frac{P_1}{\rho g}+\frac{v_1^2}{2g}+y_1+h_p
=\frac{P_2}{\rho g}+\frac{v_2^2}{2g}+y_2+h_t+h_L.
$$

A pump adds head $h_p$, a turbine removes $h_t$, and friction and fittings contribute $h_L\geq0$.

## Where losses enter

Real pipes have viscosity, wall friction, turbulence, valves, and fittings. Pumps add mechanical energy; turbines remove it. Bernoulli's ideal equation across such elements needs head-gain and head-loss terms. Applying the unmodified form through a pump or across a long rough pipe attributes real energy transfer to a fictitious pressure-speed trade.

Other recurring mistakes are more local:

- Gauge and absolute pressures may be compared only when they use the same reference.
- Buoyancy uses displaced-fluid weight, not object weight or object density directly.
- Continuity uses area ratios, so circular-pipe radius ratios are squared.
- Bernoulli points must lie on the same streamline unless the flow is irrotational.
- Static pressure, stagnation pressure, and dynamic pressure $\rho v^2/2$ are different; a probe's orientation determines what it measures.
- The pressure at a free liquid surface need not be atmospheric in a sealed container.

## Manometers and pressure measurement

A manometer turns a pressure difference into a height difference. Moving downward through a stationary fluid increases pressure by $\rho g\Delta h$; moving upward decreases it. One can trace from one connection to the other, adding changes fluid by fluid.

For a simple U-tube filled with liquid density $\rho_m$, one side open to atmosphere and the other connected to a gas, a level difference $h$ gives

$$
P_{\mathrm{gas}}-P_{\mathrm{atm}}=\rho_mgh
$$

when the gas side pushes its liquid level lower. If it stands higher, the gauge pressure is negative. In a multi-fluid manometer, no single-density shortcut works; pressure remains continuous across each fluid interface, while the slope with height changes with density.

A barometer is a closed-end manometer with near-vacuum above the column. Atmospheric pressure supports the liquid column: $P_{\mathrm{atm}}=\rho gh$. Mercury permits a short column because its density is high. Water would require a column over ten metres tall at ordinary atmospheric pressure.

## Surface tension and capillarity

Molecules at a liquid surface experience an asymmetric cohesive environment, giving the interface an energy per area and a force per length called surface tension $\gamma$. A movable wire of length $L$ on a soap film feels force $2\gamma L$ because the film has two surfaces.

Curvature creates a pressure jump. For a spherical liquid droplet of radius $R$,

$$
P_{\mathrm{in}}-P_{\mathrm{out}}=\frac{2\gamma}{R}.
$$

A soap bubble has two interfaces and gives $4\gamma/R$. Small droplets therefore have larger excess pressure than large ones.

Capillary rise follows from the vertical component of surface tension around a tube. For tube radius $r$, contact angle $\theta$, and liquid density $\rho$,

$$
2\pi r\gamma\cos\theta
=\rho g(\pi r^2h),
$$

so

$$
h=\frac{2\gamma\cos\theta}{\rho gr}.
$$

Wetting liquids with $\theta\lt 90^\circ$ rise; nonwetting liquids are depressed. The inverse dependence on radius explains why capillarity is strongest in narrow pores.

## Drag, terminal speed, and similarity

A body moving through fluid experiences drag whose form depends on Reynolds number and shape. At very low Reynolds number, a sphere of radius $R$ obeys Stokes' law

$$
F_D=6\pi\eta Rv.
$$

Balancing this against weight minus buoyancy gives a small sphere's terminal speed:

$$
v_t=\frac{2R^2(\rho_s-\rho_f)g}{9\eta}.
$$

At high Reynolds number, drag is often modeled as

$$
F_D=\frac12C_D\rho Av^2,
$$

where $C_D$ depends on shape and flow regime. Switching between linear and quadratic drag without checking Reynolds number can change predicted terminal speed substantially.

Dimensionless numbers help compare experiments at different scales. Matching Reynolds number preserves the balance of inertia and viscosity in geometrically similar flows. Froude number compares inertia with gravity in free-surface flows, while Mach number compares speed with sound speed in compressible flow. A small model and a full-size vehicle cannot always match every dimensionless group simultaneously.

## Cavitation and pressure limits

Bernoulli calculations can predict very low static pressure in fast regions. Liquid pressure cannot be reduced arbitrarily without changing phase. If local pressure falls below vapor pressure, vapor cavities form. Their later collapse can create noise, vibration, and surface damage in pumps, propellers, and valves.

Gauge pressure may be negative, but absolute pressure cannot be negative in the ordinary continuum model. When a result crosses vapor pressure, the single-phase incompressible assumptions have failed before the algebra does.

Likewise, a siphon does not work because atmospheric pressure “pulls” liquid over the top in every description. Pressure differences and gravity accelerate a continuous column, and the outlet must lie below the source surface for sustained ideal flow. Excessive summit height lowers pressure enough for cavitation or column separation, limiting operation.

## Choosing the right fluid model

Start with scale and regime. Hydrostatics applies when acceleration is absent. Continuity expresses mass conservation broadly, but $A_1v_1=A_2v_2$ additionally assumes constant density. Bernoulli preserves mechanical energy only under its stated conditions. Poiseuille covers fully developed laminar pipe flow. No one equation is a universal “fluid formula.”

Boundary conditions often carry as much information as the differential equations: no-slip at solid walls for viscous flow, specified pressure at a free jet, symmetry at a centerline, and known flow rate at an inlet. An answer with correct algebra but incompatible boundary conditions describes a different physical system.

## Momentum balance at bends and jets

Bernoulli tracks mechanical energy but does not directly give the force a flowing fluid exerts on a pipe. A control-volume momentum balance does. For steady one-dimensional flow,

$$
\sum\vec F_{\mathrm{external}}
=\dot m(\vec v_{\mathrm{out}}-\vec v_{\mathrm{in}}).
$$

Pressure forces, weight, and wall reactions all belong on the left. The force on the pipe is opposite the wall force on the fluid.

A water jet of mass flow $2.0\,\mathrm{kg/s}$ striking a flat plate normally at $10\,\mathrm{m/s}$ and leaving with zero normal velocity changes normal momentum at $20\,\mathrm N$. The plate must exert $20\,\mathrm N$ on the water, and the water exerts $20\,\mathrm N$ on the plate. If the jet rebounds, the momentum change and force are larger.

Pipe bends can therefore experience substantial reaction forces even when inlet and outlet pressures are equal. Energy conservation alone misses vector momentum change, while momentum balance alone does not determine viscous energy loss. The two laws answer complementary questions.

<div className="see-also">

See also: [Equilibrium and Elasticity](/physics/general/equilibrium-and-elasticity) · [Waves and Sound](/physics/general/waves-sound-standing-waves-and-doppler)

</div>
