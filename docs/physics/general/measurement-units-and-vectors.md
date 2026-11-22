---
title: Measurement, Units, and Vectors
sidebar_position: 2
---

# Measurement, Units, and Vectors

A measured number has a unit and limited precision. A vector also has direction. Dropping either piece can turn correct algebra into a physically meaningless answer.

Physics calculations are easier to audit when units remain attached, uncertainty is stated honestly, and vectors are resolved along declared axes. These habits catch mistakes before a more advanced law is ever needed.

## SI quantities and derived units

The International System of Units defines seven base units. Introductory mechanics mainly uses the meter, kilogram, and second; electromagnetism adds the ampere, and thermal physics uses the kelvin.

| Base quantity | SI unit | Symbol |
|---|---|---|
| Length | meter | $\mathrm m$ |
| Mass | kilogram | $\mathrm{kg}$ |
| Time | second | $\mathrm s$ |
| Electric current | ampere | $\mathrm A$ |
| Thermodynamic temperature | kelvin | $\mathrm K$ |
| Amount of substance | mole | $\mathrm{mol}$ |
| Luminous intensity | candela | $\mathrm{cd}$ |

Derived units are abbreviations for combinations of base units:

$$
1\,\mathrm N=1\,\mathrm{kg\,m/s^2},
$$

$$
1\,\mathrm J=1\,\mathrm{N\,m}
=1\,\mathrm{kg\,m^2/s^2},
$$

$$
1\,\mathrm W=1\,\mathrm{J/s}.
$$

Expanding a named unit is often the quickest check in a mixed mechanics or electrical calculation. Units obey ordinary algebra: they multiply, divide, cancel, and carry powers.

Prefixes scale by powers of ten. A millimeter is $10^{-3}\,\mathrm m$, a micrometer is $10^{-6}\,\mathrm m$, and a nanometer is $10^{-9}\,\mathrm m$. When an area or volume is converted, the prefix factor must also be squared or cubed:

$$
1\,\mathrm{cm^2}=(10^{-2}\,\mathrm m)^2=10^{-4}\,\mathrm{m^2},
$$

$$
1\,\mathrm{cm^3}=10^{-6}\,\mathrm{m^3}.
$$

Confusing $1\,\mathrm{cm^2}$ with $10^{-2}\,\mathrm{m^2}$ creates a factor-of-one-hundred error.

## Conversion factors are ratios equal to one

A conversion factor changes representation, not the physical quantity. Since $1\,\mathrm h=3600\,\mathrm s$, either ratio

$$
\frac{1\,\mathrm h}{3600\,\mathrm s}
\quad\text{or}\quad
\frac{3600\,\mathrm s}{1\,\mathrm h}
$$

equals one. Choose the orientation that cancels the unwanted unit.

Convert $72.0\,\mathrm{km/h}$ to meters per second:

$$
\begin{aligned}
72.0\,\frac{\mathrm{km}}{\mathrm h}
&\left(\frac{1000\,\mathrm m}{1\,\mathrm{km}}\right)
\left(\frac{1\,\mathrm h}{3600\,\mathrm s}\right)\\
&=20.0\,\mathrm{m/s}.
\end{aligned}
$$

The canceled units show the direction of conversion. Memorizing “divide by $3.6$” is faster only until a less familiar conversion appears.

For density, suppose $2.70\,\mathrm{g/cm^3}$ is needed in SI units:

$$
\begin{aligned}
2.70\,\frac{\mathrm g}{\mathrm{cm^3}}
&\left(\frac{1\,\mathrm{kg}}{1000\,\mathrm g}\right)
\left(\frac{100\,\mathrm{cm}}{1\,\mathrm m}\right)^3\\
&=2.70\times10^3\,\mathrm{kg/m^3}.
\end{aligned}
$$

Cubing the length conversion is essential.

## Dimensions test the structure of an equation

Dimensions classify quantities independently of the chosen unit. Write length, mass, and time as $L$, $M$, and $T$. Velocity has dimension $LT^{-1}$, acceleration $LT^{-2}$, and force $MLT^{-2}$.

Every term in a sum must have the same dimension. The equation

$$
x=x_0+v_0t+\frac12at^2
$$

is homogeneous because each term has dimension $L$. The arguments of $\sin$, $\cos$, exponentials, and logarithms must be dimensionless. An angle in radians is a ratio of arc length to radius and therefore dimensionless.

Dimensional analysis can reject a formula but cannot prove it correct. Both $x=v_0t+\tfrac12at^2$ and $x=v_0t+at^2$ are dimensionally valid; dimensions do not supply the numerical factor.

### Repairing a proposed drag law

