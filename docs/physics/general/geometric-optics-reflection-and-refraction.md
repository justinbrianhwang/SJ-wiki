---
title: "Geometric Optics: Reflection and Refraction"
sidebar_position: 23
---

# Geometric Optics: Reflection and Refraction

Geometric optics replaces a wavefront by rays perpendicular to it. The replacement is accurate when lenses, mirrors, apertures, and variations in refractive index are large compared with the wavelength. It says where light travels and where an image forms, but it cannot predict diffraction fringes or resolve structure near the wavelength scale.

The central approximation is local: over a short enough distance, a ray follows a straight line through a uniform medium. A boundary can redirect it by reflection or refraction. Curved boundaries then focus or spread families of rays.

## Why reflection and refraction follow extremal paths

Fermat's principle states that the optical path between two points is stationary with respect to small changes of route. The optical path length is

$$
\mathcal L=\int n\,ds,
$$

and light travel time is $\mathcal L/c$. “Stationary” usually means a minimum in elementary examples, although more general optical systems can have stationary paths that are not strict minima.

For reflection from a plane surface, compare nearby routes from a source to a receiver by replacing the receiver with its mirror image behind the surface. The shortest broken path becomes a straight line to that image. The resulting geometry gives

$$
\theta_i=\theta_r,
$$

where both angles are measured from the surface normal. The incident ray, reflected ray, and normal lie in the same plane.

For refraction at a flat boundary, let the ray cross the boundary at horizontal coordinate $x$. If the source and receiver lie vertical distances $a$ and $b$ from the boundary and have horizontal separation $D$, the travel time is

$$
t(x)=\frac{n_1}{c}\sqrt{x^2+a^2}
+\frac{n_2}{c}\sqrt{(D-x)^2+b^2}.
$$

The physical path satisfies $dt/dx=0$. Differentiating gives

$$
\frac{n_1}{c}\frac{x}{\sqrt{x^2+a^2}}
=
\frac{n_2}{c}\frac{D-x}{\sqrt{(D-x)^2+b^2}}.
$$

The two ratios are $\sin\theta_1$ and $\sin\theta_2$, so

$$
n_1\sin\theta_1=n_2\sin\theta_2.
$$

Snell's law follows. The refractive index $n=c/v$ measures the reduction of phase speed relative to vacuum. At a stationary boundary the frequency is continuous: wave crests cannot accumulate at the interface. Since $v=f\lambda$, the wavelength changes in the same ratio as the speed.

## Reading Snell's law before calculating

If $n_2\gt n_1$, then $\sin\theta_2\lt \sin\theta_1$ and the transmitted ray bends toward the normal. If $n_2\lt n_1$, it bends away. Normal incidence is the limiting case $\theta_1=0$, for which direction does not change even though speed and wavelength do.

Consider light entering glass with $n_2=1.50$ from air with $n_1=1.00$ at $40.0^\circ$:

$$
\sin\theta_2=\frac{n_1}{n_2}\sin\theta_1
=\frac{1.00}{1.50}\sin40.0^\circ
=0.4285.
$$

Therefore

$$
\theta_2=\sin^{-1}(0.4285)=25.4^\circ.
$$

The smaller angle agrees with the expected bend toward the normal. If the stated $40.0^\circ$ had instead been measured from the surface, the angle for Snell's law would be $50.0^\circ$.

Reflection normally accompanies refraction. The relative reflected and transmitted powers are set by the Fresnel equations and depend on polarization and angle. Snell's law alone determines directions, not brightness. Introductory ray drawings often omit the weak reflected ray at a transparent boundary, but that omission is a modeling choice.

## Total internal reflection and the critical angle

Suppose light moves from index $n_1$ into a lower index $n_2$. As $\theta_1$ grows, the refracted angle grows faster. At the critical angle, the transmitted ray is parallel to the boundary:

$$
n_1\sin\theta_c=n_2\sin90^\circ,
$$

so

$$
\sin\theta_c=\frac{n_2}{n_1},
\qquad n_1>n_2.
$$

For glass with $n_1=1.50$ next to air with $n_2=1.00$,

$$
\theta_c=\sin^{-1}\left(\frac{1.00}{1.50}\right)=41.8^\circ.
$$

An internal incidence angle of $50^\circ$ therefore produces total internal reflection. No propagating ray carries energy into the air. An evanescent field still penetrates a short distance beyond the boundary; bringing another high-index material close enough can couple energy across the gap. The ray model suppresses that wave-level detail.

There is no critical angle when light goes from lower to higher index. Substituting those indices would demand $\sin\theta_c\gt 1$. That result means the physical condition cannot occur, not that the calculator failed.

Optical fibers use repeated total internal reflection in a high-index core surrounded by a lower-index cladding. Real fibers are described by guided modes rather than literal zigzags, but the ray picture gives the correct acceptance-angle intuition when the core is many wavelengths across.

## Parallel faces shift a ray without changing its final direction

A glass window or transparent slab has two parallel interfaces. The ray bends toward the normal on entering and away from it on leaving. Applying Snell's law at both faces gives

