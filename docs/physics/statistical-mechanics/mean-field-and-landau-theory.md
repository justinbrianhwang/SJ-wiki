---
title: Mean-Field and Landau Theory
sidebar_position: 16
---

# Mean-Field and Landau Theory

Mean-field theory replaces a fluctuating environment by its average effect. It is often quantitatively imperfect near critical points, but it gives a transparent first description of spontaneous symmetry breaking, order-parameter equations, and critical exponents. Schwabl presents molecular-field ideas in magnetism and then develops Landau and Ginzburg-Landau theory as more general frameworks.

Landau theory is powerful because it does not require microscopic spin variables. It writes the free energy as a symmetry-constrained expansion in an order parameter. The coefficients depend on temperature and other control variables, and the stable phase is found by minimizing the free energy.

## Replacing neighbors by an average field

The Curie-Weiss mean-field equation for an Ising ferromagnet is

$$
m=\tanh[\beta(h+zJm)].
$$

For Ising spins $s_i=\pm1$ with interaction $-J\sum_{\langle ij\rangle}s_is_j$, write $s_i=m+\delta s_i$. Discarding the quadratic fluctuation term $\delta s_i\delta s_j$ gives

$$
s_is_j\simeq m(s_i+s_j)-m^2.
$$

Each site then sees an effective field $h_{\mathrm{eff}}=h+zJm$, where $z$ is the coordination number. A single spin in that field has average $\tanh(\beta h_{\mathrm{eff}})$, and self-consistency requires this average to equal the $m$ used in the decoupling. The approximation neglects connected correlations between neighboring fluctuations.

Linearizing at $h=0$ gives $m\simeq\beta zJm$, so the mean-field critical temperature is $k_BT_c=zJ$. Expanding one order further,

$$
0=(1-\beta zJ)m+{1\over3}(\beta zJm)^3+\cdots,
$$

already displays the Landau equation of state near $T_c$.

## Building the free energy from symmetry

The Landau free-energy density for a scalar order parameter $m$ with $m\to -m$ symmetry is

$$
f(m)=f_0+{a\over 2}t m^2+{b\over 4}m^4-hm,
\qquad
t={T-T_c\over T_c},
$$

with $b\gt 0$ for stability. If the quartic coefficient is negative, a stabilizing $m^6$ term is needed and first-order behavior can occur.

The equilibrium order parameter minimizes $f$:

$$
{\partial f\over \partial m}=a t m+b m^3-h=0.
$$

The susceptibility is

$$
\chi=\left({\partial m\over \partial h}\right)_{h=0}.
$$

The Ginzburg-Landau functional includes spatial variations:

$$
F[m]=\int d^d x\left[
{c\over 2}|\nabla m|^2+{a\over 2}t m^2+{b\over 4}m^4-hm
\right].
$$

Analyticity and symmetry determine which powers appear, while stability constrains the highest retained even coefficient. The expansion is local in both $m$ and position. It may fail if the effective interaction is nonlocal or if integrating out another gapless variable generates nonanalytic terms.

## Minima and mean-field exponents

At $h=0$, the stationary equation is

$$
m(at+bm^2)=0.
$$

For $t\gt 0$, the stable solution is $m=0$. For $t\lt 0$,

$$
m^2=-{at\over b},
\qquad
m\propto (-t)^{1/2}.
$$

Thus the mean-field exponent for the order parameter is

$$
\beta_{\mathrm{MF}}={1\over 2}.
$$

The susceptibility above $T_c$ is obtained by linearizing:

$$
h=at m+bm^3\approx at m,
\qquad
\chi={1\over at}\propto t^{-1}.
$$

Below $T_c$, expand around $m_0^2=-at/b$. The curvature is

$$
{\partial^2 f\over \partial m^2}
=at+3bm_0^2=-2at,
$$

so $\chi\propto (-t)^{-1}$ with a different amplitude. Hence

$$
\gamma_{\mathrm{MF}}=1.
$$

At $T=T_c$, the equation of state is $h=bm^3$, so

$$
m\propto h^{1/3},
\qquad
\delta_{\mathrm{MF}}=3.
$$

The heat-capacity exponent is $\alpha_{\mathrm{MF}}=0$ because Landau theory gives a finite jump rather than a power-law divergence.

The jump follows by evaluating the minimized free energy. Above $T_c$, $m=0$ and the singular contribution is zero. Below $T_c$, substitute $m_0^2=-at/b$:

