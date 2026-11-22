---
title: "General Physics: HRW Introductory Roadmap"
sidebar_position: 1
---

# General Physics: HRW Introductory Roadmap

General physics is the discipline of turning ordinary events into quantitative models: falling, sliding, rotating, heating, flowing, oscillating, charging, refracting, and scattering. The Halliday, Resnick, and Walker sequence works because each new unit reuses earlier habits. Measurement and vectors make physical language precise. Mechanics develops force, energy, and momentum. Rotation and fluids show how extended systems need new variables. Oscillations and waves introduce phase and resonance. Thermal physics adds macroscopic and microscopic energy bookkeeping. Electricity and magnetism replace contact forces with fields. Optics tests ray and wave models. Relativity and quantum physics mark the limits of the classical picture.

The notes in this folder are structured as study pages rather than textbook replacements. Each page gives definitions, key results, a visual anchor, two worked numerical examples, a short code check, common mistakes, and links to neighboring ideas. The intended use is active: read the statement of a worked example, cover the solution, attempt the method yourself, and then compare the algebra, units, and limiting-case checks.

## Definitions

A **physical model** is a simplified representation of a real situation. A point particle model ignores size and rotation; a rigid body model ignores deformation; an ideal fluid has no viscosity and is incompressible; an ideal gas follows a simple equation of state; an electrostatic model assumes charges are at rest. A **state variable** is a measurable quantity that helps specify a system, such as position, velocity, temperature, pressure, charge, current, or angular velocity. A **law** connects state variables and interactions. A **conservation principle** states that some quantity changes only by transfer across the system boundary.

Notation matters throughout the course. Vectors carry magnitude and direction, so equations such as $\vec F=m\vec a$ must be interpreted component by component. Scalars such as work, energy, temperature, pressure, entropy, and electric potential do not have direction, though they may be positive or negative relative to a reference. Units are part of definitions. A result with wrong dimensions cannot be correct, and a result with right dimensions is only a candidate until signs, assumptions, and limiting cases also make sense.

## Key results

The course can be organized into four families of results. First are evolution equations, such as kinematics, Newton's second law, rotational dynamics, circuit transients, thermodynamic process equations, and wave equations. Second are conservation laws: energy, linear momentum, angular momentum, charge, and entropy constraints for isolated systems. Third are field laws: Newton's gravitation, Coulomb's law, Gauss's law, Ampere's law, Faraday's law, and the qualitative content of Maxwell's equations. Fourth are model-transition ideas: ray versus wave optics, classical versus relativistic motion, and particle versus wave descriptions of matter.

$$
\begin{aligned}
\text{measurement} &\to \text{vectors} \\
&\to \text{motion, force, energy, momentum} \\
&\to \text{rotation, equilibrium, gravity, fluids} \\
&\to \text{oscillations, waves, thermal physics} \\
&\to \text{electricity, magnetism, optics} \\
&\to \text{relativity and quantum limits}.
\end{aligned}
$$

The sequence is cumulative. A projectile problem needs vectors and kinematics. A rolling problem needs translation, rotation, energy, and static friction. A circuit transient looks mathematically like exponential cooling or damping. A diffraction problem requires geometry, wave phase, and careful small-angle reasoning. The most efficient study question is not "Which chapter is this from?" but "Which quantity is being transferred or constrained: force, energy, momentum, angular momentum, heat, charge, flux, phase, or probability?"

## Visual

```mermaid
graph LR
  A[Measurement] --> B[Vectors]
  B --> C[Mechanics]
  C --> D[Energy and Momentum]
  D --> E[Rotation and Fluids]
  E --> F[Oscillations and Waves]
  F --> G[Thermal Physics]
  G --> H[Electricity and Magnetism]
  H --> I[Optics]
  I --> J[Modern Physics]
```

