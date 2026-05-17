---
title: Markov Chains
sidebar_position: 16
---

# Markov Chains

A Markov chain is a random process whose next state depends on the present state but not on the earlier history. This "memoryless given the present" property is discrete-time cousin of the exponential waiting-time idea. Instead of one random variable, a Markov chain is a sequence $X_0,X_1,X_2,\ldots$ moving through a state space.

MIT 18.440 introduces finite-state Markov chains through examples such as weather models, then discusses ergodicity and stationarity. The main long-run question is whether the chain forgets its starting state and settles into stable state frequencies. Transition matrices make the calculations concrete.

## Definitions

Let the finite state space be

$$
\{0,1,\ldots,M\}.
$$

A sequence $X_0,X_1,X_2,\ldots$ is a **Markov chain** if there are transition probabilities $P_{ij}$ such that

$$
P(X_{n+1}=j\mid X_n=i,\ X_{n-1}=i_{n-1},\ldots,X_0=i_0)
=P_{ij}.
$$

The matrix

$$
P=(P_{ij})
$$

is the **transition matrix**. Each row sums to $1$:

$$
\sum_j P_{ij}=1.
$$

If the distribution of $X_n$ is represented as a row vector $\mu_n$, then

$$
\mu_{n+1}=\mu_n P.
$$

A distribution $\pi$ is **stationary** if

$$
\pi P=\pi,
\qquad
\sum_i\pi_i=1,
\qquad
\pi_i\ge0.
$$

A finite Markov chain is **ergodic** in the lecture's sense if some power of its transition matrix has all positive entries. This condition implies the chain can eventually move from any state to any other state with positive probability and avoids periodic obstructions.

## Key results

The $n$-step transition probabilities are entries of $P^n$:

$$
P(X_n=j\mid X_0=i)=(P^n)_{ij}.
$$

This follows from repeated conditioning and matrix multiplication:

$$
(P^2)_{ij}=\sum_k P_{ik}P_{kj},
$$

which sums over the possible intermediate state after one step.

If the initial distribution is stationary, then every later distribution is the same:

$$
\mu_0=\pi
\quad\Rightarrow\quad
\mu_n=\pi P^n=\pi.
$$

For an ergodic finite Markov chain, there is a unique stationary distribution $\pi$, and the distribution of $X_n$ converges to $\pi$ regardless of the starting state:

$$
\mu_0P^n\to\pi.
$$

The stationary distribution is not necessarily uniform. It reflects both how often states are entered and how long the chain tends to remain there.

Expected hitting times are often computed by first-step equations. If $h_i$ is the expected time to hit a target state starting from $i$, then

$$
h_i=1+\sum_jP_{ij}h_j
$$

for non-target states, with $h_i=0$ on target states.

The Markov property does not say the process has no memory in an absolute sense. It says the current state contains all information from the past that is relevant for predicting the next state. If the state variable is chosen poorly, the Markov property may fail. For example, a model of relationship status as simply "single" or "married" may be unrealistic if the duration of the current relationship affects the chance of transition; adding duration to the state can sometimes restore a Markov description.

Transition matrices can be read row by row. Row $i$ is the probability distribution of the next state, conditional on being in state $i$ now. Matrix powers combine steps. The entry $(P^3)_{ij}$ is the probability of being in state $j$ three steps later, starting from $i$, after summing over all possible two-step intermediate paths.

Stationarity is an equilibrium for distributions, not necessarily for individual paths. A chain started from $\pi$ still moves randomly from state to state, but the marginal distribution at each time remains $\pi$. This is like shuffling mass among states in such a way that the total amount of mass in each state is restored after each transition.

Ergodicity is what turns stationarity into long-run prediction. If a chain is reducible, different starting classes may lead to different limiting behavior. If it is periodic, the distribution can oscillate rather than settle. The lecture's condition that some power of $P$ has all positive entries rules out both problems in the finite setting.

Markov chains also connect to the law of large numbers. In an ergodic finite chain, the fraction of time spent in each state converges to the stationary probability of that state. This is not the independent-sample law of large numbers, because the states are dependent, but it expresses a similar long-run averaging principle for a dependent process.

## Visual

```mermaid
flowchart LR
  subgraph Weather["Two-state weather chain"]
    direction LR
    R(("Rainy")) -- "0.5 stay" --> R
    R -- "0.5 switch" --> S(("Sunny"))
    S -- "0.2 switch" --> R
    S -- "0.8 stay" --> S
  end

  subgraph Evolution["Distribution evolution"]
    direction TB
    Mu0["initial distribution<br/>mu_0 = (P(R), P(S)"]"] --> Pmat["transition matrix<br/>P = ((0.5, 0.5"], ["0.2, 0.8"]]"]
    Pmat --> Mu1["one step<br/>mu_1 = mu_0 P"]
    Mu1 --> Mun["n steps<br/>mu_n = mu_0 P^n"]
    Mun --> Flow["stationary flow balance<br/>pi_R P_RS = pi_S P_SR"]
  end

  subgraph Absorb["Absorbing-chain template"]
    direction TB
    Canon["reorder states<br/>transient first, absorbing last"] --> Block["block matrix<br/>P = ((Q, R"], ["0, I"]]"]
    Block --> Fundamental["fundamental matrix<br/>N = (I - Q)^-1"]
    Fundamental --> Outputs["absorption probabilities and expected hitting times"]
  end

  Weather --> Pmat
  Flow --> Ergodic{"irreducible and aperiodic?"}
  Ergodic -- "yes" --> Stable["long-run state frequencies equal pi"]
  Ergodic -- "no" --> Diagnose["inspect closed classes or period"]
  Diagnose -. "absorbing case" .-> Canon
```

