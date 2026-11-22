---
title: Waves, Sound, Standing Waves, and Doppler Effect
sidebar_position: 13
---

# Waves, Sound, Standing Waves, and Doppler Effect

A wave is a disturbance whose pattern propagates. Mechanical waves require a medium; electromagnetic waves do not. In either case, the wave carries energy and momentum while the local medium or field oscillates. A marked element of string moves mostly up and down as a transverse pulse passes; it does not accompany the pulse to the far end.

Three ideas organize most introductory problems. The medium sets a propagation speed, the source sets a frequency, and boundary conditions select which superpositions can persist as normal modes. Relative motion changes the spacing or encounter rate of wavefronts and produces a Doppler shift.

## Reading amplitude, phase, and propagation direction

A sinusoidal wave traveling in the positive $x$ direction may be written

$$
y(x,t)=A\sin(kx-\omega t+\phi).
$$

Here $A$ is amplitude, $\phi$ is initial phase,

$$
k=\frac{2\pi}{\lambda},
\qquad
\omega=2\pi f,
$$

and $f=1/T$. To follow a point of constant phase, set $kx-\omega t+\phi$ equal to a constant and differentiate:

$$
k\frac{dx}{dt}-\omega=0.
$$

Therefore the phase speed is

$$
v=\frac{dx}{dt}=\frac{\omega}{k}=f\lambda.
$$

Changing the sign to $kx+\omega t$ gives propagation toward negative $x$. The sign is best checked by holding the phase fixed rather than memorizing a slogan.

For a string displacement, the transverse particle velocity and acceleration are

$$
v_y=\frac{\partial y}{\partial t},
\qquad
a_y=\frac{\partial^2y}{\partial t^2}.
$$

These are distinct from the wave speed $v$. At a crest of a sinusoidal wave, a string element has zero transverse velocity at that instant even though the crest continues to propagate.

The function satisfies the one-dimensional wave equation

$$
\frac{\partial^2 y}{\partial x^2}
=\frac1{v^2}\frac{\partial^2 y}{\partial t^2}.
$$

Any sufficiently smooth function of $x-vt$ or $x+vt$ satisfies this equation, so a wave need not be sinusoidal. Sinusoids are favored because linear systems preserve their frequency and arbitrary shapes can be decomposed into Fourier components.

### Worked example: extracting a wave's properties

Suppose

$$
y(x,t)=0.030\sin(4.0x-20t+0.50),
$$

with SI units. Comparison with the standard form gives $A=0.030\,\mathrm m$, $k=4.0\,\mathrm{rad/m}$, and $\omega=20\,\mathrm{rad/s}$. Hence

$$
\lambda=\frac{2\pi}{k}=\frac{2\pi}{4.0}=1.57\,\mathrm m,
$$

$$
f=\frac{\omega}{2\pi}=\frac{20}{2\pi}=3.18\,\mathrm{Hz},
$$

and

$$
v=\frac{\omega}{k}=\frac{20}{4.0}=5.0\,\mathrm{m/s}.
$$

Because the phase contains $kx-\omega t$, the wave travels in the positive $x$ direction. At $x=0$ and $t=0$,

$$
y(0,0)=0.030\sin0.50=0.0144\,\mathrm m.
$$

The transverse velocity there is

$$
v_y(0,0)=-A\omega\cos0.50
=-(0.030)(20)(0.878)
=-0.527\,\mathrm{m/s}.
$$

The medium element is moving downward while the pattern travels right.

## Why tension and mass density set string speed

For an ideal flexible string under tension $F_T$ with linear mass density $\mu$, a small curved element experiences a net transverse force from the slightly different directions of the end tensions. In the small-slope limit, Newton's second law gives

$$
F_T\frac{\partial^2y}{\partial x^2}\,dx
=\mu\,dx\frac{\partial^2y}{\partial t^2}.
$$

After canceling $dx$ and comparing with the wave equation,

$$
v=\sqrt{\frac{F_T}{\mu}}.
$$

Greater tension supplies a stronger restoring force; greater mass per length increases inertia. The model assumes the string is flexible, tension is nearly uniform, slopes are small, and transverse displacement does not appreciably stretch the string.

