---
title: Work-Energy Methods
sidebar_position: 11
---

# Work-Energy Methods

Work-energy methods replace a time-by-time force analysis with a balance between work and changes in kinetic and potential energy. They are especially useful when the path is known, forces depend on position, or the final speed is wanted without needing the full time history. Energy is scalar, so it often reduces vector dynamics to a compact equation.

The method does not eliminate modeling. You still need a free-body diagram to identify forces and a kinematic description to write displacements or speeds. The advantage is that constraint forces that do no work, such as ideal normal reactions or pin reactions at fixed points, can often be ignored in the energy equation.

![A simple pendulum diagram shows a mass suspended from a pivot with its angular displacement marked.](https://commons.wikimedia.org/wiki/Special:FilePath/Simple_pendulum.svg)

*Figure: A pendulum makes the links among gravity, constraint forces, energy exchange, and small-oscillation models concrete. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Simple_pendulum.svg), Chris-martin, after Unc.hbar, public domain.*

## Definitions

The **work** done by a force $\mathbf{F}$ over a displacement path from position $1$ to position $2$ is

$$
U_{1\to2}=\int_1^2 \mathbf{F}\cdot d\mathbf{r}.
$$

If the force is constant and the displacement is straight,

$$
U=Fs\cos\theta,
$$

where $\theta$ is the angle between force and displacement.

The **kinetic energy** of a particle is

$$
T=\frac{1}{2}mv^2.
$$

For a rigid body in planar motion,

$$
T=\frac{1}{2}mv_G^2+\frac{1}{2}I_G\omega^2,
$$

where $G$ is the mass center.

The **work-energy principle** for a particle is

$$
T_1+U_{1\to2}=T_2.
$$

A force is **conservative** if its work depends only on endpoints, not on the path. Gravity near Earth's surface and ideal spring forces are standard conservative forces. Conservative forces can be represented by potential energy $V$:

$$
U_{1\to2}=V_1-V_2.
$$

Gravitational potential energy near Earth is

$$
V_g=mgy,
$$

where $y$ is vertical height. Spring potential energy is

$$
V_s=\frac{1}{2}kx^2
$$

for spring stretch or compression $x$ from its unstretched length.

The **conservation of mechanical energy** is

$$
T_1+V_1=T_2+V_2
$$

when only conservative forces do work.

## Key results

The work-energy method is often selected when the desired unknown is speed, distance, spring compression, stopping distance, or required work. It is less direct when the desired unknown is time or acceleration at an instant. If time matters, Newton's second law or impulse-momentum may be better.

For nonconservative forces, include their work explicitly:

$$
T_1+V_1+U_{\text{nc}}=T_2+V_2.
$$

Kinetic friction is a common nonconservative force. If a body slides distance $s$ under kinetic friction $\mu_kN$, the work of friction is

$$
U_f=-\mu_kNs
$$

when $N$ is constant and friction opposes motion. The negative sign matters because friction removes mechanical energy.

Power is the rate of doing work:

$$
P=\frac{dU}{dt}=\mathbf{F}\cdot\mathbf{v}
$$

for a force, and

$$
P=M\omega
$$

for a couple moment or torque rotating at angular speed $\omega$. Power methods are useful for engines, motors, brakes, and steady-rate devices.

For a spring with force magnitude $kx$, the work done by the spring as it changes from extension $x_1$ to $x_2$ is

$$
U_s=\frac{1}{2}kx_1^2-\frac{1}{2}kx_2^2.
$$

This sign convention follows the potential-energy relation. If the spring is being stretched farther, the spring does negative work on the moving body.

Constraint forces can do zero work, but only if their point of application has no displacement in the force direction. A normal force on a particle constrained to a smooth fixed surface does no work because displacement is tangent and normal force is perpendicular. A normal force on a rolling wheel can be subtler; static friction at a no-slip contact may do no work at the contact point, but the point and surface idealization must be clear.

Work-energy equations are endpoint equations. They relate state 1 to state 2 and do not describe what happens at every intermediate instant unless additional information is supplied. This is why the method can find a final speed after a block slides down a track, but it cannot by itself tell the time required. It also means that the path matters for nonconservative work. Gravity can be handled by height change alone, but kinetic friction generally requires the actual sliding distance.

For variable forces, use the integral definition rather than forcing a constant-force formula. A spring force, for example, changes with deformation:

$$
U_s=\int_{x_1}^{x_2}(-kx)\,dx.
$$

The result depends on the squares of the endpoint deformations, not on an average guessed from the final force unless that average is derived correctly. Similarly, if a force acts at an angle that changes along a path, the dot product $\mathbf{F}\cdot d\mathbf{r}$ is the safe expression.

Energy methods can also expose impossible assumptions. If an equation predicts negative kinetic energy, the selected final state cannot be reached under the assumed forces and path. If a normal force is needed to compute friction but is not known, energy alone may not be enough; a force balance normal to the path may have to be solved first.

## Visual

```mermaid
flowchart LR
  A[Known positions 1 and 2] --> B[Draw FBD and identify doing-work forces]
  B --> C{"Conservative?"}
  C -->|yes| D[Use potential energy V]
  C -->|no| E[Compute explicit work U_nc]
  D --> F["T1 + V1 + U_nc = T2 + V2"]
  E --> F
  F --> G["Solve for speed, distance, compression, or work"]
```

