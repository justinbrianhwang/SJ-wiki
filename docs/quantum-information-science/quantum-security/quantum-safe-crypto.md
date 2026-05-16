---
title: Quantum-Safe Cryptography (Migration)
sidebar_position: 3
---

# Quantum-Safe Cryptography (Migration)

Quantum-safe cryptography is the engineering program that moves deployed systems away from quantum-vulnerable public-key cryptography. It is broader than choosing a new algorithm. Real systems contain TLS endpoints, VPNs, SSH, package signing, firmware signatures, document signatures, hardware security modules, certificate authorities, backup encryption, identity systems, smart cards, and embedded devices. A migration succeeds only when those uses are inventoried, prioritized, upgraded, monitored, and kept agile enough to change again if standards or attacks evolve.

The practical goal is not to panic about every cryptographic primitive. The goal is to identify where RSA, Diffie-Hellman, ECDH, DSA, ECDSA, and EdDSA are used for key establishment or signatures, then replace those uses with standardized post-quantum or hybrid constructions. Symmetric cryptography usually needs parameter review, such as preferring 256-bit keys for long-lived confidentiality, but the main operational burden is public-key migration.

## Definitions

**Quantum-safe cryptography** means cryptographic deployment that is intended to remain secure in the presence of known quantum attacks. In practice this usually means PQC for public-key functions, adequate symmetric key lengths, and protocols that can negotiate or rotate algorithms without redesign.

**Crypto agility** is the ability to replace cryptographic algorithms, parameter sets, encodings, and trust anchors without rewriting the whole system. It requires version negotiation, length-flexible encodings, policy controls, telemetry, test vectors, staged rollout, and a way to revoke or disable algorithms. Agility is not an excuse to keep weak algorithms forever; it is the mechanism that lets a system leave them.

A **hybrid key establishment** combines a classical mechanism and a post-quantum mechanism. A common TLS-style example combines X25519 with Kyber768 or ML-KEM-768. The shared traffic secret is derived from both component secrets. The intended security intuition is that an attacker must break both the classical and post-quantum component, or break the combiner, to recover the final secret. Formal details depend on the exact protocol draft and combiner.

A **cryptographic inventory** is a structured list of where cryptography is used. It should record the primitive, parameter set, protocol, library or service boundary, owner, data protected, confidentiality lifetime, authentication lifetime, exposure, replacement difficulty, and whether the use is negotiated or hard-coded. Without an inventory, migration becomes guesswork.

A **migration priority** is a risk-based ordering. Public endpoints carrying long-lived confidential data usually rank high. So do code-signing roots, firmware-signing keys, certificate authorities, and hardware roots of trust because their failure can compromise many downstream systems. Low-value, short-lived, easy-to-upgrade traffic usually ranks lower.

A **harvest-now, decrypt-later** risk exists when an attacker can record protected data now and decrypt it later after a quantum break. It is mainly a confidentiality problem for key establishment. Signature migration has a related but different problem: old signatures and old trust roots may remain accepted after their algorithms become forgeable.

The standards snapshot for this page is May 16, 2026. NIST's final first-wave PQC standards are FIPS 203 for ML-KEM, FIPS 204 for ML-DSA, and FIPS 205 for SLH-DSA, all approved on August 13, 2024. HQC was selected in March 2025 for future KEM standardization. Falcon/FN-DSA is planned as FIPS 206 but is still in development in the latest NIST material checked for this page.

## Key results

The first migration result is that **inventory precedes replacement**. A system owner must know where quantum-vulnerable algorithms are used before choosing a deployment order. TLS certificates are visible, but many important uses are not: S/MIME, JWT signing, database client certificates, package repositories, update manifests, secure boot, backups, device enrollment, manufacturing certificates, VPN appliances, SSH host keys, and custom protocols.

The second result is that **hybrid deployment reduces transition risk**. A hybrid such as X25519 plus ML-KEM-768 can keep the classical security properties operators already rely on while adding protection against future quantum attacks. If the PQC component later suffers a classical break, the classical component still protects against ordinary attackers. If a future quantum computer breaks X25519, the PQC component is intended to preserve confidentiality. This "both must fail" intuition is powerful, but it depends on correct protocol design.

Large providers tested this path before final standards settled. AWS announced hybrid post-quantum TLS for connections to KMS and ACM in 2022. Cloudflare deployed hybrid post-quantum key agreement for TLS 1.3 at large scale, with public documentation noting support across websites and APIs served through its network. Google and Chromium rolled out X25519Kyber768 experimentation in 2023 and enabled a Kyber draft by default for TLS 1.3 and QUIC on desktop Chrome in 2024, later moving toward ML-KEM naming and final-standard alignment. These deployments should be read as ecosystem migration evidence, not as a blanket claim that every implementation or configuration is secure.

