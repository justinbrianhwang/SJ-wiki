---
title: Orthogonality in Rn
sidebar_position: 8
---

# Orthogonality in Rn

Orthogonality turns vector algebra into geometry. Length, angle, distance, projection, and perpendicularity can all be expressed with the dot product. This is why systems, approximation, and decompositions become geometric: the best answer is often the one whose error is perpendicular to the space of allowable answers.

The dot product is the bridge between coordinates and measurement. Without it, vectors can be added and scaled; with it, one can ask how long a vector is, whether two directions are perpendicular, and how much of one vector lies in another direction. Projection is the key operation that later becomes least squares and QR factorization.

## Definitions

The dot product of $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ is

$$
\mathbf{u}\cdot\mathbf{v}
=u_1v_1+\cdots+u_nv_n.
$$

The Euclidean norm is

$$
\|\mathbf{v}\|=\sqrt{\mathbf{v}\cdot\mathbf{v}},
$$

and the distance between points $\mathbf{u}$ and $\mathbf{v}$ is

$$
d(\mathbf{u},\mathbf{v})=\|\mathbf{u}-\mathbf{v}\|.
$$

Nonzero vectors form angle $\theta$ satisfying

$$
\cos\theta=\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}.
$$

Vectors are orthogonal if $\mathbf{u}\cdot\mathbf{v}=0$. The projection of $\mathbf{u}$ onto a nonzero vector $\mathbf{a}$ is

$$
\operatorname{proj}_{\mathbf{a}}(\mathbf{u})
=
\frac{\mathbf{u}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}\mathbf{a}.
$$

An orthogonal set is a set whose distinct vectors are mutually orthogonal. An orthonormal set is orthogonal and each vector has norm $1$.

## Key results

The Cauchy-Schwarz inequality states

$$
|\mathbf{u}\cdot\mathbf{v}|\leq \|\mathbf{u}\|\,\|\mathbf{v}\|.
$$

This guarantees that the cosine formula is valid because the quotient lies between $-1$ and $1$.

The triangle inequality states

$$
\|\mathbf{u}+\mathbf{v}\|\leq \|\mathbf{u}\|+\|\mathbf{v}\|.
$$

The Pythagorean theorem generalizes: if $\mathbf{u}\cdot\mathbf{v}=0$, then

$$
\|\mathbf{u}+\mathbf{v}\|^2=\|\mathbf{u}\|^2+\|\mathbf{v}\|^2.
$$

Projection decomposes a vector into parallel and orthogonal parts:

$$
\mathbf{u}
=
\operatorname{proj}_{\mathbf{a}}(\mathbf{u})
+
\left(\mathbf{u}-\operatorname{proj}_{\mathbf{a}}(\mathbf{u})\right),
$$

and the second part is orthogonal to $\mathbf{a}$. To verify, compute

$$
\left(\mathbf{u}-\frac{\mathbf{u}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}\mathbf{a}\right)\cdot\mathbf{a}
=
\mathbf{u}\cdot\mathbf{a}
-
\frac{\mathbf{u}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}(\mathbf{a}\cdot\mathbf{a})
=0.
$$

If nonzero vectors are mutually orthogonal, then they are linearly independent. A linear combination equal to zero can be dotted with each vector in turn, forcing each coefficient to be zero.

Orthogonality is also the cleanest language for decomposing information. If a vector is written as a sum of perpendicular pieces, then the squared length of the whole vector is the sum of the squared lengths of the pieces. This is why projection formulas are so useful: they separate "the part explained by a direction" from "the part left over." In a data setting, the explained part might be the component along a trend vector, while the orthogonal error is the part not captured by that trend. In geometry, the same decomposition gives the shortest distance from a point to a line or plane.

For a line $L=\operatorname{span}\{\mathbf{a}\}$ through the origin, the projection $\operatorname{proj}_{\mathbf{a}}(\mathbf{u})$ is the closest point of $L$ to $\mathbf{u}$. To see this, write any vector on the line as $t\mathbf{a}$. The squared distance from $\mathbf{u}$ to $t\mathbf{a}$ is

$$
f(t)=\|\mathbf{u}-t\mathbf{a}\|^2.
$$

Expanding with dot products gives

$$
f(t)=\mathbf{u}\cdot\mathbf{u}-2t(\mathbf{u}\cdot\mathbf{a})+t^2(\mathbf{a}\cdot\mathbf{a}).
$$

