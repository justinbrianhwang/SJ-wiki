---
title: "Gravitation and Kepler's Laws"
sidebar_position: 10
---

# Gravitation and Kepler's Laws

Newtonian gravitation joins phenomena that once looked unrelated: falling bodies, the Moon's motion, planetary orbits, tides, and the trajectories of artificial satellites. Its inverse-square form is simple, but orbital motion demands careful bookkeeping of radius, energy, and angular momentum.

Kepler obtained his laws empirically from astronomical data. Newton later showed that an inverse-square central force produces those laws. The route from force to orbit is one of the cleanest examples of a model explaining earlier regularities.

## The inverse-square field

Two point masses separated by distance $r$ attract with magnitude

$$
F=G\frac{m_1m_2}{r^2}.
$$

In vector form, the force on mass $m$ at position $\vec r$ relative to mass $M$ is

$$
\vec F=-\frac{GMm}{r^3}\vec r.
$$

The minus sign points toward the source. Newton's third law gives an equal and opposite force on $M$; treating $M$ as fixed is an approximation valid when $M\gg m$.

The gravitational field is force per unit test mass:

$$
\vec g(\vec r)=\frac{\vec F}{m}
=-\frac{GM}{r^3}\vec r.
$$

Outside a spherically symmetric body, the field is exactly the same as if all mass were concentrated at its center. Inside a uniform spherical shell, contributions from different directions cancel and the field is zero. For a uniform solid sphere of density $\rho$, only the mass inside radius $r$ contributes:

$$
M(r)=\frac43\pi r^3\rho,
$$

so

$$
g(r)=\frac{GM(r)}{r^2}
=\frac43\pi G\rho r.
$$

The field therefore grows linearly from zero at the center, reaches its surface value, and then falls as $1/r^2$. Real planets are layered rather than uniform, but the argument shows why blindly extending $GM/r^2$ to the center is wrong.

Near Earth's surface, write $r=R_E+h$. When $h\ll R_E$, the fractional change in $g$ is small, and a constant value near $9.8\,\mathrm{m/s^2}$ is adequate. At orbital heights the full radial dependence matters.

## Potential energy and the meaning of its sign

For any conservative radial force,

$$
U(r)-U(\infty)=-\int_\infty^r \vec F\cdot d\vec r.
$$

Choosing $U(\infty)=0$ and integrating the inverse-square force gives

$$
U(r)=-\frac{GMm}{r}.
$$

The value is negative because a mass at finite $r$ is bound relative to the zero at infinity. Increasing $r$ raises $U$ toward zero. The difference between two radii is

$$
\Delta U=GMm\left(\frac{1}{r_i}-\frac{1}{r_f}\right).
$$

For a small height $h$ near the surface, expand $1/(R_E+h)$ to first order:

$$
\frac{1}{R_E+h}\approx\frac{1}{R_E}-\frac{h}{R_E^2}.
$$

Then

$$
\Delta U\approx\frac{GM_Em}{R_E^2}h=mgh.
$$

The familiar $mgh$ is thus a local approximation to the inverse-radius potential, not a competing formula.

## Circular orbits are continuous free fall

A satellite in a circular orbit accelerates toward the central body while its tangential velocity continually carries it past the surface. Gravity supplies the required radial force:

$$
\frac{GMm}{r^2}=\frac{mv^2}{r}.
$$

The satellite mass cancels:

$$
v_c=\sqrt{\frac{GM}{r}}.
$$

Using $v_c=2\pi r/T$ gives

$$
T=2\pi\sqrt{\frac{r^3}{GM}},
\qquad
T^2=\frac{4\pi^2}{GM}r^3.
$$

The kinetic energy of the circular orbit is

$$
K=\frac12mv_c^2=\frac{GMm}{2r}.
$$

Adding potential energy yields

$$
E=K+U=-\frac{GMm}{2r}.
$$

These relations produce a result that initially feels backward: a higher circular orbit has lower speed but greater total energy. Raising the satellite makes its potential energy much less negative; half of that energy increase appears as a decrease in kinetic energy after the new circular orbit is established.

