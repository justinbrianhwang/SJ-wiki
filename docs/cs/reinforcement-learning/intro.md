---
title: Reinforcement Learning
sidebar_position: 1
---

# Reinforcement Learning

These notes cover reinforcement learning following Richard S. Sutton and Andrew G. Barto's *Reinforcement Learning: An Introduction*, 2nd edition. The subject studies agents that learn by interacting with an environment: they observe state, choose actions, receive rewards, and improve behavior to maximize long-run return. The early material builds the finite Markov decision process framework and tabular solution methods. The middle material replaces tables with function approximation. The closing material connects RL to psychology, neuroscience, applications, and open research directions.

![An agent-environment loop shows actions, observations, and rewards cycling through interaction.](https://commons.wikimedia.org/wiki/Special:FilePath/Agent-environment-diagram-rl.svg)

*Figure: The agent-environment interface is the basic situation that defines reinforcement learning. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Agent-environment-diagram-rl.svg), Martin Thoma, CC0.*

![A cart-pole animation shows a controller trying to balance an inverted pole on a moving cart.](https://commons.wikimedia.org/wiki/Special:FilePath/Cartpole.gif)

*Figure: Cart-pole is a standard control and reinforcement-learning benchmark. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cartpole.gif), Condordellanebbia, CC BY-SA 4.0.*

The organizing thread is value: how to predict return, how to improve policies from value estimates, and when direct policy optimization or planning is more appropriate. Read the pages in order if you want the Sutton-Barto progression from bandits to dynamic programming, Monte Carlo methods, temporal-difference learning, approximation, and policy gradients.

1. [Reinforcement Learning Problem and Finite MDPs](/cs/reinforcement-learning/rl-problem-and-mdps)
2. [Multi-armed Bandits](/cs/reinforcement-learning/multi-armed-bandits)
3. [Dynamic Programming](/cs/reinforcement-learning/dynamic-programming)
4. [Monte Carlo Methods](/cs/reinforcement-learning/monte-carlo-methods)
5. [Temporal-Difference Learning](/cs/reinforcement-learning/temporal-difference-learning)
6. [n-step Bootstrapping](/cs/reinforcement-learning/n-step-bootstrapping)
7. [Planning and Learning with Tabular Methods](/cs/reinforcement-learning/planning-and-learning)
8. [On-policy Prediction with Approximation](/cs/reinforcement-learning/on-policy-prediction-approximation)
9. [On-policy Control with Approximation](/cs/reinforcement-learning/on-policy-control-approximation)
10. [Off-policy Methods with Approximation](/cs/reinforcement-learning/off-policy-approximation)
11. [Eligibility Traces](/cs/reinforcement-learning/eligibility-traces)
12. [Policy Gradient Methods](/cs/reinforcement-learning/policy-gradient-methods)
13. [Psychology Connections](/cs/reinforcement-learning/psychology-connections)
14. [Neuroscience Connections](/cs/reinforcement-learning/neuroscience-connections)
15. [Applications and Frontiers](/cs/reinforcement-learning/applications-and-frontiers)
