---
title: Reductions and the Recursion Theorem
sidebar_position: 13
---

# Reductions and the Recursion Theorem

Reductions transport impossibility results. Instead of diagonalizing afresh for every undecidable problem, transform an instance of a known hard language into an instance of the new one. If a solver for the target would decide the source, the target solver cannot exist.

The recursion theorem handles a different recurring device: a machine using its own description. It supplies fixed points for computable transformations of programs, making self-reference part of the formal model rather than an appeal to source files or informal paradox.

## A reduction turns a target solver into a source solver

A **mapping reduction** from $A$ to $B$, written $A\le_m B$, is a total computable function $f$ such that

$$
w\in A\quad\Longleftrightarrow\quad f(w)\in B
$$

for every string $w$. “Computable” here means that a Turing machine outputs $f(w)$ and halts on every input. A **many-one reduction** is the same notion: it produces one target instance and uses the resulting yes-or-no answer directly.

```mermaid
graph LR
  A[Known hard language A] -->|compute f| B[Target language B]
  B -->|hypothetical decider| C["Answer for f(w)"]
  C --> D[Answer for w in A]
  D --> E[Contradiction if A is undecidable]
```

| Goal | Reduction setup | Consequence of a target solver |
|---|---|---|
| prove $B$ undecidable | $A_{TM}\le_m B$ | a decider for $B$ would decide $A_{TM}$ |
| prove $B$ not recognizable | $\overline{A_{TM}}\le_m B$ | a recognizer for $B$ would recognize $\overline{A_{TM}}$ |
| prove complexity hardness | known hard $A\le_p B$ | an efficient solver for $B$ gives one for $A$ |
| construct self-reference | apply the recursion theorem | a computable program transformer has a behavioral fixed point |

Mapping reductions preserve decidability and recognizability downward:

$$
A\le_m B\text{ and }B\text{ decidable}
\quad\Longrightarrow\quad
A\text{ decidable},
$$

$$
A\le_m B\text{ and }B\text{ recognizable}
\quad\Longrightarrow\quad
A\text{ recognizable}.
$$

Their contrapositives are the usual hardness arguments. To prove $B$ hard, the arrow must point from the known hard problem to $B$.

## Write the proof as an algorithm and two cases

A clean mapping reduction has three parts:

1. On an arbitrary source encoding $w$, describe the terminating syntactic procedure that produces $f(w)$.
2. Prove that source yes-instances become target yes-instances.
3. Prove that source no-instances become target no-instances.

If the target is a property of a constructed machine, analyze what that machine does when the embedded source computation accepts, rejects, or loops. The reduction itself must halt in all three cases.

The transformation may write a new machine containing the code of $M$ and a literal input $w$. That is a finite operation on descriptions. It may not first run $M$ to completion and choose the output according to whether $M$ accepts, since such a transformation would already solve the source problem.

This distinction is easy to state and central to the method: build code that performs the simulation later; do not try to know the simulation's outcome while computing the reduction.

## From acceptance to nonempty machine languages

Define

$$
NE_{TM}=\{\langle N\rangle:L(N)\ne\emptyset\}.
$$

To show $A_{TM}\le_m NE_{TM}$, take an arbitrary pair $\langle M,w\rangle$ and construct a machine $N$:

> On input $x$, ignore $x$ and simulate $M$ on $w$. If $M$ accepts, accept $x$. If $M$ rejects, reject; if it loops, continue forever.

Writing this description of $N$ is computable even when the embedded simulation would never halt.

If $M$ accepts $w$, then $N$ accepts every input, so $L(N)=\Sigma^*$ and is nonempty. If $M$ does not accept $w$, then $N$ accepts no input, so $L(N)=\emptyset$. Therefore

$$
\langle M,w\rangle\in A_{TM}
\quad\Longleftrightarrow\quad
\langle N\rangle\in NE_{TM}.
$$

A decider for $NE_{TM}$ would consequently decide $A_{TM}$, proving $NE_{TM}$ undecidable.

Ignoring $x$ is deliberate. The target asks only whether at least one string is accepted, so the constructed language may be all strings in one case and no strings in the other. A universality or equivalence reduction would arrange irrelevant inputs differently to match its target property.

## Many-one reductions versus oracle access

A mapping reduction commits to one target instance before seeing its answer. A **Turing reduction** may ask several target-oracle questions, with later queries depending on earlier answers. Many-one reductions are stricter, simple to compose, and sufficient for most introductory undecidability and NP-completeness arguments.

The reducibility notion matters when transferring recognizability, completeness, or quantitative resource bounds. A result proved with an adaptive oracle reduction should not be silently restated as a mapping reduction.

## The recursion theorem as a behavioral fixed point

Let $t$ be any total computable transformation that maps machine descriptions to machine descriptions. The **recursion theorem** guarantees a machine $R$ such that

$$
\varphi_R=\varphi_{t(\langle R\rangle)},
$$

where $\varphi_M$ denotes the partial function computed by $M$. The descriptions need not be textually identical; their machines have the same behavior.

The theorem removes the need for an external “read my own source file” operation. It says that computable transformations of program descriptions have programmatic fixed points. Machines can therefore be constructed whose behavior depends on their own encodings within the ordinary Turing-machine model.

## Obtaining a self-printing machine

Define a computable transformation $t(x)$ that returns the description of a machine $P_x$ with the behavior:

> Ignore the input and print the fixed string $x$.

By the recursion theorem, there is a machine $R$ behaviorally equivalent to $P_{\langle R\rangle}$. It ignores its input and prints $\langle R\rangle$. The fixed-point theorem supplies the self-description without infinite regress.

A quine is the familiar programming analogue, but the theorem is broader. It supports reductions and diagonal constructions in which a machine embeds, compares, or transforms its own description.

## Encoding semantic properties into constructed machines

Many undecidability reductions make a target machine's language depend on one source computation:

- For emptiness or nonemptiness, accept no strings in one source case and at least one in the other.
- For universality, accept all strings exactly when the source computation has the selected outcome.
- For equivalence, construct two machines that agree in one case and differ in the other.
- For grammar problems, encode computation histories so that language membership or ambiguity reflects whether a valid accepting history exists.

Each target property requires its own treatment of inputs unrelated to the embedded computation. The common mechanism is syntactic: output a finite machine or grammar description whose later behavior carries the undecidable information.

The recursion theorem is unnecessary when the construction only embeds a separately supplied $M$ and $w$. It becomes relevant when the constructed machine must refer to its own description. Keeping those uses separate avoids invoking self-reference where an ordinary reduction suffices.

## Checks that catch invalid reductions

- The reduction machine must halt and output a valid target instance for every source string, including malformed encodings under the chosen convention.
- The equivalence needs both implications, not only preservation of yes-instances.
- A target decider or recognizer may appear only in the contradiction after the reduction is defined, not inside the computation of $f$.
- The direction $A\le_m B$ supports hardness of $B$, while $B\le_m A$ supplies an upper comparison for $B$.
- The recursion theorem concerns behavioral fixed points of computable transformations, not merely a source-code trick.

<div className="see-also">

See also:

- The source undecidable languages are in [decidability and the halting problem](/cs/theory/decidability-and-the-halting-problem).
- Encodings and computable functions rely on [Turing machines and the Church-Turing thesis](/cs/theory/turing-machines-and-the-church-turing-thesis).
- Polynomial-time reductions appear in [NP-completeness and classic reductions](/cs/theory/np-completeness-and-classic-reductions).
- Space-bounded reductions matter in [space complexity](/cs/theory/space-complexity).

</div>
