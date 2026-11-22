---
title: Renormalization Group
sidebar_position: 9
---

# Renormalization Group

A theory written at one resolution can be rewritten at another. Short-distance modes are integrated out, their effects are absorbed into new coefficients, and the remaining fields are rescaled. Repeating the operation traces a flow through the space of possible actions.

The same structure appears in two common languages. Wilsonian renormalization changes a physical cutoff and retains modes below it. The Callan--Symanzik approach changes an arbitrary subtraction scale while holding bare quantities fixed. Their couplings need not be identical coordinate systems, but both describe scale dependence and agree on observable consequences.

## Coarse-graining a field theory

Begin with a Euclidean scalar theory with cutoff $\Lambda$. Split its Fourier modes into

$$
\phi=\phi_<+\phi_>,
$$

where

$$
|k|<\frac{\Lambda}{b}
\quad\text{for }\phi_<,
\qquad
\frac{\Lambda}{b}<|k|<\Lambda
\quad\text{for }\phi_>,
\qquad b>1.
$$

Define an effective action for the slow modes by

$$
e^{-S_{\mathrm{eff}}[\phi_<]}
=
\int\mathcal D\phi_>\,
e^{-S[\phi_<+\phi_>]}.
$$

Even if the initial action contains only a few operators, shell integration generally produces every local operator allowed by the symmetries. The result may contain $\phi^6$, derivative interactions, and many others. Their coefficients are correlated by the integration.

The new cutoff is $\Lambda/b$. Rescale momentum $k'=bk$, coordinates $x'=x/b$, and the field so that the kinetic term has its original normalization. The cutoff is again $\Lambda$, but the dimensionless couplings have changed. Iteration defines the Wilsonian RG map.

```mermaid
flowchart LR
  A["Action with cutoff Lambda"] --> B["Split slow and fast modes"]
  B --> C["Integrate momentum shell"]
  C --> D["Action with cutoff Lambda over b"]
  D --> E["Rescale coordinates and fields"]
  E --> F["New point in coupling space"]
  F --> B
```

The flow parameter is not time. It labels resolution. Coarse-graining toward long distances is an infrared flow; reversing it asks how the description behaves toward the ultraviolet.

## Dimensionless couplings and linearized flow

Let an action contain

$$
S\supset\int d^dx\,g_i\mathcal O_i(x),
$$

where $\mathcal O_i$ has scaling dimension $\Delta_i$. The coupling has mass dimension

$$
[g_i]=d-\Delta_i.
$$

A dimensionless coupling can be formed as

$$
\widetilde g_i(\mu)
=\mu^{\Delta_i-d}g_i(\mu).
$$

Near a fixed point $g_i^*$, write $\delta g_i=g_i-g_i^*$. Linearization gives

$$
\frac{d}{d\log\mu}\delta g_i
=\sum_jB_{ij}\delta g_j,
\qquad
B_{ij}
=\left.\frac{\partial\beta_i}{\partial g_j}\right|_*.
$$

After diagonalizing $B$, an eigendirection obeys

$$
\delta g_a(\mu)
\propto\left(\frac{\mu}{\mu_0}\right)^{\vartheta_a}.
$$

Sign conventions vary because some authors parameterize flow toward larger length rather than larger energy. It is safer to state the behavior: a relevant perturbation grows under coarse-graining toward the infrared; an irrelevant one shrinks; a marginal direction needs nonlinear terms in the beta function.

At the Gaussian fixed point, engineering dimensions give

| Coupling dimension $d-\Delta$ | Infrared behavior | Name |
|---:|---|---|
| positive | grows | relevant |
| zero | decided by loop corrections | marginal at tree level |
| negative | shrinks | irrelevant |

At an interacting fixed point, full scaling dimensions replace engineering dimensions. Operator mixing also means that monomials written in the original fields may not be the eigenoperators of linearized flow.

## Running parameters and beta functions

In a renormalized description, a coupling $g(\mu)$ obeys

$$
\beta(g)=\mu\frac{dg}{d\mu}.
$$

The scale $\mu$ enters when a renormalization condition is imposed. A physical observable cannot depend on this arbitrary choice, but its expression splits into explicit logarithms of $\mu$ and implicit dependence through running parameters. The two cancel when calculations are performed consistently.

For one charged Dirac fermion in QED,

$$
\beta(e)=\frac{e^3}{12\pi^2}+O(e^5).
$$

The positive sign means the effective electromagnetic coupling grows toward high energy. Vacuum polarization screens charge at long distance.

