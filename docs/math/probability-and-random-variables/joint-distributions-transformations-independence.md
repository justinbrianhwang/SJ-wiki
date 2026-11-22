---
title: Joint Distributions, Transformations, and Independence
sidebar_position: 10
---

# Joint Distributions, Transformations, and Independence

Many probability questions involve several random variables defined on the same sample space. A joint distribution records how they behave together, not merely how each behaves separately. This distinction matters: the marginal laws of $X$ and $Y$ do not determine whether they are independent, positively related, negatively related, or constrained by an equation such as $Y=X^2$.

Marginalization discards coordinates; conditioning takes a slice; transformation changes coordinates. Keeping those operations distinct prevents most mistakes with joint laws. They underlie convolutions, covariance, order statistics, and conditional expectation.

## From a joint law to its margins

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

## Independence as factorization

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

The support matters when checking a proposed factorization. If a joint density is positive on a triangle such as $0\lt y\lt x\lt 1$, its support is not a Cartesian product, so the variables cannot be independent. A density written as $g(x)h(y)$ only on that triangular region does not establish independence; the indicator of the support is part of the density.

Joint distributions are also the setting for conditional densities. If $X$ and $Y$ have joint density $f_{X,Y}$, then the conditional density of $X$ given $Y=y$ is

$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$

when $f_Y(y)\gt 0$. This formula is the continuous analogue of dividing a joint probability table entry by a column total. It prepares for conditional expectation and total variance.

## Three operations on a joint law

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

## Worked example: checking independence from a joint table

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

## Worked example: transforming $X$ to $Y=X^2$

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

## A two-dimensional change of variables

Let $X$ and $Y$ be independent exponential variables with rate $1$, and define

$$
S=X+Y,\qquad R=\frac{X}{X+Y}.
$$

Here $S$ is the total and $R$ is the fraction contributed by $X$. Since $X,Y\gt 0$, the transformed support is $s\gt 0$ and $0\lt r\lt 1$. Solve for the original variables:

$$
x=rs,\qquad y=(1-r)s.
$$

The inverse Jacobian is

$$
\frac{\partial(x,y)}{\partial(s,r)}
=
\begin{pmatrix}
r&s\\
1-r&-s
\end{pmatrix},
$$

so its determinant is $-rs-s(1-r)=-s$ and the absolute determinant is $s$. The original joint density is

$$
f_{X,Y}(x,y)=e^{-x}e^{-y},\qquad x,y>0.
$$

Substitution gives

$$
\begin{aligned}
f_{S,R}(s,r)
&=e^{-rs}e^{-(1-r)s}s\\
&=se^{-s},
\qquad s>0,\ 0<r<1.
\end{aligned}
$$

This factors into

$$
\underbrace{se^{-s}}_{f_S(s)}
\underbrace{1}_{f_R(r)}.
$$

Thus $S$ and $R$ are independent, $S$ has a gamma distribution with shape $2$ and rate $1$, and $R$ is uniform on $(0,1)$. The result is less obvious in the original coordinates: knowing the sum might seem as though it should constrain the fraction, but the exponential joint density and the Jacobian cancel the dependence exactly.

Normalization checks both the formula and the support:

$$
\int_0^1\int_0^\infty se^{-s}\,ds\,dr
=1\cdot1=1.
$$

## Transformation by the CDF method

The inverse-density formula is efficient for monotone maps, but the CDF route often handles boundaries and multiple branches more safely. For $Y=X^2$ with $X$ uniform on $[-1,1]$,

$$
\begin{aligned}
F_Y(y)
&=P(X^2\le y)\\
&=P(-\sqrt y\le X\le\sqrt y)\\
&=\frac{2\sqrt y}{2}=\sqrt y,
\qquad 0\le y\le1.
\end{aligned}
$$

Differentiating gives $f_Y(y)=1/(2\sqrt y)$. The complete CDF is piecewise:

$$
F_Y(y)=
\begin{cases}
0,&y<0,\\
\sqrt y,&0\le y\le1,\\
1,&y>1.
\end{cases}
$$

Writing all pieces prevents a density formula from being applied outside its support. The divergence near zero is integrable; a density may exceed one or even become unbounded as long as its integral is one.

## Expectations without finding the transformed law

If only an expectation is wanted, deriving a new density can be wasted work. The law of the unconscious statistician gives

$$
E[g(X,Y)]=\iint g(x,y)f_{X,Y}(x,y)\,dx\,dy.
$$

For independent $X,Y\sim\operatorname{Uniform}(0,1)$, find $E[(X-Y)^2]$ directly:

$$
\begin{aligned}
E[(X-Y)^2]
&=E[X^2]-2E[XY]+E[Y^2]\\
&=\frac13-2E[X]E[Y]+\frac13\\
&=\frac23-2\left(\frac12\right)^2\\
&=\frac16.
\end{aligned}
$$

Independence is used only in $E[XY]=E[X]E[Y]$. Without it, the two marginal uniform laws would not determine the answer.

## Boundaries, atoms, and mixed laws

Not every joint distribution has a density. If $Y=X$, all mass lies on the diagonal in the plane, a set of area zero. Both coordinates can have continuous marginal densities even though the pair has no ordinary two-dimensional density. A model may also mix a point mass with a continuous component, as when a device reports exactly zero when inactive and a positive continuous reading when active.

