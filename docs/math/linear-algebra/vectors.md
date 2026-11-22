---
title: Vectors in Rn
sidebar_position: 7
---

# Vectors in Rn

Vectors in $\mathbb{R}^n$ are ordered lists of real numbers used to encode displacements, data, forces, coefficients, states, and solutions. Linear algebra begins with two operations: adding vectors and scaling them.

The pictures come most easily from $\mathbb{R}^2$ and $\mathbb{R}^3$, where arrows add tip-to-tail and scalars stretch or reverse them. The same arithmetic applies to matrix columns, feature vectors, and state vectors in models.

## Coordinates, addition, and scaling

A vector in $\mathbb{R}^n$ is a column

$$
\mathbf{v}=
\begin{bmatrix}
v_1\\
v_2\\
\vdots\\
v_n
\end{bmatrix}.
$$

Addition and scalar multiplication are componentwise:

$$
\mathbf{u}+\mathbf{v}=
\begin{bmatrix}
u_1+v_1\\
\vdots\\
u_n+v_n
\end{bmatrix},
\qquad
c\mathbf{v}=
\begin{bmatrix}
cv_1\\
\vdots\\
cv_n
\end{bmatrix}.
$$

These operations satisfy the familiar algebraic laws: vector addition is commutative and associative, the zero vector is an additive identity, every vector has an additive inverse, and scalar multiplication distributes over vector addition and respects multiplication of scalars.

The standard basis is $\mathbf{e}_1,\ldots,\mathbf{e}_n$, with a $1$ in one position and zeros elsewhere. Every vector has the unique expansion

$$
\mathbf{v}=v_1\mathbf{e}_1+\cdots+v_n\mathbf{e}_n.
$$

The $i$th component on the right is $v_i$, which proves equality; componentwise equality also proves uniqueness.

The dot product and Euclidean norm are

$$
\mathbf{u}\cdot\mathbf{v}=u_1v_1+\cdots+u_nv_n,
\qquad
\|\mathbf{v}\|=\sqrt{\mathbf{v}\cdot\mathbf{v}}.
$$

The entries are coordinates, not inherently physical directions. A vector may represent an arrow from the origin, a displacement that can be translated anywhere, or a data record whose components have no spatial interpretation. The algebra is identical; the interpretation determines whether adding or comparing components is meaningful.

A nonzero vector can be separated into magnitude and direction:

$$
\mathbf{v}=\|\mathbf{v}\|\widehat{\mathbf{v}},
\qquad
\widehat{\mathbf{v}}=\frac{\mathbf{v}}{\|\mathbf{v}\|}.
$$

The unit vector $\widehat{\mathbf{v}}$ has norm one. Normalization is undefined for $\mathbf{v}=\mathbf{0}$ because the zero vector has no direction.

## Length, angle, and projection

The dot product connects coordinates to Euclidean geometry. The Cauchy--Schwarz inequality states

$$
|\mathbf{u}\cdot\mathbf{v}|
\le \|\mathbf{u}\|\,\|\mathbf{v}\|.
$$

One proof considers the nonnegative quadratic

$$
0\le\|\mathbf{u}-t\mathbf{v}\|^2
=\|\mathbf{u}\|^2-2t(\mathbf{u}\cdot\mathbf{v})+t^2\|\mathbf{v}\|^2.
$$

Choose $t=(\mathbf{u}\cdot\mathbf{v})/\|\mathbf{v}\|^2$ for $\mathbf{v}\ne\mathbf{0}$. Substitution gives

$$
0\le \|\mathbf{u}\|^2
-\frac{(\mathbf{u}\cdot\mathbf{v})^2}{\|\mathbf{v}\|^2},
$$

which rearranges to the squared inequality. Equality occurs exactly when one vector is a scalar multiple of the other.

Because the quotient lies in $[-1,1]$, the angle between nonzero vectors can be defined by

$$
\cos\theta
=\frac{\mathbf{u}\cdot\mathbf{v}}
{\|\mathbf{u}\|\,\|\mathbf{v}\|}.
$$

A zero dot product means perpendicular directions. A positive dot product gives an acute angle, and a negative one gives an obtuse angle.

The component of $\mathbf{u}$ along a nonzero $\mathbf{v}$ is the orthogonal projection

$$
\operatorname{proj}_{\mathbf{v}}\mathbf{u}
=\frac{\mathbf{u}\cdot\mathbf{v}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}.
$$

