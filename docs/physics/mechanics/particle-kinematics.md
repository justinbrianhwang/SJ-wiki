---
title: Particle Kinematics
sidebar_position: 9
---

# Particle Kinematics

Kinematics describes how a particle moves without specifying the forces responsible. Position, velocity, and acceleration form a derivative chain, but the useful form of that chain depends strongly on the geometry. Fixed Cartesian axes suit independently described coordinates; tangent-normal axes suit a known path; polar axes suit motion along a rotating arm or radial slot.

A particle has position but no orientation. It can travel on a curved path, yet it does not itself rotate in the rigid-body sense. Once acceleration has been expressed in suitable coordinates, kinetics supplies the separate relation between that acceleration and force.

## Position, displacement, and distance traveled

Relative to a fixed origin $O$, position is

$$
\mathbf r(t)=x(t)\mathbf i+y(t)\mathbf j+z(t)\mathbf k.
$$

The displacement between two instants is

$$
\Delta\mathbf r=\mathbf r(t_2)-\mathbf r(t_1).
$$

Displacement depends only on the endpoints. Distance traveled depends on the path between them and is never negative. If $s$ measures arc length along the path,

$$
\Delta s=\int_{t_1}^{t_2}\lVert\mathbf v(t)\rVert\,dt.
$$

A particle that returns to its starting point has zero displacement but positive distance traveled. Keeping those quantities separate matters whenever velocity changes direction.

Velocity and acceleration are

$$
\mathbf v=\frac{d\mathbf r}{dt},
\qquad
\mathbf a=\frac{d\mathbf v}{dt}
=\frac{d^2\mathbf r}{dt^2}.
$$

Velocity is tangent to a smooth path. Acceleration need not point along velocity: its tangential part changes speed, while its normal part changes direction. Thus zero acceleration implies constant velocity as a vector, not merely constant speed.

## Straight-line motion without memorizing cases

For rectilinear motion along coordinate $x$,

$$
v=\frac{dx}{dt},
\qquad
a=\frac{dv}{dt}=\frac{d^2x}{dt^2}.
$$

The three familiar constant-acceleration formulas follow by integration, not as independent rules. If $a$ is constant,

$$
v=v_0+a(t-t_0).
$$

Integrating velocity once more gives

$$
x=x_0+v_0(t-t_0)+\frac12a(t-t_0)^2.
$$

Eliminating time uses the chain rule:

$$
a=\frac{dv}{dt}
=\frac{dv}{dx}\frac{dx}{dt}
=v\frac{dv}{dx}.
$$

For constant $a$, integration gives

$$
v^2=v_0^2+2a(x-x_0).
$$

The first pair applies when acceleration is known as a function of time. The chain-rule form is more direct when acceleration is given as a function of position. If acceleration is instead known as a function of velocity, separation of variables in $a(v)=dv/dt$ is often best. There is no need to force every problem into a constant-acceleration formula.

Signed velocity records direction. Speed is $\vert v\vert $. At a turning point in one-dimensional motion, $v=0$ and its sign changes; acceleration may be nonzero. When a formula gives $v^2$, choosing the square-root sign requires information about the direction of motion.

Piecewise motion needs matching conditions. Position is continuous unless the model contains an impossible instantaneous relocation. Velocity can jump only under an idealized impulse; ordinary finite acceleration keeps it continuous. An acceleration law that changes at a specified time should be integrated on each interval while carrying the ending position and velocity into the next.

## Cartesian motion and projectiles

In fixed Cartesian axes, the basis vectors do not change with time, so differentiation acts only on the scalar components:

$$
\mathbf v=\dot x\mathbf i+\dot y\mathbf j+\dot z\mathbf k,
$$

$$
\mathbf a=\ddot x\mathbf i+\ddot y\mathbf j+\ddot z\mathbf k.
$$

The component motions share the same time but otherwise can be integrated separately. For an ideal projectile with negligible air resistance and constant gravitational field,

$$
a_x=0,
\qquad
a_y=-g.
$$

Therefore

$$
x=x_0+v_{0x}t,
$$

$$
y=y_0+v_{0y}t-\frac12gt^2.
$$

The horizontal velocity stays constant while the vertical velocity changes linearly. The trajectory is parabolic only under these assumptions and only when horizontal velocity is nonzero. Air drag couples the components through speed, and a nonuniform gravitational field changes the curve.

Eliminating time can reveal path geometry, but it removes timing information. Conversely, a path equation such as $y=f(x)$ says where the particle travels but does not say how quickly it moves. A complete kinematic description needs a path plus one time law, or position coordinates directly as functions of time.

## Tangent-normal coordinates along a known path

