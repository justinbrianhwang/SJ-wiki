---
title: Internal Forces in Beams
sidebar_position: 6
---

# Internal Forces in Beams

External equilibrium finds support reactions, but it does not directly show what happens inside a beam. A beam may be in overall equilibrium while different cross sections carry different axial force, shear force, and bending moment. Internal force diagrams turn those hidden resultants into functions of position, making them essential for later stress, deflection, and design work.

The core idea is an imaginary cut. Slice the beam at a chosen position, keep one side, and replace the removed side by internal resultants on the cut face. Then write equilibrium of the retained piece. Repeating this process along the span produces axial-force, shear-force, and bending-moment diagrams.

## Definitions

A **beam** is a slender member that primarily carries transverse loads. A general planar cut exposes three internal resultants:

$$
N(x)=\text{axial force},\qquad V(x)=\text{shear force},\qquad M(x)=\text{bending moment}.
$$

Sign conventions vary. This page uses a common convention for the **left segment** of a beam:

- Positive $N$ pulls the cut face to the right, creating tension in the left segment.
- Positive $V$ acts upward on the cut face of the left segment.
- Positive $M$ is counterclockwise on the cut face of the left segment, producing sagging curvature for many standard beam diagrams.

The important rule is not which convention is chosen, but that it is used consistently.

A **shear-force diagram** plots $V(x)$ along the beam. A **bending-moment diagram** plots $M(x)$. If a distributed load $w(x)$ is taken positive downward, common differential relations are

$$
\frac{dV}{dx}=-w(x),
$$

$$
\frac{dM}{dx}=V(x).
$$

These relations are local equilibrium statements for a small beam element. They are powerful checks on hand diagrams.

A **point load** creates a jump in the shear diagram. A **concentrated couple** creates a jump in the moment diagram. A uniformly distributed load creates a linearly changing shear and a quadratic bending moment.

## Key results

For any beam segment, the internal force functions come from equilibrium of a cut part:

$$
\sum F_x=0,\qquad \sum F_y=0,\qquad \sum M_{\text{cut}}=0.
$$

Before cutting, always solve support reactions from the whole beam unless the chosen section avoids them. Reactions are external forces and therefore appear in the segment equilibrium.

The load-shear-moment relationships give diagram slopes:

$$
\Delta V=-\int_{x_1}^{x_2}w(x)\,dx,
$$

$$
\Delta M=\int_{x_1}^{x_2}V(x)\,dx.
$$

Thus the area under the load diagram changes shear, and the area under the shear diagram changes moment. These area relations are useful for checking diagrams without redoing every cut.

For a simply supported beam with no applied end couples, the bending moment at a pin or roller end is zero. A fixed support can provide a reaction moment, so the end bending moment need not be zero. At an internal pin, the bending moment transmitted through the pin is zero, although shear and axial forces may pass through.

Maximum or minimum bending moment occurs where

$$
V(x)=0
$$

inside a smooth region, or at a point where $V$ changes sign across a load discontinuity. This comes from $dM/dx=V$.

When a distributed load is replaced by a resultant for support reactions, that replacement is valid for the external equilibrium of the whole beam. For internal diagrams, however, you must keep the actual distribution in the region being cut or use piecewise expressions that account for where the distribution begins and ends.

## Visual

```text
Beam with point load

 A            P                 B
 ^            v                 ^
 |------------|-----------------|
 x=0          x=a               x=L

Shear V:  jumps up at A, down at P, up/down to zero at B
Moment M: starts at 0, changes slope at P, returns to 0
```

| Loading feature | Effect on $V(x)$ | Effect on $M(x)$ |
|---|---|---|
| Upward reaction | Positive jump | Slope changes after support |
| Downward point load | Negative jump | Moment remains continuous |
| Applied couple | No shear jump | Moment jumps |
| Uniform load $w_0$ | Linear slope $-w_0$ | Quadratic curve |
| No load region | Constant shear | Linear moment |

## Worked example 1: Simply supported beam with an off-center point load

**Problem.** A simply supported beam of length $8$ m has a pin at $A$ and a roller at $B$. A $20$ kN downward point load acts at $x=3$ m from $A$. Find the support reactions and piecewise shear and bending moment functions.

**Method.** Use whole-beam equilibrium for reactions, then cut the beam in regions $0\lt x\lt3$ and $3\lt x\lt8$.

1. Whole-beam moment balance about $A$:

$$
\sum M_A=0:\quad 8B_y-20(3)=0.
$$

$$
B_y=7.5\ \text{kN}.
$$

2. Vertical force balance:

$$
A_y+B_y-20=0,
$$

$$
A_y=12.5\ \text{kN}.
$$

3. Region 1: $0\lt x\lt3$. Keep the left segment. Forces are $A_y$ at $x=0$, internal shear $V$, and internal moment $M$ at the cut.

Vertical equilibrium:

$$
\sum F_y=0:\quad A_y+V=0
$$

under a convention where the cut force on the retained left part is drawn downward. If we define positive shear diagram value as the upward internal force on the left face, then

