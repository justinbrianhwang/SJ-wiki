---
title: Vectors in Rn
sidebar_position: 7
---

# Vectors in Rn

Vectors in $\mathbb{R}^n$ are ordered lists of real numbers, but they should be read as more than lists. They encode displacement, data, forces, coefficients, states, and solutions. Linear algebra studies operations that preserve the two essential vector actions: adding vectors and scaling them.

This page is the concrete starting point for the rest of the subject. Later pages abstract these same operations to general vector spaces, but the intuition usually comes from $\mathbb{R}^2$ and $\mathbb{R}^3$: arrows can be added tip-to-tail, stretched by scalars, and combined to reach new locations. The same algebra also describes columns of a matrix, feature vectors in data, and state vectors in applied models.

## Definitions

A vector in $\mathbb{R}^n$ is

$$
\mathbf{v}=
\begin{bmatrix}
v_1\\
v_2\\
\vdots\\
v_n
\end{bmatrix}.
$$

Vector addition and scalar multiplication are componentwise:

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

A linear combination of vectors $\mathbf{v}_1,\ldots,\mathbf{v}_k$ is

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k.
$$

The span of a set of vectors is the set of all their linear combinations. In $\mathbb{R}^2$, one nonzero vector spans a line through the origin. Two nonparallel vectors span the whole plane.

The standard basis of $\mathbb{R}^n$ is $\mathbf{e}_1,\ldots,\mathbf{e}_n$, where $\mathbf{e}_i$ has a $1$ in position $i$ and zeros elsewhere. Every vector has coordinates relative to this basis:

$$
\mathbf{v}=v_1\mathbf{e}_1+\cdots+v_n\mathbf{e}_n.
$$

The dot product and norm are

$$
\mathbf{u}\cdot\mathbf{v}=u_1v_1+\cdots+u_nv_n,
\qquad
\|\mathbf{v}\|=\sqrt{\mathbf{v}\cdot\mathbf{v}}.
$$

## Key results

The vector operations in $\mathbb{R}^n$ satisfy the usual algebraic laws: addition is commutative and associative, there is a zero vector, every vector has an additive inverse, scalar multiplication distributes over vector addition, and scalar multiplication is compatible with multiplication of scalars.

Every vector in $\mathbb{R}^n$ has a unique standard-basis expansion:

$$
\mathbf{v}=v_1\mathbf{e}_1+\cdots+v_n\mathbf{e}_n.
$$

Proof sketch: the right-hand side has $i$th component $v_i$, so it equals $\mathbf{v}$. Uniqueness follows because equality of vectors means equality component by component.

The line through a point $\mathbf{p}$ in direction $\mathbf{v}\neq\mathbf{0}$ is

$$
\mathbf{x}=\mathbf{p}+t\mathbf{v}.
$$

The plane through $\mathbf{p}$ in directions $\mathbf{u},\mathbf{v}$ is

$$
\mathbf{x}=\mathbf{p}+s\mathbf{u}+t\mathbf{v},
$$

provided $\mathbf{u}$ and $\mathbf{v}$ are not scalar multiples.

Linear dependence in $\mathbb{R}^n$ means that at least one vector in a list can be built from the others. Equivalently, the equation

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k=\mathbf{0}
$$

has a solution where not all $c_i$ are zero. Dependence is a geometric warning that the listed directions contain redundancy.

## Visual

ASCII sketch of span in $\mathbb{R}^2$:

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

## Worked example 1: Combine vectors and check a span

Problem: let

$$
\mathbf{u}=
\begin{bmatrix}
2\\-1\\3
\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}
0\\4\\1
\end{bmatrix}.
$$

Compute $3\mathbf{u}-2\mathbf{v}$, and decide whether

$$
\mathbf{w}=
\begin{bmatrix}
5\\1\\4
\end{bmatrix}
$$

lies in $\operatorname{span}\{\mathbf{u},\mathbf{v}\}$.

Step 1: compute the linear combination componentwise.

$$
3\mathbf{u}-2\mathbf{v}
=
\begin{bmatrix}
6\\-3\\9
\end{bmatrix}
-
\begin{bmatrix}
0\\8\\2
\end{bmatrix}
=
\begin{bmatrix}
6\\-11\\7
\end{bmatrix}.
$$

Step 2: set up the span equation.

$$
c_1
\begin{bmatrix}
2\\-1\\3
\end{bmatrix}
+
c_2
\begin{bmatrix}
0\\4\\1
\end{bmatrix}
=
\begin{bmatrix}
5\\1\\4
\end{bmatrix}.
$$

Step 3: compare components:

$$
2c_1=5,
\qquad
-c_1+4c_2=1,
\qquad
3c_1+c_2=4.
$$

The first equation gives $c_1=5/2$. The second gives

$$
-\frac52+4c_2=1
\quad\Longrightarrow\quad
4c_2=\frac72
\quad\Longrightarrow\quad
c_2=\frac78.
$$

The third equation would require

$$
3\left(\frac52\right)+c_2=4
\quad\Longrightarrow\quad
c_2=-\frac72.
$$

The two required values of $c_2$ disagree. Checked answer: $\mathbf{w}$ is not in the span of $\mathbf{u}$ and $\mathbf{v}$.

## Worked example 2: Parametrize a line and a plane

Problem: find a parametric equation for the line through

