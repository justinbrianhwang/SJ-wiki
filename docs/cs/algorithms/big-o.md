---
title: Big-O Notation
sidebar_position: 2
---

# Big-O Notation

Running time measured in seconds is tied to a machine, compiler, input, and implementation. Counting operations is more portable, but an exact count can bury the useful comparison under details. Asymptotic notation keeps the part that survives when the input grows: whether the work is proportional to $n$, $n\log n$, $n^2$, or something worse.

The notation describes functions, not programs by itself. An algorithm has a cost function only after the input-size parameter and the counted resource have been stated. For an array algorithm, $n$ may be the number of elements and the resource may be comparisons. For a graph algorithm, the natural parameters are usually both $\vert V\vert $ and $\vert E\vert $. Space usage can be analyzed with the same notation.

## Upper bounds, lower bounds, and tight bounds

For eventually nonnegative functions $f$ and $g$, write $f(n)=O(g(n))$ if there are constants $c\gt 0$ and $n_0$ such that

$$
0\le f(n)\le c g(n)\qquad\text{for every }n\ge n_0.
$$

The constants may depend on the algorithm, but not on $n$. The definition ignores a finite prefix of small inputs and permits a fixed multiplicative factor.

The companion notations are

$$
\begin{aligned}
f(n)=\Omega(g(n))
&\iff \exists c>0,n_0:\ 0\le c g(n)\le f(n)\text{ for }n\ge n_0,\\
f(n)=\Theta(g(n))
&\iff f(n)=O(g(n))\text{ and }f(n)=\Omega(g(n)).
\end{aligned}
$$

$\Theta$ gives an asymptotically tight rate. If $f(n)=3n^2+7n+4$, saying $f(n)=O(n^3)$ is true but loose; $f(n)=\Theta(n^2)$ carries more information. A bound can be mathematically correct and still be a poor description.

Little-o expresses strict separation:

$$
f(n)=o(g(n))\iff \lim_{n\to\infty}\frac{f(n)}{g(n)}=0,
$$

when the limit exists. Thus $n=o(n\log n)$, while $n\log n$ is not $o(n\log n)$. Little-omega is the analogous strict lower relation.

## Why constants and lower-order terms disappear

Suppose an implementation performs

$$
T(n)=6n^2+20n+100
$$

primitive operations. For $n\ge 1$, both $n\le n^2$ and $1\le n^2$, so

$$
\begin{aligned}
T(n)
&=6n^2+20n+100\\
&\le 6n^2+20n^2+100n^2\\
&=126n^2.
\end{aligned}
$$

Taking $c=126$ and $n_0=1$ proves $T(n)=O(n^2)$. For a matching lower bound, $T(n)\ge 6n^2$ for every positive $n$, so $T(n)=\Omega(n^2)$. Hence $T(n)=\Theta(n^2)$.

Dropping constants does not claim that constants never matter. An $O(n)$ routine with expensive network calls can lose to a compact $O(n\log n)$ routine over every input the application will see. Asymptotic analysis says what happens under unbounded growth; benchmarking says where the crossover lies on the actual system. Both questions are legitimate.

The logarithm base is omitted because changing bases contributes only a constant:

$$
\log_a n=\frac{\log_b n}{\log_b a}=\Theta(\log_b n).
$$

Base $2$ is usually implicit when repeated halving is involved. The base still matters when an exact comparison count is wanted.

## Reading loops without counting every instruction

A single loop is not automatically linear. Its update rule determines how many iterations occur.

```python
for i in range(n):              # n iterations
    use(i)

i = 1
while i < n:                   # ceil(log_2 n) iterations
    use(i)
    i *= 2
```

The first loop is $\Theta(n)$ if `use` costs constant time. In the second, after $k$ iterations $i=2^k$. It stops when $2^k\ge n$, so $k=\lceil\log_2 n\rceil$ and the loop is $\Theta(\log n)$.

For sequential blocks, add costs and keep the dominant term. A $\Theta(n)$ scan followed by a $\Theta(n^2)$ table fill costs $\Theta(n+n^2)=\Theta(n^2)$. For nested loops, multiplication is valid only when the inner work has the stated cost for each outer iteration.

```python
for i in range(n):
    for j in range(i):
        use(i, j)
```

The inner loop runs $i$ times, not $n$ times. The total is

$$
\sum_{i=0}^{n-1}i=\frac{n(n-1)}{2}=\Theta(n^2).
$$

The triangular shape changes the constant but not the class. A less regular nest may need a sum rather than the shortcut “two loops means quadratic.” Consider:

```python
for i in range(1, n + 1):
    j = i
    while j <= n:
        use(i, j)
        j += i
```

For a fixed $i$, the inner loop runs $\lfloor n/i\rfloor$ times. Total work is

$$
\sum_{i=1}^{n}\left\lfloor\frac{n}{i}\right\rfloor
\le n\sum_{i=1}^{n}\frac{1}{i}
=nH_n
=\Theta(n\log n),
$$

where $H_n$ is the $n$th harmonic number. A corresponding lower estimate gives a tight $\Theta(n\log n)$ result.

## Recurrences from recursive algorithms

