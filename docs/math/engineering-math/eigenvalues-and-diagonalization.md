---
title: Eigenvalues and Diagonalization
sidebar_position: 12
---

# Eigenvalues and Diagonalization

Most vectors change both length and direction under a linear transformation. Eigenvectors are the exceptional directions that stay on their own lines. Diagonalization asks whether these invariant directions form a basis; if they do, a coupled matrix action becomes independent scalar multiplication in eigenvector coordinates.

## From invariant directions to the characteristic equation

An eigenpair of a square matrix $A$ satisfies

$$
A\mathbf v=\lambda\mathbf v,
\qquad \mathbf v\ne\mathbf0.
$$

The scalar $\lambda$ may be positive, negative, zero, or complex. Over the reals, a positive value preserves direction and a negative value reverses it. A zero eigenvalue means a nonzero vector is sent to zero, so $A$ is singular.

Rearrange the equation:

$$
(A-\lambda I)\mathbf v=\mathbf0.
$$

A nonzero solution exists exactly when $A-\lambda I$ has a nontrivial nullspace, equivalently when it is singular. Therefore eigenvalues are roots of the characteristic polynomial

$$
p_A(\lambda)=\det(A-\lambda I).
$$

Some texts use $\det(\lambda I-A)$ instead. The two conventions differ by $(-1)^n$ for an $n\times n$ matrix and have the same roots.

The multiplicity of $\lambda$ as a root of $p_A$ is its algebraic multiplicity. The dimension

$$
\dim\ker(A-\lambda I)
$$

is its geometric multiplicity. For each eigenvalue,

$$
1\le\text{geometric multiplicity}
\le\text{algebraic multiplicity}.
$$

The right inequality measures a possible shortage of eigenvectors. Distinct eigenvalues always have linearly independent eigenvectors, so $n$ distinct eigenvalues guarantee diagonalizability.

Trace and determinant supply checks once the eigenvalues are known, counted with algebraic multiplicity over $\mathbb C$:

$$
\operatorname{tr}(A)=\sum_{j=1}^n\lambda_j,
\qquad
\det(A)=\prod_{j=1}^n\lambda_j.
$$

They do not by themselves determine eigenvectors or decide diagonalizability.

## Diagonalization is a change of coordinates

Suppose $A$ has a basis of eigenvectors $\mathbf v_1,\ldots,\mathbf v_n$, with corresponding eigenvalues $\lambda_1,\ldots,\lambda_n$. Put the eigenvectors in the columns of

$$
P=\begin{bmatrix}\mathbf v_1&\cdots&\mathbf v_n\end{bmatrix}
$$

and put matching eigenvalues on the diagonal of

$$
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$

The $j$th column of $AP$ is $A\mathbf v_j=\lambda_j\mathbf v_j$, which is the $j$th column of $PD$. Hence

$$
AP=PD.
$$

Since the eigenvectors form a basis, $P$ is invertible, and

$$
A=PDP^{-1},
\qquad
D=P^{-1}AP.
$$

The matrix $P^{-1}$ converts ordinary coordinates to eigenvector coordinates. The diagonal matrix $D$ acts there by scaling each coordinate independently. Finally, $P$ converts back. Similar matrices represent the same linear map in different bases and share characteristic polynomial, determinant, trace, and eigenvalues.

The ordering must stay aligned: swapping two columns of $P$ requires swapping the same two diagonal entries of $D$. The identity $AP=PD$ is usually the quickest check and avoids explicitly multiplying by $P^{-1}$.

```mermaid
flowchart LR
  X["ordinary coordinates x"] -->|"P^-1"| C["eigenvector coordinates c"]
  C -->|"D: independent scaling"| DC["scaled coordinates Dc"]
  DC -->|P| AX["transformed vector Ax"]
```

## Worked example: diagonalize and compute a power

Let

$$
A=
\begin{bmatrix}
4&1\\
2&3
\end{bmatrix}.
$$

First find the characteristic polynomial:

$$
\begin{aligned}
\det(A-\lambda I)
&=(4-\lambda)(3-\lambda)-2\\
&=\lambda^2-7\lambda+10\\
&=(\lambda-5)(\lambda-2).
\end{aligned}
$$

For $\lambda=5$,

$$
A-5I=
\begin{bmatrix}
-1&1\\
2&-2
\end{bmatrix},
$$

so $-v_1+v_2=0$. Choose

$$
\mathbf v_1=\begin{bmatrix}1\\1\end{bmatrix}.
$$

For $\lambda=2$,

$$
A-2I=
\begin{bmatrix}
2&1\\
2&1
\end{bmatrix},
$$

so $2v_1+v_2=0$. Choose

$$
\mathbf v_2=\begin{bmatrix}1\\-2\end{bmatrix}.
$$

Thus

