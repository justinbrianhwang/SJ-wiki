---
title: Rotation, Torque, and Angular Momentum
sidebar_position: 8
---

# Rotation, Torque, and Angular Momentum

Rotational mechanics looks like linear mechanics after replacing position by angle, force by torque, and mass by moment of inertia. The analogy is useful, but it has limits. Mass is an intrinsic property; moment of inertia also depends on the chosen axis. A force has a definite direction; its torque depends on both the axis and the point where the force acts. Angular velocity points along an axis even though the material points move tangent to circles.

Most introductory problems concern a rigid body rotating about a fixed axis. That model covers wheels, pulleys, flywheels, and rolling objects. More general three-dimensional rotation needs tensor moments of inertia and allows angular momentum to point in a different direction from angular velocity.

## Angle as a kinematic coordinate

For rotation about a fixed axis, angular position $\theta$ locates the body relative to a reference orientation. Angular velocity and angular acceleration are

$$
\omega=\frac{d\theta}{dt},\qquad
\alpha=\frac{d\omega}{dt}=\frac{d^2\theta}{dt^2}.
$$

Radians are dimensionless ratios of arc length to radius. They must be used in

$$
s=r\theta,\qquad v_t=r\omega,\qquad a_t=r\alpha,
$$

because these relations follow by differentiating $s=r\theta$. Degrees introduce an extra conversion factor. A point at distance $r$ from the axis also has inward normal acceleration

$$
a_n=\frac{v_t^2}{r}=r\omega^2.
$$

Thus a point on a steadily turning wheel has $\alpha=0$ and $a_t=0$, but it does not have zero acceleration. Its velocity direction changes continuously.

When $\alpha$ is constant, integration gives

$$
\begin{aligned}
\omega&=\omega_0+\alpha t,\\
\theta-\theta_0&=\omega_0t+\frac12\alpha t^2,\\
\omega^2&=\omega_0^2+2\alpha(\theta-\theta_0).
\end{aligned}
$$

The last equation follows by writing $\alpha=d\omega/dt=(d\omega/d\theta)(d\theta/dt)=\omega\,d\omega/d\theta$ and integrating. It is useful when time is not requested.

### Worked example: speeding up and then coasting

A wheel starts from rest, turns with constant angular acceleration $3.0\,\mathrm{rad/s^2}$ for $4.0\,\mathrm{s}$, and then coasts at constant angular speed for another $6.0\,\mathrm{s}$. Find its final angular speed and total number of revolutions.

During the accelerated interval,

$$
\omega_1=0+(3.0)(4.0)=12\,\mathrm{rad/s},
$$

and

$$
\Delta\theta_1=\frac12(3.0)(4.0)^2=24\,\mathrm{rad}.
$$

During coasting, $\alpha=0$, so

$$
\Delta\theta_2=\omega_1\Delta t=(12)(6.0)=72\,\mathrm{rad}.
$$

The total angle is $96\,\mathrm{rad}$. Since one revolution is $2\pi$ radians,

$$
N=\frac{96}{2\pi}=15.3\ \text{revolutions}.
$$

The final angular speed remains $12\,\mathrm{rad/s}$. Treating the whole ten seconds as one constant-acceleration interval would incorrectly continue the acceleration through the coasting stage.

## Torque measures the turning action of force

The torque of a force about an origin $O$ is

$$
\boldsymbol{\tau}_O=\mathbf r\times\mathbf F,
$$

where $\mathbf r$ runs from $O$ to the force's point of application. Its magnitude is

$$
\tau=rF\sin\phi=F\ell,
$$

with $\phi$ the angle between $\mathbf r$ and $\mathbf F$, and $\ell$ the perpendicular distance from the axis to the force's line of action. Only the component perpendicular to $\mathbf r$ produces torque. A radial force has zero torque about the center even when its magnitude is large.

The fixed-axis rotational equation

$$
\sum\tau=I\alpha
$$

can be derived from Newton's second law. For a point mass $m_i$ at radius $r_i$, the tangential force is $F_{t,i}=m_i a_{t,i}=m_i r_i\alpha$. Multiplication by $r_i$ gives $\tau_i=m_i r_i^2\alpha$. Summing all particles of a rigid body yields

