---
title: Centroids and Second Moments
sidebar_position: 8
---

# Centroids and Second Moments

Centroids and second moments connect geometry to mechanics. The centroid locates the balance point of an area, line, volume, or mass distribution. The second moment of area describes how area is spread relative to an axis, which later controls bending stress and beam deflection. The mass moment of inertia describes how mass is spread relative to an axis, which later controls rotational dynamics.

The computations look similar, but the physical meanings differ. A centroid is a first moment divided by a total measure. A second moment is an integral of squared distance. Both reward careful coordinate choice, symmetry recognition, and composite-body bookkeeping.

## Definitions

For an area $A$ in the $xy$ plane, the **centroid** $(\bar{x},\bar{y})$ is

$$
\bar{x}=\frac{1}{A}\int_A x\,dA,\qquad
\bar{y}=\frac{1}{A}\int_A y\,dA.
$$

For a composite area made from simple pieces,

$$
\bar{x}=\frac{\sum_i A_i x_i}{\sum_i A_i},\qquad
\bar{y}=\frac{\sum_i A_i y_i}{\sum_i A_i}.
$$

Voids or holes are included as negative areas. The same idea works for mass centers:

$$
\bar{x}=\frac{\sum_i m_i x_i}{\sum_i m_i}.
$$

The **first moment of area** about the $y$ axis is

$$
Q_y=\int_A x\,dA=A\bar{x}.
$$

The first moment about the $x$ axis is

$$
Q_x=\int_A y\,dA=A\bar{y}.
$$

The **second moment of area** about the $x$ and $y$ axes is

$$
I_x=\int_A y^2\,dA,\qquad I_y=\int_A x^2\,dA.
$$

The **polar second moment of area** about point $O$ is

$$
J_O=\int_A r^2\,dA=I_x+I_y
$$

when $x$ and $y$ are perpendicular axes through $O$.

The **product of inertia** is

$$
I_{xy}=\int_A xy\,dA.
$$

It is zero if either the $x$ or $y$ axis is an axis of symmetry for the area.

The **mass moment of inertia** about an axis is

$$
I=\int r^2\,dm.
$$

Its units are mass times length squared, such as kg m$^2$. Do not confuse this with second moment of area, whose units are length to the fourth power.

## Key results

Symmetry is the first result to use. If an area has a line of symmetry, its centroid lies on that line. If it has two perpendicular symmetry axes, their intersection is the centroid. If an area is symmetric about the $y$ axis, then $I_{xy}=0$ for centroidal axes aligned with that symmetry.

For composite centroid calculations, use signed pieces:

$$
\bar{x}=\frac{A_1x_1+A_2x_2-A_hx_h}{A_1+A_2-A_h}
$$

when a hole of area $A_h$ is removed. The centroid of a removed region still has coordinates; the negative sign belongs to the area, not to the coordinate unless the coordinate itself is negative.

The **parallel-axis theorem** for second moments of area states

$$
I_x=I_{x_c}+Ad^2,
$$

where $I_{x_c}$ is about a centroidal axis parallel to $x$, and $d$ is the perpendicular distance between the axes. This theorem moves from a centroidal axis to a parallel noncentroidal axis. It does not move between rotated axes.

For mass moments,

$$
I_O=I_G+md^2,
$$

where $G$ is the center of mass and $d$ is the perpendicular distance between parallel axes.

Common centroidal second moments of area are:

$$
I_x=\frac{bh^3}{12}\quad\text{for a rectangle about its centroidal horizontal axis},
$$

$$
I_y=\frac{hb^3}{12}\quad\text{for a rectangle about its centroidal vertical axis},
$$

$$
I=\frac{\pi r^4}{4}\quad\text{for a circle about a centroidal diameter}.
$$

These formulas should be paired with a sketch of the axis. The same rectangle has different $I_x$ and $I_y$ when $b\ne h$, because the squared distance is measured perpendicular to the chosen axis.