The third result is that **sizes matter**. A classical X25519 key share is 32 bytes. ML-KEM-768 has an encapsulation key of 1184 bytes and a ciphertext of 1088 bytes. Hybrid TLS key establishment therefore adds roughly a couple of kilobytes to the handshake. That is often acceptable, but it can expose packet fragmentation, middlebox limits, hardware parser assumptions, and latency sensitivity. Signatures are often more disruptive: ML-DSA signatures are several kilobytes, while SLH-DSA signatures range from roughly 8 KB to roughly 50 KB depending on parameter set. Certificate chains, transparency logs, constrained links, and firmware update formats must be tested with real sizes.

The fourth result is that **timelines are policy and risk tools, not physical predictions**. NSA's CNSA 2.0 guidance for U.S. National Security Systems targets completion of the quantum-resistant transition by 2035, with earlier milestones for some systems and use cases. NIST's transition planning similarly points to deprecating and ultimately disallowing quantum-vulnerable public-key algorithms in federal standards by 2035, with high-risk systems moving earlier. Private organizations should map those dates to their own data lifetimes, product support windows, procurement cycles, and regulatory obligations.

The fifth result is that **migration remains open-ended**. The first standardized algorithms are not the last word. NIST continues work on additional KEM guidance, HQC standardization, FN-DSA, and additional signature candidates. Side-channel resistance, formal security of hybrid modes, embedded performance, hardware acceleration, certificate ecosystem changes, and long-tail device replacement are active engineering problems.

## Visual

Quantum-safe migration is best treated as a lifecycle rather than a one-time algorithm swap.

```mermaid
flowchart LR
  A["Discover crypto use"] --> B["Classify primitive and role"]
  B --> C["Score data lifetime and exposure"]
  C --> D["Choose target: PQC or hybrid"]
  D --> E["Test size, latency, parsing"]
  E --> F["Stage rollout with telemetry"]
  F --> G["Retire vulnerable algorithms"]
  G --> H["Monitor standards and attacks"]
  H --> D
```

| Workstream | Assets to find | First migration action | Main risk |
|---|---|---|---|
| TLS and VPN key establishment | ECDHE, DH, RSA key transport | Test hybrid X25519 plus ML-KEM where supported | Handshake size, middleboxes, negotiation failures |
| Public certificates | RSA or ECDSA chains | Plan PQ or hybrid certificate strategy as ecosystem support matures | Chain size, CA support, client compatibility |
| Code and firmware signing | ECDSA, RSA, EdDSA signing roots | Introduce PQ signatures for new artifacts and plan trust-anchor rollover | Devices may trust old roots for years |
| Document and archive signing | Long-validity signatures | Add timestamp and algorithm-lifecycle policy | Future verification may accept forgeable signatures |
| Embedded devices | Fixed parsers, small memory, secure boot | Inventory hardware limits before choosing parameters | Cannot fit large keys or signatures |
| Data encryption | AES-128, short hashes, wrapped keys | Prefer strong symmetric parameters and protect key establishment | Mistaking storage encryption for handshake security |

## Worked example 1: Hybrid TLS key establishment size and security intuition

Problem: Compare a classical X25519 key establishment with a hybrid X25519 plus ML-KEM-768 exchange. Estimate key-share bytes and explain what happens if a future quantum attacker breaks X25519 but not ML-KEM.

1. Count the classical exchange. X25519 uses a 32-byte public key share from the client and a 32-byte public key share from the server:

$$
32 + 32 = 64 \text{ bytes}.
$$

2. Count the hybrid exchange using common ML-KEM-768 sizes. The client side contributes an X25519 share and an ML-KEM-768 encapsulation key:

$$
32 + 1184 = 1216 \text{ bytes}.
$$

The server side contributes an X25519 share and an ML-KEM-768 ciphertext:

$$
32 + 1088 = 1120 \text{ bytes}.
$$

The total key-establishment material is therefore

$$
1216 + 1120 = 2336 \text{ bytes}.
$$

3. Compare with classical X25519:

$$
2336 - 64 = 2272 \text{ extra bytes}.
$$

As a ratio:

$$
\frac{2336}{64} = 36.5.
$$

The key-establishment material is about 36.5 times larger, though the total connection overhead depends on the rest of the handshake, certificates, packetization, and reuse.

4. Combine secrets. A simplified hybrid derivation can be written as

$$
\text{traffic_secret} = \mathrm{KDF}(\text{x25519_secret} \mathbin\Vert \text{mlkem_secret}).
$$

If a future quantum attacker can recover `x25519_secret` from recorded traffic but cannot recover `mlkem_secret`, the KDF input still contains an unknown high-entropy component. Under a suitable combiner and KDF model, the final traffic secret should remain hidden.

Checked answer: the hybrid exchange adds about 2272 bytes of key-establishment material in this simplified count. Its purpose is not to make X25519 quantum-safe; its purpose is to ensure the final secret remains protected if at least one component remains secure and the protocol combines them correctly.

## Worked example 2: Prioritizing a crypto inventory

Problem: An organization finds three quantum-vulnerable uses. Rank them for migration.