| Course region | Central quantities | Typical method |
|---|---|---|
| Measurement and motion | $x$, $v$, $a$, $\vec r$ | units, coordinates, kinematics |
| Dynamics | $\vec F$, $K$, $U$, $\vec p$ | free-body diagrams, work, impulse |
| Extended systems | $\tau$, $I$, $\vec L$, stress | rotational dynamics and equilibrium |
| Thermal and waves | $T$, $Q$, $S$, $f$, $\lambda$ | energy accounting and phase |
| Fields and circuits | $\vec E$, $V$, $I$, $\vec B$ | flux, potential, Kirchhoff laws |
| Optics and modern limits | phase, wavelength, $\gamma$, $h$ | rays, interference, relativity, quanta |

## Worked example 1: Choosing an energy method

**Problem.** A $2.0\,\mathrm{kg}$ block slides from rest down a frictionless track and drops $1.8\,\mathrm{m}$ vertically. Find its speed at the bottom and explain why energy is the natural method.

**Method.** The normal force is perpendicular to the motion and does no work. Gravity is conservative. The track shape is irrelevant to the final speed, so use conservation of mechanical energy.

1. Define the system as block plus Earth.
2. Choose the bottom as $U_f=0$ and the release point as $U_i=mgh$.
3. Initial kinetic energy is zero.
4. Conservation gives

$$
\begin{aligned}
K_i+U_i &= K_f+U_f \\
0+mgh &= \frac12mv_f^2+0.
\end{aligned}
$$

5. Cancel mass and solve:

$$
v_f=\sqrt{2gh}=\sqrt{2(9.8)(1.8)}=5.94\,\mathrm{m/s}.
$$

**Checked answer.** The mass cancels, as expected for ideal gravitational motion. The speed is below $10\,\mathrm{m/s}$ because the drop is less than $5\,\mathrm{m}$.

## Worked example 2: Choosing a field method

**Problem.** A charge $q=3.0\,\mathrm{nC}$ is $0.20\,\mathrm{m}$ from a charge $Q=8.0\,\mathrm{nC}$. Find the force magnitude on $q$.

**Method.** For two point charges, Coulomb's law is direct. For many charges, compute $\vec E$ first and then use $\vec F=q\vec E$.

1. Use

$$
F=k\frac{|Qq|}{r^2}, \quad k=8.99\times10^9\,\mathrm{N\,m^2/C^2}.
$$

2. Substitute:

$$
F=(8.99\times10^9)\frac{(8.0\times10^{-9})(3.0\times10^{-9})}{(0.20)^2}.
$$

3. Compute:

$$
F=5.39\times10^{-6}\,\mathrm{N}.
$$

**Checked answer.** Micro-newtons are reasonable for nanocoulomb charges separated by centimeters.

## Code

```python
import math

speed = math.sqrt(2 * 9.8 * 1.8)
force = 8.99e9 * (8.0e-9 * 3.0e-9) / (0.20 ** 2)
print(f"roadmap pages = 25")
print(f"track speed = {speed:.2f} m/s")
print(f"electric force = {force:.2e} N")
```

## Common pitfalls

- Treating chapters as isolated instead of cumulative.
- Memorizing equations without their assumptions.
- Substituting numbers before choosing the system, signs, and coordinates.
- Confusing vectors and scalars.
- Reading worked examples passively instead of trying the next step first.

A final check is to perturb one input mentally. Doubling a distance, mass, charge, stiffness, frequency, or temperature should change the answer in a way that matches the physical story. If the algebra says the opposite, revisit the setup before blaming arithmetic. Also remember that a negative answer is often information: it may indicate direction opposite to the chosen axis, work done by a system rather than on it, or a potential change that lowers the energy of a positive or negative charge differently.

When a problem feels difficult, the hidden issue is often not the last algebraic step but the first modeling decision. Re-read the words and mark what is being idealized: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then mark what is conserved, if anything. Energy conservation, momentum conservation, angular momentum conservation, charge conservation, and entropy constraints are not interchangeable; each one has a system boundary and a transfer condition. If an external impulse acts, momentum may not be conserved for the chosen system. If friction acts within a block-floor system, mechanical energy is not conserved even though total energy is. If a Gaussian surface encloses no net charge, flux is zero, but the field at points on the surface need not be zero.

