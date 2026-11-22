---
title: "Coulomb's Law and Electric Fields"
sidebar_position: 16
---

# Coulomb's Law and Electric Fields

Electric charge is the source of electric force. Coulomb's law gives the interaction between stationary point charges; the electric-field description separates the source charges from the charge used to probe their effect.

Charge is conserved and quantized. The net charge of an isolated system does not change, although positive and negative charges may be transferred or created in equal amounts. An object's charge is an integer multiple of

$$
e=1.602\times10^{-19}\,\mathrm C.
$$

Macroscopic values involve enormous numbers of elementary charges: $1\,\mathrm{nC}$ corresponds to about $6.24\times10^9$ electron charges. Charging ordinary matter usually means moving electrons; protons remain bound in nuclei.

## From pairwise force to a field

For two point charges separated by distance $r$, the force magnitude is

$$
F=k\frac{\lvert q_1q_2\rvert}{r^2},
\qquad
k=\frac{1}{4\pi\epsilon_0}.
$$

The force acts along the line joining the charges. Like signs repel and opposite signs attract. A vector form that carries the direction explicitly is

$$
\vec F_{12}
=k\frac{q_1q_2}{r_{12}^2}\hat r_{12},
$$

where $\hat r_{12}$ points from charge 1 to charge 2 and $\vec F_{12}$ is the force on charge 2 due to charge 1.

A notation that is harder to misuse starts with position vectors. If the source $q_1$ is at $\vec r_1$ and the target $q_2$ is at $\vec r_2$, let $\vec R=\vec r_2-\vec r_1$. Then

$$
\vec F_{1\to2}
=\frac{1}{4\pi\epsilon_0}
\frac{q_1q_2}{|\vec R|^3}\vec R.
$$

The denominator is cubed because $\vec R$ already contains one power of distance. Interchanging the labels reverses $\vec R$, so Newton's third law follows: $\vec F_{2\to1}=-\vec F_{1\to2}$.

Coulomb's law has the same spatial form as Newtonian gravity, but electric force can attract or repel and is vastly stronger at particle scales. In a homogeneous linear dielectric, simple macroscopic calculations replace $\epsilon_0$ by the material permittivity $\epsilon$.

The electric field is defined as force per unit positive test charge:

$$
\vec E=\frac{\vec F}{q_0}.
$$

A point source charge $q$ produces

$$
\vec E=k\frac{q}{r^2}\hat r.
$$

Its units are

$$
[E]=\mathrm{N/C}=\mathrm{V/m}.
$$

The test charge is understood to be small enough not to rearrange the sources. That qualification matters near conductors, where an inserted charge can induce surface-charge motion.

Once the field is known, any charge placed there experiences

$$
\vec F=q\vec E.
$$

For a negative charge, the force points opposite the field.

## Superposition is a vector sum

Each source contributes independently:

$$
\vec E_{\mathrm{net}}=\sum_i\vec E_i,
\qquad
\vec F_{\mathrm{net}}=q_0\vec E_{\mathrm{net}}.
$$

Resolve the individual fields into components before adding them. Adding only magnitudes loses cancellation and direction.

```mermaid
graph LR
  A[Source charges] --> B[Field from each source]
  B --> C[Resolve into components]
  C --> D[Add vectors]
  D --> E[Apply force to a test charge]
```

| Quantity | Meaning | Check |
|---|---|---|
| $q$ | source or test charge | sign determines direction |
| $\vec E$ | force per unit positive charge | depends on sources, not on the test charge |
| $\vec F=q\vec E$ | force on a placed charge | reverses for negative $q$ |
| $r$ | source-to-field-point distance | point-charge field falls as $1/r^2$ |

Two equal positive charges at $x=\pm0.10\,\mathrm{m}$ produce equal-magnitude fields at the origin. One points in $+\hat i$ and the other in $-\hat i$, so

$$
\vec E_{\mathrm{net}}=E\hat i-E\hat i=0.
$$

The zero field at one point does not mean the sources are absent or that the field vanishes nearby.

### Worked example: a two-dimensional vector sum

Place $q_1=+3.0\,\mathrm{nC}$ at $(0,0)$ and $q_2=-3.0\,\mathrm{nC}$ at $(0.40,0)\,\mathrm m$. Find the field at $P=(0,0.30)\,\mathrm m$.

For $q_1$, the displacement to $P$ is $0.30\hat{\mathbf j}\,\mathrm m$, so

$$
\vec E_1
=k\frac{3.0\times10^{-9}}{(0.30)^2}\hat{\mathbf j}
=300\hat{\mathbf j}\,\mathrm{N/C}.
$$

For $q_2$,

$$
\vec R_2=(-0.40\hat{\mathbf i}+0.30\hat{\mathbf j})\,\mathrm m,
\qquad |\vec R_2|=0.50\,\mathrm m.
$$

Because $q_2$ is negative, its field points from $P$ toward $q_2$, along $0.8\hat{\mathbf i}-0.6\hat{\mathbf j}$. Its magnitude is

$$
E_2=k\frac{3.0\times10^{-9}}{(0.50)^2}=108\,\mathrm{N/C}.
$$

