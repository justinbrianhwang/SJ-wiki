---
title: Multi-armed Bandits
sidebar_position: 3
---

# Multi-armed Bandits

A $k$-armed bandit removes states and delayed consequences from reinforcement learning. At each step the learner chooses one action, observes one reward, and learns nothing directly about the actions it did not choose. The whole problem is the allocation of observations: exploit the action that currently looks best, or spend a trial resolving uncertainty elsewhere.

That stripped-down setting is useful far beyond toy slot machines. It fits repeated choices such as which recommendation to show when the reward is immediate and one choice does not alter the next user's context. It also isolates ideas that return in full RL: incremental value estimates, stochastic policies, optimism, confidence bonuses, and baselines.

## Values are unknown means, not observed labels

Each action $a\in\mathcal A=\{1,\ldots,k\}$ has a reward distribution with true value

$$
q_*(a)=\mathbb E[R_t\mid A_t=a].
$$

The learner sees $R_t$ only for $A_t$. If action $a$ has been selected $N_t(a)$ times, its sample-average estimate is

$$
Q_t(a)=\frac{1}{N_t(a)}
\sum_{i<t:A_i=a}R_i.
$$

The direct sum need not be stored. If $Q_n$ is the average after $n-1$ rewards for one action, then after reward $R_n$,

$$
Q_{n+1}=Q_n+\frac1n(R_n-Q_n).
$$

The term $R_n-Q_n$ is an estimation error. The general pattern

$$
\text{new estimate}=\text{old estimate}+\text{step size}\times\text{error}
$$

reappears in temporal-difference learning. Bandits provide the clean case where the target is an immediate observed reward rather than a bootstrapped return.

For stationary rewards, the law of large numbers makes the sample mean converge when each action is sampled indefinitely. Convergence of estimates alone does not specify an action-selection strategy: a purely greedy learner may stop sampling some actions, so their estimates remain based on early noise.

## Regret states the cost of learning

Let $a_*$ be an optimal action. The expected instantaneous regret of choosing $A_t$ is

$$
q_*(a_*)-q_*(A_t).
$$

Cumulative regret through horizon $T$ is

$$
L_T=\sum_{t=1}^{T}\left(q_*(a_*)-q_*(A_t)\right).
$$

The values $q_*$ are unknown to the learner, so regret is mainly an analysis and simulation measure. It captures opportunity cost better than the reward of one exploratory step. Trying a weak-looking action can incur regret now and still be worthwhile if the information improves many later choices.

Average reward, fraction of optimal actions, and cumulative regret emphasize different behavior. An algorithm may identify the exact best action slowly while earning nearly optimal reward because several actions are close. Conversely, a high optimal-action percentage can coexist with poor early regret if exploration was costly.

## Four ways to allocate exploration

### Random exploration with $\epsilon$-greedy

With probability $1-\epsilon$, choose an action maximizing $Q_t(a)$; with probability $\epsilon$, choose uniformly from all $k$ actions. Under the usual convention, the greedy action can also be drawn during the random branch. Its total selection probability is therefore

$$
1-\epsilon+\frac{\epsilon}{k}
$$

when the greedy action is unique. Each nongreedy action has probability $\epsilon/k$.

Random tie-breaking matters at initialization, when estimates are often equal. Always choosing the first maximum creates an arbitrary positional bias. A fixed positive $\epsilon$ ensures continued exploration but also keeps wasting some trials on actions already known to be poor. Decaying $\epsilon$ reduces that waste; if it decays too quickly, early mistakes can become permanent.

### Optimistic initial estimates

Set all initial $Q_1(a)$ above plausible rewards and act greedily. Selecting an action pulls its estimate toward reality, leaving untried actions optimistic and therefore attractive. This produces directed early exploration without random moves.

Optimism depends on reward scale and disappears after actions have been sampled. In a nonstationary problem, an action rejected long ago does not regain its initial optimism when its value later improves. Optimistic starts are best understood as an initialization technique for stationary tasks, not a continuing uncertainty model.

