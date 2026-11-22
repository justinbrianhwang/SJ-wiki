---
title: Centroids and Second Moments
sidebar_position: 8
---

# Centroids and Second Moments

Centroids and second moments connect geometry to mechanics. A centroid locates a weighted center. A second moment measures how widely area or mass is spread about a specified axis. The formulas resemble one another, but their meanings and units do not.

The three questions to attach to every calculation are: what is being integrated, where is the reference axis, and what are the units? A first moment of area answers a location question. A second moment of area enters bending and deflection. A mass moment of inertia enters rotational dynamics.

## From a weighted average to an integral

For point masses, the center coordinate is a weighted average,

$$
\bar{x}=\frac{\sum_i m_i x_i}{\sum_i m_i}.
$$

Replace the discrete masses by small elements $dm$ and take the limit:

$$
\bar{x}=\frac{1}{m}\int x\,dm,
\qquad
\bar{y}=\frac{1}{m}\int y\,dm,
\qquad
m=\int dm.
$$

For a uniform thin plate, $dm=\rho_A\,dA$ with constant areal density $\rho_A$. The density cancels, leaving the **area centroid**

$$
\bar{x}=\frac{1}{A}\int_A x\,dA,
\qquad
\bar{y}=\frac{1}{A}\int_A y\,dA.
$$

The corresponding first moments are

$$
Q_y=\int_A x\,dA=A\bar{x},
\qquad
Q_x=\int_A y\,dA=A\bar{y}.
$$

The subscript identifies the axis about which the moment is taken, so $Q_x$ contains the perpendicular distance $y$. Some books reverse the subscript convention; checking the defining integral is safer than trusting the symbol alone.

Symmetry should be used before integration. Reflection about the $y$ axis pairs each area element at $x$ with one at $-x$, so their contributions to $\int x\,dA$ cancel and $\bar{x}=0$. A centroid must lie on every symmetry line, though it need not lie inside the material. The centroid of a semicircular arc or a C-shaped area can sit in empty space.

For a composite area divided into pieces whose centroids are known,

$$
\bar{x}=\frac{\sum_i A_i x_i}{\sum_i A_i},
\qquad
\bar{y}=\frac{\sum_i A_i y_i}{\sum_i A_i}.
$$

Holes are entered with negative signed area. Their centroid coordinates remain ordinary coordinates; only the area carries the minus sign. This convention is algebraically identical to subtracting the hole integrals from the solid-region integrals.

## Squared distance and bending resistance

The second moments of area about Cartesian axes are

$$
I_x=\int_A y^2\,dA,
\qquad
I_y=\int_A x^2\,dA.
$$

Area far from an axis contributes disproportionately because the distance is squared. Two sections can have equal area yet very different $I_x$. Moving material away from the neutral axis is the geometric reason an I-section can be much stiffer in bending than a compact rectangle of comparable area.

The product of inertia and polar second moment are

$$
I_{xy}=\int_A xy\,dA,
\qquad
J_O=\int_A (x^2+y^2)\,dA=I_x+I_y.
$$

$I_{xy}$ can be positive, negative, or zero. If either coordinate axis is a symmetry axis, reflected elements cancel in pairs and $I_{xy}=0$. The sign convention for product of inertia sometimes differs in stress-transformation texts, so transformation formulas should be used with the convention under which they were derived.

| Quantity | Integral | Units | Typical use |
|---|---|---|---|
| Area centroid | $\bar{x}=\int x\,dA/A$ | length | load location, neutral axis |
| First moment of area | $Q_x=\int y\,dA$ | length$^3$ | centroid and beam shear |
| Second moment of area | $I_x=\int y^2\,dA$ | length$^4$ | bending stress and deflection |
| Polar second moment | $J_O=\int r^2\,dA$ | length$^4$ | circular-shaft torsion |
| Mass moment of inertia | $I=\int r^2\,dm$ | mass length$^2$ | rotational dynamics |

The mass moment of inertia has the same mathematical form but a different measure:

$$
I_z=\int r^2\,dm.
$$

For constant density and thickness it is proportional to an area polar moment, but the two quantities are not interchangeable. Beam tables normally list area moments in mm$^4$ or in$^4$; dynamics tables list mass moments in kg m$^2$ or slug ft$^2$.

