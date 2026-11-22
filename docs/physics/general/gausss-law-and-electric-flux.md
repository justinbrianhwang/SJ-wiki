---
title: "Gauss's Law and Electric Flux"
sidebar_position: 17
---

# Gauss's Law and Electric Flux

Electric flux measures the component of a field passing through a surface. Gauss's law relates the net flux through any closed surface to the charge inside it. Symmetry determines whether that relation can also be solved easily for the field.

Flux is an integral, not a new kind of field. Its units are $\mathrm{N\,m^2/C}$, and it can be positive, negative, or zero depending on orientation. The word “flow” is only an analogy: field lines are not material moving through a surface.

## Flux keeps track of orientation

For an oriented surface,

$$
\Phi_E=\int\vec E\cdot d\vec A.
$$

The area vector is normal to the surface. For a flat area in a uniform field,

$$
\Phi_E=EA\cos\theta,
$$

where $\theta$ is the angle between $\vec E$ and the area normal. A field tangent to the surface gives zero flux through it, even when the field magnitude is large.

For a closed surface, $d\vec A$ points outward and the integral is written with a circle:

$$
\oint\vec E\cdot d\vec A.
$$

Outward crossings contribute positive flux; inward crossings contribute negative flux.

For a small patch, $d\Phi_E=E\cos\theta\,dA$. A curved surface is handled by summing these local contributions. Reversing the normal reverses the flux through an open surface. A closed surface has the standard outward orientation.

Put a point charge $q$ at the center of a sphere of radius $r$. The field is normal and constant, so

$$
\Phi_E=E(4\pi r^2)
=\left(k\frac q{r^2}\right)(4\pi r^2)
=\frac q{\epsilon_0}.
$$

The cancellation of $r^2$ expresses inverse-square geometry: the same total flux spreads across larger spherical areas. More generally, flux from a point charge through an open patch is $(q/4\pi\epsilon_0)$ times the solid angle subtended by that patch.

## What Gauss's law says and what symmetry adds

Gauss's law is

$$
\oint\vec E\cdot d\vec A
=\frac{q_{\mathrm{enc}}}{\epsilon_0}.
$$

Only enclosed net charge appears on the right. Charges outside the surface can alter the field at every point on the surface, but their contributions to the total flux cancel.

The local form is

$$
\nabla\cdot\vec E=\frac{\rho}{\epsilon_0}.
$$

Divergence measures outward flux per unit volume. Integrating over a volume and applying the divergence theorem recovers the integral law. The integral form suits symmetric fields; the differential form suits local field equations and numerical work.

Gauss's law always holds, but solving for $E$ needs more than a chosen surface. The distribution must force the field direction and magnitude to behave simply there. A cube around a point charge has known total flux, yet the field is not constant on each face, so the cube does not easily derive the field.

```mermaid
graph LR
  A[Identify charge symmetry] --> B[Choose a matching closed surface]
  B --> C[Determine field direction]
  C --> D[Find where field magnitude is constant]
  D --> E[Evaluate the flux integral]
  E --> F[Relate flux to enclosed charge]
```

| Charge symmetry | Gaussian surface | Flux simplification |
|---|---|---|
| Spherical | concentric sphere | $E$ constant and normal everywhere |
| Cylindrical | coaxial cylinder | curved side contributes; end caps do not |
| Planar | pillbox | two flat faces contribute |
| No sufficient symmetry | any closed surface | law remains true, but usually does not isolate $E$ |

A Gaussian surface is an imaginary integration surface, chosen for convenience. It need not coincide with a material boundary.

## Field of a very long line charge

For an infinite line with linear charge density $\lambda$, choose a coaxial cylinder of radius $r$ and length $L$. Cylindrical symmetry makes the field radial and constant on the curved side. The field is parallel to the end caps, so their flux is zero:

$$
E(2\pi rL)=\frac{\lambda L}{\epsilon_0}.
$$

Thus

$$
E=\frac{\lambda}{2\pi\epsilon_0r}.
$$

For $\lambda=3.0\times10^{-6}\,\mathrm{C/m}$ at $r=0.20\,\mathrm m$,

$$
\begin{aligned}
E
&=\frac{3.0\times10^{-6}}
{2\pi(8.85\times10^{-12})(0.20)}\\
&=2.70\times10^5\,\mathrm{N/C}.
\end{aligned}
$$

The direction is radially outward for positive $\lambda$ and inward for negative $\lambda$. The $1/r$ dependence differs from the $1/r^2$ field of a point charge because the source has cylindrical rather than spherical symmetry.

The result approximates a finite wire only when the observation point is much closer to the wire than to either end. Near an end, the field has an axial component and is not constant on a coaxial cylinder.

