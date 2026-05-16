---
title: Edge Colouring and Chromatic Polynomials
sidebar_position: 11
---

# Edge Colouring and Chromatic Polynomials

Edge colouring assigns colours to edges so that adjacent edges receive different colours. It is the natural model for scheduling pairwise interactions: games sharing a team, jobs sharing a machine, or communication links sharing a port cannot happen in the same time slot. Unlike vertex colouring, edge colouring is controlled closely by the maximum degree, but the exact answer still contains subtle structure.

Chromatic polynomials count proper vertex colourings as a function of the number of available colours. They refine the yes/no question "is this graph $k$-colourable?" into "how many $k$-colourings does it have?" This gives a bridge from graph theory to algebra and combinatorics.

## Definitions

A **proper edge colouring** of a graph $G$ assigns colours to edges so that any two edges sharing an endpoint have different colours. The **chromatic index** $\chi'(G)$ is the least number of colours needed.

The **line graph** $L(G)$ has one vertex for each edge of $G$, with two vertices adjacent in $L(G)$ exactly when the corresponding edges of $G$ share an endpoint. Edge colouring $G$ is the same as vertex colouring $L(G)$, so

$$
\chi'(G)=\chi(L(G)).
$$

The **chromatic polynomial** $P_G(k)$ counts the number of proper vertex colourings of $G$ using colours from a set of size $k$. It is a polynomial in $k$ for every finite graph.

For an edge $e$ that is not a loop, $G-e$ denotes deletion of $e$, and $G/e$ denotes contraction of $e$.

## Key results

**Lower bound for edge colouring.**

$$
\chi'(G)\ge \Delta(G),
$$

because all edges incident with a vertex of maximum degree need distinct colours.

**Vizing's theorem.** For every simple graph,

$$
\Delta(G)\le \chi'(G)\le \Delta(G)+1.
$$

Graphs with $\chi'(G)=\Delta(G)$ are called Class 1; graphs with $\chi'(G)=\Delta(G)+1$ are Class 2.

**Konig's line-colouring theorem.** If $G$ is bipartite, then

$$
\chi'(G)=\Delta(G).
$$

**Deletion-contraction for chromatic polynomials.** If $e$ is not a loop, then

$$
P_G(k)=P_{G-e}(k)-P_{G/e}(k).
$$

Reason: colourings of $G-e$ either give different colours to the endpoints of $e$, in which case they are colourings of $G$, or give the same colour to the endpoints, in which case they correspond to colourings of $G/e$.

**Special values of chromatic polynomials.** If $G$ has at least one vertex, then $P_G(0)=0$ because there are no colours available. If $G$ has at least one edge, then $P_G(1)=0$ because adjacent vertices cannot share the only colour. The value $P_G(2)$ detects bipartiteness for connected graphs: it is $2$ when $G$ is connected and bipartite, and $0$ when $G$ has an odd cycle.

**Leading terms.** For a graph with $n$ vertices and $m$ edges,

$$
P_G(k)=k^n-mk^{n-1}+\text{lower-degree terms}.
$$

The leading term counts all colour assignments. The next term subtracts assignments that violate one specified edge, and the lower-order terms correct overlaps among violations. This gives a quick check on small polynomial computations.

**Edge colouring through line graphs.** Because $\chi'(G)=\chi(L(G))$, every theorem about vertex colouring can be applied to edge colouring after forming the line graph. The translation is powerful but can obscure the original graph. For example, a clique in $L(G)$ may come from all edges incident with one high-degree vertex, or from the three edges of a triangle in $G$.

**Planar connection.** Edge colouring also interacts with map colouring. For a plane cubic graph, face colouring of the dual and edge colouring of the original graph are closely related. Historically, several equivalent formulations of the four-colour problem passed through edge-colouring statements about cubic planar graphs. This is one reason Wilson treats vertex colouring, map colouring, edge colouring, and chromatic polynomials in the same chapter.

**Chromatic roots.** The values of $k$ for which $P_G(k)=0$ are called chromatic roots. The integers $0,1,\dots,\chi(G)-1$ are always roots in the sense that no proper colouring exists with that many colours. Noninteger chromatic roots are a deeper topic, but even at an introductory level they remind us that $P_G(k)$ is both a counting function and an algebraic object.

**Disjoint unions.** If $G$ is the disjoint union of $G_1$ and $G_2$, then

$$
P_G(k)=P_{G_1}(k)P_{G_2}(k).
$$

Colour choices on different components are independent.

## Visual

The triangle needs three edge colours because every pair of edges is adjacent.

```mermaid
graph LR
  A("(A")) ---|red| B("(B"))
  B ---|blue| C("(C"))
  C ---|green| A
```

| Graph $G$ | $\Delta(G)$ | $\chi'(G)$ | Chromatic polynomial |
|---|---:|---:|---|
| Path $P_n$ with $n\ge 2$ | 2 or 1 | 2 or 1 | $k(k-1)^{n-1}$ |
| Cycle $C_{2r}$ | 2 | 2 | $(k-1)^{2r}+(k-1)$ |
| Cycle $C_{2r+1}$ | 2 | 3 | $(k-1)^{2r+1}-(k-1)$ |
| Complete graph $K_3$ | 2 | 3 | $k(k-1)(k-2)$ |
| Complete bipartite $K_{r,s}$ | $\max(r,s)$ | $\max(r,s)$ | no single short form |

## Worked example 1: Edge-colour an odd cycle