Let $s$ be arc length, $\mathbf e_t$ the unit tangent in the direction of increasing $s$, and $\mathbf e_n$ the principal normal pointing toward the local center of curvature. Then

$$
\mathbf v=\dot s\,\mathbf e_t=v\mathbf e_t.
$$

Differentiate. The speed contributes $\dot v\mathbf e_t$. The tangent direction rotates as the particle advances. From the geometry of a smooth curve,

$$
\frac{d\mathbf e_t}{ds}=\frac{1}{\rho}\mathbf e_n,
$$

where $\rho$ is the radius of curvature. Since $ds/dt=v$,

$$
\frac{d\mathbf e_t}{dt}=\frac{v}{\rho}\mathbf e_n.
$$

Consequently,

$$
\boxed{\mathbf a=\dot v\mathbf e_t+\frac{v^2}{\rho}\mathbf e_n}.
$$

The tangential component $a_t=dot v$ changes speed. The normal component $a_n=v^2/\rho$ changes direction and always points toward the center of curvature. Constant-speed curved motion still has acceleration. At an inflection point the signed curvature changes sign and the center of curvature switches sides; using curvature magnitude with a locally chosen principal normal avoids sign confusion.

For a plane curve $y=f(x)$,

$$
\rho=\frac{\left[1+(dy/dx)^2\right]^{3/2}}
{|d^2y/dx^2|}.
$$

This coordinate system is efficient when speed and path shape are known at an instant. It is less useful when the curve itself must first be reconstructed from unrelated $x(t)$ and $y(t)$ data.

## Why polar acceleration has extra terms

For planar polar coordinates,

$$
\mathbf r=r\mathbf e_r.
$$

The basis vectors rotate with $\theta$. Written in fixed Cartesian vectors,

$$
\mathbf e_r=\cos\theta\mathbf i+\sin\theta\mathbf j,
$$

$$
\mathbf e_\theta=-\sin\theta\mathbf i+\cos\theta\mathbf j.
$$

Differentiation gives

$$
\dot{\mathbf e}_r=\dot\theta\mathbf e_\theta,
\qquad
\dot{\mathbf e}_\theta=-\dot\theta\mathbf e_r.
$$

Using the product rule once,

$$
\boxed{\mathbf v=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta}.
$$

Differentiating again, including the changing basis, gives

$$
\boxed{
\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r
+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta}.
$$

The term $-r\dot\theta^2$ is inward centripetal acceleration. The term $r\ddot\theta$ comes from angular acceleration. The term $2\dot r\dot\theta$ appears when radial motion occurs while the radial line rotates; it is the Coriolis term in this coordinate description.

Special cases check the formula. If $r=R$ is constant, then

$$
v=R\dot\theta,
\qquad
a_r=-R\dot\theta^2,
\qquad
a_\theta=R\ddot\theta.
$$

If $\dot\theta=0$, the basis stops rotating and the equations reduce to straight radial motion. Angular quantities must be in radians because the derivative relations for the basis vectors assume radian measure.

Cylindrical coordinates add independent vertical motion:

$$
\mathbf v=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta+\dot z\mathbf k,
$$

$$
\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r
+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta
+\ddot z\mathbf k.
$$

## Translating reference frames

If $B$ is described relative to a translating point $A$ whose reference axes remain parallel to fixed axes,

$$
\mathbf r_B=\mathbf r_A+\mathbf r_{B/A}.
$$

Direct differentiation gives

$$
\mathbf v_B=\mathbf v_A+\mathbf v_{B/A},
$$

$$
\mathbf a_B=\mathbf a_A+\mathbf a_{B/A}.
$$

This covers a person walking inside a train moving on a straight track, or a boat whose velocity relative to the water combines with the current. All terms must be expressed in the same coordinate basis before adding them.

These simple equations do not apply unchanged when the reference axes rotate. Rotating frames produce transport, centripetal, and Coriolis terms. Polar-coordinate differentiation already displays the same mechanism: components alone do not capture the changing directions of the basis vectors.

## Motion constrained by an inextensible cable

Connected particles often have dependent motion because a cable length is fixed. Write the total variable cable length before differentiating. Constant portions can be grouped into one constant, while every changing segment must appear with the correct multiplicity.

For example, suppose a movable pulley attached to block $B$ is supported by two vertical segments of one cable, while the free end is attached to block $A$. If downward coordinates are $y_A$ and $y_B$, the variable cable length has the form

$$
L=y_A+2y_B+\text{constant}.
$$

Because $L$ is constant,

$$
v_A+2v_B=0,
$$

and differentiating again gives

$$
a_A+2a_B=0.
$$

