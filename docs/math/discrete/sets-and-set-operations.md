---
title: Sets and Set Operations
sidebar_position: 5
---

# Sets and Set Operations

Sets are the basic containers of discrete mathematics. Relations are sets of ordered pairs, graphs are sets of vertices and edges, languages are sets of strings, and events in probability are sets of outcomes. The discipline around sets is simple but strict: order does not matter, repetition does not matter, and membership is the central question.

![Two overlapping circles show a highlighted Venn diagram region.](https://commons.wikimedia.org/wiki/Special:FilePath/Venn0001.svg)

*Figure: A Venn diagram connects set operations with the same logical connectives used in proofs. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Venn0001.svg), Watchduck, public domain.*

Set notation gives a compact way to describe large or infinite collections. Instead of listing every object, we can define a set by a property, combine sets with operations, and prove two descriptions match by checking membership element by element. This makes set theory the bridge between logic and the rest of the subject.

## Definitions

A **set** is an unordered collection of distinct elements. Write $a\in A$ when $a$ is an element of $A$, and $a\notin A$ otherwise. The same set can be described by roster notation, such as $\{1,2,3\}$, or set-builder notation, such as $\{x\in\mathbb{Z}:1\le x\le3\}$.

Two sets are equal exactly when they have the same elements:

$$
A=B \quad\text{if and only if}\quad \forall x(x\in A \leftrightarrow x\in B).
$$

$A$ is a **subset** of $B$, written $A\subseteq B$, if every element of $A$ is also in $B$:

$$
A\subseteq B \quad\text{if and only if}\quad \forall x(x\in A \to x\in B).
$$

If $A\subseteq B$ and $A\ne B$, then $A$ is a **proper subset** of $B$. The empty set $\emptyset$ has no elements and is a subset of every set. The **power set** $\mathcal{P}(A)$ is the set of all subsets of $A$.

For sets within a universal set $U$:

- Union: $A\cup B=\{x:x\in A\lor x\in B\}$.
- Intersection: $A\cap B=\{x:x\in A\land x\in B\}$.
- Difference: $A-B=\{x:x\in A\land x\notin B\}$.
- Complement: $\overline{A}=U-A$.
- Symmetric difference: $A\oplus B=(A-B)\cup(B-A)$.
- Cartesian product: $A\times B=\{(a,b):a\in A\land b\in B\}$.

Sets can contain other sets. For example, if $A=\{1,2\}$, then $\mathcal{P}(A)=\{\emptyset,\{1\},\{2\},\{1,2\}\}$. Notice that $1\in A$, but $\{1\}\subseteq A$ and $\{1\}\in\mathcal{P}(A)$.

## Key results

Set identities mirror logical equivalences. De Morgan's laws for sets are:

$$
\overline{A\cup B}=\overline{A}\cap\overline{B},
\qquad
\overline{A\cap B}=\overline{A}\cup\overline{B}.
$$

Proof of the first identity by element chasing: let $x$ be arbitrary. Then

$$
\begin{aligned}
x\in\overline{A\cup B}
&\leftrightarrow x\notin A\cup B\\
&\leftrightarrow \neg(x\in A\lor x\in B)\\
&\leftrightarrow x\notin A\land x\notin B\\
&\leftrightarrow x\in\overline{A}\cap\overline{B}.
\end{aligned}
$$

Since the equivalence holds for every $x$, the sets are equal.

Other useful identities include:

$$
\begin{aligned}
A\cup(B\cap C)&=(A\cup B)\cap(A\cup C),\\
A\cap(B\cup C)&=(A\cap B)\cup(A\cap C),\\
A\cup\emptyset&=A,\\
A\cap U&=A,\\
A\cup\overline{A}&=U,\\
A\cap\overline{A}&=\emptyset.
\end{aligned}
$$

