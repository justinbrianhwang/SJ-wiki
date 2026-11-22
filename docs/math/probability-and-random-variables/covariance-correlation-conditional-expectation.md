---
title: Covariance, Correlation, and Conditional Expectation
sidebar_position: 12
---

# Covariance, Correlation, and Conditional Expectation

Variance measures how one random variable spreads around its mean. Covariance measures how two variables move together. Conditional expectation gives the best average prediction after observing information. The ideas meet in the law of total variance and in problems where one random variable is used to predict another.

MIT 18.440 develops covariance and correlation before conditional expectation. Two warnings recur: independence implies zero covariance, but zero covariance does not imply independence; conditional expectation can behave counterintuitively when the relevant expectations are infinite or the conditioning information is misunderstood.

## What covariance and correlation record

For random variables $X,Y$ with finite second moments, the **covariance** is

$$
\operatorname{Cov}(X,Y)
=E[(X-E[X])(Y-E[Y])].
$$

Equivalently,

$$
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].
$$

Covariance is bilinear:

$$
\operatorname{Cov}(aX+bY,Z)
=a\operatorname{Cov}(X,Z)+b\operatorname{Cov}(Y,Z),
$$

and similarly in the second argument. It follows that

$$
\operatorname{Var}(X+Y)
=
\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y).
$$

Positive covariance increases the variance of a sum, while negative covariance decreases it. Negatively correlated assets can therefore reduce portfolio variance. In probability calculations, covariance terms account for indicator variables that are not independent.

The **correlation coefficient** is

$$
\rho(X,Y)=
\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}},
$$

provided both variances are positive and finite. Covariance depends on units: changing height from meters to centimeters multiplies its covariance with another variable by $100$. Correlation divides by the standard deviations, so it is unitless and lies between $-1$ and $1$.

Values near $1$ or $-1$ indicate strong linear association. A value near $0$ indicates little linear association, not the absence of every relationship. If $X$ and $Y$ are independent, then $E[XY]=E[X]E[Y]$ and their covariance is zero; the converse fails. Correlation is undefined when either variance is zero.

The bound $\vert \rho\vert \leq1$ is Cauchy--Schwarz applied to the centered variables:

$$
|E[(X-E[X])(Y-E[Y])]|^2
\leq E[(X-E[X])^2]E[(Y-E[Y])^2].
$$

Equality holds exactly when the centered variables are linearly dependent almost surely. Thus $\rho=1$ means $Y=aX+b$ almost surely with $a\gt 0$, and $\rho=-1$ means the slope is negative. A high correlation need not mean equality of values or equality of distributions.

For a direct counterexample to the converse of independence, let $X$ be uniform on $\{-1,0,1\}$ and set $Y=X^2$. The variables are dependent because $Y$ is determined by $X$. Symmetry gives $E[X]=0$ and $E[XY]=E[X^3]=0$, so

$$
\operatorname{Cov}(X,Y)=0-E[X]E[Y]=0.
$$

The relationship is entirely nonlinear and Pearson correlation does not record it.

For a random vector $X=(X_1,\ldots,X_d)^T$, the covariance matrix has entries $\Sigma_{ij}=\operatorname{Cov}(X_i,X_j)$. It is symmetric and positive semidefinite because for every vector $a$,

$$
a^T\Sigma a=\operatorname{Var}(a^TX)\geq0.
$$

Diagonal entries are variances; off-diagonal entries determine how linear combinations co-vary. A singular covariance matrix means some nonzero linear combination has zero variance and is therefore constant almost surely.

## Conditioning selects a new distribution

For jointly discrete random variables, the **conditional mass function** of $X$ given $Y=y$ is

$$
p_{X\mid Y}(x\mid y)
=
\frac{p_{X,Y}(x,y)}{p_Y(y)},
$$

when $p_Y(y)\gt 0$. Its mean is

$$
E[X\mid Y=y]=\sum_x x\,p_{X\mid Y}(x\mid y).
$$

The direction of conditioning matters: $E[X\mid Y=y]$ and $E[Y\mid X=x]$ generally answer different questions.

As $y$ varies, the conditional means form a function. Evaluating that function at the random value $Y$ gives $E[X\mid Y]$, which is itself a random variable rather than a single number. It can be read as averaging $X$ under the probability law selected by the observed value of $Y$.

The broader definition conditions on information represented by a sigma-algebra $\mathcal G$. The random variable $E[X\mid\mathcal G]$ must be $\mathcal G$-measurable and satisfy

$$
E[X\mathbf1_G]=E[E[X\mid\mathcal G]\mathbf1_G]
$$

for every event $G\in\mathcal G$. It is unique up to events of probability zero. Conditioning on $Y$ means taking $\mathcal G=\sigma(Y)$, the information revealed by knowing $Y$.