The remainder $\mathbf{u}-\operatorname{proj}_{\mathbf{v}}\mathbf{u}$ is perpendicular to $\mathbf{v}$. To check it, take its dot product with $\mathbf{v}$ and observe that the two terms cancel.

For

$$
\mathbf{u}=\begin{bmatrix}3\\4\end{bmatrix},
\qquad
\mathbf{v}=\begin{bmatrix}2\\1\end{bmatrix},
$$

the coefficient is

$$
\frac{\mathbf{u}\cdot\mathbf{v}}{\mathbf{v}\cdot\mathbf{v}}
=\frac{3(2)+4(1)}{2^2+1^2}
=\frac{10}{5}=2.
$$

Hence

$$
\operatorname{proj}_{\mathbf{v}}\mathbf{u}
=2\begin{bmatrix}2\\1\end{bmatrix}
=\begin{bmatrix}4\\2\end{bmatrix},
$$

and the perpendicular remainder is

$$
\begin{bmatrix}3\\4\end{bmatrix}
-\begin{bmatrix}4\\2\end{bmatrix}
=\begin{bmatrix}-1\\2\end{bmatrix}.
$$

Indeed, $(-1,2)\cdot(2,1)=0$. The Pythagorean identity checks the decomposition:

$$
\|\mathbf{u}\|^2=25
=\left\|\begin{bmatrix}4\\2\end{bmatrix}\right\|^2
+\left\|\begin{bmatrix}-1\\2\end{bmatrix}\right\|^2
=20+5.
$$

## Span: which vectors can be built?

A linear combination of $\mathbf{v}_1,\ldots,\mathbf{v}_k$ is

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k.
$$

Their span is the set of all such combinations. One nonzero vector spans a line through the origin. Two nonparallel vectors span $\mathbb{R}^2$; in $\mathbb{R}^3$, two vectors span at most a plane.

```text
one nonzero vector                  two nonparallel vectors

        ^                                   ^
        | span{v}                           |       / u+v
        |                                   |      /
--------+--------->                 --------+-----/------>
       / v                                  |    /
      /                                     |   / v
                                            |  /
                                      u ----+ /

line through origin                  whole plane by combinations su + tv
```

| Concept | Algebraic test | Geometric meaning |
|---|---|---|
| Scalar multiple | $\mathbf{u}=c\mathbf{v}$ | same or opposite line direction |
| Span of one nonzero vector | $\{t\mathbf{v}:t\in\mathbb{R}\}$ | line through origin |
| Span of two nonparallel vectors in $\mathbb{R}^2$ | $c_1\mathbf{u}+c_2\mathbf{v}$ | entire plane |
| Linear dependence | nontrivial combination gives $\mathbf{0}$ | redundant directions |

A list is linearly dependent when

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k=\mathbf{0}
$$

has a solution with at least one nonzero coefficient. Equivalently, one listed vector can be built from the others. Dependence records redundancy among directions.

The zero vector belongs to every span, since all coefficients may be zero. Any list containing $\mathbf{0}$ is dependent because $1\mathbf{0}=\mathbf{0}$ is already a nontrivial relation.

Dependence can be tested by placing the vectors as columns of a matrix. The columns $\mathbf{v}_1,\ldots,\mathbf{v}_k$ are independent exactly when

$$
\begin{bmatrix}\mathbf{v}_1&\cdots&\mathbf{v}_k\end{bmatrix}
\mathbf{c}=\mathbf{0}
$$

has only the zero solution. A pivot in every column is the row-reduction signal. Several dimension facts follow immediately:

- more than $n$ vectors in $\mathbb{R}^n$ must be dependent;
- fewer than $n$ vectors cannot span $\mathbb{R}^n$;
- exactly $n$ vectors form a basis if they are either independent or spanning.

For example, let

$$
\mathbf{a}=\begin{bmatrix}1\\0\\1\end{bmatrix},
\quad
\mathbf{b}=\begin{bmatrix}0\\1\\1\end{bmatrix},
\quad
\mathbf{c}=\begin{bmatrix}2\\-1\\1\end{bmatrix}.
$$

Solving $r\mathbf{a}+s\mathbf{b}=\mathbf{c}$ gives $r=2$ from the first component and $s=-1$ from the second. The third component then reads $r+s=1$, which holds. Thus

$$
\mathbf{c}=2\mathbf{a}-\mathbf{b},
$$

and the three-vector list is dependent. The relation

$$
2\mathbf{a}-\mathbf{b}-\mathbf{c}=\mathbf{0}
$$

displays the nonzero coefficient vector explicitly.

