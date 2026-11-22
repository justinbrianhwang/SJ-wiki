---
title: Complex Functions and Analyticity
sidebar_position: 21
---

# Complex Functions and Analyticity

A complex function can be viewed as a map from the plane to itself, but complex differentiability imposes far more structure than ordinary differentiability of a two-variable map. A single derivative must describe the change produced by increments from every direction in the complex plane. That requirement leads to the Cauchy–Riemann equations, harmonic real and imaginary parts, local power series, and angle-preserving maps.

## One difference quotient, every direction

Write

$$
z=x+iy,
\qquad
f(z)=u(x,y)+iv(x,y),
$$

where $u$ and $v$ are real-valued. The complex derivative at $z_0$ is

$$
f'(z_0)=\lim_{h\to0}
\frac{f(z_0+h)-f(z_0)}{h}.
$$

The increment $h$ is complex and may approach zero along any path. First restrict it to real values, $h=\Delta x$. If the relevant partial derivatives exist, the limit is

$$
f'(z)=u_x+iv_x.
$$

Next take a purely imaginary increment $h=i\Delta y$:

$$
\begin{aligned}
f'(z)
&=\lim_{\Delta y\to0}
\frac{u(x,y+\Delta y)-u(x,y)
+i\bigl(v(x,y+\Delta y)-v(x,y)\bigr)}{i\Delta y}\\
&=v_y-iu_y.
\end{aligned}
$$

For one direction-independent limit, the real and imaginary parts must agree:

$$
u_x=v_y,
\qquad
u_y=-v_x.
$$

These are the Cauchy–Riemann equations. They are necessary wherever the complex derivative exists. If the first partial derivatives are continuous in a neighborhood and satisfy the equations there, they are also sufficient for complex differentiability throughout that neighborhood.

The real Jacobian of $f$ is

$$
J_f=
\begin{pmatrix}
u_x & u_y\\
v_x & v_y
\end{pmatrix}.
$$

Under the Cauchy–Riemann equations it has the form

$$
J_f=
\begin{pmatrix}
a & -b\\
b & a
\end{pmatrix},
$$

which is exactly real matrix multiplication by $a+ib=f'(z)$. Its determinant is $a^2+b^2=\vert f'(z)\vert ^2$. When the derivative is nonzero, the linearized map is a positive scaling combined with a rotation.

## Differentiable at a point versus analytic on a domain

Complex differentiability at one point is weaker than analyticity. A function is analytic, or holomorphic, on an open set if it is complex differentiable at every point of that set. It is analytic at a point when some neighborhood of the point has that property. The word *entire* means analytic on all of $\mathbb C$.

The Cauchy–Riemann equations at one point do not establish even complex differentiability there without further information. For example, define

$$
f(z)=
\begin{cases}
\dfrac{x^3}{x^2+y^2}
+i\dfrac{y^3}{x^2+y^2}, & z\ne0,\\
0, & z=0.
\end{cases}
$$

The coordinate-axis partial derivatives at the origin exist and satisfy the Cauchy–Riemann equations. Along the line $y=x$, however,

$$
f(x+ix)=\frac{x}{2}+i\frac{x}{2}=\frac{1+i}{2}x,
$$

so

$$
\frac{f(x+ix)}{x+ix}=\frac12.
$$

Along the real axis, $f(x)/x=1$. The difference quotient has different directional limits, so no complex derivative exists at zero. The usual theorem assumes continuous first partials in a neighborhood precisely to exclude such behavior.

There are also functions complex differentiable at an isolated point but nowhere analytic. For $f(z)=\vert z\vert ^2=z\bar z$,

$$
\frac{f(h)-f(0)}{h}=\frac{|h|^2}{h}=\bar h\to0,
$$

so $f'(0)=0$. Away from zero its components $u=x^2+y^2$ and $v=0$ fail the Cauchy–Riemann equations. No neighborhood of the origin is analytic.

## Worked test: $z^2$ and $\bar z$

For

