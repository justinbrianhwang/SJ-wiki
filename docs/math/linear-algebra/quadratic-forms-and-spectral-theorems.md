---
title: Quadratic Forms and Spectral Theorems
sidebar_position: 16
---

# Quadratic Forms and Spectral Theorems

Quadratic forms turn symmetric matrices into scalar-valued geometry. They describe conic sections, surfaces, energy functions, constrained extrema, and optimization tests. The spectral theorem is the key simplifier: a real symmetric matrix can be diagonalized by an orthogonal change of coordinates.

![An eigenvector keeps its direction while a matrix scales it.](https://commons.wikimedia.org/wiki/Special:FilePath/Eigenvalue_equation.svg)

*Figure: The eigenvalue equation captures directions preserved by a linear transformation. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Eigenvalue_equation.svg), Lyudmil Antonov, CC BY-SA 4.0.*

The reason symmetry matters is that symmetric matrices have especially clean eigenstructure. Their eigenvalues are real, eigenvectors from different eigenspaces are orthogonal, and an orthonormal eigenbasis exists. That lets quadratic forms be rotated into a coordinate system with no cross terms.

## Definitions

A quadratic form in $\mathbb{R}^n$ is an expression

$$
Q(\mathbf{x})=\mathbf{x}^TA\mathbf{x},
$$

where $A$ is symmetric. For two variables,

$$
Q(x,y)=ax^2+2bxy+cy^2
$$

corresponds to

$$
A=
\begin{bmatrix}
a&b\\
b&c
\end{bmatrix}.
$$

A matrix $Q$ is orthogonal if

$$
Q^TQ=I.
$$

Orthogonal matrices preserve lengths and dot products. A matrix $A$ is orthogonally diagonalizable if

$$
Q^TAQ=D
$$

for some orthogonal $Q$ and diagonal $D$.

A quadratic form is positive definite if $Q(\mathbf{x})\gt 0$ for every nonzero $\mathbf{x}$. It is negative definite if $Q(\mathbf{x})\lt 0$ for every nonzero $\mathbf{x}$. It is indefinite if it takes both positive and negative values.

## Key results

Spectral theorem for real symmetric matrices: if $A$ is real and symmetric, then $A$ is orthogonally diagonalizable. That is, there is an orthogonal matrix $Q$ and a real diagonal matrix $D$ such that

$$
A=QDQ^T.
$$

The columns of $Q$ are orthonormal eigenvectors of $A$, and the diagonal entries of $D$ are the corresponding eigenvalues.

Principal axes theorem: if $A$ is symmetric and $\mathbf{x}=Q\mathbf{y}$, then

$$
\mathbf{x}^TA\mathbf{x}
=
\mathbf{y}^TQ^TAQ\mathbf{y}
=
\mathbf{y}^TD\mathbf{y}.
$$

Thus the quadratic form becomes

$$
\lambda_1y_1^2+\cdots+\lambda_ny_n^2,
$$

with no cross terms.

Eigenvalues classify definiteness:

| Eigenvalues of symmetric $A$ | Type of quadratic form |
|---|---|
| all positive | positive definite |
| all nonnegative and at least one zero | positive semidefinite |
| all negative | negative definite |
| all nonpositive and at least one zero | negative semidefinite |
| both positive and negative | indefinite |

For a differentiable function of two variables, the Hessian matrix at a critical point is symmetric under common smoothness assumptions. The definiteness of the Hessian gives the second-derivative test: positive definite means local minimum, negative definite means local maximum, and indefinite means saddle point.

The cross term in a quadratic form measures how the original coordinate axes fail to align with the natural axes of the form. For

$$
Q(x,y)=ax^2+2bxy+cy^2,
$$

the term $2bxy$ mixes the variables. Orthogonal diagonalization chooses new perpendicular axes so that the same form is written without a mixed term:

$$
Q=\lambda_1y_1^2+\lambda_2y_2^2.
$$

The eigenvectors of the symmetric matrix point along these principal axes, and the eigenvalues measure curvature or scaling in those directions.

Positive definiteness has several equivalent tests. For symmetric matrices, the eigenvalue test is conceptually clean: all eigenvalues must be positive. For a $2\times2$ symmetric matrix

$$
\begin{bmatrix}
a&b\\
b&c
\end{bmatrix},
$$

positive definiteness is equivalent to

$$
a>0
\quad\text{and}\quad
ac-b^2>0.
$$

