---
title: MAC and Local Area Networks
sidebar_position: 3
---

# MAC and Local Area Networks

Local area networks solve a deceptively hard problem: many devices need to share a limited communication medium while still giving each host the illusion that it can send frames to another host. Peterson-Davie treat Ethernet and wireless LANs as concrete examples of a broader question: who may transmit next, and how does the system recover when two senders interfere [1]?

This page covers medium access control (MAC), Ethernet, switched LANs, VLANs, spanning tree, and Wi-Fi. The shared-medium ideas are old, but they still matter. Wi-Fi is shared radio. Data-center Ethernet uses switching rather than coaxial contention, but MAC addresses, VLAN tags, broadcast, loops, and queueing still shape operational behavior.

## Definitions

**Medium access control (MAC)** is the set of rules that decides how nodes share a broadcast or contention medium. A **collision** occurs when two transmissions overlap so the receiver cannot decode either one. A **collision domain** is the set of stations whose transmissions can collide. A **broadcast domain** is the set of stations that receive link-layer broadcasts.

**ALOHA** is a random-access protocol in which a node transmits when it has data and retries after a random delay if the frame is not acknowledged. **Slotted ALOHA** restricts transmissions to slot boundaries, doubling the maximum theoretical throughput compared with pure ALOHA. **CSMA** is carrier-sense multiple access: listen before transmitting. **CSMA/CD** adds collision detection, historically used by half-duplex Ethernet. **CSMA/CA** adds collision avoidance, used by Wi-Fi because radios usually cannot transmit and listen for collisions on the same channel at the same time.

An **Ethernet MAC address** is a 48-bit link-layer identifier, commonly written as six hexadecimal octets. A **switch** learns which MAC addresses appear on which ports by observing source addresses, then forwards known unicast frames only out the learned port. Unknown unicast, broadcast, and many multicast frames are flooded within the broadcast domain.

A **VLAN** is a logical LAN over shared physical switching infrastructure. IEEE 802.1Q inserts a tag containing a VLAN identifier into Ethernet frames, allowing one trunk link to carry multiple logical LANs [2]. The **spanning tree protocol (STP)** disables selected switch ports so the active topology is loop-free even when physical links contain redundancy [3]. Rapid spanning tree (RSTP) improves convergence.

**Wi-Fi** is the IEEE 802.11 family of wireless LAN standards [4]. Important generations include 802.11a/b/g, 802.11n, 802.11ac, and 802.11ax. Wi-Fi uses association, authentication, acknowledgments, retransmissions, rate adaptation, and CSMA/CA. **Hidden terminals** are stations that cannot hear each other but can both reach the access point. **RTS/CTS** reserves the medium to reduce hidden-terminal collisions.

## Key results

The first result is the ALOHA throughput bound. If frame attempts follow a Poisson process with offered load $G$, pure ALOHA succeeds when no other frame overlaps a vulnerable period of two frame times:

$$
S_{\mathrm{pure}} = G e^{-2G}
$$

The maximum occurs at $G = 1/2$, giving $S = 1/(2e) \approx 0.184$. Slotted ALOHA reduces the vulnerable period to one frame time:

$$
S_{\mathrm{slotted}} = G e^{-G}
$$

The maximum occurs at $G = 1$, giving $S = 1/e \approx 0.368$. Real LANs need better efficiency, which motivates carrier sensing, switching, scheduling, or smaller collision domains.

The second result is the Ethernet minimum frame constraint for collision detection. In half-duplex Ethernet, a sender must still be transmitting when a worst-case collision signal can return. Therefore the minimum frame transmission time must be at least twice the maximum propagation delay across the collision domain. This explains the classic Ethernet minimum frame size and collision-domain diameter restrictions. Full-duplex switched Ethernet removes collisions, but the frame format remains.

The third result is that switches are transparent but not magic. MAC learning creates forwarding state from data traffic, so hosts do not need to know the topology. However, unknown unicast flooding, broadcast ARP, and loops can still overload a LAN. Spanning tree prevents loops by turning a graph into a tree, but that sacrifices some path capacity. Modern data centers often replace large layer-2 trees with routed layer-3 fabrics or controlled overlays.

The fourth result is that VLANs separate broadcast domains but not automatically trust domains. A VLAN can isolate ARP, DHCP, and broadcast traffic for engineering, guest, voice, or storage networks. Security still requires correct trunk configuration, firewalling or routing policy between VLANs, DHCP snooping, dynamic ARP inspection, and careful native VLAN handling.

The fifth result is that Wi-Fi performance is governed by airtime rather than only nominal bit rate. A slow station consumes more airtime for the same payload, lowering aggregate capacity. Interference, retransmissions, management frames, contention backoff, and rate adaptation make delivered throughput lower than the advertised PHY rate.