For a sinusoidal string wave, the average transported power is

$$
P_{avg}=\frac12\mu\omega^2A^2v.
$$

Power scales with amplitude squared and frequency squared when the other quantities are fixed. Doubling amplitude therefore quadruples average power rather than doubling it.

### Worked example: a driven string

A string has tension $80\,\mathrm N$, linear density $0.020\,\mathrm{kg/m}$, and carries a $50\,\mathrm{Hz}$ sinusoidal wave of amplitude $5.0\,\mathrm{mm}$. First,

$$
v=\sqrt{\frac{80}{0.020}}=63.2\,\mathrm{m/s}.
$$

Its wavelength is

$$
\lambda=\frac vf=\frac{63.2}{50}=1.26\,\mathrm m.
$$

The angular frequency is

$$
\omega=2\pi f=314\,\mathrm{rad/s}.
$$

Using $A=0.0050\,\mathrm m$,

$$
P_{avg}=\frac12(0.020)(314)^2(0.0050)^2(63.2)
=1.56\,\mathrm W.
$$

The wavelength follows from speed and source frequency; changing tension would change $v$ and $\lambda$ but not the driving frequency.

## Superposition, interference, and beats

In a linear medium, overlapping displacements add:

$$
y_{total}=y_1+y_2.
$$

Equal-frequency waves in phase interfere constructively; those differing by $\pi$ interfere destructively. The waves continue after overlap because superposition does not make either constituent vanish permanently.

Two nearby frequencies produce beats. Using the sum identity,

$$
\cos(2\pi f_1t)+\cos(2\pi f_2t)
=2\cos\left[2\pi\frac{f_1-f_2}{2}t\right]
\cos\left[2\pi\frac{f_1+f_2}{2}t\right].
$$

The rapid oscillation occurs near the average frequency, while its amplitude envelope repeats at

$$
f_{beat}=|f_1-f_2|.
$$

Musicians use the slowing beat rate between a reference and an instrument as a tuning cue. The simple interpretation works when the frequencies are close enough that individual rapid cycles are not heard as separate tones.

## Standing waves are boundary-value solutions

Superpose two waves of equal amplitude and frequency traveling in opposite directions:

$$
y_1=A\sin(kx-\omega t),
\qquad
y_2=A\sin(kx+\omega t).
$$

Their sum is

$$
y=2A\sin(kx)\cos(\omega t).
$$

The spatial factor and time factor are separated. Nodes occur where $\sin(kx)=0$ and remain at rest; antinodes oscillate with maximum amplitude $2A$. There is no net average energy transport in an ideal standing wave because equal traveling waves carry equal power in opposite directions.

For a string fixed at $x=0$ and $x=L$, both endpoints must be nodes. The second condition requires

$$
\sin(kL)=0,
$$

so

$$
kL=n\pi,qquad n=1,2,3,\ldots
$$

and therefore

$$
\lambda_n=\frac{2L}{n},
\qquad
f_n=\frac{nv}{2L}.
$$

$n=1$ is the fundamental; higher integer $n$ values are harmonics. The mode frequencies are properties of the string and its boundary conditions. A driver produces a large response when its frequency lies near one of them, with the finite amplitude set by damping and drive strength.

Air columns require care because pressure and displacement boundary conditions are complementary. At an open end, pressure variation is approximately a node and air displacement an antinode. At a closed end, displacement is a node and pressure variation an antinode.

| Ideal resonator | Allowed wavelengths | Frequencies |
|---|---|---|
| String fixed at both ends | $\lambda_n=2L/n$ | $f_n=nv/(2L)$, $n=1,2,3,\ldots$ |
| Pipe open at both ends | $\lambda_n=2L/n$ | $f_n=nv/(2L)$, $n=1,2,3,\ldots$ |
| Pipe closed at one end | $\lambda_n=4L/n$ | $f_n=nv/(4L)$, $n=1,3,5,\ldots$ |

Real open pipes have an end correction because the oscillating air extends beyond the geometric end. The ideal formulas treat the effective length as the stated $L$.

### Worked example: identifying a closed pipe

