---
title: Constituency Parsing with CKY
sidebar_position: 12
---

# Constituency Parsing with CKY

Constituency parsing analyzes a sentence as nested phrases. Jurafsky and Martin introduce context-free grammars, treebanks, Chomsky normal form, ambiguity, CKY dynamic programming, span-based neural parsing, and parser evaluation. Eisenstein gives a complementary formal treatment of context-free languages, weighted context-free grammars, probabilistic CFGs, semiring parsing, grammar refinement, and links to transition-based parsing.

The main idea is that natural language has hierarchical structure. A noun phrase can contain a determiner and nominal; a verb phrase can contain a verb and noun phrase; larger phrases can be built recursively. CKY shows how to search the enormous space of possible trees efficiently when the grammar is in a suitable binary form.

## Definitions

A **context-free grammar** is a tuple $G=(N,\Sigma,R,S)$ where $N$ is a set of nonterminals, $\Sigma$ is a set of terminals, $R$ is a set of productions, and $S$ is the start symbol. Productions have a single nonterminal on the left:

$$
A\to \beta.
$$

A **constituency parse tree** shows how a sentence is derived from grammar rules. Internal nodes are nonterminals such as `S`, `NP`, and `VP`; leaves are words.

A grammar is in **Chomsky normal form** when every rule has one of these forms:

$$
A\to BC,\qquad A\to w.
$$

CKY requires this binary branching structure. Any CFG can be converted into a weakly equivalent CNF grammar, meaning it recognizes the same strings, though the tree shape may change.

The **CKY chart** is a triangular table. Cell $[i,j]$ stores nonterminals that can derive the span from word position $i$ up to but not including $j$. For a binary rule $A\to BC$, CKY adds $A$ to $[i,j]$ if there is a split $k$ such that $B\in[i,k]$ and $C\in[k,j]$.

A **probabilistic CFG** assigns probabilities to rules. The probability of a tree is the product of its rule probabilities, often computed in log space.

## Key results

CKY is dynamic programming over spans. It avoids repeated work because once a constituent is found for a span, that result can be reused in every larger span. For a sentence of length $n$ and a grammar in CNF, there are $O(n^2)$ spans and $O(n)$ split points per span, giving an $O(n^3)$ parsing structure, multiplied by grammar lookup costs.

Ambiguity is central. A sentence can have many parses due to prepositional phrase attachment, coordination, noun compound structure, and other phenomena. The basic CKY recognizer tells whether a sentence is in the language. A parser stores backpointers to recover one or all trees. A weighted or probabilistic parser stores scores to recover the best tree.

The CKY recurrence for a best-scoring parse is

$$
\pi[i,j,A]=\max_{A\to BC,\;i<k<j}
\left(s(A\to BC)+\pi[i,k,B]+\pi[k,j,C]\right).
$$

Lexical rules initialize length-one spans:

$$
\pi[i,i+1,A]=s(A\to w_i).
$$

Neural span-based parsers keep the chart idea but replace hand-written grammar scores with learned span scores. A transformer or BiLSTM encodes the sentence; an MLP scores each span and label; a CKY-style algorithm finds the highest-scoring tree. This preserves dynamic programming while using modern representations.

Parser evaluation commonly uses labeled precision, labeled recall, and $F_1$ over constituents. A predicted constituent is correct if its span and label match the gold tree, usually after standard preprocessing conventions.

CKY is also a template for thinking about chart algorithms. The chart stores completed subanalyses, not partial guesses that must be recomputed. This is why dynamic programming works for ambiguous grammars: two larger parses can share the same noun phrase analysis for a span. The same idea appears in semiring parsing, where changing the operations changes the computation. A max-plus semiring finds the best parse; a sum-product semiring computes total probability; a boolean semiring performs recognition.

Weighted grammars make the independence assumptions visible. A PCFG assumes that the probability of expanding a nonterminal depends only on that nonterminal, not on its parent, lexical head, or wider context. This is often too weak for natural language. Grammar refinements, parent annotation, lexicalization, and neural span scores all add context back into the scoring function while trying to preserve tractable search.

Constituency parsing remains useful even when dependency parsing is more compact. Constituents identify spans that behave as units, which is valuable for question answering, summarization, semantic role labeling, and grammar checking. A dependency tree says which word is head of a phrase; a constituency tree says where the phrase begins and ends. Many applications need both views.

Treebanks make parsing measurable but also define what counts as syntax. The Penn Treebank, for example, uses conventions for flat noun phrases, traces, function tags, and punctuation that affect both training and evaluation. A parser trained on one treebank learns those annotation decisions, not a universal truth about grammar. When applying a parser to another domain or language, check whether the target annotation scheme expects the same structures.

For hand calculations, it is useful to separate the recognizer from the scorer. First verify that every span can be built by grammar rules; then add probabilities or neural span scores. This prevents arithmetic mistakes from hiding grammar mistakes.

## Visual