Thus

$$
\begin{aligned}
\vec E_2&=(86.4\hat{\mathbf i}-64.8\hat{\mathbf j})\,\mathrm{N/C},\\
\vec E_{\mathrm{net}}
&=(86.4\hat{\mathbf i}+235.2\hat{\mathbf j})\,\mathrm{N/C},\\
E&=\sqrt{86.4^2+235.2^2}=251\,\mathrm{N/C},\\
\theta&=\tan^{-1}(235.2/86.4)=69.8^\circ.
\end{aligned}
$$

The angle is above the positive $x$-axis. Establishing each direction before inserting signs avoids reversing the negative charge's contribution twice.

## Force between two nanocoulomb charges

Charges $+4.0\,\mathrm{nC}$ and $-6.0\,\mathrm{nC}$ are separated by $0.030\,\mathrm{m}$. Their force magnitude is

$$
\begin{aligned}
F
&=(8.99\times10^9\,\mathrm{N\,m^2/C^2})
\frac{\lvert(4.0\times10^{-9}\,\mathrm C)(-6.0\times10^{-9}\,\mathrm C)\rvert}
{(0.030\,\mathrm m)^2}\\
&=2.40\times10^{-4}\,\mathrm N.
\end{aligned}
$$

The opposite signs make the force attractive: each charge is pulled toward the other. Doubling their separation would reduce the magnitude by a factor of four.

The calculation assumes each charged object is small compared with the separation. Conducting spheres close together redistribute their surface charge, so the point-charge approximation may be poor. A spherically symmetric distribution still has the external field of a point charge at its center.

## From discrete charges to charge density

An extended distribution is divided into elements $dq$. Superposition becomes

$$
\vec E(\vec r)
=\frac1{4\pi\epsilon_0}
\int\frac{\vec r-\vec r'}{|\vec r-\vec r'|^3}\,dq.
$$

The charge element depends on the geometry:

$$
dq=\lambda\,d\ell,
\qquad
dq=\sigma\,dA,
\qquad
dq=\rho\,dV
$$

for line, surface, and volume densities, with units $\mathrm{C/m}$, $\mathrm{C/m^2}$, and $\mathrm{C/m^3}$.

### Worked example: field on the axis of a charged ring

A ring of radius $a$ carries uniform total charge $Q$. Find the field at a point a distance $z$ along its axis. Every charge element is the same distance $r=\sqrt{a^2+z^2}$ from the point. Opposite elements have transverse components that cancel. The axial component from $dq$ is

$$
dE_z
=k\frac{dq}{a^2+z^2}\cos\theta,
\qquad
\cos\theta=\frac{z}{\sqrt{a^2+z^2}}.
$$

All remaining factors are constant around the ring, so

$$
\begin{aligned}
E_z
&=k\frac{z}{(a^2+z^2)^{3/2}}\int dq\\
&=\frac1{4\pi\epsilon_0}
\frac{Qz}{(a^2+z^2)^{3/2}}.
\end{aligned}
$$

At $z=0$ the field vanishes. Far away, $z\gg a$, it approaches $kQ/z^2$. Differentiating shows that the axial magnitude is largest at $\vert z\vert =a/\sqrt2$.

## Electric dipoles

Charges $+q$ and $-q$ separated by displacement $\vec d$ from negative to positive form a dipole with moment

$$
\vec p=q\vec d.
$$

At distances much larger than $d$, its field falls as $1/r^3$, faster than a point charge's $1/r^2$ field because the net charge is zero. Along the axis,

$$
E_{\mathrm{axis}}\approx\frac1{4\pi\epsilon_0}\frac{2p}{r^3},
$$

while on the perpendicular bisector its magnitude is approximately $kp/r^3$ and it points opposite $\vec p$.

In a uniform external field, the two forces cancel in translation but form a torque:

$$
\vec\tau=\vec p\times\vec E,
\qquad
U=-\vec p\cdot\vec E.
$$

The stable orientation has $\vec p$ parallel to $\vec E$. A nonuniform field can also exert a net force, which accounts for the attraction of polarized neutral matter toward a charged object.

## Reading field-line diagrams

Field lines are a representation, not physical filaments.

- The tangent to a line gives the direction of $\vec E$.
- Greater line density represents a stronger field.
- Lines begin on positive charge and end on negative charge or at infinity.
- Lines do not cross, because a field cannot point in two directions at one point.

The number of lines drawn is conventional. Only relative density and geometry carry information.

Field lines meet an ideal conductor in electrostatic equilibrium perpendicularly. A tangential component would drive surface charges. The field inside the conducting material is zero, and excess charge resides on its surface. These claims apply after electrostatic equilibrium; a resistive wire carrying steady current has a nonzero internal electric field.

## Direction errors to catch early

Distinguish the source charge from the test charge. The source determines $\vec E$; the sign of the test charge determines whether its force follows or opposes that field. Keep the unit vector until the vector sum is complete, especially for configurations that are not one-dimensional.

Point-charge formulas also have a domain. They apply directly to particles or spherically symmetric charge distributions observed from outside. For extended asymmetric distributions, divide the charge into elements and integrate, or use Gauss's law when the symmetry supports it.

