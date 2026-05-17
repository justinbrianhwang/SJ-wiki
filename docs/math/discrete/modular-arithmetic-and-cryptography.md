---
title: Modular Arithmetic and Cryptography
sidebar_position: 10
---

# Modular Arithmetic and Cryptography

Modular arithmetic treats integers by their remainders. This turns infinite integer questions into finite arithmetic on residue classes, which is why it appears in hashing, pseudorandom generators, checksums, calendars, cyclic schedules, and public-key cryptography.

![A Diffie-Hellman diagram shows two parties combining public and private values.](https://commons.wikimedia.org/wiki/Special:FilePath/Diffie-Hellman_Key_Exchange.svg)

*Figure: Diffie-Hellman key exchange is a standard application of modular arithmetic to secure communication. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange.svg), A. J. Han Vinck and Flugaal, public domain.*

The main shift is to stop asking for the exact integer and ask only for its class modulo $m$. Once this is done carefully, addition, multiplication, inverses, and exponentiation can be performed with small representatives. Cryptography then uses the fact that some modular operations are easy in one direction but hard to reverse without hidden information.

## Definitions

For integers $a,b$ and a positive integer $m$, $a$ is **congruent** to $b$ modulo $m$, written

$$
a\equiv b\pmod m,
$$

if $m\mid(a-b)$. Equivalently, $a$ and $b$ have the same remainder when divided by $m$.

The **residue class** of $a$ modulo $m$ is the set

$$
[a]_m=\{b\in\mathbb{Z}:b\equiv a\pmod m\}.
$$

There are exactly $m$ residue classes modulo $m$, represented by $0,1,\dots,m-1$. Arithmetic modulo $m$ can be performed on any representatives and then reduced back to this range.

A **multiplicative inverse** of $a$ modulo $m$ is an integer $b$ such that

$$
ab\equiv1\pmod m.
$$

The inverse, when it exists, is unique modulo $m$. The set of invertible residue classes modulo $m$ is often denoted $U_m$.

Euler's phi function $\phi(n)$ counts the positive integers not exceeding $n$ that are relatively prime to $n$. If $n=pq$ for distinct primes $p$ and $q$, then

$$
\phi(n)=(p-1)(q-1).
$$

## Key results

Congruence is compatible with addition and multiplication. If

$$
a\equiv b\pmod m,\qquad c\equiv d\pmod m,
$$

then

$$
a+c\equiv b+d\pmod m,\qquad ac\equiv bd\pmod m.
$$

Proof sketch: $m\mid(a-b)$ and $m\mid(c-d)$. Therefore $m$ divides $(a+c)-(b+d)$ and also divides $ac-bd=a(c-d)+d(a-b)$.

An inverse of $a$ modulo $m$ exists if and only if $\gcd(a,m)=1$. This follows from Bezout's identity: there are integers $s,t$ such that

$$
as+mt=1
$$

exactly when $\gcd(a,m)=1$. Reducing modulo $m$ gives $as\equiv1\pmod m$, so $s$ is an inverse of $a$ modulo $m$.

The **Chinese remainder theorem** says that if $m_1,\dots,m_k$ are pairwise relatively prime, then the system

$$
x\equiv a_i\pmod{m_i}\quad(1\le i\le k)
$$

has a unique solution modulo $M=m_1m_2\cdots m_k$.

Fast modular exponentiation uses repeated squaring. If the exponent has binary expansion

$$
e=\sum_j b_j2^j,
$$

then

$$
a^e=\prod_{b_j=1} a^{2^j}.
$$

Reducing modulo $m$ after each multiplication keeps the numbers small and uses only $O(\log e)$ modular multiplications.

RSA, in simplified mathematical form, chooses primes $p,q$, sets $n=pq$, chooses $e$ relatively prime to $\phi(n)$, and finds $d$ with $ed\equiv1\pmod{\phi(n)}$. Encryption sends $M$ to $C\equiv M^e\pmod n$, and decryption computes $C^d\pmod n$. The practical security rests on the difficulty of factoring large $n$ into $p$ and $q$.