Several calculation rules follow. Constants and known quantities can be pulled out:

$$
E[Z X\mid\mathcal G]=Z E[X\mid\mathcal G]
$$

when $Z$ is $\mathcal G$-measurable and integrability holds. If $X$ is independent of $\mathcal G$, then $E[X\mid\mathcal G]=E[X]$. For nested information $\mathcal H\subseteq\mathcal G$, the tower property says

$$
E[E[X\mid\mathcal G]\mid\mathcal H]=E[X\mid\mathcal H].
$$

Conditioning in the reverse order generally cannot be simplified unless the sigma-algebras are nested.

## Splitting variation across conditional slices

The **law of total expectation** is

$$
E[E[X\mid Y]]=E[X].
$$

There are two equivalent ways to average: directly, or first within each conditional slice and then across the slice means. A class average computed from section averages needs the same weighting by section size.

The **law of total variance** is

$$
\operatorname{Var}(X)
=
\operatorname{Var}(E[X\mid Y])
+E[\operatorname{Var}(X\mid Y)].
$$

The first term measures variation in the conditional means; the second is the average variation remaining within a slice.

To derive it, write $m(Y)=E[X\mid Y]$ and decompose

$$
X-E[X]=(X-m(Y))+(m(Y)-E[X]).
$$

After squaring and taking expectations, the cross term vanishes:

$$
\begin{aligned}
E[(X-m(Y))(m(Y)-E[X])]
&=E\left[(m(Y)-E[X])E[X-m(Y)\mid Y]\right]\\
&=0.
\end{aligned}
$$

The squared first term averages to $E[\operatorname{Var}(X\mid Y)]$; the second is $\operatorname{Var}(E[X\mid Y])$. The identity is an orthogonal decomposition of centered variation.

```mermaid
graph TD
  A["Observe Y"] --> B["Conditional distribution of X"]
  B --> C["Conditional mean: E#lsqb;X | Y"]"]
  B --> D["Conditional variance: Var(X | Y)"]
  C --> E["Variation between slice means"]
  D --> F["Variation remaining within slices"]
  E --> G["Total variance"]
  F --> G
```

| Quantity | Formula | Role |
|---|---|---|
| Covariance | $E[XY]-E[X]E[Y]$ | signed joint variation |
| Correlation | covariance divided by standard deviations | unitless linear association |
| Conditional mean | $E[X\mid Y=y]$ | average after observing $Y=y$ |
| Total expectation | $E[E[X\mid Y]]=E[X]$ | average the conditional averages |
| Total variance | $\operatorname{Var}(E[X\mid Y])+E[\operatorname{Var}(X\mid Y)]$ | between-slice plus within-slice spread |

Covariance and conditional expectation answer related but distinct questions. Covariance gives one number for linear co-movement. Conditional expectation gives a function describing the average of $X$ at each observed value of $Y$. The views align closely when that function is linear; a nonlinear conditional mean can carry structure that covariance misses.

## Conditional expectation as a least-squares predictor

For square-integrable $X$, the mean-square error

$$
E[(X-g(Y))^2]
$$

is minimized over functions of $Y$ by $g(Y)=E[X\mid Y]$. With squared-error loss and information $Y$, no other function of $Y$ has lower average loss. A regression curve estimates such a conditional mean, while residual variance measures what remains after conditioning on the predictors.

The proof mirrors least squares in Euclidean space. Put $m(Y)=E[X\mid Y]$. For any square-integrable $g(Y)$,

$$
\begin{aligned}
E[(X-g(Y))^2]
&=E[(X-m(Y)+m(Y)-g(Y))^2]\\
&=E[(X-m(Y))^2]+E[(m(Y)-g(Y))^2],
\end{aligned}
$$

because the cross term has conditional expectation zero. The first term does not depend on $g$, and the second is nonnegative. Conditional expectation is therefore the orthogonal projection of $X$ onto the square-integrable functions of the observed information.

Restricting predictors to affine functions $a+bY$ gives the best linear predictor instead. When $\operatorname{Var}(Y)\gt 0$, differentiation yields

$$
b=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)},
\qquad a=E[X]-bE[Y].
$$

This equals the full conditional expectation only when $E[X\mid Y]$ is affine. Jointly Gaussian variables have that property, but general distributions do not. The earlier example $Y=X^2$ has zero linear slope in predicting $Y$ from $X$, despite perfect nonlinear predictability.

The same interpretation leads to martingales: successive conditional expectations are revised best guesses as information arrives. Finiteness assumptions matter throughout; identities involving conditional expectations may be meaningless when the required expectations do not exist.

## A signal plus independent noise