### Upper confidence bounds

UCB chooses

$$
A_t=\arg\max_a
\left[Q_t(a)+c\sqrt{\frac{\ln t}{N_t(a)}}\right].
$$

The first term exploits a high estimate. The second is large for actions with few samples and grows slowly when time passes without selecting them. The constant $c$ converts statistical uncertainty into the reward scale and controls exploration.

The expression is undefined for $N_t(a)=0$. A standard implementation selects every action once before using the formula, or assigns untried actions an infinite score. UCB's confidence interpretation is cleanest for stationary rewards with suitable concentration assumptions. It is not automatically calibrated for heavy-tailed noise or abrupt drift.

### Learning preferences with a gradient bandit

A gradient bandit keeps preferences $H_t(a)$ and defines a softmax policy

$$
\pi_t(a)=\frac{\exp(H_t(a))}{\sum_b\exp(H_t(b))}.
$$

Preferences are identifiable only up to an additive constant; adding the same number to every $H_t(a)$ leaves probabilities unchanged. They are not estimates of expected reward.

For observed action $A_t$ and baseline $B_t$, the update is

$$
H_{t+1}(a)=H_t(a)
+\alpha(R_t-B_t)
\left(\mathbb 1[a=A_t]-\pi_t(a)\right).
$$

If reward is above baseline, the selected action's preference rises and others fall. If it is below baseline, the direction reverses. Taking $B_t$ as an incremental average reward reduces variance. Because the baseline does not depend on the current action, it does not change the expected policy-gradient direction.

| Method | Stored statistics | Source of exploration | Persistent? |
|---|---|---|---|
| $\epsilon$-greedy | values and usually counts | uniform random branch | yes, if $\epsilon\gt 0$ |
| optimistic greedy | values | inflated untried estimates | no |
| UCB | values, counts, time | count-based bonus | yes, but shrinking |
| gradient bandit | action preferences, baseline | softmax stochasticity | yes |

## Stationary and drifting rewards require different memory

A sample average gives equal weight to every observation. After thousands of pulls it reacts very slowly to a changed reward mean. A constant step size uses

$$
Q_{n+1}=Q_n+\alpha(R_n-Q_n).
$$

Expanding the recursion gives

$$
Q_{n+1}=(1-\alpha)^nQ_1
+\sum_{i=1}^{n}\alpha(1-\alpha)^{n-i}R_i.
$$

Recent rewards receive exponentially larger weights. The weights on rewards sum to $1-(1-\alpha)^n$; the remaining weight stays on the initial estimate. As $n$ grows, that initial influence vanishes.

Constant-step estimates do not converge to a fixed number under stationary noise. They continue fluctuating, trading asymptotic precision for responsiveness. Smaller $\alpha$ smooths noise but tracks drift slowly. The correct timescale depends on how quickly the environment changes.

Sample-average convergence also requires step sizes satisfying stochastic-approximation conditions such as $\sum_n\alpha_n=\infty$ and $\sum_n\alpha_n^2\lt \infty$. The choice $\alpha_n=1/n$ satisfies both. A constant $\alpha$ fails the second condition deliberately, preserving adaptation.

## Worked example: incremental sample averages

One action produces rewards $1,3,2,6$. Start with $Q_1=0$ as a placeholder before observing data. After the first reward,

$$
Q_2=0+\frac11(1-0)=1.
$$

After the second,

$$
Q_3=1+\frac12(3-1)=2.
$$

The third reward equals the current estimate:

$$
Q_4=2+\frac13(2-2)=2.
$$

After the fourth,

$$
Q_5=2+\frac14(6-2)=3.
$$

The direct check is

$$
\frac{1+3+2+6}{4}=3.
$$

Now repeat only the last update with a constant step size $\alpha=0.1$ and previous estimate $Q=2$:

$$
Q'=2+0.1(6-2)=2.4.
$$

The sample average moves by $1$ because this is only the fourth observation; the constant-step estimate moves by $0.4$ because its effective memory is longer at that point.

## Worked example: a UCB choice

