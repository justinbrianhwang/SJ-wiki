---
title: Authenticated Encryption and GCM
sidebar_position: 8
---

# Authenticated Encryption and GCM

Authenticated encryption combines confidentiality and integrity in one interface. It encrypts the message and authenticates both the ciphertext and optional associated data such as headers, sequence numbers, protocol versions, or content types. This is the primitive most applications should want, because bare encryption is malleable and separate encryption/MAC composition is easy to get wrong.

Katz and Lindell emphasize generic composition, especially encrypt-then-MAC, and explain how authenticated encryption yields stronger guarantees such as resistance to chosen-ciphertext attacks. Smart's hybrid-encryption and symmetric-security chapters reinforce the same engineering picture: protect the payload with a data encapsulation mechanism that already includes confidentiality and authenticity. GCM is a widely deployed example built from CTR encryption plus polynomial authentication.

## Definitions

An **authenticated encryption with associated data** scheme, abbreviated AEAD, has algorithms:

- $\mathrm{Gen}(1^n)$: sample a key.
- $\mathrm{Enc}_k(N,A,m)$: encrypt message $m$ using nonce $N$ and associated data $A$, returning ciphertext and tag.
- $\mathrm{Dec}_k(N,A,c,t)$: return $m$ or reject.

The associated data $A$ is not encrypted, but it is authenticated. If $A$ changes, decryption should reject.

The two main security goals are:

1. **Confidentiality**: ciphertexts hide plaintexts under allowed nonce rules.
2. **Integrity**: attackers cannot produce a new valid tuple $(N,A,c,t)$ that decrypts successfully, except by replaying something allowed by the protocol.

Generic composition combines an encryption scheme and a MAC:

