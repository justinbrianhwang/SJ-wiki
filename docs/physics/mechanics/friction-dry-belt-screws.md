---
title: "Friction: Dry Contact, Belts, and Screws"
sidebar_position: 7
---

# Friction: Dry Contact, Belts, and Screws

Friction turns statics from pure equality into a problem with inequalities and impending motion. A normal force may be determined by force balance, but the friction force adjusts as needed up to a limit. That limit depends on the contact model and on whether the surfaces are sticking, sliding, wrapping, or acting through a screw thread.

This page collects the engineering friction models most often used in statics: dry Coulomb friction, belt friction, and square-thread screw friction. These models are idealizations, but they are practical when the surfaces are dry, the contact state is known or can be tested, and the goal is a first-order force estimate rather than detailed tribology.

## Definitions

For dry contact, the normal reaction $N$ acts perpendicular to the contact surface. The friction force $F$ acts tangent to the surface and opposes relative motion or impending relative motion.

In **static friction**, the surfaces do not slip. The friction magnitude satisfies

$$
|F|\le \mu_s N,
$$

where $\mu_s$ is the coefficient of static friction. The actual value of $F$ is whatever equilibrium requires, up to the maximum.

At **impending slip**,

$$
|F|=\mu_s N.
$$

In **kinetic friction**, the surfaces are sliding. The usual model is

$$
|F|=\mu_k N,
$$

where $\mu_k$ is the coefficient of kinetic friction. Typically $\mu_k\lt\mu_s$, though measured values depend on materials, speed, lubrication, and surface condition.

The **friction angle** $\phi$ is defined by

$$
\tan\phi=\mu.
$$

At impending slip, the resultant contact force is tilted by angle $\phi$ from the normal.

For a flexible belt or rope wrapped around a fixed drum through wrap angle $\beta$ in radians, the **capstan equation** is

$$
\frac{T_{\text{tight}}}{T_{\text{slack}}}=e^{\mu\beta}
$$

at impending slip. This assumes a flexible belt, uniform coefficient of friction, and no belt bending stiffness effects.

For a square-thread screw, the lead angle $\lambda$ satisfies

$$
\tan\lambda=\frac{l}{2\pi r_m},
$$

where $l$ is the lead per revolution and $r_m$ is the mean thread radius. Thread friction is often modeled with the friction angle $\phi=\tan^{-1}\mu$.

## Key results

The most important dry-friction result is that static friction is not automatically $\mu_sN$. It is bounded:

$$
-\mu_sN\le F\le \mu_sN.
$$

Use equality only when the problem states impending motion or when a trial equilibrium solution reaches the friction limit. A typical procedure is:

1. Assume the body sticks.
2. Solve equilibrium for the required friction force.
3. Check whether $\vert F\vert \le \mu_sN$.
4. If the check fails, sticking is impossible and motion or another contact state must be analyzed.

For a block on an incline at angle $\theta$, with no other applied forces, impending downward sliding occurs when

$$
mg\sin\theta=\mu_smg\cos\theta,
$$

so

$$
\tan\theta=\mu_s.
$$

This is a useful interpretation of the friction angle.

For belt friction, consider a small belt element. Tangential equilibrium leads to

$$
dT=\mu T\,d\theta
$$

at impending slip, and integration gives

$$
\ln\left(\frac{T_2}{T_1}\right)=\mu\beta.
$$

The result is exponential: more wrap angle produces a large holding advantage.

For square-thread screws, a common torque estimate for raising a load $W$ is

$$
M_{\text{raise}}=Wr_m\tan(\lambda+\phi),
$$

and for lowering,

$$
M_{\text{lower}}=Wr_m\tan(\phi-\lambda)
$$

when $\phi\gt\lambda$. If $\phi\gt\lambda$, the screw is self-locking in the simplified model; the load will not back-drive the screw without applied torque. If $\phi\lt\lambda$, the screw can overhaul.

These equations neglect collar friction. If collar friction is present, add an additional collar torque such as $\mu_cWR_c$ for a simple mean collar radius model.

Friction problems should also be read as contact-state problems. The equations for a body at rest, a body just about to slip, and a body already sliding are not the same model with different numbers; they are different assumptions about the contact. A good solution states the assumed tendency of motion before assigning the friction direction. If the solved static friction force changes sign, the assumed tendency was opposite. If its magnitude exceeds $\mu_sN$, the assumed sticking state cannot exist. If the normal force solves as negative, the contact has opened and the friction model at that contact is invalid because dry friction requires compression.

The friction cone gives a compact geometric test. At a rough point contact, the resultant contact force must lie inside a cone whose half-angle is $\phi_s=\tan^{-1}\mu_s$ measured from the normal. For a 2D contact this is a wedge. If equilibrium demands a contact resultant outside that wedge, sticking is impossible. This viewpoint is helpful for ladders, wedges, blocks with multiple contacts, and machine elements where the normal and friction components are easier to visualize as one resultant reaction.

For screws and wedges, friction can either help hold a load or make motion inefficient. A self-locking screw is useful in a jack because the load does not descend by itself, but the same friction means extra input torque is needed to raise the load. The ideal equations on this page are therefore best treated as force estimates; real designs also check thread form, bearing friction, material strength, wear, lubrication, and safety factors.

## Visual

