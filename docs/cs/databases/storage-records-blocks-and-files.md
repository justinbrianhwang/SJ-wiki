---
title: Storage, Records, Blocks, and Files
sidebar_position: 9
---

# Storage, Records, Blocks, and Files

The relational model hides physical storage, but database systems live on real hardware. Records must be laid out in pages or blocks, pages must be read into memory, and files must be organized so that common access patterns are not painfully expensive. Storage design explains why a query can be fast or slow before indexes and optimizers even enter the discussion.

![A PostgreSQL B-tree diagram shows index pages connected by parent and leaf links.](https://commons.wikimedia.org/wiki/Special:FilePath/PostgreSQL_B-tree.svg)

*Figure: PostgreSQL B-tree pages show how logical indexes map to storage structures. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:PostgreSQL_B-tree.svg), Kelti, CC BY-SA 4.0.*

This topic connects the logical world of relations to the implementation world of disks, flash storage, memory, and buffer managers. A database administrator can declare a table and write SQL without specifying exact record offsets, but a DBMS still chooses layouts and file organizations. Understanding those choices makes indexing, query processing, recovery, and transaction performance easier to reason about.

## Definitions

A **record** is the physical representation of one tuple. Fixed-length records reserve the same amount of space for every record. Variable-length records support attributes such as strings, nullable columns, and repeated or optional fields. A record often contains a header, null bitmap, fixed-length fields, and pointers or offsets to variable-length fields.

A **block** or **page** is the unit of transfer between disk and memory. Database systems commonly use pages such as 4 KiB, 8 KiB, or 16 KiB, though exact sizes vary. A page contains multiple records, page metadata, free space, and sometimes a slot directory that maps stable record identifiers to physical offsets inside the page.

A **file organization** determines how records of a relation are arranged. Common organizations include heap files, sequential files, hash files, and clustered organizations. A heap file places records wherever there is space. A sequential file keeps records ordered by a search key. A hash file uses a hash function to choose a bucket.

A **record identifier (RID)** points to a physical record, often as `(page_id, slot_number)`. A slot directory lets a record move inside a page without changing its RID, as long as the slot entry is updated.

A **buffer manager** manages the in-memory cache of disk pages. It decides which pages to read, which dirty pages to write back, and which pages to evict when memory is full. Replacement policies such as LRU are useful starting points, but database systems often need policies aware of scans, indexes, and recovery.

## Key results

The cost of I/O dominates many traditional database operations. Reading one page can bring many records into memory, so clustering related records matters. If a query scans a table, page count is more important than tuple count. If a query fetches scattered records through an index, random I/O can dominate.

Slotted pages solve variable-length record management. The page header stores the number of slots and free-space information. Records are placed from one end of the page, while the slot directory grows from the other. Deleting a record can mark a slot free; compacting the page can move records while keeping their slot numbers stable.

Free-space management is required for efficient insertion. The DBMS needs to find pages with enough room without scanning the whole file. Common methods include free lists, bitmaps, and directory pages that summarize free space by page.

Column-oriented storage stores values of the same attribute together, rather than storing all attributes of a tuple together. It is excellent for analytical scans over a few columns and for compression. Row-oriented storage is often better for transaction workloads that read or update whole records.

Physical layout choices interact with the buffer manager. A table scan benefits from sequential prefetch and may intentionally avoid polluting the cache with pages that will not be reused. An index lookup benefits from keeping upper index levels hot in memory. A nested-loop join may repeatedly touch the same inner pages, making replacement policy important. The same page count can therefore have different observed costs depending on access order and cache reuse.

Modern storage also changes, but does not remove, the need for careful design. Flash storage reduces random-read penalties compared with magnetic disks, yet write amplification, erase blocks, and endurance still matter. Main-memory databases avoid many disk I/O costs but still need cache-conscious layouts, logging, snapshots, and recovery. The abstraction of pages remains useful because data movement between storage layers is still a dominant systems concern.

Record layout affects CPU work as well as I/O. Fixed-width fields are easy to address by offset, while variable-width fields require an offset table or length decoding. Null bitmaps let the system represent missing values compactly, but every expression that reads nullable columns must check visibility and null state. Compression can reduce I/O and memory bandwidth, but it adds decompression cost. Physical design is therefore a balance among page density, CPU cost, and update flexibility.

Heap files are simple, but they still need organization around free space. If every insert scans pages looking for a gap, insertion becomes slow as the table grows. A free-space map lets the DBMS jump to a page likely to have enough room. When records grow after update, the system may relocate them, leave forwarding pointers, or reject the update if the layout cannot accommodate it efficiently.

