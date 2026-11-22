---
title: Discrete Random Variables, Expectation, and Variance
sidebar_position: 5
---

# Discrete Random Variables, Expectation, and Variance

A probability model begins with outcomes, but raw outcomes are often more detailed than the question requires. A sequence of ten coin tosses records their order; the number of heads discards that order and retains one integer. A random variable performs this compression. It assigns a number to each outcome so that numerical questions can replace set-by-set bookkeeping.

Expectation and variance then summarize the induced distribution. Expectation is a probability-weighted average, while variance measures squared distance from that average. Neither number identifies a distribution by itself. Their value comes from algebra: expectations of sums separate cleanly, and variances of sums can be analyzed through covariance.

## A random variable is a function

Let $\Omega$ be the sample space. A random variable is a function

$$
X:\Omega\to\mathbb R.
$$

For a die roll, an outcome might be the physical landing configuration, while $X$ reports the number of pips on the upper face. For three coin tosses, the outcome HHT might be mapped to $X=2$, the number of heads. Different outcomes can map to the same value.

A random variable is **discrete** when its possible values form a finite or countable set. Its probability mass function, or PMF, is

$$
p_X(x)=P(X=x).
$$

A valid PMF satisfies

$$
p_X(x)\ge0,
\qquad
\sum_x p_X(x)=1.
$$

The sum ranges over the support, the values with positive mass. The cumulative distribution function is

$$
F_X(a)=P(X\le a)=\sum_{x\le a}p_X(x).
$$

For a discrete variable the CDF is a step function. Its jump at $x$ has size $p_X(x)$:

$$
p_X(x)=F_X(x)-F_X(x^-),
$$

where $F_X(x^-)$ is the limit from the left. The PMF and CDF both determine the full distribution, while the mean and variance retain only selected features.

Between support points the CDF stays constant. At an integer support value it includes the mass at that value, so its right-continuity matters when translating inequalities. In particular, $P(X\lt a)$ and $P(X\le a)$ can differ by $P(X=a)$; endpoint conventions cannot be discarded as they can for a variable with a density.

| Object | Formula | Information retained |
|---|---|---|
| PMF | $p_X(x)=P(X=x)$ | mass at each possible value |
| CDF | $F_X(a)=P(X\le a)$ | all lower-tail probabilities |
| Mean | $E[X]$ | probability-weighted center |
| Second moment | $E[X^2]$ | average squared magnitude |
| Variance | $E[(X-E[X])^2]$ | squared spread around the mean |
| Standard deviation | $\sqrt{\operatorname{Var}(X)}$ | spread in the units of $X$ |

## Expectation as a weighted average

For a discrete $X$ with finite absolute mean,

$$
E[X]=\sum_x x p_X(x),
\qquad
\sum_x |x|p_X(x)<\infty.
$$

Absolute convergence matters for an infinite support. It permits rearranging and grouping terms without changing the result. For a nonnegative variable, the sum always has a well-defined extended value, but that value may be $+\infty$.

The same expectation may be computed on the original sample space:

$$
E[X]=\sum_{\omega\in\Omega}X(\omega)P(\{\omega\}).
$$

Grouping outcomes that share the same value of $X$ turns this expression into the PMF formula. That grouping also proves the transformation rule often called LOTUS, the law of the unconscious statistician:

$$
E[g(X)]=\sum_x g(x)p_X(x).
$$

There is no need to derive the PMF of $Y=g(X)$ first. For instance, $E[X^2]$ follows directly by placing $g(x)=x^2$ into the sum.

Expectation need not be a possible value. A fair die has mean $3.5$. Nor does it have to be the most probable value: a distribution can have a unique mode far from its mean if a thin tail contains large values. The long-run interpretation also needs care. Under suitable independence and integrability assumptions, the sample average of repeated copies approaches the expectation. The definition itself is the weighted sum, not a promise about a short run of observations.

## Why linearity is so effective

For constants $a,b$ and integrable random variables $X,Y$,

$$
E[aX+bY]=aE[X]+bE[Y].
$$

On a countable sample space, the proof is direct:

$$
\begin{aligned}
E[aX+bY]
&=\sum_{\omega\in\Omega}
\bigl(aX(\omega)+bY(\omega)\bigr)P(\{\omega\})\\
&=a\sum_{\omega\in\Omega}X(\omega)P(\{\omega\})
+b\sum_{\omega\in\Omega}Y(\omega)P(\{\omega\})\\
&=aE[X]+bE[Y].
\end{aligned}
$$

No independence was used. Dependence changes joint probabilities, but addition distributes before those probabilities are summed. By induction,

$$
E\!\left[\sum_{i=1}^n X_i\right]
=\sum_{i=1}^n E[X_i].
$$