Jacobian formulas apply to absolutely continuous pieces. Atoms must be moved and combined as probability masses. For a discrete map $Z=g(X,Y)$,

$$
P(Z=z)=\sum_{(x,y):g(x,y)=z}P(X=x,Y=y).
$$

That sum is the discrete analogue of collecting inverse branches in a continuous transformation.

## Failure modes to check

### Worked example: conditioning on a triangular support

Let the joint density be

$$
f_{X,Y}(x,y)=2,
\qquad 0<y<x<1,
$$

and zero elsewhere. Its integral is $2$ times the area of a triangle of area $1/2$, so it is normalized. Marginalizing in the correct directions gives

$$
f_X(x)=\int_0^x2\,dy=2x,
\qquad 0<x<1,
$$

and

$$
f_Y(y)=\int_y^12\,dx=2(1-y),
\qquad 0<y<1.
$$

The bounds differ because fixing $x$ permits $0\lt y\lt x$, whereas fixing $y$ permits $y\lt x\lt 1$. The variables are not independent: their support is triangular, and

$$
f_X(x)f_Y(y)=4x(1-y)
$$

does not equal the constant joint density on that triangle.

For a fixed $y$ with $0\lt y\lt 1$, the conditional density of $X$ is

$$
f_{X\mid Y}(x\mid y)
=\frac{2}{2(1-y)}
=\frac{1}{1-y},
\qquad y<x<1.
$$

Thus $X\mid Y=y$ is uniform on $(y,1)$, with

$$
E[X\mid Y=y]=\frac{1+y}{2}.
$$

Larger observed values of $Y$ force $X$ upward because the support requires $X\gt Y$. The dependence is carried entirely by the boundary even though the joint density is constant wherever it is positive.

### Jacobian orientation and normalization

The change-of-variables formula uses the determinant of the **inverse** transformation when the original density is evaluated at $x(u,v),y(u,v)$. Using the forward determinant requires taking its reciprocal. The absolute value removes orientation: swapping coordinate order changes the determinant's sign but cannot make density negative.

Three checks catch most errors. State the transformed support, integrate the proposed density to one, and map a simple interior point through both directions. A correct algebraic determinant paired with a wrong support still gives a wrong distribution.

- Assuming marginals determine the joint distribution. They do not.
- Checking independence at only one point in a joint table. A single mismatch disproves independence, but agreement at one entry proves nothing.
- Forgetting the absolute derivative factor when transforming a density.
- Using a one-to-one change-of-variables formula for a many-to-one map like $Y=X^2$.
- Treating zero-probability conditioning events in continuous models as if the elementary discrete formula applies unchanged.

## Dependence beyond factorization

Boundary points usually have probability zero for an absolutely continuous law, so strict or non-strict inequalities there do not change probabilities. The boundary can still control an answer by setting integration limits. Mixed laws require separate bookkeeping: a transformation may send an entire region or line to one value and thereby create an atom. Before applying a density formula, check whether the transformed variable can equal some value with positive probability.

### Same marginals, several possible couplings

A **coupling** is any joint distribution with specified marginals. Let $U$ be uniform on $(0,1)$. The pairs $(U,U)$, $(U,1-U)$, and $(U,V)$ with an independent uniform $V$ all have uniform marginal laws. Their dependence is respectively perfectly increasing, perfectly decreasing, and independent.

The difference appears in functions of both coordinates. For the sum,

$$
U+U=2U,\qquad U+(1-U)=1,
$$

while $U+V$ has a triangular density. Thus knowing two marginal distributions cannot determine the variance of a portfolio, the probability of simultaneous failure, or the law of a sum.

Covariance distinguishes these three examples:

$$
\operatorname{Cov}(U,U)=\frac1{12},\qquad
\operatorname{Cov}(U,1-U)=-\frac1{12},\qquad
\operatorname{Cov}(U,V)=0.
$$

Zero covariance alone still does not prove independence. If $X$ is uniform on $[-1,1]$ and $Y=X^2$, symmetry gives $E[XY]=E[X^3]=0$ and $E[X]=0$, hence covariance zero. Yet $Y$ is completely determined by $X$.

For continuous marginals, a copula records the dependence after transforming each coordinate to a uniform scale. Sklar's representation writes a joint CDF as

$$
F_{X,Y}(x,y)=C(F_X(x),F_Y(y)).
$$

Independence corresponds to $C(u,v)=uv$. The formalism separates marginal behavior from dependence, which is useful when component distributions are well understood but their joint extremes are not. A correlation coefficient captures only one aspect of that dependence and can miss asymmetric or nonlinear tail association.

When building a model from marginals, independence is therefore an additional modeling choice, not a neutral default forced by the data. It should be supported by the mechanism or checked against joint observations.

## Related pages

- [Conditional probability, Bayes, and independence](/math/probability-and-random-variables/conditional-probability-bayes-independence)
- [Continuous random variables and uniform laws](/math/probability-and-random-variables/continuous-random-variables-and-uniform-laws)
- [Sums, convolutions, and order statistics](/math/probability-and-random-variables/sums-convolutions-order-statistics)
- [Covariance, correlation, and conditional expectation](/math/probability-and-random-variables/covariance-correlation-conditional-expectation)
