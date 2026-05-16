---
title: Euler, Hamilton, Planarity, and Coloring
sidebar_position: 22
---

# Euler, Hamilton, Planarity, and Coloring

Several classic graph questions ask for special traversals or drawings. Euler paths use every edge exactly once. Hamilton paths visit every vertex exactly once. Planarity asks whether a graph can be drawn without crossings. Coloring asks how to label vertices so adjacent vertices differ.

These problems look similar because they all concern graph structure, but their difficulty differs sharply. Euler paths have a complete degree test. Hamilton circuits do not have a simple necessary-and-sufficient degree test. Planarity has structural characterizations and useful inequalities. Coloring is easy to state but can be computationally difficult.

![Three vertices on one side are connected to three vertices on the other side in the complete bipartite graph K three three.](https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Complete_bipartite_graph_K3%2C3.svg/500px-Complete_bipartite_graph_K3%2C3.svg.png)

*Figure: The complete bipartite graph $K_{3,3}$, a classical nonplanar graph. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Complete_bipartite_graph_K3%2C3.svg), David Benbennick, public domain.*

## Definitions

An **Euler path** uses every edge of a graph exactly once. An **Euler circuit** is an Euler path that starts and ends at the same vertex.

A **Hamilton path** visits every vertex exactly once. A **Hamilton circuit** visits every vertex exactly once and returns to the starting vertex. Hamilton questions constrain vertices, while Euler questions constrain edges.

A graph is **planar** if it can be drawn in the plane with edges crossing only at shared endpoints. A planar drawing divides the plane into regions called **faces**, including the unbounded outside face.

A **proper vertex coloring** assigns colors to vertices so adjacent vertices have different colors. The **chromatic number** $\chi(G)$ is the fewest colors needed. A graph is **$k$-colorable** if it has a proper coloring using at most $k$ colors.

A **bridge** is an edge whose removal increases the number of connected components. A **cut vertex** is a vertex whose removal increases the number of connected components. These features often affect Euler and Hamilton behavior.

## Key results

For a connected undirected multigraph with at least two vertices:

- It has an Euler circuit if and only if every vertex has even degree.
- It has an Euler path but not an Euler circuit if and only if exactly two vertices have odd degree.

Necessity is based on entering and leaving vertices in pairs. A circuit enters and exits every time it visits a vertex, so all degrees are even. For a non-closed Euler path, only the start and end vertices have one unpaired incident edge. The converse can be proved constructively by building trails and splicing unused cycles.

Euler's formula for a connected planar graph is

$$
v-e+f=2.
$$

For connected planar simple graphs with $v\ge3$,

$$
e\le3v-6.
$$

If the graph has no triangles, then

$$
e\le2v-4.
$$

These inequalities prove that $K_5$ and $K_{3,3}$ are nonplanar. For $K_5$, $v=5$ and $e=10$, but $3v-6=9$. For $K_{3,3}$, there are no triangles, $v=6$, and $e=9$, but $2v-4=8$.

Unlike Euler circuits, Hamilton circuits have no simple degree test that is both necessary and sufficient. Sufficient conditions exist, such as Dirac's theorem: if a simple graph has $n\ge3$ vertices and every vertex has degree at least $n/2$, then it has a Hamilton circuit.

Every planar graph is $4$-colorable, by the four color theorem. Many elementary problems require fewer tools: bipartite graphs are exactly the graphs with chromatic number at most $2$, except edgeless graphs may have chromatic number $1$.

## Visual

```mermaid
graph LR
  A("(a")) --- B("(b"))
  B --- C("(c"))
  C --- D("(d"))
  D --- A
  A --- C
```

| Question | Object used exactly once | Main tool | Warning |
| --- | --- | --- | --- |
| Euler path | every edge | odd-degree count | vertices may repeat |
| Euler circuit | every edge, return home | all degrees even | graph must be connected apart from isolated vertices |
| Hamilton path | every vertex | structural search or sufficient theorems | edges may be unused |
| planarity | drawing without crossings | Euler formula and inequalities | a bad drawing does not prove nonplanarity |
| coloring | adjacent vertices differ | greedy, bipartite test, bounds | greedy may use too many colors |

## Worked example 1: Decide whether an Euler path exists

**Problem.** A connected graph has vertices $a,b,c,d,e$ with degrees

$$
3,2,4,3,2.
$$

Does it have an Euler circuit? Does it have an Euler path?

**Method.**

1. Count odd degrees. The odd degrees are $3$ and $3$, at vertices $a$ and $d$.
2. There are exactly two odd-degree vertices.
3. A connected graph has an Euler circuit only when every vertex has even degree. This condition fails.
4. A connected graph has an Euler path but not a circuit when exactly two vertices have odd degree. This condition holds.
5. The Euler path, if constructed, must start at one odd-degree vertex and end at the other.

