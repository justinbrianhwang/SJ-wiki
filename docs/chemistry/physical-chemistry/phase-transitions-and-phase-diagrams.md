---
title: Phase Transitions and Phase Diagrams
sidebar_position: 6
---

# Phase Transitions and Phase Diagrams

Phase diagrams compress a large amount of thermodynamic information into a visual map. They show which phases are stable at given temperature, pressure, and composition, and they mark the conditions under which phases coexist.

Pure-substance and mixture diagrams look different, but both come from the same condition: coexisting phases have equal chemical potentials. Vaporization, fusion, azeotropes, eutectics, and materials purification are variations on that condition. A boundary is the set of states at which neither phase has a molar-Gibbs-energy advantage.

## What a phase diagram counts

A **phase** is a form of matter uniform in chemical composition and physical state. A **component** is the minimum number of independent species needed to describe the composition of all phases. A **constituent** is an actual chemical species present.

For a one-component system at phase equilibrium between phases $\alpha$ and $\beta$,

$$
\mu^\alpha(T,p)=\mu^\beta(T,p)
$$

The **phase rule** is

$$
F=C-P+2
$$

where $F$ is the variance or number of independent intensive variables, $C$ is the number of components, and $P$ is the number of phases. At fixed pressure for condensed binary diagrams, the reduced rule is

$$
F=C-P+1
$$

The **Clapeyron equation** gives the slope of a phase boundary:

$$
\frac{dp}{dT}
=\frac{\Delta_{\mathrm{trs}}S}{\Delta_{\mathrm{trs}}V}
=\frac{\Delta_{\mathrm{trs}}H}{T\Delta_{\mathrm{trs}}V}
$$

For vaporization or sublimation, if the vapor is a perfect gas and condensed-phase volume is neglected, the Clausius-Clapeyron equation is

$$
\frac{d\ln p}{dT}
=\frac{\Delta_{\mathrm{vap}}H}{RT^2}
$$

If $\Delta_{\mathrm{vap}}H$ is constant,

$$
\ln\frac{p_2}{p_1}
=-\frac{\Delta_{\mathrm{vap}}H}{R}
\left(\frac{1}{T_2}-\frac{1}{T_1}\right)
$$

For binary liquid-vapor diagrams, a **tie line** at fixed temperature or pressure connects coexisting phase compositions. The **lever rule** gives phase amounts:

$$
\frac{n_\alpha}{n_\beta}
=\frac{\mathrm{distance\ from\ overall\ composition\ to\ }\beta}
{\mathrm{distance\ from\ overall\ composition\ to\ }\alpha}
$$

## Pure substances: regions, boundaries, and special points

For a pure substance, phase boundaries meet at the triple point, where solid, liquid, and vapor coexist. Since $C=1$ and $P=3$,

$$
F=1-3+2=0
$$

so the triple point has no freedom: both $T$ and $p$ are fixed. Along a two-phase boundary,

$$
F=1-2+2=1
$$

so choosing $T$ fixes $p$, or choosing $p$ fixes $T$.

The critical point terminates the liquid-vapor boundary. Above the critical temperature, there is no sharp liquid-vapor phase transition; a supercritical fluid can have liquid-like density and gas-like transport.

Liquid and vapor differ in density and composition fluctuations below the critical point. On approaching the critical point, their densities converge, the enthalpy of vaporization tends toward zero, and density fluctuations grow over long length scales. The meniscus disappears because there are no longer two bulk phases separated by a surface. By contrast, the solid-liquid line does not ordinarily terminate at a critical point: a crystal and a liquid differ in symmetry, so they cannot generally be connected continuously without a phase transition.

The sign of the solid-liquid slope follows from the Clapeyron equation. Most substances have $\Delta_{\mathrm{fus}}V\gt 0$, so the melting point rises with pressure. Water is unusual because ice is less dense than liquid water, so $\Delta_{\mathrm{fus}}V\lt 0$ and the melting line has negative slope.

In binary liquid-vapor diagrams, fractional distillation works because vapor and liquid compositions differ. Azeotropes are exceptions where vapor and liquid have the same composition at a boiling extremum, so simple distillation cannot pass that composition.

In binary liquid-solid diagrams, eutectics are compositions that melt or freeze at a minimum temperature. At the eutectic temperature in a simple binary eutectic,

