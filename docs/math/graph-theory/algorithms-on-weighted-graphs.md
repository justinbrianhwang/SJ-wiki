---
title: Algorithms on Weighted Graphs
sidebar_position: 5
---

# Algorithms on Weighted Graphs

Weighted graphs attach numerical costs, lengths, capacities, or rewards to edges. This changes the basic question from "is there a route?" to "which route is best?" The same graph can model a road network with travel times, a communication network with latencies, a pipeline with construction costs, or a dependency graph with penalties.

Two families of problems dominate the introductory theory. **Shortest path** algorithms minimize the total weight of a route between vertices. **Minimum spanning tree** algorithms connect all vertices with minimum total edge weight. Both are greedy in important cases, but the reason the greedy choice is valid is different in each setting.

## Definitions

A **weighted graph** is a graph $G$ together with a weight function

$$
w:E(G)\to \mathbb{R}.
$$

The **weight** of a path is the sum of the weights of its edges. A **shortest path** from $s$ to $t$ is a path of minimum total weight among all $s$-$t$ paths. If negative edge weights are present, shortest paths are still meaningful unless a reachable negative cycle allows the cost to decrease without bound.

A **spanning tree** of a connected graph is a subgraph that includes every vertex and is a tree. A **minimum spanning tree** (MST) is a spanning tree of minimum total edge weight.

Common algorithms:

| Problem | Algorithm | Weight condition | Typical time with binary heap |
|---|---|---|---|
| Single-source shortest paths | BFS | all weights equal | $O(n+m)$ |
| Single-source shortest paths | Dijkstra | nonnegative weights | $O((n+m)\log n)$ |
| Single-source shortest paths | Bellman-Ford | negative allowed, no reachable negative cycle | $O(nm)$ |
| All-pairs shortest paths | Floyd-Warshall | negative allowed, no negative cycle | $O(n^3)$ |
| Minimum spanning tree | Kruskal | any real weights | $O(m\log m)$ |
| Minimum spanning tree | Prim | any real weights | $O(m\log n)$ |

## Key results

**Dijkstra invariant.** In a graph with nonnegative edge weights, when Dijkstra's algorithm permanently selects an unsettled vertex $u$ of minimum tentative distance, that tentative distance is the true shortest distance from the source to $u$.

Proof sketch: any alternative route to $u$ would have to pass through an unsettled vertex first. Because all remaining edge weights are nonnegative, that route cannot become cheaper than the current minimum tentative distance.

**MST cut property.** For any cut of a connected weighted graph, a lightest edge crossing the cut belongs to at least one MST.

Proof sketch: take an MST not using such an edge $e$. Adding $e$ creates a cycle. That cycle contains another edge $f$ crossing the same cut. Since $e$ is no heavier than $f$, replacing $f$ with $e$ gives another spanning tree with no larger weight.

**MST cycle property.** If an edge is strictly heavier than every other edge on some cycle, then it belongs to no MST.

The cycle property justifies rejecting expensive cycle-closing edges in Kruskal's algorithm.

**Relaxation.** Shortest-path algorithms repeatedly apply the same local test: if the current best known distance to $u$ plus the edge weight $w(u,v)$ improves the current best known distance to $v$, replace it. In symbols,

$$
d(v)>d(u)+w(u,v)
$$

triggers the update

$$
d(v)\leftarrow d(u)+w(u,v).
$$

Dijkstra, Bellman-Ford, and many dynamic-programming shortest-path algorithms differ mainly in the order and number of relaxations. Dijkstra's priority queue order is valid only when future edges cannot reduce a settled distance, which is exactly where nonnegative weights enter the proof. Bellman-Ford is slower because it allows negative edges and therefore cannot trust a vertex after one minimum-priority extraction.

**MSTs versus shortest paths.** Both problems may produce a tree, but the objectives are different. A shortest-path tree from $s$ minimizes the route from $s$ to each vertex separately. A minimum spanning tree minimizes the sum of all chosen edges. In the visual graph, the MST and shortest-path tree from $A$ may share edges, but this is not guaranteed. The MST might choose an edge that is useless for the shortest route from $A$ to any particular destination because it cheaply connects two remote parts of the graph.

**Tie handling.** When several edges have the same weight, Kruskal and Prim may return different MSTs. This is not a contradiction. The total weight is the invariant; the edge set need not be unique. A graph has a unique MST if every cut has a unique lightest crossing edge, and in particular if all edge weights are distinct.

**Negative cycles.** A negative edge is not automatically a problem for shortest paths, but a reachable negative cycle is. Once a path can enter a cycle of negative total weight and later reach the target, looping around the cycle repeatedly makes the path weight arbitrarily small. In that case there is no well-defined shortest path. Bellman-Ford detects this by checking whether any edge can still be relaxed after $n-1$ full passes.

## Visual

