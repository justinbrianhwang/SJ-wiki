---
title: Particle Equilibrium
sidebar_position: 3
---

# Particle Equilibrium

A particle model keeps the location and mass of a body but discards its size and orientation. It is appropriate when all relevant forces can be treated as concurrent and no requested quantity depends on rotation. Rings at cable junctions, small collars on guides, pin joints in trusses, and idealized knots are standard examples.

For a particle at rest, or moving with constant velocity in an inertial frame,

$$
\boxed{\sum \mathbf F=\mathbf 0}.
$$

There is no separate moment equation. Every force is applied at the same idealized point, so each has zero moment about that point. If support couples or the spacing between forces matters, the object must be modeled as a rigid body instead.

## The free-body diagram carries the model

Most errors occur before any equation is written. Isolate one particle and draw only forces exerted on it by bodies outside the chosen system. The equal and opposite force exerted by the particle belongs on the other body's diagram, not on the same one.

Common force models are specific about direction:

| Interaction | Force on the isolated particle | Restriction |
|---|---|---|
| Cable or rope | Tension along the cable, pulling away from the particle | An ideal cable cannot push |
| Two-force link | Force along the line joining its two pins | May be tension or compression |
| Smooth surface | Normal reaction perpendicular to the surface | No tangential component |
| Rough surface | Normal reaction plus friction tangent to the surface | Friction is limited by the contact law |
| Smooth slot or guide | Reaction normal to the guide | The guide allows motion along its tangent |
| Spring | Force along the spring | Magnitude follows its force-extension law |
| Gravity | Weight $m\mathbf g$ through the mass center | Usually vertical near Earth's surface |

Cable arrows should initially point away from the particle. If the solved tension is negative, the assumed cable-only model cannot realize that force: a slack cable supplies zero force rather than compression. A two-force link is different. One may assume its force points away from the joint; a negative result then means the link is in compression.

For a continuous massless cable passing over frictionless, massless pulleys, the tension magnitude is constant along the cable. A real capstan, accelerating pulley, or massive cable does not satisfy that idealization. Pulley geometry can also create several tension forces on one moving block; equal tension does not mean their vector sum equals one tension.

## Components and independent equations

In a plane,

$$
\sum F_x=0,
\qquad
\sum F_y=0.
$$

In three dimensions,

$$
\sum F_x=0,
\qquad
\sum F_y=0,
\qquad
\sum F_z=0.
$$

Axes can be chosen freely. Horizontal and vertical axes usually make weight simple; axes tangent and normal to an incline often make contact forces simple. The equations remain equivalent under a rotation of coordinates. A good choice reduces the number of forces that must be resolved, but does not create additional information.

Equation counting is necessary but not sufficient. A planar particle provides at most two independent scalar equations, so three unrelated unknown magnitudes cannot be found from equilibrium alone. Even two equations may fail to be independent if all unknown force directions are parallel. In matrix form,

$$
\begin{bmatrix}
u_{1x} & u_{2x} & \cdots\\
u_{1y} & u_{2y} & \cdots
\end{bmatrix}
\begin{bmatrix}
F_1\\F_2\\\vdots
\end{bmatrix}
=-\mathbf F_{\mathrm{known}}.
$$

The rank of the direction matrix determines how many independent combinations can be solved. Nearly parallel cable directions create a nearly singular system: a formal solution may exist, but small changes in geometry produce large changes in tension. This is also a physical warning, since shallow cables require large tension to produce a modest transverse component.

## Describing directions without guessing signs

In two dimensions, a force of magnitude $F$ making an angle $\theta$ counterclockwise from $+x$ is

$$
\mathbf F=F\cos\theta\,\mathbf i+F\sin\theta\,\mathbf j.
$$

For a cable from point $O$ to point $A$, the safer three-dimensional construction is

$$
\mathbf r_{OA}=\mathbf r_A-\mathbf r_O,
\qquad
\mathbf u_{OA}=\frac{\mathbf r_{OA}}{\lVert\mathbf r_{OA}\rVert},
$$