- **Encrypt-and-MAC**: send $\mathrm{Enc}_k(m)$ and $\mathrm{Mac}_{k'}(m)$.
- **MAC-then-encrypt**: encrypt $m\|\mathrm{Mac}_{k'}(m)$.
- **Encrypt-then-MAC**: send $c=\mathrm{Enc}_k(m)$ and $t=\mathrm{Mac}_{k'}(c)$.

Under standard assumptions, encrypt-then-MAC is the robust generic choice. It authenticates the exact ciphertext before decryption, reducing exposure to decryption-oracle behavior.

**AES-GCM** uses AES-CTR for encryption and GHASH, a polynomial hash over $\mathrm{GF}(2^{128})$, for authentication. Its nonce must be unique for a given key. A 96-bit nonce is the standard fast path.

## Key results

Encrypt-then-MAC gives authenticated encryption when the encryption is CPA secure and the MAC is strongly unforgeable. The receiver verifies the MAC first. If verification fails, it rejects without decrypting. This prevents attackers from using decryption error messages to learn about plaintext structure.

MAC-then-encrypt can be secure in some carefully specified systems, but it is fragile. The history of padding-oracle attacks shows why: when receivers decrypt first and then check padding or tags, different error behavior can become a chosen-ciphertext side channel. The lesson is not that every MAC-then-encrypt system is broken, but that composition order and error handling are part of the security proof.

GCM's confidentiality comes from CTR mode. If a nonce repeats with the same key, the keystream repeats, exposing XORs of plaintexts. Worse, GCM's authentication can also fail under nonce reuse because GHASH equations leak information about the authentication subkey. Nonce uniqueness is therefore a hard requirement, not a performance suggestion.

AEAD does not automatically prevent replay. If an attacker records a valid ciphertext and sends it again with the same nonce and associated data, decryption may succeed. Protocols handle replay with sequence numbers, epochs, channel state, or transcript binding. In TLS, record sequence numbers and key updates are part of the surrounding design.

Associated data is how protocols bind context. Suppose a packet header says `type=payment` and the encrypted body says an amount. If the header is not authenticated, an attacker may move the ciphertext into a different context. AEAD lets the header remain visible while still making it tamper-evident.

Proof sketch for encrypt-then-MAC: first, any accepted modified ciphertext must carry a valid tag. If the tag is new, it breaks MAC unforgeability. If the tag is copied from a previous ciphertext, then the ciphertext is the same value and replay is a protocol matter. Once invalid ciphertexts are rejected before decryption, the confidentiality game reduces to CPA security of the encryption scheme because the adversary cannot get useful decryptions of modified challenges.

GCM deserves special attention because it is both common and easy to misuse. Its encryption half is CTR mode, so the AES inputs are derived from a nonce and counter. Its authentication half, GHASH, evaluates a polynomial over the binary field $\mathrm{GF}(2^{128})$ using a hash subkey $H=E_k(0^{128})$. The final tag combines the GHASH result with an encrypted counter block. This design is fast because CTR encryption and polynomial hashing can be parallelized, and because processors often include carryless multiplication instructions. The security analysis, however, assumes nonce uniqueness. When a nonce repeats, the same CTR pad repeats and the polynomial authentication equations can give the adversary algebraic information about $H$.

AEAD APIs also force a useful separation between public context and private payload. A packet number, content type, protocol version, sender identity, or routing header may need to remain visible to intermediaries, but the receiver still needs to reject tampering. Associated data is the place for that context. Omitting it is a design error even if the encrypted body is protected, because an attacker may move a valid ciphertext into a different semantic setting.

Tag length is a concrete-security choice. A 128-bit tag gives a generic forgery probability near $2^{-128}$ per independent attempt in the idealized model. Truncating to 96, 64, or 32 bits may be acceptable only after accounting for the total number of verification attempts, the cost of online guessing, and the damage from one accepted forgery. This is why protocol standards usually specify tag lengths rather than leaving every application to improvise.

Misuse-resistant AEAD modes exist, but they are not a license to ignore nonces. Schemes such as SIV-style constructions can remain confidential under some nonce-reuse patterns by deriving a synthetic IV from the message and associated data. They have different performance and online-processing properties. The ordinary lesson for GCM remains simpler: design the surrounding protocol so the same key and nonce cannot repeat.

In reductions, authenticated encryption is often treated as a combined privacy-and-integrity object, but deployments must still decide what to do on failure. The only safe plaintext output on tag failure is no plaintext at all. Logging, metrics, and error messages should avoid including decrypted fragments, parser details, or timing differences. This keeps the implementation aligned with the ideal decryption oracle, which simply returns reject.

Key rotation sets another boundary. Even with unique nonces, a long-lived key eventually accumulates many forgery attempts and much encrypted data. Protocols often limit records per key and derive fresh traffic keys before counters approach their limits. Rekeying is a concrete way to keep the proof's query bounds close to reality.

In short, AEAD security is a contract among the primitive, nonce allocation, tag checking, context binding, and protocol state.

## Visual

```mermaid
flowchart LR
  A[Associated data A] --> T[MAC / GHASH]
  M[Message m] --> E[CTR encryption]
  N[Nonce N] --> E
  N --> T
  E --> C[Ciphertext c]
  C --> T
  T --> G[Tag t]
  C --> OUT["("#quot;#quot;c,t#quot;#quot;")"]
  G --> OUT
```

| Composition | Receiver order | Typical status | Main risk |
|---|---|---|---|
| Encrypt-and-MAC | verify plaintext tag separately | generally not preferred | tag may leak plaintext properties |
| MAC-then-encrypt | decrypt before checking MAC | fragile unless carefully proven | padding/error oracles |
| Encrypt-then-MAC | verify tag before decrypting | robust generic construction | must authenticate nonce/context too |
| AEAD mode | one integrated API | preferred | nonce misuse can still be fatal |

## Worked example 1: associated data catches header tampering

Problem: an AEAD scheme encrypts body `amount=100` with associated data `type=invoice`. An attacker changes the visible header to `type=refund` but leaves ciphertext and tag unchanged. What happens?

Method:

1. During encryption, the tag is computed over both associated data and ciphertext:

$$
t=\mathrm{Auth}_k(N,A,c).
$$

2. The original accepted tuple is:

$$
(N,\ A=\texttt{type=invoice},\ c,\ t).
$$

3. The attacker submits:

$$
(N,\ A'=\texttt{type=refund},\ c,\ t).
$$

4. Verification recomputes:

$$
t'=\mathrm{Auth}_k(N,A',c).
$$

5. Since $A'\ne A$, a secure authenticator makes $t'=t$ only with negligible probability.

Checked answer: decryption rejects. The body was not changed, but the authenticated context was changed.

## Worked example 2: encrypt-then-MAC verification order

Problem: a receiver gets $(c,t)$ in an encrypt-then-MAC system. The MAC verification fails. Should the receiver decrypt to produce a detailed error?

Method:

1. Encrypt-then-MAC computes:

$$
c=\mathrm{Enc}_{k_E}(m),\qquad t=\mathrm{Mac}_{k_M}(c).
$$

2. The receiver first checks:

$$
\mathrm{Vrfy}_{k_M}(c,t)\stackrel{?}{=}1.
$$

3. If this is false, the ciphertext is not authenticated. Decrypting it could expose padding checks, parser differences, or timing behavior.

4. Therefore the receiver returns a single reject result without decryption.

5. Only if the tag verifies does the receiver compute:

$$
m=\mathrm{Dec}_{k_E}(c).
$$

Checked answer: reject before decrypting. The verification order is part of the construction's security argument.

## Code

```python
import hashlib
import hmac
import secrets

def stream(key: bytes, nonce: bytes, length: int) -> bytes:
    out = b""
    counter = 0
    while len(out) < length:
        block = hmac.new(key, nonce + counter.to_bytes(4, "big"), hashlib.sha256).digest()
        out += block
        counter += 1
    return out[:length]

def toy_aead_encrypt(key: bytes, nonce: bytes, ad: bytes, message: bytes):
    # Demonstrates AEAD shape with encrypt-then-MAC; use standard AEAD in production.
    pad = stream(key, nonce, len(message))
    ciphertext = bytes(a ^ b for a, b in zip(message, pad))
    tag = hmac.new(key, b"tag" + nonce + ad + ciphertext, hashlib.sha256).digest()[:16]
    return ciphertext, tag

def toy_aead_decrypt(key: bytes, nonce: bytes, ad: bytes, ciphertext: bytes, tag: bytes):
    expected = hmac.new(key, b"tag" + nonce + ad + ciphertext, hashlib.sha256).digest()[:16]
    if not hmac.compare_digest(expected, tag):
        raise ValueError("reject")
    pad = stream(key, nonce, len(ciphertext))
    return bytes(a ^ b for a, b in zip(ciphertext, pad))

key = secrets.token_bytes(32)
nonce = secrets.token_bytes(12)
associated_data = b"type=invoice;version=1"
message = b"amount=100;currency=USD"
ciphertext, tag = toy_aead_encrypt(key, nonce, associated_data, message)
plaintext = toy_aead_decrypt(key, nonce, associated_data, ciphertext, tag)
print(plaintext)
```

## Common pitfalls

- Reusing a GCM nonce with the same key.
- Encrypting without authenticating, then trying to patch integrity later.
- Authenticating the plaintext but not the ciphertext in a fragile custom composition.
- Forgetting to include headers, algorithm identifiers, sequence numbers, or channel context as associated data.
- Returning different errors for padding, tag failure, parse failure, and version failure.
- Assuming AEAD prevents replay without protocol-level sequence tracking.

## Connections

- [Symmetric encryption and modes](/cs/cryptography/symmetric-encryption-modes)
- [Message authentication codes](/cs/cryptography/message-authentication-codes)
- [TLS protocol overview](/cs/cryptography/tls-protocol-overview)
- [Public-key encryption](/cs/cryptography/public-key-encryption-elgamal-hybrid)
