---
title: Warehouse-Scale Computers
sidebar_position: 15
---

# Warehouse-Scale Computers

Warehouse-scale computers, WSCs, treat a building full of servers, networking, power distribution, cooling, and storage as one large computer. They are built to serve Internet-scale workloads: search, storage, maps, machine learning services, streaming, social applications, and many independent user requests. H&P separates WSCs from traditional supercomputers because their goals and constraints differ.

A supercomputer often targets tightly coupled scientific jobs and expensive low-latency interconnects. A WSC targets request-level parallelism, data-level parallelism across huge datasets, operational cost, energy proportionality, fault tolerance, and software systems that survive component failures. The individual server matters, but the architecture of the whole facility matters more.

## When the warehouse is the computer

Request-level parallelism, RLP, is parallelism across independent or loosely coupled requests. A web service can handle many users at once because each request can often be assigned to a different server or process.

Warehouse-scale computer refers to the full system: servers, racks, networks, storage, power delivery, cooling, monitoring, deployment systems, and software frameworks. A cluster is a collection of connected machines; a WSC is a deliberately engineered datacenter-scale computer.

Energy proportionality is the ideal that a system's power consumption should scale linearly with load:

$$
P(u)=P_{idle}+u(P_{peak}-P_{idle})
$$

where $u$ is utilization. A perfectly energy-proportional system would have very low idle power. Real servers often consume a large fraction of peak power even when lightly loaded.

Power usage effectiveness, PUE, measures facility overhead:

$$
\mathrm{PUE}=
\frac{\mathrm{Total\ facility\ power}}{\mathrm{IT\ equipment\ power}}
$$

Lower PUE means less power is spent on cooling, conversion losses, and other non-compute infrastructure.

Service-level objectives, SLOs, specify latency, availability, or throughput targets. Tail latency is the high-percentile response time, such as 99th percentile latency. It matters because a user-visible request may depend on many subrequests; one slow component can delay the whole response.

## Coordinating services across racks

The load balancers, service racks, storage, monitoring, and deployment systems form a feedback loop. Monitoring detects failures and load changes; scheduling and deployment then alter where work runs.

```mermaid
flowchart TD
    U[Users] --> LB[Load balancers]
    LB --> R1[Rack 1 services]
    LB --> R2[Rack 2 services]
    LB --> R3[Rack 3 services]
    R1 --> S[Distributed storage]
    R2 --> S
    R3 --> S
    S --> M[Monitoring and repair]
    M --> D[Deployment and scheduling]
    D --> R1
    D --> R2
    D --> R3
```

| Metric | Meaning | Why architects care |
|---|---|---|
| Requests/s | Service throughput | Capacity planning |
| Median latency | Typical response | User experience baseline |
| 99th percentile latency | Tail behavior | Multi-service requests amplify tails |
| PUE | Facility efficiency | Power and cooling overhead |
| Utilization | Fraction of useful work | Low utilization wastes capital and power |
| Availability | Service accomplishment | Failures are routine at scale |

## Cost, latency, and failure at fleet scale

WSC design is dominated by total cost of ownership. Server purchase price, power, cooling, networking, building infrastructure, repair, and replacement cycles all matter. A small percentage improvement in energy efficiency or utilization can be worth a large absolute amount because it applies to thousands of servers.

RLP changes the performance metric. A single request's latency matters, but the system must also maximize useful throughput under latency constraints. If throughput rises only by violating tail-latency SLOs, it is not a valid improvement.

Fault tolerance is mandatory. At WSC scale, hardware failures are normal events. Software must replicate data, retry tasks, route around failures, and deploy changes gradually. The architecture assumes components fail and designs for service continuity.

Networking is part of architecture. Oversubscription, rack locality, bisection bandwidth, and congestion affect application placement. A data-intensive job that repeatedly crosses racks can be slower and more expensive than one scheduled near its data.

WSC workloads often mix online services and batch analytics. Online services need predictable latency. Batch systems want high throughput and can use spare capacity. Coordinating these workloads is a scheduling and isolation problem.

Tail latency is amplified by fan-out. A front-end request may query dozens or hundreds of back-end shards, then wait for the slowest required response. Even if each shard is fast most of the time, the probability that at least one shard is slow can be high. WSC software therefore uses replication, hedged requests, timeouts, partial results, and careful dependency graphs to control the tail.

Utilization is a cost problem as much as a performance problem. Servers bought for peak traffic sit partly idle during low demand, yet they still consume power and occupy capital. Workload consolidation improves utilization but can create interference in caches, memory bandwidth, storage, and networks. Isolation mechanisms and cluster schedulers try to pack work while preserving SLOs.

The network topology affects application architecture. Placing related services or data shards in the same rack can reduce latency and cross-rack traffic, but it may reduce fault isolation. Spreading replicas across failure domains improves availability but increases network distance. WSC design repeatedly balances locality, redundancy, and operational simplicity.

