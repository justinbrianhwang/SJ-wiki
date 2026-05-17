---
title: Root Locus Sketching and Analysis
sidebar_position: 10
---

# Root Locus Sketching and Analysis

Root locus is a graphical method for seeing how closed-loop poles move as a parameter, usually gain, changes. Nise emphasizes it because it connects stability, transient response, and design intuition in one $s$-plane picture. Instead of repeatedly solving the closed-loop characteristic equation for many gains, the designer sketches the paths that poles must follow.

![A feedback control block diagram shows compensators wrapped around a plant.](https://commons.wikimedia.org/wiki/Special:FilePath/Control_System.svg)

*Figure: The standard feedback loop keeps control pages tied to the plant-controller interface. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Control_System.svg), Inductiveload, public domain.*

The method is built around the characteristic equation $1+KG(s)H(s)=0$. Points on the root locus are candidate closed-loop pole locations. Once a point is chosen, the gain required to place a pole there is found from the magnitude condition. This makes root locus a design tool, not only an analysis tool.

## Definitions

For negative feedback with loop transfer function

$$
KG(s)H(s)=K\frac{\prod (s-z_i)}{\prod (s-p_i)},
$$

the characteristic equation is

$$
1+KG(s)H(s)=0.
$$

Thus

$$
KG(s)H(s)=-1.
$$

The **angle condition** for a point $s$ to lie on the root locus is

$$
\angle G(s)H(s)=(2k+1)180^\circ,\qquad k\in\mathbb Z.
$$

The **magnitude condition** gives the gain at that point:

$$
K=\frac{1}{|G(s)H(s)|}.
$$

The **branches** of the root locus start at open-loop poles and end at open-loop zeros. If there are more poles than finite zeros, the remaining branches go to zeros at infinity along asymptotes.

The **centroid** of the asymptotes is

$$
\sigma_a=\frac{\sum p_i-\sum z_i}{n-m},
$$

where $n$ is the number of open-loop poles and $m$ is the number of finite open-loop zeros. The asymptote angles for negative feedback are

$$
\theta_q=\frac{(2q+1)180^\circ}{n-m},\qquad q=0,1,\ldots,n-m-1.
$$

## Key results

The standard sketching rules are:

| Rule | Statement |
|---|---|
| number of branches | equals number of open-loop poles |
| symmetry | symmetric about real axis for real coefficients |
| real-axis segments | locus exists to the left of an odd number of real poles and zeros |
| starting points | branches start at open-loop poles when $K=0$ |
| ending points | branches end at finite or infinite zeros as $K\to\infty$ |
| asymptotes | used when $n\gt m$ |
| breakaway and break-in | occur where $dK/ds=0$ on real-axis segments |
| imaginary-axis crossing | found by Routh-Hurwitz or direct substitution $s=j\omega$ |

The root locus translates transient specifications into pole regions. A desired percent overshoot implies a damping ratio line. A desired settling time implies a vertical line. A desired peak time implies a horizontal line. If the root locus passes through the acceptable region, gain adjustment alone may meet the transient specification. If not, compensation is needed.

Zeros attract branches and poles repel branches. Adding a zero can pull the locus left or reshape it through the desired region. Adding a pole can pull the locus right and slow the response. This qualitative statement becomes the basis of lead, lag, and PID compensator design.

Breakaway and break-in points deserve more than a formula. On a real-axis segment between two poles, branches may move toward each other as gain increases, meet, and leave the real axis as a complex pair. On a segment between two zeros, branches may enter the real axis and terminate at those zeros. The condition $dK/ds=0$ finds candidate points because gain has a local extremum along the real-axis locus. Only candidates that lie on valid real-axis segments are physically part of the root locus.

Angle of departure and angle of arrival become important when open-loop poles or zeros are complex. A branch leaving a complex pole must do so at an angle that satisfies the total angle condition immediately near that pole. The calculation sums angles from all other poles and zeros to the pole of interest. This lets the sketch start correctly before numerical plotting or design refinements are used.

The root locus also shows stability range visually. If a branch crosses the imaginary axis, the gain at that crossing is a stability boundary. Routh-Hurwitz can compute the exact gain, while the locus shows how the poles approach and leave the stable half-plane. This combination is more informative than either method alone: Routh gives the number; root locus gives the motion.

When using root locus for transient design, the designer typically overlays damping-ratio and settling-time grids. The desired point is not chosen solely because it satisfies percent overshoot; it must also be on the root locus and yield an acceptable gain. If the locus crosses the damping line too far to the right, settling is slow. If it crosses at a high imaginary part with low damping, peak time may improve while overshoot becomes unacceptable.

Computer root-locus plots are valuable, but hand rules still matter. Software can draw a plot without explaining which poles and zeros shape it, where asymptotes go, or why a compensator helps. A quick hand sketch catches modeling errors such as missing integrators, wrong feedback sign, or an accidental unstable pole before numerical design proceeds.

Positive-feedback and generalized root loci use modified angle conditions. If the characteristic equation is $1-KG(s)H(s)=0$, then points on the locus satisfy an angle of $0^\circ$ modulo $360^\circ$ rather than an odd multiple of $180^\circ$. Nise includes these variants to show that root locus is really a parameterized root-solving method, not a rule tied only to negative feedback gain.

