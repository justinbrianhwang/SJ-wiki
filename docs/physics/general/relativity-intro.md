---
title: Relativity Intro
sidebar_position: 25
---

# Relativity Intro

Special relativity describes measurements made by inertial observers when relative speeds are not negligible compared with the speed of light. It does not say that every statement is subjective. Observers can disagree about elapsed time, length, and simultaneity while agreeing on invariant spacetime intervals and the laws relating their measurements.

## The two postulates

Einstein's formulation begins with two statements:

1. The laws of physics have the same form in every inertial frame.
2. Light in vacuum has the same speed $c$ for every inertial observer, independent of source or observer motion.

The first rules out a preferred state of uniform motion. The second conflicts with Galilean velocity addition. Reconciliation requires space and time coordinates to mix between frames.

An event is something assigned coordinates $(t,x,y,z)$ in a frame: a flash emitted, a detector clicked, or two objects crossed. Coordinate comparisons must refer to the same events. Vague phrases such as “the time of the trip” conceal which pair of events defines the interval.

The invariant speed is exactly

$$
c=299\,792\,458\,\mathrm{m/s}.
$$

Ordinary mechanics remains an excellent approximation when $v/c$ is small.

## The Lorentz factor

Most results contain

$$
\gamma=\frac{1}{\sqrt{1-\beta^2}},
\qquad
\beta=\frac{v}{c}.
$$

It satisfies $\gamma\ge1$ and grows without bound as $v$ approaches $c$. At low speed, a binomial expansion gives

$$
\gamma\approx1+\frac12\frac{v^2}{c^2}+\cdots.
$$

The small correction explains why relativistic effects are inconspicuous in daily motion.

| Speed | $\gamma$ |
|---|---:|
| $0.10c$ | $1.005$ |
| $0.50c$ | $1.155$ |
| $0.80c$ | $1.667$ |
| $0.98c$ | $5.025$ |

Massive particles cannot be accelerated to $c$ because their required energy grows without limit. Light travels at $c$ in vacuum because photons have zero rest mass.

## Time dilation from a light clock

Imagine a clock that ticks when a light pulse travels between two mirrors separated by proper distance $D$. In the clock's rest frame, one half-tick takes

$$
\Delta t_0=\frac{D}{c}.
$$

In a frame where the clock moves sideways at speed $v$, the pulse follows a diagonal path. During half a tick, Pythagoras gives

$$
(c\Delta t)^2=D^2+(v\Delta t)^2.
$$

Substitute $D=c\Delta t_0$:

$$
c^2\Delta t^2=c^2\Delta t_0^2+v^2\Delta t^2.
$$

Solving,

$$
\Delta t=\frac{\Delta t_0}{\sqrt{1-v^2/c^2}}
=\gamma\Delta t_0.
$$

Proper time $\Delta t_0$ is the interval measured by one clock present at both events. Other inertial frames see those two events at different positions and measure a longer coordinate time.

Time dilation is reciprocal for uniform relative motion: each inertial observer says the other's moving clocks run slowly. There is no contradiction because the observers use different sets of synchronized clocks and disagree about simultaneity at separated locations.

## Worked muon lifetime

A muon has mean proper lifetime $2.20\,\mu\mathrm s$ and moves through a laboratory at $0.98c$. Its rest frame records decay at one location, so the proper interval belongs to the muon.

First,

$$
\gamma=\frac{1}{\sqrt{1-0.98^2}}=5.03.
$$

The mean laboratory lifetime is

$$
\Delta t=\gamma\Delta t_0
=(5.03)(2.20\,\mu\mathrm s)
=11.1\,\mu\mathrm s.
$$

Its mean laboratory travel distance is

$$
\begin{aligned}
d&=v\Delta t\\
&=(0.98)(3.00\times10^8)
(11.1\times10^{-6})\\
&=3.26\times10^3\,\mathrm m.
\end{aligned}
$$

