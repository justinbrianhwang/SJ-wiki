---
title: Real Gases, Virial Expansion, and van der Waals Theory
sidebar_position: 12
---

# Real Gases, Virial Expansion, and van der Waals Theory

Real gases differ from ideal gases because molecules exclude volume and attract or repel each other. The ideal gas is still the reference point, but corrections encode microscopic interactions. Schwabl develops these corrections through the virial expansion, then uses the van der Waals equation as a simple mean-field model of liquid-gas coexistence.

The main conceptual shift is that the equation of state is no longer determined by one-particle momentum integrals alone. Configurational integrals over interparticle potentials enter, and their low-density expansion produces virial coefficients. These coefficients are measurable thermodynamic quantities and also microscopic integrals over molecular forces.

## From pair forces to a density expansion

The virial expansion writes the pressure as a density series:

$$
{p\over k_BT}
=n+B_2(T)n^2+B_3(T)n^3+\cdots,
\qquad n={N\over V}.
$$

Equivalently,

$$
{pV\over Nk_BT}
=1+B_2(T)n+B_3(T)n^2+\cdots.
$$

For a classical pair potential $u(r)$, the Mayer function is

$$
f(r)=e^{-\beta u(r)}-1.
$$

The second virial coefficient is

$$
B_2(T)=-{1\over 2}\int f(r)\,d^3r
=-2\pi\int_0^\infty \left(e^{-\beta u(r)}-1\right)r^2\,dr.
$$

The van der Waals equation is

$$
\left(p+a{N^2\over V^2}\right)(V-Nb)=Nk_BT,
$$

or in molar volume $v=V/N$,

$$
p={k_BT\over v-b}-{a\over v^2}.
$$

Here $b$ models excluded volume and $a$ models attractive cohesion.

The Mayer function arises by writing the configurational Boltzmann factor as

$$
e^{-\beta\sum_{i<j}u(r_{ij})}
=\prod_{i<j}[1+f(r_{ij})].
$$

Expanding the product organizes terms by graphs connecting particle labels. For two particles, the interaction correction to the configuration integral is $V\int f(r)d^3r$ up to boundary terms, and the resulting pressure correction is exactly the stated $B_2$. Higher coefficients involve connected clusters of three or more particles; $B_3$ is not generally determined by pairwise copies of $B_2$.

## Reading the second virial coefficient

For hard spheres of diameter $d$,

$$
u(r)=
\begin{cases}
\infty, & r<d,\\
0, & r>d.
\end{cases}
$$

Thus $e^{-\beta u}-1=-1$ inside the hard core and $0$ outside, giving

$$
B_2={2\pi d^3\over 3}.
$$

Attractions make $B_2$ smaller and can make it negative at low temperature. The Boyle temperature is defined by $B_2(T_B)=0$, where the leading real-gas correction vanishes.

For the van der Waals equation, the critical point satisfies

$$
\left({\partial p\over \partial v}\right)_T=0,
\qquad
\left({\partial^2 p\over \partial v^2}\right)_T=0.
$$

Solving gives

$$
v_c=3b,\qquad
k_BT_c={8a\over 27b},\qquad
p_c={a\over 27b^2}.
$$

Below $T_c$, the van der Waals isotherm has an unstable segment with positive slope in the $p$-$V$ curve. The Maxwell construction replaces it by a horizontal coexistence line whose areas above and below are equal:

$$
\int_{v_l}^{v_g}\left[p(v,T)-p_{\mathrm{coex}}\right]\,dv=0.
$$

This enforces equality of chemical potentials between liquid and gas.

Cluster expansions generalize the virial expansion by organizing many-particle configurational integrals into connected clusters. The physical rule is that disconnected pieces exponentiate into the partition function, while connected clusters contribute to $\ln Z$ and hence to thermodynamics.

The mechanical virial theorem gives another route to pressure. For an isotropic pair potential in three dimensions,

$$
pV=Nk_BT-{1\over6}
\left\langle\sum_{i\ne j}r_{ij}u'(r_{ij})\right\rangle.
$$

At low density, replace the pair distribution by its Boltzmann form $e^{-\beta u(r)}$. Integrating by parts recovers the $B_2$ correction. At higher density the radial distribution function $g(r)$ replaces the simple Boltzmann factor:

$$
p=nk_BT-{2\pi n^2\over3}
\int_0^\infty r^3u'(r)g(r)\,dr.
$$

This equation links the equation of state to liquid structure. It also shows why knowing the pair potential alone is insufficient at high density: correlations encoded in $g(r)$ depend on the collective state.

The sign and temperature dependence of $B_2$ give a compact diagnostic of interactions. A purely repulsive potential makes $e^{-\beta u(r)}-1\le 0$, so $B_2\gt 0$ and the pressure is larger than the ideal-gas value at the same density. Attractive regions make the Mayer function positive, lowering $B_2$. At high temperature, attractions are weak compared with $k_BT$ and excluded volume tends to dominate. At lower temperature, attractions can dominate and $B_2$ becomes negative, indicating a tendency toward condensation.

Expanding the van der Waals equation at low density provides a useful comparison:

$$
{p\over k_BT}
={n\over1-bn}-{a\over k_BT}n^2
=n+\left(b-{a\over k_BT}\right)n^2+b^2n^3+\cdots.
$$

Thus the model predicts $B_2^{\mathrm{vdW}}(T)=b-a/(k_BT)$ and Boyle temperature $k_BT_B=a/b$. Matching this form over a narrow range can motivate values of $a$ and $b$, but a real potential generally gives a more complicated temperature dependence and independent higher virial coefficients.

## The van der Waals landscape

The van der Waals parameters are a crude compression of this microscopic information. The excluded-volume parameter $b$ is related to short-range repulsion, while $a$ approximates the integrated attractive tail. But the model is not a systematic low-density expansion unless its parameters are matched carefully; it is better viewed as a mean-field equation of state. Its greatest value is qualitative: it produces a critical point, metastable branches, and coexistence from a simple analytic formula.

In reduced variables $p_r=p/p_c$, $v_r=v/v_c$, and $T_r=T/T_c$, all $a$ and $b$ dependence drops out:

$$
p_r={8T_r\over3v_r-1}-{3\over v_r^2}.
$$

This is the van der Waals law of corresponding states. Real substances show approximate corresponding behavior when their interactions have similar shapes, but two parameters cannot represent molecular polarity, association, or quantum effects.

## Why the Maxwell area is an equilibrium condition

The Maxwell construction can be derived by requiring equality of chemical potential. At fixed $T$,

$$
d\mu=v\,dp.
$$

Along an isotherm, the difference in chemical potential between two volumes is

$$
\mu(v_g)-\mu(v_l)=\int_{v_l}^{v_g} v\,dp.
$$

After integration by parts, equality of chemical potentials is equivalent to the equal-area rule in the $p$-$v$ diagram. Thus the graphical construction is not an arbitrary repair of a bad curve; it enforces phase equilibrium.

The middle part of the loop has $(\partial p/\partial v)_T\gt 0$, hence negative isothermal compressibility, and is mechanically unstable. Parts between the coexistence volumes and the spinodals have positive compressibility but higher free energy than the two-phase mixture; they are metastable. Nucleation can delay their decay, producing superheated liquid or supercooled vapor.

Near the critical point, expanding the van der Waals equation gives mean-field critical exponents. For example, the order parameter $v_g-v_l$ scales as $(T_c-T)^{1/2}$, and the isothermal compressibility diverges as $\vert T-T_c\vert ^{-1}$. Real fluids near criticality cross over to non-mean-field exponents because long-wavelength density fluctuations become important.

The critical isotherm can be read from the reduced equation. Put $T_r=1$, $v_r=1+\omega$, and expand for small $\omega$. The constant and linear and quadratic terms cancel at the critical point, leaving

$$
p_r-1=-{3\over2}\omega^3+O(\omega^4).
$$

Thus $\vert p-p_c\vert \propto\vert v-v_c\vert ^3$ and the mean-field critical exponent is $\delta=3$. The cancellations are another expression of the two derivative conditions defining the inflection point.

The model also predicts a density-dependent internal energy. A Helmholtz free energy consistent with the equation of state contains an attractive term $-aN^2/V$, leading, for constant $a$, to

$$
U(T,V,N)=U_{\mathrm{ideal}}(T,N)-a{N^2\over V}.
$$

Expansion at fixed energy can therefore change temperature, unlike free expansion of an ideal gas. Quantitative Joule and Joule--Thomson effects require more accurate equations of state, but the contrast locates the missing ideal-gas physics: intermolecular potential energy couples temperature to density.

