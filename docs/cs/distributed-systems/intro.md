---
title: Distributed Systems
sidebar_position: 0
---

# Distributed Systems

Distributed systems study what happens when a computation is spread across independently failing machines connected by imperfect networks. The subject sits between systems engineering, algorithms, databases, operating systems, networking, and security. The notes in this section synthesize three complementary perspectives: Kleppmann's data-intensive systems view, Lynch's formal distributed-algorithms view, and van Steen and Tanenbaum's broad textbook view.

Kleppmann is strongest on the production trade-offs behind replication, partitioning, transactions, storage engines, stream processing, and the reality of unreliable clocks and networks. Lynch supplies the mathematical model: message passing, shared memory, executions, safety, liveness, impossibility results, I/O automata, consensus, snapshots, and Byzantine agreement. Van Steen and Tanenbaum provide the wide map of distributed-system goals: transparency, scalability, communication, naming, coordination, replication, fault tolerance, and security. Combining them keeps the wiki from treating distributed systems as only a database subject, only a proof subject, or only a middleware subject.

Read these pages as a layered path. Start with models and time, then move to replication, consensus, and failures. After that, study the data-system topics: transactions, partitioning, storage, and streams. The final page revisits fault tolerance under malicious behavior and links the subject to cryptography.

1. [Foundations and System Models](/cs/distributed-systems/foundations-and-system-models)
2. [Time, Clocks, and Event Ordering](/cs/distributed-systems/time-clocks-and-event-ordering)
3. [Replication and Consistency](/cs/distributed-systems/replication-and-consistency)
4. [Consensus: Paxos and Raft](/cs/distributed-systems/consensus-paxos-and-raft)
5. [Fault Tolerance and Failure Detection](/cs/distributed-systems/fault-tolerance-and-failure-detection)
6. [Transactions and Isolation Levels](/cs/distributed-systems/transactions-and-isolation-levels)
7. [Partitioning and Sharding](/cs/distributed-systems/partitioning-and-sharding)
8. [Distributed Storage and CAP](/cs/distributed-systems/distributed-storage-and-cap)
9. [Stream Processing and Event-Driven Systems](/cs/distributed-systems/stream-processing-and-event-driven-systems)
10. [Security and Byzantine Fault Tolerance](/cs/distributed-systems/security-and-byzantine-fault-tolerance)
