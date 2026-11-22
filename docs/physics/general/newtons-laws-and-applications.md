---
title: "Newton's Laws and Applications"
sidebar_position: 5
---

# Newton's Laws and Applications

Newton's laws turn an interaction model into a prediction of acceleration. The recurring work is to choose the body or system, identify external forces, choose useful axes, and apply any geometric constraints. Most mistakes occur before the algebra: a force is omitted, a third-law partner is drawn on the wrong body, or friction is assigned its maximum value without checking whether slipping begins.

## What the three laws say

Newton's first law defines inertial frames. In such a frame, an object with zero net external force has constant velocity:

$$
\sum\vec F=0
\quad\Longrightarrow\quad
\vec v=\text{constant}.
$$

Rest is only one constant-velocity state. A puck gliding in a straight line at steady speed needs no net force to maintain its motion.

Newton's second law in its general momentum form is

$$
\sum\vec F_{ext}=\frac{d\vec p}{dt}.
$$

For constant mass it becomes

$$
\sum\vec F=m\vec a.
$$

This is a vector relation, normally written by components:

$$
\sum F_x=ma_x,
\qquad
\sum F_y=ma_y.
$$

Newton's third law says that if body A exerts a force on body B, body B simultaneously exerts an equal and opposite force on A:

$$
\vec F_{A\to B}=-\vec F_{B\to A}.
$$

The two forces act on different bodies, so they do not cancel on either body's free-body diagram. They cancel as internal forces only when A and B are treated as one system.

The laws are an excellent approximation for ordinary speeds and weak gravitational fields. At relativistic speeds, momentum retains the second-law structure but is no longer $m\vec v$. At atomic scales, quantum mechanics replaces definite trajectories.

## How to build a free-body diagram

A free-body diagram isolates one body or a clearly named system. Draw forces exerted on it by objects outside the boundary:

- Weight $m\vec g$ points toward Earth near the surface.
- A normal force is perpendicular to a contact surface.
- Tension pulls along a string away from the attached body.
- Friction opposes actual or impending relative sliding between surfaces.
- Drag opposes velocity relative to the fluid.
- A spring force opposes displacement from equilibrium in the ideal Hooke model.

Velocity and acceleration are not forces. Neither is “centripetal force”; that phrase names the inward net-force requirement for circular motion.

Axes should fit the geometry. On an incline at angle $\theta$, choose one axis along the plane and one perpendicular to it. Weight then has components

$$
mg\sin\theta
$$

down the plane and

$$
mg\cos\theta
$$

into the plane. The normal force follows from the perpendicular equation; it is not automatically $mg$.

## Worked incline with kinetic friction

A $5.0\,\mathrm{kg}$ block slides down a $30^\circ$ incline with coefficient of kinetic friction $\mu_k=0.20$. Find its acceleration.

Take downhill as positive. There is no acceleration perpendicular to the surface:

$$
N-mg\cos30^\circ=0,
$$

so

$$
N=(5.0)(9.8)\cos30^\circ=42.4\,\mathrm N.
$$

Kinetic friction points uphill because the block slides downhill:

$$
f_k=\mu_kN=(0.20)(42.4)=8.49\,\mathrm N.
$$

The downhill component of weight is

$$
mg\sin30^\circ=(5.0)(9.8)(0.500)=24.5\,\mathrm N.
$$

Newton's second law along the plane gives

$$
mg\sin30^\circ-f_k=ma.
$$

Therefore

$$
a=\frac{24.5-8.49}{5.0}
=3.20\,\mathrm{m/s^2}.
$$

The value lies between zero and the frictionless result $g\sin30^\circ=4.9\,\mathrm{m/s^2}$.

## Static friction chooses its value

Static friction obeys

$$
\lvert f_s\rvert\le\mu_sN.
$$

The equality holds only at impending slip. If a $20\,\mathrm{kg}$ crate on a horizontal floor has $\mu_s=0.50$, its maximum static friction is

$$
f_{s,\max}=(0.50)(20)(9.8)=98\,\mathrm N.
$$

An $80\,\mathrm N$ horizontal pull produces $f_s=80\,\mathrm N$ in the opposite direction and the crate remains at rest. Friction does not jump to $98\,\mathrm N$.

If the pull increases to $120\,\mathrm N$ and $\mu_k=0.35$, the crate slides. Then

$$
f_k=(0.35)(196)=68.6\,\mathrm N
$$

and

$$
a=\frac{120-68.6}{20}=2.57\,\mathrm{m/s^2}.
$$

An angled pull changes the normal force. If force $P$ acts upward at angle $\alpha$ above horizontal and vertical acceleration is zero,

$$
N=mg-P\sin\alpha.
$$

The upward component reduces both $N$ and the friction limit. Pushing downward at the same angle increases them.

On an incline, a stationary block needs friction $mg\sin\theta$. It remains at rest only if

$$
mg\sin\theta\le\mu_smg\cos\theta,
$$

or

