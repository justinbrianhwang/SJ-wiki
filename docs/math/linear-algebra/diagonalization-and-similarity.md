---
title: Diagonalization and Similarity
sidebar_position: 12
---

# Diagonalization and Similarity

Diagonalization changes coordinates so that a linear transformation becomes simple. A diagonal matrix acts independently on coordinate axes; a diagonalizable matrix acts independently along eigenvector directions. Similarity formalizes the idea that two matrices can describe the same linear transformation in different bases.

![An eigenvector keeps its direction while a matrix scales it.](https://commons.wikimedia.org/wiki/Special:FilePath/Eigenvalue_equation.svg)

*Figure: The eigenvalue equation captures directions preserved by a linear transformation. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Eigenvalue_equation.svg), Lyudmil Antonov, CC BY-SA 4.0.*

This is where eigenvectors become computationally powerful. If a matrix can be written as $A=PDP^{-1}$, then powers, recurrences, and many qualitative questions reduce to the diagonal entries of $D$. The matrix $P$ changes from eigenvector coordinates to standard coordinates, while $P^{-1}$ changes back.

## Definitions

Square matrices $A$ and $B$ are similar if there is an invertible matrix $P$ such that

$$
B=P^{-1}AP.
$$

A matrix $A$ is diagonalizable if it is similar to a diagonal matrix:

$$
P^{-1}AP=D.
$$

Equivalently,

$$
A=PDP^{-1}.
$$

The columns of $P$ are usually chosen to be eigenvectors of $A$, and the corresponding diagonal entries of $D$ are their eigenvalues.

The algebraic multiplicity of an eigenvalue is its multiplicity as a root of the characteristic polynomial. The geometric multiplicity is the dimension of its eigenspace.

Similarity is an equivalence relation: $A$ is similar to itself, similarity is symmetric, and similarity is transitive. Similar matrices represent the same linear map in different bases.

## Key results

An $n\times n$ matrix $A$ is diagonalizable if and only if it has $n$ linearly independent eigenvectors. If $P=[\mathbf{v}_1\ \cdots\ \mathbf{v}_n]$ and $A\mathbf{v}_i=\lambda_i\mathbf{v}_i$, then

$$
AP=
\begin{bmatrix}
A\mathbf{v}_1&\cdots&A\mathbf{v}_n
\end{bmatrix}
=
\begin{bmatrix}
\lambda_1\mathbf{v}_1&\cdots&\lambda_n\mathbf{v}_n
\end{bmatrix}
=PD.
$$

Multiplying by $P^{-1}$ gives $P^{-1}AP=D$.

If an $n\times n$ matrix has $n$ distinct eigenvalues, then it is diagonalizable, because eigenvectors corresponding to distinct eigenvalues are linearly independent. The converse is false: a diagonalizable matrix can have repeated eigenvalues as long as the eigenspaces are large enough.

For each eigenvalue,

$$
1\leq \text{geometric multiplicity}\leq \text{algebraic multiplicity}.
$$

A matrix is diagonalizable exactly when the sum of the geometric multiplicities of its eigenvalues is $n$.

If $A=PDP^{-1}$, then powers are easy:

$$
A^k=PD^kP^{-1}.
$$

This works because the middle factors cancel:

$$
A^2=(PDP^{-1})(PDP^{-1})=PD^2P^{-1}.
$$

The same cancellation repeats for higher powers.

Similarity preserves the characteristic polynomial. If $B=P^{-1}AP$, then

$$
\det(\lambda I-B)
=
\det(\lambda I-P^{-1}AP)
=
\det(P^{-1}(\lambda I-A)P).
$$

Using multiplicativity of determinants gives

$$
\det(P^{-1})\det(\lambda I-A)\det(P)=\det(\lambda I-A),
$$

because $\det(P^{-1})\det(P)=1$. Therefore similar matrices have the same eigenvalues, determinant, and trace. They may look different entry by entry, but their coordinate-independent spectral information is the same.

Diagonalization is best understood as an eigenbasis test. The standard basis vectors are ideal for a diagonal matrix because each one is an eigenvector. A diagonalizable matrix is one whose action becomes diagonal after choosing a better basis. In that basis, the first coordinate evolves independently from the second, the second independently from the third, and so on. Coupled equations become uncoupled scalar equations.

Not every failure of diagonalization is caused by missing eigenvalues. A matrix can have all eigenvalues real and still lack enough independent eigenvectors. The matrix

