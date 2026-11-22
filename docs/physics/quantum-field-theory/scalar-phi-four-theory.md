---
title: Scalar Phi-Four Theory
sidebar_position: 5
---

# Scalar Phi-Four Theory

Real scalar $\phi^4$ theory is the laboratory model of perturbative quantum field theory. It has a kinetic term, a mass term, and the simplest nontrivial local self-interaction in four spacetime dimensions. Because it avoids spin, gauge redundancy, and group theory, it lets the central machinery stand in the open: propagators, vertices, loops, divergences, counterterms, and running couplings.

The theory is also physically flexible. In relativistic particle physics it models contact scattering and spontaneous symmetry breaking. In condensed matter, its Euclidean version becomes the Landau-Ginzburg theory of critical phenomena. Zee uses this kind of model repeatedly because it is simple enough to calculate with and rich enough to display the logic of QFT.

## The action, propagator, and potential

The Lagrangian density for a real scalar with quartic interaction is

$$
\mathcal{L}=
\frac{1}{2}\partial_\mu\phi\,\partial^\mu\phi
-\frac{1}{2}m^2\phi^2
-\frac{\lambda}{4!}\phi^4.
$$

The free propagator in momentum space is

$$
\tilde{\Delta}_F(p)=\frac{i}{p^2-m^2+i\epsilon}.
$$

The four-point vertex is

$$
-i\lambda.
$$

The classical potential is

$$
V(\phi)=\frac{1}{2}m^2\phi^2+\frac{\lambda}{4!}\phi^4.
$$

For stability at large $\vert \phi\vert $, one wants $\lambda\gt 0$. If $m^2\gt 0$, the minimum is at $\phi=0$. If $m^2\lt 0$, the symmetric point becomes unstable and two nonzero minima appear, making the same model a prototype for spontaneous symmetry breaking.

The $n$-point correlation functions are generated from

$$
Z[J]=
\int\mathcal{D}\phi\,
\exp\left(i\int d^4x\left[
\mathcal{L}+J\phi
\right]\right).
$$

## Power counting and renormalization

The field equation is nonlinear:

$$
(\partial^2+m^2)\phi+\frac{\lambda}{3!}\phi^3=0.
$$

Perturbatively, the first nontrivial correction to the two-point function is the tadpole loop. The first correction to the four-point amplitude is the bubble diagram. These two diagrams already show the two main renormalization targets: the mass and the coupling.

The superficial degree of divergence in four-dimensional $\phi^4$ theory is

$$
D=4-E,
$$

where $E$ is the number of external legs. This follows from $D=4L-2I$ and the graph identities for quartic vertices. The two-point function is quadratically divergent by power counting, the four-point function logarithmically divergent, and higher-point functions superficially convergent. A finite counterterm basis suffices:

$$
\delta\mathcal{L}=
\frac{1}{2}\delta Z\,\partial_\mu\phi\,\partial^\mu\phi
-\frac{1}{2}\delta m^2\phi^2
-\frac{\delta\lambda}{4!}\phi^4.
$$

At tree level the $2\to2$ amplitude is constant, but loops introduce momentum dependence and scale dependence. The theory is therefore a compact testing ground for the idea that measured parameters depend on the scale at which they are measured.

The theory is also useful because the same Lagrangian supports several physical interpretations depending on parameters and signature. With $m^2\gt 0$ and Minkowski time, it describes a massive scalar particle with a short-range contact self-interaction. With $m^2\lt 0$, the classical potential has degenerate minima and becomes the simplest algebraic model of spontaneous symmetry breaking. After Wick rotation to Euclidean signature, the action resembles a statistical free energy for an order parameter, and the parameter $m^2$ plays the role of distance from a critical point.

Renormalization conditions can be stated directly in this model. One may demand that the exact two-point function has a pole at $p^2=m_{\text{phys}}^2$ with residue one, and that the four-point amplitude at a specified symmetric momentum equals $-\lambda_{\text{phys}}$. These requirements determine $\delta m^2$, $\delta Z$, and $\delta\lambda$ order by order. Other schemes choose different finite parts, but all schemes agree on physical observables after parameters are translated.

The model also illustrates why "simple" does not mean "trivial." In four dimensions the coupling is marginal at tree level, so loop effects decide its scale dependence. In dimensions below four, the quartic coupling becomes relevant and drives nontrivial critical behavior. In dimensions above four, it becomes irrelevant in the RG sense, and the free Gaussian fixed point dominates long-distance behavior unless other scales intervene.

The same symbol $\lambda$ may denote a bare coupling, a renormalized coupling at scale $\mu$, or a measured low-energy parameter. The renormalization condition identifies which quantity appears in a calculation and how the alternatives are related.

```mermaid
flowchart TD
  A[Phi-four Lagrangian] --> B[Propagator]
  A --> C[Four-point vertex]
  B --> D[Two-point function]
  C --> E[Tree scattering]
  C --> F[Loops]
  F --> G[Mass renormalization]
  F --> H[Coupling renormalization]
  H --> I[Running lambda]
```

