---
title: Orthogonality, Gram-Schmidt, and QR
sidebar_position: 14
---

# Orthogonality, Gram-Schmidt, and QR

Orthogonal bases are computationally valuable because coordinates become dot products and projections separate cleanly. The Gram-Schmidt process converts an independent set into an orthogonal or orthonormal set with the same span. In matrix form, this becomes QR decomposition, one of the central tools for least squares and numerical linear algebra.

The main idea is to remove from each new vector the parts already explained by previous directions. What remains is perpendicular to the earlier directions. Repeating this produces a basis with the same span but much cleaner geometry.

## Definitions

A set $\{\mathbf{q}_1,\ldots,\mathbf{q}_k\}$ is orthonormal if

$$
\mathbf{q}_i\cdot\mathbf{q}_j=
\begin{cases}
1,&i=j,\\
0,&i\neq j.
\end{cases}
$$

The orthogonal projection of $\mathbf{v}$ onto a subspace $W$ with orthonormal basis $\mathbf{q}_1,\ldots,\mathbf{q}_k$ is

$$
\operatorname{proj}_W(\mathbf{v})
=
(\mathbf{v}\cdot\mathbf{q}_1)\mathbf{q}_1+\cdots+
(\mathbf{v}\cdot\mathbf{q}_k)\mathbf{q}_k.
$$

A QR decomposition of an $m\times n$ matrix $A$ with independent columns is

$$
A=QR,
$$

where $Q$ has orthonormal columns and $R$ is upper triangular with positive diagonal entries in the standard construction.

Classical Gram-Schmidt starts with independent vectors $\mathbf{v}_1,\ldots,\mathbf{v}_k$ and produces orthogonal vectors $\mathbf{u}_1,\ldots,\mathbf{u}_k$:

$$
\mathbf{u}_1=\mathbf{v}_1,
$$

and

$$
\mathbf{u}_j=\mathbf{v}_j-\sum_{i=1}^{j-1}
\operatorname{proj}_{\mathbf{u}_i}(\mathbf{v}_j).
$$

Then $\mathbf{q}_j=\mathbf{u}_j/\|\mathbf{u}_j\|$ gives an orthonormal set.

## Key results

Gram-Schmidt preserves span at each step:

$$
\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_j\}
=
\operatorname{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_j\}.
$$

The reason is that $\mathbf{u}_j$ is obtained from $\mathbf{v}_j$ by subtracting a vector in the span of the previous $\mathbf{u}$'s, and the operation can be reversed.

The vectors produced by Gram-Schmidt are orthogonal. When constructing $\mathbf{u}_j$, the projection terms remove exactly the components in the earlier directions. For $i\lt j$,

$$
\mathbf{u}_j\cdot\mathbf{u}_i=0.
$$

If $A$ has independent columns $\mathbf{a}_1,\ldots,\mathbf{a}_n$, applying Gram-Schmidt to those columns gives

$$
A=QR.
$$

The entries of $R$ are dot products and norms:

$$
r_{ij}=\mathbf{q}_i\cdot\mathbf{a}_j
\quad (i\leq j),
\qquad
r_{jj}=\|\mathbf{u}_j\|.
$$

Because $Q^TQ=I$, QR simplifies least squares. Instead of solving normal equations $A^TA\hat{\mathbf{x}}=A^T\mathbf{b}$, one can solve

$$
R\hat{\mathbf{x}}=Q^T\mathbf{b}.
$$

This is often more numerically stable.

The upper triangular shape of $R$ records the order in which new directions are explained by previous orthonormal directions. If $A=[\mathbf{a}_1\ \cdots\ \mathbf{a}_n]$ and $Q=[\mathbf{q}_1\ \cdots\ \mathbf{q}_n]$, then the equation $A=QR$ says each original column can be reconstructed from the orthonormal columns:

$$
\mathbf{a}_j=r_{1j}\mathbf{q}_1+r_{2j}\mathbf{q}_2+\cdots+r_{jj}\mathbf{q}_j.
$$

No later $\mathbf{q}$ appears in this expression, which is why $R$ has zeros below the diagonal. The diagonal entry $r_{jj}$ is the length of the new component that remains after subtracting earlier projections. If that length is zero, the original columns were dependent and the standard full-column QR construction breaks down.

For hand computation, classical Gram-Schmidt is transparent because each projection is visible. For numerical computation, however, classical Gram-Schmidt can lose orthogonality when vectors are nearly dependent. Modified Gram-Schmidt rearranges the same mathematical operations to reduce error accumulation. Householder QR uses orthogonal reflections to zero out entire subcolumns and is the usual dense-matrix workhorse. These algorithms produce the same kind of factorization, but they differ in stability and implementation cost.

The QR factorization also explains why orthonormal columns are ideal for least squares. If $Q$ has orthonormal columns, then

$$
\|Q\mathbf{x}-\mathbf{b}\|^2
=
\|\mathbf{x}-Q^T\mathbf{b}\|^2+\|\mathbf{b}-QQ^T\mathbf{b}\|^2.
$$