$$
f(z)=z^2=(x+iy)^2=x^2-y^2+2ixy,
$$

identify

$$
u=x^2-y^2,
\qquad
v=2xy.
$$

Compute all four first partials:

$$
u_x=2x,
\quad u_y=-2y,
\quad v_x=2y,
\quad v_y=2x.
$$

They obey $u_x=v_y$ and $u_y=-v_x$ at every point, and they are continuous. Hence $z^2$ is entire. The derivative can be read as

$$
f'(z)=u_x+iv_x=2x+2iy=2z.
$$

At $z=0$ the derivative vanishes, so the function is analytic but not conformal there. At every nonzero point its local scale factor is $\vert 2z\vert $ and its local rotation angle is $\arg(2z)$.

Now take $g(z)=\bar z=x-iy$. Then

$$
u=x,
\qquad v=-y,
$$

and

$$
u_x=1,
\qquad v_y=-1.
$$

The first Cauchy–Riemann equation fails everywhere. The difference quotient confirms the result: real increments give $1$, while imaginary increments give $-1$. The map is perfectly smooth as a real map—it reflects the plane across the real axis—but it is nowhere complex differentiable. Reflection reverses orientation, whereas multiplication by a nonzero complex derivative preserves it.

## Harmonic components

Assume $f=u+iv$ is analytic and the second partials are continuous. Differentiate the Cauchy–Riemann equations:

$$
u_{xx}=v_{yx},
\qquad
u_{yy}=-v_{xy}.
$$

Equality of mixed partials gives

$$
u_{xx}+u_{yy}=0.
$$

The same calculation gives

$$
v_{xx}+v_{yy}=0.
$$

Thus both components are harmonic. Their level curves meet orthogonally where $f'(z)\ne0$. Indeed, the gradients are

$$
\nabla u=\langle u_x,u_y\rangle,
\qquad
\nabla v=\langle v_x,v_y\rangle
=\langle-u_y,u_x\rangle,
$$

and their dot product vanishes. In potential flow, one component can represent a velocity potential and the other a stream function.

On a simply connected domain, every harmonic function has a harmonic conjugate. On a region with holes, a conjugate may exist locally but fail to be single-valued globally. The function $u(z)=\log\vert z\vert $ is harmonic on $\mathbb C\setminus\{0\}$, and its local conjugate is the argument. A full circuit around the origin changes the argument by $2\pi$, preventing a single-valued global conjugate on the punctured plane.

## Worked construction: recovering a harmonic conjugate

Let

$$
u(x,y)=e^x\cos y.
$$

First check harmonicity:

$$
u_x=e^x\cos y,
\qquad
u_{xx}=e^x\cos y,
$$

$$
u_y=-e^x\sin y,
\qquad
u_{yy}=-e^x\cos y.
$$

Therefore $u_{xx}+u_{yy}=0$. Seek $v$ from the Cauchy–Riemann equation $v_y=u_x$:

$$
v_y=e^x\cos y.
$$

Integrating with respect to $y$ gives

$$
v(x,y)=e^x\sin y+g(x),
$$

where the “constant” may depend on $x$. Use the other equation, $v_x=-u_y$:

$$
e^x\sin y+g'(x)=e^x\sin y.
$$

Hence $g'(x)=0$, so $g(x)=C$. The analytic function is

$$
f(z)=e^x\cos y+i(e^x\sin y+C)=e^z+iC.
$$

The conjugate is unique up to a real additive constant. Adding $C$ to $v$ adds the purely imaginary constant $iC$ to $f$ and does not change its derivative.

## Building analytic functions from known ones

The familiar differentiation rules survive because the complex derivative uses the same algebraic limit laws. Sums and products of analytic functions are analytic, and a quotient is analytic wherever its denominator is nonzero. Compositions are analytic when the inner function maps into the domain of the outer one. The chain rule reads

$$
(f\circ g)'(z)=f'(g(z))g'(z).
$$

