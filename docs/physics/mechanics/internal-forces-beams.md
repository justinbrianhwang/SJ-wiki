---
title: Internal Forces in Beams
sidebar_position: 6
---

# Internal Forces in Beams

Whole-body equilibrium determines support reactions, but it does not say how strongly each cross section is loaded. A beam can have zero resultant force and zero resultant moment while carrying large internal forces. Stress and deflection calculations begin only after those internal resultants are known as functions of position.

The basic operation is an imaginary cut. Keep either side of the cut, replace the discarded material by the forces and couple it exerted across the section, and impose equilibrium on the retained segment. Moving the cut along the member produces axial-force, shear-force, and bending-moment diagrams.

## What a cut exposes

For planar loading, a general section carries three resultants:

$$
N(x)=\text{axial force},\qquad
V(x)=\text{shear force},\qquad
M(x)=\text{bending moment}.
$$

They are resultants of a stress distribution over the cut area. Normal stress contributes to $N$ and $M$; shear stress contributes to $V$. Replacing that distribution by three section resultants is exact for equilibrium, even before a material law or stress formula is introduced.

A sign convention must pair the two exposed faces correctly. Here, positive diagram values mean:

- $N\gt 0$ is tension. On the right face of a left segment, positive $N$ points right.
- $V\gt 0$ acts downward on the right face of a left segment and upward on the left face of a right segment.
- $M\gt 0$ is sagging. It acts counterclockwise on the right face of a left segment and clockwise on the left face of a right segment.

The forces on opposite cut faces are equal and opposite. With this convention, a positive bending moment tends to put the lower fibers in tension in the usual horizontal beam drawing.

```text
positive resultants on two matching cut faces

 left segment          right segment
             N ->    <- N
             V down  up V
             M CCW   CW M
```

If a textbook uses the opposite shear sign, its equations and diagrams can still be correct. Trouble begins when a cut free-body diagram follows one convention and the plotted ordinate follows another.

## From a small element to the load–shear–moment equations

Let $w(x)$ be distributed load intensity, positive downward. Isolate an element of length $dx$. At its left face the positive shear acts upward; at its right face it acts downward. Vertical equilibrium gives, after dropping products of differentials,

$$
V-(V+dV)-w(x)\,dx=0.
$$

Hence

$$
\boxed{\frac{dV}{dx}=-w(x)}.
$$

Moment equilibrium about the left face gives

$$
M+V\,dx-(M+dM)-w(x)\,dx\frac{dx}{2}=0.
$$

The final term is second order in $dx$, so the limit yields

$$
\boxed{\frac{dM}{dx}=V(x)}.
$$

The integral versions are equally useful:

$$
V(x_2)-V(x_1)=-\int_{x_1}^{x_2}w(x)\,dx,
$$

$$
M(x_2)-M(x_1)=\int_{x_1}^{x_2}V(x)\,dx.
$$

The negative area under a downward load diagram is the change in shear. The signed area under the shear diagram is the change in moment. These statements provide both a construction method and a strong check on piecewise formulas.

The degree of each curve follows immediately. In an unloaded interval, shear is constant and moment is linear. Under uniform load, shear is linear and moment is quadratic. Under linearly varying load, shear is quadratic and moment is cubic.

## Jumps, continuity, and boundary values

Differential relations apply between concentrated actions. At a point load or applied couple, use a jump condition.

| Feature crossed from left to right | Change in $V$ | Change in $M$ |
|---|---:|---:|
| Downward point load $P$ | $-P$ | none |
| Upward point force $R$ | $+R$ | none |
| Concentrated applied couple | none | jump equal to its signed value |
| Uniform distributed load | continuous, linear variation | continuous, quadratic variation |
| No distributed load | constant | linear variation |

A finite point force cannot create an instantaneous moment jump because its lever arm tends to zero as the two sides of the point merge. A concentrated couple has finite moment with no resultant force, so it jumps $M$ without jumping $V$.

Boundary conditions depend on the support, not on a memorized diagram shape. At an unloaded free end, $N=V=M=0$. At a pin or roller end with no applied couple, $M=0$, but shear can equal the support reaction. A fixed end can carry force and moment, so none of the three internal resultants need vanish there. An ideal internal hinge transmits axial force and shear but no bending moment.

Since $dM/dx=V$, an interior smooth maximum or minimum of $M$ occurs where $V=0$. A moment extremum can also occur at a point where shear jumps across zero. Endpoints and moment jumps must be checked separately; differentiating one smooth region cannot find them.

## A reliable order of work

First draw the whole-beam free-body diagram and solve its reactions. Replace a distributed load by its equivalent resultant only for that whole-body equilibrium calculation. Once a cut passes through a loaded region, the retained portion of the distribution changes with $x$ and must be integrated over its actual length.

Next divide the span wherever the loading expression changes: point forces, couples, the start or end of distributed loading, and internal hinges all create region boundaries. Put one symbolic cut in each open region. The cut should not sit exactly at a discontinuity because the left and right limits differ there.