The second term is independent of $\mathbf{x}$, so the best choice is $\mathbf{x}=Q^T\mathbf{b}$. For a general $A=QR$, the vector $R\hat{\mathbf{x}}$ plays the role of those orthonormal coordinates. This is why QR is more than a neat decomposition: it converts a geometric projection problem into a triangular system.

When the columns of $A$ are not independent, QR still exists in variants with column pivoting or reduced rank. In that setting, the diagonal entries of $R$ help reveal numerical rank. A very small diagonal entry means a new column adds little independent information beyond the previous columns. This diagnostic role is one reason QR appears in data fitting and numerical rank estimation.

## Visual

```mermaid
flowchart LR
  A["Independent columns of A"] --> B["Subtract projections"]
  B --> C["Orthogonal vectors u_i"]
  C --> D["Normalize"]
  D --> E["Orthonormal columns Q"]
  E --> F["Upper triangular coefficients R"]
  F --> G["A = Q R"]
```

ASCII projection removal:

```text
v2
 *
 |\
 | \
 |  \  u2 = v2 - proj_u1(v2)
 |   *
 |  /
 | /
 *--------------------> u1
0       proj_u1(v2)
```

## Worked example 1: Apply Gram-Schmidt in R2

Problem: orthonormalize

$$
\mathbf{v}_1=
\begin{bmatrix}
1\\1
\end{bmatrix},
\qquad
\mathbf{v}_2=
\begin{bmatrix}
1\\0
\end{bmatrix}.
$$

Step 1: set

$$
\mathbf{u}_1=\mathbf{v}_1=
\begin{bmatrix}
1\\1
\end{bmatrix}.
$$

Normalize:

$$
\|\mathbf{u}_1\|=\sqrt{1^2+1^2}=\sqrt2,
\qquad
\mathbf{q}_1=\frac{1}{\sqrt2}
\begin{bmatrix}
1\\1
\end{bmatrix}.
$$

Step 2: subtract the projection of $\mathbf{v}_2$ onto $\mathbf{u}_1$:

$$
\operatorname{proj}_{\mathbf{u}_1}(\mathbf{v}_2)
=
\frac{\mathbf{v}_2\cdot\mathbf{u}_1}{\mathbf{u}_1\cdot\mathbf{u}_1}\mathbf{u}_1
=
\frac{1}{2}
\begin{bmatrix}
1\\1
\end{bmatrix}
=
\begin{bmatrix}
1/2\\1/2
\end{bmatrix}.
$$

Thus

$$
\mathbf{u}_2=
\begin{bmatrix}
1\\0
\end{bmatrix}
-
\begin{bmatrix}
1/2\\1/2
\end{bmatrix}
=
\begin{bmatrix}
1/2\\-1/2
\end{bmatrix}.
$$

Step 3: normalize $\mathbf{u}_2$.

$$
\|\mathbf{u}_2\|=\sqrt{1/4+1/4}=\frac{1}{\sqrt2},
$$

so

$$
\mathbf{q}_2=
\begin{bmatrix}
1/\sqrt2\\
-1/\sqrt2
\end{bmatrix}.
$$

Checked answer: $\mathbf{q}_1\cdot\mathbf{q}_2=1/2-1/2=0$, and both vectors have norm $1$.

## Worked example 2: Build QR and solve a least-squares system

Problem: let

$$
A=
\begin{bmatrix}
1&1\\
1&0\\
0&1
\end{bmatrix},
\qquad
\mathbf{b}=
\begin{bmatrix}
2\\1\\1
\end{bmatrix}.
$$

Find the QR decomposition by Gram-Schmidt and solve the least-squares problem.

Step 1: columns are

$$
\mathbf{a}_1=
\begin{bmatrix}1\\1\\0\end{bmatrix},
\qquad
\mathbf{a}_2=
\begin{bmatrix}1\\0\\1\end{bmatrix}.
$$

Normalize $\mathbf{a}_1$:

$$
r_{11}=\|\mathbf{a}_1\|=\sqrt2,
\qquad
\mathbf{q}_1=\frac{1}{\sqrt2}\begin{bmatrix}1\\1\\0\end{bmatrix}.
$$

Step 2: compute

$$
r_{12}=\mathbf{q}_1\cdot\mathbf{a}_2=\frac{1}{\sqrt2}.
$$

Remove this component:

$$
\mathbf{u}_2=\mathbf{a}_2-r_{12}\mathbf{q}_1
=
\begin{bmatrix}1\\0\\1\end{bmatrix}
-
\frac12\begin{bmatrix}1\\1\\0\end{bmatrix}
=
\begin{bmatrix}1/2\\-1/2\\1\end{bmatrix}.
$$

Then

$$
r_{22}=\|\mathbf{u}_2\|=\sqrt{\frac14+\frac14+1}=\sqrt{\frac32}.
$$

Step 3: solve $R\hat{\mathbf{x}}=Q^T\mathbf{b}$. The right side entries are

