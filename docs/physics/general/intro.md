---
title: "General Physics: HRW Introductory Roadmap"
sidebar_position: 1
---

# General Physics: HRW Introductory Roadmap

General physics turns ordinary events into quantitative models: falling, sliding, rotating, heating, flowing, oscillating, charging, refracting, and scattering. The Halliday–Resnick–Walker sequence is cumulative. Measurement and vectors establish the language; mechanics develops force, energy, and momentum; rotation and fluids extend it beyond point particles; oscillations and waves introduce phase and resonance; thermal physics adds macroscopic and microscopic energy bookkeeping; fields replace contact interactions in electricity and magnetism; optics tests ray and wave descriptions; relativity and quantum physics mark the limits of classical models.

## Models, state, and system boundaries

A **physical model** suppresses details that do not matter at the scale of the question. A point particle has no size or rotation, a rigid body does not deform, an ideal fluid is incompressible and nonviscous, an ideal gas follows a simple equation of state, and an electrostatic model holds charges fixed.

A **state variable** helps specify a system: position, velocity, temperature, pressure, charge, current, and angular velocity are examples. A **law** relates state variables and interactions. A **conservation principle** states that a quantity changes only by transfer across a chosen system boundary.

Vectors carry magnitude and direction, so $\vec F=m\vec a$ must be read component by component. Work, energy, temperature, pressure, entropy, and electric potential are scalars; their signs still depend on references and conventions.

Units are part of the model. Wrong dimensions rule out an answer. Correct dimensions leave a candidate that still needs checks on sign, assumptions, limiting cases, and scale.

## The course as a chain of reused ideas

The subject can be grouped into four families:

- **Evolution equations:** kinematics, Newton's second law, rotational dynamics, circuit transients, thermodynamic process equations, and wave equations.
- **Conservation laws:** energy, linear momentum, angular momentum, charge, and entropy constraints for isolated systems.
- **Field laws:** Newtonian gravitation, Coulomb's law, Gauss's law, Ampère's law, Faraday's law, and the qualitative content of Maxwell's equations.
- **Model transitions:** ray and wave optics, classical and relativistic motion, and particle and wave descriptions of matter.

```mermaid
graph LR
  A["Measurement"] --> B["Vectors"]
  B --> C["Mechanics"]
  C --> D["Energy and momentum"]
  D --> E["Rotation and fluids"]
  E --> F["Oscillations and waves"]
  F --> G["Thermal physics"]
  G --> H["Electricity and magnetism"]
  H --> I["Optics"]
  I --> J["Modern physics"]
```

| Course region | Central quantities | Typical method |
|---|---|---|
| Measurement and motion | $x$, $v$, $a$, $\vec r$ | units, coordinates, kinematics |
| Dynamics | $\vec F$, $K$, $U$, $\vec p$ | free-body diagrams, work, impulse |
| Extended systems | $\tau$, $I$, $\vec L$, stress | rotational dynamics and equilibrium |
| Thermal physics and waves | $T$, $Q$, $S$, $f$, $\lambda$ | energy accounting and phase |
| Fields and circuits | $\vec E$, $V$, $I$, $\vec B$ | flux, potential, Kirchhoff's laws |
| Optics and modern limits | phase, wavelength, $\gamma$, $h$ | rays, interference, relativity, quanta |

In compact form,

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

A projectile uses vectors and kinematics. Rolling combines translation, rotation, energy, and static friction. A circuit transient has the same exponential structure as cooling and damping. Diffraction combines geometry, phase, and small-angle approximations. Instead of asking which chapter supplied a problem, identify what is transferred or constrained: force, energy, momentum, angular momentum, heat, charge, flux, phase, or probability.

## Energy when the path shape does not matter

A $2.0\,\mathrm{kg}$ block starts from rest and descends $1.8\,\mathrm{m}$ on a frictionless track. The normal force is perpendicular to the motion and does no work; gravity is conservative. Because only the vertical drop affects the final speed, an energy balance is shorter than resolving forces along an unspecified track.

Take the system to be the block and Earth, and choose the bottom as $U_f=0$. Then

$$
\begin{aligned}
K_i+U_i &= K_f+U_f, \\
0+mgh &= \frac12mv_f^2+0.
\end{aligned}
$$

Mass cancels, leaving

$$
v_f=\sqrt{2gh}
=\sqrt{2(9.8)(1.8)}
=5.94\,\mathrm{m/s}.
$$

Independence from mass agrees with ideal gravitational motion. A drop under two meters should produce a speed of only several meters per second, so the scale is plausible.

## Coulomb's law for two point charges

Let $q=3.0\,\mathrm{nC}$ and $Q=8.0\,\mathrm{nC}$ be separated by $0.20\,\mathrm{m}$. For two point charges, the force magnitude follows directly from

$$
F=k\frac{|Qq|}{r^2},
\qquad
k=8.99\times10^9\,\mathrm{N\,m^2/C^2}.
$$

Substitution gives

$$
\begin{aligned}
F
&=(8.99\times10^9)
\frac{(8.0\times10^{-9})(3.0\times10^{-9})}{(0.20)^2} \\
&=5.39\times10^{-6}\,\mathrm{N}.
\end{aligned}
$$

