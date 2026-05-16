---
title: Computational Performance
sidebar_position: 15
---

# Computational Performance

Deep learning performance is not only about choosing a good model. D2L devotes a chapter to compilers, asynchronous execution, parallelism, multiple GPUs, and parameter servers because large models are systems as much as they are mathematics. A model that is theoretically reasonable can be unusable if data loading stalls, tensor transfers dominate runtime, or distributed workers communicate inefficiently.

The central performance question is where time and memory go. Computation happens in kernels, data moves across device boundaries, gradients synchronize across workers, and framework execution may be lazy or asynchronous. Good engineering overlaps work where possible, batches small operations into larger ones, keeps tensors on the right device, and uses parallelism only when communication costs justify it.

## Definitions

A **compiler** transforms code into a lower-level representation that may run faster. In deep learning frameworks, graph capture and compilation can fuse operations, remove overhead, and improve layout choices.

**Eager execution** runs operations immediately from Python. **Graph execution** captures a computation graph before running it. PyTorch 2 includes compilation tools such as `torch.compile`, while older discussions often refer to TorchScript or hybridization.

**Asynchronous execution** means a framework call can return to Python before the device finishes the operation. GPU kernels are commonly launched asynchronously, so timing requires synchronization.

**Data parallelism** replicates the model on multiple devices, splits a minibatch, computes gradients independently, and aggregates gradients before updating shared parameters.

**Model parallelism** splits one model across devices. It is used when a model or activation set does not fit on one device, but it introduces communication between layers or tensor partitions.

A **parameter server** is a distributed architecture where workers compute gradients and servers store and update parameters. D2L uses this to explain distributed training patterns and communication bottlenecks.

**Throughput** measures examples processed per second. **Latency** measures time for one request or batch. Training usually cares about throughput; interactive inference often cares about latency.

## Key results

Vectorization improves performance because large tensor operations amortize overhead and use optimized kernels. A Python loop over examples blocks the framework from using parallel hardware effectively. This is one reason D2L repeatedly writes batched code.

Timing GPU code requires synchronization. If a timer starts and stops around a kernel launch without `torch.cuda.synchronize()`, the measured time may only include launch overhead, not actual execution.

Parallel speedup is limited by the serial fraction and by communication. If a fraction $s$ of work is serial, Amdahl's law gives ideal speedup on $p$ workers as

$$
\mathrm{speedup} \le \frac{1}{s + \frac{1-s}{p}}.
$$

Even if computation parallelizes perfectly, gradient synchronization can dominate when the model has many parameters or the per-device batch is too small.

In synchronous data parallelism, each worker must wait for the others before the update. This gives consistent gradients but can suffer from stragglers. Asynchronous training can improve utilization, but gradients may be stale.

Input pipelines matter. If CPU preprocessing and disk reads are slower than GPU training steps, the GPU waits idle. DataLoader workers, pinned memory, caching, prefetching, and appropriate batch sizes can matter as much as model code.

Memory is often the limiting resource. Parameters, optimizer state, activations, gradients, and temporary buffers all consume memory. Adam stores extra moment tensors, so it uses more memory than plain SGD.

Performance work should start with measurement. A slow training job can be limited by the model, the input pipeline, synchronization, memory allocation, or logging. Looking only at wall-clock epoch time hides the cause. A useful breakdown separates data time, forward time, backward time, optimizer time, and evaluation time. D2L's emphasis on benchmarking small pieces reflects the same principle: optimize the bottleneck that actually exists.

Compilation and graph capture help most when the program contains many framework operations whose overhead or memory traffic can be reduced. Fusion can combine adjacent elementwise operations so tensors are read and written fewer times. It may help less when runtime is dominated by one already-optimized matrix multiplication or convolution. This is why compilation should be treated as a measured optimization, not a guaranteed speedup.

Mixed precision is another common performance tool, even though it must be used carefully. Lower-precision arithmetic can improve throughput and reduce memory, especially on accelerators with specialized tensor cores. Loss scaling may be needed to avoid underflow in gradients. The conceptual lesson matches D2L's systems discussion: numerical format, memory bandwidth, and hardware kernels interact with the mathematical model.

Distributed training also changes the meaning of a minibatch. With data parallelism across $p$ devices and per-device batch size $b$, the effective batch size is $pb$. If the learning rate schedule was tuned for batch size $b$, scaling to $pb$ may require warmup, learning-rate adjustment, or more epochs to reach the same number of parameter updates.