| Quantity | Circular-orbit value | Radial scaling |
|---|---|---|
| Field magnitude | $GM/r^2$ | $r^{-2}$ |
| Speed | $\sqrt{GM/r}$ | $r^{-1/2}$ |
| Period | $2\pi\sqrt{r^3/(GM)}$ | $r^{3/2}$ |
| Kinetic energy | $GMm/(2r)$ | $r^{-1}$ |
| Total energy | $-GMm/(2r)$ | approaches zero below |

## Worked orbit: altitude is not orbital radius

Find the circular speed and period of a satellite $400\,\mathrm{km}$ above Earth. Use $R_E=6.37\times10^6\,\mathrm m$ and $GM_E=3.986\times10^{14}\,\mathrm{m^3/s^2}$.

The center-to-center radius is

$$
\begin{aligned}
r&=R_E+h\\
&=6.37\times10^6+0.400\times10^6\\
&=6.77\times10^6\,\mathrm m.
\end{aligned}
$$

Then

$$
\begin{aligned}
v_c
&=\sqrt{\frac{3.986\times10^{14}}{6.77\times10^6}}\\
&=7.67\times10^3\,\mathrm{m/s}.
\end{aligned}
$$

The period is

$$
\begin{aligned}
T&=\frac{2\pi r}{v_c}\\
&=\frac{2\pi(6.77\times10^6)}{7.67\times10^3}\\
&=5.55\times10^3\,\mathrm s\\
&=92.5\,\mathrm{min}.
\end{aligned}
$$

Using the altitude $400\,\mathrm{km}$ as $r$ would put the satellite inside Earth and give a meaningless result.

## Why Kepler's second law follows from a central force

Gravity always points along $\vec r$, so its torque about the central mass is zero:

$$
\vec\tau=\vec r\times\vec F=0.
$$

Hence angular momentum $\vec L=\vec r\times m\vec v$ is conserved. During a short time $dt$, the radius vector sweeps a narrow triangle of area

$$
dA=\frac12r v_\perp\,dt.
$$

Since $L=mrv_\perp$,

$$
\frac{dA}{dt}=\frac{L}{2m},
$$

which is constant. Equal areas are swept in equal times. Near periapsis the radius is smaller, so the tangential speed must be larger; near apoapsis the body moves more slowly.

This argument uses only the fact that the force is central. The elliptical shape and the period-semimajor-axis relation depend on the inverse-square form.

## Ellipses, energy, and Kepler's first and third laws

A bound orbit under an inverse-square force is an ellipse with the central mass at one focus. In polar coordinates its shape may be written

$$
r(\theta)=\frac{p}{1+e\cos\theta},
$$

where $e$ is eccentricity and $p$ is the semilatus rectum. A circle has $e=0$; bound ellipses have $0\lt e\lt 1$. The closest and farthest distances are

$$
r_p=a(1-e),
\qquad
r_a=a(1+e),
$$

with semimajor axis $a$.

For any bound Kepler ellipse, the total mechanical energy depends only on $a$:

$$
E=-\frac{GMm}{2a}.
$$

Combining energy conservation with the potential gives the vis-viva equation,

$$
v^2=GM\left(\frac{2}{r}-\frac{1}{a}\right).
$$

It reduces to the circular result when $r=a$. It also shows directly that speed is greatest at periapsis.

Kepler's third law for two bodies orbiting their common center of mass is

$$
T^2=\frac{4\pi^2}{G(M+m)}a^3.
$$

When $m\ll M$, the denominator becomes $GM$. The orbital period depends on semimajor axis, not eccentricity. Two ellipses around the same mass with equal $a$ have equal periods even if their shapes differ.

Historically, Kepler described these relations from Tycho Brahe's observations before a dynamical cause was known. Newton's mechanics explained them and also predicted non-elliptic trajectories: parabolas at zero total energy and hyperbolas at positive energy.

## The two-body correction

Neither body is truly stationary. Both orbit their common center of mass, or barycenter. Their distances $r_M$ and $r_m$ from that point satisfy

$$
Mr_M=mr_m,
\qquad
r_M+r_m=r.
$$

