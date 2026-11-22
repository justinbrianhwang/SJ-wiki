---
title: Gas Mixtures
sidebar_position: 13
---

# Gas Mixtures

Air, combustion products, natural gas, and exhaust are mixtures, so their thermodynamic state requires composition as well as temperature and pressure. The main bookkeeping difficulty is that composition is reported on either a mole or mass basis. Partial pressure and reaction stoichiometry use mole fractions naturally; energy balances with mass flow rates often use mass fractions. Silent conversion between the two is the source of many otherwise mysterious errors.

The simplest model is an ideal-gas mixture. Each constituent behaves as an ideal gas at the mixture temperature while occupying the entire mixture volume. Intermolecular interactions are neglected, including interactions between unlike species. Under that model, component energies depend only on temperature, partial pressures follow directly from mole fractions, and the entropy contains a composition term.

## One composition, two bases

For component $i$, define the mole fraction $y_i$ and mass fraction $w_i$ by

$$
y_i=\frac{N_i}{N},
\qquad
w_i=\frac{m_i}{m}.
$$

Both sets sum to one. Since $m_i=N_iM_i$, where $M_i$ is molar mass, the mixture molar mass is

$$
M_m=\frac{m}{N}=\sum_i y_iM_i.
$$

The conversion formulas follow immediately:

$$
w_i=\frac{y_iM_i}{M_m},
\qquad
y_i=\frac{w_i/M_i}{\sum_j w_j/M_j}.
$$

A quick way to avoid basis mistakes is to choose a concrete amount. For mole percentages, take $1\ \mathrm{kmol}$ or $100\ \mathrm{kmol}$ of mixture. For mass percentages, take $1\ \mathrm{kg}$ or $100\ \mathrm{kg}$. Convert every constituent amount before calculating the fractions on the other basis.

The specific gas constant of the mixture is

$$
R_m=\frac{R_u}{M_m}.
$$

It can also be obtained from mass fractions:

$$
R_m=\sum_i w_iR_i,
$$

because $R_i=R_u/M_i$. A light component contributes many moles per unit mass, so its mole fraction can be much larger than its mass fraction.

| Quantity | Natural basis | Mixture expression |
|---|---|---|
| Partial pressure | mole | $P_i=y_iP$ |
| Reaction coefficients | mole | use $N_i$ or $y_i$ |
| Mixture molar mass | mole | $M_m=\sum y_iM_i$ |
| Specific enthalpy | mass | $h_m=\sum w_i h_i$ |
| Molar enthalpy | mole | $\bar h_m=\sum y_i\bar h_i$ |
| Species mass flow | mass | $\dot m_i=w_i\dot m$ |

## Dalton and Amagat from the ideal-gas equation

For constituent $i$ in an ideal mixture, imagine it alone at the mixture temperature $T$ in the full volume $V$. Its partial pressure is

$$
P_iV=N_iR_uT.
$$

Adding this relation over all constituents gives

$$
\left(\sum_iP_i\right)V
=\left(\sum_iN_i\right)R_uT
=NR_uT=PV.
$$

Therefore

$$
P=\sum_iP_i,
\qquad
P_i=\frac{N_i}{N}P=y_iP.
$$

This is Dalton's law of additive pressures. A partial pressure is not a separate local pressure measured in one corner of a well-mixed vessel. All constituents share the same physical space and mixture pressure; $P_i$ is the pressure that species would exert alone at $T$ and $V$.

Amagat's law uses a different thought experiment. Let $V_i$ be the volume that component $i$ would occupy alone at the mixture $T$ and $P$:

$$
PV_i=N_iR_uT.
$$

Adding gives $V=\sum_iV_i$ and hence

$$
V_i=y_iV.
$$

For ideal gases, pressure fraction, partial-volume fraction, and mole fraction are numerically equal. Partial pressures and partial volumes are alternative constructions; one should not assign both the full mixture volume and the partial volume to a constituent in the same equation.

### Worked example: oxygen and nitrogen

A vessel contains $1\ \mathrm{kmol}$ of oxygen and $3\ \mathrm{kmol}$ of nitrogen at $400\ \mathrm{kPa}$ and $300\ \mathrm{K}$. Use $M_{O_2}=32\ \mathrm{kg/kmol}$, $M_{N_2}=28\ \mathrm{kg/kmol}$, and $R_u=8.314\ \mathrm{kJ/(kmol\,K)}$.

The total amount and mole fractions are

$$
N=1+3=4\ \mathrm{kmol},
$$

$$
y_{O_2}=\frac14=0.25,
\qquad
y_{N_2}=\frac34=0.75.
$$

Dalton's law gives

$$
P_{O_2}=0.25(400)=100\ \mathrm{kPa},
$$