Choose whichever side of the cut contains fewer forces. A right-segment free-body diagram is as valid as a left-segment one, provided the cut-face signs are reversed consistently. Finish with global checks: expected endpoint values, shear jumps equal to point loads, moment jumps equal to couples, and the areas implied by the differential relations.

## Worked example: an off-center point load

A simply supported beam has length $8$ m. A pin at $A$ is at $x=0$, a roller at $B$ is at $x=8$ m, and a $20$ kN downward load acts at $x=3$ m. Find the reactions and the shear and moment functions.

Whole-beam moment equilibrium about $A$ gives

$$
8B_y-20(3)=0,
$$

so

$$
B_y=7.5\ \text{kN}.
$$

Vertical equilibrium then gives

$$
A_y+B_y-20=0,
\qquad
A_y=12.5\ \text{kN}.
$$

For $0\lt x\lt 3$, the only vertical force to the left of the cut is $A_y$. The positive diagram shear equals the net upward force on that left portion:

$$
V(x)=12.5\ \text{kN}.
$$

Taking moments of the external loads to the left of the cut gives

$$
M(x)=12.5x\ \text{kN m}.
$$

For $3\lt x\lt 8$, the point load is included:

$$
V(x)=12.5-20=-7.5\ \text{kN},
$$

and

$$
\begin{aligned}
M(x)&=12.5x-20(x-3)\\
&=60-7.5x\ \text{kN m}.
\end{aligned}
$$

Thus

$$
\boxed{
V(x)=
\begin{cases}
12.5,&0<x<3,\\
-7.5,&3<x<8,
\end{cases}
\quad
M(x)=
\begin{cases}
12.5x,&0<x<3,\\
60-7.5x,&3<x<8.
\end{cases}}
$$

The shear falls by exactly $20$ kN at the load. The moment is continuous there:

$$
M(3^-)=M(3^+)=37.5\ \text{kN m}.
$$

It returns to zero at $x=8$. Shear changes from positive to negative at the load, so the maximum bending moment is $37.5$ kN m at $x=3$ m.

## Worked example: a partially distributed load

A simply supported $6$ m beam carries a uniform downward load $w_0=4$ kN/m only over $0\le x\le3$ m. Find the reactions and all piecewise functions.

The distributed load has resultant

$$
W=w_0(3)=12\ \text{kN}
$$

acting at its centroid, $x=1.5$ m. Moment equilibrium about $A$ gives

$$
6B_y-12(1.5)=0,
\qquad
B_y=3\ \text{kN}.
$$

Then

$$
A_y=12-3=9\ \text{kN}.
$$

For a cut inside the loaded interval, $0\lt x\lt 3$, the retained load has magnitude $4x$ and acts at $x/2$:

$$
V(x)=9-4x\ \text{kN},
$$

$$
\begin{aligned}
M(x)&=9x-(4x)\frac{x}{2}\\
&=9x-2x^2\ \text{kN m}.
\end{aligned}
$$

For $3\lt x\lt 6$, the entire $12$ kN resultant lies to the left:

$$
V(x)=9-12=-3\ \text{kN},
$$

$$
M(x)=9x-12(x-1.5)=18-3x\ \text{kN m}.
$$

Continuity at $x=3$ checks the algebra:

$$
9(3)-2(3)^2=9\ \text{kN m},
$$

$$
18-3(3)=9\ \text{kN m}.
$$

The shear vanishes inside the first region:

$$
9-4x=0,
\qquad
x=2.25\ \text{m}.
$$

Substitution gives the maximum moment:

$$
M_{\max}=9(2.25)-2(2.25)^2=10.125\ \text{kN m}.
$$

The zero-shear location does not coincide with the end or centroid of the distributed load. It emerges from the accumulated load to the left of the section.

## Worked example: a cantilever from the free end

A $4$ m cantilever is fixed at $A$ and carries a uniform downward load $w=2.5$ kN/m over its entire span. Let $x$ be measured from the fixed end. Find $V(x)$ and $M(x)$ with sagging positive.

The support reactions are useful checks:

$$
A_y=wL=10\ \text{kN},
$$

and the wall supplies a counterclockwise reaction couple of magnitude

$$
M_A=\frac{wL^2}{2}=20\ \text{kN m}.
$$

For internal forces, the right segment is shorter to draw. Its loaded length is $L-x$. The distributed load on it has magnitude $w(L-x)$ and acts halfway along that length. Equilibrium gives

$$
V(x)=w(L-x)=2.5(4-x)\ \text{kN},
$$

under the stated positive-shear diagram convention, and

$$
M(x)=-\frac{w(L-x)^2}{2}
=-1.25(4-x)^2\ \text{kN m}.
$$

The negative sign denotes hogging. At the free end, both values are zero. At the wall,

$$
V(0)=10\ \text{kN},
\qquad
M(0)=-20\ \text{kN m}.
$$

Differentiation checks both relations:

$$
\frac{dV}{dx}=-2.5=-w,
\qquad
\frac{dM}{dx}=2.5(4-x)=V.
$$