## Visual

```text
Integers modulo 5 split into five residue classes:

[0]: ..., -10, -5, 0, 5, 10, ...
[1]: ...,  -9, -4, 1, 6, 11, ...
[2]: ...,  -8, -3, 2, 7, 12, ...
[3]: ...,  -7, -2, 3, 8, 13, ...
[4]: ...,  -6, -1, 4, 9, 14, ...
```

| Operation | Modular rule | Example modulo $7$ |
| --- | --- | --- |
| reduce | replace by remainder | $31\equiv3$ |
| add | add then reduce | $5+6\equiv11\equiv4$ |
| multiply | multiply then reduce | $4\cdot5\equiv20\equiv6$ |
| inverse | solve $ab\equiv1$ | $3^{-1}\equiv5$ |
| exponentiate | repeated squaring | $3^8\equiv2$ |
| cancel | only invertible factors | can cancel $3$ mod $7$, not $2$ mod $6$ |

## Worked example 1: Solve a linear congruence

**Problem.** Solve

$$
14x\equiv21\pmod{35}.
$$

**Method.**

1. Compute the gcd:

$$
\gcd(14,35)=7.
$$

2. A congruence $ax\equiv b\pmod m$ has a solution only if $\gcd(a,m)\mid b$. Here $7\mid21$, so solutions exist.
3. Divide the congruence by $7$:

$$
2x\equiv3\pmod5.
$$

4. Find the inverse of $2$ modulo $5$. Since $2\cdot3=6\equiv1\pmod5$, the inverse is $3$.
5. Multiply both sides by $3$:

$$
x\equiv9\equiv4\pmod5.
$$

6. Convert back to solutions modulo $35$. The numbers congruent to $4$ modulo $5$ are

$$
4,9,14,19,24,29,34\pmod{35}.
$$

**Checked answer.** The seven incongruent solutions modulo $35$ are $x\equiv4,9,14,19,24,29,34\pmod{35}$. Substituting $x=4$ gives $14\cdot4=56\equiv21\pmod{35}$, and adding $5$ to $x$ preserves the congruence because $14\cdot5=70$ is divisible by $35$.

## Worked example 2: Fast modular exponentiation

**Problem.** Compute $7^{23}\pmod{33}$ without expanding $7^{23}$.

**Method.**

1. Write the exponent in binary:

$$
23=16+4+2+1.
$$

2. Repeatedly square modulo $33$:

$$
\begin{aligned}
7^1&\equiv7\pmod{33},\\
7^2&\equiv49\equiv16\pmod{33},\\
7^4&\equiv16^2=256\equiv25\pmod{33},\\
7^8&\equiv25^2=625\equiv31\pmod{33},\\
7^{16}&\equiv31^2=961\equiv4\pmod{33}.
\end{aligned}
$$

3. Multiply the powers corresponding to $16,4,2,1$:

$$
7^{23}\equiv7^{16}7^4 7^2 7
\equiv4\cdot25\cdot16\cdot7\pmod{33}.
$$

4. Reduce step by step:

$$
\begin{aligned}
4\cdot25&=100\equiv1,\\
1\cdot16&\equiv16,\\
16\cdot7&=112\equiv13.
\end{aligned}
$$

**Checked answer.** $7^{23}\equiv13\pmod{33}$. The computation used five squarings and a few multiplications instead of forming a huge integer.

## Code

```python
def egcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def inv_mod(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("no inverse")
    return x % m

def modexp(base, exp, mod):
    result = 1
    base %= mod
    while exp:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

print(inv_mod(3, 7))
print(modexp(7, 23, 33))
```

The `modexp` routine is the repeated-squaring algorithm used in real modular arithmetic libraries, although production cryptographic code must also handle side-channel concerns and padding schemes.

## Common pitfalls