| Quantity | Formula | Sign or use |
|---|---|---|
| Particle kinetic energy | $T=\frac12 mv^2$ | Always nonnegative |
| Translational plus rotational kinetic energy | $T=\frac12 mv_G^2+\frac12I_G\omega^2$ | Planar rigid body |
| Work of constant force | $U=Fs\cos\theta$ | Positive if force aids motion |
| Gravity potential | $V_g=mgy$ | Higher means more potential |
| Spring potential | $V_s=\frac12kx^2$ | Depends on deformation from natural length |
| Power | $P=\mathbf{F}\cdot\mathbf{v}$ | Work rate |

## Worked example 1: Sliding block with friction and a spring

**Problem.** A $10$ kg block moves on a horizontal rough surface with initial speed $6$ m/s. It compresses a spring of stiffness $k=800$ N/m. The coefficient of kinetic friction is $\mu_k=0.20$. Find the maximum spring compression.

**Method.** Initial kinetic energy is spent on spring potential energy and negative work by friction. At maximum compression, the block's speed is zero.

1. Initial kinetic energy:

$$
T_1=\frac{1}{2}mv_1^2=\frac{1}{2}(10)(6^2)=180\ \text{J}.
$$

2. Final kinetic energy:

$$
T_2=0.
$$

3. Normal force on a horizontal surface:

$$
N=mg=10(9.81)=98.1\ \text{N}.
$$

4. Kinetic friction magnitude:

$$
F_k=\mu_kN=0.20(98.1)=19.62\ \text{N}.
$$

5. If maximum compression is $x$, friction acts over distance $x$, so

$$
U_f=-19.62x.
$$

6. Spring potential at maximum compression:

$$
V_s=\frac{1}{2}kx^2=\frac{1}{2}(800)x^2=400x^2.
$$

7. Energy equation:

$$
T_1+U_f=V_s.
$$

Equivalently,

$$
180-19.62x=400x^2.
$$

8. Rearrange:

$$
400x^2+19.62x-180=0.
$$

9. Solve the quadratic:

$$
x=\frac{-19.62+\sqrt{19.62^2+4(400)(180)}}{2(400)}.
$$

$$
x=\frac{-19.62+\sqrt{384.94+288000}}{800}.
$$

$$
x=\frac{-19.62+536.97}{800}=0.6467\ \text{m}.
$$

The negative root is physically meaningless for compression distance. The checked answer is

$$
\boxed{x_{\max}=0.647\ \text{m}.}
$$

Without friction, the compression would satisfy $180=400x^2$, giving $x=0.671$ m, so the smaller value is plausible.

## Worked example 2: Speed of a particle on a smooth circular track

**Problem.** A $2$ kg bead slides without friction on a fixed circular track. It starts from rest at height $1.5$ m above the lowest point. Find its speed at the lowest point.

**Method.** The normal force does no work because it is perpendicular to the bead's motion. Use conservation of mechanical energy.

1. Choose the lowest point as $y=0$. Initial height:

$$
y_1=1.5\ \text{m}.
$$

Final height:

$$
y_2=0.
$$

2. Initial kinetic energy:

$$
T_1=0
$$

because the bead starts from rest.

3. Initial potential energy:

$$
V_1=mgy_1=2(9.81)(1.5)=29.43\ \text{J}.
$$

4. Final potential energy:

$$
V_2=0.
$$

5. Final kinetic energy:

$$
T_2=\frac{1}{2}mv_2^2.
$$

6. Conservation of energy:

$$
T_1+V_1=T_2+V_2.
$$

$$
0+29.43=\frac{1}{2}(2)v_2^2+0.
$$

7. Solve:

$$
29.43=v_2^2,
$$

$$
v_2=5.425\ \text{m/s}.
$$

The checked answer is

$$
\boxed{v_2=5.43\ \text{m/s}.}
$$

The mass cancels from the calculation, as expected for frictionless gravitational motion.

## Code

```python
import math

def max_spring_compression(mass, speed, k, mu_k, g=9.81):
    T1 = 0.5 * mass * speed**2
    friction = mu_k * mass * g
    # Solve 0.5*k*x^2 + friction*x - T1 = 0.
    a = 0.5 * k
    b = friction
    c = -T1
    return (-b + math.sqrt(b*b - 4*a*c)) / (2*a)

x = max_spring_compression(10.0, 6.0, 800.0, 0.20)
print(f"maximum compression = {x:.4f} m")

height = 1.5
speed_bottom = math.sqrt(2.0 * 9.81 * height)
print(f"speed at bottom = {speed_bottom:.3f} m/s")
```

## Common pitfalls

- Using work-energy to find time directly.
- Including normal reactions or fixed-pin reactions that do no work in the energy equation.
- Forgetting negative work by kinetic friction.
- Treating static friction as always doing work; in ideal rolling without slip the contact point may have zero velocity.
- Using spring deformation from an arbitrary coordinate instead of from the spring's unstretched length.
- Mixing gravitational potential signs by changing the vertical datum mid-problem.
- Applying conservation of mechanical energy when nonconservative work is present.

## Connections

- [Particle kinetics with Newton's second law](/physics/mechanics/particle-kinetics-newton)
- [Particle kinematics](/physics/mechanics/particle-kinematics)
- [Impulse, momentum, and impact](/physics/mechanics/impulse-momentum-impact)
- [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)
