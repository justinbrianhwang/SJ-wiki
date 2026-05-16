---
title: Adversarial Attacks
sidebar_position: 1
---

# Adversarial Attacks

The study of how machine learning models — especially deep neural networks — fail under small, targeted perturbations of their inputs, and what can be done to defend against those attacks.

## Scope

Adversarial machine learning sits at the intersection of [machine learning](/cs/machine-learning/intro), [deep learning](/cs/deep-learning/intro), and [cryptography / security](/cs/cryptography/intro). The questions are:

- Can a small, often imperceptible perturbation of an input cause a classifier to misclassify? **Yes**, demonstrated by Szegedy et al. 2013 and many follow-ups.
- What are the optimal attack budgets, threat models, and norms ($\ell_2$, $\ell_\infty$, $\ell_0$)?
- Do robustness and accuracy trade off?
- Can we *certify* robustness — prove no perturbation within a ball will flip a prediction?
- How do attacks transfer between models? Between modalities? To physical-world objects?
- What defenses actually work (adversarial training, randomized smoothing) vs. only appear to work (gradient masking)?

## Planned pages

*Content being added based on papers in `tmp/` (to be uploaded).*

Likely structure once papers arrive:

- Foundations and threat models
- White-box attacks (FGSM, PGD, C&W, DeepFool, …)
- Black-box and transfer attacks
- Physical-world and patch attacks
- Adversarial training as a defense
- Certified defenses (randomized smoothing, interval bound propagation)
- Attacks on LLMs (prompt injection, jailbreaks)
- Attacks on diffusion / generative models
- Robustness and accuracy trade-offs

The page set will be populated once relevant papers are dropped into `tmp/`.

## Connections

- [Deep Learning](/cs/deep-learning/intro) — most attacks target deep networks
- [Machine Learning](/cs/machine-learning/intro) — classical PAC framing and decision boundaries
- [Reinforcement Learning](/cs/reinforcement-learning/intro) — RL policies are also attackable (e.g., adversarial state observations)
- [Cryptography](/cs/cryptography/intro) — formal threat-model discipline and security definitions

## How to contribute

Drop papers into `tmp/` (e.g., Goodfellow et al. 2014 *Explaining and Harnessing Adversarial Examples*, Madry et al. 2017 *Towards Deep Learning Models Resistant to Adversarial Attacks*, Carlini & Wagner 2017, etc.) and request the Codex agent run; it will populate the section following the combine-mode and depth-addendum policies already in `tools/codex-prompts/_depth-addendum.md`.
