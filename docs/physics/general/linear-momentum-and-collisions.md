---
title: Linear Momentum and Collisions
sidebar_position: 7
---

# Linear Momentum and Collisions

Momentum tracks motion through interactions, especially brief interactions where internal forces are large and external impulses are small. Collisions, explosions, recoil, and center-of-mass motion are momentum problems because the total momentum of an isolated system is conserved even when kinetic energy changes.

Energy may transform into sound, heat, or deformation during a crash, but momentum conservation survives if the system boundary is chosen well. This makes momentum the natural language for impact processes.

## Definitions

- **Momentum** is $\vec p=m\vec v$.
- **Impulse** is $\vec J=\int\vec F\,dt=\Delta\vec p$.
- **Center of mass** satisfies $M\vec r_{cm}=\sum m_i\vec r_i$.
- **Elastic collision** conserves kinetic energy and momentum.
- **Inelastic collision** conserves momentum but not kinetic energy.
- **Completely inelastic collision** means objects stick together.
- A system is isolated for momentum when external impulse is negligible.

The definitions in this page are meant to be operational. A symbol is useful only after you know how it would be measured, what units it carries, what sign convention is being used, and which idealizations are being assumed. Before substituting numbers, identify the system boundary and the relevant state variables. For a particle problem the state variables might be position and velocity; for a circuit they might be charge, current, and potential difference; for a thermodynamic process they might be pressure, volume, temperature, and internal energy.

A second habit is to separate model statements from algebra. A model statement says something physical, such as "air resistance is negligible", "the string is massless", "the gas is ideal", "the process is quasistatic", or "the field is uniform". Algebra then follows from those statements. If the model changes, the algebra may still look familiar but the result can become invalid. Write the model assumptions as part of the solution, not as an afterthought.

## Key results

Total momentum is

$$
\vec P=\sum_i m_i\vec v_i=M\vec v_{cm}.
$$

For a system,

$$
\sum\vec F_{ext}=\frac{d\vec P}{dt}.
$$

If external impulse is negligible,

$$
\vec P_i=\vec P_f.
$$

For a completely inelastic one-dimensional collision,

$$
m_1v_{1i}+m_2v_{2i}=(m_1+m_2)v_f.
$$

For elastic one-dimensional collisions, combine momentum conservation with reversal of relative speed: $v_{1i}-v_{2i}=-(v_{1f}-v_{2f})$.

These formulas are conditional statements. Each equation is powerful inside its domain and misleading outside it. Constant-acceleration kinematics requires constant acceleration. Conservation of mechanical energy requires either no nonconservative work or an explicit accounting of it. Gauss's law is always true, but it directly gives an electric field only when symmetry lets the flux integral simplify. Bernoulli's equation assumes steady, incompressible, nonviscous flow along a streamline. Keeping the conditions attached to the formula is part of the formula.

For numerical work, solve symbolically before inserting values whenever possible. A symbolic expression exposes dimensions and limiting behavior. If a mass should cancel, it should cancel before arithmetic. If an answer should decrease when distance grows, the final expression should show that trend. If an answer becomes infinite in an unphysical limit, that usually marks the boundary where the model has stopped applying.

## Visual

```mermaid
graph LR
  A[Physical situation] --> B[Choose model]
  B --> C[Define variables]
  C --> D[Apply key law]
  D --> E[Solve symbolically]
  E --> F[Check units and limits]
```

| Quantity or idea | Use | Check |
|---|---|---|
| Momentum | $m\vec v$ | vector by components |
| Impulse | force-time area | units equal momentum |
| Center of mass | system average position | moves under external force |
| Elasticity | kinetic energy condition | separate from momentum conservation |

## Worked example 1: Sticking carts

**Problem.** A $0.20\,\mathrm{kg}$ cart moving at $3.0\,\mathrm{m/s}$ sticks to a $0.30\,\mathrm{kg}$ cart at rest. Find final speed and kinetic energy lost.

**Method.** Momentum conserved; kinetic energy not conserved.

1. Initial momentum:

$$
p_i=(0.20)(3.0)=0.60\,\mathrm{kg\,m/s}.
$$

2. Final momentum:

$$
p_f=(0.50)v_f.
$$

3. $v_f=0.60/0.50=1.2\,\mathrm{m/s}$.
4. $K_i=\frac12(0.20)(3.0)^2=0.90\,\mathrm{J}$.
5. $K_f=\frac12(0.50)(1.2)^2=0.36\,\mathrm{J}$.

**Checked answer.** Mechanical kinetic energy lost is $0.54\,\mathrm{J}$.

## Worked example 2: Impulse pulse

**Problem.** A triangular force pulse has base $0.030\,\mathrm{s}$ and height $120\,\mathrm{N}$. Find impulse and speed change of a $0.15\,\mathrm{kg}$ ball.

**Method.** Impulse is area under $F(t)$.

1. Triangle area:

$$
J=\frac12(0.030)(120)=1.80\,\mathrm{N\,s}.
$$

2. Impulse-momentum theorem:

$$
J=m\Delta v.
$$

3. Speed change:

$$
\Delta v=1.80/0.15=12.0\,\mathrm{m/s}.
$$

**Checked answer.** $\mathrm{N\,s}$ equals $\mathrm{kg\,m/s}$, so dividing by mass gives speed.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
m1,v1,m2,v2 = 0.20,3.0,0.30,0.0
vf=(m1*v1+m2*v2)/(m1+m2)
Ki=0.5*m1*v1**2
Kf=0.5*(m1+m2)*vf**2
J=0.5*0.030*120
print(f"vf = {vf:.2f} m/s, energy lost = {Ki-Kf:.2f} J")
print(f"impulse = {J:.2f} N s, delta v = {J/0.15:.1f} m/s")
```

## Common pitfalls

- Conserving kinetic energy in every collision.
- Forgetting momentum is vectorial.
- Ignoring external impulse.
- Confusing impulse with average force.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation)
- [Rotation and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum)
- [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications)
