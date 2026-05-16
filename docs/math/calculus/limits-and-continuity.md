---
title: Limits and Continuity
sidebar_position: 3
---

# Limits and Continuity

A limit describes the value a function approaches, not necessarily the value it actually attains. This distinction lets calculus handle holes, jumps, asymptotes, oscillations, and functions whose formulas change from one region to another. Continuity is the special case where approaching and evaluating agree.

Limits sit between algebra and the derivative. The derivative is defined as a limit of slopes, and the definite integral is defined as a limit of sums. A weak understanding of limits usually becomes a weak understanding of every later topic, so the goal is not just to compute limits but to recognize what kind of behavior the graph has near the point.

## Definitions

We write

$$
\lim_{x\to a} f(x)=L
$$

when $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $a$, with $x\ne a$. The value $f(a)$ is irrelevant to the limit except in the special case of continuity.

The one-sided limits are

$$
\lim_{x\to a^-} f(x),\qquad \lim_{x\to a^+} f(x).
$$

The two-sided limit exists exactly when both one-sided limits exist and are equal:

$$
\lim_{x\to a^-} f(x)=\lim_{x\to a^+} f(x)=L.
$$

A function is continuous at $a$ when all three conditions hold:

$$
\begin{aligned}
f(a) &\text{ is defined},\\
\lim_{x\to a} f(x) &\text{ exists},\\
\lim_{x\to a} f(x) &= f(a).
\end{aligned}
$$

An infinite limit, such as $\lim_{x\to a^+}f(x)=\infty$, describes unbounded behavior rather than a real-number limit. A vertical asymptote occurs when a one-sided limit is infinite. A horizontal asymptote occurs when

$$
\lim_{x\to\infty} f(x)=L
\quad\text{or}\quad
\lim_{x\to-\infty} f(x)=L.
$$

The $\epsilon$-$\delta$ definition gives the formal meaning: $\lim_{x\to a}f(x)=L$ if for every $\epsilon\gt 0$ there exists $\delta\gt 0$ such that

$$
0<|x-a|<\delta \quad\Rightarrow\quad |f(x)-L|<\epsilon.
$$

The phrase "deleted window" is important. The condition $0\lt \vert x-a\vert $ excludes the point $a$ itself. A function may be undefined at $a$, or may be assigned a value far from $L$, while still having limit $L$. Continuity adds the missing requirement that the function value and limiting value match.

Continuity on an interval means continuity at every point inside the interval and one-sided continuity at endpoints. On $[a,b]$, continuity at $a$ uses the right-hand limit, and continuity at $b$ uses the left-hand limit. This convention matters in optimization and integration, where closed intervals include endpoints but the function may not be defined beyond them.

## Key results

The standard limit laws allow sums, differences, products, quotients, powers, and roots to be moved through limits when the resulting expressions are defined. If $\lim f(x)=A$ and $\lim g(x)=B$ as $x\to a$, then

$$
\begin{aligned}
\lim(f+g) &= A+B,\\
\lim(fg) &= AB,\\
\lim\frac{f}{g} &= \frac{A}{B}\quad (B\ne 0).
\end{aligned}
$$

For polynomials, substitution works:

$$
\lim_{x\to a}p(x)=p(a).
$$

For rational functions, if $q(a)\ne 0$, then

$$
\lim_{x\to a}\frac{p(x)}{q(x)}=\frac{p(a)}{q(a)}.
$$

If substitution gives $0/0$, the expression is indeterminate, not impossible. Algebra may reveal a removable discontinuity:

$$
\frac{x^2-a^2}{x-a}=x+a\quad (x\ne a).
$$

The simplified expression has the same values near $a$ but not necessarily at $a$. This distinction is why cancellation is valid for limits but not for redefining the original function without saying so.

The Squeeze Theorem states that if $g(x)\le f(x)\le h(x)$ near $a$ and

$$
\lim_{x\to a}g(x)=\lim_{x\to a}h(x)=L,
$$

then $\lim_{x\to a}f(x)=L$. It is especially useful for oscillating functions such as $x\sin(1/x)$.

The Intermediate Value Theorem is a central consequence of continuity. If $f$ is continuous on $[a,b]$ and $N$ lies between $f(a)$ and $f(b)$, then there is at least one $c$ in $[a,b]$ such that $f(c)=N$. The theorem does not say where $c$ is or how many such points exist. It says that a continuous graph cannot jump over an intermediate height.

The Extreme Value Theorem is another consequence used later. If $f$ is continuous on a closed interval $[a,b]$, then $f$ attains both an absolute maximum and an absolute minimum on that interval. The hypotheses are both necessary: an open interval may fail to include the height it approaches, and a discontinuous function may have a missing or unbounded value.

For rational limits at infinity, divide numerator and denominator by the highest power of $x$ in the denominator. Lower powers vanish because

$$
\lim_{x\to\infty}\frac1{x^k}=0\quad (k>0).
$$

For limits involving absolute value, roots, or piecewise definitions, one-sided analysis is often cleaner than forcing a single formula. For example, $\vert x\vert /x$ equals $-1$ for $x\lt 0$ and $1$ for $x\gt 0$, so the two-sided limit at $0$ does not exist. For square roots, the domain itself may force a one-sided limit, such as $\lim_{x\to 0^+}\sqrt{x}=0$.

A short $\epsilon$-$\delta$ proof shows what the formal definition checks. To prove $\lim_{x\to 3}(2x-1)=5$, start with the desired bound:

$$
|(2x-1)-5|=|2x-6|=2|x-3|.
$$

If we want this to be less than $\epsilon$, it is enough to require $\vert x-3\vert \lt \epsilon/2$. Therefore choose $\delta=\epsilon/2$. Then whenever $0\lt \vert x-3\vert \lt \delta$,

$$
|(2x-1)-5|=2|x-3|<2\delta=2\cdot\frac{\epsilon}{2}=\epsilon.
$$

The proof does not rely on a table or graph. It shows that every requested output tolerance $\epsilon$ can be met by a corresponding input tolerance $\delta$. For more complicated functions, the algebra may require extra bounding steps, but the logic is the same: translate closeness in $x$ into closeness in $f(x)$.

Continuity also interacts well with composition. If $g$ is continuous at $a$ and $f$ is continuous at $g(a)$, then $f\circ g$ is continuous at $a$. This is why many everyday limits are solved by substitution: polynomials, rational functions away from zero denominators, roots on their domains, trigonometric functions, exponentials, and logarithms are continuous where defined. When a composed expression fails, the failure usually comes from a domain restriction, a denominator becoming zero, or a piecewise change in formula.

That diagnostic habit keeps computation tied to the graph instead of turning limits into memorized algebra or isolated symbol pushing.

## Visual

ASCII sketch of the $\epsilon$-$\delta$ idea:

```text
output y
   ^
L+e|        ------------------  top of epsilon band
   |              f(x) values must land here
 L |        ---------- L -------------------------
   |
L-e|        ------------------  bottom of epsilon band
   |
   +-------------|------|-------------|------> input x
               a-d     a            a+d
             x must stay in this deleted delta window
```

| Situation near $x=a$ | Left limit | Right limit | Two-sided limit | Continuity |
|---|---:|---:|---:|---|
| Smooth graph | $L$ | $L$ | Exists | Yes if $f(a)=L$ |
| Removable hole | $L$ | $L$ | Exists | No unless hole is filled with $L$ |
| Jump | $L_1$ | $L_2$ | Does not exist if $L_1\ne L_2$ | No |
| Vertical asymptote | Infinite or unbounded | Infinite or unbounded | No real limit | No |
| Oscillation | No settling | No settling | Does not exist | No |

## Worked example 1: removable discontinuity

**Problem.** Compute

$$
\lim_{x\to 2}\frac{x^2-4}{x-2}
$$

and explain whether the original function is continuous at $x=2$.

**Method.**

1. Direct substitution gives

$$
\frac{2^2-4}{2-2}=\frac00,
$$

so the expression is indeterminate.

2. Factor the numerator:

$$
x^2-4=(x-2)(x+2).
$$

3. Cancel only for $x\ne 2$:

$$
\frac{x^2-4}{x-2}=\frac{(x-2)(x+2)}{x-2}=x+2.
$$

4. Now take the limit:

$$
\lim_{x\to 2}(x+2)=4.
$$

**Checked answer.** The limit is $4$. The original function is not continuous at $x=2$ because it is not defined there. If we define $f(2)=4$, the discontinuity becomes removable.

## Worked example 2: one-sided limits and a jump

**Problem.** Let

$$
f(x)=
\begin{cases}
x+1, & x<1,\\
3, & x\ge 1.
\end{cases}
$$

Find the one-sided limits at $x=1$, decide whether the two-sided limit exists, and decide whether $f$ is continuous at $1$.

**Method.**

1. Approach from the left using the rule for $x\lt 1$:

$$
\lim_{x\to 1^-}f(x)=\lim_{x\to 1^-}(x+1)=2.
$$

2. Approach from the right using the rule for $x\ge 1$:

$$
\lim_{x\to 1^+}f(x)=\lim_{x\to 1^+}3=3.
$$

3. Compare one-sided limits:

$$
2\ne 3.
$$

4. Evaluate the function:

$$
f(1)=3,
$$

because the second branch includes $x=1$.

**Checked answer.** The two-sided limit does not exist because the one-sided limits disagree. The function is not continuous at $x=1$, even though $f(1)$ is defined.

## Code

```python
def sample_limit_values(f, a, steps=(1e-1, 1e-2, 1e-3, 1e-4)):
    for h in steps:
        left = f(a - h)
        right = f(a + h)
        print(f"h={h:g}: left={left:.8f}, right={right:.8f}")

def removable(x):
    return (x * x - 4) / (x - 2)

sample_limit_values(removable, 2.0)
```

## Common pitfalls

- Substituting into an indeterminate form and concluding that no limit exists. The form $0/0$ means more work is needed.
- Saying an infinite limit "exists" as a real number. Infinite limits describe unbounded behavior.
- Forgetting to compare left and right limits for piecewise functions, absolute values, and rational functions with sign changes.
- Canceling a factor and then forgetting that the original expression may still be undefined at the canceled value.
- Confusing continuity at a point with continuity on an interval. Endpoints use one-sided continuity.
- Treating numerical tables as proof. Tables suggest behavior, but algebra or theorems justify the answer.

## Connections

- [Functions and Models](/math/calculus/functions-and-models): domains and graph behavior determine which limits are meaningful.
- [Derivatives and Rates](/math/calculus/derivatives-and-rates): derivatives are limits of difference quotients.
- [Definite Integrals and the Fundamental Theorem](/math/calculus/definite-integrals-fundamental-theorem): definite integrals arise as limits of Riemann sums.
- [Sequences and Series](/math/calculus/sequences-and-series): convergence is the limit concept applied to indexed lists and infinite sums.