$$
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
$$

has only the eigenvalue $1$, and its eigenspace is one-dimensional. Since a $2\times2$ matrix needs two independent eigenvectors to be diagonalizable, it fails the test. This kind of example is the reason geometric multiplicity matters.

When diagonalization is available, it is especially effective for discrete dynamical systems. If $\mathbf{x}_{k+1}=A\mathbf{x}_k$ and $A=PDP^{-1}$, then

$$
\mathbf{x}_k=A^k\mathbf{x}_0=PD^kP^{-1}\mathbf{x}_0.
$$

The entries of $D^k$ are powers of eigenvalues. Large absolute eigenvalues dominate long-term behavior, eigenvalues with absolute value less than one decay, and negative eigenvalues alternate signs. This is the bridge from algebraic factorization to qualitative dynamics.

## Visual

```mermaid
flowchart LR
  X["standard coordinates"] --> PInv["P inverse: eigenvector coordinates"]
  PInv --> D["D: scale each coordinate by eigenvalue"]
  D --> P["P: return to standard coordinates"]
  P --> Y["A x"]
```

| Property | Similar matrices | Diagonalizable matrices |
|---|---|---|
| Definition | $B=P^{-1}AP$ | $P^{-1}AP=D$ diagonal |
| Preserves eigenvalues | yes | yes |
| Preserves determinant and trace | yes | yes |
| Requires eigenbasis | no | yes |
| Main use | change coordinates | compute powers and decouple dynamics |

## Worked example 1: Diagonalize a 2 by 2 matrix

Problem: diagonalize

$$
A=
\begin{bmatrix}
4&1\\
2&3
\end{bmatrix}.
$$

Step 1: use the eigenpairs from the eigenvalue computation:

$$
\lambda_1=5,\quad \mathbf{v}_1=\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\lambda_2=2,\quad \mathbf{v}_2=\begin{bmatrix}1\\-2\end{bmatrix}.
$$

Step 2: build $P$ from the eigenvectors and $D$ from the matching eigenvalues:

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

Step 3: compute $P^{-1}$. Since $\det(P)=-3$,

$$
P^{-1}
=
\frac{1}{-3}
\begin{bmatrix}
-2&-1\\
-1&1
\end{bmatrix}
=
\begin{bmatrix}
2/3&1/3\\
1/3&-1/3
\end{bmatrix}.
$$

Step 4: verify $A=PDP^{-1}$. First compute

$$
PD=
\begin{bmatrix}
1&1\\
1&-2
\end{bmatrix}
\begin{bmatrix}
5&0\\
0&2
\end{bmatrix}
=
\begin{bmatrix}
5&2\\
5&-4
\end{bmatrix}.
$$

Then

$$
PDP^{-1}
=
\begin{bmatrix}
5&2\\
5&-4
\end{bmatrix}
\begin{bmatrix}
2/3&1/3\\
1/3&-1/3
\end{bmatrix}
=
\begin{bmatrix}
4&1\\
2&3
\end{bmatrix}.
$$

Checked answer: $A=PDP^{-1}$.

## Worked example 2: Use diagonalization to compute a power

Problem: compute $A^3$ for the same matrix.

Step 1: use

$$
A^3=PD^3P^{-1}.
$$

Step 2: cube the diagonal matrix entrywise:

$$
D^3=
\begin{bmatrix}
5^3&0\\
0&2^3
\end{bmatrix}
=
\begin{bmatrix}
125&0\\
0&8
\end{bmatrix}.
$$

Step 3: multiply.

$$
PD^3=
\begin{bmatrix}
1&1\\
1&-2
\end{bmatrix}
\begin{bmatrix}
125&0\\
0&8
\end{bmatrix}
=
\begin{bmatrix}
125&8\\
125&-16
\end{bmatrix}.
$$

Now

$$
PD^3P^{-1}
=
\begin{bmatrix}
125&8\\
125&-16
\end{bmatrix}
\begin{bmatrix}
2/3&1/3\\
1/3&-1/3
\end{bmatrix}
=
\begin{bmatrix}
86&39\\
78&47
\end{bmatrix}.
$$

Step 4: check by repeated multiplication. $A^2=\begin{bmatrix}18&7\\14&11\end{bmatrix}$, and