$$
P=
\begin{bmatrix}
1&1\\
1&-2
\end{bmatrix},
\qquad
D=
\begin{bmatrix}
5&0\\
0&2
\end{bmatrix}.
$$

The inverse is

$$
P^{-1}=\frac{1}{-3}
\begin{bmatrix}
-2&-1\\
-1&1
\end{bmatrix}
=\frac13
\begin{bmatrix}
2&1\\
1&-1
\end{bmatrix}.
$$

To compute $A^k$, use cancellation of adjacent factors:

$$
A^k=(PDP^{-1})^k=PD^kP^{-1}.
$$

Since

$$
D^k=
\begin{bmatrix}
5^k&0\\
0&2^k
\end{bmatrix},
$$

multiplication gives

$$
A^k=\frac13
\begin{bmatrix}
2\cdot5^k+2^k&5^k-2^k\\
2\cdot5^k-2^{k+1}&5^k+2^{k+1}
\end{bmatrix}.
$$

At $k=1$, this reduces to the original matrix, which checks the algebra. For large $k$, the $5^k$ mode dominates unless the initial vector has zero component along $\mathbf v_1$.

## Repeated eigenvalues and defective matrices

A repeated eigenvalue does not automatically prevent diagonalization. The identity matrix has one eigenvalue of algebraic multiplicity $n$, and every nonzero vector is an eigenvector. The eigenspace dimension must be computed.

Consider

$$
J=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}.
$$

Because $J$ is triangular, its only eigenvalue is $1$, with algebraic multiplicity $2$. But

$$
J-I=
\begin{bmatrix}
0&1\\
0&0
\end{bmatrix}
$$

forces the second component of every eigenvector to be zero. The eigenspace is

$$
\operatorname{span}\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\},
$$

which has dimension $1$. There is no eigenvector basis, so $J$ is defective and cannot be diagonalized.

Write $J=I+N$, where

$$
N=
\begin{bmatrix}0&1\\0&0\end{bmatrix},
\qquad N^2=0.
$$

The binomial theorem now gives a useful substitute:

$$
J^k=(I+N)^k=I+kN
=\begin{bmatrix}1&k\\0&1\end{bmatrix}.
$$

The factor $k$ is the discrete signature of the missing eigenvector. For the matrix exponential,

$$
e^{Jt}=e^{(I+N)t}=e^t(I+tN)
=e^t
\begin{bmatrix}1&t\\0&1\end{bmatrix}.
$$

Generalized eigenvectors and Jordan chains systematize this structure. In numerical work, however, explicit Jordan form is highly sensitive and is rarely the preferred computational representation.

## Deciding diagonalizability without guessing a basis

An $n\times n$ matrix is diagonalizable over a chosen field exactly when the dimensions of all its eigenspaces add to $n$. Equivalently, for every eigenvalue, geometric multiplicity must equal algebraic multiplicity. The field matters: a real rotation through $90^\circ$ is not diagonalizable over $\mathbb R$ because it has no real eigenvalues, but over $\mathbb C$ it has the distinct eigenvalues $i$ and $-i$ and is diagonalizable.

Several sufficient conditions are useful:

| Condition | Consequence |
|---|---|
| $n$ distinct eigenvalues | diagonalizable |
| real symmetric matrix | orthogonally diagonalizable over $\mathbb R$ |
| triangular with distinct diagonal entries | diagonalizable |
| $A^2=A$ | diagonalizable, with eigenvalues only $0$ and $1$ |

The projection case $A^2=A$ follows directly. If $A\mathbf v=\lambda\mathbf v$, then $A^2\mathbf v=\lambda^2\mathbf v$ but also $A^2\mathbf v=A\mathbf v=\lambda\mathbf v$, so $\lambda(\lambda-1)=0$. More strongly, every vector splits as

$$
\mathbf x=A\mathbf x+(\mathbf x-A\mathbf x).
$$

The first term lies in the eigenvalue-$1$ subspace, and applying $A$ to the second gives zero. Thus the two eigenspaces span the whole space.

The minimal polynomial gives another exact criterion: a matrix is diagonalizable precisely when its minimal polynomial splits into distinct linear factors. A repeated factor records a nontrivial Jordan block. This viewpoint avoids confusing repeated characteristic roots with automatic failure; only repeated factors required by the matrix action matter.

Simple transformations preserve eigenvectors when defined. If $A\mathbf v=\lambda\mathbf v$, then

$$
(A+cI)\mathbf v=(\lambda+c)\mathbf v,
$$

and, when $A$ is invertible,

$$
A^{-1}\mathbf v=\lambda^{-1}\mathbf v.
$$

Polynomial functions satisfy $p(A)\mathbf v=p(\lambda)\mathbf v$. These identities explain spectral shifting in numerical algorithms and let many matrix expressions be understood without recomputing their eigenvectors.

## Matrix functions and dynamical systems