Both charges are positive, so the force on $q$ points away from $Q$. For many source charges, it is usually cleaner to sum their electric fields first and then apply $\vec F=q\vec E$.

## Choosing an equation only after choosing a model

Many wrong solutions begin with a familiar formula before the system, coordinates, and assumptions are fixed. Mark the idealizations in the prompt: frictionless surface, ideal string, point charge, thin lens, small angle, steady flow, reversible process, nonrelativistic particle, or uniform field. Then choose a boundary and ask what can cross it.

Conservation laws are not interchangeable. An external impulse can change the momentum of the selected system. Friction inside a block–floor system preserves total energy while converting mechanical energy into thermal energy. A Gaussian surface enclosing zero net charge has zero net flux, even though the field at individual points on the surface may be nonzero.

A negative result often reports direction or bookkeeping rather than failure: a velocity may oppose the positive axis, work may be done by the system rather than on it, or a potential change may lower the energy of one sign of charge and raise the other.

## Reversing familiar formulas

Equations are relationships, not one-way recipes. Solve kinematic equations for time, acceleration, or displacement according to the available data. Rearrange Ohm's law for voltage, current, or resistance and then check power. Solve the thin-lens equation for image distance, object distance, or focal length and compare the sign with a ray diagram. Rearrange the first law of thermodynamics only after fixing the convention for work done by or on the system.

After a forward solution, change the target. Ask which initial speed, resistance, angle, charge, temperature change, or wavelength would produce the stated outcome. This exposes the structure of the relationship more clearly than repeating the same substitution.

Then change an assumption. Air resistance couples the horizontal and vertical parts of projectile motion. A pulley with rotational inertia may have unequal string tensions. A thick lens makes the thin-lens equation approximate. For an irreversible gas process, entropy change can be calculated along a reversible path connecting the same equilibrium states, even though that path is not the actual process.

## Scale, units, and limiting cases

Perturb one input mentally. Doubling a distance, charge, stiffness, frequency, or temperature should change the answer in a way consistent with the model. An inverse-square law must weaken by a factor of four when distance doubles. A spring frequency should rise with stiffness and fall with mass.

Keep a few scale anchors: walking speeds are meters per second, orbital speeds kilometers per second, visible wavelengths hundreds of nanometers, household currents commonly amperes or less, and room-temperature molecular energies are tiny in joules but convenient in electron-volts. Results many orders of magnitude away from these scales call for a unit check. Nano versus micro, centimeters versus meters, and milliseconds versus seconds are frequent sources of large errors.

Before leaving a calculation, state the result in one complete physical sentence naming the system, direction or sign when relevant, and the assumptions under which the number holds.

## A working routine for the examples

1. Identify the system, environment, coordinates, and requested quantity.
2. List the approximations and determine the regime in which they hold.
3. Draw the geometry, free-body diagram, circuit, ray diagram, or process path that corresponds to the model.
4. Choose a law from the interactions and boundary conditions, then solve symbolically as far as useful.
5. Substitute values with units and retain enough precision for the data.
6. Check dimensions, sign, limiting behavior, and order of magnitude.
7. Change the target or one assumption to test whether the relationship is understood beyond a single calculation.

<div className="see-also">

See also: [Measurement and Vectors](/physics/general/measurement-units-and-vectors) · [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics) · [Two-Dimensional Motion](/physics/general/two-dimensional-motion) · [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications) · [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions) · [Rotation and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum) · [Equilibrium and Elasticity](/physics/general/equilibrium-and-elasticity) · [Gravitation](/physics/general/gravitation-and-keplers-laws) · [Fluids](/physics/general/fluids-statics-dynamics-and-bernoulli) · [Oscillations](/physics/general/oscillations-shm-damping-and-resonance) · [Waves and Sound](/physics/general/waves-sound-standing-waves-and-doppler) · [Temperature, Heat, and Kinetic Theory](/physics/general/temperature-heat-and-kinetic-theory) · [Thermodynamics](/physics/general/first-law-entropy-and-second-law) · [Coulomb's Law and Electric Field](/physics/general/coulombs-law-and-electric-fields) · [Gauss's Law](/physics/general/gausss-law-and-electric-flux) · [Electric Potential and Capacitance](/physics/general/electric-potential-and-capacitance) · [Current, Resistance, and DC Circuits](/physics/general/current-resistance-and-dc-circuits) · [Magnetic Fields and Forces](/physics/general/magnetic-fields-and-forces) · [Magnetic Sources and Induction](/physics/general/ampere-faraday-lenz-and-inductance) · [AC Circuits and EM Waves](/physics/general/ac-circuits-and-electromagnetic-waves) · [Geometric Optics](/physics/general/geometric-optics-reflection-and-refraction) · [Interference and Diffraction](/physics/general/interference-diffraction-and-gratings) · [Relativity Intro](/physics/general/relativity-intro) · [Quantum Intro](/physics/general/quantum-intro-photons-and-matter-waves)

</div>