```mermaid
flowchart TD
  A[Friction problem] --> B{Contact slipping?}
  B -->|no or unknown| C[Static friction: solve required F]
  C --> D{Is |F| <= mu_s N?}
  D -->|yes| E[Sticking equilibrium valid]
  D -->|no| F[Sticking impossible; use impending or kinetic model]
  B -->|sliding| G[Kinetic friction F = mu_k N]
  B -->|belt wrap| H[Capstan equation]
  B -->|screw thread| I[Friction angle and lead angle]
```

| Model | Governing relation | Equality means | Main caution |
|---|---|---|---|
| Static dry friction | $\vert F\vert \le \mu_sN$ | Impending slip only | Do not set equality automatically |
| Kinetic dry friction | $\vert F\vert =\mu_kN$ | Sliding contact | Direction opposes relative motion |
| Belt friction | $T_2/T_1=e^{\mu\beta}$ | Impending slip | $\beta$ must be in radians |
| Screw friction | $M=Wr_m\tan(\lambda+\phi)$ | Raising load, square thread | Collar torque may be separate |

## Worked example 1: Block on a rough incline

**Problem.** A $40$ kg block rests on a $25^\circ$ incline. The coefficient of static friction is $\mu_s=0.35$. Determine whether it remains at rest. If it does, find the friction force. Use $g=9.81$ m/s$^2$.

**Method.** Assume static equilibrium. Resolve weight into components normal and parallel to the incline. Solve for required friction and compare with $\mu_sN$.

1. Weight:

$$
W=mg=40(9.81)=392.4\ \text{N}.
$$

2. Components relative to the plane:

$$
W_\parallel=W\sin25^\circ=392.4(0.4226)=165.8\ \text{N}.
$$

This component tends to pull the block down the plane.

$$
W_\perp=W\cos25^\circ=392.4(0.9063)=355.7\ \text{N}.
$$

3. Normal equilibrium:

$$
N-W_\perp=0,\qquad N=355.7\ \text{N}.
$$

4. Tangential equilibrium requires friction up the plane:

$$
F-W_\parallel=0,\qquad F=165.8\ \text{N}.
$$

5. Maximum static friction:

$$
F_{\max}=\mu_sN=0.35(355.7)=124.5\ \text{N}.
$$

6. Compare:

$$
165.8\ \text{N}\gt124.5\ \text{N}.
$$

The required static friction exceeds the available maximum. The checked conclusion is

$$
\boxed{\text{The block cannot remain at rest; it will slide down the incline.}}
$$

At impending slip, friction would act up the incline with magnitude $124.5$ N, but that is not enough to balance the downhill component of weight.

## Worked example 2: Belt holding force around a drum

**Problem.** A rope wraps around a fixed drum through $210^\circ$. The coefficient of static friction is $\mu_s=0.28$. If the slack-side tension is $150$ N, find the largest tight-side tension that can be held without slipping.

**Method.** Use the capstan equation at impending slip. Convert the wrap angle to radians.

1. Convert angle:

$$
\beta=210^\circ\left(\frac{\pi}{180^\circ}\right)=3.665\ \text{rad}.
$$

2. Capstan relation:

$$
\frac{T_{\text{tight}}}{T_{\text{slack}}}=e^{\mu\beta}.
$$

3. Substitute:

$$
T_{\text{tight}}=150e^{0.28(3.665)}.
$$

4. Compute exponent:

$$
0.28(3.665)=1.026.
$$

5. Exponential factor:

$$
e^{1.026}=2.790.
$$

6. Tight-side tension:

$$
T_{\text{tight}}=150(2.790)=418.5\ \text{N}.
$$

The checked answer is

$$
\boxed{T_{\text{tight,max}}\approx 419\ \text{N}.}
$$

If the applied tight-side tension is less than this, static friction can supply the difference. If it is larger, the rope slips with the tight side moving relative to the drum.

## Code

```python
import math

def block_on_incline(mass, theta_deg, mu_s, g=9.81):
    theta = math.radians(theta_deg)
    W = mass * g
    required = W * math.sin(theta)
    normal = W * math.cos(theta)
    maximum = mu_s * normal
    return required, normal, maximum, required <= maximum

required, normal, maximum, sticks = block_on_incline(40.0, 25.0, 0.35)
print(f"required friction = {required:.1f} N")
print(f"normal force = {normal:.1f} N")
print(f"max static friction = {maximum:.1f} N")
print("sticks?", sticks)

mu = 0.28
beta = math.radians(210.0)
T_slack = 150.0
T_tight = T_slack * math.exp(mu * beta)
print(f"tight-side limit = {T_tight:.1f} N")
```

## Common pitfalls

- Setting $F=\mu_sN$ even when the contact is merely sticking.
- Forgetting to test whether the required static friction is within its limit.
- Drawing friction in the direction of motion rather than opposite impending or relative motion.
- Using degrees instead of radians in the belt-friction exponent.
- Confusing tight side and slack side in the capstan equation.
- Ignoring collar friction in screw problems when the problem states a collar is present.
- Assuming coefficients of friction are exact material constants; they are model parameters with experimental scatter.

## Connections

- [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium)
- [Particle equilibrium](/physics/mechanics/particle-equilibrium)
- [Work-energy methods](/physics/mechanics/work-energy-methods)
- [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)
