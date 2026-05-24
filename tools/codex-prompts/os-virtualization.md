You are adding ONE new chapter to the existing **Operating Systems** section.

## Inputs

- **OUTPUT FILE**: `f:/coding/SJ Wiki/docs/cs/operating-systems/virtualization.md`
- **SOURCE TEXTBOOK**: `f:/coding/SJ Wiki/tmp/Operating System/Advanced Systems Format, Virtualization Machines - James E. Smith, Ravi Nair.pdf` (Smith-Nair, *Virtual Machines: Versatile Platforms for Systems and Processes*)
- Cross-reference: Bovet-Cesati *Understanding the Linux Kernel*, Love *Linux Kernel Development*, Tanenbaum-Bos *Modern Operating Systems*, Arpaci-Dusseau OSTEP — for context.
- **STYLE**: Topical chapter name. IEEE inline citations `[N]`.

## Page metadata

```yaml
---
title: Virtualization
sidebar_position: 14
---
```

Place after `linux-case-study.md` (or wherever logical based on existing positions). Existing OS pages cover overview, processes, threads, scheduling, sync, deadlocks, memory, VM, file systems, IO, mass storage, protection, security, linux-case-study. This new page covers the virtualization layer beneath the OS.

## Content scope (~2500-3500 words)

### Definitions
- Process VM (e.g., JVM, .NET CLR) vs System VM (e.g., VMware, KVM, Xen)
- Host vs guest; virtual machine monitor (VMM) / hypervisor
- Type 1 (bare metal: Xen, ESXi, Hyper-V) vs Type 2 (hosted: VMware Workstation, VirtualBox, QEMU)
- Full virtualization, paravirtualization, hardware-assisted virtualization
- Popek-Goldberg requirements (1974): equivalence, resource control, efficiency; trap-and-emulate classification of instructions

### CPU virtualization
- Classical trap-and-emulate; problems with x86 (17 non-virtualizable instructions in pre-VT-x era)
- Binary translation (VMware) vs paravirtualization (Xen hypercalls) vs hardware-assisted (Intel VT-x VMX root/non-root, AMD-V SVM)
- Privilege rings; VMX root/non-root distinction
- World switches: VMENTRY / VMEXIT, VMCS state
- Nested virtualization

### Memory virtualization
- Shadow page tables (legacy software approach)
- Extended Page Tables (EPT, Intel) / Nested Page Tables (NPT, AMD): two-level translation guest-virtual → guest-physical → host-physical
- Memory ballooning, page sharing (Transparent Page Sharing, KSM), compression
- IOMMU (Intel VT-d, AMD-Vi): DMA remapping, interrupt remapping
- PCI passthrough, SR-IOV

### I/O virtualization
- Emulated devices, paravirtualized devices (virtio, Xen frontend/backend split drivers)
- Direct assignment (passthrough) via IOMMU
- SR-IOV virtual functions, GPU virtualization (NVIDIA vGPU, GVT-g)
- Networking: virtual switches (Open vSwitch), VXLAN overlays, virtio-net + vhost
- Storage: virtio-blk, virtio-scsi, paravirtualized storage

### Containers
- Containers vs full VMs: namespaces, cgroups, no separate kernel
- Docker, containerd, runc, CRI-O
- Container security: capabilities, seccomp, AppArmor/SELinux
- Container orchestration (Kubernetes) — brief reference
- LXC, OpenVZ history

### Hypervisor architectures
- KVM (Linux kernel module) + QEMU userspace
- Xen split: dom0 control + domU guests
- VMware ESXi VMM design
- Microsoft Hyper-V parent partition / child partitions
- Microhypervisors (NOVA, seL4); formal verification frontier

### Performance
- VMEXIT cost (cycles), TLB flushing, IPI cost
- Steal time, NUMA awareness, vCPU pinning
- Live migration: pre-copy (VMware vMotion, KVM), post-copy
- Checkpoint / restore (CRIU for containers)

### Modern context
- AWS Nitro, Firecracker microVM (used by AWS Lambda)
- gVisor (user-space kernel for sandboxing)
- Confidential computing: SEV/SEV-ES/SEV-SNP, Intel TDX, Arm CCA
- Unikernels (MirageOS, IncludeOS)

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter
2. `# Virtualization` H1
3. 1-2 opening paragraphs (motivation: consolidation, isolation, cloud)
4. (Optional) 1 Wikimedia image — `Hypervisor.svg` (verify), `Hardware_Virtualization_(copy).svg` (skip if unsure)
5. `## Definitions`
6. `## Key results` — Popek-Goldberg, EPT/NPT, virtio, IOMMU
7. `## Visual` — **MANDATORY Mermaid** showing Type 1 vs Type 2 hypervisor stacks, VM lifecycle (VMENTRY/VMEXIT), nested paging two-level translation
8. `## Worked example 1` — Popek-Goldberg classification: classify a small set of instructions (mov, popf, mov-cr3, hlt) as privileged / sensitive / non-virtualizable
9. `## Worked example 2` — nested paging address translation: walk a guest virtual address through guest and host page tables
10. `## Code` — Python pseudo-code: a 2-level shadow page table; a virtio-style ring buffer
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — links to existing OS pages: [Virtual Memory](/cs/operating-systems/virtual-memory), [Processes](/cs/operating-systems/processes), [Security](/cs/operating-systems/security), [Linux Case Study](/cs/operating-systems/linux-case-study); also [Computer Architecture](/cs/computer-architecture/intro), [Distributed Systems](/cs/distributed-systems/intro)
13. `## References` — IEEE-style (Smith-Nair textbook; Popek-Goldberg 1974 *CACM*; Bugnion et al. 1997 Disco; Barham et al. 2003 Xen; Adams-Agesen 2006 VMware comparison; Kivity et al. 2007 KVM; Belay et al. 2017 IX; Manco et al. 2017 Unikernels; Agache et al. 2020 Firecracker NSDI)

## Constraints

- Stay inside `docs/cs/operating-systems/`.
- Only create `virtualization.md`.
- No paper titles in filenames.
- Mermaid special chars in `"..."`; internal `"` → `#quot;`.
- English. Match depth addendum.

## Output summary

```
File: virtualization.md
Word count: <N>
Figures: Wikimedia=W, Mermaid=M
References: <r>
```

Begin now.