## Testing membership in a span

Let

$$
\mathbf{u}=
\begin{bmatrix}2\\-1\\3\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}0\\4\\1\end{bmatrix}.
$$

First,

$$
3\mathbf{u}-2\mathbf{v}
=
\begin{bmatrix}6\\-3\\9\end{bmatrix}
-
\begin{bmatrix}0\\8\\2\end{bmatrix}
=
\begin{bmatrix}6\\-11\\7\end{bmatrix}.
$$

To decide whether

$$
\mathbf{w}=\begin{bmatrix}5\\1\\4\end{bmatrix}
$$

lies in $\operatorname{span}\{\mathbf{u},\mathbf{v}\}$, solve

$$
c_1\mathbf{u}+c_2\mathbf{v}=\mathbf{w}.
$$

Componentwise, this is

$$
2c_1=5,
\qquad
-c_1+4c_2=1,
\qquad
3c_1+c_2=4.
$$

The first two equations require $c_1=5/2$ and $c_2=7/8$, while the first and third require $c_2=-7/2$. The requirements conflict, so $\mathbf{w}$ is outside the span.

Any span-membership question can be translated into a linear system. For columns $\mathbf{v}_1,\ldots,\mathbf{v}_k$, consistency of

$$
[\mathbf{v}_1\ \cdots\ \mathbf{v}_k]\mathbf{c}=\mathbf{w}
$$

is exactly membership of $\mathbf{w}$ in their span.

When membership fails, least squares finds the point in the span closest to $\mathbf{w}$. The residual is perpendicular to every spanning column at the minimizing combination. Exact membership asks whether that residual is zero; numerical code needs a scale-aware tolerance rather than equality of floating-point values.

## Lines and planes in vector form

The line through $\mathbf{p}$ in a nonzero direction $\mathbf{v}$ is

$$
\mathbf{x}=\mathbf{p}+t\mathbf{v}.
$$

The plane through $\mathbf{p}$ in two nonparallel directions $\mathbf{u},\mathbf{v}$ is

$$
\mathbf{x}=\mathbf{p}+s\mathbf{u}+t\mathbf{v}.
$$

For example, the line through

$$
\mathbf{p}=\begin{bmatrix}1\\-2\\0\end{bmatrix}
$$

in direction

$$
\mathbf{v}=\begin{bmatrix}3\\1\\-4\end{bmatrix}
$$

has equation

$$
\mathbf{x}=
\begin{bmatrix}1\\-2\\0\end{bmatrix}
+t\begin{bmatrix}3\\1\\-4\end{bmatrix},
$$

or

$$
x=1+3t,
\qquad
y=-2+t,
\qquad
z=-4t.
$$

For $\mathbf{q}=\begin{bmatrix}7&0&-8\end{bmatrix}^T$, the first coordinate gives $t=2$. The other two coordinates then give $0$ and $-8$, so $\mathbf{q}$ lies on the line.

The zero vector cannot serve as a direction: $\mathbf{p}+t\mathbf{0}$ never leaves $\mathbf{p}$.

A line or plane written with a base point is generally an affine set, not a vector subspace. It becomes a subspace precisely when it contains the origin. For the line $\mathbf{x}=\mathbf{p}+t\mathbf{v}$, this requires $\mathbf{p}$ itself to be a scalar multiple of $\mathbf{v}$; the same set can then be written as $\mathbf{x}=s\mathbf{v}$.

Parametric and normal descriptions carry complementary information. A plane through $\mathbf{p}$ with normal vector $\mathbf{n}\ne\mathbf{0}$ is

$$
\mathbf{n}\cdot(\mathbf{x}-\mathbf{p})=0.
$$

Every direction lying in the plane must be perpendicular to $\mathbf{n}$. In $\mathbb{R}^3$, two independent in-plane directions determine a normal through their cross product. In higher dimensions there is usually a whole orthogonal complement rather than one distinguished normal vector.

The distance between points $\mathbf{p}$ and $\mathbf{q}$ is $\|\mathbf{q}-\mathbf{p}\|$. For a plane $\mathbf{n}\cdot(\mathbf{x}-\mathbf{p})=0$, the signed normal component of $\mathbf{q}-\mathbf{p}$ gives

$$
\operatorname{dist}(\mathbf{q},\text{plane})
=\frac{|\mathbf{n}\cdot(\mathbf{q}-\mathbf{p})|}{\|\mathbf{n}\|}.
$$

This formula keeps only the component perpendicular to the plane.

## Weighted combinations and data interpretation

