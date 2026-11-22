---
title: Interference, Diffraction, and Gratings
sidebar_position: 24
---

# Interference, Diffraction, and Gratings

Wave optics tracks phase differences. Two or more coherent contributions can reinforce or cancel, while a finite aperture causes different parts of the same wavefront to interfere. Double-slit fringes, single-slit diffraction, and grating spectra are three versions of that one superposition principle.

## Path difference sets the phase

For two coherent waves of wavelength $\lambda$, a path difference $\delta$ corresponds to phase difference

$$
\Delta\phi=\frac{2\pi}{\lambda}\delta.
$$

Equal-phase contributions interfere constructively; contributions separated by an odd multiple of $\pi$ interfere destructively.

For two narrow slits separated by $d$,

$$
\delta=d\sin\theta.
$$

Bright fringes occur when

$$
d\sin\theta=m\lambda,
\qquad m=0,\pm1,\pm2,\ldots,
$$

and dark fringes occur when

$$
d\sin\theta=\left(m+\frac12\right)\lambda.
$$

The sources must maintain a stable phase relation for a stationary pattern. Ordinary independent light sources do not usually provide that coherence.

## Adding amplitudes before intensities

Interference comes from superposition of wave amplitudes. For two sinusoidal electric fields of equal amplitude,

$$
E_1=E_0\cos\omega t,
\qquad
E_2=E_0\cos(\omega t+\Delta\phi),
$$

the trigonometric sum is

$$
E_1+E_2
=2E_0\cos\left(\frac{\Delta\phi}{2}\right)
\cos\left(\omega t+\frac{\Delta\phi}{2}\right).
$$

Intensity is proportional to the time average of the squared total field, so

$$
I=4I_0\cos^2\left(\frac{\Delta\phi}{2}\right).
$$

Here $I_0$ is the intensity from either source alone. At zero phase difference the intensity is $4I_0$, not $2I_0$, because equal amplitudes double before squaring. At phase difference $\pi$, the ideal equal-amplitude fields cancel.

For unequal source intensities,

$$
I=I_1+I_2+2\sqrt{I_1I_2}\cos\Delta\phi.
$$

The minimum is $(\sqrt{I_1}-\sqrt{I_2})^2$, so complete darkness requires equal amplitudes as well as opposite phase. Conditions written only in terms of path difference silently assume those amplitudes match.

Coherence describes whether the phase relation remains predictable. Temporal coherence is limited by the range of frequencies in the source; a narrow spectral width gives a longer coherence time and length. Spatial coherence describes phase correlation across a wavefront. Illuminating two slits from one small or distant source gives them a shared phase history, while two unrelated lamps fluctuate too independently to leave stationary optical fringes.

Fringe contrast can be summarized by visibility

$$
\mathcal V=\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}.
$$

Unequal illumination, finite source size, polarization mismatch, and phase fluctuations all reduce $\mathcal V$. They can wash out a pattern even though each opening still diffracts light.

## Young fringes on a distant screen

When the screen distance $L$ is much larger than the fringe displacement $y$, the small-angle approximation gives $\sin\theta\approx\tan\theta\approx y/L$. Adjacent bright fringes are then separated by

$$
\Delta y=\frac{\lambda L}{d}.
$$

For $\lambda=600\,\mathrm{nm}$, $d=0.20\,\mathrm{mm}$, and $L=2.0\,\mathrm m$,

$$
\Delta y
=\frac{(600\times10^{-9})(2.0)}{0.20\times10^{-3}}
=6.0\times10^{-3}\,\mathrm m
=6.0\,\mathrm{mm}.
$$

Wider slit separation produces more closely spaced fringes; a longer wavelength or more distant screen spreads them apart.

The spacing formula measures adjacent bright fringes. Since the center is order zero, the fifth bright fringe above it has $y_5=5\Delta y$. If the apparatus is immersed in a medium of index $n$, wavelength becomes $\lambda_0/n$ while frequency remains fixed:

$$
\Delta y=\frac{\lambda_0L}{nd}.
$$