Thus $A$ moves twice as fast as $B$ in the opposite coordinate direction. The factor two comes from two cable segments changing when the movable pulley moves. It cannot be inferred reliably from the number of pulleys alone.

Signs depend on coordinate choices. If one coordinate is positive upward and the other downward, the algebraic relation changes sign even though the physical motion is unchanged. Drawing coordinate arrows beside the mechanism before writing $L$ prevents that ambiguity.

An inextensible cable constrains motion only while it remains taut. If a computed configuration would require a cable to push, the cable goes slack and the length relation no longer governs both particles. Elastic cables also require a deformation law; their length is then a dynamic variable rather than a constant constraint.

## Worked example: acceleration given by position

A slider moves along a straight track. At $x=0$, its speed is $3$ m/s in the positive direction. Its acceleration is $a(x)=2+0.5x$ m/s$^2$, with $x$ in meters. Find its speed at $x=8$ m.

Since acceleration is given by position, use

$$
a=v\frac{dv}{dx}.
$$

Separate and integrate between the known states:

$$
\int_3^v v\,dv=\int_0^8(2+0.5x)\,dx.
$$

The left side is

$$
\frac12(v^2-9).
$$

The right side is

$$
\left[2x+0.25x^2\right]_0^8=16+16=32.
$$

Therefore

$$
\frac12(v^2-9)=32,
$$

so

$$
v^2=73.
$$

The initial direction and positive acceleration show that the positive root is required:

$$
\boxed{v=8.54\ \text{m/s}}.
$$

Differentiating the integrated relation $v^2=9+4x+0.5x^2$ gives $2v\,dv/dx=4+x$, hence $v\,dv/dx=2+0.5x$, recovering the stated acceleration.

## Worked example: speed and curvature on a path

A particle follows $y=0.20x^2$, with $x$ and $y$ in meters. At $x=2$ m it moves in the direction of increasing $x$ with speed $6$ m/s, and its speed is increasing at $1.5$ m/s$^2$. Find its tangent-normal acceleration.

The path derivatives are

$$
\frac{dy}{dx}=0.40x,
\qquad
\frac{d^2y}{dx^2}=0.40.
$$

At $x=2$ m,

$$
\frac{dy}{dx}=0.80.
$$

The radius of curvature is

$$
\rho=\frac{(1+0.80^2)^{3/2}}{0.40}
=5.25\ \text{m}.
$$

The tangential component is given directly:

$$
a_t=\dot v=1.5\ \text{m/s}^2.
$$

The normal component is

$$
a_n=\frac{v^2}{\rho}
=\frac{6^2}{5.25}
=6.86\ \text{m/s}^2.
$$

Thus

$$
\boxed{\mathbf a=1.50\mathbf e_t+6.86\mathbf e_n\ \text{m/s}^2}.
$$

Because the parabola is concave upward, the principal normal at this point points toward the concave side. The acceleration magnitude is

$$
\lVert\mathbf a\rVert
=\sqrt{1.50^2+6.86^2}
=7.02\ \text{m/s}^2.
$$

## Worked example: a bead in a rotating radial slot

At an instant, a bead in a rotating slot has $r=0.80$ m, $\dot r=0.50$ m/s, $\ddot r=0.20$ m/s$^2$, $\dot\theta=3.0$ rad/s, and $\ddot\theta=1.5$ rad/s$^2$. Find its velocity and acceleration components.

The velocity components are

$$
v_r=\dot r=0.50\ \text{m/s},
$$

$$
v_\theta=r\dot\theta=0.80(3.0)=2.40\ \text{m/s}.
$$

Hence its speed is

$$
v=\sqrt{0.50^2+2.40^2}=2.45\ \text{m/s}.
$$

For acceleration,

$$
\begin{aligned}
a_r&=\ddot r-r\dot\theta^2\\
&=0.20-0.80(3.0)^2\\
&=-7.00\ \text{m/s}^2,
\end{aligned}
$$

and

$$
\begin{aligned}
a_\theta&=r\ddot\theta+2\dot r\dot\theta\\
&=0.80(1.5)+2(0.50)(3.0)\\
&=4.20\ \text{m/s}^2.
\end{aligned}
$$

Therefore

$$
\boxed{\mathbf a=-7.00\mathbf e_r+4.20\mathbf e_\theta\ \text{m/s}^2}.
$$

The inward radial term dominates the small outward $\ddot r$. Of the transverse acceleration, $1.20$ m/s$^2$ comes from angular acceleration and $3.00$ m/s$^2$ from the simultaneous radial and angular motion.

## Average quantities and instantaneous limits

Average velocity over an interval is

$$
\mathbf v_{\mathrm{avg}}=\frac{\Delta\mathbf r}{\Delta t},
$$

