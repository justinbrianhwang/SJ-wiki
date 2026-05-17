---
title: Generating Functions
sidebar_position: 17
---

# Generating Functions

Generating functions turn sequences into algebraic objects. Instead of studying $a_0,a_1,a_2,\dots$ directly, package the sequence as coefficients of a power series. Algebraic operations on the series then correspond to counting constructions, recurrence solving, and convolution.

![Pascal's triangle fills in row by row with binomial coefficients.](https://commons.wikimedia.org/wiki/Special:FilePath/PascalTriangleAnimated2.gif)

*Figure: Pascal's triangle organizes binomial coefficients, combinations, and recurrence patterns. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif), Hersfold, public domain.*

The main idea is that the exponent tracks size while the coefficient tracks how many objects have that size. Once a counting problem is translated into a generating function, multiplication, coefficient extraction, and algebraic simplification do the bookkeeping that would otherwise require many cases.

## Definitions

The **ordinary generating function** for a sequence $\{a_n\}_{n\ge0}$ is

$$
G(x)=\sum_{n=0}^{\infty}a_nx^n.
$$

In many discrete mathematics applications this is treated as a formal power series, so convergence is not the main issue. The coefficient of $x^n$ records $a_n$. We often write $[x^n]G(x)$ for the coefficient of $x^n$ in $G(x)$.

Basic generating functions:

$$
\begin{aligned}
\frac{1}{1-x} &= 1+x+x^2+x^3+\cdots,\\
\frac{1}{(1-x)^2} &= \sum_{n=0}^{\infty}(n+1)x^n,\\
\frac{1}{1-ax} &= \sum_{n=0}^{\infty}a^nx^n,\\
(1+x)^n &= \sum_{r=0}^{n}\binom nr x^r.
\end{aligned}
$$

Multiplying generating functions performs **convolution**:

$$
\left(\sum_{n\ge0}a_nx^n\right)
\left(\sum_{n\ge0}b_nx^n\right)
=\sum_{n\ge0}\left(\sum_{k=0}^{n}a_kb_{n-k}\right)x^n.
$$

This is why products of generating functions model independent contributions whose sizes add.

## Key results

Generating functions solve linear recurrences. For the Fibonacci sequence $F_0=0$, $F_1=1$, and $F_n=F_{n-1}+F_{n-2}$, let

$$
F(x)=\sum_{n=0}^{\infty}F_nx^n.
$$

Multiply the recurrence by $x^n$ and sum for $n\ge2$:

$$
\sum_{n\ge2}F_nx^n
=\sum_{n\ge2}F_{n-1}x^n+\sum_{n\ge2}F_{n-2}x^n.
$$

Using $F_0=0$ and $F_1=1$:

$$
F(x)-x=xF(x)+x^2F(x).
$$

Therefore

$$
F(x)=\frac{x}{1-x-x^2}.
$$

This rational function contains the whole Fibonacci sequence in its coefficients.

Generating functions also prove identities. The coefficient of $x^r$ in $(1+x)^m(1+x)^n$ is

$$
\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k},
$$

while $(1+x)^m(1+x)^n=(1+x)^{m+n}$ has coefficient $\binom{m+n}{r}$. Hence Vandermonde's identity follows:

$$
\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}=\binom{m+n}{r}.
$$

For restricted integer solutions, each variable contributes a factor whose terms represent its allowed values. If $x_i$ can be $0,1,2$, its factor is $1+x+x^2$. If it can be any nonnegative integer, its factor is $1/(1-x)$.

## Visual

```mermaid
flowchart LR
  A[Counting choices] --> B[One factor per component]
  B --> C[Multiply factors]
  C --> D[Coefficient of x^n]
  D --> E[Number of objects of size n]
```

| Constraint on one variable | Generating factor | Meaning |
| --- | --- | --- |
| $x_i\ge0$ | $1+x+x^2+\cdots=\frac1{1-x}$ | any nonnegative contribution |
| $0\le x_i\le m$ | $1+x+\cdots+x^m$ | bounded contribution |
| $x_i\in\{0,1\}$ | $1+x$ | choose or do not choose |
| $x_i$ even and nonnegative | $1+x^2+x^4+\cdots$ | even contribution |
| one coin of value $d$ or none | $1+x^d$ | at most one coin |
| unlimited coins of value $d$ | $\frac1{1-x^d}$ | any number of that coin |

