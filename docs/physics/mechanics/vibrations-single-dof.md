---
title: Vibrations of Single-Degree-of-Freedom Systems
sidebar_position: 14
---

# Vibrations of Single-Degree-of-Freedom Systems

Vibration concerns motion near an equilibrium configuration. A single-degree-of-freedom system has one independent coordinate after all constraints are imposed: the extension of a spring, the rotation of a shaft, or the small angular displacement of a pendulum.

The linear mass-spring-damper model is deliberately spare. It separates inertia, energy storage, dissipation, and forcing well enough to explain free oscillation, transient decay, resonance, and isolation. Multi-degree systems retain the same ideas but attach them to several natural frequencies and mode shapes.

## Building the equation about equilibrium

Let $x(t)$ measure the displacement of a mass from its static equilibrium position. A linear spring exerts $-kx$, a viscous damper exerts $-c\dot{x}$, and an external force is $F(t)$. Newton's second law gives

$$
F(t)-c\dot{x}-kx=m\ddot{x},
$$

or

$$
\boxed{m\ddot{x}+c\dot{x}+kx=F(t).}
$$

The constants have different dimensions:

| Parameter | Meaning | SI unit |
|---|---|---|
| $m$ | inertia | kg |
| $c$ | viscous damping coefficient | N s/m |
| $k$ | linear stiffness | N/m |
| $x$ | displacement from equilibrium | m |
| $F$ | applied force | N |

Measuring from equilibrium removes constant loads. For a vertical spring with downward displacement $q$ measured from its unstretched length,

$$
m\ddot{q}=mg-kq.
$$

The static extension is $q_s=mg/k$. Set $x=q-q_s$; then $\ddot{x}=\ddot{q}$ and

$$
m\ddot{x}=mg-k(x+q_s)=-kx.
$$

Gravity determines the equilibrium position but not the small-oscillation frequency of this ideal linear system.

The same equation appears after linearization. A pendulum of length $L$ obeys

$$
mL^2\ddot{\theta}+mgL\sin\theta=0.
$$

For small angles in radians, $\sin\theta\approx\theta$, so

$$
\ddot{\theta}+\frac{g}{L}\theta=0.
$$

Here the generalized inertia is $mL^2$ and the linearized rotational stiffness is $mgL$. Large-angle pendulum motion is amplitude-dependent and no longer exactly sinusoidal, marking the limit of the linear model.

## Reducing mechanisms to one coordinate

“One degree of freedom” refers to independent motion, not to the number of physical parts. Several masses, springs, and levers can still form an SDOF system when constraints express every displacement in terms of one coordinate $q$.

Springs in parallel undergo the same displacement and their forces add:

$$
k_{eq}=k_1+k_2+\cdots.
$$

Springs in series carry the same force while their extensions add:

$$
\frac{1}{k_{eq}}
=\frac{1}{k_1}+\frac{1}{k_2}+\cdots.
$$

These rules assume massless connectors and linear springs. A massive intermediate connector introduces another inertial coordinate unless its motion is constrained.

Energy gives a systematic reduction for levers and rotational systems. Express every point velocity in terms of $\dot{q}$ and write total kinetic and potential energies as

$$
T=\frac12m_{eq}\dot{q}^{,2},
\qquad
V=\frac12k_{eq}q^2.
$$

The coefficients define the effective mass and stiffness for that coordinate. If $q$ is an angle, the corresponding quantities are a mass moment of inertia and torsional stiffness:

$$
J\ddot{\theta}+c_\theta\dot{\theta}+k_\theta\theta=M(t).
$$

Changing the coordinate rescales the effective parameters but leaves the physical natural frequency unchanged. If $x=a\theta$, the $x$-based stiffness and $\theta$-based stiffness differ by $a^2$, as do the effective inertias, leaving $k_{eq}/m_{eq}$ unchanged.

Static stiffness can also be obtained with a test load. If a force $P$ produces a small displacement $\delta$ at the selected coordinate, then

$$
k_{eq}=\frac{P}{\delta}
$$

for a linear system. This method can include compliant beams or supports without assigning each one another coordinate, provided their deformation pattern is uniquely tied to $q$ and their inertia is either negligible or included in $m_{eq}$.

## Undamped free motion and conservation of energy

With $c=0$ and $F(t)=0$,

$$
m\ddot{x}+kx=0.
$$

Trying $x=e^{st}$ gives the characteristic equation

$$
ms^2+k=0,
$$

whose roots are $s=\pm i\sqrt{k/m}$. Define the undamped natural frequency