These closure rules are often more efficient than expanding into $u$ and $v$. For example,

$$
h(z)=\frac{e^{z^2}}{z-3i}
$$

is analytic on $\mathbb C\setminus\{3i\}$ because polynomials and the exponential are entire, their composition is entire, and the only denominator zero is $3i$. Its derivative follows from quotient and chain rules:

$$
h'(z)=
\frac{2ze^{z^2}(z-3i)-e^{z^2}}{(z-3i)^2}.
$$

The point $3i$ is a genuine singularity because the numerator $e^{(3i)^2}=e^{-9}$ is nonzero there. By contrast, $(z^2-1)/(z-1)$ simplifies to $z+1$ away from $1$ and has a removable singularity at $1$. Defining its value there as $2$ produces an entire function.

Complex conjugation is the recurring warning sign. A formula involving both $z$ and $\bar z$ may still be differentiable at isolated points, but it rarely defines an analytic function on an open region. Rewriting $x=(z+\bar z)/2$ and $y=(z-\bar z)/(2i)$ can expose such dependence quickly.

## Power series and rigidity

An analytic function has a local Taylor expansion

$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n
$$

inside a disk extending to the nearest obstruction to analyticity. This conclusion is much stronger than the corresponding real statement: a smooth real function need not equal its Taylor series. In complex analysis, contour integration supplies estimates that force analyticity and local power-series representation to coincide.

Several consequences express the rigidity:

- analytic functions possess derivatives of every order;
- zeros are isolated unless the function vanishes identically on a connected domain;
- if two analytic functions agree on a set with a limit point inside a connected domain, they agree everywhere in that domain;
- values on a suitable boundary determine interior values through Cauchy's integral formula.

The radius of a Taylor series is controlled by complex singularities, even when one studies a real-variable restriction. For instance, the real series for $1/(1+x^2)$ around zero has radius $1$ because its complex extension has poles at $z=\pm i$.

## Conformal maps and critical points

At a point where $f'(z_0)\ne0$, the first-order approximation is

$$
f(z_0+h)=f(z_0)+f'(z_0)h+o(|h|).
$$

Multiplication by $f'(z_0)$ rotates every small tangent direction through the same angle and scales it by the same positive factor. Angles and their orientation are therefore preserved locally. This is conformality.

When $f'(z_0)=0$, the function may remain analytic but the linear part collapses. For $f(z)=z^2$ at zero, rays with arguments $\theta$ and $\phi$ map to rays with arguments $2\theta$ and $2\phi$; angles are doubled rather than preserved. Such points are critical points of the map.

Conformality is local. An analytic function may fail to be globally one-to-one: $e^z$ is entire with nonzero derivative, yet $e^{z+2\pi i}=e^z$. A conformal bijection between domains needs both local nonvanishing derivative and global injectivity.

## Branches belong to the function definition

For $z=re^{i\theta}$, a complex logarithm would satisfy

$$
\log z=\ln r+i(\theta+2\pi k),
\qquad k\in\mathbb Z.
$$

There is no single-valued analytic logarithm on all of $\mathbb C\setminus\{0\}$. A branch chooses a continuous argument on a domain that excludes a curve preventing circuits around the origin. The principal branch commonly takes $-\pi\lt \arg z\lt \pi$, giving a cut along the nonpositive real axis.

Fractional powers inherit the choice through $z^\alpha=e^{\alpha\log z}$. Identities familiar from positive real logarithms can fail across branches. Any contour or mapping argument involving $\log z$, $z^\alpha$, or inverse trigonometric functions must state a domain and branch.

| Function | Analytic domain |
|---|---|
| polynomial | all of $\mathbb C$ |
| rational function | wherever its denominator is nonzero after cancellation |
| $e^z$, $\sin z$, $\cos z$ | all of $\mathbb C$ |
| $1/z$ | $\mathbb C\setminus\{0\}$ |
| $\bar z$ | nowhere complex differentiable |
| a branch of $\log z$ | its stated cut domain |

