You are an autonomous content author for **SJ Wiki**. Populate the **Quantum Security** area of QIS with foundational concept pages.

## Inputs

- **SOURCE_PDFs**: NONE. Write from general knowledge. Future paper drops will merge in combine mode.
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-security/`

## Pages to rewrite (3 stubs)

| File | Role |
|---|---|
| `intro.md` | Area hub: threat model, PQC vs QKD framing |
| `pqc.md` | Post-Quantum Cryptography algorithm families and NIST standardization |
| `quantum-safe-crypto.md` | Migration strategies and real-world deployment |

## Per-page content guidance

**`intro.md`** — area scope: what changes when a sufficiently large quantum computer exists. Shor's algorithm breaks RSA, DH, ECDH, ECDSA, DSA. Grover's algorithm only square-roots brute force on symmetric primitives (AES, hashes — doubling key length restores security). PQC vs QKD: two independent paths (algorithmic / hardware). Migration timeline: NIST PQC since 2016, FIPS 203 (ML-KEM / Kyber), FIPS 204 (ML-DSA / Dilithium), FIPS 205 (SLH-DSA / SPHINCS+) standardized in 2024. "Harvest now, decrypt later" threat. Mermaid showing where each primitive sits.

**`pqc.md`** — algorithm families with sketches of hardness assumptions, schemes, key sizes, and signing/encryption speeds:
- **Lattice-based** (LWE, Module-LWE, Ring-LWE, NTRU). Schemes: **Kyber** (ML-KEM, FIPS 203 KEM), **Dilithium** (ML-DSA, FIPS 204 signature), **Falcon** (FIPS 206, NTRU-based signature with floating-point). Hardness from worst-case lattice problems.
- **Hash-based** signatures. Schemes: **XMSS**, **LMS** (stateful, RFC 8391 / RFC 8554); **SPHINCS+** (SLH-DSA, stateless, FIPS 205). Larger signatures but minimal assumptions (collision resistance of hash).
- **Code-based**. Schemes: **Classic McEliece** (KEM, 1978 — long-standing, large keys but small ciphertexts; NIST round-4 / IETF track).
- **Multivariate**. **Rainbow** broken in 2022; cautionary tale of why peer review matters in NIST competition.
- **Isogeny-based**. **SIKE** broken in 2022 by Castryck-Decru; another cautionary tale.
- Comparison table: family / hardness / key size / signature size / signing speed / verification speed. Comparison vs RSA / ECC.

**`quantum-safe-crypto.md`** — migration strategies:
- Crypto agility: software / protocol design to swap primitives without redesigning systems.
- Hybrid schemes: combine classical (X25519) + PQC (Kyber768) so both must break for security to fail. Used by Cloudflare, Google, AWS in TLS 1.3 trials (2022-2024).
- NSA CNSA 2.0 timeline (US NSS migration by 2035; specific subsets by 2030).
- "Harvest now, decrypt later" risk for long-lived secrets (medical, legal, government).
- Performance / size trade-offs vs classical: Kyber768 ciphertext ≈ 1.1 kB vs ECDH ≈ 32 bytes; signing latency comparisons.
- Crypto inventory: how organizations identify and prioritize asymmetric-crypto endpoints to migrate first (TLS certs, code signing, document signing, hardware roots of trust).
- Open challenges: side-channel resistance, hybrid mode formal security proofs, hardware accelerators, embedded device migration.

## Format

Depth addendum (1500-3500 words; mandatory Mermaid diagram or comparison table; ≥2 worked examples per page; common pitfalls; Python sketches — e.g., a tiny lattice LWE example with `numpy`; cross-links).

## Cross-linking

- `/cs/cryptography/` — classical baseline (RSA, ECDH, AES, hashes) and the broader security definitions
- `/quantum-information-science/quantum-computing/algorithms` — Shor and Grover details
- `/quantum-information-science/quantum-communication/qkd` — alternative quantum approach (compare/contrast)
- `/math/discrete/number-theory-basics` — lattices/RSA/etc number-theoretic background
- `/math/linear-algebra/` — lattice geometry

## Constraints

- Stay inside OUTPUT_DIR. No external file edits.
- English. KaTeX math. Mermaid (escape special chars).
- Conservative on PQC timeline and SOTA — NIST process evolved rapidly; state which version of NIST standardization you're citing (FIPS 203/204/205 final 2024).
- Do not give specific implementation security claims for any library; treat that as out of scope.

Begin now.