$$
P_{N_2}=0.75(400)=300\ \mathrm{kPa}.
$$

The mixture molar mass is

$$
M_m=0.25(32)+0.75(28)=29\ \mathrm{kg/kmol},
$$

and the mixture gas constant is

$$
R_m=\frac{8.314}{29}
=0.2867\ \mathrm{kJ/(kg\,K)}.
$$

On the original $4\ \mathrm{kmol}$ basis, the mass is $1(32)+3(28)=116\ \mathrm{kg}$, which also gives $M_m=116/4=29\ \mathrm{kg/kmol}$. The mass fractions are

$$
w_{O_2}=\frac{32}{116}=0.2759,
\qquad
w_{N_2}=\frac{84}{116}=0.7241.
$$

Their difference from the mole fractions is small because the two molar masses are close, but they are not interchangeable.

## Energy and heat capacities of an ideal mixture

The Gibbs–Dalton model treats each constituent as if it were alone at the mixture temperature and its partial pressure. Ideal-gas internal energy and enthalpy depend only on temperature, so the total extensive properties add:

$$
U=\sum_iN_i\bar u_i(T)=\sum_i m_i u_i(T),
$$

$$
H=\sum_iN_i\bar h_i(T)=\sum_i m_i h_i(T).
$$

On a mass basis,

$$
u_m=\sum_iw_i u_i(T),
\qquad
h_m=\sum_iw_i h_i(T).
$$

Differentiating at fixed composition gives

$$
c_{v,m}=\sum_iw_i c_{v,i},
\qquad
c_{p,m}=\sum_iw_i c_{p,i}.
$$

Likewise, on a molar basis, $\bar c_{p,m}=\sum_i y_i\bar c_{p,i}$. Mixing a molar-weighted heat capacity into a mass-basis energy equation introduces a factor-of-molar-mass error. Units reveal the mismatch: $\mathrm{kJ/(kmol\,K)}$ cannot multiply kilograms.

If two adiabatic ideal-gas streams of fixed composition mix at negligible kinetic energy and do no shaft work, steady energy conservation gives

$$
\sum_{\mathrm{in}}\dot m_i h_i(T_i)
=\dot m_{\mathrm{out}}h_m(T_{\mathrm{out}}).
$$

With constant heat capacities, the outlet temperature becomes a heat-capacity-rate weighted average, not generally a simple arithmetic or mass-weighted mean.

### Worked example: mixing two gas streams

A steady insulated chamber mixes $1\ \mathrm{kg/s}$ of nitrogen at $500\ \mathrm{K}$ with $2\ \mathrm{kg/s}$ of oxygen at $300\ \mathrm{K}$. Both enter at the outlet pressure. Take $c_{p,N_2}=1.04\ \mathrm{kJ/(kg\,K)}$ and $c_{p,O_2}=0.918\ \mathrm{kJ/(kg\,K)}$, constant over the range.

Choose a common enthalpy datum. The steady energy balance becomes

$$
1(1.04)(500)+2(0.918)(300)
=\left[1(1.04)+2(0.918)\right]T_3.
$$

The numerator is

$$
520+550.8=1070.8\ \mathrm{kW},
$$

and the total heat-capacity rate is

$$
1.04+1.836=2.876\ \mathrm{kW/K}.
$$

Thus

$$
T_3=\frac{1070.8}{2.876}=372.3\ \mathrm{K}.
$$

The outlet mass fractions follow from species balances: $w_{N_2}=1/3$ and $w_{O_2}=2/3$. Partial pressures require mole fractions, so one more conversion is needed before applying Dalton's law.

## Species balances when composition changes

A total mass balance cannot determine outlet composition. Each nonreacting constituent has its own conservation equation:

$$
\frac{dm_i}{dt}
=\sum_{\mathrm{in}}\dot m_i
-\sum_{\mathrm{out}}\dot m_i.
$$

With $\dot m_i=w_i\dot m$, a well-mixed steady vessel having one outlet satisfies

$$
w_{i,\mathrm{out}}
=\frac{\sum_{\mathrm{in}}w_{i,k}\dot m_k}
{\sum_{\mathrm{in}}\dot m_k}.
$$

This mass-weighted result applies to composition, even though the outlet temperature may require heat-capacity weighting. If reaction occurs, a generation term appears in each species balance while total mass remains conserved. It is usually cleaner to switch to molar reaction extents because stoichiometric coefficients count molecules.

Separation processes reverse the mixing operation only with work or some other resource. A membrane, distillation column, adsorption bed, or centrifuge can produce streams richer in selected species, but an isolated mixture does not spontaneously unmix. For ideal gases at fixed temperature and pressure, the minimum reversible work of separating a mixture into pure components is tied to the negative of the mixing Gibbs-energy change. The positive entropy of mixing accounts for why energy input is required even when ideal-gas enthalpy is unchanged.