For the same apparatus in water with $n=1.33$, the $6.0\,\mathrm{mm}$ air spacing becomes

$$
\Delta y_{\text{water}}=\frac{6.0\,\mathrm{mm}}{1.33}
=4.5\,\mathrm{mm}.
$$

| Pattern | Geometric scale | Condition |
|---|---|---|
| Double-slit bright fringe | separation $d$ | $d\sin\theta=m\lambda$ |
| Double-slit dark fringe | separation $d$ | $d\sin\theta=(m+\tfrac12)\lambda$ |
| Single-slit minimum | width $a$ | $a\sin\theta=m\lambda$, $m=1,2,\ldots$ |
| Grating principal maximum | spacing $d$ | $d\sin\theta=m\lambda$ |

## Why a single slit produces minima

A slit of finite width $a$ contains a continuous range of secondary wave contributions. At angles satisfying

$$
a\sin\theta=m\lambda,
\qquad m=1,2,3,\ldots,
$$

those contributions pair off and cancel. The central maximum lies between the first minima and is twice as wide as the secondary maxima in the small-angle screen geometry.

For the first minimum, divide the slit into two equal halves. When the full path difference across the slit is one wavelength, corresponding points in the halves differ by half a wavelength and cancel pairwise. For the second minimum, four equal strips cancel in adjacent pairs. Integration gives the complete Fraunhofer profile:

$$
I(\theta)=I(0)\left(\frac{\sin\beta}{\beta}\right)^2,
\qquad
\beta=\frac{\pi a\sin\theta}{\lambda}.
$$

Zeros occur at $\beta=m\pi$. Secondary maxima are weaker than the center and are not exactly halfway between zeros. The central lobe spans from the first negative-angle minimum to the first positive-angle minimum, so it is twice the width of an outer lobe measured between successive minima.

For $a=0.10\,\mathrm{mm}$ and $\lambda=500\,\mathrm{nm}$, the first minimum satisfies

$$
\sin\theta_1=\frac{\lambda}{a}
=\frac{500\times10^{-9}}{0.10\times10^{-3}}
=0.0050,
$$

so

$$
\theta_1=0.286^\circ.
$$

On a screen $3.00\,\mathrm m$ away, the first minima lie at

$$
y_1=L\tan\theta_1\approx(3.00)(0.00500)
=0.0150\,\mathrm m.
$$

The central maximum width is therefore

$$
w_{\text{central}}=2y_1=3.00\,\mathrm{cm}.
$$

The equation for single-slit minima resembles the equation for double-slit maxima, but $a$ is slit width and $d$ is slit separation. Interchanging them predicts the wrong angular scale.

Diffraction grows when an aperture narrows, directly from $\sin\theta_1=\lambda/a$. This behavior sets a resolution limit for optical instruments. Closing an aperture may reduce geometric aberrations, yet eventually each point source spreads into a broader diffraction pattern.

## Interference fringes inside a diffraction envelope

Real double slits have finite width. Their narrow interference fringes are multiplied by a broad single-slit diffraction envelope. A nominal double-slit maximum can disappear when it lands at a single-slit minimum. Treating the two effects as alternatives misses this combined pattern.

For identical slits of width $a$ and center separation $d$, the far-field intensity has the form

$$
I(\theta)=I_{\max}
\left(\frac{\sin\beta}{\beta}\right)^2
\cos^2\alpha,
$$

where

$$
\beta=\frac{\pi a\sin\theta}{\lambda},
\qquad
\alpha=\frac{\pi d\sin\theta}{\lambda}.
$$

The cosine factor creates the fine fringes; the sinc-squared factor changes their heights. A missing order occurs when an interference maximum and a diffraction minimum coincide:

$$
d\sin\theta=m\lambda,
\qquad
a\sin\theta=p\lambda.
$$

Thus $m/p=d/a$. If $d=3a$, every third interference order lies at a diffraction zero and disappears.