A linear combination allows arbitrary coefficients. Two restricted forms occur often. An affine combination has coefficients that sum to one, so translating every input vector translates the result by the same amount. A convex combination also requires nonnegative coefficients. Convex combinations of two points trace the line segment between them; convex combinations of several points fill their convex hull.

For two points $\mathbf{p}$ and $\mathbf{q}$,

$$
(1-t)\mathbf{p}+t\mathbf{q}
$$

is affine for every $t$ and convex when $0\le t\le1$. At $t=0$ it equals $\mathbf{p}$, at $t=1$ it equals $\mathbf{q}$, and at $t=1/2$ it is their midpoint. Values outside that interval extrapolate beyond the segment.

This distinction matters for averaging data. A mean is a convex combination when the weights are nonnegative and sum to one. It remains in any convex feasible region containing the observations. A general linear combination need not. Negative weights can be useful for contrasts or finite differences, but the result no longer has the interpretation of an average.

Component scales must be considered before using Euclidean distance. If one coordinate is measured in meters and another in millimeters, their raw numerical magnitudes do not represent comparable variation. Rescaling or using a weighted norm changes the geometry. The vector-space operations remain valid, but claims about nearest points, angles, or dominant directions depend on the chosen units and inner product.

## Orientation in three dimensions

The cross product is a special operation in $\mathbb{R}^3$. For

$$
\mathbf{u}=
\begin{bmatrix}u_1\\u_2\\u_3\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix},
$$

it is

$$
\mathbf{u}\times\mathbf{v}
=
\begin{bmatrix}
u_2v_3-u_3v_2\\
u_3v_1-u_1v_3\\
u_1v_2-u_2v_1
\end{bmatrix}.
$$

The result is perpendicular to both inputs. Its magnitude is $\|\mathbf{u}\|\|\mathbf{v}\|\sin\theta$, the area of the parallelogram spanned by the vectors. Reversing the order changes the sign, reflecting orientation. If the vectors are parallel, the cross product is zero.

For example, with

$$
\mathbf{u}=\begin{bmatrix}1\\2\\0\end{bmatrix},
\qquad
\mathbf{v}=\begin{bmatrix}0\\1\\3\end{bmatrix},
$$

one obtains

$$
\mathbf{u}\times\mathbf{v}
=\begin{bmatrix}6\\-3\\1\end{bmatrix}.
$$

The checks are immediate:

$$
\begin{bmatrix}6\\-3\\1\end{bmatrix}
\cdot
\begin{bmatrix}1\\2\\0\end{bmatrix}
=6-6=0,
$$

$$
\begin{bmatrix}6\\-3\\1\end{bmatrix}
\cdot
\begin{bmatrix}0\\1\\3\end{bmatrix}
=-3+3=0.
$$

The cross product should not be treated as the general definition of perpendicularity. Dot products and orthogonal complements work in every $\mathbb{R}^n$; a binary vector-valued cross product of this familiar kind is peculiar to three-dimensional geometry.

## Vectors under linear transformations

A matrix transforms a vector by forming a linear combination of its columns. The same map also sends lines through the origin to lines through the origin, or possibly collapses them to zero. It sends a span to the span of the transformed generators:

$$
A\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}
=\operatorname{span}\{A\mathbf{v}_1,\ldots,A\mathbf{v}_k\}.
$$

Independence need not survive. A projection can collapse two distinct directions onto the same line, and any null-space direction disappears. If $A$ is invertible, it preserves all linear relations in both directions, so a list is independent before transformation exactly when its image list is independent.

Translations behave differently because $\mathbf{x}\mapsto A\mathbf{x}+\mathbf{b}$ is not linear unless $\mathbf{b}=\mathbf{0}$. It preserves affine combinations and sends lines to lines, but it moves the origin. Separating the linear part from the translation keeps span and subspace arguments from being applied to an affine map by mistake.

## A numerical span check

```python
import numpy as np

u = np.array([2, -1, 3], dtype=float)
v = np.array([0, 4, 1], dtype=float)
w = np.array([5, 1, 4], dtype=float)

print(3 * u - 2 * v)

A = np.column_stack([u, v])
coeffs, residuals, rank, singular_values = np.linalg.lstsq(A, w, rcond=None)
print(coeffs)
print(A @ coeffs)
print(np.allclose(A @ coeffs, w))
print(rank, singular_values)
```

The least-squares call returns the closest vector in the span. `np.allclose` then tests whether the computed combination actually matches $\mathbf{w}$ to floating-point tolerance; here it does not.

