---
title: "Coulomb's Law and Electric Fields"
sidebar_position: 16
---

# Coulomb's Law and Electric Fields

Coulomb's Law and Electric Fields covers electric charge, Coulomb force, electric fields, superposition, and field lines. The goal is to recognize the physical structure before choosing equations. In the HRW progression, this topic extends earlier mechanics and prepares later field, wave, or modern-physics reasoning by reusing the same habits: define the system, choose signs and variables, state assumptions, and check dimensions.

The core idea is not a list of formulas but a model. Once the model is chosen, the equations express conservation, response, geometry, or symmetry. If the physical assumptions change, the algebra must be revisited. This is especially important here because many formulas are compact but have narrow domains of validity.

![Four electric dipole configurations are drawn with dense field-line patterns.](https://commons.wikimedia.org/wiki/Special:FilePath/VFPt_dipoles_electric.svg)

*Figure: Dipole field lines make superposition, potential gradients, and boundary intuition visible. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:VFPt_dipoles_electric.svg), Geek3, CC BY-SA 4.0.*

## Definitions

- **Scope:** electric charge, Coulomb force, electric fields, superposition, and field lines.
- **Primary symbols:** $q$, $k$, $\epsilon_0$, $\vec E$, $r$.
- **Reference equations:** $F=k\vert q_1q_2\vert /r^2$, $\vec E=\vec F/q_0$, $E=k\vert q\vert /r^2$, $\vec F=q\vec E$.
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
\text{core formulas} &: $F=k\vert q_1q_2\vert /r^2$, $\vec E=\vec F/q_0$, $E=k\vert q\vert /r^2$, $\vec F=q\vec E$.
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
| Main model | electric charge, Coulomb force, electric fields, superposition, and field lines | assumptions must match the formula |
| Symbols | $q$, $k$, $\epsilon_0$, $\vec E$, $r$ | define each before use |
| Key formulas | $F=k\vert q_1q_2\vert /r^2$, $\vec E=\vec F/q_0$, $E=k\vert q\vert /r^2$, $\vec F=q\vec E$ | check dimensions term by term |
| Limiting case | simplify one parameter | result should match intuition |

## Worked example 1: Direct calculation

**Problem.** Charges $+4.0\,\mathrm{nC}$ and $-6.0\,\mathrm{nC}$ are separated by $0.030\,\mathrm{m}$. Find force magnitude.

**Method.** Select the listed governing relationship and solve symbolically before substituting numbers.

1. Write the relevant relation.
2. Substitute the known quantities with SI units or consistent derived units.
3. Solve algebraically for the requested quantity.
4. The calculation gives

$$
$F=(8.99\times10^9)\vert (4.0\times10^{-9})(-6.0\times10^{-9})\vert /(0.030)^2=2.40\times10^{-4}\,\mathrm{N}$; opposite signs attract..
$$

5. Interpret the magnitude and sign in the original physical situation.

**Checked answer.** The result has the expected units and changes in the expected direction when the main input is increased.

## Worked example 2: Rearranged calculation

**Problem.** Two equal positive charges are at $x=\pm0.10\,\mathrm{m}$. Find the field at the origin.

**Method.** Use the same modeling routine with a different unknown so the equation is not memorized in only one direction.

1. Identify the system and the applicable approximation.
2. Start from the governing equation.
3. Rearrange before substituting values.
4. The numerical work is

$$
Each field has equal magnitude and opposite direction, so $\vec E_{net}=E\hat i-E\hat i=0$..
$$

5. Compare with a nearby limiting case or a familiar scale.

**Checked answer.** The answer is consistent with the qualitative trend predicted by the formula.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
k=8.99e9
F=k*abs(4e-9*-6e-9)/(0.030**2)
print(F, 'midpoint field = 0 by symmetry')
```

## Common pitfalls

- Adding field magnitudes when vectors cancel.
- Confusing field with force.
- Forgetting negative charges feel force opposite $\vec E$.
- Treating field lines as physical objects.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [Gauss's Law](/physics/general/gausss-law-and-electric-flux)
- [Electric Potential and Capacitance](/physics/general/electric-potential-and-capacitance)
