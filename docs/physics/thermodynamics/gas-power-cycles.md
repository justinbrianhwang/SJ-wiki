---
title: Gas Power Cycles
sidebar_position: 9
---

# Gas Power Cycles

Ideal gas power cycles strip an engine down to a sequence of compression, heat addition, expansion, and heat rejection. Combustion and exhaust are replaced by heat transfer, the working fluid is returned to its initial state, and mechanical details are removed. The resulting cycles do not predict brake power directly; they show how compression ratio, pressure ratio, temperature limits, and component losses shape performance.

Two families dominate introductory analysis. Reciprocating-engine models use the Otto and Diesel cycles and are drawn most naturally on $P$-$v$ diagrams. Continuous-flow gas turbines use the Brayton cycle, with a compressor, combustor or heater, turbine, and cooler or exhaust. Stirling and Ericsson cycles provide useful reversible benchmarks but describe different hardware and heat-transfer requirements.

## What the air-standard model keeps and discards

The air-standard assumptions replace the open combustion process by a closed loop:

- Air circulates as the working fluid and behaves as an ideal gas.
- Combustion becomes external heat addition; exhaust and intake become heat rejection that restores the initial state.
- Every process is internally reversible in the basic ideal cycle.
- The cold-air-standard refinement takes $c_p$, $c_v$, and $k=c_p/c_v$ as constants, usually at a reference temperature.

Variable-specific-heat air-standard analysis keeps $c_p(T)$ and $c_v(T)$ while retaining the other idealizations. Real engines add combustion chemistry, pressure losses, heat transfer through cylinder walls, friction, non-isentropic compression and expansion, and finite valve timing. Gas-turbine calculations also need compressor and turbine efficiencies, combustor pressure drop, cooling flow, and mechanical losses.

Thermal efficiency and net specific work answer different design questions:

$$
\eta_{th}=\frac{w_{net}}{q_{in}}
=1-\frac{q_{out}}{q_{in}},
$$

$$
w_{net}=w_{out}-w_{in}.
$$

A change can raise specific work without raising efficiency, or raise efficiency while reducing specific work. A complete cycle calculation should report both and satisfy $q_{in}-q_{out}=w_{net}$.

## Otto cycle: heat addition at constant volume

The ideal Otto cycle represents a spark-ignition engine:

1. $1\rightarrow2$: isentropic compression.
2. $2\rightarrow3$: constant-volume heat addition.
3. $3\rightarrow4$: isentropic expansion.
4. $4\rightarrow1$: constant-volume heat rejection.

```text
P
|           3 *
|             |\
|             | \
|           2 *  * 4
|             \  /
|              \/
|           1  *
|_____________________ v
```

The compression ratio is

$$
r=\frac{v_1}{v_2}=\frac{V_{\max}}{V_{\min}}.
$$

Since processes 2–3 and 4–1 occur at constant volume,

$$
q_{in}=c_v(T_3-T_2),
\qquad
q_{out}=c_v(T_4-T_1).
$$

The two isentropic processes have the same volume ratio:

$$
\frac{T_2}{T_1}=r^{k-1},
\qquad
\frac{T_3}{T_4}=r^{k-1}.
$$

Therefore $T_2=r^{k-1}T_1$ and $T_3=r^{k-1}T_4$. Subtracting gives

$$
T_3-T_2=r^{k-1}(T_4-T_1).
$$

Substitution into the efficiency definition yields

$$
\eta_{\mathrm{Otto}}
=1-\frac{T_4-T_1}{T_3-T_2}
=1-\frac{1}{r^{k-1}}.
$$

Within the cold-air model, efficiency depends only on $r$ and $k$, not on the amount of heat supplied. Increasing compression ratio raises the ideal efficiency by lowering the fraction of input heat rejected. Actual spark-ignition engines cannot increase $r$ without limit because autoignition, heat loss, friction, peak pressure, and material constraints intervene.