## Worked example 1: Count restricted solutions

**Problem.** Count nonnegative integer solutions to

$$
x_1+x_2+x_3=5
$$

with $0\le x_i\le2$ for each $i$.

**Method.**

1. Each variable can contribute $0$, $1$, or $2$, so each variable has generating factor

$$
1+x+x^2.
$$

2. For three variables, use

$$
(1+x+x^2)^3.
$$

3. We need the coefficient of $x^5$.
4. Expand in a controlled way:

$$
(1+x+x^2)^2=1+2x+3x^2+2x^3+x^4.
$$

5. Multiply by $1+x+x^2$ and track only terms contributing to $x^5$:

$$
[x^5](1+2x+3x^2+2x^3+x^4)(1+x+x^2).
$$

6. Contributions to $x^5$ are:

$$
[x^3]\cdot[x^2] + [x^4]\cdot[x^1] = 2\cdot1+1\cdot1=3.
$$

**Checked answer.** There are $3$ solutions: $(1,2,2)$, $(2,1,2)$, and $(2,2,1)$.

## Worked example 2: Solve a recurrence with a generating function

**Problem.** Solve $a_0=1$ and $a_n=2a_{n-1}+1$ for $n\ge1$.

**Method.**

1. Let

$$
A(x)=\sum_{n\ge0}a_nx^n.
$$

2. Multiply the recurrence by $x^n$ and sum for $n\ge1$:

$$
\sum_{n\ge1}a_nx^n=2\sum_{n\ge1}a_{n-1}x^n+\sum_{n\ge1}x^n.
$$

3. Rewrite each sum:

$$
A(x)-a_0=2xA(x)+\frac{x}{1-x}.
$$

4. Since $a_0=1$,

$$
A(x)-1=2xA(x)+\frac{x}{1-x}.
$$

5. Solve for $A(x)$:

$$
\begin{aligned}
A(x)(1-2x)
&=1+\frac{x}{1-x}\\
&=\frac{1}{1-x}.
\end{aligned}
$$

So

$$
A(x)=\frac{1}{(1-x)(1-2x)}.
$$

6. Use partial fractions:

$$
\frac{1}{(1-x)(1-2x)}=\frac{-1}{1-x}+\frac{2}{1-2x}.
$$

7. Extract coefficients:

$$
a_n=-1+2\cdot2^n=2^{n+1}-1.
$$

**Checked answer.** $a_n=2^{n+1}-1$. Check: $a_0=1$, and $2a_{n-1}+1=2(2^n-1)+1=2^{n+1}-1$.

## Code

```python
from collections import Counter

def multiply(p, q):
    out = Counter()
    for i, ai in p.items():
        for j, bj in q.items():
            out[i + j] += ai * bj
    return out

def power(poly, k):
    result = Counter({0: 1})
    for _ in range(k):
        result = multiply(result, poly)
    return result

restricted = power(Counter({0: 1, 1: 1, 2: 1}), 3)
print(dict(sorted(restricted.items())))
print("coefficient of x^5:", restricted[5])
```

The dictionary key is the exponent, and the value is the coefficient. Multiplication implements convolution.

## Common pitfalls

- Forgetting that ordinary generating functions usually track size by exponent and count by coefficient.
- Multiplying factors when the modeled choices are not independent components.
- Extracting the wrong coefficient after a shift in indices.
- Treating formal power series as analytic functions without checking whether convergence matters.
- Using an unrestricted factor $1/(1-x)$ when the problem has upper bounds.
- Solving the algebra but not checking the resulting sequence against the initial conditions.

The most common modeling error is choosing the right-looking algebra before deciding what one unit of size means. In a coin problem, the exponent usually tracks total value, so a dime contributes $x^{10}$, not $x$. In a word problem, the exponent may track length. In a distribution problem, the exponent may track total score. State this meaning explicitly before multiplying factors; otherwise the coefficient you extract may answer a different question.

