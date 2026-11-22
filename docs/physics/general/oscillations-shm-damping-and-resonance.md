---
title: "Oscillations: SHM, Damping, and Resonance"
sidebar_position: 12
---

# Oscillations: SHM, Damping, and Resonance

An oscillator moves repeatedly around a stable equilibrium. Near that equilibrium, many restoring forces are approximately linear, which leads to simple harmonic motion. Real oscillators lose energy, and many are driven by an external periodic force. The equation

$$
m\ddot x+b\dot x+kx=F_0\cos\omega_dt
$$

contains all three ingredients: inertia, linear damping, and a restoring spring, with an optional drive on the right.

## Why harmonic motion appears so often

Let a system have potential energy $U(x)$ with a stable minimum at $x=x_0$. Expand near the minimum:

$$
U(x)\approx U(x_0)
+U'(x_0)(x-x_0)
+\frac12U''(x_0)(x-x_0)^2+\cdots.
$$

At equilibrium $U'(x_0)=0$, and stability requires $U''(x_0)\gt 0$. Keeping the first nonconstant term gives

$$
U(x)\approx U(x_0)+\frac12k_{\text{eff}}(x-x_0)^2.
$$

The force is then

$$
F=-\frac{dU}{dx}\approx-k_{\text{eff}}(x-x_0).
$$

Thus small oscillations around almost any smooth stable equilibrium are approximately harmonic. Larger amplitudes sample higher terms in the expansion, so their waveform or period can depend on amplitude.

For a mass attached to an ideal spring, measure $x$ from equilibrium. Newton's law gives

$$
m\ddot x=-kx,
$$

or

$$
\ddot x+\omega_0^2x=0,
\qquad
\omega_0=\sqrt{\frac{k}{m}}.
$$

The general solution is

$$
x(t)=A\cos(\omega_0t+\phi).
$$

Here $A$ and $\phi$ are set by the initial position and velocity. Frequency and period are

$$
f=\frac{\omega_0}{2\pi},
\qquad
T=\frac{2\pi}{\omega_0}
=2\pi\sqrt{\frac{m}{k}}.
$$

Angular frequency is measured in radians per second; ordinary frequency is cycles per second. Writing $\cos(ft)$ without a factor $2\pi$ mixes the two.

## Position, velocity, and phase

Differentiate the displacement:

$$
v(t)=-A\omega_0\sin(\omega_0t+\phi),
$$

$$
a(t)=-A\omega_0^2\cos(\omega_0t+\phi)
=-\omega_0^2x(t).
$$

Velocity is one quarter-cycle out of phase with position. Acceleration is opposite to position. The extreme values are

$$
v_{\max}=A\omega_0,
\qquad
a_{\max}=A\omega_0^2.
$$

At $x=\pm A$, the oscillator turns around: velocity is zero and acceleration magnitude is greatest. At equilibrium, acceleration is zero and speed is greatest.

Initial conditions determine phase. If $x(0)=x_0$ and $v(0)=v_0$,

$$
x_0=A\cos\phi,
\qquad
v_0=-A\omega_0\sin\phi.
$$

Squaring the first relation and the second divided by $\omega_0$, then adding, gives

$$
A=\sqrt{x_0^2+\left(\frac{v_0}{\omega_0}\right)^2}.
$$

The signs of both initial quantities are needed to select the correct phase quadrant.

## Energy exchange in simple harmonic motion

For an undamped spring oscillator,

$$
E=\frac12mv^2+\frac12kx^2
$$

is constant. At a turning point,

$$
E=\frac12kA^2.
$$

Equating these forms gives speed at any position:

$$
\frac12mv^2+\frac12kx^2=\frac12kA^2,
$$

so

$$
v=\pm\omega_0\sqrt{A^2-x^2}.
$$

The two signs correspond to passing the same position in opposite directions.

Potential and kinetic energies vary as squared sine and cosine functions. Each repeats twice during one displacement cycle: both $+A$ and $-A$ are all-potential-energy states, while the two equilibrium crossings are all-kinetic-energy states.

### Worked spring oscillator

A $0.40\,\mathrm{kg}$ mass on a $160\,\mathrm{N/m}$ spring oscillates with amplitude $0.050\,\mathrm m$. Its angular frequency is

$$
\omega_0=\sqrt{\frac{160}{0.40}}
=20.0\,\mathrm{rad/s}.
$$

Thus

$$
T=\frac{2\pi}{20.0}=0.314\,\mathrm s,
$$

$$
v_{\max}=A\omega_0=(0.050)(20.0)
=1.00\,\mathrm{m/s},
$$