| Quantity | Symbol | Tree-level expression | Loop sensitivity |
|---|---|---|---|
| Propagator | $\tilde{\Delta}_F(p)$ | $i/(p^2-m^2+i\epsilon)$ | mass and field-strength shifts |
| Vertex | four-point | $-i\lambda$ | logarithmic correction in $d=4$ |
| Potential | $V(\phi)$ | $m^2\phi^2/2+\lambda\phi^4/4!$ | effective potential |
| Counterterms | $\delta Z,\delta m^2,\delta\lambda$ | absent in bare tree theory | chosen by renormalization conditions |

## Minima and the fluctuation mass

Consider

$$
V(\phi)=-\frac{1}{2}\mu^2\phi^2+\frac{\lambda}{4!}\phi^4,
\qquad \mu^2>0,\quad \lambda>0.
$$

Differentiating gives

$$
\frac{dV}{d\phi}=-\mu^2\phi+\frac{\lambda}{3!}\phi^3.
$$

The stationary-point equation is

$$
\phi\left(-\mu^2+\frac{\lambda}{6}\phi^2\right)=0.
$$

Its solutions are

$$
\phi=0,
\qquad
\phi^2=\frac{6\mu^2}{\lambda}.
$$

Define

$$
v=\sqrt{\frac{6\mu^2}{\lambda}}.
$$

Their stability follows from the second derivative,

$$
\frac{d^2V}{d\phi^2}=-\mu^2+\frac{\lambda}{2}\phi^2.
$$

At $\phi=0$ this is $-\mu^2$, so the origin is unstable. At $\phi=\pm v$,

$$
\frac{d^2V}{d\phi^2}
=-\mu^2+\frac{\lambda}{2}\frac{6\mu^2}{\lambda}
=2\mu^2.
$$

Writing $\phi=v+\eta$, the small fluctuation has mass squared

$$
m_\eta^2=2\mu^2.
$$

The two minima at $\phi=\pm v$ are degenerate, and the stable excitation around either one has mass $\sqrt{2}\mu$.

## Deriving $D=4-E$

For a connected $\phi^4$ graph in four spacetime dimensions, each loop integral contributes four powers of momentum,

$$
4L.
$$

while each internal scalar propagator behaves as $1/p^2$ at large momentum and contributes

$$
-2I.
$$

Thus

$$
D=4L-2I.
$$

For a connected graph,

$$
L=I-V+1.
$$

Substitute:

$$
D=4(I-V+1)-2I=2I-4V+4.
$$

Counting line ends gives

$$
4V=2I+E.
$$

Therefore

$$
2I=4V-E.
$$

The final substitution yields

$$
D=(4V-E)-4V+4=4-E.
$$

Thus $D=4-E$. A two-point graph has $D=2$, a four-point graph has $D=0$, and a six-point graph has $D=-2$.

## Sign, scheme, and expansion-point checks

- Forgetting the $4!$ in the interaction and then assigning the wrong vertex factor.
- Treating $\lambda\gt 0$ as optional for a stable potential. Without higher stabilizing terms, negative $\lambda$ makes the potential unbounded.
- Confusing the sign of $m^2$ in the Lagrangian with the sign in the potential.
- Assuming every divergent graph requires a new physical parameter. Renormalizability means divergences can be absorbed into existing terms.
- Ignoring disconnected vacuum bubbles when deriving diagrams; they cancel from normalized correlators but matter for vacuum energy discussions.
- Using the same symbol for bare and renormalized quantities without saying which is meant. In loop calculations, $\lambda_0$, $\lambda(\mu)$, and a measured scattering coupling are different until a renormalization condition relates them.
- Forgetting that the same polynomial potential has different physics in different regimes. Positive $m^2$ gives a symmetric massive phase; negative $m^2$ requires expanding around a nonzero vacuum; Euclidean signature turns the model into a critical-phenomena workhorse.
- Treating power counting as the whole calculation. It predicts possible divergence, not the finite part, symmetry factor, threshold structure, or scheme-dependent subtraction.
- Assuming the classical potential alone determines the quantum phase diagram. Loop corrections can shift masses, couplings, and the effective potential.
- Expanding around an unstable point and then interpreting the resulting negative mass squared as a particle mass.

<div className="see-also">

See also: [Perturbation Theory and Feynman Diagrams](/physics/quantum-field-theory/perturbation-and-feynman-diagrams) · [Renormalization and Counterterms](/physics/quantum-field-theory/renormalization-and-counterterms) · [Renormalization Group](/physics/quantum-field-theory/renormalization-group) · [Symmetry Breaking, Goldstone Bosons, and Higgs Physics](/physics/quantum-field-theory/symmetry-breaking-goldstone-higgs)

</div>