$$
f_{\min}-f_0
={a\over2}t\left(-{at\over b}\right)
+{b\over4}\left({a^2t^2\over b^2}\right)
=-{a^2t^2\over4b}.
$$

Two temperature derivatives produce a finite constant below the transition and zero above within this truncated model. The regular background heat capacity remains present; Landau theory predicts the discontinuity in its singular part.

The exponents obey the mean-field scaling relations $\alpha+2\beta+\gamma=2$ and $\gamma=\beta(\delta-1)$. These equalities are more robust than the individual mean-field values, although fluctuation effects change the values below the upper critical dimension.

## Spatial variations and correlation length

The Ginzburg criterion estimates where fluctuations invalidate mean-field theory. Roughly, mean-field theory is self-consistent when order-parameter fluctuations inside a correlation volume are small compared with the squared mean order parameter. This tends to be better in high dimensions and worse near $T_c$.

Landau theory is a local analytic expansion, so it assumes that the order parameter is small and that no other soft modes have been omitted. It works best near continuous transitions above the upper critical dimension or outside the narrow fluctuation-dominated region. Symmetry is the starting point: forbidden terms cannot be generated in the free energy unless the symmetry is explicitly broken.

The gradient term in Ginzburg-Landau theory penalizes rapid spatial variation. Linearizing about the disordered phase gives a Gaussian functional

$$
F_2[m]=\int d^dx\left[
{c\over 2}|\nabla m|^2+{a\over 2}t m^2
\right].
$$

In Fourier space this becomes

$$
F_2={1\over 2}\sum_k (ck^2+at)|m_k|^2.
$$

The correlation function is therefore controlled by

$$
ck^2+at,
$$

and the mean-field correlation length is

$$
\xi=\sqrt{c\over at}\propto t^{-1/2}
$$

above $T_c$. This gives $\nu_{\mathrm{MF}}=1/2$ and $\eta_{\mathrm{MF}}=0$.

Landau theory also gives a clean criterion for first-order transitions. If a cubic term is allowed,

$$
f(m)=am^2-wm^3+bm^4,
$$

then two minima can coexist while the order parameter jumps. If a symmetry forbids the cubic term but the quartic coefficient becomes negative, a stabilizing sixth-order term produces a first-order transition. Thus discontinuity is not an accident; it is encoded in the allowed structure of the free-energy expansion.

For the symmetric sixth-order form

$$
f(m)={r\over2}m^2+{u\over4}m^4+{v\over6}m^6,
\qquad u<0,\quad v>0,
$$

coexistence requires both stationarity at $m=m_*$ and equal free energy with the $m=0$ phase. Writing $x=m_*^2$, these conditions are

$$
r+ux+vx^2=0,
$$

and

$$
{r\over2}x+{u\over4}x^2+{v\over6}x^3=0.
$$

Eliminating $r$ gives $x=-3u/(4v)$, followed by

$$
r={3u^2\over16v}>0.
$$

The ordered minimum therefore becomes globally competitive while the quadratic coefficient is still positive, and $m$ jumps from zero to $\sqrt{-3u/(4v)}$. The point $r=u=0$ separating continuous and first-order lines is a mean-field tricritical point; its leading stabilizing nonlinearity is sixth order.

The Curie-Weiss equation can be understood as a microscopic realization of Landau theory. Expanding

$$
m=\tanh[\beta(zJm+h)]
$$

for small $m$ and $h$ produces an equation of state with the same powers of $m$ as the Landau derivative $\partial f/\partial m=h$. The coefficient of $m$ changes sign at $T_c$, while the cubic term stabilizes the ordered solution. Mean-field spin models and phenomenological Landau expansions therefore share the same critical exponents.

Ginzburg-Landau theory adds interfaces. For two coexisting minima, a domain wall is a spatial solution interpolating between them. The gradient term sets a wall width of order the correlation length, and the free-energy cost per area is the surface tension. This connects phase-transition theory with nucleation, magnetic domains, and pattern formation.

For the scalar $m^4$ theory, balancing the gradient and quadratic terms gives $\xi\sim\sqrt{c/(a\vert t\vert )}$. A Gaussian estimate of fluctuations in a correlation volume leads to the dimensionless comparison

$$
{\langle(\delta m)^2\rangle_\xi\over m_0^2}
\sim |t|^{(d-4)/2}
$$

up to coefficient-dependent factors. It grows as $t\to0$ for $d\lt 4$, identifying four as the upper critical dimension for short-range scalar $\phi^4$ theory. At $d\gt 4$, fluctuations become relatively less important near the transition; at $d=4$, logarithmic corrections require finer analysis.