The second condition is the determinant being positive. These are the leading principal minor conditions in the $2\times2$ case.

Quadratic forms also encode constrained extrema on spheres. If $A$ is symmetric and $\|\mathbf{x}\|=1$, then the Rayleigh quotient

$$
R(\mathbf{x})=\mathbf{x}^TA\mathbf{x}
$$

takes values between the smallest and largest eigenvalues of $A$. The maximum is the largest eigenvalue, achieved at a corresponding unit eigenvector; the minimum is the smallest eigenvalue. This result explains why eigenvalues appear in optimization, mechanics, statistics, and numerical methods.

In applications, a positive definite matrix often represents energy, variance, or squared distance. The positivity condition guarantees that the quantity is genuinely zero only at the zero vector and positive otherwise. Indefinite forms represent saddle geometry: there are directions of increase and directions of decrease through the same point.

## Visual

```mermaid
flowchart LR
  X["original coordinates x"] --> QT["rotate/reflection Q^T"]
  QT --> Y["principal coordinates y"]
  Y --> D["diagonal quadratic form"]
  D --> Z["lambda_1 y_1^2 + ... + lambda_n y_n^2"]
```

ASCII picture of removing a cross term:

```text
xy-coordinate axes             principal axes

      y                              y2
      |      tilted ellipse           |    ellipse aligned
      |    /-----/                    |   -----
------+---/-----/---- x        ------+---------- y1
      |  /-----/                      |   -----
      |
```

## Worked example 1: Diagonalize a quadratic form

Problem: diagonalize

$$
Q(x,y)=5x^2+4xy+2y^2.
$$

Step 1: write the symmetric matrix. Since the cross term is $2bxy$, we have $2b=4$, so $b=2$:

$$
A=
\begin{bmatrix}
5&2\\
2&2
\end{bmatrix}.
$$

Step 2: compute eigenvalues.

$$
\det(A-\lambda I)
=
\det
\begin{bmatrix}
5-\lambda&2\\
2&2-\lambda
\end{bmatrix}
=(5-\lambda)(2-\lambda)-4.
$$

Expand:

$$
(5-\lambda)(2-\lambda)-4
=10-7\lambda+\lambda^2-4
=\lambda^2-7\lambda+6.
$$

Factor:

$$
\lambda^2-7\lambda+6=(\lambda-6)(\lambda-1).
$$

Step 3: find orthogonal eigenvectors. For $\lambda=6$,

$$
A-6I=
\begin{bmatrix}
-1&2\\
2&-4
\end{bmatrix},
$$

so $-x+2y=0$ and an eigenvector is $\begin{bmatrix}2\\1\end{bmatrix}$.

For $\lambda=1$,

$$
A-I=
\begin{bmatrix}
4&2\\
2&1
\end{bmatrix},
$$

so $2x+y=0$ and an eigenvector is $\begin{bmatrix}1\\-2\end{bmatrix}$.

Step 4: normalize:

$$
\mathbf{q}_1=\frac{1}{\sqrt5}\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\mathbf{q}_2=\frac{1}{\sqrt5}\begin{bmatrix}1\\-2\end{bmatrix}.
$$

Then in principal coordinates,

$$
Q=6y_1^2+y_2^2.
$$

Checked answer: both eigenvalues are positive, so the form is positive definite.

## Worked example 2: Classify a critical point with a Hessian

Problem: classify the critical point $(0,0)$ of

$$
f(x,y)=x^2+4xy+y^2.
$$

Step 1: compute the gradient.

$$
f_x=2x+4y,
\qquad
f_y=4x+2y.
$$

At $(0,0)$ both derivatives are zero, so it is a critical point.

Step 2: compute the Hessian.

$$
H=
\begin{bmatrix}
f_{xx}&f_{xy}\\
f_{yx}&f_{yy}
\end{bmatrix}
=
\begin{bmatrix}
2&4\\
4&2
\end{bmatrix}.
$$

Step 3: find eigenvalues.

$$
\det(H-\lambda I)
=
\det
\begin{bmatrix}
2-\lambda&4\\
4&2-\lambda
\end{bmatrix}
=(2-\lambda)^2-16.
$$

Set this equal to zero:

$$
(2-\lambda)^2=16
\quad\Longrightarrow\quad
2-\lambda=\pm4.
$$

Thus $\lambda=-2$ or $\lambda=6$.