If $A=PDP^{-1}$ and a scalar function is defined on its eigenvalues, then

$$
g(A)=Pg(D)P^{-1}.
$$

For powers, $g(\lambda)=\lambda^k$; for linear differential systems, $g(\lambda)=e^{\lambda t}$:

$$
e^{At}=Pe^{Dt}P^{-1},
\qquad
e^{Dt}=\operatorname{diag}(e^{\lambda_1t},\ldots,e^{\lambda_nt}).
$$

In $\mathbf x'=A\mathbf x$, a real negative eigenvalue gives exponential decay along its eigenvector, while a positive one gives growth. A complex conjugate pair $\alpha\pm i\beta$ produces oscillation or rotation under an envelope $e^{\alpha t}$. Defective blocks add polynomial factors such as $te^{\lambda t}$.

For a discrete system $\mathbf x_{k+1}=A\mathbf x_k$, magnitudes $\vert \lambda\vert \lt 1$ decay, $\vert \lambda\vert \gt 1$ grow, and values on the unit circle require closer inspection. A defective eigenvalue with $\vert \lambda\vert =1$ can still cause polynomial growth.

## Symmetric matrices have an orthogonal eigenbasis

The spectral theorem strengthens diagonalization for a real symmetric matrix:

$$
A=QDQ^T,
$$

where $Q$ is orthogonal and $D$ is real diagonal. Eigenvalues are real, and eigenvectors belonging to distinct eigenvalues are orthogonal. Within a repeated eigenspace, an orthonormal basis can be chosen.

Orthogonal changes of coordinates preserve lengths and angles, and $Q^{-1}=Q^T$. They are also well conditioned numerically. For the quadratic form $\mathbf x^TA\mathbf x$, set $\mathbf x=Q\mathbf z$:

$$
\mathbf x^TA\mathbf x
=\mathbf z^TD\mathbf z
=\lambda_1z_1^2+\cdots+\lambda_nz_n^2.
$$

All positive eigenvalues make the form positive definite; mixed signs make it indefinite. This criterion appears in optimization, energy stability, principal axes, and covariance analysis.

The theorem does not extend unchanged to arbitrary real matrices. A rotation through a nonzero angle other than $\pi$ has no real eigenvectors, although it has complex eigenvalues. Normal and Hermitian matrices have related unitary spectral theorems over $\mathbb C$.

## Worked example: orthogonal diagonalization

Take

$$
S=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}.
$$

The characteristic polynomial is

$$
(2-\lambda)^2-1
=(\lambda-3)(\lambda-1).
$$

For $\lambda=3$, an eigenvector is $[1,1]^T$; for $\lambda=1$, one is $[1,-1]^T$. They are already orthogonal. Normalize them:

$$
\mathbf q_1=\frac1{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf q_2=\frac1{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Then

$$
Q=\frac1{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix},
\qquad
D=
\begin{bmatrix}3&0\\0&1\end{bmatrix},
$$

and $S=QDQ^T$. Consequently,

$$
\begin{bmatrix}x&y\end{bmatrix}
S
\begin{bmatrix}x\\y\end{bmatrix}
=3z_1^2+z_2^2,
$$

where $\mathbf z=Q^T\mathbf x$. Both coefficients are positive, so the quadratic form is positive definite.

## Numerical eigenpairs and conditioning

For large matrices, explicitly expanding a determinant is a poor numerical algorithm. Stable library routines use reductions and iterative methods. Symmetric or Hermitian structure should be passed to a specialized solver, which returns real eigenvalues and an orthonormal eigenbasis.

```python
import numpy as np

A = np.array([[4.0, 1.0],
              [2.0, 3.0]])
values, vectors = np.linalg.eig(A)

residual = A @ vectors - vectors @ np.diag(values)
print(values)
print(np.linalg.norm(residual))
print(np.linalg.cond(vectors))
```

The residual checks whether the computed columns satisfy $A\mathbf v\approx\lambda\mathbf v$. The condition number of the eigenvector matrix warns how strongly errors may be amplified by the coordinate change. A matrix can be diagonalizable in exact algebra yet have a nearly singular eigenvector matrix, making its eigenpairs sensitive to perturbations.

For a real symmetric matrix, `numpy.linalg.eigh` is preferable. Approximate eigenvectors also have arbitrary scale and sign, and complex eigenvectors have arbitrary phase. Tests should compare invariant equations or subspaces rather than raw vector entries.

Common bookkeeping errors have clear checks:

- The zero vector never qualifies as an eigenvector.
- Algebraic multiplicity alone does not count independent directions; compute each nullspace.
- Eigenvalue order and eigenvector-column order must match.
- Real matrices may require complex eigenpairs.
- A small residual supports a computed pair, while a large basis condition number still signals sensitivity.
- Diagonalization simplifies a matrix only after the cost and stability of the basis change are considered.

## Spectral information without full diagonalization

Many questions need only part of the spectrum. Singularity is equivalent to zero being an eigenvalue. Stability may depend only on the eigenvalue with largest real part or largest modulus. A determinant gives the product and a trace gives the sum, which can reject an incorrect list quickly but cannot reconstruct a reliable list for a large matrix.

Triangular matrices expose eigenvalues on the diagonal because their characteristic determinant is the product of diagonal terms. Their eigenvectors still require solving nullspaces, and a triangular matrix can be defective. Block triangular matrices similarly have the union of the eigenvalues of their diagonal blocks, allowing a large problem to be divided before any eigenvector calculation.

The spectral radius is the largest eigenvalue modulus. It controls the asymptotic scale of matrix powers, but norms and transient behavior may differ greatly when the matrix is nonnormal. A matrix can have all eigenvalues inside the unit disk and still amplify some vectors for several steps before eventual decay. Eigenvalues describe invariant directions and long-term modes; they do not bound every short-term action by themselves.

Left eigenvectors satisfy a transposed equation and are useful when a matrix is not symmetric. They provide coordinates dual to right eigenvectors and appear in sensitivity formulas. For a diagonalizable nonnormal matrix, right eigenvectors need not be orthogonal, so extracting modal coefficients requires the inverse eigenvector matrix rather than ordinary dot products.

## Scaling, signs, and complex pairs

An eigenvector has no preferred scale. Multiplying it by any nonzero scalar gives the same invariant line. Numerical software may normalize vectors to length one, but their signs remain arbitrary. For complex vectors, any unit complex phase is arbitrary. Comparisons should therefore use residuals, angles between subspaces, or phase-aligned vectors.

Real matrices with nonreal eigenvalues produce conjugate pairs. Their complex eigenvectors also pair by conjugation. Real solutions of a differential system are obtained by combining the real and imaginary parts of a complex mode. The result is a two-dimensional invariant plane on which the action combines scaling with rotation. Treating one complex eigenvector as a physical real direction loses this geometry.

Repeated eigenvalues make individual eigenvectors especially nonunique. Even for a symmetric matrix, any orthonormal basis of a repeated eigenspace is valid. Small perturbations can rotate the reported basis dramatically while leaving the eigenspace stable. Comparing subspaces is then more meaningful than comparing columns.

## Modal coordinates in applications

In a coupled vibration model, the original coordinates may be displacements of physical components. Eigenvectors give mode shapes: patterns in which all components oscillate with a common frequency ratio. Expressing an initial displacement as a combination of modes lets each modal amplitude evolve independently when the system has the required symmetric structure.

For a Markov transition matrix, conventions determine whether probability vectors multiply on the left or right. The stationary distribution belongs to the eigenvalue one on the appropriate side. Other eigenvalues describe decay of deviations only under additional assumptions such as irreducibility and aperiodicity. The existence of eigenvalue one alone does not guarantee convergence from every initial distribution.

In recurrence relations, diagonalization converts a vector recurrence into scalar geometric sequences. A dominant eigenvalue explains leading growth, while equal dominant moduli can preserve oscillation. If the initial state has no component in the dominant eigenspace, the next mode controls the outcome; stating dominance without checking modal coefficients can therefore be misleading.

Principal-axis problems use the symmetric case. Orthogonal eigenvectors identify mutually perpendicular directions with no cross terms. The sign and magnitude of eigenvalues then describe curvature, energy, or variance along those axes. The orthogonality is a consequence of symmetry, not a general property of eigenvectors.

## Perturbations and numerical meaning

Computed eigenvalues solve a nearby problem, and their usefulness depends on sensitivity. Symmetric matrices have well-behaved orthogonal eigenvectors and real eigenvalues whose perturbations can be bounded directly by the matrix perturbation norm. Nonnormal matrices may have eigenvalues that move much farther under a small change.

A tiny eigenpair residual says the displayed pair nearly satisfies the equation. It does not by itself say the eigenvalue is close to a unique exact eigenvalue when the problem is ill conditioned. Reporting residuals together with structural information and condition estimates gives a more honest numerical result.

Forming an inverse eigenvector matrix explicitly is seldom necessary. Linear solves with the eigenvector matrix are more stable and cheaper. Likewise, computing a high power through repeated dense multiplication may be inferior to applying a decomposition or a dedicated matrix-function algorithm. The algebraic identity guides the method, but reliable software should exploit matrix structure rather than reproduce hand formulas literally.

<div className="see-also">

See also: [Matrices and linear systems](/math/engineering-math/matrices-and-linear-systems) · [Systems of ODEs and phase planes](/math/engineering-math/systems-of-odes-and-phase-plane) · [Second-order linear ODEs](/math/engineering-math/second-order-linear-odes) · [Numerical methods overview](/math/engineering-math/numerical-methods-overview)

</div>