At time $t=100$, suppose

$$
Q(a_1)=1.0,\quad Q(a_2)=1.3,\quad Q(a_3)=0.8,
$$

with counts

$$
N(a_1)=50,\quad N(a_2)=5,\quad N(a_3)=45.
$$

Use $c=2$. Since $\ln100\approx4.6052$, the bonuses are

$$
\begin{aligned}
b_1&=2\sqrt{4.6052/50}\approx0.6070,\\
b_2&=2\sqrt{4.6052/5}\approx1.9194,\\
b_3&=2\sqrt{4.6052/45}\approx0.6396.
\end{aligned}
$$

Adding estimates and bonuses gives

$$
\begin{aligned}
U_1&=1.6070,\\
U_2&=3.2194,\\
U_3&=1.4396.
\end{aligned}
$$

UCB selects $a_2$. It has the largest empirical mean, but its very small count supplies most of the advantage. After repeated selection its bonus will shrink.

## Worked example: one gradient-bandit update

Let there be three actions with equal preferences $H=[0,0,0]$, so $\pi=[1/3,1/3,1/3]$. Suppose action 2 is selected, reward is $5$, baseline is $2$, and $\alpha=0.1$. The advantage-like term is

$$
R-B=5-2=3.
$$

For selected action 2,

$$
H'(a_2)=0+0.1(3)(1-1/3)=0.2.
$$

For each unselected action,

$$
H'(a)=0+0.1(3)(0-1/3)=-0.1.
$$

The new preferences are $[-0.1,0.2,-0.1]$. Subtract the maximum before softmax:

$$
[-0.3,0,-0.3].
$$

Since $e^{-0.3}\approx0.7408$, the new probability of action 2 is

$$
\pi'(a_2)=\frac1{1+2(0.7408)}\approx0.403.
$$

Each other action has probability about $0.299$. Above-baseline reward has increased, but not collapsed, the policy's preference for the selected action.

## Contextual bandits: covariates without delayed effects

A contextual bandit observes $X_t$, chooses $A_t$, and receives immediate reward $R_t$. The best action can depend on context, so a separate scalar mean per action is inadequate. A linear contextual model might estimate

$$
q(x,a)=\theta_a^\top x.
$$

The boundary with a full MDP is causal. If the action changes future contexts in a reward-relevant way, treating each round independently discards delayed consequences. A recommender that changes a user's long-term interests is not faithfully modeled as a contextual bandit merely because the logs are arranged in sessions.

Offline evaluation is also difficult because logged data reveal rewards only for chosen actions. Comparing a new policy on arbitrary historical rows creates selection bias. Randomized logging or propensity-aware estimators are needed; supervised accuracy on observed actions is not a substitute.

## Simulation with fair tie-breaking

```python
import numpy as np

rng = np.random.default_rng(7)
k = 10
steps = 1000
epsilon = 0.1

true_values = rng.normal(0.0, 1.0, size=k)
estimates = np.zeros(k)
counts = np.zeros(k, dtype=int)
rewards = []

for _ in range(steps):
    if rng.random() < epsilon:
        action = int(rng.integers(k))
    else:
        tied = np.flatnonzero(estimates == estimates.max())
        action = int(rng.choice(tied))

    reward = rng.normal(true_values[action], 1.0)
    counts[action] += 1
    estimates[action] += (reward - estimates[action]) / counts[action]
    rewards.append(reward)

print("true best:", int(np.argmax(true_values)))
print("estimated best:", int(np.argmax(estimates)))
print("average reward:", float(np.mean(rewards)))
print("selection counts:", counts.tolist())
```

One run is noisy and can flatter any method. Comparisons should reuse the same randomly generated bandit instances across algorithms and average over many independent runs. For nonstationary tests, specify how true values drift; a random walk and abrupt change reward different tracking behavior.

## Delayed feedback and missing observations

The elementary bandit assumes reward arrives immediately after the action. Real experiments may return conversions hours later, while many newer actions are already in flight. Updating the wrong action with a delayed reward corrupts estimates; every outcome needs an identifier linking it to the decision that caused it.

