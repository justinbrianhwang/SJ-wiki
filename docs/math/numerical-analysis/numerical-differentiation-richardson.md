---
title: Numerical Differentiation and Richardson Extrapolation
sidebar_position: 9
---

# Numerical Differentiation and Richardson Extrapolation

Numerical differentiation estimates derivatives from function values. It looks simple because the formulas resemble the limit definitions from calculus, but it is one of the most error-sensitive tasks in numerical analysis. Difference quotients subtract nearby values, and that subtraction can amplify both measurement noise and floating-point roundoff.

Richardson extrapolation improves a difference formula by combining approximations computed with different step sizes. When the leading error term is known, the combination cancels that term and raises the order. The idea appears again in Romberg integration, deferred correction, and step-size control for differential equations.

## Difference formulas from Taylor series

The forward difference approximation to $f'(x)$ is

$$
D_+(h)=\frac{f(x+h)-f(x)}{h}.
$$

The backward difference is

$$
D_-(h)=\frac{f(x)-f(x-h)}{h},
$$

and the centered difference is

$$
D_0(h)=\frac{f(x+h)-f(x-h)}{2h}.
$$

Taylor expansion gives the truncation orders

$$
D_+(h)=f'(x)+O(h),\qquad D_0(h)=f'(x)+O(h^2).
$$

A common centered approximation to the second derivative is

$$
\frac{f(x+h)-2f(x)+f(x-h)}{h^2}=f''(x)+O(h^2).
$$

Richardson extrapolation assumes an approximation has an error expansion

$$
A(h)=A+C h^p+O(h^{p+1})
$$

or, more commonly for symmetric formulas, $A(h)=A+C h^p+O(h^{p+2})$. Combining $A(h)$ and $A(h/2)$ gives

$$
A_R=\frac{2^pA(h/2)-A(h)}{2^p-1}.
$$

## Cancellation produces the order

Taylor's theorem is the source of finite-difference formulas. For example,

$$
\begin{aligned}
f(x+h)&=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\frac{h^3}{6}f^{(3)}(\xi_+),\\
f(x-h)&=f(x)-hf'(x)+\frac{h^2}{2}f''(x)-\frac{h^3}{6}f^{(3)}(\xi_-).
\end{aligned}
$$

Subtracting the second line from the first cancels the even powers and leaves the centered difference with second-order truncation error.

The total error has two competing parts. A model for first derivative approximation is

$$
\text{error}(h)\approx C_1h^p+C_2\frac{u}{h},
$$

where $u$ is unit roundoff. The first term decreases as $h$ decreases; the second term increases because subtracting nearby rounded values and dividing by $h$ magnifies roundoff. Therefore the best $h$ is not the smallest possible $h$.

Richardson extrapolation is reliable only when the assumed asymptotic error expansion has begun to dominate. If $h$ is too large, higher-order terms spoil the cancellation. If $h$ is too small, roundoff and data noise dominate. A sound implementation computes a table and stops when improvement stalls.

Dividing the forward Taylor series by $h$ gives

$$
\frac{f(x+h)-f(x)}{h}
=f'(x)+\frac{h}{2}f''(x)+O(h^2).
$$

The leading bias is proportional to $h$. Subtracting the backward expansion from the forward expansion removes every even-power term before division:

$$
\frac{f(x+h)-f(x-h)}{2h}
=f'(x)+\frac{h^2}{6}f^{(3)}(x)+O(h^4).
$$

Adding the two expansions and subtracting $2f(x)$ instead isolates the second derivative:

$$
\frac{f(x+h)-2f(x)+f(x-h)}{h^2}
=f''(x)+\frac{h^2}{12}f^{(4)}(x)+O(h^4).
$$

Symmetry earns second order with only two samples for the first derivative, but it is unavailable at a boundary. A second-order forward formula can be derived by choosing weights that cancel the constant and second-derivative terms:

$$
f'(x)\approx\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}.
$$

The larger coefficients amplify noisy data more than the first-order forward quotient. Order and robustness are separate properties.

## Why a smaller step eventually hurts

