---
title: Mining Graph Data
sidebar_position: 19
---

# Mining Graph Data

Graph mining studies data whose structure is expressed through nodes and edges. Aggarwal's graph chapter covers graph matching and distance computation, transformation-based graph distances, frequent substructure mining, graph clustering, and graph classification. Graphs appear in chemistry, social networks, web links, communication networks, biological interactions, fraud rings, and knowledge bases.

This page covers core graph mining ideas for both single large graphs and collections of many graphs. The main challenge is that topology matters: two objects may have identical attributes but different neighborhoods, and two graphs may be similar even when their node labels do not align exactly.

## Definitions

A **graph** is $G=(V,E)$, where $V$ is a set of vertices and $E$ is a set of edges. Graphs may be directed or undirected, weighted or unweighted, labeled or unlabeled.

An **adjacency matrix** $A$ has $A_{ij}=1$ when edge $(i,j)$ exists, or a weight for weighted graphs.

The **degree** of a node is the number of incident edges. In directed graphs, in-degree and out-degree are separated.

**Graph matching** finds a correspondence between nodes or edges of two graphs.

**Graph edit distance** is the minimum cost of edit operations, such as inserting, deleting, or relabeling nodes and edges, to transform one graph into another.

A **frequent subgraph** is a substructure appearing in many graphs or many places within a graph.

**Graph clustering** can mean clustering nodes in one graph, clustering edges, or clustering a collection of graphs.

**Graph classification** predicts a label for a node, edge, or entire graph using attributes and topology.

## Key results

**Exact graph matching is hard.** Subgraph isomorphism is computationally difficult in general. Practical graph mining uses pruning, canonical labels, approximate matching, kernels, embeddings, or domain constraints.

**Graph edit distance generalizes edit distance.** It supports approximate similarity between graphs, but the search space is much larger than string edit distance because node correspondences must be considered.

**Transformation-based features make graphs usable by standard algorithms.** A graph can be mapped to features such as degree counts, label counts, shortest-path histograms, graphlet counts, spectral values, or frequent-subgraph indicators.

**Frequent subgraph mining uses anti-monotonicity.** If a subgraph is infrequent, any supergraph containing it is also infrequent, because a larger structure cannot appear more often than its substructure.

**Node classification uses homophily and relational dependence.** In many graphs, neighboring nodes tend to have related labels. Collective classification and label propagation exploit this, but can fail when edges connect dissimilar nodes.

**Graph clustering often optimizes connectivity.** Community detection aims for dense internal connections and sparse external connections, but the right definition depends on whether edges represent friendship, citation, traffic, or transactions.

**There are two different graph-mining regimes.** In a single large graph, the objects may be nodes or edges, and algorithms exploit shared topology. In a graph database, each object is an entire graph, such as a molecule or program structure, and algorithms compare or classify graphs. Confusing these regimes leads to wrong feature design. Node degree is a feature for node classification in one graph; a histogram of degrees may be a feature for whole-graph classification.

**Graph labels and attributes can dominate topology.** In chemical graphs, atom and bond labels are essential. In social graphs, profile features may be as important as edges. In web graphs, anchor text and page content affect link meaning. A graph miner should specify whether matching is label-preserving, whether attributes are used in similarity, and whether edge weights or directions alter the result.

**Graph sampling can distort structure.** Sampling nodes uniformly may remove many edges and break communities. Sampling edges uniformly may overrepresent high-degree nodes. Snowball sampling preserves local neighborhoods but biases toward well-connected regions. When graphs are too large to mine exactly, the sampling design should be matched to the target property, such as degree distribution, triangles, shortest paths, or communities.

**Evaluation must prevent topology leakage.** In node classification, random splits can leave test nodes surrounded by training neighbors whose labels reveal the answer. In link prediction, random missing-edge evaluation may be easier than predicting future links. Graph mining experiments should define what information would really be available at prediction time.

**Scalability often requires local computation.** Many graph algorithms become expensive when they need all-pairs shortest paths, full eigendecompositions, or enumeration of many subgraphs. Large graph mining therefore uses local neighborhoods, sampled walks, sparse matrix operations, approximate embeddings, or distributed message passing. The approximation should be judged against the graph property the task needs.

**Dynamic graphs add another layer.** Edges and node attributes can change over time. A community, anomaly, or link prediction model that ignores timestamps may mix old and current structure. Temporal graph mining asks not only what is connected, but when and in what order connections appeared.

**Canonicalization prevents duplicate work.** Frequent subgraph mining needs a consistent representation of graph patterns so the same structure is not counted many times under different node orderings. This bookkeeping is central to efficiency.

**Disconnected components should be inspected.** Many graph algorithms behave differently on isolated components, sinks, or tiny fragments. Preprocessing often records component sizes and decides whether to mine each component separately or keep a global representation.

