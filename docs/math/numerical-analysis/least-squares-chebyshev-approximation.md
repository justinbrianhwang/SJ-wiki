---
title: Least Squares and Chebyshev Approximation
sidebar_position: 19
---

# Least Squares and Chebyshev Approximation

Approximation is different from interpolation. Interpolation insists on matching data exactly at nodes, while approximation looks for a simpler function that is close in a chosen sense. Least squares minimizes the sum of squared residuals. Chebyshev, or minimax, approximation minimizes the maximum error.

The choice of norm changes the meaning of best. Least squares suits noisy data with many small independent errors. Chebyshev approximation suits problems where the worst deviation matters, including uniform polynomial approximation and filter design.

## Least squares as an orthogonal projection

A linear least-squares problem has the form

$$
\min_x \|Ax-b\|_2,
$$

where $A$ is often tall and rectangular and $r=b-Ax$ is the residual. At the solution, the residual is orthogonal to every column of $A$, which gives the normal equations

$$
A^TAx=A^Tb.
$$

To derive them, minimize the squared norm

$$
\phi(x)=(b-Ax)^T(b-Ax).
$$

Its gradient is $\nabla\phi(x)=-2A^T(b-Ax)$. A stationary point therefore satisfies $A^Tr=0$. If the columns of $A$ are independent, $A^TA$ is positive definite and the stationary point is the unique minimum. Geometrically, $A\hat x$ is the orthogonal projection of $b$ onto the column space of $A$, while $r$ lies in its orthogonal complement. The Pythagorean identity

$$
\|b-Ax\|_2^2
=\|r\|_2^2+\|A(\hat x-x)\|_2^2
$$

proves optimality without differentiation.

Their mathematical simplicity hides a numerical cost. For full-column-rank $A$, in the 2-norm,

$$
\kappa_2(A^TA)=\kappa_2(A)^2,
$$

so nearly dependent columns become substantially harder to handle. A QR factorization avoids forming $A^TA$. If $A=QR$ with orthonormal columns in $Q$, then

$$
Rx=Q^Tb.
$$

With a full orthogonal factorization $A=Q\begin{bmatrix}R\\0\end{bmatrix}$ and $Q^Tb=\begin{bmatrix}c\\d\end{bmatrix}$,

$$
\|Ax-b\|_2^2=\|Rx-c\|_2^2+\|d\|_2^2.
$$

The first term is minimized by solving $Rx=c$; the second is the unavoidable residual norm. Householder QR is the usual dense method because reflectors are stable and efficient. Modified Gram--Schmidt can be appropriate when columns arrive sequentially, but may need reorthogonalization for nearly dependent bases.

If $A$ is rank deficient, $R$ has zero or tiny diagonal entries and the minimizer is not unique. A column-pivoted QR can estimate rank and choose an independent subset. The singular value decomposition gives the minimum-norm solution

$$
\hat x=A^+b=V\Sigma^+U^Tb,
$$

while exposing which directions are poorly determined. Truncating tiny singular values or adding a penalty changes the statistical model, so it should be reported rather than hidden as a numerical detail.

Weighted least squares minimizes $\sum_iw_i r_i^2$ with positive weights. It is ordinary least squares for $W^{1/2}A$ and $W^{1/2}b$. Larger $w_i$ means that observation is trusted more, often because its error variance is smaller. Correlated errors require a non-diagonal covariance model rather than independent scalar weights.

Report the basis along with the coefficients: changing from monomials to an orthogonal basis can improve conditioning without changing the approximation space. Residuals should also be inspected as data. A curved residual pattern can reveal an inadequate model even when $\|r\|_2$ is small.

## Chebyshev polynomials and uniform error

On $[-1,1]$, the Chebyshev polynomials are

$$
T_n(x)=\cos(n\arccos x).
$$

They obey the three-term recurrence

$$
T_0(x)=1,
\quad T_1(x)=x,
\quad T_{n+1}(x)=2xT_n(x)-T_{n-1}(x).
$$

The recurrence follows from $2\cos\theta\cos(n\theta)=\cos((n+1)\theta)+\cos((n-1)\theta)$. It evaluates a Chebyshev expansion without constructing high powers of $x$. The polynomials are orthogonal with weight $(1-x^2)^{-1/2}$:

$$
\int_{-1}^1\frac{T_m(x)T_n(x)}{\sqrt{1-x^2}}\,dx=0,
\qquad m\ne n.
$$

Substitution $x=\cos\theta$ reduces this to cosine orthogonality on $[0,\pi]$. A function can therefore be expanded in Chebyshev coefficients much as a periodic function is expanded in Fourier coefficients. Truncation often gives a near-minimax polynomial for a smooth function, though it need not be the exact minimax solution.

A minimax polynomial solves

$$
\min_p \|f-p\|_\infty
$$

over a chosen polynomial space. Chebyshev polynomials are useful here because $\vert T_n(x)\vert \leq 1$ and their extrema alternate between $1$ and $-1$. Under the usual hypotheses, the error of the best degree-$n$ polynomial reaches alternating positive and negative extrema of equal magnitude at at least $n+2$ points. This equioscillation condition is both a characterization and a useful diagnostic. Imbalanced positive and negative peaks indicate that a candidate is not minimax.

For sufficiency, suppose $f-p$ alternates between $+E$ and $-E$ at $n+2$ ordered points. Any polynomial $q$ with smaller maximum error would force $q-p$ to change sign between each consecutive pair. That gives at least $n+1$ roots, impossible for a nonzero polynomial of degree at most $n$. The necessity follows by constructing a small degree-$n$ correction when the controlling extrema do not alternate evenly.

The Remez algorithm uses the characterization computationally. Begin with $n+2$ candidate extremal points, solve for the coefficients and a common signed error, find the actual extrema of the new error, then exchange points and repeat. Locating the extremal set is the nonlinear part; once those points are fixed, the coefficient problem is linear.

Chebyshev nodes cluster near the endpoints and reduce the oscillation seen with equally spaced interpolation nodes. For an interval $[a,b]$, map it to $[-1,1]$ before applying formulas written in the standard coordinate.

## Choosing the norm and the solver

| Approximation type | Objective | Typical equation | Best for | Numerical warning |
|---|---|---|---|---|
| Interpolation | exact node matching | $P(x_i)=y_i$ | trusted exact data | oscillation and noise fitting |
| Least squares | minimize $\|r\|_2$ | $A^TAx=A^Tb$ or QR | noisy overdetermined data | normal equations square conditioning |
| Chebyshev/minimax | minimize $\|r\|_\infty$ | equioscillation | uniform worst-case control | harder to compute directly |
| Chebyshev basis | stable polynomial basis | recurrence for $T_n$ | high-degree approximation | map intervals to $[-1,1]$ |

```mermaid
flowchart TB
  Data["Approximation data or function<br/>samples, weights, interval"] --> Objective{"Choose error objective"}

  subgraph LS["Least-squares architecture"]
    direction TB
    Design["build design matrix A<br/>basis functions at data points"] --> Solve["solve min ||A c - y||_2<br/>prefer QR over normal equations"]
    Solve --> Resid["inspect residuals and conditioning"]
  end

  subgraph Cheb["Chebyshev/minimax architecture"]
    direction TB
    Map["map interval to #lsqb;-1,1"]"] --> Basis["use Chebyshev basis T_n(x)<br/>stable recurrence"]
    Basis --> Equi["minimax target<br/>alternating peak errors of equal magnitude"]
    Equi --> Uniform["control ||error||_infinity"]
  end

  Objective -- "average squared error" --> Design
  Objective -- "worst-case uniform error" --> Map
  Resid --> Check["validate norm, residual pattern, and endpoint behavior"]
  Uniform --> Check
  Check --> Approx(("approximant"))
```

The two branches have different error contracts. Least squares builds and solves a design-matrix problem in the 2-norm; minimax approximation maps the interval and targets balanced peak error in the infinity norm. The reported norm is part of the result, since a best fit in one norm can be poor in another.

The computational comparison should use cost to reach a verified tolerance. QR factorization, basis evaluation, and the conditioning of the design matrix usually dominate here. A dense factorization that is harmless for a small data set may be unsuitable for a large discretized problem.

## Fitting a line by least squares

Fit $y=c_0+c_1x$ to

$$
(0,1),\quad (1,2),\quad (2,2).
$$

The design matrix and data vector are

$$
A=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix},
\qquad
b=\begin{bmatrix}1\\2\\2\end{bmatrix}.
$$

For this small hand calculation, form