Sampling can introduce a less obvious basis issue. A gas analyzer often reports dry mole fractions after water has been removed. The fractions then sum to one over the dry constituents, not over the original wet mixture. If water has mole fraction $y_w$, a reported dry fraction $y_{i,d}$ converts to the wet basis by

$$
y_i=(1-y_w)y_{i,d}.
$$

Combustion calculations distinguish wet and dry product analyses for exactly this reason. Using dry oxygen percentage directly with a wet total pressure overstates its partial pressure.

## Entropy of a mixture and entropy of mixing

For an ideal mixture, each constituent entropy is evaluated at its partial pressure:

$$
s_m=\sum_iw_i s_i(T,P_i).
$$

On a molar basis, using a common standard pressure $P^\circ$,

$$
\bar s_m
=\sum_i y_i\left[\bar s_i^\circ(T)
-R_u\ln\left(\frac{y_iP}{P^\circ}\right)\right].
$$

The logarithm separates into a pressure part and a composition part. If distinct ideal gases initially at the same $T$ and $P$ are separated, then the partition is removed while total $T$ and $P$ remain unchanged. Each species effectively expands from its initial volume to the full mixture volume. The entropy increase is

$$
\Delta S_{\mathrm{mix}}
=-NR_u\sum_i y_i\ln y_i.
$$

Since $0\lt y_i\lt 1$, every $\ln y_i$ is negative and the result is positive. For one mole each of two distinct gases, $y_1=y_2=1/2$ and $N=2\ \mathrm{mol}$, so

$$
\Delta S_{\mathrm{mix}}
=-2R_u\left[\frac12\ln\frac12+\frac12\ln\frac12\right]
=2R_u\ln2.
$$

If the two sides contain the same gas at the same state, removing the partition causes no thermodynamic change and no entropy of mixing. Treating artificially labeled portions of an identical gas as different species would predict a false entropy increase. This discontinuity in the classical counting argument is the Gibbs paradox; statistical mechanics resolves it through the indistinguishability of identical particles.

The mixing formula can also be derived directly from reversible isothermal expansions. Before removing the partitions, species $i$ occupies $V_i=y_iV$ at the common pressure $P$. Afterward it occupies $V$. Its entropy change is

$$
\Delta S_i=N_iR_u\ln\left(\frac{V}{V_i}\right)
=-N_iR_u\ln y_i.
$$

Summing over species gives the stated result. No heat or work need cross the outer boundary during actual free mixing, so the entropy rise is generated internally. The reversible expansion construction calculates the same state-function change along a different path.

Ideal-gas enthalpy has no corresponding mixing term because $h_i$ depends only on temperature. At a fixed temperature,

$$
\Delta H_{\mathrm{mix}}=0
$$

for an ideal mixture, even though $\Delta S_{\mathrm{mix}}\gt 0$. Hence the Gibbs free-energy change at constant $T$ and $P$ is

$$
\Delta G_{\mathrm{mix}}
=\Delta H_{\mathrm{mix}}-T\Delta S_{\mathrm{mix}}
=NR_uT\sum_i y_i\ln y_i<0.
$$

The negative value is the thermodynamic driving force for spontaneous mixing. Real mixtures may release or absorb heat upon mixing because unlike-molecule interactions differ from like-molecule interactions. Their enthalpy of mixing need not vanish.

Composition may remain constant during compression or heating, but entropy still changes through temperature and total pressure. For fixed ideal-mixture composition with constant mixture heat capacity,

$$
s_2-s_1
=c_{p,m}\ln\left(\frac{T_2}{T_1}\right)
-R_m\ln\left(\frac{P_2}{P_1}\right).
$$

The composition-dependent terms cancel only because the mole fractions are the same at both states.

For a process that changes composition, that shortcut is unsafe. One must evaluate each species entropy at its own initial and final partial pressure or retain the explicit $-R_u\sum y_i\ln y_i$ contribution. The entropy of a mixture cannot be reconstructed from only $T$, $P$, and an average gas constant when the composition changes.

## Effective mixture properties and their limits

At fixed composition an ideal mixture can often be treated as a single pseudogas with $R_m$, $c_{p,m}$, and $c_{v,m}$. The identity

$$
c_{p,m}-c_{v,m}=R_m
$$

still holds, and one may define

$$
k_m=\frac{c_{p,m}}{c_{v,m}}.
$$

Constant-$k_m$ isentropic relations then have the same form as for a pure ideal gas. This reduction is useful for compression, expansion, and nozzle estimates when no species is added, removed, condensed, or reacted. It ceases to describe a combustor, a humid stream crossing its dew point, or a separator because the mixture properties evolve with composition.

