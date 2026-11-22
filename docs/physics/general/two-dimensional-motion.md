---
title: "Two-Dimensional Motion: Projectiles and Circular Motion"
sidebar_position: 4
---

# Two-Dimensional Motion: Projectiles and Circular Motion

Motion in a plane is governed by the same definitions as motion on a line, but position, velocity, and acceleration are vectors. The main choice is the coordinate system. Fixed horizontal and vertical axes make projectile motion nearly separable. Tangential and normal directions follow a curved path and expose the two distinct ways velocity can change: its magnitude can change, and its direction can turn.

Projectiles and circular motion are often taught together because each defeats a common shortcut. A projectile has one time coordinate shared by two component equations; the components are not two separate journeys. An object moving around a circle can have constant speed while retaining a nonzero acceleration.

## Vector kinematics in a fixed plane

Write the position as

$$
\mathbf r(t)=x(t)\mathbf i+y(t)\mathbf j.
$$

Differentiation gives

$$
\mathbf v=\dot x\mathbf i+\dot y\mathbf j,
\qquad
\mathbf a=\ddot x\mathbf i+\ddot y\mathbf j.
$$

If acceleration is constant, integration produces the vector equations

$$
\mathbf v=\mathbf v_0+\mathbf a t,
$$

$$
\mathbf r=\mathbf r_0+\mathbf v_0t+\frac12\mathbf a t^2.
$$

These are shorthand for independent scalar equations along fixed perpendicular axes. The independence comes from vector addition, not from separate clocks: the same $t$ appears in every component.

## Building the projectile equations

Neglect air resistance and treat gravity as uniform near Earth's surface. Taking $x$ horizontal and $y$ upward,

$$
\mathbf a=-g\mathbf j.
$$

A launch speed $v_0$ at angle $\theta$ above horizontal has components

$$
v_{0x}=v_0\cos\theta,
\qquad
v_{0y}=v_0\sin\theta.
$$

If the launch point is $(x_0,y_0)$, integration gives

$$
\begin{aligned}
x(t)&=x_0+v_0\cos\theta\,t,\\
y(t)&=y_0+v_0\sin\theta\,t-\frac12gt^2,\\
v_x(t)&=v_0\cos\theta,\\
v_y(t)&=v_0\sin\theta-gt.
\end{aligned}
$$

At the top of the trajectory, $v_y=0$ but $v_x$ remains unchanged, so the projectile is not momentarily at rest unless it was launched vertically. The time to the apex is

$$
t_{top}=\frac{v_0\sin\theta}{g},
$$

and the height gained above launch is

$$
\Delta y_{max}=\frac{v_0^2\sin^2\theta}{2g}.
$$

Eliminating time gives the path itself. From $t=(x-x_0)/(v_0\cos\theta)$,

$$
y-y_0=(x-x_0)\tan\theta
-\frac{g(x-x_0)^2}{2v_0^2\cos^2\theta}.
$$

The negative quadratic coefficient identifies a parabola. This result depends on uniform vertical acceleration and zero horizontal acceleration; aerodynamic drag destroys the exact parabolic form.

## Equal-height range and its restricted optimum

When the projectile lands at its launch elevation, set $y-y_0=0$:

$$
0=t\left(v_0\sin\theta-\frac12gt\right).
$$

The root $t=0$ represents launch. The later root gives the flight time

$$
T=\frac{2v_0\sin\theta}{g}.
$$

Multiplying by the constant horizontal velocity gives

$$
R=v_0\cos\theta\,T
=\frac{v_0^2\sin2\theta}{g}.
$$

For fixed $v_0$ and equal launch and landing heights, $\sin2\theta$ is largest at $2\theta=90^\circ$, so the range is maximal at $45^\circ$. Complementary angles, such as $30^\circ$ and $60^\circ$, have the same ideal range. Neither statement survives unchanged when launch height, drag, or terrain geometry changes.

### Worked example: launch and landing at the same height

A ball is launched at $20.0\,\mathrm{m/s}$ and $35.0^\circ$ above horizontal. Find the time of flight, maximum height, and range using $g=9.81\,\mathrm{m/s^2}$.

Resolve the initial velocity:

$$
v_{0x}=20.0\cos35.0^\circ=16.38\,\mathrm{m/s},
$$

$$
v_{0y}=20.0\sin35.0^\circ=11.47\,\mathrm{m/s}.
$$

The nonzero landing-time root is

$$
T=\frac{2v_{0y}}{g}
=\frac{2(11.47)}{9.81}
=2.34\,\mathrm s.
$$

The height above launch at the apex is

$$
\Delta y_{max}=\frac{v_{0y}^2}{2g}
=\frac{(11.47)^2}{2(9.81)}
=6.71\,\mathrm m.
$$

