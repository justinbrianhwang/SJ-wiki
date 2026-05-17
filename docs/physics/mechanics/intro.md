---
title: Statics and Dynamics
sidebar_position: 1
---

# Engineering Mechanics: Statics and Dynamics

These notes organize engineering mechanics around the balance laws that connect forces, moments, motion, energy, and momentum. The sequence begins with vector modeling and free-body diagrams, moves through statics of particles and rigid bodies, then develops the dynamics of particles and planar rigid bodies. The emphasis is practical setup: isolate the body, draw the force model, choose coordinates, write the governing equations, and check the result against units and physical intuition.

The source PDF's table of contents separates the subject into mechanics basics, statics, and dynamics, including vectors, free-body diagrams, equilibrium, trusses and frames, internal forces, one-dimensional and spatial particle dynamics, rigid-body planar motion, constraints, and friction. This wiki path follows that structure while also adding the standard section-property and vibration tools commonly paired with an engineering mechanics course.

Use the pages in order for a first pass. Later, jump directly to the method family needed for a problem.

![A truss bridge diagram shows triangular members carrying loads across a span.](https://commons.wikimedia.org/wiki/Special:FilePath/Truss_bridge.svg)

*Figure: A truss bridge gives statics pages an immediate real structure for joints, members, and load paths. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Truss_bridge.svg), Noleander, CC0 1.0.*

![A beam bends under transverse loading in a simple mechanics schematic.](https://commons.wikimedia.org/wiki/Special:FilePath/Beam_bending.svg)

*Figure: Beam bending connects support reactions, internal shear, bending moment, and section stiffness. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Beam_bending.svg), Krishnavedala, CC0 1.0.*

![An inverted pendulum is mounted on a cart with its angle and cart position labeled.](https://commons.wikimedia.org/wiki/Special:FilePath/Cart-pendulum.svg)

*Figure: The cart-pendulum setup is a classic benchmark for unstable dynamics, feedback, and hybrid simulation tests. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cart-pendulum.svg), Krishnavedala, CC0 1.0.*

## Chapter List

1. [Force Vectors, Resultants, and Components](/physics/mechanics/force-vectors-resultants-components)
2. [Particle Equilibrium](/physics/mechanics/particle-equilibrium)
3. [Rigid-Body Equilibrium](/physics/mechanics/rigid-body-equilibrium)
4. [Trusses, Frames, and Machines](/physics/mechanics/trusses-frames-machines)
5. [Internal Forces in Beams](/physics/mechanics/internal-forces-beams)
6. [Friction: Dry Contact, Belts, and Screws](/physics/mechanics/friction-dry-belt-screws)
7. [Centroids and Second Moments](/physics/mechanics/centroids-second-moments)
8. [Particle Kinematics](/physics/mechanics/particle-kinematics)
9. [Particle Kinetics with Newton's Second Law](/physics/mechanics/particle-kinetics-newton)
10. [Work-Energy Methods](/physics/mechanics/work-energy-methods)
11. [Impulse, Momentum, and Impact](/physics/mechanics/impulse-momentum-impact)
12. [Planar Rigid-Body Motion](/physics/mechanics/planar-rigid-body-motion)
13. [Vibrations of Single-Degree-of-Freedom Systems](/physics/mechanics/vibrations-single-dof)

## Problem-Solving Pattern

Most mechanics problems become manageable when the setup is disciplined:

1. Choose the system or body to isolate.
2. Draw a free-body diagram with only external forces and moments.
3. Choose coordinates that fit the geometry or motion.
4. Write the applicable balance law: force, moment, energy, impulse-momentum, or angular momentum.
5. Add kinematic or geometric constraints.
6. Solve with units attached.
7. Check signs, limiting cases, and physical reasonableness.

Statics uses the zero-acceleration limits of the same balance laws:

$$
\sum\mathbf{F}=\mathbf{0},\qquad \sum\mathbf{M}=\mathbf{0}.
$$

Dynamics keeps the inertial terms:

$$
\sum\mathbf{F}=m\mathbf{a},\qquad \sum M_G=I_G\alpha.
$$

Energy and momentum methods give alternate views:

$$
T_1+V_1+U_{\mathrm{nc}}=T_2+V_2,
$$

$$
\int_{t_1}^{t_2}\sum\mathbf{F}\,dt=m\mathbf{v}_2-m\mathbf{v}_1.
$$

The pages that follow repeat this pattern with different modeling assumptions, diagrams, examples, and runnable code.
