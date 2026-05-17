---
title: Real Gases, Virial Expansion, and van der Waals Theory
sidebar_position: 12
---

# Real Gases, Virial Expansion, and van der Waals Theory

Real gases differ from ideal gases because molecules exclude volume and attract or repel each other. The ideal gas is still the reference point, but corrections encode microscopic interactions. Schwabl develops these corrections through the virial expansion, then uses the van der Waals equation as a simple mean-field model of liquid-gas coexistence.

The main conceptual shift is that the equation of state is no longer determined by one-particle momentum integrals alone. Configurational integrals over interparticle potentials enter, and their low-density expansion produces virial coefficients. These coefficients are measurable thermodynamic quantities and also microscopic integrals over molecular forces.

## Definitions

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

## Key results

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

The sign and temperature dependence of $B_2$ give a compact diagnostic of interactions. A purely repulsive potential makes $e^{-\beta u(r)}-1\le 0$, so $B_2\gt 0$ and the pressure is larger than the ideal-gas value at the same density. Attractive regions make the Mayer function positive, lowering $B_2$. At high temperature, attractions are weak compared with $k_BT$ and excluded volume tends to dominate. At lower temperature, attractions can dominate and $B_2$ becomes negative, indicating a tendency toward condensation.

The van der Waals parameters are a crude compression of this microscopic information. The excluded-volume parameter $b$ is related to short-range repulsion, while $a$ approximates the integrated attractive tail. But the model is not a systematic low-density expansion unless its parameters are matched carefully; it is better viewed as a mean-field equation of state. Its greatest value is qualitative: it produces a critical point, metastable branches, and coexistence from a simple analytic formula.

The Maxwell construction can be derived by requiring equality of chemical potential. At fixed $T$,

$$
d\mu=v\,dp.
$$

Along an isotherm, the difference in chemical potential between two volumes is

$$
\mu(v_g)-\mu(v_l)=\int_{v_l}^{v_g} v\,dp.
$$

After integration by parts, equality of chemical potentials is equivalent to the equal-area rule in the $p$-$v$ diagram. Thus the graphical construction is not an arbitrary repair of a bad curve; it enforces phase equilibrium.

Near the critical point, expanding the van der Waals equation gives mean-field critical exponents. For example, the order parameter $v_g-v_l$ scales as $(T_c-T)^{1/2}$, and the isothermal compressibility diverges as $\vert T-T_c\vert ^{-1}$. Real fluids near criticality cross over to non-mean-field exponents because long-wavelength density fluctuations become important.

The virial and van der Waals approaches therefore answer different questions. The virial expansion is controlled at low density and can be made systematically more accurate by computing more cluster integrals, but it does not by itself give a simple global picture of condensation. The van der Waals equation is uncontrolled near the critical region and inaccurate in detail, but it gives a compact thermodynamic landscape with unstable, metastable, and stable branches. A good statistical-mechanics reader should know which role each approximation is playing.

Liquids remain difficult precisely because neither limit is fully satisfactory. Their density is high, so low-density cluster expansions converge poorly, and their correlations are strong enough that simple mean fields miss structure. This is why liquid-state theory develops separate tools such as correlation functions, structure factors, and integral equations, even though the starting point is still the same canonical configurational integral.

The second virial coefficient can be measured experimentally by fitting low-density pressure data. This makes it a bridge between microscopic potential models and laboratory thermodynamics. If a proposed pair potential gives the wrong $B_2(T)$ over a range of temperatures, it cannot be a reliable molecular model even before higher-density behavior is tested.

The critical-point failure of mean-field theory is also visible experimentally as critical opalescence: long-wavelength density fluctuations scatter light strongly. Such phenomena are outside the smooth van der Waals picture but natural in the scaling picture developed later.

## Visual

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

## Code

```python
import numpy as np

def vdw_pressure(v, T, a=1.0, b=0.1, kB=1.0):
    return kB * T / (v - b) - a / v**2

def hard_sphere_B2(d):
    return 2 * np.pi * d**3 / 3

a, b = 1.0, 0.1
Tc = 8 * a / (27 * b)
vc = 3 * b
pc = a / (27 * b**2)
print("critical", Tc, vc, pc)
print("B2 hard sphere d=1", hard_sphere_B2(1.0))

v = np.linspace(0.12, 2.0, 8)
print(vdw_pressure(v, 0.8 * Tc, a=a, b=b))
```

## Common pitfalls

- Using the virial expansion at high density where powers of $n$ no longer converge usefully.
- Forgetting that $B_2(T)$ can be negative when attractions dominate.
- Treating the unstable van der Waals loop as physical instead of applying the Maxwell construction.
- Confusing the hard-sphere diameter $d$ with the molecular radius.
- Assuming van der Waals critical exponents are exact for real fluids; they are mean-field values.

## Connections

- [Thermodynamic potentials and phase equilibrium](/physics/statistical-mechanics/thermodynamic-potentials-and-phase-equilibrium)
- [Phase transitions and order parameters](/physics/statistical-mechanics/phase-transitions-and-order-parameters)
- [Mean-field and Landau theory](/physics/statistical-mechanics/mean-field-and-landau-theory)
- [Classical ideal gas and Maxwell distribution](/physics/statistical-mechanics/classical-ideal-gas-and-maxwell-distribution)
- [Thermodynamics](/physics/thermodynamics/)
