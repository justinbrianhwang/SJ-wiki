---
title: Mean-Field and Landau Theory
sidebar_position: 16
---

# Mean-Field and Landau Theory

Mean-field theory replaces a fluctuating environment by its average effect. It is often quantitatively imperfect near critical points, but it gives a transparent first description of spontaneous symmetry breaking, order-parameter equations, and critical exponents. Schwabl presents molecular-field ideas in magnetism and then develops Landau and Ginzburg-Landau theory as more general frameworks.

Landau theory is powerful because it does not require microscopic spin variables. It writes the free energy as a symmetry-constrained expansion in an order parameter. The coefficients depend on temperature and other control variables, and the stable phase is found by minimizing the free energy.

## Definitions

The Curie-Weiss mean-field equation for an Ising ferromagnet is

$$
m=\tanh[\beta(h+zJm)].
$$

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

## Key results

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

The Ginzburg criterion estimates where fluctuations invalidate mean-field theory. Roughly, mean-field theory is self-consistent when order-parameter fluctuations inside a correlation volume are small compared with the squared mean order parameter. This tends to be better in high dimensions and worse near $T_c$.

Landau theory is a local analytic expansion, so it assumes that the order parameter is small and that no other soft modes have been omitted. This is why it works best near continuous transitions above the upper critical dimension or outside the narrow fluctuation-dominated region. It also explains why symmetry is the starting point: terms absent by symmetry cannot be generated in the free energy unless the symmetry is explicitly broken.

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

The Curie-Weiss equation can be understood as a microscopic realization of Landau theory. Expanding

$$
m=\tanh[\beta(zJm+h)]
$$

for small $m$ and $h$ produces an equation of state with the same powers of $m$ as the Landau derivative $\partial f/\partial m=h$. The coefficient of $m$ changes sign at $T_c$, while the cubic term stabilizes the ordered solution. This is why mean-field spin models and phenomenological Landau expansions share the same critical exponents.

Ginzburg-Landau theory adds interfaces. For two coexisting minima, a domain wall is a spatial solution interpolating between them. The gradient term sets a wall width of order the correlation length, and the free-energy cost per area is the surface tension. This connects phase-transition theory with nucleation, magnetic domains, and pattern formation.

External fields round the zero-field singularity. In the Ising case, $h\ne 0$ explicitly favors one sign of $m$, so the order parameter no longer changes sign discontinuously at $T_c$. The critical isotherm $h\propto m^\delta$ is therefore measured by tuning temperature to $T_c$ and varying the field, not by crossing the transition at nonzero field.

Landau coefficients are phenomenological unless derived from a microscopic model. Their signs and temperature dependence carry physical content, but the expansion is not unique without specifying normalization of the order parameter.

The normalization issue is harmless for exponents but important for amplitudes. Rescaling $m$ changes $a$, $b$, and $h$, while leaving predictions such as $\beta=1/2$ unchanged. This is why Landau theory is best at classifying qualitative behavior and exponent values, not at predicting precise material constants without microscopic input.

Despite its limits, Landau theory remains a useful first pass because it forces the analyst to identify the order parameter, symmetry, allowed couplings, and stability conditions. Those same ingredients are required before applying more sophisticated RG or numerical methods.

In that sense, Landau theory is often the grammar of the problem even when it is not the final quantitative solution.

## Visual

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

## Code

```python
import numpy as np

def landau_order_parameter(t, a=1.0, b=1.0):
    if t >= 0:
        return 0.0
    return np.sqrt(-a * t / b)

def landau_susceptibility(t, a=1.0):
    if t > 0:
        return 1.0 / (a * t)
    if t < 0:
        return 1.0 / (-2.0 * a * t)
    return np.inf

for t in [0.2, 0.05, -0.05, -0.2]:
    print(t, landau_order_parameter(t), landau_susceptibility(t))
```

## Common pitfalls

- Forgetting to include all symmetry-allowed terms. A cubic term is forbidden by $m\to -m$ symmetry but allowed in other transitions.
- Assuming $b\gt 0$ automatically. If $b\lt 0$, a stabilizing sixth-order term changes the transition character.
- Confusing the Landau exponent $\beta$ with inverse temperature $\beta=1/(k_BT)$.
- Trusting mean-field exponents too close to the critical point in low-dimensional systems.
- Minimizing the free energy without checking second derivatives and global stability.

## Connections

- [Phase transitions and order parameters](/physics/statistical-mechanics/phase-transitions-and-order-parameters)
- [Magnetism, lattice gases, and binary alloys](/physics/statistical-mechanics/magnetism-lattice-gases-and-binary-alloys)
- [Scaling, universality, and renormalization group](/physics/statistical-mechanics/scaling-universality-and-renormalization-group)
- [Scalar phi-four theory](/physics/quantum-field-theory/scalar-phi-four-theory)
- [Renormalization group in QFT](/physics/quantum-field-theory/renormalization-group)
