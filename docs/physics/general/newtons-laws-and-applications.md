---
title: "Newton's Laws and Applications"
sidebar_position: 5
---

# Newton's Laws and Applications

Newton's laws connect motion to interaction. Kinematics says how motion changes; dynamics explains why by summing external forces on a chosen system. Applications such as inclines, Atwood machines, friction, drag, and circular motion are mainly tests of free-body diagrams and constraints.

A free-body diagram is a physics argument, not decoration. It states the system, lists only external forces, chooses axes, and prepares the component equations. Most mistakes come from drawing forces that do not act on the chosen body or from assuming the normal force, tension, or friction has a value before the equations determine it.

![William Blake's portrait of Isaac Newton shows geometry as a physical way of thinking.](https://commons.wikimedia.org/wiki/Special:FilePath/Newton-WilliamBlake.jpg)

*Figure: Blake's Newton gives the mechanics section a historical anchor for forces, geometry, and idealization. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Newton-WilliamBlake.jpg), William Blake, public domain.*

## Definitions

- **First law:** zero net external force means constant velocity in an inertial frame.
- **Second law:** $\sum\vec F=m\vec a$ for constant mass.
- **Third law:** interaction forces are equal in magnitude, opposite in direction, and act on different bodies.
- **Weight** is $m\vec g$ near Earth's surface.
- **Normal force** is perpendicular contact support.
- **Tension** is an ideal string pull along the string.
- **Static friction** satisfies $f_s\le\mu_sN$; **kinetic friction** is $f_k=\mu_kN$.
- **Quadratic drag** is often modeled as $\frac12C_D\rho Av^2$ opposite velocity.

The definitions in this page are meant to be operational. A symbol is useful only after you know how it would be measured, what units it carries, what sign convention is being used, and which idealizations are being assumed. Before substituting numbers, identify the system boundary and the relevant state variables. For a particle problem the state variables might be position and velocity; for a circuit they might be charge, current, and potential difference; for a thermodynamic process they might be pressure, volume, temperature, and internal energy.

A second habit is to separate model statements from algebra. A model statement says something physical, such as "air resistance is negligible", "the string is massless", "the gas is ideal", "the process is quasistatic", or "the field is uniform". Algebra then follows from those statements. If the model changes, the algebra may still look familiar but the result can become invalid. Write the model assumptions as part of the solution, not as an afterthought.

## Key results

Apply Newton's second law by components:

$$
\sum F_x=ma_x,\quad \sum F_y=ma_y.
$$

On a frictionless incline, weight components are $mg\sin\theta$ down the plane and $mg\cos\theta$ into the plane. The normal force is found from the perpendicular equation; it is not automatically $mg$. For friction, static friction adjusts up to $\mu_sN$ before slipping, while kinetic friction applies after sliding begins. Terminal speed with quadratic drag follows from

$$
mg=\frac12C_D\rho Av_t^2,\quad v_t=\sqrt{\frac{2mg}{C_D\rho A}}.
$$

For circular motion, the inward net force must satisfy $\sum F_r=mv^2/r$.

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
| Free-body diagram | lists external forces | no action-reaction pair on one body |
| Incline axes | parallel and perpendicular | normal from perpendicular balance |
| Static friction | adjusts to prevent slip | capped by $\mu_sN$ |
| Drag | opposes relative velocity | grows with speed in common models |

## Worked example 1: Friction threshold

**Problem.** A $20\,\mathrm{kg}$ crate on a horizontal floor has $\mu_s=0.50$ and $\mu_k=0.35$. Does an $80\,\mathrm{N}$ pull move it? If the pull is $120\,\mathrm{N}$, find sliding acceleration.

**Method.** Test static friction first.

1. $N=mg=(20)(9.8)=196\,\mathrm{N}$.
2. $f_{s,max}=\mu_sN=(0.50)(196)=98\,\mathrm{N}$.
3. Since $80\lt 98$, the crate does not move; static friction is $80\,\mathrm{N}$.
4. If $F=120\,\mathrm{N}$, kinetic friction is $f_k=(0.35)(196)=68.6\,\mathrm{N}$.
5. Acceleration is

$$
a=\frac{120-68.6}{20}=2.57\,\mathrm{m/s^2}.
$$

**Checked answer.** Static friction is not automatically maximum; it becomes maximum only at impending slip.

## Worked example 2: Atwood machine

**Problem.** Masses $m_1=2.0\,\mathrm{kg}$ and $m_2=3.0\,\mathrm{kg}$ hang over an ideal pulley. Find acceleration and tension.

**Method.** Let $m_2$ accelerate downward and $m_1$ upward.

1. Equations:

$$
T-m_1g=m_1a,\quad m_2g-T=m_2a.
$$

2. Add to eliminate $T$:

$$
(m_2-m_1)g=(m_1+m_2)a.
$$

3. Acceleration:

$$
a=\frac{(3.0-2.0)9.8}{5.0}=1.96\,\mathrm{m/s^2}.
$$

4. Tension:

$$
T=m_1(g+a)=2.0(11.76)=23.5\,\mathrm{N}.
$$

**Checked answer.** Tension lies between the two weights, as expected.

## Code

The snippet below is a small numerical check for the page. It uses only Python's standard library and keeps the physical constants visible so the assumptions can be changed.

```python
m, g = 20.0, 9.8
N = m*g
fsmax = 0.50*N
a = (120 - 0.35*N)/m
m1, m2 = 2.0, 3.0
aA = (m2-m1)*g/(m1+m2)
T = m1*(g+aA)
print(f"fs max = {fsmax:.1f} N, sliding a = {a:.2f} m/s^2")
print(f"Atwood a = {aA:.2f} m/s^2, T = {T:.1f} N")
```

## Common pitfalls

- Putting action-reaction pairs on the same free-body diagram.
- Assuming normal force always equals weight.
- Using kinetic friction before proving sliding.
- Forgetting constraints such as equal string acceleration.
- Always check units, signs, and limiting cases before treating a numerical result as finished.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [Two-Dimensional Motion](/physics/general/two-dimensional-motion)
- [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation)
- [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions)