### Worked example: Otto cycle state calculation

Air begins compression at $T_1=300\ \mathrm{K}$. Let $r=8.0$, $k=1.4$, $c_v=0.718\ \mathrm{kJ/(kg\,K)}$, and let constant-volume heat addition be $q_{in}=800\ \mathrm{kJ/kg}$.

First calculate the isentropic temperature ratio:

$$
r^{k-1}=8^{0.4}=2.297.
$$

Thus

$$
T_2=300(2.297)=689.1\ \mathrm{K}.
$$

Heat addition sets state 3:

$$
T_3=T_2+\frac{q_{in}}{c_v}
=689.1+\frac{800}{0.718}
=1803.3\ \mathrm{K}.
$$

Isentropic expansion gives

$$
T_4=\frac{T_3}{2.297}=785.1\ \mathrm{K}.
$$

The rejected heat magnitude is

$$
q_{out}=0.718(785.1-300)
=348.3\ \mathrm{kJ/kg}.
$$

Then

$$
w_{net}=800-348.3=451.7\ \mathrm{kJ/kg},
$$

$$
\eta_{th}=\frac{451.7}{800}=0.5646.
$$

The direct formula gives $1-1/2.297=0.5646$, providing an independent check. The peak temperature is part of the result and should be compared with whatever material or combustion limit the model is meant to represent.

### Net work and mean effective pressure

For a closed piston cycle, the area enclosed on a $P$-$v$ diagram is the net specific boundary work. A wider or taller loop generally indicates more work per unit mass, but it does not by itself determine efficiency because heat input may have risen as well. On a $T$-$s$ diagram for internally reversible paths, the corresponding enclosed area is net heat, equal to net work over a cycle.

Engine size enters through mean effective pressure rather than thermal efficiency. The mean effective pressure is the hypothetical constant pressure that would produce the same net work over the displacement volume:

$$
\mathrm{MEP}=\frac{W_{net}}{V_{\max}-V_{\min}}
=\frac{w_{net}}{v_1-v_2}.
$$

MEP has units of pressure and compares work output among engines of different displacement. Two ideal cycles can have the same thermal efficiency but different MEP if their heat input or peak pressure differs. Actual engine performance further distinguishes indicated work inside the cylinder from brake work available at the shaft; their difference includes mechanical friction and accessory loads.

## Diesel and dual cycles

The ideal Diesel cycle replaces Otto's constant-volume heat addition with constant-pressure heat addition. It approximates the early textbook picture of compression ignition, where fuel injection continues while the piston moves outward. Its processes are isentropic compression, constant-pressure heat addition, isentropic expansion, and constant-volume heat rejection.

Define the cutoff ratio

$$
r_c=\frac{v_3}{v_2}.
$$

At constant pressure, $T_3/T_2=v_3/v_2=r_c$. Combining that result with the two isentropic legs gives

$$
\eta_{\mathrm{Diesel}}
=1-\frac{1}{r^{k-1}}
\left[\frac{r_c^k-1}{k(r_c-1)}\right].
$$

For fixed compression ratio, larger $r_c$ extends heat addition farther into the expansion stroke and lowers thermal efficiency. At equal compression ratio and equal heat input, the ideal Otto cycle is more efficient than the ideal Diesel cycle. That comparison does not say a real spark-ignition engine must outperform a real compression-ignition engine: Diesel engines commonly operate at higher compression ratios and different load-control conditions.

The dual cycle splits heat addition into constant-volume and constant-pressure parts. It often tracks pressure histories better than either limiting model, at the cost of one more parameter. Modern combustion does not occur at exactly constant volume or pressure, so all three remain comparison models rather than literal indicator diagrams.

