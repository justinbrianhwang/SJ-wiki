---
title: Thermodynamic Potentials and Phase Equilibrium
sidebar_position: 11
---

# Thermodynamic Potentials and Phase Equilibrium

Thermodynamic potentials are Legendre transforms of the internal energy. Statistical mechanics supplies them from partition functions, but their power is broader: they encode natural variables, stability, response functions, and phase coexistence. Schwabl uses this machinery to connect ensembles with the laws of equilibrium thermodynamics.

Phase equilibrium is where the formalism becomes geometric. A stable phase minimizes the appropriate potential under the imposed constraints; coexistence means two phases have equal chemical potential or equal Gibbs free energy per particle. Slopes of coexistence curves follow from derivative identities rather than from microscopic details.

## Definitions

The fundamental thermodynamic differential for a simple single-component system is

$$
dE=T\,dS-p\,dV+\mu\,dN.
$$

Legendre transforms define

$$
F=E-TS,
\qquad
H_E=E+pV,
\qquad
G=E-TS+pV.
$$

Here $H_E$ denotes enthalpy, avoiding conflict with the Hamiltonian. Their differentials are

$$
dF=-S\,dT-p\,dV+\mu\,dN,
$$

$$
dH_E=T\,dS+V\,dp+\mu\,dN,
$$

$$
dG=-S\,dT+V\,dp+\mu\,dN.
$$

For a homogeneous one-component system,

$$
G=\mu N.
$$

The Gibbs-Duhem relation is

$$
S\,dT - V\,dp + N\,d\mu=0.
$$

## Key results

Maxwell relations follow from equality of mixed partial derivatives. From $dF=-S\,dT-p\,dV$ at fixed $N$,

$$
\left({\partial S\over \partial V}\right)_{T,N}
=
\left({\partial p\over \partial T}\right)_{V,N}.
$$

From $dG=-S\,dT+V\,dp$,

$$
\left({\partial S\over \partial p}\right)_{T,N}
=-
\left({\partial V\over \partial T}\right)_{p,N}.
$$

Stability requires appropriate convexity or concavity. For example,

$$
C_V=T\left({\partial S\over \partial T}\right)_{V,N}\ge 0,
$$

and the isothermal compressibility

$$
\kappa_T=-{1\over V}\left({\partial V\over \partial p}\right)_{T,N}
$$

must be nonnegative for mechanical stability.

For two phases $\alpha$ and $\beta$ of one component in coexistence,

$$
\mu_\alpha(T,p)=\mu_\beta(T,p).
$$

Differentiating along the coexistence curve gives the Clausius-Clapeyron equation:

$$
{dp\over dT}
={s_\beta-s_\alpha\over v_\beta-v_\alpha}
={L\over T(v_\beta-v_\alpha)},
$$

where $s$ and $v$ are entropy and volume per particle and $L=T(s_\beta-s_\alpha)$ is latent heat per particle.

For multicomponent systems, Gibbs' phase rule is

$$
f=C-P+2,
$$

where $C$ is the number of components, $P$ the number of phases, and $f$ the number of intensive degrees of freedom.

Legendre transforms should be read as changes of experimental control. If the walls are fixed and the system is held at a fixed temperature, $F$ is the potential that decreases toward equilibrium. If pressure and temperature are imposed by reservoirs, $G$ is the useful potential. In the grand ensemble, $T,V,\mu$ are fixed and the grand potential $\Phi_G$ is minimized. Using the wrong potential is a common source of sign errors and incorrect stability conditions.

Phase coexistence has a simple free-energy geometry. At fixed $T$, a stable single phase has a convex Helmholtz free energy as a function of volume or density. A concave segment would imply negative compressibility and instability. The physical free energy is the convex envelope, which represents a mixture of two phases. The Maxwell construction in the van der Waals model is the equation-of-state version of this convexification.

The chemical potential is the slope of free energy with respect to particle number. In a one-component system at fixed $T$ and $p$, equality of $\mu$ between phases is equivalent to equality of molar Gibbs free energies. For a multicomponent system, every independently transferable component must have equal chemical potential across coexisting phases. This condition is what drives distillation, osmosis, alloy phase separation, and chemical partitioning.

Response functions are second derivatives of potentials, so their signs express stability. For example, $C_V\gt 0$ follows from energy fluctuations in the canonical ensemble, and $\kappa_T\gt 0$ follows from volume stability at fixed temperature. Near criticality these second derivatives can become large, signaling that the free-energy surface is becoming flat in an order-parameter direction.

Thermodynamic identities are most reliable when derived from differentials rather than memorized. For instance, if a derivative contains variables that are not natural for the chosen potential, Jacobian manipulations or Maxwell relations are needed. Schwabl emphasizes these derivative methods because statistical mechanics constantly moves between ensembles. A fluctuation formula may naturally give a derivative at fixed $T,V,N$, while an experiment may report a derivative at fixed $T,p,N$.

The Gibbs-Duhem relation also prevents intensive variables from varying independently in a single homogeneous phase. For one component,

$$
d\mu=-s\,dT+v\,dp.
$$

This compact formula underlies coexistence slopes, chemical-potential matching, and the response of open systems to reservoir changes.

Jacobians are often the safest way to transform derivatives. If an equation of state is known in variables $(T,V,N)$ but an experiment fixes $(T,p,N)$, direct substitution can silently hold the wrong variable constant. Writing derivatives as Jacobian ratios keeps the constraints explicit and prevents common sign mistakes in heat-capacity and compressibility identities.

