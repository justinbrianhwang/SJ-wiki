You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/software-engineering.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/software-engineering/`
- **SUBJECT**: Software Engineering

## Produce

1. **`intro.md`** — overview + chapter list (after you identify the book and its scope).

2. **12-18 detail pages** covering whatever the source covers. Typical SE textbook topics:
   - SE fundamentals (process models: waterfall, agile, spiral, RAD)
   - Requirements engineering (elicitation, analysis, specification, validation)
   - System modeling (UML use cases, class, sequence, state diagrams)
   - Architectural design patterns (layered, MVC, microservices, event-driven)
   - Design patterns (creational, structural, behavioral GoF)
   - Software testing (unit, integration, system, acceptance; black/white box)
   - Verification & validation
   - Configuration management & version control
   - Project management (estimation, risk, scheduling)
   - Quality assurance and metrics
   - Maintenance & evolution
   - DevOps / CI/CD (if covered)

3. Per-page: definitions → diagrams (Mermaid for UML) → examples → trade-offs.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` to identify the actual textbook + its TOC. 3. Iterate chapters. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