Recursive code is commonly described by a recurrence. Binary search does constant work and recurses into half the array:

$$
T(n)=T(n/2)+\Theta(1).
$$

After $k$ expansions,

$$
T(n)=T(n/2^k)+k\Theta(1).
$$

The base case is reached when $n/2^k=1$, or $k=\log_2 n$. Therefore $T(n)=\Theta(\log n)$.

Merge sort makes two half-size recursive calls and merges in linear time:

$$
T(n)=2T(n/2)+\Theta(n).
$$

At recursion level $j$, there are $2^j$ subproblems of size $n/2^j$. Their merge work totals

$$
2^j\cdot\Theta\left(\frac{n}{2^j}\right)=\Theta(n).
$$

There are $\log_2 n+1$ levels, so the entire cost is $\Theta(n\log n)$. The recursion tree explains the result rather than merely naming the Master theorem.

Recurrences require care when subproblems overlap. The naive Fibonacci recurrence $T(n)=T(n-1)+T(n-2)+\Theta(1)$ grows exponentially because the same values are recomputed. Memoization changes the executed computation: each of the $n$ states is solved once, producing $\Theta(n)$ time and $\Theta(n)$ stored results.

## A scale for common classes

| Class | Typical source | Scale at $n=1{,}000$ |
|---|---|---:|
| $\Theta(1)$ | array indexing, stack push | constant |
| $\Theta(\log n)$ | repeated halving, balanced-tree height | about $10$ for base $2$ |
| $\Theta(n)$ | one full scan | $1{,}000$ |
| $\Theta(n\log n)$ | comparison sorting, divide and combine | about $10{,}000$ |
| $\Theta(n^2)$ | all ordered pairs | $1{,}000{,}000$ |
| $\Theta(n^3)$ | a triple all-pairs loop | $1{,}000{,}000{,}000$ |
| $\Theta(2^n)$ | enumerating all subsets | already enormous |
| $\Theta(n!)$ | enumerating all permutations | larger still |

The scale column is illustrative, not a runtime prediction. It omits operation cost and constants. It does show why moving from quadratic to $n\log n$ often matters more than low-level tuning once $n$ becomes large.

Multivariable bounds need more precision than a single $n$. Breadth-first search with adjacency lists costs $O(\vert V\vert +\vert E\vert )$; replacing it by $O(n)$ hides which graph feature grows. An adjacency matrix traversal costs $O(\vert V\vert ^2)$ even if there are few edges. Keeping both parameters exposes the representation tradeoff.

## Algebra for combining bounds

Asymptotic bounds can be manipulated much like inequalities, provided the functions are eventually nonnegative. If $f=O(g)$ and $h=O(k)$, then

$$
f+h=O(g+k)
$$

and

$$
fh=O(gk).
$$

If one term dominates the other, the sum simplifies. For example, $n=O(n\log n)$ for $n\ge2$, so $O(n+n\log n)=O(n\log n)$. Sequential phases add. A loop that invokes a $\Theta(\log n)$ operation $n$ times multiplies to $\Theta(n\log n)$ when every invocation has that cost.

Conditional branches use the cost of the path under analysis. For a worst-case bound, take the more expensive reachable branch. If one branch costs $\Theta(n)$ and another costs $\Theta(n^2)$, the worst case is $\Theta(n^2)$; it is not $\Theta(n+n^2)$ because a single execution takes only one branch. Expected analysis instead weights branches by their probabilities, which must be supplied rather than guessed.

Transitivity is useful for proofs. If $f=O(g)$ and $g=O(h)$, then $f=O(h)$. Symmetry does not hold: $n=O(n^2)$ but $n^2\ne O(n)$. Big-O is therefore not an equality relation despite the conventional equals sign. Read $f(n)=O(g(n))$ as membership in a set of functions bounded by a constant multiple of $g$.

Not every pair of functions has a clean eventual ordering. Oscillating functions can alternate which one is larger. Algorithm cost functions are often monotone enough that standard classes compare neatly, but the definition itself does not require monotonicity.

## Limit comparisons as a shortcut

For positive functions, the ratio

$$
L=\lim_{n\to\infty}\frac{f(n)}{g(n)}
$$

often settles the relationship. If $0\lt L\lt \infty$, then $f=\Theta(g)$. If $L=0$, then $f=o(g)$ and therefore $f=O(g)$. If the limit is infinite, $f$ grows strictly faster than $g$.

Take $f(n)=7n^2+3n$ and $g(n)=n^2$. Dividing numerator and denominator by $n^2$ gives

$$
\lim_{n\to\infty}\frac{7n^2+3n}{n^2}
=\lim_{n\to\infty}\left(7+\frac{3}{n}\right)
=7.
$$

The finite positive limit proves $f=\Theta(n^2)$. For logarithms versus powers,

$$
\lim_{n\to\infty}\frac{\log n}{n^\varepsilon}=0
$$

for every fixed $\varepsilon\gt 0$. Thus even a small positive power eventually outgrows a logarithm. Similarly, every fixed-degree polynomial is asymptotically smaller than $a^n$ for fixed $a\gt 1$.