If $A$ is finite with $n$ elements, then $\vert \mathcal{P}(A)\vert =2^n$. Each element of $A$ has two independent choices when forming a subset: include it or exclude it. By the product rule, this gives $2^n$ subsets.

For finite sets, inclusion-exclusion begins with

$$
|A\cup B|=|A|+|B|-|A\cap B|.
$$

The subtraction corrects the double count of elements lying in both sets. This same idea grows into the larger inclusion-exclusion formulas used in counting.

## Visual

```text
Universal set U

+------------------------------------------------+
|                                                |
|        A only        A and B        B only      |
|      +---------+   +---------+   +---------+   |
|      | A - B   |   | A cap B |   | B - A   |   |
|      +---------+   +---------+   +---------+   |
|                                                |
|  outside both = complement of A union B         |
+------------------------------------------------+
```

| Identity | Membership translation | Logic law behind it |
| --- | --- | --- |
| $\overline{A\cup B}=\overline{A}\cap\overline{B}$ | not in $A$ or $B$ | $\neg(P\lor Q)\equiv\neg P\land\neg Q$ |
| $\overline{A\cap B}=\overline{A}\cup\overline{B}$ | not in both | $\neg(P\land Q)\equiv\neg P\lor\neg Q$ |
| $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ | in $A$ and one of $B,C$ | distributive law |
| $A\cup(A\cap B)=A$ | $A$ already contains $A\cap B$ | absorption law |

## Worked example 1: Compute operations and check inclusion-exclusion

**Problem.** Let

$$
U=\{1,2,3,4,5,6,7,8\},\quad A=\{1,2,3,5,8\},\quad B=\{2,4,5,6\}.
$$

Find $A\cup B$, $A\cap B$, $A-B$, $\overline{A}$, and verify inclusion-exclusion.

**Method.**

1. The union contains elements appearing in either set:

$$
A\cup B=\{1,2,3,4,5,6,8\}.
$$

2. The intersection contains elements appearing in both:

$$
A\cap B=\{2,5\}.
$$

3. The difference $A-B$ keeps elements of $A$ that are not in $B$:

$$
A-B=\{1,3,8\}.
$$

4. The complement of $A$ is computed relative to $U$:

$$
\overline{A}=U-A=\{4,6,7\}.
$$

5. Check inclusion-exclusion:

$$
\begin{aligned}
|A|+|B|-|A\cap B|
&=5+4-2\\
&=7\\
&=|A\cup B|.
\end{aligned}
$$

**Checked answer.** The operations are correct, and the count agrees. Element $7$ is in neither $A$ nor $B$, which is why it does not appear in the union even though it is in the universal set.

## Worked example 2: Prove a set identity by element chasing

**Problem.** Prove

$$
A-(B\cup C)=(A-B)\cap(A-C).
$$

**Method.**

1. Let $x$ be an arbitrary element.
2. Translate membership in the left side:

$$
\begin{aligned}
x\in A-(B\cup C)
&\leftrightarrow x\in A\land x\notin B\cup C\\
&\leftrightarrow x\in A\land \neg(x\in B\lor x\in C)\\
&\leftrightarrow x\in A\land x\notin B\land x\notin C.
\end{aligned}
$$

3. Translate membership in the right side:

$$
\begin{aligned}
x\in (A-B)\cap(A-C)
&\leftrightarrow x\in A-B\land x\in A-C\\
&\leftrightarrow (x\in A\land x\notin B)\land(x\in A\land x\notin C)\\
&\leftrightarrow x\in A\land x\notin B\land x\notin C.
\end{aligned}
$$

4. Both sides have the same membership condition for arbitrary $x$.

**Checked answer.** Since every element belongs to the left side exactly when it belongs to the right side, the sets are equal. This proof also shows why the formula is a set version of De Morgan's law.

## Code

