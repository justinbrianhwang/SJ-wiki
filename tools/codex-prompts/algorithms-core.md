You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes that flesh out the **Algorithms** section under `docs/cs/algorithms/` with a comprehensive textbook-scale chapter set.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/algorithms/`
- **SUBJECT**: Algorithms (undergraduate-to-graduate, full course scope)
- **STYLE**: Topical chapter names (NOT paper titles). Inline citations as `[N]` with a References section per page (IEEE style). Anchor on standard textbooks: CLRS (Cormen-Leiserson-Rivest-Stein, *Introduction to Algorithms*, 4th ed), Kleinberg-Tardos (*Algorithm Design*), Sedgewick-Wayne (*Algorithms*, 4th ed), Motwani-Raghavan (*Randomized Algorithms*), Vazirani (*Approximation Algorithms*), Mehlhorn-Sanders (*Algorithms and Data Structures*).

## Existing pages (do not modify)

- `intro.md` (will be edited separately after this run to remove "coming soon" markers)
- `big-o.md` (sidebar_position 2)

## Produce exactly 13 new pages

| sidebar_position | filename | title |
|---|---|---|
| 3 | `sorting-algorithms.md` | Sorting Algorithms |
| 4 | `searching-algorithms.md` | Searching Algorithms |
| 5 | `divide-and-conquer.md` | Divide and Conquer |
| 6 | `dynamic-programming.md` | Dynamic Programming |
| 7 | `greedy-algorithms.md` | Greedy Algorithms |
| 8 | `backtracking-and-branch-and-bound.md` | Backtracking and Branch & Bound |
| 9 | `graph-algorithms.md` | Graph Algorithms |
| 10 | `network-flow-and-matching.md` | Network Flow and Matching |
| 11 | `string-algorithms.md` | String Algorithms |
| 12 | `number-theoretic-and-algebraic-algorithms.md` | Number-Theoretic and Algebraic Algorithms |
| 13 | `computational-geometry.md` | Computational Geometry |
| 14 | `randomized-algorithms.md` | Randomized Algorithms |
| 15 | `approximation-algorithms.md` | Approximation Algorithms |

## Content scope per page

### 3 — `sorting-algorithms.md`
- Stability, in-place, adaptive, comparison vs non-comparison
- **Comparison-based**: bubble, insertion, selection, merge, quicksort (Lomuto vs Hoare partition, randomized pivot, three-way partition), heapsort, shellsort
- **Non-comparison**: counting, radix (LSD/MSD), bucket
- $\Omega(n\log n)$ lower bound via decision-tree argument
- Tim Sort (Python/Java default), Intro Sort (C++)
- External sorting (merge passes), parallel sorting (brief)
- Comparison table of worst/average/best time, space, stability, adaptive
- Worked examples: (1) merge-sort recurrence, (2) quicksort partition trace
- Python: merge_sort, quicksort

### 4 — `searching-algorithms.md`
- Linear, binary, ternary, interpolation, exponential search
- Search in rotated/sorted arrays, peak in mountain array
- k-th order statistic: Quickselect, median-of-medians ($O(n)$ worst case)
- Hash-based lookup (chaining, open addressing, load factor); cuckoo hashing
- Tree-based search (BST, AVL, RB-tree, B-tree, skip list)
- Worked examples: (1) binary search first occurrence, (2) Quickselect for k-th smallest
- Python: binary_search variants, quickselect

### 5 — `divide-and-conquer.md`
- Pattern: divide / conquer / combine
- Master Theorem (all three cases, examples), Akra-Bazzi extension brief
- Key algorithms: merge sort, quicksort (cross-link), binary search, closest pair of points ($O(n\log n)$), Karatsuba integer multiplication ($n^{\log_2 3}$), Strassen matrix multiplication ($n^{\log_2 7}$), Cooley-Tukey FFT ($n\log n$), maximum subarray (Kadane vs D&C)
- Recursion-tree intuition and substitution method
- Worked examples: (1) Master Theorem on $T(n)=3T(n/4)+n\log n$, (2) Karatsuba multiplication of two 4-digit numbers
- Python: karatsuba_multiply, closest_pair (sketch)

### 6 — `dynamic-programming.md`
- Two ingredients: optimal substructure + overlapping subproblems
- Memoization vs tabulation; space optimization (rolling arrays)
- 1D problems: Fibonacci, climbing stairs, house robber, maximum subarray (Kadane)
- LIS ($O(n^2)$ and $O(n\log n)$), LCS, edit distance
- Knapsack (0/1 and unbounded), subset sum, partition equal subset sum
- Matrix chain multiplication; optimal BST
- DP on trees (rerooting), DP on intervals, bitmask DP (TSP $O(n^2 2^n)$)
- Palindrome partitioning, word break, regex matching DP
- View: DP = shortest path on subproblem DAG
- Worked examples: (1) LCS of two strings via 2D table, (2) 0/1 knapsack with explicit table
- Python: edit_distance, knapsack_01, lis_nlogn

### 7 — `greedy-algorithms.md`
- Matroid theorem (Edmonds); exchange and stay-ahead arguments
- Activity selection / interval scheduling / interval partitioning
- Fractional knapsack
- Huffman coding (priority-queue construction)
- Kruskal MST (union-find), Prim MST (heap)
- Dijkstra greedy view (cross-link with graph chapter)
- Job scheduling to minimize lateness
- Set cover greedy approximation ($H_n=\ln n+O(1)$, cross-link with approximation chapter)
- When greedy fails: 0/1 knapsack, longest path, arbitrary-coin change
- Worked examples: (1) interval scheduling on 6 activities, (2) Huffman code construction
- Python: activity_selection, huffman_code, fractional_knapsack

### 8 — `backtracking-and-branch-and-bound.md`
- Search-space tree, pruning, constraint propagation
- Backtracking classics: N-queens, Sudoku, graph coloring, subset sum, Hamiltonian cycle, knight's tour
- Branch & bound: 0/1 knapsack via LP relaxation bound, TSP via reduced-cost bounds, integer LP
- Heuristics: variable / value ordering, forward checking, AC-3 for constraint satisfaction
- Iterative deepening and beam search for large state spaces
- Worked examples: (1) N-queens for $N=4$ trace, (2) 0/1 knapsack branch & bound on a small instance
- Python: n_queens_backtrack, sudoku_solve

### 9 — `graph-algorithms.md`
- Representations: adjacency list, adjacency matrix, edge list
- BFS, DFS, edge classification (tree / back / forward / cross), topological sort (Kahn + DFS)
- Connected components (undirected); strongly connected components (Tarjan, Kosaraju)
- Bridges and articulation points (low-link)
- MST: Kruskal (union-find), Prim (heap), Borůvka
- Shortest paths: Dijkstra (binary heap, Fibonacci heap), Bellman-Ford (negative cycles), Floyd-Warshall, Johnson's algorithm; $A^*$ search
- Eulerian and Hamiltonian tours (Hamiltonian is NP-complete)
- Worked examples: (1) Dijkstra step-by-step on 5-node graph, (2) Bellman-Ford detecting negative cycle
- Python: dijkstra_heap, bellman_ford, kruskal_mst, scc_tarjan

### 10 — `network-flow-and-matching.md`
- Max-flow / min-cut duality
- Ford-Fulkerson framework; augmenting-path correctness via residual graph
- Edmonds-Karp BFS variant ($O(VE^2)$); Dinic's blocking-flow algorithm ($O(V^2 E)$); Push-relabel
- Min-cost max-flow (Bellman-Ford on residual graph; SSP algorithm)
- Bipartite matching: König's theorem; Hopcroft-Karp ($O(E\sqrt V)$)
- Stable matching: Gale-Shapley algorithm, proofs of stability and proposer optimality
- Applications: assignment, image segmentation (graph cuts), project selection, baseball elimination
- Worked examples: (1) max-flow on a 4-node graph by Ford-Fulkerson, (2) Gale-Shapley on 3 men × 3 women preferences
- Python: edmonds_karp, hopcroft_karp (sketch), gale_shapley

### 11 — `string-algorithms.md`
- Naive matching $O(nm)$
- Knuth-Morris-Pratt failure function ($O(n+m)$)
- Rabin-Karp rolling hash (expected $O(n+m)$); multi-pattern collisions
- Boyer-Moore bad-character + good-suffix
- Aho-Corasick multi-pattern matching with automaton + failure links
- Z-algorithm, prefix function (Z and pi arrays)
- Suffix array (SA-IS algorithm sketch, $O(n\log n)$ naive)
- Suffix tree (Ukkonen's algorithm idea); generalized suffix tree for multiple strings
- Longest Common Substring via suffix array + LCP
- Edit-distance review (cross-link DP chapter), approximate matching
- Compression-aware searches: BWT / FM-index sketch
- Worked examples: (1) KMP failure function for `ABABCABAB`, (2) Rabin-Karp matching `ABAB` in `ABCABABAB`
- Python: kmp_search, rabin_karp, z_function

### 12 — `number-theoretic-and-algebraic-algorithms.md`
- Euclidean and extended Euclidean GCD; modular inverse
- Fast modular exponentiation ($O(\log n)$)
- Sieve of Eratosthenes; segmented and linear sieves
- Primality testing: Fermat, Miller-Rabin (witness count and error bound), AKS (mention)
- Integer factorization: trial division, Pollard's rho, Pollard's $p-1$, quadratic sieve (mention)
- Chinese Remainder Theorem (CRT) and applications
- Discrete logarithm (Baby-step giant-step, Pollard's rho for log) — cross-link with cryptography
- Fast Fourier Transform (Cooley-Tukey) for polynomial multiplication ($O(n\log n)$); NTT for modular FFT
- Matrix exponentiation ($O(k^3\log n)$) for linear recurrences
- Karatsuba and Toom-Cook integer multiplication; Schönhage-Strassen (mention)
- Worked examples: (1) extended Euclidean for $\gcd(252,198)$, (2) Miller-Rabin witness check for $n=561$ (Carmichael)
- Python: gcd_ext, mod_pow, sieve_eratosthenes, miller_rabin

### 13 — `computational-geometry.md`
- Primitives: orientation test (cross product), segment intersection
- Convex hull: Graham scan ($O(n\log n)$), Andrew monotone chain, Jarvis march, Chan's algorithm ($O(n\log h)$)
- Closest pair of points via D&C ($O(n\log n)$)
- Sweep-line: segment intersection (Bentley-Ottmann), rectangle union, area of union
- Voronoi diagram and Delaunay triangulation (Fortune's algorithm sketch)
- Point location in planar subdivisions; range trees and kd-trees
- Polygon triangulation (ear clipping); polygon area via shoelace formula
- Linear programming in low dimension (Megiddo / Seidel)
- Worked examples: (1) Graham scan trace on 6 points, (2) closest pair on a small instance via D&C
- Python: convex_hull_andrew, closest_pair, segment_intersect

### 14 — `randomized-algorithms.md`
- Las Vegas vs Monte Carlo; expected vs worst-case
- Randomized quicksort and quickselect (expected $O(n\log n)$, $O(n)$)
- Skip lists (expected $O(\log n)$)
- Hashing: universal hashing, perfect hashing (2-level), cuckoo hashing, count-min sketch, Bloom filter
- Randomized min-cut (Karger's algorithm; success probability boost by repetition)
- Random projections; Johnson-Lindenstrauss lemma
- Streaming algorithms: reservoir sampling, Misra-Gries heavy hitters, HyperLogLog distinct count
- Randomized matrix multiplication / Freivalds' algorithm
- Worked examples: (1) reservoir sampling correctness for $k=1$, (2) Bloom filter false positive computation
- Python: skip_list_basic, reservoir_sample, bloom_filter

### 15 — `approximation-algorithms.md`
- Approximation ratio; absolute vs relative
- Vertex cover: 2-approximation via maximal matching; LP relaxation rounding
- TSP: 2-approximation via MST doubling (metric); Christofides 1.5-approximation
- Set cover: greedy gives $\ln n$ approximation; LP rounding analysis
- Knapsack FPTAS via DP rounding ($1+\varepsilon$ in $O(n^2/\varepsilon)$)
- Max-3SAT: random assignment gives 7/8 approximation in expectation
- Steiner tree, k-center
- PCP theorem (statement only) and hardness-of-approximation context (cross-link theory)
- Worked examples: (1) MST-doubling TSP on metric 4-node, (2) greedy set cover analysis
- Python: vertex_cover_2approx, tsp_mst_doubling, set_cover_greedy

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter: `title:`, `sidebar_position:`
2. `# Title` (H1)
3. Opening 1-2 paragraphs (motivation + scope)
4. (Optional but encouraged) 1-2 Wikimedia context images
5. `## Definitions` — formal setup, terminology
6. `## Key results` — main algorithms with derivations / proofs sketched
7. `## Visual` — **MANDATORY Mermaid diagram(s)** showing flowchart / decision tree / recursion tree / DAG / network depending on chapter. Special-char labels in `"..."`; internal `"` → `#quot;`.
8. `## Worked example 1: ...`
9. `## Worked example 2: ...`
10. `## Code` — clean Python (no heavy deps)
11. `## Common pitfalls` — 10-15 bulleted items
12. `## Connections` — cross-links to other algorithms pages, `[Data Structures](/cs/data-structures/intro)`, `[Theory of Computation](/cs/theory/intro)`, `[Discrete Math](/math/discrete/intro)`, `[Cryptography](/cs/cryptography/intro)` (where relevant)
13. `## References` — IEEE-style numbered list (10-18 entries; cite CLRS chapters with `[CLRS, Ch. X]`-style annotations, plus foundational papers — Dijkstra 1959, Bellman 1958, Floyd 1962, Knuth-Morris-Pratt 1977, Rabin-Karp 1987, Strassen 1969, Karatsuba 1962, Cooley-Tukey 1965, Miller 1976, Rabin 1980, Karger 1993, Christofides 1976, etc.)