$$
\tan\theta\le\mu_s.
$$

This inequality determines whether slipping occurs before any kinetic-friction equation is used.

## Ideal strings, pulleys, and coupled motion

An ideal string is massless and inextensible. A massless string over a massless frictionless pulley has one tension magnitude throughout, and its fixed length constrains attached bodies to equal acceleration magnitudes. These statements are model assumptions, not universal facts.

For an Atwood machine with $m_1=2.0\,\mathrm{kg}$ and $m_2=3.0\,\mathrm{kg}$, let $m_2$ move down and $m_1$ move up:

$$
T-m_1g=m_1a,
$$

$$
m_2g-T=m_2a.
$$

Adding eliminates tension:

$$
(m_2-m_1)g=(m_1+m_2)a.
$$

Thus

$$
a=\frac{m_2-m_1}{m_1+m_2}g
=\frac{1.0}{5.0}(9.8)
=1.96\,\mathrm{m/s^2}.
$$

Substitute into the first equation:

$$
T=m_1(g+a)
=(2.0)(9.8+1.96)
=23.5\,\mathrm N.
$$

The acceleration approaches zero as the masses approach equality and remains below $g$. The tension lies between the two weights. If the pulley has rotational inertia, a torque is needed to accelerate it and the tensions on its two sides differ. If the string has mass, tension can vary along its length.

## Apparent weight in an elevator

A scale reads the normal force. For a person of mass $m$ in an elevator, choose upward as positive:

$$
N-mg=ma.
$$

Therefore

$$
N=m(g+a).
$$

Upward acceleration increases the reading; downward acceleration decreases it. Velocity direction does not determine apparent weight. An elevator moving downward while slowing has upward acceleration and a reading larger than $mg$.

For a $70\,\mathrm{kg}$ passenger accelerating downward at $2.0\,\mathrm{m/s^2}$, $a=-2.0\,\mathrm{m/s^2}$:

$$
N=(70)(9.8-2.0)=546\,\mathrm N.
$$

In free fall, $a=-g$ and $N=0$. Gravity is still acting; the person and elevator share the same acceleration, leaving no support force.

## Circular motion is a radial equation

Motion at speed $v$ along a circle of radius $r$ has inward acceleration

$$
a_r=\frac{v^2}{r}.
$$

The actual inward force components must satisfy

$$
\sum F_r=\frac{mv^2}{r}.
$$

For a car on a flat curve, static friction may supply this net inward force:

$$
f_s=\frac{mv^2}{r}.
$$

Since $f_s\le\mu_smg$, the maximum speed before slipping is

$$
v_{\max}=\sqrt{\mu_sgr}.
$$

Take $\mu_s=0.60$ and $r=50\,\mathrm m$:

$$
v_{\max}=\sqrt{(0.60)(9.8)(50)}
=17.1\,\mathrm{m/s}.
$$

The friction points toward the circle's center, not opposite the car's forward velocity. It prevents sideways slipping.

On a frictionless banked curve, resolve the normal force:

$$
N\cos\theta=mg,
\qquad
N\sin\theta=\frac{mv^2}{r}.
$$

Dividing gives

$$
\tan\theta=\frac{v^2}{rg}.
$$

Only one speed needs no friction at a given bank angle. At other speeds, static friction may point up or down the slope depending on the tendency to slip.

## Drag and terminal speed

Drag depends on velocity relative to the fluid. A common quadratic model is

$$
F_D=\frac12C_D\rho Av^2.
$$

For a falling body, drag grows as speed grows. Terminal speed occurs when acceleration reaches zero:

$$
mg=\frac12C_D\rho Av_t^2.
$$

Hence

$$
v_t=\sqrt{\frac{2mg}{C_D\rho A}}.
$$

Terminal speed is a steady speed, not an absence of forces. Weight and drag are equal and opposite. The formula assumes constant $C_D$, fixed orientation and area, uniform fluid density, and quadratic drag. Small particles in viscous flow often experience drag proportional to speed instead.

For a body released from rest, drag initially vanishes and acceleration begins near $g$. As speed rises, net downward force and acceleration decrease toward zero. Throwing the body downward faster than terminal speed makes drag exceed weight, so it slows toward the same terminal value.

## Noninertial frames and fictitious forces

Newton's laws take their simplest form in inertial frames. In a frame accelerating with $\vec a_f$, one can preserve the familiar equation by adding a fictitious force

$$
\vec F_{\text{fict}}=-m\vec a_f.
$$

Passengers in a car accelerating forward feel as if they are pushed backward because the car and seat accelerate beneath them. In the ground frame, the seat exerts a real forward force. In the car frame, a backward fictitious force is added to account for the frame's acceleration.

Rotating frames require centrifugal and Coriolis terms. They are useful descriptions inside the rotating frame but are not third-law partners of ordinary forces.

## Static equilibrium

An object in translational equilibrium has

$$
\sum\vec F=0.
$$