The limit test is sufficient, not necessary. A ratio may oscillate without converging even though constant upper and lower bounds still prove a $\Theta$ relation. The original constant-based definition remains the authority.

## Input-sensitive bounds

Worst-case analysis can hide structure that an algorithm exploits. Insertion sort has $\Theta(n^2)$ worst-case time, but if the input contains only $r$ inversions, its work can be expressed as $\Theta(n+r)$. When an array is already sorted, $r=0$ and the scan is linear. Such a parameterized bound explains behavior that a single function of $n$ cannot.

Output size can also impose a lower bound. An algorithm that explicitly lists all $k$ reported matches needs $\Omega(k)$ time merely to write them. Reporting every edge of a dense graph costs $\Omega(V^2)$ because the output itself may contain that many records. No data structure can evade the cost of materializing an output the caller requested.

For numeric algorithms, distinguish the magnitude of a number from its encoded length. An integer $m$ uses $\Theta(\log m)$ bits. A loop that counts from `1` to `m` is polynomial in the value $m$ but exponential in the input length. Complexity theory normally measures encoded length; ordinary application analysis sometimes uses a domain quantity directly. State the convention before interpreting the class.

## Worked example: a halving loop with a linear body

Consider an outer value that doubles while the body scans the entire array:

```python
i = 1
while i < n:
    for x in values:            # len(values) == n
        consume(x)
    i *= 2
```

Let $k$ be the number of outer iterations. The values of `i` are $1,2,4,\ldots,2^{k-1}$, and the loop ends once $2^k\ge n$. Thus

$$
k=\lceil\log_2 n\rceil.
$$

Every outer iteration performs $n$ calls to `consume`, so the exact number of calls is

$$
n\lceil\log_2 n\rceil.
$$

An upper bound follows from $\lceil\log_2 n\rceil\le\log_2 n+1$, and a lower bound follows from $\lceil\log_2 n\rceil\ge\log_2 n$. Therefore the running time is $\Theta(n\log n)$, assuming `consume` takes constant time. The logarithmic outer loop does not make the whole routine logarithmic.

## Worked example: amortized array growth

A dynamic array often doubles its capacity when full. One append usually writes one element, but a resizing append may copy every old element. The worst case for a single append is $\Theta(n)$, yet a sequence of appends has constant amortized cost.

Start with capacity $1$ and append $n$ items. Resizes copy arrays of sizes

$$
1,2,4,8,\ldots,2^k<n.
$$

Their total copying cost is a geometric sum:

$$
1+2+4+\cdots+2^k=2^{k+1}-1<2n.
$$

The $n$ appends also perform $n$ writes into their final slots. Total work over the sequence is below $3n$, so the average per append is bounded by a constant. Append is $O(1)$ amortized, although an individual append remains $O(n)$ in the worst case. Amortized analysis makes no random-input assumption; it distributes occasional expensive operations across a whole operation sequence.

## Best, worst, expected, and amortized costs

These qualifiers answer different questions. Linear search has best-case $\Theta(1)$ time if the first item matches and worst-case $\Theta(n)$ time if the key is absent. Under a model where a successful key is equally likely to occupy any position, it performs $(n+1)/2$ comparisons on average, still $\Theta(n)$.

Expected time averages over stated randomness, which may come from the input distribution or the algorithm itself. A randomized quicksort analysis can hold for every fixed input while taking expectation over random pivot choices. An average-case input analysis instead needs probabilities for the inputs.

Amortized time has no probability distribution. It bounds the total cost of any operation sequence and divides that total across the operations. Dynamic-array append is the standard example; disjoint-set operations supply a subtler one.

## Bounds that are easy to misstate

- A library call is not automatically $O(1)$. Python list membership is linear, while dictionary membership is expected constant time under the usual hash-table model.
- Average-case and expected bounds require a probability model. “Usually fast” is not a mathematical distribution.
- Input encoding matters. Trial division up to $\sqrt m$ takes $O(\sqrt m)$ arithmetic steps as a function of the numeric value $m$, but $m$ has only $\Theta(\log m)$ bits. Expressed in bit length, that loop is exponential.
- Space may mean total space or auxiliary space. Merge sort uses $\Theta(n)$ auxiliary array storage in a common implementation; the input itself is not normally charged as auxiliary space.
- A tight bound for one operation may conceal a larger setup cost. Binary search is $\Theta(\log n)$ per query, but sorting previously unsorted data costs $\Theta(n\log n)$ with a comparison sort.
- Hash-table lookup is commonly $O(1)$ expected and $O(n)$ worst case. Writing only $O(1)$ loses the qualification that makes the claim accurate.
- If $n$ is small or capped by the domain, asymptotics alone may not decide the implementation. Memory traffic and constant factors can dominate.

<div className="see-also">

See also: [Algorithms and complexity](/math/discrete/algorithms-and-complexity) · [Recurrence relations](/math/discrete/recurrence-relations) · [Divide and conquer](/cs/algorithms/divide-and-conquer) · [Sorting algorithms](/cs/algorithms/sorting-algorithms) · [Time complexity, P, and NP](/cs/theory/time-complexity-p-and-np)

</div>