| Cycle | Ideal heat addition | Principal ratios | Typical role |
|---|---|---|---|
| Otto | constant volume | compression ratio $r$ | spark-ignition benchmark |
| Diesel | constant pressure | $r$, cutoff ratio $r_c$ | compression-ignition benchmark |
| Dual | volume then pressure | $r$, pressure and cutoff ratios | closer pressure-shape model |
| Brayton | constant pressure | pressure ratio $r_p$ | continuous-flow gas turbine |

## Brayton cycle: compression and expansion in steady devices

The ideal Brayton cycle has four steady-flow components:

1. $1\rightarrow2$: isentropic compression.
2. $2\rightarrow3$: constant-pressure heat addition.
3. $3\rightarrow4$: isentropic expansion.
4. $4\rightarrow1$: constant-pressure heat rejection.

Let $r_p=P_2/P_1=P_3/P_4$ and define

$$
a=r_p^{(k-1)/k}.
$$

The isentropic relations give

$$
T_2=aT_1,
\qquad
T_4=\frac{T_3}{a}.
$$

With constant $c_p$,

$$
w_c=c_p(T_2-T_1),
\qquad
w_t=c_p(T_3-T_4),
$$

$$
q_{in}=c_p(T_3-T_2),
\qquad
w_{net}=w_t-w_c.
$$

Because $(T_4-T_1)/(T_3-T_2)=1/a$, the thermal efficiency is

$$
\eta_{\mathrm{Brayton}}
=1-\frac{1}{a}
=1-\frac{1}{r_p^{(k-1)/k}}.
$$

The ideal efficiency rises with pressure ratio, but fixed minimum and maximum temperatures place a separate limit on net work. Substituting the state relations gives

$$
\frac{w_{net}}{c_p}
=T_3\left(1-\frac1a\right)-T_1(a-1).
$$

Differentiating with respect to $a$ shows that net work is maximum when

$$
a_{\mathrm{opt}}=\sqrt{\frac{T_3}{T_1}},
$$

or

$$
r_{p,\mathrm{opt}}
=\left(\frac{T_3}{T_1}\right)^{k/[2(k-1)]}.
$$

At that point $T_2=T_4=\sqrt{T_1T_3}$. Pushing pressure ratio toward the value at which $T_2=T_3$ leaves no temperature interval for heat addition and drives net work back toward zero, even though the simple efficiency expression continues to rise over its valid range.

### Worked example: simple ideal Brayton cycle

Air enters at $T_1=300\ \mathrm{K}$. The pressure ratio is $r_p=10$, turbine inlet temperature is $T_3=1400\ \mathrm{K}$, $k=1.4$, and $c_p=1.004\ \mathrm{kJ/(kg\,K)}$.

The isentropic temperature ratio is

$$
a=10^{0.4/1.4}=1.931.
$$

Hence

$$
T_2=1.931(300)=579.3\ \mathrm{K},
$$

$$
T_4=\frac{1400}{1.931}=725.0\ \mathrm{K}.
$$

Compressor work and turbine work are

$$
w_c=1.004(579.3-300)=280.4\ \mathrm{kJ/kg},
$$

$$
w_t=1.004(1400-725.0)=677.7\ \mathrm{kJ/kg}.
$$

Thus

$$
w_{net}=677.7-280.4=397.3\ \mathrm{kJ/kg}.
$$

Heat input is

$$
q_{in}=1.004(1400-579.3)=824.0\ \mathrm{kJ/kg},
$$

and

$$
\eta_{th}=\frac{397.3}{824.0}=0.482.
$$

The compressor consumes $280.4/677.7=41.4\%$ of the turbine output. This back-work ratio is much larger than in liquid-pump vapor cycles because compressing a gas requires substantial specific work.

## Moving from ideal to actual turbomachinery

An actual adiabatic compressor has a higher outlet enthalpy than an isentropic compressor reaching the same pressure. Its isentropic efficiency is

$$
\eta_c=\frac{h_{2s}-h_1}{h_2-h_1}.
$$

For a constant-$c_p$ ideal gas,

