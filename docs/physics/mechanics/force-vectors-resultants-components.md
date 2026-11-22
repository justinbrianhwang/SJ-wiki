---
title: Force Vectors, Resultants, and Components
sidebar_position: 2
---

# Force Vectors, Resultants, and Components

A force needs a magnitude, a direction, and a line of action. Treating it as a vector handles the first two. Recording where it acts supplies the third, which becomes essential when moments enter the problem.

Most early mechanics errors happen before an equilibrium equation is written: an angle is read from the wrong axis, a cable direction is reversed, or magnitudes are added as though they were signed components. A consistent vector description turns those geometric decisions into ordinary algebra.

## What the arrow carries

A scalar has magnitude but no spatial direction. Mass, time, temperature, work, and kinetic energy are scalars. A vector has components that change when the coordinate basis changes while the geometric object itself stays the same. Force, position, velocity, acceleration, and moment are vectors.

In a right-handed Cartesian basis,

$$
\mathbf{F}=F_x\mathbf{i}+F_y\mathbf{j}+F_z\mathbf{k}.
$$

Its magnitude is

$$
F=\lVert\mathbf{F}\rVert
=\sqrt{F_x^2+F_y^2+F_z^2}.
$$

The basis vectors $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ have unit length and are mutually perpendicular. The signed coefficients $F_x$, $F_y$, and $F_z$ are scalar components. The vectors $F_x\mathbf{i}$, $F_y\mathbf{j}$, and $F_z\mathbf{k}$ are vector components. Textbooks sometimes use “component” for both, so the surrounding equation has to settle which one is meant.

Two vectors are equal when their corresponding components in the same basis are equal. Their points of application do not enter that equality. In rigid-body mechanics, however, equal force vectors applied on different lines can have different rotational effects. A force vector and a fully specified force on a body are therefore related but distinct descriptions.

Vector addition follows the parallelogram or tip-to-tail construction. Algebraically it is component-wise:

$$
\sum_i\mathbf{F}_i=
\left(\sum_iF_{ix}\right)\mathbf{i}
+\left(\sum_iF_{iy}\right)\mathbf{j}
+\left(\sum_iF_{iz}\right)\mathbf{k}.
$$

This sum is the **resultant force**

$$
\mathbf{R}=\sum_i\mathbf{F}_i.
$$

If all forces are concurrent, replacing them by $\mathbf{R}$ at their common point preserves their external effect. For nonconcurrent forces, the resultant alone generally loses moment information.

## Resolving a planar force without guessing signs

If $\theta$ is measured counterclockwise from the positive $x$ axis,

$$
F_x=F\cos\theta,
\qquad
F_y=F\sin\theta.
$$

That formula works for angles in any quadrant if the trigonometric functions retain their signs. Many diagrams instead give an acute reference angle from a vertical axis. Then the adjacent component uses cosine and the opposite component uses sine:

$$
|F_y|=F\cos\beta,
\qquad
|F_x|=F\sin\beta
$$

when $\beta$ is measured from the $y$ direction. Signs come from the arrow's actual directions, not from the triangle lengths.

A robust sequence is:

1. Draw the force arrow in the chosen axes.
2. Mark the given angle at the axis from which it is measured.
3. Compute positive triangle lengths.
4. Attach component signs from left/right and up/down.

For a planar resultant,

$$
R_x=\sum_iF_{ix},
\qquad
R_y=\sum_iF_{iy},
$$

$$
R=\sqrt{R_x^2+R_y^2}.
$$

The direction is best written as

$$
\theta=\operatorname{atan2}(R_y,R_x),
$$

because the two-argument arctangent uses the signs of both components. A calculator evaluation of $\tan^{-1}(R_y/R_x)$ cannot distinguish opposite quadrants and fails when $R_x=0$.

The magnitude of a resultant is bounded by the triangle inequality,

$$
\left\lVert\sum_i\mathbf{F}_i\right\rVert
\le\sum_i\lVert\mathbf{F}_i\rVert.
$$

Equality occurs when all nonzero forces point in the same direction. A computed resultant larger than the sum of the force magnitudes is impossible.

### Components are not extra forces

Resolving one force into $x$ and $y$ components creates an equivalent representation, not two additional loads to place beside the original force on a free-body diagram. Either draw the original inclined force or draw its components. Drawing all three double-counts the load.

