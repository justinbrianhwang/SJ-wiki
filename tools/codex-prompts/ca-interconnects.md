You are adding ONE new chapter to the existing **Computer Architecture** section.

## Inputs

- **OUTPUT FILE**: `f:/coding/SJ Wiki/docs/cs/computer-architecture/interconnection-networks.md`
- **SOURCE TEXTBOOK**: `f:/coding/SJ Wiki/tmp/Computer Architecture/Principles and Practices of Interconnection Networks - William James, Brain Towles.pdf` (Dally-Towles, *Principles and Practices of Interconnection Networks*)
- **STYLE**: Topical chapter name. IEEE inline citations `[N]`.

## Page metadata

```yaml
---
title: Interconnection Networks
sidebar_position: 16
---
```

Place after `warehouse-scale-computers.md`. Existing CA pages cover ISA, pipelining, branch prediction, caches, coherence, MESI/consistency, multicore-NUMA, vector/SIMD/GPU, virtual memory, storage, accelerators, warehouse-scale. This new page fills the on-chip / off-chip interconnect topic.

## Content scope (~2500-3500 words)

### Definitions
- Interconnection network: nodes, channels, switches, bandwidth, latency, throughput
- On-chip (NoC) vs off-chip (system area, datacenter fabric); InfiniBand, RoCE, NVLink, PCIe, CXL context
- Topology, routing, flow control as three orthogonal axes

### Topologies
- Direct: mesh (2D / 3D / torus / k-ary n-cube), tree, fat-tree, hypercube
- Indirect: butterfly, Clos, Benes
- Bisection bandwidth, diameter, degree, scalability tradeoffs
- Folded torus, dragonfly, hyperX

### Routing
- Deterministic (dimension-order) vs adaptive (Duato, fully adaptive)
- Minimal vs non-minimal; oblivious (Valiant)
- Deadlock avoidance: ordering, virtual channels
- Livelock and starvation avoidance
- Source routing vs distributed routing tables

### Flow control
- Bufferless (hot-potato), store-and-forward, virtual cut-through, wormhole
- Virtual channels for deadlock and QoS
- Credit-based vs ack/nack flow control
- Backpressure, head-of-line blocking, virtual output queues

### Router microarchitecture
- Pipeline stages: route compute, virtual-channel allocation, switch allocation, switch traversal, link traversal
- Speculation, lookahead routing, bypass
- Allocators: separable, wavefront, iSLIP
- Buffer organization

### Performance modeling
- Mean network latency: $T = T_{\text{header}} + T_{\text{serial}} + T_{\text{router}} \cdot H$ where $H$ is hop count
- Saturation throughput, knee of latency-throughput curve
- Synthetic traffic patterns: uniform random, bit-reverse, complement, hot-spot
- Booksim, garnet simulators (cross-link with SST/gem5)

### On-chip networks
- Mesh NoCs in multicore (Tilera/MIT RAW, Intel Xeon Phi, Esperanto), routerless on-chip interconnects
- Power constraints, link voltage scaling
- TSV-based 3D NoCs

### Off-chip / datacenter
- InfiniBand, RDMA, GPU-direct
- NVLink / NVSwitch for GPU clusters
- CXL coherent links
- Dragonfly+ topology in supercomputers (Aries, Slingshot)
- Optical interconnects (silicon photonics)

### Connection to AI clusters
- Tensor parallelism, pipeline parallelism, data-parallel reductions and the demands they place on bisection bandwidth
- Collective communications: ring AllReduce, tree AllReduce
- Topology-aware scheduling

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter
2. `# Interconnection Networks` H1
3. 1-2 opening paragraphs
4. (Optional) 1 Wikimedia image (verified): `Hypercube_(generalised).svg` (probably exists), `Fat_tree.svg` (uncertain — skip if not sure)
5. `## Definitions`
6. `## Key results` — topology metrics, routing/flow-control theorems, deadlock conditions
7. `## Visual` — **MANDATORY Mermaid** comparing topologies (mesh / torus / fat-tree / dragonfly) and showing a router microarchitecture pipeline
8. `## Worked example 1` — compute bisection bandwidth and diameter for $4 \times 4$ mesh, 16-node hypercube, 16-node fat-tree
9. `## Worked example 2` — wormhole latency: 4 flits, 6 hops, 1-cycle router, 1-cycle link → end-to-end latency
10. `## Code` — Python: simple routing-table mesh router; bisection-bandwidth checker
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — links to existing CA pages: [Cache Coherence](/cs/computer-architecture/coherence-consistency-mesi), [Multicore Synchronization](/cs/computer-architecture/multicore-synchronization-numa), [Warehouse-Scale Computers](/cs/computer-architecture/warehouse-scale-computers); also [Computer Networks](/cs/computer-networks/intro), [Distributed Systems](/cs/distributed-systems/intro)
13. `## References` — IEEE-style (Dally-Towles textbook with chapter refs; Valiant 1981 routing; Kermani-Kleinrock 1979 virtual cut-through; Dally 1992 virtual channels; Duato 1993 adaptive routing; Kim et al. 2008 Flattened Butterfly; Kim et al. 2008 dragonfly; Hoefler et al. on InfiniBand; etc.)

## Constraints

- Stay inside `docs/cs/computer-architecture/`.
- Only create `interconnection-networks.md`.
- No paper titles in filenames.
- Mermaid special chars in `"..."`; internal `"` → `#quot;`.
- English. Match depth addendum.

## Output summary

```
File: interconnection-networks.md
Word count: <N>
Figures: Wikimedia=W, Mermaid=M
References: <r>
```

Begin now.
