---
title: Cardinality
sidebar_position: 7
---

# Cardinality

Cardinality measures the size of a set. For finite sets, this is just counting elements. Infinite sets require a deeper idea: two sets have the same size when their elements can be paired perfectly by a bijection. This makes it possible to compare infinities without treating all infinite sets as the same.

![David Hilbert is shown wearing a hat in a historical photograph.](https://commons.wikimedia.org/wiki/Special:FilePath/Hilbert.jpg)

*Figure: David Hilbert's work frames modern foundations, geometry, and infinite-dimensional thinking. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hilbert.jpg), Unknown author, public domain.*

The topic is surprising because infinite sets can behave unlike finite sets. A proper subset of an infinite set can have the same cardinality as the whole set, as the even positive integers do with the positive integers. At the same time, Cantor's diagonal argument shows that some infinite sets are strictly larger than countable ones.

## Definitions

Sets $A$ and $B$ have the same cardinality, written $\vert A\vert =\vert B\vert $, if there is a bijection $f:A\to B$. For finite sets, this agrees with ordinary counting. For infinite sets, bijections replace subtraction or division as the reliable comparison tool.

A set is **countably infinite** if it has the same cardinality as the positive integers $\mathbb{Z}^+$. A set is **countable** if it is finite or countably infinite. A set is **uncountable** if it is not countable.

Useful examples:

- $\mathbb{Z}^+$ is countably infinite.
- $\mathbb{Z}$ is countably infinite.
- $\mathbb{Q}$ is countably infinite.
- The set of finite strings over a finite alphabet is countable.
- $\mathbb{R}$ is uncountable.
- The set of infinite bit strings is uncountable.

For finite sets, $\vert A\cup B\vert =\vert A\vert +\vert B\vert -\vert A\cap B\vert $. For any set $S$, its power set $\mathcal{P}(S)$ is the set of all subsets of $S$. Cantor's theorem says $\vert \mathcal{P}(S)\vert \gt \vert S\vert $ for every set $S$, finite or infinite.

An **enumeration** of a set is a list $a_1,a_2,a_3,\dots$ that contains every element of the set at least once. A countably infinite set can be enumerated without omission. If repetitions occur, they can usually be skipped to form a bijective listing.

## Key results

The integers are countable. One enumeration is

$$
0,1,-1,2,-2,3,-3,\dots
$$

This lists every integer exactly once, so it defines a bijection from $\mathbb{N}$ to $\mathbb{Z}$ after indexing the sequence.

The rational numbers are countable. Arrange positive rationals $p/q$ in an infinite grid by numerator and denominator. Traverse the grid diagonally and skip fractions that are not in lowest terms. This gives a list containing every positive rational exactly once. Interleaving positive and negative rationals and including $0$ gives a countable list of all rationals.

Cantor's diagonal argument shows that real numbers in $(0,1)$ are uncountable. Suppose they could be listed:

$$
r_1,r_2,r_3,\dots
$$

Write each in decimal form. Construct a new real number $x$ whose $n$th digit differs from the $n$th digit of $r_n$ and avoids ambiguous choices such as repeating $9$s. Then $x$ differs from every $r_n$ in at least one decimal place, so it is not on the list. This contradicts the assumption that the list was complete.

Cantor's theorem for power sets has a related diagonal proof. Suppose $f:S\to\mathcal{P}(S)$ were onto. Define

$$
D=\{s\in S:s\notin f(s)\}.
$$

Since $D\subseteq S$, surjectivity would require $D=f(d)$ for some $d\in S$. But then $d\in D$ iff $d\notin f(d)=D$, a contradiction. Hence no function from $S$ to $\mathcal{P}(S)$ can be onto.

## Visual

```text
Counting the integers by zigzag:

index:   0   1   2   3   4   5   6   7
value:   0   1  -1   2  -2   3  -3   4 ...

Counting positive rationals by diagonals:

        q=1   q=2   q=3   q=4
p=1     1/1   1/2   1/3   1/4
p=2     2/1   2/2   2/3   2/4
p=3     3/1   3/2   3/3   3/4
p=4     4/1   4/2   4/3   4/4

Traverse p+q=2, then p+q=3, then p+q=4, ...
Skip duplicates such as 2/2 because 2/2 = 1/1.
```

| Set | Cardinality type | Reason |
| --- | --- | --- |
| finite set with $n$ elements | finite | direct counting |
| even positive integers | countably infinite | bijection $n\mapsto2n$ |
| integers | countably infinite | zigzag enumeration |
| rationals | countably infinite | diagonal enumeration by numerator and denominator |
| real numbers in $(0,1)$ | uncountable | Cantor diagonal argument |
| $\mathcal{P}(\mathbb{N})$ | uncountable | Cantor's theorem |

## Worked example 1: Build a bijection from natural numbers to integers

**Problem.** Give an explicit bijection $f:\mathbb{N}\to\mathbb{Z}$, where $\mathbb{N}=\{0,1,2,\dots\}$.

**Method.**

1. Use the zigzag list

$$
0,1,-1,2,-2,3,-3,\dots
$$

2. Even indices should map to nonpositive integers; odd indices should map to positive integers.
3. One compact formula is

$$
f(n)=
\begin{cases}
n/2, & n\text{ is even},\\
-(n+1)/2, & n\text{ is odd}.
\end{cases}
$$

This gives $f(0)=0$, $f(1)=-1$, $f(2)=1$, $f(3)=-2$, and $f(4)=2$. That is a zigzag list with negatives first after zero.

4. To see every integer appears, let $z\in\mathbb{Z}$. If $z\ge0$, then $z=f(2z)$. If $z\lt 0$, then $z=f(-2z-1)$.
5. To see no integer appears twice, the preimage formulas above are unique.

**Checked answer.** The function is a bijection. Therefore $\mathbb{Z}$ is countably infinite.

## Worked example 2: Use diagonalization on infinite bit strings

**Problem.** Show that the set of infinite bit strings is uncountable.

**Method.**

1. Suppose, for contradiction, that all infinite bit strings could be listed:

$$
s_1,s_2,s_3,\dots
$$

2. Write the strings as rows, with bits $s_{ij}$:

$$
\begin{array}{cccc}
s_{11}&s_{12}&s_{13}&\cdots\\
s_{21}&s_{22}&s_{23}&\cdots\\
s_{31}&s_{32}&s_{33}&\cdots\\
\vdots&\vdots&\vdots&
\end{array}
$$

3. Construct a new infinite bit string $t$ by flipping the diagonal bit:

$$
t_i=
\begin{cases}
1, & s_{ii}=0,\\
0, & s_{ii}=1.
\end{cases}
$$

4. For each row $i$, the string $t$ differs from $s_i$ in position $i$.

**Checked answer.** The constructed $t$ is not equal to any listed string, contradicting the claim that the list was complete. Therefore the set of infinite bit strings is uncountable.

## Code

```python
from math import gcd

def integers():
    yield 0
    n = 1
    while True:
        yield n
        yield -n
        n += 1

def rationals(limit_sum):
    yield (0, 1)
    for s in range(2, limit_sum + 1):
        for p in range(1, s):
            q = s - p
            if gcd(p, q) == 1:
                yield (p, q)
                yield (-p, q)

print([next(integers()) for _ in range(1)])  # starts a generator
g = integers()
print([next(g) for _ in range(10)])
print(list(rationals(6)))
```

The rational generator follows diagonal layers $p+q=s$ and skips duplicate rational representations.

## Common pitfalls

- Assuming every infinite set has the same size. Countable and uncountable infinities differ.
- Saying a proper subset must be smaller. That is true for finite sets but not for infinite sets.
- Listing a pattern without proving every element appears. An enumeration must be complete.
- Forgetting to remove duplicate fractions when enumerating rationals.
- Using decimal expansions in diagonal arguments without handling ambiguous representations. Bit strings avoid this issue cleanly.
- Confusing "not yet listed" with "not listable." Diagonalization proves no complete list can exist.

For countability proofs, an explicit listing is helpful but not always necessary. It is enough to describe a systematic enumeration that eventually reaches every object. Listing strings by length works because every finite string has some finite length, and all shorter lengths are completed first. Diagonal enumeration of rationals works because every numerator-denominator pair lies on some finite diagonal.

When proving two infinite sets have the same cardinality, a bijection must be both one-to-one and onto. The function $f(n)=2n$ from positive integers to positive even integers is one-to-one because equal outputs force equal inputs, and onto because every positive even integer has the form $2n$. Both directions are part of the proof.

Diagonal arguments do more than exhibit a missing element from one attempted list. They show how to defeat any proposed list. Given any enumeration of infinite bit strings, the diagonal construction builds a new string that differs from row $i$ in position $i$. Since the argument works for an arbitrary list, no complete list exists.

The power-set theorem is a general diagonal argument. The set $D=\{s\in S:s\notin f(s)\}$ is defined to disagree with each proposed image $f(s)$ at the element $s$. If $D=f(d)$, then asking whether $d\in D$ gives a contradiction. This proof works for finite and infinite sets, so power sets are always strictly larger.

Countability also has consequences for computation. There are countably many finite programs because programs are finite strings over a finite alphabet. There are uncountably many languages over a nonempty finite alphabet because languages are sets of strings, i.e. elements of a power set. Therefore most languages cannot be decided by any program.

A countability proof should say how long one waits before an object appears. In diagonal listings of rationals, a fraction $p/q$ appears on diagonal $p+q$, so it is eventually reached. In listings by string length, a string of length $k$ appears after all shorter strings. This "eventually" argument is what turns a pattern into an enumeration.

For uncountability proofs, be clear about the contradiction. The diagonal object is not merely absent from the first several rows; it differs from row $n$ in position $n$ for every $n$. Therefore it is absent from the entire proposed list. That universal disagreement is the heart of the argument.

## Connections

- [Functions, sequences, and sums](/math/discrete/functions-sequences-sums) supplies bijections and sequences.
- [Sets and set operations](/math/discrete/sets-and-set-operations) introduces power sets and subsets.
- [Proof techniques](/math/discrete/proof-techniques) covers contradiction and diagonal-style arguments.
- [Finite-state machines and computation](/math/discrete/finite-state-machines-and-computation) uses countability to compare programs and languages.