Cartesian components are especially convenient because perpendicular unit vectors form an orthonormal basis. Components in oblique directions require more care. Suppose

$$
\mathbf{F}=P\mathbf{u}+Q\mathbf{v},
$$

where $\mathbf{u}$ and $\mathbf{v}$ are unit vectors that are not perpendicular. The coefficients are found by solving the vector equation; they are not generally the dot products $\mathbf{F}\cdot\mathbf{u}$ and $\mathbf{F}\cdot\mathbf{v}$. Those dot products are orthogonal projections, which differ from oblique resolution because each oblique basis vector itself has a component along the other.

Coordinate choice can reduce the algebra. On an incline, axes tangent and normal to the surface turn the normal reaction into one component and often turn friction into the other. The weight must then be resolved in that rotated basis. Changing axes does not change the physical force or resultant; it changes only their component descriptions.

## Direction from geometry in three dimensions

Cables and links are usually specified by two endpoints rather than three direction angles. If a cable runs from $A$ to $B$, its direction vector is

$$
\mathbf{r}_{AB}
=(x_B-x_A)\mathbf{i}
+(y_B-y_A)\mathbf{j}
+(z_B-z_A)\mathbf{k}.
$$

Normalize it to obtain a unit vector:

$$
\mathbf{u}_{AB}
=\frac{\mathbf{r}_{AB}}{\lVert\mathbf{r}_{AB}\rVert}.
$$

A tension of magnitude $T$ pulling on the attachment at $A$ toward $B$ is

$$
\mathbf{T}=T\mathbf{u}_{AB}.
$$

Point order carries the sign. Since $\mathbf{r}_{BA}=-\mathbf{r}_{AB}$, reversing the order reverses the force direction.

The components of a unit vector are also the direction cosines:

$$
\mathbf{u}
=(\cos\alpha)\mathbf{i}
+(\cos\beta)\mathbf{j}
+(\cos\gamma)\mathbf{k},
$$

where $\alpha$, $\beta$, and $\gamma$ are the angles with the positive coordinate axes. Unit length implies

$$
\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1.
$$

Three direction angles are therefore not independent. If two cosines and the octant are known, the third follows from normalization. Direction angles are commonly taken between $0^\circ$ and $180^\circ$; a component pointing toward a negative axis has an obtuse direction angle and a negative cosine.

## Solving for unknown force magnitudes

When force directions are known but magnitudes are not, each force can be written as an unknown scalar times a known unit vector:

$$
\mathbf{F}_i=T_i\mathbf{u}_i.
$$

An equilibrium or specified-resultant condition then becomes a linear system for the scalars. In three dimensions,

$$
\begin{bmatrix}
u_{1x}&u_{2x}&u_{3x}\\
u_{1y}&u_{2y}&u_{3y}\\
u_{1z}&u_{2z}&u_{3z}
\end{bmatrix}
\begin{bmatrix}
T_1\\T_2\\T_3
\end{bmatrix}
=-\mathbf{F}_{known}.
$$

The geometry controls whether the system can be solved. If the direction vectors are coplanar, they cannot balance a load with a component normal to that plane. If two directions are nearly parallel, the coefficient matrix is poorly conditioned and small geometric changes can produce large changes in the solved forces.

Assumed arrows determine the signs of the unknown scalars. A negative answer does not automatically indicate failed algebra; it says the actual force acts opposite the assumed arrow. For a cable, a negative tension is physically inadmissible because an ideal cable cannot push. The model must then be reconsidered: that cable would go slack, and the remaining supports would need to satisfy equilibrium.

Graphical force polygons were once a standard engineering method and remain a useful check. For equilibrium, vectors placed tip to tail must close. The polygon shows direction and relative magnitude well, while component equations provide the precision expected in calculations.

## From a physical contact to a free-body arrow

A vector equation is only as complete as the isolated system. Before resolving components, decide which body or particle is being separated from its surroundings. Each cut connection is then replaced by the force that the removed surroundings exert on the isolated object.

Different idealizations imply different unknown vectors. A smooth surface supplies one normal reaction. A rough contact may supply a normal and a tangential friction force. A two-force link supplies one axial force along its centerline. A pin in a planar rigid body generally supplies two force components, while a fixed support also supplies a reaction moment.