$$
A^TA=\begin{bmatrix}3&3\\3&5\end{bmatrix},
\qquad
A^Tb=\begin{bmatrix}5\\6\end{bmatrix}.
$$

Solving the $2\times2$ system gives

$$
c_0=\frac{5(5)-3(6)}{15-9}=\frac76,
\qquad
c_1=\frac{3(6)-3(5)}{15-9}=\frac12.
$$

The fitted line is $y=7/6+x/2$.

The residuals are

$$
r=b-Ac=\begin{bmatrix}-1/6\\1/3\\-1/6\end{bmatrix}.
$$

They sum to zero and their $x$-weighted sum is zero:

$$
\begin{bmatrix}1&1&1\\0&1&2\end{bmatrix}r
=\begin{bmatrix}0\\0\end{bmatrix}.
$$

That is $A^Tr=0$. The residual norm is $\sqrt{1/6}$. An intercept-only model gives the mean $5/3$ and squared residual $2/3$, so adding the slope reduces squared error by $1/2$.

## Checking the Chebyshev recurrence

Starting with $T_0=1$ and $T_1=x$ gives

$$
T_2(x)=2xT_1(x)-T_0(x)=2x^2-1
$$

and

$$
T_3(x)=2xT_2(x)-T_1(x)=4x^3-3x.
$$

At $x=1/2$,

$$
T_3(1/2)=4(1/8)-3(1/2)=-1.
$$

The trigonometric definition agrees because $1/2=\cos(\pi/3)$ and

$$
T_3(1/2)=\cos(3\pi/3)=\cos(\pi)=-1.
$$

## A minimax constant for a quadratic

Approximate $f(x)=x^2$ on $[-1,1]$ by a constant $c$. The error $e(x)=x^2-c$ has minimum $-c$ at zero and maximum $1-c$ at the endpoints. Equal opposite extremes require

$$
c=1-c,
$$

so $c=1/2$ and the uniform error is $1/2$. Indeed,

$$
e(-1)=\frac12,\qquad e(0)=-\frac12,\qquad e(1)=\frac12.
$$

The continuous unweighted least-squares constant is instead the average of $x^2$:

$$
c_{LS}=\frac12\int_{-1}^1x^2\,dx=\frac13.
$$

It has smaller integrated squared error but a larger endpoint error of $2/3$. The norms encode different goals, so neither result supersedes the other.

## Computing with QR and the three-term recurrence

```python
import numpy as np

def least_squares_qr(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    Q, R = np.linalg.qr(A, mode="reduced")
    return np.linalg.solve(R, Q.T @ b)

def chebyshev_values(x, n):
    values = [np.ones_like(x, dtype=float)]
    if n == 0:
        return values
    values.append(np.array(x, dtype=float))
    for k in range(1, n):
        values.append(2 * x * values[-1] - values[-2])
    return values

A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
b = np.array([1.0, 2.0, 2.0])
print(least_squares_qr(A, b))
print(chebyshev_values(np.array([0.5]), 3))
```

## From coefficients to uncertainty

In the linear statistical model $b=A\beta+\varepsilon$, suppose the error has mean zero and covariance $\sigma^2I$. The least-squares estimator is unbiased when $A$ has full column rank, and

$$
\operatorname{Cov}(\hat\beta)=\sigma^2(A^TA)^{-1}.
$$

Nearly dependent columns make this matrix large, so individual coefficients can be uncertain even when fitted values are stable. The residual sum of squares estimates $\sigma^2$ after accounting for degrees of freedom, under the model assumptions. None of these uncertainty claims follow from linear algebra alone; correlated errors, changing variance, or model bias require a different analysis.

Leverage measures how strongly an observation's predictor row can affect its fitted value. A point at an extreme predictor location may have high leverage even with a small residual. Conversely, a large residual at an ordinary location signals lack of fit or unusual noise. Residual plots against fitted values and predictors reveal structure that one scalar norm suppresses.

Scaling the columns before solving helps separate numerical conditioning from units. If $A=DS$ represents a better-scaled design $D$ and a diagonal conversion $S$, solve for the scaled coefficients and transform them back. QR still avoids squaring the condition number, but it cannot make two genuinely redundant model terms identifiable.

## Evaluating a Chebyshev series

A polynomial stored as

$$
p(x)=\sum_{k=0}^nc_kT_k(x)
$$

