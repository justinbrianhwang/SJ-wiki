---
title: Orthogonality in Rn
sidebar_position: 8
---

# Orthogonality in Rn

The dot product adds measurement to vector-space algebra. It defines length, angle, distance, and perpendicularity, then turns approximation into a geometric condition: the closest allowed vector is the one whose error is perpendicular to every allowed direction. That condition leads directly to projection, least squares, QR factorization, and orthogonal decompositions.

## Measurement from the dot product

For $\mathbf u,\mathbf v\in\mathbb R^n$, the standard dot product is

$$
\mathbf u\cdot\mathbf v
=u_1v_1+\cdots+u_nv_n
=\mathbf u^T\mathbf v.
$$

It is symmetric, linear in each argument when the other is fixed, and positive definite:

$$
\mathbf v\cdot\mathbf v\ge0,
$$

with equality only for $\mathbf v=\mathbf0$. These properties allow the definitions

$$
\lVert\mathbf v\rVert=\sqrt{\mathbf v\cdot\mathbf v},
\qquad
d(\mathbf u,\mathbf v)=\lVert\mathbf u-\mathbf v\rVert.
$$

For nonzero vectors, their angle $0\le\theta\le\pi$ is determined by

$$
\cos\theta=\frac{\mathbf u\cdot\mathbf v}
{\lVert\mathbf u\rVert\lVert\mathbf v\rVert}.
$$

The Cauchy–Schwarz inequality

$$
|\mathbf u\cdot\mathbf v|
\le\lVert\mathbf u\rVert\lVert\mathbf v\rVert
$$

ensures that the quotient lies in $[-1,1]$. Equality holds exactly when the vectors are linearly dependent.

One proof already contains the projection idea. For $\mathbf v\ne0$, nonnegativity of

$$
\left\lVert
\mathbf u-\frac{\mathbf u\cdot\mathbf v}{\mathbf v\cdot\mathbf v}\mathbf v
\right\rVert^2
$$

expands to

$$
\lVert\mathbf u\rVert^2
-\frac{(\mathbf u\cdot\mathbf v)^2}{\lVert\mathbf v\rVert^2}
\ge0.
$$

Multiplication by $\lVert\mathbf v\rVert^2$ gives Cauchy–Schwarz after taking square roots. The vector subtracted from $\mathbf u$ is precisely its component along $\mathbf v$.

The inequality also proves the triangle inequality:

$$
\begin{aligned}
\lVert\mathbf u+\mathbf v\rVert^2
&=\lVert\mathbf u\rVert^2
+2\mathbf u\cdot\mathbf v
+\lVert\mathbf v\rVert^2\\
&\le(\lVert\mathbf u\rVert+\lVert\mathbf v\rVert)^2.
\end{aligned}
$$

Taking nonnegative square roots yields

$$
\lVert\mathbf u+\mathbf v\rVert
\le\lVert\mathbf u\rVert+\lVert\mathbf v\rVert.
$$

## Orthogonal and orthonormal sets

Vectors are orthogonal when their dot product is zero. A set is orthogonal if every distinct pair is orthogonal; it is orthonormal if, in addition, every vector has norm $1$.

Any orthogonal set of nonzero vectors is linearly independent. If

$$
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf0,
$$

dotting with $\mathbf v_j$ removes every cross term:

$$
c_j\lVert\mathbf v_j\rVert^2=0.
$$

Since $\mathbf v_j\ne0$, $c_j=0$. This works for each $j$.

The same cancellation gives the Pythagorean identity. If $\mathbf u\cdot\mathbf v=0$, then

$$
\lVert\mathbf u+\mathbf v\rVert^2
=\lVert\mathbf u\rVert^2+\lVert\mathbf v\rVert^2.
$$

For a sum of mutually orthogonal vectors, squared norm is the sum of their squared norms. In an orthonormal basis $\mathbf q_1,\ldots,\mathbf q_n$, the coordinate of $\mathbf x$ along $\mathbf q_j$ is simply $\mathbf x\cdot\mathbf q_j$, and

$$
\mathbf x=\sum_{j=1}^n(\mathbf x\cdot\mathbf q_j)\mathbf q_j.
$$

