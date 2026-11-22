---
title: Linear Momentum and Collisions
sidebar_position: 7
---

# Linear Momentum and Collisions

Momentum tracks motion through brief interactions in which internal forces are large and external impulses are small. Collisions, explosions, recoil, and center-of-mass motion all fit this description. Total momentum can remain constant even when kinetic energy becomes sound, heat, or deformation.

## Momentum bookkeeping

- **Momentum:** $\vec p=m\vec v$.
- **Impulse:** $\vec J=\int\vec F\,dt=\Delta\vec p$.
- **Center of mass:** $M\vec r_{cm}=\sum_i m_i\vec r_i$.
- An **elastic collision** conserves kinetic energy as well as momentum.
- An **inelastic collision** conserves momentum but not kinetic energy; in a completely inelastic collision, the objects stick together.

Momentum and impulse are vectors, so a sign convention or component axes belong in the setup. The system is effectively isolated for momentum only when its external impulse is negligible over the interaction time.

Momentum is especially useful during a short collision. Contact forces between the bodies may be large, but they occur as equal and opposite internal pairs. Gravity or friction may act externally, yet their impulse over a few milliseconds can be negligible beside the collision impulse. Conservation is an approximation whose quality depends on the chosen system and time interval.

Impulse is the time integral of force:

$$
\vec J=\int_{t_i}^{t_f}\vec F\,dt.
$$

For constant force it reduces to $\vec F\Delta t$. For a changing force, it is the signed area under the force-time graph. Peak force alone does not determine momentum change. Extending collision time at the same impulse lowers average force, as in padding and airbags.

| Quantity or idea | Use | Check |
|---|---|---|
| Momentum | $m\vec v$ | resolve it by components |
| Impulse | area under a force-time curve | units equal momentum |
| Center of mass | mass-weighted system position | accelerates only under external force |
| Elasticity | kinetic-energy condition | test separately from momentum conservation |

## Conservation across an interaction

For a collection of particles,

$$
\vec P=\sum_i m_i\vec v_i=M\vec v_{cm},
$$

and the net external force controls its change:

$$
\sum\vec F_{ext}=\frac{d\vec P}{dt}.
$$

Integrating over the collision gives $\Delta\vec P=\vec J_{ext}$. If the external impulse is negligible,

$$
\vec P_i=\vec P_f.
$$

The center of mass is

$$
\vec r_{cm}=\frac{1}{M}\sum_i m_i\vec r_i.
$$

Differentiating twice gives

$$
M\vec a_{cm}=\sum\vec F_{ext}.
$$

Internal forces cancel. An explosion can send fragments in complicated directions, but their center of mass follows the motion dictated by external force. If a projectile explodes in flight and air resistance is negligible, its center of mass continues along the parabola the intact projectile would have followed.

For a completely inelastic one-dimensional collision,

$$
m_1v_{1i}+m_2v_{2i}=(m_1+m_2)v_f.
$$

An elastic one-dimensional collision supplies a second relation through the reversal of relative velocity:

$$
v_{1i}-v_{2i}=-(v_{1f}-v_{2f}).
$$

The relative-speed relation follows by factoring the kinetic-energy equation and dividing by the momentum equation. Solving the two conservation equations gives

$$
v_{1f}
=\frac{m_1-m_2}{m_1+m_2}v_{1i}
+\frac{2m_2}{m_1+m_2}v_{2i},
$$

$$
v_{2f}
=\frac{2m_1}{m_1+m_2}v_{1i}
+\frac{m_2-m_1}{m_1+m_2}v_{2i}.
$$

Equal masses exchange velocities. A light object striking a massive stationary wall reverses at nearly unchanged speed. Those limits are useful algebra checks.

The useful order is physical model first, algebra second. Choose the system boundary, state why external impulse can be neglected, assign component signs, and only then apply conservation. A symbolic result should also reveal dimensions and limiting behavior before numbers obscure them.

## A completely inelastic collision

