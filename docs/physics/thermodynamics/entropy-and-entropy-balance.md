---
title: Entropy and Entropy Balance
sidebar_position: 7
---

# Entropy and Entropy Balance

The first law rules out energy creation, but it does not say which energy-conserving processes can occur. A hot block can warm a cold block; the reverse transfer would also conserve energy, yet it never occurs without some other change. A turbine may satisfy the energy balance while producing less work than its reversible ideal. Entropy supplies the missing direction test and gives a numerical account of the loss.

Energy and entropy obey different bookkeeping rules. Heat and mass can carry either property across a boundary. Energy is conserved; entropy can also be produced inside the boundary by friction, mixing, electrical resistance, chemical reaction, unrestrained expansion, or heat transfer through a finite temperature difference. It cannot be destroyed:

$$
S_{\mathrm{gen}}\ge 0.
$$

The distinction among entropy change, entropy transfer, and entropy generation is the center of every calculation. An entropy increase of a system does not by itself prove irreversibility: a reversibly heated system gains entropy through its boundary. Conversely, a system can have zero entropy change while entropy is generated and exported.

## From the Clausius inequality to a property

For a reversible cycle, the Clausius equality is

$$
\oint \frac{\delta Q_{\mathrm{rev}}}{T}=0.
$$

The integral of an exact differential around a cycle is zero. Therefore there is a state property $S$ whose differential along an internally reversible path is

$$
dS=\frac{\delta Q_{\mathrm{rev}}}{T}.
$$

The subscript matters. Entropy is a property at every equilibrium state, but $\delta Q/T$ equals $dS$ only for an internally reversible path. For an irreversible process between the same end states, entropy change is still found by choosing any convenient reversible path between those states. It is not found by integrating the actual irreversible heat transfer divided by an ill-defined system temperature.

For any cycle, Clausius' inequality gives

$$
\oint \frac{\delta Q}{T_b}\le 0,
$$

where $T_b$ is the absolute temperature at the part of the boundary crossed by heat. Combining the actual process from state 1 to state 2 with a reversible return path produces

$$
S_2-S_1\ge \int_1^2 \frac{\delta Q}{T_b}.
$$

The difference is defined as entropy generation:

$$
\Delta S=\int_1^2\frac{\delta Q}{T_b}+S_{\mathrm{gen}}.
$$

Equality corresponds to an internally reversible process. The inequality is a direction test: a proposed process yielding negative $S_{\mathrm{gen}}$ cannot occur as stated. A positive result says the second law permits it, not that the process must occur.

## Entropy relations for substances

Combining the first law for a reversible differential process, $\delta Q_{\mathrm{rev}}-\delta W_{\mathrm{rev}}=dU$, with $\delta W_{\mathrm{rev}}=P\,dV$ gives

$$
T\,dS=dU+P\,dV.
$$

Per unit mass,

$$
T\,ds=du+P\,dv.
$$

Using $h=u+Pv$ and $dh=du+P\,dv+v\,dP$ gives the second $Tds$ relation,

$$
T\,ds=dh-v\,dP.
$$

These identities relate equilibrium properties and remain valid between neighboring equilibrium states even when the actual process is irreversible. The reversible path was needed in the derivation, not as a restriction on the resulting property relation.

For an ideal gas, $du=c_v\,dT$, $dh=c_p\,dT$, and $Pv=RT$. Substitution and integration give, for constant specific heats,

$$
s_2-s_1=c_v\ln\left(\frac{T_2}{T_1}\right)
+R\ln\left(\frac{v_2}{v_1}\right),
$$

or equivalently,

$$
s_2-s_1=c_p\ln\left(\frac{T_2}{T_1}\right)
-R\ln\left(\frac{P_2}{P_1}\right).
$$

When heat capacities vary appreciably with temperature, the more accurate form is

$$
s_2-s_1=\int_{T_1}^{T_2}\frac{c_p(T)}{T}\,dT
-R\ln\left(\frac{P_2}{P_1}\right).
$$

Ideal-gas tables package the temperature integral into a standard-state entropy $s^\circ(T)$. Relative-pressure and relative-volume tables provide another convenient route for isentropic calculations. The familiar constant-$k$ formulas are approximations obtained by setting $ds=0$ and treating $c_p$, $c_v$, and $k=c_p/c_v$ as constants:

$$
\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{(k-1)/k},
\qquad
\frac{P_2}{P_1}=\left(\frac{v_1}{v_2}\right)^k.
$$

For an incompressible substance, $dv\approx0$ and $du\approx c\,dT$, so

$$
s_2-s_1\approx c\ln\left(\frac{T_2}{T_1}\right).
$$

Across a phase change at saturation, a reversible constant-temperature path gives $s_{fg}=h_{fg}/T_{\mathrm{sat}}$. In the two-phase region, specific entropy follows the same quality construction used for other specific properties:

$$
s=s_f+x s_{fg}.
$$

## The balance for a closed system

If heat crosses at several boundary locations, each contribution uses its own boundary temperature:

$$
\Delta S_{\mathrm{system}}
=\sum_k\int\frac{\delta Q_k}{T_{b,k}}+S_{\mathrm{gen}}.
$$

For a constant boundary temperature during each heat interaction, this reduces to $\sum_k Q_k/T_{b,k}$. Heat into the system is positive under the usual convention. Work carries no entropy. Frictional work can create entropy inside a system, but there is no term of the form $W/T$ crossing its boundary.

An adiabatic closed system satisfies

$$
\Delta S_{\mathrm{system}}=S_{\mathrm{gen}}\ge0.
$$

Thus an adiabatic process may be isentropic only when it is internally reversible. Free expansion into a vacuum is adiabatic and does no work, yet it generates entropy. The common implication runs one way: reversible and adiabatic implies isentropic. Constant entropy alone does not establish that both conditions held; generated entropy could have left with heat.

### Worked example: entropy generated during reservoir heat transfer

A $600\ \mathrm{K}$ reservoir transfers $100\ \mathrm{kJ}$ to a $300\ \mathrm{K}$ reservoir. Take both reservoirs together as an isolated system.

The hot reservoir remains at constant temperature, so its entropy change is

$$
\Delta S_H=\frac{Q_H}{T_H}
=\frac{-100}{600}
=-0.1667\ \mathrm{kJ/K}.
$$

For the cold reservoir,

$$
\Delta S_L=\frac{Q_L}{T_L}
=\frac{100}{300}
=0.3333\ \mathrm{kJ/K}.
$$

No entropy crosses the outer boundary of the combined system. Its entropy change is therefore entirely generated entropy:

$$
S_{\mathrm{gen}}
=\Delta S_H+\Delta S_L
=0.1666\ \mathrm{kJ/K}.
$$

The result can also be written $Q(1/T_L-1/T_H)$. It tends to zero as the two temperatures approach one another, which is the reversible heat-transfer limit. A finite heat-transfer rate then requires an increasingly large area or increasingly long time.

### Worked example: an insulated free expansion

One kilogram of ideal gas initially occupies $0.20\ \mathrm{m^3}$ in one side of a rigid insulated vessel. A partition is removed and the gas fills a total volume of $0.50\ \mathrm{m^3}$. For an ideal gas, $u=u(T)$. Since $Q=0$, $W=0$, and kinetic and potential changes are negligible, the first law gives

$$
\Delta U=0\quad\Longrightarrow\quad T_2=T_1.
$$

The entropy change is evaluated from the end states, even though the intermediate states are not in equilibrium:

$$
\begin{aligned}
s_2-s_1
&=c_v\ln\left(\frac{T_2}{T_1}\right)
+R\ln\left(\frac{v_2}{v_1}\right)\\
&=R\ln\left(\frac{0.50}{0.20}\right)\\
&=R\ln(2.5).
\end{aligned}
$$

For air with $R=0.287\ \mathrm{kJ/(kg\,K)}$,

$$
\Delta S=1(0.287)\ln(2.5)
=0.263\ \mathrm{kJ/K}.
$$

Because the vessel is adiabatic, $S_{\mathrm{gen}}=0.263\ \mathrm{kJ/K}$. Treating $Q=0$ as evidence of $\Delta S=0$ would miss the irreversibility of the unrestrained expansion.

## Entropy carried through a control volume

Matter entering or leaving carries specific entropy. The rate balance is

