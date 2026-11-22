---
title: Joint Distributions, Transformations, and Independence
sidebar_position: 10
---

# Joint Distributions, Transformations, and Independence

Many probability questions involve several random variables defined on the same sample space. A joint distribution records how they behave together, not merely how each behaves separately. This distinction matters: the marginal laws of $X$ and $Y$ do not determine whether they are independent, positively related, negatively related, or constrained by an equation such as $Y=X^2$.

MIT 18.440 introduces joint mass functions, joint densities, marginal distributions, independent random variables, and distributions of functions of random variables. These ideas are the technical foundation for convolutions, conditional densities, covariance, order statistics, and the transform methods used later in the course.

## Definitions

For discrete random variables $X$ and $Y$, the **joint probability mass function** is

$$
p_{X,Y}(x,y)=P(X=x,\ Y=y).
$$

The marginal mass functions are obtained by summing:

$$
p_X(x)=\sum_y p_{X,Y}(x,y),
\qquad
p_Y(y)=\sum_x p_{X,Y}(x,y).
$$

For continuous random variables, a **joint density** $f_{X,Y}$ satisfies

$$
P((X,Y)\in A)=\iint_A f_{X,Y}(x,y)\,dx\,dy.
$$

The marginal densities are

$$
f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy,
\qquad
f_Y(y)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx.
$$

Random variables $X$ and $Y$ are **independent** if for all suitable sets $A,B$,

$$
P(X\in A,\ Y\in B)=P(X\in A)P(Y\in B).
$$

In the discrete case, this is equivalent to

$$
p_{X,Y}(x,y)=p_X(x)p_Y(y)
$$

for all $x,y$. In the continuous case, it is equivalent to

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y)
$$

where densities are defined.

## Key results

If $Y=g(X)$ and $g$ is strictly increasing, then

$$
F_Y(a)=P(Y\le a)=P(g(X)\le a)=P(X\le g^{-1}(a))=F_X(g^{-1}(a)).
$$

If $g$ is differentiable with differentiable inverse, the density form is

$$
f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|.
$$

For a non-one-to-one transformation, sum the contributions from each preimage:

$$
f_Y(y)=\sum_{x:g(x)=y} f_X(x)\left|\frac{d}{dy}x(y)\right|.
$$

For a two-dimensional differentiable one-to-one transformation $(U,V)=T(X,Y)$ with inverse $(x,y)=T^{-1}(u,v)$,

$$
f_{U,V}(u,v)
=
f_{X,Y}(x(u,v),y(u,v))
\left|
\det
\frac{\partial(x,y)}{\partial(u,v)}
\right|.
$$

Even when two random variables have the same marginal distribution, their joint laws can be completely different. For example, if $X$ is uniform on $[0,1]$, then $Y=X$ has the same marginal as $X$ but is not independent of $X$. If $Y$ is separately sampled uniform on $[0,1]$, then $X$ and $Y$ can be independent.

The marginalization formulas are probability versions of "ignore one coordinate". In a joint table, summing a row forgets which value of $Y$ occurred and keeps only the value of $X$. In a joint density, integrating over $y$ performs the same operation continuously. This operation always loses information: many different joint laws can have the same marginals.

Independence is a factorization statement. In a finite table, every entry must equal row sum times column sum. Geometrically, the joint distribution has no interaction term; the probability assigned to a rectangle $A\times B$ is the product of the two side probabilities. For continuous variables, this means the density surface separates into an $x$-part and a $y$-part.

Transformations require special care because density is tied to scale. If $Y=2X$, intervals in $Y$ correspond to intervals half as long in $X$, so the density height changes by a factor of $1/2$. The derivative factor in the change-of-variables formula is exactly this scale correction. In multiple dimensions, the absolute Jacobian determinant measures how areas or volumes are distorted.

The transformation method has two complementary approaches. The CDF method asks for $P(g(X)\le a)$ and is often best when the event has a simple inequality description. The density method uses inverse branches and derivatives and is often faster when the transformation is monotone or piecewise monotone. Both methods should give the same answer when applied correctly.

Joint distributions are also the setting for conditional densities. If $X$ and $Y$ have joint density $f_{X,Y}$, then the conditional density of $X$ given $Y=y$ is formally

$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$

when $f_Y(y)\gt 0$. This formula is the continuous analogue of dividing a joint probability table entry by a column total. It prepares for conditional expectation and total variance.

## Visual

```text
Discrete joint law as a matrix

             Y=1       Y=2       row sum pX
X=1        p11       p12       p1.
X=2        p21       p22       p2.

column     p.1       p.2       total 1
sum pY
```

| Operation | Discrete version | Continuous version |
|---|---|---|
| Joint law | $p_{X,Y}(x,y)$ | $f_{X,Y}(x,y)$ |
| Marginal of $X$ | $\sum_y p_{X,Y}(x,y)$ | $\int f_{X,Y}(x,y)\,dy$ |
| Independence | $p_{X,Y}=p_Xp_Y$ | $f_{X,Y}=f_Xf_Y$ |
| Probability of region | sum over grid points | double integral over region |
| Transformation | collect masses with same value | density times Jacobian |