**Problem.** A $0.20\,\mathrm{kg}$ cart moving at $3.0\,\mathrm{m/s}$ sticks to a $0.30\,\mathrm{kg}$ cart at rest. Find the final speed and kinetic energy lost.

Momentum is conserved, while kinetic energy is not. Initially,

$$
p_i=(0.20)(3.0)=0.60\,\mathrm{kg\,m/s}.
$$

After the carts stick,

$$
p_f=(0.50)v_f,
$$

so $v_f=0.60/0.50=1.2\,\mathrm{m/s}$. The kinetic energies are

$$
K_i=\frac12(0.20)(3.0)^2=0.90\,\mathrm{J}
$$

and

$$
K_f=\frac12(0.50)(1.2)^2=0.36\,\mathrm{J}.
$$

The collision converts $0.54\,\mathrm{J}$ of kinetic energy into other forms.

For any completely inelastic one-dimensional collision, the kinetic-energy loss can be written

$$
K_i-K_f
=\frac12\frac{m_1m_2}{m_1+m_2}
(v_{1i}-v_{2i})^2.
$$

Only relative motion is available for conversion. If both carts initially move together, sticking changes nothing and the loss is zero.

## Reading impulse from a force pulse

**Problem.** A triangular force pulse has base $0.030\,\mathrm{s}$ and height $120\,\mathrm{N}$. Find its impulse and the speed change of a $0.15\,\mathrm{kg}$ ball.

The impulse is the area under $F(t)$:

$$
J=\frac12(0.030)(120)=1.80\,\mathrm{N\,s}.
$$

Using $J=m\Delta v$ gives

$$
\Delta v=\frac{1.80}{0.15}=12.0\,\mathrm{m/s}.
$$

The unit check is direct: $\mathrm{N\,s}=\mathrm{kg\,m/s}$, and division by mass leaves speed.

If the ball initially moves opposite to the force, direction matters. With $v_i=-5.0\,\mathrm{m/s}$ and positive impulse $1.80\,\mathrm{N\,s}$,

$$
v_f=v_i+\frac{J}{m}
=-5.0+\frac{1.80}{0.15}
=+7.0\,\mathrm{m/s}.
$$

The impulse stops and reverses the ball. A calculation using speed alone would hide that change.

## A two-dimensional collision

A $0.20\,\mathrm{kg}$ puck moving east at $4.0\,\mathrm{m/s}$ sticks to a $0.30\,\mathrm{kg}$ puck moving north at $2.0\,\mathrm{m/s}$. Conserve each momentum component:

$$
p_{x,i}=(0.20)(4.0)=0.80\,\mathrm{kg\,m/s},
$$

$$
p_{y,i}=(0.30)(2.0)=0.60\,\mathrm{kg\,m/s}.
$$

The combined mass is $0.50\,\mathrm{kg}$, so

$$
v_{f,x}=1.6\,\mathrm{m/s},
\qquad
v_{f,y}=1.2\,\mathrm{m/s}.
$$

Thus

$$
v_f=\sqrt{1.6^2+1.2^2}=2.0\,\mathrm{m/s},
$$

at

$$
\theta=\tan^{-1}\left(\frac{1.2}{1.6}\right)=36.9^\circ
$$

north of east. The energies are

$$
K_i=\frac12(0.20)(4.0)^2+\frac12(0.30)(2.0)^2
=2.20\,\mathrm J,
$$

$$
K_f=\frac12(0.50)(2.0)^2=1.00\,\mathrm J.
$$

Momentum conservation does not require kinetic-energy conservation.

## Between elastic and sticking

The coefficient of restitution models intermediate one-dimensional collisions:

$$
e=\frac{\text{relative speed of separation}}
{\text{relative speed of approach}}
=\frac{v_{2f}-v_{1f}}{v_{1i}-v_{2i}}.
$$

An ideal elastic collision has $e=1$; objects that stick have $e=0$. Momentum conservation plus a measured $e$ supplies two equations for the final velocities. The coefficient can depend on speed, material, temperature, and deformation. In an oblique impact it applies along the contact normal, while tangential motion also depends on friction.

## Recoil and changing mass

