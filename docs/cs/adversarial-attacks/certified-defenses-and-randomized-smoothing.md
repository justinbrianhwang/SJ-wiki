---
title: Certified Defenses and Randomized Smoothing
sidebar_position: 8
---

# Certified Defenses and Randomized Smoothing

Empirical defenses try strong attacks and report whether the model survives. Certified defenses make a different kind of claim: within a specified perturbation set, no adversarial example exists for a particular input. This distinction is essential. A failed PGD attack is evidence; a valid certificate is a proof under assumptions.

The field contains many certification approaches, including interval bound propagation, linear relaxations such as CROWN-style methods, convex relaxations, exact verification for small networks, and randomized smoothing. Randomized smoothing is especially important because it scales to large classifiers and gives clean $\ell_2$ certificates by wrapping a base classifier with Gaussian noise.

## Definitions

Let $h(x)$ be a classifier. A **pointwise robustness certificate** at $(x,y)$ with radius $r$ under norm $p$ proves:

$$
\forall x' \text{ such that } \|x'-x\|_p \le r,\quad h(x') = y.
$$

A certificate is **sound** if every certified point is truly robust under the stated assumptions. It may be conservative: some robust points may not be certified.

A **certified accuracy curve** reports the fraction of test examples that are both correctly classified and certified at radius $r$:

$$
\mathrm{CertAcc}(r)
=
\frac{1}{n}\sum_{i=1}^n
\mathbf{1}\left[h(x_i)=y_i \ \text{and certificate radius at } x_i \ge r\right].
$$

**Randomized smoothing** builds a smoothed classifier $g$ from a base classifier $f$:

$$
g(x) = \arg\max_c \Pr_{\eta \sim \mathcal{N}(0,\sigma^2 I)}(f(x+\eta)=c).
$$

If class $A$ has sufficiently higher probability than every other class under Gaussian noise, then $g$ is certifiably robust in $\ell_2$. A common form of the radius is:

$$
R = \frac{\sigma}{2}
\left(
\Phi^{-1}(p_A) - \Phi^{-1}(p_B)
\right),
$$

where $p_A$ is a lower confidence bound on the top-class probability, $p_B$ is an upper confidence bound on the runner-up probability, and $\Phi^{-1}$ is the inverse standard normal CDF.

**Interval Bound Propagation (IBP)** propagates lower and upper activation bounds through the network. **Linear bound propagation** methods propagate affine upper and lower relaxations. **Convex relaxation** methods replace the nonconvex neural network verification problem with a tractable relaxation that upper-bounds worst-case loss or lower-bounds margins.

## Key results

Certification is threat-model-specific. A certificate for $\ell_2$ radius $0.5$ does not imply robustness to $\ell_\infty$ radius $8/255$, patches, rotations, corruptions, or semantic edits. The certificate is only as broad as the perturbation set and assumptions used by the verifier.

For classifiers, many verifiers reason about margins. Let $z_k(x)$ be the logit for class $k$. To certify class $y$, it is enough to prove:

$$
z_y(x') - z_j(x') > 0
\quad \text{for all } j \ne y
\quad \text{and all } x' \in B_p(x,\epsilon).
$$

Equivalently, prove a lower bound on every margin:

$$
\underline{m}_{y,j}
\le
\min_{x' \in B_p(x,\epsilon)}
\left(z_y(x') - z_j(x')\right),
$$

and show $\underline{m}_{y,j} \gt  0$ for all $j \ne y$. Bound-propagation and relaxation methods differ in how tightly and efficiently they compute these lower bounds.

Randomized smoothing gives a probabilistic certificate with statistical confidence. Since $p_A$ and $p_B$ are estimated by sampling noisy inputs, the implementation must report sample counts, confidence level, abstention rule, noise level $\sigma$, and base classifier training procedure. If the top class is not sufficiently likely, the smoothed classifier abstains rather than certifying.

Certified training often optimizes a surrogate upper bound on worst-case loss. For IBP-style training, the model is trained so interval bounds remain tight enough to prove positive margins. A common practical pattern is to warm up the perturbation radius or the weight on certified loss, because training from the full robust objective can be unstable.

The central tradeoff is tightness versus scalability. Exact verification is tight but limited to small networks or small inputs. Loose bounds scale but certify smaller radii. Randomized smoothing scales well and gives strong $\ell_2$ certificates, but it requires many noisy samples at inference and is naturally tied to Gaussian noise and $\ell_2$ geometry.

Certification also has a workflow distinction between prediction and certification. A smoothed classifier may use a modest number of samples to predict a label, then many more samples to certify that label with a chosen confidence level. A bound-propagation verifier may first run the ordinary network for a prediction, then run a separate bound computation to prove all competing logits stay below the predicted logit. These extra steps affect latency and should be included in the system claim. A certificate that is too slow for deployment may still be scientifically useful, but it is not the same as a cheap runtime defense.

Certificates can be abstaining by design. If the verifier cannot prove the margin or the smoothing vote is not decisive, the honest result is "not certified," not "not robust." This conservatism is why certified accuracy is usually lower than empirical robust accuracy.

## Visual

```mermaid
flowchart TB
  Input["Input x with label y and threat set B_p(x, epsilon)"]

  subgraph Smooth["Randomized smoothing certificate"]
    direction TB
    Noise["Sample Gaussian noise eta_i ~ N(0, sigma^2 I)"]
    Noisy["Evaluate base classifier f(x + eta_i) for n samples"]
    Counts["Class counts: top class A, runner-up B"]
    Bounds["Confidence bounds: p_A lower, p_B upper"]
    Radius["Certified L2 radius: R = sigma/2 * (Phi^-1(p_A) - Phi^-1(p_B))"]
    Decision{"Radius meets target and A = y?"}
    SmoothCert["Certified robust prediction inside L2 ball"]
    Abstain["Abstain / not certified"]
    Noise --> Noisy --> Counts --> Bounds --> Radius --> Decision
    Decision -->|"Yes"| SmoothCert
    Decision -->|"No"| Abstain
  end

  subgraph IBP["Interval bound propagation through a small network"]
    direction TB
    Box["Input interval: lower_0 = x - epsilon, upper_0 = x + epsilon"]
    Linear1["Affine/conv layer: bound W x + b with sign-split weights"]
    ReLU1["#quot;ReLU interval: [max(0, lower), max(0, upper)"]"]
    Linear2["Next affine layer bounds"]
    Logits["Logit intervals: lower_j, upper_j"]
    Margin["Worst-case margin: lower_y - max_{j != y} upper_j"]
    IBPCert{"Worst-case margin positive?"}
    Proven["Certified no class change in input box"]
    NotProven["Not proven: bound too loose or model not robust"]
    Box --> Linear1 --> ReLU1 --> Linear2 --> Logits --> Margin --> IBPCert
    IBPCert -->|"Yes"| Proven
    IBPCert -->|"No"| NotProven
  end

  subgraph Relax["Other verifier families"]
    direction TB
    Crown["CROWN / linear relaxations: tighter affine upper/lower bounds"]
    Convex["Convex relaxations or branch-and-bound"]
    Exact["Exact small-network verification"]
    Crown --> CertCurve["Certified accuracy vs radius curve"]
    Convex --> CertCurve
    Exact --> CertCurve
  end

  Input --> Noise
  Input --> Box
  SmoothCert --> CertCurve
  Proven --> CertCurve
  Abstain --> CertCurve
  NotProven --> CertCurve
```

This diagram shows randomized smoothing and IBP as two different certificate-producing architectures. Smoothing certifies a probabilistic decision radius from noisy votes, while IBP pushes lower and upper activation bounds layer by layer until the final logit margin either proves robustness or exposes a loose/failed certificate.

| Method | Certificate norm or set | Main object bounded | Strength | Limitation |
|---|---|---|---|---|
| Randomized smoothing | Usually $\ell_2$ | Class probabilities under Gaussian noise | Scales to large models | Sampling cost, abstentions, $\ell_2$ focus |
| IBP | Commonly $\ell_\infty$ | Activation intervals and logits | Fast and trainable | Bounds can be loose |
| CROWN-style bounds | $\ell_p$ variants depending method | Linear relaxations of network | Tighter than simple intervals | More complex and costly |
| Convex relaxations | Norm-bounded sets | Relaxed worst-case margins | Sound and often tighter | Scalability limits |
| Exact verification | Specified finite network/input setting | Exact satisfiability or optimization | Strongest proof | Usually small-scale |

## Worked example 1: Certified accuracy from radii

Problem: A test set has five examples. Their certified radii are:

$$
0.10,\quad 0.25,\quad 0.00,\quad 0.40,\quad 0.18.
$$

The third example is misclassified, so its radius is reported as $0$. Compute certified accuracy at radius $r=0.20$.

1. Certified accuracy at $r=0.20$ counts examples with radius at least $0.20$.

2. Check each radius:

$$
0.10 < 0.20 \quad \text{not counted}
$$

$$
0.25 \ge 0.20 \quad \text{counted}
$$

$$
0.00 < 0.20 \quad \text{not counted}
$$

$$
0.40 \ge 0.20 \quad \text{counted}
$$

$$
0.18 < 0.20 \quad \text{not counted}
$$

3. Count:

$$
\text{certified examples}=2.
$$

4. Divide by the test size:

$$
\mathrm{CertAcc}(0.20)=\frac{2}{5}=0.40.
$$

Checked answer: the certified accuracy at radius $0.20$ is $40\%$.

## Worked example 2: Randomized smoothing radius

Problem: A smoothed classifier uses $\sigma=0.50$. Suppose the top class has lower confidence bound $p_A=0.90$ and the runner-up has upper confidence bound $p_B=0.05$. Use approximate values $\Phi^{-1}(0.90)=1.282$ and $\Phi^{-1}(0.05)=-1.645$. Compute the certified $\ell_2$ radius.

1. Use the smoothing radius formula:

$$
R=\frac{\sigma}{2}(\Phi^{-1}(p_A)-\Phi^{-1}(p_B)).
$$

2. Substitute:

$$
R=\frac{0.50}{2}(1.282-(-1.645)).
$$

3. Compute the probability-margin term:

$$
1.282+1.645=2.927.
$$

4. Compute $\sigma/2$:

$$
\frac{0.50}{2}=0.25.
$$

5. Multiply:

$$
R=0.25(2.927)=0.73175.
$$

Checked answer: the certified $\ell_2$ radius is approximately $0.732$. If the statistical confidence bounds were weaker, the radius would shrink even with the same observed top class.

## Code

```python
import math
import torch

def certify_from_counts(count_top, count_runner_up, n, sigma, normal_icdf):
    # Simplified plug-in sketch. Production smoothing uses confidence bounds,
    # abstention rules, and careful binomial intervals.
    p_a = count_top / n
    p_b = count_runner_up / n
    if p_a <= p_b:
        return 0.0
    radius = 0.5 * sigma * (normal_icdf(torch.tensor(p_a)) - normal_icdf(torch.tensor(p_b)))
    return float(torch.clamp(radius, min=0.0))

@torch.no_grad()
def smoothed_predict(model, x, sigma=0.25, samples=128):
    counts = None
    for _ in range(samples):
        logits = model((x + sigma * torch.randn_like(x)).clamp(0.0, 1.0))
        preds = logits.argmax(dim=1)
        if counts is None:
            counts = torch.zeros(x.shape[0], logits.shape[1], device=x.device)
        counts.scatter_add_(1, preds[:, None], torch.ones_like(preds[:, None], dtype=counts.dtype))
    return counts.argmax(dim=1), counts
```

The code illustrates noisy voting, not a production certificate. Correct randomized-smoothing certification requires confidence intervals for $p_A$ and $p_B$, a fixed confidence level, and an abstain decision when the top class is not statistically dominant.

## Common pitfalls

- Calling a defense certified when it has only been tested against attacks.
- Reporting certified accuracy without the radius, norm, confidence level, verifier, and abstention policy.
- Comparing empirical robust accuracy with certified accuracy as if they measure the same thing.
- Forgetting that randomized smoothing certificates are usually $\ell_2$ certificates, not universal robustness claims.
- Using plug-in class probabilities without statistical confidence bounds.
- Certifying the wrong model, for example the base classifier instead of the smoothed classifier or a preprocessing-free version.
- Ignoring the clean-accuracy cost and inference-time sampling cost of certification.

## Connections

- [Mathematical formulation](/cs/adversarial-attacks/mathematical-formulation) defines pointwise robustness and robust risk.
- [Adversarial training](/cs/adversarial-attacks/adversarial-training) gives empirical robustness methods that can be combined with certified training.
- [Gradient masking and obfuscation](/cs/adversarial-attacks/gradient-masking-and-obfuscation) contrasts certificates with attacks that merely fail.
- [Evaluation and benchmarks](/cs/adversarial-attacks/evaluation-and-benchmarks) explains certified accuracy curves and benchmark reporting.
- [Robustness-accuracy tradeoff](/cs/adversarial-attacks/robustness-accuracy-tradeoff) discusses the cost of robustness objectives.

## Further reading

- Cohen, Rosenfeld, and Kolter, "Certified Adversarial Robustness via Randomized Smoothing."
- Gowal et al., work on interval bound propagation for certified robustness.
- Zhang et al., CROWN and related linear bound propagation methods.
- Wong and Kolter, work on provable defenses via convex outer adversarial polytopes.
- Salman et al., work combining adversarial training and randomized smoothing.
