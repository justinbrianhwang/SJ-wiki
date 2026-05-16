---
title: White-Box Attacks
sidebar_position: 4
---

# White-Box Attacks

White-box attacks assume the attacker can inspect and differentiate the full model and defense. This is the standard stress test for adversarial robustness because it removes accidental secrecy: if a defense only works when the attacker does not know the preprocessing, loss, randomness, or architecture, the defense is brittle under a security interpretation.

Most white-box image attacks are variations on constrained optimization. They use gradients with respect to the input, not the weights, and search inside a threat set such as an $\ell_\infty$ or $\ell_2$ ball. This page gives the conceptual scaffold for FGSM, BIM/I-FGSM, PGD, momentum iterative attacks, Carlini-Wagner attacks, DeepFool, and elastic-net attacks with the original papers cited inline.

## Definitions

For a classifier $f_\theta$, loss $\mathcal{L}$, clean input $x$, label $y$, perturbation set $\Delta(x)$, and adversarial input $x_{\mathrm{adv}}=x+\delta$, the white-box untargeted attack problem is:

$$
\max_{\delta \in \Delta(x)}
\mathcal{L}(f_\theta(x+\delta), y).
$$

The attacker can compute:

$$
\nabla_x \mathcal{L}(f_\theta(x), y),
$$

and, when needed, gradients through preprocessing, random transformations, differentiable defenses, logit margins, or surrogate losses.

**FGSM** uses one first-order step:

$$
x_{\mathrm{adv}} =
\Pi_{[0,1]^d}
\left(x + \epsilon\,\mathrm{sign}(\nabla_x \mathcal{L}(f_\theta(x), y))\right).
$$

**BIM** or **I-FGSM** repeats small FGSM-like steps and clips after each step:

$$
x^{t+1} =
\Pi_{B_\infty(x,\epsilon)}
\left(x^t + \alpha\,\mathrm{sign}(\nabla_x \mathcal{L}(f_\theta(x^t), y))\right).
$$

**PGD** is the same projected-gradient idea, usually with a random start:

$$
x^0 = x + u,\qquad u \sim \mathrm{Uniform}([-\epsilon,\epsilon]^d).
$$

**Momentum iterative attacks** stabilize the direction by accumulating normalized gradients:

$$
g_{t+1} = \mu g_t + \frac{\nabla_x \mathcal{L}(f_\theta(x^t), y)}
{\|\nabla_x \mathcal{L}(f_\theta(x^t), y)\|_1}.
$$

**Carlini-Wagner attacks** often optimize a penalty objective such as:

$$
\min_\delta \|\delta\|_2^2 + c \cdot \Phi(x+\delta)
$$

with a loss $\Phi$ designed around logit margins and target success. **DeepFool** approximates the classifier locally by linear decision boundaries and iteratively moves to the nearest boundary.

## Key results

FGSM follows from the first-order Taylor approximation described in [mathematical formulation](/cs/adversarial-attacks/mathematical-formulation). It is fast, simple, and historically important, but it is not a strong standalone robustness evaluation. A model can resist one-step attacks while remaining vulnerable to iterative attacks.

PGD is the workhorse first-order attack for norm-bounded white-box evaluation. For $\ell_\infty$ attacks, one iteration is:

$$
\begin{aligned}
z^{t+1} &= x^t + \alpha\,\mathrm{sign}(\nabla_x \mathcal{L}(f_\theta(x^t), y)), \\
x^{t+1} &= \Pi_{[0,1]^d \cap B_\infty(x,\epsilon)}(z^{t+1}).
\end{aligned}
$$

The projection is coordinatewise:

$$
x^{t+1}
=
\min(1,\max(0,\min(x+\epsilon,\max(x-\epsilon,z^{t+1})))).
$$

For $\ell_2$ attacks, the update uses normalized gradients and projection onto the $\ell_2$ ball:

$$
z^{t+1} = x^t + \alpha
\frac{\nabla_x \mathcal{L}(f_\theta(x^t), y)}
{\|\nabla_x \mathcal{L}(f_\theta(x^t), y)\|_2}.
$$

An important evaluation point is that white-box attacks should be adaptive. If the defended model is:

$$
F(x) = f_\theta(T(x)),
$$

where $T$ is preprocessing, the gradient should be taken through $T$ when possible:

$$
\nabla_x \mathcal{L}(f_\theta(T(x)), y).
$$

If $T$ is nondifferentiable, the attacker may use BPDA, a differentiable approximation, score-based search, or another adaptive method. If the defense is randomized, the attacker may optimize the expected loss with expectation over transformations:

$$
\nabla_x \mathbb{E}_{\omega}[\mathcal{L}(F(x,\omega), y)]
\approx
\frac{1}{m}\sum_{i=1}^m
\nabla_x \mathcal{L}(F(x,\omega_i), y).
$$

Algorithm choice depends on the goal. FGSM is useful as a pedagogical baseline and for fast adversarial training variants. PGD is a strong default for $\ell_p$ evaluation. C&W-style attacks are useful when minimizing distortion or handling confidence margins. DeepFool estimates boundary distance and can be useful for geometric diagnostics. Momentum attacks often improve transferability because they avoid overfitting to local gradient noise.

Attack complexity is usually reported in gradient evaluations. FGSM uses one backward pass with respect to the input. PGD-$k$ uses roughly $k$ such backward passes per restart. A PGD-50 attack with 10 restarts is therefore much more expensive than PGD-10 with one restart, and the comparison matters when evaluating defenses. Hyperparameters should be strong enough to make the loss increase and the success rate stabilize. Step size, number of steps, random starts, loss choice, and targeted versus untargeted variants are not cosmetic details; they can change a robustness number by a large amount.

White-box access also includes preprocessing and postprocessing when those components affect the decision. If the system normalizes inputs, crops images, rejects examples, or ensembles several models, the attack should target that whole computation. Otherwise the evaluation is only white-box for a simplified model, not for the deployed system.

## Representative white-box methods

### Single-step sign attacks

Goodfellow, Shlens, and Szegedy [1] introduced the fast gradient sign method as the canonical first-order $\ell_\infty$ attack. The contribution was both algorithmic and explanatory: if a high-dimensional model behaves locally like a linear function, many tiny coordinatewise changes can add up to a large logit or loss change.

The method starts from the Taylor approximation:

$$
\mathcal{L}(f_\theta(x+\delta),y)
\approx
\mathcal{L}(f_\theta(x),y)
+ \delta^\top g,
\qquad
g=\nabla_x\mathcal{L}(f_\theta(x),y).
$$

Over $\|\delta\|_\infty\le\epsilon$, the linear term is maximized by:

$$
\delta^\star=\epsilon\,\mathrm{sign}(g),
\qquad
x_{\mathrm{adv}}=
\Pi_{[0,1]^d}(x+\delta^\star).
$$

For a targeted variant, descend the target-class loss:

$$
x_{\mathrm{adv}}=
\Pi_{[0,1]^d}
\left(x-\epsilon\,\mathrm{sign}(\nabla_x\mathcal{L}(f_\theta(x),y_t))\right).
$$

Compact pseudo-code:

```text
g = gradient(loss(model(x), y), x)
x_adv = clip(x + epsilon * sign(g), 0, 1)
```

This one backward pass is useful as a sanity check and teaching baseline. It is not a complete robustness evaluation because it trusts the loss surface at exactly the clean input.

### Iterative projected gradient methods

Kurakin, Goodfellow, and Bengio [2] popularized basic iterative methods, also called BIM or I-FGSM, by repeating small clipped sign-gradient steps. Madry et al. [3] made the projected-gradient view central to robust optimization: the same inner maximization used for evaluation also becomes the workhorse inner loop of adversarial training.

For $\ell_\infty$ attacks, initialize either at $x^0=x$ or at a random point in the ball:

$$
x^0=x+u,\qquad u_i\sim\mathrm{Uniform}[-\epsilon,\epsilon],
$$

then iterate:

$$
\begin{aligned}
z^{t+1} &= x^t+\alpha\,\mathrm{sign}(\nabla_x\mathcal{L}(f_\theta(x^t),y)),\\
x^{t+1} &= \Pi_{[0,1]^d\cap B_\infty(x,\epsilon)}(z^{t+1}).
\end{aligned}
$$

For $\ell_2$, replace the sign direction by a normalized gradient direction:

$$
z^{t+1}=x^t+\alpha
\frac{\nabla_x\mathcal{L}(f_\theta(x^t),y)}
{\|\nabla_x\mathcal{L}(f_\theta(x^t),y)\|_2}.
$$

The robust optimization objective from [3] is:

$$
\min_\theta
\mathbb{E}_{(x,y)}
\left[
\max_{\delta\in\Delta(x)}
\mathcal{L}(f_\theta(x+\delta),y)
\right].
$$

Compact pseudo-code:

```text
x_adv = random_point_in_ball(x, epsilon)
for step in 1..k:
    g = gradient(loss(model(x_adv), y), x_adv)
    x_adv = project_to_ball_and_pixels(x_adv + alpha * sign(g), x, epsilon)
return strongest_restart_by_loss
```

The important reporting fields are $\epsilon$, step size, number of steps, random starts, loss, clipping range, and whether gradients pass through the full defended pipeline.

### Momentum-smoothed transfer directions

Dong et al. [4] introduced momentum iterative FGSM to make iterative sign attacks less tied to noisy local gradients of one source model. The method is especially important for transfer attacks: it can craft examples on a source model or ensemble that cross decision boundaries shared by other models.

At step $t$, normalize the current gradient and accumulate a velocity:

$$
\tilde{g}_{t+1}
=
\frac{\nabla_x\mathcal{L}(f_\theta(x^t),y)}
{\|\nabla_x\mathcal{L}(f_\theta(x^t),y)\|_1},
\qquad
g_{t+1}=\mu g_t+\tilde{g}_{t+1}.
$$

Then update by the sign of the accumulated direction:

$$
x^{t+1}
=
\Pi_{[0,1]^d\cap B_\infty(x,\epsilon)}
\left(x^t+\alpha\,\mathrm{sign}(g_{t+1})\right).
$$

For an ensemble source, the loss can be averaged:

$$
\mathcal{L}_{\mathrm{ens}}(x,y)=
\sum_{m=1}^M w_m\mathcal{L}(f_m(x),y).
$$

Compact pseudo-code:

```text
momentum = 0
for step in 1..k:
    grad = gradient(loss(source_or_ensemble(x_adv), y), x_adv)
    grad = grad / mean(abs(grad))
    momentum = mu * momentum + grad
    x_adv = project_to_ball_and_pixels(x_adv + alpha * sign(momentum), x, epsilon)
```

Momentum is an optimizer change, not a new threat model. A report should separate white-box source success from black-box transfer success.

### Logit-margin and boundary-distance optimization

Carlini and Wagner [5] showed that defenses which appeared strong against earlier attacks could fail under an adaptive optimization objective based on logits and confidence margins. The best-known $\ell_2$ version solves a penalty problem:

$$
\min_\delta
\|\delta\|_2^2+c\,g(x+\delta)
\quad\text{subject to}\quad x+\delta\in[0,1]^d,
$$

with targeted logit-margin loss:

$$
g(x')=
\max\left(\max_{i\ne t} Z_i(x')-Z_t(x'),-\kappa\right).
$$

The confidence $\kappa$ requires the target logit to beat every other logit by a margin. A binary search over $c$ is part of the method because too small a penalty fails to attack and too large a penalty over-perturbs.

DeepFool, introduced by Moosavi-Dezfooli, Fawzi, and Frossard [6], asks a different but related question: how far is the nearest decision boundary under a local linear approximation? For binary affine score $f(x)=w^\top x+b$, the smallest $\ell_2$ move to the boundary is:

$$
r^\star=-\frac{f(x)}{\|w\|_2^2}w.
$$

For multiclass scores, compare each class boundary by:

$$
w_k=\nabla f_k(x)-\nabla f_{k_0}(x),
\qquad
b_k=f_k(x)-f_{k_0}(x),
\qquad
d_k=\frac{|b_k|}{\|w_k\|_2}.
$$

DeepFool moves toward the nearest $d_k$ and repeats until the predicted class changes. It is a geometric diagnostic and low-distortion attack, not a proof of the true nonlinear minimum.

Elastic-net attacks, introduced by Chen et al. [7], extend the C&W template with an $\ell_1$ term:

$$
\min_{x'}
c\,g(x')+\beta\|x'-x\|_1+\|x'-x\|_2^2
\quad\text{subject to}\quad x'\in[0,1]^d.
$$

The $\ell_1$ penalty encourages sparse perturbations. A proximal shrinkage step for one coordinate is:

$$
\mathrm{shrink}(z_i-x_i,\lambda)
=
\mathrm{sign}(z_i-x_i)\max(|z_i-x_i|-\lambda,0).
$$

Worked micro-example: if $x_i=0.50$, $z_i=0.57$, and $\lambda=0.03$, shrinkage gives $0.04$, so the updated coordinate is $0.54$ rather than $0.57$. That single coordinate illustrates the elastic-net tradeoff: move toward attack success, but pull small unnecessary changes back to zero.

Compact C&W-style pseudo-code:

```text
for c in binary_search_values:
    optimize norm(x_adv - x) + c * logit_margin_loss(x_adv)
    keep the lowest-distortion successful candidate
```

These attacks are most useful when the evaluation question is low distortion, confidence-margin behavior, metric sensitivity, or whether a suspicious defense only defeated a weak loss.

## Visual

| Attack | Main idea | Typical budget | Strengths | Limitations |
|---|---|---|---|---|
| FGSM | One signed gradient step | $\ell_\infty$ | Very fast, interpretable | Weak evaluation by itself |
| BIM/I-FGSM | Repeated clipped FGSM | $\ell_\infty$ | Stronger than FGSM | Can overfit local model, needs step tuning |
| PGD | Iterative projected ascent with random starts | $\ell_\infty$, $\ell_2$ | Standard first-order baseline | Still approximate, can miss masked gradients |
| MIM | PGD with momentum | $\ell_\infty$, $\ell_2$ | Often better transfer | Extra hyperparameter $\mu$ |
| C&W | Optimize norm plus logit-margin penalty | $\ell_2$, $\ell_\infty$, $\ell_0$ variants | Strong for low-distortion attacks | Slower, coefficient search matters |
| DeepFool | Iteratively cross local linear boundary | Often $\ell_2$ | Geometric boundary estimate | Not a full robust evaluation |

```mermaid
flowchart TB
  Clean["Clean input x, label y, model f_theta, loss L"]

  subgraph PGD["PGD / iterative first-order attack"]
    direction TB
    Init["Initialize x_adv^0 = x + random delta in epsilon-ball"]
    Grad["Compute gradient: grad_x L(f_theta(x_adv^t), y)"]
    Step["Gradient step: x_adv^t + alpha * sign(grad) or normalized grad"]
    Project["Project to threat set: Pi_{B_p(x, epsilon)}"]
    Clip["#quot;Clip to valid input range: [0, 1"] or normalized bounds"]
    Check{"More PGD steps or restarts?"}
    Select["Select highest-loss successful adversarial example"]
    Init --> Grad --> Step --> Project --> Clip --> Check
    Check -->|"Yes"| Grad
    Check -->|"No"| Select
  end

  subgraph CW["Carlini-Wagner-style optimization"]
    direction TB
    Param["Unconstrained variable w with tanh/box transform to x_adv"]
    Objective["Objective: norm(x_adv - x) + c * max(logit_y - max logit_other + kappa, 0)"]
    Optim["Adam/gradient descent on w"]
    Binary["Binary search or schedule for coefficient c"]
    Best["Keep lowest-distortion adversarial solution"]
    Param --> Objective --> Optim --> Binary
    Binary -->|"continue"| Objective
    Binary -->|"done"| Best
  end

  Clean --> Init
  Clean --> Param
  Select --> Verify["Verify misclassification, norm budget, clipping, targeted/untargeted goal"]
  Best --> Verify
  Verify --> Output(("Return x_adv with attack metadata"))
```

This diagram separates the two white-box loops that are often compressed into one arrow. PGD alternates gradient ascent, projection into the epsilon ball, and clipping to the valid input range, while C&W optimizes a distortion-plus-logit-margin objective with a coefficient search before returning the best verified adversarial example.

## Worked example 1: One FGSM step on normalized pixels

Problem: A grayscale input has four pixels:

$$
x = (0.20, 0.50, 0.90, 0.10).
$$

The input gradient is:

$$
g = \nabla_x \mathcal{L} = (-2.0, 0.3, 0.0, 5.0).
$$

Compute the FGSM adversarial input for $\epsilon=0.05$ and clip to $[0,1]$.

1. Take the elementwise sign:

$$
\mathrm{sign}(g)=(-1,1,0,1).
$$

2. Multiply by $\epsilon$:

$$
\delta = 0.05(-1,1,0,1)=(-0.05,0.05,0,0.05).
$$

3. Add to the input:

$$
x+\delta=(0.15,0.55,0.90,0.15).
$$

4. Clip to $[0,1]$. No coordinate is outside the interval, so the value is unchanged.

Checked answer:

$$
x_{\mathrm{adv}}=(0.15,0.55,0.90,0.15).
$$

The third pixel does not change because the gradient coordinate is zero. In real floating-point code, exactly zero gradients can also be a warning sign if they arise from nondifferentiable preprocessing or saturated activations.

## Worked example 2: Two PGD iterations with projection

Problem: Let:

$$
x=(0.50,0.50),\quad \epsilon=0.10,\quad \alpha=0.08.
$$

Assume the attack starts at $x^0=x$ and sees gradient signs:

$$
\mathrm{sign}(g^0)=(1,1), \qquad \mathrm{sign}(g^1)=(1,-1).
$$

Compute two $\ell_\infty$ PGD steps.

1. First gradient step:

$$
z^1=x^0+\alpha(1,1)=(0.58,0.58).
$$

2. Project to the $\ell_\infty$ ball around $x$. The allowed interval for each coordinate is $[0.40,0.60]$. The point $(0.58,0.58)$ is valid, so:

$$
x^1=(0.58,0.58).
$$

3. Second gradient step:

$$
z^2=x^1+\alpha(1,-1)=(0.66,0.50).
$$

4. Project coordinatewise to $[0.40,0.60]$:

$$
x^2=(0.60,0.50).
$$

5. Check the perturbation:

$$
x^2-x=(0.10,0.00), \qquad \|x^2-x\|_\infty=0.10.
$$

Checked answer: after two steps, $x^2=(0.60,0.50)$, exactly on the boundary of the allowed $\ell_\infty$ ball.

## Code

```python
import torch
import torch.nn.functional as F

def fgsm(model, x, y, epsilon):
    x_adv = x.detach().clone().requires_grad_(True)
    loss = F.cross_entropy(model(x_adv), y)
    loss.backward()
    with torch.no_grad():
        x_adv = x_adv + epsilon * x_adv.grad.sign()
        return x_adv.clamp(0.0, 1.0).detach()

def pgd_linf(model, x, y, epsilon, step_size, steps, restarts=1):
    best_x = x.detach()
    best_loss = torch.full((x.shape[0],), -float("inf"), device=x.device)

    for _ in range(restarts):
        x0 = x.detach()
        x_adv = (x0 + torch.empty_like(x0).uniform_(-epsilon, epsilon)).clamp(0.0, 1.0)

        for _ in range(steps):
            x_adv.requires_grad_(True)
            loss = F.cross_entropy(model(x_adv), y, reduction="sum")
            grad = torch.autograd.grad(loss, x_adv)[0]
            with torch.no_grad():
                x_adv = x_adv + step_size * grad.sign()
                delta = (x_adv - x0).clamp(-epsilon, epsilon)
                x_adv = (x0 + delta).clamp(0.0, 1.0)

        with torch.no_grad():
            losses = F.cross_entropy(model(x_adv), y, reduction="none")
            replace = losses > best_loss
            best_loss[replace] = losses[replace]
            best_x[replace] = x_adv[replace]

    return best_x.detach()
```

This code uses gradients with respect to the input, not the model parameters. In a real evaluation, the model should be in `eval()` mode unless the threat model intentionally allows batch-statistics behavior during attack.

## Common pitfalls

- Calling FGSM robustness a strong white-box evaluation. It is a baseline, not a complete test.
- Forgetting random starts and restarts for PGD, especially when evaluating defenses.
- Taking gradients through a different pipeline than the deployed model uses.
- Leaving dropout, batch normalization, or stochastic layers in an unintended mode during evaluation.
- Using a step size so large that PGD bounces around and looks weaker than it is.
- Reporting only average loss increase instead of attack success rate or robust accuracy.
- Ignoring adaptive methods such as BPDA or EOT when the defense uses nondifferentiable or randomized preprocessing.

## Connections

- [Mathematical formulation](/cs/adversarial-attacks/mathematical-formulation) derives FGSM and projected-gradient updates.
- [Gradient masking and obfuscation](/cs/adversarial-attacks/gradient-masking-and-obfuscation) explains why white-box attacks must be adaptive.
- [Adversarial training](/cs/adversarial-attacks/adversarial-training) uses [PGD-like attacks](/cs/adversarial-attacks/white-box-attacks#iterative-projected-gradient-methods) inside training.
- [Evaluation and benchmarks](/cs/adversarial-attacks/evaluation-and-benchmarks) discusses AutoAttack, restarts, and benchmark discipline.
- [Deep learning](/cs/deep-learning/intro) gives the backpropagation machinery used to compute input gradients.

## Further reading

- Goodfellow, Shlens, and Szegedy, "Explaining and Harnessing Adversarial Examples."
- Kurakin, Goodfellow, and Bengio, "Adversarial Examples in the Physical World."
- Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks."
- Dong et al., "Boosting Adversarial Attacks with Momentum."
- Carlini and Wagner, "Towards Evaluating the Robustness of Neural Networks."
- Moosavi-Dezfooli, Fawzi, and Frossard, "DeepFool: A Simple and Accurate Method to Fool Deep Neural Networks."

## References

[1] I. J. Goodfellow, J. Shlens, C. Szegedy. *Explaining and Harnessing Adversarial Examples*. ICLR 2015.
[2] A. Kurakin, I. J. Goodfellow, S. Bengio. *Adversarial Examples in the Physical World*. ICLR Workshop 2017.
[3] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, A. Vladu. *Towards Deep Learning Models Resistant to Adversarial Attacks*. ICLR 2018.
[4] Y. Dong, F. Liao, T. Pang, H. Su, J. Zhu, X. Hu, J. Li. *Boosting Adversarial Attacks with Momentum*. CVPR 2018.
[5] N. Carlini, D. Wagner. *Towards Evaluating the Robustness of Neural Networks*. IEEE Symposium on Security and Privacy 2017.
[6] S.-M. Moosavi-Dezfooli, A. Fawzi, P. Frossard. *DeepFool: A Simple and Accurate Method to Fool Deep Neural Networks*. CVPR 2016.
[7] P.-Y. Chen, Y. Sharma, H. Zhang, J. Yi, C.-J. Hsieh. *EAD: Elastic-Net Attacks to Deep Neural Networks via Adversarial Examples*. AAAI 2018.