Another common pitfall is using a memorized equation in only its most familiar direction. A formula is a relationship, so practice solving it for different unknowns. In kinematics, solve for time, acceleration, or displacement depending on what the data support. In circuits, solve Ohm's law for voltage, current, or resistance and then check power. In optics, solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. In thermodynamics, rearrange the first law only after deciding whether work is done by the system or on the system. This flexibility prevents formula matching from replacing reasoning.

Finally, keep scale awareness. Introductory physics problems often use idealized numbers, but the answers should still sit on recognizable scales: walking speeds are meters per second, orbital speeds are kilometers per second, visible wavelengths are hundreds of nanometers, household currents are often amperes or less, and thermal energies per molecule at room temperature are small in joules but meaningful in electron-volts. When an answer is many orders of magnitude away from these anchors, check unit conversions first. Prefix errors such as nano versus micro, centimeters versus meters, and milliseconds versus seconds are among the fastest ways to turn correct physics into a wrong result.

For exam preparation, make the worked examples bidirectional. After solving a forward problem, change the target: ask what initial speed, resistance, angle, charge, temperature change, or wavelength would have produced the stated answer. This exposes whether you understand the structure or only followed the arithmetic once. Then make one assumption false and describe what would change. If air resistance is no longer negligible, projectile motion no longer separates into a constant horizontal speed. If a pulley has rotational inertia, the two string tensions need not match. If a lens is not thin, the thin-lens equation becomes an approximation. If a gas process is not reversible, entropy must be found from a reversible path connecting the same states, not from the literal irreversible path. These small variations turn a page of notes into a usable problem-solving tool.

Before leaving the problem, write one complete sentence that states the result in physical language. That sentence should name the object or system, the direction or sign when relevant, and the assumption under which the answer was obtained.

## Connections

- [Measurement and Vectors](/physics/general/measurement-units-and-vectors)
- [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics)
- [Two-Dimensional Motion](/physics/general/two-dimensional-motion)
- [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications)
- [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation)
- [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions)
- [Rotation and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum)
- [Equilibrium and Elasticity](/physics/general/equilibrium-and-elasticity)
- [Gravitation](/physics/general/gravitation-and-keplers-laws)
- [Fluids](/physics/general/fluids-statics-dynamics-and-bernoulli)
- [Oscillations](/physics/general/oscillations-shm-damping-and-resonance)
- [Waves and Sound](/physics/general/waves-sound-standing-waves-and-doppler)
- [Temperature, Heat, and Kinetic Theory](/physics/general/temperature-heat-and-kinetic-theory)
- [Thermodynamics](/physics/general/first-law-entropy-and-second-law)
- [Coulomb's Law and Electric Field](/physics/general/coulombs-law-and-electric-fields)
- [Gauss's Law](/physics/general/gausss-law-and-electric-flux)
- [Electric Potential and Capacitance](/physics/general/electric-potential-and-capacitance)
- [Current, Resistance, and DC Circuits](/physics/general/current-resistance-and-dc-circuits)
- [Magnetic Fields and Forces](/physics/general/magnetic-fields-and-forces)
- [Magnetic Sources and Induction](/physics/general/ampere-faraday-lenz-and-inductance)
- [AC Circuits and EM Waves](/physics/general/ac-circuits-and-electromagnetic-waves)
- [Geometric Optics](/physics/general/geometric-optics-reflection-and-refraction)
- [Interference and Diffraction](/physics/general/interference-diffraction-and-gratings)
- [Relativity Intro](/physics/general/relativity-intro)
- [Quantum Intro](/physics/general/quantum-intro-photons-and-matter-waves)
