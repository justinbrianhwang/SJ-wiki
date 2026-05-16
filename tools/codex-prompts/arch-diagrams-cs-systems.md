## Domain: CS Systems (OS, DB, Comp Arch, Embedded, ML/RL, NLP)

- **TARGET_DIRS** (visit each):
  - `f:/coding/SJ Wiki/docs/cs/operating-systems/`
  - `f:/coding/SJ Wiki/docs/cs/databases/`
  - `f:/coding/SJ Wiki/docs/cs/computer-architecture/`
  - `f:/coding/SJ Wiki/docs/cs/embedded/`
  - `f:/coding/SJ Wiki/docs/cs/data-mining/`
  - `f:/coding/SJ Wiki/docs/cs/machine-learning/`
  - `f:/coding/SJ Wiki/docs/cs/reinforcement-learning/`
  - `f:/coding/SJ Wiki/docs/cs/nlp/`
  - `f:/coding/SJ Wiki/docs/cs/data-structures/`
  - `f:/coding/SJ Wiki/docs/cs/algorithms/`
  - `f:/coding/SJ Wiki/docs/cs/theory/`
  - `f:/coding/SJ Wiki/docs/cs/programming/`

### Guidance

- **OS**: process state diagram (new → ready → running → waiting → terminated with transitions); scheduling Gantt-style diagram; virtual memory layout (kernel space / user space / heap / stack); paging with page table walk; multi-level page tables; TLB lookup; file system inode + indirect blocks layout; disk scheduling head movement; MESI / MOESI cache coherence state machines (real ones, not summaries).
- **DB**: B+ tree internal/leaf node layout with key separators and sibling pointers; query plan tree (LogicalPlan → optimized PhysicalPlan with chosen Hash Join / Merge Join nodes); ARIES recovery with WAL+CLR; MVCC version chain.
- **Comp Arch**: 5-stage RISC pipeline showing IF → ID → EX → MEM → WB with forwarding paths and bubble locations; cache line layout (tag/set/offset bits); virtual address translation through TLB → page table; superscalar issue width; out-of-order Tomasulo with reservation stations and CDB; branch predictor (2-bit FSM, gshare).
- **Embedded**: 8085 register file + flags + bus diagram; 8051 architecture (CPU, on-chip RAM, ROM, ports, timers, serial UART); 8255 mode 0/1/2 wiring; AVR ATmega register file; SPI / I2C / UART timing diagrams.
- **Data Mining**: k-means iteration as a state diagram; decision-tree growth; DBSCAN density reachability; Apriori candidate generation; PageRank power iteration as a data-flow graph.
- **ML**: SVM margin geometry illustrated as graph with support vectors highlighted; Naive Bayes graphical model; expectation-maximization E-step / M-step loop; gradient descent contour with iterations; bias-variance decomposition diagram.
- **RL**: actor-environment loop; Q-learning update with target network; Monte Carlo vs TD update; eligibility traces; policy gradient computation graph.
- **NLP**: encoder-decoder MT pipeline; CKY parsing chart; dependency parse tree example; CRF chain factor graph; word2vec skip-gram negative-sampling sampler.
- **Data structures**: skip list with pointer levels; B-tree node layout; LSM tree compaction; trie with branching factor; union-find with path compression + union by rank.
- **Algorithms**: A* open/closed list flow; Dijkstra with priority queue updates; merge-sort recursion tree; quicksort partition step.
- **Theory**: DFA / NFA / PDA / Turing machine state diagrams (with explicit transitions on at least 2 inputs); Cook-Levin reduction structure; Karp reduction examples.
- **Programming languages**: C compilation pipeline (preprocessor → compile → assemble → link); C++ object layout with vtable; Rust ownership/borrow check decision flow; Python interpreter bytecode loop; Java JVM (classloader → bytecode → JIT → native).

Apply the policy. Be ruthless about replacing toy diagrams with proper architecture-level ones.

Begin now.
