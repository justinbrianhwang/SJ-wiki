You are adding **paper architecture figures** to the NLP and reinforcement-learning sections of SJ Wiki.

## Target

`f:/coding/SJ Wiki/docs/cs/nlp/`
`f:/coding/SJ Wiki/docs/cs/reinforcement-learning/`

## What to do

Read the **MODEL ARCHITECTURE FIGURES POLICY** above. For each named model in these sections, embed the paper's architecture figure with full caption + attribution. Place at the top of the named-model subsection.

## Models to cover (NLP)

### `transformers-self-attention.md` (Transformer already embedded — confirm not duplicated)

### `pretrained-language-models.md` (BERT already embedded — confirm not duplicated)
- **GPT-3** (`2005.14165`, `x1.png` — few-shot performance scaling) — if a GPT page section exists
- **T5** (`1910.10683`, `x1.png` — text-to-text framework)
- **BART** (`1910.13461`, `x1.png` — encoder-decoder denoising)
- **LLaMA** (`2302.13971`, `x1.png`) — if mentioned
- **ELMo / ULMFiT** — typically no ar5iv figures, skip

### `machine-translation.md`
- **Seq2seq with attention** (`1409.0473` Bahdanau, `x1.png`)
- **Transformer for MT** — already covered.

### `speech-recognition-and-synthesis.md`
- **DeepSpeech 2** (`1512.02595`, `x1.png`)
- **Tacotron 2** (`1712.05884`, `x1.png`)
- **wav2vec 2.0** (`2006.11477`, `x1.png`)
- **Whisper** (`2212.04356`, `x1.png`)

### `dialogue-and-chatbots.md`
- **DialoGPT / BlenderBot** — typically tech reports, skip if no ar5iv.
- **InstructGPT / RLHF** (`2203.02155`, `x2.png`)

### `vector-semantics-and-embeddings.md`
- **word2vec** (`1301.3781`, `x1.png` if exists)
- **GloVe** — Stanford report, no arxiv. Skip or use Wikimedia.

## Models to cover (RL)

### `reinforcement-learning/` pages

Look at what models are named in each page. Likely candidates:
- **DQN** (`1312.5602`, `x1.png`) — but original is short and may not have a good ar5iv figure. The Nature 2015 version has one — use Wikimedia `DQN_architecture.svg` if you remember it, else skip.
- **A3C / A2C** (`1602.01783`, `x1.png`)
- **PPO** (`1707.06347`) — usually no architecture figure; skip
- **TRPO** (`1502.05477`) — same; skip
- **DDPG** (`1509.02971`, `x1.png` if exists)
- **SAC** (`1801.01290`, `x1.png` if exists)
- **Rainbow DQN** (`1710.02298`, `x1.png` — combination figure)
- **AlphaGo / AlphaZero** — Nature papers, no ar5iv. Skip or use Wikimedia.
- **MuZero** (`1911.08265`, `x2.png`)
- **Dreamer / DreamerV2 / DreamerV3** (`2010.02193`, `2301.04104`, `x2.png`)
- **R2D2** (`2009.10881` for variants) — skip if uncertain
- **IMPALA** (`1802.01561`, `x1.png`)
- **GAE / advantage estimation** (`1506.02438`) — skip
- **MCTS / AlphaGo / Go** — use Wikimedia `Monte_carlo_tree_search.svg` if relevant
- **Decision Transformer** (`2106.01345`, `x1.png`)

## Format (mandatory)

```markdown
![<descriptive alt text>](https://ar5iv.labs.arxiv.org/html/<id>/assets/x<N>.png)

*Figure: <one-line description>. From [Author et al., Year](https://arxiv.org/abs/<id>) — embedded under educational fair use with attribution.*
```

## Verification (mandatory)

After all edits, run:

```bash
python tools/check-image-urls.py docs/cs/nlp/ docs/cs/reinforcement-learning/ 2>&1 | grep BROKEN
```

For each BROKEN URL: try `x1.png` → `x2.png` → `x3.png`. If none work, remove. Never push a broken URL.

## Output

Final summary table:

```
Pages touched: N
Figures embedded: M (ar5iv: M-k, Wikimedia: k)
Broken URLs found and removed: x
Models skipped: list
```

## Constraints

- Stay inside `docs/cs/nlp/` and `docs/cs/reinforcement-learning/`.
- Don't touch existing Mermaid diagrams or other content.
- Don't duplicate already-embedded figures.
- Don't fabricate arxiv IDs or figure numbers.

Begin now.
