You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/BartoSutton.pdf` (Richard S. Sutton & Andrew G. Barto — *Reinforcement Learning: An Introduction*, 2nd ed)
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/reinforcement-learning/`
- **SUBJECT**: Reinforcement Learning

## Produce

1. **`intro.md`** — replace the stub. 200-400 word overview, numbered list of pages.

2. **15-22 detail pages** covering Sutton & Barto's full scope:
   - **Part I: Tabular Solution Methods**
     - The reinforcement learning problem (agent-environment, reward, return)
     - Multi-armed bandits (action-value methods, ε-greedy, UCB, gradient bandit, optimistic initial values)
     - Finite Markov decision processes (MDP definition, value functions, optimality)
     - Dynamic programming (policy evaluation, policy improvement, policy iteration, value iteration, async DP, generalized policy iteration)
     - Monte Carlo methods (first-visit and every-visit, on-policy vs off-policy, importance sampling)
     - Temporal-difference learning (TD(0), SARSA, Q-learning, expected SARSA, double Q-learning)
     - n-step bootstrapping (n-step TD, n-step SARSA, n-step off-policy)
     - Planning and learning with tabular methods (models, Dyna, prioritized sweeping, MCTS)
   - **Part II: Approximate Solution Methods**
     - On-policy prediction with approximation (gradient TD, semi-gradient, function approximation)
     - On-policy control with approximation (semi-gradient SARSA, mountain car, average reward)
     - Off-policy methods with approximation (deadly triad, gradient TD)
     - Eligibility traces (λ-returns, TD(λ), true online TD, Watkins's Q(λ))
     - Policy gradient methods (REINFORCE, baselines, actor-critic, policy gradient theorem)
   - **Part III: Looking Deeper**
     - Psychology connections (animal learning, classical conditioning, instrumental)
     - Neuroscience connections (dopamine, basal ganglia)
     - Applications and case studies (TD-Gammon, Atari, AlphaGo, robotics)
     - Frontiers (deep RL, exploration, abstraction, sample efficiency)

3. Per-page format (per addendum): 1500-3500 words, mandatory Mermaid diagram OR table OR ASCII figure (state-action diagrams in Mermaid work well), ≥2 worked examples with full steps, common pitfalls, **runnable Python code** (NumPy-based for tabular methods; PyTorch for function approximation / DRL).

4. **Math notation** — value functions $V_\pi$, $Q_\pi$, optimality $V_*$, $Q_*$; Bellman equations; expectation under policy $\mathbb{E}_\pi[\cdot]$; discount $\gamma$; returns $G_t = \sum_{k=0}^\infty \gamma^k R_{t+k+1}$.

5. Cross-link to:
   - `/cs/machine-learning/` (Mitchell's RL intro)
   - `/cs/deep-learning/` (d2l for function approximation backbones)
   - `/math/probability-and-random-variables/` (MDPs, expectations)
   - `/math/linear-algebra/` (function approximation)

## Workflow

1. `pdfinfo`, `pdftotext -l 30 "<pdf>" -` for cover + TOC.
2. Iterate chapters; 1-2 wiki pages each.
3. Write `intro.md` last.
4. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/reinforcement-learning/`.
- No `_category_.json` edits, no config edits, no `npm`.
- English. Mathematically precise. Match the depth addendum.
- Don't fabricate beyond Sutton & Barto's content.

Begin now.
