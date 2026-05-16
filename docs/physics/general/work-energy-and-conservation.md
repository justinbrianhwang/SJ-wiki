---
title: Work, Energy, and Conservation
sidebar_position: 6
---

# Work, Energy, and Conservation

Work and energy track how interactions transfer the capacity to produce motion, deformation, heat, sound, or field changes. Instead of solving for acceleration at every instant, energy methods often compare initial and final states. This is why they are powerful for tracks, springs, gravity, circuits, and thermodynamic accounting.

Mechanical energy conservation is a statement about a chosen system. If only conservative forces act internally, $K+U$ is constant. If friction, drag, motors, or other nonconservative transfers occur, mechanical energy changes while total energy accounting remains valid.

## Definitions

- **Work** is $W=\vec F\cdot\vec d=Fd\cos\theta$ for a constant force.
- For variable force, $W=\int F_x\,dx$.
- **Kinetic energy** is $K=\frac12mv^2$.
- **Power** is $P=dW/dt=\vec F\cdot\vec v$.
- A **conservative force** has path-independent work.
- **Potential energy** satisfies $\Delta U=-W_c$.
- Near Earth, $U_g=mgy$; for a spring, $U_s=\frac12kx^2$.

The definitions in this page are meant to be operational. A symbol is useful only after you know how it would be measured, what units it carries, what sign convention is being used, and which idealizations are being assumed. Before substituting numbers, identify the system boundary and the relevant state variables. For a particle problem the state variables might be position and velocity; for a circuit they might be charge, current, and potential difference; for a thermodynamic process they might be pressure, volume, temperature, and internal energy.

A second habit is to separate model statements from algebra. A model statement says something physical, such as "air resistance is negligible", "the string is massless", "the gas is ideal", "the process is quasistatic", or "the field is uniform". Algebra then follows from those statements. If the model changes, the algebra may still look familiar but the result can become invalid. Write the model assumptions as part of the solution, not as an afterthought.

## Key results

The work-energy theorem is

$$
W_{net}=\Delta K.
$$

If only conservative forces matter,

$$
K_i+U_i=K_f+U_f.
$$

If nonconservative work is done,

$$
W_{nc}=\Delta K+\Delta U.
$$

For a one-dimensional conservative force,

$$
F_x=-\frac{dU}{dx}.
$$

Power connects energy transfer to time. A system can move at constant speed and still require power, as in an elevator rising steadily, because kinetic energy is unchanged while gravitational potential energy increases.

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
| Work | force component along displacement | joules are newton-meters |
| Kinetic energy | motion energy | scalar and nonnegative |
| Potential energy | position-dependent interaction energy | reference can be chosen |
| Power | rate of energy transfer | watts are joules per second |

## Worked example 1: Pulling work

**Problem.** A $50\,\mathrm{N}$ force pulls a crate $6.0\,\mathrm{m}$ at $25^\circ$ above horizontal. Find work by the pull.

**Method.** Use the force component along displacement.

1. $W=Fd\cos\theta$.
2. Substitute:

$$
W=(50)(6.0)\cos25^\circ.
$$

3. Compute:

$$
W=300(0.906)=272\,\mathrm{J}.
$$

4. The vertical component changes the normal force but does no work if displacement is horizontal.

**Checked answer.** The work is less than $Fd=300\,\mathrm{J}$ because the force is angled.

## Worked example 2: Spring launch

**Problem.** A $0.50\,\mathrm{kg}$ block compresses a $200\,\mathrm{N/m}$ spring by $0.10\,\mathrm{m}$ on a frictionless surface. Find launch speed.

**Method.** Spring potential energy becomes kinetic energy.

1. Conservation:

$$
\frac12kx^2=\frac12mv^2.
$$

2. Cancel $1/2$ and solve:

$$
v=x\sqrt{\frac{k}{m}}.
$$

3. Substitute:

$$
v=0.10\sqrt{\frac{200}{0.50}}=2.0\,\mathrm{m/s}.
$$

**Checked answer.** Higher stiffness or compression increases speed; larger mass decreases it.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
import math
work = 50*6.0*math.cos(math.radians(25))
v = 0.10*math.sqrt(200/0.50)
print(f"work = {work:.0f} J")
print(f"spring launch speed = {v:.2f} m/s")
```

## Common pitfalls

- Multiplying force by distance without the angle.
- Using $K+U=constant$ while friction does work.
- Treating potential energy reference as physically unique.
- Confusing work with power.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications)
- [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions)
- [First Law, Entropy, and Second Law](/physics/general/first-law-entropy-and-second-law)
