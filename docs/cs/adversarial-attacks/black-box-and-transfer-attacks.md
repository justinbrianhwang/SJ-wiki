---
title: Black-Box and Transfer Attacks
sidebar_position: 5
---

# Black-Box and Transfer Attacks

Black-box attacks study what an adversary can do without direct access to model weights or gradients. That restriction is common in deployed systems: an attacker may only submit inputs to an API, observe labels or confidence scores, and pay a cost for every query. Transfer attacks are even more restrictive at attack time: the adversary builds adversarial examples on a surrogate model and hopes they generalize to the target.

These attacks matter because white-box robustness is not the only operational question. A public classifier, moderation model, malware detector, speech recognizer, or LLM endpoint may expose limited feedback rather than gradients. The right evaluation asks how success changes with attacker knowledge, feedback type, query budget, surrogate data, and distribution shift.

## Definitions

A **black-box attack** assumes the attacker cannot directly inspect parameters $\theta$ or compute exact gradients $\nabla_x \mathcal{L}(f_\theta(x), y)$. The attacker may have one of several feedback channels:

- **Score-based access**: the model returns logits, probabilities, or confidence scores.
- **Decision-based access**: the model returns only a top-1 label or accept/reject decision.
- **Top-$k$ access**: the model returns a ranked set of labels, sometimes with scores.
- **Bandit access**: the attacker receives a scalar objective, reward, or partial feedback.
- **Transfer-only access**: the attacker receives no target feedback during attack construction.

A **query budget** $Q$ limits calls to the target model. An attack is often summarized by success rate at $Q$, median queries among successful examples, and failure rate after budget exhaustion.

A **surrogate model** $\tilde{f}_{\phi}$ approximates the target $f_\theta$. The attacker crafts:

$$
\tilde{x}_{\mathrm{adv}}
= x + \arg\max_{\delta \in \Delta(x)}
\mathcal{L}(\tilde{f}_{\phi}(x+\delta), y),
$$

then tests whether $f_\theta(\tilde{x}_{\mathrm{adv}})$ fails.

A **zeroth-order attack** estimates gradients from function values rather than backpropagation. If the attacker can query a scalar loss $J(x)$, a finite-difference estimate in coordinate direction $e_i$ is:

$$
\frac{\partial J}{\partial x_i}
\approx
\frac{J(x+\sigma e_i)-J(x-\sigma e_i)}{2\sigma}.
$$

Random-direction estimators such as NES and SPSA estimate the full gradient with fewer structured queries:

$$
\nabla J(x)
\approx
\frac{1}{m\sigma}\sum_{i=1}^{m} J(x+\sigma u_i)u_i,
$$

where $u_i$ are random perturbation directions. A symmetric estimator uses both $x+\sigma u_i$ and $x-\sigma u_i$ to reduce bias.

## Key results

Transferability is the first black-box baseline. If two models learn similar decision boundaries, an input that crosses one boundary can cross the other. Transfer improves when the surrogate shares architecture, training data, preprocessing, loss, and augmentation with the target. It can also improve with attack choices that avoid overfitting to one model's local gradient, such as momentum or input transformations.

Score-based attacks turn black-box access into an optimization problem. For an untargeted attack with returned probabilities, define:

$$
J(x) = \mathcal{L}(f(x), y).
$$

The attacker estimates $\nabla_x J(x)$ and runs projected ascent. The cost depends on dimension $d$. Naive coordinate finite differences can require $2d$ queries per gradient estimate, which is expensive for images. Random-direction methods reduce the per-step query count but introduce variance.

Decision-based attacks are harder because the model does not reveal a smooth score. A typical strategy is:

1. Find any starting point $x_0$ already classified as the target class or any wrong class.
2. Move along the line or boundary toward the clean input $x$ while staying adversarial.
3. Estimate boundary normals using label queries.
4. Reduce the perturbation norm until the query budget is exhausted.

Square Attack is a strong score-based or decision-flavored black-box method for $\ell_\infty$ and $\ell_2$ settings. It does not estimate full gradients. Instead, it samples localized square-shaped perturbation updates and accepts those that improve the objective, making it query-efficient and useful in benchmarks such as AutoAttack-style evaluation.

Black-box attacks expose a central evaluation point: limited-query robustness is not the same as true robustness. A model may survive 100 queries but fail at 10,000 queries. Conversely, a defense that hides scores can reduce practical attack success without providing a mathematical certificate. The claim must name the feedback channel and budget.

## Visual

```mermaid
flowchart TD
  A[No target gradients] --> B{Target feedback}
  B -->|No queries| C[Transfer attack]
  B -->|Scores/logits| D[Score-based query attack]
  B -->|Labels only| E[Decision-based attack]
  C --> F[Train or choose surrogate]
  F --> G[Craft examples on surrogate]
  G --> H[Test target once or few times]
  D --> I[Estimate gradient or search updates]
  I --> J[Projected black-box optimization]
  E --> K[Find adversarial starting point]
  K --> L[Boundary search]
```

