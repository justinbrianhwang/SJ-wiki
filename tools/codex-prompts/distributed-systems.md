You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for a new **Distributed Systems** subject under `docs/cs/distributed-systems/`.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/distributed-systems/`
- **SUPPLIED_TEXTBOOKS**: `f:/coding/SJ Wiki/tmp/Distributed Systems/`
  - `Designing Data-Intensive Applications - Martin Kleppmann.pdf` (Kleppmann DDIA — systems-engineering focus)
  - `Distributed Algorithms - Nancy A. Lynch.pdf` (Lynch DA — formal algorithm focus)
  - `Distributed Systems - Maarten van Steen, Andrew S. Tanenbaum.pdf` (van Steen-Tanenbaum DS — textbook breadth)
- **STYLE**: Topical chapter names. IEEE inline citations `[N]`.

## Combine mode

When topics overlap across the 3 books (consistency, consensus, replication, fault tolerance), write **one** chapter that synthesizes the systems view (Kleppmann), formal model (Lynch), and textbook view (Steen-Tanenbaum). Don't duplicate.

## Workflow

1. `pdfinfo` for page counts, `pdftotext -l 30` for TOCs.
2. Iterate topics, synthesize per chapter.
3. Replace `intro.md` last.
4. Print summary.

## Produce

### 1. Replace `intro.md` (sidebar_position 0)
250-400 word overview describing the systems / algorithmic / textbook perspectives, plus numbered list of all pages.

### 2. Create exactly 10 detail pages

| sidebar_position | filename | title |
|---|---|---|
| 1 | `foundations-and-system-models.md` | Foundations and System Models |
| 2 | `time-clocks-and-event-ordering.md` | Time, Clocks, and Event Ordering |
| 3 | `replication-and-consistency.md` | Replication and Consistency |
| 4 | `consensus-paxos-and-raft.md` | Consensus: Paxos and Raft |
| 5 | `fault-tolerance-and-failure-detection.md` | Fault Tolerance and Failure Detection |
| 6 | `transactions-and-isolation-levels.md` | Transactions and Isolation Levels |
| 7 | `partitioning-and-sharding.md` | Partitioning and Sharding |
| 8 | `distributed-storage-and-cap.md` | Distributed Storage and CAP |
| 9 | `stream-processing-and-event-driven-systems.md` | Stream Processing and Event-Driven Systems |
| 10 | `security-and-byzantine-fault-tolerance.md` | Security and Byzantine Fault Tolerance |

## Content scope

### 1 Foundations
- What is a distributed system; transparency goals (access, location, replication, concurrency, failure)
- System models: synchronous / asynchronous / partially synchronous; message-passing vs shared memory
- Failure models: crash-stop, crash-recovery, omission, Byzantine
- FLP impossibility (Fischer-Lynch-Paterson 1985); CAP statement
- Lynch's I/O automata formalism (brief)

### 2 Time, Clocks, Event Ordering
- Physical clocks, drift, NTP, PTP, TrueTime (Google Spanner)
- Logical time: Lamport clocks (Lamport 1978), vector clocks (Mattern, Fidge 1988)
- Happens-before relation, concurrent events
- Hybrid logical clocks (Kulkarni et al. 2014)
- Snapshot algorithms: Chandy-Lamport (1985)

### 3 Replication and Consistency
- Replication strategies: primary-backup, chain, quorum, leaderless
- Consistency models: linearizability (Herlihy-Wing 1990), sequential consistency, causal consistency, eventual consistency
- Read-your-writes, monotonic reads, monotonic writes, writes-follow-reads (session guarantees)
- CRDTs (state-based and op-based): counters, registers, sets
- Anti-entropy: gossip, Merkle trees
- Read repair, hinted handoff

### 4 Consensus
- Problem statement: agreement, validity, termination
- Paxos (Lamport 1998, 2001) — Single-decree Paxos, Multi-Paxos, prepare/promise/accept phases
- Raft (Ongaro-Ousterhout 2014) — leader election, log replication, safety
- Byzantine consensus: PBFT (Castro-Liskov 1999), HotStuff (Yin et al. 2019)
- Zab (ZooKeeper), Viewstamped Replication
- Reconfiguration and joint consensus

### 5 Fault Tolerance and Failure Detection
- Failure detector classes (Chandra-Toueg 1996): perfect, eventually perfect, strong, weak
- Heartbeats, $\phi$-accrual failure detector (Hayashibara 2004)
- Crash recovery, write-ahead logging
- State-machine replication (Schneider 1990)
- Checkpointing, message logging
- Recovery time objective (RTO), recovery point objective (RPO)

### 6 Transactions and Isolation Levels
- ACID, BASE
- Isolation levels: read uncommitted / committed, repeatable read, snapshot isolation, serializable
- Anomalies: dirty read, non-repeatable read, phantom, write skew, lost update
- Concurrency control: 2PL, OCC, MVCC, timestamp ordering
- Distributed transactions: 2PC, 3PC, Saga, Percolator (Google)
- Spanner, Calvin, Aurora

### 7 Partitioning and Sharding
- Key-range partitioning vs hash partitioning vs consistent hashing
- Skew, hot spots, rebalancing
- Secondary indexes (local vs global)
- Routing requests: client-side, proxy, gossip
- Resharding without downtime

### 8 Distributed Storage and CAP
- CAP theorem (Brewer; Gilbert-Lynch 2002 proof)
- PACELC (Abadi 2012)
- Distributed file systems: GFS, HDFS, Ceph
- Key-value stores: Dynamo, Cassandra, Riak; LSM-trees (LevelDB, RocksDB)
- Object storage (S3 architecture)
- Lakehouse / OLAP: Iceberg, Delta Lake, Hudi
- Storage tiers, erasure coding (Reed-Solomon)

### 9 Stream Processing and Event-Driven Systems
- Pub/sub: Kafka, Pulsar, Kinesis; partitions, consumer groups, offsets
- Exactly-once semantics (Kafka EOS, Flink checkpoints)
- Watermarks, windows (tumbling, sliding, session), late data
- Stream-stream and stream-table joins
- Stateful operators, RocksDB-backed state, savepoints
- Event sourcing, CQRS

### 10 Security and Byzantine Fault Tolerance
- Threat models: malicious participants, eclipse attack, Sybil, BGP hijacking
- Byzantine consensus revisited (PBFT, HotStuff)
- Blockchain consensus: PoW, PoS, BFT-based (Tendermint, Algorand)
- Authenticated data structures: Merkle trees, accumulators
- Secret sharing, threshold cryptography (cross-link cryptography)
- Network adversaries, secure channels
- Trusted execution environments in distributed contexts

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter
2. `# Title` H1
3. 1-2 opening paragraphs
4. (Optional) 1-2 Wikimedia or paper figures with attribution
5. `## Definitions`
6. `## Key results` — protocols/theorems/proofs
7. `## Visual` — **MANDATORY Mermaid** (Paxos message diagram, Raft leader election state, vector clock evolution, CAP triangle, 2PC sequence, Kafka consumer/partition diagram, etc.)
8. `## Worked example 1` (e.g., trace Lamport clocks on a 3-process scenario; Raft leader election timeline)
9. `## Worked example 2`
10. `## Code` — Python: vector-clock implementation, simple Raft RPC stub, 2PC coordinator/participant, Kafka-style offset tracking
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — links to [Computer Networks](/cs/computer-networks/intro), [Operating Systems](/cs/operating-systems/intro), [Databases](/cs/databases/intro), [Cryptography](/cs/cryptography/intro)
13. `## References` — IEEE-style (cite all 3 supplied textbooks + foundational papers: Lamport 1978/1998, Fischer-Lynch-Paterson 1985, Brewer/CAP/Gilbert-Lynch 2002, Chandra-Toueg 1996, Castro-Liskov PBFT 1999, Ongaro-Ousterhout Raft 2014, Herlihy-Wing 1990, Chandy-Lamport 1985, Dean-Ghemawat GFS/MapReduce, Lakshman-Malik Cassandra, etc.)

## Word count

Each page: **2000-3500 words**.

## Visual policy

- **Mermaid mandatory** per page.
- Optional Wikimedia images (be conservative — skip if uncertain).
- Skip arxiv figures unless certain (most foundational DS papers are pre-arxiv).
- For Raft, a Wikimedia image like `Raft_(algorithm).svg` exists — but verify by HEAD-checking conservatively.
- Do not fabricate filenames.

## Constraints

- Stay inside `docs/cs/distributed-systems/`. Do not touch `_category_.json`.
- No paper titles in filenames.
- Mermaid special chars in `"..."`; internal `"` → `#quot;`.
- English. Match depth addendum.

## Output summary

```
Pages created: 1 intro + 10 detail = 11
Word counts per page
Figures: Wikimedia=W, Mermaid=M
References per page (avg)
```

Begin now.