$$
n_1\sin\theta_1=n_2\sin\theta_2
$$

and

$$
n_2\sin\theta_2=n_1\sin\theta_3.
$$

Therefore $\theta_3=\theta_1$: the emerging ray is parallel to the incident ray. It is nevertheless displaced sideways. For slab thickness $t$, the perpendicular separation between the continued incident ray and the emerging ray is

$$
s=t\frac{\sin(\theta_1-\theta_2)}{\cos\theta_2}.
$$

Take a $4.00\,\mathrm{cm}$ glass plate of index $1.50$ in air, with incidence angle $45.0^\circ$. Refraction inside the plate gives

$$
\theta_2=\sin^{-1}\left(\frac{\sin45.0^\circ}{1.50}\right)=28.1^\circ.
$$

Then

$$
\begin{aligned}
s
&=(4.00\,\mathrm{cm})
\frac{\sin(45.0^\circ-28.1^\circ)}{\cos28.1^\circ}\\
&=1.32\,\mathrm{cm}.
\end{aligned}
$$

The plate changes the ray's position and travel time even though its final direction is unchanged. That distinction matters when aligning optical systems.

Refraction also produces apparent depth. Looking nearly straight down into water, rays from a submerged object spread as they enter air. Backward extensions of those rays meet above the object, so it appears shallower. At small angles,

$$
d_{\text{apparent}}\approx d_{\text{real}}\frac{n_{\text{observer}}}{n_{\text{object medium}}}.
$$

A coin $12.0\,\mathrm{cm}$ below water of index $1.33$, viewed from air, appears at a depth

$$
d_{\text{apparent}}\approx(12.0\,\mathrm{cm})\frac{1.00}{1.33}
=9.02\,\mathrm{cm}.
$$

This approximation loses accuracy far from normal viewing because the exact relation contains tangents as well as Snell's law.

## From a curved surface to a thin lens

A spherical refracting surface changes the direction of each paraxial ray by a slightly different amount. Combining two such surfaces gives a lens. Under the thin-lens and paraxial approximations, the image equation is

$$
\frac{1}{f}=\frac{1}{d_o}+\frac{1}{d_i},
$$

and transverse magnification is

$$
m=\frac{h_i}{h_o}=-\frac{d_i}{d_o}.
$$

The following real-is-positive convention is used:

| Quantity | Positive | Negative |
|---|---|---|
| Focal length $f$ | converging lens | diverging lens |
| Object distance $d_o$ | real object on incoming side | virtual object |
| Image distance $d_i$ | real image on outgoing side | virtual image on incoming side |
| Magnification $m$ | upright image | inverted image |

Other conventions are valid, especially for mirrors, but equations and signs must come from one convention. A ray construction is useful before substitution:

```mermaid
graph LR
  A["Mark the axis, lens, and focal points"] --> B["Draw a ray parallel to the axis"]
  B --> C["Refract it through the far focal point"]
  C --> D["Draw a ray through the lens center"]
  D --> E["Locate the intersection or backward extensions"]
  E --> F["Check the algebra against the drawing"]
```

For a converging thin lens, a ray parallel to the principal axis emerges through the far focal point. A ray through the optical center continues approximately undeviated. A ray through the near focal point emerges parallel to the axis. Any two independent rays locate the image.

The lens equation can be obtained from similar triangles in a paraxial ray diagram. The small-angle approximation $\tan\theta\approx\theta$ allows the surface geometry to be summarized by a single focal length. Rays far from the axis violate that approximation and contribute spherical aberration. Dispersion adds chromatic aberration because $n$, and hence $f$, depends on wavelength.

For a thin lens in air with surface radii $R_1$ and $R_2$, the lensmaker equation is

$$
\frac{1}{f}=(n-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right).
$$

The signs of the radii depend on which side their centers of curvature lie. The equation explains two useful trends without detailed ray tracing: increasing the index strengthens the lens, and tighter curvature shortens the focal length. A biconvex lens has positive power under the usual radius convention; a biconcave lens has negative power.

Optometrists often use optical power

$$
P=\frac{1}{f},
$$

with $f$ in meters and $P$ in diopters. Thin lenses in contact have powers that add:

$$
P_{\text{eq}}=P_1+P_2.
$$

A $+2.0\,\mathrm D$ lens combined with a $-0.50\,\mathrm D$ lens gives $+1.5\,\mathrm D$, corresponding to

$$
f_{\text{eq}}=\frac{1}{1.5\,\mathrm{m^{-1}}}=0.67\,\mathrm m.
$$

Separated lenses require an additional spacing term, so the contact rule should not be applied to an arbitrary two-lens instrument.

## What an optical instrument changes

A camera places a real image on a sensor. Focusing changes the lens-to-sensor distance or the effective focal length until the sensor coincides with the image plane. For a distant subject, $d_o$ is much larger than $f$, so the lens equation gives $d_i\approx f$. A nearby subject requires $d_i\gt f$. The aperture controls the cone of accepted rays: closing it reduces aberration and increases depth of field, but admits less light and eventually strengthens diffraction.