$$
\omega_n=\sqrt{\frac{k}{m}}.
$$

The response is

$$
x(t)=A\cos\omega_nt+B\sin\omega_nt.
$$

For initial displacement $x(0)=x_0$ and velocity $\dot{x}(0)=v_0$,

$$
\boxed{
x(t)=x_0\cos\omega_nt
+\frac{v_0}{\omega_n}\sin\omega_nt.
}
$$

The period and cyclic frequency are

$$
T_n=\frac{2\pi}{\omega_n},
\qquad
f_n=\frac{1}{T_n}=\frac{\omega_n}{2\pi}.
$$

Radians are dimensionless, but writing rad/s helps distinguish angular frequency from hertz.

Multiply the equation of motion by $\dot{x}$:

$$
m\ddot{x}\dot{x}+kx\dot{x}=0.
$$

Recognizing total derivatives gives

$$
\frac{d}{dt}
\left(
\frac12m\dot{x}^2+\frac12kx^2
\right)=0.
$$

Thus

$$
E=\frac12m\dot{x}^2+\frac12kx^2
$$

is constant. At a turning point, all energy is spring potential; at equilibrium, all of it is kinetic. The amplitude follows directly from the initial energy:

$$
\frac12kX^2
=\frac12kx_0^2+\frac12mv_0^2,
$$

$$
X=\sqrt{x_0^2+\left(\frac{v_0}{\omega_n}\right)^2}.
$$

## What damping changes

For free vibration with viscous damping,

$$
m\ddot{x}+c\dot{x}+kx=0.
$$

Introduce

$$
c_c=2m\omega_n=2\sqrt{km},
\qquad
\zeta=\frac{c}{c_c}.
$$

$c_c$ is the critical damping coefficient and $\zeta$ is the dimensionless damping ratio. Dividing the equation by $m$ gives

$$
\ddot{x}+2\zeta\omega_n\dot{x}+\omega_n^2x=0.
$$

The characteristic roots are

$$
s_{1,2}
=-\zeta\omega_n
\pm\omega_n\sqrt{\zeta^2-1}.
$$

Their form divides the response into three regimes.

### Underdamped response

For $0\lt\zeta\lt1$, define

$$
\omega_d=\omega_n\sqrt{1-\zeta^2}.
$$

Then

$$
x(t)=e^{-\zeta\omega_nt}
\left(A\cos\omega_dt+B\sin\omega_dt\right).
$$

Initial conditions give

$$
A=x_0,
\qquad
B=\frac{v_0+\zeta\omega_nx_0}{\omega_d}.
$$

The oscillation lies between exponential envelopes proportional to $e^{-\zeta\omega_nt}$. Successive positive peaks one damped period apart have a constant ratio. The logarithmic decrement is

$$
\delta=\ln\frac{x_j}{x_{j+1}}
=\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}.
$$

This relation estimates light damping from a free-decay record. Using peaks of the same sign matters; adjacent positive and negative extrema are only half a damped period apart.

### Critical and overdamped response

At $\zeta=1$, the characteristic root is repeated:

$$
x(t)=(A+Bt)e^{-\omega_nt}.
$$

This case returns toward equilibrium without oscillating and without the two distinct slow exponential modes of the overdamped case. The phrase “fastest return” needs a qualification: critical damping is the boundary between oscillatory and nonoscillatory free response, but settling comparisons depend on initial conditions and the chosen tolerance.

For $\zeta\gt1$, two negative real roots give

$$
x(t)=A e^{s_1t}+B e^{s_2t}.
$$

The motion is nonoscillatory. Increasing damping far beyond critical introduces a slow root approximately equal to $-k/c$, so a heavily overdamped system can return very slowly.

Energy also shows the direction of decay. With no external force,

$$
E=\frac12m\dot{x}^2+\frac12kx^2,
$$

and

$$
\frac{dE}{dt}
=\dot{x}(m\ddot{x}+kx)
=-c\dot{x}^2\le0.
$$

Viscous damping removes energy whenever the mass moves; it does no work at an instant when $\dot{x}=0$.

## Harmonic forcing and the frequency response

Consider

$$
m\ddot{x}+c\dot{x}+kx=F_0\cos\omega t.
$$

The complete response is a homogeneous transient plus a particular steady response. For positive damping the transient decays, leaving

$$
x_{ss}(t)=X\cos(\omega t-\phi).
$$

Using complex notation, take $F(t)$ as the real part of $F_0e^{i\omega t}$ and seek the real part of $\hat{X}e^{i\omega t}$. Substitution gives

$$
(-m\omega^2+ic\omega+k)\hat{X}=F_0,
$$