Even at fixed composition, heat capacities vary with temperature. Combustion products over a wide temperature range should use species heat-capacity functions before forming mixture enthalpy. Averaging constant room-temperature values can distort flame temperatures and turbine work. The correct order is to evaluate each constituent property over the relevant temperature interval and then weight it on a consistent mole or mass basis.

The pseudogas model also gives a useful density check:

$$
\rho=\frac{P}{R_mT}=\frac{PM_m}{R_uT}.
$$

At fixed temperature and pressure, a mixture with larger molar mass is denser. This relation can expose a composition conversion error: using mass fractions as though they were mole fractions produces the wrong $M_m$ and therefore the wrong density. It also explains why gas volume percentage is identified with mole percentage only under a common temperature and pressure and an ideal-gas assumption.

Composition measurements need their reported conditions attached. A volumetric flow meter gives actual volume per time at the line state, whereas a standard volumetric flow rate refers to a specified reference temperature and pressure. The same molar flow occupies different actual volumes as pressure and temperature change. Converting a standard volume fraction to mole fraction is harmless for an ideal mixture because both constituents share the same reference state; converting the total standard volumetric flow to mass flow still requires the reference density and mixture molar mass.

Trace concentrations are often reported in parts per million by volume. For an ideal gas mixture, ppm by volume equals ppm by mole, so $500\ \mathrm{ppmv}$ corresponds to $y_i=500\times10^{-6}$. It is not generally $500\ \mathrm{ppm}$ by mass. The mass fraction must still be calculated from $w_i=y_iM_i/M_m$, a significant correction when the trace species is much heavier or lighter than the carrier gas.

## Converting a mass analysis to a mole analysis

A fuel-gas sample is $60\%$ methane and $40\%$ carbon dioxide by mass. Use $M_{CH_4}=16\ \mathrm{kg/kmol}$ and $M_{CO_2}=44\ \mathrm{kg/kmol}$.

Take a $1\ \mathrm{kg}$ basis:

$$
m_{CH_4}=0.60\ \mathrm{kg},
\qquad
m_{CO_2}=0.40\ \mathrm{kg}.
$$

Convert each mass separately:

$$
N_{CH_4}=\frac{0.60}{16}=0.03750\ \mathrm{kmol},
$$

$$
N_{CO_2}=\frac{0.40}{44}=0.009091\ \mathrm{kmol}.
$$

The total is $N=0.046591\ \mathrm{kmol}$. Therefore

$$
y_{CH_4}=\frac{0.03750}{0.046591}=0.8050,
$$

$$
y_{CO_2}=\frac{0.009091}{0.046591}=0.1950.
$$

The fractions sum to one. An independent check is the mixture molar mass:

$$
M_m=\frac{1\ \mathrm{kg}}{0.046591\ \mathrm{kmol}}
=21.46\ \mathrm{kg/kmol}.
$$

The same value follows from $0.8050(16)+0.1950(44)$. Methane dominates the mole count because a kilogram of methane contains many more molecules than a kilogram of carbon dioxide.

## When the ideal-mixture model becomes weak

Dalton's and Amagat's laws are exact within the ideal-gas model and often good at low density. At high pressure, near condensation, or near a component's critical region, intermolecular effects matter. Partial pressure then remains useful for some definitions, but it no longer captures chemical potential or phase equilibrium accurately. Fugacity replaces pressure in rigorous equilibrium calculations, and an equation of state with mixing rules supplies departure properties.

Kay's pseudocritical rule forms

$$
T_{c,m}=\sum_i y_iT_{c,i},
\qquad
P_{c,m}=\sum_i y_iP_{c,i},
$$

then treats the mixture through corresponding states. It is a rough engineering estimate, not a true critical point calculation and not reliable for every strongly nonideal or polar mixture. A compressibility-factor approximation may be adequate for density while still being too crude for phase equilibrium.

Useful consistency checks are simple: all fractions lie between zero and one, each set of fractions sums to one, ideal-gas partial pressures sum to $P$, and $M_m$ lies between the smallest and largest constituent molar masses. Every reported specific property should state whether it is per kilogram or per kilomole.

<div className="see-also">

See also: [gas-vapor mixtures and air conditioning](/physics/thermodynamics/gas-vapor-mixtures-and-air-conditioning) · [chemical reactions and combustion](/physics/thermodynamics/chemical-reactions-and-combustion) · [thermodynamic property relations](/physics/thermodynamics/thermodynamic-property-relations) · [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance) · [compressible flow](/physics/thermodynamics/compressible-flow)

</div>