This Markov-chain architecture shows both a concrete weather state machine and the linear-algebra pipeline behind it. The transition matrix turns current distributions into future distributions, while flow balance gives the stationary distribution for the two-state example. The absorbing-chain subgraph adds the standard block form and fundamental matrix used when probability mass eventually enters terminal states.

| Concept | Formula | Meaning |
|---|---|---|
| Markov property | next depends only on current state | history is summarized by present |
| Transition matrix | $P_{ij}$ | chance to move $i$ to $j$ |
| Distribution update | $\mu_{n+1}=\mu_nP$ | one-step evolution |
| Stationarity | $\pi P=\pi$ | unchanged by transition |
| Ergodicity | some $P^k$ has positive entries | long-run forgetting of start |

The weather diagram shows two different kinds of persistence. A rainy day has probability $0.5$ of being followed by another rainy day, while a sunny day has probability $0.8$ of being followed by another sunny day. This asymmetry is why the stationary distribution puts more mass on sun. Stationarity is not found by averaging the four transition probabilities; it is found by balancing the long-run flow of probability between the states.

In a two-state chain, the stationary equations can often be read as a flow balance. The long-run probability flow from rain to sun is $\pi_RP_{RS}$, and the flow from sun to rain is $\pi_SP_{SR}$. At equilibrium these flows match. This gives $\pi_R(0.5)=\pi_S(0.2)$ in the worked example, the same equation obtained from $\pi P=\pi$.

When the state space is larger, the same ideas remain but the algebra becomes linear algebra. Solving for stationarity means finding a left eigenvector of $P$ with eigenvalue $1$ and normalizing it to sum to one. Numerical computation is often straightforward, but interpretation still requires checking whether the chain is irreducible, aperiodic, and appropriate for the modeled system. A correct matrix calculation cannot rescue a poor state description.

## Worked example 1: stationary weather distribution

Problem: A weather chain has states $R$ for rainy and $S$ for sunny. If today is rainy, tomorrow is rainy with probability $0.5$ and sunny with probability $0.5$. If today is sunny, tomorrow is rainy with probability $0.2$ and sunny with probability $0.8$. Find the stationary distribution.

Method:

1. With state order $(R,S)$, the transition matrix is

$$
P=
\begin{pmatrix}
0.5&0.5\\
0.2&0.8
\end{pmatrix}.
$$

2. Let $\pi=(r,s)$. Stationarity means

$$
(r,s)P=(r,s),
\qquad r+s=1.
$$

3. The first coordinate equation is

$$
r=0.5r+0.2s.
$$

4. Rearrange:

$$
0.5r=0.2s
\quad\Rightarrow\quad
s=2.5r.
$$

5. Use $r+s=1$:

$$
r+2.5r=1
\quad\Rightarrow\quad
3.5r=1
\quad\Rightarrow\quad
r=\frac{2}{7}.
$$

6. Then

$$
s=\frac{5}{7}.
$$

Checked answer: the long-run fraction of sunny days is $5/7$, larger than rainy because sunny days are more persistent.

## Worked example 2: expected waiting time to sun

Problem: In the same weather chain, starting from a rainy day, what is the expected number of days until the first sunny day?

Method:

1. Let $h_R$ be the expected waiting time to hit $S$ starting from $R$.
2. Let $h_S=0$ because we are already sunny.
3. From $R$, after one day the chain is sunny with probability $0.5$ and rainy again with probability $0.5$.
4. First-step equation:

$$
h_R=1+0.5h_R+0.5h_S.
$$

5. Substitute $h_S=0$:

$$
h_R=1+0.5h_R.
$$

6. Solve:

$$
0.5h_R=1
\quad\Rightarrow\quad
h_R=2.
$$

Checked answer: rainy persists with probability $0.5$ each day, so the wait for sun is geometric with success probability $0.5$ and mean $1/0.5=2$ days.

## Code

```python
import numpy as np

P = np.array([[0.5, 0.5],
              [0.2, 0.8]])

# Stationary distribution solves (P.T - I) pi = 0 with sum pi = 1.
A = np.vstack([P.T - np.eye(2), np.ones(2)])
b = np.array([0.0, 0.0, 1.0])
pi, *_ = np.linalg.lstsq(A, b, rcond=None)
print("stationary distribution:", pi)

mu = np.array([1.0, 0.0])  # start rainy
for _ in range(20):
    mu = mu @ P
print("distribution after 20 days:", mu)

h_r = 1 / 0.5
print("expected days from rain to sun:", h_r)
```

## Common pitfalls

- Confusing independence with the Markov property. Markov chains usually have dependent consecutive states.
- Multiplying transition matrices in the wrong orientation. This page uses row distributions and $\mu_{n+1}=\mu_nP$.
- Assuming the stationary distribution is uniform because the state space is finite.
- Forgetting to impose $\sum_i\pi_i=1$ when solving $\pi P=\pi$.
- Assuming every finite chain converges to a stationary distribution from every start. Periodicity and reducibility can obstruct convergence.

## Connections

- [Conditional probability, Bayes, and independence](/math/probability-and-random-variables/conditional-probability-bayes-independence)
- [Strong law and Jensen's inequality](/math/probability-and-random-variables/strong-law-and-jensens-inequality)
- [Martingales, risk-neutral probability, and Black-Scholes](/math/probability-and-random-variables/martingales-risk-neutral-probability-black-scholes)
- [Entropy and coding](/math/probability-and-random-variables/entropy-and-coding)
- [Markov chains in the shorter probability section](/math/probability/markov-chains)