## Axial force and combined loading

Axial force is easy to overlook when attention is on shear and moment. If a horizontal force component acts along the member, include $N(x)$ from $\sum F_x=0$. An inclined point load generally contributes to both axial and transverse diagrams. For a straight prismatic beam with no distributed axial load, $N$ remains constant between axial point loads and jumps by their axial components.

Internal diagrams do not themselves give stress. Under elementary beam assumptions, later formulas use them as inputs: average axial stress involves $N/A$, bending stress involves $My/I$, and transverse shear stress depends on $V$. A zero bending moment does not imply a completely unloaded section if $N$ or $V$ remains nonzero.

## Building diagrams from slopes and areas

Repeated section cuts are systematic, but a complete diagram can often be drawn faster from jumps, slopes, and boundary values. Begin at a boundary where $V$ or $M$ is known. Move from left to right. Apply each point-force jump to shear, use the distributed load to set the shear slope between jumps, and accumulate signed area under $V$ to obtain moment. Apply a moment jump only where an external couple acts.

Consider the point-load example above. Immediately to the right of $A$, the upward reaction jumps shear from zero to $+12.5$ kN. With no distributed load, shear stays horizontal until $x=3$ m. The $20$ kN downward load then drops it to $-7.5$ kN, where it remains until the $+7.5$ kN reaction at $B$ returns it to zero. The moment begins at zero. Its slope is first $+12.5$, then $-7.5$, so it rises linearly to the load and falls linearly afterward. No separate moment calculation is needed to see the shape.

Area gives the ordinates. From $x=0$ to $x=3$ m, the shear area is

$$
(12.5)(3)=37.5\ \text{kN m},
$$

which is the moment at the load. From $x=3$ to $x=8$ m, the area is

$$
(-7.5)(5)=-37.5\ \text{kN m},
$$

bringing the moment back to zero at the roller. Failure to return to the required boundary value exposes a missed load, bad reaction, or incorrect diagram area.

This graphical construction also distinguishes load intensity from accumulated force. The ordinate of the load diagram has units force per length. Its area has units force and changes shear. Shear has units force; its area has units moment and changes bending moment. Checking these units makes the two integrations easier to remember.

## Sections at concentrated loads and hinges

At a point force, $V(x)$ has different left and right limits, so “the shear at the load” is ambiguous unless a side is specified. The bending moment has one common limiting value when no concentrated couple is present. At an applied couple, the situation reverses: shear is continuous while moment has two limiting values.

An internal hinge imposes $M=0$ at its section but does not generally make the shear zero. It also divides a structure into parts whose equilibrium can supply additional equations. The moment diagram must pass through zero at the hinge, while the equal and opposite hinge forces appear on free-body diagrams of the two substructures.

A point of contraflexure is a location where bending moment changes sign, indicating a reversal between sagging and hogging. It need not be a hinge: the section can carry zero moment at one location while remaining materially continuous. Likewise, a zero shear location is not automatically a support or a load application point; under distributed loading it often lies inside a span.

## What the diagrams can and cannot say

Internal-resultant diagrams are independent of cross-sectional shape for a statically determinate beam. Changing a rectangular section to an I-section does not change $N(x)$, $V(x)$, or $M(x)$ when the external loading and support idealization remain the same. It changes the stresses and deformation produced by those resultants.

The usual later relations introduce section properties and material response. Axial stress scales with $N/A$; elementary bending stress scales with $My/I$; beam curvature is related to $M/(EI)$ under linear elastic, small-deflection assumptions. A maximum $\vert M\vert $ section is often important for bending stress, but the largest stress can occur elsewhere if section modulus varies along the beam. A shear maximum likewise does not determine shear stress without the cross-sectional distribution.

Statics alone also cannot find reactions in a statically indeterminate beam. Extra supports create more reaction unknowns than equilibrium equations, and compatibility of deformation is required. Once those reactions have been found by a suitable method, however, the same cutting and load–shear–moment relations construct the internal diagrams.

## Errors that survive neat algebra

- Replacing a distributed load by its full resultant after cutting inside the loaded interval changes both its magnitude and its centroid. Use only the portion actually retained.
- A point load changes shear abruptly but leaves moment continuous. Drawing a moment jump under a force violates local moment equilibrium.
- A concentrated couple changes moment abruptly without changing shear. Its sign follows the chosen moment convention.
- Solving only one region misses every downstream load. Place region boundaries wherever the loading description changes.
- The condition $V=0$ locates smooth interior extrema of $M$, not every possible maximum. Check boundaries and both sides of jumps as well.
- Units can conceal a factor of one thousand. If force is in kN and distance in m, moment is in kN m; stress work often requires conversion to N and mm.

## Related pages

- [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium)
- [Centroids and second moments](/physics/mechanics/centroids-second-moments)
- [Trusses, frames, and machines](/physics/mechanics/trusses-frames-machines)
- [Equilibrium and elasticity](/physics/general/equilibrium-and-elasticity)