Without time dilation, the classical estimate would be only about $647\,\mathrm m$. Atmospheric muons reaching Earth's surface are a familiar application of this effect, though real muons have a distribution of energies and decay times.

## Relativity of simultaneity

Suppose lightning strikes both ends of a train simultaneously in the ground frame. An observer at the train's midpoint moves toward the flash from the front and away from the flash from the rear, so the front flash reaches that observer first. This difference cannot be dismissed as light travel delay after frame coordinates are properly synchronized; the train frame assigns the strikes different times.

For two events, the Lorentz time transformation gives

$$
\Delta t'=\gamma\left(\Delta t-\frac{v\Delta x}{c^2}\right).
$$

If the ground frame has $\Delta t=0$ but the events are separated by $\Delta x\ne0$, then

$$
\Delta t'=-\gamma\frac{v\Delta x}{c^2}\ne0.
$$

Events simultaneous in one frame are generally not simultaneous in another. This result underlies length contraction: measuring a moving object's length requires simultaneous endpoint positions in the measuring frame, and another frame does not agree that those endpoint measurements were simultaneous.

## The Lorentz transformation

Let frame $S'$ move at speed $v$ along the positive $x$ direction relative to $S$, with origins coinciding at $t=t'=0$. Coordinates transform as

$$
\begin{aligned}
x'&=\gamma(x-vt),\\
t'&=\gamma\left(t-\frac{vx}{c^2}\right),\\
y'&=y,\\
z'&=z.
\end{aligned}
$$

The inverse is obtained by replacing $v$ with $-v$:

$$
\begin{aligned}
x&=\gamma(x'+vt'),\\
t&=\gamma\left(t'+\frac{vx'}{c^2}\right).
\end{aligned}
$$

At low speed and over scales where $vx/c^2$ is negligible, these approach the Galilean relations $x'=x-vt$ and $t'=t$.

Substitute a light ray $x=ct$ into the transformation:

$$
x'=\gamma(c-v)t,
$$

$$
t'=\gamma\left(1-\frac{v}{c}\right)t.
$$

Their ratio is $x'/t'=c$. Both frames measure the same light speed.

## Proper length and length contraction

Proper length $L_0$ is measured in the object's rest frame, where its endpoints are stationary. An observer who sees the object moving parallel to its length measures

$$
L=\frac{L_0}{\gamma}.
$$

Only the dimension parallel to relative velocity contracts. Perpendicular dimensions do not.

Consider a spacecraft with proper length $L_0=100\,\mathrm m$ moving at $0.80c$. Since $\gamma=1.667$,

$$
L=\frac{100}{1.667}=60.0\,\mathrm m.
$$

The laboratory must record front and rear positions at the same laboratory time. Observers aboard the craft do not regard those endpoint events as simultaneous, so they do not calculate their proper length from that pair.

Length contraction is not an optical photograph effect. Light travel times, aberration, and Doppler shift affect appearance separately. It is a statement about coordinates assigned by a synchronized measurement procedure.

## The spacetime interval

For two events, define

$$
\Delta s^2=c^2\Delta t^2-\Delta x^2-\Delta y^2-\Delta z^2.
$$

Every inertial frame obtains the same $\Delta s^2$. This invariant organizes causal structure:

| Interval | Condition | Possible relation |
|---|---|---|
| Timelike | $\Delta s^2\gt 0$ | one event can causally influence the other below $c$ |
| Lightlike | $\Delta s^2=0$ | connected by a light signal |
| Spacelike | $\Delta s^2\lt 0$ | no causal signal can connect them |

For timelike-separated events, a frame exists where they occur at the same place. Proper time satisfies

$$
c^2\Delta\tau^2=\Delta s^2.
$$

For spacelike-separated events, different frames can reverse their time order, but no cause-and-effect paradox follows because no signal traveling at or below $c$ can connect them.

## Velocity addition

