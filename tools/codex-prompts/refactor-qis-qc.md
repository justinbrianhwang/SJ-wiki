## Section: QIS — Quantum Computing area

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-computing/`

### Foundation pages (preserve and enrich)

```
intro.md, hardware.md, algorithms.md, error-correction.md, quantum-ml.md
```

### Paper-named pages to merge then delete

Run `ls` to confirm. Approximate mapping:

```
willow-surface-code-below-threshold.md,
concatenated-bosonic-cat-qubits.md,
gkp-qudit-error-correction.md,
failure-mechanisms-of-ec-gates.md,
silicon-spin-logical-qubits.md (if exists),
quantum-decoder-circuit.md
  → error-correction.md  (most are QEC papers)

Any paper that's primarily about a hardware platform (silicon, ions, etc.) → hardware.md

Any paper about a specific algorithm → algorithms.md
```

### Notes

- The Nielsen & Chuang content already lives in the foundation pages from the previous combine pass. Preserve it.
- Section headings:
  - ✅ `### Surface code memory below threshold` (covers Google Willow 2024 [1])
  - ✅ `### Concatenated bosonic codes` (covers cat-qubit + repetition [2])
  - ✅ `### Beyond break-even with bosonic qudit codes` (covers GKP qudit [3])
  - ✅ `### Learned decoders for real-time error correction` (covers quantum-decoder circuit [4])
  - ✅ `### Failure modes of fault-tolerant gates` (covers failure-mechanisms paper [5])

Apply the refactor policy above. Begin now.