Several checks catch most algebra errors. Field must scale linearly with source charge and have units of $\mathrm{N/C}$. A far-away finite distribution should resemble its net point charge to leading order. Symmetry can eliminate components before integration, but it cannot assign the remaining magnitude. At the source point the ideal point-charge field diverges; that singularity marks the limit of the classical point model rather than a measurable infinite field inside a finite object.

## How the inverse-square law is tested

Coulomb's torsion-balance experiments compared the twist of a fine fiber under electrostatic forces at different separations. A torsion balance translates a small horizontal force into an angular deflection, allowing much weaker forces to be measured than with an ordinary spring scale. Modern tests are more precise, but the logic remains: change distance while controlling charge and look for the exponent in the force law.

The numerical constant $k$ depends on the unit system. SI writes the vacuum permittivity explicitly and defines charge through the ampere and second. The value of $\epsilon_0$ is therefore tied to the SI electromagnetic conventions, while the inverse-square content lies in the spatial dependence and vector direction.

Inverse-square behavior has a geometric consequence. A sphere centered on a point charge has area proportional to $r^2$, exactly canceling the field's decrease in the total flux. Gauss's law expresses that global relation. Coulomb's law gives the field of a point source; superposition then recovers the field of any classical static distribution.

## Near fields, far fields, and multipoles

At large distance, details of a localized charge distribution become progressively less important. The leading term is set by total charge $Q$ and falls as $1/r^2$. If $Q=0$, that term vanishes and the dipole term, falling as $1/r^3$, usually dominates. If both net charge and dipole moment vanish, quadrupole and higher moments control the far field and decay still faster.

The ordering is useful before any calculation. A neutral molecule may have a permanent dipole and interact strongly with a distant field gradient. A symmetric neutral distribution may have no dipole, leaving a weaker quadrupole response. Shifting the coordinate origin does not change total charge; for a neutral distribution, it also does not change the dipole moment.

For a point on the axis of charges $+q$ and $-q$ separated by distance $d$, the exact field at distance $r$ from the midpoint is a difference of two inverse squares. When $r\gg d$, expanding those terms leaves the leading value $2kp/r^3$. The approximation should not be used when the observation distance is comparable with the separation.

## Fields in matter

A conductor contains mobile charge that rearranges until its electrostatic interior field vanishes. An insulator lacks freely moving bulk charge, but its atoms and molecules polarize slightly. Positive and negative bound charge shift in opposite directions, creating induced dipoles. The resulting field partly opposes the applied field.

In a linear isotropic dielectric, polarization is proportional to field over a limited range. The simple replacement of $\epsilon_0$ by $\epsilon=\kappa\epsilon_0$ works for highly symmetric problems filled uniformly with one material. At interfaces or in nonuniform dielectrics, bound surface and volume charges must be included more carefully. Strong fields can make response nonlinear or cause breakdown.

Neutral objects can therefore feel electric forces. A charged rod brought near neutral paper polarizes the paper. The opposite induced charge lies slightly closer than the like induced charge, and the stronger near-side attraction wins. The effect does not require the paper to acquire net charge.

## Equilibrium and the limits of electrostatic trapping

A charge at a point where $\vec E=0$ has zero instantaneous electric force, but stability requires examining nearby points. Between two equal positive charges, the midpoint field vanishes. A small displacement along the line joining them is driven away from the midpoint, while a small perpendicular displacement can be restored. The point is a saddle, not a stable three-dimensional trap.

Earnshaw's theorem formalizes the limitation: fixed classical point charges cannot create a stable electrostatic equilibrium for another free charge in empty space. Stable confinement needs additional physics, such as time-varying fields, magnetic forces, material constraints, or quantum effects. The theorem does not prohibit a bead constrained to move along one line from having stable equilibrium along that restricted coordinate.

Force balance between several charges also needs care because the charges producing the field may themselves move. A configuration can have zero net force on one selected charge while large forces act on the sources. Treating sources as fixed implies an external support that absorbs those reactions.

## From field to motion

Once the field is known, Newton's law determines a particle's acceleration:

$$
m\frac{d^2\vec r}{dt^2}=q\vec E(\vec r,t).
$$

In a uniform field, acceleration is constant and the trajectory is the same parabola as projectile motion, with $q\vec E/m$ replacing gravity. In a nonuniform field, acceleration changes with position and numerical integration may be required.

For an electron and proton in the same field, force magnitudes are equal because their charge magnitudes match, but the accelerations differ inversely with mass and point in opposite directions. Ignoring mass when moving from field to motion is as serious as ignoring the charge sign.

Dimensional estimates help before detailed work. A nanocoulomb at a centimetre produces a field of order $10^5\,\mathrm{N/C}$; the same charge at a metre produces only order ten. Such estimates expose misplaced metric prefixes and squared-distance errors quickly.

<div className="see-also">

See also: [Gauss's Law](/physics/general/gausss-law-and-electric-flux) · [Electric Potential and Capacitance](/physics/general/electric-potential-and-capacitance)

</div>
