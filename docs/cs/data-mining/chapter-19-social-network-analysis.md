---
title: Social Network Analysis
sidebar_position: 21
---

# Social Network Analysis

Social network analysis studies graphs whose nodes are people, accounts, organizations, or social entities and whose edges represent relationships or interactions. Aggarwal's social network chapter covers preliminaries and properties, community detection, collective classification, link prediction, and social influence analysis. The topic is graph mining with stronger behavioral assumptions: social ties often imply homophily, influence, triadic closure, and community structure.

This page covers network properties, centrality, community detection, collective classification, link prediction, and influence. It connects directly to graph mining, web mining, classification, clustering, and privacy.

## Definitions

A **social network** is a graph $G=(V,E)$ where nodes represent social actors and edges represent ties such as friendship, following, messaging, co-authorship, or transactions.

**Homophily** is the tendency of similar nodes to connect.

**Influence** is the process by which behavior or attributes of one node affect others over edges.

**Community detection** partitions nodes into groups with dense internal edges and sparser external edges.

**Modularity** compares observed within-community edges to what would be expected under a random graph with similar degrees.

**Collective classification** predicts node labels using both node features and labels or features of neighboring nodes.

**Link prediction** estimates which missing or future edges are likely to appear.

**Social influence analysis** models how information, behavior, or adoption spreads through a network.

## Key results

**Network data violate independence assumptions.** A user's label, behavior, or risk may be correlated with neighboring users. This helps relational models but complicates evaluation.

**Community detection is clustering on graph structure.** The similarity signal is edge connectivity rather than Euclidean distance. Methods include modularity optimization, spectral partitioning, hierarchical divisive methods such as edge-betweenness removal, and label propagation.

**Collective classification can bootstrap labels.** If a few nodes are labeled, iterative methods can propagate label information across edges. This works best when homophily is strong and labels are smooth over the graph.

**Link prediction uses proximity and shared context.** Common-neighbor count, Jaccard coefficient, Adamic-Adar score, preferential attachment, and supervised edge features are standard signals.

**Influence and homophily are hard to separate.** If connected people behave similarly, they may influence each other, or they may have connected because they were already similar. Causal claims need temporal evidence or experimental design.

**Evaluation needs graph-aware splits.** Randomly hiding edges or labels can leak information through nearby structure. Time-based splits are often better for link prediction and influence tasks.

**Social networks are not just generic graphs.** Edge semantics matter: friendship, following, reply, co-location, and payment edges imply different levels of trust, direction, and causality. A directed follower edge should not be treated the same as a mutual friendship edge unless the task justifies it. Weighted interaction frequency, recency, and multiplex edge types can change centrality, communities, and influence estimates.

**Influence modeling needs temporal order.** If user A adopts a behavior before user B and there is an edge from A to B, influence is plausible but not proven. If both adopted before the edge existed, homophily or external events are more plausible. Diffusion models should therefore use timestamps, exposure definitions, and baselines for global popularity shocks.

**Communities can overlap.** A person may belong to family, workplace, hobby, and geographic communities simultaneously. Hard partitions are easy to visualize, but overlapping community methods may better represent social reality. The right choice depends on whether the application needs exclusive segments, role discovery, recommendation groups, or influence neighborhoods.

**Centrality is task-specific.** Degree centrality finds locally connected nodes, betweenness centrality finds bridge nodes, eigenvector-like measures find nodes connected to other important nodes, and closeness centrality favors short paths to many nodes. A high-degree celebrity may be poor for targeted diffusion if their neighbors ignore recommendations, while a bridge node may be valuable for connecting communities.

**Network data can amplify bias.** Missing edges, platform-specific behavior, bots, and unequal access to technology all shape the observed graph. Mining results should be interpreted as patterns in the measured network, not automatically as complete patterns in the real social system.

**Link prediction needs negative examples carefully.** Most pairs of nodes are not connected, but treating every missing edge as a true negative can create an overwhelming and sometimes false negative class. Some missing edges are unobserved rather than nonexistent. Sampling negatives, using time-based nonedges, and reporting ranking metrics are common ways to make the problem meaningful.

**Privacy risk is structural.** Even if names are removed, a person's pattern of connections may be unique. Social network mining can reveal communities, bridges, or sensitive associations. This is why social network pages connect naturally to privacy-preserving mining rather than only to graph algorithms.

**Temporal granularity matters.** Daily, weekly, and monthly interaction graphs can show different communities and influence paths. Aggregating too broadly can create edges between people who were never active at the same time.

**Edge absence is ambiguous.** Two users may not be connected because they dislike each other, never met, use different platforms, or because the relationship was not observed. Social network algorithms should avoid overinterpreting missing edges as negative relationships.

