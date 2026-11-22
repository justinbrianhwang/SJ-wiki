---
title: "Quantum Intro: Photons and Matter Waves"
sidebar_position: 26
---

# Quantum Intro: Photons and Matter Waves

Classical wave theory explains interference and diffraction of light, but several experiments require energy and momentum exchange in discrete quanta. Material particles, meanwhile, produce diffraction patterns associated with a wavelength. Quantum theory keeps both sets of evidence by assigning a complex probability amplitude to a state and quantized outcomes to measurements.

“Wave-particle duality” is useful historical shorthand, but it can suggest that a quantum object alternates between two classical identities. A photon or electron is described by one quantum framework. Wave-like propagation and particle-like detections are different aspects of that description.

## Planck's constant sets the quantum scale

The constant

$$
h=6.62607015\times10^{-34}\,\mathrm{J\,s}
$$

relates frequency to energy and wavelength to momentum. Its reduced form is

$$
\hbar=\frac{h}{2\pi}.
$$

For everyday masses and actions, $h$ is extremely small, so quantum interference between macroscopically distinct motions is hard to preserve. At atomic scales, quantities comparable to $h$ are ordinary.

Planck introduced quantized energy exchange while modeling thermal radiation. Einstein treated the light quantum more directly in explaining the photoelectric effect. The modern photon concept also includes momentum and polarization.

## Photon energy, momentum, and intensity

A photon of frequency $f$ and vacuum wavelength $\lambda$ has

$$
E=hf=\frac{hc}{\lambda}
$$

and

$$
p=\frac{E}{c}=\frac{h}{\lambda}.
$$

A photon has zero rest mass but nonzero energy and momentum. For light in vacuum, the relativistic relation $E=pc$ applies.

Frequency fixes energy per photon. Intensity measures energy delivered per area per time. At fixed frequency, increasing intensity increases the average photon arrival rate, not the energy of each photon:

$$
\text{photon rate}=\frac{\text{optical power}}{hf}.
$$

A $1.00\,\mathrm{mW}$ laser at $500\,\mathrm{nm}$ emits photons of energy

$$
E=\frac{1240\,\mathrm{eV\,nm}}{500\,\mathrm{nm}}
=2.48\,\mathrm{eV}.
$$

In joules,

$$
E=(2.48)(1.602\times10^{-19})
=3.97\times10^{-19}\,\mathrm J.
$$

The photon rate is

$$
\dot N=\frac{1.00\times10^{-3}\,\mathrm{J/s}}
{3.97\times10^{-19}\,\mathrm J}
=2.52\times10^{15}\,\mathrm{s^{-1}}.
$$

The convenient constant $hc\approx1240\,\mathrm{eV\,nm}$ requires wavelength in nanometers and returns energy in electron-volts.

Photon momentum produces radiation pressure. Absorbing light transfers momentum $E/c$; ideal reflection reverses the photon's normal momentum and transfers twice as much. The force is tiny for ordinary optical powers but measurable and useful in precision experiments and solar sailing.

## The photoelectric effect

When light illuminates a material, electrons may be emitted. The work function $\phi$ is the minimum energy needed to remove an electron from the surface. Energy conservation for a single absorbed photon gives

$$
K_{\max}=hf-\phi.
$$

Electrons within the material begin with different energies and may lose energy before escaping, so emitted electrons have a range of kinetic energies. The equation describes the maximum.

The threshold frequency is

$$
f_0=\frac{\phi}{h},
$$

or threshold wavelength

$$
\lambda_0=\frac{hc}{\phi}.
$$

Below threshold, the ideal single-photon process emits no electrons regardless of intensity. Above threshold, increasing frequency raises $K_{\max}$. Increasing intensity at fixed frequency increases the number of available photons and usually the photoelectric current, without changing the maximum kinetic energy.

A stopping potential $V_s$ can halt the most energetic electrons:

$$
eV_s=K_{\max}.
$$

Plotting $V_s$ against frequency gives slope $h/e$ and an intercept related to the work function.

### Worked photoelectric threshold

A metal has work function $\phi=2.20\,\mathrm{eV}$ and is illuminated with $400\,\mathrm{nm}$ light. Photon energy is