A pipe $0.85\,\mathrm m$ long is closed at one end. Take the sound speed as $343\,\mathrm{m/s}$. The fundamental is

$$
f_1=\frac{v}{4L}
=\frac{343}{4(0.85)}
=100.9\,\mathrm{Hz}.
$$

Only odd harmonics occur in the ideal model, so the next resonance is $n=3$:

$$
f_3=3f_1=302.6\,\mathrm{Hz}.
$$

The value $2f_1$ is absent. Observing resonances near $101$, $303$, and $505\,\mathrm{Hz}$ would support the closed-open boundary model.

## Sound intensity and the decibel scale

Sound is primarily a longitudinal pressure and density wave in a fluid. Its speed depends on the medium's elastic response and density. In a gas, temperature and composition matter; the source frequency does not determine the sound speed in the nondispersive approximation.

Intensity is average power per area:

$$
I=\frac{P}{A}.
$$

For a point source radiating uniformly in free space,

$$
I=\frac{P}{4\pi r^2}.
$$

The inverse-square law reflects geometric spreading, not loss of total power. Absorption, obstacles, and directional sources require additional modeling.

Sound level is logarithmic:

$$
\beta=10\log_{10}\left(\frac{I}{I_0}\right)\ \mathrm{dB},
$$

where $I_0=10^{-12}\,\mathrm{W/m^2}$ is the usual reference intensity in air. Multiplying intensity by $10$ adds $10\,\mathrm{dB}$; doubling it adds about $3.0\,\mathrm{dB}$. Decibels compare levels and are not direct units of intensity.

## Deriving the one-dimensional Doppler formula

Let sound speed relative to stationary air be $v$. A source emitting frequency $f$ has period $T=1/f$. If it moves toward the observer at speed $v_s$, it advances $v_sT$ between emitted crests. The forward wavelength becomes

$$
\lambda'=vT-v_sT=\frac{v-v_s}{f}.
$$

A stationary observer then measures

$$
f'=\frac{v}{\lambda'}=f\frac{v}{v-v_s}.
$$

If the observer also moves toward the arriving crests at speed $v_o$, wavefronts pass the observer at relative speed $v+v_o$, giving

$$
f'=f\frac{v+v_o}{v-v_s}.
$$

Other directions are obtained by signed velocity components along the source-observer line. A common mnemonic form is

$$
f'=f\frac{v\pm v_o}{v\mp v_s},
$$

but the physical trend is safer: approach must raise the frequency and separation must lower it. Source and observer velocities are measured relative to the medium, so a wind requires a consistent frame.

### Worked example: approaching siren and observer

A $700\,\mathrm{Hz}$ siren approaches at $25\,\mathrm{m/s}$ while an observer moves toward it at $10\,\mathrm{m/s}$. Take $v=343\,\mathrm{m/s}$. Both motions increase the encounter rate, so

$$
f'=700\frac{343+10}{343-25}.
$$

Evaluating numerator and denominator,

$$
f'=700\frac{353}{318}=777\,\mathrm{Hz}.
$$

After they pass, both signs reverse:

$$
f'_{recede}=700\frac{343-10}{343+25}
=700\frac{333}{368}
=633\,\mathrm{Hz}.
$$

The abrupt idealized change corresponds to the line-of-sight velocity changing sign at passage. A real trajectory with nonzero miss distance gives a rapid but continuous transition.

## Reflection, transmission, and impedance

When a wave reaches a boundary, part may reflect and part transmit. The signs and amplitudes follow boundary conditions rather than a universal “bounce” rule. A pulse on a string reflecting from a fixed end is inverted because displacement must remain zero at the endpoint. Reflection from an ideal free end is not inverted because the transverse force, and therefore the slope in the ideal model, vanishes there.

At a junction between strings, both displacement and transverse force must match. A large mismatch in wave impedance produces strong reflection. For a string, the characteristic impedance is

$$
Z=\mu v=\sqrt{\mu F_T}.
$$

Joining strings with equal impedance eliminates reflection in the ideal linear model even if their individual density and speed values differ appropriately. Energy conservation constrains reflected and transmitted power, so displacement-amplitude ratios alone can be misleading when impedances differ.