$$
T_2=T_1+\frac{T_{2s}-T_1}{\eta_c}.
$$

An actual adiabatic turbine delivers less work and exits at a higher enthalpy than its isentropic reference:

$$
\eta_t=\frac{h_3-h_4}{h_3-h_{4s}},
$$

$$
T_4=T_3-\eta_t(T_3-T_{4s}).
$$

The subscripts $2s$ and $4s$ identify hypothetical isentropic outlets at the actual outlet pressures. Using the compressor formula for a turbine, or placing an efficiency in the wrong side of the fraction, can predict an actual device better than the reversible benchmark.

Take the preceding Brayton cycle but let $\eta_c=0.82$ and $\eta_t=0.86$, while keeping $r_p=10$, $T_1=300\ \mathrm{K}$, and $T_3=1400\ \mathrm{K}$. The isentropic reference temperatures remain $T_{2s}=579.3\ \mathrm{K}$ and $T_{4s}=725.0\ \mathrm{K}$.

The actual compressor outlet is

$$
\begin{aligned}
T_2
&=300+\frac{579.3-300}{0.82}\\
&=640.6\ \mathrm{K}.
\end{aligned}
$$

The actual turbine outlet is

$$
\begin{aligned}
T_4
&=1400-0.86(1400-725.0)\\
&=819.5\ \mathrm{K}.
\end{aligned}
$$

Using $c_p=1.004\ \mathrm{kJ/(kg\,K)}$,

$$
w_c=1.004(640.6-300)=342.0\ \mathrm{kJ/kg},
$$

$$
w_t=1.004(1400-819.5)=582.8\ \mathrm{kJ/kg}.
$$

The net work falls to

$$
w_{net}=582.8-342.0=240.8\ \mathrm{kJ/kg}.
$$

Heat addition is

$$
q_{in}=1.004(1400-640.6)=762.4\ \mathrm{kJ/kg},
$$

so

$$
\eta_{th}=\frac{240.8}{762.4}=0.316.
$$

The efficiency loss is larger than either component's percentage loss considered alone because the compressor penalty and turbine penalty act in opposite directions on net work. The actual back-work ratio is $342.0/582.8=58.7\%$. Pressure losses in the combustor and ducts would reduce performance further by lowering the turbine expansion ratio relative to the compressor pressure ratio.

For variable heat capacities, these efficiency definitions remain enthalpy ratios. The temperature forms do not. One first finds $h_{2s}$ or $h_{4s}$ from an isentropic property calculation, applies the efficiency to enthalpy, then obtains the actual temperature from $h(T)$.

The specific-heat ratio $k$ needs attention in cycle comparisons. A larger $k$ produces a larger temperature change for a given isentropic pressure or volume ratio and raises the cold-air Otto and Brayton efficiency formulas. Real combustion products have different composition from air, and their effective $k$ changes with temperature. Substituting $k=1.4$ everywhere can give internally tidy state tables that do not represent the hot expansion accurately. Variable-property analysis avoids assigning one average $k$ to every leg: entropy functions determine isentropic outlet states, while enthalpy differences determine heat and work.

Cycle limits should also be imposed as physical state constraints. A maximum temperature represents material durability, blade cooling, emissions, or knock only indirectly; a maximum pressure controls cylinder and casing loads. Optimizing with only one limit can push another state outside its allowed range. Comparisons are clearest when the inlet state, peak temperature, pressure or volume ratio, component efficiencies, and pressure losses are held or varied explicitly.

## Regeneration, intercooling, and reheat

A regenerator transfers heat from turbine exhaust to compressed air before the combustor. In the ideal limiting case of perfect regeneration, the compressed stream can approach $T_4$ and the exhaust can approach $T_2$. Regeneration is thermodynamically possible only when

$$
T_4>T_2.
$$

It reduces external heat input for a given turbine inlet temperature but does not change compressor or turbine work in the ideal cycle. Its effectiveness is commonly defined as