Delays also change exploration. An action with many pending outcomes can appear under-sampled if only completed rewards count. Treating pending trials as zero is biased. One approach tracks selections and observations separately, using observed counts for uncertainty while limiting how many unresolved trials are assigned to one action.

Some rewards are censored rather than merely delayed. A user who has not converted by the end of a measurement window may convert later. Short windows systematically undervalue slow outcomes. Survival models or a fixed mature-data cutoff can address the issue, but they change the statistical problem beyond a stationary immediate-reward bandit.

## Reward scale and heavy tails

Sample means are sensitive to extreme rewards. If an action usually gives zero and rarely gives a very large payoff, early estimates can be dominated by one event. UCB formulas based on bounded or sub-Gaussian noise may then be overconfident. Robust mean estimators, clipped rewards, or problem-specific transforms can help, but clipping changes the objective when large outcomes are genuinely important.

Rescaling all rewards by a positive constant preserves the optimal action but changes useful values of $c$, $\alpha$, optimistic initialization, and gradient-bandit baselines. Hyperparameters tied to reward units should be retuned after a scale change. Adding a constant to every action's reward leaves value differences unchanged in a stationary bandit, but a gradient method without an effective baseline can still suffer larger variance.

Bernoulli outcomes deserve the same care. An estimated click-through rate of one from a single impression is not comparable in certainty to $0.6$ from ten thousand impressions. UCB and Bayesian methods encode that difference; greedy sample averages do not.

## Nonstationarity can affect more than the means

A random-walk benchmark usually changes each true mean gradually. Production drift may change variance, introduce new actions, retire old ones, or alter which users arrive. A constant step size tracks mean drift but does not automatically detect a new action or a context shift.

Sliding-window estimates discard observations older than a chosen horizon. They adapt sharply after a change and waste stable historical data. Exponential recency weighting forgets smoothly. Change-point methods attempt to reset only when evidence supports a jump, adding assumptions and detection delay.

Exploration needs to persist under drift. A fixed small $\epsilon$ keeps sampling every action, while vanilla UCB bonuses may become overconfident because counts grow forever. Discounted counts or windowed UCB restore uncertainty for actions not sampled recently. Optimistic initial values offer no such recovery once their initial effect has vanished.

## Experimental units and interference

Online bandit trials assume one action's reward does not change another trial's outcome. This can fail in marketplaces, social networks, or inventory systems. Recommending one item depletes stock; treating one user affects peers; assigning traffic to one server changes latency for others. Rewards are then coupled and the independent-round model is misspecified.

The randomization unit should match the interference structure. User-level assignment avoids switching a person's experience every visit but reduces the number of independent units. Session-level assignment adapts faster and can create carryover. These are design choices, not implementation details of $\epsilon$-greedy.

Guardrail metrics also sit outside a scalar reward unless explicitly incorporated. Optimizing clicks while monitoring latency is a constrained decision problem. Folding everything into one weighted reward is possible, but the weights encode value judgments and can hide violations behind gains elsewhere.

## When a bandit model is too small

If the best action depends on observed covariates, pooling everyone into one mean wastes information and can create unfair allocations. A contextual bandit is the next model. If actions affect future states or available actions, delayed control requires an MDP. If several actions reveal correlated information about one latent function, structured or Gaussian-process bandits may use that relation.

Moving to a richer model costs assumptions and data. A simple bandit remains valuable as a baseline and as a diagnostic of whether sequential state dynamics actually matter. The smallest model that respects the causal timing of the task is usually the easiest one to audit.

<div className="see-also">

See also: [Reinforcement learning problem and finite MDPs](/cs/reinforcement-learning/rl-problem-and-mdps) · [Policy gradient methods](/cs/reinforcement-learning/policy-gradient-methods) · [Monte Carlo methods](/cs/reinforcement-learning/monte-carlo-methods) · [Temporal-difference learning](/cs/reinforcement-learning/temporal-difference-learning)

</div>
