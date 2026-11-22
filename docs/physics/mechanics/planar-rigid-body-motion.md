---
title: Planar Rigid-Body Motion
sidebar_position: 13
---

# Planar Rigid-Body Motion

A rigid body in planar motion can translate and rotate while every point remains in a plane parallel to a fixed reference plane. A wheel, connecting rod, door, gear, and sliding link all fit this model as long as deformation is negligible.

The rigidity constraint is the useful part: distances between body-fixed points do not change. Knowing the motion of one point plus the body's angular motion determines the velocity and acceleration of every other point. Forces then determine the acceleration of the mass center and the angular acceleration.

## Three kinds of planar motion

**Translation** occurs when any line fixed in the body keeps the same orientation. Every point has the same instantaneous velocity and acceleration:

$$
\mathbf{v}_B=\mathbf{v}_A,
\qquad
\mathbf{a}_B=\mathbf{a}_A.
$$

Translation may be rectilinear or curvilinear. A body can follow a curved path without rotating if its orientation remains fixed.

**Rotation about a fixed axis** occurs when one body-fixed point $O$ is stationary and the body changes orientation about an axis through $O$ perpendicular to the plane. For a point $P$ at distance $r$ from $O$,

$$
v_P=r\omega,
\qquad
a_{P,t}=r\alpha,
\qquad
a_{P,n}=r\omega^2.
$$

The velocity is tangent to the circular path. Tangential acceleration follows the sign of $\alpha$; normal acceleration always points toward $O$.

**General planar motion** combines translation and rotation. It can be viewed as translation of a chosen reference point plus rotation about that point. The choice of reference point is arbitrary, although pins, mass centers, and points with known path constraints are usually convenient.

| Motion | Point velocities | Point accelerations | Common model |
|---|---|---|---|
| Translation | equal at an instant | equal at an instant | sliding block |
| Fixed-axis rotation | tangent to circles about a fixed point | tangential plus inward normal | crank about a bearing |
| General planar motion | reference velocity plus rotational term | reference acceleration plus tangential and normal terms | connecting rod, rolling wheel |

Angular velocity and acceleration are axial vectors. With counterclockwise positive,

$$
\boldsymbol{\omega}=\omega\mathbf{k},
\qquad
\boldsymbol{\alpha}=\alpha\mathbf{k}.
$$

A negative scalar $\omega$ means clockwise rotation. A negative $\alpha$ means the angular velocity is changing in the clockwise sense; it does not by itself say whether the body is speeding up or slowing down. A clockwise body with counterclockwise angular acceleration is slowing down.

## Degrees of freedom and constraints

A free rigid body moving in a plane has three degrees of freedom: two coordinates locating a reference point and one orientation angle. Each independent ideal constraint removes one. A fixed pin removes both translations but leaves rotation. A slider guide removes motion normal to the guide and usually prevents body rotation if the slider is modeled as a block. A smooth pin in a slot constrains normal motion while allowing motion along the slot.

This count is a diagnostic rather than a substitute for equations. Redundant constraints may be geometrically dependent, and some mechanisms pass through singular configurations where an instantaneous degree of freedom changes. In a four-bar linkage, for example, one prescribed input angle normally fixes the other link positions, but aligned links can make velocity ratios very large or leave the assembly branch ambiguous.

Position constraints are differentiated to obtain velocity constraints, then differentiated again for acceleration. If a point satisfies

$$
f(x,y,t)=0,
$$

its velocity obeys

$$
\frac{\partial f}{\partial x}\dot{x}
+\frac{\partial f}{\partial y}\dot{y}
+\frac{\partial f}{\partial t}=0.
$$

The acceleration equation contains second-derivative terms. It cannot generally be guessed by replacing every velocity symbol with acceleration. Curved paths introduce normal acceleration through those additional terms.

## Relative velocity from the rigidity constraint

For body-fixed points $A$ and $B$,

$$
\mathbf{r}_B=\mathbf{r}_A+\mathbf{r}_{B/A}.
$$

