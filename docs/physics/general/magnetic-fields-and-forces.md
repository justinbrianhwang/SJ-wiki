---
title: Magnetic Fields and Forces
sidebar_position: 20
---

# Magnetic Fields and Forces

Magnetic fields act on moving charge. Their geometry is encoded by a cross product, so direction matters as much as magnitude. A field can bend a charged particle, push a wire, or rotate a current loop, yet a static magnetic force cannot change the kinetic energy of a point charge.

The SI unit is the tesla:

$$
1\,\mathrm T=1\,\frac{\mathrm N}{\mathrm{A\,m}}
=1\,\frac{\mathrm{N\,s}}{\mathrm{C\,m}}.
$$

Field lines are a drawing convention: their tangent gives the field direction and their density suggests relative strength. They do not represent material threads or particle trajectories.

## The magnetic part of the Lorentz force

For a particle of charge $q$ and velocity $\vec v$,

$$
\vec F_B=q\vec v\times\vec B,
$$

with magnitude

$$
F_B=\lvert q\rvert vB\sin\theta.
$$

The angle $\theta$ is between velocity and field. Parallel or antiparallel motion gives zero force; perpendicular motion gives the maximum. For a positive charge, curl the right-hand fingers from $\vec v$ toward $\vec B$ through the smaller angle and the thumb gives $\vec F_B$. A negative charge reverses that direction.

The complete electromagnetic force is

$$
\vec F=q(\vec E+\vec v\times\vec B).
$$

Electric and magnetic contributions must be added as vectors. The electric term can act on a charge at rest and can change its speed. The magnetic term requires motion relative to the frame in which the field is specified.

Since the cross product is perpendicular to velocity,

$$
\vec F_B\cdot\vec v=0.
$$

The magnetic power delivered to a point charge is therefore zero. A static magnetic field changes momentum direction without changing speed or kinetic energy. If a magnetic device appears to accelerate a charge, an electric field, a time-dependent field, or another force is doing the work.

## Circular and helical motion

Suppose $\vec v$ is perpendicular to a uniform $\vec B$. The magnetic force has constant magnitude and remains perpendicular to the motion, so it supplies centripetal force:

$$
\lvert q\rvert vB=\frac{mv^2}{r}.
$$

Hence

$$
r=\frac{mv}{\lvert q\rvert B}
=\frac{p}{\lvert q\rvert B}.
$$

The momentum form remains useful relativistically if $p=\gamma mv$ is used. The nonrelativistic angular frequency follows from $v=r\omega$:

$$
\omega_c=\frac{\lvert q\rvert B}{m},
\qquad
T_c=\frac{2\pi m}{\lvert q\rvert B}.
$$

At nonrelativistic speed, the cyclotron period is independent of radius and speed. Relativistic momentum breaks that simple independence.

If velocity has both perpendicular and parallel components, only $v_\perp$ bends. The particle follows a helix:

$$
r=\frac{mv_\perp}{\lvert q\rvert B},
\qquad
\text{pitch}=v_\parallel T_c.
$$

The sign of charge determines the handedness. Looking along the field, positive and negative charges circulate in opposite directions.

### Worked orbit of a proton

A proton moves at $2.0\times10^6\,\mathrm{m/s}$ perpendicular to a $0.50\,\mathrm T$ field. With $m_p=1.67\times10^{-27}\,\mathrm{kg}$ and $q=1.60\times10^{-19}\,\mathrm C$,

$$
\begin{aligned}
r
&=\frac{m_pv}{qB}\\
&=\frac{(1.67\times10^{-27})(2.0\times10^6)}
{(1.60\times10^{-19})(0.50)}\\
&=4.18\times10^{-2}\,\mathrm m.
\end{aligned}
$$

The radius is $4.18\,\mathrm{cm}$. Its period is

$$
\begin{aligned}
T_c
&=\frac{2\pi m_p}{qB}\\
&=\frac{2\pi(1.67\times10^{-27})}
{(1.60\times10^{-19})(0.50)}\\
&=1.31\times10^{-7}\,\mathrm s.
\end{aligned}
$$

Changing the proton to an electron at the same speed and field would sharply reduce the radius because the electron mass is smaller. Its curvature direction would also reverse because its charge is negative.

## Crossed fields as a velocity selector

Let an electric field and magnetic field be perpendicular to each other and to a particle beam. Orient them so their forces oppose. An undeflected particle satisfies

$$
\lvert q\rvert E=\lvert q\rvert vB,
$$

giving

$$
v=\frac{E}{B}.
$$

Charge magnitude and mass cancel. Faster particles experience the larger magnetic force and bend one way; slower particles are dominated by the electric force and bend the other way.

For $E=3.0\times10^4\,\mathrm{N/C}$ and $B=0.20\,\mathrm T$,

$$
v=\frac{3.0\times10^4}{0.20}
=1.5\times10^5\,\mathrm{m/s}.
$$

After selection, a second region containing only a magnetic field can sort particles by mass-to-charge ratio:

$$
\frac{m}{\lvert q\rvert}=\frac{rB}{v}.
$$