Suppose each function value carries absolute error of size roughly $\delta$. A first-difference quotient can amplify that error to order $\delta/h$. For floating-point evaluation of a well-scaled smooth function, $\delta$ is often comparable to unit roundoff $u$ times the function scale. The centered first derivative then has the model

$$
E(h)\approx C_th^2+C_r\frac{u}{h}.
$$

Balancing the terms gives an optimal scale proportional to $u^{1/3}$, not $u$ itself. For a forward difference, balancing $C_th$ with $C_ru/h$ gives a scale proportional to $u^{1/2}$. The unknown constants depend on derivative and function magnitudes, so these are starting scales rather than universal step sizes.

Second derivatives are harsher: roundoff is divided by $h^2$, while the centered truncation error remains $O(h^2)$. Their balance occurs around $u^{1/4}$ after scaling. Numerical differentiation is therefore often the wrong operation for raw measured data. A fitted local polynomial or smoothing spline can estimate a derivative while controlling noise amplification.

Absolute scaling matters too. Perturbing a value $x=10^8$ by $h=10^{-8}$ may produce no representable change at all. Step choices often use $h$ relative to $\max(1,\vert x\vert )$, and implementations should verify that $x+h\ne x$ in floating-point arithmetic.

## Richardson columns and their assumptions

For a symmetric base formula,

$$
A(h)=A+c_2h^2+c_4h^4+c_6h^6+\cdots.
$$

The first Richardson column uses

$$
A_1(h)=\frac{4A(h/2)-A(h)}{3}
=A+O(h^4).
$$

A second extrapolation combines $A_1(h)$ and $A_1(h/2)$ with factor $16$:

$$
A_2(h)=\frac{16A_1(h/2)-A_1(h)}{15}
=A+O(h^6).
$$

The factor changes by column because the leading power changes. A table routine that repeatedly uses the same factor of four after the first column is wrong.

Extrapolation assumes a smooth power-series error and that the selected $h$ values already lie in its asymptotic range. A kink, branch switch, noisy evaluation, or discontinuous higher derivative can invalidate it. A useful table shows the base estimates and every extrapolated column. Stable digits should appear across adjacent rows before the final entry is trusted.

## Alternatives when the function is available as code

The complex-step formula avoids subtracting two nearby real numbers. For a real analytic function extended to complex arguments,

$$
f(x+\mathrm{i}h)=f(x)+\mathrm{i}hf'(x)-\frac{h^2}{2}f''(x)+O(h^3),
$$

so

$$
f'(x)\approx\frac{\operatorname{Im}f(x+\mathrm{i}h)}{h}
$$

with $O(h^2)$ truncation error. Very small $h$ can be used because there is no real subtraction. The method fails when the program discards imaginary parts, uses nonanalytic operations such as absolute value, or branches differently for complex input.

Automatic differentiation propagates derivatives through program operations and avoids truncation error. Symbolic differentiation gives an expression when the function is sufficiently manageable. Finite differences remain useful for black-box functions and for checking an analytic or automatic derivative. A directional check is often cheaper than testing every partial derivative separately.

## Reading an error curve

The left side of the sketch corresponds to tiny $h$, where roundoff or data error dominates. The right side corresponds to large $h$, where truncation dominates. A step-halving experiment should first improve at the expected rate and then flatten or worsen. If no expected-rate region appears, increasing the extrapolation depth will not rescue the estimate.

## Unequally spaced samples

Uniform-grid formulas cannot be copied unchanged onto irregular data. Suppose values are known at $x-h_-$, $x$, and $x+h_+$ with unequal positive spacings. Differentiating the quadratic interpolant gives

$$
f'(x)\approx
-\frac{h_+}{h_-(h_-+h_+)}f(x-h_-)
+\frac{h_+-h_-}{h_-h_+}f(x)
+\frac{h_-}{h_+(h_-+h_+)}f(x+h_+).
$$

When $h_-=h_+=h$, the center coefficient vanishes and the formula reduces to the usual centered difference. With unequal spacings, simply dividing the endpoint difference by $h_-+h_+$ generally leaves a first-order bias.

Finite-difference weights for more points can be obtained by requiring exactness on monomials up to a chosen degree. For nodes $x_j$, choose weights $w_j$ so that