The relative vector $\mathbf{r}_{B/A}$ has constant length but rotates with the body. The time derivative of a body-fixed vector observed from the inertial frame is

$$
\frac{d\mathbf{r}_{B/A}}{dt}
=\boldsymbol{\omega}\times\mathbf{r}_{B/A}.
$$

Differentiating the position relation gives

$$
\boxed{
\mathbf{v}_B
=\mathbf{v}_A
+\boldsymbol{\omega}\times\mathbf{r}_{B/A}.
}
$$

For $\mathbf{r}_{B/A}=x\mathbf{i}+y\mathbf{j}$,

$$
\boldsymbol{\omega}\times\mathbf{r}_{B/A}
=-\omega y\mathbf{i}+\omega x\mathbf{j}.
$$

Hence

$$
v_{Bx}=v_{Ax}-\omega y,
\qquad
v_{By}=v_{Ay}+\omega x.
$$

The relative-velocity term is perpendicular to $AB$. Taking the dot product with $\mathbf{r}_{B/A}$ gives zero, which is another statement that the distance $AB$ is not changing.

The same result follows by differentiating the rigidity condition directly:

$$
\mathbf{r}_{B/A}\cdot\mathbf{r}_{B/A}=L^2.
$$

Since $L$ is constant,

$$
2\mathbf{r}_{B/A}\cdot
(\mathbf{v}_B-\mathbf{v}_A)=0.
$$

Thus the relative velocity has no component along the line joining the points. For a planar body, every relative velocity field satisfying that condition can be represented by one common scalar angular velocity $\omega$.

Choosing another reference point does not change $\omega$. If $C$ is a third body-fixed point, applying the relative equation twice gives

$$
\mathbf{v}_C
=\mathbf{v}_A+\boldsymbol{\omega}\times\mathbf{r}_{C/A}
=\mathbf{v}_B+\boldsymbol{\omega}\times\mathbf{r}_{C/B}.
$$

This invariance is a good algebra check in mechanism calculations. Computing $\mathbf{v}_C$ through two different known points must give the same vector. Disagreement usually means a reversed relative-position vector or inconsistent angular sign.

Constraint directions often determine unknowns without solving every component. A slider in a horizontal guide has vertical velocity zero. A pinned point fixed to ground has both components zero. A point on a rotating crank has velocity perpendicular to the crank. Combining those direction statements with the relative-velocity equation is the standard route through linkage problems.

## The instantaneous center is a velocity construction

At any instant when $\omega\ne0$, general planar motion can be represented kinematically as rotation about an **instantaneous center of zero velocity** $C$. If $C$ is known,

$$
v_P=\omega r_{P/C},
$$

and $\mathbf{v}_P$ is perpendicular to the line $CP$. The center can be located by drawing a line through each of two points perpendicular to that point's known velocity; their intersection is $C$.

The construction has several edge cases:

- For pure translation, $\omega=0$ and the instantaneous center is at infinity in a direction perpendicular to the common velocities.
- The center may lie outside the physical body.
- Its location can change from instant to instant and need not be a material point.
- Parallel velocity-direction lines may make a graphical construction poorly conditioned even when a distant center exists.

The center gives a compact velocity field, but it is generally unsafe for acceleration. Zero velocity at one instant does not imply zero acceleration. A rolling wheel's ground-contact point is the familiar example: its instantaneous velocity is zero, while its acceleration is usually nonzero.

## Acceleration keeps both angular terms

Differentiate the relative-velocity equation:

$$
\boxed{
\mathbf{a}_B
=\mathbf{a}_A
+\boldsymbol{\alpha}\times\mathbf{r}_{B/A}
+\boldsymbol{\omega}\times
(\boldsymbol{\omega}\times\mathbf{r}_{B/A}).
}
$$

For planar motion,

$$
\boldsymbol{\omega}\times
(\boldsymbol{\omega}\times\mathbf{r}_{B/A})
=-\omega^2\mathbf{r}_{B/A}.
$$

Thus the relative acceleration consists of:

$$
\mathbf{a}_{B/A,t}
=\boldsymbol{\alpha}\times\mathbf{r}_{B/A},
$$

perpendicular to $AB$, and

$$
\mathbf{a}_{B/A,n}
=-\omega^2\mathbf{r}_{B/A},
$$

directed from $B$ toward $A$. The normal term depends on $\omega^2$, so reversing the rotation direction does not reverse it.

Acceleration constraints differ from velocity constraints when a path is curved. A collar on a circular guide has velocity tangent to the guide but also has a normal acceleration $v^2/\rho$ toward the center of curvature. Setting its normal acceleration to zero because its normal velocity is zero confuses two different derivatives.

For points sliding relative to a rotating body, further relative-motion and Coriolis terms appear. The equations above apply only when $A$ and $B$ are fixed points of the same rigid body.

## Rolling without slipping

For a wheel of radius $R$ on a fixed straight surface, no slip means the contact-point velocity relative to the surface is zero. If $x_G$ is positive right and $\theta$ is positive counterclockwise, the constraint is

$$
x_G+R\theta=\text{constant}.
$$

Differentiation gives

$$
v_G=-R\omega,
\qquad
a_G=-R\alpha.
$$

The minus sign follows from the stated convention: rightward rolling is clockwise. If clockwise angular variables are instead declared positive, the scalar equations become $v_G=R\omega$ and $a_G=R\alpha$. Writing the sign convention beside the diagram is better than memorizing one version.

No slip is a static-friction condition, not a guarantee. After solving for the required friction $f$, verify

$$
|f|\le\mu_sN.
$$

If the requirement exceeds the available static friction, the wheel slips and the rolling constraint cannot be used. The translational and rotational equations must then be solved with an appropriate kinetic-friction model.

At the contact point $C$ of a steadily rolling wheel, $\mathbf{v}_C=\mathbf{0}$ at that instant. With constant $\omega$ and $a_G=0$,

$$
\mathbf{a}_C=-\omega^2\mathbf{r}_{C/G},
$$

which points upward toward the center. The contact point is not a fixed pivot.

## Force and moment equations for the body

For a rigid body of constant mass with center of mass $G$,

$$
\sum F_x=ma_{Gx},
\qquad
\sum F_y=ma_{Gy},
$$

$$
\sum M_G=I_G\alpha.
$$

The force resultant controls translation of $G$; the moment resultant about $G$ controls rotation. Constraints couple the two parts. A pin reaction may affect $\mathbf{a}_G$ without appearing in a moment equation taken about the pin, while friction may influence both translation and rotation.

For rotation about a point $O$ fixed in an inertial frame,

$$
\sum M_O=I_O\alpha.
$$

That compact equation does not extend unchanged to an arbitrary accelerating point. The always-valid planar relation about a point $P$ is obtained from the mass-center equations:

$$
\sum M_P
=I_G\alpha
+\mathbf{r}_{G/P}\times m\mathbf{a}_G.
$$

Taking moments about $G$ avoids the extra term. Taking moments about another point can still be efficient, but the kinematic status of that point must be established first.

The kinetic energy of any body in planar motion is

$$
T=\frac12mv_G^2+\frac12I_G\omega^2.
$$

For fixed-axis rotation about $O$, the parallel-axis theorem and $v_G=\omega r_{G/O}$ combine to give

$$
T=\frac12I_O\omega^2.
$$

Energy methods can eliminate unknown constraint forces that do no work, but they give less direct information about reactions and friction than the force-moment equations.

Angular momentum offers the parallel momentum description. About the mass center,

$$
\mathbf{H}_G=I_G\boldsymbol{\omega},
$$

and the moment equation is

$$
\sum\mathbf{M}_G=\frac{d\mathbf{H}_G}{dt}.
$$

In planar motion the axis direction is fixed, so this reduces to $\sum M_G=I_G\alpha$. About another point, angular momentum also contains the orbital term $\mathbf{r}_{G/P}\times m\mathbf{v}_G$. Omitting it is the momentum counterpart of using $I_G$ about the wrong point.