Finally,

$$
R=v_{0x}T=(16.38)(2.34)=38.3\,\mathrm m.
$$

As a check, the compact range formula gives $20.0^2\sin70^\circ/9.81=38.3\,\mathrm m$.

## Landing at another elevation

If the final elevation differs by $\Delta y=y_f-y_0$, the vertical condition is

$$
\Delta y=v_0\sin\theta\,t-\frac12gt^2.
$$

Rearranging and applying the quadratic formula gives

$$
t=\frac{v_0\sin\theta
\pm\sqrt{v_0^2\sin^2\theta-2g\Delta y}}{g}.
$$

Only roots that are real, nonnegative, and compatible with the physical interval are retained. Two positive roots can occur when the projectile crosses a chosen height once while rising and once while falling. A negative discriminant means that height cannot be reached with the specified launch.

### Worked example: horizontal launch from a cliff

A stone leaves a $45.0\,\mathrm m$ cliff horizontally at $12.0\,\mathrm{m/s}$. Find the impact time, horizontal distance, and impact speed.

Set the launch point to $y_0=0$, so the ground is $y=-45.0\,\mathrm m$. Since $v_{0y}=0$,

$$
-45.0=-\frac12(9.81)t^2.
$$

Thus

$$
t=\sqrt{\frac{2(45.0)}{9.81}}=3.03\,\mathrm s.
$$

Horizontal displacement is

$$
x=(12.0)(3.03)=36.4\,\mathrm m.
$$

At impact,

$$
v_x=12.0\,\mathrm{m/s},
\qquad
v_y=-gt=-(9.81)(3.03)=-29.7\,\mathrm{m/s}.
$$

The speed is the magnitude of the velocity vector:

$$
v=\sqrt{v_x^2+v_y^2}
=\sqrt{12.0^2+29.7^2}
=32.0\,\mathrm{m/s}.
$$

The vertical fall time does not depend on the horizontal launch speed under the ideal model.

## Tangential and normal acceleration along a curve

At any smooth point on a path, define unit vector $\mathbf e_t$ tangent to the motion and $\mathbf e_n$ toward the local center of curvature. Then

$$
\mathbf v=v\mathbf e_t
$$

and

$$
\mathbf a=\frac{dv}{dt}\mathbf e_t+\frac{v^2}{\rho}\mathbf e_n,
$$

where $\rho$ is the local radius of curvature. The tangential component changes speed; the normal component turns the velocity vector. A straight path has $\rho\to\infty$ and therefore no normal acceleration.

For a circle of fixed radius $r$,

$$
a_n=\frac{v^2}{r}=\omega^2r,
\qquad
v=r\omega.
$$

Uniform circular motion means constant speed, so $a_t=0$, while $a_n$ remains directed inward. “Centripetal” describes this inward net acceleration or the required inward resultant force. It is not an extra force to add to gravity, tension, friction, or a normal force.

For nonuniform circular motion,

$$
a_t=r\alpha,
$$

and the total acceleration magnitude is

$$
a=\sqrt{(r\alpha)^2+(r\omega^2)^2}.
$$

The period and frequency satisfy

$$
T=\frac{2\pi r}{v}=\frac{2\pi}{\omega},
\qquad f=\frac1T.
$$

Angular speed in these equations must be in radians per second.

### Worked example: turntable kinematics

A point $0.150\,\mathrm m$ from a turntable's center rotates at $45.0\,\mathrm{rpm}$. Find its speed and inward acceleration.

Convert the rotation rate:

$$
\omega=45.0\frac{\mathrm{rev}}{\mathrm{min}}
\frac{2\pi\,\mathrm{rad}}{1\,\mathrm{rev}}
\frac{1\,\mathrm{min}}{60\,\mathrm s}
=4.71\,\mathrm{rad/s}.
$$

Then

$$
v=r\omega=(0.150)(4.71)=0.707\,\mathrm{m/s},
$$

and

$$
a_n=r\omega^2=(0.150)(4.71)^2=3.33\,\mathrm{m/s^2}.
$$

The acceleration direction changes with the point's location, even though its magnitude remains constant.

## Forces that maintain circular motion

Newton's second law in tangential-normal components reads

$$
\sum F_t=m\frac{dv}{dt},
\qquad
\sum F_n=m\frac{v^2}{r}.
$$

On a level road, static friction may supply the inward force for a turning car. With maximum friction $\mu_smg$,

$$
\frac{mv^2}{r}\le\mu_smg,
$$

so

$$
v\le\sqrt{\mu_sgr}.
$$

On an ideally banked frictionless curve of angle $\beta$, the normal force has vertical and horizontal components:

$$
N\cos\beta=mg,
\qquad
N\sin\beta=\frac{mv^2}{r}.
$$

