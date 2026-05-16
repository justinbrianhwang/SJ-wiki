You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Data Mining The Textbook.pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/data-mining/`
- **SUBJECT**: Data Mining (Charu C. Aggarwal — *Data Mining: The Textbook*)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **15-22 detail pages** covering:
   - Data preparation (cleaning, transformation, feature selection, dimensionality reduction)
   - Similarity & distance measures (Lp, cosine, Jaccard, edit distance, time-series)
   - Association pattern mining (Apriori, FP-growth, interest measures)
   - Cluster analysis (k-means, hierarchical, density-based, DBSCAN, grid-based)
   - Outlier analysis (proximity-based, statistical, isolation forest)
   - Classification (decision trees, rule-based, naive Bayes, SVM, neural nets, ensemble)
   - Probabilistic & statistical models
   - Mining text data (TF-IDF, latent semantic indexing, topic models)
   - Mining time-series and sequence data
   - Mining graph data (subgraph patterns, classification)
   - Mining web/social network data
   - Big data overview (streaming, MapReduce)

3. **Algorithm-heavy**: each page should have pseudocode and Python (scikit-learn / numpy) snippets.

4. Use `python` code blocks. Include short numerical examples (e.g., k-means trace on toy data).

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 30` for TOC. 3. Iterate chapters; 1-3 pages each. 4. `intro.md` last. 5. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