Suppose a drag model is written $F=C\rho Av$, with density $\rho$, reference area $A$, and speed $v$. Its right side has dimension

$$
[\rho Av]=(ML^{-3})(L^2)(LT^{-1})=MT^{-1},
$$

which is not force. One additional speed repairs the dimensions:

$$
F=C\rho Av^2.
$$

The common high-Reynolds-number model is

$$
F_D=\frac12C_D\rho Av^2,
$$

where $C_D$ is dimensionless. Dimensional reasoning cannot decide the value of $C_D$ or whether a linear rather than quadratic law applies in a different flow regime.

Dimensions also reveal scaling. A pendulum period made only from length $L$ and gravitational acceleration $g$ must have the form

$$
T=C L^a g^b.
$$

Matching dimensions,

$$
T=L^{a+b}T^{-2b},
$$

gives $-2b=1$ and $a+b=0$, so $a=1/2$ and $b=-1/2$. Thus

$$
T=C\sqrt{\frac{L}{g}}.
$$

Dimensional analysis finds the dependence but not $C=2\pi$, nor the small-angle assumptions behind the pendulum formula.

## Precision, accuracy, and uncertainty

Accuracy means closeness to an accepted or true value; precision means repeatability or fineness of resolution. Repeated readings can be tightly clustered and still biased by a miscalibrated instrument.

A measured value should be reported with uncertainty, for example

$$
L=(12.4\pm0.1)\,\mathrm{cm}.
$$

The uncertainty describes a plausible range under a stated procedure. It is not a guarantee that the true value lies inside, and its interpretation depends on whether it is a resolution estimate, standard deviation, confidence interval, or another convention.

For independent small uncertainties, sums and differences combine absolute uncertainties approximately in quadrature:

$$
\sigma_z=\sqrt{\sigma_x^2+\sigma_y^2}
\qquad
\text{for }z=x\pm y.
$$

Products and quotients combine fractional uncertainties:

$$
\left(\frac{\sigma_z}{z}\right)^2
\approx
\left(\frac{\sigma_x}{x}\right)^2+
\left(\frac{\sigma_y}{y}\right)^2
$$

for $z=xy$ or $x/y$. Correlated uncertainties need covariance terms; blindly applying the independent-error rule can overstate or understate the result.

Suppose a rectangle has

$$
L=(20.0\pm0.2)\,\mathrm{cm},
\qquad
W=(10.0\pm0.1)\,\mathrm{cm}.
$$

Its area is $A=200\,\mathrm{cm^2}$. The fractional uncertainty is

$$
\frac{\sigma_A}{A}
=\sqrt{\left(\frac{0.2}{20.0}\right)^2+
\left(\frac{0.1}{10.0}\right)^2}
=0.0141.
$$

Hence

$$
\sigma_A=(200)(0.0141)=2.8\,\mathrm{cm^2},
$$

reported reasonably as

$$
A=(200\pm3)\,\mathrm{cm^2}.
$$

Keeping extra digits during intermediate calculation avoids rounding drift. The final uncertainty is commonly rounded to one significant digit, sometimes two when its first digit is small, and the measured value is rounded to the same decimal place.

Exact counts and defined conversion factors do not limit significant figures. A measured $2.4\,\mathrm m$ divided into exactly three equal parts is limited by the measurement, not by the integer three.

## Random scatter and systematic bias

Repeated measurements reveal random variation. Their arithmetic mean is

$$
\bar x=\frac{1}{N}\sum_{i=1}^N x_i,
$$

and their sample standard deviation estimates the spread:

$$
s=\sqrt{\frac{1}{N-1}\sum_{i=1}^N(x_i-\bar x)^2}.
$$

If readings are independent, the uncertainty of the mean from random scatter decreases roughly as $s/\sqrt N$. Repetition therefore improves the estimate of a stable mean.

Systematic errors behave differently. A balance with a persistent zero offset can give a very repeatable but biased mass. Taking more readings does not remove the offset. Calibration against known standards, reversal of the apparatus, background subtraction, or a different measurement method is needed.

Resolution is the smallest change an instrument can display or distinguish. It contributes uncertainty, but it need not be the only contribution. Parallax, environmental drift, model assumptions, and sample variation may dominate. Reporting many calculator digits cannot recover information absent from the measurement.

Percent difference and percent error answer different questions. When comparing a measurement $x$ with accepted value $x_a$,

$$
\text{percent error}
=\frac{\lvert x-x_a\rvert}{\lvert x_a\rvert}\times100\%.
$$

When neither of two measurements is privileged, percent difference commonly divides their absolute difference by their average magnitude.

## Scientific notation and scale

Scientific notation separates a coefficient from a power of ten:

$$
0.000\,004\,20=4.20\times10^{-6}.
$$

The trailing zero in $4.20$ records precision. In multiplication, exponents add; in division, they subtract. Keeping the coefficient between one and ten makes powers easier to audit.

An order of magnitude is the nearest power-of-ten scale, not an exact rounded value. Estimating before detailed substitution is useful. For example, the time for light to cross a room a few meters wide is on the order of

$$
\frac{10^0\,\mathrm m}{10^8\,\mathrm{m/s}}
\sim10^{-8}\,\mathrm s.
$$

A calculator output of milliseconds would then signal a unit or exponent error.

Dimensionless quantities can still carry named conventions. Plane angle in radians and solid angle in steradians are dimensionless ratios. Strain, refractive index, and coefficients of friction are also dimensionless. Their lack of dimensions does not make them interchangeable.

## Scalars, vectors, and components

A scalar has magnitude only. Mass, temperature, energy, and time are scalars. Displacement, velocity, acceleration, force, momentum, and many fields are vectors.

In Cartesian components,

$$
\vec A=A_x\hat i+A_y\hat j+A_z\hat k.
$$

For a two-dimensional vector of magnitude $A$ at angle $\theta$ counterclockwise from the positive $x$-axis,

$$
A_x=A\cos\theta,
\qquad
A_y=A\sin\theta.
$$

The magnitude follows from

$$
A=\sqrt{A_x^2+A_y^2}.
$$

Components may be negative even though magnitude is nonnegative. A component is not a “part” that must have positive size; it is a signed projection on an axis.

Vector addition is componentwise:

$$
\vec R=\vec A+\vec B,
$$

$$
R_x=A_x+B_x,
\qquad
R_y=A_y+B_y.
$$

The result does not depend on coordinate choice, though its components do. Choosing axes along an incline or symmetry direction can make one component vanish and shorten the algebra.

Vector subtraction is addition of the negative:

$$
\vec A-\vec B=\vec A+(-\vec B).
$$

Relative velocity uses this form. If car A moves east at $25\,\mathrm{m/s}$ and car B moves east at $20\,\mathrm{m/s}$, A's velocity relative to B is

$$
\vec v_{A/B}=\vec v_A-\vec v_B
=5\,\mathrm{m/s}\ \text{east}.
$$

If B instead moves west at $20\,\mathrm{m/s}$, take its component as negative and obtain $45\,\mathrm{m/s}$ east. Verbal “closing speed” rules are less reliable than signed components.

Unit vectors carry direction but have magnitude one. A unit vector along nonzero $\vec A$ is

$$
\hat A=\frac{\vec A}{\lvert\vec A\rvert}.
$$

For $\vec A=3\hat i+4\hat j$,

$$
\hat A=\frac35\hat i+\frac45\hat j.
$$

Its magnitude is one, which provides a direct check.

## Worked displacement with a quadrant check

A hiker walks $4.0\,\mathrm{km}$ east and then $3.0\,\mathrm{km}$ at $40^\circ$ north of east. Take east as $+x$ and north as $+y$:

$$
A_x=4.0,\qquad A_y=0,
$$

$$
B_x=3.0\cos40^\circ=2.30,
\qquad
B_y=3.0\sin40^\circ=1.93.
$$

Therefore

$$
R_x=6.30\,\mathrm{km},
\qquad
R_y=1.93\,\mathrm{km}.
$$

The magnitude is

$$
R=\sqrt{6.30^2+1.93^2}=6.59\,\mathrm{km},
$$

and the direction is

$$
\theta=\tan^{-1}\left(\frac{1.93}{6.30}\right)=17.0^\circ.
$$

Both components are positive, so the first-quadrant angle is correct. In software, a two-argument arctangent function uses the signs of both components and is safer when the vector may lie in any quadrant.

Distance traveled is $7.0\,\mathrm{km}$, while displacement magnitude is $6.59\,\mathrm{km}$. The first is path length; the second joins start to finish.

## Dot products: projection and work

The dot product is

$$
\vec A\cdot\vec B
=A_xB_x+A_yB_y+A_zB_z
=AB\cos\theta.
$$

It returns a scalar and measures parallel overlap. The component of $\vec A$ along a unit vector $\hat n$ is $\vec A\cdot\hat n$. Perpendicular vectors have zero dot product.

Work by a constant force is

$$
W=\vec F\cdot\Delta\vec r.
$$

If a $50\,\mathrm N$ force acts $30^\circ$ above a horizontal displacement of $4.0\,\mathrm m$,

$$
W=(50)(4.0)\cos30^\circ=173\,\mathrm J.
$$