Taking squared norms gives Parseval's identity in finite dimensions:

$$
\lVert\mathbf x\rVert^2
=\sum_{j=1}^n|\mathbf x\cdot\mathbf q_j|^2.
$$

For an orthonormal list that spans only a subspace, the corresponding sum is at most $\lVert\mathbf x\rVert^2$; the missing amount is the squared norm of the perpendicular residual.

## Projection onto a line

Let $L=\operatorname{span}\{\mathbf a\}$ with $\mathbf a\ne0$. Seek a multiple $c\mathbf a$ such that the residual $\mathbf u-c\mathbf a$ is perpendicular to the line. The condition is

$$
(\mathbf u-c\mathbf a)\cdot\mathbf a=0.
$$

Solving for $c$ gives

$$
c=\frac{\mathbf u\cdot\mathbf a}{\mathbf a\cdot\mathbf a}.
$$

Therefore

$$
\operatorname{proj}_{\mathbf a}\mathbf u
=\frac{\mathbf u\cdot\mathbf a}{\mathbf a\cdot\mathbf a}\mathbf a.
$$

The scalar component in the unit direction of $\mathbf a$ is

$$
\operatorname{comp}_{\mathbf a}\mathbf u
=\frac{\mathbf u\cdot\mathbf a}{\lVert\mathbf a\rVert}.
$$

Do not confuse the scalar component with the projection vector, and do not replace the projection denominator by $\lVert\mathbf a\rVert$.

The perpendicular condition also proves closest-point optimality. Any other point on the line is $c\mathbf a+t\mathbf a$, where $c\mathbf a$ is the projection. Then

$$
\mathbf u-(c+t)\mathbf a
=\underbrace{(\mathbf u-c\mathbf a)}_{\perp\mathbf a}
-t\mathbf a.
$$

By Pythagoras,

$$
\lVert\mathbf u-(c+t)\mathbf a\rVert^2
=\lVert\mathbf u-c\mathbf a\rVert^2
+t^2\lVert\mathbf a\rVert^2.
$$

The second term is nonnegative and vanishes only at $t=0$. The perpendicular projection is the unique closest point.

### Worked example: projection and residual

Project

$$
\mathbf u=\begin{bmatrix}3\\4\\1\end{bmatrix}
$$

onto the line through

$$
\mathbf a=\begin{bmatrix}1\\2\\-1\end{bmatrix}.
$$

First compute

$$
\mathbf u\cdot\mathbf a=3+8-1=10,
$$

$$
\mathbf a\cdot\mathbf a=1+4+1=6.
$$

Hence

$$
\mathbf p=\operatorname{proj}_{\mathbf a}\mathbf u
=\frac{10}{6}\mathbf a
=\begin{bmatrix}5/3\\10/3\\-5/3\end{bmatrix}.
$$

The residual is

$$
\mathbf e=\mathbf u-\mathbf p
=\begin{bmatrix}4/3\\2/3\\8/3\end{bmatrix}.
$$

Check orthogonality:

$$
\mathbf e\cdot\mathbf a
=\frac43+\frac43-\frac83=0.
$$

The distance from $\mathbf u$ to the line is

$$
\lVert\mathbf e\rVert
=\sqrt{\frac{16+4+64}{9}}
=\frac{2\sqrt{21}}{3}.
$$

Finally,

$$
\lVert\mathbf u\rVert^2=26,
\qquad
\lVert\mathbf p\rVert^2=\frac{50}{3},
\qquad
\lVert\mathbf e\rVert^2=\frac{28}{3},
$$

and $50/3+28/3=26$, confirming the Pythagorean decomposition.

## Projection onto a subspace

If $W$ has an orthonormal basis $\mathbf q_1,\ldots,\mathbf q_k$, then

$$
\operatorname{proj}_W\mathbf b
=\sum_{j=1}^k(\mathbf b\cdot\mathbf q_j)\mathbf q_j.
$$

Each coefficient is independent because the basis directions are orthonormal. The residual

$$
\mathbf r=\mathbf b-\operatorname{proj}_W\mathbf b
$$

is perpendicular to every $\mathbf q_j$, and therefore to every vector in $W$.

