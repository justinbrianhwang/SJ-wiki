## Section: QIS — Quantum Communication AND Quantum Internet (combined since both are small)

This refactor touches two adjacent areas. Apply the policy to both directories.

### Quantum Communication

- **OUTPUT_DIR_1**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-communication/`

**Foundation pages (preserve and enrich):**
- `intro.md`, `bb84.md`, `qkd.md`, `quantum-network.md`

**Paper-named pages to merge then delete:**
```
efficient-bb84-metropolitan-network.md  → quantum-network.md (or bb84.md if more BB84-focused)
qkd-security-proofs-and-attacks-review.md → qkd.md (review-style content fits the qkd survey page)
```

If other paper-named pages exist, apply same mapping.

**Subsection-heading style** (topical, not paper-named):
- ✅ `### Field-deployed metropolitan networks with optical switches` (covers De Toni 2025 [1])
- ✅ `### Comprehensive security proofs and practical attacks` (covers Jha 2025 review [2])

### Quantum Internet

- **OUTPUT_DIR_2**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-internet/`

**Foundation pages (preserve):**
- `intro.md`, `entanglement.md`, `teleportation.md`, `quantum-repeater.md`

**Paper-named pages to merge then delete:**
```
entanglement-swapping-time-bin-telecom.md (or similar)  → quantum-repeater.md (the natural home — swapping is the repeater primitive)
```

**Subsection-heading style:**
- ✅ `### Deployable telecom-band entanglement swapping` (covers Caltech/Fermilab 2025 [1])

### Both areas: References

Each foundation page that receives merged content gets a `## References` section at the bottom, numbered in order of first appearance.

Apply the refactor policy above to BOTH directories. Begin now.