It may be at rest or move at constant velocity. For an extended rigid body, zero net force is not enough; zero net torque is also required:

$$
\sum\vec\tau=0.
$$

A ladder leaning against a wall can have balanced horizontal and vertical forces yet still rotate if their lines of action do not balance torques. Choosing a torque origin at an unknown support force often removes that force from the torque equation.

Consider a $10\,\mathrm{kg}$ traffic light suspended symmetrically by two cables, each making $40^\circ$ above horizontal. Horizontal components cancel. Vertical balance gives

$$
2T\sin40^\circ=mg.
$$

Therefore

$$
T=\frac{(10)(9.8)}{2\sin40^\circ}
=76.2\,\mathrm N.
$$

As the cables become more horizontal, $\sin\theta$ decreases and tension grows sharply. A perfectly horizontal cable could not support a finite weight with finite tension.

## Connected blocks on a surface

Two blocks of masses $m_1=4.0\,\mathrm{kg}$ and $m_2=6.0\,\mathrm{kg}$ are connected by a light string on a frictionless floor. A horizontal force $F=30\,\mathrm N$ pulls the larger block. Treat both blocks as one system first:

$$
F=(m_1+m_2)a.
$$

Thus

$$
a=\frac{30}{10.0}=3.0\,\mathrm{m/s^2}.
$$

Now isolate the smaller block. Its only horizontal force is tension:

$$
T=m_1a=(4.0)(3.0)=12\,\mathrm N.
$$

If the same external force pulled the smaller block instead, system acceleration would remain $3.0\,\mathrm{m/s^2}$, but the tension would be $m_2a=18\,\mathrm N$. Net system motion alone does not determine internal tension.

With kinetic friction, include each surface force in the system equation. If both blocks have the same coefficient on the same horizontal surface, total friction is $\mu_k(m_1+m_2)g$. Different coefficients require separate terms.

## Springs and normal-force contact

An ideal spring obeys Hooke's law

$$
\vec F_s=-k\vec x
$$

within its elastic range. The minus sign indicates that force opposes displacement from equilibrium. Stretching or compressing beyond the linear range can permanently deform the spring, so $k$ is not a universal description at arbitrary extension.

Contact forces can disappear. A block on top of an accelerating platform remains in contact only while the required normal force is nonnegative. For a platform accelerating downward with magnitude $a$,

$$
mg-N=ma,
$$

so

$$
N=m(g-a).
$$

If the platform attempts downward acceleration greater than $g$, this formula predicts $N\lt 0$. A surface cannot pull an unattached block downward, so contact is lost and the correct force becomes $N=0$ while the block free-falls.

## A loop-the-loop contact condition

At the top of a vertical circular track, both weight and the normal force may point toward the center. For an object moving on the inside of the loop,

$$
mg+N=\frac{mv^2}{r}.
$$

The minimum speed that maintains contact occurs when $N=0$:

$$
v_{\min}=\sqrt{gr}.
$$

Below this speed, the track would need to pull the object inward to preserve the circular path, which an ordinary contact surface cannot do. The object instead leaves the track and follows projectile motion.

At the bottom of the loop,

$$
N-mg=\frac{mv^2}{r},
$$

so $N$ exceeds weight. Applying one radial equation at every point without changing force directions produces sign errors.

## Force models have domains

The coefficient model $f_k=\mu_kN$ treats friction as independent of apparent contact area and speed. It is useful for many dry surfaces but not exact. Rolling resistance, lubrication, adhesion, temperature, and speed can matter.

Likewise, a point-particle model ignores rotation and size. A force through the center of mass can translate a rigid body without rotating it; an off-center force generally does both. If a pulley or wheel has rotational inertia, torque equations accompany the translational equations.

When a force is specified as a function of time, position, or velocity, the second law becomes a differential equation. Constant-acceleration kinematics follows only when the net force and mass make acceleration constant.

The first-law statement also reminds us that “force causes motion” is too broad. Net force causes acceleration, meaning a change of velocity. A moving object under balanced forces continues moving; an object instantaneously at rest under unbalanced force begins accelerating. Force diagrams predict the change, not the current velocity by inspection.

## Checks before trusting the equations

- Draw only forces acting on the chosen body. A third-law partner belongs on the other body.
- Determine whether static friction is sufficient before replacing it with kinetic friction.
- Compute the normal force from perpendicular dynamics; do not assume $N=mg$.
- Equal tensions and matched accelerations require an ideal string-pulley constraint.
- In circular motion, identify which real force components point inward.
- A negative acceleration means the actual direction opposes the chosen positive axis; it does not by itself indicate an error.
- Test limiting cases: equal Atwood masses give zero acceleration, zero friction recovers the frictionless incline, and infinite curve radius removes radial acceleration.

<div className="see-also">

See also: [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics) · [Two-Dimensional Motion](/physics/general/two-dimensional-motion) · [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Linear Momentum and Collisions](/physics/general/linear-momentum-and-collisions)

</div>