$$
A^3=A^2A=
\begin{bmatrix}
18&7\\
14&11
\end{bmatrix}
\begin{bmatrix}
4&1\\
2&3
\end{bmatrix}
=
\begin{bmatrix}
86&39\\
78&47
\end{bmatrix}.
$$

Checked answer: $A^3=\begin{bmatrix}86&39\\78&47\end{bmatrix}$.

## Code

```python
import numpy as np

A = np.array([[4, 1],
              [2, 3]], dtype=float)

values, P = np.linalg.eig(A)
D = np.diag(values)
A_rebuilt = P @ D @ np.linalg.inv(P)

print(values)
print(A_rebuilt)
print(np.linalg.matrix_power(A, 3))
print(P @ np.linalg.matrix_power(D, 3) @ np.linalg.inv(P))
```

Numerical eigensolvers may return eigenvectors scaled differently or ordered differently. The diagonalization is valid as long as the columns of $P$ match the corresponding diagonal entries of $D$.

## Common pitfalls

- Putting eigenvalues in $D$ in an order that does not match the eigenvectors in $P$.
- Assuming a repeated eigenvalue automatically prevents diagonalization. It depends on eigenspace dimension.
- Assuming every matrix is diagonalizable. Some matrices do not have enough independent eigenvectors.
- Confusing $P^{-1}AP=D$ with $PAP^{-1}=D$. The basis-change order matters.
- Forgetting that similar matrices are the same size.
- Computing powers as $P^kD^k(P^{-1})^k$. The cancellation gives $PD^kP^{-1}$, not that expression.

The most important diagnostic for diagonalization is the eigenvector count. After finding each eigenspace, add their dimensions. If the total is $n$ for an $n\times n$ matrix, the matrix is diagonalizable. If the total is less than $n$, it is not. Distinct eigenvalues are a convenient sufficient condition, but they are not the definition.

When constructing $P$, order is bookkeeping. If the first column of $P$ is an eigenvector for $\lambda=5$, then the first diagonal entry of $D$ must be $5$. If the second column is an eigenvector for $\lambda=2$, the second diagonal entry must be $2$. Many incorrect diagonalizations come from correct eigenvectors and correct eigenvalues placed in mismatched order.

Similarity should be read as a change of coordinates, not as an arbitrary algebraic trick. The matrix $P^{-1}$ converts a standard-coordinate input into coordinates in the new basis. The diagonal matrix $D$ performs the simple action in that basis. The matrix $P$ converts the result back. This interpretation makes the formula $A=PDP^{-1}$ natural.

Diagonalization is powerful but not always numerically ideal. If the eigenvector matrix $P$ is poorly conditioned, computations using $PDP^{-1}$ may amplify rounding error. Orthogonal diagonalization for symmetric matrices avoids this issue because orthogonal matrices preserve lengths and have condition number $1$ in the Euclidean norm. This is one reason symmetric eigenvalue problems are especially well behaved.

A diagonal form also makes invariant subspaces visible. Each coordinate axis in the diagonal basis is preserved by the transformation. If several eigenvectors correspond to the same eigenvalue, every vector in their eigenspace is preserved as a direction up to the same scaling. This explains why repeated eigenvalues can still be harmless when their eigenspaces are large enough.

Similarity is not the same as row equivalence. Row-equivalent matrices arise from left multiplication by elementary matrices and generally do not have the same eigenvalues. Similar matrices involve both $P^{-1}$ and $P$, representing a change of basis in the same space, and they preserve spectral data. Confusing these two equivalence notions leads to incorrect eigenvalue arguments.

When a matrix is not diagonalizable, one can still study it through other forms, such as Jordan form in more advanced courses or Schur form in numerical work. The introductory lesson is simpler: diagonalization is a powerful special case, and the test is the existence of an eigenbasis.

A good final verification is to multiply $AP$ and $PD$. If the columns of $P$ are correctly matched with the diagonal entries of $D$, these two products are equal. This avoids computing $P^{-1}$ just to check the eigenvector pairing.

This check catches most ordering mistakes.

## Connections

- [Eigenvalues and Eigenvectors](/math/linear-algebra/eigenvalues-and-eigenvectors)
- [Matrix Inverses and Elementary Matrices](/math/linear-algebra/matrix-inverses-and-elementary-matrices)
- [Quadratic Forms and Spectral Theorems](/math/linear-algebra/quadratic-forms-and-spectral-theorems)
- [Singular Value Decomposition](/math/linear-algebra/singular-value-decomposition)