Pole sensitivity is another reason to inspect the locus shape. Where branches are crowded or nearly tangent to performance boundaries, a small gain change can create a large pole movement. Where the locus is well separated from the imaginary axis and performance limits, tuning is less delicate. The geometry therefore tells the designer how forgiving the gain setting is likely to be.

The gain value should be marked on any design point. A pole location without its associated gain is incomplete because the controller must realize that gain and the resulting actuator effort.

## Visual

```text
Example root-locus skeleton

Im
 ^
 |        / branch to infinity
 |       /
 |  x---o-------------x-----------> Re
 | -6  -3            0
 |       \
 |        \ branch to infinity

x = open-loop pole, o = open-loop zero
```

| Desired time feature | $s$-plane interpretation | Root-locus use |
|---|---|---|
| lower overshoot | larger damping ratio | choose pole on larger $\zeta$ ray |
| faster settling | more negative real part | choose pole left of settling boundary |
| shorter peak time | larger imaginary part | choose pole farther from real axis |
| stable closed loop | all poles in LHP | keep gain before RHP crossing |

## Worked example 1: real-axis segments and asymptotes

Problem: Sketch the structural features for

$$
G(s)H(s)=\frac{K}{s(s+2)(s+6)}.
$$

Find real-axis segments, asymptote centroid, and asymptote angles.

Method:

1. Identify open-loop poles and zeros:

$$
p=0,-2,-6,\qquad \text{no finite zeros}.
$$

2. Number of branches:

$$
n=3.
$$

3. Real-axis rule. Test intervals:

- $(0,\infty)$ has zero poles/zeros to the right, so no locus.
- $(-2,0)$ has one pole to the right, so locus exists.
- $(-6,-2)$ has two poles to the right, so no locus.
- $(-\infty,-6)$ has three poles to the right, so locus exists.

4. There are $n-m=3$ asymptotes. Centroid:

$$
\sigma_a=\frac{0+(-2)+(-6)-0}{3}=-\frac{8}{3}.
$$

5. Asymptote angles:

$$
\theta_q=\frac{(2q+1)180^\circ}{3}.
$$

For $q=0,1,2$:

$$
60^\circ,\quad 180^\circ,\quad 300^\circ.
$$

Checked answer: Real-axis locus on $(-2,0)$ and $(-\infty,-6)$, centroid $-8/3$, asymptotes at $60^\circ$, $180^\circ$, and $300^\circ$.

## Worked example 2: gain from the magnitude condition

Problem: For the same system,

$$
G(s)H(s)=\frac{K}{s(s+2)(s+6)},
$$

find the gain required for a closed-loop pole at $s=-1+j2$ if the point satisfies the angle condition.

Method:

1. The magnitude condition is

$$
K=|s(s+2)(s+6)|.
$$

2. Compute each vector magnitude at $s=-1+j2$:

$$
|s|=|-1+j2|=\sqrt{(-1)^2+2^2}=\sqrt5.
$$

$$
|s+2|=|1+j2|=\sqrt{1^2+2^2}=\sqrt5.
$$

$$
|s+6|=|5+j2|=\sqrt{5^2+2^2}=\sqrt{29}.
$$

3. Multiply:

$$
K=\sqrt5\sqrt5\sqrt{29}=5\sqrt{29}.
$$

4. Approximate:

$$
\sqrt{29}\approx5.385,\qquad K\approx26.93.
$$

Checked answer: If $-1+j2$ lies on the locus, the required gain is $K=5\sqrt{29}\approx26.9$.

## Code

```python
import numpy as np

poles = np.array([0, -2, -6], dtype=complex)
zeros = np.array([], dtype=complex)

centroid = (np.sum(poles) - np.sum(zeros)) / (len(poles) - len(zeros))
angles = [(2*q + 1) * 180 / (len(poles) - len(zeros)) for q in range(3)]
point = -1 + 2j
K = np.prod(np.abs(point - poles))

print("centroid:", centroid)
print("asymptote angles:", angles)
print("gain at point:", K)

# Closed-loop roots for several gains: s(s+2)(s+6)+K = 0
for gain in [1, 10, 26.93, 60]:
    coeffs = [1, 8, 12, gain]
    print(gain, np.roots(coeffs))
```

## Common pitfalls

- Drawing real-axis branches to the right of an even number of poles and zeros.
- Using closed-loop poles instead of open-loop poles and zeros to sketch the locus.
- Forgetting zeros at infinity when counting branch endpoints.
- Applying the magnitude condition before checking the angle condition.
- Assuming gain adjustment can place poles anywhere in the plane. It can only place them on the locus.
- Ignoring closed-loop zeros when judging whether a second-order approximation is valid.

## Connections

- [Time response](/cs/control-engineering/time-response-first-and-second-order) maps desired transient specs to pole locations.
- [Routh-Hurwitz stability](/cs/control-engineering/routh-hurwitz-stability) finds imaginary-axis crossings and gain ranges.
- [Root-locus design](/cs/control-engineering/root-locus-design-and-classical-compensation) uses the locus to choose compensators.
- [PID and compensators](/cs/control-engineering/pid-lead-lag-and-lag-lead-compensators) explains how added poles and zeros reshape the locus.
- [Frequency-response design](/cs/control-engineering/frequency-response-compensator-design) is the complementary classical design method.