The sixth result is that Bluetooth and ZigBee occupy different points in the design space. Bluetooth targets short-range personal-area connectivity and peripherals. ZigBee, built over IEEE 802.15.4, targets low-power sensor and control networks. Both remind us that "LAN" does not always mean high-throughput Ethernet.

A seventh result is that broadcast is expensive in both switched and wireless LANs. Ethernet switches must flood ARP requests, DHCP discovery, and unknown unicast frames across the relevant VLAN. Wi-Fi access points often transmit broadcast and multicast frames at low basic rates so all associated stations can decode them, consuming disproportionate airtime. Large flat layer-2 domains therefore suffer from control traffic, accidental loops, and noisy hosts. This is one reason operators segment networks with VLANs, route between segments, and suppress or proxy some discovery traffic.

An eighth result is that link-layer topology is partly a control-plane problem. A data frame can be forwarded based on a learned table, but the network still needs rules for root bridge election, port roles, VLAN membership, trunk negotiation, authentication, and failure recovery. STP and RSTP are distributed algorithms running inside the LAN. Wi-Fi association and roaming are also control-plane behaviors: the data frame format alone does not decide which AP should serve a client or when a client should move.

Finally, LAN performance is often limited by edge behavior rather than core bandwidth. A gigabit switch fabric does not help a Wi-Fi client stuck at a low modulation rate. A clean VLAN design does not help if a host floods broadcasts or a looped cable triggers a storm before control protocols converge. Good LAN engineering combines protocol knowledge with measurement: port counters, channel utilization, retransmission rates, spanning-tree state, and packet captures.

## Visual

```mermaid
graph TD
  H1["Host A"] --> S1["Switch 1"]
  H2["Host B"] --> S1
  S1 -- "trunk: VLAN 10,20" --> S2["Switch 2"]
  S2 --> H3["Host C"]
  S2 --> AP["Wi-Fi access point"]
  AP -. "CSMA/CA radio cell" .-> W1["Laptop"]
  AP -. "hidden from Laptop" .-> W2["Phone"]
  S1 -- "blocked by STP" -.-> S3["Switch 3"]
  S3 --> S2
```

| LAN technology | Access method | Typical issue | Common mitigation |
|---|---|---|---|
| Pure ALOHA | Random transmit | Many overlaps | Backoff, slots, or different MAC |
| Half-duplex Ethernet | CSMA/CD | Collisions and diameter limit | Switches and full duplex |
| Switched Ethernet | Point-to-point full duplex | Loops, broadcasts, flooding | STP/RSTP, VLANs, routing |
| Wi-Fi | CSMA/CA with ACKs | Hidden terminals and interference | RTS/CTS, channel planning, 802.11ax scheduling |
| Bluetooth | Frequency hopping | Coexistence and range | Adaptive hopping, low-power profiles |
| ZigBee | Low-power 802.15.4 MAC | Tiny frames and sleeping nodes | Mesh routing, duty cycling |

## Worked example 1: ALOHA throughput comparison

Problem: Compare pure ALOHA and slotted ALOHA when offered load is $G = 0.5$ frame attempts per frame time. Then compare their theoretical maxima.

1. Pure ALOHA at $G = 0.5$:

$$
\begin{aligned}
S_{\mathrm{pure}} &= G e^{-2G} \\
&= 0.5 e^{-1} \\
&\approx 0.5 \times 0.3679 \\
&= 0.184
\end{aligned}
$$

2. Slotted ALOHA at $G = 0.5$:

$$
\begin{aligned}
S_{\mathrm{slotted}} &= G e^{-G} \\
&= 0.5 e^{-0.5} \\
&\approx 0.5 \times 0.6065 \\
&= 0.303
\end{aligned}
$$

3. Pure ALOHA maximum:

$$
S_{\max} = 1/(2e) \approx 0.184
$$

4. Slotted ALOHA maximum:

$$
S_{\max} = 1/e \approx 0.368
$$

Answer: At $G = 0.5$, slotted ALOHA carries about 30.3 percent of one frame time as successful traffic, while pure ALOHA carries about 18.4 percent. Slotting doubles the best-case maximum because it halves the vulnerable period.

## Worked example 2: Learning-switch forwarding table

Problem: A switch has ports 1, 2, and 3. Host A is on port 1, B on port 2, and C on port 3. The switch starts with an empty table. Process these frames: A to B, B to A, C to A, A to C.

1. Frame A to B arrives on port 1. The switch learns `A -> 1`. B is unknown, so it floods out ports 2 and 3.