```python
from itertools import chain, combinations

def powerset(items):
    items = list(items)
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            yield set(combo)

U = set(range(1, 9))
A = {1, 2, 3, 5, 8}
B = {2, 4, 5, 6}

print("union", A | B)
print("intersection", A & B)
print("difference", A - B)
print("complement", U - A)
print("powerset size", len(list(powerset(A))))
```

Python sets implement union, intersection, difference, and symmetric difference directly. The `powerset` function uses combinations of all possible subset sizes.

## Common pitfalls

- Confusing $\in$ and $\subseteq$. An element belongs to a set; a set can be a subset of another set.
- Forgetting the universal set when taking complements. $\overline{A}$ depends on the surrounding $U$.
- Treating repeated roster entries as distinct. $\{1,1,2\}=\{1,2\}$.
- Assuming $A-B=B-A$. Set difference is not commutative.
- Treating Cartesian products as unordered. Usually $(a,b)\ne(b,a)$.
- Proving a set identity by drawing only one picture. Diagrams build intuition, but element chasing provides a proof.

Set-builder notation should always include a domain when ambiguity is possible. The expression $\{x:x^2\lt 4\}$ means different things over integers, rationals, and real numbers. Writing $\{x\in\mathbb{Z}:x^2\lt 4\}$ makes the intended set finite and equal to $\{-1,0,1\}$, while the real-domain version is the interval $(-2,2)$.

To prove $A=B$, use the element method or prove two subset inclusions. The element method shows $x\in A\leftrightarrow x\in B$ for arbitrary $x$. The subset method proves $A\subseteq B$ and $B\subseteq A$ separately. Both approaches are formal versions of "same elements," and both avoid relying on a diagram that may not capture all cases.

Power sets are a common source of type errors. If $A=\{1,2\}$, then $\{1\}\in\mathcal{P}(A)$ and $\{1\}\subseteq A$, but $\{1\}\notin A$ unless $A$ itself contains the set $\{1\}$ as an element. Keeping track of whether an object is an element or a set of elements prevents many mistakes in relations and functions.

Cartesian products are ordered and can change size quickly. If $\vert A\vert =m$ and $\vert B\vert =n$, then $\vert A\times B\vert =mn$. If $A=B$, the product $A\times A$ contains ordered pairs, so $(a,b)$ and $(b,a)$ are different when $a\ne b$. Relations on $A$ are subsets of this ordered product, which is why there are $2^{\vert A\vert ^2}$ possible relations on a finite set $A$.

For complements and differences, always name the universal set. In probability, the complement of an event is relative to the sample space. In number theory, the complement of even integers might mean odd integers within $\mathbb{Z}$, but within $\mathbb{N}$ it means positive odd integers. The notation alone does not determine the surrounding universe.

For finite examples, verify identities by testing membership rather than by comparing roster lists too early. Roster lists can hide duplicates or ordering changes. The element method forces the exact logical condition on both sides, which is why it scales from three-element examples to arbitrary sets.

When a problem involves several operations, add parentheses before simplifying. Set difference binds less predictably in students' minds than union and intersection, and $A-(B-C)$ is not the same as $(A-B)-C$. Translating every operation into membership logic is the most reliable way to disambiguate the expression.

For finite sets, cardinality checks are useful but not complete proofs of equality unless one subset relation is already known. Two sets can have the same size and different elements. If you prove $A\subseteq B$ and $\vert A\vert =\vert B\vert $ for finite sets, then equality follows; without the subset relation, equal size alone is not enough.

## Connections

- [Propositional logic](/math/discrete/propositional-logic) explains the logical laws behind set identities.
- [Predicates and quantifiers](/math/discrete/predicates-and-quantifiers) gives the formal language for subset and equality proofs.
- [Counting principles](/math/discrete/counting-principles) uses set sizes, products, and unions.
- [Pigeonhole and inclusion-exclusion](/math/discrete/pigeonhole-and-inclusion-exclusion) extends the counting formula for unions.
- [Relations](/math/discrete/relations) treats relations as sets of ordered pairs.