When an isolated object initially at rest separates into two pieces,

$$
m_1\vec v_1+m_2\vec v_2=0.
$$

The momenta are equal and opposite, but speeds are inversely proportional to mass. For equal momentum magnitudes,

$$
\frac{K_1}{K_2}=\frac{m_2}{m_1},
$$

so the lighter fragment carries more kinetic energy.

A rocket needs different bookkeeping because exhaust crosses the system boundary. For an ideal rocket in empty space with constant exhaust speed $u$ relative to the rocket, momentum balance gives

$$
\Delta v=u\ln\left(\frac{m_i}{m_f}\right).
$$

Momentum is conserved for rocket plus exhaust. Applying $m_iv_i=m_fv_f$ to the rocket alone discards exhaust momentum. Gravity and drag add further terms during a real launch.

## The center-of-mass frame

In the frame moving with $\vec v_{cm}$, total momentum is zero. A one-dimensional elastic collision is simple there: each particle reverses its velocity while keeping its speed. Transforming back recovers the general laboratory formulas.

Total kinetic energy separates into center-of-mass and relative parts:

$$
K=\frac12M v_{cm}^2+K_{\text{relative}}.
$$

Internal interactions cannot change the first term. In an inelastic collision, some relative kinetic energy becomes internal energy, while center-of-mass kinetic energy remains fixed if external impulse is negligible.

## Worked measurement: a ballistic pendulum

A ballistic pendulum uses an inelastic collision followed by an energy-conserving swing. The two stages obey different conservation laws. Suppose a bullet of mass $m=0.010\,\mathrm{kg}$ embeds in a block of mass $M=1.99\,\mathrm{kg}$. The combined body rises by $h=0.050\,\mathrm m$. Find the bullet's initial speed.

During the swing, mechanical energy is approximately conserved:

$$
\frac12(M+m)V^2=(M+m)gh.
$$

The common mass cancels, leaving

$$
V=\sqrt{2gh}
=\sqrt{2(9.8)(0.050)}
=0.990\,\mathrm{m/s}.
$$

During the brief embedding collision, momentum is conserved:

$$
mv=(M+m)V.
$$

Therefore

$$
\begin{aligned}
v
&=\frac{M+m}{m}V\\
&=\frac{2.00}{0.010}(0.990)\\
&=198\,\mathrm{m/s}.
\end{aligned}
$$

Mechanical energy cannot be conserved through the embedding step because deformation and heating are substantial. Momentum cannot be treated as conserved during the whole upward swing because gravity supplies external impulse. Splitting the process at the right instant is the main modeling decision.

The collision kinetic energies emphasize the loss:

$$
K_{\text{bullet}}=\frac12(0.010)(198)^2\approx196\,\mathrm J,
$$

whereas the kinetic energy immediately after impact is

$$
K_{\text{after}}=\frac12(2.00)(0.990)^2\approx0.980\,\mathrm J.
$$

Most of the initial kinetic energy becomes internal energy even though collision momentum is conserved.

## Worked explosion from a moving platform

A $60\,\mathrm{kg}$ person stands at rest on a $240\,\mathrm{kg}$ cart that rolls east at $3.0\,\mathrm{m/s}$ on a level, nearly frictionless track. The person jumps west relative to the ground at $2.0\,\mathrm{m/s}$. Find the cart's final speed.

Choose east as positive. Initial system momentum is

$$
p_i=(60+240)(3.0)=900\,\mathrm{kg\,m/s}.
$$

After separation,

$$
p_f=(60)(-2.0)+(240)v_c.
$$

Set the two equal:

$$
900=-120+240v_c.
$$

Thus

$$
v_c=\frac{1020}{240}=4.25\,\mathrm{m/s}.
$$

The cart speeds up east while the person moves west. Internal muscular energy raises the system's kinetic energy; momentum conservation does not restrict such an energy increase during an explosion-like separation.

If the stated $2.0\,\mathrm{m/s}$ had been the person's velocity relative to the cart, the condition would instead be $v_p-v_c=-2.0\,\mathrm{m/s}$. Relative-to-ground and relative-to-cart speeds are different data, and substituting one for the other changes the answer.