## Word count

Each page: **2000-3500 words**. Dense pages (graph, DP, network-flow, geometry) lean toward upper end.

## Math precision (KaTeX)

- Master Theorem: $T(n)=aT(n/b)+f(n)$; case 1/2/3 conditions
- Dijkstra relaxation; Bellman-Ford; max-flow / min-cut duality $\max f=\min \mathrm{cut}$
- KMP failure function; Z-array
- FFT: $X_k=\sum_n x_n e^{-2\pi i kn/N}$
- Miller-Rabin: $n-1=2^s d$, witness $a^d\bmod n$
- Approximation ratio: $\rho=\sup_I \mathrm{ALG}(I)/\mathrm{OPT}(I)$ for minimization

## Visual policy

**Mermaid is MANDATORY per page** (structural / control-flow / decision-tree / DAG / recursion-tree diagram). Match the level of detail of `docs/cs/deep-learning/attention-transformers.md`.

**Wikimedia algorithm-visualization figures (mandatory where the page topic matches a verified URL)** — use ONLY the URLs below. They were HEAD-verified; do not invent new filenames.

### Verified Wikimedia URLs (use freely)

Sorting page (use 2–3):
- `Quicksort.gif`
- `Sorting_quicksort_anim.gif`
- `Merge-sort-example-300px.gif`
- `Selection-Sort-Animation.gif`
- `Insertion-sort-example-300px.gif`
- `Sorting_heapsort_anim.gif`
- `Heap_sort_example.gif`