**Edge weights should be normalized by meaning.** Ten messages, ten dollars, and ten citations are not comparable weights. Before weighted graph mining, define whether weights represent intensity, cost, capacity, trust, distance, or frequency, because algorithms interpret larger weights differently.

## Visual

```mermaid
graph LR
  A("(A")) --- B("(B"))
  B --- C("(C"))
  C --- A
  C --- D("(D"))
  D --- E("(E"))
  E --- F("(F"))
  F --- D
```

| Graph task | Input | Output | Common approach |
|---|---|---|---|
| Node similarity | One graph | Similar node pairs | Neighborhoods, random walks |
| Graph similarity | Two graphs | Distance or kernel | Edit distance, features |
| Frequent subgraph mining | Graph database | Repeated substructures | Candidate growth and pruning |
| Node clustering | One graph | Communities | Cuts, modularity, spectral methods |
| Graph classification | Graphs with labels | Predictive model | Graph features or kernels |

## Worked example 1: Adjacency and degree features

**Problem.** For undirected graph with edges

$$
(A,B),\ (A,C),\ (B,C),\ (C,D),
$$

write the adjacency matrix in node order A, B, C, D and compute degrees.

**Method.**

1. The adjacency matrix is symmetric because the graph is undirected.

2. Fill entries:
   - A connected to B and C.
   - B connected to A and C.
   - C connected to A, B, and D.
   - D connected to C.

3. Matrix:

$$
A=
\begin{bmatrix}
0&1&1&0\\
1&0&1&0\\
1&1&0&1\\
0&0&1&0
\end{bmatrix}.
$$

4. Degrees are row sums:

$$
deg(A)=2,\quad deg(B)=2,\quad deg(C)=3,\quad deg(D)=1.
$$

**Checked answer.** C is the highest-degree node with degree 3; D is a leaf with degree 1. These simple features can feed node classification or graph summaries.

## Worked example 2: Frequent subgraph pruning

**Problem.** A graph database has 5 graphs. Subgraph $g$ appears in 2 graphs. Minimum support is 3. Can any supergraph of $g$ be frequent?

**Method.**

1. Support of $g$ is 2.
2. Minimum support is 3, so $g$ is infrequent.
3. Any supergraph $h$ containing $g$ can only appear in graphs where $g$ appears.
4. Therefore:

$$
\mathrm{support}(h)\le \mathrm{support}(g)=2<3.
$$

5. Thus $h$ is also infrequent.

**Checked answer.** No supergraph of $g$ can be frequent. This is the graph analogue of Apriori pruning, although graph candidate generation is much harder.

## Code

Pseudocode for graph feature extraction:

```text
INPUT: graph G = (V, E)
OUTPUT: numeric feature vector

compute number of nodes and edges
compute degree sequence
compute summary statistics of degrees
optionally compute triangles, components, shortest paths, or labels
concatenate summaries into feature vector
return vector
```

```python
import numpy as np
import networkx as nx
from sklearn.ensemble import RandomForestClassifier

G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")])

adj = nx.to_numpy_array(G, nodelist=["A", "B", "C", "D"], dtype=int)
degrees = dict(G.degree())
print(adj)
print(degrees)

def graph_features(graph):
    deg = np.array([d for _, d in graph.degree()], dtype=float)
    triangles = sum(nx.triangles(graph).values()) / 3
    return np.array([graph.number_of_nodes(), graph.number_of_edges(), deg.mean(), deg.max(), triangles])

graphs = [nx.path_graph(4), nx.cycle_graph(4), nx.complete_graph(4), nx.star_graph(3)]
y = np.array([0, 1, 1, 0])
X = np.vstack([graph_features(g) for g in graphs])
clf = RandomForestClassifier(n_estimators=50, random_state=0).fit(X, y)
print(X)
print(clf.predict(X))
```

## Common pitfalls

- Treating graph node IDs as meaningful numeric features.
- Comparing adjacency matrices without aligning node order.
- Assuming graph edit distance is cheap for large graphs.
- Mining frequent subgraphs without canonicalization or duplicate control.
- Ignoring edge direction, weight, or labels when they carry the main meaning.
- Applying homophily-based classification when links connect opposites or competitors.
- Evaluating graph models with random edge or node splits that leak neighborhood information.

## Connections

- [Similarity and Distances](/cs/data-mining/chapter-03-similarity-distances)
- [Advanced Association Patterns](/cs/data-mining/chapter-05-advanced-association-patterns)
- [Cluster Analysis](/cs/data-mining/chapter-06-cluster-analysis)
- [Data Classification](/cs/data-mining/chapter-10-data-classification)
- [Social Network Analysis](/cs/data-mining/chapter-19-social-network-analysis)