$$
E_\gamma=\frac{1240}{400}=3.10\,\mathrm{eV}.
$$

Therefore

$$
K_{\max}=3.10-2.20=0.90\,\mathrm{eV}.
$$

The stopping potential magnitude is

$$
V_s=\frac{K_{\max}}{e}=0.90\,\mathrm V.
$$

The threshold wavelength is

$$
\lambda_0=\frac{1240\,\mathrm{eV\,nm}}{2.20\,\mathrm{eV}}
=564\,\mathrm{nm}.
$$

Since $400\,\mathrm{nm}$ is shorter than the threshold wavelength, its photons have enough energy. If the illumination were $600\,\mathrm{nm}$, the calculated kinetic energy would be negative; the physical result would be no single-photon emission.

Real materials complicate the clean model through surface contamination, band structure, multiphoton absorption at high intensity, and field-assisted emission. The threshold equation remains the introductory baseline.

## Compton scattering confirms photon momentum

In Compton scattering, an X-ray photon collides with an electron and emerges at angle $\theta$ with longer wavelength. Relativistic energy and momentum conservation give

$$
\Delta\lambda
=\lambda'-\lambda
=\frac{h}{m_ec}(1-\cos\theta).
$$

The shift depends on scattering angle and electron mass, not on incident intensity. Classical wave scattering did not account for the observed wavelength shift in this form. Treating the interaction as a collision between a photon and electron does.

At $\theta=180^\circ$, the shift is largest:

$$
\Delta\lambda_{\max}=\frac{2h}{m_ec}.
$$

The quantity $h/(m_ec)$ is the electron Compton wavelength. This process requires relativistic kinematics even if the electron initially rests.

## De Broglie waves for material particles

De Broglie proposed that a particle with momentum $p$ has wavelength

$$
\lambda=\frac{h}{p}.
$$

For a slow particle, $p=mv$. At relativistic speed,

$$
p=\gamma mv
$$

must be used. Large momentum means short wavelength, which helps explain why wave effects are difficult to observe for macroscopic objects.

For an electron moving at $1.0\times10^6\,\mathrm{m/s}$,

$$
p=(9.11\times10^{-31})(1.0\times10^6)
=9.11\times10^{-25}\,\mathrm{kg\,m/s}.
$$

The speed is much smaller than $c$, so the nonrelativistic momentum is adequate:

$$
\begin{aligned}
\lambda
&=\frac{6.626\times10^{-34}}
{9.11\times10^{-25}}\\
&=7.27\times10^{-10}\,\mathrm m\\
&=0.727\,\mathrm{nm}.
\end{aligned}
$$

That scale is comparable to atomic spacing, so crystals can diffract electrons. Electron diffraction and microscopy use the same wave relation while detections remain localized events.

## Electrons accelerated through a voltage

An electron accelerated from rest through potential difference $V$ gains kinetic energy

$$
K=eV.
$$

In the nonrelativistic regime,

$$
\frac{p^2}{2m_e}=eV,
$$

so

$$
\lambda=\frac{h}{\sqrt{2m_eeV}}.
$$

For $V=150\,\mathrm V$,

$$
\begin{aligned}
p
&=\sqrt{2(9.11\times10^{-31})
(1.602\times10^{-19})(150)}\\
&=6.61\times10^{-24}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Then

$$
\lambda=\frac{6.626\times10^{-34}}
{6.61\times10^{-24}}
=1.00\times10^{-10}\,\mathrm m
=0.100\,\mathrm{nm}.
$$

The kinetic energy is only $150\,\mathrm{eV}$ compared with electron rest energy about $511\,\mathrm{keV}$, so nonrelativistic mechanics is adequate. At accelerating voltages of tens or hundreds of kilovolts, relativistic correction becomes important.

## Interference one detection at a time

Sending electrons or photons through two slits at low rate produces isolated detector spots. After many events, the distribution builds an interference pattern. The theory adds probability amplitudes for indistinguishable alternatives and then squares the magnitude:

$$
P\propto\lvert\psi_1+\psi_2\rvert^2.
$$

Expanding gives

$$
\lvert\psi_1\rvert^2+\lvert\psi_2\rvert^2
+2\operatorname{Re}(\psi_1^*\psi_2).
$$