$$
\mathbf{q}_1\cdot\mathbf{b}=\frac{3}{\sqrt2},
\qquad
\mathbf{q}_2\cdot\mathbf{b}=\frac{1}{\sqrt{3/2}}.
$$

The triangular system is

$$
\begin{bmatrix}
\sqrt2&1/\sqrt2\\
0&\sqrt{3/2}
\end{bmatrix}
\begin{bmatrix}
x_1\\x_2
\end{bmatrix}
=
\begin{bmatrix}
3/\sqrt2\\
1/\sqrt{3/2}
\end{bmatrix}.
$$

The second equation gives $x_2=2/3$. The first gives

$$
\sqrt2x_1+\frac{1}{\sqrt2}\frac23=\frac{3}{\sqrt2}.
$$

Multiply by $\sqrt2$:

$$
2x_1+\frac23=3
\quad\Longrightarrow\quad
x_1=\frac76.
$$

Checked answer: $\hat{\mathbf{x}}=\begin{bmatrix}7/6&2/3\end{bmatrix}^T$.

## Code

```python
import numpy as np

A = np.array([[1, 1],
              [1, 0],
              [0, 1]], dtype=float)
b = np.array([2, 1, 1], dtype=float)

Q, R = np.linalg.qr(A, mode="reduced")
x = np.linalg.solve(R, Q.T @ b)

print(Q)
print(R)
print(x)
print(np.allclose(A, Q @ R))
```

NumPy uses stable QR algorithms rather than the classical hand version. The mathematical factorization is the same: orthonormal columns in $Q$ and an upper triangular matrix $R$.

## Common pitfalls

- Forgetting to subtract all previous projections, not only the immediately previous one.
- Normalizing before subtracting projections without adjusting formulas consistently.
- Treating an orthogonal basis as automatically orthonormal.
- Using Gram-Schmidt on a dependent list without handling the zero vector that appears.
- Assuming classical Gram-Schmidt is the most stable numerical method. Modified Gram-Schmidt or Householder QR is preferred in serious computation.
- Mixing the full and reduced QR shapes.

A good hand-check for Gram-Schmidt is to verify two properties at every stage: the new vector is orthogonal to all earlier vectors, and the span has not changed. Orthogonality checks the projection arithmetic. Span preservation checks that no direction was accidentally discarded. If a nonzero vector becomes zero during the process, the original list was dependent and cannot produce the requested number of orthonormal vectors.

For QR, shape awareness prevents many mistakes. If $A$ is $m\times n$ with independent columns and $m\geq n$, the reduced $Q$ is $m\times n$ and $R$ is $n\times n$. The full $Q$ is $m\times m$, but the additional columns are not needed for most least-squares computations. Both conventions are valid, so always identify which one is being used.

The diagonal entries of $R$ have geometric meaning. Each $r_{jj}$ is the length of the component of $\mathbf{a}_j$ that remains after removing projections onto the earlier $\mathbf{q}$ vectors. Large values mean the column contributes a substantial new direction. Tiny values mean the column is nearly dependent on earlier columns, which can be a warning sign in data fitting.

When QR is used for least squares, the residual is still the central geometric object. QR does not change the goal; it provides a stable way to compute the projection onto the column space. After solving $R\hat{\mathbf{x}}=Q^T\mathbf{b}$, it is still useful to compute $\mathbf{r}=\mathbf{b}-A\hat{\mathbf{x}}$ and check that $A^T\mathbf{r}$ is close to zero.

The order of the input vectors affects the intermediate Gram-Schmidt vectors. Different orders can produce different orthonormal bases for the same subspace. This is not a contradiction, because bases are not unique. The subspace is the invariant object; the particular orthonormal basis depends on the construction choices.

In exact arithmetic, the formula using projections onto $\mathbf{u}_i$ and the formula using dot products with normalized $\mathbf{q}_i$ are equivalent. In computation, the normalized version is often easier to organize because the coefficient of $\mathbf{q}_i$ is simply $\mathbf{v}\cdot\mathbf{q}_i$. Keeping vectors normalized also makes it easier to detect loss of orthogonality.

QR also gives a clean determinant fact for square matrices. If $A=QR$ and $Q$ is orthogonal, then $\vert \det(Q)\vert =1$, so

$$
|\det(A)|=|\det(R)|.
$$

Since $R$ is triangular, its determinant is the product of its diagonal entries. This is another example of a factorization turning a hard matrix question into an easier triangular one.

A compact verification for QR is to check both $Q^TQ=I$ and $QR=A$. The first condition confirms orthonormal columns; the second confirms that the original matrix was reconstructed. One without the other is not enough.

Together they verify the geometry and the factorization.

## Connections

- [Orthogonality in Rn](/math/linear-algebra/orthogonality-in-rn)
- [Inner Product Spaces](/math/linear-algebra/inner-product-spaces)
- [Least Squares](/math/linear-algebra/least-squares)
- [Numerical Linear Algebra](/math/linear-algebra/numerical-linear-algebra)