This identity is especially strong when the distribution of the sum is unpleasant. Computing an expected count often requires only one-event probabilities, whereas computing the entire PMF may require inclusion-exclusion or a recurrence.

Conditional convergence is a boundary to the usual algebra. If positive and negative parts both have infinite expectation, symbols such as $\infty-\infty$ do not define a mean. Linearity should then not be applied as if all terms were finite.

## Indicators turn counting into addition

For an event $A$, its indicator is

$$
\mathbf 1_A=
\begin{cases}
1, & A\text{ occurs},\\
0, & A\text{ does not occur}.
\end{cases}
$$

Its expectation is exactly the probability of the event:

$$
E[\mathbf 1_A]
=0\cdot P(A^c)+1\cdot P(A)
=P(A).
$$

Suppose $X$ counts how many of the events $A_1,\ldots,A_n$ occur. Pointwise,

$$
X=\sum_{i=1}^n \mathbf 1_{A_i}.
$$

Linearity gives

$$
E[X]=\sum_{i=1}^n P(A_i).
$$

The events may overlap heavily. For example, birthday matches among people are dependent, fixed points in a permutation are dependent, and occupied bins in an allocation model are dependent. The expected count still separates. Independence becomes relevant when one asks for the variance or the probability of a particular count.

Another useful indicator identity counts unordered pairs. If $X$ is the number of matching pairs among $n$ objects, write one indicator for each pair rather than one for each object:

$$
X=\sum_{1\le i<j\le n}\mathbf 1_{\{i\text{ matches }j\}}.
$$

Choosing the objects indexed by the count correctly is often the main step. Once that representation is found, the expectation usually follows in a few lines.

## Variance and its algebra

Let $\mu=E[X]$. If $E[X^2]\lt \infty$, the variance is

$$
\operatorname{Var}(X)=E[(X-\mu)^2].
$$

It is nonnegative and equals zero exactly when $X$ is constant with probability one. Expanding the square yields the computational formula:

$$
\begin{aligned}
\operatorname{Var}(X)
&=E[X^2-2\mu X+\mu^2]\\
&=E[X^2]-2\mu E[X]+\mu^2\\
&=E[X^2]-\mu^2.
\end{aligned}
$$

The centered definition is conceptually clearer; the second-moment formula is often faster. A useful numerical warning accompanies it: subtracting two nearly equal floating-point numbers can lose precision. Directly accumulating centered squared deviations, or using a stable online algorithm, is safer in computation.

Shifts and scales behave differently:

$$
\begin{aligned}
E[aX+b]&=aE[X]+b,\\
\operatorname{Var}(aX+b)&=a^2\operatorname{Var}(X).
\end{aligned}
$$

Adding $b$ moves every value and the mean by the same amount, leaving deviations unchanged. Multiplying by $a$ multiplies each deviation by $a$, so its square gains a factor $a^2$. Variance has squared units; standard deviation restores the original units.

Variance is not linear. For two square-integrable variables,

$$
\operatorname{Var}(X+Y)
=\operatorname{Var}(X)+\operatorname{Var}(Y)
+2\operatorname{Cov}(X,Y),
$$

where

$$
\operatorname{Cov}(X,Y)
=E[(X-E[X])(Y-E[Y])]
=E[XY]-E[X]E[Y].
$$

Independence implies zero covariance, and then variances add. The converse is false in general: uncorrelated variables can still be dependent. For a longer sum,

$$
\operatorname{Var}\!\left(\sum_{i=1}^n X_i\right)
=\sum_{i=1}^n\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).
$$

The covariance terms record whether the components tend to move together or in opposite directions.

### Bernoulli sums as the basic variance calculation

A Bernoulli variable $B$ equals one with probability $p$ and zero with probability $1-p$. Since $B^2=B$ pointwise,

$$
E[B]=p,
\qquad
E[B^2]=p,
$$

and therefore

$$
\operatorname{Var}(B)=p-p^2=p(1-p).
$$

Now let $X=B_1+\cdots+B_n$ count successes. Linearity always gives

$$
E[X]=\sum_{i=1}^n p_i,
$$

even if the trials are dependent or have different success probabilities. If they are independent, the covariance terms vanish and

$$
\operatorname{Var}(X)=\sum_{i=1}^n p_i(1-p_i).
$$

For identically distributed independent trials this reduces to the familiar binomial formulas $E[X]=np$ and $\operatorname{Var}(X)=np(1-p)$. Shared conditions can make the variance larger. For example, successes produced under the same randomly changing environment tend to occur together, creating positive covariance. Sampling without replacement often creates negative covariance because one success slightly reduces the chance of another. The expectation may stay unchanged in both models while the variance records the altered dependence.

### The mean is the least-squares center