| Attack family | Feedback required | Query pattern | Typical advantage | Typical weakness |
|---|---|---|---|---|
| Transfer | Surrogate only | No target queries during crafting | Cheap and realistic when queries are monitored | Depends on surrogate quality |
| ZOO | Scores/logits | Coordinate finite differences | Direct zeroth-order optimization | High query cost in high dimensions |
| NES | Scores/logits | Random directional queries | Lower-dimensional gradient estimate | Noisy, needs tuning |
| SPSA | Scores/logits or scalar loss | Simultaneous random perturbations | Simple and scalable | Variance and step-size sensitivity |
| Square Attack | Scores or decisions depending setup | Random localized updates | Query-efficient, gradient-free | Still approximate |
| Boundary attack | Decisions only | Boundary-following search | Works with hard labels | Needs adversarial starting point |

## Worked example 1: Finite-difference gradient cost

Problem: A score-based attacker wants to estimate the gradient of a loss for a $32 \times 32 \times 3$ image using central finite differences. How many model queries are needed for one full coordinate gradient estimate? What if the query budget is $20{,}000$?

1. Compute dimension:

$$
d = 32 \cdot 32 \cdot 3 = 3072.
$$

2. Central finite differences use two queries per coordinate:

$$
x+\sigma e_i \quad \text{and} \quad x-\sigma e_i.
$$

3. Queries for one full gradient:

$$
Q_{\mathrm{grad}} = 2d = 6144.
$$

4. With budget $20{,}000$, the maximum number of complete coordinate-gradient estimates is:

$$
\left\lfloor \frac{20000}{6144} \right\rfloor = 3.
$$

5. The remaining budget is:

$$
20000 - 3(6144)=1568.
$$

Checked answer: only three full central-difference gradients fit in the budget. This explains why random-direction estimators and search-based attacks are attractive for high-dimensional images.

## Worked example 2: Transfer attack accounting

Problem: An attacker trains a surrogate model and creates 500 adversarial images. The target API is queried once per image. A total of 180 images fool the target. Compute the transfer success rate and explain what query budget should be reported.

1. The number of attempted target inputs is:

$$
n = 500.
$$

2. The number of successful target misclassifications is:

$$
s = 180.
$$

3. Transfer success rate is:

$$
\frac{s}{n}=\frac{180}{500}=0.36.
$$

4. Convert to a percentage:

$$
0.36 \cdot 100\% = 36\%.
$$

5. The target-query budget during crafting is zero if the attacker did not use target feedback to tune the examples. The final evaluation uses one target query per example.

Checked answer: the transfer success rate is $36\%$. The report should say "transfer-only crafting with 0 target queries, evaluated with 1 target query per candidate." If the attacker repeatedly adjusted examples based on target failures, it would no longer be pure transfer.

## Code

```python
import torch
import torch.nn.functional as F

@torch.no_grad()
def nes_gradient(model, x, y, sigma=0.001, samples=32):
    grad = torch.zeros_like(x)
    for _ in range(samples):
        u = torch.randn_like(x)
        loss_pos = F.cross_entropy(model((x + sigma * u).clamp(0, 1)), y, reduction="none")
        loss_neg = F.cross_entropy(model((x - sigma * u).clamp(0, 1)), y, reduction="none")
        scale = ((loss_pos - loss_neg) / (2 * sigma)).view(-1, 1, 1, 1)
        grad += scale * u
    return grad / samples

def black_box_pgd_nes(model, x, y, epsilon=8 / 255, step_size=2 / 255, steps=20):
    x0 = x.detach()
    x_adv = x0.clone()
    for _ in range(steps):
        grad = nes_gradient(model, x_adv, y)
        x_adv = x_adv + step_size * grad.sign()
        delta = (x_adv - x0).clamp(-epsilon, epsilon)
        x_adv = (x0 + delta).clamp(0, 1).detach()
    return x_adv
```

This sketch assumes score access sufficient to compute cross-entropy from logits. A real API may return only labels, rounded probabilities, top-$k$ outputs, or rate-limited responses; the attack and query accounting must match that interface.

## Common pitfalls

- Calling an attack black-box even though it uses gradients from the exact target model.
- Ignoring query counts or reporting only final success after unlimited retries.
- Comparing score-based attacks with decision-based attacks as if they had the same information.
- Forgetting that transfer-only attack construction uses no target feedback; tuning on target failures changes the threat model.
- Treating low transfer success as a proof of robustness against white-box or high-query attacks.
- Estimating gradients through logits when the deployed API exposes only labels.
- Omitting failed attempts from median-query or success-rate reporting.

## Connections

- [Threat models and attack taxonomy](/cs/adversarial-attacks/threat-models-and-attack-taxonomy) defines score-query, decision-query, and transfer-only access.
- [White-box attacks](/cs/adversarial-attacks/white-box-attacks) are the gradient-access baseline that black-box attacks approximate or replace.
- [Gradient masking and obfuscation](/cs/adversarial-attacks/gradient-masking-and-obfuscation) explains why black-box attacks can sometimes outperform naive white-box attacks against broken defenses.
- [Evaluation and benchmarks](/cs/adversarial-attacks/evaluation-and-benchmarks) covers AutoAttack, adaptive evaluation, and reporting discipline.
- [Machine learning](/cs/machine-learning/intro) gives the model-fitting background for surrogate models.

## Further reading

- Papernot et al., work on substitute models and transfer attacks.
- Chen et al., "ZOO: Zeroth Order Optimization Based Black-box Attacks to Deep Neural Networks."
- Ilyas et al., work on black-box adversarial attacks with limited queries and priors.
- Uesato et al., work on adversarial risk and black-box attacks.
- Andriushchenko et al., "Square Attack: A Query-Efficient Black-Box Adversarial Attack via Random Search."
