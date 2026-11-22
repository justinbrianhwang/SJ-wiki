---
title: Memory Architectures
sidebar_position: 58
---

# Memory Architectures

Memory architecture is often the difference between an embedded system that merely runs and one that meets its timing, energy, persistence, and reliability requirements. Embedded systems mix volatile and non-volatile technologies, small fast memories and larger slow memories, memory-mapped devices, stacks, heaps, caches, scratchpads, and sometimes memory-protection hardware.

Lee and Seshia treat memory as part of the cyber-physical platform because it affects not only capacity but timing. A cache miss, DRAM refresh, flash write, page fault, stack overflow, or garbage-collection pause can change whether a task meets a real-time deadline.

## Definitions

**Volatile memory** loses contents when power is removed. SRAM and DRAM are volatile; DRAM also requires refresh while powered.

**Non-volatile memory** persists without power. ROM, EEPROM, flash, and disks are examples. Flash is common in embedded systems but has slow writes, block erase constraints, and limited write endurance.

A **memory hierarchy** combines memories with different cost, capacity, energy, and speed. Registers are closest to the CPU; SRAM, cache, DRAM, flash, and disk-like storage are progressively farther away.

A **memory map** assigns address ranges to memory or devices. In memory-mapped I/O, writing an address may configure a timer, set a GPIO output, or acknowledge an interrupt rather than store ordinary data.

A **Harvard architecture** separates program and data memories, often allowing instruction fetch and data access to proceed in parallel. A **von Neumann architecture** uses one memory space for both program and data.

A **scratchpad** is a fast memory explicitly managed by software. A **cache** is a fast memory automatically managed by hardware to duplicate recently used blocks from slower memory.

A cache is often described by address width $m$, number of sets $S=2^s$, associativity $E$, and block size $B=2^b$. Its data capacity is

$$
C=S E B.
$$

A **stack** stores procedure-call frames in last-in, first-out order. A **heap** supports dynamic memory allocation such as `malloc` and `free`.

## Key results

Memory timing is platform behavior, not just program behavior. The same instruction sequence can take different time depending on whether data are in registers, SRAM, cache, DRAM, flash, or a memory-mapped peripheral.

Caches improve average performance but complicate worst-case timing. A direct-mapped cache has one line per set, so two addresses mapping to the same set can repeatedly evict each other. A set-associative cache reduces conflict misses but uses replacement policies such as LRU or FIFO, which must be analyzed.

Flash memory is not a drop-in replacement for RAM. Reads may be reasonably fast, but writes and erases are much slower, often block-oriented, and endurance-limited. Firmware and persistent configuration belong in flash; frequently changing working data usually do not.

Stack overflow is dangerous in embedded C. If stack growth exceeds the allocated region, it may overwrite globals, heap objects, interrupt data, or memory-mapped regions. A program may then fail far from the cause.

Dynamic allocation is risky in long-running real-time systems. Memory leaks exhaust memory; fragmentation prevents large allocations even when total free memory is sufficient; garbage collection or defragmentation can introduce long pauses.

C's memory model exposes addresses through pointers. Returning a pointer to a local stack variable is invalid because the stack frame disappears after the function returns.

Memory maps are also documentation of authority. If a region maps to flash, writes may be slow or require special erase sequences. If a region maps to GPIO or a timer, a write may cause immediate physical effects. If a region is reserved, accessing it may trigger a fault or undefined hardware behavior. Embedded C code that manipulates raw addresses must therefore be reviewed against the processor reference manual, not just against the C language.

Caches and scratchpads represent two different philosophies. A cache tries to make fast memory transparent, which is helpful for average performance but problematic for timing guarantees. A scratchpad makes fast memory explicit, which burdens the programmer or compiler but can support repeatable timing. Some real-time designs deliberately disable caches for critical regions or lock selected cache lines, while others place critical data in tightly coupled memory.

Persistent memory introduces lifecycle concerns. Flash endurance means that a logging design that writes every millisecond may wear out a sector quickly. Block erase means that updating one byte can require copying and rewriting a larger region. Power failure during an update can corrupt state unless the design uses journaling, double buffering, checksums, or another recovery protocol. These concerns belong in the system model because they affect long-term correctness.

Memory protection changes failure modes. Without protection, a bad pointer can silently overwrite another task's data or a device register. With a memory protection unit or memory management unit, the same bug may raise an exception that can be handled by the kernel or fault manager. Protection is not free: it requires configuration, context-switch support, and a clear memory layout. In safety-oriented embedded systems, those costs may be worthwhile because they turn silent corruption into a diagnosable fault.