Phase diagrams are maps of which potential minimum is global under each set of intensive variables. Metastable extensions may be drawn, but equilibrium curves are determined by equality of the appropriate potentials. This is why the same microscopic model can show smooth behavior in one path through parameter space and a discontinuity along another.

In multicomponent systems, the same logic operates in a higher-dimensional composition space. Tie lines, coexistence surfaces, and reaction constraints are geometric expressions of minimizing free energy under conservation laws. Gibbs' phase rule is a dimension count of this constrained minimization problem, not a separate empirical rule.

The statistical-mechanical role of these potentials is to summarize many microscopic states into a surface whose derivatives are observable quantities. Once $F$, $G$, or $\Phi_G$ is known, equations of state, stability tests, and coexistence conditions are obtained by calculus. That is why partition functions are so central.

This calculus-first discipline is what keeps signs, constraints, and physical interpretations aligned.

## Visual

```text
p
^
|                 solid
|                  /
|                 /  liquid
|        triple  *-------- critical *
|              /   \      /
|             /     \    /
|            /       vapor
+----------------------------------> T
```

| Potential | Natural variables | Equilibrium principle |
|---|---:|---|
| $E$ | $S,V,N$ | minimized at fixed $S,V,N$ |
| $F=E-TS$ | $T,V,N$ | minimized at fixed $T,V,N$ |
| $H_E=E+pV$ | $S,p,N$ | minimized at fixed $S,p,N$ |
| $G=E-TS+pV$ | $T,p,N$ | minimized at fixed $T,p,N$ |
| $\Phi_G=E-TS-\mu N$ | $T,V,\mu$ | minimized at fixed $T,V,\mu$ |

## Worked example 1: A Maxwell relation from the Helmholtz free energy

Problem: Derive

$$
\left({\partial S\over \partial V}\right)_T
=
\left({\partial p\over \partial T}\right)_V
$$

from $F(T,V)$.

Method:

1. Start with

$$
dF=-S\,dT-p\,dV.
$$

2. Identify first derivatives:

$$
S=-\left({\partial F\over \partial T}\right)_V,
\qquad
p=-\left({\partial F\over \partial V}\right)_T.
$$

3. Differentiate $S$ with respect to $V$:

$$
\left({\partial S\over \partial V}\right)_T
=-\frac{\partial^2 F}{\partial V\,\partial T}.
$$

4. Differentiate $p$ with respect to $T$:

$$
\left({\partial p\over \partial T}\right)_V
=-\frac{\partial^2 F}{\partial T\,\partial V}.
$$

5. Equality of mixed partial derivatives gives the result.

Checked answer: the signs match because both $S$ and $p$ enter $dF$ with minus signs.

## Worked example 2: Slope of a vapor-pressure curve

Problem: Estimate $dp/dT$ for a liquid-vapor transition at $T=373\,\mathrm K$ with molar latent heat $L_m=40.7\,\mathrm{kJ/mol}$ and vapor molar volume $v_g=3.06\times 10^{-2}\,\mathrm{m^3/mol}$. Neglect the liquid molar volume.

Method:

1. Use the molar Clausius-Clapeyron formula:

$$
{dp\over dT}={L_m\over T(v_g-v_l)}.
$$

2. Neglect $v_l$:

$$
{dp\over dT}\approx {L_m\over T v_g}.
$$

3. Insert values:

$$
T v_g=(373)(3.06\times 10^{-2})
\approx 11.41\,\mathrm{m^3 K/mol}.
$$

4. Compute the slope:

$$
{dp\over dT}
\approx {4.07\times 10^4\over 11.41}
\approx 3.57\times 10^3\,\mathrm{Pa/K}.
$$

Checked answer: near the normal boiling point, vapor pressure changes by several kilopascals per kelvin, consistent with the steep liquid-vapor curve.

## Code

```python
def clapeyron_slope(T, latent_heat_molar, v_gas_molar, v_liquid_molar=0.0):
    return latent_heat_molar / (T * (v_gas_molar - v_liquid_molar))

def gibbs_phase_rule(components, phases):
    return components - phases + 2

print(clapeyron_slope(373.0, 40.7e3, 3.06e-2), "Pa/K")
for C, P in [(1, 1), (1, 2), (1, 3), (2, 2)]:
    print(C, P, gibbs_phase_rule(C, P))
```

## Common pitfalls

- Mixing natural variables when differentiating a potential. Each potential has its own correct independent variables.
- Forgetting that phase coexistence for one component means equal chemical potentials, not merely equal pressures.
- Applying the Clausius-Clapeyron equation with total latent heat and per-particle volume changes; units must match.
- Treating the critical point as a triple point. At a critical point two phases become indistinguishable; at a triple point three coexist.
- Ignoring stability conditions when an equation of state gives negative compressibility.

## Connections

- [Canonical ensemble and fluctuations](/physics/statistical-mechanics/canonical-ensemble-and-fluctuations)
- [Grand canonical ensemble and particle exchange](/physics/statistical-mechanics/grand-canonical-ensemble-and-particle-exchange)
- [Real gases, virial expansion, and van der Waals theory](/physics/statistical-mechanics/real-gases-virial-expansion-and-van-der-waals-theory)
- [Phase transitions and order parameters](/physics/statistical-mechanics/phase-transitions-and-order-parameters)
- [Thermodynamics](/physics/thermodynamics/)