External fields round the zero-field singularity. In the Ising case, $h\ne 0$ explicitly favors one sign of $m$, so the order parameter no longer changes sign discontinuously at $T_c$. The critical isotherm $h\propto m^\delta$ is therefore measured by tuning temperature to $T_c$ and varying the field, not by crossing the transition at nonzero field.

Below $T_c$, a small field leaves a local minimum opposed to the field. It is metastable until that minimum meets the intervening maximum at a spinodal. For the quartic model, the spinodal satisfies both

$$
h=at m+bm^3
$$

and

$$
{dh\over dm}=at+3bm^2=0.
$$

Thus $m_{\mathrm{sp}}^2=-at/(3b)$, and substitution gives the limiting field. A real finite-range system normally nucleates before reaching this mean-field spinodal, because a droplet of the stable phase can cross a finite barrier. The local-minimum picture is still useful for separating coexistence, metastability, and linear instability.

Hysteresis obtained by following metastable minima is therefore protocol dependent, not an equilibrium equation of state. Equilibrium always selects the global minimum. Confusing those two constructions can turn a kinetic delay into a supposed thermodynamic phase boundary.

Landau coefficients are phenomenological unless derived from a microscopic model. Their signs and temperature dependence carry physical content, but the expansion is not unique without specifying normalization of the order parameter.

Several distinct approximations are often grouped under the label ``mean field.'' The Curie--Weiss decoupling replaces neighboring spins by their mean. Landau theory assumes an analytic free energy organized by symmetry. Saddle-point evaluation of a field theory neglects fluctuations around a stationary configuration. They frequently lead to the same exponents, but their inputs and failure modes differ.

Order-parameter dimension also matters. A scalar Ising order parameter has two disconnected minima below $T_c$. A vector order parameter with continuous rotational symmetry has a whole sphere of minima, producing transverse Goldstone modes when the symmetry is broken. The scalar formulas for susceptibility and domain walls cannot be copied unchanged into that case.

Coupled order parameters can alter even the qualitative phase diagram. If two scalar orders $m$ and $\psi$ are both allowed, the lowest mixed term is often $g m^2\psi^2$. Positive $g$ makes the orders compete, while negative $g$ favors coexistence, subject to overall stability of the quartic form. Eliminating a secondary noncritical variable can renormalize the coefficients of the primary Landau expansion and may turn a continuous transition first order.

Conservation laws do not change the static minimum but do change relaxation. A nonconserved magnetization can relax locally toward lower free energy; a conserved density must move through a current and relax diffusively. Static Landau theory alone therefore cannot assign a dynamic critical exponent. A time-dependent equation must state which variables are conserved and what noise is coupled to them.

Boundary conditions matter for finite samples. A surface may favor one sign of the order parameter, suppress its magnitude, or impose a twist. Such terms shift finite-size behavior even when they disappear from the bulk free-energy density.

The normalization issue is harmless for exponents but important for amplitudes. Rescaling $m$ changes $a$, $b$, and $h$, while leaving predictions such as $\beta=1/2$ unchanged. Landau theory is strongest at classifying qualitative behavior and exponent values; precise material constants require microscopic input.

Despite its limits, Landau theory remains a useful first pass because it forces the analyst to identify the order parameter, symmetry, allowed couplings, and stability conditions. Those same ingredients are required before applying more sophisticated RG or numerical methods.

Landau theory remains the grammar of many transition problems even when it is not the final quantitative solution.

| Exponent | Definition | Mean-field value |
|---|---:|---:|
| $\alpha$ | $C\sim \vert t\vert ^{-\alpha}$ | $0$ |
| $\beta$ | $m\sim (-t)^\beta$ | $1/2$ |
| $\gamma$ | $\chi\sim \vert t\vert ^{-\gamma}$ | $1$ |
| $\delta$ | $m\sim h^{1/\delta}$ at $t=0$ | $3$ |
| $\nu$ | $\xi\sim \vert t\vert ^{-\nu}$ | $1/2$ |
| $\eta$ | $G(r)\sim r^{-(d-2+\eta)}$ at $t=0$ | $0$ |

```text
Landau f(m)

t > 0:      t < 0:
   f           f
   ^           ^
   |  \_/      | \_/ \_/
   +--> m      +-------> m
      0          -m0  +m0
```

## Worked example 1: Spontaneous magnetization in Landau theory