Searching page (use 1–2):
- `Binary_search_into_array_-_example.svg`
- `Binary_search_complexity.svg`

Divide and conquer page:
- `Strassen_algorithm.svg`

Dynamic programming page:
- `Hamming_distance_4_bit_binary.svg` (use as a state-distance example)

Greedy page:
- `Huffman_tree_2.svg`

Graph algorithms page (use 3–4):
- `Dijkstra_Animation.gif`
- `Animated_BFS.gif`
- `Breadth-first-tree.svg`
- `Depth-first-tree.svg`
- `Tarjan%27s_Algorithm_Animation.gif`
- `Kruskal_Algorithm_6.svg`
- `MST_kruskal_en.gif`
- `Astar_progress_animation.gif`
- `Bellman%E2%80%93Ford_algorithm_example.gif`
- `Shortest_path_with_direct_weights.svg`
- `Scc-1.svg`

String algorithms page:
- `Trie_example.svg`

Number-theoretic page:
- `Sieve_of_Eratosthenes_animation.gif`

Computational geometry page:
- `ConvexHull.svg`

Randomized algorithms page:
- `Skip_list.svg`

Approximation algorithms page:
- `TSP_Deutschland_3.png`

Pages without a Wikimedia match (Backtracking, Flow, some others): rely on Mermaid only, do not fabricate URLs. You may also embed `Algorithms.svg` (already used on `intro.md` / `big-o.md`) as a generic header on pages that have nothing else.