The matrix picture is a useful diagnostic for independence. Once row and column sums are known, an independent joint table is forced: it must be the outer product of the marginal vectors. If the actual table differs from that outer product, the variables are dependent. For continuous variables, the same idea is harder to see visually, but a product density has rectangular probabilities that factor exactly.

For transformations, the table reminds us that discrete and continuous cases use different bookkeeping. A discrete transformation moves point masses and combines masses that land on the same value. A continuous transformation moves density through a change of scale. Forgetting this distinction leads to common errors such as assigning positive probability to a point in a continuous model or omitting a Jacobian factor.

## Worked example 1: checking independence from a joint table

Problem: Let $X,Y$ take values in $\{0,1\}$ with joint probabilities

|  | $Y=0$ | $Y=1$ |
|---|---:|---:|
| $X=0$ | $0.30$ | $0.20$ |
| $X=1$ | $0.15$ | $0.35$ |

Find the marginal distributions and decide whether $X$ and $Y$ are independent.

Method:

1. Sum rows for $X$:

$$
P(X=0)=0.30+0.20=0.50,
$$

$$
P(X=1)=0.15+0.35=0.50.
$$

2. Sum columns for $Y$:

$$
P(Y=0)=0.30+0.15=0.45,
$$

$$
P(Y=1)=0.20+0.35=0.55.
$$

3. If independent, we would need

$$
P(X=0,Y=0)=P(X=0)P(Y=0)=0.50\cdot0.45=0.225.
$$

4. But the table gives

$$
P(X=0,Y=0)=0.30.
$$

Checked answer: $X$ and $Y$ are not independent. The marginals alone do not reveal this; the joint table does.

## Worked example 2: transforming $X$ to $Y=X^2$

Problem: Let $X$ be uniform on $[-1,1]$ and define $Y=X^2$. Find the density of $Y$.

Method:

1. The support of $Y$ is $[0,1]$.
2. For $0\lt y\lt 1$, the equation $x^2=y$ has two solutions:

$$
x=\sqrt y,\qquad x=-\sqrt y.
$$

3. The density of $X$ is $f_X(x)=1/2$ on $[-1,1]$.
4. For the positive branch, $x=\sqrt y$, so

$$
\left|\frac{dx}{dy}\right|=\frac{1}{2\sqrt y}.
$$

5. For the negative branch, $x=-\sqrt y$, so

$$
\left|\frac{dx}{dy}\right|=\frac{1}{2\sqrt y}.
$$

6. Add both contributions:

$$
f_Y(y)=\frac12\cdot\frac{1}{2\sqrt y}
+\frac12\cdot\frac{1}{2\sqrt y}
=\frac{1}{2\sqrt y},
\qquad 0<y<1.
$$

Checked answer: integrate the density:

$$
\int_0^1 \frac{1}{2\sqrt y}\,dy
=\left[\sqrt y\right]_0^1
=1.
$$

So it is a valid density.

## Code

```python
import numpy as np

joint = np.array([[0.30, 0.20],
                  [0.15, 0.35]])

px = joint.sum(axis=1)
py = joint.sum(axis=0)
independent_table = np.outer(px, py)

print("pX:", px)
print("pY:", py)
print("independent table would be:")
print(independent_table)
print("is independent?", np.allclose(joint, independent_table))

def density_y_square(y):
    y = np.asarray(y)
    out = np.zeros_like(y, dtype=float)
    mask = (y > 0) & (y < 1)
    out[mask] = 1 / (2 * np.sqrt(y[mask]))
    return out

grid = np.linspace(0.001, 0.999, 1000)
approx_integral = np.trapz(density_y_square(grid), grid)
print("approx integral:", approx_integral)
```

## Common pitfalls

- Assuming marginals determine the joint distribution. They do not.
- Checking independence at only one point in a joint table. Independence requires factorization everywhere.
- Forgetting the absolute derivative factor when transforming a density.
- Using a one-to-one change-of-variables formula for a many-to-one map like $Y=X^2$.
- Treating zero-probability conditioning events in continuous models as if the elementary discrete formula applies unchanged.

## Connections

- [Conditional probability, Bayes, and independence](/math/probability-and-random-variables/conditional-probability-bayes-independence)
- [Continuous random variables and uniform laws](/math/probability-and-random-variables/continuous-random-variables-and-uniform-laws)
- [Sums, convolutions, and order statistics](/math/probability-and-random-variables/sums-convolutions-order-statistics)
- [Covariance, correlation, and conditional expectation](/math/probability-and-random-variables/covariance-correlation-conditional-expectation)
- [Joint, marginal, and conditional distributions](/math/probability/joint-marginal-conditional-distributions)