## Choosing the system and interval

System boundaries determine whether a force is internal. For two colliding carts taken together, their mutual contact forces are internal and cancel. For one cart alone, the other cart's force is external and supplies its impulse. Both descriptions are valid, but only the two-cart system has conserved momentum when track forces are negligible.

The time interval matters equally. A ball bouncing from the floor has nearly conserved ball-plus-Earth momentum. For the ball alone, the floor's impulse is dominant. If the collision lasts very briefly, the impulse of gravity on the ball can be neglected during contact, though gravity matters over the longer flight.

Momentum conservation can also be applied to one direction while failing in another. During a short collision on a horizontal surface, vertical normal and gravitational impulses may be large or cancel in an unknown way, while horizontal external impulse is negligible. Horizontal momentum may then be conserved without claiming full vector momentum conservation.

For continuously flowing material, momentum balance becomes a rate statement. A water jet that turns at a vane changes momentum each second and exerts a force on the vane. If mass flows steadily at rate $\dot m$ from velocity $\vec v_{\text{in}}$ to $\vec v_{\text{out}}$, the required force contains

$$
\vec F=\dot m(\vec v_{\text{out}}-\vec v_{\text{in}}),
$$

along with pressure and body-force terms when relevant. The expression is the continuous counterpart of impulse divided by time.

## Energy loss and deformation

“Inelastic” does not mean momentum is lost. It means translational kinetic energy of the chosen bodies is not conserved. Energy itself remains conserved when internal energy, sound, permanent deformation, rotation, and vibration are included. A superelastic collision can even increase translational kinetic energy by releasing stored chemical or elastic energy.

Macroscopic elasticity is an ideal limit. At the contact, each body compresses, stores elastic energy, and then recovers it. If recovery is incomplete, some ordered motion becomes microscopic motion. The coefficient of restitution summarizes the final relative speed without resolving those details.

Perfectly inelastic motion produces the largest kinetic-energy loss consistent with a fixed initial momentum and given masses. After sticking, all bodies share the center-of-mass velocity, so relative kinetic energy is zero. No other common final velocity can conserve the same total momentum.

## Common bookkeeping failures

- Conservation applies to total vector momentum, not separately to the magnitudes of individual momenta.
- Kinetic energy supplies an extra equation only when the collision is stated or shown to be elastic.
- Internal forces may be enormous without changing total momentum. External impulse, rather than force magnitude alone, controls the approximation.
- A negative velocity reports direction. Replacing velocities by speeds before writing momentum usually destroys information.
- The force-time area is impulse. A curve's maximum height is not enough unless its duration and shape are also known.
- For multi-stage problems, decide which law applies to each stage instead of carrying one conservation statement through the entire event.

## Checks that catch collision errors

Kinetic energy is not conserved in every collision, and momentum is not conserved for a poorly chosen system with appreciable external impulse. Treat momentum component by component; a negative result often reports direction rather than a mistake. Impulse is a change in momentum, not an average force—the average force is $J/\Delta t$.

Scale and limiting checks are especially effective here. With one incoming cart initially at rest, the speed of two carts stuck together must lie between zero and the incoming speed. Changing one input mentally should move the result in the expected direction. If the algebra disagrees, revisit the system boundary, signs, and units before the arithmetic.

Momentum is frame-dependent, but conservation holds in every inertial frame. Transforming all velocities by the same constant changes the numerical total before and after a collision by the same amount. Kinetic energy also depends on frame; whether it is conserved in an elastic collision does not. These facts are useful when choosing the center-of-mass frame for simpler algebra.

It is also useful to reverse a solved problem: find the initial speed required for a stated final speed, or ask how a non-negligible external impulse would alter the result. That variation tests whether the conservation statement is understood rather than merely copied.

<div className="see-also">

See also: [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Rotation and Angular Momentum](/physics/general/rotation-torque-and-angular-momentum) · [Newton's Laws and Applications](/physics/general/newtons-laws-and-applications)

</div>
