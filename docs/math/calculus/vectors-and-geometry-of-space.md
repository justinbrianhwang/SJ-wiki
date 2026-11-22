---
title: Vectors and Geometry of Space
sidebar_position: 16
---

# Vectors and Geometry of Space

Vectors describe magnitude and direction. In space, they provide the language for lines, planes, distances, projections, angles, areas, and volumes. Calculus in several variables depends on this geometry because gradients, vector fields, tangent planes, and surface integrals all use vector operations.

The main shift from two-dimensional coordinate geometry is that equations are often not unique. A line in space needs a point and a direction vector. A plane needs a point and a normal vector. Vector notation keeps those relationships organized.

## Definitions

A vector in $\mathbb{R}^3$ is

$$
\mathbf{v}=\langle v_1,v_2,v_3\rangle.
$$

Its magnitude is

$$
|\mathbf{v}|=\sqrt{v_1^2+v_2^2+v_3^2}.
$$

The dot product is

$$
\mathbf{u}\cdot\mathbf{v}=u_1v_1+u_2v_2+u_3v_3.
$$

It also satisfies

$$
\mathbf{u}\cdot\mathbf{v}=|\mathbf{u}||\mathbf{v}|\cos\theta.
$$

The cross product is

$$
\mathbf{u}\times\mathbf{v}
=
\langle u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1\rangle.
$$

It is perpendicular to both $\mathbf{u}$ and $\mathbf{v}$, and its magnitude is

$$
|\mathbf{u}\times\mathbf{v}|=|\mathbf{u}||\mathbf{v}|\sin\theta.
$$

A line through point $\mathbf{r}_0$ with direction $\mathbf{v}$ is

$$
\mathbf{r}(t)=\mathbf{r}_0+t\mathbf{v}.
$$

A plane through point $\mathbf{r}_0$ with normal vector $\mathbf{n}$ is

$$
\mathbf{n}\cdot(\mathbf{r}-\mathbf{r}_0)=0.
$$

## Key results

The angle between nonzero vectors is determined by

$$
\cos\theta=\frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{u}||\mathbf{v}|}.
$$

Vectors are orthogonal exactly when their dot product is zero.

The projection of $\mathbf{u}$ onto $\mathbf{v}$ is

$$
\operatorname{proj}_{\mathbf{v}}\mathbf{u}
=
\frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{v}|^2}\mathbf{v}.
$$

The scalar component of $\mathbf{u}$ in the direction of $\mathbf{v}$ is

$$
\operatorname{comp}_{\mathbf{v}}\mathbf{u}
=
\frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{v}|}.
$$

The area of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$ is

$$
|\mathbf{u}\times\mathbf{v}|.
$$

The volume of the parallelepiped spanned by $\mathbf{u}$, $\mathbf{v}$, and $\mathbf{w}$ is

$$
|\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})|.
$$

The distance from point $\mathbf{p}$ to the plane

$$
ax+by+cz=d
$$

is

$$
\frac{|a p_1+b p_2+c p_3-d|}{\sqrt{a^2+b^2+c^2}}.
$$

This formula is projection of the point-plane displacement onto the unit normal.

Quadric surfaces extend conics into space. Ellipsoids, paraboloids, hyperboloids, cones, and cylinders are recognized by squared variables and signs. Cross-sections, traces, and symmetry help identify their shapes.

The dot product detects how much one vector points in another vector's direction. If $\mathbf{u}\cdot\mathbf{v}\gt 0$, the angle is acute. If it is negative, the angle is obtuse. If it is zero, the vectors are perpendicular. This sign information is often enough for geometry problems before calculating the actual angle.

The cross product encodes orientation as well as area. Its direction is determined by the right-hand rule. Reversing the order reverses the direction:

$$
\mathbf{v}\times\mathbf{u}=-(\mathbf{u}\times\mathbf{v}).
$$

This matters in torque, normal vectors, and surface orientation in vector calculus.