Problem: For

$$
f(m)={a\over 2}t m^2+{b\over 4}m^4
$$

with $a,b\gt 0$, find the stable equilibrium $m$ at $h=0$.

Method:

1. Differentiate:

$$
{df\over dm}=at m+b m^3=m(at+bm^2).
$$

2. Stationary points satisfy

$$
m=0
\quad\text{or}\quad
m^2=-{at\over b}.
$$

3. If $t\gt 0$, the second solution is not real. The only stationary point is $m=0$.
4. Check stability:

$$
{d^2f\over dm^2}=at+3bm^2.
$$

At $m=0$ and $t\gt 0$, this is positive, so $m=0$ is stable.
5. If $t\lt 0$, $m=0$ has negative curvature and is unstable. The stable minima are

$$
m=\pm\sqrt{-{at\over b}}.
$$

Checked answer: the order parameter grows continuously as $(-t)^{1/2}$ below $T_c$.

## Worked example 2: Mean-field susceptibility amplitude ratio

Problem: Compute the ratio $\chi_+/\chi_-$ above and below $T_c$ in the same Landau model at $h=0$.

Method:

1. The equation of state with field is

$$
h=at m+bm^3.
$$

2. Differentiate with respect to $m$:

$$
{dh\over dm}=at+3bm^2.
$$

Thus

$$
\chi=\left({dh\over dm}\right)^{-1}.
$$

3. Above $T_c$, $m=0$ and $t\gt 0$:

$$
\chi_+={1\over at}.
$$

4. Below $T_c$, $m_0^2=-at/b$:

$$
{dh\over dm}=at+3b\left(-{at\over b}\right)
=-2at.
$$

Since $t\lt 0$,

$$
\chi_-={1\over -2at}.
$$

5. Compare at equal $\vert t\vert $:

$$
{\chi_+\over \chi_-}=2.
$$

Checked answer: the exponent is the same on both sides, but amplitudes differ.

## Worked example 3: a planar domain wall

At $t\lt 0$ and $h=0$, consider a profile depending only on $x$ and joining the two minima. Varying the functional gives

$$
c{d^2m\over dx^2}=at\,m+bm^3.
$$

Set $m_0=\sqrt{-at/b}$ and try $m(x)=m_0\tanh(x/\ell)$. Its derivatives are

$$
m'= {m_0\over\ell}\operatorname{sech}^2(x/\ell),
$$

$$
m''=-{2m_0\over\ell^2}\tanh(x/\ell)\operatorname{sech}^2(x/\ell).
$$

On the right-hand side,

$$
at\,m+bm^3
=at\,m_0\tanh(x/\ell)\operatorname{sech}^2(x/\ell),
$$

because $bm_0^2=-at$. Matching coefficients gives

$$
\ell=\sqrt{2c\over-a t}=\sqrt2\,\xi_-.
$$

The wall broadens on approach to $T_c$. Substituting the solution back into the excess free energy gives a positive surface tension proportional to $c^{1/2}(-at)^{3/2}/b$, which vanishes as the two phases become indistinguishable.

## Where the approximation fails

- A term cannot be omitted merely because it complicates the minimum. A cubic invariant is forbidden by Ising symmetry but allowed for other order parameters and can change the transition order.
- If $b\lt 0$, the quartic truncation is unbounded. A positive sixth-order term is then required, and coexistence must be found by comparing global minima.
- The exponent $\beta$ and inverse temperature $\beta=1/(k_BT)$ share a symbol in standard notation; context must distinguish them.
- Low-dimensional short-range systems have strong critical fluctuations. Mean-field exponents should not be fitted arbitrarily close to $T_c$ there.
- Solving $df/dm=0$ finds stationary points, including maxima and metastable minima. Curvature and global free energy both need checking.
- An incorrect order parameter or a missing conserved or gapless field cannot be repaired by retaining more powers of the same scalar $m$.

## Related pages

- [Phase transitions and order parameters](/physics/statistical-mechanics/phase-transitions-and-order-parameters)
- [Magnetism, lattice gases, and binary alloys](/physics/statistical-mechanics/magnetism-lattice-gases-and-binary-alloys)
- [Scaling, universality, and renormalization group](/physics/statistical-mechanics/scaling-universality-and-renormalization-group)
- [Scalar phi-four theory](/physics/quantum-field-theory/scalar-phi-four-theory)
- [Renormalization group in QFT](/physics/quantum-field-theory/renormalization-group)