- Treating $a\bmod m=b$ and $a\equiv b\pmod m$ as the same statement. The first names a remainder; the second is a relation.
- Cancelling a factor that is not invertible modulo $m$.
- Forgetting that a linear congruence may have zero, one, or several solutions modulo $m$.
- Allowing intermediate powers to grow unnecessarily instead of reducing after each multiplication.
- Thinking RSA security depends on the algorithm being secret. The method is public; the factorization of $n$ is the hidden part.
- Using textbook RSA directly for real messages. Practical cryptography requires padding, randomness, validated parameters, and vetted libraries.

When reducing expressions modulo $m$, reduce early and often. The congruence rules allow replacing a large number by any congruent representative, so $37^2\pmod{11}$ can become $4^2\pmod{11}$ and then $16\equiv5\pmod{11}$. This does not change the residue class, but it keeps arithmetic small and reduces mistakes.

Linear congruences require a gcd check before cancellation. The congruence $6x\equiv3\pmod9$ has no solution because $\gcd(6,9)=3$ divides $3$, so actually it does have solutions after reducing to $2x\equiv1\pmod3$; but $6x\equiv4\pmod9$ has none because $3\nmid4$. This distinction is exactly why blind division by $6$ modulo $9$ is invalid.

The Chinese remainder theorem is constructive. To solve $x\equiv a\pmod m$ and $x\equiv b\pmod n$ with $\gcd(m,n)=1$, one can search modulo $mn$ for small examples or build the solution using inverses. The uniqueness is modulo $mn$, meaning every solution differs by a multiple of $mn$.

In cryptography examples, separate the mathematics from the protocol. Modular exponentiation explains how RSA transforms numbers. Real encryption additionally needs message encoding, padding, randomization, parameter validation, and resistance to timing attacks. A discrete mathematics course usually studies the number-theoretic core, not the full engineering standard.

Finally, distinguish congruence classes from their representatives. The class $[3]_{10}$ contains $\dots,-7,3,13,23,\dots$. Writing $x\equiv3\pmod{10}$ identifies a class, not a single integer. If a problem asks for solutions modulo $10$, one representative from each class is enough.

When checking modular computations, substitute the answer into the original congruence rather than only checking the simplified version. If $x\equiv4\pmod5$ came from reducing a congruence modulo $35$, verify several lifted representatives modulo $35$. This catches mistakes in the number of solution classes and in the modulus after division by a gcd.

It is also helpful to keep a table of units for small moduli. Modulo $10$, only $1,3,7,9$ have inverses. Modulo a prime $p$, every nonzero residue has an inverse. This difference explains why fields such as $\mathbb{Z}_p$ behave much more like ordinary arithmetic than composite-modulus systems such as $\mathbb{Z}_{10}$.

For worked cryptography exercises, use intentionally small primes only to understand the mechanism. Small RSA examples are insecure precisely because factoring $n$ is easy. The lesson is the algebraic loop: choose relatively prime exponents, use an inverse modulo $\phi(n)$, and rely on modular exponentiation for encryption and decryption. Do not infer practical parameter sizes or security practices from classroom-sized numbers.

In modular arithmetic, the modulus is part of the statement. The claim $x\equiv2$ is incomplete until the modulus is named. Changing the modulus changes the residue classes, the invertible elements, and the number of distinct solutions.

For that reason, carry the modulus through every displayed step instead of mentioning it only at the beginning.

This habit makes invalid cancellation easier to notice.

## Connections

- [Number theory basics](/math/discrete/number-theory-basics) supplies divisibility, gcds, primes, and Bezout coefficients.
- [Algorithms and complexity](/math/discrete/algorithms-and-complexity) explains why repeated squaring is efficient.
- [Relations](/math/discrete/relations) frames congruence modulo $m$ as an equivalence relation.
- [Equivalence relations and partial orders](/math/discrete/equivalence-relations-and-partial-orders) studies residue classes as equivalence classes.
- [Finite-state machines and computation](/math/discrete/finite-state-machines-and-computation) connects modular arithmetic to finite memory and cyclic state.
