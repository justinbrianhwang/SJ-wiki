---
title: Shortest Paths
sidebar_position: 13
---

# Shortest Paths

Shortest-path algorithms find minimum-cost routes through weighted graphs. They are related to traversal, but weights change the problem. BFS is enough when every edge has equal cost; once edges have different nonnegative weights, Dijkstra's algorithm is the standard single-source method. For all-pairs shortest paths, Floyd-Warshall uses dynamic programming over an adjacency matrix.

The source textbook's graph chapter treats shortest paths after spanning trees. That contrast is important. A minimum spanning tree minimizes the total weight of a connecting tree, while shortest paths minimize route cost between specified vertices. The MST of a road network does not necessarily contain the shortest route between two cities.

## Definitions

Let $G = (V, E)$ be a weighted graph with edge weight function $w(u,v)$. The **length** of a path is the sum of its edge weights. A **shortest path** from source `s` to vertex `v` is a path with minimum total weight among all paths from `s` to `v`.

The **single-source shortest-path** problem computes distances:

$$
d[v] = \delta(s, v)
$$

for every vertex `v`, where $\delta(s,v)$ is the true shortest-path distance from `s` to `v`.

The **all-pairs shortest-path** problem computes $\delta(i,j)$ for every ordered pair of vertices.

Core operation:

- **Relaxation**: given an edge `u -> v`, if the known distance to `v` can be improved by going through `u`, update it:

$$
\text{if } d[u] + w(u,v) < d[v], \text{ then } d[v] = d[u] + w(u,v)
$$

Dijkstra's algorithm assumes all edge weights are nonnegative. Floyd-Warshall can handle negative edges, but not negative cycles. A negative cycle makes shortest paths undefined for reachable pairs because the path cost can be reduced without bound.

## Key results

Dijkstra's algorithm maintains a set of finalized vertices whose distances are known to be optimal. At each step it selects the unsettled vertex with the smallest tentative distance. With nonnegative weights, no later path through another unsettled vertex can improve it, because every extra edge adds a nonnegative amount.

Using an adjacency matrix and scanning for the next minimum tentative distance gives $O(V^2)$ time. Using adjacency lists and a binary heap priority queue gives $O((V + E)\log V)$ in a typical implementation.

Floyd-Warshall uses the recurrence:

$$
D^{(k)}[i][j] = \min\left(D^{(k-1)}[i][j],\ D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\right)
$$

Here $D^{(k)}[i][j]$ is the best distance from `i` to `j` using only intermediate vertices from the set `{0, 1, ..., k}`. The final matrix after all `k` values gives all-pairs shortest paths. The time complexity is $O(V^3)$ and the matrix space is $O(V^2)$.

| Algorithm | Problem | Weight restrictions | Time with common representation | Main data structure |
|---|---|---|---:|---|
| BFS | single-source unweighted | all edges equal | $O(V + E)$ | queue |
| Dijkstra | single-source weighted | nonnegative weights | $O(V^2)$ matrix or $O(E \log V)$ heap | priority queue or arrays |
| Floyd-Warshall | all-pairs weighted | no negative cycles | $O(V^3)$ | distance matrix |

Shortest-path implementations usually store a predecessor or parent array in addition to distances. Distances answer "how much does the best path cost?" Parents answer "what is the path?" After Dijkstra finishes, following `parent[target]`, then `parent[parent[target]]`, and so on reconstructs the path backward from the target to the source. If the parent remains `-1` for a non-source vertex, the vertex was unreachable.

The choice between Dijkstra and Floyd-Warshall is mostly about query pattern and graph size. If there is one source or a few sources in a sparse graph, repeated Dijkstra with adjacency lists is usually appropriate. If all vertex pairs are needed and the graph is small enough for a matrix, Floyd-Warshall is compact and handles dense graphs well. Its triple loop is also a classic example of dynamic programming over allowed intermediate vertices.

Negative weights require special care. A single negative edge can invalidate Dijkstra's finalized-distance argument. Floyd-Warshall can incorporate negative edges, but a negative diagonal entry after the algorithm indicates a negative cycle reachable from that vertex.

## Visual

```mermaid
flowchart TB
  subgraph Graph["Weighted directed graph"]
    direction LR
    A(("A")) -- "2" --> B(("B"))
    A -- "5" --> C(("C"))
    B -- "1" --> C
    B -- "2" --> D(("D"))
    C -- "3" --> D
    D -- "1" --> E(("E"))
    C -- "5" --> E
  end

  Init["#quot;Initialize d[A"]=0; all other d[v]=infinity; parent[v]=null"] --> PQ["Priority queue keyed by tentative distance"]
  Graph --> PQ
  PQ --> Extract["#quot;Extract unsettled vertex u with smallest d[u"]"]
  Extract --> Finalize["#quot;Finalize u; d[u"] is now shortest because weights are nonnegative"]
  Finalize --> Edges["For each outgoing edge u -> v with weight w"]
  Edges --> Relax{"d[u] + w < d[v]?"}
  Relax -- "yes" --> Update["#quot;Set d[v"]=d[u]+w; parent[v]=u; decrease-key or push duplicate"]
  Relax -- "no" --> Keep["#quot;Keep current d[v"] and parent[v]"]
  Update --> PQ
  Keep --> More{"Unsettled vertices remain?"}
  PQ --> More
  More -- "yes" --> Extract
  More -- "no" --> Paths(("Distances and predecessor tree from source A"))
```

This Dijkstra diagram combines the weighted graph, priority queue, finalization invariant, and relaxation operation. The extract-min step is what makes a vertex settled, while each outgoing edge may update a tentative distance and predecessor. The update label includes the two common heap strategies: true decrease-key or inserting a duplicate entry and ignoring stale removals later.

