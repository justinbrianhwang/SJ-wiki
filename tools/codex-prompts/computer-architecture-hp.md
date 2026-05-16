You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Computer Architecture A Quantitative Approach (5th edition).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/computer-architecture/`
- **SUBJECT**: Computer Architecture (Hennessy & Patterson — *A Quantitative Approach*, 5th ed)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **15-22 detail pages** covering H&P 5e scope:
   - Fundamentals (Moore's law, Amdahl's law, performance metrics)
   - ISAs (RISC vs CISC, addressing modes, MIPS / RISC-V style)
   - Pipelining (5-stage, hazards: structural/data/control, forwarding, branch prediction)
   - Instruction-level parallelism (out-of-order execution, Tomasulo, register renaming, speculation)
   - Memory hierarchy (cache organization, replacement, write policies, multi-level)
   - Virtual memory hardware support (TLB, page tables)
   - Cache coherence and consistency (MESI, snooping, directory protocols)
   - Multicore & multiprocessors (SMP, NUMA, synchronization primitives)
   - Vector / SIMD / GPU architectures
   - Warehouse-scale computers
   - Storage systems (RAID, SSDs)
   - Domain-specific architectures (TPUs, accelerators — if covered)

3. **Quantitative**: include formulas (CPI = Σ(IC_i × CPI_i) / IC, AMAT = hit time + miss rate × miss penalty, speedup, etc.) and worked numerical examples.

4. Code/pseudocode for branch predictors, cache lookups, etc.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 35` for TOC. 3. Iterate chapters; 1-3 pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
