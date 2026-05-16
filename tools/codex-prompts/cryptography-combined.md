You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from **two complementary textbooks**.

## Inputs

- **SOURCE_PDFs**:
  - `f:/coding/SJ Wiki/tmp/[Jonathan_Katz,_Yehuda_Lindell]_Introduction_to_Mo(2nd).pdf` (Katz & Lindell — *Introduction to Modern Cryptography*, 2nd ed)
  - `f:/coding/SJ Wiki/tmp/IntroToCrypto.pdf` (supplementary)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/cryptography/`
- **SUBJECT**: Cryptography

## How to combine

- **Katz & Lindell** is the canonical modern (provable-security) treatment — primary source.
- Use IntroToCrypto for additional examples or alternative presentations. If it's a different book entirely (e.g. more applied), say so in `intro.md`.

Merge into one set of topic pages; cite differences.

## Produce

1. **`intro.md`** — overview + chapter list + note on combined sourcing.

2. **15-22 detail pages** covering:
   - Classical ciphers + their weaknesses
   - Perfect secrecy, one-time pad, Shannon's theorem
   - Computational security, PPT adversaries, negligible functions
   - Pseudorandom generators (PRGs) and pseudorandom functions (PRFs)
   - Symmetric encryption (PRF-based, stream and block ciphers, modes: ECB/CBC/CTR)
   - Message authentication codes (MACs, PRF-based, CBC-MAC, HMAC)
   - Authenticated encryption (Encrypt-then-MAC, GCM)
   - Collision-resistant hash functions, Merkle-Damgård, SHA-2/3
   - Random oracle model
   - Number theory background (primes, GCD, modular arithmetic, Fermat, Euler, CRT)
   - Discrete log & DH key exchange
   - RSA & textbook RSA pitfalls; OAEP padding
   - Digital signatures (RSA-FDH, DSA, Schnorr, ECDSA)
   - Public-key encryption schemes (ElGamal, hybrid encryption)
   - TLS protocol overview
   - Zero-knowledge proofs (basic definitions, examples)
   - Post-quantum cryptography (intro)

3. **Proof-aware**: state security definitions formally, sketch reductions, note distinguishing experiments.

4. Use `python` snippets where useful (e.g., CRT, Fermat test). LaTeX for math.

## Workflow

1. `pdfinfo` both. 2. `pdftotext -l 25` both. 3. Build merged outline. 4. Per topic, read relevant pages from both, synthesize one page. 5. `intro.md` last. 6. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
