You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes adding a **Graph Neural Networks** chapter set to the existing Deep Learning section.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/deep-learning/`
- **SUBJECT**: Graph Neural Networks (graduate-level, book-style)
- **STYLE**: Topical chapter names (NOT paper titles). Inline paper citations as `[N]` with a References section at the end (IEEE style).

## Produce exactly 2 pages

| sidebar_position | filename | title |
|---|---|---|
| 21 | `gnn-basics.md` | Graph Neural Networks: Basics |
| 22 | `gnn-applications.md` | Graph Neural Networks: Applications |

These are the ONLY two files to create. Do not create per-architecture files. This is a deliberately compact, book-style 2-chapter set covering core theory + applied uses.

## Word count

Each page: **2500-4000 words**. The two chapters are denser than usual because each covers what would otherwise be multiple chapters.

## Content scope

### Chapter 1 — `gnn-basics.md` (sidebar_position: 21)

Cover the full theoretical and architectural foundation in one consolidated chapter:

**Foundations**
- Graphs as data (nodes, edges, attributes, directed/undirected, weighted, heterogeneous)
- Node-, edge-, graph-level tasks; transductive vs inductive
- Classical embeddings as background: DeepWalk, node2vec, LINE (brief)
- Notation: adjacency $A$, degree $D$, Laplacian $L=D-A$, normalized $\tilde{A}=D^{-1/2}(A+I)D^{-1/2}$

**Spectral methods**
- Graph Laplacian, eigendecomposition, graph Fourier transform
- Spectral convolution; ChebNet polynomial approximation
- GCN as first-order Chebyshev: $H^{(\ell+1)}=\sigma(\tilde{A}H^{(\ell)}W^{(\ell)})$

**Message passing framework**
- MPNN abstraction (Gilmer et al.): message, aggregate, update
  $$m_v^{(\ell+1)}=\sum_{u\in\mathcal{N}(v)}M_\ell(h_v^{(\ell)},h_u^{(\ell)},e_{uv}),\quad h_v^{(\ell+1)}=U_\ell(h_v^{(\ell)},m_v^{(\ell+1)})$$
- GraphSAGE (sampling + mean/max/LSTM aggregators)
- GIN (sum aggregator + MLP, WL-equivalent)

**Attention and transformers on graphs**
- GAT attention coefficients (and GATv2 dynamic fix):
  $$\alpha_{ij}=\mathrm{softmax}_j\!\bigl(\mathrm{LeakyReLU}(a^\top[Wh_i\Vert Wh_j])\bigr)$$
- Graph Transformer / Graphormer with spatial / centrality / edge encodings (brief)

**Expressiveness & pathologies**
- 1-WL bound (Xu et al., Morris et al.) — message-passing GNNs are bounded by the 1-WL test
- Over-smoothing (Dirichlet energy decay with depth) and over-squashing (bottlenecks, Ricci curvature)
- Mitigations: residual, PairNorm, DropEdge, graph rewiring

**Geometric / equivariant (one section)**
- Permutation, translation, rotation equivariance
- E(3)-equivariant nets, SchNet, EGNN coordinate-update rule (brief)

### Chapter 2 — `gnn-applications.md` (sidebar_position: 22)

Cover applied uses, real-world systems, heterogeneous/dynamic graph variants, and frontiers:

**Heterogeneous graphs**
- Node/edge types; RGCN, HAN (meta-path attention), HGT
- Knowledge graph embeddings (TransE, RotatE, ComplEx) and GNN variants

**Dynamic / temporal graphs**
- Snapshot-based vs event-based modeling
- TGN, TGAT, ROLAND
- Time encoding strategies

**Major application domains** (each with a worked or representative architecture):

1. **Molecular property prediction / drug discovery** — MoleculeNet, equivariant nets, AlphaFold-style structure (brief)
2. **Recommendation** — PinSAGE, LightGCN, GraphRec
3. **Knowledge graph reasoning** — R-GCN for entity classification, attention-based reasoning
4. **Traffic forecasting** — DCRNN, Graph WaveNet (spatial-temporal modeling)
5. **Physics simulation** — Graph Network Simulator (GNS), MeshGraphNet
6. **Combinatorial optimization** — NeuroSAT, attention-based TSP solvers, graph matching

**Frontiers** — scalability beyond billion-node graphs (cluster-GCN, sampling tricks), graph foundation models (GraphGPS, OFA), oversmoothing-free architectures, GNNs + LLMs.

## Per-page format (mandatory)

Each page MUST include in this order:

1. Frontmatter: `title:`, `sidebar_position:`
2. `# Title` (H1)
3. Opening 1-2 paragraphs (motivation + scope)
4. Optional 1 contextual image with proper attribution
5. `## Definitions` — formal setup, notation
6. `## Key results` — main theorems / algorithms / model families
7. `## Visual` — **MANDATORY Mermaid diagram(s)** showing the chapter's architecture flow. Match the level of `attention-transformers.md` (sublayers, residuals, dimensions, subgraph grouping). Special-char labels in `"..."`; internal `"` → `#quot;`. For Chapter 1: a unified diagram covering spectral → message-passing → attention flow + one over-smoothing / depth diagram. For Chapter 2: a per-application sketch (subgraphs per domain) + dynamic-graph timing diagram.
8. `## Worked example 1: ...` (numerical / by-hand)
   - Ch.1: GCN forward pass on a 3-node graph with explicit $\tilde{A}H W$ computation
   - Ch.2: TransE/RotatE score on a fact, or LightGCN propagation step