This quadratic in $t$ is minimized when

$$
t=\frac{\mathbf{u}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}},
$$

which is exactly the projection coefficient. The algebraic minimizer and the geometric perpendicular-error condition are the same fact in two languages.

The dot product also encodes orientation information. A positive dot product means the angle is acute and the vectors point partly in the same direction. A negative dot product means the angle is obtuse and the vectors point partly against each other. A zero dot product means neither vector has a component in the direction of the other. This interpretation is often faster than computing the actual angle.

Orthogonal matrices preserve this entire geometry. If $Q^TQ=I$, then

$$
(Q\mathbf{u})\cdot(Q\mathbf{v})
=
\mathbf{u}^TQ^TQ\mathbf{v}
=
\mathbf{u}\cdot\mathbf{v}.
$$

Therefore orthogonal transformations preserve lengths, distances, angles, and projections. Rotations and reflections are the standard examples. This fact becomes essential in QR factorization, the spectral theorem, and the singular value decomposition, where orthogonal changes of coordinates are preferred because they do not distort measurement.

## Visual

ASCII projection picture:

```text
                 u
                *
               /|
              / |
             /  | orthogonal error
            /   |
-----------*----*----------------> span{a}
          0   proj_a(u)
```

| Quantity | Formula | Meaning |
|---|---|---|
| Dot product | $\mathbf{u}\cdot\mathbf{v}$ | signed alignment |
| Norm | $\sqrt{\mathbf{v}\cdot\mathbf{v}}$ | length |
| Distance | $\|\mathbf{u}-\mathbf{v}\|$ | length of displacement |
| Projection onto $\mathbf{a}$ | $\frac{\mathbf{u}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}\mathbf{a}$ | closest vector on the line through $\mathbf{a}$ |
| Orthogonality | $\mathbf{u}\cdot\mathbf{v}=0$ | perpendicular directions |

## Worked example 1: Angle, norm, and orthogonality

Problem: for

$$
\mathbf{u}=
\begin{bmatrix}
2\\-1\\2
\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}
1\\4\\1
\end{bmatrix},
$$

compute the dot product, norms, and angle.

Step 1: compute the dot product.

$$
\mathbf{u}\cdot\mathbf{v}
=2(1)+(-1)(4)+2(1)=2-4+2=0.
$$

Step 2: compute norms.

$$
\|\mathbf{u}\|=\sqrt{2^2+(-1)^2+2^2}=\sqrt9=3,
$$

and

$$
\|\mathbf{v}\|=\sqrt{1^2+4^2+1^2}=\sqrt{18}=3\sqrt2.
$$

Step 3: compute the angle.

$$
\cos\theta=\frac{0}{3(3\sqrt2)}=0.
$$

Thus $\theta=\pi/2$. Checked answer: the vectors are orthogonal.

## Worked example 2: Projection onto a vector

Problem: project

$$
\mathbf{u}=
\begin{bmatrix}
3\\4
\end{bmatrix}
$$

onto

$$
\mathbf{a}=
\begin{bmatrix}
1\\2
\end{bmatrix}.
$$

Step 1: compute the dot products.

$$
\mathbf{u}\cdot\mathbf{a}=3(1)+4(2)=11,
\qquad
\mathbf{a}\cdot\mathbf{a}=1^2+2^2=5.
$$

Step 2: apply the projection formula.

$$
\operatorname{proj}_{\mathbf{a}}(\mathbf{u})
=
\frac{11}{5}
\begin{bmatrix}
1\\2
\end{bmatrix}
=
\begin{bmatrix}
11/5\\22/5
\end{bmatrix}.
$$

Step 3: compute the error vector.

$$
\mathbf{e}
=
\mathbf{u}-\operatorname{proj}_{\mathbf{a}}(\mathbf{u})
=
\begin{bmatrix}
3\\4
\end{bmatrix}
-
\begin{bmatrix}
11/5\\22/5
\end{bmatrix}
=
\begin{bmatrix}
4/5\\-2/5
\end{bmatrix}.
$$

Step 4: check orthogonality.

$$
\mathbf{e}\cdot\mathbf{a}
=
\frac45(1)+\left(-\frac25\right)(2)
=\frac45-\frac45=0.
$$

Checked answer: the projection is $\begin{bmatrix}11/5&22/5\end{bmatrix}^T$, and the error is perpendicular to $\mathbf{a}$.