Lines in space may intersect, be parallel, or be skew. Skew lines are nonparallel lines that do not intersect; this cannot happen in the plane but is common in three dimensions. To test intersection, set the parametric coordinates equal and solve for the parameters. If no common parameters exist and direction vectors are not parallel, the lines are skew.

Planes can be parallel, identical, or intersect in a line. Two planes with normals $\mathbf{n}_1$ and $\mathbf{n}_2$ are parallel when the normals are scalar multiples. If the normals are not parallel, the direction of their line of intersection is

$$
\mathbf{n}_1\times\mathbf{n}_2.
$$

Distance formulas are projection formulas. The distance from a point to a line can be written

$$
\frac{|(\mathbf{p}-\mathbf{r}_0)\times\mathbf{v}|}{|\mathbf{v}|},
$$

where $\mathbf{r}_0$ is a point on the line and $\mathbf{v}$ is a direction vector. The numerator is the area of a parallelogram; dividing by the base length gives the height, which is the perpendicular distance.

Coordinate surfaces provide quick orientation. Equations such as $x=c$, $y=c$, and $z=c$ are planes parallel to coordinate planes. Equations such as $x^2+y^2=R^2$ describe circular cylinders around the $z$-axis because $z$ is unrestricted. Recognizing unrestricted variables helps identify cylinders and extruded surfaces.

Vector equations are often easier to translate after identifying what must be parallel or perpendicular. A line's direction vector is parallel to the line. A plane's normal vector is perpendicular to every direction lying in the plane. If two nonparallel vectors lie in a plane, their cross product gives a normal vector for the plane.

The scalar triple product has a sign as well as a magnitude. The sign indicates orientation of the ordered triple $(\mathbf{u},\mathbf{v},\mathbf{w})$. If the scalar triple product is zero, the three vectors are coplanar, so the parallelepiped volume is zero. This provides a compact test for whether four points lie in the same plane: form three displacement vectors from one point and compute the scalar triple product.

Projections split a vector into parallel and perpendicular parts:

$$
\mathbf{u}=\operatorname{proj}_{\mathbf{v}}\mathbf{u}
\ +\left(\mathbf{u}-\operatorname{proj}_{\mathbf{v}}\mathbf{u}\right).
$$

The first part lies along $\mathbf{v}$, and the second part is orthogonal to $\mathbf{v}$. This decomposition is the geometric heart of least squares, work as force along displacement, and distance formulas.

Spheres have equation

$$
(x-h)^2+(y-k)^2+(z-\ell)^2=R^2.
$$

The center is $(h,k,\ell)$ and radius is $R$. Completing squares in three variables reveals this form, just as in two-dimensional circles.

Coordinate choices can simplify computations. If a problem involves a plane with normal $\mathbf{n}$, using components parallel and perpendicular to $\mathbf{n}$ often reduces the geometry to one projection. If a problem involves a line, decomposing a vector into parts parallel and perpendicular to the line usually reveals distances and closest points.

The algebra should always match the dimension. Two equations usually describe a curve in space, often the intersection of two surfaces. One equation usually describes a surface. Three independent equations usually identify isolated points. This differs from the plane, where one equation usually describes a curve.

## Visual

| Operation | Formula | Geometric meaning |
|---|---:|---|
| Magnitude | $\vert \mathbf{v}\vert $ | length |
| Dot product | $\mathbf{u}\cdot\mathbf{v}$ | angle and projection |
| Cross product | $\mathbf{u}\times\mathbf{v}$ | perpendicular vector and area |
| Scalar triple product | $\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})$ | signed volume |
| Line | $\mathbf{r}_0+t\mathbf{v}$ | point plus direction |
| Plane | $\mathbf{n}\cdot(\mathbf{r}-\mathbf{r}_0)=0$ | point plus normal |

```text
           n
           ^
           |     plane: n dot (r-r0)=0
           |
     ------*----------------
          r0

line: r(t)=r0+t v moves from r0 in direction v
```

## Worked example 1: equation of a plane

**Problem.** Find the plane through $P=(1,2,0)$ with normal vector