so

$$
\hat{X}=\frac{F_0}{k-m\omega^2+ic\omega}.
$$

The amplitude is the modulus:

$$
X=\frac{F_0}
{\sqrt{(k-m\omega^2)^2+(c\omega)^2}}.
$$

With frequency ratio $r=\omega/\omega_n$,

$$
\boxed{
\frac{X}{F_0/k}
=\frac{1}
{\sqrt{(1-r^2)^2+(2\zeta r)^2}}.
}
$$

The denominator combines the elastic-inertial mismatch $1-r^2$ and the damping term $2\zeta r$. The phase lag should be evaluated by quadrant-aware arctangent:

$$
\phi=\operatorname{atan2}(2\zeta r,1-r^2).
$$

At low frequency, $r\ll1$, the response approaches the static deflection $F_0/k$ and nearly follows the force. At $r=1$, the phase lag is $90^\circ$ and

$$
X=\frac{F_0/k}{2\zeta}
$$

for nonzero damping. At high frequency, inertia dominates, the displacement becomes small, and the response approaches $180^\circ$ out of phase with the force.

For displacement amplitude, the damped peak occurs at

$$
r_{peak}=\sqrt{1-2\zeta^2}
$$

when $\zeta\lt1/\sqrt2$. It is slightly below $r=1$. If damping is at least $1/\sqrt2$, the displacement magnification has no interior resonant peak, although phase still changes across the natural-frequency region.

The undamped case at $\omega=\omega_n$ is singular. A bounded sinusoidal steady state does not exist; the resonant particular solution contains a term proportional to $t\sin\omega_nt$. Any real dissipation or nonlinearity limits the growth, but the ideal result warns that a small periodic force can accumulate energy coherently.

## Base motion, steps, and impulses

Many systems are excited through a moving support rather than by a force applied directly to the mass. Let $y(t)$ be the base displacement and $x(t)$ the absolute mass displacement. Spring and damper deformation depend on $x-y$, so

$$
m\ddot{x}
+c(\dot{x}-\dot{y})
+k(x-y)=0.
$$

With relative displacement $z=x-y$,

$$
m\ddot{z}+c\dot{z}+kz=-m\ddot{y}.
$$

Base acceleration acts as an effective force on the relative coordinate. For $y=Y\cos\omega t$, the absolute displacement transmissibility is

$$
\frac{X}{Y}
=\sqrt{
\frac{1+(2\zeta r)^2}
{(1-r^2)^2+(2\zeta r)^2}
}.
$$

At low frequency the mass follows the base, so $X/Y\approx1$. Isolation of absolute motion begins when $r\gt \sqrt2$; below that threshold the mount may amplify motion. Added damping suppresses the resonant peak but increases high-frequency transmission through the damper. Mount design therefore trades resonance control against high-frequency isolation.

Force transmissibility instead concerns the force passed into a support. Its ratio is not identical to displacement magnification. The word “transmissibility” should be paired with the transmitted quantity: absolute displacement, relative displacement, or support force.

A sudden constant force $F_0$ creates a new static equilibrium $F_0/k$. For an initially resting undamped system,

$$
x(t)=\frac{F_0}{k}(1-\cos\omega_nt).
$$

The first peak is $2F_0/k$, twice the static deflection. A slowly applied load approaches only $F_0/k$; application time relative to $T_n$ controls the dynamic overshoot.

An ideal impulse

$$
J=\int F(t)\,dt
$$

changes velocity nearly instantaneously while displacement remains continuous. Integrating the equation across the short event gives

$$
m(\dot{x}^+-\dot{x}^-)=J.
$$

The system then follows free vibration from the new initial velocity. The impulse approximation is accurate when the force duration is much shorter than the natural period and spring and damping impulses during the event are small.

## Nondimensional form

Scaling exposes which parameter combinations control the response. Let

$$
\tau=\omega_nt,
\qquad
u=\frac{x}{F_0/k},
$$

for a harmonically forced system. Derivatives with respect to time become $\dot{x}=\omega_nx'$ and $\ddot{x}=\omega_n^2x''$, where primes now denote derivatives with respect to $\tau$. After division by the force scale, the equation is

$$
u''+2\zeta u'+u=\cos(r\tau).
$$

Mass, damping coefficient, stiffness, and forcing frequency have collapsed into two dimensionless groups: $\zeta$ and $r$. Systems with very different physical size have the same normalized response when those groups and normalized initial conditions match.

