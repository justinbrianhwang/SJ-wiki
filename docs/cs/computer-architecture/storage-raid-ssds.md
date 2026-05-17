---
title: Storage, RAID, and SSDs
sidebar_position: 16
---

# Storage, RAID, and SSDs

Storage systems sit below memory hierarchy but strongly affect whole-system performance and dependability. Databases, file servers, virtual machines, WSCs, and scientific workflows often wait on persistent storage. H&P's storage appendix treats I/O performance and reliability quantitatively, especially through RAID and queueing ideas.

![An ENIAC installation shows early computer architecture as cabinets, switches, and wiring.](https://commons.wikimedia.org/wiki/Special:FilePath/ENIAC_Penn1.jpg)

*Figure: ENIAC gives architecture pages a physical reference point before modern chips. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ENIAC_Penn1.jpg), Paul W. Shaffer and TexasDex, CC BY-SA 3.0/GFDL.*

Architecturally, storage is different from cache and DRAM because persistence, failure recovery, and service time variation matter. A disk access includes mechanical seek and rotation. An SSD avoids mechanical delay but has erase-before-write behavior, limited write endurance, internal parallelism, and controller-managed flash translation. RAID combines multiple devices to improve performance, capacity, and dependability.

## Definitions

Disk service time is commonly decomposed as:

$$
T_{disk}=T_{seek}+T_{rotation}+T_{transfer}+T_{controller}
$$

Average rotational latency for a disk spinning at RPM revolutions per minute is:

$$
T_{rotation,avg}=\frac{1}{2}\times\frac{60}{\mathrm{RPM}}
$$

RAID, redundant array of independent disks, organizes multiple drives as one logical storage system:

- RAID 0 stripes data without redundancy.
- RAID 1 mirrors data.
- RAID 4 uses block-level striping with a dedicated parity disk.
- RAID 5 distributes parity across disks.
- RAID 6 uses two independent parity values to tolerate two drive failures.

For parity RAID, the small-write penalty is important. Updating one block in RAID 5 often requires reading old data and old parity, then writing new data and new parity: four I/O operations. Full-stripe writes can be much more efficient because parity is computed from all new data.

An SSD stores data in flash pages but erases larger blocks. The flash translation layer, FTL, maps logical block addresses to physical flash locations, performs wear leveling, garbage collection, and bad-block management.

Queueing matters when requests arrive faster than a device can serve them. For an M/M/1 queue with arrival rate $\lambda$ and service rate $\mu$, utilization is:

$$
\rho=\frac{\lambda}{\mu}
$$

and average response time is:

$$
T=\frac{1}{\mu-\lambda}
$$

This simple formula shows why latency grows sharply as utilization approaches 100%.

## Key results

RAID trades capacity, performance, and reliability. RAID 0 improves bandwidth but makes reliability worse because any drive failure loses the array. RAID 1 halves usable capacity but can improve read throughput and survive one drive failure per mirror pair. RAID 5 has efficient capacity but poor small-write behavior and vulnerability during rebuild. RAID 6 spends more capacity on parity but protects against a second failure during rebuild.

Availability depends on repair time as well as failure rate. Large arrays rebuild slowly, and rebuild traffic can reduce foreground performance. During rebuild, the array may be exposed to additional failures. This is why stronger redundancy and scrubbing become more important as device capacity grows.

SSDs reduce random-read latency dramatically compared with disks, but they are not simply faster disks. Sequential bandwidth, random write amplification, garbage collection pauses, endurance, and controller parallelism matter. TRIM and overprovisioning help the SSD maintain free blocks and reduce write amplification.

Storage benchmarks must specify request size, read/write mix, sequential versus random access, queue depth, working set, durability settings, and failure mode. A result that looks excellent for sequential reads may say little about synchronous small writes.

Queue depth changes the interpretation of latency and throughput. A single synchronous request to a disk sees seek and rotation directly. Many outstanding requests let the device reorder work, combine operations, and keep internal resources busy, increasing throughput but also increasing waiting time. SSDs also benefit from parallelism across channels and dies, so a benchmark at queue depth one may understate peak throughput while still representing latency-sensitive applications.

Durability semantics are part of performance. A write acknowledged after reaching a volatile cache is much faster than a write acknowledged only after persistent media or protected nonvolatile cache. Databases and file systems use flushes, barriers, journaling, and checksums because losing or reordering writes can corrupt state. Storage architecture must state exactly when data is durable.

RAID rebuild is a stress case, not a background detail. Reconstructing a failed drive reads large amounts of surviving data and writes replacement data, reducing foreground performance and exposing latent sector errors. Larger drives increase rebuild time, which increases the window for a second failure. RAID 6 and erasure-coded storage address this by tolerating more failures, but they add parity computation and repair traffic.

SSDs introduce write amplification. Updating a small logical block may require writing new flash pages, copying still-live data from an erase block, and erasing old blocks later. Overprovisioning, wear leveling, and TRIM reduce the effect, but workloads with random synchronous writes can still behave very differently from sequential write streams.

## Visual

```text
RAID 5 distributed parity across four disks

Stripe 0:  D0   D1   D2   P0
Stripe 1:  D3   D4   P1   D5
Stripe 2:  D6   P2   D7   D8
Stripe 3:  P3   D9   D10  D11
```