For a planet orbiting a much heavier star, the barycenter lies close to the star's center, so fixing the star is an excellent first approximation. For comparable masses, as in a binary-star system, both motions are conspicuous. The relative separation still follows a Kepler orbit, but the gravitational parameter is $G(M+m)$ rather than $GM$.

This correction also explains how an unseen companion can be detected. The visible star executes a small orbit about the barycenter, periodically changing its position or line-of-sight velocity. Inferring a companion's properties then requires inclination information and careful observation, but the underlying motion is ordinary two-body dynamics.

The satellite's mass cancels from its acceleration only when inertial and gravitational mass are proportional. Galileo's falling-body result and later equivalence-principle tests support that equality to high precision. In Newtonian calculations it is built into the statement that all test masses at the same point share the same gravitational acceleration.

## Changing orbits takes two velocity changes

Moving between circular orbits is not achieved by pointing radially outward and coasting. A common ideal maneuver uses an elliptical transfer orbit tangent to both circles. From a lower circular orbit, a prograde burn increases tangential speed and raises the opposite side of the orbit. At the new apoapsis, a second prograde burn raises the periapsis and circularizes.

The first burn adds both kinetic and total energy. During the coast upward, kinetic energy falls while potential energy rises. At apoapsis the spacecraft moves more slowly than it did in the lower circle, yet it is generally not moving at the correct speed for the higher circular orbit. The second burn supplies the missing tangential speed.

For transfer semimajor axis $a_t=(r_1+r_2)/2$, vis-viva gives the transfer speeds:

$$
v_{t1}=\sqrt{GM\left(\frac{2}{r_1}-\frac{1}{a_t}\right)},
$$

$$
v_{t2}=\sqrt{GM\left(\frac{2}{r_2}-\frac{1}{a_t}\right)}.
$$

Compare these with circular speeds at $r_1$ and $r_2$ to obtain the two velocity increments. The ideal calculation neglects finite burn time, drag, plane changes, and perturbations. Still, it clarifies why “a higher orbit is slower” does not mean a spacecraft should fire backward to climb there.

An impulsive burn changes velocity immediately but leaves position unchanged. Energy and angular momentum therefore jump, selecting a new conic through the same point. Between burns, both quantities remain constant in the ideal two-body model.

## Tides come from field differences

Uniform gravitational acceleration moves every part of an extended body together. Tides arise from the variation of the field across the body. Along the line toward a distant mass $M$, compare the acceleration at radius $r$ with that at $r+\Delta r$. For $\Delta r\ll r$,

$$
\Delta g\approx\left|\frac{dg}{dr}\right|\Delta r
=\frac{2GM}{r^3}\Delta r.
$$

The tidal scale falls as $1/r^3$, faster than the field itself. A nearby less massive body can therefore raise stronger tides than a much more massive but distant one. On the near side of Earth, the Moon's pull exceeds the pull at Earth's center; on the far side it is weaker. Relative to the freely falling center, both differences stretch Earth along the Earth-Moon line. Compression occurs in transverse directions.

Calling the far-side bulge a result of the Moon “pulling water away from Earth” misses the reference frame. Earth and its oceans are all accelerating toward the Moon, but by slightly different amounts. Ocean dynamics, basin shapes, Earth's rotation, and the Sun then modify the simple equilibrium picture.

## Apparent weight in orbit

A scale reads a contact force, not gravitational force directly. In an elevator or spacecraft, apparent weight is the normal force required to keep a person following the vehicle's motion. During free fall, the person and vehicle accelerate together under gravity, so no supporting normal force is needed and the scale reads zero.

At $400\,\mathrm{km}$ altitude, the gravitational field is

$$
\frac{g(h)}{g(0)}
=\left(\frac{R_E}{R_E+h}\right)^2
=\left(\frac{6.37}{6.77}\right)^2
\approx0.885.
$$

Gravity there is about $89\%$ of its surface strength. Astronauts float because the station and everything inside it share the same orbital free fall. Small residual accelerations from drag, vibrations, and onboard motion motivate the term microgravity rather than perfect zero gravity.