$$
V(x)=A_y=12.5\ \text{kN}.
$$

Moment about the cut gives

$$
M(x)=A_yx=12.5x\ \text{kN m}.
$$

4. Region 2: $3\lt x\lt8$. The left segment includes $A_y$ and the point load.

Shear:

$$
V(x)=A_y-20=12.5-20=-7.5\ \text{kN}.
$$

Moment:

$$
M(x)=A_yx-20(x-3).
$$

Simplify:

$$
M(x)=12.5x-20x+60=60-7.5x\ \text{kN m}.
$$

5. Check endpoint and continuity:

At $x=3^-$,

$$
M=12.5(3)=37.5\ \text{kN m}.
$$

At $x=3^+$,

$$
M=60-7.5(3)=37.5\ \text{kN m}.
$$

At $x=8$,

$$
M=60-7.5(8)=0.
$$

The checked result is

$$
\boxed{
V(x)=
\begin{cases}
12.5,&0\lt x\lt3,\\
-7.5,&3\lt x\lt8,
\end{cases}
\quad
M(x)=
\begin{cases}
12.5x,&0\lt x\lt3,\\
60-7.5x,&3\lt x\lt8.
\end{cases}}
$$

The maximum moment is $37.5$ kN m at the point load, where shear changes sign.

## Worked example 2: Cantilever beam with a uniform load

**Problem.** A cantilever beam is fixed at $A$ and free at $B$. The length is $L=4$ m. A uniform downward load $w=2.5$ kN/m acts over the whole span. Find the fixed-end reactions and internal shear and moment at a section $x$ measured from the fixed end.

**Method.** The total distributed load is $wL$. Use whole-beam equilibrium for reactions, then cut at distance $x$ from $A$.

1. Equivalent load:

$$
R=wL=2.5(4)=10\ \text{kN}.
$$

It acts at $L/2=2$ m from $A$.

2. Vertical reaction:

$$
A_y-10=0,\qquad A_y=10\ \text{kN}.
$$

3. Moment reaction at fixed end. Taking counterclockwise positive:

$$
M_A-10(2)=0,\qquad M_A=20\ \text{kN m}.
$$

This is the support moment applied by the wall on the beam.

4. Cut at $0\lt x\lt4$ and keep the left segment. The distributed load on the retained segment has magnitude $wx$ and acts at $x/2$ from $A$.

Shear diagram value:

$$
V(x)=A_y-wx=10-2.5x\ \text{kN}.
$$

5. Bending moment using forces to the left of the cut:

$$
M(x)=M_A+A_yx-\frac{wx^2}{2}
$$

with sign depending on the chosen internal moment convention. If the bending moment diagram is taken as the internal moment balancing the left side with sagging positive, the cantilever under downward load is often plotted negative:

$$
M_{\text{beam}}(x)=-\frac{w(L-x)^2}{2}.
$$

To avoid sign confusion, use the free-end expression for physical magnitude:

At a cut $x$ from the fixed end, the load to the right has length $L-x$ and resultant $w(L-x)$ at a distance $(L-x)/2$ from the cut. Therefore the internal moment magnitude is

$$
|M(x)|=\frac{w(L-x)^2}{2}.
$$

6. At the fixed end:

$$
|M(0)|=\frac{2.5(4)^2}{2}=20\ \text{kN m}.
$$

At the free end:

$$
|M(4)|=0.
$$

The checked result is

$$
\boxed{A_y=10\ \text{kN},\quad M_A=20\ \text{kN m},\quad V(x)=10-2.5x,\quad |M(x)|=\frac{2.5(4-x)^2}{2}.}
$$

The maximum bending moment occurs at the fixed wall, which is why cantilever roots are critical.

## Code

```python
import numpy as np

L = 8.0
P = 20.0
a = 3.0
By = P * a / L
Ay = P - By

xs = np.linspace(0.0, L, 17)
V = np.where(xs < a, Ay, Ay - P)
M = np.where(xs < a, Ay * xs, Ay * xs - P * (xs - a))

print(f"Ay={Ay:.2f} kN, By={By:.2f} kN")
for x, v, m in zip(xs, V, M):
    print(f"x={x:4.1f} m, V={v:6.2f} kN, M={m:7.2f} kN*m")
```

## Common pitfalls

- Drawing internal shear and moment with one sign convention, then interpreting the diagram with another.
- Replacing a distributed load by a resultant before cutting through the loaded region.
- Forgetting that point loads jump shear but not bending moment.
- Forgetting that applied couples jump bending moment but not shear.
- Looking for maximum bending moment only under point loads instead of also checking where $V=0$.
- Reporting support reactions without checking that the moment diagram returns to the correct boundary value.
- Mixing units such as kN and N, or m and mm, in moment calculations.

## Connections

- [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium)
- [Centroids and second moments](/physics/mechanics/centroids-second-moments)
- [Work-energy methods](/physics/mechanics/work-energy-methods)
- [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)