and

$$
a_{\max}=A\omega_0^2=(0.050)(400)
=20.0\,\mathrm{m/s^2}.
$$

At $x=0.030\,\mathrm m$, the speed magnitude is

$$
\begin{aligned}
\lvert v\rvert
&=20.0\sqrt{0.050^2-0.030^2}\\
&=0.800\,\mathrm{m/s}.
\end{aligned}
$$

Position alone does not say whether the mass is moving left or right, so energy gives only the speed magnitude.

## Vertical springs and shifted equilibrium

For a mass hanging vertically, gravity changes the equilibrium position but not the angular frequency. Let downward extension from the spring's natural length be $y$. Equilibrium satisfies

$$
ky_{\text{eq}}=mg.
$$

Write displacement from equilibrium as $x=y-y_{\text{eq}}$. Then

$$
m\ddot x=-kx,
$$

because the constant gravitational and equilibrium spring forces cancel. The period remains $2\pi\sqrt{m/k}$.

Using the natural length as the origin without retaining gravity gives the wrong equation. Once the coordinate is shifted to equilibrium, gravity no longer appears explicitly.

## The pendulum and the small-angle limit

For a point mass on a light string of length $L$, torque about the pivot gives

$$
mL^2\ddot\theta=-mgL\sin\theta.
$$

Therefore

$$
\ddot\theta+\frac{g}{L}\sin\theta=0.
$$

This equation is nonlinear. For small angles in radians, $\sin\theta\approx\theta$, so

$$
\ddot\theta+\frac{g}{L}\theta=0
$$

and

$$
T=2\pi\sqrt{\frac{L}{g}}.
$$

The bob's mass cancels. At larger amplitude, the exact period is longer and depends on amplitude. The first correction is approximately

$$
T\approx T_0\left(1+\frac{\theta_0^2}{16}\right)
$$

when $\theta_0$ is in radians and not too large.

For a desired small-angle period $1.50\,\mathrm s$ near Earth,

$$
L=g\left(\frac{T}{2\pi}\right)^2
=9.8\left(\frac{1.50}{2\pi}\right)^2
=0.558\,\mathrm m.
$$

The model assumes a point-like bob, massless inextensible string, fixed pivot, and negligible damping.

## Free motion with viscous damping

Set the drive to zero:

$$
m\ddot x+b\dot x+kx=0.
$$

Define

$$
\gamma=\frac{b}{2m},
\qquad
\omega_0=\sqrt{\frac{k}{m}}.
$$

The behavior depends on the comparison between $\gamma$ and $\omega_0$.

| Regime | Condition | Motion |
|---|---|---|
| Underdamped | $\gamma\lt \omega_0$ | oscillatory decay |
| Critically damped | $\gamma=\omega_0$ | fastest nonoscillatory return |
| Overdamped | $\gamma\gt \omega_0$ | slower nonoscillatory return |

For the underdamped case,

$$
x(t)=A_0e^{-\gamma t}\cos(\omega_dt+\phi),
$$

where

$$
\omega_d=\sqrt{\omega_0^2-\gamma^2}.
$$

Amplitude decays as $e^{-\gamma t}$ and mechanical energy approximately as $e^{-2\gamma t}$. Damping also lowers the oscillation frequency slightly.

Critical damping is useful when a system should return quickly without overshoot, as in some door closers or measuring instruments. More damping is not always faster: the overdamped system creeps back because resistance is too strong.

The linear damping force $-b\dot x$ is a model appropriate to some viscous regimes. Dry friction or quadratic fluid drag produces different decay envelopes.

## Periodic driving and the resonance curve

With a sinusoidal drive, transients eventually decay and the steady response has the drive frequency:

$$
x_{ss}(t)=A(\omega_d)\cos(\omega_dt-\delta).
$$

The amplitude is

$$
A(\omega_d)=
\frac{F_0}
{\sqrt{(k-m\omega_d^2)^2+(b\omega_d)^2}}.
$$

At low frequency, the oscillator follows quasi-statically with $A\approx F_0/k$. At high frequency, inertia dominates and amplitude falls roughly as $F_0/(m\omega_d^2)$. Between them lies a resonance peak.

For weak damping, the displacement-amplitude peak lies near $\omega_0$. The exact peak frequency is

$$
\omega_r=\sqrt{\omega_0^2-\frac{b^2}{2m^2}},
$$

provided damping is small enough for a peak to exist. The frequency of maximum average power absorption is $\omega_0$ for this model, so “the resonance frequency” can depend on which response is being maximized.