This is the basic geometry behind a mass spectrometer. Ions with the same selected speed but different $m/\lvert q\rvert$ follow different radii.

## From moving charges to force on a wire

In a straight conductor, many charge carriers drift through the material. Summing their magnetic forces gives

$$
\vec F=I\vec L\times\vec B,
$$

where $\vec L$ points along conventional current. In a metal, electrons drift opposite to $\vec L$. Reversing both the carrier charge and its velocity leaves the conventional-current direction consistent.

For a curved wire or nonuniform field, use

$$
d\vec F=I\,d\vec\ell\times\vec B
$$

and integrate along the conductor. A closed loop in a uniform field has zero net force because opposite segments cancel. It may still have a torque.

### Worked force on a wire

A $0.30\,\mathrm m$ wire carries $4.0\,\mathrm A$ east through a $0.20\,\mathrm T$ field directed north. East crossed with north points upward, and the magnitude is

$$
F=ILB\sin90^\circ
=(4.0)(0.30)(0.20)
=0.24\,\mathrm N.
$$

If the wire is rotated until it lies $30^\circ$ from the field,

$$
F=(4.0)(0.30)(0.20)\sin30^\circ
=0.12\,\mathrm N.
$$

If it becomes parallel, the force vanishes. The magnetic field does not push charges along a wire parallel to itself.

## Torque and magnetic dipole energy

For a planar loop carrying current $I$, define the magnetic dipole moment

$$
\vec\mu=NI\vec A,
$$

where $N$ is the turn count and $\vec A$ is normal to the loop by the right-hand rule. In a uniform field,

$$
\vec\tau=\vec\mu\times\vec B,
\qquad
\tau=\mu B\sin\theta.
$$

Opposite sides of a rectangular loop experience equal and opposite forces. Their net force is zero, but their lines of action differ, producing a couple. The associated potential energy is

$$
U=-\vec\mu\cdot\vec B=-\mu B\cos\theta.
$$

Stable equilibrium has $\vec\mu$ parallel to $\vec B$, where energy is minimum. Antiparallel alignment is unstable.

Take a $50$-turn loop of area $2.0\times10^{-3}\,\mathrm{m^2}$ carrying $0.40\,\mathrm A$ in a $0.30\,\mathrm T$ field. When its moment is $60^\circ$ from the field,

$$
\mu=NIA=(50)(0.40)(2.0\times10^{-3})
=4.0\times10^{-2}\,\mathrm{A\,m^2},
$$

and

$$
\tau=\mu B\sin60^\circ
=(4.0\times10^{-2})(0.30)(0.866)
=1.04\times10^{-2}\,\mathrm{N\,m}.
$$

This torque principle underlies simple motors and moving-coil meters. Continuous motor rotation also requires current switching or an alternating field so that torque continues in the desired rotational sense.

## Sources of magnetic field

Steady currents create magnetic fields. For a long straight wire,

$$
B=\frac{\mu_0I}{2\pi r},
$$

with circular field direction given by a right-hand grip around the current. For the center of a circular loop of radius $R$,

$$
B=\frac{\mu_0NI}{2R}.
$$

Inside an ideal long solenoid with $n$ turns per unit length,

$$
B\approx\mu_0nI.
$$

These are symmetry results from the Biot–Savart law or Ampère's law. The long-wire expression fails near the wire's ends or when its finite length matters. The ideal-solenoid result neglects edge fringing.

Two long parallel wires illustrate how fields and forces combine. Currents in the same direction attract; opposite currents repel. Each wire creates a field at the other's position, and $I\vec L\times\vec B$ gives the resulting force. It is safer to derive the direction than to memorize the rule in isolation.

## Hall voltage and the sign of charge carriers

A current-carrying strip in a perpendicular magnetic field experiences sideways magnetic force on its mobile carriers. Charge accumulates along one edge until the resulting electric force balances the magnetic force:

$$
qE_H=qv_dB.
$$

Thus $E_H=v_dB$. For strip width $w$, the transverse Hall voltage magnitude is

$$
V_H=E_Hw.
$$

Its polarity reveals the sign of the dominant carriers. Combining Hall voltage with current and sample geometry can also determine carrier density. The simple formula assumes one dominant carrier type and a uniform sample.

## Magnetic flux is not magnetic force

Magnetic flux through a surface is

$$
\Phi_B=\int\vec B\cdot d\vec A.
$$

For uniform field through a flat area, $\Phi_B=BA\cos\theta$, where $\theta$ is measured from the area normal. Force on a moving charge instead contains a sine of the angle between velocity and field. Mixing these angles is common because both formulas involve $\vec B$ but represent different dot and cross products.

Flux becomes central when fields change with time: Faraday's law relates changing flux to induced electric fields. A static uniform flux by itself does not imply a force on a stationary charge.

## Magnetic dipoles in nonuniform fields

A uniform field can rotate a dipole but exerts no net translational force on an ideal current loop. In a nonuniform field, the forces on opposite sides no longer cancel. For a dipole aligned along one dimension, the force is approximately