Dividing eliminates $N$ and $m$:

$$
\tan\beta=\frac{v^2}{rg}.
$$

This is a design speed, not a universal safe speed. At other speeds friction generally participates, and real roads impose additional limits.

## Relative velocity in a plane

Many two-dimensional problems concern motion as seen from another moving object. If $A$ and $B$ are observed from the same inertial frame,

$$
\mathbf v_{A/B}=\mathbf v_A-\mathbf v_B.
$$

Rearranging gives $\mathbf v_A=\mathbf v_{A/B}+\mathbf v_B$. The vectors must be added by components; their speeds cannot normally be added as scalars. The same relation describes a boat relative to water and shore, an aircraft relative to air and ground, or rain relative to a moving car.

**Problem.** A river flows east at $3.0\,\mathrm{m/s}$. A boat can move at $5.0\,\mathrm{m/s}$ relative to the water. The river is $120$ m wide north-south. Find the heading needed to land directly north of the start, and the crossing time.

To cancel the current, the boat needs a westward relative-water component of $3.0\,\mathrm{m/s}$. If $\theta$ is the angle west of north,

$$
5.0\sin\theta=3.0,
$$

so

$$
\theta=\sin^{-1}(0.600)=36.9^\circ.
$$

The northward component is

$$
v_N=5.0\cos36.9^\circ=4.0\,\mathrm{m/s}.
$$

The ground velocity has zero east-west component and northward magnitude $4.0\,\mathrm{m/s}$. Therefore

$$
t=\frac{120}{4.0}=30\,\mathrm s.
$$

Heading straight north would cross faster, in $24$ s, but the boat would drift $72$ m east. “Shortest time” and “arrive directly opposite” impose different conditions.

Relative acceleration follows the same subtraction rule in translating inertial frames. If the reference frame accelerates or rotates, additional apparent terms enter. Treating a rotating platform as an ordinary inertial frame misses centrifugal and Coriolis effects.

## Polar coordinates for changing radius and angle

Circular motion holds radius fixed, but many planar paths are more naturally described by $r(t)$ and $\theta(t)$. The polar unit vectors rotate with the particle. Differentiating the position $\mathbf r=r\mathbf e_r$ gives

$$
\mathbf v=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta,
$$

and a second derivative gives

$$
\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r
+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta.
$$

The radial velocity $\dot r$ changes distance from the origin; the transverse term $r\dot\theta$ sweeps around it. Even with constant $r$ and constant $\dot\theta$, radial acceleration remains $-r\dot\theta^2$. If $r$ changes while the line rotates, the $2\dot r\dot\theta$ term contributes transverse acceleration.

Consider a bead sliding outward in a straight slot that rotates at constant $\omega=2.0\,\mathrm{rad/s}$. At an instant, $r=0.40$ m, $\dot r=0.30\,\mathrm{m/s}$, and $\ddot r=0$. Since $\ddot\theta=0$,

$$
a_r=-r\omega^2=-(0.40)(2.0)^2=-1.60\,\mathrm{m/s^2},
$$

$$
a_\theta=2\dot r\omega=2(0.30)(2.0)=1.20\,\mathrm{m/s^2}.
$$

The acceleration magnitude is

$$
a=\sqrt{1.60^2+1.20^2}=2.00\,\mathrm{m/s^2}.
$$

Calling the motion “constant angular speed” would not remove either component.

## What air resistance changes

The vacuum projectile model has constant horizontal velocity, symmetric ascent and descent between equal heights, and a parabolic path. A drag force opposes the velocity, so its components evolve as the velocity direction changes. Horizontal and vertical equations become coupled differential equations.

At low speed in a viscous regime, drag may be approximately proportional to speed. For many ordinary projectiles in air, a quadratic model is closer:

$$
\mathbf F_D=-\frac12\rho C_DA|\mathbf v|\mathbf v.
$$

Here $\rho$ is air density, $C_D$ a shape-dependent drag coefficient, and $A$ reference area. No constant-acceleration shortcut solves the full trajectory. Numerical integration advances velocity and position in small time steps.

Qualitatively, drag reduces range and maximum height. For an equal-height shot it makes descent steeper than ascent and shifts the range-maximizing launch angle below $45^\circ$ in many conditions. The exact optimum depends on speed, size, mass, shape, spin, and atmospheric properties, so there is no universal corrected angle.

Spin introduces a lift-like Magnus force that can curve the trajectory sideways or change vertical motion. Wind is best handled first as a relative-velocity problem: aerodynamic force depends on projectile velocity relative to air, not ground. These effects matter for balls and long trajectories but are intentionally excluded from elementary component equations.

## Geometry checks at limiting cases