### Paper figures via ar5iv

Most foundational algorithms papers (Dijkstra 1959, Knuth-Morris-Pratt 1977, Strassen 1969, Cooley-Tukey 1965, Hoare 1962, Huffman 1952, Bellman 1958, Ford-Fulkerson 1956, Christofides 1976, Gale-Shapley 1962, etc.) are pre-arxiv and **do not have ar5iv figures**. Do **NOT** invent arxiv IDs for them. Only embed an ar5iv figure if the paper is a modern (post-2007) arxiv paper that you are confident has a real figure. For all classical algorithms, Mermaid + Wikimedia is the right visual.

### Image caption format

```markdown
*Figure: <one-line description>. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:FILENAME), Author, License.*
```

You may omit `Author, License` if not known; replace with `public domain or CC-BY-SA via Wikimedia Commons.`. Do not fabricate author names.

## Citation format

```markdown
Quicksort [1, Ch. 7] [8] partitions around a pivot...

## References
[1] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, *Introduction to Algorithms*, 4th ed. MIT Press, 2022.
[2] R. Sedgewick and K. Wayne, *Algorithms*, 4th ed. Addison-Wesley, 2011.
[3] J. Kleinberg and É. Tardos, *Algorithm Design*. Pearson, 2005.
[4] S. S. Skiena, *The Algorithm Design Manual*, 3rd ed. Springer, 2020.
[5] R. Motwani and P. Raghavan, *Randomized Algorithms*. Cambridge University Press, 1995.
[6] V. V. Vazirani, *Approximation Algorithms*. Springer, 2003.
[7] E. W. Dijkstra, "A note on two problems in connexion with graphs," *Numerische Mathematik*, 1959. https://doi.org/10.1007/BF01386390
[8] C. A. R. Hoare, "Quicksort," *The Computer Journal*, 1962. https://doi.org/10.1093/comjnl/5.1.10
...
```