$$
C=2,\quad P=3,\quad F=2-3+1=0
$$

at fixed pressure, so solid $A$, solid $B$, and liquid coexist invariantly.

A phase is stable when its chemical potential is lower than alternatives at the same $T$ and $p$. A boundary occurs when two phases have equal chemical potential. If the system crosses the boundary, the lower-$\mu$ phase changes, and a phase transformation becomes thermodynamically favorable. Every line is therefore a balance of molar Gibbs energies rather than an empirical curve to memorize.

The Clapeyron equation follows by differentiating the equality $\mu^\alpha=\mu^\beta$ along a coexistence curve. For each phase,

$$
d\mu=V_m\,dp-S_m\,dT
$$

so equality of changes gives

$$
(V_m^\beta-V_m^\alpha)dp=(S_m^\beta-S_m^\alpha)dT
$$

and therefore

$$
\frac{dp}{dT}=\frac{\Delta S}{\Delta V}
$$

Phase-boundary slopes are therefore ratios of entropy and volume changes. The equation also explains why a nearly vertical melting line means that fusion changes volume only slightly.

The Clausius-Clapeyron approximation works best for vaporization and sublimation because gas volume dominates condensed-phase volume. If the vapor behaves ideally, $\Delta V\approx RT/p$, and substitution into Clapeyron gives the logarithmic vapor-pressure relation. Plotting $\ln p$ against $1/T$ often gives an approximately straight line whose slope yields $\Delta_{\mathrm{vap}}H/R$ with a sign convention. Curvature appears when the enthalpy of vaporization changes appreciably with temperature or the vapor is not ideal.

The phase rule is a counting rule with chemical content. In a one-component two-phase system, only one intensive variable is free. The boiling point of a pure liquid is consequently fixed once the external pressure is fixed. At the triple point of a pure substance, no intensive freedom remains. In a binary mixture at fixed pressure, a two-phase region has one freedom: if temperature is fixed, the compositions of the two phases are fixed by the ends of the tie line, and the overall composition determines only the relative amounts.

Binary liquid-vapor diagrams explain distillation. If vapor is richer in the more volatile component than the liquid, repeated vaporization and condensation enrich the distillate. An azeotrope breaks this strategy because liquid and vapor compositions become equal at the azeotropic point. The mixture then boils like a pure substance at that composition even though it contains two components. The thermodynamic cause is nonideal solution behavior strong enough to create an extremum in boiling temperature or vapor pressure.

Liquid-solid diagrams are central in materials chemistry. Eutectics melt at a lower temperature than either pure component and solidify into two-phase microstructures. Peritectics and incongruent melting show that compounds in a binary system may be stable as solids but not as liquids of the same composition. Such diagrams guide alloy preparation, solder selection, ceramic processing, and semiconductor purification.

## Why a binary two-phase field has width

For a pure substance at fixed pressure, liquid and vapor coexist at one boiling temperature. A binary mixture has two chemical-potential equalities: each component must have the same chemical potential in both phases. At a chosen pressure and temperature, these conditions determine a liquid composition and a vapor composition, which are generally different. Any overall composition between them can be assembled by changing only the relative phase amounts. The diagram therefore shows a two-phase region rather than a single coexistence line.

The bubble-point boundary is reached when the first infinitesimal vapor appears from a liquid mixture. Its composition lies at the other end of a tie line. The dew-point boundary is reached when the first infinitesimal liquid appears from vapor. Between the boundaries, neither the plotted overall composition nor either boundary alone describes the whole sample; both endpoint compositions and a phase fraction are needed.

Raoult's law gives the ideal-solution starting point. Each component's partial vapor pressure is its liquid mole fraction times its pure-component vapor pressure. The vapor is enriched in the component with the larger pure vapor pressure, which supplies the separation exploited by distillation. Positive or negative departures from Raoult's law bend the boundaries. Strong enough departures can produce a vapor-pressure extremum and an azeotrope.

At an azeotrope, liquid and vapor compositions coincide. Boiling then removes material with the same composition as the residue, so repeated equilibrium stages cannot cross that point by ordinary distillation at fixed pressure. Changing pressure may move the azeotropic composition, and other separation methods can exploit a third component, adsorption, membranes, or chemical reaction, but those are changes to the process rather than exceptions to the equilibrium diagram.