```mermaid
flowchart TB
  Sent["Sentence with boundaries: 0 book 1 the 2 flight 3"] --> Lex["Lexical initialization for length-1 spans"]

  subgraph Chart["CKY triangular chart cells"]
    direction TB
    C01["#lsqb;0,1"]: V via V -> book"]
    C12["#lsqb;1,2"]: Det via Det -> the"]
    C23["#lsqb;2,3"]: N via N -> flight"]
    C02["#lsqb;0,2"]: empty after split k=1"]
    C13["#lsqb;1,3"]: NP via NP -> Det N, split k=2"]
    C03["#lsqb;0,3"]: S via S -> V NP, split k=1"]
    C12 --> C13
    C23 --> C13
    C01 --> C03
    C13 --> C03
    C01 --> C02
    C12 --> C02
  end

  Lex --> C01
  Lex --> C12
  Lex --> C23

  subgraph Recurrence["Dynamic-programming recurrence"]
    direction TB
    Span["Target span #lsqb;i,j"]"]
    Split{"Choose split k with i < k < j"}
    Left["Left cell #lsqb;i,k"] contains B"]
    Right["Right cell #lsqb;k,j"] contains C"]
    Rule["Grammar rule A -> B C"]
    Add["Add A to #lsqb;i,j"] and store backpointer ("A -> B C, k")"]
    Span --> Split
    Split --> Left
    Split --> Right
    Left --> Rule
    Right --> Rule
    Rule --> Add
  end

  C03 --> Tree["Recovered parse: S(V(book), NP(Det(the), N(flight)))"]
  Tree --> Output(("recognized because S is in [0,3]"))
```

The CKY visual lays out the chart cells by span length and shows the exact binary combinations that build `NP` and then `S`. The recurrence subgraph makes the I/O contract explicit: a rule `A -> B C` plus a split `k` converts two smaller completed spans into a larger span and stores the backpointer needed to reconstruct the tree.

| Concept | In CKY | Why it matters |
|---|---|---|
| Span | contiguous substring $[i,j]$ | unit of dynamic programming |
| Split | $k$ with $i\lt k\lt j$ | combines two smaller constituents |
| CNF rule | $A\to BC$ | guarantees binary combination |
| Backpointer | chosen rule and split | reconstructs parse tree |
| Weight | log rule or span score | chooses among ambiguous parses |

## Worked example 1: CKY recognition

Problem: parse `book the flight` with this CNF grammar:

```text
S  -> V NP
NP -> Det N
V  -> book
Det -> the
N -> flight
```

Use positions `0 book 1 the 2 flight 3`.

1. Initialize length-one spans:
   - `[0,1]` contains `V` because `V -> book`.
   - `[1,2]` contains `Det` because `Det -> the`.
   - `[2,3]` contains `N` because `N -> flight`.
2. Fill length-two span `[0,2]`:
   - Split at $k=1$: left `[0,1]={V}`, right `[1,2]={Det}`.
   - No rule expands to `V Det`, so add nothing.
3. Fill length-two span `[1,3]`:
   - Split at $k=2$: left `Det`, right `N`.
   - Rule `NP -> Det N` applies, so add `NP` to `[1,3]`.
4. Fill length-three span `[0,3]`:
   - Split at $k=1$: left `V`, right `NP`.
   - Rule `S -> V NP` applies, so add `S`.
   - Split at $k=2`: `[0,2]` is empty, so nothing else.

Checked answer: because `S` is in `[0,3]`, the sentence is recognized and has parse `(S (V book) (NP (Det the) (N flight)))`.

## Worked example 2: choosing a weighted parse

Problem: a span `[0,3]` can be built as `VP -> V NP` in two ways:

1. Split $k=1$: score of left `V` is $-0.1$, right `NP` is $-1.0$, rule score is $-0.2$.
2. Split $k=2$: score of left `V` is $-2.0$, right `NP` is $-0.3$, rule score is $-0.2$.

Use log scores and choose the maximum.

1. Compute split $k=1$:

$$
-0.2 + (-0.1) + (-1.0) = -1.3.
$$

2. Compute split $k=2$:

$$
-0.2 + (-2.0) + (-0.3) = -2.5.
$$

3. Compare:

$$
-1.3 > -2.5.
$$

Checked answer: choose split $k=1$ and store its backpointer. In probability space, this is the higher-probability derivation because log probabilities closer to zero are larger.

## Code

```python
from collections import defaultdict

words = "book the flight".split()
binary = {
    ("V", "NP"): ["S"],
    ("Det", "N"): ["NP"],
}
lexicon = {
    "book": ["V"],
    "the": ["Det"],
    "flight": ["N"],
}

n = len(words)
chart = [[set() for _ in range(n + 1)] for _ in range(n)]
back = {}

for i, word in enumerate(words):
    for lhs in lexicon.get(word, []):
        chart[i][i + 1].add(lhs)
        back[(i, i + 1, lhs)] = word

for span in range(2, n + 1):
    for i in range(n - span + 1):
        j = i + span
        for k in range(i + 1, j):
            for b in chart[i][k]:
                for c in chart[k][j]:
                    for a in binary.get((b, c), []):
                        chart[i][j].add(a)
                        back[(i, j, a)] = (k, b, c)

print("S" in chart[0][n])
print(chart[0][n])
```

## Common pitfalls

- Running CKY on a grammar that has not been converted to CNF or otherwise adapted.
- Confusing recognition with parsing; recognition only says whether a parse exists.
- Keeping chart entries but no backpointers, then being unable to reconstruct trees.
- Forgetting that CNF conversion can alter tree shape, affecting evaluation unless reversed or normalized.
- Assuming one parse means one meaning; syntactic ambiguity often remains semantically important.
- Evaluating by exact whole-tree match only; constituent precision and recall give more informative diagnostics.
- Treating neural span parsers as unrelated to CKY when many still use chart-style dynamic programming.

## Connections

- [Dependency parsing](/cs/nlp/dependency-parsing)
- [Sequence labeling with HMMs and CRFs](/cs/nlp/sequence-labeling-hmms-crfs)
- [Semantic role labeling and word-sense disambiguation](/cs/nlp/semantic-role-labeling-and-word-sense-disambiguation)
- [Transformers and self-attention](/cs/nlp/transformers-self-attention)