Another useful check is to compute the first few coefficients directly. If a generating function claims to count restricted solutions to $x_1+x_2+x_3=n$ with each variable at most $2$, then the coefficients should be symmetric from degree $0$ through degree $6$: $1,3,6,7,6,3,1$. The symmetry comes from replacing each value $a_i$ by $2-a_i$. If the algebra gives a coefficient sequence that violates an obvious structural check, the factor or coefficient target is probably wrong.

When solving recurrences, index shifts deserve special attention. If the recurrence starts at $n\ge2$, then $\sum_{n\ge2}a_nx^n$ is usually $A(x)-a_0-a_1x$, not just $A(x)$. Similarly, $\sum_{n\ge2}a_{n-1}x^n=x(A(x)-a_0)$. Writing two or three terms under the summation often prevents an off-by-one error that would change the numerator of the final rational function.

Generating functions are formal objects in this setting, but algebraic manipulation still needs valid formal rules. Multiplication is safe when each coefficient of the product receives only finitely many contributions. Ordinary products used for finite constraints and standard geometric series satisfy this. Infinite products require more care and should be used only when the coefficient of each $x^n$ is determined by finitely many choices.

Finally, remember that a generating function is not the answer by itself unless the problem asks for one. Most counting questions ask for a coefficient, a closed form, or a recurrence. After obtaining $G(x)$, finish the task: extract $[x^n]G(x)$, compute the requested coefficient, or explain how the expression encodes the sequence.

For coefficient extraction, keep a small library of standard forms and learn to reshape expressions into them. For instance, $\frac{1}{1-3x}$ immediately gives coefficient $3^n$, while $\frac{x^4}{1-3x}$ gives coefficient $3^{n-4}$ for $n\ge4$ and $0$ for smaller $n$. The numerator shift is not cosmetic; it changes which terms exist. When a rational function contains several factors, partial fractions often turn one difficult coefficient extraction into several standard geometric extractions.

Generating functions can also encode choices with signs or weights. If an object contributes a weight $w$, use $w x^k$ rather than just $x^k$. This produces weighted counts, such as total value or probability mass, not just the number of objects. The same algebra works, but the meaning of coefficients changes. State whether coefficients are counts, weighted sums, or probabilities.

As a final verification, translate a coefficient back into a combinatorial statement. If $[x^5](1+x+x^2)^3=3$, explain that the three contributions correspond to placing one variable at $1$ and the other two at $2$. This reverse translation is the best evidence that the algebra and the original counting problem still match.

A practical workflow is: define the coefficient meaning, build one factor per independent component, multiply or simplify, extract the coefficient, and then interpret the coefficient back in the original language. Skipping the final interpretation is risky because the algebra may have counted a related but different object, such as ordered selections instead of unordered selections.

For difficult coefficient extractions, compute the first few terms before seeking a closed form. Expanding through degree $5$ or $6$ often reveals whether the generating function has the right initial behavior. These low-degree coefficients also provide test data for recurrence solutions derived from rational generating functions.

If a generating function has a product of factors, annotate each factor in the margin. For example, in $\frac{1}{(1-x)(1-x^5)(1-x^{10})}$, the factors represent pennies, nickels, and dimes. This annotation keeps the algebra tied to the counting model and makes it easier to modify the expression when supplies become limited.

When the same problem can be solved by stars and bars, a recurrence, and a generating function, compare the answers. Agreement across methods is a strong validation, and disagreement usually reveals whether order, repetition, or a boundary constraint was modeled differently.

This comparison also helps decide which method gives the clearest explanation for the audience.

Prefer the method that exposes the constraint most directly.

## Connections

- [Recurrence relations](/math/discrete/recurrence-relations) gives the recurrences generating functions often solve.
- [Permutations and combinations](/math/discrete/permutations-and-combinations) supplies binomial coefficients and stars-and-bars counts.
- [Counting principles](/math/discrete/counting-principles) supplies product-rule reasoning for multiplying factors.
- [Discrete probability](/math/discrete/discrete-probability) uses generating functions for distributions in more advanced work.