Power gives a useful instantaneous check on those equations. The power delivered by external forces and couples is

$$
\mathcal{P}
=\sum_i\mathbf{F}_i\cdot\mathbf{v}_i
+\sum_j M_j\omega.
$$

For a rigid body it equals the time derivative of kinetic energy. A pin reaction at a fixed pin has zero power because the point velocity is zero. Static friction at an ideal no-slip contact also has zero instantaneous power because the material contact point is at rest relative to the fixed surface, even though friction can change the division of energy between translation and rotation.

## Worked example: translating and rotating bar

A $0.9$ m bar has

$$
\mathbf{r}_{B/A}=0.9\mathbf{i}\ \text{m}.
$$

At one instant,

$$
\mathbf{v}_A=1.2\mathbf{i}\ \text{m/s},
\qquad
\mathbf{a}_A=0.5\mathbf{j}\ \text{m/s}^2,
$$

and the bar has $\omega=4$ rad/s counterclockwise and $\alpha=2$ rad/s$^2$ counterclockwise.

The relative velocity is

$$
\begin{aligned}
\boldsymbol{\omega}\times\mathbf{r}_{B/A}
&=4\mathbf{k}\times0.9\mathbf{i}\\
&=3.6\mathbf{j}\ \text{m/s}.
\end{aligned}
$$

Therefore

$$
\boxed{\mathbf{v}_B=1.2\mathbf{i}+3.6\mathbf{j}\ \text{m/s}.}
$$

For acceleration, first compute the tangential part:

$$
\boldsymbol{\alpha}\times\mathbf{r}_{B/A}
=2\mathbf{k}\times0.9\mathbf{i}
=1.8\mathbf{j}\ \text{m/s}^2.
$$

The normal part is

$$
-\omega^2\mathbf{r}_{B/A}
=-(4)^2(0.9\mathbf{i})
=-14.4\mathbf{i}\ \text{m/s}^2.
$$

Adding the reference-point acceleration,

$$
\begin{aligned}
\mathbf{a}_B
&=0.5\mathbf{j}+1.8\mathbf{j}-14.4\mathbf{i}\\
&=-14.4\mathbf{i}+2.3\mathbf{j}\ \text{m/s}^2.
\end{aligned}
$$

Thus

$$
\boxed{\mathbf{a}_B=-14.4\mathbf{i}+2.3\mathbf{j}\ \text{m/s}^2.}
$$

The large negative $x$ component is the normal acceleration toward $A$. It would remain negative even if the bar's angular velocity were clockwise with the same magnitude.

## Worked example: velocity in a slider-crank

A crank $OA$ has length $0.20$ m and is at $60^\circ$ above the positive horizontal axis. It rotates counterclockwise at $5$ rad/s. A connecting rod $AB$ of length $0.60$ m joins $A$ to a slider $B$ constrained to the horizontal axis to the right of $O$. Find the slider velocity and the connecting rod's angular velocity.

The point coordinates of $A$ are

$$
x_A=0.20\cos60^\circ=0.1000\ \text{m},
$$

$$
y_A=0.20\sin60^\circ=0.1732\ \text{m}.
$$

Because $B$ lies on $y=0$ and $AB=0.60$ m, the horizontal separation is

$$
x_B-x_A
=\sqrt{0.60^2-0.1732^2}
=0.5745\ \text{m}.
$$

Thus

$$
\mathbf{r}_{B/A}
=0.5745\mathbf{i}-0.1732\mathbf{j}\ \text{m}.
$$

The velocity of $A$ follows from fixed-axis rotation of the crank:

$$
\begin{aligned}
\mathbf{v}_A
&=5\mathbf{k}\times
(0.1000\mathbf{i}+0.1732\mathbf{j})\\
&=-0.8660\mathbf{i}+0.5000\mathbf{j}\ \text{m/s}.
\end{aligned}
$$

Let the connecting rod angular velocity be $\omega_{AB}\mathbf{k}$, positive counterclockwise. Relative velocity gives