2. Frame B to A arrives on port 2. The switch learns `B -> 2`. A is known on port 1, so it forwards only to port 1.

3. Frame C to A arrives on port 3. The switch learns `C -> 3`. A is known on port 1, so it forwards only to port 1.

4. Frame A to C arrives on port 1. The source A refreshes `A -> 1`. C is known on port 3, so the switch forwards only to port 3.

Final table:

| MAC | Port |
|---|---:|
| A | 1 |
| B | 2 |
| C | 3 |

Answer: only the first frame is flooded. After the switch learns all three source locations, the later known unicast frames are filtered to a single egress port.

## Code

```python
class LearningSwitch:
    def __init__(self, ports):
        self.ports = set(ports)
        self.table = {}

    def forward(self, in_port, src, dst):
        self.table[src] = in_port
        if dst in self.table:
            out = {self.table[dst]}
        else:
            out = self.ports - {in_port}
        return sorted(out)

sw = LearningSwitch([1, 2, 3])
traffic = [(1, "A", "B"), (2, "B", "A"), (3, "C", "A"), (1, "A", "C")]
for frame in traffic:
    print(frame, "-> ports", sw.forward(*frame), "table", sw.table)
```

## Common pitfalls

- Confusing collision domains with broadcast domains. Switches break collision domains; VLANs and routers constrain broadcast domains.
- Assuming modern Ethernet still uses CSMA/CD on every link. Full-duplex switched Ethernet has no collisions.
- Forgetting why the Ethernet minimum frame size existed: collision detection needed a round-trip propagation bound.
- Treating MAC addresses as stable user identities. They identify link-layer interfaces and can be randomized or spoofed.
- Building redundant switch links without a loop-prevention or loop-control mechanism.
- Assuming STP uses all physical links. Some links are intentionally blocked to maintain a tree.
- Misconfiguring 802.1Q trunks and leaking VLANs across unintended switches.
- Treating VLANs as sufficient security boundaries without routing policy, filtering, and control-plane protections.
- Comparing Wi-Fi standards only by advertised PHY rate. Airtime, signal quality, channel width, and contention dominate user experience.
- Ignoring hidden terminals in Wi-Fi designs. Two clients may each hear the AP but not each other.
- Assuming RTS/CTS always improves performance. It adds overhead and helps mainly when hidden-terminal loss is significant.
- Forgetting that broadcast and multicast over Wi-Fi are often sent at conservative rates.
- Mixing low-power IoT networks with high-throughput LAN expectations.

## Connections

- [Physical and Data Link Layer](/cs/computer-networks/physical-and-data-link-layer) explains framing, CRCs, and ARQ beneath Ethernet and Wi-Fi.
- [Internetworking and IP Routing](/cs/computer-networks/internetworking-and-ip-routing) shows how ARP, IP, and routing cross LAN boundaries.
- [Modern Data Center Networks and SDN](/cs/computer-networks/modern-data-center-and-sdn) explains why large networks moved from spanning-tree LANs to leaf-spine fabrics and overlays.
- [Network Security and TLS](/cs/computer-networks/network-security-and-tls) includes VLAN security limits, spoofing, wireless security, and network access controls.
- [Cryptography](/cs/cryptography/intro) is needed for WPA, 802.1X, MACsec, and secure management.
- [Distributed Systems](/cs/distributed-systems/intro) depends on LAN behavior for leader election, membership, and service discovery.
- [Operating Systems](/cs/operating-systems/intro) explains NIC drivers, packet queues, interrupt moderation, and bridge implementations.
- [Computer Architecture](/cs/computer-architecture/intro) connects switch ASICs, CAM tables, and high-speed packet processing.

## References

[1] L. L. Peterson and B. S. Davie, *Computer Networks: A Systems Approach*, supplied edition, chs. 2-3.

[2] IEEE, "IEEE Standard for Local and metropolitan area networks: Bridges and Bridged Networks," IEEE Std 802.1Q.

[3] IEEE, "IEEE Standard for Local and metropolitan area networks: Media Access Control Bridges," IEEE Std 802.1D.

[4] IEEE, "IEEE Standard for Information Technology: Telecommunications and Information Exchange Between Systems, LAN/MAN Specific Requirements, Part 11: Wireless LAN MAC and PHY Specifications," IEEE Std 802.11.

[5] N. Abramson, "The ALOHA System: Another alternative for computer communications," in *Proc. AFIPS*, 1970.

[6] R. Metcalfe and D. Boggs, "Ethernet: Distributed packet switching for local computer networks," *Communications of the ACM*, vol. 19, no. 7, pp. 395-404, 1976.