Zone refining and zone leveling use phase diagrams under non-equilibrium operating conditions. If impurities are more soluble in the melt than in the solid, a moving molten zone can sweep impurities toward one end of a solid rod. The equilibrium diagram explains the direction of partitioning, while the practical purification depends on repeated passes and controlled solidification. This is a good example of equilibrium thermodynamics informing a process that is deliberately run dynamically.

Liquid crystals broaden the meaning of phase. A mesophase can have orientational order without full positional order, so it lies between an isotropic liquid and an ordinary crystal. Its phase behavior depends on temperature, composition, and molecular shape. The phase rule still applies even when the structural distinction is subtler than solid versus liquid.

## One counting rule, several kinds of diagram

```mermaid
flowchart TB
  Start["Thermodynamic state<br/>choose component count C, phases P, variables T and p"] --> Rule["Gibbs phase rule<br/>F = C - P + 2"]

  subgraph Pure["Pure substance p-T map"]
    direction TB
    Pure1["Single phase region<br/>solid, liquid, or vapor; P = 1, F = 2"] --> Boundary["Two-phase boundary<br/>mu_alpha = mu_beta; P = 2, F = 1"]
    Boundary --> Triple["Triple point<br/>solid + liquid + vapor; P = 3, F = 0"]
    Boundary --> Critical["Critical point<br/>liquid-vapor distinction ends"]
    Boundary --> Slope["Clapeyron slope<br/>dp/dT = Delta S / Delta V"]
    Slope --> CC["Clausius-Clapeyron approximation<br/>ln p vs 1/T for vaporization"]
  end

  subgraph Binary["Binary mixture at fixed pressure"]
    direction TB
    Bin1["One-phase field<br/>liquid or solid solution; F = 2"] --> Bin2["Two-phase region<br/>tie line fixes phase compositions; F = 1"]
    Bin2 --> Lever["Lever rule<br/>phase amounts from overall composition"]
    Bin2 --> Eutectic["Three-phase invariant<br/>solid A + solid B + liquid; F = 0"]
    Bin1 --> Azeo["Liquid-vapor extremum<br/>azeotrope when x_liquid = x_vapor"]
  end

  Rule --> Pure1
  Rule --> Bin1
  Slope -. "uses dmu = Vm dp - Sm dT" .-> Boundary
  Lever -. "mass balance constraint" .-> Bin2
```

The labeled freedoms explain why a two-phase coexistence state is a line for a pure substance in the $p$-$T$ plane but a region for a binary mixture plotted against temperature and overall composition. In the mixture, the tie-line endpoints specify two equilibrium compositions while the overall composition can vary between them by changing phase amounts.

| Feature | Pure substance | Binary mixture |
|---|---|---|
| Phase boundary | Line in $p$-$T$ plane | Region in $T$-$x$ or $p$-$x$ plane |
| Coexistence condition | equal $\mu$ of same substance | equal component chemical potentials across phases |
| Invariant point | triple point | eutectic, peritectic, three-phase point |
| Distillation relevance | boiling point | vapor and liquid compositions differ |
| Materials relevance | melting/freezing | alloy microstructure, zone refining, liquid crystals |

## Worked example: vapor pressure from Clausius-Clapeyron

Suppose a liquid has vapor pressure $100.0\ \mathrm{kPa}$ at $350.0\ \mathrm{K}$ and $\Delta_{\mathrm{vap}}H=35.0\ \mathrm{kJ\ mol^{-1}}$. Estimate its vapor pressure at $330.0\ \mathrm{K}$.

1. Write the relation:

$$
\ln\frac{p_2}{p_1}
=-\frac{\Delta_{\mathrm{vap}}H}{R}
\left(\frac{1}{T_2}-\frac{1}{T_1}\right)
$$

2. Substitute:

$$
\frac{1}{330.0}-\frac{1}{350.0}
=0.0030303-0.0028571
=1.7316\times 10^{-4}\ \mathrm{K^{-1}}
$$

3. Enthalpy factor:

$$
\frac{\Delta_{\mathrm{vap}}H}{R}
=\frac{35000}{8.314}
=4210\ \mathrm{K}
$$