The eye also forms a real inverted image, on the retina. Accommodation changes the crystalline lens's optical power while the retina stays at nearly fixed distance. A magnifier does something different: it forms an enlarged virtual image that the eye then focuses. Telescopes and microscopes use an objective to create an intermediate image and an eyepiece to increase its angular size. Their useful measure is usually angular magnification, not the transverse magnification of one lens alone.

Ray tracing predicts these image locations without describing resolution or brightness completely. Aperture size, diffraction, transmission losses, detector response, and aberrations determine how much detail survives after the geometric image has been located.

## Worked image: object beyond twice the focal length

An object $4.0\,\mathrm{cm}$ tall is $30.0\,\mathrm{cm}$ from a converging lens of focal length $10.0\,\mathrm{cm}$. The object lies beyond $2f$, so the image should be real, inverted, and reduced, between $f$ and $2f$ on the far side.

Solve for image distance:

$$
\begin{aligned}
\frac{1}{d_i}
&=\frac{1}{f}-\frac{1}{d_o}\\
&=\frac{1}{10.0\,\mathrm{cm}}-\frac{1}{30.0\,\mathrm{cm}}\\
&=\frac{2}{30.0\,\mathrm{cm}}.
\end{aligned}
$$

Thus

$$
d_i=15.0\,\mathrm{cm}.
$$

The magnification and height are

$$
m=-\frac{15.0}{30.0}=-0.500,
\qquad
h_i=mh_o=(-0.500)(4.0\,\mathrm{cm})=-2.0\,\mathrm{cm}.
$$

The signs reproduce the prediction. A screen placed $15.0\,\mathrm{cm}$ behind the lens would capture the image.

## Worked image: object inside the focal length

Move the same object to $6.0\,\mathrm{cm}$ from the lens. Rays leaving the lens diverge, so the eye traces them backward to a virtual image. Algebra gives

$$
\begin{aligned}
\frac{1}{d_i}
&=\frac{1}{10.0}-\frac{1}{6.0}\\
&=\frac{3-5}{30}\\
&=-\frac{1}{15},
\end{aligned}
$$

with distances in centimeters. Hence

$$
d_i=-15.0\,\mathrm{cm}.
$$

Then

$$
m=-\frac{-15.0}{6.0}=+2.50,
\qquad
h_i=(2.50)(4.0\,\mathrm{cm})=10.0\,\mathrm{cm}.
$$

The virtual image is on the object's side, upright, and enlarged. It cannot be projected onto a screen because rays do not actually converge there. A magnifying glass operates in this regime.

## Mirrors and the origin of focal length

For a spherical mirror in the paraxial limit,

$$
f=\frac{R}{2},
$$

where $R$ is the radius of curvature. A concave mirror is converging and a convex mirror is diverging. The same formal image equation applies under a consistent mirror sign convention. Reflection reverses the propagation direction, so importing lens signs without checking the convention often causes mistakes.

The focal point is exact only for rays close to the principal axis. Marginal rays on a spherical concave mirror focus closer to the mirror than paraxial rays. A parabolic mirror removes spherical aberration for incoming rays parallel to its axis, which is why reflecting telescopes and radio dishes use paraboloidal surfaces.

Plane mirrors are a useful limiting case: their radius and focal length are infinite. An object a distance $d$ in front of a plane mirror produces a virtual image the same distance behind it, with magnification $+1$. The image is commonly called “laterally inverted,” but the geometry is better described as front-to-back reversal. The mirror does not exchange left and right axes on the object; it reverses the coordinate perpendicular to its surface.

Two plane mirrors also show how repeated image formation works. With mirrors at right angles, each mirror forms an image of the object and one mirror forms an image of the other's image, giving three images for a generic object position. At special angles and placements, images can overlap. Counting reflected paths is more reliable than memorizing a formula without its symmetry conditions.

## Limits and checks

- Angles in reflection and refraction are measured from the normal. An angle from the surface must be replaced by its complement.
- Frequency remains fixed at a stationary interface; speed and wavelength change.
- Real and virtual describe whether rays actually meet. Upright and inverted describe orientation. Neither term determines the other.
- A negative image distance has a geometric meaning under the chosen convention; discarding the sign loses that information.
- The thin-lens equation assumes negligible thickness and small ray angles. Thick lenses require principal planes, and large apertures expose aberrations.
- Ray optics does not set the ultimate resolution. Diffraction limits how finely even a perfect lens can distinguish nearby points.

Whenever the calculated image contradicts the preliminary ray sketch, check the sign convention and object location before accepting the numerical result.

<div className="see-also">

See also: [Interference, Diffraction, and Gratings](/physics/general/interference-diffraction-and-gratings) · [AC Circuits and Electromagnetic Waves](/physics/general/ac-circuits-and-electromagnetic-waves) · [Measurement, Units, and Vectors](/physics/general/measurement-units-and-vectors)

</div>