Newton's third-law pair belongs on two different free-body diagrams. If a cable pulls a ring toward an anchor, the ring pulls the cable toward the ring with an equal and opposite vector. Placing both arrows on the ring's diagram would cancel a real interaction and erase the cable's effect.

Known geometry should be kept separate from unknown mechanics. The direction of an ideal cable force is known from its endpoints, but its tension magnitude may be unknown. A pin reaction has unknown magnitude and direction, so Cartesian components are more economical than an unknown magnitude plus an unknown angle. Selecting unknowns that enter linearly keeps the eventual equilibrium equations transparent.

## Projections answer a different question

Resolving into Cartesian components asks how much of a vector lies along each coordinate basis direction. Projection can ask the same question along any line.

The dot product is

$$
\mathbf{A}\cdot\mathbf{B}
=A_xB_x+A_yB_y+A_zB_z
=\lVert\mathbf{A}\rVert\lVert\mathbf{B}\rVert\cos\theta.
$$

For a unit direction $\mathbf{u}$, the signed scalar component of $\mathbf{F}$ along that direction is

$$
F_u=\mathbf{F}\cdot\mathbf{u}.
$$

The corresponding vector projection is

$$
\operatorname{proj}_{\mathbf{u}}\mathbf{F}
=(\mathbf{F}\cdot\mathbf{u})\mathbf{u}.
$$

If the supplied direction vector $\mathbf{a}$ is not a unit vector, normalize it first or use

$$
\operatorname{proj}_{\mathbf{a}}\mathbf{F}
=\frac{\mathbf{F}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}\mathbf{a}.
$$

A negative scalar projection means the force points partly opposite the chosen positive direction. It does not mean the projection magnitude is physically negative.

The cross product addresses perpendicular effect:

$$
\mathbf{A}\times\mathbf{B}
=
\begin{vmatrix}
\mathbf{i}&\mathbf{j}&\mathbf{k}\\
A_x&A_y&A_z\\
B_x&B_y&B_z
\end{vmatrix}.
$$

Its magnitude is $AB\sin\theta$, and its direction follows the right-hand rule. In mechanics,

$$
\mathbf{M}_O=\mathbf{r}\times\mathbf{F}
$$

is the moment of a force about $O$. Only the component of $\mathbf{r}$ perpendicular to the force contributes.

| Operation | Result type | Geometric meaning | Mechanics use |
|---|---|---|---|
| $\mathbf{A}+\mathbf{B}$ | vector | tip-to-tail combination | resultant force |
| $\mathbf{A}\cdot\mathbf{B}$ | scalar | aligned projection | work, force along a line |
| $\mathbf{A}\times\mathbf{B}$ | vector | oriented perpendicular area | moment, angular momentum |
| $\lVert\mathbf{A}\rVert$ | scalar | vector length | force magnitude |

## A resultant for a rigid body also needs a moment

For forces acting at positions $\mathbf{r}_i$ measured from $O$, form

$$
\mathbf{R}=\sum_i\mathbf{F}_i,
\qquad
\mathbf{M}_O=\sum_i\mathbf{r}_i\times\mathbf{F}_i.
$$

The pair $(\mathbf{R},\mathbf{M}_O)$ is an equivalent force-couple system at $O$. Moving the reference point to $P$ changes the reported moment according to

$$
\mathbf{M}_P=\mathbf{M}_O-\mathbf{r}_{OP}\times\mathbf{R}.
$$

If $\mathbf{R}\ne\mathbf{0}$, a planar system may sometimes be replaced by a single resultant on a suitable line of action. Its location must satisfy

$$
\mathbf{r}\times\mathbf{R}=\mathbf{M}_O.
$$

If $\mathbf{R}=\mathbf{0}$ but $\mathbf{M}_O\ne\mathbf{0}$, no single force can represent the system. The remainder is a pure couple, whose moment is the same about every point. This edge case explains why “the resultant is zero” does not always mean “the force system has no external effect.”

For an ideal rigid body, a force may be moved anywhere along its own line of action without changing its external force or moment about any point. This is the principle of transmissibility. Moving the force to a parallel line is different: it changes the moment by $\mathbf{d}\times\mathbf{F}$ and must be accompanied by a couple to retain equivalence.