$$
\frac{dS_{\mathrm{CV}}}{dt}
=\sum_k\frac{\dot Q_k}{T_{b,k}}
+\sum_{\mathrm{in}}\dot m s
-\sum_{\mathrm{out}}\dot m s
+\dot S_{\mathrm{gen}}.
$$

At steady state the accumulation term vanishes. For one inlet and one outlet,

$$
\dot S_{\mathrm{gen}}
=\dot m(s_2-s_1)-\sum_k\frac{\dot Q_k}{T_{b,k}}.
$$

An adiabatic steady one-stream device therefore has $s_2\ge s_1$. An ideal turbine, compressor, pump, or nozzle uses the limiting value $s_2=s_1$ as its benchmark. A throttling valve is different: its energy model gives $h_2\approx h_1$, while its entropy generally rises.

### Worked example: heat loss from a steady turbine

Air flows through a turbine at $\dot m=2.0\ \mathrm{kg/s}$. It enters at $800\ \mathrm{K}$ and $600\ \mathrm{kPa}$ and leaves at $500\ \mathrm{K}$ and $100\ \mathrm{kPa}$. The turbine loses $40\ \mathrm{kW}$ through a boundary at $350\ \mathrm{K}$. Use $c_p=1.005\ \mathrm{kJ/(kg\,K)}$ and $R=0.287\ \mathrm{kJ/(kg\,K)}$.

First find the specific-entropy change:

$$
\begin{aligned}
s_2-s_1
&=1.005\ln\left(\frac{500}{800}\right)
-0.287\ln\left(\frac{100}{600}\right)\\
&=1.005(-0.4700)-0.287(-1.7918)\\
&=-0.4724+0.5142\\
&=0.0418\ \mathrm{kJ/(kg\,K)}.
\end{aligned}
$$

Heat into the control volume is negative: $\dot Q=-40\ \mathrm{kW}$. The steady entropy balance gives

$$
\begin{aligned}
\dot S_{\mathrm{gen}}
&=\dot m(s_2-s_1)-\frac{\dot Q}{T_b}\\
&=2.0(0.0418)-\frac{-40}{350}\\
&=0.0836+0.1143\\
&=0.1979\ \mathrm{kW/K}.
\end{aligned}
$$

The air's entropy rises only slightly, but entropy also leaves with the rejected heat. Generation must cover both effects. If the calculation had used $+40\ \mathrm{kW}$ for heat into the turbine, it would understate generation and could even produce a false negative result.

## Locating irreversibility in equipment

Entropy generation is most useful when the boundary is chosen to isolate a component. For an adiabatic turbine with one inlet and one outlet,

$$
\dot S_{\mathrm{gen}}=\dot m(s_2-s_1).
$$

The ideal reference outlet at the same pressure has $s_{2s}=s_1$. The actual outlet has $s_2\gt s_1$, and, for a gas turbine, generally $h_2\gt h_{2s}$. Less of the inlet enthalpy drop appears as shaft work. The isentropic efficiency packages that comparison as $(h_1-h_2)/(h_1-h_{2s})$, while the entropy balance identifies the irreversibility responsible for the departure.

For an adiabatic compressor, the same entropy inequality holds, but the work consequence is reversed. At a fixed outlet pressure the actual enthalpy is higher than the isentropic outlet enthalpy, so the compressor needs more work. Entropy generation does not itself have units of lost work. Multiplication by an appropriate environmental temperature turns it into exergy destruction, $\dot X_{\mathrm{dest}}=T_0\dot S_{\mathrm{gen}}$.

A heat exchanger containing both streams illustrates why component boundaries matter. If the whole exchanger is approximately adiabatic to its surroundings, no entropy term crosses with heat even though substantial heat passes internally from the hot stream to the cold stream. At steady state,

$$
\dot S_{\mathrm{gen}}
=\sum_{\mathrm{out}}\dot m s
-\sum_{\mathrm{in}}\dot m s.
$$

The hot stream loses entropy and the cold stream gains entropy. The cold-side gain exceeds the hot-side loss whenever heat crosses a finite temperature difference. If only the hot stream were selected as the control volume, the heat crossing the separating wall would appear explicitly as $\dot Q/T_b$. Both descriptions agree when their boundaries and temperatures are stated consistently.

