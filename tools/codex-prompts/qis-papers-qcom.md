You are an autonomous content author for **SJ Wiki**. Add **technique-named deep-dive pages** for the **Quantum Communication** area of QIS, based on the papers below.

## Inputs

- **SOURCE_PDFs** (3 QKD papers):
  - `f:/coding/SJ Wiki/tmp/2510.16867v1.pdf` — De Toni et al. 2025 *Long-term analysis of efficient-BB84 4-node network with optical switches in metropolitan environment*
  - `f:/coding/SJ Wiki/tmp/2511.20602v1.pdf` — Jha 2025 *Quantum Key Distribution: Bridging Theoretical Security Proofs, Practical Attacks, and Error Correction for Quantum-Augmented Networks*
  - `f:/coding/SJ Wiki/tmp/JRTCSE.2025.13.2.3.pdf` — Nair 2025 *Exploring QKD Protocols for Secure Communication Over Classical Networks*

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-communication/`

## Naming policy

Page filenames MUST be the **technique / system / topic** name, NOT the paper title or author. Suggested:

- `efficient-bb84-metropolitan-network.md` (De Toni 2025)
- `qkd-security-proofs-and-attacks-review.md` (Jha 2025 — review-style)
- `qkd-protocols-survey.md` OR group with above as `qkd-classical-network-integration.md` (Nair 2025) — use your judgment, possibly merge the two review papers into one combined survey page if they substantially overlap.

If a review and a technical paper duplicate too much, merge into one combined page or keep separate by emphasis (foundations vs deployment).

## Existing foundational pages (DO NOT REPLACE)

```
intro.md             (only append "## Deep-dive papers" section)
bb84.md              (foundational; do not modify)
qkd.md               (foundational; do not modify)
quantum-network.md   (foundational; do not modify)
```

## Per-page format

Depth addendum (1500-3500 words; Mermaid diagram or table; ≥2 worked examples; common pitfalls; cross-links). Sections per page:

- Frontmatter: `title:` (technique/topic + year), `sidebar_position:` starting at **20**
- 1-paragraph pitch + full citation
- Problem & motivation
- Method / protocol details with KaTeX math (QBER calculations, sifting probabilities, decoy-state intensity estimates, secret key rate formulas)
- Visual (mandatory) — Mermaid of protocol flow or network topology
- Experimental setup / parameters (when applicable — wavelengths, switch counts, fiber loss, key rates)
- Results — conservative
- Connections — cross-link to foundational `bb84.md`/`qkd.md`/`quantum-network.md` and to `/quantum-information-science/quantum-internet/`, `/cs/cryptography/`
- Numpy/Python sketch — e.g., a small efficient-BB84 sifting simulation
- Common pitfalls / deployment caveats
- Further reading

## Update intro.md

Append "## Deep-dive papers" listing each new page with a 1-line summary. Preserve original content.

## Workflow

1. `pdftotext -l 2 "<pdf>" -` each paper to confirm scope.
2. Decide grouping (1-3 new pages depending on overlap).
3. Write each deep-dive page.
4. Append to `intro.md`.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/quantum-information-science/quantum-communication/`.
- Do not modify `_category_.json`, config files, sidebars, or foundational pages (bb84/qkd/quantum-network).
- No `npm`. English. KaTeX. Mermaid (escape special chars).
- Conservative on key rates and distance claims — quote conditions (loss budget, error rate, decoy probabilities).
- Don't fabricate.

Begin now.