## Diagnostic checks

- Verify an open domain, not only the Cauchy–Riemann equations at one point, before claiming analyticity.
- The common sufficient test uses continuous first partial derivatives. If continuity fails, return to the difference quotient or a more refined theorem.
- Harmonicity of $u$ is necessary for it to be a real part, but a global conjugate also depends on domain topology.
- A formula may be analytic while its chosen branch is not defined across a cut. The expression and its domain must be carried together.
- Conformality requires a nonzero derivative and refers to local angle behavior; injectivity is a separate global question.
- Apparent singularities may cancel. Simplify a rational expression before naming its analytic domain, while remembering that an originally undefined point may still require explicit extension.

## Local tests and global conclusions

The derivative and the Cauchy–Riemann equations are local: they inspect behavior in arbitrarily small neighborhoods. Branches, harmonic conjugates, and one-to-one mappings also depend on the shape of the whole domain. Mixing those scales is a common source of false conclusions. A function may have a valid derivative at every point of a punctured domain while still lacking a global antiderivative there. A harmonic conjugate can be constructed in small disks yet fail to return to its starting value after a circuit around a hole.

Simple connectedness removes many of these obstructions because every closed loop can be contracted without leaving the domain. It does not make every formula single-valued automatically; the formula must still be defined consistently. Conversely, a domain with a hole can support a global analytic function perfectly well. The issue is whether a particular construction accumulates nonzero change around that hole.

Analytic continuation extends a locally defined function by overlapping analytic neighborhoods. The identity principle guarantees consistency when two continuations overlap and agree on a set with an interior limit point. Continuation may encounter a singularity, or different paths may lead to different branches when the domain permits nontrivial loops. The logarithm is the basic model for the latter phenomenon.

## Interpreting the derivative geometrically

At a noncritical point, the derivative contains two real quantities. Its modulus is the local scale factor, and its argument is the local rotation. The Jacobian determinant is the square of the scale factor, so a small area is multiplied approximately by that square. Orientation stays positive because the determinant cannot be negative for multiplication by a nonzero complex number.

Conformality concerns angles between smooth curves at their intersection. Each curve has a tangent direction; the derivative applies the same rotation and positive scale to both directions. Their angle is retained. Lengths are generally not retained because the scale factor may differ from one point to another. A conformal map can greatly distort a large figure while preserving its small crossing angles.

Critical points need separate local analysis. If the first nonzero Taylor term near a point has degree greater than one, the map behaves to leading order like a power. It can multiply angles, fold neighborhoods, and fail local one-to-one behavior. The derivative being zero does not signal a singularity of the function; it signals failure of the linear approximation to capture the first nonconstant change.

## Harmonic functions without a guessed conjugate

When constructing a conjugate, both Cauchy–Riemann equations must be checked after integration. The undetermined single-variable term is not optional bookkeeping; it is what makes the two partial-derivative conditions compatible. If the remaining equation asks that a function of one variable equal an expression involving both variables, no conjugate of the proposed form exists on that region.

Harmonicity gives a quick necessary test but also carries independent meaning. Harmonic functions obey mean-value behavior: their value at the center of a disk equals an average of boundary values. As a consequence, a nonconstant harmonic function cannot attain a strict interior maximum or minimum on a connected domain. Potential models use this to rule out isolated interior peaks unless a source or singularity is present.

Boundary data and domain shape therefore matter as much as the differential equation. Two harmonic functions with the same suitable boundary values agree under standard hypotheses. Complex analytic methods package a pair of harmonic functions together, but many potential problems can be studied directly through their real component when no global conjugate is convenient.

<div className="see-also">

See also: [Complex integration and residues](/math/engineering-math/complex-integration-and-residues) · [Laplace equation and potential](/math/engineering-math/laplace-equation-and-potential) · [Vector differential calculus](/math/engineering-math/vector-differential-calculus) · [Fourier integrals and transforms](/math/engineering-math/fourier-integrals-and-transforms)

</div>