WSC dependability is usually achieved above individual hardware components. Instead of making every server extremely reliable, designers often use commodity servers with software replication and automatic recovery. This shifts complexity into distributed systems, monitoring, and deployment, but it can produce better cost-performance and faster hardware refresh cycles.

## Converting PUE into megawatts

A datacenter has 20 MW of IT load and a PUE of 1.25. Total facility power follows directly from the definition:

$$
\mathrm{Total}=\mathrm{PUE}\times \mathrm{IT}
$$

At the original PUE, total power is:

$$
1.25 \times 20\ \mathrm{MW}=25\ \mathrm{MW}
$$

The non-IT overhead is:

$$
25-20=5\ \mathrm{MW}
$$

Reducing PUE to 1.15 at the same IT load changes total power to:

$$
1.15 \times 20\ \mathrm{MW}=23\ \mathrm{MW}
$$

The new overhead is:

$$
23-20=3\ \mathrm{MW}
$$

The continuous saving is:

$$
25-23=2\ \mathrm{MW}
$$

Over a year, the 2 MW reduction becomes:

$$
2\ \mathrm{MW}\times8760\ \mathrm{h}=17520\ \mathrm{MWh}
$$

## Why p99 latency compounds under fan-out

A user request fans out to 50 independent backend services and waits for all of them. Each backend meets a local 99th-percentile target of 100 ms, so each has a 1% chance of exceeding 100 ms. The probability that one backend stays within the target is:

$$
1-0.01=0.99
$$

Assuming independence, the probability that all 50 stay within the target is:

$$
0.99^{50}=0.605
$$

The complementary event is that at least one backend exceeds 100 ms:

$$
1-0.605=0.395
$$

There is about a 39.5% chance that at least one backend exceeds 100 ms, even though each service has only a 1% tail probability. WSC software uses hedged requests, careful fan-out control, caching, and tail-tolerant designs to contain that amplification.

## Back-of-the-envelope fleet calculations

```python
def facility_power(it_mw, pue):
    total = it_mw * pue
    overhead = total - it_mw
    return total, overhead

def fanout_tail_probability(backends, per_backend_tail):
    all_fast = (1.0 - per_backend_tail) ** backends
    return 1.0 - all_fast

total, overhead = facility_power(20, 1.25)
print(f"total={total:.1f} MW overhead={overhead:.1f} MW")
print(f"tail risk={fanout_tail_probability(50, 0.01):.1%}")
```

The PUE calculation isolates facility overhead, but server efficiency still matters inside the IT load. A low PUE datacenter full of inefficient servers can waste more energy than a higher-PUE facility with better utilization and newer hardware. Architects therefore combine facility metrics with server-level performance per watt, workload placement, and power management policies.

The tail-probability function assumes independent back-end delays. Real delays are often correlated because many services share networks, storage systems, power events, software releases, or overloaded dependencies. Correlation can make tail behavior worse than the independent estimate. Monitoring systems therefore track both per-service latency and fleet-wide events.

Capacity planning also needs headroom. Running close to saturation increases queueing delay and leaves little room for failures or traffic bursts. WSC operators often reserve capacity for maintenance, machine failures, and sudden demand. The unused headroom looks inefficient in a narrow utilization chart, but it is part of meeting availability and latency objectives.

Software deployment is another architectural workload. Rolling out a new binary to thousands of machines can create cache cold starts, load shifts, and correlated failures if done carelessly. Staged rollout, canaries, automatic rollback, and version skew handling are part of making the warehouse behave like a dependable computer rather than a collection of individually managed servers.

The same systems view applies to hardware refresh. Replacing servers gradually means several generations of processors, disks, and network cards may run one service at the same time. Software must tolerate heterogeneity, and capacity models must account for mixed performance instead of assuming every machine is identical.

Even naming, inventory, and monitoring data become architectural inputs at this scale for daily service operation.

## Errors in fleet-level reasoning

A WSC is not a larger supercomputer: request-level parallelism, commodity failure modes, energy, and service continuity lead to different design choices. Average latency can hide a poor tail, and throughput numbers are incomplete without the SLO under which they were measured.

Idle power and weak energy proportionality matter even when peak efficiency looks good. Hardware failures must be treated as routine operating conditions. Data placement belongs in the same analysis: repeatedly moving a large dataset across the network may cost more than scheduling computation near the data.

<div className="see-also">

See also: [Power, Energy, Cost, and Dependability](/cs/computer-architecture/power-energy-cost-dependability) · [Multicore, Synchronization, and NUMA](/cs/computer-architecture/multicore-synchronization-numa) · [Storage, RAID, and SSDs](/cs/computer-architecture/storage-raid-ssds) · [Vector, SIMD, and GPU Architectures](/cs/computer-architecture/vector-simd-gpu)

</div>