whereas average speed is distance traveled divided by elapsed time. They agree in magnitude only for motion along a straight line without reversal. On a closed lap, average velocity is zero while average speed is positive.

Instantaneous velocity is the limit of average velocity as the interval shrinks. Geometrically, the secant joining two positions approaches the tangent to the path. Instantaneous acceleration is the corresponding limit of velocity change divided by time. Since velocity change includes direction change, a speedometer alone cannot determine acceleration on a curved road.

Average acceleration,

$$
\mathbf a_{\mathrm{avg}}=\frac{\mathbf v_2-\mathbf v_1}{t_2-t_1},
$$

does not generally equal acceleration at the midpoint. It does equal the time average of acceleration over the interval. For constant acceleration the instantaneous and average values coincide, which is why the elementary formulas work so cleanly in that special case.

Measured position data bring a numerical issue. Differentiation amplifies noise, so velocity inferred from nearby position samples can fluctuate, and a second differentiation is worse. Wider finite-difference intervals suppress noise but blur rapid changes. The mathematical definitions remain exact; experimental estimates require a choice of sampling interval and often smoothing justified by the measurement process.

## Worked example: relative velocity across a river

A boat points due north and moves at $4.0$ m/s relative to the water. The river current is $1.5$ m/s due east. The river is $120$ m wide. Find the boat's velocity relative to the ground, crossing time, and downstream drift. Then find the heading required to arrive directly opposite while keeping the same speed relative to the water.

Let east be $+x$ and north be $+y$. For the first trip,

$$
\mathbf v_{B/G}
=\mathbf v_{B/W}+\mathbf v_{W/G}
=1.5\mathbf i+4.0\mathbf j\ \text{m/s}.
$$

Its ground speed is

$$
\lVert\mathbf v_{B/G}\rVert
=\sqrt{1.5^2+4.0^2}
=4.27\ \text{m/s}.
$$

Only the north component closes the $120$ m width, so

$$
t=\frac{120}{4.0}=30.0\ \text{s}.
$$

During that time the current carries the boat

$$
\Delta x=(1.5)(30.0)=45.0\ \text{m}
$$

downstream.

To arrive directly opposite, the boat's westward velocity relative to the water must cancel the eastward current. If $\alpha$ is the heading angle west of north,

$$
4.0\sin\alpha=1.5.
$$

Thus

$$
\alpha=\sin^{-1}\left(\frac{1.5}{4.0}\right)=22.0^\circ.
$$

The remaining northward ground component is

$$
v_y=4.0\cos22.0^\circ=3.71\ \text{m/s},
$$

and the new crossing time is

$$
t=\frac{120}{3.71}=32.4\ \text{s}.
$$

Aiming upstream removes drift but lengthens the crossing because part of the boat's fixed speed is spent opposing the current. If the current speed were greater than the boat's water-relative speed, no heading could produce zero downstream component.

## Choosing coordinates from the data

| Given information | Usually efficient coordinates | Reason |
|---|---|---|
| $x(t),y(t),z(t)$ or component accelerations | Fixed Cartesian | Basis vectors are constant |
| Speed and geometric path | Tangent-normal | Separates speed change from turning |
| Radius and angle on a rotating mechanism | Polar | Coordinates follow the geometry |
| Radius, angle, and height | Cylindrical | Adds an independent $z$ motion |
| Motion relative to translating nonrotating carrier | Relative Cartesian | Derivatives add directly |

Coordinate choice does not change the physical vector. Results obtained in two systems should agree after their components are transformed to the same basis. A familiar coordinate system can still be an inefficient one if it hides the supplied constraints.

## Checks and recurring mistakes

- Constant speed does not mean zero acceleration on a curved path. Inspect the direction of velocity as well as its magnitude.
- Constant-acceleration equations require constant vector components over the interval, not merely a one-dimensional sketch.
- A path equation alone supplies geometry, not timing. Add a speed law or one coordinate as a function of time.
- When $v^2$ is found by integration, choose the sign of $v$ from the actual direction and account for any turning point in the interval.
- Polar formulas require derivatives of the rotating basis. Omitting $-r\dot\theta^2$ or $2\dot r\dot\theta$ amounts to differentiating components but not directions.
- Use radians for angular rates in derivative formulas.
- Differentiate a final position expression to recover velocity, and differentiate velocity to recover acceleration. Initial conditions and units should survive both checks.

## Related pages

- [Particle kinetics with Newton's second law](/physics/mechanics/particle-kinetics-newton)
- [Work-energy methods](/physics/mechanics/work-energy-methods)
- [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)
- [Two-dimensional motion](/physics/general/two-dimensional-motion)