followed by

$$
\mathbf T_{OA}=T_{OA}\mathbf u_{OA}.
$$

Subtract endpoint coordinates in the direction the cable pulls. Each direction cosine must lie between $-1$ and $1$, and a unit-vector check should give

$$
\mathbf u\cdot\mathbf u=1.
$$

Rounding unit vectors too early can spoil a three-dimensional equilibrium check. Keep radicals or several decimal places until the final tensions are known.

## Three-force equilibrium and the force triangle

If exactly three nonparallel coplanar forces hold a particle in equilibrium, their vectors placed head-to-tail form a closed triangle:

$$
\mathbf F_1+\mathbf F_2+\mathbf F_3=\mathbf 0.
$$

The law of sines applied to this force triangle gives Lami's relation,

$$
\frac{F_1}{\sin\alpha_1}
=\frac{F_2}{\sin\alpha_2}
=\frac{F_3}{\sin\alpha_3},
$$

where $\alpha_1$ is the angle between the other two force directions, and similarly for the remaining terms. It is concise for a three-force joint, but component equations are harder to misuse when angles are given from different reference lines.

The geometry explains why a nearly horizontal suspension cable develops high tension. If two symmetric cables each make a small angle $\theta$ above horizontal while supporting weight $W$, horizontal components cancel and

$$
2T\sin\theta=W,
\qquad
T=\frac{W}{2\sin\theta}.
$$

As $\theta\to0$, the required tension becomes unbounded in the ideal model. No finite horizontal cable tension can supply a vertical resultant without some vertical component.

## Worked example: an asymmetric suspended ring

A ring supports a $500$ N downward load. The left cable is $35^\circ$ above horizontal and the right cable is $50^\circ$ above horizontal. Find both cable tensions.

Let $T_B$ denote the left tension and $T_C$ the right tension. Both arrows point away from the isolated ring. With $+x$ right and $+y$ up,

$$
\mathbf T_B=-T_B\cos35^\circ\,\mathbf i
+T_B\sin35^\circ\,\mathbf j,
$$

$$
\mathbf T_C=T_C\cos50^\circ\,\mathbf i
+T_C\sin50^\circ\,\mathbf j.
$$

Horizontal equilibrium gives

$$
-T_B\cos35^\circ+T_C\cos50^\circ=0,
$$

so

$$
T_C=\frac{T_B\cos35^\circ}{\cos50^\circ}.
$$

Vertical equilibrium is

$$
T_B\sin35^\circ+T_C\sin50^\circ-500=0.
$$

Substituting the first relation,

$$
T_B\left(\sin35^\circ+\cos35^\circ\tan50^\circ\right)=500.
$$

Using the trigonometric values without premature rounding,

$$
T_B=322.6\ \text{N}.
$$

Then

$$
T_C=\frac{322.6\cos35^\circ}{\cos50^\circ}
=411.2\ \text{N}.
$$

The component check is

$$
322.6\sin35^\circ+411.2\sin50^\circ
\approx500.0\ \text{N}.
$$

Both values are positive, so both cable assumptions are physically admissible. The steeper cable has the larger tension here because horizontal cancellation fixes a ratio between the two tensions; cable angle alone does not determine which is larger.

## Worked example: a collar on a smooth incline

A $20$ kg collar rests on a smooth guide inclined $30^\circ$ above horizontal. A cable pulls horizontally to the right. Find the cable tension and the guide's normal reaction.

The collar is a particle. Its forces are weight $W=mg$ downward, horizontal tension $T$, and normal reaction $N$ perpendicular to the guide. Choose tangent $s$ up the incline and normal $n$ away from it. The weight is

$$
W=20(9.81)=196.2\ \text{N}.
$$

The horizontal tension has tangential component $T\cos30^\circ$ and normal component directed into the guide with magnitude $T\sin30^\circ$. The weight has a downslope component $W\sin30^\circ$ and an into-guide component $W\cos30^\circ$.

Tangential equilibrium gives

