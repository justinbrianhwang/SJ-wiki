---
title: Cache Organization and AMAT
sidebar_position: 9
---

# Cache Organization and AMAT

Processors are much faster than main memory, so modern computers rely on a hierarchy of storage technologies. Small memories close to the processor are fast and expensive per byte. Larger memories farther away are slower and cheaper per byte. Caches exploit locality so that most accesses hit in a fast level while the full address space remains backed by larger memory.

The central cache question is quantitative: how much does a design reduce execution time, not just miss rate? A larger block may reduce compulsory misses but increase miss penalty. Higher associativity may reduce conflict misses but lengthen hit time. A bigger cache may reduce capacity misses while increasing power and access latency. Average memory access time, AMAT, is the first-order model that keeps these trade-offs visible.

![A cache hierarchy diagram shows progressively larger memory levels between CPU cores and main memory.](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Multi-level_Cache_Hierarchy.svg/500px-Multi-level_Cache_Hierarchy.svg.png)

*Figure: Multi-level cache hierarchy between processors and memory. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Multi-level_Cache_Hierarchy.svg), Ferry24.Milan, CC BY-SA 3.0.*

## Definitions

A cache block, or line, is the unit transferred between adjacent hierarchy levels. If a processor requests an address and the corresponding block is present in the cache, the access is a hit. Otherwise it is a miss, and a lower level must supply the block.

The cache fields for a byte address are:

$$
\mathrm{Address} = \mathrm{Tag}\ \Vert\ \mathrm{Index}\ \Vert\ \mathrm{Block\ offset}
$$

The block offset chooses a byte within a cache block. The index chooses a set. The tag identifies which memory block is currently stored in a cache entry.

Placement policies include:

- Direct-mapped: each memory block maps to exactly one cache location.
- Set-associative: each block maps to one set and may occupy any way in that set.
- Fully associative: a block may occupy any cache location.

The number of sets in a set-associative cache is:

$$
\mathrm{Sets}=
\frac{\mathrm{Cache\ size}}{\mathrm{Block\ size}\times \mathrm{Associativity}}
$$

Misses are often classified by the three Cs:

- Compulsory misses: first access to a block.
- Capacity misses: cache cannot hold the working set.
- Conflict misses: placement restrictions force useful blocks to evict one another.

Average memory access time is:

$$
\mathrm{AMAT}=
\mathrm{Hit\ time}+
\mathrm{Miss\ rate}\times\mathrm{Miss\ penalty}
$$

For two cache levels:

$$
\mathrm{AMAT}=
T_{L1}+
MR_{L1}\times(T_{L2}+MR_{L2}\times P_{L2})
$$

Here $MR_{L2}$ is the local L2 miss rate among accesses that reach L2, unless explicitly stated as a global miss rate.

## Key results

Locality is the reason caches work. Temporal locality says recently used data is likely to be used again. Spatial locality says nearby data is likely to be used soon. Instruction streams often have strong spatial locality; loops add temporal locality. Data locality depends heavily on layout and access order.

Associativity reduces conflict misses, but it is not free. More ways require more tag comparisons and a way selection. This can increase hit time and energy. Many L1 caches use modest associativity to keep hit time short. Lower-level caches can be larger and more associative because their hit time is less often on the processor's critical path.

Write policies solve the problem that stores update cached copies. A write-through cache updates the lower level on every store. It is simpler and keeps lower memory current, but it increases write traffic. A write-back cache updates only the cache on a hit and writes the block to the lower level when it is evicted if dirty. It reduces bandwidth but requires dirty bits and more complex coherence.

Write allocation controls what happens on a store miss. Write-allocate brings the block into cache, then writes it. No-write-allocate writes directly to the lower level without filling the cache. Write-back caches commonly use write-allocate; write-through caches may use either.

AMAT is not the final performance metric. Out-of-order cores can overlap some misses with other work. Multithreading can hide latency. Memory bandwidth can dominate when many cores miss at once. Still, AMAT is the basic language for reasoning about cache organization.

Address mapping deserves special care because a cache is not just a small memory; it is a small memory with rules about where each block may reside. Two arrays whose addresses differ by a multiple of the cache size can repeatedly map to the same direct-mapped line, creating conflict misses even when the cache has enough total capacity. Padding or changing layout can fix such conflicts without changing hardware.

Replacement policy matters most when associativity is limited and the working set is near the cache capacity. Least recently used, LRU, is intuitive but expensive to implement exactly for high associativity. Many caches use approximations such as pseudo-LRU or random replacement. The performance difference is workload-dependent, and the energy and timing cost of exact tracking may not be justified.

Inclusive, exclusive, and non-inclusive multilevel caches also change behavior. An inclusive lower-level cache contains copies of blocks in upper levels, which can simplify coherence because the shared last-level cache knows which blocks may be private. The cost is duplication and possible back-invalidation when the lower level evicts a block. Exclusive caches avoid duplication but make lookup and movement policies more complex.

## Visual

```text
32-bit address with 64-byte blocks and 256 sets

  31                         14 13          6 5        0
 +-----------------------------+-------------+----------+
 |             Tag             |    Index    |  Offset  |
 +-----------------------------+-------------+----------+
                 18 bits            8 bits      6 bits
```