$$
F_x\approx\mu_x\frac{dB_x}{dx}.
$$

The dipole tends to move toward stronger field if its moment is aligned and toward weaker field if anti-aligned. A bar magnet near another magnet behaves this way; saying only that “north attracts south” does not account for the field gradient and orientation that produce net motion.

Atomic magnetic moments arise from electron orbital motion and intrinsic spin. Their interaction energy still has the form $-\vec\mu\cdot\vec B$, although spin is a quantum property rather than a literal charged sphere rotating. Spatially varying fields can split beams according to moment orientation, as in the Stern–Gerlach experiment.

## Magnetic materials

Materials respond differently to applied fields. Diamagnetic response opposes the applied field and occurs in all matter, though it is usually weak. Paramagnetic materials contain moments that tend to align with the field but are randomized by thermal motion. Ferromagnets can develop strong collective alignment and retain magnetization after the external field is removed.

Ferromagnetic material is divided into domains. Within a domain, many moments are aligned; an unmagnetized sample can still have domains oriented so their macroscopic fields largely cancel. An applied field changes domain walls and orientations. The resulting magnetization depends on the material's previous history, producing hysteresis.

These responses mean that the simple vacuum relation between current and field may need a material model. Introductory force formulas using a specified $\vec B$ remain valid for a test charge, but predicting $\vec B$ inside a magnetic material requires more information than current geometry alone.

## No isolated magnetic poles in classical electromagnetism

Electric field lines may begin on positive charge and end on negative charge. Magnetic field lines form closed loops. Gauss's law for magnetism states

$$
\oint\vec B\cdot d\vec A=0
$$

for every closed surface. Magnetic flux entering a closed surface equals flux leaving it.

Cutting a bar magnet in half does not isolate north and south poles; it produces two smaller dipoles. Magnetic monopoles have been considered in theoretical physics, but none is needed for the standard classical equations used here.

The zero-flux law does not say the magnetic field is zero. A uniform field through a box has nonzero flux through individual faces, but opposite faces cancel in the closed-surface sum.

## Worked helical path

An electron enters a $0.080\,\mathrm T$ field with perpendicular velocity $v_\perp=3.0\times10^6\,\mathrm{m/s}$ and parallel velocity $v_\parallel=4.0\times10^6\,\mathrm{m/s}$. Its helical radius is

$$
\begin{aligned}
r&=\frac{m_ev_\perp}{eB}\\
&=\frac{(9.11\times10^{-31})(3.0\times10^6)}
{(1.602\times10^{-19})(0.080)}\\
&=2.13\times10^{-4}\,\mathrm m.
\end{aligned}
$$

The cyclotron period is

$$
\begin{aligned}
T_c&=\frac{2\pi m_e}{eB}\\
&=4.47\times10^{-10}\,\mathrm s.
\end{aligned}
$$

During one turn, the electron advances along the field by

$$
\text{pitch}=v_\parallel T_c
=(4.0\times10^6)(4.47\times10^{-10})
=1.79\times10^{-3}\,\mathrm m.
$$

The total speed stays $5.0\times10^6\,\mathrm{m/s}$ because the perpendicular and parallel components are unchanged in magnitude. Replacing total speed by $v_\perp$ in the radius and by $v_\parallel$ in the pitch is essential.

## Magnetism and reference frames

Electric and magnetic fields are different components of one electromagnetic field. A situation described as magnetic force in one inertial frame can involve a different mixture of electric and magnetic fields in another. For example, a neutral current-carrying wire in the laboratory can have a different charge density in a moving particle's frame because relativistic length contraction affects positive lattice charges and moving carriers differently.

This frame dependence does not make magnetic effects optional. The combined Lorentz force transforms consistently, and all observers agree on the particle's physical trajectory after translating coordinates. It explains why electric and magnetic units and laws fit together so tightly.

The field also depends on the observer, so a bare statement of $\vec B$ should be understood as belonging to a specified frame. Laboratory problems normally leave that frame implicit. When source and test-particle speeds are ordinary, transforming fields is unnecessary; the supplied laboratory fields and velocities belong in the Lorentz-force equation together.

At high relative speed, electric and magnetic field transformation formulas are required; mixing quantities quoted in different frames gives no valid force.

## Geometry and model checks

- Draw $\vec v$, $\vec B$, and the positive-charge force before reversing for a negative charge.
- The sine belongs to the angle between the vectors in the cross product. It is not automatically one.
- A magnetic field alone cannot change a point charge's speed.
- Conventional current points opposite electron drift in a metal.
- The circular-radius formula uses the velocity component perpendicular to the field.
- At relativistic speed, replace $mv$ by relativistic momentum.
- A uniform field can torque a current loop with zero net force; a field gradient can also produce net force on a dipole.

<div className="see-also">

See also: [Ampère, Faraday, Lenz, and Inductance](/physics/general/ampere-faraday-lenz-and-inductance) · [AC Circuits and Electromagnetic Waves](/physics/general/ac-circuits-and-electromagnetic-waves) · [Relativity Intro](/physics/general/relativity-intro)

</div>
