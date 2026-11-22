---
title: One-Dimensional Kinematics
sidebar_position: 3
---

# One-Dimensional Kinematics

Kinematics describes motion without asking what force causes it. In one dimension, every vector points along one chosen axis, so direction can be carried by a plus or minus sign. That apparent simplicity puts more weight on definitions: position is not distance, velocity is not speed, and negative acceleration does not always mean slowing down.

## Position, displacement, and distance

Position $x(t)$ gives location relative to an origin. The origin is arbitrary; changing it changes every coordinate but not the physical motion. Displacement over an interval is

$$
\Delta x=x_f-x_i.
$$

It depends only on endpoints. Distance traveled is the total path length and is always nonnegative.

If a runner moves from $x=2\,\mathrm m$ to $x=10\,\mathrm m$ and then back to $x=6\,\mathrm m$, the displacement is

$$
\Delta x=6-2=4\,\mathrm m,
$$

while the distance is

$$
d=(10-2)+(10-6)=12\,\mathrm m.
$$

The difference appears whenever motion reverses.

Average velocity and average speed are likewise distinct:

$$
v_{\text{avg}}=\frac{\Delta x}{\Delta t},
\qquad
\text{average speed}=\frac{\text{distance}}{\Delta t}.
$$

A round trip has zero average velocity but nonzero average speed.

## Instantaneous velocity and acceleration

Average velocity over a shrinking time interval approaches the derivative

$$
v(t)=\frac{dx}{dt}.
$$

Speed is $\lvert v\rvert$. Acceleration is the rate at which velocity changes:

$$
a(t)=\frac{dv}{dt}=\frac{d^2x}{dt^2}.
$$

Acceleration and velocity can have either sign. An object speeds up when they have the same sign and slows down when their signs differ:

| Velocity | Acceleration | Speed |
|---|---|---|
| positive | positive | increasing |
| positive | negative | decreasing |
| negative | negative | increasing |
| negative | positive | decreasing |

A car moving left has negative velocity under a right-positive convention. If it accelerates left, acceleration is also negative and its speed increases. The phrase “negative acceleration” identifies direction, not a change in speed by itself.

Zero velocity at an instant does not imply zero acceleration. A ball at the top of its flight has $v=0$ and downward acceleration. Conversely, zero acceleration means constant velocity, which need not be zero.

## Reading motion graphs

The slope of a position-time graph is velocity. A steep positive slope means large positive velocity; a horizontal tangent means momentary rest; a negative slope means motion toward decreasing $x$. Curvature shows acceleration: if slopes become more positive, acceleration is positive.

The slope of a velocity-time graph is acceleration. Its signed area is displacement:

$$
\Delta x=\int_{t_i}^{t_f}v(t)\,dt.
$$

Area below the time axis contributes negative displacement. Distance requires integrating speed:

$$
d=\int_{t_i}^{t_f}\lvert v(t)\rvert\,dt.
$$

The signed area under an acceleration-time graph is velocity change:

$$
\Delta v=\int_{t_i}^{t_f}a(t)\,dt.
$$

There is no standard elementary interpretation for area under a position-time graph. A graph table should not suggest one merely to fill a cell.

Suppose velocity rises linearly from $2\,\mathrm{m/s}$ at $t=0$ to $8\,\mathrm{m/s}$ at $t=3\,\mathrm s$. The acceleration is the slope,

$$
a=\frac{8-2}{3}=2.0\,\mathrm{m/s^2}.
$$

Displacement is the trapezoid area:

$$
\Delta x=\frac12(2+8)(3)=15\,\mathrm m.
$$

The same result follows from average velocity because constant acceleration makes the velocity graph a straight line.

## Deriving the constant-acceleration equations

When acceleration is constant,

$$
a=\frac{v-v_0}{t},
$$

so

$$
v=v_0+at.
$$

Integrating velocity gives