Differentiate the Lorentz transformation for motion along $x$. If an object has velocity $u'$ in $S'$ and $S'$ moves at $v$ relative to $S$, then

$$
u=\frac{u'+v}{1+u'v/c^2}.
$$

For $u'=0.80c$ and $v=0.80c$,

$$
u=\frac{1.60c}{1+0.64}
=0.976c.
$$

Galilean addition would give $1.60c$, while the relativistic result remains below $c$. Setting $u'=c$ gives $u=c$ for every allowed $v$.

At low speeds, $u'v/c^2$ is negligible and $u\approx u'+v$. The relativistic rule contains the classical one as a limit.

Transverse velocity components also transform and include factors of $\gamma$. The collinear expression should not be applied unchanged to arbitrary vector directions.

## Momentum and energy

Relativistic momentum is

$$
\vec p=\gamma m\vec v,
$$

and total energy is

$$
E=\gamma mc^2.
$$

Rest energy is

$$
E_0=mc^2,
$$

so kinetic energy is

$$
K=E-E_0=(\gamma-1)mc^2.
$$

Energy and momentum satisfy

$$
E^2=(pc)^2+(mc^2)^2.
$$

For a photon $m=0$, this reduces to $E=pc$. For a massive particle at rest, $p=0$ and $E=mc^2$.

At low speed,

$$
K=(\gamma-1)mc^2
\approx\frac12mv^2,
$$

recovering classical kinetic energy.

### Worked electron energy

An electron moves at $0.80c$. With $\gamma=1.667$,

$$
K=(1.667-1)m_ec^2
=0.667m_ec^2.
$$

Using $m_ec^2=511\,\mathrm{keV}$,

$$
K=(0.667)(511\,\mathrm{keV})
=341\,\mathrm{keV}.
$$

The classical estimate is

$$
K_{\text{classical}}=\frac12m_e(0.80c)^2
=0.32m_ec^2
=164\,\mathrm{keV},
$$

less than half the relativistic value. Relativistic momentum is similarly larger than $m_ev$ by the factor $\gamma$.

## The twin journey

If one twin travels rapidly and returns, less proper time can elapse along the traveler's path than along the stay-at-home twin's path. This is not a contradiction with reciprocal time dilation during uniform legs. The traveling twin changes inertial frames at turnaround, while the stay-at-home twin remains approximately in one frame.

The invariant calculation compares proper time along two different spacetime paths:

$$
\Delta\tau=\int dt\sqrt{1-\frac{v(t)^2}{c^2}}.
$$

Acceleration marks the asymmetry, but the age difference can be calculated by integrating the constant-speed legs; long acceleration is not required. General relativity is unnecessary for the ideal flat-spacetime version.

## Doppler shift for light

Relative motion changes measured light frequency. For source and receiver receding directly at speed $v$, the relativistic longitudinal Doppler relation is

$$
f_{\text{obs}}=f_{\text{src}}
\sqrt{\frac{1-\beta}{1+\beta}}.
$$

Approach reverses the sign of $\beta$, producing a blueshift. Unlike the classical sound Doppler effect, no material medium supplies a preferred frame. Time dilation contributes essentially to the relativistic result.

## Synchronizing distant clocks

An inertial frame needs more than one clock to assign times at separated locations. Einstein synchronization places identical clocks at rest throughout the frame and uses light signals. If a signal leaves clock A at $t_1$, reflects from clock B, and returns to A at $t_2$, B is set to

$$
t_B=\frac{t_1+t_2}{2}
$$

at reflection. The rule uses equal outward and return light speeds in that frame.

Another inertial frame moving relative to these clocks does not regard them as synchronized. The disagreement is the operational content of relativity of simultaneity, not a defect in either clock.

Clock synchronization also explains why one cannot compare distant moving clocks by merely looking at them. Signal travel time and relativistic coordinate assignment must be separated. Local meetings of clocks are events that all observers agree occurred, even though they assign different coordinates.

## Energy-momentum conservation

