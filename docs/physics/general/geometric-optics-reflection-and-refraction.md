---
title: "Geometric Optics: Reflection and Refraction"
sidebar_position: 23
---

# Geometric Optics: Reflection and Refraction

Geometric Optics: Reflection and Refraction covers ray optics, reflection, refraction, total internal reflection, mirrors, and thin lenses. The goal is to recognize the physical structure before choosing equations. In the HRW progression, this topic extends earlier mechanics and prepares later field, wave, or modern-physics reasoning by reusing the same habits: define the system, choose signs and variables, state assumptions, and check dimensions.

The core idea is not a list of formulas but a model. Once the model is chosen, the equations express conservation, response, geometry, or symmetry. If the physical assumptions change, the algebra must be revisited. This is especially important here because many formulas are compact but have narrow domains of validity.

![A Snell-law diagram shows incident, reflected, and refracted rays at a boundary.](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Snells_law.svg/600px-Snells_law.svg.png)

*Figure: Reflection and refraction geometry for Snell's law. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Snells_law.svg), Cristan and Sawims, public domain.*

## Definitions

- **Scope:** ray optics, reflection, refraction, total internal reflection, mirrors, and thin lenses.
- **Primary symbols:** $n$, $\theta$, $f$, $d_o$, $d_i$, $m$.
- **Reference equations:** $\theta_r=\theta_i$, $n_1\sin\theta_1=n_2\sin\theta_2$, $1/f=1/d_o+1/d_i$, $m=-d_i/d_o$.
- A **system** is the object, field region, circuit, gas, optical element, or particle collection being modeled.
- A **state** is specified by the variables that determine the relevant energy, momentum, phase, field, or thermodynamic condition.
- A **constraint** is a physical restriction such as no slip, fixed length, constant temperature, steady flow, fixed boundary, or symmetry.
- A **limiting case** is a simplified parameter choice used to test whether the result behaves sensibly.

The definitions in this page are meant to be operational. A symbol is useful only after you know how it would be measured, what units it carries, what sign convention is being used, and which idealizations are being assumed. Before substituting numbers, identify the system boundary and the relevant state variables. For a particle problem the state variables might be position and velocity; for a circuit they might be charge, current, and potential difference; for a thermodynamic process they might be pressure, volume, temperature, and internal energy.

A second habit is to separate model statements from algebra. A model statement says something physical, such as "air resistance is negligible", "the string is massless", "the gas is ideal", "the process is quasistatic", or "the field is uniform". Algebra then follows from those statements. If the model changes, the algebra may still look familiar but the result can become invalid. Write the model assumptions as part of the solution, not as an afterthought.

## Key results

The main relationships are

$$
\begin{aligned}
\text{core formulas} &: $\theta_r=\theta_i$, $n_1\sin\theta_1=n_2\sin\theta_2$, $1/f=1/d_o+1/d_i$, $m=-d_i/d_o$.
\end{aligned}
$$

Use these relationships only after identifying which variables are known and which conditions are being assumed. Many problems can be solved by matching a physical phrase to a mathematical operation: balance forces or torques for equilibrium, integrate a rate for accumulated change, conserve a quantity when external transfer is absent, or apply a boundary condition when waves or fields must fit a geometry.

A useful solution pattern is: write the governing equation, substitute symbolic constraints, solve for the unknown, and only then insert numbers. This prevents units from becoming decorative and keeps the answer interpretable.

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
| Main model | ray optics, reflection, refraction, total internal reflection, mirrors, and thin lenses | assumptions must match the formula |
| Symbols | $n$, $\theta$, $f$, $d_o$, $d_i$, $m$ | define each before use |
| Key formulas | $\theta_r=\theta_i$, $n_1\sin\theta_1=n_2\sin\theta_2$, $1/f=1/d_o+1/d_i$, $m=-d_i/d_o$ | check dimensions term by term |
| Limiting case | simplify one parameter | result should match intuition |

## Worked example 1: Direct calculation

**Problem.** Light in air enters glass with $n=1.50$ at $40^\circ$ from the normal. Find refracted angle.

**Method.** Select the listed governing relationship and solve symbolically before substituting numbers.

1. Write the relevant relation.
2. Substitute the known quantities with SI units or consistent derived units.
3. Solve algebraically for the requested quantity.
4. The calculation gives

$$
$\sin\theta_2=(1.00/1.50)\sin40^\circ=0.4285$, so $\theta_2=25.4^\circ$..
$$

5. Interpret the magnitude and sign in the original physical situation.

**Checked answer.** The result has the expected units and changes in the expected direction when the main input is increased.

## Worked example 2: Rearranged calculation

**Problem.** An object is $30\,\mathrm{cm}$ from a converging lens with $f=10\,\mathrm{cm}$. Find image distance and magnification.

**Method.** Use the same modeling routine with a different unknown so the equation is not memorized in only one direction.

1. Identify the system and the applicable approximation.
2. Start from the governing equation.
3. Rearrange before substituting values.
4. The numerical work is

$$
$1/d_i=1/10-1/30=1/15$, so $d_i=15\,\mathrm{cm}$ and $m=-15/30=-0.50$..
$$

5. Compare with a nearby limiting case or a familiar scale.

**Checked answer.** The answer is consistent with the qualitative trend predicted by the formula.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
import math
theta=math.degrees(math.asin(math.sin(math.radians(40))/1.5))
di=1/(1/10-1/30)
print(theta,di,-di/30)
```

## Common pitfalls

- Measuring angles from the surface instead of normal.
- Using total internal reflection from low to high index.
- Applying lens signs without a ray diagram.
- Confusing real or virtual with upright or inverted.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [AC Circuits and EM Waves](/physics/general/ac-circuits-and-electromagnetic-waves)
- [Interference and Diffraction](/physics/general/interference-diffraction-and-gratings)