$$
\begin{aligned}
x-x_0
&=\int_0^t(v_0+at')\,dt'\\
&=v_0t+\frac12at^2.
\end{aligned}
$$

Because velocity changes linearly, its average is

$$
v_{\text{avg}}=\frac{v_0+v}{2},
$$

and therefore

$$
x-x_0=\frac12(v_0+v)t.
$$

Eliminate time between $v=v_0+at$ and the displacement equation:

$$
v^2=v_0^2+2a(x-x_0).
$$

These four expressions contain the same model:

$$
\begin{aligned}
v &= v_0+at,\\
x &= x_0+v_0t+\frac12at^2,\\
v^2 &= v_0^2+2a(x-x_0),\\
x-x_0 &= \frac12(v_0+v)t.
\end{aligned}
$$

Choose the form that omits an unknown you do not need. None applies over an interval where acceleration varies. Piecewise-constant motion may be handled by applying them separately to each interval and carrying final conditions from one stage into the next.

## Braking distance and reaction distance

A car travels initially at $25\,\mathrm{m/s}$ and then brakes at constant acceleration $-6.0\,\mathrm{m/s^2}$. With forward positive and final velocity zero,

$$
0=25^2+2(-6.0)\Delta x.
$$

Thus

$$
\Delta x=\frac{-25^2}{-12.0}=52.1\,\mathrm m.
$$

Stopping time is

$$
t=\frac{0-25}{-6.0}=4.17\,\mathrm s.
$$

The braking displacement is positive because the car continues forward while slowing.

Real stopping distance also includes driver reaction. For a reaction time of $0.75\,\mathrm s$ at constant initial speed,

$$
d_{\text{reaction}}=v_0t_r
=(25)(0.75)=18.8\,\mathrm m.
$$

Total distance is

$$
d_{\text{total}}=18.8+52.1=70.9\,\mathrm m.
$$

At fixed braking acceleration, braking distance scales as $v_0^2$. Doubling speed doubles reaction distance but quadruples braking distance.

## Vertical motion under constant gravity

Near Earth's surface and without appreciable air resistance, every freely moving object has downward acceleration of magnitude $g\approx9.8\,\mathrm{m/s^2}$. If upward is positive,

$$
a=-g.
$$

The sign belongs to the coordinate choice. If downward were positive, the same physical acceleration would be $+g$.

A ball is thrown upward from ground level at $18\,\mathrm{m/s}$. At maximum height, $v=0$ while $a=-g$:

$$
0=18^2+2(-9.8)\Delta y.
$$

Hence

$$
\Delta y=\frac{18^2}{19.6}=16.5\,\mathrm m.
$$

Time to the top is

$$
0=18-9.8t,
$$

so

$$
t_{\text{up}}=1.84\,\mathrm s.
$$

Returning to launch height takes another $1.84\,\mathrm s$ under the ideal model, and the final velocity is $-18\,\mathrm{m/s}$. That symmetry fails with air resistance or if final height differs from launch height.

## Worked drop from a moving elevator

An elevator moves upward at constant $3.0\,\mathrm{m/s}$ when a bolt falls from its ceiling, $2.5\,\mathrm m$ above the floor. How long until the bolt hits the floor?

Use an Earth-fixed frame with upward positive. At release, bolt and floor both move upward at $3.0\,\mathrm{m/s}$. Let the floor's initial position be zero:

$$
y_f(t)=3.0t.
$$

The bolt begins at $2.5\,\mathrm m$ with the same velocity and acceleration $-g$:

$$
y_b(t)=2.5+3.0t-\frac12gt^2.
$$

Set their positions equal:

$$
2.5+3.0t-\frac12gt^2=3.0t.
$$

The common velocity terms cancel:

$$
2.5-\frac12(9.8)t^2=0.
$$

Therefore

$$
t=\sqrt{\frac{2(2.5)}{9.8}}=0.714\,\mathrm s.
$$

The answer is the same as dropping through $2.5\,\mathrm m$ in a frame moving uniformly with the elevator. A common initial velocity does not change relative motion.

## Meeting and overtaking problems

Two objects meet when their positions are equal at the same time. Their speeds need not be equal.

Suppose cyclist A passes $x=0$ at constant $6.0\,\mathrm{m/s}$. Cyclist B passes the same point $5.0\,\mathrm s$ later at $8.0\,\mathrm{m/s}$. Set $t=0$ when B starts. A then has a $30\,\mathrm m$ lead:

$$
x_A=30+6.0t,
\qquad
x_B=8.0t.
$$

Equating positions,

$$
30+6.0t=8.0t,
$$

so

$$
t=15\,\mathrm s.
$$

They meet at

$$
x=(8.0)(15)=120\,\mathrm m
$$

from the origin. Subtracting speeds first gives the same result: B closes a $30\,\mathrm m$ gap at $2.0\,\mathrm{m/s}$.

## Variable acceleration

When acceleration depends on time,

$$
v(t)=v_0+\int_0^t a(t')\,dt',
$$

and

$$
x(t)=x_0+\int_0^t v(t')\,dt'.
$$

For $a(t)=kt$, integration gives

$$
v(t)=v_0+\frac12kt^2
$$

and

$$
x(t)=x_0+v_0t+\frac16kt^3.
$$

Substituting an “average acceleration” into constant-acceleration equations is generally unsafe unless the relevant integral relations are preserved.

If acceleration is given as a function of position, use the chain rule:

$$
a=\frac{dv}{dt}
=\frac{dv}{dx}\frac{dx}{dt}
=v\frac{dv}{dx}.
$$

Then

$$
v\,dv=a(x)\,dx,
$$

which can be integrated without first finding time.

## A position function contains the whole motion

Suppose

$$
x(t)=2.0+6.0t-1.5t^2
$$

in meters, with time in seconds. Differentiation gives

$$
v(t)=6.0-3.0t
$$

and

$$
a(t)=-3.0\,\mathrm{m/s^2}.
$$

The particle changes direction when velocity crosses zero:

$$
6.0-3.0t=0,
$$

so $t=2.0\,\mathrm s$. Its turning position is

$$
x(2.0)=2.0+12.0-6.0=8.0\,\mathrm m.
$$

From $t=0$ to $t=4.0\,\mathrm s$, the final position is

$$
x(4.0)=2.0+24.0-24.0=2.0\,\mathrm m.
$$

Displacement over the four seconds is zero. Distance is the outward $6.0\,\mathrm m$ plus the return $6.0\,\mathrm m$, totaling $12.0\,\mathrm m$. Integrating the absolute value of velocity gives the same result, but the integral must be split where $v=0$.

Average velocity over the interval is zero, even though the average of the initial and final speeds is $6.0\,\mathrm{m/s}$. The shortcut $(v_i+v_f)/2$ uses signed velocities and requires constant acceleration; using speed discards the reversal.

## Dropping from a height

A stone is released from rest from a bridge $45.0\,\mathrm m$ above water. Neglect air resistance. Choose downward as positive and the release point as $y=0$. Then $v_0=0$ and $a=g$:

$$
45.0=\frac12gt^2.
$$

Thus

$$
t=\sqrt{\frac{2(45.0)}{9.8}}
=3.03\,\mathrm s.
$$

Impact velocity is

$$
v=gt=(9.8)(3.03)=29.7\,\mathrm{m/s}
$$

downward. The time-free equation checks it:

$$
v=\sqrt{2g\Delta y}
=\sqrt{2(9.8)(45.0)}
=29.7\,\mathrm{m/s}.
$$

If the stone were thrown downward, $v_0$ would be positive under this convention. If upward were chosen positive instead, displacement and acceleration would both be negative. Either convention gives the same physical impact speed.

Sound travel can matter in timing observations. If an observer on the bridge hears the splash after a total delay, that delay includes fall time plus sound propagation back upward. Treating the entire delay as free-fall time overestimates the height.

## Piecewise motion

A subway train accelerates from rest at $1.2\,\mathrm{m/s^2}$ for $10\,\mathrm s$, cruises for $20\,\mathrm s$, then brakes uniformly to rest in $8.0\,\mathrm s$.

After acceleration,

$$
v_1=(1.2)(10)=12\,\mathrm{m/s},
$$

and

$$
\Delta x_1=\frac12(1.2)(10)^2=60\,\mathrm m.
$$

During cruise,

$$
\Delta x_2=(12)(20)=240\,\mathrm m.
$$

During braking, average velocity is

$$
v_{\text{avg}}=\frac{12+0}{2}=6.0\,\mathrm{m/s},
$$

so

$$
\Delta x_3=(6.0)(8.0)=48\,\mathrm m.
$$

Total distance and time are

$$
d=60+240+48=348\,\mathrm m,
$$

$$
\Delta t=10+20+8=38\,\mathrm s.
$$

The trip's average speed is

$$
\frac{348}{38}=9.16\,\mathrm{m/s}.
$$

A single constant-acceleration equation cannot cover the full trip. Velocity is continuous at the boundaries, while acceleration changes abruptly in the idealized model.

## Average acceleration can conceal the path

Two motions with the same initial velocity, final velocity, and elapsed time have the same average acceleration,

$$
a_{\text{avg}}=\frac{v_f-v_i}{\Delta t},
$$

but can have different displacements. One may accelerate early and then coast; another may coast and accelerate late. Their velocity-time graphs have the same endpoints but different areas.

Similarly, average velocity does not identify velocity at the midpoint in time. Equality between average velocity and $(v_i+v_f)/2$ relies on a linear velocity-time graph. For arbitrary motion, only the displacement divided by elapsed time is guaranteed.

## Numerical data and finite differences

Experimental positions are often available at discrete times rather than as a formula. A central-difference estimate of velocity is

$$
v(t_i)\approx\frac{x_{i+1}-x_{i-1}}{t_{i+1}-t_{i-1}}.
$$

Acceleration can be estimated from velocity data in the same way. Smaller time spacing can improve time resolution but makes measurement noise more prominent in derivatives. Smoothing or fitting a physically motivated model may be better than repeatedly differencing noisy data.

Numerical integration works in the other direction. Areas under measured acceleration data estimate velocity change, and areas under velocity data estimate displacement. Trapezoids usually improve on rectangular approximations when samples are not extremely close.

The distinction between measurement noise and real changes matters. A jagged numerical derivative does not automatically imply rapidly fluctuating physical acceleration.

## Reference frames and relative position

Position depends on the chosen reference frame. If frame $S'$ moves at constant velocity $V$ relative to frame $S$ and their origins coincide at $t=0$, Galilean kinematics gives

$$
x'=x-Vt.
$$

Differentiation gives

$$
v'=v-V,
\qquad
a'=a.
$$

All constant-velocity frames therefore agree on acceleration in Newtonian mechanics. A passenger walking forward at $1.5\,\mathrm{m/s}$ relative to a train moving at $20\,\mathrm{m/s}$ has ground velocity $21.5\,\mathrm{m/s}$. Walking backward at the same relative speed gives $18.5\,\mathrm{m/s}$ forward relative to ground.

This rule fails when speeds approach light speed, where Lorentz transformations replace Galilean ones. It also needs modification in accelerating frames, which introduce apparent forces if Newton's laws are written from within them.

## Finding extrema from velocity

Maximum or minimum position occurs where $v=dx/dt=0$, but a zero derivative alone does not distinguish the two. Check the sign of velocity on both sides or inspect acceleration. If velocity changes from positive to negative, position has a local maximum; negative to positive gives a local minimum.

A zero of acceleration marks an extremum of velocity only if acceleration changes sign. It does not necessarily mark an extremum of position. These derivative tests carry over from calculus but their physical wording helps avoid mixing the graphs.

For

$$
v(t)=3t^2-12t+9,
$$

velocity vanishes at $t=1\,\mathrm s$ and $t=3\,\mathrm s$. Factoring gives

$$
v=3(t-1)(t-3).
$$

It is positive before $1\,\mathrm s$, negative between the roots, and positive after $3\,\mathrm s$. Position therefore has a local maximum at the first root and a local minimum at the second.

## Model boundaries in free fall

Constant $g$ is a near-surface approximation. At heights comparable with Earth's radius, gravitational acceleration changes appreciably and inverse-square dynamics is needed. Air resistance depends on shape, area, air density, and speed; it breaks the upward-downward symmetry of vacuum motion.

With drag, a falling object approaches terminal speed rather than accelerating indefinitely. A thrown object usually returns to launch height with smaller speed than it had at launch because drag converts mechanical energy into thermal energy. Treating $a=-g$ remains valuable when drag is negligible over the required accuracy and distance.

Objects of different mass share the same vacuum acceleration. Differences seen in air arise mainly from drag relative to weight, not from a different gravitational acceleration. A crumpled and flat sheet of the same paper make that distinction clear.

## Sign and model checks

- Declare the positive direction once and keep it through the calculation.
- A negative result usually reports direction relative to the chosen axis.
- Separate distance from displacement whenever velocity changes sign.
- At a turning point, velocity can vanish while acceleration remains nonzero.
- Constant-acceleration formulas require constant acceleration over the chosen interval.
- Check graph areas with units: area under $v(t)$ has units of length, while area under $a(t)$ has units of velocity.
- Reject extraneous negative times when the problem begins at $t=0$, unless an earlier event is physically relevant.

<div className="see-also">

See also: [Measurement, Units, and Vectors](/physics/general/measurement-units-and-vectors) · [Two-Dimensional Motion](/physics/general/two-dimensional-motion) · [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications)

</div>