**Problem.** Find $\chi'(C_5)$.

**Method.**

1. The graph $C_5$ has maximum degree

$$
\Delta(C_5)=2.
$$

2. Therefore $\chi'(C_5)\ge 2$.
3. Suppose two edge colours were enough. Around the cycle, adjacent edges must alternate colours:

$$
1,2,1,2,1.
$$

4. The first and last edges of the cycle are adjacent, but both would have colour $1$. This is impossible.
5. So $\chi'(C_5)\ge 3$.
6. Three colours suffice: colour the first four edges $1,2,1,2$ and the last edge $3$.

**Checked answer.**

$$
\chi'(C_5)=3.
$$

This agrees with the general rule that odd cycles are Class 2.

## Worked example 2: Compute a chromatic polynomial by deletion-contraction

**Problem.** Compute $P_{P_3}(k)$ for the path $a-b-c$ using deletion-contraction on edge $bc$.

**Method.**

Let $G=P_3$ and $e=bc$.

1. Delete $e$. The graph $G-e$ has one edge $ab$ and an isolated vertex $c$.
2. The edge $ab$ can be coloured in $k(k-1)$ ways, and $c$ can be coloured independently in $k$ ways. Therefore

$$
P_{G-e}(k)=k^2(k-1).
$$

3. Contract $e=bc$. The vertices $b$ and $c$ merge, and the result is a single edge between $a$ and the merged vertex. Hence

$$
P_{G/e}(k)=k(k-1).
$$

4. Apply deletion-contraction:

$$
P_G(k)=P_{G-e}(k)-P_{G/e}(k).
$$

5. Substitute:

$$
\begin{aligned}
P_G(k) &= k^2(k-1)-k(k-1)\\
&= k(k-1)(k-1)\\
&= k(k-1)^2.
\end{aligned}
$$

**Check.** Directly, colour $a$ in $k$ ways, then $b$ in $k-1$ ways, then $c$ in $k-1$ ways because it only needs to differ from $b$. The answer matches.

The leading-term check also works:

$$
k(k-1)^2=k^3-2k^2+k.
$$

The path has $3$ vertices and $2$ edges, so the first two terms should be $k^3-2k^2$, exactly as computed.

## Code

This exact chromatic-polynomial routine uses deletion-contraction symbolically through SymPy. It is meant for small simple graphs.

```python
from functools import lru_cache
import sympy as sp

k = sp.symbols("k")

def normalize(vertices, edges):
    vertices = tuple(sorted(vertices))
    edges = tuple(sorted(tuple(sorted(e)) for e in edges if e[0] != e[1]))
    return vertices, tuple(sorted(set(edges)))

@lru_cache(None)
def chrom_poly(vertices, edges):
    vertices, edges = normalize(vertices, edges)
    if not edges:
        return k ** len(vertices)
    u, v = edges[0]
    deleted = tuple(e for e in edges if e != (u, v))
    merged_vertices = tuple(x for x in vertices if x != v)
    contracted_edges = []
    for a, b in deleted:
        a = u if a == v else a
        b = u if b == v else b
        if a != b:
            contracted_edges.append(tuple(sorted((a, b))))
    return sp.expand(chrom_poly(vertices, deleted) - chrom_poly(merged_vertices, tuple(contracted_edges)))

print(chrom_poly(("a", "b", "c"), (("a", "b"), ("b", "c"))))
```

The recursive code recomputes many isomorphic subproblems unless caching catches the exact normalized edge set. Serious implementations use canonical graph forms or specialized deletion-contraction strategies. For small examples, however, the code mirrors the theorem closely enough to be useful as a checking tool.

As a quick sanity check, evaluate a computed chromatic polynomial at small integers. For a graph with an edge, $P_G(1)$ should be $0$. For a connected bipartite graph, $P_G(2)$ should be $2$; for a graph containing an odd cycle, it should be $0$.

For edge-colouring, do the analogous check at a maximum-degree vertex. If a vertex has degree $\Delta$, then its incident edges already require $\Delta$ distinct colours. Any proposed colouring with fewer is impossible before the rest of the graph is considered.

For chromatic polynomial computations, keep the graph operation visible beside the algebra. Deleting an edge and contracting an edge produce different graphs, and the subtraction order matters. For edge-colouring, sketch the line graph only when it clarifies adjacency among edges; otherwise, checking edge conflicts directly in the original graph is often cleaner.

## Common pitfalls

- Confusing vertex colouring with edge colouring. Adjacent edges share an endpoint; adjacent vertices share an edge.
- Assuming every graph satisfies $\chi'(G)=\Delta(G)$. Odd cycles and many complete graphs require $\Delta+1$ colours.
- Applying Konig's line-colouring theorem to non-bipartite graphs.
- Forgetting that a loop makes proper vertex colouring impossible and also disrupts ordinary edge-colouring assumptions.
- Counting colourings "up to renaming colours" when computing $P_G(k)$. The chromatic polynomial counts actual assignments from a fixed colour set.
- Using deletion-contraction with the signs reversed.

## Connections

- [Vertex and map colouring](/math/graph-theory/vertex-and-map-colouring)
- [Matchings Hall and Konig](/math/graph-theory/matchings-hall-and-konig)
- [Algebraic graph theory basics](/math/graph-theory/algebraic-graph-theory-basics)
- [Ramsey theory basics](/math/graph-theory/ramsey-theory-basics)