Memory-saving techniques trade computation for capacity. Gradient checkpointing discards some forward activations and recomputes them during the backward pass, reducing memory at the cost of extra compute. Accumulating gradients over several smaller minibatches can simulate a larger batch when one large batch does not fit, although normalization layers and optimizer step counts still need attention. These choices are part of model design once networks approach hardware limits.

Inference performance has a different objective from training performance. Training benefits from large batches and full backward graphs. Serving may need low latency, dynamic shapes, quantization, caching, or batching requests that arrive at different times. The same model can be excellent for offline batch scoring and poor for an interactive system if its latency or memory footprint is too high. D2L's performance principles apply to both, but the metric changes.

The simplest reliable performance habit is to change one variable at a time. Batch size, number of data workers, precision, compilation, and device count interact, so uncontrolled changes make timing results hard to interpret. Record throughput, memory use, and final validation quality together.

## Visual

```mermaid
flowchart LR
  D[Disk or dataset] --> W[DataLoader workers]
  W --> C[CPU preprocessing]
  C --> T[Transfer to GPU]
  T --> F[Forward kernels]
  F --> B[Backward kernels]
  B --> G[Gradient sync if multi-GPU]
  G --> O[Optimizer step]
  O --> F
```

| Bottleneck | Symptom | Typical fix |
|---|---|---|
| Python overhead | Many tiny ops, low GPU utilization | Vectorize or compile |
| Data loading | GPU idle between batches | More workers, cache, prefetch |
| Host-device transfer | Time spent moving tensors | Keep tensors on device, pinned memory |
| Kernel launch overhead | Tiny batches or many small kernels | Larger batches, fused operations |
| Communication | Multi-GPU speedup poor | Larger per-GPU batch, efficient all-reduce |
| Memory | Out-of-memory errors | Smaller batch, checkpointing, mixed precision |

## Worked example 1: Amdahl speedup limit

Problem: a training job spends $10\%$ of time in serial data preparation and $90\%$ in parallelizable computation. What is the maximum ideal speedup on $4$ workers?

Method:

1. Identify the serial fraction:

$$
s=0.10.
$$

2. The parallel fraction is

$$
1-s=0.90.
$$

3. Apply Amdahl's law:

$$
\mathrm{speedup}
\le
\frac{1}{s + \frac{1-s}{p}}
=
\frac{1}{0.10 + \frac{0.90}{4}}.
$$

4. Compute the denominator:

$$
0.10 + 0.225 = 0.325.
$$

5. Compute speedup:

$$
\frac{1}{0.325} \approx 3.08.
$$

Checked answer: even with perfect parallel compute, the job cannot exceed about $3.08$ times speedup on $4$ workers because of the serial component.

## Worked example 2: data-parallel gradient averaging

Problem: two GPUs process equal minibatch shards and compute scalar gradients $g_1=2$ and $g_2=6$ for the same parameter. What gradient should synchronous data parallelism apply for the full minibatch?

Method:

1. Since shard sizes are equal, average the gradients:

$$
g = \frac{g_1+g_2}{2}.
$$

2. Substitute:

$$
g = \frac{2+6}{2}=4.
$$

3. If the learning rate is $\eta=0.1$, the update is

$$
\theta \leftarrow \theta - 0.1(4).
$$

4. The parameter decreases by $0.4$.

Checked answer: the synchronized gradient is $4$. If shard sizes differ, use a weighted average by number of examples rather than a simple average.

## Code

```python
import time
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(2048, 2048, device=device)
w = torch.randn(2048, 2048, device=device)

def sync_if_needed():
    if device.type == "cuda":
        torch.cuda.synchronize()

# Warm up kernels and caches.
for _ in range(3):
    y = x @ w
sync_if_needed()

start = time.perf_counter()
for _ in range(10):
    y = x @ w
sync_if_needed()
elapsed = time.perf_counter() - start

print(f"device: {device}")
print(f"average matmul time: {elapsed / 10:.4f} seconds")
print("result norm:", y.norm().item())
```

## Common pitfalls

- Timing CUDA operations without synchronization.
- Moving tensors between CPU and GPU inside the inner training loop unnecessarily.
- Assuming more GPUs always improve throughput. Communication and small batches can erase gains.
- Letting data loading starve the accelerator.
- Using many small tensor operations where one batched operation would be clearer and faster.
- Forgetting optimizer-state memory when estimating how large a model or batch can fit.

## Connections

- [Optimization algorithms](/cs/deep-learning/optimization-algorithms)
- [PyTorch builders guide](/cs/deep-learning/pytorch-builders-guide)
- [Modern CNNs](/cs/deep-learning/modern-cnns)
- [Computer architecture](/cs/computer-architecture/)
- [Machine learning](/cs/machine-learning/)