$$
\sum\tau=\left(\sum_i m_i r_i^2\right)\alpha=I\alpha.
$$

Internal forces cancel in the total under the usual rigid-body assumptions. Static rotational equilibrium is the special case $\alpha=0$, and it must be combined with translational equilibrium:

$$
\sum\mathbf F=\mathbf 0,\qquad \sum\boldsymbol\tau_O=\mathbf 0.
$$

## Why mass distribution enters through $I$

For discrete masses,

$$
I=\sum_i m_i r_i^2,
$$

and for a continuous body,

$$
I=\int r_\perp^2\,dm.
$$

The squared radius heavily weights material far from the axis. A thin hoop and a solid disk with the same mass and radius have

$$
I_{\text{hoop}}=MR^2,\qquad I_{\text{disk}}=\frac12MR^2.
$$

The hoop is harder to spin up because all its mass lies at the largest radius. Other common results include $I=\frac25MR^2$ for a solid sphere about a diameter and $I=\frac1{12}ML^2$ for a thin rod about its center perpendicular to the rod.

If an axis is parallel to an axis through the center of mass and displaced by distance $d$, the parallel-axis theorem gives

$$
I=I_{cm}+Md^2.
$$

It follows by expanding the squared distance from the shifted axis; the cross term integrates to zero because coordinates measured from the center of mass have zero mass-weighted mean. The theorem does not apply between nonparallel axes.

Rotational kinetic energy follows by summing the translational kinetic energy of all mass elements:

$$
K=\sum_i\frac12m_i(r_i\omega)^2
=\frac12I\omega^2.
$$

The expression assumes every point shares the same angular velocity, as a rigid body does.

| Linear description | Fixed-axis rotational description | Qualification |
|---|---|---|
| $x$, $v$, $a$ | $\theta$, $\omega$, $\alpha$ | radians connect the two |
| mass $m$ | moment of inertia $I$ | depends on axis |
| force $F$ | torque $\tau$ | depends on origin |
| momentum $p=mv$ | $L=I\omega$ | simple form needs a principal fixed axis |
| $K=\frac12mv^2$ | $K=\frac12I\omega^2$ | add both terms for rolling |

## Angular momentum and angular impulse

For a particle,

$$
\mathbf L_O=\mathbf r\times\mathbf p.
$$

Differentiating about a fixed inertial origin gives

$$
\frac{d\mathbf L_O}{dt}
=\frac{d\mathbf r}{dt}\times m\mathbf v+\mathbf r\times\frac{d\mathbf p}{dt}
=\mathbf v\times m\mathbf v+\mathbf r\times\mathbf F
=\boldsymbol\tau_O.
$$

For a system of particles,

$$
\sum\boldsymbol\tau_{O,ext}=\frac{d\mathbf L_O}{dt}.
$$

Integrating over a time interval gives

$$
\int_{t_1}^{t_2}\sum\boldsymbol\tau_{O,ext}\,dt
=\mathbf L_{O,2}-\mathbf L_{O,1}.
$$

If the external torque about $O$ is zero, angular momentum about $O$ is constant. Zero external force is not required. For example, the tension on a mass moving in a circle exerts no torque about the center because it is radial.

### Worked example: pulling masses inward

Two small $2.0\,\mathrm{kg}$ masses are attached to a light horizontal rotating assembly, each initially $0.50\,\mathrm{m}$ from the axis. The assembly rotates at $3.0\,\mathrm{rad/s}$. The masses are pulled to $0.20\,\mathrm{m}$ while external torque about the axis is negligible. Find the new angular speed and the change in kinetic energy.

The initial and final moments of inertia are

$$
I_1=2m r_1^2=2(2.0)(0.50)^2=1.00\,\mathrm{kg\,m^2},
$$

$$
I_2=2m r_2^2=2(2.0)(0.20)^2=0.160\,\mathrm{kg\,m^2}.
$$

Angular momentum conservation gives

$$
I_1\omega_1=I_2\omega_2,
$$

so