The nondimensional equation also clarifies limiting cases. Small $r$ means the load changes slowly compared with the system's own time scale. Large $r$ means many forcing cycles occur within one natural-response time. Damping always appears through $\zeta$, so comparing raw values of $c$ between systems with different $m$ and $k$ says little about their decay.

## Decay time, bandwidth, and quality factor

The underdamped envelope gives a direct estimate of settling. To reduce an initial envelope amplitude by a fraction $\varepsilon$,

$$
e^{-\zeta\omega_nt_s}=\varepsilon,
$$

so

$$
t_s=\frac{-\ln\varepsilon}{\zeta\omega_n}.
$$

For the familiar two-percent envelope, $-\ln(0.02)=3.912$, giving $t_s\approx4/(\zeta\omega_n)$. It describes an envelope crossing, not the exact time of the final oscillatory peak, and it applies to an underdamped linear response.

Lightly damped resonators are also described by the quality factor

$$
Q\approx\frac{1}{2\zeta}.
$$

Large $Q$ means slow energy decay and a narrow frequency-response peak. Near resonance, the half-power bandwidth satisfies approximately

$$
\Delta\omega\approx2\zeta\omega_n,
\qquad
Q\approx\frac{\omega_n}{\Delta\omega}.
$$

The half-power points have amplitude $1/\sqrt2$ times the peak amplitude because average dissipated power scales with amplitude squared. These bandwidth relations assume light damping and a well-separated resonance; applying them to a heavily damped response with no clear peak gives a misleading estimate.

## Limits of the viscous linear model

The term $c\dot{x}$ often fits fluid damping or serves as an equivalent linear approximation. Dry friction produces a nearly constant opposing force, hysteretic materials dissipate energy through a force-displacement loop, and aerodynamic drag may scale with velocity squared. Their free-decay envelopes are not generally exponential.

Real stiffness may depend on amplitude. A pendulum's period increases as the swing grows, while geometric and material nonlinearities can shift a structure's resonance. Clearance, stops, and backlash create piecewise dynamics. Linear SDOF predictions are local to the displacement range used to identify $m$, $c$, and $k$.

Measured data can check the assumptions. Free-decay peak spacing estimates $\omega_d$, peak ratios estimate $\zeta$ when exponential decay is plausible, and a static force-deflection test estimates $k$. The inferred mass can then be compared with $m=k/\omega_n^2$. Estimates that vary strongly with amplitude point toward nonlinearity or non-viscous damping rather than a single set of constant parameters.

## Worked example: free vibration from two initial conditions

A $5$ kg mass on a frictionless surface is attached to a spring of stiffness $180$ N/m. It begins at $x_0=0.08$ m with velocity $v_0=0.30$ m/s in the positive direction.

First compute

$$
\omega_n=\sqrt{\frac{180}{5}}=6\ \text{rad/s}.
$$

The initial-condition form gives

$$
x(t)=0.08\cos6t+\frac{0.30}{6}\sin6t,
$$

so

$$
\boxed{x(t)=0.08\cos6t+0.05\sin6t\ \text{m}.}
$$

The amplitude is

$$
\begin{aligned}
X
&=\sqrt{0.08^2+0.05^2}\\
&=\sqrt{0.0089}
=0.0943\ \text{m}.
\end{aligned}
$$

As an energy check,

$$
E_0
=\frac12(180)(0.08)^2
+\frac12(5)(0.30)^2
=0.801\ \text{J}.
$$

At maximum displacement,

$$
\frac12kX^2
=\frac12(180)(0.0943)^2
=0.801\ \text{J},
$$

which agrees. The period is

$$
T_n=\frac{2\pi}{6}=1.047\ \text{s}.
$$

## Worked example: two springs in series

An $8$ kg mass is connected to a rigid wall by two massless springs in series, with $k_1=300$ N/m and $k_2=600$ N/m. It is displaced $0.040$ m from equilibrium and released from rest. Find the natural frequency and motion.

The same force passes through both springs, while their extensions add. Their equivalent stiffness is

$$
\begin{aligned}
\frac{1}{k_{eq}}
&=\frac{1}{300}+\frac{1}{600}\\
&=\frac{3}{600},
\end{aligned}
$$

so

$$
k_{eq}=200\ \text{N/m}.
$$

The natural frequency is

$$
\omega_n
=\sqrt{\frac{k_{eq}}{m}}
=\sqrt{\frac{200}{8}}
=5.00\ \text{rad/s}.
$$

With $x_0=0.040$ m and $v_0=0$,

$$
x(t)
=x_0\cos\omega_nt
+\frac{v_0}{\omega_n}\sin\omega_nt,
$$

which becomes