Variance also characterizes the mean as the best constant predictor under squared error. For any real number $a$,

$$
\begin{aligned}
E[(X-a)^2]
&=E[(X-\mu+\mu-a)^2]\\
&=E[(X-\mu)^2]
+2(\mu-a)E[X-\mu]
+(\mu-a)^2\\
&=\operatorname{Var}(X)+(\mu-a)^2.
\end{aligned}
$$

The cross term vanishes because $E[X-\mu]=0$. The remaining expression is minimized uniquely at $a=\mu$, unless one allows distinctions only on probability-zero events. The minimum achievable mean squared error is the variance.

This gives a reason for centering squared deviations at the expectation rather than at an arbitrary reference point. It also explains the role of conditional expectation in prediction: after observing information, the conditional mean is the constant based on that information that minimizes conditional squared error. Other loss functions select other centers. Absolute error is minimized by a median, so the “best” summary depends on the penalty assigned to mistakes.

Mean and variance still leave much of the distribution unspecified. Consider a variable $X$ taking $-1$ and $1$ with equal probabilities, and a variable $Y$ taking $-\sqrt2$, $0$, and $\sqrt2$ with probabilities $1/4$, $1/2$, and $1/4$. Both have mean zero and variance one. Yet $P(X=0)=0$ while $P(Y=0)=1/2$, and their tail probabilities differ. Moment summaries support comparisons and bounds; they do not replace a PMF when exact probabilities matter.

## Turning moments into probability bounds

Even without the complete distribution, an expectation can limit how much probability lies in a tail. If $X\ge0$ and $a\gt 0$, then on the event $\{X\ge a\}$ one has $X\ge a$. Therefore

$$
X\ge a\mathbf 1_{\{X\ge a\}}.
$$

Taking expectations gives **Markov's inequality**:

$$
P(X\ge a)\le\frac{E[X]}{a}.
$$

The nonnegativity assumption cannot be dropped. A large negative part could reduce $E[X]$ even while the positive tail is substantial. The bound is often loose because it uses only one number, but it is sharp in the sense that some distributions attain equality. A variable that equals $a$ with probability $p$ and $0$ otherwise has $E[X]=ap$ and equality at the threshold $a$.

Apply Markov's inequality to the nonnegative variable $(X-\mu)^2$. For $t\gt 0$,

$$
\begin{aligned}
P(|X-\mu|\ge t)
&=P((X-\mu)^2\ge t^2)\\
&\le\frac{E[(X-\mu)^2]}{t^2}\\
&=\frac{\operatorname{Var}(X)}{t^2}.
\end{aligned}
$$

This is **Chebyshev's inequality**. Writing $t=k\sigma$, where $\sigma$ is the standard deviation, gives

$$
P(|X-\mu|\ge k\sigma)\le\frac1{k^2}.
$$

No symmetry, independence, or bell-shaped distribution is assumed. With finite variance alone, at least $3/4$ of the probability lies within two standard deviations of the mean, and at least $8/9$ lies within three. These guarantees are conservative for many familiar distributions but remain valid when the PMF is unknown.

As a numerical example, suppose a nonnegative count has mean $10$. Markov gives

$$
P(X\ge50)\le\frac{10}{50}=0.2.
$$

If its variance is also known to be $16$, then Chebyshev bounds a two-sided deviation of $20$:

$$
P(|X-10|\ge20)\le\frac{16}{20^2}=0.04.
$$

Because $X$ is nonnegative, the event $\vert X-10\vert \ge20$ is the same as $X\ge30$. Here the variance information yields a much stronger statement than Markov's bound $P(X\ge30)\le1/3$. Neither calculation gives the exact tail probability; both certify what is possible from the stated moments alone.

## The tail-sum formula

For a nonnegative integer-valued random variable,

$$
E[X]=\sum_{k=1}^{\infty}P(X\ge k).
$$

To see it, write each integer $x$ as a sum of $x$ ones:

$$
x=\sum_{k=1}^{\infty}\mathbf 1_{\{x\ge k\}}.
$$

Substituting $X$ and taking expectations gives the formula. Every realization contributes to the first $X$ tail events. This form is useful for waiting times because survival probabilities are often easier to obtain than the PMF.

It also exposes infinite means. Suppose

$$
P(X=n)=\frac{1}{n(n+1)},
\qquad n=1,2,\ldots
$$

The probabilities sum to one by telescoping, since

$$
\frac{1}{n(n+1)}=\frac1n-\frac{1}{n+1}.
$$

The tail is $P(X\ge k)=1/k$, so

$$
E[X]=\sum_{k=1}^{\infty}\frac1k=\infty.
$$

Every outcome is a finite integer, yet the mean is infinite because large values decay too slowly.

## Worked example: a loaded die

