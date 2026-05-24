You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes for a new **Computer Networks** subject under `docs/cs/computer-networks/`.

## Inputs

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/computer-networks/`
- **SUPPLIED_TEXTBOOK**: `f:/coding/SJ Wiki/tmp/Computer Networks/Computer Networks, A Systems Approach - Larry Peterson, Bruce Davie.pdf` (Peterson & Davie, *Computer Networks: A Systems Approach*, 6th ed)
- **STYLE**: Topical chapter names (NOT paper titles). IEEE citations as `[N]`.

## Workflow

1. `pdfinfo` for page count, `pdftotext -l 30` for cover + TOC.
2. Iterate Peterson-Davie chapters, write topical pages.
3. Replace `intro.md` last.
4. Print summary.

## Produce

### 1. Replace `intro.md` (sidebar_position 0)
250-400 word overview + numbered list of all pages.

### 2. Create exactly 9 detail pages

| sidebar_position | filename | title |
|---|---|---|
| 1 | `foundations-and-layered-architecture.md` | Foundations and Layered Architecture |
| 2 | `physical-and-data-link-layer.md` | Physical and Data Link Layer |
| 3 | `mac-and-local-area-networks.md` | MAC and Local Area Networks |
| 4 | `internetworking-and-ip-routing.md` | Internetworking and IP Routing |
| 5 | `transport-layer-tcp-udp.md` | Transport Layer: TCP and UDP |
| 6 | `congestion-control-and-queue-management.md` | Congestion Control and Queue Management |
| 7 | `application-layer-and-naming.md` | Application Layer and Naming |
| 8 | `network-security-and-tls.md` | Network Security and TLS |
| 9 | `modern-data-center-and-sdn.md` | Modern Data Center Networks and SDN |

## Content scope (Peterson-Davie)

### 1 Foundations
- ISO/OSI and TCP/IP stacks, encapsulation, end-to-end argument, layering principles
- Performance: bandwidth, latency, BDP, throughput, jitter, packet loss
- Network requirements: scalability, reliability, performance, cost
- Protocol design principles, headers vs payload

### 2 Physical & Data Link
- Encoding (NRZ, NRZI, Manchester, 4B/5B), framing (HDLC, PPP, sentinel/length/clock-based)
- Error detection: parity, CRC, checksum
- Reliable transmission: stop-and-wait, sliding window (Go-Back-N, Selective Repeat)
- ARQ flavors

### 3 MAC and LANs
- Multi-access: ALOHA, CSMA/CD (Ethernet), CSMA/CA (Wi-Fi)
- Ethernet (10/100/1000/10G), MAC addresses, switching, VLANs (802.1Q), spanning tree (STP/RSTP)
- Wi-Fi 802.11 a/b/g/n/ac/ax, hidden terminal, RTS/CTS
- Bluetooth, ZigBee briefly

### 4 Internetworking
- IPv4 addressing, subnetting, CIDR, NAT, ICMP, ARP, DHCP
- IPv6 addressing, transition mechanisms, ICMPv6, NDP
- Routing: distance-vector (RIP), link-state (OSPF), path-vector (BGP); IS-IS
- Intra-domain vs inter-domain routing, BGP policy, route reflectors
- MPLS, segment routing

### 5 Transport
- UDP: datagram model, applications (DNS, DHCP, VoIP, RTP)
- TCP: connection setup (3-way handshake), state machine, reliable delivery, sequence/ACK numbers, flow control (sliding window)
- TCP variants: Reno, NewReno, SACK, CUBIC, BBR
- QUIC: UDP + TLS 1.3 + stream multiplexing + 0-RTT
- TCP options, MSS, PMTU discovery

### 6 Congestion Control & Queue Management
- AIMD, slow start, congestion avoidance, fast retransmit/recovery
- TCP throughput model (Mathis equation), congestion control as game
- AQM: RED, CoDel, FQ-CoDel
- ECN, DCTCP
- Bufferbloat

### 7 Application & Naming
- DNS: hierarchy, caching, DNSSEC, DoH/DoT
- HTTP/1.1, HTTP/2 (multiplexing), HTTP/3 (over QUIC)
- Email (SMTP, IMAP, POP3), FTP/SFTP, NFS
- WebSocket, gRPC, REST vs RPC
- CDNs, anycast, geo-DNS

### 8 Network Security & TLS
- Threat model in networking: eavesdropping, spoofing, MITM, DoS/DDoS
- Symmetric vs public-key crypto (cross-link cryptography), AEAD ciphers
- TLS 1.2 vs TLS 1.3 handshake, certificate chains, PKI, OCSP
- IPsec, VPNs (IKEv2), WireGuard
- Firewalls, IDS/IPS, Zero Trust
- DDoS mitigation, BGP hijacking and RPKI

### 9 Modern Data Center & SDN
- Clos / fat-tree topologies, ECMP, leaf-spine
- East-west vs north-south traffic
- Overlay networks: VXLAN, GENEVE
- SDN: OpenFlow, control / data plane separation, P4 programmable data planes
- Network function virtualization (NFV), service mesh (Envoy, Istio)
- RDMA over Converged Ethernet (RoCE), InfiniBand
- Programmable NICs (DPU/SmartNIC)
- Lossless networking, PFC, ECN-DCTCP for AI workloads

## Per-page format (mandatory — depth addendum applies)

1. Frontmatter (`title:`, `sidebar_position:`)
2. `# Title` H1
3. 1-2 opening paragraphs (motivation + scope)
4. (Optional but encouraged) 1-2 Wikimedia or paper figures with attribution
5. `## Definitions`
6. `## Key results` — protocols/algorithms/theorems with derivations
7. `## Visual` — **MANDATORY Mermaid diagram(s)** (protocol state machine, layered stack, network topology, TCP state diagram, BGP path-vector flow, TLS handshake sequence, SDN control/data plane, etc.)
8. `## Worked example 1` (numerical / by-hand: e.g., CRC computation, subnetting, TCP window evolution, BGP route selection)
9. `## Worked example 2`
10. `## Code` — Python: socket programming, simple TCP/UDP echo, BGP-style routing simulation, RED queue dynamics
11. `## Common pitfalls` — 10-15 items
12. `## Connections` — links to [Cryptography](/cs/cryptography/intro), [Distributed Systems](/cs/distributed-systems/intro), [Operating Systems](/cs/operating-systems/intro), [Computer Architecture](/cs/computer-architecture/intro)
13. `## References` — IEEE-style numbered list (Peterson-Davie chapter refs, RFC numbers — RFC 791 IP, RFC 793 TCP, RFC 1771 BGP, RFC 5246 TLS 1.2, RFC 8446 TLS 1.3, RFC 9000 QUIC, RFC 9293 TCP updated; plus key papers — Saltzer-Reed-Clark 1984 (end-to-end argument), Jacobson 1988 (TCP congestion control), Vegas/Reno/CUBIC papers)

## Word count

Each page: **2000-3500 words**.

## Visual policy

- **Mermaid mandatory** per page.
- Optional Wikimedia images (HEAD-verified): `OSI-model-Communication.svg`, `TCP_3way_handshake.svg`, `TCP_state_diagram_fixed.svg`, `IP_stack_connections.svg`, `IPv4_address_structure_and_writing_systems.svg` (skip if not confident), `BGP_route_advertisement.svg` (skip if not sure). Prefer to skip than fabricate.
- Skip arxiv figures (most networking is RFC, not arxiv).
- Caption: `*Figure: <desc>. Image: [Wikimedia Commons](file-url), Author, License.*`

## Constraints

- Stay inside `docs/cs/computer-networks/`. Do not touch `_category_.json`.
- No paper titles in filenames.
- Mermaid special chars in `"..."`; internal `"` → `#quot;`.
- Do not fabricate Wikimedia filenames or arxiv IDs.
- English. Match depth addendum.

## Output summary

```
Pages created: 1 intro + 9 detail = 10
Word counts per page
Figures: Wikimedia=W, Mermaid=M
References per page (avg)
```

Begin now.