The virial and van der Waals approaches therefore answer different questions. The virial expansion is controlled at low density and can be made systematically more accurate by computing more cluster integrals, but it does not by itself give a simple global picture of condensation. The van der Waals equation is uncontrolled near the critical region and inaccurate in detail, but it gives a compact thermodynamic landscape with unstable, metastable, and stable branches. A good statistical-mechanics reader should know which role each approximation is playing.

Liquids remain difficult precisely because neither limit is fully satisfactory. Their density is high, so low-density cluster expansions converge poorly, and their correlations are strong enough that simple mean fields miss structure. Liquid-state theory accordingly develops separate tools such as correlation functions, structure factors, and integral equations, even though the starting point is still the same canonical configurational integral.

The second virial coefficient can be measured experimentally by fitting low-density pressure data. This makes it a bridge between microscopic potential models and laboratory thermodynamics. If a proposed pair potential gives the wrong $B_2(T)$ over a range of temperatures, it cannot be a reliable molecular model even before higher-density behavior is tested.

Experimental virial data may be reported in powers of pressure rather than density. If

$$
{p\over nk_BT}=1+B_2n+B_3n^2+\cdots,
$$

inverting the series gives a compressibility factor of the form $1+B_2'p+B_3'p^2+\cdots$ with different coefficients and units. The two conventions should not be mixed. Density virial coefficients connect most directly to cluster integrals.

For mixtures, the second correction becomes a sum over species pairs,

$$
{p\over k_BT}=\sum_i n_i+sum_{ij}B_{ij}(T)n_in_j+\cdots.
$$

Cross coefficients probe unlike-particle interactions and cannot generally be inferred by averaging pure-component coefficients. Phase equilibrium in a mixture then requires equality of every component chemical potential across phases, adding composition variables to the liquid--gas construction.

The critical-point failure of mean-field theory is also visible experimentally as critical opalescence: long-wavelength density fluctuations scatter light strongly. Such phenomena are outside the smooth van der Waals picture but natural in the scaling picture developed later.

The compressibility sum rule connects those fluctuations to structure:

$$
S(0)=nk_BT\kappa_T,
$$

where $S(0)$ is the zero-wave-number limit of the static structure factor. The van der Waals divergence of $\kappa_T$ signals growing long-wavelength density fluctuations, but its mean-field treatment does not calculate their correct critical scaling. Virial coefficients characterize dilute local correlations; the structure factor describes correlations across length scales.

Temperature derivatives of virial coefficients also determine caloric corrections. Pressure data alone give $B_2(T)$, while the interaction contribution to internal energy involves $dB_2/dT$. A gas can have a pressure close to ideal at the Boyle temperature and still have nonzero interaction energy, because cancellation in $B_2$ does not force its temperature derivative to vanish.

The radius of convergence of a virial series is controlled by singularities of the thermodynamic functions in the complex-density plane, not merely by the numerical size of the next fitted term. Close agreement of two truncations over a short interval is useful evidence but not a proof that the series reaches the liquid regime.

```text
p
^        T > Tc
|         \____
|              \__
|   T = Tc       \__
|      \__          \_
|         \__
| T < Tc     \_/---\_
|          Maxwell line
+----------------------------> v
```

| Model | Microscopic input | Strength | Limitation |
|---|---:|---|---|
| Virial expansion | pair and higher cluster integrals | systematic at low density | fails near condensation/criticality |
| Hard spheres | excluded volume only | exact $B_2$ simple | no attraction, no liquid-gas transition |
| van der Waals | two parameters $a,b$ | qualitative coexistence and critical point | mean-field exponents, poor near criticality |
| Cluster expansion | connected Mayer graphs | principled interaction expansion | combinatorially complex |

## Worked example 1: Second virial coefficient of hard spheres

Problem: Derive $B_2$ for hard spheres of diameter $d$.

Method:

1. For $r\lt d$, $u(r)=\infty$, so

$$
e^{-\beta u(r)}=0,
\qquad
f(r)=-1.
$$

2. For $r\gt d$, $u(r)=0$, so

$$
e^{-\beta u(r)}=1,
\qquad
f(r)=0.
$$

3. Insert into

