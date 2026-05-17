---
title: Measurement, Units, and Vectors
sidebar_position: 2
---

# Measurement, Units, and Vectors

Measurement gives physics its contact with the world, and vectors give it a precise language for direction. A physical claim must be comparable with a standard: length in meters, time in seconds, mass in kilograms, force in newtons, and energy in joules. A number without a unit is usually not a physical quantity; it is arithmetic detached from meaning.

Vectors enter as soon as direction matters. Displacement, velocity, acceleration, force, momentum, electric field, and magnetic field cannot be described by magnitude alone. Components let us convert geometric statements into algebra, while dimensional analysis checks whether the algebra still describes a possible physical relationship.

![Two vectors are added tip-to-tail and by the parallelogram construction.](https://commons.wikimedia.org/wiki/Special:FilePath/Vector_addition.svg)

*Figure: Vector addition is the visual grammar behind force resultants, displacements, and field components. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Vector_addition.svg), Benjamin D. Esham, public domain.*

## Definitions

- A **physical quantity** is a number times a unit.
- The common SI base dimensions are length $L$, mass $M$, time $T$, current $I$, and temperature $\Theta$.
- A **derived unit** is built from base units, such as $1\,\mathrm{N}=1\,\mathrm{kg\,m/s^2}$.
- A **vector** has magnitude and direction: $\vec A=A_x\hat i+A_y\hat j+A_z\hat k$.
- A **scalar** has no direction; examples include mass, time, energy, temperature, and electric potential.
- The **dot product** $\vec A\cdot\vec B=AB\cos\theta$ measures parallel overlap.
- The **cross product** $\vec A\times\vec B$ measures perpendicular leverage or oriented area.

The definitions in this page are meant to be operational. A symbol is useful only after you know how it would be measured, what units it carries, what sign convention is being used, and which idealizations are being assumed. Before substituting numbers, identify the system boundary and the relevant state variables. For a particle problem the state variables might be position and velocity; for a circuit they might be charge, current, and potential difference; for a thermodynamic process they might be pressure, volume, temperature, and internal energy.

A second habit is to separate model statements from algebra. A model statement says something physical, such as "air resistance is negligible", "the string is massless", "the gas is ideal", "the process is quasistatic", or "the field is uniform". Algebra then follows from those statements. If the model changes, the algebra may still look familiar but the result can become invalid. Write the model assumptions as part of the solution, not as an afterthought.

## Key results

Dimensional homogeneity requires every term in a sum or equation to have the same dimensions. The constant-acceleration equation

$$
x=x_0+v_0t+\frac12at^2
$$

is valid dimensionally because each term has dimension $L$. Component rules are

$$
A_x=A\cos\theta,\quad A_y=A\sin\theta,\quad A=\sqrt{A_x^2+A_y^2}.
$$

For vector addition,

$$
\vec R=\vec A+\vec B,\quad R_x=A_x+B_x,\quad R_y=A_y+B_y.
$$

Dot products appear in work and flux. Cross products appear in torque, angular momentum, and magnetic force. Angles inside trigonometric functions must be dimensionless, and arguments of exponentials or logarithms must also be dimensionless.

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
| SI unit | keeps measurements comparable | final dimensions must match |
| Components | convert geometry to algebra | signs follow chosen axes |
| Dot product | work, flux, projections | result is scalar |
| Cross product | torque and magnetic force | zero for parallel vectors |

## Worked example 1: Checking a drag formula

**Problem.** A proposed drag law is $F=C\rho Av$, where $\rho$ is density, $A$ is area, and $v$ is speed. Check it and repair the simplest missing factor.

**Method.** Compare dimensions with force.

1. Force has dimensions $[F]=MLT^{-2}$.
2. The proposed right side has

$$
[\rho Av]=(ML^{-3})(L^2)(LT^{-1})=MT^{-1}.
$$

3. It is missing dimensions $LT^{-1}$.
4. The natural available factor is another speed, so

$$
F=C\rho Av^2.
$$

5. A detailed model often writes $F=\frac12C_D\rho Av^2$, where $\frac12$ and $C_D$ are dimensionless.

**Checked answer.** $(ML^{-3})(L^2)(L^2T^{-2})=MLT^{-2}$, so the repaired expression has force units.

## Worked example 2: Adding displacements

**Problem.** A hiker walks $4.0\,\mathrm{km}$ east and then $3.0\,\mathrm{km}$ at $40^\circ$ north of east. Find the resultant displacement.

**Method.** Add components.

1. First displacement: $A_x=4.0$, $A_y=0$.
2. Second displacement:

$$
B_x=3.0\cos40^\circ=2.30,\quad B_y=3.0\sin40^\circ=1.93.
$$

3. Resultant components:

$$
R_x=6.30\,\mathrm{km},\quad R_y=1.93\,\mathrm{km}.
$$

4. Magnitude:

$$
R=\sqrt{6.30^2+1.93^2}=6.59\,\mathrm{km}.
$$

5. Direction:

$$
\theta=\tan^{-1}(1.93/6.30)=17.0^\circ.
$$

**Checked answer.** The result points mostly east with a modest northward angle, matching the path.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
import math

rho, area, speed = 1.2, 0.030, 15.0
drag = 0.5 * 1.0 * rho * area * speed**2
Bx = 3.0 * math.cos(math.radians(40))
By = 3.0 * math.sin(math.radians(40))
Rx, Ry = 4.0 + Bx, By
print(f"drag estimate = {drag:.2f} N")
print(f"resultant = {math.hypot(Rx, Ry):.2f} km at {math.degrees(math.atan2(Ry, Rx)):.1f} deg")
```

## Common pitfalls

- Dropping units during substitution.
- Adding quantities with different dimensions.
- Using the wrong axis for sine and cosine.
- Reporting an arctangent angle without checking the quadrant.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics)
- [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation)
- [Magnetic Fields and Forces](/physics/general/magnetic-fields-and-forces)