```mermaid
graph LR
  A("(A")) ---|4| B("(B"))
  A ---|2| C("(C"))
  C ---|1| B
  B ---|5| D("(D"))
  C ---|8| D
  C ---|10| E("(E"))
  D ---|2| E
```

The shortest path from $A$ to $E$ is not necessarily the path with the fewest edges. Here $A-C-B-D-E$ has weight $2+1+5+2=10$, while $A-C-E$ has only two edges but weight $12$.

## Worked example 1: Dijkstra from a source

**Problem.** In the weighted graph shown above, find shortest distances from $A$ to every vertex.

**Method.**

Initialize

$$
d(A)=0,\quad d(B)=d(C)=d(D)=d(E)=\infty.
$$

1. Settle $A$. Relax its edges:

$$
d(B)=4,\quad d(C)=2.
$$

2. The smallest unsettled distance is $d(C)=2$. Settle $C$. Relax edges from $C$:

$$
d(B)=\min(4,2+1)=3,
$$

$$
d(D)=\min(\infty,2+8)=10,
$$

$$
d(E)=\min(\infty,2+10)=12.
$$

3. The smallest unsettled distance is $d(B)=3$. Settle $B$. Relax $BD$:

$$
d(D)=\min(10,3+5)=8.
$$

4. The smallest unsettled distance is $d(D)=8$. Settle $D$. Relax $DE$:

$$
d(E)=\min(12,8+2)=10.
$$

5. Settle $E$ with distance $10$.

**Checked answer.**

$$
d(A)=0,\quad d(C)=2,\quad d(B)=3,\quad d(D)=8,\quad d(E)=10.
$$

A shortest $A$-$E$ path is $A-C-B-D-E$.

Notice that the direct-looking edge $C-E$ is not used. Shortest-path algorithms do not minimize the number of hops; they minimize total weight. If each edge represented travel time, the path with four edges could still be faster than the path with two edges.

## Worked example 2: Kruskal minimum spanning tree

**Problem.** Find an MST of the same graph.

**Method.** Sort edges by increasing weight:

$$
CB(1),\ AC(2),\ DE(2),\ AB(4),\ BD(5),\ CD(8),\ CE(10).
$$

Kruskal's algorithm adds the next lightest edge that does not create a cycle.

1. Add $CB(1)$.
2. Add $AC(2)$. The component is now $\{A,B,C\}$.
3. Add $DE(2)$. The component $\{D,E\}$ is separate.
4. Consider $AB(4)$. It would create the cycle $A-C-B-A$, so reject it.
5. Add $BD(5)$. This connects $\{A,B,C\}$ to $\{D,E\}$.
6. Now all five vertices are connected with four edges, so stop.

The MST edge set is

$$
\{CB,AC,DE,BD\}.
$$

Its total weight is

$$
1+2+2+5=10.
$$

**Check.** A spanning tree on $5$ vertices has exactly $4$ edges, and the selected four edges connect all vertices. Each rejection was justified by a cycle, so Kruskal's rule is satisfied.

## Code

```python
import heapq

def dijkstra(adj, source):
    dist = {v: float("inf") for v in adj}
    parent = {v: None for v in adj}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist, parent

adj = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
    "D": [("B", 5), ("C", 8), ("E", 2)],
    "E": [("C", 10), ("D", 2)],
}

dist, parent = dijkstra(adj, "A")
print(dist)
```

To reconstruct a path, follow the `parent` dictionary backward from the target to the source. The distance values alone answer "how far"; the parent pointers answer "which route." Many bugs in shortest-path code come from updating the distance but forgetting to update the predecessor at the same time.

When comparing weighted-graph algorithms, keep the invariant visible. Dijkstra certifies settled shortest distances, Kruskal maintains an acyclic partial forest, Prim maintains a connected growing tree, and Bellman-Ford performs enough relaxations to account for paths with many edges. Remembering the invariant is more reliable than memorizing the implementation details alone.

## Common pitfalls

- Using Dijkstra's algorithm when a negative edge is present. Nonnegative weights are part of the correctness proof.
- Confusing shortest-path trees with minimum spanning trees. A shortest-path tree is source-based; an MST is global and source-free.
- Assuming the lightest edge incident to each vertex forms an MST. Local choices can create cycles or disconnected pieces.
- Forgetting to stop Kruskal after $n-1$ accepted edges.
- Treating equal-weight MST choices as errors. Multiple distinct MSTs may have the same total weight.
- Ignoring negative cycles in shortest-path problems. If one is reachable and can reach the target, there is no finite minimum.

## Connections

- [Walks, paths, and connectedness](/math/graph-theory/walks-paths-and-connectedness)
- [Trees and spanning trees](/math/graph-theory/trees-and-spanning-trees)
- [Menger theorem and network flows](/math/graph-theory/menger-theorem-and-network-flows)
- [Random graphs basics](/math/graph-theory/random-graphs-basics)
