---
title: Vectors and Geometry of Space
sidebar_position: 16
---

# Vectors and Geometry of Space

Three-dimensional analytic geometry becomes manageable once points and directions are kept separate. A point marks a location; a vector records displacement. Lines are built from a point and a direction, while planes are built from a point and a normal. Dot products extract parallel components, cross products produce perpendicular directions, and the triple product measures oriented volume.

## Displacement, length, and direction

For points $P=(p_1,p_2,p_3)$ and $Q=(q_1,q_2,q_3)$, the displacement from $P$ to $Q$ is

$$
\overrightarrow{PQ}
=\langle q_1-p_1,q_2-p_2,q_3-p_3\rangle.
$$

A vector $\mathbf v=\langle v_1,v_2,v_3\rangle$ has Euclidean norm

$$
\lVert\mathbf v\rVert
=\sqrt{v_1^2+v_2^2+v_3^2}.
$$

The distance between $P$ and $Q$ is $\lVert\overrightarrow{PQ}\rVert$. Any nonzero vector can be normalized to a unit vector

$$
\widehat{\mathbf v}=\frac{\mathbf v}{\lVert\mathbf v\rVert}.
$$

Normalization fails for the zero vector because it has no direction. That small restriction recurs in angle, projection, and distance formulas whenever a denominator contains a vector norm.

Vectors are free vectors in elementary calculus: translating an arrow without changing its components does not change the vector. Points are not interchangeable in that way. Expressions such as $Q-P$ and $P+\mathbf v$ make geometric sense; adding two points does not have the same coordinate-independent meaning.

## The dot product measures alignment

The dot product is

$$
\mathbf u\cdot\mathbf v
=u_1v_1+u_2v_2+u_3v_3.
$$

It is connected to angle by

$$
\mathbf u\cdot\mathbf v
=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta,
$$

where $0\le\theta\le\pi$ is the smaller angle between nonzero vectors. One derivation compares two expressions for the squared length of $\mathbf u-\mathbf v$. Coordinate algebra gives

$$
\lVert\mathbf u-\mathbf v\rVert^2
=\lVert\mathbf u\rVert^2+\lVert\mathbf v\rVert^2
-2\mathbf u\cdot\mathbf v.
$$

The law of cosines applied to the triangle formed by $\mathbf u$ and $\mathbf v$ gives the same left side as

$$
\lVert\mathbf u\rVert^2+\lVert\mathbf v\rVert^2
-2\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta.
$$

Equating the two proves the angle identity. It immediately gives

$$
\cos\theta
=\frac{\mathbf u\cdot\mathbf v}
{\lVert\mathbf u\rVert\lVert\mathbf v\rVert}.
$$

A positive dot product indicates an acute angle, a negative one an obtuse angle, and zero means orthogonality. Floating-point calculations may produce a cosine slightly outside $[-1,1]$ through rounding, so numerical code commonly clamps the ratio before applying inverse cosine.

The scalar component of $\mathbf u$ along $\mathbf v$ is

$$
\operatorname{comp}_{\mathbf v}\mathbf u
=\frac{\mathbf u\cdot\mathbf v}{\lVert\mathbf v\rVert},
$$

and the vector projection is

$$
\operatorname{proj}_{\mathbf v}\mathbf u
=\frac{\mathbf u\cdot\mathbf v}{\lVert\mathbf v\rVert^2}\mathbf v.
$$

The remainder is perpendicular to $\mathbf v$:

$$
\mathbf u
=\operatorname{proj}_{\mathbf v}\mathbf u
+\left(\mathbf u-\operatorname{proj}_{\mathbf v}\mathbf u\right).
$$

Checking the dot product of the parenthesized remainder with $\mathbf v$ gives zero. This parallel/perpendicular split is the common mechanism behind closest points, least squares, and work done by a force.

## The cross product produces an oriented normal

For vectors in $\mathbb R^3$,

$$
\mathbf u\times\mathbf v
=\left\langle
u_2v_3-u_3v_2,
u_3v_1-u_1v_3,
u_1v_2-u_2v_1
\right\rangle.
$$

Taking its dot product with either input gives zero after cancellation, so it is perpendicular to both. Its magnitude is

$$
\lVert\mathbf u\times\mathbf v\rVert
=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\sin\theta.
$$

This is the area of the parallelogram spanned by the two vectors: base times perpendicular height. Half the magnitude gives the area of the corresponding triangle. Parallel inputs give the zero vector, which cannot serve as a normal.

Direction follows the right-hand rule. Reversing the inputs reverses orientation:

$$
\mathbf v\times\mathbf u=-(\mathbf u\times\mathbf v).
$$

Unlike the dot product, the cross product is not commutative and should not be manipulated as though it were ordinary scalar multiplication.

The scalar triple product

$$
\mathbf u\cdot(\mathbf v\times\mathbf w)
$$

is the signed volume of the parallelepiped determined by the ordered vectors. Its absolute value is ordinary volume; its sign records orientation. A zero triple product means the three vectors are coplanar. To test whether four points are coplanar, choose one as a base point and use the three displacement vectors to the others.

## Lines: one point and one direction

A line through $P_0$ with nonzero direction $\mathbf v$ has vector equation

$$
\mathbf r(t)=\mathbf r_0+t\mathbf v.
$$

In coordinates, if $\mathbf r_0=\langle x_0,y_0,z_0\rangle$ and $\mathbf v=\langle a,b,c\rangle$, then

$$
x=x_0+at,
\qquad y=y_0+bt,
\qquad z=z_0+ct.
$$

Different choices of base point and nonzero scalar multiples of the direction describe the same line. Symmetric equations such as

$$
\frac{x-x_0}{a}=\frac{y-y_0}{b}=\frac{z-z_0}{c}
$$

are valid only when all displayed direction components are nonzero. If $b=0$, the safe coordinate statement is $y=y_0$, not division by zero.

Two lines in space can intersect, be parallel, or be skew. Nonparallel lines need not intersect because they may lie in different planes. To test intersection, give the lines different parameters, equate all three coordinates, and look for one pair of parameter values satisfying every equation. Using the same parameter for both lines silently imposes an extra condition.

The distance from a point $P$ to a line through $P_0$ in direction $\mathbf v$ is

$$
d=\frac{\lVert\overrightarrow{P_0P}\times\mathbf v\rVert}
{\lVert\mathbf v\rVert}.
$$

The numerator is the area of a parallelogram with base $\lVert\mathbf v\rVert$ and height $d$. Dividing area by base recovers the perpendicular height.

## Planes: one point and one normal

A plane through $P_0$ with nonzero normal $\mathbf n$ consists of all points $P$ for which $\overrightarrow{P_0P}$ is perpendicular to $\mathbf n$:

$$
\mathbf n\cdot(\mathbf r-\mathbf r_0)=0.
$$

Writing $\mathbf n=\langle a,b,c\rangle$ produces

$$
a(x-x_0)+b(y-y_0)+c(z-z_0)=0,
$$

or $ax+by+cz=d$. Scaling the entire equation by a nonzero constant does not change the plane.

Two nonparallel direction vectors $\mathbf u$ and $\mathbf v$ lying in a plane determine a normal $\mathbf u\times\mathbf v$. If they are parallel, they do not determine a unique plane. Two planes are parallel exactly when their normals are scalar multiples. Otherwise their intersection is a line whose direction is parallel to $\mathbf n_1\times\mathbf n_2$.

The signed distance from $P=(p_1,p_2,p_3)$ to $ax+by+cz=d$ is

$$
\delta=\frac{ap_1+bp_2+cp_3-d}{\sqrt{a^2+b^2+c^2}}.
$$

Ordinary distance is $\vert \delta\vert $. To derive it, take any point $P_0$ in the plane and project $\overrightarrow{P_0P}$ onto the unit normal $\mathbf n/\lVert\mathbf n\rVert$. The numerator is the plane equation evaluated at $P$, and the denominator corrects for a normal that is not unit length.

The closest point on the plane follows by subtracting the signed normal displacement:

$$
P_{\mathrm{closest}}
=P-\delta\frac{\mathbf n}{\lVert\mathbf n\rVert}.
$$

## Worked example: a plane through three points

Find the plane through

$$
A=(1,0,2),\qquad B=(3,1,1),\qquad C=(0,2,4),
$$

then find the distance from $Q=(2,2,5)$ to that plane.

First form two directions in the plane:

$$
\overrightarrow{AB}=\langle2,1,-1\rangle,
\qquad
\overrightarrow{AC}=\langle-1,2,2\rangle.
$$

Their cross product is

$$
\begin{aligned}
\overrightarrow{AB}\times\overrightarrow{AC}
&=\langle
1(2)-(-1)(2),
(-1)(-1)-2(2),
2(2)-1(-1)
\rangle\\
&=\langle4,-3,5\rangle.
\end{aligned}
$$

This nonzero result also confirms that the three points are not collinear. Using point $A$ and normal $\mathbf n=\langle4,-3,5\rangle$,

$$
4(x-1)-3(y-0)+5(z-2)=0.
$$

