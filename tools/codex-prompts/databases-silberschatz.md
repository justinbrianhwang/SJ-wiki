You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Abraham-Silberschatz-Henry-F.-Korth-S.-Sudarshan-Database-System-Concepts-McGraw-Hill-Education-2019.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/databases/`
- **SUBJECT**: Database Systems (Silberschatz, Korth, Sudarshan — 7th ed)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **15-22 detail pages** covering:
   - Relational model + relational algebra
   - SQL (DDL, DML, joins, subqueries, views, aggregation, window functions)
   - Database design (E-R modeling, conversion to relations)
   - Normalization (1NF–BCNF, 3NF, decomposition, multi-valued dependencies, 4NF)
   - Storage and file structure (records, blocks, indexes)
   - Indexing (B+ trees, hash indexes, bitmap)
   - Query processing & optimization (algorithms for joins, cost estimation)
   - Transactions (ACID, serializability, recoverability)
   - Concurrency control (2PL, deadlocks, timestamp ordering, MVCC, snapshot isolation)
   - Recovery (write-ahead logging, ARIES, checkpoints)
   - Distributed databases (replication, partitioning, 2PC, CAP)
   - NoSQL & big data overview

3. Per-page format: motivation → formal definitions → algorithms/SQL examples → trade-offs.

4. Use `sql` and `python` code blocks for SQL and procedural examples. Diagrams in Mermaid for E-R and B+ trees.

## Workflow

1. `pdfinfo` → page count.
2. `pdftotext -l 30` → TOC.
3. Iterate chapters; write 1-3 pages each.
4. Write `intro.md` last.
5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits, no config edits, no `npm`. English. Don't fabricate.

Begin now.