## Visual

```text
+---------------- page ----------------+
| header: LSN, free pointer, slot count |
| slot 0 -> offset 760, length 42       |
| slot 1 -> offset 700, length 55       |
| slot 2 -> free                        |
|                free space             |
| record bytes grow from page end       |
+--------------------------------------+
RID = (page_id, slot_number)
```

| File organization | Strength | Weakness | Good fit |
| --- | --- | --- | --- |
| Heap | fast unordered inserts | slow search without index | staging tables, small tables |
| Sequential | efficient range scans | costly inserts unless space managed | ordered reports |
| Hash | fast equality lookup | poor range queries | key-value style access |
| Clustered | related rows near each other | expensive reorganization | joins and range-heavy tables |
| Column store | scans few columns, compresses well | tuple reconstruction cost | analytics and warehouses |

## Worked example 1: Estimate pages for fixed-length records

Problem: A table has fixed-length records of 160 bytes. The DBMS uses 8 KiB pages, with 192 bytes of page overhead. Estimate how many pages are needed for 100,000 records.

Method:

1. Convert page size:

$$
8\ \text{KiB} = 8192\ \text{bytes}
$$

2. Subtract page overhead:

$$
8192 - 192 = 8000\ \text{usable bytes}
$$

3. Compute records per page:

$$
\left\lfloor \frac{8000}{160} \right\rfloor = 50
$$

4. Compute required pages:

$$
\left\lceil \frac{100000}{50} \right\rceil = 2000
$$

5. Interpret the result. A full table scan reads about 2000 pages, not 100,000 separate records. If the storage layer can read pages sequentially, the scan may be much faster than 100,000 random reads.

Checked answer: 2,000 data pages are needed under these assumptions. The estimate ignores file headers, indexes, and partially filled pages, so it is a clean lower-level planning estimate rather than an exact storage bill.

## Worked example 2: Slotted-page deletion and insertion

Problem: A slotted page has three slots. Slot 0 points to record A, slot 1 points to record B, and slot 2 points to record C. Record B is deleted, then a new record D of the same size is inserted. Explain what happens to RIDs.

Method:

1. Before deletion:

   ```text
   slot 0 -> A
   slot 1 -> B
   slot 2 -> C
   ```

2. Delete B. The DBMS can mark slot 1 as free and mark B's bytes as reusable:

   ```text
   slot 0 -> A
   slot 1 -> free
   slot 2 -> C
   ```

3. Insert D. Since D has the same size, the DBMS may reuse the free space and slot 1:

   ```text
   slot 0 -> A
   slot 1 -> D
   slot 2 -> C
   ```

4. Check RIDs. A keeps `(page, 0)`. C keeps `(page, 2)`. D receives `(page, 1)`. The old RID for B should not be used by application code after deletion; if an index still points to it, that index entry must be removed or updated as part of the delete.

Checked answer: the slot directory gives stable identifiers for surviving records even if compaction moves bytes inside the page. Deleted RIDs can be reused internally, but transactional visibility and index maintenance must prevent stale references.

## Code

```python
from math import ceil

def pages_needed(record_count, record_size, page_size=8192, page_overhead=192):
    usable = page_size - page_overhead
    records_per_page = usable // record_size
    if records_per_page <= 0:
        raise ValueError("record does not fit on a page")
    return ceil(record_count / records_per_page), records_per_page

pages, capacity = pages_needed(100_000, 160)
print(f"records/page={capacity}, pages={pages}")
```

## Common pitfalls

- Estimating scan cost by tuple count instead of page count.
- Ignoring page overhead, slot directories, and free space when estimating capacity.
- Assuming variable-length records can be updated in place without consequences. Growing records may need forwarding or relocation.
- Confusing row-store and column-store strengths. Neither layout dominates for every workload.
- Forgetting that indexes also consume pages and must be maintained on writes.
- Treating the buffer manager as a generic operating-system cache. A DBMS has query and recovery knowledge that can guide replacement and flushing.

## Connections

- [Indexing with B+ Trees, Hashing, and Bitmaps](/cs/databases/indexing-bplus-hash-bitmap)
- [Query Processing and Join Algorithms](/cs/databases/query-processing-join-algorithms)
- [Recovery with WAL, ARIES, and Checkpoints](/cs/databases/recovery-wal-aries-checkpoints)
- [Transactions, ACID, and Serializability](/cs/databases/transactions-acid-and-serializability)