$$
\sum_jw_j(x_j-x)^m=
\begin{cases}
1,&m=1,\\
0,&m=0,2,\ldots,q.
\end{cases}
$$

Then $\sum_jw_jf(x_j)$ approximates $f'(x)$. The resulting Vandermonde-like system can be ill-conditioned when formed naively for high degree, so established weight-generation recurrences are preferable in software. Irregular spacing also complicates error estimates. A nominally high-degree interpolant may be dominated by one distant point, and clustered nodes can create large alternating weights.

## Derivatives from measured data

When samples contain noise $y_i=f(x_i)+\varepsilon_i$, differencing treats the noise as signal. A centered quotient has noise contribution

$$
\frac{\varepsilon_{i+1}-\varepsilon_{i-1}}{2h},
$$

whose variance is $\sigma_\varepsilon^2/(2h^2)$ for independent equal-variance errors. Collecting measurements more densely without reducing noise can therefore make a raw derivative estimate more variable.

Local polynomial regression addresses the tradeoff. Around $x_0$, fit

$$
y\approx a_0+a_1(x-x_0)+a_2(x-x_0)^2+\cdots
$$

by weighted least squares, then use $a_1$ as the derivative estimate. A wider neighborhood reduces noise but smooths genuine local features; a narrower neighborhood follows features but has higher variance. Savitzky--Golay filters are fixed-grid versions of this local polynomial idea.

Smoothing splines choose a function by balancing fit to the data against a roughness penalty such as

$$
\sum_i(y_i-s(x_i))^2
+\lambda\int[s''(x)]^2\,dx.
$$

The derivative comes from the fitted smooth function. The parameter $\lambda$ controls the bias--variance compromise and should be selected from the measurement goal, cross-validation, or a noise model rather than chosen to make the derivative curve attractive.

## Partial derivatives and Jacobian checks

For $F:\mathbb R^n\to\mathbb R^m$, a forward-difference Jacobian column costs one additional evaluation of the whole vector function:

$$
J_{\cdot j}(x)\approx
\frac{F(x+h_je_j)-F(x)}{h_j}.
$$

A dense Jacobian therefore costs $n+1$ evaluations, while central differences cost about $2n$. If the Jacobian is sparse and the sparsity pattern is known, structurally independent columns can be perturbed together, reducing evaluation count through graph coloring.

A directional derivative check avoids constructing all columns. Choose a vector $v$ and compare $J(x)v$ with

$$
\frac{F(x+hv)-F(x)}{h}.
$$

Trying several step sizes should show the expected decrease and eventual roundoff plateau. Several directions catch many analytic-Jacobian bugs, though they do not certify every entry.

## Differentiation matrices and boundary rows

On a fixed grid, all finite differences can be assembled into a matrix $D$ so that sampled derivatives are approximated by $D\mathbf f$. Interior rows may use centered formulas while boundary rows use one-sided formulas. This form is convenient for PDE discretizations and repeated differentiation, but it also exposes noise amplification through $\|D\|$, which grows as the grid is refined.

Repeatedly applying a first-derivative matrix need not equal a carefully derived second-derivative matrix at boundaries. The product $D^2$ inherits two layers of boundary closure and can have different accuracy or stability. For a second derivative, use a stencil and boundary treatment designed for that operator rather than assuming matrix powers preserve the desired properties.

Units remain a useful guardrail. If $f$ is measured in meters and $x$ in seconds, a first derivative must have units meters per second and a second derivative meters per second squared. Each first-derivative weight therefore carries inverse-time units. Missing a power of $h$ in a second-difference formula changes both convergence and dimensions, a mistake that a numerical spot check at one spacing may not reveal.

| Formula | Approximation | Truncation order | Function values | Main risk |
|---|---|---:|---:|---|
| Forward difference | $f'(x)$ | $O(h)$ | 2 | biased one-sided error |
| Backward difference | $f'(x)$ | $O(h)$ | 2 | biased one-sided error |
| Centered difference | $f'(x)$ | $O(h^2)$ | 2 | cancellation for tiny $h$ |
| Centered second difference | $f''(x)$ | $O(h^2)$ | 3 | noise amplification |
| Richardson extrapolated centered | $f'(x)$ | often $O(h^4)$ | 4 total | assumes asymptotic regime |

