---
title: Matrix Factorizations and Special Systems
sidebar_position: 16
---

# Matrix Factorizations and Special Systems

General Gaussian elimination is a powerful default, but many matrices have structure that should not be ignored. Symmetric positive definite matrices, tridiagonal matrices, banded matrices, and orthogonal factorizations all allow algorithms that are faster, more stable, or more memory efficient than treating the matrix as dense and unstructured.

The main numerical lesson is to let the matrix structure choose the solver. A direct method that respects symmetry or bandwidth can reduce both arithmetic and roundoff. This page focuses on Cholesky factorization for symmetric positive definite systems and the Thomas algorithm for tridiagonal systems, with QR noted as the stable workhorse for least squares.

## Definitions

A matrix $A$ is **symmetric positive definite** (SPD) if

$$
A=A^T
\quad \text{and} \quad
x^TAx\gt 0 \text{ for every nonzero }x.
$$

An SPD matrix has a Cholesky factorization

$$
A=LL^T,
$$

where $L$ is lower triangular with positive diagonal entries. Cholesky uses about half the work and storage of a general LU factorization.

A **tridiagonal matrix** has nonzero entries only on the main diagonal, first subdiagonal, and first superdiagonal. It can be written through three arrays:

$$
a_i x_{i-1}+b_i x_i+c_i x_{i+1}=d_i.
$$

The Thomas algorithm is specialized Gaussian elimination for tridiagonal systems.

A QR factorization writes

$$
A=QR,
$$

where $Q$ has orthonormal columns and $R$ is upper triangular. QR is especially important for least squares because orthogonal transformations preserve norms.

## Key results

Cholesky exists and is unique for SPD matrices when the diagonal of $L$ is required to be positive. The factorization is stable without pivoting for SPD matrices, which is one reason SPD structure is so valuable. In contrast, applying ordinary LU without recognizing symmetry can waste work and lose a useful diagnostic: a nonpositive Cholesky pivot indicates that the matrix is not SPD in working precision.

For a dense $n\times n$ matrix, Cholesky costs about $n^3/3$ floating-point operations, compared with about $2n^3/3$ for LU. For a tridiagonal system, the Thomas algorithm costs only $O(n)$ operations and stores only three diagonals. This difference is decisive in boundary value problems and finite difference PDEs, where tridiagonal or banded matrices occur naturally.

QR factorization is more expensive than normal equations for least squares, but it avoids squaring the condition number. If $A$ is ill-conditioned, solving $A^TAx=A^Tb$ can lose many digits, while Householder QR gives a more stable path.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For matrix factorizations and special systems, the input record should include symmetry, definiteness, bandwidth, sparsity pattern, and right-hand-side count. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include factor residuals, solve residuals, pivot or Cholesky diagnostics, and structure preservation. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually storage, fill-in, and arithmetic cost compared with dense LU. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: using the wrong factorization, destroying sparsity, and ignoring condition estimates. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

## Visual

```text
Tridiagonal structure stores only three diagonals.

[ b0 c0  0  0 ]
[ a1 b1 c1  0 ]
[  0 a2 b2 c2 ]
[  0  0 a3 b3 ]
```

| Structure | Factorization or algorithm | Cost | Typical source |
|---|---|---:|---|
| SPD dense | Cholesky $A=LL^T$ | about $n^3/3$ | normal modes, covariance, energy systems |
| Tridiagonal | Thomas algorithm | $O(n)$ | 1D finite differences, splines |
| Banded | banded LU or Cholesky | depends on bandwidth | PDE grids, local coupling |
| Tall rectangular | QR | $O(mn^2)$ | least squares |

## Worked example 1: Cholesky factorization

**Problem.** Factor

$$
A=\begin{bmatrix}4&2\\2&3\end{bmatrix}
$$

as $A=LL^T$.

**Method.** Let

$$
L=\begin{bmatrix}\ell_{11}&0\\\ell_{21}&\ell_{22}\end{bmatrix}.
$$

1. From the $(1,1)$ entry:

$$
\ell_{11}^2=4 \Rightarrow \ell_{11}=2.
$$

2. From the $(2,1)$ entry:

$$
\ell_{21}\ell_{11}=2 \Rightarrow \ell_{21}=1.
$$

3. From the $(2,2)$ entry:

$$
\ell_{21}^2+\ell_{22}^2=3
\Rightarrow
1+\ell_{22}^2=3.
$$

Thus $\ell_{22}=\sqrt{2}$.

**Checked answer.**

$$
L=\begin{bmatrix}2&0\\1&\sqrt{2}\end{bmatrix},
\qquad
LL^T=\begin{bmatrix}4&2\\2&3\end{bmatrix}.
$$

## Worked example 2: tridiagonal solve

**Problem.** Solve

$$
\begin{bmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}1\\0\\1\end{bmatrix}.
$$

**Method.** Use the equations directly to verify the tridiagonal solution.

1. The system is

$$
2x_1-x_2=1,
$$

$$
-x_1+2x_2-x_3=0,
$$

$$
-x_2+2x_3=1.
$$

2. Symmetry of the right-hand side suggests $x_1=x_3$.

3. Let $x_1=x_3=s$. The middle equation gives

$$
-s+2x_2-s=0 \Rightarrow x_2=s.
$$

4. The first equation gives

$$
2s-s=1 \Rightarrow s=1.
$$

**Checked answer.** The solution is $(1,1,1)^T$. A Thomas algorithm would find the same solution in linear time for larger tridiagonal systems.

## Code

```python
import numpy as np

def cholesky_lower(A):
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    L = np.zeros_like(A)
    for i in range(n):
        for j in range(i + 1):
            s = np.dot(L[i, :j], L[j, :j])
            if i == j:
                value = A[i, i] - s
                if value <= 0:
                    raise np.linalg.LinAlgError("matrix is not positive definite")
                L[i, j] = np.sqrt(value)
            else:
                L[i, j] = (A[i, j] - s) / L[j, j]
    return L

def thomas(a, b, c, d):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)
    d = np.array(d, dtype=float)
    n = len(b)
    for i in range(1, n):
        m = a[i - 1] / b[i - 1]
        b[i] -= m * c[i - 1]
        d[i] -= m * d[i - 1]
    x = np.zeros(n)
    x[-1] = d[-1] / b[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
    return x

A = np.array([[4.0, 2.0], [2.0, 3.0]])
print(cholesky_lower(A))
print(thomas([-1.0, -1.0], [2.0, 2.0, 2.0], [-1.0, -1.0], [1.0, 0.0, 1.0]))
```

## Common pitfalls

- Running Cholesky on a matrix that is symmetric but not positive definite.
- Destroying banded sparsity by converting a structured system to a dense matrix.
- Solving least squares with normal equations when the matrix is ill-conditioned.
- Forgetting that a tridiagonal algorithm assumes nonzero modified pivots.
- Ignoring storage costs. For large structured systems, memory can matter as much as arithmetic.

## Connections

- [Gaussian elimination pivoting and LU](/math/numerical-analysis/gaussian-elimination-pivoting-lu)
- [least squares and Chebyshev approximation](/math/numerical-analysis/least-squares-chebyshev-approximation)
- [finite difference methods for PDEs](/math/numerical-analysis/finite-difference-pdes)
- [cubic splines and parametric curves](/math/numerical-analysis/cubic-splines-parametric-curves)