The phase lag satisfies

$$
\tan\delta=\frac{b\omega_d}{k-m\omega_d^2}.
$$

At low frequency, displacement is nearly in phase with the drive. Near $\omega_0$, the lag is about $\pi/2$. Far above resonance, it approaches $\pi$.

## Quality factor and energy loss

For weak damping, the quality factor is

$$
Q=\frac{m\omega_0}{b}.
$$

It can also be understood as roughly $2\pi$ times the energy stored divided by energy lost per cycle. A high-$Q$ oscillator has a narrow resonance and rings for many cycles. A low-$Q$ oscillator has a broad response and settles quickly.

Near weak resonance, the half-power bandwidth obeys

$$
\Delta\omega\approx\frac{\omega_0}{Q}.
$$

Resonance does not imply unlimited amplitude in a real device. Damping balances the average power supplied by the drive. Nonlinearities, finite strength, and changing material behavior also limit motion. In the ideal undamped equation driven exactly at $\omega_0$, amplitude grows approximately linearly with time because energy is added coherently each cycle.

## Worked driven response

Take $m=1.0\,\mathrm{kg}$, $k=100\,\mathrm{N/m}$, $b=2.0\,\mathrm{kg/s}$, and drive amplitude $F_0=5.0\,\mathrm N$. The natural frequency is

$$
\omega_0=\sqrt{\frac{100}{1.0}}
=10.0\,\mathrm{rad/s},
$$

and

$$
Q=\frac{(1.0)(10.0)}{2.0}=5.0.
$$

At drive frequency $10.0\,\mathrm{rad/s}$,

$$
\begin{aligned}
A
&=\frac{5.0}
{\sqrt{(100-1.0\cdot10.0^2)^2+(2.0\cdot10.0)^2}}\\
&=\frac{5.0}{20.0}\\
&=0.250\,\mathrm m.
\end{aligned}
$$

The static displacement under a constant $5.0\,\mathrm N$ force would be only $F_0/k=0.050\,\mathrm m$. Resonant energy accumulation enlarges the response, while damping keeps it finite.

## Phase-space view

Plotting velocity against position removes time from the horizontal axis. For undamped SHM,

$$
v^2=\omega_0^2(A^2-x^2),
$$

or

$$
\frac{x^2}{A^2}+\frac{v^2}{A^2\omega_0^2}=1.
$$

The trajectory is an ellipse in the $x$-$v$ plane. Each circuit represents one cycle. Its clockwise or counterclockwise orientation depends on the plotting convention and initial motion.

Damping makes the trajectory spiral inward as energy decreases. A maintained periodic drive can produce a closed long-term orbit after transients fade. Phase space distinguishes repeated motion from simple repetition of position: the oscillator can pass through the same $x$ twice per cycle with opposite velocities.

Energy curves supply another geometric view. Horizontal total-energy lines intersect the parabolic potential $U=\tfrac12kx^2$ at turning points. Larger energy gives wider turning points and higher equilibrium speed while the ideal harmonic period remains unchanged.

## Physical pendulums and torsional oscillators

A rigid body pivoted a distance $d$ from its center of mass is a physical pendulum. For small angular displacement, its gravitational torque is approximately

$$
\tau\approx-mgd\theta.
$$

With rotational inertia $I$ about the pivot,

$$
I\ddot\theta=-mgd\theta,
$$

so

$$
\omega_0=\sqrt{\frac{mgd}{I}},
\qquad
T=2\pi\sqrt{\frac{I}{mgd}}.
$$

The simple pendulum is recovered by taking a point mass at distance $L$, so $I=mL^2$ and $d=L$.

A torsional oscillator has restoring torque

$$
\tau=-\kappa\theta,
$$

where $\kappa$ is the torsion constant. Its period is

$$
T=2\pi\sqrt{\frac{I}{\kappa}}.
$$

This rotational form parallels the spring-mass result with $I$ replacing mass and $\kappa$ replacing the linear spring constant.

### Worked physical pendulum

A uniform thin rod of length $L$ pivots about one end. Its center of mass lies at $d=L/2$, and its moment of inertia about the end is $I=mL^2/3$. Therefore

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{mL^2/3}{mg(L/2)}}\\
&=2\pi\sqrt{\frac{2L}{3g}}.
\end{aligned}
$$

For $L=1.00\,\mathrm m$,

$$
T=2\pi\sqrt{\frac{2}{3(9.8)}}
=1.64\,\mathrm s.
$$