This expression assumes equal, uniformly illuminated rectangular slits in the far field. Fresnel diffraction retains wavefront curvature and depends on propagation distance more intricately. A lens can map far-field angles to points in its focal plane, making a Fraunhofer pattern accessible without an extremely distant screen.

## Aperture shape and resolution

The single-slit formula belongs to a rectangular one-dimensional aperture. A circular opening produces an Airy pattern: a bright central disk surrounded by weaker rings. The first dark ring occurs at

$$
\sin\theta_1\approx1.22\frac{\lambda}{D},
$$

where $D$ is aperture diameter. Under the Rayleigh criterion, two equally bright point sources are barely resolved when the central maximum of one falls on the first minimum of the other:

$$
\theta_R\approx1.22\frac{\lambda}{D}.
$$

Larger apertures therefore improve diffraction-limited angular resolution. Magnification alone cannot recover detail that the aperture has already blended.

For a telescope with diameter $D=0.100\,\mathrm m$ observing at $\lambda=550\,\mathrm{nm}$,

$$
\begin{aligned}
\theta_R
&=1.22\frac{550\times10^{-9}}{0.100}\\
&=6.71\times10^{-6}\,\mathrm{rad}.
\end{aligned}
$$

Multiplying by $206\,265$ arcseconds per radian gives about $1.38$ arcseconds. Atmospheric turbulence often broadens ground-based images beyond this ideal limit, while aberrations and detector sampling can add other constraints.

The far-field diffraction pattern is mathematically related to the Fourier transform of the aperture. A narrow feature in the aperture corresponds to a broad angular distribution; repeated features produce sharply selected spatial frequencies. This viewpoint unifies the broad single-slit envelope, the fine double-slit fringes, and the narrow peaks of a many-groove grating without treating them as unrelated formulas.

## Polarization can remove interference

Two waves interfere through the dot product of their electric-field amplitudes. If the slits produce mutually perpendicular linear polarizations, the detector records the sum of their intensities without a cross term, and the fringes vanish. Placing a polarizer after the slits at an angle that projects both fields onto the same axis can restore fringes, at reduced intensity.

This is a useful warning about “which-path” information. Orthogonal polarization can label the paths even when no observer reads the label. Once the alternatives are distinguishable in principle, their amplitudes no longer contribute the same interference cross term at an ordinary polarization-insensitive detector. Erasing the distinguishing polarization by a common projection makes the alternatives indistinguishable again.

The observation also separates coherence from mere overlap. Beams can occupy the same region, have the same frequency, and still fail to form visible fringes if their polarizations are orthogonal or their phase relation wanders during the detector's averaging time.

## Historical route to wave optics

Young's two-source interference supplied strong evidence that light behaves as a wave. Fresnel developed the quantitative diffraction theory, while Fraunhofer studied the far-field limit and spectral lines. Later electromagnetic theory identified light as an electromagnetic wave. Quantum experiments retain the same interference equations for detection probabilities, even when particles arrive one at a time; the accumulated distribution follows the wave-amplitude pattern.

The classical formulas remain appropriate whenever source statistics and detector response allow intensity to be treated continuously. At very low light levels, individual detections are discrete, but the probability distribution builds the same fringes. Blocking one slit changes the available amplitudes and leaves the single-aperture diffraction pattern.

The small-angle expression $y\approx L\theta$ is convenient near the center. At larger angles, keep

$$
y=L\tan\theta
$$

and solve the exact sine condition first.

## Gratings sharpen wavelength separation

A diffraction grating has many evenly spaced slits. Its principal maxima obey the same condition as two-slit maxima,

$$
d\sin\theta=m\lambda,
$$

but increasing the number of illuminated slits narrows the peaks. Different wavelengths then appear at different angles, which allows a grating to resolve spectral lines.

For $N$ equally spaced narrow slits, the interference factor is

$$
\left(\frac{\sin N\alpha}{\sin\alpha}\right)^2.
$$