## Worked example 1: Dijkstra from A

Problem: Run Dijkstra's algorithm from `A` on the graph in the visual.

Method: keep tentative distances. Use infinity for unknown distances. Choose the unsettled vertex with smallest tentative distance each round.

Initial:

```text
d[A]=0, d[B]=inf, d[C]=inf, d[D]=inf, d[E]=inf
settled = {}
```

1. Choose `A` with distance `0`. Relax outgoing edges:
   - `A -> B` weight `2`: `0 + 2 < inf`, so `d[B]=2`, parent `A`.
   - `A -> C` weight `5`: `0 + 5 < inf`, so `d[C]=5`, parent `A`.
   Settled: `{A}`.
2. Choose unsettled minimum `B` with distance `2`. Relax:
   - `B -> C` weight `1`: `2 + 1 = 3 < 5`, so `d[C]=3`, parent `B`.
   - `B -> D` weight `2`: `2 + 2 = 4 < inf`, so `d[D]=4`, parent `B`.
   Settled: `{A,B}`.
3. Choose `C` with distance `3`. Relax:
   - `C -> D` weight `3`: `3 + 3 = 6`, not better than `4`.
   - `C -> E` weight `5`: `3 + 5 = 8 < inf`, so `d[E]=8`, parent `C`.
   Settled: `{A,B,C}`.
4. Choose `D` with distance `4`. Relax:
   - `D -> E` weight `1`: `4 + 1 = 5 < 8`, so `d[E]=5`, parent `D`.
   Settled: `{A,B,C,D}`.
5. Choose `E` with distance `5`. No outgoing improvements. Done.

Checked answer: distances are `A:0`, `B:2`, `C:3`, `D:4`, `E:5`. The shortest path to `E` is `A -> B -> D -> E`, with cost `2 + 2 + 1 = 5`.

## Worked example 2: one Floyd-Warshall update

Problem: Suppose vertices are `0, 1, 2`, and the current distance matrix before allowing vertex `1` as an intermediate is:

```text
      0   1   2
0     0   4   10
1   inf   0    3
2   inf inf    0
```

Update distances using vertex `1` as a possible intermediate.

Method: for every pair `(i,j)`, test whether `D[i][1] + D[1][j]` improves `D[i][j]`.

1. Pair `(0,2)`:

$$
\begin{aligned}
D[0][1] + D[1][2] &= 4 + 3 \\
&= 7
\end{aligned}
$$

Current `D[0][2]` is `10`, so update it to `7`.

2. Pair `(0,0)`: `D[0][1] + D[1][0] = 4 + inf = inf`, no improvement over `0`.
3. Pair `(0,1)`: `D[0][1] + D[1][1] = 4 + 0 = 4`, equal to current `4`.
4. Pairs starting from `1`: going through `1` adds `D[1][1] = 0`, so no improvement.
5. Pairs starting from `2`: `D[2][1] = inf`, so no path through `1`.

Updated matrix:

```text
      0   1   2
0     0   4    7
1   inf   0    3
2   inf inf    0
```

Checked answer: the new shortest known path from `0` to `2` is `0 -> 1 -> 2` with cost `7`, replacing the direct edge cost `10`.

## Code

This C program implements Dijkstra's algorithm with an adjacency matrix and simple $O(V^2)$ minimum selection.

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define V 5
#define INF 1000000000

static int min_unvisited(int dist[V], int used[V]) {
    int best = -1;
    for (int i = 0; i < V; ++i) {
        if (!used[i] && (best == -1 || dist[i] < dist[best])) {
            best = i;
        }
    }
    return best;
}

static void dijkstra(int graph[V][V], int source) {
    int dist[V];
    int parent[V];
    int used[V] = {0};

    for (int i = 0; i < V; ++i) {
        dist[i] = INF;
        parent[i] = -1;
    }
    dist[source] = 0;

    for (int step = 0; step < V; ++step) {
        int u = min_unvisited(dist, used);
        if (u == -1 || dist[u] == INF) break;
        used[u] = 1;

        for (int v = 0; v < V; ++v) {
            if (graph[u][v] != INF && !used[v]) {
                int candidate = dist[u] + graph[u][v];
                if (candidate < dist[v]) {
                    dist[v] = candidate;
                    parent[v] = u;
                }
            }
        }
    }

    for (int i = 0; i < V; ++i) {
        printf("vertex %d: dist=%d parent=%d\n", i, dist[i], parent[i]);
    }
}

int main(void) {
    int g[V][V] = {
        {INF, 2,   5,   INF, INF},
        {INF, INF, 1,   2,   INF},
        {INF, INF, INF, 3,   5},
        {INF, INF, INF, INF, 1},
        {INF, INF, INF, INF, INF}
    };
    dijkstra(g, 0);
    return EXIT_SUCCESS;
}
```

## Common pitfalls

- Running Dijkstra on graphs with negative edge weights. The finalized-distance argument no longer works.
- Confusing unreachable distance with a large real distance. Choose `INF` carefully to avoid overflow in `dist[u] + weight`.
- Forgetting to initialize `dist[source] = 0`.
- Treating an MST as a shortest-path tree. The optimization goals differ.
- Using Floyd-Warshall on a graph with a negative cycle and interpreting the output as finite shortest paths.
- In an adjacency matrix, using `0` for "no edge" when zero-weight edges are possible.

## Connections

- [graph representation](/cs/data-structures/graph-representation)
- [graph traversals](/cs/data-structures/graph-traversals)
- [heaps and priority queues](/cs/data-structures/heaps-priority-queues)
- [minimum spanning trees](/cs/data-structures/minimum-spanning-trees)
- [queues](/cs/data-structures/queues)