**Checked answer.** The graph has no Euler circuit, but it has an Euler path. Any Euler path must start at $a$ and end at $d$, or start at $d$ and end at $a$.

## Worked example 2: Use Euler's inequality to prove nonplanarity

**Problem.** Prove that $K_{3,3}$ is nonplanar using Euler's formula.

**Method.**

1. $K_{3,3}$ has $v=6$ vertices, split into two parts of size $3$.
2. Every vertex in one part connects to all $3$ vertices in the other part, so

$$
e=3\cdot3=9.
$$

3. $K_{3,3}$ has no triangles because it is bipartite. Every cycle in a bipartite graph has even length.
4. A planar simple graph with no triangles and $v\ge3$ must satisfy

$$
e\le2v-4.
$$

5. Substitute $v=6$:

$$
e\le2(6)-4=8.
$$

6. But $K_{3,3}$ has $e=9$.

**Checked answer.** The inequality required of triangle-free planar simple graphs is violated, so $K_{3,3}$ is nonplanar.

## Code

```python
def euler_status(graph):
    odd = [v for v, nbrs in graph.items() if len(nbrs) % 2 == 1]
    if len(odd) == 0:
        return "Euler circuit possible", odd
    if len(odd) == 2:
        return "Euler path possible", odd
    return "No Euler path", odd

def greedy_coloring(graph):
    color = {}
    for v in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        used = {color[w] for w in graph[v] if w in color}
        c = 0
        while c in used:
            c += 1
        color[v] = c
    return color

G = {"a": {"b", "d", "c"}, "b": {"a", "c"}, "c": {"a", "b", "d", "e"}, "d": {"a", "c", "e"}, "e": {"c", "d"}}
print(euler_status(G))
print(greedy_coloring(G))
```

The Euler test is exact for connected undirected graphs. The greedy coloring algorithm is heuristic: it always produces a proper coloring, but not always one with the fewest colors.

## Common pitfalls

- Confusing Euler and Hamilton conditions. Euler uses edges; Hamilton uses vertices.
- Applying the Euler degree test to a disconnected graph without checking connectivity.
- Assuming a drawing with crossings proves nonplanarity. A different drawing might remove them.
- Using $e\le3v-6$ for graphs with $v\lt 3$ or for multigraphs without checking hypotheses.
- Forgetting the triangle-free condition before using $e\le2v-4$.
- Treating greedy coloring as an exact chromatic-number algorithm.

Euler path problems should begin by removing isolated vertices from the connectivity check. Isolated vertices have degree $0$ and do not affect an edge-using walk, but all vertices with nonzero degree must lie in one connected component. After that, the odd-degree count gives the exact answer for undirected graphs.

Hamilton problems are different because degree parity is not decisive. A graph may have all even degrees and still fail to have a Hamilton circuit. Conversely, a graph with odd-degree vertices can have a Hamilton circuit. Hamilton reasoning often uses cut vertices, degree conditions, exhaustive search, or known sufficient theorems rather than the Euler test.

Planarity arguments using inequalities are one-way tests. If a graph violates $e\le3v-6$, it is nonplanar. If it satisfies the inequality, it may still be nonplanar; the inequality is necessary, not sufficient. The same caution applies to the triangle-free bound. These tests are powerful for $K_5$ and $K_{3,3}$ but do not decide every graph.

For coloring, lower and upper bounds are both useful. A clique of size $k$ forces at least $k$ colors. A successful coloring with $k$ colors proves at most $k$ colors are needed. When the lower and upper bounds match, the chromatic number is known. Greedy coloring gives an upper bound, but a poor vertex order can use more colors than necessary.

Map coloring models regions as vertices only when adjacency means sharing a boundary segment, not merely touching at a point. This modeling convention matters because point-touching regions need not receive different colors in the usual map-coloring problem.

For Euler questions, vertices of degree zero can be ignored for the edge traversal but not for statements that require the whole graph to be connected. Many textbooks state the theorem for connected graphs, while applications sometimes allow isolated vertices because they do not affect edge use. State the convention being used.

For coloring problems, a greedy coloring should be followed by a lower-bound argument if the chromatic number is requested. A triangle proves at least three colors; a displayed three-coloring proves at most three. Together they prove exactly three. Without the lower bound, the coloring only gives an upper bound.

## Connections

- [Graphs basics](/math/discrete/graphs-basics) supplies degree, complete graph, and bipartite graph definitions.
- [Graph paths, connectivity, and shortest paths](/math/discrete/graph-paths-connectivity-shortest-paths) supplies path and connectivity language.
- [Trees](/math/discrete/trees) are planar connected graphs with no cycles and satisfy $e=v-1$.
- [Algorithms and complexity](/math/discrete/algorithms-and-complexity) studies the computational difficulty of Hamilton and coloring problems.
- [Finite-state machines and computation](/math/discrete/finite-state-machines-and-computation) connects graph traversal to state-space search.