Mixing is another common source. Suppose two portions of the same ideal gas at equal pressure but different temperatures mix adiabatically in a rigid, insulated vessel. Conservation of energy fixes the final temperature. Each portion's entropy change is then evaluated between its own initial state and the common final state. One portion may lose entropy as it cools, but the sum is positive. If different ideal gases mix at the same temperature and pressure, entropy also rises because each species expands into the volume formerly unavailable to it. A model based only on final temperature would miss that composition effect.

The words *internally reversible* and *externally reversible* separate two issues. Internal reversibility excludes friction, viscous dissipation, unrestrained expansion, mixing, and other entropy production inside the chosen system. External reversibility also requires heat transfer across an infinitesimal temperature difference and mechanical interaction across an infinitesimal pressure difference at the surroundings. A piston-cylinder can be internally close to equilibrium while exchanging heat irreversibly with a reservoir much hotter than its boundary. Its working fluid may follow a well-defined quasi-equilibrium path even though the combined system and surroundings generate entropy.

The entropy change of the universe is shorthand for the entropy change of a sufficiently large isolated composite:

$$
\Delta S_{\mathrm{univ}}
=\Delta S_{\mathrm{system}}+\Delta S_{\mathrm{surroundings}}
=S_{\mathrm{gen}}.
$$

It is often an easy check for closed systems interacting with thermal reservoirs. It is less convenient for a plant with several flowing streams, where the control-volume rate balance keeps the bookkeeping local and avoids having to model an abstract universe.

Entropy generation depends on the process and boundary, but the total generation for a fixed physical process does not disappear when the analysis is subdivided. Splitting a plant into a compressor, combustor, turbine, and heat exchanger assigns a generation rate to each component; adding them recovers the generation for the enclosing plant when internal transfer terms cancel. That additive structure allows an engineer to rank where thermodynamic improvement is available. It does not say which modification is economical, only where irreversibility is being produced.

## Reading a $T$-$s$ diagram

For an internally reversible process, $\delta q_{\mathrm{rev}}=T\,ds$. The area under a path on a $T$-$s$ diagram is therefore heat per unit mass:

```text
T
|             2 *
|              /|
|             / |   area under path = q_rev
|            /  |
|       1 *-----|
|___________________ s
```

That area interpretation does not apply directly to an irreversible path, although the end states can still be plotted. A vertical line denotes constant entropy, not automatically an adiabatic reversible history.

| Process | System entropy change | Entropy generation | Main constraint |
|---|---:|---:|---|
| Reversible adiabatic | $0$ | $0$ | Isentropic benchmark |
| Actual adiabatic compression | $\gt0$ | $\gt0$ | More work than the isentropic compressor |
| Finite-temperature heat transfer | depends on boundary | $\gt0$ | Combined bodies gain entropy |
| Steady throttling | usually $\gt0$ | $\gt0$ | $h_2\approx h_1$ |
| Reversible isothermal heat addition | $Q/T$ | $0$ | Entropy enters with heat |

## Checks that catch most errors

- Temperatures inside logarithms, denominators, and isentropic relations must be absolute. Celsius temperature differences are usable, but Celsius temperature ratios are not.
- A heat-transfer entropy term uses the local boundary temperature. The fluid's bulk mean temperature is a substitute only when a model establishes it as the crossing temperature.
- Specific entropy has units such as $\mathrm{kJ/(kg\,K)}$; multiplying by mass flow gives $\mathrm{kW/K}$. Adding a specific term directly to a total rate is dimensionally wrong.
- An entropy balance does not replace the mass and energy balances. Outlet state properties often require all three.
- A negative computed generation rate signals a sign error, a poor property approximation, inconsistent states, or an impossible proposed process. Rounding can create a tiny negative value near the reversible limit, but it cannot explain a substantial one.
- Constant-$k$ relations should not be used across a large temperature range when variable heat capacity matters. Property tables or the integral in $c_p(T)/T$ preserve the same balance structure.

<div className="see-also">

See also: [second-law heat engines and refrigerators](/physics/thermodynamics/second-law-heat-engines-and-refrigerators) · [exergy and second-law efficiency](/physics/thermodynamics/exergy-and-second-law-efficiency) · [thermodynamic property relations](/physics/thermodynamics/thermodynamic-property-relations) · [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis) · [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables)

</div>