## Spherical charge distributions

For any spherically symmetric density $\rho(r)$, a concentric sphere gives

$$
E(r)4\pi r^2=\frac{q_{\mathrm{enc}}(r)}{\epsilon_0},
\qquad
E(r)=\frac1{4\pi\epsilon_0}\frac{q_{\mathrm{enc}}(r)}{r^2}.
$$

Outside the distribution, $q_{\mathrm{enc}}=Q$ and the field equals that of a point charge at the center. Inside, only charge at smaller radii enters. Outer spherical shells contribute zero net field at an interior point.

### Worked example: uniformly charged solid sphere

Let a nonconducting sphere of radius $R$ carry charge $Q$ uniformly. Its density is

$$
\rho=\frac{Q}{(4/3)\pi R^3}.
$$

For $r\lt R$,

$$
q_{\mathrm{enc}}=\rho\frac43\pi r^3
=Q\frac{r^3}{R^3}.
$$

Therefore

$$
E(r)=\frac1{4\pi\epsilon_0}\frac{Qr}{R^3}.
$$

The interior field grows linearly from zero. For $r\geq R$,

$$
E(r)=\frac1{4\pi\epsilon_0}\frac Q{r^2}.
$$

Both expressions give $kQ/R^2$ at the surface. A conducting sphere differs: all excess charge lies on its surface and the field inside the material is zero.

## Infinite sheets and parallel plates

An infinite sheet with uniform density $\sigma$ has a perpendicular field of equal magnitude on both sides. A pillbox crossing it gives

$$
2EA=\frac{\sigma A}{\epsilon_0},
\qquad
E=\frac{\sigma}{2\epsilon_0}.
$$

The ideal sheet field does not decrease with distance. The approximation holds near the center of a finite plate when the distance is small compared with plate dimensions.

Two oppositely charged parallel sheets superpose. Between them the fields add to

$$
E=\frac{\sigma}{\epsilon_0},
$$

while outside they cancel. This is the field model behind the parallel-plate capacitor.

### Worked example: field of a thick slab

An infinite insulating slab occupies $-a\leq x\leq a$ and has uniform volume density $\rho$. Symmetry makes the field point along the $x$-axis and vanish at the midplane.

For $\vert x\vert \lt a$, a pillbox extending from $-x$ to $+x$ gives

$$
2EA=\frac{\rho(2xA)}{\epsilon_0},
\qquad
E_x=\frac{\rho x}{\epsilon_0}.
$$

Outside, the pillbox encloses the full thickness:

$$
2EA=\frac{\rho(2aA)}{\epsilon_0},
\qquad
|E|=\frac{\rho a}{\epsilon_0}.
$$

The field grows linearly inside and remains constant outside, matching continuously at each boundary.

## Flux can be known without knowing the field

If a closed surface encloses $+5.0\,\mathrm{nC}$, its total flux is fixed regardless of the surface's shape or the charge's position inside:

$$
\Phi_E=\frac{q_{\mathrm{enc}}}{\epsilon_0}
=\frac{5.0\times10^{-9}}{8.85\times10^{-12}}
=5.65\times10^2\,\mathrm{N\,m^2/C}.
$$

The local field can be highly nonuniform while this integral remains unchanged.

## Conductors in electrostatic equilibrium

For a conductor at electrostatic equilibrium:

- The electric field inside the conducting material is zero.
- Any excess charge resides on the surface.
- The conductor is an equipotential.
- The electric field immediately outside is normal to the surface.

A Gaussian surface lying entirely within the conducting material has zero flux and therefore encloses zero net charge. A cavity with no charge inside has zero field when fully enclosed by a conductor in electrostatic equilibrium; a charged cavity changes the induced surface-charge distribution.

If a charge $q$ is placed in a cavity, a Gaussian surface in the surrounding conductor has zero field and hence zero enclosed charge. The cavity wall must carry total induced charge $-q$. If the conductor itself has net charge $Q$, its outer surface carries $Q+q$. The detailed wall distribution depends on the charge position, but its total does not.

Immediately outside a conductor, a thin pillbox gives

$$
E_{\perp,\mathrm{out}}=\frac{\sigma}{\epsilon_0}
$$

when the inside field is zero. Charge crowds near sharp regions of small curvature radius, producing larger fields. If the field reaches the medium's breakdown strength, charge can leak through corona or a spark.

A closed conductor shields an empty cavity from external static fields. The converse needs care: a charge in a cavity can alter the outer surface charge unless the conductor is grounded. Grounding permits charge exchange with Earth while fixing conductor potential.

## Zero flux is not zero field