## Code

```python
import numpy as np

u = np.array([3, 4], dtype=float)
a = np.array([1, 2], dtype=float)

proj = (u @ a) / (a @ a) * a
error = u - proj

print(proj)
print(error)
print(error @ a)
print(np.linalg.norm(u) ** 2, np.linalg.norm(proj) ** 2 + np.linalg.norm(error) ** 2)
```

The final line checks the Pythagorean decomposition $\|\mathbf{u}\|^2=\|\operatorname{proj}_{\mathbf{a}}(\mathbf{u})\|^2+\|\mathbf{e}\|^2$.

## Common pitfalls

- Forgetting that projection onto $\mathbf{a}$ requires $\mathbf{a}\neq\mathbf{0}$.
- Using $\|\mathbf{a}\|$ instead of $\mathbf{a}\cdot\mathbf{a}$ in the projection denominator.
- Assuming a zero dot product means one vector must be zero. Nonzero perpendicular vectors have zero dot product.
- Mixing degrees and radians when interpreting angles.
- Treating orthogonal and orthonormal as the same. Orthonormal also requires unit length.
- Believing projection preserves the original vector's length. Projection usually shortens it.

A dependable projection check is to compute the error and dot it with the target direction or subspace basis. If the projection is correct, the error should be orthogonal to every direction in the subspace. This check is often easier and more meaningful than recomputing the projection formula. It also prepares for least squares, where the residual must be orthogonal to every column of the design matrix.

When working with angles, avoid computing inverse cosine unless the angle itself is required. The dot product already tells much of the story. Positive means acute, negative means obtuse, and zero means right angle. The magnitude of the dot product relative to the product of norms tells how strongly aligned the vectors are. This interpretation is common in data analysis, where cosine similarity compares directions rather than lengths.

Orthogonality is not the same as independence, but nonzero orthogonal vectors are automatically independent. The converse is false: independent vectors need not be perpendicular. This distinction matters in basis work. Any basis can express vectors, but an orthonormal basis makes coordinates especially easy because coordinates are dot products.

In numerical work, exact zero dot products are rare when data are measured or computed with floating-point arithmetic. Instead of testing whether $\mathbf{u}\cdot\mathbf{v}=0$ exactly, one usually checks whether its absolute value is small relative to the norms involved. The mathematical definition is exact; the computational test must account for rounding and noise.

Orthogonal complements give another organizing idea. If $W$ is a subspace of $\mathbb{R}^n$, then

$$
W^\perp=\{\mathbf{z}:\mathbf{z}\cdot\mathbf{w}=0\text{ for every }\mathbf{w}\in W\}
$$

is the set of all vectors perpendicular to $W$. Projection decomposes a vector into a part in $W$ and a part in $W^\perp$. This is the geometric form of many algebraic decompositions.

For a matrix $A$, the null space of $A^T$ is orthogonal to the column space of $A$. This is exactly what least squares uses: the residual $\mathbf{b}-A\hat{\mathbf{x}}$ lies in the orthogonal complement of the column space. A fact that begins as perpendicular arrows in $\mathbb{R}^2$ becomes the core condition for regression and approximation.

When studying orthogonality, draw both the vector and its projection whenever possible. The picture reinforces which vector is being projected, which direction or subspace receives the projection, and which error is perpendicular. Most formula errors come from mixing up those roles.

The same dot product can represent physical work, statistical similarity, or geometric alignment depending on context. In physics, force dotted with displacement measures work. In data analysis, normalized dot products compare direction patterns. In geometry, dot products measure angles and projections. The formula is the same, but the interpretation comes from the modeled quantities.

Orthogonality also gives a way to simplify calculations. If vectors are orthogonal, many cross terms vanish when norms are squared. This is why orthogonal bases, QR factorization, and spectral decompositions are so valuable: they turn coupled calculations into sums of independent contributions.

This simplification is the recurring payoff of perpendicular coordinates.

Whenever a calculation becomes messy, look for an orthogonal basis or projection that separates the components.

## Connections

- [Vectors in Rn](/math/linear-algebra/vectors)
- [Orthogonality, Gram-Schmidt, and QR](/math/linear-algebra/orthogonality-qr-gram-schmidt)
- [Least Squares](/math/linear-algebra/least-squares)
- [Inner Product Spaces](/math/linear-algebra/inner-product-spaces)