For an $SU(N_c)$ gauge theory with $n_f$ Dirac fermions in the fundamental representation,

$$
\beta(g)
=-\frac{g^3}{16\pi^2}
\left(
\frac{11}{3}N_c-\frac{2}{3}n_f
\right)
+O(g^5).
$$

When the bracket is positive, the coupling decreases toward high energy. Gauge-boson self-interactions produce the antiscreening term. The one-loop coefficient is universal under ordinary analytic scheme changes; higher coefficients have more scheme dependence, with qualifications about the class of schemes used.

## Solving one-loop flow

Suppose

$$
\mu\frac{dg}{d\mu}=-b_0g^3,
\qquad b_0>0.
$$

Using $t=\log\mu$ and separating variables,

$$
\int_{g_0}^{g(\mu)}\frac{dg}{g^3}
=-b_0\int_{\log\mu_0}^{\log\mu}dt.
$$

Evaluation gives

$$
\frac1{g^2(\mu)}
=\frac1{g_0^2}
+2b_0\log\frac{\mu}{\mu_0}.
$$

Define an RG-invariant scale by

$$
\Lambda
=\mu\exp\left[-\frac1{2b_0g^2(\mu)}\right].
$$

Then

$$
g^2(\mu)
=\frac1{2b_0\log(\mu/\Lambda)}.
$$

A dimensionless input coupling has been traded for a dimensionful scale, a phenomenon called dimensional transmutation. The one-loop expression is trustworthy only for $\mu\gg\Lambda$, where $g$ is small. Its divergence near $\Lambda$ marks the failure of perturbation theory, not a literal proof that the exact coupling is infinite.

For a positive beta function $\beta(g)=+b_0g^3$, the denominator instead decreases toward the ultraviolet and predicts a Landau pole. That pole may lie far beyond the regime where the theory is intended as an effective description.

## The Callan--Symanzik equation

Let $G_R^{(n)}$ be a renormalized $n$-point function. Independence of the bare correlator from $\mu$ gives, in a simplified massless theory,

$$
\left[
\mu\frac{\partial}{\partial\mu}
+\beta(g)\frac{\partial}{\partial g}
+n\gamma_\phi(g)
\right]
G_R^{(n)}=0.
$$

Depending on the convention for $Z_\phi$ and $\gamma_\phi$, the sign of the last term may be written oppositely. With masses present one adds a mass-running term. Composite operator insertions require anomalous-dimension matrices.

The equation resums logarithms. If a fixed-order result contains powers of $g\log(Q/\mu)$, choosing $\mu$ near the characteristic momentum $Q$ prevents large explicit logarithms, while evolving $g$ from a reference scale resums their leading towers. A multi-scale process may need factorization and several coupled RG equations rather than one optimal scale.

## Anomalous dimensions and fixed-point correlators

Interactions alter scaling dimensions. For a field,

$$
\Delta_\phi
=\frac{d-2}{2}+\gamma_\phi^*
$$

at a fixed point, where $\gamma_\phi^*$ is the fixed-point anomalous contribution in the stated convention. Scale invariance then constrains the two-point function:

$$
\langle\phi(x)\phi(0)\rangle
\propto\frac1{|x|^{2\Delta_\phi}}.
$$

At the Gaussian fixed point $\gamma_\phi^*=0$. At an interacting fixed point it need not vanish.

A fixed point can control a continuous phase transition. The correlation length diverges as

$$
\xi\sim|t|^{-\nu},
$$

where $t$ is the relevant temperature-like deformation. If its RG eigenvalue under length rescaling is $y_t\gt 0$, then

$$
\nu=\frac1{y_t}.
$$

Microscopic systems with the same dimensionality, symmetry, field content, and relevant deformations can approach the same fixed point and share critical exponents. This is universality. Microscopic lattice details affect nonuniversal scales and corrections to scaling, while irrelevant couplings fade at long distance.

## Worked example: classifying scalar operators

At the free scalar fixed point in $d$ dimensions,

$$
[\phi]=\frac{d-2}{2}.
$$

For $d=4$, $[\phi]=1$. The operators have dimensions

$$
[\phi^2]=2,
\qquad
[\phi^4]=4,
\qquad
[\phi^6]=6.
$$

Their coupling dimensions are

$$
[g_2]=4-2=2,
\qquad
[g_4]=4-4=0,
\qquad
[g_6]=4-6=-2.
$$