4. Log pressure ratio:

$$
\ln\frac{p_2}{p_1}
=-(4210)(1.7316\times 10^{-4})
=-0.729
$$

5. Pressure:

$$
p_2=100.0e^{-0.729}
=48.2\ \mathrm{kPa}
$$

Lower temperature must give lower vapor pressure, and the estimate $48\ \mathrm{kPa}$ has that sign. The numerical value assumes a constant vaporization enthalpy and ideal vapor.

## Worked example: deriving and applying the lever rule

At a certain temperature, a binary liquid-vapor system has liquid composition $x_B^{(l)}=0.20$ and vapor composition $x_B^{(v)}=0.70$. A sample has overall composition $z_B=0.40$. Find the fraction of the total amount in the vapor phase.

$$
z_B=f_vx_B^{(v)}+(1-f_v)x_B^{(l)}
$$

1. Substitute:

$$
0.40=f_v(0.70)+(1-f_v)(0.20)
$$

2. Expand:

$$
0.40=0.70f_v+0.20-0.20f_v
$$

3. Collect:

$$
0.20=0.50f_v
$$

4. Solve:

$$
f_v=0.40
$$

The other fraction is $f_l=1-f_v=0.60$. Subtracting $x_B^{(l)}$ from the material balance gives the general result

$$
f_v=\frac{z_B-x_B^{(l)}}{x_B^{(v)}-x_B^{(l)}},
\qquad
f_l=\frac{x_B^{(v)}-z_B}{x_B^{(v)}-x_B^{(l)}}.
$$

Each phase amount is proportional to the tie-line segment on the opposite side. Here the overall composition is closer to the liquid endpoint, so liquid must be the larger fraction; $60\%$ liquid and $40\%$ vapor pass that check.

## Metastability and how to read the map

An equilibrium boundary says where two phases have equal chemical potential; it does not guarantee immediate conversion on crossing the line. A new phase usually needs a nucleus with enough volume benefit to compensate for the cost of creating an interface. A liquid may therefore supercool below its freezing point, and a vapor may remain supersaturated. Such states are metastable: a lower-$\mu$ state exists, but the activation barrier delays its appearance. The reported transition on heating can consequently differ from the transition on cooling.

- Using the phase rule without checking whether pressure is fixed. Condensed phase diagrams often use the reduced form.
- Reading a two-phase composition from the overall composition. Phase compositions come from tie-line endpoints; the overall composition gives amounts through the lever rule.
- Applying Clausius-Clapeyron over too wide a temperature range while treating $\Delta H$ as constant.
- Confusing a eutectic with an azeotrope. A eutectic is liquid-solid behavior; an azeotrope is liquid-vapor behavior.
- Ignoring metastability. Supercooling and supersaturation can delay phase change but do not redefine equilibrium boundaries.

When reading a phase diagram, first identify the axes and what is held fixed. A $p$-$T$ diagram for a pure substance, a $T$-$x$ diagram at fixed pressure, and a $p$-$x$ diagram at fixed temperature answer different questions. Then identify the region, not just the nearest curve. A point in a two-phase region represents an overall composition and temperature; the actual phase compositions are found at boundary intersections connected by a tie line.

For lever-rule calculations, draw the tie line and label distances before inserting numbers. The amount of a phase is proportional to the distance from the overall composition to the opposite phase boundary. This "opposite side" rule is easy to reverse if done mentally. A quick check is that if the overall composition lies close to the liquid boundary, most of the sample should be liquid.

For phase-boundary slopes, return to Clapeyron rather than memorized signs. The sign depends on both entropy and volume changes. Vaporization has positive $\Delta S$ and large positive $\Delta V$, so vapor pressure rises with temperature. Fusion usually has positive $\Delta S$ and positive $\Delta V$, but water has negative $\Delta V$ for melting ice, giving a negative melting-line slope.

<div className="see-also">

See also: [Properties of gases](/chemistry/physical-chemistry/properties-of-gases) · [Mixtures, solutions, and activities](/chemistry/physical-chemistry/mixtures-solutions-and-activities) · [Molecular interactions and transport](/chemistry/physical-chemistry/molecular-interactions-and-transport) · [states of matter: liquids and solids](/chemistry/general/states-of-matter-liquids-and-solids)

</div>