The final term is interference. If path information becomes encoded in a detector or environment strongly enough to distinguish the alternatives, that cross term is reduced or lost in the observed subsystem. Physical interaction, not human awareness, controls the change.

Matter waves are therefore not material ripples following a particle. The wavefunction encodes amplitudes for possible outcomes. Its squared magnitude is interpreted as probability density after proper normalization:

$$
\int_{-\infty}^{\infty}\lvert\psi(x,t)\rvert^2\,dx=1.
$$

## Wave packets and group velocity

A single sinusoidal wave extends through all space and has definite wavelength and momentum. A localized particle state requires a superposition of many wave numbers. The resulting wave packet has a carrier oscillation and an envelope.

For a free nonrelativistic particle,

$$
E=\frac{p^2}{2m},
\qquad
\omega=\frac{\hbar k^2}{2m}.
$$

Its group velocity is

$$
v_g=\frac{d\omega}{dk}
=\frac{\hbar k}{m}
=\frac{p}{m},
$$

matching classical particle velocity. The phase velocity differs and does not represent the speed of localized information. Because different wave-number components have different group velocities, a free packet generally spreads with time.

## Uncertainty from Fourier structure

Position and momentum spreads obey

$$
\Delta x\,\Delta p\ge\frac{\hbar}{2}.
$$

Here $\Delta x$ and $\Delta p$ are standard deviations in a quantum state. The relation is not merely disturbance by a clumsy measurement. A narrow spatial wave packet needs a broad range of wave numbers, and $p=\hbar k$ turns that range into momentum spread.

If an electron is localized to $\Delta x=0.10\,\mathrm{nm}$, the minimum momentum uncertainty is

$$
\begin{aligned}
\Delta p
&\ge\frac{\hbar}{2\Delta x}\\
&=\frac{1.055\times10^{-34}}
{2(1.0\times10^{-10})}\\
&=5.28\times10^{-25}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

The corresponding nonrelativistic velocity spread is at least

$$
\Delta v\approx\frac{\Delta p}{m_e}
=5.79\times10^5\,\mathrm{m/s}.
$$

The inequality constrains preparation of the state. Individual measurements yield particular values; repeated measurements on identically prepared systems reveal the distributions.

Energy and time have a related but subtler uncertainty relation because time is normally a parameter rather than a standard position-like operator. It often expresses a relation between a state's lifetime and energy linewidth, not a blanket permission to violate energy conservation temporarily.

## Quantized bound states

Confinement turns a continuous range of wavelengths into a discrete set of standing-wave patterns. For an ideal one-dimensional infinite well of width $L$, the wavefunction vanishes at both walls. The allowed wavelengths satisfy

$$
L=n\frac{\lambda_n}{2},
\qquad
n=1,2,3,\ldots,
$$

so

$$
\lambda_n=\frac{2L}{n}.
$$

Using $p=h/\lambda$ and nonrelativistic kinetic energy gives

$$
E_n=\frac{p_n^2}{2m}
=\frac{n^2h^2}{8mL^2}.
$$

There is no $n=0$ state: a wavefunction zero everywhere cannot represent a particle. The lowest state has nonzero energy, consistent with the impossibility of having both perfectly fixed position inside the well and zero momentum.

Atoms also have discrete bound-state energies, though their three-dimensional Coulomb problem differs from the square well. When an atom changes from higher energy $E_i$ to lower energy $E_f$, emitted photon energy satisfies

$$
hf=E_i-E_f.
$$

Absorption requires a photon matching an allowed energy difference, subject to additional transition rules. Discrete spectral lines therefore record differences between energy levels rather than arbitrary electron orbital frequencies.

For a transition of $2.00\,\mathrm{eV}$, the photon wavelength is

$$
\lambda=\frac{1240\,\mathrm{eV\,nm}}{2.00\,\mathrm{eV}}
=620\,\mathrm{nm}.
$$

The photon lies in the visible red region. A larger energy gap gives shorter wavelength.

## Tunneling through a barrier

