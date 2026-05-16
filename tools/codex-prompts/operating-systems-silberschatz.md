You are an autonomous content author for **SJ Wiki**. Generate **detailed**, well-structured Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Operating_System_Concepts_Essentials_2nd_Edition.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/operating-systems/`
- **SUBJECT**: Operating Systems (Silberschatz, Galvin, Gagne — *Operating System Concepts Essentials*, 2nd ed)

## What to produce

1. **`intro.md`** — replace the stub. Overview + chapter list.

2. **One Markdown file per major topic.** Cover the dinosaur book's scope:
   - OS introduction (services, system calls, kernel structure)
   - Processes (process control block, scheduling states, IPC)
   - Threads (user vs kernel threads, models, libraries: POSIX/Java)
   - CPU scheduling (FCFS, SJF, priority, RR, multilevel, real-time, multiprocessor)
   - Process synchronization (race conditions, critical sections, semaphores, monitors, deadlocks)
   - Deadlocks (necessary conditions, prevention, avoidance with banker's, detection, recovery)
   - Main memory management (paging, segmentation, TLB)
   - Virtual memory (demand paging, page replacement: FIFO/LRU/clock, thrashing, working set)
   - File systems (interface, implementation, allocation methods, free-space management)
   - Mass storage (disk scheduling: FCFS/SSTF/SCAN/C-SCAN/LOOK, RAID)
   - I/O systems (hardware, kernel I/O subsystem, performance)
   - Protection & security (access control, capability lists, ACLs, encryption basics)

   Aim for **15-22 pages**, each 500-1500 words.

3. **Per-page format**: motivation → mechanisms → algorithms (with pseudocode) → trade-offs → real-world examples (Linux/Windows where mentioned).

4. **Diagrams** in Mermaid for state transitions and structures where simple.

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 30` → cover + TOC.
3. Iterate chapters; write 1-3 wiki pages each.
4. Write `intro.md` last.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/operating-systems/`. Don't touch other folders, `_category_.json`, config files.
- Don't run `npm`.
- English. Precise. Don't fabricate.

Begin now.