## Spheres, shells, and when point-mass reasoning fails

The exterior point-mass result requires spherical symmetry. A planet's equatorial bulge and uneven density add corrections that slowly rotate an orbit's plane or apsidal line. Engineers exploit some of these perturbations, while precision orbit prediction must model many of them.

The shell theorem also has a subtle limitation: zero field inside a spherical shell does not mean zero potential. The potential is constant there,

$$
V=-\frac{GM}{R},
$$

for shell radius $R$. No force acts because the gradient is zero, yet moving a test mass from inside the shell to infinity still requires an energy change. Potential values and field gradients answer different questions.

For overlapping nonspherical bodies, extended galaxies, or points inside an irregular asteroid, summing or integrating the actual mass distribution replaces the point-mass shortcut. The inverse-square law remains the local rule for pairs of mass elements.

## Worked ellipse: speed at periapsis and apoapsis

A spacecraft orbits Earth with perigee radius $r_p=7.00\times10^6\,\mathrm m$ and apogee radius $r_a=1.30\times10^7\,\mathrm m$. First find

$$
a=\frac{r_p+r_a}{2}
=1.00\times10^7\,\mathrm m.
$$

At perigee, vis-viva gives

$$
\begin{aligned}
v_p
&=\sqrt{GM_E\left(\frac{2}{r_p}-\frac{1}{a}\right)}\\
&=\sqrt{(3.986\times10^{14})
\left(\frac{2}{7.00\times10^6}-\frac{1}{1.00\times10^7}\right)}\\
&=8.60\times10^3\,\mathrm{m/s}.
\end{aligned}
$$

At apogee,

$$
\begin{aligned}
v_a
&=\sqrt{(3.986\times10^{14})
\left(\frac{2}{1.30\times10^7}-\frac{1}{1.00\times10^7}\right)}\\
&=4.63\times10^3\,\mathrm{m/s}.
\end{aligned}
$$

Angular momentum supplies a separate check. At both apsides the velocity is perpendicular to the radius, so $r_pv_p$ should equal $r_av_a$. The products agree to rounding.

## Escape as an energy boundary

An object barely escaping reaches infinity with zero speed. Setting total energy to zero at launch radius $r$ gives

$$
\frac12mv_e^2-\frac{GMm}{r}=0,
$$

and therefore

$$
v_e=\sqrt{\frac{2GM}{r}}=\sqrt2\,v_c.
$$

At Earth's surface,

$$
v_e=\sqrt{\frac{2(3.986\times10^{14})}{6.37\times10^6}}
=1.12\times10^4\,\mathrm{m/s}.
$$

This value assumes an instantaneous unpowered launch, no atmosphere, and a nonrotating Earth. A rocket can escape without ever moving at $11.2\,\mathrm{km/s}$ relative to Earth at one instant because its engines add energy throughout the climb. Conversely, reaching that speed in the atmosphere would entail severe drag losses. Escape speed is best read as a specific-energy threshold.

The sign of total energy classifies ideal Kepler trajectories:

| Total energy | Orbit type | Long-term behavior |
|---|---|---|
| $E\lt 0$ | circle or ellipse | bound |
| $E=0$ | parabola | marginal escape |
| $E\gt 0$ | hyperbola | unbound with residual speed |

## Assumptions to keep in view

- Distances in gravity formulas are center-to-center. Altitude must be added to planetary radius.
- Constant $g$ and $mgh$ require height changes small compared with the planet's radius.
- Circular formulas cannot be substituted unchanged into an elliptical orbit. Use $a$, angular momentum, or vis-viva.
- The two-body model neglects other bodies, atmospheric drag, nonspherical mass distributions, and relativistic corrections.
- “Weightlessness” in orbit means free fall, not absence of gravity. At low-Earth-orbit altitude, gravitational field strength is still a large fraction of its surface value.

<div className="see-also">

See also: [Two-Dimensional Motion](/physics/general/two-dimensional-motion) · [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Rotation, Torque, and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum) · [Relativity Intro](/physics/general/relativity-intro)

</div>