Classically, a particle with energy below a potential barrier cannot cross it. A quantum wavefunction penetrates into the forbidden region and decays rather than becoming immediately zero. If the barrier is finite, a nonzero amplitude can reach the far side, producing transmission.

For a rectangular barrier with height $V_0\gt E$ and width $a$, the transmission probability has an approximate exponential dependence

$$
T\propto e^{-2\kappa a},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

Increasing barrier width, particle mass, or energy deficit suppresses tunneling strongly. The process does not give the transmitted particle an energy above its original value; energy is conserved. “Borrowing energy” is a misleading explanation.

Tunneling contributes to radioactive alpha decay, scanning tunneling microscopy, semiconductor devices, and nuclear fusion rates. The details require the actual potential and boundary conditions.

## Measurement and expectation values

Quantum theory predicts probability distributions for repeated measurements on identically prepared systems. For a normalized one-dimensional wavefunction, position probability in an interval is

$$
P(a<x<b)=\int_a^b\lvert\psi(x,t)\rvert^2\,dx.
$$

The expectation value is

$$
\langle x\rangle=\int_{-\infty}^{\infty}
\psi^*x\psi\,dx.
$$

It is the mean of many outcomes, not necessarily a position obtained in any one trial. The spread is

$$
(\Delta x)^2=\langle x^2\rangle-\langle x\rangle^2.
$$

Other observables are represented by operators. Momentum in the position representation is

$$
\hat p=-i\hbar\frac{\partial}{\partial x}.
$$

The noncommuting position and momentum operators underlie their uncertainty relation. This mathematical statement is stronger and more precise than a story about a measuring probe knocking a particle.

## Classical behavior as a limit

Quantum theory does not switch off for large objects. Classical behavior emerges when relevant actions are large compared with $h$, wave packets remain narrow on the scale of interest, and environmental interactions rapidly suppress observable interference between alternatives.

The correspondence principle requires quantum predictions to approach classical ones in the appropriate limit. For high quantum numbers, neighboring energy levels can become close relative to experimental resolution. Average motion can then follow classical trajectories even though the underlying state remains quantum.

Decoherence explains why macroscopic superpositions are difficult to isolate: countless uncontrolled degrees of freedom record phase information. It does not by itself select a unique interpretation of quantum measurement, but it quantitatively accounts for loss of accessible interference.

## What the introductory formulas do not say

The relations $E=hf$ and $p=h/\lambda$ do not replace a full state description. A photon can have a spread of frequencies, directions, positions, and polarization. Likewise, quoting one de Broglie wavelength assumes momentum is sufficiently well defined.

The Schrödinger equation governs nonrelativistic quantum evolution:

$$
i\hbar\frac{\partial\psi}{\partial t}
=\hat H\psi.
$$

For a particle in potential $V(x)$,

$$
\hat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x).
$$

Boundary conditions and normalization select physical solutions. Relativistic particles, photon creation, and changing particle number require more advanced field theories.

Quantum predictions are exact probabilities within a specified model, while uncertainty in experimental parameters adds ordinary statistical and systematic error. Keeping those two kinds of uncertainty separate prevents the uncertainty principle from becoming a catch-all explanation for imprecise apparatus.

Spin is another intrinsically quantum property. It contributes angular momentum and magnetic moment, but it is not well modeled as a tiny classical body rotating about an axis. Measurements along a chosen direction return discrete outcomes, and changing the measurement direction changes the probabilities. Its full treatment requires quantum-state notation beyond the introductory wavelength formulas.

## Where the classical picture fails

- Intensity and photon energy are independent at fixed frequency; more intense light usually means more photons.
- A negative value from $hf-\phi$ means the one-photon process is forbidden, not that an electron has negative kinetic energy.
- De Broglie wavelength uses momentum. The replacement $p=mv$ needs a nonrelativistic check.
- Interference requires addition of amplitudes before probabilities.
- Uncertainty describes statistical spreads of a state, not only instrumental resolution.
- Electron-volts measure energy, while volts measure potential difference. For a singly charged particle, the numerical conversion through $eV$ can conceal that distinction.

<div className="see-also">

See also: [Interference, Diffraction, and Gratings](/physics/general/interference-diffraction-and-gratings) · [Relativity Intro](/physics/general/relativity-intro)

</div>