Limiting cases expose algebra errors quickly. A launch angle of zero gives zero initial vertical velocity; for equal launch and landing height in the ideal model, the nonzero flight time collapses to zero. A launch angle approaching $90^\circ$ gives zero horizontal range. The equal-height range expression is symmetric under $\theta\to90^\circ-\theta$ because $\sin2\theta$ is unchanged.

For circular motion, letting radius grow without bound at fixed speed makes $v^2/r$ approach zero, recovering straight-line motion locally. At fixed angular speed, however, $a_n=\omega^2r$ grows with radius because tangential speed also grows. Holding $v$ fixed and holding $\omega$ fixed describe different comparisons.

## Intercept and closest-approach problems

To decide whether one moving object meets another, equate their position vectors at the same time. Let a target begin at $\mathbf r_{T0}$ with constant velocity $\mathbf v_T$, and an interceptor begin at $\mathbf r_{I0}$ with fixed speed $u$ but selectable direction. Interception requires

$$
\mathbf r_{I0}+\mathbf v_It
=\mathbf r_{T0}+\mathbf v_Tt,
$$

with $\vert \mathbf v_I\vert =u$. Rearranging gives

$$
\mathbf v_I=\frac{\mathbf r_{T0}-\mathbf r_{I0}}{t}+\mathbf v_T.
$$

Taking the magnitude produces an equation for positive encounter time. Aiming at the target's initial location generally misses because the target moves while the interceptor travels.

The existence of a solution depends on geometry and relative speed. An interceptor slower than a fleeing target may still meet it if initially ahead or if paths cross, but it cannot catch a target receding along the same line from behind. A quadratic time equation may yield two positive encounters, one tangent encounter, or no real encounter. Roots need geometric interpretation.

Closest approach uses the relative position

$$
\mathbf r_{A/B}(t)=\mathbf r_{A/B}(0)+\mathbf v_{A/B}t.
$$

Minimizing its squared magnitude gives

$$
t_*=-\frac{\mathbf r_{A/B}(0)\cdot\mathbf v_{A/B}}
{|\mathbf v_{A/B}|^2},
$$

when relative velocity is nonzero. A negative value means the closest approach under constant velocities occurred in the past, so future separation is already increasing.

## Assumptions to inspect before using a compact formula

## Choosing coordinates without changing the physics

Coordinate axes are bookkeeping choices. Rotating them changes vector components but not the physical trajectory, speed, or acceleration magnitude. Horizontal-vertical axes are efficient for uniform gravity because one acceleration component vanishes. Tangential-normal axes are efficient when path geometry and speed are known. Polar axes are efficient when forces or constraints point toward a center.

A poor coordinate choice is not wrong, but it creates extra projections and sign opportunities. On a banked curve, horizontal-vertical axes expose weight balance and inward acceleration. On a bead constrained to a known curved track, tangential-normal axes separate speed change from contact-force calculation. Mixing force components from one basis with acceleration components from another is wrong unless an explicit projection connects them.

Unit vectors also behave differently by basis. Cartesian unit vectors remain fixed, which is why component differentiation is direct. Tangential-normal and polar unit vectors rotate along the motion, producing curvature and angular-rate terms. Omitting those derivatives is equivalent to pretending a moving basis remains fixed.

Dimensional checks remain useful across every basis. Position components have units of length, velocity components length per time, and acceleration components length per time squared. Angles in derivatives are measured in radians, so angular velocity can combine with radius without an extra conversion factor. A result for range should not retain time, and a centripetal acceleration should scale as speed squared divided by length.

Finally, signs belong to components rather than magnitudes. A negative vertical velocity means downward motion under an upward-positive convention. Speed, radius of curvature, flight duration, and traveled distance remain nonnegative. Keeping that distinction prevents a negative component from being discarded merely because it looks unfamiliar.

- The equal-height flight-time and range formulas require identical launch and landing elevations. Use the vertical landing equation otherwise.
- At an apex, only the vertical velocity component vanishes. Acceleration remains $-g\mathbf j$.
- Components share one time variable. Solving separate horizontal and vertical times and then combining them has no physical basis.
- A negative velocity component indicates direction; a negative speed is not meaningful.
- Uniform circular motion has zero tangential acceleration, not zero total acceleration.
- Convert revolutions to radians before using $v=r\omega$ or $a_n=r\omega^2$.
- Air resistance depends on velocity and couples horizontal and vertical motion. Long-range, light, or fast projectiles can depart strongly from the vacuum model.
- The inward force is the sum of actual force components. Do not draw an additional “centripetal force” on the free-body diagram.

<div className="see-also">

See also: [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics) · [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications) · [Rotation, Torque, and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum) · [Particle Kinematics](/physics/mechanics/particle-kinematics)

</div>