$$
\mathbf{v}_B
=\mathbf{v}_A
+\omega_{AB}\mathbf{k}\times\mathbf{r}_{B/A}.
$$

Since

$$
\mathbf{k}\times\mathbf{r}_{B/A}
=0.1732\mathbf{i}+0.5745\mathbf{j},
$$

the component equations are

$$
v_B=-0.8660+0.1732\omega_{AB},
$$

$$
0=0.5000+0.5745\omega_{AB}.
$$

The second equation uses the slider constraint $v_{By}=0$. It gives

$$
\omega_{AB}
=-\frac{0.5000}{0.5745}
=-0.8703\ \text{rad/s}.
$$

The negative sign means the connecting rod rotates clockwise at this instant. Substitute into the horizontal equation:

$$
v_B
=-0.8660+0.1732(-0.8703)
=-1.017\ \text{m/s}.
$$

Therefore

$$
\boxed{\mathbf{v}_B=-1.017\mathbf{i}\ \text{m/s},\qquad
\omega_{AB}=0.870\ \text{rad/s clockwise}.}
$$

Although the crank rotates counterclockwise, the slider is moving left and the connecting rod is rotating clockwise in this configuration. Mechanism directions cannot be inferred reliably from the input rotation alone; the constraint equations settle them.

## Worked example: cylinder pulled through its center

A solid cylinder has mass $m=12$ kg and radius $R=0.20$ m. It rolls without slipping on a horizontal floor while a horizontal force $P=30$ N is applied to its center toward the right. Find the center acceleration and the static-friction force. For a solid cylinder,

$$
I_G=\frac12mR^2.
$$

Assume a friction magnitude $f$ acting left. Horizontal translation gives

$$
P-f=ma.
$$

Take clockwise angular acceleration as positive for this calculation. Only friction creates a moment about $G$:

$$
fR=I_G\alpha.
$$

The rolling constraint with the same positive directions is

$$
a=R\alpha.
$$

Eliminate $\alpha$:

$$
fR=I_G\frac{a}{R},
$$

$$
f=\frac{I_G}{R^2}a
=\frac12ma.
$$

Substitute into translation:

$$
P-\frac12ma=ma,
$$

$$
a=\frac{2P}{3m}
=\frac{2(30)}{3(12)}
=1.667\ \text{m/s}^2.
$$

Then

$$
f=\frac12(12)(1.667)=10.0\ \text{N}.
$$

The result is

$$
\boxed{a_G=1.67\ \text{m/s}^2\text{ right},\qquad
f=10.0\ \text{N left}.}
$$

The assumed friction direction produced a positive magnitude. Leftward friction supplies the clockwise torque required for rolling even though the center accelerates right. With $N=mg$, the minimum static-friction coefficient is

$$
\mu_s\ge\frac{f}{N}
=\frac{10.0}{12(9.81)}
=0.085.
$$

Below that value the no-slip solution is inconsistent.

## Failure modes to watch

- The instantaneous center belongs to velocity analysis. Using it as a fixed pivot in an acceleration equation drops the center's own acceleration.
- The $-\omega^2\mathbf{r}$ term is present even when $\alpha=0$. Constant angular speed does not mean zero point acceleration.
- Relative-motion formulas for two body-fixed points do not cover a collar sliding along a rotating bar; that problem includes relative velocity and Coriolis acceleration.
- Friction opposes impending relative slip at the contact, not necessarily the motion of the mass center.
- A rolling constraint needs a declared angular sign. Mixing counterclockwise-positive kinetics with clockwise-positive constraint equations changes a sign silently.
- $I_G$ belongs with moments about $G$. Fixed-axis equations about $O$ use $I_O$, while moments about a general point need the mass-center acceleration term.

## Related pages

- [Particle kinematics](/physics/mechanics/particle-kinematics)
- [Particle kinetics with Newton's second law](/physics/mechanics/particle-kinetics-newton)
- [Work-energy methods](/physics/mechanics/work-energy-methods)
- [Centroids and second moments](/physics/mechanics/centroids-second-moments)