Transmissibility concerns the body's external rigid-body response. The internal stress distribution near the load application can depend strongly on the actual contact region. A concentrated arrow is an idealization of a bearing, bolt, cable eye, or pressure patch; it should not be used to infer local stress without a more detailed model.

Distributed loads follow the same reduction. For a load intensity $w(x)$ along a beam,

$$
R=\int_a^b w(x)\,dx,
\qquad
x_R=\frac{\int_a^b xw(x)\,dx}{\int_a^b w(x)\,dx}.
$$

The resultant equals the area under the load diagram and acts through that area's centroid. A triangular load therefore acts one third of its base length from the larger-intensity end.

Several common special cases follow directly:

| Load shape over length $L$ | Resultant magnitude | Location from the left end |
|---|---:|---:|
| Uniform $w_0$ | $w_0L$ | $L/2$ |
| Triangle from $0$ to $w_0$ | $w_0L/2$ | $2L/3$ |
| Triangle from $w_0$ to $0$ | $w_0L/2$ | $L/3$ |
| General $w(x)$ | $\int_0^Lw(x)\,dx$ | $\int_0^Lxw(x)\,dx/R$ |

If $w(x)$ changes sign, the signed area gives the resultant. When the positive and negative areas cancel, $R=0$ and the centroid formula divides by zero. The distribution can still have a nonzero net moment, so its reduction is then a pure couple rather than a force at an infinitely distant point.

## Worked example: three concurrent planar forces

Three forces act at a pin: $80$ N at $30^\circ$ above $+x$, $55$ N at $120^\circ$ counterclockwise from $+x$, and $40$ N downward. Find the resultant.

Resolve the first force:

$$
\begin{aligned}
F_{1x}&=80\cos30^\circ=69.28\ \text{N},\\
F_{1y}&=80\sin30^\circ=40.00\ \text{N}.
\end{aligned}
$$

For the second force, $120^\circ$ lies in quadrant II:

$$
\begin{aligned}
F_{2x}&=55\cos120^\circ=-27.50\ \text{N},\\
F_{2y}&=55\sin120^\circ=47.63\ \text{N}.
\end{aligned}
$$

The downward force is

$$
\mathbf{F}_3=-40.00\mathbf{j}\ \text{N}.
$$

Add signed components:

$$
\begin{aligned}
R_x&=69.28-27.50=41.78\ \text{N},\\
R_y&=40.00+47.63-40.00=47.63\ \text{N}.
\end{aligned}
$$

Thus

$$
\mathbf{R}=41.78\mathbf{i}+47.63\mathbf{j}\ \text{N}.
$$

Its magnitude is

$$
R=\sqrt{41.78^2+47.63^2}=63.36\ \text{N}.
$$

Both components are positive, so the resultant is in quadrant I:

$$
\theta=\operatorname{atan2}(47.63,41.78)=48.74^\circ.
$$

The result is

$$
\boxed{R=63.36\ \text{N at }48.7^\circ\text{ counterclockwise from }+x.}
$$

The component reconstruction gives $63.36$ N, and the triangle-inequality bound is $80+55+40=175$ N, so both checks pass.

## Worked example: a cable force and its projection

A cable runs from $A=(1,2,0)$ m to $B=(4,-1,6)$ m. Its tension is $240$ N and it pulls the attachment at $A$ toward $B$. Find the Cartesian force vector. Then find its scalar component along the axis from $A$ toward $C=(3,4,1)$ m.

The cable direction is

$$
\mathbf{r}_{AB}
=(4-1)\mathbf{i}+(-1-2)\mathbf{j}+(6-0)\mathbf{k}
=3\mathbf{i}-3\mathbf{j}+6\mathbf{k}\ \text{m}.
$$

Its length is

$$
\lVert\mathbf{r}_{AB}\rVert
=\sqrt{3^2+(-3)^2+6^2}
=\sqrt{54}=3\sqrt{6}\ \text{m}.
$$

Therefore

$$
\mathbf{u}_{AB}
=\frac{1}{\sqrt6}\mathbf{i}
-\frac{1}{\sqrt6}\mathbf{j}
+\frac{2}{\sqrt6}\mathbf{k}.
$$

Multiplying by the tension gives

$$
\begin{aligned}
\mathbf{T}
&=240\mathbf{u}_{AB}\\
&=97.98\mathbf{i}-97.98\mathbf{j}+195.96\mathbf{k}\ \text{N}.
\end{aligned}
$$