If the basis columns form $Q$ with $Q^TQ=I$, projection has matrix form

$$
\mathbf p=QQ^T\mathbf b.
$$

The projection matrix $P=QQ^T$ is symmetric and idempotent:

$$
P^T=P,
\qquad
P^2=P.
$$

Idempotence says that projecting a vector already in the subspace changes nothing. The complementary projection $I-P$ maps onto $W^\perp$.

For a full-column-rank matrix $A$ whose columns are not orthonormal, the same projection is

$$
P=A(A^TA)^{-1}A^T.
$$

This formula comes from requiring $A^T(\mathbf b-A\widehat{\mathbf x})=0$. QR factorization is usually a better computational route because it avoids explicitly forming $A^TA$.

### Worked example: projection onto a plane in $\mathbb R^3$

Let

$$
W=\operatorname{span}\left\{
\mathbf q_1=\frac1{\sqrt2}\begin{bmatrix}1\\1\\0\end{bmatrix},
\mathbf q_2=\frac1{\sqrt6}\begin{bmatrix}1\\-1\\2\end{bmatrix}
\right\}
$$

and project $\mathbf b=[2,1,3]^T$. The basis is orthonormal because each vector has norm $1$ and

$$
\mathbf q_1\cdot\mathbf q_2
=\frac{1-1+0}{\sqrt{12}}=0.
$$

The coordinates are

$$
c_1=\mathbf b\cdot\mathbf q_1=\frac3{\sqrt2},
$$

$$
c_2=\mathbf b\cdot\mathbf q_2
=\frac{2-1+6}{\sqrt6}=\frac7{\sqrt6}.
$$

Therefore

$$
\begin{aligned}
\mathbf p
&=c_1\mathbf q_1+c_2\mathbf q_2\\
&=\frac32\begin{bmatrix}1\\1\\0\end{bmatrix}
+\frac76\begin{bmatrix}1\\-1\\2\end{bmatrix}\\
&=\begin{bmatrix}8/3\\1/3\\7/3\end{bmatrix}.
\end{aligned}
$$

The residual is

$$
\mathbf r=\mathbf b-\mathbf p
=\begin{bmatrix}-2/3\\2/3\\2/3\end{bmatrix}.
$$

Checking against both basis directions gives

$$
\mathbf r\cdot\mathbf q_1=0,
\qquad
\mathbf r\cdot\mathbf q_2=0.
$$

Thus $\mathbf r\in W^\perp$, as required.

## Affine sets: projecting when the target misses the origin

A linear subspace contains the origin, but many geometric constraints are translated subspaces. An affine set has form

$$
\mathbf p_0+W
=\{\mathbf p_0+\mathbf w:\mathbf w\in W\}.
$$

To project $\mathbf b$ onto it, first translate by $-\mathbf p_0$, project the displacement onto $W$, and translate back:

$$
\operatorname{proj}_{\mathbf p_0+W}(\mathbf b)
=\mathbf p_0+\operatorname{proj}_W(\mathbf b-\mathbf p_0).
$$

The residual remains perpendicular to $W$, the set of allowable directions. It need not be perpendicular to the position vector of the closest point, since that point is generally not in $W$.

For a hyperplane

$$
H=\{\mathbf x:\mathbf n\cdot\mathbf x=d\},
\qquad \mathbf n\ne0,
$$

the correction from $\mathbf b$ must lie along the normal. Write the closest point as $\mathbf p=\mathbf b-c\mathbf n$ and impose the plane equation:

$$
\mathbf n\cdot(\mathbf b-c\mathbf n)=d.
$$

Solving,

$$
c=\frac{\mathbf n\cdot\mathbf b-d}{\lVert\mathbf n\rVert^2},
$$

so

$$
\mathbf p=\mathbf b-
\frac{\mathbf n\cdot\mathbf b-d}{\lVert\mathbf n\rVert^2}\mathbf n.
$$

The point-to-hyperplane distance is the correction length,

$$
\frac{|\mathbf n\cdot\mathbf b-d|}{\lVert\mathbf n\rVert}.
$$

This is the same projection geometry used for a plane in three dimensions, now stated for $\mathbb R^n$.