Step 4: classify. The Hessian has one positive and one negative eigenvalue, so it is indefinite. Checked answer: $(0,0)$ is a saddle point.

## Code

```python
import numpy as np

A = np.array([[5, 2],
              [2, 2]], dtype=float)

values, Q = np.linalg.eigh(A)
D = np.diag(values)

print(values)
print(Q.T @ A @ Q)
print(np.all(values > 0))
```

`np.linalg.eigh` is specialized for symmetric or Hermitian matrices. It returns real eigenvalues and orthonormal eigenvectors, matching the spectral theorem.

## Common pitfalls

- Forgetting that the matrix of $ax^2+2bxy+cy^2$ has off-diagonal entries $b$, not $2b$.
- Applying the real spectral theorem to a nonsymmetric matrix.
- Assuming diagonalizable automatically means orthogonally diagonalizable. Orthogonal diagonalization is stronger and is guaranteed for real symmetric matrices.
- Classifying definiteness from diagonal entries of $A$ instead of eigenvalues or a valid criterion.
- Ignoring zero eigenvalues when distinguishing positive definite from positive semidefinite.
- Losing the coordinate change: $\mathbf{x}=Q\mathbf{y}$, so the new variables are coordinates in the orthonormal eigenbasis.

A safe classification routine is to start with symmetry. The standard eigenvalue definiteness test applies to symmetric matrices. If the matrix is not symmetric, first rewrite the quadratic form using its symmetric part, because

$$
\mathbf{x}^TA\mathbf{x}
=
\mathbf{x}^T\left(\frac{A+A^T}{2}\right)\mathbf{x}.
$$

The skew-symmetric part contributes nothing to the quadratic form. After the symmetric matrix is identified, use eigenvalues or a valid principal-minor test.

When diagonalizing a quadratic form, keep track of which variables are old and which are new. The equation $\mathbf{x}=Q\mathbf{y}$ means the columns of $Q$ are the new orthonormal axes written in old coordinates. The vector $\mathbf{y}$ contains coordinates along those axes. Losing this distinction can lead to correct eigenvalue arithmetic but wrong geometric interpretation.

The signs of eigenvalues describe the shape. In two variables, two positive eigenvalues give ellipses for level curves $Q=c\gt 0$. One positive and one negative eigenvalue gives hyperbola-like level curves and saddle behavior. A zero eigenvalue creates a flat direction. These pictures are often more memorable than the terminology.

In optimization, positive definite Hessians mean the function curves upward in every direction near the critical point. Negative definite Hessians mean it curves downward in every direction. Indefinite Hessians mean there are both upward and downward directions, so the point is a saddle. This is the multivariable version of the one-variable second derivative test.

Orthogonal changes of coordinates are preferred because they do not distort lengths. If $Q$ is orthogonal, then $\|\mathbf{x}\|=\|\mathbf{y}\|$ when $\mathbf{x}=Q\mathbf{y}$. Thus diagonalizing a quadratic form by an orthogonal matrix rotates or reflects the coordinate system without stretching it. The shape changes its description, not its underlying geometry.

Positive semidefinite forms deserve separate attention. They never take negative values, but they can be zero for nonzero vectors. Geometrically, this means there are flat directions. In statistics, covariance matrices are positive semidefinite because variances cannot be negative, but zero variance can occur in directions with exact linear dependence.

The spectral theorem is also the reason symmetric matrices are central in applications. Energy matrices, covariance matrices, Hessians, and many graph matrices are symmetric. Their orthonormal eigenvectors provide stable axes for analysis, and their real eigenvalues can be ordered and interpreted as curvatures, variances, frequencies, or connectivity measures depending on the model.

A useful final check is to evaluate the quadratic form on eigenvectors. If $A\mathbf{q}_i=\lambda_i\mathbf{q}_i$ and $\|\mathbf{q}_i\|=1$, then

$$
\mathbf{q}_i^TA\mathbf{q}_i=\lambda_i.
$$

So eigenvalues are the values of the quadratic form on its principal unit directions.

That sentence is often the simplest interpretation of the spectral theorem for quadratic forms.

## Connections

- [Eigenvalues and Eigenvectors](/math/linear-algebra/eigenvalues-and-eigenvectors)
- [Diagonalization and Similarity](/math/linear-algebra/diagonalization-and-similarity)
- [Orthogonality in Rn](/math/linear-algebra/orthogonality-in-rn)
- [Singular Value Decomposition](/math/linear-algebra/singular-value-decomposition)