$$
\omega_2=\frac{I_1}{I_2}\omega_1
=\frac{1.00}{0.160}(3.0)
=18.75\,\mathrm{rad/s}.
$$

The kinetic energies are

$$
K_1=\frac12(1.00)(3.0)^2=4.50\,\mathrm{J},
$$

$$
K_2=\frac12(0.160)(18.75)^2=28.1\,\mathrm{J}.
$$

Angular momentum is conserved, but kinetic energy increases by $23.6\,\mathrm{J}$. The inward pull does positive work while the masses move radially. Conservation of angular momentum never implied conservation of mechanical energy.

## Rolling ties translation to rotation

For a rigid wheel rolling without slipping on a stationary surface, the point of contact is instantaneously at rest. The geometric constraint is

$$
v_{cm}=R\omega,\qquad a_{cm,t}=R\alpha.
$$

It does not imply that the center is at rest, and it fails once the contact slides. The kinetic energy is

$$
K=\frac12Mv_{cm}^2+\frac12I_{cm}\omega^2.
$$

Consider an object released from rest and rolling down through height $h$. If static friction does no net work and deformation losses are negligible,

$$
Mgh=\frac12Mv^2+\frac12I_{cm}\frac{v^2}{R^2}.
$$

Writing $I_{cm}=\beta MR^2$ gives

$$
v=\sqrt{\frac{2gh}{1+\beta}}.
$$

A hoop has $\beta=1$, a solid cylinder $\beta=1/2$, and a solid sphere $\beta=2/5$. The sphere reaches the bottom fastest among these because less of the available energy goes into rotation for the same center-of-mass speed.

### Worked example: solid cylinder on a ramp

A solid cylinder rolls from rest down through $h=1.2\,\mathrm{m}$. With $I_{cm}=\frac12MR^2$,

$$
Mgh=\frac12Mv^2+\frac12\left(\frac12MR^2\right)\left(\frac vR\right)^2
=\frac34Mv^2.
$$

After canceling $M$,

$$
v=\sqrt{\frac{4gh}{3}}
=\sqrt{\frac{4(9.81)(1.2)}{3}}
=3.96\,\mathrm{m/s}.
$$

The radius cancels because both $I$ and the rolling constraint contain $R^2$. A larger cylinder of the same shape is not faster merely because it is larger.

## Rotational work, power, and braking

If a torque acts through an angular displacement, its work is

$$
W=\int_{\theta_1}^{\theta_2}\tau\,d\theta.
$$

For constant torque this reduces to $W=\tau\Delta\theta$. Differentiating with respect to time gives rotational power:

$$
P=\tau\omega.
$$

The scalar form assumes torque and angular velocity lie along the same fixed axis; the general expression is $P=\boldsymbol\tau\cdot\boldsymbol\omega$. Positive power adds rotational kinetic energy, while a braking torque gives negative power.

The rotational work-energy theorem follows from $\tau=I\alpha$ when $I$ is constant. Since $\alpha=\omega,d\omega/d\theta$,

$$
\tau\,d\theta=I\omega\,d\omega.
$$

Integration produces

$$
W_{net}=\frac12I\omega_2^2-\frac12I\omega_1^2.
$$

This route is often shorter than solving for angular acceleration and time. It also handles a torque that varies with angle, such as the torque from gravity on a pendulum-like rigid body.

Suppose a flywheel with $I=8.0\,\mathrm{kg\,m^2}$ rotates at $20\,\mathrm{rad/s}$ and is stopped by a constant opposing torque of $16\,\mathrm{N\,m}$. Its initial energy is

$$
K_i=\frac12(8.0)(20)^2=1600\,\mathrm J.
$$

If $\Delta\theta$ is the positive angle turned before stopping, the brake work is $-16\Delta\theta$. Hence

$$
1600-16\Delta\theta=0,
$$

so $\Delta\theta=100\,\mathrm{rad}$, or $15.9$ revolutions. The constant angular deceleration is $-2.0\,\mathrm{rad/s^2}$, which independently gives a stopping time of $10\,\mathrm s$. Energy finds the stopping angle without first finding time.

## Center of mass motion remains separate

A body's rotation does not replace the translation of its center of mass. For any rigid body,