| Organization | Placement | Hit lookup | Main advantage | Main drawback |
|---|---|---|---|---|
| Direct-mapped | One possible line | One tag compare | Fast and low power | Conflict misses |
| 2-way set associative | Two possible ways | Two compares | Fewer conflicts | More energy than direct |
| 8-way set associative | Eight ways | Many compares | Good for lower levels | Longer hit path |
| Fully associative | Anywhere | Search all entries | Minimal conflicts | Expensive for large caches |

## Worked example 1: Cache fields and number of sets

Problem: A 32 KiB L1 data cache is 4-way set associative with 64-byte blocks and byte addressing. Addresses are 32 bits. Find the number of sets and the number of offset, index, and tag bits.

Method:

1. Convert cache size to bytes.

$$
32\ \mathrm{KiB}=32\times1024=32768\ \mathrm{bytes}
$$

2. Compute sets.

$$
\begin{aligned}
\mathrm{Sets}
&= \frac{32768}{64 \times 4} \\
&= \frac{32768}{256} \\
&= 128
\end{aligned}
$$

3. Compute offset bits.

$$
64=2^6
$$

So the block offset uses 6 bits.

4. Compute index bits.

$$
128=2^7
$$

So the set index uses 7 bits.

5. Compute tag bits.

$$
\mathrm{Tag\ bits}=32-7-6=19
$$

Checked answer: The cache has 128 sets, 6 offset bits, 7 index bits, and 19 tag bits. The fields add to 32 bits, so the decomposition is consistent.

## Worked example 2: AMAT for a two-level hierarchy

Problem: An L1 cache has hit time 1 cycle and miss rate 4%. The L2 cache has hit time 10 cycles and local miss rate 20%. Main-memory penalty after an L2 miss is 100 cycles. Compute AMAT.

Method:

1. Write the two-level formula.

$$
\mathrm{AMAT}=T_{L1}+MR_{L1}(T_{L2}+MR_{L2}P_{L2})
$$

2. Substitute values.

$$
\begin{aligned}
\mathrm{AMAT}
&= 1 + 0.04(10 + 0.20 \times 100) \\
&= 1 + 0.04(10 + 20) \\
&= 1 + 0.04 \times 30 \\
&= 1 + 1.2 \\
&= 2.2\ \mathrm{cycles}
\end{aligned}
$$

3. Check using 10,000 memory references.

L1 misses:

$$
10000 \times 0.04=400
$$

L2 misses:

$$
400 \times 0.20=80
$$

Total cycles:

$$
10000(1)+400(10)+80(100)=22000
$$

Average:

$$
22000/10000=2.2
$$

Checked answer: AMAT is 2.2 cycles per memory reference. The reference-count check matches the formula.

## Code

```python
def cache_fields(address_bits, cache_bytes, block_bytes, ways):
    sets = cache_bytes // (block_bytes * ways)
    if sets & (sets - 1):
        raise ValueError("sets must be a power of two")
    offset_bits = block_bytes.bit_length() - 1
    index_bits = sets.bit_length() - 1
    tag_bits = address_bits - offset_bits - index_bits
    return sets, tag_bits, index_bits, offset_bits

def amat(l1_hit, l1_miss_rate, l2_hit=None, l2_miss_rate=None, mem_penalty=None):
    if l2_hit is None:
        return l1_hit + l1_miss_rate * mem_penalty
    return l1_hit + l1_miss_rate * (l2_hit + l2_miss_rate * mem_penalty)

print(cache_fields(32, cache_bytes=32 * 1024, block_bytes=64, ways=4))
print(f"AMAT={amat(1, 0.04, 10, 0.20, 100):.2f} cycles")
```

This code treats every memory reference as if it pays the same average cost. That is useful for early reasoning, but instruction fetches, loads, stores, page-table walks, and prefetches can see different paths through the hierarchy. A write miss may allocate a block, merge into a write buffer, or wait for ownership from the coherence protocol. A load miss on an out-of-order core may be partly hidden if independent instructions execute while the miss is outstanding.

The field calculation also assumes power-of-two sizes and a conventional indexed cache. Some specialized memories use banking, hashing, skewed associativity, or victim buffers that complicate the simple tag-index-offset picture. The simple picture remains the foundation because it explains why alignment, stride, and address bits can have visible performance effects.

## Common pitfalls

- Confusing local and global miss rates in multilevel caches.
- Optimizing miss rate while increasing hit time enough to lose performance.
- Forgetting that block size changes both miss rate and miss penalty.
- Assuming higher associativity is always better.
- Ignoring write-buffer stalls and dirty write-backs in write-back caches.
- Treating AMAT as exact execution time on processors that overlap misses.

## Connections

- [Cache Optimization and Prefetching](/cs/computer-architecture/cache-optimization-and-prefetching)
- [Virtual Memory, TLBs, and VMs](/cs/computer-architecture/virtual-memory-tlb-vms)
- [Coherence, Consistency, and MESI](/cs/computer-architecture/coherence-consistency-mesi)
- [Quantitative Design and Performance](/cs/computer-architecture/quantitative-design-and-performance)