Only the force component along the displacement contributes. A perpendicular normal force does zero work on a body moving along a fixed horizontal surface.

## Cross products: area and orientation

The cross product has magnitude

$$
\lvert\vec A\times\vec B\rvert=AB\sin\theta
$$

and direction perpendicular to the plane of the vectors by the right-hand rule. Reversing order changes sign:

$$
\vec A\times\vec B=-\vec B\times\vec A.
$$

Parallel vectors have zero cross product. Its magnitude equals the area of the parallelogram formed by the vectors.

Torque about an origin is

$$
\vec\tau=\vec r\times\vec F.
$$

A $20\,\mathrm N$ force applied perpendicular to a wrench $0.25\,\mathrm m$ from the pivot produces

$$
\tau=rF\sin90^\circ=(0.25)(20)=5.0\,\mathrm{N\,m}.
$$

The same force directed along the wrench produces zero torque because its line of action passes through the pivot.

In component form,

$$
\vec A\times\vec B=
\begin{vmatrix}
\hat i&\hat j&\hat k\\
A_x&A_y&A_z\\
B_x&B_y&B_z
\end{vmatrix}.
$$

For $\vec A=2\hat i+3\hat j$ and $\vec B=4\hat i-\hat j$,

$$
\vec A\times\vec B
=(2\cdot-1-3\cdot4)\hat k
=-14\hat k.
$$

The negative $z$ direction agrees with the clockwise rotation from $\vec A$ toward $\vec B$ through the smaller angle.

## Coordinate choice does not change the physics

Rotate Cartesian axes by angle $\alpha$. Components of a fixed vector change according to

$$
A_{x'}=A_x\cos\alpha+A_y\sin\alpha,
$$

$$
A_{y'}=-A_x\sin\alpha+A_y\cos\alpha.
$$

The magnitude remains invariant:

$$
A_{x'}^2+A_{y'}^2=A_x^2+A_y^2.
$$

Dot products and physical predictions are likewise unchanged. Selecting axes along an incline or along a relative velocity is therefore an algebraic convenience, not a change to the system.

## Fitting data and reporting a model

Measurements often test a relation rather than one isolated value. If theory predicts $y=mx+b$, a plot can reveal whether the data are plausibly linear and can estimate slope and intercept. Units belong to fitted parameters: if $y$ is position and $x$ is time, slope has velocity units.

Residuals are the differences between measured values and fitted predictions. Randomly scattered residuals support the model more than a curved or steadily drifting pattern does. A high number of decimal places in a fitted slope cannot compensate for systematic residual structure.

Linearization can expose a power law. If $y=Cx^n$, taking logarithms gives

$$
\ln y=\ln C+n\ln x.
$$

A log-log plot has slope $n$, provided both quantities are positive and their uncertainties are treated appropriately. Transforming data also transforms its error distribution, so an unweighted straight-line fit may not be statistically suitable.

Graphs need labeled axes, units, uncertainty indicators when available, and a distinction between measured points and a model curve. Connecting every noisy point with straight segments can imply structure that was never measured.

## Significant figures are a reporting convention

For multiplication and division, the least precise measured factor usually limits the reported significant figures. For addition and subtraction, decimal place is the relevant guide because absolute uncertainties combine.

For example,

$$
12.1\,\mathrm m+0.35\,\mathrm m=12.45\,\mathrm m
$$

is normally reported as $12.5\,\mathrm m$ when the first measurement is known only to tenths. In a multistep calculation, retain guard digits until the end. Repeated intermediate rounding can shift the final answer.

Significant-figure rules are a compact substitute when explicit uncertainties are absent. When uncertainties are known, they provide the better basis for rounding and comparison.

## Estimation and final checks

Order-of-magnitude estimates expose misplaced prefixes and implausible calculator output. Round inputs to one significant digit, calculate the power-of-ten scale, then compare with the detailed result. A human walking speed is a few meters per second, not kilometers per second; an atomic length is around nanometers or less, not meters.

Before accepting a result:

- Confirm that added terms share dimensions and the final unit matches the requested quantity.
- Check prefix powers, especially for area and volume.
- Distinguish exact numbers from measured inputs when rounding.
- State coordinate axes and the reference direction for every angle.
- Use component signs to determine the quadrant rather than trusting a one-argument inverse tangent.
- Compare limiting cases and rough scale with physical expectations.

<div className="see-also">

See also: [One-Dimensional Kinematics](/physics/general/one-dimensional-kinematics) · [Two-Dimensional Motion](/physics/general/two-dimensional-motion) · [Work, Energy, and Conservation](/physics/general/work-energy-and-conservation) · [Magnetic Fields and Forces](/physics/general/magnetic-fields-and-forces)

</div>