Let $X$ and $Y$ be independent with $E[X]=E[Y]=0$, variances $\sigma_X^2$ and $\sigma_Y^2$, and set $Z=X+Y$. Bilinearity gives

$$
\begin{aligned}
\operatorname{Cov}(X,Z)
&=\operatorname{Cov}(X,X+Y) \\
&=\operatorname{Cov}(X,X)+\operatorname{Cov}(X,Y) \\
&=\sigma_X^2.
\end{aligned}
$$

Independence also gives

$$
\operatorname{Var}(Z)=\sigma_X^2+\sigma_Y^2,
$$

so

$$
\rho(X,Z)
=
\frac{\sigma_X^2}
{\sigma_X\sqrt{\sigma_X^2+\sigma_Y^2}}
=
\frac{\sigma_X}{\sqrt{\sigma_X^2+\sigma_Y^2}}.
$$

Large $\sigma_Y^2$ means that $Z$ contains substantial noise unrelated to $X$, reducing the correlation. At $\sigma_Y^2=0$, $Z=X$ and the correlation is $1$.

## Reading one die from the observed sum

Roll two fair dice. Let $X$ be the first die, $Y$ the second, and $Z=X+Y$. Conditional on $Z=5$, the possible outcomes are

$$
(1,4),(2,3),(3,2),(4,1).
$$

They remain equally likely, so $X$ is conditionally uniform on $\{1,2,3,4\}$ and

$$
E[X\mid Z=5]
=\frac{1+2+3+4}{4}
=\frac52.
$$

Symmetry gives a quick check: the two dice have equal conditional expectations, and those expectations add to $5$.

The symmetry works for every attainable sum. Because $X$ and $Y$ are exchangeable and $X+Y=Z$,

$$
E[X\mid Z]+E[Y\mid Z]=E[Z\mid Z]=Z,
$$

while exchangeability gives $E[X\mid Z]=E[Y\mid Z]$. Hence

$$
E[X\mid Z]=\frac Z2.
$$

The result is linear even though the conditional distribution changes shape near sums $2$ and $12$.

It also gives a total-variance check. Since $\operatorname{Var}(X)=35/12$ and $\operatorname{Var}(Z)=35/6$ for two independent fair dice,

$$
\operatorname{Var}(E[X\mid Z])
=\operatorname{Var}(Z/2)=\frac{35}{24}.
$$

Therefore

$$
E[\operatorname{Var}(X\mid Z)]
=\frac{35}{12}-\frac{35}{24}
=\frac{35}{24}.
$$

Exactly half the variance of one die is explained, in mean-square terms, by observing the sum.

## Enumerating the examples

```python
from collections import defaultdict

# Conditional expectation for dice.
outcomes = [(x, y) for x in range(1, 7) for y in range(1, 7)]
groups = defaultdict(list)
for x, y in outcomes:
    groups[x + y].append(x)

for z in [5, 7, 10]:
    print(z, sum(groups[z]) / len(groups[z]))

# Covariance and correlation for X and Z = X + Y.
sigma_x = 2.0
sigma_y = 3.0
cov_xz = sigma_x ** 2
var_z = sigma_x ** 2 + sigma_y ** 2
corr_xz = cov_xz / (sigma_x * (var_z ** 0.5))
print("Cov(X,Z):", cov_xz)
print("Corr(X,Z):", corr_xz)
```

## Total covariance

Conditioning also decomposes covariance. Add and subtract conditional means, then use the same vanishing cross-term argument as for total variance:

$$
\operatorname{Cov}(X,Z)
=E[\operatorname{Cov}(X,Z\mid Y)]
+\operatorname{Cov}(E[X\mid Y],E[Z\mid Y]).
$$

The first term is average within-slice co-movement; the second is co-movement of slice means. Setting $Z=X$ recovers total variance. The identity is useful when dependence is induced by a shared group. Two measurements may be conditionally independent given a group label and still be positively correlated marginally because groups have different means.

For example, suppose $Y$ selects one of two populations with equal probability. Conditional on $Y=0$, let independent $X$ and $Z$ each have mean $0$; conditional on $Y=1$, let them be independent with mean $10$. Their conditional covariance is zero in both groups. Yet the covariance of their conditional means is the variance of $10Y$, equal to $25$. Pooling the groups creates strong association without within-group association. Reversals of this kind underlie Simpson-type effects.

## Sample covariance is an estimator

Given paired observations $(x_i,y_i)$, the usual sample covariance is

$$
s_{xy}=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y).
$$

The divisor $n-1$ makes it unbiased for population covariance under independent identical sampling with finite second moments. Dividing by $n$ gives the empirical-distribution covariance and is also the maximum-likelihood convention in some Gaussian calculations. The chosen denominator should be stated when small samples matter.