Sound behaves similarly at changes in acoustic impedance. A pressure wave meeting an open end, closed end, or material interface has different reflection behavior. Medical ultrasound coupling gel reduces the severe impedance discontinuity that an air gap would create between the transducer and skin.

## Dispersion and group velocity

The relation $v=\omega/k$ defines phase velocity. In a nondispersive medium, $\omega$ is proportional to $k$, all Fourier components share the same speed, and a pulse keeps its shape. In a dispersive medium, phase speed depends on frequency. Components drift in phase and a localized packet can spread.

The envelope of a narrow-band packet moves at group velocity

$$
v_g=\frac{d\omega}{dk}.
$$

Phase velocity and group velocity can differ. The crests inside a water-wave packet may move through the envelope, appearing at one edge and disappearing at the other. Information and energy are usually associated with the group behavior in ordinary transparent media, though absorption and anomalous dispersion require more careful definitions.

An ideal taut string has linear dispersion relation $\omega=vk$, so $v_g=v$. Real strings have stiffness, and water surface waves are strongly dispersive. The phrase “wave speed” should therefore be tied to phase, group, or signal propagation when the distinction matters.

## Resonance is a driven response

Normal modes are the system's allowed free-oscillation patterns. Resonance occurs when periodic driving lies near a normal-mode frequency. The two ideas coincide in frequency for a lightly damped linear resonator but answer different questions: boundary conditions determine the modes, while forcing and damping determine the steady amplitude.

At exact resonance an undamped ideal model predicts amplitude growing without bound, which is an artifact of omitted loss and nonlinearity. Real systems dissipate energy. Their response peak has finite height and width, often summarized by a quality factor. Narrow peaks distinguish nearby frequencies well but take longer to build up and decay.

The mode shape also affects whether a driver excites a resonance. Driving at a node of a particular string mode couples weakly to that mode, while driving near an antinode couples more strongly. Likewise, microphone placement can suppress or emphasize room modes without changing their frequencies.

## Shock waves are beyond the ordinary Doppler formula

As a source speed approaches sound speed from below, the forward wavelength in the elementary formula approaches zero and the predicted frequency diverges. The assumptions fail before that mathematical singularity. Disturbances accumulate and nonlinear compression produces a shock.

For a source moving supersonically at speed $v_s$, wavefronts form a Mach cone with half-angle

$$
\sin\mu=\frac{v}{v_s}=\frac1{Ma}.
$$

An observer hears the sonic boom when the cone sweeps past, not when the source is directly overhead. The boom comes from the pressure jump across the shock surface; it is not a one-time sound emitted only as the source crosses Mach one.

Electromagnetic Doppler shift has a different relativistic formula because light needs no material medium and all inertial observers measure the same vacuum light speed. Substituting light speed into the classical sound formula gives the wrong result.

## Assumptions that formulas tend to hide

- Keep frequency $f$ in hertz distinct from angular frequency $\omega$ in radians per second, and wavelength $\lambda$ distinct from wavenumber $k$.
- The medium's particles oscillate; the wave pattern propagates. Their speeds are different quantities.
- The relation $v=f\lambda$ always links a single wave's phase speed, frequency, and wavelength, but it does not say which one remains fixed when the medium changes. Frequency normally follows the source across a boundary.
- Draw node and antinode conditions before choosing a standing-wave formula. Closed-open pipes do not have the full integer harmonic series.
- Sound intensity adds for independent incoherent sources; amplitudes and phases must be added for coherent interference.
- The elementary Doppler formula assumes speeds below the sound speed and motion along one line. Supersonic sources produce shock-wave geometry instead of merely shifted forward crests.
- A measured resonance has finite width because damping removes energy. The ideal normal-mode formula locates its center, not its amplitude.

<div className="see-also">

See also: [Oscillations, SHM, Damping, and Resonance](/physics/general/oscillations-shm-damping-and-resonance) · [Interference, Diffraction, and Gratings](/physics/general/interference-diffraction-and-gratings) · [Waves, Phasors, and Spectrum](/physics/electromagnetics/waves-phasors-spectrum) · [Fourier Series for Periodic Signals](/physics/signals-systems/fourier-series-periodic-signals)

</div>