Stacks deserve special attention because they are easy to underestimate. Ordinary function calls, nested calls, interrupt service routines, compiler-generated spill code, and library calls all consume stack space. If interrupts can nest, the worst-case stack includes the interrupted task's call chain plus one or more ISR frames. Recursion makes static stack bounds much harder, which is why many embedded coding standards ban it. A stack-size calculation is therefore a quantitative analysis problem tied directly to the memory architecture.

The C abstract machine also hides details that matter on hardware. Alignment restrictions, endianness, volatile access, and aliasing rules can affect whether a memory operation is valid and what code the compiler emits. Firmware that casts integers to pointers or overlays structures on device registers is stepping outside ordinary portable C and into the platform contract.

Memory architecture is therefore a cross-cutting design input. It influences compiler output, startup code, linker scripts, bootloaders, interrupt latency, persistence, security, and WCET. A memory map should be treated as an executable contract between hardware, toolchain, operating system, and application code. When that contract is vague, bugs tend to appear as rare crashes, corrupt configuration, or timing anomalies.

Good reviews check both the map and the code that assumes it, including startup initialization.

## Visual

```text
Fast / small / close to CPU

  registers
      |
  L1 cache or scratchpad
      |
  SRAM
      |
  DRAM
      |
  flash / disk-like storage

Slow / large / persistent
```

| Memory type | Volatile | Typical use | Timing concern |
|---|---|---|---|
| Register file | Yes | Current operands | Very fast, scarce |
| SRAM | Yes | stack, heap, working data | Predictable relative to DRAM |
| DRAM | Yes | larger working memory | Refresh and access history |
| NOR flash | No | executable firmware | Slow writes/erases |
| NAND flash | No | block storage | Block access and wear |
| Cache | Yes | automatic copies | hits/misses and replacement |
| Scratchpad | Yes | managed hot data | programmer/compiler burden |

## Worked example 1: Cache capacity and address fields

Problem: A 32-bit address machine has a cache with $S=64$ sets, associativity $E=2$, and block size $B=16$ bytes. Compute the data capacity and the number of offset, set-index, and tag bits.

Method:

1. Capacity:

$$
C=S E B = 64\cdot 2\cdot 16 = 2048\text{ bytes}.
$$

2. Block offset bits:

$$
B=16=2^4 \Rightarrow b=4.
$$

3. Set index bits:

$$
S=64=2^6 \Rightarrow s=6.
$$

4. Tag bits:

$$
t=m-s-b=32-6-4=22.
$$

Answer: The cache stores $2048$ data bytes. Each address has $4$ offset bits, $6$ set-index bits, and $22$ tag bits.

## Worked example 2: Direct-mapped conflict

Problem: A direct-mapped cache has $S=4$ sets and block size $B=16$ bytes. Addresses $0x00$ and $0x40$ are accessed alternately. Determine whether they map to the same set.

Method:

1. The block number for address $a$ is

$$
\left\lfloor a/B\right\rfloor.
$$

2. For $0x00=0$:

$$
\left\lfloor 0/16\right\rfloor=0.
$$

3. For $0x40=64$:

$$
\left\lfloor 64/16\right\rfloor=4.
$$

4. Set index is block number modulo number of sets:

$$
0\bmod 4=0,\qquad 4\bmod 4=0.
$$

5. Both blocks map to set $0$. Because the cache is direct-mapped, set $0$ has only one line.

Answer: The two addresses conflict. Alternating accesses can cause repeated misses because each block evicts the other.

## Code

```python
def cache_fields(address, sets=64, block_size=16):
    block = address // block_size
    set_index = block % sets
    offset = address % block_size
    tag = block // sets
    return {"tag": tag, "set": set_index, "offset": offset}

for address in [0x00, 0x10, 0x40, 0x400]:
    print(hex(address), cache_fields(address, sets=4, block_size=16))
```

## Common pitfalls

- Assuming RAM, flash, and memory-mapped registers behave like identical arrays of bytes.
- Using caches in hard real-time paths without accounting for hit/miss variability.
- Returning pointers to stack-local variables in C.
- Allowing unbounded recursion or large automatic arrays on a small embedded stack.
- Relying on dynamic allocation in long-running firmware without leak, fragmentation, and pause-time analysis.
- Forgetting that global variables may retain values across soft resets if the program is not fully reloaded.

## Connections

- [embedded processors architecture](/cs/embedded/embedded-processors-architecture)
- [input and output interfacing](/cs/embedded/input-output-interfacing)
- [8051 architecture, memory, and ports](/cs/embedded/8051-architecture-memory-ports)
- [8085 I/O, memory, and DMA interfacing](/cs/embedded/8085-io-memory-dma-interfacing)
- [quantitative analysis](/cs/embedded/quantitative-analysis)