Sample correlation is a ratio of random quantities. It can be noisy, especially with few observations or heavy tails, and one outlying pair can dominate both covariance and standard deviations. A scatterplot or residual analysis remains necessary even though a decorative plot is not needed for the definition.

Serial data require more care. Treating dependent time points as independent pairs understates uncertainty. Lag-$k$ autocovariance compares $X_t$ with $X_{t+k}$ and describes persistence; effective sample size depends on the whole dependence pattern rather than the number of rows alone.

## Conditioning a mixture

Let $Y$ be Bernoulli with $P(Y=1)=p$. Conditional on $Y$, suppose $X$ has mean $\mu_Y$ and variance $\sigma_Y^2$. Total expectation gives

$$
E[X]=(1-p)\mu_0+p\mu_1.
$$

Total variance gives

$$
\operatorname{Var}(X)
=(1-p)\sigma_0^2+p\sigma_1^2
+p(1-p)(\mu_1-\mu_0)^2.
$$

The first two terms average within-group spread. The final term is between-group spread and remains even if both conditional variances are zero. For $p=1/2$, $\mu_0=0$, $\mu_1=4$, and both conditional variances equal $1$, the total variance is $1+4=5$. Directly, the mixture mean is $2$ and each component mean lies two units from it, confirming the calculation.

This decomposition also warns against replacing a mixture by a single distribution having only the averaged conditional variance. Variation of the conditional mean is part of the marginal uncertainty.

## Interpretive checks

- Correlation has no meaning when a variance is zero, and it can be unstable when a variance is merely tiny. Report the scale and sample size beside an estimated correlation.
- Pairwise zero covariance does not imply joint independence. The implication does hold for jointly Gaussian vectors, a special structural fact rather than a general rule.
- $E[X\mid Y]$ is a function of the random variable $Y$; $E[X\mid Y=y]$ is a number for a specified value. Confusing them often leads to missing an outer expectation.
- Events with probability zero require a regular conditional distribution or another measure-theoretic construction. The elementary ratio formula cannot condition on $P(Y=y)=0$ for a continuous $Y$.
- The tower property needs nested information. Expressions such as $E[E[X\mid Y]\mid Z]$ do not collapse to $E[X\mid Z]$ without an inclusion relation or additional assumptions.

## Conditional expectation with continuous variables

If $(X,Y)$ has a joint density and $f_Y(y)\gt 0$, then

$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)},
\qquad
E[X\mid Y=y]=\int x f_{X\mid Y}(x\mid y)\,dx.
$$

The event $Y=y$ has probability zero, so this is not the elementary ratio of event probabilities. A conditional density is a version defined for almost every $y$; changing it on a zero-probability set does not change $E[X\mid Y]$ as a random variable.

For independent standard normal $X$ and $N$, let $Y=X+N$. The pair $(X,Y)$ is jointly Gaussian, with covariance $1$ and $\operatorname{Var}(Y)=2$. The best linear predictor is therefore

$$
E[X\mid Y]=\frac12Y.
$$

Joint Gaussianity makes the conditional mean exactly linear, not merely the best linear approximation. Its explained variance is $\operatorname{Var}(Y/2)=1/2$, and total variance leaves conditional variance $1/2$. Observing a noisy sum cuts the mean-square uncertainty in half in this equal-variance case.

If the noise variance were $\tau^2$ and signal variance $\sigma^2$, the coefficient would become $\sigma^2/(\sigma^2+\tau^2)$. The predictor shrinks a noisy observation toward the prior mean; larger noise produces stronger shrinkage.

## Existence assumptions

Covariance requires integrability of the product, usually guaranteed by finite second moments. Correlation additionally requires positive finite variances. Conditional expectation $E[X\mid\mathcal G]$ needs $E\vert X\vert \lt \infty$ in the standard definition. Heavy-tailed variables can violate these assumptions even when simulated samples look ordinary.

For nonnegative $X$, an extended conditional expectation can be defined even when the mean is infinite, but subtraction identities may then involve undefined expressions such as infinity minus infinity. Checking finiteness before applying covariance or total-variance algebra is part of the calculation, not a technical afterthought.

<div className="see-also">

See also: [Discrete random variables, expectation, and variance](/math/probability-and-random-variables/discrete-random-variables-expectation-variance) · [Joint distributions, transformations, and independence](/math/probability-and-random-variables/joint-distributions-transformations-independence) · [Sums, convolutions, and order statistics](/math/probability-and-random-variables/sums-convolutions-order-statistics) · [Martingales, risk-neutral probability, and Black-Scholes](/math/probability-and-random-variables/martingales-risk-neutral-probability-black-scholes) · [Covariance, correlation, and independence](/math/probability/covariance-correlation-independence)

</div>