After expansion,

$$
4x-3y+5z=14.
$$

Substituting $B$ gives $12-3+5=14$, and substituting $C$ gives $0-6+20=14$, so both checks pass.

For $Q$, the numerator of the distance formula is

$$
|4(2)-3(2)+5(5)-14|=|13|=13.
$$

The normal length is

$$
\sqrt{4^2+(-3)^2+5^2}=\sqrt{50}=5\sqrt2.
$$

Therefore

$$
d=\frac{13}{5\sqrt2}=\frac{13\sqrt2}{10}.
$$

## Worked example: deciding whether two lines are skew

Consider

$$
L_1:\ \mathbf r=\langle1,0,1\rangle
+s\langle1,2,-1\rangle
$$

and

$$
L_2:\ \mathbf r=\langle0,1,2\rangle
+t\langle2,1,1\rangle.
$$

The direction vectors are not scalar multiples, so the lines are not parallel. An intersection would require

$$
\begin{aligned}
1+s&=2t,\\
2s&=1+t,\\
1-s&=2+t.
\end{aligned}
$$

From the first equation, $s=2t-1$. Substitute this into the second:

$$
2(2t-1)=1+t
\quad\Longrightarrow\quad
3t=3
\quad\Longrightarrow\quad
t=1.
$$

Then $s=1$. The third equation would demand

$$
1-1=2+1,
$$

or $0=3$, which is impossible. The first two coordinates can agree at a projected crossing, but the third does not. Since the lines are neither parallel nor intersecting, they are skew.

Their separation can be found with a triple product. Let $\mathbf d_1$ and $\mathbf d_2$ be the two directions and let $\mathbf w=\langle0,1,2\rangle-\langle1,0,1\rangle=\langle-1,1,1\rangle$. A normal to both directions is

$$
\mathbf d_1\times\mathbf d_2
=\langle3,-3,-3\rangle.
$$

Thus the distance between the skew lines is

$$
\frac{|\mathbf w\cdot(\mathbf d_1\times\mathbf d_2)|}
{\lVert\mathbf d_1\times\mathbf d_2\rVert}
=\frac{|-3-3-3|}{\sqrt{27}}
=\sqrt3.
$$

## Reading equations of surfaces

One scalar equation in three variables usually describes a surface. Two independent equations usually intersect in a curve, and three independent equations usually leave isolated points. Degeneracies and dependent equations are the exceptions.

A sphere has equation

$$
(x-h)^2+(y-k)^2+(z-\ell)^2=R^2.
$$

Completing squares reveals its center and radius. If a variable is absent, the surface often extends freely in that direction: $x^2+y^2=R^2$ is a circular cylinder parallel to the $z$-axis.

Quadric surfaces are classified by signs, coefficients, and planar traces:

| Standard pattern | Surface | Useful trace |
|---|---|---|
| $x^2/a^2+y^2/b^2+z^2/c^2=1$ | ellipsoid | ellipses in coordinate planes |
| $z=x^2/a^2+y^2/b^2$ | elliptic paraboloid | horizontal ellipses, vertical parabolas |
| $z=x^2/a^2-y^2/b^2$ | hyperbolic paraboloid | opposite-opening parabolas |
| $x^2/a^2+y^2/b^2-z^2/c^2=1$ | one-sheet hyperboloid | horizontal ellipses |
| $z^2/c^2-x^2/a^2-y^2/b^2=1$ | two-sheet hyperboloid | no points near $z=0$ |
| $x^2/a^2+y^2/b^2-z^2/c^2=0$ | elliptic cone | lines through the origin in vertical traces |

Before naming a surface, inspect several traces and note which variables are unrestricted. A memorized silhouette is less reliable when axes are permuted, centers are translated, or coefficients stretch the shape.

## Checks that catch geometric mix-ups

- A line needs a direction parallel to it; a plane equation needs a vector perpendicular to it. Swapping those roles gives plausible-looking but wrong equations.
- Cross-product order controls orientation. Areas and distances use its magnitude, but oriented normals and flux retain its sign.
- Distance formulas divide by the norm of a direction or normal. Without that division, rescaling the same line or plane would change the alleged distance.
- Symmetric line equations cannot divide by a zero direction component. Parametric equations handle every direction without a special case.
- Solving only two coordinate equations does not prove two space lines intersect. The remaining coordinate is an independent consistency check.
- An angle formula assumes both vectors are nonzero. Orthogonality with the zero vector is algebraically true, but the angle with it is undefined.

## Choosing a representation that matches the question