A six-sided die has probabilities proportional to the face value. Find its PMF, mean, variance, and $P(X\ge4)$.

Write $p_X(k)=ck$ for $k=1,\ldots,6$. Normalization determines $c$:

$$
1=\sum_{k=1}^6 ck
=c(1+2+3+4+5+6)
=21c,
$$

so $c=1/21$ and

$$
p_X(k)=\frac{k}{21}.
$$

The mean is

$$
\begin{aligned}
E[X]
&=\sum_{k=1}^6 k\frac{k}{21}\\
&=\frac{1^2+2^2+3^2+4^2+5^2+6^2}{21}\\
&=\frac{91}{21}\\
&=\frac{13}{3}.
\end{aligned}
$$

For the variance, first compute

$$
\begin{aligned}
E[X^2]
&=\sum_{k=1}^6 k^2\frac{k}{21}\\
&=\frac{1^3+2^3+3^3+4^3+5^3+6^3}{21}\\
&=\frac{441}{21}\\
&=21.
\end{aligned}
$$

Therefore

$$
\operatorname{Var}(X)
=21-\left(\frac{13}{3}\right)^2
=\frac{189-169}{9}
=\frac{20}{9}.
$$

Finally,

$$
P(X\ge4)
=\frac{4+5+6}{21}
=\frac57.
$$

The loading shifts the mean above the fair-die mean $7/2$, as expected from the larger masses on high faces.

## Worked example: fixed points in a random permutation

Shuffle $n$ labeled hats uniformly among $n$ people, and let $X$ be the number who receive their own hat. For person $i$, define

$$
I_i=\mathbf 1_{\{i\text{ receives hat }i\}}.
$$

Then $X=I_1+\cdots+I_n$. A fixed person receives their own hat in $(n-1)!$ of the $n!$ permutations, so

$$
P(I_i=1)=\frac{(n-1)!}{n!}=\frac1n.
$$

Linearity immediately gives

$$
E[X]=\sum_{i=1}^n E[I_i]
=n\cdot\frac1n
=1.
$$

The variance reveals the dependence that the mean ignored. Since $I_i$ is Bernoulli,

$$
\operatorname{Var}(I_i)
=\frac1n\left(1-\frac1n\right).
$$

For distinct $i$ and $j$, fixing both hats leaves $(n-2)!$ permutations:

$$
E[I_iI_j]
=P(I_i=1,I_j=1)
=\frac{(n-2)!}{n!}
=\frac{1}{n(n-1)}.
$$

Hence

$$
\begin{aligned}
\operatorname{Cov}(I_i,I_j)
&=E[I_iI_j]-E[I_i]E[I_j]\\
&=\frac{1}{n(n-1)}-\frac1{n^2}\\
&=\frac{1}{n^2(n-1)}.
\end{aligned}
$$

There are $\binom n2$ unordered pairs, so for $n\ge2$,

$$
\begin{aligned}
\operatorname{Var}(X)
&=n\cdot\frac1n\left(1-\frac1n\right)
+2\binom n2\frac{1}{n^2(n-1)}\\
&=1-\frac1n+\frac1n\\
&=1.
\end{aligned}
$$

The indicators are positively correlated: knowing one person got the correct hat slightly raises the chance that another did too, because the remaining permutation is smaller. The expected count and variance are both $1$ for every $n\ge2$, even though the exact distribution changes with $n$.

## Checks that prevent common errors

- A random variable is a numerical function, not an event. The expression $\{X\le3\}$ is an event obtained from that function.
- A proposed PMF needs nonnegative entries whose total is one. A proportionality statement leaves a normalizing constant to determine.
- Linearity of expectation does not require independence. Variance addition does require zero covariance.
- $E[X^2]$ and $(E[X])^2$ are generally different. Their difference is the variance.
- A zero covariance claim needs justification. Dependence does not always create nonzero covariance, and pairwise independence does not imply mutual independence.
- An expected value can lie outside the support or be dominated by rare outcomes. It should not automatically be described as “typical.”
- Infinite series require convergence checks. A PMF can be perfectly valid while its mean or variance is infinite.

<div className="see-also">

See also: [Bernoulli, binomial, geometric, and negative binomial laws](/math/probability-and-random-variables/bernoulli-binomial-geometric-negative-binomial) · [Continuous random variables and uniform laws](/math/probability-and-random-variables/continuous-random-variables-and-uniform-laws) · [Covariance, correlation, and conditional expectation](/math/probability-and-random-variables/covariance-correlation-conditional-expectation) · [Poisson random variables and Poisson processes](/math/probability-and-random-variables/poisson-random-variables-and-processes) · [Weak law, concentration, and the central limit theorem](/math/probability-and-random-variables/weak-law-concentration-central-limit-theorem)

</div>