For the requested projection, first form the new unit direction:

$$
\mathbf{r}_{AC}=2\mathbf{i}+2\mathbf{j}+1\mathbf{k},
\qquad
\lVert\mathbf{r}_{AC}\rVert=3,
$$

$$
\mathbf{u}_{AC}
=\frac23\mathbf{i}+\frac23\mathbf{j}+\frac13\mathbf{k}.
$$

The signed scalar component is

$$
\begin{aligned}
T_{AC}
&=\mathbf{T}\cdot\mathbf{u}_{AC}\\
&=97.98\left(\frac23\right)
-97.98\left(\frac23\right)
+195.96\left(\frac13\right)\\
&=65.32\ \text{N}.
\end{aligned}
$$

Hence

$$
\boxed{\mathbf{T}=(97.98,-97.98,195.96)\ \text{N},\qquad
T_{AC}=65.32\ \text{N}.}
$$

The $x$ and $y$ contributions to the projection cancel because the projection axis has equal positive components in those directions. Checking

$$
\sqrt{97.98^2+(-97.98)^2+195.96^2}=240.0\ \text{N}
$$

confirms that normalization preserved the stated cable tension.

## Worked example: reducing a trapezoidal beam load

A downward load varies linearly from $2$ kN/m at the left end of a $6$ m interval to $8$ kN/m at the right end. Find its equivalent resultant and line of action.

Write the intensity as

$$
w(x)=2+\frac{8-2}{6}x=2+x
$$

in kN/m, with $x$ in meters from the left end. The resultant magnitude is the signed area:

$$
\begin{aligned}
R
&=\int_0^6(2+x)\,dx \\
&=\left[2x+\frac{x^2}{2}\right]_0^6 \\
&=12+18
=30\ \text{kN}.
\end{aligned}
$$

The moment of the distributed load about the left end is

$$
\begin{aligned}
M_O
&=\int_0^6x(2+x)\,dx \\
&=\left[x^2+\frac{x^3}{3}\right]_0^6 \\
&=36+72
=108\ \text{kN m}.
\end{aligned}
$$

Place the resultant at $x_R$ so that it produces the same moment:

$$
Rx_R=M_O,
$$

$$
x_R=\frac{108}{30}=3.60\ \text{m}.
$$

Therefore

$$
\boxed{R=30\ \text{kN downward at }x=3.60\ \text{m}.}
$$

The location is to the right of the midpoint because the load is heavier there. The same answer comes from decomposing the trapezoid into a $2$ kN/m rectangle and a $0$-to-$6$ kN/m triangle:

$$
R_1=2(6)=12\ \text{kN},
\qquad x_1=3\ \text{m},
$$

$$
R_2=\frac12(6)(6)=18\ \text{kN},
\qquad x_2=\frac23(6)=4\ \text{m}.
$$

Then

$$
x_R=\frac{12(3)+18(4)}{12+18}
=\frac{108}{30}
=3.60\ \text{m}.
$$

The integral and composite-area methods are two versions of the same first-moment calculation.

## Sign and modeling checks

- Cable tension on an isolated attachment points away from that attachment along the cable. A cable can pull; an ideal flexible cable cannot push.
- A component magnitude cannot exceed the vector magnitude when the basis is orthonormal. If $\vert F_x\vert \gt F$, the angle or arithmetic is wrong.
- Angles must be tied to a named axis and direction of measurement. “$30^\circ$ force” is incomplete.
- Adding magnitudes discards cancellation. Only collinear forces already carrying signs may be combined as one-dimensional scalars.
- A unit vector should satisfy $u_x^2+u_y^2+u_z^2=1$ before it is multiplied by a force magnitude.
- A zero force resultant does not rule out a nonzero couple. Check moments whenever forces are nonconcurrent.
- Newtons and meters may be used together in a moment calculation, but geometry given in millimeters must first be converted if the desired moment unit is N m.

<div className="see-also">

See also: [Particle equilibrium](/physics/mechanics/particle-equilibrium) · [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium) · [Particle kinematics](/physics/mechanics/particle-kinematics) · [Impulse, momentum, and impact](/physics/mechanics/impulse-momentum-impact)

</div>