$$
\sum\mathbf F_{ext}=M\mathbf a_{cm}.
$$

Moments about the center of mass govern the rotation. In planar motion,

$$
\sum\tau_{cm}=I_{cm}\alpha.
$$

Together these equations describe objects that translate and rotate at once. Taking moments about some other accelerating point may require extra terms, so the center of mass or a fixed inertial point is normally the clean choice.

An off-center impulse illustrates the separation. A brief force applied through the center of mass changes linear momentum but produces no angular impulse about that center. The same impulse applied away from the center produces the same change in linear momentum and also changes angular momentum. A cue ball struck through its center initially slides without spin; an offset strike gives it both translation and rotation.

Rolling adds a constraint between these otherwise separate motions. Static friction supplies whatever torque is needed to satisfy that constraint within its limit. For a body descending an incline, the gravitational force acts through the center of mass and has no torque about it, while static friction at the contact provides the torque that increases spin. The same friction points uphill even though the body accelerates downhill.

## What changes in three dimensions

Finite rotations about different axes do not commute. Rotating a book $90^\circ$ about one axis and then another generally produces a different orientation from performing the same rotations in reverse order. Infinitesimal rotations can be represented by vectors because products of small angles are negligible; finite orientation needs a rotation matrix, quaternion, or another ordered description.

Moment of inertia is likewise directional. In three dimensions it is a tensor relating angular momentum and angular velocity:

$$
\mathbf L=\mathbf I\boldsymbol\omega.
$$

Only along a principal axis are the vectors guaranteed parallel. A freely rotating asymmetric body can therefore have constant angular momentum in inertial space while its angular velocity and body axes change direction. Introductory fixed-axis formulas suppress this behavior by choosing a principal axis held fixed by bearings.

Gyroscopic precession follows from the vector torque law rather than from a mysterious extra force. When a rapidly spinning wheel is supported at one end, gravity exerts a torque roughly perpendicular to its spin angular momentum. A perpendicular torque changes the direction of $\mathbf L$ more strongly than its magnitude, causing the axle to precess. The simple steady-precession estimate depends on fast spin and small nutation; a slowly spinning wheel can tip instead.

The axis qualification also matters for conservation statements. Angular momentum about a fixed inertial origin is conserved when net external torque about that origin vanishes. About a moving origin, especially an accelerating one, additional terms can enter. The center of mass is a useful moving origin because the total linear momentum term simplifies, but its conditions should still be stated.

Rotational balance also explains why dynamic balancing matters in machinery. A rotor whose center of mass is displaced from its bearing axis requires an inward force that grows as the square of angular speed. Bearings then feel a rotating load even if angular speed is steady. Placing counterweights can move the center of mass onto the axis, but a long rotor may still have a couple imbalance if different axial planes are unbalanced in opposite directions. Static balance and dynamic balance are therefore different tests.

Real bodies also have finite strength. Increasing angular speed raises internal stresses needed to hold distant material on circular paths. The rigid-body model assumes those deformations are negligible; it does not predict burst speed. Flywheels, turbines, and centrifuges require stress analysis in addition to torque and energy calculations.

## Checks that prevent the usual errors

- State the axis before calculating torque, $I$, or angular momentum. Quantities computed about different axes cannot be combined.
- A tabulated moment of inertia is tied to a particular axis. Use the parallel-axis theorem only for a parallel displacement.
- Degrees are acceptable for reporting angles, but angular kinematics and $s=r\theta$ require radians.
- Constant angular speed still produces radial acceleration of every off-axis point.
- The relation $L=I\omega$ is safe for fixed-axis rotation about a principal axis. The vector relation is more subtle in general three-dimensional motion.
- Static friction in pure rolling need not equal $\mu_sN$; it takes the value required to prevent slip, up to that limit.
- Angular momentum conservation and energy conservation are separate claims. Internal work can change kinetic energy while leaving total angular momentum fixed.

<div className="see-also">

See also: [Two-Dimensional Motion](/physics/general/two-dimensional-motion) · [Equilibrium and Elasticity](/physics/general/equilibrium-and-elasticity) · [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions)

</div>
