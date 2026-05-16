---
title: Reinforcement Learning Problem and Finite MDPs
sidebar_position: 2
---

# Reinforcement Learning Problem and Finite MDPs

Reinforcement learning studies how an agent can learn to choose actions through interaction. The agent is not handed labeled correct actions. Instead, it receives scalar rewards after acting, observes the next situation, and must improve behavior from experience. Sutton and Barto use this setup to separate reinforcement learning from supervised learning and from pure planning: the learner is active, its actions influence later data, and the main objective is long-run return rather than immediate prediction accuracy.

The mathematical home for this problem is the finite Markov decision process, or finite MDP. An MDP turns informal ideas such as "state," "action," "reward," and "future consequence" into a compact stochastic model. Once the MDP is defined, later chapters can ask more focused questions: how to estimate values, how to improve a policy, when bootstrapping helps, and what changes when the state space is too large for a table.

## Definitions

A reinforcement learning problem is organized around an agent-environment interface. At time $t$, the agent observes a state $S_t \in \mathcal{S}$, selects an action $A_t \in \mathcal{A}(S_t)$, and receives a reward $R_{t+1} \in \mathbb{R}$ and next state $S_{t+1}$. The interaction continues either forever in a continuing task or until a terminal state in an episodic task.

A finite MDP is specified by finite state and action sets and one-step dynamics:

$$
p(s', r \mid s, a) = \Pr(S_{t+1}=s', R_{t+1}=r \mid S_t=s, A_t=a).
$$

The Markov property says this conditional distribution depends on the present state and action, not on the complete earlier history. This is not a claim that the world has no hidden causes. It is a modeling requirement: the chosen state representation should contain enough information for predicting the next state and reward distribution relevant to control.

A policy $\pi$ is a decision rule. In the stochastic case,

$$
\pi(a \mid s) = \Pr(A_t=a \mid S_t=s).
$$

The return is the discounted sum of future rewards:

$$
G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1},
$$

where $0 \le \gamma \le 1$ is the discount rate. In episodic tasks, the sum stops at termination. In continuing tasks, $\gamma \lt  1$ keeps the infinite sum finite in many common settings. Sutton and Barto also introduce average-reward formulations later for continuing control.

The state-value function under policy $\pi$ is

$$
V_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t=s],
$$

and the action-value function is

$$
Q_\pi(s,a) = \mathbb{E}_\pi[G_t \mid S_t=s, A_t=a].
$$

Optimal values compare all policies:

$$
V_*(s) = \max_\pi V_\pi(s), \qquad Q_*(s,a) = \max_\pi Q_\pi(s,a).
$$

A reward signal defines the goal. A value function predicts long-run reward. A model predicts consequences, usually through samples $(s',r)$ or probabilities $p(s',r \mid s,a)$. Model-free methods learn directly from experience, while model-based methods also use a learned or supplied model for planning.

## Key results

The central recursive fact is that returns decompose into immediate reward plus discounted future return:

$$
G_t = R_{t+1} + \gamma G_{t+1}.
$$

Taking conditional expectations gives the Bellman expectation equation for a fixed policy:

$$
V_\pi(s) =
\sum_a \pi(a \mid s)
\sum_{s',r} p(s',r \mid s,a)
\left[r + \gamma V_\pi(s')\right].
$$

For action values,

$$
Q_\pi(s,a) =
\sum_{s',r} p(s',r \mid s,a)
\left[
r + \gamma \sum_{a'} \pi(a' \mid s') Q_\pi(s',a')
\right].
$$

The optimality equations replace policy averaging with maximization:

$$
V_*(s) =
\max_a \sum_{s',r} p(s',r \mid s,a)
\left[r + \gamma V_*(s')\right],
$$

and

$$
Q_*(s,a) =
\sum_{s',r} p(s',r \mid s,a)
\left[r + \gamma \max_{a'} Q_*(s',a')\right].
$$

These equations justify the later algorithmic pattern of bootstrapping: update a current estimate toward a target that uses another current estimate. They also explain why value is not the same as immediate reward. An action with small immediate reward can be best if it tends to lead to valuable future states.

For finite discounted MDPs, at least one deterministic optimal policy exists. If $Q_*$ is known, an optimal policy can choose any action in

$$
\arg\max_a Q_*(s,a).
$$

This result is powerful because it reduces the control problem to estimating values accurately enough. Many RL algorithms differ mainly in what target they use, how they sample experience, and whether they evaluate the policy being followed or a different target policy.

## Visual

```mermaid
flowchart LR
  S[State S_t] --> P["Policy pi(a | s)"]
  P --> A[Action A_t]
  A --> E["Environment dynamics p(s', r | s, a)"]
  E --> R[Reward R_{t+1}]
  E --> N[Next state S_{t+1}]
  R --> G[Return G_t]
  N --> S
  G --> V["Value estimates V_pi, Q_pi"]
  V --> P
```

| Concept | Symbol | Role in the MDP | Common confusion |
|---|---:|---|---|
| State | $s$ | Information used for prediction and control | Treating raw observation as automatically Markov |
| Action | $a$ | Agent's controllable choice | Ignoring state-dependent action sets |
| Reward | $r$ | Immediate scalar objective signal | Designing reward as a hint instead of the real goal |
| Return | $G_t$ | Total discounted future reward | Forgetting the first reward is $R_{t+1}$ |
| Policy | $\pi(a \mid s)$ | Behavior rule | Mixing behavior policy and target policy |
| Value | $V_\pi$, $Q_\pi$ | Expected return prediction | Equating high immediate reward with high value |
| Model | $p(s',r \mid s,a)$ | Predicts next consequences | Assuming a model is required for all RL |

## Worked example 1: Computing returns in an episode

Problem: An episode has rewards $R_1=2$, $R_2=-1$, $R_3=4$, then terminates. Let $\gamma=0.5$. Compute $G_0$, $G_1$, and $G_2$.

Step 1: Start from the last nonterminal time. At $t=2$, only $R_3$ remains:

$$
G_2 = R_3 = 4.
$$

Step 2: At $t=1$, use $G_1 = R_2 + \gamma G_2$:

$$
\begin{aligned}
G_1 &= -1 + 0.5(4) \\
&= -1 + 2 \\
&= 1.
\end{aligned}
$$

Step 3: At $t=0$, use $G_0 = R_1 + \gamma G_1$:

$$
\begin{aligned}
G_0 &= 2 + 0.5(1) \\
&= 2.5.
\end{aligned}
$$

Check: Expanding the full sum directly gives

$$
G_0 = 2 + 0.5(-1) + 0.5^2(4) = 2 - 0.5 + 1 = 2.5.
$$

The checked answer is $G_0=2.5$, $G_1=1$, and $G_2=4$.

## Worked example 2: Solving a two-state Bellman system

Problem: A policy $\pi$ always takes the only available action in two nonterminal states $A$ and $B$. From $A$, the environment gives reward $1$ and moves to $B$. From $B$, it gives reward $2$ and moves to $A$. Let $\gamma=0.9$. Solve for $V_\pi(A)$ and $V_\pi(B)$.

Step 1: Write Bellman equations from the transitions:

$$
\begin{aligned}
V_\pi(A) &= 1 + 0.9 V_\pi(B), \\
V_\pi(B) &= 2 + 0.9 V_\pi(A).
\end{aligned}
$$

Step 2: Substitute the second equation into the first:

$$
\begin{aligned}
V_\pi(A) &= 1 + 0.9(2 + 0.9V_\pi(A)) \\
&= 1 + 1.8 + 0.81V_\pi(A) \\
&= 2.8 + 0.81V_\pi(A).
\end{aligned}
$$

Step 3: Isolate $V_\pi(A)$:

$$
\begin{aligned}
V_\pi(A) - 0.81V_\pi(A) &= 2.8 \\
0.19V_\pi(A) &= 2.8 \\
V_\pi(A) &= \frac{2.8}{0.19} \approx 14.7368.
\end{aligned}
$$

Step 4: Plug back into the second equation:

$$
\begin{aligned}
V_\pi(B) &= 2 + 0.9(14.7368) \\
&= 2 + 13.2631 \\
&\approx 15.2631.
\end{aligned}
$$

Check: Put these values into the first equation:

$$
1 + 0.9(15.2631) = 1 + 13.7368 = 14.7368.
$$

The checked answer is $V_\pi(A)\approx 14.7368$ and $V_\pi(B)\approx 15.2631$.

## Code

```python
import numpy as np

# Two-state Markov reward process under a fixed policy.
# States: 0 = A, 1 = B
gamma = 0.9
P = np.array([
    [0.0, 1.0],  # A -> B
    [1.0, 0.0],  # B -> A
])
r = np.array([1.0, 2.0])

# Bellman equation: v = r + gamma P v
# Rearranged: (I - gamma P) v = r
I = np.eye(2)
v = np.linalg.solve(I - gamma * P, r)

print({"V(A)": v[0], "V(B)": v[1]})
print("Bellman residual:", v - (r + gamma * P @ v))
```

## Common pitfalls

- Treating the reward as a training label for the last action only. In RL, the reward is part of a sequential objective, and the consequences of an action can arrive much later.
- Forgetting the time indexing: after choosing $A_t$ in state $S_t$, the reward is $R_{t+1}$ and the next state is $S_{t+1}$.
- Assuming every observation is a Markov state. A camera frame, sensor reading, or database row may omit information needed to predict future rewards.
- Confusing $V_\pi$ with $V_*$. The first evaluates a particular policy; the second is the best value achievable by any policy.
- Using $\gamma$ as a vague preference for "short-term thinking." Discounting also controls mathematical convergence in continuing tasks.
- Designing rewards that encode advice rather than the real goal. If reward gives points for intermediate behavior that can be exploited, the agent may optimize the proxy.

## Connections

- [Multi-armed bandits](/cs/reinforcement-learning/multi-armed-bandits)
- [Dynamic programming](/cs/reinforcement-learning/dynamic-programming)
- [Temporal-difference learning](/cs/reinforcement-learning/temporal-difference-learning)
- [Mitchell machine learning RL intro](/cs/machine-learning/)
- [Probability and random variables](/math/probability-and-random-variables/)