## Orthogonal complements and the four fundamental subspaces

For a subspace $W\subseteq\mathbb R^n$, define

$$
W^\perp=\{\mathbf z:\mathbf z\cdot\mathbf w=0
\text{ for every }\mathbf w\in W\}.
$$

The complement is itself a subspace, and finite-dimensional Euclidean space decomposes as

$$
\mathbb R^n=W\oplus W^\perp.
$$

Every vector has a unique sum of one vector in $W$ and one in $W^\perp$. Their dimensions satisfy

$$
\dim W+\dim W^\perp=n.
$$

For an $m\times n$ matrix $A$, orthogonality links its fundamental subspaces:

$$
\operatorname{Null}(A)=\operatorname{Row}(A)^\perp,
$$

$$
\operatorname{Null}(A^T)=\operatorname{Col}(A)^\perp.
$$

The second identity explains least-squares residuals. If $A\widehat{\mathbf x}$ is the closest vector in the column space to $\mathbf b$, then

$$
\mathbf b-A\widehat{\mathbf x}\in\operatorname{Null}(A^T),
$$

which is equivalent to the normal equations

$$
A^TA\widehat{\mathbf x}=A^T\mathbf b.
$$

## Orthogonal matrices preserve Euclidean geometry

A square matrix $Q$ is orthogonal when

$$
Q^TQ=I.
$$

Its columns and rows are orthonormal, and $Q^{-1}=Q^T$. For any vectors,

$$
(Q\mathbf u)\cdot(Q\mathbf v)
=\mathbf u^TQ^TQ\mathbf v
=\mathbf u\cdot\mathbf v.
$$

Lengths, distances, angles, and orthogonality are preserved. The determinant is $1$ or $-1$: rotations have determinant $1$, while reflections and orientation-reversing combinations have determinant $-1$.

Orthogonal coordinate changes are numerically attractive because they do not magnify the Euclidean norm. QR factorization, the symmetric spectral theorem, and the singular value decomposition all rely on them.

## Floating-point orthogonality

Measured or computed vectors rarely have dot product exactly zero. A scale-aware test compares

$$
|\mathbf u\cdot\mathbf v|
$$

with a tolerance times $\lVert\mathbf u\rVert\lVert\mathbf v\rVert$. An absolute tolerance alone behaves poorly when vector magnitudes vary widely. For a computed basis matrix $Q$, inspect

$$
\lVert Q^TQ-I\rVert
$$

rather than comparing every entry for exact equality.

Near-zero input vectors also need care: normalization amplifies relative error and may divide by a number below the meaningful scale of the data. Numerical rank and “orthogonal enough” always depend on a tolerance tied to the matrix scale and intended use.

## Beyond the standard dot product

Orthogonality depends on the chosen inner product. The standard dot product treats coordinate axes as perpendicular and weights every coordinate equally. A positive-definite matrix can define a weighted inner product in which directions or units carry different importance. Length, projection, and perpendicularity then change with that choice.

This matters when coordinates use different physical units or have unequal uncertainty. Raw Euclidean distance between a temperature and a pressure coordinate has no clear meaning until scaling is chosen. Standardizing variables, weighting by measurement precision, or using an energy matrix states what discrepancies count as large. The algebra of projection remains the same after replacing the dot product consistently.

Changing the inner product midway through a calculation is invalid. A basis orthonormal under one weighting may not be orthogonal under another, and a residual perpendicular in the Euclidean sense may not minimize the weighted error. The metric belongs with the model, not merely with the final numerical method.

The familiar function-space inner products follow the same pattern. Dot-product sums become integrals, and orthogonal vectors become orthogonal functions. Fourier coefficients are projections onto sine and cosine directions. Finite-dimensional formulas therefore serve as prototypes for approximation in much larger spaces.

## Projection operators as linear maps

Projection onto a fixed subspace is linear even though finding the subspace or a basis may require substantial work. Its matrix has eigenvalue one on the target subspace and eigenvalue zero on the orthogonal complement. Applying it twice changes nothing, which is the geometric content of idempotence.