should usually be evaluated by Clenshaw's recurrence, the analogue of Horner's method for a three-term basis. Set $b_{n+2}=b_{n+1}=0$ and compute backward

$$
b_k=2xb_{k+1}-b_{k+2}+c_k.
$$

Then $p(x)=b_0-xb_1$ under this coefficient convention. Backward evaluation avoids conversion to monomial coefficients, whose large alternating values can cancel badly near $[-1,1]$.

Chebyshev coefficients also provide a useful error indicator. For a smooth function their magnitudes often decay steadily until reaching a floor set by rounding or data error. A tail that does not decay suggests insufficient smoothness, a singularity near the interval, or a degree already beyond what the data support. Truncating after the settled tail is usually safer than retaining coefficients dominated by noise.

Mapping $t\in[a,b]$ to $x=(2t-a-b)/(b-a)$ must be included when differentiating. Since $dx/dt=2/(b-a)$, every derivative gains the corresponding scale factor. Forgetting it produces coefficients that look numerically consistent on $[-1,1]$ but represent the wrong physical derivative.

## Discrete least squares versus continuous approximation

Fitting samples minimizes a finite sum. Continuous least squares minimizes an integral such as

$$
\int_a^b w(x)[f(x)-p(x)]^2\,dx.
$$

The normal equations become orthogonality conditions against every basis function. If the basis is orthogonal for the weight $w$, the coefficient equations decouple. Chebyshev polynomials use the singular endpoint weight $(1-x^2)^{-1/2}$; Legendre polynomials use constant weight. The choice encodes where error matters, not merely a computational preference.

A quadrature rule can turn the continuous problem into a weighted discrete one, but the rule must integrate the relevant products accurately. Dense sampling with arbitrary weights does not automatically reproduce the intended continuous norm.

## What to verify before trusting the approximation

- Record the data model, basis, norm, interval scaling, and noise assumptions. Similar-looking computations can otherwise represent different numerical problems.
- Check residual orthogonality for least squares and alternating maximum error for a minimax candidate.
- When no exact answer is available, compare independent approximations, refine the mesh or tolerance, or test a nearby problem with known behavior.
- Increasing polynomial degree alone does not repair poor scaling, unsuitable nodes, or a badly conditioned basis.
- Do not judge a least-squares fit solely by its maximum error, or a minimax fit solely by its sum of squares.

Nearly dependent design columns need special attention. Centering and scaling the independent variable can improve a polynomial design matrix sharply, and a Chebyshev basis is usually preferable to monomials at moderate degree. Such transformations change coefficient interpretation, so predictions must be converted carefully if coefficients are reported in original units.

Outliers expose the assumptions behind squared error. One large residual contributes quadratically and can dominate the fit. A robust loss or explicit data review may be justified, but silently deleting observations is not a numerical method. A tiny training residual can likewise indicate overfitting when the number of basis functions approaches the number of observations; withheld-data error answers a different question from algebraic optimality.

Keep the continuous problem, its discrete approximation, the algorithm used to compute it, and the diagnostic used to judge it separate. A small algebraic residual, for example, says little about modeling error.

## Regularization changes the question

When the design is ill-conditioned, ridge regression minimizes

$$
\|Ax-b\|_2^2+\lambda\|x\|_2^2.
$$

The added term stabilizes directions associated with small singular values, but introduces bias and depends on coefficient scaling. It is not a numerically cleaner way to solve the original least-squares problem; it defines a different approximation problem. The value of $\lambda$ and any column standardization must accompany the reported coefficients.

Truncated SVD makes the same distinction explicit by discarding selected singular directions. It can be appropriate when those directions represent noise below measurement resolution. A rank threshold chosen merely because a solver printed a warning is not a model justification.

Cross-validation, information criteria, or a held-out set can guide degree and regularization choices. These assess predictive behavior, whereas the residual norm assesses fit to the supplied data. Keeping those roles separate prevents a high-degree polynomial from being declared superior solely because it has more freedom.

<div className="see-also">

See also: [matrix factorizations and special systems](/math/numerical-analysis/matrix-factorizations-special-systems) · [rational trigonometric approximation and FFT](/math/numerical-analysis/rational-trigonometric-fft) · [interpolation Lagrange and Neville method](/math/numerical-analysis/interpolation-lagrange-neville) · [eigenvalue methods](/math/numerical-analysis/eigenvalue-methods)

</div>
