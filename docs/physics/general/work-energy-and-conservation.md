---
title: Work, Energy, and Conservation
sidebar_position: 6
---

# Work, Energy, and Conservation

Work and energy provide an accounting method for motion and interactions. Instead of finding the acceleration at every instant, an energy calculation can compare two states directly. The method is especially useful for tracks, springs, gravity, and any problem in which the path is awkward but the initial and final states are simple.

Mechanical energy conservation depends on the chosen system. When only conservative forces transfer energy within it, $K+U$ is constant. Friction, drag, motors, and other nonconservative transfers change mechanical energy, although a complete energy balance still holds for a sufficiently broad closed system.

## Choosing the system and the energy ledger

The central quantities are operational:

- **Work** by a constant force over a displacement is $W=\vec F\cdot\vec d=Fd\cos\theta$.
- Along a general path, $W=\int \vec F\cdot d\vec r$; in one dimension this reduces to $W=\int F_x\,dx$.
- **Kinetic energy** is $K=\frac12mv^2$.
- **Power** is the rate of energy transfer, $P=dW/dt=\vec F\cdot\vec v$.
- A **conservative force** does path-independent work.
- **Potential energy** is defined so that $\Delta U=-W_c$ for conservative work.
- In a uniform gravitational field, $U_g=mgy$; for an ideal spring, $U_s=\frac12kx^2$.

Before writing an equation, draw the system boundary and name the two states being compared. A block alone and a block-plus-floor are different systems: kinetic friction is an external transfer for the first, while for the second it converts mechanical energy into internal energy. State the model assumptions at the same time—frictionless surface, massless spring, uniform gravitational field—because the energy ledger follows from those assumptions.

The following sequence keeps the physical model ahead of the algebra:

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

## From net work to speed

The work-energy theorem states

$$
W_{net}=\Delta K.
$$

It follows from Newton's second law, but it packages the force history into an integral. Positive net work raises the speed, negative net work lowers it, and zero net work leaves the kinetic energy unchanged. Individual forces may still do nonzero work that cancels in the total.

Power adds the time scale. A system can move at constant speed and still require power: an elevator rising steadily has constant kinetic energy while its gravitational potential energy increases.

## Conservative forces and mechanical energy

For conservative interactions,

$$
K_i+U_i=K_f+U_f.
$$

Potential energy belongs to the interaction represented in the system, not to an isolated object. Its zero is arbitrary; only differences in $U$ enter measurable predictions. In one dimension, the associated force is

$$
F_x=-\frac{dU}{dx}.
$$

If nonconservative forces do work on the chosen system, the corresponding balance is

$$
W_{nc}=\Delta K+\Delta U.
$$

This equation is often safer than writing “energy is lost.” Friction may reduce $K+U$, but the missing mechanical energy normally appears as thermal energy. Whether that conversion is represented by $W_{nc}$ or by an internal-energy term depends on where the system boundary was drawn.

## Pulling a crate at an angle

**Problem.** A $50\,\mathrm{N}$ force pulls a crate $6.0\,\mathrm{m}$ at $25^\circ$ above horizontal. Find the work done by the pull.

Only the force component along the displacement contributes:

$$
W=Fd\cos\theta.
$$

Substitution gives

$$
W=(50)(6.0)\cos25^\circ
  =300(0.906)
  =272\,\mathrm{J}.
$$

The answer is below $Fd=300\,\mathrm{J}$ because the force is angled. The vertical component changes the normal force, but it does no work during a horizontal displacement.

## Launching a block from a spring

**Problem.** A $0.50\,\mathrm{kg}$ block compresses a $200\,\mathrm{N/m}$ spring by $0.10\,\mathrm{m}$ on a frictionless surface. Find the launch speed.

Spring potential energy becomes kinetic energy:

$$
\frac12kx^2=\frac12mv^2.
$$

Solving before inserting values gives

$$
v=x\sqrt{\frac{k}{m}}.
$$

Therefore,

$$
v=0.10\sqrt{\frac{200}{0.50}}=2.0\,\mathrm{m/s}.
$$

The symbolic form also shows the expected trends: greater stiffness or compression raises the launch speed, while greater mass lowers it.

## Checks that catch bad energy setups

Several errors recur often enough to check explicitly:

- In $W=Fd\cos\theta$, $\theta$ is the angle between the force and displacement, not necessarily an angle measured from the horizontal.
- Do not impose $K+U=\text{constant}$ when friction, drag, or an applied motor transfers energy across the system boundary. Include the work or enlarge the system and track the resulting energy form.
- The numerical value of potential energy depends on the chosen reference. A change in the reference cannot change $\Delta U$, the force, or the predicted motion.
- Work and power answer different questions. Equal amounts of work delivered over different intervals correspond to different average powers.
- A negative result often carries physical information: a force may oppose the motion, or the chosen system may be doing work on its surroundings.

Solve symbolically when possible, then check dimensions, signs, and limiting behavior. In the spring result, for example, the final units reduce to meters per second. Mentally varying one input is another useful test. If the algebra predicted a lower launch speed for a more compressed spring, the setup would need correction before any arithmetic check.

Scale checks catch unit-prefix mistakes quickly. Everyday speeds are usually measured in meters per second, and mechanical energies in introductory problems are commonly joules rather than enormous powers of ten. Converting centimeters to meters before squaring a spring compression is particularly important because the conversion error is squared as well.

After a forward solution, reversing the unknown tests whether the relation is understood rather than memorized. The crate calculation can be solved for the pulling angle or distance; the spring calculation can be solved for the compression needed to reach a specified speed. Changing one assumption is equally revealing: adding kinetic friction introduces a negative work term, while giving the spring mass requires accounting for some kinetic energy in the spring itself.

<div className="see-also">

See also: [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications) · [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions) · [First Law, Entropy, and Second Law](/physics/general/first-law-entropy-and-second-law)

</div>