For distributed loads and hydrostatic pressure, the resultant location is also a centroid idea. The equivalent force of a uniform distributed load acts at the centroid of the loaded length. A linearly varying triangular load acts one third of the base length from the larger-intensity end, or two thirds from the zero-intensity end.

## Visual

```text
Composite area bookkeeping

      y
      ^
      |
      |     +-----------+
      |     |           |
      |     |   hole    |  hole is entered as negative area
      |     |     o     |
      |     |           |
      |     +-----------+
      |
      +--------------------> x

Centroid formula: sum(signed area * centroid coordinate) / sum(signed area)
```

| Quantity | Integral | Units | Main use |
|---|---|---|---|
| Area centroid $\bar{x},\bar{y}$ | $\bar{x}=\int x\,dA/A$ | length | Resultant location, geometry balance |
| First moment $Q$ | $Q_x=\int y\,dA$ | length$^3$ | Shear stress, centroid calculations |
| Second moment $I_x$ | $I_x=\int y^2\,dA$ | length$^4$ | Bending stiffness and stress |
| Polar second moment $J$ | $J=I_x+I_y$ | length$^4$ | Torsion for circular shafts |
| Mass moment $I$ | $I=\int r^2\,dm$ | mass length$^2$ | Rotational dynamics |

## Worked example 1: Centroid of an L-shaped plate

**Problem.** An L-shaped plate is made from a $120$ mm by $80$ mm rectangle with a $70$ mm by $40$ mm rectangular cutout removed from the upper right corner. The origin is at the lower-left corner of the original rectangle. The remaining shape consists of the full rectangle minus the cutout occupying $50\le x\le120$ mm and $40\le y\le80$ mm. Find the centroid.

**Method.** Treat the plate as a positive large rectangle plus a negative cutout.

1. Large rectangle:

$$
A_1=120(80)=9600\ \text{mm}^2.
$$

Its centroid is

$$
(x_1,y_1)=(60,40)\ \text{mm}.
$$

2. Cutout:

$$
A_2=70(40)=2800\ \text{mm}^2.
$$

Its centroid is halfway through the removed region:

$$
x_2=\frac{50+120}{2}=85\ \text{mm},
$$

$$
y_2=\frac{40+80}{2}=60\ \text{mm}.
$$

Use $A_2$ as negative in the composite formula.

3. Remaining area:

$$
A=A_1-A_2=9600-2800=6800\ \text{mm}^2.
$$

4. Compute $\bar{x}$:

$$
\bar{x}=\frac{A_1x_1-A_2x_2}{A}
=\frac{9600(60)-2800(85)}{6800}.
$$

$$
\bar{x}=\frac{576000-238000}{6800}
=\frac{338000}{6800}=49.71\ \text{mm}.
$$

5. Compute $\bar{y}$:

$$
\bar{y}=\frac{A_1y_1-A_2y_2}{A}
=\frac{9600(40)-2800(60)}{6800}.
$$

$$
\bar{y}=\frac{384000-168000}{6800}
=\frac{216000}{6800}=31.76\ \text{mm}.
$$

The checked answer is

$$
\boxed{(\bar{x},\bar{y})=(49.7,\ 31.8)\ \text{mm}.}
$$

The centroid moves down and left from the center of the original rectangle because material was removed from the upper-right corner.

## Worked example 2: Second moment of a composite rectangular section

**Problem.** A T-section consists of a flange $100$ mm wide by $20$ mm thick on top of a web $20$ mm wide by $120$ mm tall. The web is centered under the flange. Find the centroidal $I_x$ about the horizontal centroidal axis. Measure $y$ upward from the bottom of the web.

**Method.** Find the composite centroid, then use the parallel-axis theorem for each rectangle.

1. Web area and centroid:

$$
A_w=20(120)=2400\ \text{mm}^2,
$$

$$
y_w=60\ \text{mm}.
$$

2. Flange area and centroid:

$$
A_f=100(20)=2000\ \text{mm}^2,
$$

The flange spans $120\le y\le140$ mm, so

$$
y_f=130\ \text{mm}.
$$

3. Total area:

$$
A=2400+2000=4400\ \text{mm}^2.
$$

4. Centroid:

$$
\bar{y}=\frac{2400(60)+2000(130)}{4400}
=\frac{144000+260000}{4400}=91.82\ \text{mm}.
$$

5. Web centroidal second moment about its own horizontal centroidal axis:

$$
I_{x,w,c}=\frac{b h^3}{12}=\frac{20(120)^3}{12}=2{,}880{,}000\ \text{mm}^4.
$$

Distance to composite centroid:

$$
d_w=91.82-60=31.82\ \text{mm}.
$$

Parallel-axis contribution:

$$
I_{x,w}=2{,}880{,}000+2400(31.82)^2.
$$

$$
I_{x,w}=2{,}880{,}000+2{,}430{,}000=5{,}310{,}000\ \text{mm}^4.
$$

6. Flange centroidal second moment:

$$
I_{x,f,c}=\frac{100(20)^3}{12}=66{,}667\ \text{mm}^4.
$$

Distance:

$$
d_f=130-91.82=38.18\ \text{mm}.
$$

$$
I_{x,f}=66{,}667+2000(38.18)^2.
$$

$$
I_{x,f}=66{,}667+2{,}916{,}000=2{,}982{,}667\ \text{mm}^4.
$$

7. Total:

$$
I_x=5{,}310{,}000+2{,}982{,}667=8{,}292{,}667\ \text{mm}^4.
$$

The checked answer is

$$
\boxed{\bar{y}=91.8\ \text{mm},\qquad I_x\approx 8.29\times10^6\ \text{mm}^4.}
$$

The flange has a small local $I_x$, but its distance from the centroid makes a large parallel-axis contribution.

## Code

```python
parts = [
    # name, area, xbar, ybar
    ("large rectangle", 120.0 * 80.0, 60.0, 40.0),
    ("cutout", -70.0 * 40.0, 85.0, 60.0),
]

A = sum(area for name, area, x, y in parts)
xbar = sum(area * x for name, area, x, y in parts) / A
ybar = sum(area * y for name, area, x, y in parts) / A

print(f"area = {A:.1f} mm^2")
print(f"xbar = {xbar:.2f} mm")
print(f"ybar = {ybar:.2f} mm")

# Parallel-axis computation for the T-section.
rectangles = [
    ("web", 20.0, 120.0, 60.0),
    ("flange", 100.0, 20.0, 130.0),
]
area_total = sum(b * h for name, b, h, yc in rectangles)
y_centroid = sum(b * h * yc for name, b, h, yc in rectangles) / area_total
Ix = 0.0
for name, b, h, yc in rectangles:
    area = b * h
    Ix_local = b * h**3 / 12.0
    Ix += Ix_local + area * (yc - y_centroid) ** 2
print(f"T-section ybar = {y_centroid:.2f} mm, Ix = {Ix:.0f} mm^4")
```

## Common pitfalls

- Treating a hole as a positive area in the composite centroid formula.
- Using a second moment formula about the wrong axis or wrong centroidal orientation.
- Applying the parallel-axis theorem with distance measured along the axis instead of perpendicular to it.
- Confusing mass moment of inertia with second moment of area.
- Dropping units: $I_x$ for an area is length$^4$, not length$^2$.
- Ignoring symmetry that could simplify a centroid or product-of-inertia calculation.
- Rounding the centroid too early before using it in a parallel-axis term.

## Connections

- [Rigid-body equilibrium](/physics/mechanics/rigid-body-equilibrium)
- [Internal forces in beams](/physics/mechanics/internal-forces-beams)
- [Planar rigid-body motion](/physics/mechanics/planar-rigid-body-motion)
- [Planar rigid-body kinetics](/physics/mechanics/planar-rigid-body-motion)