Vector, parametric, and scalar equations describe the same geometric objects from different angles. A parametric line is best for generating points, testing an intersection, or describing motion. Two scalar plane equations can describe a line as their intersection, which is sometimes better for constraints. A plane's scalar equation makes side tests and distances immediate, while a two-parameter vector equation displays the directions lying inside it.

Converting between forms should be driven by the next operation. To intersect a line with a plane, substitute the line parametrization into the plane equation and solve one scalar equation for the line parameter. To intersect two planes, take the cross product of their normals for a direction and solve the two plane equations for one point. To measure distance, move to a normal or projection description. Reaching for coordinates before identifying the relevant parallel or perpendicular relation usually creates more equations than needed.

Representations are nonunique. A direction vector can be multiplied by any nonzero scalar, a plane equation can be scaled, and the base point of a line can be replaced by any other point on it. Verification should compare the represented sets rather than the literal coefficients. Parallel normals plus one shared point identify the same plane; parallel line directions plus one shared point identify the same line.

Degenerate input requires a pause. Two identical points do not determine a line direction. Three collinear points do not determine a unique plane. Two parallel direction vectors have zero cross product and therefore cannot supply a plane normal. The zero result is information about the geometry, not an invitation to pick an arbitrary normal and continue.

## Closest points as orthogonal decompositions

Every elementary distance problem here is a closest-point problem. The displacement from the closest point on a line to the external point must be perpendicular to the line direction. The displacement from the closest point on a plane must be parallel to its normal. These conditions produce linear equations and also prove minimality through the Pythagorean theorem.

For a line, write a candidate point using its parameter and minimize the squared distance. Differentiating that quadratic gives the same orthogonality equation as projection. Squared distance is preferred because it has the same minimizer as distance but avoids a square root. In higher-dimensional linear algebra, this becomes least squares: the residual is perpendicular to every column direction.

The distance between skew lines follows the same logic. Their common perpendicular must be perpendicular to both direction vectors, so it lies along their cross product. Projecting the displacement between any chosen base points onto the unit common-normal direction gives the separation. Changing either base point by a line-direction multiple does not alter that projection, because those added parts are perpendicular to the common normal.

Signed distances retain side information. Once a unit normal orientation is chosen, points on one side of a plane have positive signed distance and points on the other have negative signed distance. Reversing the normal reverses every sign but leaves ordinary distances unchanged. Signed distance functions are useful for clipping, collision tests, and determining whether points lie in the same half-space.

## Orientation and coordinate handedness

The right-hand rule assumes a right-handed coordinate system. In such a system, the first standard basis vector crossed with the second gives the third. Swapping two axes changes handedness and reverses orientation-sensitive signs. Dot products and lengths are unaffected, but cross products, oriented surface normals, and signed volumes change sign.

The scalar triple product detects orientation consistently. A positive value says the ordered third vector lies on the positive side of the oriented plane formed by the first two; a negative value says the opposite. Cyclic permutations preserve the value, while exchanging any pair reverses it. Remembering these permutation rules is safer than repeatedly expanding a determinant.

Normal direction is often a convention chosen by the problem. A closed surface uses outward normals. A graph can use an upward-pointing normal. A plane by itself has two equally valid unit normals. Calculations of unsigned area or distance erase this choice with an absolute value, whereas flux and torque keep it. Applying an absolute value too early can destroy physical direction information.

## Traces before sketches

For an unfamiliar surface, first set one coordinate equal to several constants. These traces reduce the equation to familiar plane curves. Then check intercepts, symmetries under sign changes, and which variables can grow without bound. A single perspective sketch can hide disconnected sheets or a narrow saddle direction; traces expose them algebraically.

Translations and unequal coefficients do not change the basic quadric type. Completing squares finds the center or vertex, and dividing by a positive constant produces a recognizable standard form. A negative right side may signal no real points, or it may be moved across the equation to reveal a hyperboloid with a different axis. Classification should occur only after these normalizations.

Equations with cross terms require rotation of coordinates to align principal axes. In matrix language, a symmetric quadratic-form matrix is orthogonally diagonalized. Its eigenvectors give the new axes and its eigenvalues give the signed squared coefficients. The familiar axis-aligned table is therefore the special case in which the coordinate basis already follows the principal directions.

<div className="see-also">

See also: [Parametric, polar, and conic curves](/math/calculus/parametric-polar-conics) · [Vector functions and motion](/math/calculus/vector-functions-and-motion) · [Partial derivatives and the gradient](/math/calculus/partial-derivatives-and-gradient) · [Vector calculus](/math/calculus/vector-calculus)

</div>