### Foundational papers to cite where applicable

Each page MUST cite the relevant foundational paper(s) in addition to textbooks. Suggested mapping (use DOIs/links as shown when known; otherwise just author/venue/year):

- **Sorting**: Hoare 1962 (Quicksort), Williams 1964 (Heapsort), Knuth 1973 *TAOCP Vol. 3*, Sedgewick 1978 (Quicksort thesis)
- **Searching**: Hoare 1961 (Quickselect), Blum-Floyd-Pratt-Rivest-Tarjan 1973 (median-of-medians, *Journal of CSS*)
- **Divide and conquer**: Karatsuba-Ofman 1962, Strassen 1969 (*Numerische Mathematik*), Cooley-Tukey 1965 (*Mathematics of Computation*), Shamos-Hoey 1975 (closest pair)
- **Dynamic programming**: Bellman 1957 (book *Dynamic Programming*), Wagner-Fischer 1974 (edit distance), Knuth 1971 (optimal BST), Held-Karp 1962 (TSP DP)
- **Greedy**: Huffman 1952, Kruskal 1956, Prim 1957, Dijkstra 1959, Edmonds 1971 (matroid theorem)
- **Backtracking**: Knuth 2000 (*Dancing Links*, arxiv `cs/0011047`), Davis-Putnam-Logemann-Loveland 1962 (DPLL)
- **Graph**: Dijkstra 1959, Bellman 1958, Floyd 1962, Tarjan 1972 (SCC), Hopcroft-Tarjan 1973 (planarity), Johnson 1977 (all-pairs)
- **Network flow / matching**: Ford-Fulkerson 1956, Edmonds-Karp 1972, Dinic 1970, Hopcroft-Karp 1973, Goldberg-Tarjan 1986 (push-relabel), Gale-Shapley 1962
- **String**: Knuth-Morris-Pratt 1977 (*SIAM J. Comput.*), Boyer-Moore 1977, Aho-Corasick 1975, Karp-Rabin 1987, Ukkonen 1995 (suffix tree), Nong-Zhang-Chan 2009 (SA-IS)
- **Number theory**: Miller 1976, Rabin 1980, Pollard 1975 (rho), Agrawal-Kayal-Saxena 2004 (AKS, *Annals of Math*; arxiv `math/0205028`), Schönhage-Strassen 1971, Karatsuba-Ofman 1962
- **Geometry**: Graham 1972 (Graham scan, *IPL*), Andrew 1979 (monotone chain), Bentley-Ottmann 1979 (sweep line), Fortune 1987 (Voronoi), Chan 1996 (*output-sensitive convex hull*)
- **Randomized**: Bloom 1970 (*CACM*), Rabin 1976 (probabilistic algorithms), Karger 1993 (min-cut, *SODA*), Pugh 1990 (skip lists, *CACM*), Johnson-Lindenstrauss 1984, Freivalds 1979
- **Approximation**: Christofides 1976 (TSP), Lovász 1975 (set cover greedy), Goemans-Williamson 1995 (Max-Cut SDP, *JACM*), Arora-Lund-Motwani-Sudan-Szegedy 1998 (PCP theorem)

When citing journal/conference papers, write IEEE-style entries like:
```
[N] C. A. R. Hoare, "Quicksort," *The Computer Journal*, vol. 5, no. 1, pp. 10-16, 1962. https://doi.org/10.1093/comjnl/5.1.10
[N+1] D. R. Karger, "Global min-cuts in RNC, and other ramifications of a simple min-out algorithm," *SODA*, 1993.
```

## Constraints

- Stay inside `docs/cs/algorithms/`.
- Create exactly 13 new files (sidebar positions 3–15). Do not touch `intro.md` or `big-o.md`.
- No paper titles in filenames.
- No `_category_.json` or config edits.
- Mermaid label special chars in `"..."`; internal `"` → `#quot;`.
- For images, use `https://commons.wikimedia.org/wiki/Special:FilePath/<filename>` only. Skip if uncertain.
- English. Match depth addendum.

## Output summary

```
Pages created: 13
Word counts per page
Figures: Wikimedia=W, Mermaid=M
References per page (avg)
```

Begin now.
