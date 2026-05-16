## Section: Adversarial Attacks

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/`

### Foundation pages (preserve and enrich)

```
intro.md
threat-models-and-attack-taxonomy.md
mathematical-formulation.md
white-box-attacks.md
black-box-and-transfer-attacks.md
physical-world-and-patch-attacks.md
adversarial-training.md
certified-defenses-and-randomized-smoothing.md
gradient-masking-and-obfuscation.md
evaluation-and-benchmarks.md
robustness-accuracy-tradeoff.md
attacks-on-llms-and-other-modalities.md
```

### Paper-named pages to merge then delete

```
fgsm.md, pgd.md, bim.md, momentum-iterative-fgsm.md, deepfool.md, carlini-wagner-attack.md, ead-elastic-net-attack.md
  → white-box-attacks.md

zoo.md, boundary-attack.md
  → black-box-and-transfer-attacks.md

adversarial-patch.md, physical-stop-sign-attack.md, universal-adversarial-perturbations.md,
rf-universal-adversarial-perturbations.md, one-pixel-attack.md
  → physical-world-and-patch-attacks.md (some may better fit white-box if they're $\ell_p$ image attacks — use judgment)

badnets-backdoor.md
  → could go to a new "Data poisoning and backdoors" section if you'd rather create one; otherwise into evaluation-and-benchmarks.md as a related-threat-model section

audio-adversarial-examples.md, textfooler.md, hotflip.md, bert-attack.md
  → attacks-on-llms-and-other-modalities.md

adaptive-autoattack.md
  → evaluation-and-benchmarks.md
```

If any other paper-named pages exist (run `ls` to check), apply the same rule: pick the most natural foundation home and merge.

### Notes

- Subsection headings should be topical, not paper-named:
  - ✅ `### Single-step sign attacks` (covers FGSM [1])
  - ✅ `### Iterative projected gradient methods` (covers BIM [2], PGD [3])
  - ✅ `### Optimization-based $\ell_2$ attacks` (covers C&W [4], DeepFool [5])
  - ❌ `### FGSM (Goodfellow et al., 2014)`

- For PGD specifically, `adversarial-training.md` (the defense page) already references PGD as the inner-attack of choice. When you merge `pgd.md` into `white-box-attacks.md`, ensure `adversarial-training.md` cross-links to the new PGD subsection rather than to the deleted `pgd.md`.

Apply the refactor policy above. Begin now.