Treating the rod as a point mass at its center would give the wrong rotational inertia and period.

## Superposition and coupled oscillators

The undamped harmonic equation is linear. If $x_1(t)$ and $x_2(t)$ are solutions, their sum is also a solution. Two oscillations at the same frequency combine into one sinusoid with a new amplitude and phase.

Nearby frequencies produce beats. For equal amplitudes,

$$
\cos\omega_1t+\cos\omega_2t
=2\cos\left(\frac{\omega_1-\omega_2}{2}t\right)
\cos\left(\frac{\omega_1+\omega_2}{2}t\right).
$$

The rapid oscillation is modulated by a slow envelope. In ordinary frequency units, beat frequency is $\lvert f_1-f_2\rvert$.

Coupled oscillators have normal modes: collective patterns in which every part oscillates at one shared frequency with fixed amplitude ratios. Two identical masses joined by springs have an in-phase mode and an out-of-phase mode. General motion is a superposition of modes, so energy may appear to pass back and forth between the masses.

Normal modes extend to strings, air columns, molecules, buildings, and crystal lattices. A continuous wave system can be regarded as having many oscillator modes, each with its own natural frequency.

## Transients and steady state

The driven solution is the sum of a homogeneous transient and a particular steady response:

$$
x(t)=x_{\text{transient}}(t)+x_{\text{steady}}(t).
$$

Initial conditions set the transient. Damping makes it decay, leaving a steady oscillation at the driving frequency. Measurements made immediately after switching on a drive can therefore differ substantially from the long-term amplitude formula.

Near resonance in a high-$Q$ system, the buildup time is long. A narrow resonance and slow settling are two aspects of weak energy loss. Sweeping drive frequency too quickly may fail to let the oscillator reach its steady amplitude, distorting the measured resonance curve.

External forcing need not be additive. Parametric driving changes a system parameter, such as varying pendulum length or spring stiffness periodically. Resonance can then occur when the modulation frequency is near twice the natural frequency. Pumping a playground swing by changing body configuration is closer to parametric excitation than to applying a simple sinusoidal horizontal force.

## Nonlinear oscillation

Real restoring forces eventually depart from $-kx$. A nonlinear oscillator can have amplitude-dependent frequency, asymmetric cycles, multiple stable responses, or chaotic motion under driving. Superposition then fails.

For a pendulum, retaining $\sin\theta$ rather than replacing it with $\theta$ is already a nonlinear model. Its period grows with amplitude and becomes unbounded as the energy approaches the top of a full rotation. Above that energy, the pendulum rotates rather than oscillating between turning points.

Linear SHM remains useful because it is the leading approximation near stable equilibrium. Its limits should be read from displacement scale and observed waveform, not assumed from the mere presence of repeated motion.

## Measuring an oscillator

Period is best estimated over many cycles and divided by the cycle count. This reduces the fractional effect of reaction time or sampling resolution. Amplitude should be measured from equilibrium to one extreme, not as the full peak-to-peak distance.

A displacement record can reveal damping by fitting successive peak magnitudes to an exponential envelope. Taking the logarithm of peak amplitude gives a straight line for linear viscous damping:

$$
\ln A(t)=\ln A_0-\gamma t.
$$

Systematic curvature in that plot suggests a different damping law or changing parameters.

Natural frequency can be measured either from free oscillation or from a driven response. With appreciable damping, the free damped frequency, displacement-resonance frequency, and undamped parameter $\omega_0$ are not identical. Reporting which one was measured prevents a small but real ambiguity.

Energy checks are also diagnostic. For nominally undamped data, compute $\tfrac12mv^2+\tfrac12kx^2$ at several times. A steady decline indicates loss; a phase-dependent oscillation may instead signal calibration error or an incorrect equilibrium position.

## Assumptions and checks

- Measure spring displacement from equilibrium when using $F=-kx$ in the SHM equation.
- Keep $\omega$ in radians per second distinct from $f$ in hertz.
- Harmonic motion requires a restoring force linear over the displacement range.
- The pendulum formula requires angles small enough for $\sin\theta\approx\theta$.
- Damping changes both amplitude and, generally, frequency.
- A driven oscillator's long-term frequency equals the drive frequency, not its free natural frequency.
- Check the zero-damping and zero-drive limits of any formula before using it.

<div className="see-also">

See also: [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Waves, Sound, Standing Waves, and Doppler](/physics/general/waves-sound-standing-waves-and-doppler) · [AC Circuits and Electromagnetic Waves](/physics/general/ac-circuits-and-electromagnetic-waves)

</div>