$$
\boxed{x(t)=0.040\cos5t\ \text{m}.}
$$

The period is

$$
T_n=\frac{2\pi}{5}=1.257\ \text{s}.
$$

The softer spring extends twice as much as the stiffer spring because both carry equal force and $\delta=F/k$. Their extensions add to the mass displacement, consistent with the equivalent-stiffness calculation.

## Worked example: damping from a decay record

A lightly damped oscillator has successive positive displacement peaks of $12.0$ mm and $7.20$ mm. Its damped period is $0.80$ s. Estimate $\zeta$, $\omega_n$, and the exponential decay rate $\zeta\omega_n$.

The logarithmic decrement is

$$
\delta=\ln\frac{12.0}{7.20}
=\ln(1.6667)
=0.5108.
$$

From

$$
\delta=\frac{2\pi\zeta}{\sqrt{1-\zeta^2}},
$$

solve for $\zeta$ by squaring and rearranging:

$$
\delta^2(1-\zeta^2)=4\pi^2\zeta^2,
$$

$$
\zeta
=\frac{\delta}{\sqrt{4\pi^2+\delta^2}}
=\frac{0.5108}{\sqrt{4\pi^2+0.5108^2}}
=0.0810.
$$

The damped frequency is

$$
\omega_d=\frac{2\pi}{0.80}=7.854\ \text{rad/s}.
$$

Since $\omega_d=\omega_n\sqrt{1-\zeta^2}$,

$$
\omega_n
=\frac{7.854}{\sqrt{1-0.0810^2}}
=7.880\ \text{rad/s}.
$$

The envelope decay rate is

$$
\zeta\omega_n=(0.0810)(7.880)=0.638\ \text{s}^{-1}.
$$

Therefore

$$
\boxed{\zeta=0.0810,\qquad
\omega_n=7.88\ \text{rad/s},\qquad
\zeta\omega_n=0.638\ \text{s}^{-1}.}
$$

One damped period multiplies the envelope by $e^{-0.638(0.80)}=0.600$, matching $7.20/12.0$.

## Worked example: forced-response amplitude and phase

A machine component has $m=20$ kg, $k=5000$ N/m, and $\zeta=0.08$. It is forced by

$$
F(t)=120\cos12t\ \text{N}.
$$

The natural frequency and frequency ratio are

$$
\omega_n=\sqrt{\frac{5000}{20}}
=15.811\ \text{rad/s},
$$

$$
r=\frac{12}{15.811}=0.7589.
$$

The static deflection associated with the force amplitude is

$$
\frac{F_0}{k}=\frac{120}{5000}=0.0240\ \text{m}.
$$

Now evaluate the dynamic denominator:

$$
1-r^2=1-0.7589^2=0.4240,
$$

$$
2\zeta r=2(0.08)(0.7589)=0.1214,
$$

$$
D=\sqrt{0.4240^2+0.1214^2}=0.4410.
$$

Hence

$$
X=\frac{0.0240}{0.4410}=0.0544\ \text{m}.
$$

The phase lag is

$$
\phi=\operatorname{atan2}(0.1214,0.4240)
=15.98^\circ.
$$

The steady response is

$$
\boxed{
x_{ss}(t)=0.0544\cos(12t-15.98^\circ)\ \text{m}.
}
$$

This is only the long-time part. Specified initial displacement and velocity would determine an added underdamped transient at $\omega_d$.

## Model checks and recurring mistakes

- Displacement measured from the unstretched length keeps constant gravity terms in a vertical equation. Shifting to static equilibrium produces the standard homogeneous form.
- Frequency in hertz is $\omega/(2\pi)$, not $\omega$. Confusing the two changes a period by a factor of $2\pi$.
- The damping coefficient $c$ has units; the damping ratio $\zeta=c/(2m\omega_n)$ does not.
- Initial velocity contributes to free-vibration amplitude. Setting the amplitude equal to $x_0$ is valid only when $v_0=0$.
- The forced steady state does not satisfy arbitrary initial conditions by itself. The transient supplies the difference at startup.
- Resonance is a frequency-response statement. A large static displacement caused by a soft spring is not resonant motion.
- Linear stiffness and viscous damping are models over a limited range. Clearance, dry friction, geometric nonlinearity, and amplitude-dependent material behavior can change both decay and frequency.

## Related pages

- [Particle kinetics with Newton's second law](/physics/mechanics/particle-kinetics-newton)
- [Work-energy methods](/physics/mechanics/work-energy-methods)
- [Impulse, momentum, and impact](/physics/mechanics/impulse-momentum-impact)
- [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)
