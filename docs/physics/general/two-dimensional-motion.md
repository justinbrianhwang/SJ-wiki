---
title: "Two-Dimensional Motion: Projectiles and Circular Motion"
sidebar_position: 4
---

# Two-Dimensional Motion: Projectiles and Circular Motion

Two-dimensional motion is where vector components become necessary. A projectile can accelerate downward while moving horizontally, and uniform circular motion can have constant speed while velocity changes every instant. Perpendicular components can often be analyzed independently when acceleration components are known.

Projectile motion and circular motion teach complementary lessons. Projectile motion separates into horizontal constant-velocity motion and vertical constant-acceleration motion when air resistance is neglected. Circular motion keeps radius fixed and bends velocity with inward acceleration.

## Definitions

- **Projectile motion** is motion under gravity alone after launch.
- The ideal projectile acceleration is $\vec a=(0,-g)$ for horizontal $x$ and upward $y$.
- **Range** is horizontal displacement to a specified landing height.
- **Uniform circular motion** has constant speed on a circle but nonzero acceleration.
- **Centripetal acceleration** points inward with magnitude $a_c=v^2/r=\omega^2r$.
- **Angular speed** is $\omega=d\theta/dt$, and $v=r\omega$ for rigid circular motion.

The definitions in this page are meant to be operational. A symbol is useful only after you know how it would be measured, what units it carries, what sign convention is being used, and which idealizations are being assumed. Before substituting numbers, identify the system boundary and the relevant state variables. For a particle problem the state variables might be position and velocity; for a circuit they might be charge, current, and potential difference; for a thermodynamic process they might be pressure, volume, temperature, and internal energy.

A second habit is to separate model statements from algebra. A model statement says something physical, such as "air resistance is negligible", "the string is massless", "the gas is ideal", "the process is quasistatic", or "the field is uniform". Algebra then follows from those statements. If the model changes, the algebra may still look familiar but the result can become invalid. Write the model assumptions as part of the solution, not as an afterthought.

## Key results

For a projectile launched with speed $v_0$ at angle $\theta$,

$$
\begin{aligned}
x(t)&=v_0\cos\theta\,t,\\
y(t)&=v_0\sin\theta\,t-\frac12gt^2,\\
v_x(t)&=v_0\cos\theta,\\
v_y(t)&=v_0\sin\theta-gt.
\end{aligned}
$$

If launch and landing heights are equal,

$$
T=\frac{2v_0\sin\theta}{g},\quad R=\frac{v_0^2\sin2\theta}{g}.
$$

For circular motion,

$$
a_c=\frac{v^2}{r}=\omega^2r,\quad T=\frac{2\pi r}{v}.
$$

The inward acceleration in uniform circular motion changes direction of velocity, not its magnitude.

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
| Projectile $x$ | $a_x=0$ | horizontal velocity stays constant |
| Projectile $y$ | $a_y=-g$ | vertical velocity changes linearly |
| Circular speed | $v=r\omega$ | radians are dimensionless |
| Centripetal acceleration | $v^2/r$ | points inward |

## Worked example 1: Projectile range

**Problem.** A ball is launched at $20\,\mathrm{m/s}$ and $35^\circ$ above horizontal from ground level. Find flight time and range.

**Method.** Resolve initial velocity and use vertical motion for time.

1. Components:

$$
v_{0x}=20\cos35^\circ=16.38\,\mathrm{m/s},
\quad v_{0y}=20\sin35^\circ=11.47\,\mathrm{m/s}.
$$

2. Landing condition $y=0$:

$$
0=t(v_{0y}-\frac12gt).
$$

3. Nonzero time:

$$
t=\frac{2v_{0y}}{g}=\frac{2(11.47)}{9.8}=2.34\,\mathrm{s}.
$$

4. Range:

$$
R=v_{0x}t=(16.38)(2.34)=38.3\,\mathrm{m}.
$$

**Checked answer.** Range is less than $v_0t$ because not all launch speed is horizontal.

## Worked example 2: Turntable acceleration

**Problem.** A point $0.15\,\mathrm{m}$ from the center of a turntable rotates at $45\,\mathrm{rpm}$. Find speed and centripetal acceleration.

**Method.** Convert rpm to rad/s, then use $v=r\omega$ and $a_c=\omega^2r$.

1. Angular speed:

$$
\omega=45\frac{\mathrm{rev}}{\mathrm{min}}\frac{2\pi\,\mathrm{rad}}{\mathrm{rev}}\frac{1\,\mathrm{min}}{60\,\mathrm{s}}=4.71\,\mathrm{rad/s}.
$$

2. Speed:

$$
v=(0.15)(4.71)=0.707\,\mathrm{m/s}.
$$

3. Acceleration:

$$
a_c=(4.71)^2(0.15)=3.33\,\mathrm{m/s^2}.
$$

**Checked answer.** Acceleration is inward and about one third of $g$.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
import math
v0, theta, g = 20.0, math.radians(35), 9.8
vx, vy = v0*math.cos(theta), v0*math.sin(theta)
t = 2*vy/g
omega = 45*2*math.pi/60
r = 0.15
print(f"time = {t:.2f} s, range = {vx*t:.1f} m")
print(f"speed = {r*omega:.3f} m/s, ac = {omega**2*r:.2f} m/s^2")
```

## Common pitfalls

- Using equal-height range formulas when final height differs.
- Forgetting both components share the same time.
- Calling centripetal acceleration a force.
- Assuming constant speed means zero acceleration.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics)
- [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications)
- [Rotation and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum)