```text
error
  ^        roundoff ~ u/h
  |       /
  |      /\
  |     /  \   total
  |    /    \_
  |   /       \ truncation ~ h^p
  +------------------> h
        best h
```

## Worked example 1: centered difference for $\sin x$

**Problem.** Approximate $f'(0)$ for $f(x)=\sin x$ using the centered difference with $h=0.1$.

**Method.** The exact derivative is $f'(x)=\cos x$, so $f'(0)=1$.

1. Apply the centered formula:

$$
D_0(0.1)=\frac{\sin(0.1)-\sin(-0.1)}{0.2}.
$$

2. Since $\sin(-0.1)=-\sin(0.1)$,

$$
D_0(0.1)=\frac{2\sin(0.1)}{0.2}=\frac{\sin(0.1)}{0.1}.
$$

3. Numerically,

$$
D_0(0.1)=0.9983341665\ldots.
$$

4. The absolute error is

$$
|1-0.9983341665\ldots|=0.0016658335\ldots.
$$

**Checked answer.** The centered difference gives $0.9983341665\ldots$, close to the exact derivative $1$, with error about $1.67\times 10^{-3}$.

## Worked example 2: Richardson improvement

**Problem.** Improve the previous derivative estimate using $h=0.1$ and $h/2=0.05$.

**Method.** The centered difference has leading error order $p=2$, so use

$$
D_R=D_0(h/2)+\frac{D_0(h/2)-D_0(h)}{2^2-1}.
$$

1. The two centered estimates are

$$
D_0(0.1)=0.9983341665\ldots,
$$

$$
D_0(0.05)=\frac{\sin(0.05)}{0.05}=0.9995833854\ldots.
$$

2. Extrapolate:

$$
D_R=0.9995833854+\frac{0.9995833854-0.9983341665}{3}.
$$

3. Compute the correction:

$$
\frac{0.0012492189}{3}=0.0004164063.
$$

4. Therefore

$$
D_R=0.9999997917\ldots.
$$

**Checked answer.** Richardson extrapolation reduces the error from about $1.67\times 10^{-3}$ to about $2.08\times 10^{-7}$ for this smooth example.

The improvement also matches the predicted orders. Halving $h$ reduces the centered error by about four, while cancelling that $h^2$ term leaves an $h^4$ error. Repeating the calculation at $h=0.05$ and $0.025$ gives another extrapolated value; agreement between the two extrapolated rows is stronger evidence than one impressive-looking number.

## Step-halving code

```python
import math

def centered_first(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)

def centered_second(f, x, h):
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)

def richardson(values, p):
    table = [list(values)]
    factor = 2**p
    while len(table[-1]) > 1:
        previous = table[-1]
        current = []
        for i in range(len(previous) - 1):
            current.append((factor * previous[i + 1] - previous[i]) / (factor - 1.0))
        table.append(current)
        factor *= 2**p
    return table

hs = [0.2, 0.1, 0.05, 0.025]
vals = [centered_first(math.sin, 0.0, h) for h in hs]
for row in richardson(vals, p=2):
    print(row)

print(centered_second(math.exp, 0.0, 0.01), "exact", 1.0)
```

## Failure patterns

- Making $h$ extremely small and expecting a better derivative. Roundoff grows like a negative power of $h$.
- Differentiating noisy data with high-order formulas. Differentiation amplifies high-frequency noise.
- Applying Richardson extrapolation before the leading error term is actually dominant.
- Forgetting that one-sided formulas are lower order unless specially designed.
- Using a derivative estimate without checking sensitivity to several nearby step sizes.

<div className="see-also">

See also: [mathematical preliminaries and error analysis](/math/numerical-analysis/mathematical-preliminaries-error-analysis) · [floating point conditioning and stability](/math/numerical-analysis/floating-point-conditioning-stability) · [Newton Secant and polynomial roots](/math/numerical-analysis/newton-secant-polynomial-roots) · [Newton Cotes and Romberg integration](/math/numerical-analysis/newton-cotes-romberg-integration)

</div>