$$
B_2=-{1\over 2}\int f(r)\,d^3r.
$$

4. Only the excluded sphere contributes:

$$
B_2=-{1\over 2}\int_{r<d}(-1)\,d^3r
={1\over 2}{4\pi d^3\over 3}
={2\pi d^3\over 3}.
$$

Checked answer: $B_2$ is four times the physical volume of one hard sphere, because the excluded volume is a two-particle relative-coordinate volume.

## Worked example 2: van der Waals critical constants

Problem: Starting from

$$
p={k_BT\over v-b}-{a\over v^2},
$$

derive $v_c$, $T_c$, and $p_c$.

Method:

1. Differentiate once:

$$
{\partial p\over \partial v}
=-{k_BT\over (v-b)^2}+{2a\over v^3}.
$$

At criticality this is zero:

$$
{k_BT_c\over (v_c-b)^2}={2a\over v_c^3}.
$$

2. Differentiate twice:

$$
{\partial^2p\over \partial v^2}
={2k_BT\over (v-b)^3}-{6a\over v^4}.
$$

At criticality:

$$
{2k_BT_c\over (v_c-b)^3}={6a\over v_c^4}.
$$

3. Divide the second condition by the first:

$$
{2\over v_c-b}={3\over v_c},
$$

so

$$
2v_c=3v_c-3b,\qquad v_c=3b.
$$

4. Substitute into the first condition:

$$
{k_BT_c\over (2b)^2}={2a\over (3b)^3},
\qquad
k_BT_c={8a\over 27b}.
$$

5. Insert into the equation of state:

$$
p_c={k_BT_c\over 2b}-{a\over 9b^2}
={4a\over 27b^2}-{3a\over 27b^2}
={a\over 27b^2}.
$$

Checked answer: the compressibility factor is $p_cv_c/(k_BT_c)=3/8$, the classic van der Waals prediction.

## Worked example 3: square-well potential and Boyle temperature

Consider

$$
u(r)=
\begin{cases}
\infty,&0<r<d,\\
-\varepsilon,&d<r<\lambda d,\\
0,&r>\lambda d,
\end{cases}
$$

with $\lambda\gt 1$. The Mayer function is $-1$ in the hard core, $e^{\beta\varepsilon}-1$ in the attractive well, and zero outside. Split the radial integral:

$$
\begin{aligned}
B_2
&=-2\pi\left[
\int_0^d(-1)r^2dr
+\int_d^{\lambda d}(e^{\beta\varepsilon}-1)r^2dr
\right]\\
&={2\pi d^3\over3}
\left[1-(\lambda^3-1)(e^{\beta\varepsilon}-1)\right].
\end{aligned}
$$

The Boyle condition $B_2=0$ gives

$$
e^{\varepsilon/(k_BT_B)}-1={1\over\lambda^3-1},
$$

so

$$
k_BT_B={\varepsilon\over
\ln[1+1/(\lambda^3-1)]}.
$$

The hard core contributes positively and the well negatively. Increasing the well depth or range raises the temperature at which attraction and exclusion cancel.

## Choosing the approximation by regime

- The virial series is a low-density expansion. Adding one more term does not make it reliable in a dense liquid if the series is outside its useful range.
- Attractive regions can make $B_2(T)$ negative. Its sign cannot be inferred from the hard-core diameter alone.
- The rising portion of a subcritical van der Waals loop has negative compressibility and is unstable. Equilibrium uses a two-phase Maxwell line.
- The hard-sphere diameter is the center-to-center exclusion distance, twice the radius of the sphere model.
- Van der Waals critical exponents are mean-field values. Density fluctuations close to a real fluid critical point change them.
- $a$ and $b$ are model parameters whose numerical convention depends on whether $v$ is per particle or per mole.

<div className="see-also">

See also: [Thermodynamic potentials and phase equilibrium](/physics/statistical-mechanics/thermodynamic-potentials-and-phase-equilibrium) · [Phase transitions and order parameters](/physics/statistical-mechanics/phase-transitions-and-order-parameters) · [Mean-field and Landau theory](/physics/statistical-mechanics/mean-field-and-landau-theory) · [Classical ideal gas and Maxwell distribution](/physics/statistical-mechanics/classical-ideal-gas-and-maxwell-distribution) · [Thermodynamics](/physics/thermodynamics/intro)

</div>