$$
T\cos30^\circ-W\sin30^\circ=0,
$$

therefore

$$
T=W\tan30^\circ
=196.2(0.57735)
=113.3\ \text{N}.
$$

Normal equilibrium gives

$$
N-T\sin30^\circ-W\cos30^\circ=0.
$$

Thus

$$
\begin{aligned}
N&=113.3(0.5)+196.2(0.8660)\\
&=226.6\ \text{N}.
\end{aligned}
$$

The positive normal reaction confirms that the guide can maintain contact. Had the solution required $N\lt 0$, the assumed one-sided contact would have failed and the collar would separate from that surface.

## Worked example: three-dimensional cable support

A joint at $O=(0,0,0)$ supports a $900$ N downward load. Three cables run to $A=(3,0,4)$ m, $B=(-2,3,6)$ m, and $C=(-2,-3,6)$ m. Find their tensions.

The cable directions are

$$
\mathbf u_A=\frac{\langle3,0,4\rangle}{5}
=\left\langle\frac35,0,\frac45\right\rangle,
$$

$$
\mathbf u_B=\frac{\langle-2,3,6\rangle}{7},
\qquad
\mathbf u_C=\frac{\langle-2,-3,6\rangle}{7}.
$$

Equilibrium is

$$
T_A\mathbf u_A+T_B\mathbf u_B+T_C\mathbf u_C
-900\mathbf k=\mathbf0.
$$

Its components are

$$
\begin{aligned}
\frac35T_A-\frac27T_B-\frac27T_C&=0,\\
\frac37T_B-\frac37T_C&=0,\\
\frac45T_A+\frac67T_B+\frac67T_C&=900.
\end{aligned}
$$

The $y$ equation gives $T_B=T_C=T$ by symmetry. The $x$ equation then gives

$$
\frac35T_A-\frac47T=0,
\qquad
T_A=\frac{20}{21}T.
$$

Substitute into the vertical equation:

$$
\frac45\left(\frac{20}{21}T\right)
+\frac{12}{7}T=900.
$$

Combining terms,

$$
\left(\frac{16}{21}+\frac{36}{21}\right)T=900,
$$

so

$$
T=\frac{900(21)}{52}=363.46\ \text{N}.
$$

Finally,

$$
T_A=\frac{20}{21}(363.46)=346.15\ \text{N}.
$$

Therefore

$$
\boxed{T_A=346\ \text{N},\qquad
T_B=T_C=363\ \text{N}.}
$$

Equal $B$ and $C$ tensions cancel their $y$ components. Substitution into the other two components recovers zero horizontal resultant and $900$ N upward.

## Ideal pulleys: count forces on the chosen body

An ideal pulley changes the direction of a cable tension but does not automatically multiply its magnitude. Mechanical advantage comes from the number and orientation of cable segments pulling on the moving body. The free-body diagram must therefore be drawn for the body whose motion or support force is being studied.

As a simple example, a $600$ N load hangs from a movable pulley. One continuous ideal cable passes under the pulley, and both of its free segments are vertical. If the cable tension is $T$, the pulley-and-load assembly receives two upward forces, each of magnitude $T$. Equilibrium of that assembly gives

$$
2T-600=0,
$$

so

$$
T=300\ \text{N}.
$$

The support holding the fixed end of the cable carries one $300$ N cable force. A ceiling bracket supporting a separate fixed redirecting pulley may carry the vector sum of two cable tensions instead. Those are different bodies and need different free-body diagrams.

If the two segments supporting a movable pulley are inclined rather than vertical, their upward components support the load. For equal tensions and symmetric angles $\theta$ measured from horizontal,

$$
2T\sin\theta=W.
$$

The force advantage is then less than two unless the segments are vertical. Counting segments without resolving their directions gives the wrong answer whenever the geometry is not parallel to the load.

The equal-tension rule relies on the ideal assumptions. A pulley with rotational inertia needs unequal tensions to produce angular acceleration. Bearing friction can also create a tension difference. In a statics problem those effects may still be neglected deliberately, but the assumption belongs in the model rather than being inferred from the word “pulley.”