The returned coefficients depend on the chosen spanning vectors. If the columns are dependent, more than one coefficient vector may represent the same point in the span. The geometric projection remains unique, while its coordinates in a redundant generating list need not be.

## Coordinates are representations

In the standard basis, a vector’s coordinates are its entries. In another basis, its coordinates are the weights needed to build the same vector from different basis directions. Equality in a fixed coordinate system means componentwise equality, but a change of basis can give the same abstract vector a different coordinate column.

Several distinctions prevent common errors:

- Vectors must have the same dimension before they can be added or compared componentwise.
- Span contains all scalar combinations, not a short list of sample combinations.
- Two nonzero vectors need not span the ambient space; the number and independence of directions both matter.
- A visual guess does not establish span membership; the coefficient system does.
- A positive scalar preserves direction, a negative scalar reverses it, and addition usually changes both direction and length.

The triangle inequality,

$$
\|\mathbf{u}+\mathbf{v}\|
\le \|\mathbf{u}\|+\|\mathbf{v}\|,
$$

follows by expanding the squared norm and applying Cauchy--Schwarz:

$$
\begin{aligned}
\|\mathbf{u}+\mathbf{v}\|^2
&=\|\mathbf{u}\|^2+2\mathbf{u}\cdot\mathbf{v}+\|\mathbf{v}\|^2\\
&\le \|\mathbf{u}\|^2+2\|\mathbf{u}\|\|\mathbf{v}\|+\|\mathbf{v}\|^2\\
&=(\|\mathbf{u}\|+\|\mathbf{v}\|)^2.
\end{aligned}
$$

Equality requires the vectors to point in the same direction, including the case where one is zero. This inequality lets the Euclidean norm define a metric.

Component meaning also matters in applications. Adding measurement vectors is sensible only when corresponding entries describe the same quantities in compatible units. Matrix multiplication organizes the same linear-combination idea: if $A$ has columns $\mathbf{a}_1,\ldots,\mathbf{a}_n$, then

$$
A\mathbf{x}=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n.
$$

Systems, column spaces, rank, and linear transformations all build on that column-combination interpretation.

## Other norms and high-dimensional effects

Euclidean length is one choice among several. Two common alternatives are

$$
\|\mathbf{x}\|_1=\sum_i|x_i|,
\qquad
\|\mathbf{x}\|_\infty=\max_i|x_i|.
$$

All three are norms: they are nonnegative, homogeneous, and satisfy a triangle inequality. They rank vectors differently. The vector $(1,1)^T$ has Euclidean norm $\sqrt2$, one-norm $2$, and infinity norm $1$. Optimization models choose a norm to encode the kind of error or structure that matters, not merely for notation.

The one-norm often accompanies sparse modeling because its diamond-shaped level sets tend to meet constraints on coordinate axes. The infinity norm controls the worst component. Euclidean norm is rotationally invariant, which fits geometric distance when coordinates share a common scale. Weighted norms incorporate unequal units or confidence.

In high dimensions, geometric intuition from two dimensions can mislead. Random directions are often nearly orthogonal, and the norm of a vector with many modest components can be large even when no single component is. Distance-based methods therefore need scaling and sometimes dimensionality reduction. The componentwise definition remains exact, but pictures of arrows become less informative.

Sparse vectors store only nonzero entries. Addition and dot products can then be computed by merging index lists instead of visiting every coordinate. The mathematical vector still belongs to the full ambient space; sparsity is a representation property. A linear transformation may preserve sparsity, increase it, or destroy it depending on its columns.

Floating-point vectors also change how equality is tested. Results obtained by different arithmetic paths may differ in their last bits. A tolerance should combine absolute and relative scales, and the chosen tolerance belongs to the application. Exact componentwise equality remains appropriate for integer or symbolic coordinates, identifiers, and values known to be copied rather than recomputed.

Missing values are not ordinary coordinates. Replacing an unknown measurement by zero changes dot products, distances, and spans because zero is a known numerical value. A data workflow must impute, mask, or otherwise model missingness before applying vector arithmetic. The linear algebra then describes the completed or restricted data representation, not the unobserved quantities themselves.

<div className="see-also">

See also: [Systems of Linear Equations](/math/linear-algebra/systems-of-linear-equations) · [Orthogonality in Rn](/math/linear-algebra/orthogonality-in-rn) · [General Vector Spaces](/math/linear-algebra/vector-spaces) · [Linear Transformations](/math/linear-algebra/linear-transformations)

</div>