Zero enclosed charge implies zero net flux, not zero field at each point. A closed surface placed in a uniform external field has as much flux entering as leaving. Conversely, a nonzero field can be tangent to an open surface and produce zero flux through it.

The fastest consistency checks are geometric: verify the outward normal, include only enclosed charge, and ask whether symmetry actually makes $E$ constant or makes the dot product vanish on each part of the surface.

Do not count a charge merely because it is near the surface; only inside-or-outside status matters. A charge exactly on an ideal Gaussian surface is handled by a limiting surface or a boundary condition. Also distinguish zero enclosed **net** charge from no enclosed charge: equal positive and negative charges give zero total flux while producing a complicated nonzero field.

## A disciplined symmetry test

Before drawing a Gaussian surface, identify transformations that leave the source unchanged. Spherical symmetry requires invariance under every rotation about one point. Cylindrical symmetry requires rotations about and translations along an axis. Planar symmetry requires translations within and rotations about the normal to an infinite plane.

Then ask what those transformations force the field to do. Spherical symmetry permits only a radial field whose magnitude depends on radius. Cylindrical symmetry permits a radial field depending only on distance from the axis. Planar symmetry permits a normal field depending only on distance from the plane. The Gaussian surface comes last, chosen to exploit those conclusions.

Finite rods, disks, and plates lack the full translation symmetry of their infinite idealizations. A long wire may be approximated as infinite near its middle, and a large sheet may be approximated as infinite close to its center. The quality of the approximation depends on dimensionless ratios such as distance divided by wire length or plate width.

A common failed strategy chooses a sphere merely because spheres are easy to integrate. Around a nonspherical distribution, the field need not be radial or constant on that sphere. Gauss's law then supplies one integral number but not the many local values needed to determine the field.

## Piecewise fields and boundary behavior

Charge distributions with several regions require a separate enclosed-charge expression in each region. A thick spherical shell, for example, has an empty cavity, charged material, and exterior. The field formula changes when the Gaussian radius crosses each boundary, although physical continuity rules constrain how pieces join.

The normal electric field has a jump across a surface charge:

$$
E_{2\perp}-E_{1\perp}=\frac{\sigma}{\epsilon_0}.
$$

This follows from a vanishingly thin pillbox. With no surface charge, the normal component is continuous. Electrostatics also makes the tangential component continuous; otherwise a shrinking rectangular loop would have nonzero circulation. At a conductor surface, the inside field is zero, leaving the earlier result $E_\perp=\sigma/\epsilon_0$ outside.

Volume charge can make the slope of the field change without making the field itself jump. In the uniformly charged solid sphere, $E$ is continuous at the boundary but its derivative changes. A mathematical surface charge is the limiting case that produces a finite jump.

## Recovering potential after using Gauss's law

Gauss's law often gives field first. Potential follows from

$$
V(b)-V(a)=-\int_a^b\vec E\cdot d\vec l.
$$

For the infinite line field,

$$
V(r_2)-V(r_1)
=-\frac{\lambda}{2\pi\epsilon_0}\ln\frac{r_2}{r_1}.
$$

One cannot choose zero potential at infinity because the logarithm diverges. A finite reference radius is required. This is not a failure of the field; it reflects the infinite source idealization.

For the uniformly charged solid sphere, choose zero at infinity and integrate the exterior and interior pieces. The result inside is

$$
V(r)=\frac{kQ}{2R}\left(3-\frac{r^2}{R^2}\right),
\qquad r\leq R.
$$

It joins the exterior value $kQ/R$ at the surface and has zero slope at the center. Potential remains finite where the symmetric field vanishes.

## Flux in numerical and experimental settings

When symmetry is absent, Gauss's law remains a stringent check on a computed field. A numerical solver can integrate its field over a closed mesh and compare the result with enclosed charge divided by $\epsilon_0$. Failure signals inadequate resolution, incorrect boundary conditions, or a field that does not satisfy Maxwell's equation.

Flux also explains why shielding and charge measurement work. A Faraday cup surrounds an inserted charged object with a conductor. Induced charge on the cup can be measured through the conductor's potential or transferred charge, while the detailed location of the object inside does not change the total induced amount under ideal conditions.

The magnetic analogue has a decisive difference: the net magnetic flux through every closed surface is zero, expressed by $\nabla\cdot\vec B=0$. Electric fields have charges as sources and sinks; ordinary magnetic fields form continuous loops. The similar-looking flux integrals therefore encode different source structures.

<div className="see-also">

See also: [Coulomb's Law and Electric Fields](/physics/general/coulombs-law-and-electric-fields) · [Magnetic Sources and Induction](/physics/general/ampere-faraday-lenz-and-inductance)

</div>