An orthogonal projection is symmetric. An idempotent matrix that is not symmetric still projects onto a subspace, but generally along a nonperpendicular complementary direction. Such an oblique projection can magnify lengths and does not give the nearest Euclidean point. Symmetry distinguishes closest-point projection from projection in a broader algebraic sense.

The trace of an orthogonal projection equals the dimension of its range because its eigenvalues consist of ones and zeros. This supplies a useful check on an explicitly formed projection matrix. Its rank, trace, and number of unit eigenvalues agree.

Projection matrices should often remain implicit in computation. If an orthonormal basis is available, applying the projection as two matrix-vector multiplications avoids storing a dense square matrix. In least squares, QR applies the same idea while preserving numerical accuracy. Explicit formulas are valuable for reasoning but can be an inefficient implementation.

## Distance, approximation, and information loss

Projection keeps the component representable by the target subspace and discards the orthogonal component. The squared residual quantifies the lost Euclidean information. Enlarging the target subspace cannot increase the best approximation error, because every old candidate remains available in the larger set.

Equality can occur when every newly added direction is orthogonal to the residual's useful component. A smaller error therefore measures whether new directions explain something previously missing, not merely whether the model has more columns. This observation underlies nested least-squares models and incremental basis construction.

In data analysis, cosine similarity compares direction after ignoring overall magnitude. It is undefined for a zero vector and can be misleading when a common offset dominates every coordinate. Centering or otherwise preprocessing data changes the geometry and should be reported. A high cosine similarity says vectors point similarly under the chosen coordinate weighting; it does not by itself mean their entries are close in absolute size.

The nearest-point theorem relies on the target being a closed subspace. Every subspace of finite-dimensional Euclidean space is closed, so no qualification is needed here. In infinite-dimensional settings, a nonclosed subspace may have an infimum distance without containing a closest point. The finite-dimensional theory hides that topological complication.

## Dimension checks and constructive complements

To compute an orthogonal complement from spanning vectors, place those vectors as rows and solve the homogeneous system requiring zero dot products. To find vectors perpendicular to a column space, solve the transpose system. Row reduction gives a basis, and Gram–Schmidt can make it orthonormal afterward.

Dimension provides a strong check. If a subspace of the ambient space has dimension equal to the ambient dimension, its orthogonal complement contains only zero. If the subspace has codimension one, its complement is a line generated by a normal vector. More generally, the number of independent perpendicular directions equals the codimension.

Taking the orthogonal complement twice returns the original subspace in finite dimensions. One inclusion is immediate because every vector in the subspace is perpendicular to every vector in its complement. The dimension formula forces equality. This identity lets a subspace be represented either by spanning directions or by homogeneous constraints, whichever is more convenient.

For a matrix, the row-space/nullspace pair and column-space/left-nullspace pair express the same duality. Rank-nullity and orthogonal-complement dimensions agree. These relations are useful diagnostic tools: a computed residual claimed to lie in the left nullspace should be checked against the columns, and a proposed null vector should be checked against every row.

## Geometry under finite precision

Near orthogonality is scale dependent. An absolute dot product of one may be negligible for vectors of length a million and decisive for unit vectors. Normalizing before comparison or using a relative criterion gives a dimensionless measure. The angle itself can be unstable near parallel or antiparallel configurations because inverse cosine changes rapidly there.

Forming a difference of nearly parallel vectors can lose relative accuracy. Projection residuals in Gram–Schmidt encounter exactly this situation. Stable algorithms reorganize operations or use orthogonal reflections to reduce the damage. The underlying theorem is exact; the route used to evaluate it determines how well finite precision preserves the geometry.

Checks should match the claimed property. A small reconstruction error does not imply that a basis is orthogonal, and a nearly orthogonal basis does not imply it spans the intended data accurately. Projection work should inspect both the residual's orthogonality and the reconstruction of the original vector as projected part plus residual.

<div className="see-also">

See also: [Vectors in Rn](/math/linear-algebra/vectors) · [Orthogonality, Gram–Schmidt, and QR](/math/linear-algebra/orthogonality-qr-gram-schmidt) · [Least squares](/math/linear-algebra/least-squares) · [Inner product spaces](/math/linear-algebra/inner-product-spaces)

</div>
