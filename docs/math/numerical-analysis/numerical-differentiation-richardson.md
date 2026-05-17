---
title: Numerical Differentiation and Richardson Extrapolation
sidebar_position: 9
---

# Numerical Differentiation and Richardson Extrapolation

Numerical differentiation estimates derivatives from function values. It looks simple because the formulas resemble the limit definitions from calculus, but it is one of the most error-sensitive tasks in numerical analysis. Difference quotients subtract nearby values, and that subtraction can amplify both measurement noise and floating-point roundoff.

![A tangent line touches a curve at a point to show instantaneous slope.](https://commons.wikimedia.org/wiki/Special:FilePath/Derivative_with_tangent.svg)

*Figure: A tangent line gives the local geometric meaning of a derivative. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Derivative_with_tangent.svg), Olivier Cleynen, CC0 1.0.*

Richardson extrapolation improves a difference formula by combining approximations computed with different step sizes. When the leading error term is known, the combination cancels that term and raises the order. The idea appears again in Romberg integration, deferred correction, and step-size control for differential equations.

## Definitions

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

## Key results

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

Richardson extrapolation is reliable only when the assumed asymptotic error expansion has begun to dominate. If $h$ is too large, higher-order terms spoil the cancellation. If $h$ is too small, roundoff and data noise dominate. A practical implementation computes a table and stops when improvement stalls.

A reliable way to use these results is to keep the analysis tied to the actual numerical question rather than to the formula alone. For numerical differentiation and Richardson extrapolation, the input record should include the function values, step sequence, formula order, and noise level. Without that record, two computations that look similar on paper may have different numerical meanings. The same formula can be a safe production tool in one scaling and a fragile experiment in another. This is why the examples on this page show the intermediate arithmetic: the goal is not only to reach a number, but to expose what assumptions made that number meaningful.

The next record is the verification record. Useful diagnostics for this topic include step-halving tables, extrapolated differences, and roundoff plateaus. A diagnostic should be chosen before the computation is trusted, not after a pleasing answer appears. When an exact answer is unavailable, compare two independent approximations, refine the mesh or tolerance, check a residual, or test the method on a neighboring problem with known behavior. If several diagnostics disagree, treat the disagreement as information about conditioning, stability, or implementation rather than as a nuisance to be averaged away.

The cost record matters as well. In this topic the dominant costs are usually function evaluations per derivative estimate and reuse of symmetric samples. Numerical analysis is full of methods that are mathematically attractive but computationally mismatched to the problem size. A dense factorization may be acceptable for a classroom matrix and impossible for a PDE grid. A high-order rule may use fewer steps but more expensive stages. A guaranteed method may take many iterations but provide a bound that a faster method cannot. The right comparison is therefore cost to reach a verified tolerance, not order or elegance in isolation.

Finally, every method here has a recognizable failure mode: choosing h too small, differentiating noisy data, and extrapolating before asymptotic behavior appears. These failures are not edge cases to memorize; they are signals that the hypotheses behind the result have been violated or that a different numerical model is needed. A good implementation makes such failures visible through exceptions, warnings, residual reports, or conservative stopping rules. A good hand solution does the same thing in prose by naming the assumption being used and checking it at the point where it matters.

For study purposes, the most useful habit is to separate four layers: the continuous mathematical problem, the discrete approximation, the algebraic or iterative algorithm used to compute it, and the diagnostic used to judge the result. Many mistakes come from mixing these layers. A small algebraic residual may not mean a small modeling error. A small step-to-step change may not mean the discrete equations are solved. A high-order truncation formula may not help when the data are noisy or the arithmetic is unstable. Keeping the layers separate makes the results on this page portable to larger examples.

A compact derivative report should include the step sizes, the base formula, and the extrapolation table. Without the table, the final extrapolated number can hide the moment when roundoff began to dominate. The best evidence for a derivative estimate is a visible plateau of stable digits across several reasonable step choices.

## Visual

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

## Code

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

## Common pitfalls

- Making $h$ extremely small and expecting a better derivative. Roundoff grows like a negative power of $h$.
- Differentiating noisy data with high-order formulas. Differentiation amplifies high-frequency noise.
- Applying Richardson extrapolation before the leading error term is actually dominant.
- Forgetting that one-sided formulas are lower order unless specially designed.
- Using a derivative estimate without checking sensitivity to several nearby step sizes.

## Connections

- [mathematical preliminaries and error analysis](/math/numerical-analysis/mathematical-preliminaries-error-analysis)
- [floating point conditioning and stability](/math/numerical-analysis/floating-point-conditioning-stability)
- [Newton Secant and polynomial roots](/math/numerical-analysis/newton-secant-polynomial-roots)
- [Newton Cotes and Romberg integration](/math/numerical-analysis/newton-cotes-romberg-integration)