- A public medical-records API uses ECDHE for TLS. Data confidentiality lifetime is 25 years. The service is patched quarterly.
- A public marketing site uses ECDHE for TLS. Data confidentiality lifetime is less than one day. The service is easy to patch.
- A firmware update system uses ECDSA P-256 signatures. Devices may remain in the field for 12 years and update parsers are hard to change.

Use this simple score:

| Factor | Points |
|---|---:|
| Publicly reachable endpoint | 3 |
| Internal or limited endpoint | 1 |
| Long-lived confidentiality or authentication, at least 10 years | 4 |
| Medium lifetime, 1 to 9 years | 2 |
| Short lifetime, less than 1 year | 0 |
| Quantum-vulnerable key establishment | 3 |
| Quantum-vulnerable signature root or update trust | 4 |
| Hard to patch or hardware-bound | 2 |
| Easy to patch | 0 |

1. Medical-records API:

$$
3 \text{ public} + 4 \text{ long-lived data} + 3 \text{ key establishment} + 0 \text{ easy enough to patch} = 10.
$$

2. Marketing site:

$$
3 \text{ public} + 0 \text{ short-lived data} + 3 \text{ key establishment} + 0 \text{ easy to patch} = 6.
$$

3. Firmware update system:

The update service may not be a public data API, but the trust decision affects many deployed devices. Give it limited exposure points, long authentication lifetime, signature-root points, and hard-to-patch points:

$$
1 + 4 + 4 + 2 = 11.
$$

4. Rank:

$$
\text{firmware signing }(11) > \text{medical API }(10) > \text{marketing site }(6).
$$

Checked answer: the firmware signing system ranks first because long-lived devices may continue accepting forgeable signatures after a future break. The medical API is nearly as urgent because of harvest-now, decrypt-later confidentiality. The marketing site still needs migration, but it is a lower-risk early target if its data truly expires quickly.

## Code

This script turns a small crypto inventory into a repeatable priority list. It is a planning sketch, not a substitute for a formal risk assessment.

```python
from dataclasses import dataclass

@dataclass
class CryptoUse:
    name: str
    primitive: str
    role: str
    exposure: str
    lifetime_years: float
    hard_to_patch: bool

def score(item: CryptoUse) -> int:
    total = 0
    total += 3 if item.exposure == "public" else 1

    if item.lifetime_years >= 10:
        total += 4
    elif item.lifetime_years >= 1:
        total += 2

    if item.role == "key establishment":
        total += 3
    elif item.role == "signature trust":
        total += 4

    if item.hard_to_patch:
        total += 2

    return total

inventory = [
    CryptoUse("medical records API", "ECDHE", "key establishment", "public", 25, False),
    CryptoUse("marketing website", "ECDHE", "key establishment", "public", 0.01, False),
    CryptoUse("firmware update root", "ECDSA P-256", "signature trust", "limited", 12, True),
]

for item in sorted(inventory, key=score, reverse=True):
    print(f"{score(item):2d}  {item.name:22s}  {item.primitive:10s}  {item.role}")
```

The output ranks firmware update trust and long-lived medical confidentiality ahead of the short-lived marketing site. A real inventory would include owners, protocols, certificate chains, hardware limits, regulatory tags, and rollback plans.

## Common pitfalls

- Starting with algorithm replacement before building an inventory. Unknown cryptography cannot be migrated deliberately.
- Treating TLS key exchange as the whole problem. Signatures, certificates, package managers, secure boot, and document workflows often have longer tails.
- Assuming hybrid modes are automatically secure. The exact combiner, transcript binding, downgrade protection, and failure handling matter.
- Ignoring message sizes. PQC keys and signatures can break fixed buffers, MTU assumptions, certificate-chain limits, and embedded parsers.
- Waiting for every ecosystem detail to be final. Long-lived data may need protection before all certificate and protocol work is complete.
- Confusing policy dates with predictions of when a quantum computer will exist. Migration dates are chosen around risk, procurement, and replacement cycles.
- Making library-specific security claims from algorithm names. Implementation quality, side-channel defenses, validation status, and configuration are out of scope for this conceptual page.

## Connections

- [Quantum Security](/quantum-information-science/quantum-security/intro) for the threat model, harvest-now risk, and PQC versus QKD framing.
- [Post-Quantum Cryptography](/quantum-information-science/quantum-security/pqc) for the algorithm families and NIST standardization snapshot.
- [Classical cryptography](/cs/cryptography/) for the RSA, ECDH, AES, hash, and signature baseline being migrated.
- [Quantum computing algorithms](/quantum-information-science/quantum-computing/algorithms) for why Shor and Grover affect different primitives differently.
- [Quantum key distribution](/quantum-information-science/quantum-communication/qkd) for the hardware path and its contrast with PQC migration.
- [Number theory basics](/math/discrete/number-theory-basics) for RSA and discrete-logarithm background.
- [Linear algebra](/math/linear-algebra/) for the matrix and vector language used in lattice-based PQC.