$$
\mathbf{p}=
\begin{bmatrix}
1\\-2\\0
\end{bmatrix}
$$

in the direction

$$
\mathbf{v}=
\begin{bmatrix}
3\\1\\-4
\end{bmatrix},
$$

then test whether $\mathbf{q}=\begin{bmatrix}7\\0\\-8\end{bmatrix}$ lies on it.

Step 1: write the vector equation.

$$
\mathbf{x}=\mathbf{p}+t\mathbf{v}
=
\begin{bmatrix}
1\\-2\\0
\end{bmatrix}
+t
\begin{bmatrix}
3\\1\\-4
\end{bmatrix}.
$$

Step 2: write component equations:

$$
x=1+3t,\qquad y=-2+t,\qquad z=-4t.
$$

Step 3: test $\mathbf{q}$. From $x=7$,

$$
7=1+3t
\quad\Longrightarrow\quad
t=2.
$$

With $t=2$, the $y$ coordinate is $-2+2=0$, and the $z$ coordinate is $-8$. Both match $\mathbf{q}$.

Checked answer: $\mathbf{q}$ lies on the line, and it corresponds to $t=2$.

## Code

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

The least-squares call returns the closest vector in the span. `allclose` checks whether the match is exact up to floating-point tolerance; here it reports that the span equation is not exactly solvable.

## Common pitfalls

- Treating vectors as points only. A vector can represent a point, displacement, data record, or coefficient list depending on context.
- Adding vectors of different dimensions. Operations in $\mathbb{R}^n$ require matching lengths.
- Confusing span with a finite list of combinations. Span contains all scalar combinations, usually infinitely many.
- Assuming two nonzero vectors in $\mathbb{R}^3$ span all of $\mathbb{R}^3$. Two directions can span at most a plane.
- Forgetting that the zero vector cannot determine a line direction by itself.
- Deciding span membership by visual guess instead of solving the coefficient equation.

A strong habit is to translate every span question into a linear system. To ask whether $\mathbf{w}$ lies in the span of $\mathbf{v}_1,\ldots,\mathbf{v}_k$, set

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k=\mathbf{w}
$$

and solve for the coefficients. If the system is consistent, the vector is in the span. If it is inconsistent, the vector is outside the span. This method scales from pictures in $\mathbb{R}^2$ to high-dimensional data where visualization is impossible.

Linear combinations also provide the first intuition for coordinates. In the standard basis, the coordinates of $\mathbf{v}$ are its entries. In a nonstandard basis, coordinates are the weights needed to build the same vector from different basis directions. This distinction becomes essential when studying change of basis, diagonalization, and linear transformations.

The zero vector deserves special attention. It belongs to every span because all coefficients can be chosen as zero. It is also linearly dependent with any list that contains it, because $1\cdot\mathbf{0}=\mathbf{0}$ is a nontrivial relation. But it cannot serve as a direction vector for a line, since $t\mathbf{0}$ never moves away from the starting point.

In applications, vector entries should have a consistent interpretation. A vector might represent measurements, but adding two measurement vectors only makes sense if corresponding entries refer to the same quantities and units. Linear algebra supplies formal operations; modeling supplies the meaning of the components.

Vector equations are often cleaner than coordinate equations. The parametric line

$$
\mathbf{x}=\mathbf{p}+t\mathbf{v}
$$

encodes three component equations in $\mathbb{R}^3$ and makes the direction visible. Similarly, a plane equation using two direction vectors shows immediately which movements stay inside the plane. Coordinate equations are useful for solving; vector equations are useful for structure.

The idea of a linear combination is the seed of matrix multiplication. If $A$ has columns $\mathbf{a}_1,\ldots,\mathbf{a}_n$, then

$$
A\mathbf{x}=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n.
$$

Thus every matrix-vector product is a column combination. This viewpoint makes systems, column spaces, rank, and linear transformations feel like continuations of vector arithmetic rather than separate topics.

Magnitude and direction should also be kept separate. Scaling by a positive scalar changes length but not direction; scaling by a negative scalar reverses direction; adding vectors changes both. Later, normalization will create unit vectors that preserve direction while simplifying length calculations.

A final useful distinction is between equality of vectors and equality of representations. In $\mathbb{R}^n$, equality means every corresponding component is equal. But the same geometric vector may be represented with different coordinates after a change of basis. The entries are not the essence of the vector; they are its coordinates in a chosen coordinate system.

Many later computations are just organized vector arithmetic. Solving a system asks whether one vector is a linear combination of others. Finding a basis asks for a nonredundant spanning list. Orthogonal projection asks for the closest vector inside a span. Keeping the basic vector operations clear makes those later topics much easier to connect.

Before moving on, be able to move between three descriptions of the same object: a column of entries, an arrow or displacement, and a linear combination of basis vectors. Most later errors come from forgetting which description is being used in a given argument.

Also practice checking dimensions aloud: only vectors in the same $\mathbb{R}^n$ can be added, and only matching component positions should be compared or combined.

That discipline prevents silent coordinate mistakes.

## Connections

- [Systems of Linear Equations](/math/linear-algebra/systems-of-linear-equations)
- [Orthogonality in Rn](/math/linear-algebra/orthogonality-in-rn)
- [General Vector Spaces](/math/linear-algebra/vector-spaces)
- [Linear Transformations](/math/linear-algebra/linear-transformations)