Under infrared coarse-graining, the mass perturbation grows, $\phi^6$ shrinks, and $\phi^4$ is classically marginal. Quantum corrections decide the last case. In four-dimensional scalar theory the quartic coupling is marginally irrelevant toward the infrared for small positive coupling, or equivalently grows slowly toward the ultraviolet.

Now repeat in $d=3$. The free-field dimension is $1/2$, so

$$
[\phi^4]=2,
\qquad
[g_4]=3-2=1.
$$

The quartic interaction is relevant at the three-dimensional Gaussian fixed point. Its flow can approach an interacting Wilson--Fisher fixed point, where engineering dimensions no longer give the final critical exponents.

## Worked example: RG improvement of a logarithm

Suppose an amplitude calculated to one loop has the form

$$
\mathcal A(Q)
=g(\mu)
+c\,g^2(\mu)\log\frac{Q}{\mu}
+O(g^3).
$$

Let

$$
\beta(g)=b\,g^2+O(g^3).
$$

Demand scale independence through order $g^2$:

$$
0=\frac{d\mathcal A}{d\log\mu}
=\beta(g)
-cg^2+O(g^3).
$$

Thus consistency requires $c=b$ in this simplified example. Solve the running:

$$
\frac{dg}{d\log\mu}=bg^2.
$$

Integration gives

$$
\frac1{g(Q)}
=\frac1{g(\mu)}
-b\log\frac{Q}{\mu}.
$$

Expanding the solution,

$$
g(Q)
=\frac{g(\mu)}
{1-bg(\mu)\log(Q/\mu)}
=g(\mu)+bg^2(\mu)\log\frac{Q}{\mu}+\cdots.
$$

The one-loop logarithm is precisely the first term in the expansion of the running coupling. Choosing $\mu=Q$ moves the large logarithm into $g(Q)$ and sums the leading repeated contributions.

## Worked example: a simple two-coupling fixed point

Consider

$$
\beta_r=2r,
\qquad
\beta_u=-\epsilon u+3u^2.
$$

The fixed points satisfy both beta functions equal to zero. The first equation gives $r^*=0$. The second gives

$$
u^*=0
\quad\text{or}\quad
u^*=\frac{\epsilon}{3}.
$$

At the interacting point, the stability matrix is diagonal:

$$
B=
\begin{pmatrix}
2&0\\
0&-\epsilon+6u^*
\end{pmatrix}
=
\begin{pmatrix}
2&0\\
0&\epsilon
\end{pmatrix}.
$$

These eigenvalues describe flow with increasing $\mu$ under the convention used in the beta functions. To discuss infrared relevance, reverse the direction and inspect whether perturbations grow during coarse-graining. The example also shows why naming a direction from a sign alone is risky unless the flow convention has been declared.

## Thresholds and effective theories

A particle of mass $M$ does not contribute equally at all scales. In mass-independent subtraction schemes, beta functions may still display the heavy field below $M$. One then matches the full theory to an effective theory near $\mu\sim M$ and runs with the lighter particle content below the threshold.

Matching fixes finite threshold corrections; running evolves between well-separated scales. Keeping those tasks distinct avoids large logarithms. Gauge-coupling unification, weak decays, and heavy-particle effects all use this pattern.

## Points that require a declared convention

- Relevant and irrelevant refer to behavior near a specified fixed point and in a specified flow direction.
- A running coupling is scheme-dependent; an observable assembled from it and the corresponding matrix elements is not.
- Engineering dimensions classify perturbations only near a Gaussian fixed point. Interacting fixed points require full scaling dimensions.
- Marginal at tree level does not mean exactly marginal. The first nonzero beta-function term decides.
- A perturbative pole marks loss of perturbative control or of the effective description. Its exact physical interpretation needs more information.
- Universality requires matching symmetries and relevant variables, not merely similar-looking microscopic Hamiltonians.
- Decoupling heavy particles may require explicit EFT matching in a mass-independent scheme.

## Scheme changes as coordinate changes

Let two renormalization schemes define couplings related perturbatively by

$$
g'=g+a g^3+O(g^5).
$$

Their beta functions obey the chain rule:

$$
\beta'(g')
=\frac{dg'}{dg}\beta(g).
$$

If

$$
\beta(g)=b_1g^3+b_2g^5+\cdots,
$$

substitution shows that the leading coefficient is unchanged by this analytic redefinition. Later coefficients can change, depending on the coupling structure and permitted class of schemes. Fixed-point coordinates are therefore scheme-dependent, while critical exponents obtained from the linearized flow are invariant under nonsingular coordinate changes.

This geometric view prevents overinterpretation of a plotted trajectory. A beta function describes components of a vector field in chosen coupling coordinates. The existence of a fixed point and universal scaling data are more robust than the numerical value assigned to a nonobservable coupling there.

## Deriving correlation-length scaling

Near a critical fixed point, let $t$ be the single relevant temperature-like scaling field. Under a length rescaling by $b$,

$$
t\to t'=b^{y_t}t,
$$

with $y_t\gt 0$. The correlation length transforms as a length:

$$
\xi(t)=b\,\xi(t').
$$

Choose $b$ so the transformed coupling becomes order one:

$$
b^{y_t}|t|=1,
\qquad
b=|t|^{-1/y_t}.
$$

The remaining correlation length $\xi(t')$ is a finite microscopic number. Therefore

$$
\xi(t)\propto|t|^{-1/y_t},
\qquad
\nu=\frac1{y_t}.
$$

An irrelevant coupling $u$ with exponent $y_u\lt 0$ produces corrections suppressed by $b^{y_u}$. Expressed in $t$, these become powers such as $\vert t\vert ^{-y_u/y_t}$. Finite data near a critical point often require these corrections before the asymptotic exponent can be extracted reliably.

The same reasoning gives scaling forms. If an operator $O$ has dimension $\Delta_O$, its two-point function near criticality can be written

$$
\langle O(x)O(0)\rangle_t
=\frac1{|x|^{2\Delta_O}}
F\left(\frac{|x|}{\xi}
ight)
$$

up to normalization and corrections from irrelevant variables. At criticality, $\xi$ diverges and the scaling function approaches a constant in the short-distance regime.

## Dangerous irrelevant variables

Calling a coupling irrelevant usually means its direct perturbation shrinks near the fixed point. Occasionally an observable depends singularly on that coupling as it approaches zero. Then setting it to zero too early gives the wrong scaling form. Such a parameter is called dangerously irrelevant.

The phenomenon appears above the upper critical dimension in scalar models: the quartic interaction flows toward zero at the Gaussian fixed point, yet it is needed to stabilize the ordered phase and influences some thermodynamic scaling. Universality remains, but naive hyperscaling relations can fail because the irrelevant coupling supplies an additional scale.

This exception does not overturn the RG classification. It warns that flow of couplings and dependence of particular observables must both be examined. “Irrelevant” refers to linearized motion in theory space, not permission to delete a coefficient from every question.

## Limit cycles and flow beyond fixed points

Fixed points are the most familiar scale-invariant endpoints, but RG flows can have other structures. A limit cycle returns to the same couplings after a finite change in logarithmic scale and produces discrete rather than continuous scale invariance. Observables can then repeat periodically in $\log E$.

Such behavior is unusual in standard relativistic four-dimensional examples but occurs in some few-body systems. It broadens the interpretation of the word “group”: coarse-graining transformations compose, while their long-distance attractor need not be a single stationary point.

Flows may also run away to strong coupling. A runaway direction can indicate symmetry breaking, confinement, a first-order transition, or merely the breakdown of chosen variables. Perturbative beta functions alone cannot decide among those outcomes once the couplings become large.

## Matching and running as a two-stage calculation

Suppose a heavy particle of mass $M$ contributes to a low-energy process at scale $E\ll M$. Compute amplitudes in the full and effective theories near $\mu=M$ and choose Wilson coefficients so they agree. This matching step contains finite information about the heavy particle.

Then solve effective-theory RG equations from $M$ down to $E$. The running sums logarithms of $M/E$. Evaluating the full theory directly at $mu=E$ would leave large logarithms in fixed-order coefficients; evaluating the low-energy theory at $mu=M$ would leave them in its matrix elements. Matching near each threshold and running between scales keeps every expansion under control.

If several heavy masses are widely separated, remove them sequentially. Each threshold changes beta functions and operator bases. Smooth physical predictions result because matching corrections compensate the change in running at the order calculated.

<div className="see-also">

See also: [Renormalization and Counterterms](/physics/quantum-field-theory/renormalization-and-counterterms) · [Yang--Mills Theory and QCD](/physics/quantum-field-theory/yang-mills-theory-and-qcd) · [Effective Field Theory](/physics/quantum-field-theory/effective-field-theory) · [Collective and Condensed Matter Field Theory](/physics/quantum-field-theory/collective-and-condensed-matter-field-theory)

</div>