**Multiplex networks need layer choices.** The same people may be connected by friendship, messages, follows, and transactions. Mining one collapsed graph can hide differences among layers, while mining each layer separately can miss cross-layer reinforcement.

## Visual

```mermaid
graph TD
  A("(A")) --- B("(B"))
  A --- C("(C"))
  B --- C
  C --- D("(D"))
  D --- E("(E"))
  D --- F("(F"))
  E --- F
  B -. possible link .- D
```

| Task | Input | Output | Common signal |
|---|---|---|---|
| Community detection | Social graph | Node groups | Dense internal edges |
| Collective classification | Partly labeled graph | Node labels | Neighbor labels/features |
| Link prediction | Current graph | Future/missing edges | Common neighbors, paths |
| Influence analysis | Network plus adoption times | Spread model | Temporal cascades |
| Centrality | Network | Important nodes | Degree, paths, eigenvectors |

## Worked example 1: Common-neighbor link prediction

**Problem.** In a social graph, edges are:

$$
(A,B),\ (A,C),\ (B,C),\ (C,D),\ (D,E),\ (D,F),\ (E,F).
$$

Compare possible links B-D and A-D using common-neighbor count.

**Method.**

1. Neighbors of B are A and C.
2. Neighbors of D are C, E, and F.
3. Common neighbors of B and D:

$$
\{A,C\}\cap\{C,E,F\}=\{C\}.
$$

   Score is 1.

4. Neighbors of A are B and C.
5. Common neighbors of A and D:

$$
\{B,C\}\cap\{C,E,F\}=\{C\}.
$$

   Score is 1.

6. The two candidate links tie under common-neighbor count.

7. A different measure, such as preferential attachment, would compare degrees:

$$
deg(B)deg(D)=2\cdot3=6,\quad deg(A)deg(D)=2\cdot3=6.
$$

   They still tie.

**Checked answer.** B-D and A-D have equal score under these simple local measures. More features or temporal evidence would be needed to rank them differently.

## Worked example 2: One round of label propagation

**Problem.** Nodes A and C are labeled positive; node E is labeled negative. Unlabeled node D connects to C, E, and F. Node F connects to D and E. Initialize unlabeled labels as unknown. Predict D after one neighbor vote using known labels only.

**Method.**

1. D's neighbors are C, E, and F.
2. Known labels among those neighbors:
   - C is positive.
   - E is negative.
   - F is unknown.
3. Count known votes:
   - positive: 1
   - negative: 1
4. The vote is tied.
5. A tie-breaking rule is required. Options include using class priors, edge weights, node features, or leaving D unlabeled for this round.

**Checked answer.** D cannot be assigned unambiguously by one unweighted known-neighbor vote. This illustrates why collective classification needs careful update and tie rules.

## Code

Pseudocode for common-neighbor link prediction:

```text
INPUT: graph G, candidate non-edge pairs P
OUTPUT: ranked candidate links

for each pair (u, v) in P:
    Nu = neighbors of u
    Nv = neighbors of v
    score(u, v) = size of intersection Nu and Nv
rank pairs by descending score
return ranking
```

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([
    ("A", "B"), ("A", "C"), ("B", "C"),
    ("C", "D"), ("D", "E"), ("D", "F"), ("E", "F")
])

candidates = [("B", "D"), ("A", "D"), ("A", "E")]
for u, v in candidates:
    common = set(G.neighbors(u)) & set(G.neighbors(v))
    jaccard = len(common) / len(set(G.neighbors(u)) | set(G.neighbors(v)))
    print((u, v), "common", common, "jaccard", round(jaccard, 3))

communities = nx.community.greedy_modularity_communities(G)
print([sorted(c) for c in communities])
print(nx.degree_centrality(G))
```

## Common pitfalls

- Interpreting correlation among connected nodes as causal influence.
- Evaluating link prediction with random splits when the real task is future-link prediction.
- Assuming high-degree nodes are always the most influential.
- Using community detection output as ground truth social groups without validation.
- Ignoring edge direction and weight in follower or interaction networks.
- Applying homophily-based label propagation in heterophilous networks.
- Publishing network-derived results without considering privacy leakage through edges.

## Connections

- [Mining Graph Data](/cs/data-mining/chapter-17-mining-graph-data)
- [Mining Web Data and Recommenders](/cs/data-mining/chapter-18-mining-web-data)
- [Cluster Analysis](/cs/data-mining/chapter-06-cluster-analysis)
- [Data Classification](/cs/data-mining/chapter-10-data-classification)
- [Privacy-Preserving Data Mining](/cs/data-mining/chapter-20-privacy-preserving-data-mining)