9. `## Worked example 2: ...`
   - Ch.1: GAT attention coefficients on a small graph, or EGNN coordinate update
   - Ch.2: PinSAGE neighbor sampling pipeline, or temporal aggregation in TGN
10. `## Code` — minimal PyTorch / NumPy / PyG sketch
11. `## Common pitfalls` — bulleted, 10-15 items
12. `## Connections` — links to other DL pages + `[graph-theory](/math/graph-theory/)` + `[linear-algebra](/math/linear-algebra/)` + applicable
13. `## References` — IEEE-style numbered list (15-25 entries per page is appropriate for the breadth)

## Visual policy

- Mermaid mandatory.
- Optional: embed paper figures via `https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png`. Verified candidates:
  - GAT (`1710.10903`, `x1.png`)
  - GraphSAGE (`1706.02216`, `x1.png`)
  - EGNN (`2102.09844`, `x1.png`)
  - PinSAGE (`1806.01973`, `x1.png`)
- For graph theory context use Wikimedia (e.g. `Graph_definition.svg`, `7_bridges_of_Königsberg.png`).
- Always include attribution caption.
- Don't fabricate arxiv IDs or figure numbers — skip if unsure.

## Citation format

Inline as `[N]` matched to numbered References at end:

> First-order Chebyshev approximation [3] reduces the spectral filter to a sparse matrix-vector operation.

> ## References
> [1] T. N. Kipf and M. Welling, "Semi-Supervised Classification with Graph Convolutional Networks," ICLR, 2017. https://arxiv.org/abs/1609.02907
> ...

## Constraints

- Stay inside `docs/cs/deep-learning/`.
- Create EXACTLY 2 files: `gnn-basics.md`, `gnn-applications.md`.
- No paper titles in filenames.
- No `_category_.json` or config edits.
- Mermaid label special chars in `"..."`; internal `"` → `#quot;`.
- Don't fabricate beyond standard GNN literature.

## Output summary

End with:

```
Files created: 2
Word counts: gnn-basics.md=<X>, gnn-applications.md=<Y>
Figures: ar5iv=<a>, Wikimedia=<w>, Mermaid=<m>
References: ch.1=<N1>, ch.2=<N2>
```

Begin now.