$$
\mathbf{n}=\langle 3,-1,4\rangle.
$$

Then decide whether $Q=(2,1,1)$ lies on the plane.

**Method.**

1. Use the point-normal form:

$$
\mathbf{n}\cdot(\mathbf{r}-\mathbf{r}_0)=0.
$$

2. Let $\mathbf{r}=\langle x,y,z\rangle$ and $\mathbf{r}_0=\langle1,2,0\rangle$:

$$
\langle3,-1,4\rangle\cdot\langle x-1,y-2,z-0\rangle=0.
$$

3. Compute the dot product:

$$
3(x-1)-1(y-2)+4z=0.
$$

4. Expand:

$$
3x-3-y+2+4z=0.
$$

5. Simplify:

$$
3x-y+4z-1=0.
$$

6. Test $Q=(2,1,1)$:

$$
3(2)-1+4(1)-1=8.
$$

**Checked answer.** The plane is $3x-y+4z-1=0$. Since substituting $Q$ gives $8\ne 0$, the point $Q$ is not on the plane.

## Worked example 2: projection and distance to a plane

**Problem.** Find the distance from $P=(2,0,3)$ to the plane

$$
2x-y+2z=5.
$$

**Method.**

1. Identify

$$
a=2,\qquad b=-1,\qquad c=2,\qquad d=5.
$$

2. Substitute the point into the numerator:

$$
|2(2)-0+2(3)-5|=|4+6-5|=5.
$$

3. Compute the normal magnitude:

$$
\sqrt{2^2+(-1)^2+2^2}=\sqrt{4+1+4}=3.
$$

4. Divide:

$$
\text{distance}=\frac{5}{3}.
$$

**Checked answer.** The point is $5/3$ units from the plane. The formula uses perpendicular distance because the shortest path to a plane is along its normal vector.

This distance is positive by definition. The signed numerator

$$
2(2)-0+2(3)-5=5
$$

also tells which side of the oriented plane the point lies on if the normal $\langle2,-1,2\rangle$ is chosen as positive. Signed distance is useful in geometry and numerical methods, but ordinary distance uses absolute value.

As another check, the denominator $3$ is the length of the normal vector, not the length of a point coordinate. Forgetting this division would measure displacement along a non-unit normal and overstate the actual perpendicular distance.

The closest point on the plane can be found by moving from $P$ in the normal direction by the signed distance measured in normal units. That construction is a projection problem, which is why the same dot product appears in both projection and distance formulas.

Because normals can be scaled without changing the plane, formulas must either use ratios or divide by the normal length. The plane $2x-y+2z=5$ has the same points as $4x-2y+4z=10$, and the distance formula gives the same answer only because numerator and denominator scale together.

## Code

```python
from math import sqrt

def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

def cross(u, v):
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    )

def norm(v):
    return sqrt(dot(v, v))

print(dot((3, -1, 4), (1, -1, 1)))
print(cross((1, 0, 0), (0, 1, 0)))
print(norm((2, -1, 2)))
```

## Common pitfalls

- Confusing a direction vector for a line with a normal vector for a plane.
- Forgetting that the cross product is defined only in three dimensions in this elementary form.
- Reversing cross product order. $\mathbf{u}\times\mathbf{v}=-(\mathbf{v}\times\mathbf{u})$.
- Using a non-unit normal in a distance formula without dividing by its magnitude.
- Treating skew lines in space as if they must intersect.
- Misclassifying quadric surfaces without checking traces in coordinate planes.

## Connections

- [Parametric Polar and Conic Curves](/math/calculus/parametric-polar-conics): space curves extend parametric ideas.
- [Vector Functions and Motion](/math/calculus/vector-functions-and-motion): derivatives of vector-valued functions describe motion.
- [Partial Derivatives and the Gradient](/math/calculus/partial-derivatives-and-gradient): gradients are normal vectors to level surfaces.
- [Vector Calculus](/math/calculus/vector-calculus): dot and cross products support line, surface, flux, and circulation integrals.