$$
\varepsilon_{\mathrm{reg}}
=\frac{T_5-T_2}{T_4-T_2},
$$

where state 5 is the compressed-air outlet from the regenerator. Real regenerators impose pressure drops and have finite effectiveness, so a small ideal heat-recovery benefit may not survive implementation.

Intercooling divides compression into stages and cools the gas between them. For ideal cooling back to the original inlet temperature and negligible pressure losses, minimum compressor work occurs when the pressure ratios are equal across stages. Reheat makes the analogous division on the turbine side and raises expansion work by reheating between stages. Intercooling and reheat tend to increase net specific work, but both add external heat that can lower simple-cycle thermal efficiency. Combining them with regeneration recovers some of the added exhaust heat and can improve efficiency as well.

### Worked example: regenerator heat saving

Use the Brayton states above, with $T_2=579.3\ \mathrm{K}$ and $T_4=725.0\ \mathrm{K}$. Let regenerator effectiveness be $0.75$.

The compressed air leaves the regenerator at

$$
T_5=T_2+\varepsilon_{\mathrm{reg}}(T_4-T_2)
=579.3+0.75(725.0-579.3)
=688.6\ \mathrm{K}.
$$

External heat input becomes

$$
q_{in,\mathrm{reg}}
=c_p(T_3-T_5)
=1.004(1400-688.6)
=714.2\ \mathrm{kJ/kg}.
$$

The ideal compressor and turbine works remain unchanged, so $w_{net}=397.3\ \mathrm{kJ/kg}$. The regenerated efficiency is

$$
\eta_{\mathrm{reg}}
=\frac{397.3}{714.2}
=0.556.
$$

The heat saved is $824.0-714.2=109.8\ \mathrm{kJ/kg}$. At a higher pressure ratio, $T_2$ rises and $T_4$ falls; eventually their order reverses and regeneration offers no temperature driving force.

## Reversible external-heating benchmarks

The Stirling cycle uses isothermal compression and expansion joined by constant-volume regeneration. The Ericsson cycle uses isothermal compression and expansion joined by constant-pressure regeneration. With complete regeneration and reversible processes, both have the Carnot efficiency $1-T_L/T_H$. Reaching that limit requires isothermal heat transfer with vanishing temperature differences and a perfect regenerator, which implies severe heat-transfer and size demands at finite power.

Jet engines use a Brayton-like gas-generator path but aim primarily at thrust rather than shaft work. Their useful output depends on aircraft speed and exhaust momentum. A cycle improvement that increases turbine shaft work is not automatically the best propulsion change; propulsive efficiency also penalizes producing a small mass flow at an excessively high jet velocity.

## Limits to keep attached to the formulas

- Compression ratio $V_{\max}/V_{\min}$ belongs to piston cycles; compressor pressure ratio belongs to Brayton machinery. They are not substitutes.
- Constant-$k$ equations overpredict or underpredict state temperatures when heat capacities change substantially. High turbine inlet temperatures call for variable-property data.
- Isentropic component formulas describe benchmarks. Actual outlet temperatures require compressor and turbine isentropic efficiencies and should include pressure losses where relevant.
- Regeneration can reduce fuel input but cannot create net work by itself. A temperature crossover, finite heat-exchanger area, and pressure-drop allowance are required.
- Comparing cycles at different peak temperatures, pressure limits, or heat inputs can reverse apparent rankings. State the common constraints before drawing a design conclusion.

<div className="see-also">

See also: [energy, heat, work, and the first law](/physics/thermodynamics/energy-heat-work-and-first-law) · [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance) · [exergy and second-law efficiency](/physics/thermodynamics/exergy-and-second-law-efficiency) · [compressible flow](/physics/thermodynamics/compressible-flow) · [vapor and combined power cycles](/physics/thermodynamics/vapor-and-combined-power-cycles)

</div>
