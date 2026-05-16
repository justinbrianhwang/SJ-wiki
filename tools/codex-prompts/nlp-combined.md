You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from **two complementary textbooks**.

## Inputs

- **SOURCE_PDFs** (both):
  - `f:/coding/SJ Wiki/tmp/NLP.pdf` (Eisenstein — *Natural Language Processing*)
  - `f:/coding/SJ Wiki/tmp/자연어 처리 교재.pdf` (Jurafsky & Martin — *Speech and Language Processing*, 3rd ed draft)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/nlp/`
- **SUBJECT**: Natural Language Processing — combined coverage

## How to combine

These are **complementary**, not duplicates:
- **Jurafsky & Martin** is more comprehensive and authoritative — use as **primary**.
- **Eisenstein** has more formal/ML-flavored treatment of probabilistic models — use as **secondary** for theoretical depth.

Do **not** create separate per-book directories. Merge: each topic page mentions which source(s) it draws on, and where they differ in notation or emphasis.

## Produce

1. **`intro.md`** — overview + chapter list + note about combined sourcing.

2. **18-25 detail pages** covering:
   - Regular expressions, text normalization, edit distance
   - N-gram language models (Markov, smoothing: add-k, Kneser-Ney)
   - Naive Bayes & sentiment classification
   - Logistic regression for text
   - Vector semantics & embeddings (TF-IDF, PPMI, word2vec, GloVe)
   - Neural network basics for NLP (FFN, embeddings → softmax)
   - RNN/LSTM for sequence modeling
   - Transformers and self-attention
   - Pretrained language models (BERT-style + GPT-style)
   - Sequence labeling (POS, NER) with HMMs and CRFs
   - Constituency parsing (CKY)
   - Dependency parsing (transition-based + graph-based)
   - Statistical machine translation overview + neural MT
   - Semantic role labeling, word-sense disambiguation
   - Coreference resolution
   - Information extraction
   - Dialog & chatbots
   - Speech recognition / synthesis (if Jurafsky covers — likely brief)

3. **Algorithm + math depth**. Use `python` (PyTorch / sklearn) snippets. KaTeX math for probabilities, attention formulas, etc.

## Workflow

1. `pdfinfo` both books. 2. `pdftotext -l 25` both books to extract TOCs. 3. Build a merged outline. 4. For each topic, read relevant pages from *both* books and synthesize one page. 5. `intro.md` last. 6. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English (handle the Korean filename — actual content of `자연어 처리 교재.pdf` is in English, it's just titled in Korean). Don't fabricate.

Begin now.