Relativistic energy and momentum are conserved in isolated interactions. Pair creation and annihilation make rest energy especially concrete. A photon cannot create an electron-positron pair in empty space by itself because energy-momentum conservation cannot be satisfied; a nearby nucleus can recoil and carry momentum.

Conversely, an electron and positron annihilating from rest can produce two photons moving in opposite directions. Two are needed so total momentum remains zero. Their total energy equals the initial rest energy plus any kinetic energy.

The invariant mass of a system depends on total energy and total momentum:

$$
M^2c^4=E_{\text{tot}}^2-p_{\text{tot}}^2c^2.
$$

It need not equal the sum of component rest masses. Two photons individually have zero rest mass, yet a pair moving in opposite directions has zero total momentum and positive total energy, so the system has positive invariant mass.

### Threshold energy and center-of-momentum motion

In a fixed-target collision, some incoming energy must remain as kinetic energy of the center of momentum after new particles are produced. Supplying only the sum of final rest energies is therefore insufficient. Colliding equal-energy beams head-on is more efficient for particle creation because their total laboratory momentum can be zero, making the laboratory the center-of-momentum frame.

This distinction is why modern high-energy colliders use opposing beams. It follows directly from conserving the four-component energy-momentum quantity, not from a failure of energy conservation in fixed-target experiments.

## Constant proper acceleration

Special relativity can describe acceleration; it is not restricted to objects that never accelerate. An inertial frame covers free observers, while an accelerating traveler can be analyzed through a sequence of momentarily comoving inertial frames.

Proper acceleration is what an onboard accelerometer reads. Under constant proper acceleration, coordinate acceleration measured in the original inertial frame decreases as speed approaches $c$. The traveler can continue to gain energy and rapidity without crossing the light-speed limit.

Rapidity $\eta$ is defined by

$$
\tanh\eta=\frac{v}{c}.
$$

Collinear rapidities add linearly. Since $\tanh\eta$ remains below one for finite $\eta$, this gives another way to see why repeated boosts never carry a massive object past $c$.

## Causality and faster-than-light signals

For spacelike-separated events, some inertial frames reverse their temporal order. If controllable signals could travel faster than light, a change of frame could turn reception into an event preceding transmission, allowing causal loops when signals are exchanged.

The light cone separates events reachable by subluminal influence from spacelike events. Massive particles follow timelike paths inside the cone; light follows its boundary. Lorentz transformations preserve this classification.

Phase velocities can exceed $c$ in some wave settings, and a light pulse can show unusual peak motion in dispersive media. Such behavior does not transmit information faster than $c$. The relevant causal front and locally transferable information remain constrained.

## Gravity and the boundary of special relativity

Special relativity assumes flat spacetime and inertial frames, though it can handle accelerated coordinates. Gravitation in modern physics is described by general relativity, where mass-energy curves spacetime.

Local freely falling laboratories still recover special relativity over sufficiently small regions. Over larger regions, gravitational time dilation, curved trajectories, and tidal effects require the general theory. Newtonian gravity remains highly accurate for weak fields and low speeds, while special-relativistic corrections handle fast motion without strong spacetime curvature.

## Frame and limit checks

- Name the two events before deciding which interval is proper time.
- Proper length belongs to the object's rest frame.
- Length contraction applies only parallel to relative motion.
- Simultaneity of separated events depends on frame.
- Replace Galilean velocity addition at relativistic speed.
- Use $\gamma mv$ and $(\gamma-1)mc^2$, not “relativistic mass.”
- Check that every expression approaches its Newtonian form as $v/c\to0$.
- No inertial frame moves with a photon, so a photon's “point of view” is not a valid rest-frame argument.

<div className="see-also">

See also: [Gravitation and Kepler's Laws](/physics/general/gravitation-and-keplers-laws) · [Quantum Intro: Photons and Matter Waves](/physics/general/quantum-intro-photons-and-matter-waves) · [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics)

</div>