## Geometry, conditioning, and large tensions

Equilibrium can become sensitive even before it becomes impossible. For the symmetric two-cable suspension,

$$
T=\frac{W}{2\sin\theta}.
$$

At $\theta=30^\circ$, each cable carries $T=W$. At $\theta=5^\circ$, each carries about $5.74W$. A small error in a shallow angle then causes a substantial tension error. The joint may be perfectly balanced on paper while the cables are overloaded.

The three-dimensional analogue occurs when cable unit vectors lie nearly in one plane or nearly point in the same direction. Their component matrix is close to singular. Large positive and negative algebraic coefficients must cancel to produce the required load, so small coordinate changes can alter the solution sharply. If the solution requires a negative cable tension, the geometry does not support the load with those cables taut.

Support capability can often be assessed before solving. The resultant of nonnegative cable tensions must lie inside the cone generated by their pulling directions. To balance a known load, the opposite of that load must lie in this force cone. In two dimensions the cone is the angular sector between the outer cable directions. A load outside it cannot be balanced by those cables, regardless of their strength.

## Friction is an inequality until slipping is imminent

For a rough contact, static friction adjusts to the value required for equilibrium up to its limiting magnitude:

$$
|F|\le\mu_sN.
$$

The equality $\vert F\vert =\mu_sN$ applies only at impending slip. Setting it automatically can create a fictitious friction force when a smaller one would hold the particle. A sound procedure is to solve equilibrium for the required $F$ and $N$, then check the inequality.

Suppose a $100$ N block rests on a horizontal rough surface and is pulled horizontally by $20$ N. Equilibrium requires $N=100$ N and a $20$ N friction force opposing the pull. If $\mu_s=0.30$, the available limit is

$$
\mu_sN=30\ \text{N}.
$$

Since $20\lt 30$, the block can remain at rest and the actual friction is $20$ N, not $30$ N. If the pull rises to $35$ N, no static-equilibrium solution exists under the model because the required friction exceeds the limit. The problem then becomes one of kinetics, usually with a kinetic-friction law after sliding begins.

Friction direction should oppose impending or actual relative motion, not necessarily the applied force in isolation. On an incline with several loads, first infer which way the particle would tend to move without friction. If that tendency is uncertain, assume a direction, solve, and let the sign of $F$ correct the assumption.

## When equilibrium has no physical solution

Algebraic solvability does not guarantee that every assumed support can supply the computed force. Cables require nonnegative tension. Smooth unilateral contacts require nonnegative normal reaction. Dry friction must remain within its limiting inequality until impending motion is specified. A negative value can mean only that an arrow was assumed backward for a bidirectional member, or it can expose an invalid physical model.

An underdetermined system needs more information, not an arbitrary symmetry assumption. The missing information may come from another connected body's equilibrium, a geometric constraint, a prescribed force ratio, or deformation compatibility. Conversely, inconsistent equations often indicate omitted contact, an incorrect direction vector, or a body that actually accelerates.

## Checks before accepting a result

- Count independent unknown force magnitudes after the free-body diagram is complete. Counting arrows before assigning their directions can be misleading.
- Verify each cable or member unit vector from endpoint coordinates and check its length is one.
- Substitute the solved values into every component equation, including an equation not used after a symmetry reduction.
- Interpret negative results according to the force model. A compressive link is possible; a compressive ideal cable is not.
- Reconsider the particle idealization if a couple acts, forces are nonconcurrent, or support spacing affects the answer.
- Avoid rounding direction cosines until the final step, especially when cable directions are nearly dependent.

<div className="see-also">

See also: [Force vectors, resultants, and components](/physics/mechanics/force-vectors-resultants-components) · [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium) · [Trusses, frames, and machines](/physics/mechanics/trusses-frames-machines) · [Particle kinetics with Newton's second law](/physics/mechanics/particle-kinetics-newton)

</div>