## Deriving two standard formulas

For a rectangle of width $b$ and height $h$, use a horizontal strip $dA=b\,dy$ about the centroidal $x$ axis:

$$
\begin{aligned}
I_x
&=\int_{-h/2}^{h/2}y^2b\,dy \\
&=b\left[\frac{y^3}{3}\right]_{-h/2}^{h/2}
=\frac{bh^3}{12}.
\end{aligned}
$$

Interchanging $x$ and $y$ gives

$$
I_y=\frac{hb^3}{12}.
$$

The cube belongs to the dimension perpendicular to the axis. That observation is more dependable than memorizing which letter goes where.

For a circle of radius $R$, polar coordinates give $dA=r\,dr\,d\theta$:

$$
\begin{aligned}
J_O
&=\int_0^{2\pi}\int_0^R r^2(r\,dr\,d\theta) \\
&=2\pi\left[\frac{r^4}{4}\right]_0^R
=\frac{\pi R^4}{2}.
\end{aligned}
$$

Symmetry requires $I_x=I_y$, and $J_O=I_x+I_y$, hence

$$
I_x=I_y=\frac{\pi R^4}{4}.
$$

These derivations show why tabulated formulas are tied to particular axes. A formula without an axis sketch is incomplete information.

### A triangle from the integral

Consider a triangle of base $b$ on the $x$ axis and height $h$, tapering linearly to zero width at $y=h$. A horizontal strip has width

$$
b(y)=b\left(1-\frac{y}{h}\right)
$$

and area $dA=b(y)\,dy$. Its second moment about the base is

$$
\begin{aligned}
I_{base}
&=\int_0^h y^2b\left(1-\frac{y}{h}\right)dy\\
&=b\left[\frac{y^3}{3}-\frac{y^4}{4h}\right]_0^h\\
&=\frac{bh^3}{12}.
\end{aligned}
$$

The triangle's area is $A=bh/2$, and its centroid lies $h/3$ above the base. Shift from the base to the parallel centroidal axis by rearranging the parallel-axis theorem:

$$
\begin{aligned}
I_c
&=I_{base}-A\left(\frac{h}{3}\right)^2\\
&=\frac{bh^3}{12}-\frac{bh}{2}\frac{h^2}{9}\\
&=\frac{bh^3}{36}.
\end{aligned}
$$

The edge-axis value is larger, as it must be. This calculation also shows that the parallel-axis theorem can be used in reverse only when the destination is the centroidal parallel axis and the subtraction remains consistent with $I_{base}=I_c+Ad^2$.

## Scaling and section efficiency

Uniformly scale every dimension of a cross section by a factor $s$. Its area scales as $s^2$, its first moments as $s^3$, and its second moments as $s^4$. Doubling a rectangular section's depth while retaining its shape multiplies $I$ by $16$. If only the depth is doubled while width stays fixed, $I_x=bh^3/12$ increases by a factor of $8$.

Beam bending uses the combination $EI$, where $E$ is a material property and $I$ is geometric. Bending stress under moment $M$ is

$$
\sigma=-\frac{My}{I},
$$

and the extreme stress is often written

$$
|\sigma_{max}|=\frac{|M|}{S},
\qquad
S=\frac{I}{c},
$$

where $S$ is the elastic section modulus and $c$ is the farthest distance from the neutral axis. Increasing depth helps twice: it spreads material far from the centroidal axis and usually increases the lever arm to the extreme fiber more slowly than it increases $I$.

The radius of gyration supplies another comparison. Since $I=Ak^2$, sections with the same area but larger $k$ place their material farther from the chosen axis. Thin-walled sections exploit this arrangement efficiently, although local buckling, shear deformation, connection details, and torsion can govern before the full bending efficiency is realized.

Neither $I$ nor $S$ is an intrinsic number for a shape without an axis. A tall rectangle is efficient about its horizontal centroidal axis and relatively weak about its vertical one. Rotating the same physical member by $90^\circ$ exchanges those roles.

## Moving an axis without reintegrating

Let $x_c$ be a centroidal axis and let a parallel axis $x$ be a perpendicular distance $d$ away. Write the distance of an element from $x$ as $y=y'+d$, where $y'$ is measured from $x_c$:

$$
\begin{aligned}
I_x
&=\int_A (y'+d)^2\,dA \\
&=\int_A y'^2\,dA+2d\int_A y'\,dA+d^2\int_A dA.
\end{aligned}
$$

The middle integral is zero because $x_c$ passes through the centroid. Therefore

$$
I_x=I_{x_c}+Ad^2.
$$

The parallel-axis theorem only connects parallel axes, and the reference formula must be centroidal. The added term is nonnegative, so among all parallel axes the centroidal one has the smallest second moment. The mass version follows by replacing $dA$ with $dm$:

$$
I_O=I_G+md^2.
$$

A related measure is the radius of gyration,

$$
k_x=\sqrt{\frac{I_x}{A}},
$$

the distance at which the whole area could be imagined concentrated while retaining the same second moment about the axis. For mass, $k=\sqrt{I/m}$. It is a compact measure of spread, not a physical radius of the boundary.

## Choosing the differential element

Direct integration is often shorter than decomposing a curved boundary into many familiar shapes. The useful element is the one that turns the region into a single integral. For an area under $y=f(x)$, a vertical strip has

$$
dA=y\,dx,
$$

and its own centroid lies at $(x,y/2)$. The area and first moments become

$$
A=\int y\,dx,
\qquad
Q_y=\int xy\,dx,
\qquad
Q_x=\frac12\int y^2\,dx.
$$

A horizontal strip may be better when $x$ is naturally a function of $y$. Neither choice changes the answer; it only changes the algebra. Double integrals are needed when the density varies in both directions or when no strip describes the region cleanly.

As an example, consider the parabolic spandrel bounded by

$$
y=h\left(\frac{x}{b}\right)^2,
$$

the $x$ axis, and $x=b$, for $0\le x\le b$. A vertical strip gives

$$
\begin{aligned}
A
&=\int_0^b h\frac{x^2}{b^2}\,dx \\
&=\frac{h}{b^2}\left[\frac{x^3}{3}\right]_0^b
=\frac{bh}{3}.
\end{aligned}
$$

The first moment about the $y$ axis is

$$
\begin{aligned}
Q_y
&=\int_0^b xh\frac{x^2}{b^2}\,dx \\
&=\frac{h}{b^2}\left[\frac{x^4}{4}\right]_0^b
=\frac{hb^2}{4}.
\end{aligned}
$$

Therefore

$$
\bar{x}=\frac{Q_y}{A}
=\frac{hb^2/4}{bh/3}
=\frac{3b}{4}.
$$

For the vertical coordinate, remember that each strip's centroid is at $y/2$:

$$
\begin{aligned}
Q_x
&=\int_0^b\frac{y}{2}\,dA
=\frac12\int_0^b y^2\,dx \\
&=\frac12\int_0^b
h^2\frac{x^4}{b^4}\,dx
=\frac{bh^2}{10}.
\end{aligned}
$$

Hence

$$
\boxed{\bar{x}=\frac{3b}{4},\qquad
\bar{y}=\frac{3h}{10}.}
$$

Both coordinates lean toward the tall end at $x=b$, but $\bar{y}$ remains below half height because most of the area is near the base.

## When geometric centroid and mass center separate

The weighting measure changes with the object. A slender wire uses arc length,

$$
\bar{x}=\frac{1}{L}\int_Cx\,ds,
$$

while a solid volume uses

$$
\bar{x}=\frac{1}{V}\int_Vx\,dV.
$$

With variable line, area, or volume density, insert the density into the measure: $dm=\lambda\,ds$, $dm=\rho_A\,dA$, or $dm=\rho\,dV$. A geometric centroid depends only on shape. A center of mass also depends on how material is distributed. The two coincide under uniform density, but symmetry of the boundary alone cannot locate the mass center when density breaks that symmetry.

The area centroid equals the mass center of a thin plate only when areal density is uniform. For a nonuniform lamina,

$$
m=\int_A\rho_A(x,y)\,dA,
$$

$$
\bar{x}=\frac{1}{m}\int_Ax\rho_A(x,y)\,dA,
\qquad
\bar{y}=\frac{1}{m}\int_Ay\rho_A(x,y)\,dA.
$$

Take a rectangular plate $0\le x\le L$, $0\le y\le H$ whose density increases linearly,

$$
\rho_A(x)=\rho_0\left(1+\frac{x}{L}\right).
$$

Its mass is

$$
\begin{aligned}
m
&=\int_0^L\int_0^H
\rho_0\left(1+\frac{x}{L}\right)dy\,dx \\
&=\rho_0H\left(L+\frac{L}{2}\right)
=\frac32\rho_0HL.
\end{aligned}
$$

The $x$ numerator is

$$
\begin{aligned}
\int_Ax\rho_A\,dA
&=\rho_0H\int_0^L
x\left(1+\frac{x}{L}\right)dx \\
&=\rho_0H\left(\frac{L^2}{2}+\frac{L^2}{3}\right)
=\frac56\rho_0HL^2.
\end{aligned}
$$

Thus

$$
\bar{x}
=\frac{(5/6)\rho_0HL^2}{(3/2)\rho_0HL}
=\frac{5L}{9},
\qquad
\bar{y}=\frac{H}{2}.
$$

The geometric centroid remains at $L/2$, while the mass center moves toward the denser right edge. Symmetry in the $y$ direction still fixes $\bar{y}$.

## Why the first moment returns in beam shear

The quantity $Q$ reappears in the beam shear formula

$$
\tau=\frac{VQ}{It}.
$$

Here $Q$ is the first moment of the portion of cross-sectional area above or below the level where shear stress is evaluated, taken about the neutral axis. It is not usually the first moment of the entire section: that would be zero about a centroidal axis. Confusing the selected partial area with the whole cross section is a common source of a falsely zero shear stress.

Composite calculations benefit from a table containing signed area, centroid coordinates, local centroidal moments, and axis offsets. The centroid must be found before the offsets for a composite $I$ are known. Keeping those stages separate also prevents a local centroidal formula from being shifted twice.

## Worked example: centroid of an L-shaped plate

A $120$ mm by $80$ mm rectangle has a $70$ mm by $40$ mm cutout in its upper-right corner. The removed rectangle occupies $50\le x\le120$ mm and $40\le y\le80$ mm. Take the origin at the lower-left corner of the original rectangle.

Use the full rectangle as a positive piece and the cutout as a negative piece:

| Piece | Signed area (mm$^2$) | $x_i$ (mm) | $y_i$ (mm) |
|---|---:|---:|---:|
| Full rectangle | $120(80)=9600$ | $60$ | $40$ |
| Cutout | $-70(40)=-2800$ | $85$ | $60$ |

The remaining area is

$$
A=9600-2800=6800\ \text{mm}^2.
$$

Its horizontal coordinate is

$$
\begin{aligned}
\bar{x}
&=\frac{9600(60)-2800(85)}{6800} \\
&=\frac{338000}{6800}
=49.71\ \text{mm}.
\end{aligned}
$$

Likewise,

$$
\begin{aligned}
\bar{y}
&=\frac{9600(40)-2800(60)}{6800} \\
&=\frac{216000}{6800}
=31.76\ \text{mm}.
\end{aligned}
$$

Thus

$$
\boxed{(\bar{x},\bar{y})=(49.7,31.8)\ \text{mm}.}
$$

The answer passes two geometric checks. Both coordinates move away from the removed upper-right material, and the centroid remains within the lower-left portion of the plate. Treating $x_2$ or $y_2$ as negative as well as the cutout area would move the result in the wrong direction.

## Worked example: centroidal moment of a T-section

A T-section has a web $20$ mm wide and $120$ mm high, topped by a flange $100$ mm wide and $20$ mm thick. The web is centered below the flange. Find $I_x$ about the horizontal centroidal axis, measuring $y$ upward from the bottom of the web.

First locate the composite centroid. The web and flange data are

$$
A_w=20(120)=2400\ \text{mm}^2,
\qquad y_w=60\ \text{mm},
$$

$$
A_f=100(20)=2000\ \text{mm}^2,
\qquad y_f=120+10=130\ \text{mm}.
$$

Then

$$
\begin{aligned}
\bar{y}
&=\frac{A_wy_w+A_fy_f}{A_w+A_f} \\
&=\frac{2400(60)+2000(130)}{4400} \\
&=91.818\ \text{mm}.
\end{aligned}
$$

The local centroidal moments are

$$
I_{w,c}=\frac{20(120)^3}{12}=2{,}880{,}000\ \text{mm}^4,
$$

$$
I_{f,c}=\frac{100(20)^3}{12}=66{,}666.7\ \text{mm}^4.
$$

The distances to the composite centroid are

$$
d_w=91.818-60=31.818\ \text{mm},
$$

$$
d_f=130-91.818=38.182\ \text{mm}.
$$

Apply the parallel-axis theorem to each piece:

$$
\begin{aligned}
I_x
&=I_{w,c}+A_wd_w^2+I_{f,c}+A_fd_f^2 \\
&=2{,}880{,}000+2400(31.818)^2 \\
&\quad+66{,}666.7+2000(38.182)^2 \\
&\approx8.292\times10^6\ \text{mm}^4.
\end{aligned}
$$

Therefore

$$
\boxed{\bar{y}=91.82\ \text{mm},\qquad I_x\approx8.29\times10^6\ \text{mm}^4.}
$$

The flange's own centroidal $I_x$ is small because its vertical thickness is only $20$ mm. Its parallel-axis term is large because most of its area sits far from the section centroid. That separation is the main purpose of the flange.

## Rotated axes and principal directions

The parallel-axis theorem cannot rotate an axis. Under a counterclockwise axis rotation by $\theta$, the area moments transform as

$$
I_{x'}=\frac{I_x+I_y}{2}
+\frac{I_x-I_y}{2}\cos 2\theta
-I_{xy}\sin 2\theta,
$$

$$
I_{x'y'}=\frac{I_x-I_y}{2}\sin 2\theta+I_{xy}\cos 2\theta.
$$

Principal axes are orientations for which $I_{x'y'}=0$. About those axes the second moments take their maximum and minimum values. Symmetry axes through the centroid are principal axes, which is why standard beam sections are normally analyzed in their symmetry directions. For unsymmetric sections such as unequal angles, the principal directions need not align with the drawing axes.

The polar moment about a fixed point is invariant under rotation of the Cartesian axes through that point:

$$
I_{x'}+I_{y'}=I_x+I_y=J_O.
$$

Rotation redistributes the total between the two perpendicular axes but cannot change their sum. This provides a quick check on transformed moments. The principal values are

$$
I_{1,2}
=\frac{I_x+I_y}{2}
\pm\sqrt{
\left(\frac{I_x-I_y}{2}\right)^2+I_{xy}^2
}.
$$

Their sum equals $J_O$, and neither can be negative because each represents an integral of squared distance. A negative transformed second moment indicates a sign or formula error, while a negative product of inertia may be perfectly valid.

For composite sections, products of inertia also require a parallel-axis term:

$$
I_{xy}=I_{xy,c}+A d_xd_y.
$$

Unlike $Ad^2$, the product $Ad_xd_y$ carries a sign determined by the centroid's quadrant relative to the new axes. Holes again use negative area. Keeping a small coordinate sketch beside the table is especially helpful here because distances in opposite directions can cancel.

## Checks that catch most errors

- A composite centroid should move toward added material and away from a hole. It may fall outside a concave shape, so “inside the material” is not a universal check.
- The distance in $Ad^2$ is perpendicular to the two parallel axes. A horizontal shift does not change the moment about a horizontal axis.
- A centroidal rectangle formula cannot be used directly about an edge. For a base axis, $I_x=bh^3/3$, obtained from $bh^3/12+A(h/2)^2$.
- Keep full precision for $\bar{x}$ and $\bar{y}$ until all parallel-axis terms are evaluated. Squaring an early rounded distance can noticeably alter a built-up section result.
- Area moments must have fourth-power length units. A result in mm$^2$ or mm$^3$ signals that either the integral or the units were mishandled.
- $J=I_x+I_y$ holds for perpendicular area axes through the same point. It does not state that every section's torsional stiffness equals $GJ/L$.

<div className="see-also">

See also: [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium) · [Internal forces in beams](/physics/mechanics/internal-forces-beams) · [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)

</div>