| Level | Usable capacity with N drives | Fault tolerance | Read performance | Write concern |
|---|---:|---|---|---|
| RAID 0 | $N$ drives | None | High | Any failure loses data |
| RAID 1 | $N/2$ drives | One per mirror pair | Good | Duplicate writes |
| RAID 5 | $N-1$ drives | One drive | Good | Small-write parity penalty |
| RAID 6 | $N-2$ drives | Two drives | Good | Higher parity cost |
| Erasure coding | Configurable | Configurable | Good for large objects | CPU and repair traffic |

## Worked example 1: Disk access time

Problem: A disk has average seek time 4 ms, spins at 7200 RPM, transfers at 160 MB/s, and has 0.2 ms controller overhead. Estimate service time for a 64 KiB read.

Method:

1. Average rotational latency:

$$
\begin{aligned}
T_{rotation}
&= \frac{1}{2}\times\frac{60}{7200}\ \mathrm{s} \\
&= 0.004167\ \mathrm{s} \\
&= 4.167\ \mathrm{ms}
\end{aligned}
$$

2. Transfer time. Use $64\ \mathrm{KiB}=65536$ bytes and $160\ \mathrm{MB/s}\approx160000000$ bytes/s.

$$
\begin{aligned}
T_{transfer}
&= \frac{65536}{160000000}\ \mathrm{s} \\
&= 0.0004096\ \mathrm{s} \\
&= 0.410\ \mathrm{ms}
\end{aligned}
$$

3. Sum components.

$$
\begin{aligned}
T_{disk}
&=4+4.167+0.410+0.2 \\
&=8.777\ \mathrm{ms}
\end{aligned}
$$

Checked answer: The estimated service time is about 8.78 ms. Seek and rotation dominate this small random read; transfer time is a minor part.

## Worked example 2: RAID 5 capacity and small-write penalty

Problem: A RAID 5 array has 8 drives of 12 TB each. Compute usable capacity. Then estimate backend I/O operations for 10,000 small random logical writes using read-modify-write parity updates.

Method:

1. RAID 5 usable capacity:

$$
(N-1)\times \mathrm{drive\ capacity}
$$

2. Substitute values.

$$
(8-1)\times12\ \mathrm{TB}=84\ \mathrm{TB}
$$

3. Small-write parity update operations. Each logical write needs:

- read old data,
- read old parity,
- write new data,
- write new parity.

So the write penalty is 4 backend I/Os per logical write.

4. Compute backend I/Os.

$$
10000 \times 4 = 40000
$$

Checked answer: Usable capacity is 84 TB, and 10,000 small writes can require about 40,000 backend I/O operations. Full-stripe writes can avoid much of this penalty.

## Code

```python
def avg_rotational_latency_ms(rpm):
    return 0.5 * 60_000 / rpm

def disk_service_ms(seek_ms, rpm, transfer_bytes, bandwidth_bytes_s, controller_ms):
    rotation_ms = avg_rotational_latency_ms(rpm)
    transfer_ms = 1000 * transfer_bytes / bandwidth_bytes_s
    return seek_ms + rotation_ms + transfer_ms + controller_ms

def raid5_capacity(drives, capacity_tb):
    return (drives - 1) * capacity_tb

print(f"disk service={disk_service_ms(4, 7200, 64*1024, 160_000_000, 0.2):.3f} ms")
print(f"RAID5 usable={raid5_capacity(8, 12)} TB")
```

The service-time function models one isolated request. Under load, requests wait in a queue before service begins. As utilization approaches one, the waiting component can exceed seek and transfer time. This is why storage systems are often provisioned for latency at moderate utilization rather than driven continuously at the theoretical maximum throughput.

The RAID capacity function also hides rebuild and spare policies. Arrays may reserve hot spares, use declustered parity, or distribute erasure-coded fragments across racks. These choices reduce usable capacity but improve repair parallelism and availability. In WSC storage, the logical design may resemble RAID at a high level while being implemented by distributed software instead of one hardware controller.

For SSDs, the comparable model would include read latency, program latency, erase latency, write amplification, and internal parallelism. A random write workload can trigger garbage collection that changes latency over time. Good SSD benchmarks therefore include warm-up, steady-state measurement, and percentile latency rather than only average throughput.

Storage performance also depends on the software path. System calls, file-system metadata, journaling mode, block-layer scheduling, device drivers, and network storage protocols can add latency before a request reaches media. Architecture-level comparisons should say whether they measure raw device behavior or application-visible I/O.

## Common pitfalls

- Comparing disks using only transfer bandwidth while ignoring seek and rotation.
- Comparing SSDs and disks without specifying random versus sequential workload.
- Treating RAID as backup; RAID improves availability but does not protect against deletion, corruption, or site loss.
- Ignoring rebuild time and degraded-mode performance.
- Measuring storage at low queue depth when the real workload uses high concurrency, or the reverse.
- Forgetting parity write penalties for small random writes.

## Connections

- [Power, Energy, Cost, and Dependability](/cs/computer-architecture/power-energy-cost-dependability)
- [Warehouse-Scale Computers](/cs/computer-architecture/warehouse-scale-computers)
- [Virtual Memory, TLBs, and VMs](/cs/computer-architecture/virtual-memory-tlb-vms)
- [Cache Organization and AMAT](/cs/computer-architecture/cache-organization-amat)