At a principal maximum, all $N$ amplitudes add, so peak intensity scales as $N^2$ relative to one slit. Peak width shrinks roughly as $1/N$. More illuminated grooves produce narrow, bright spectral lines rather than merely increasing total light.

Angular dispersion measures how rapidly diffraction angle changes with wavelength. Differentiating the grating equation at fixed order gives

$$
d\cos\theta\,\frac{d\theta}{d\lambda}=m,
$$

or

$$
\frac{d\theta}{d\lambda}=\frac{m}{d\cos\theta}.
$$

Higher orders and smaller groove spacing spread wavelengths through larger angles, although high orders may fail to exist or may overlap other wavelengths.

The order is limited by $\lvert\sin\theta\rvert\le1$, so

$$
\lvert m\rvert\le\frac{d}{\lambda}.
$$

Higher algebraic orders that violate this bound do not correspond to propagating beams.

Consider a grating with $600$ lines per millimeter used with $500\,\mathrm{nm}$ light. Its groove spacing is

$$
d=\frac{1.00\,\mathrm{mm}}{600}
=1.67\times10^{-6}\,\mathrm m.
$$

For first order,

$$
\sin\theta_1=\frac{\lambda}{d}
=\frac{500\times10^{-9}}{1.67\times10^{-6}}
=0.300,
$$

so $\theta_1=17.5^\circ$. The order bound is

$$
m\le\frac{d}{\lambda}=3.33,
$$

which gives $m_{\max}=3$. The integer floor is required; fractional diffraction orders do not exist.

Under the Rayleigh criterion, the ideal resolving power is

$$
\mathcal R=\frac{\lambda}{\Delta\lambda}=mN.
$$

Resolution improves with order and the number of illuminated grooves. Dispersion and resolution answer different questions. A grating can spread wavelengths through a large angle while each line remains too broad to distinguish a close neighbor.

## Thin films and reflection phase

Rays reflected from the two surfaces of a thin film can interfere. Their geometric round-trip optical path within a film of thickness $t$ and index $n$ is $2nt\cos\theta_t$, where $\theta_t$ is the internal angle. A reflection toward a medium of higher index adds a phase shift of $\pi$, equivalent to half a wavelength. Reflection toward lower index adds no such shift.

The number of reflection phase reversals decides whether $2nt=m\lambda$ is bright or dark. Drawing the index sequence is safer than carrying one memorized rule between different coatings. If exactly one of the two reflected rays receives a $\pi$ shift, constructive reflected interference at normal incidence requires

$$
2nt=\left(m+\frac12\right)\lambda_0.
$$

For the thinnest such coating that reflects $\lambda_0=550\,\mathrm{nm}$ strongly with $n=1.38$, take $m=0$:

$$
t=\frac{\lambda_0}{4n}
=\frac{550\,\mathrm{nm}}{4(1.38)}
=99.6\,\mathrm{nm}.
$$

If both reflections receive the same phase shift, their relative reflection phase is zero and the conditions swap. Anti-reflection coatings use thickness and index choices that make leading reflected rays cancel while transmitting most of the light. Broadband coatings require multiple layers because a single quarter-wave layer is optimized around a limited wavelength and angle range.

Interference colors in soap films arise because thickness varies across the film and the constructive wavelength changes with position. When the film is comparable to the coherence length, multiple reflected contributions can remain correlated. Very thick or uneven films average over phase and lose clear color bands.

## Pattern checks

- Convert nanometers and millimeters to the same units before taking ratios.
- Use slit separation for interference spacing and slit width for the diffraction envelope.
- Verify the small-angle condition rather than assuming it for every fringe.
- Count the central maximum as $m=0$ for interference; single-slit minima begin at $m=1$.
- A finite-width multi-slit pattern contains both interference and diffraction structure.
- Add field amplitudes before computing intensity.
- For thin films, count phase shifts at both reflecting boundaries.

<div className="see-also">

See also: [Waves and Sound](/physics/general/waves-sound-standing-waves-and-doppler) · [Quantum Intro](/physics/general/quantum-intro-photons-and-matter-waves)

</div>
