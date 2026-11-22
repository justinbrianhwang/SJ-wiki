---
title: Vapor and Combined Power Cycles
sidebar_position: 10
---

# Vapor and Combined Power Cycles

Vapor power cycles exploit phase change. A pump raises the pressure of liquid water with small work input, a boiler adds heat to produce high-pressure vapor, a turbine extracts work, and a condenser rejects heat to return the working fluid to liquid. The Rankine cycle is the practical alternative to the Carnot vapor cycle because it avoids compressing a wet mixture and accommodates real boilers and turbines.

Cengel develops the ideal Rankine cycle, actual deviations, reheat, regeneration, cogeneration, and combined gas-vapor cycles. The design logic is temperature management: raise the average temperature of heat addition, lower the average temperature of heat rejection, keep turbine moisture within limits, and recover heat where it has enough temperature to be useful.

## Tracking water through the Rankine loop

- The **Rankine cycle** is the ideal vapor power cycle: pump, boiler, turbine, condenser.
- **Pump work** is small because liquid specific volume is small: $w_p\approx v(P_2-P_1)$.
- **Boiler heat input** raises compressed liquid to saturated liquid, vaporizes it, and often superheats it.
- **Turbine work** comes from vapor enthalpy drop. Moisture at turbine exit must be limited to avoid blade erosion.
- **Condenser heat rejection** condenses low-pressure vapor to saturated liquid, closing the cycle.
- **Reheat** expands steam in stages with reheating between turbines, increasing turbine exit quality and often increasing net work.
- **Regeneration** bleeds steam from the turbine to heat feedwater before the boiler, raising the average heat-addition temperature.
- An **open feedwater heater** mixes extracted steam with feedwater at the same pressure. A **closed feedwater heater** transfers heat across a surface without mixing.
- **Cogeneration** produces both useful work and useful process heat from the same fuel input.
- A **combined cycle** uses a gas turbine topping cycle and a steam Rankine bottoming cycle, recovering high-temperature exhaust heat in a heat recovery steam generator.

Real plants include pressure drops, non-isentropic pumps and turbines, heat losses, mechanical losses, and condenser limitations. The ideal cycle remains useful because it isolates the thermodynamic benefit of pressure, temperature, reheat, and regeneration changes before component details are added.

The diagram shows one open feedwater heater. Plants with more heaters repeat the extraction and pumping pattern; without regeneration, the condenser pump sends feedwater toward the boiler train directly.

```mermaid
flowchart LR
  D["Condenser"] --> A["Condensate pump"]
  A --> E["Open feedwater heater"]
  E --> F["Boiler-feed pump"]
  F --> B["Boiler"]
  B --> C["Turbine"]
  C --> D
  C -.->|Extraction| E
```

State the plant boundary, time basis, property model, and sign convention before substituting values. Write the steady-flow balance for each component first, justify neglected heat, work, kinetic-energy, and potential-energy terms, and then insert property-table values.

Keep the mass-flow basis visible. Specific turbine work in $\mathrm{kJ/kg}$ becomes power only after multiplication by the mass flow rate. In regenerative cycles, bleed fractions change the flow through downstream turbine stages and the condenser.

## Rankine-cycle enthalpy bookkeeping

For the ideal Rankine cycle,

$$
\begin{aligned}
w_t &= h_3-h_4, \\
w_p &= h_2-h_1 \approx v_1(P_2-P_1), \\
q_{in} &= h_3-h_2, \\
q_{out} &= h_4-h_1, \\
\eta_{th} &= \frac{w_t-w_p}{q_{in}}.
\end{aligned}
$$

The pump raises pressure nearly isentropically while the fluid remains liquid. The turbine is ideally isentropic, so $s_4=s_3$ and the exit quality at condenser pressure is found from

$$
x_4=\frac{s_4-s_f}{s_{fg}}.
$$

## Raising the average heat-addition temperature

Ways to improve Rankine efficiency include lowering condenser pressure, superheating to higher turbine inlet temperature, increasing boiler pressure, reheating, and regenerating feedwater heating. Each has constraints. Lower condenser pressure can increase moisture; high boiler pressure may reduce exit quality; superheat is limited by materials; regeneration improves efficiency but reduces the mass flow through later turbine stages.

| Modification | Main benefit | Main tradeoff |
|---|---|---|
| Lower condenser pressure | lowers heat-rejection temperature | may increase turbine moisture |
| Superheat | raises heat-addition temperature and exit quality | material temperature limit |
| Reheat | improves quality and work output | added equipment and controls |
| Regeneration | raises feedwater temperature | reduces low-pressure turbine flow |
| Combined cycle | recovers gas-turbine exhaust heat | integration complexity |

## Using gas-turbine exhaust in a bottoming cycle

For a combined gas-vapor plant, the total thermal efficiency is

$$
\eta=\frac{\dot W_{gas}+\dot W_{steam}}{\dot Q_{fuel}}.
$$

The bottoming cycle uses energy that would otherwise leave with gas-turbine exhaust, but only the exergy above the steam-cycle temperature levels can be converted effectively.

Mass and energy balances set the accounting; property tables supply the water and steam states; entropy generation and exergy identify where performance is lost. Check that the component balances close, that pump and turbine work have the intended signs, and that the turbine exit state lies in the region used to evaluate $h_4$.

Name the approximations: incompressible pump work, isentropic turbomachinery, negligible kinetic and potential energy changes, adiabatic mixing, and linear table interpolation. Pressure drop, heat loss, and isentropic efficiencies can then be restored component by component.

## Estimating an ideal Rankine efficiency

**Problem.** An ideal Rankine cycle operates with condenser pressure $10\ \mathrm{kPa}$ and boiler pressure $8\ \mathrm{MPa}$. Saturated liquid leaves the condenser. Steam enters the turbine at $8\ \mathrm{MPa}$ and $480{}^{\circ}C$ with $h_3\approx3335\ \mathrm{kJ/kg}$ and $s_3\approx6.82\ \mathrm{kJ/(kg\,K)}$. At $10\ \mathrm{kPa}$, use $h_f=191.8\ \mathrm{kJ/kg}$, $h_{fg}=2392\ \mathrm{kJ/kg}$, $s_f=0.649\ \mathrm{kJ/(kg\,K)}$, $s_{fg}=7.501\ \mathrm{kJ/(kg\,K)}$, and $v_f=0.00101\ \mathrm{m^3/kg}$. Estimate efficiency.

**Method.**

1. Pump work:

$$
w_p\approx v_f(P_2-P_1)=0.00101(8000-10)=8.07\ \mathrm{kJ/kg}.
$$

2. Pump exit enthalpy:

$$
h_2=h_1+w_p=191.8+8.07=199.9\ \mathrm{kJ/kg}.
$$

3. Turbine exit is isentropic, so $s_4=s_3$. Quality:

$$
x_4=\frac{6.82-0.649}{7.501}=0.823.
$$

4. Turbine exit enthalpy:

$$
h_4=191.8+0.823(2392)=2161\ \mathrm{kJ/kg}.
$$

5. Work and heat:

$$
w_t=3335-2161=1174\ \mathrm{kJ/kg},
$$

$$
q_{in}=3335-199.9=3135\ \mathrm{kJ/kg}.
$$

6. Efficiency:

$$
\eta=\frac{1174-8.07}{3135}=0.372.
$$

**Checked answer.** The ideal efficiency is about $37\%$. The turbine exit quality is $82\%$, low enough that reheat or altered pressure choices may be considered.

## Solving the bleed fraction for an open heater

**Problem.** In an ideal regenerative Rankine cycle, feedwater enters an open feedwater heater at $h_2=200\ \mathrm{kJ/kg}$, extracted steam enters at $h_6=2700\ \mathrm{kJ/kg}$, and saturated liquid leaves at $h_3=640\ \mathrm{kJ/kg}$. Find the extraction fraction $y$ per kg of boiler flow.

**Method.**

1. Take the open feedwater heater as an adiabatic mixing chamber.
2. Let $y$ kg of extracted steam mix with $(1-y)$ kg of feedwater to produce $1$ kg leaving.
3. Energy balance:

$$
yh_6+(1-y)h_2=h_3.
$$

4. Solve:

$$
y(h_6-h_2)=h_3-h_2.
$$

5. Substitute:

$$
y=\frac{640-200}{2700-200}=\frac{440}{2500}=0.176.
$$

**Checked answer.** About $17.6\%$ of the main steam flow is extracted. This reduces low-pressure turbine work but raises the feedwater temperature and can increase cycle efficiency.

## Repeating the cycle calculation in Python

```python
def rankine_efficiency(h1, v1, P1, P2, h3, s3, sf, sfg, hfg):
    wp = v1 * (P2 - P1)
    h2 = h1 + wp
    x4 = (s3 - sf) / sfg
    h4 = h1 + x4 * hfg
    wt = h3 - h4
    qin = h3 - h2
    return x4, (wt - wp) / qin

def open_fwh_fraction(h_feed, h_bleed, h_exit):
    return (h_exit - h_feed) / (h_bleed - h_feed)

print(rankine_efficiency(191.8, 0.00101, 10, 8000, 3335, 6.82, 0.649, 7.501, 2392))
print(open_fwh_fraction(200, 2700, 640))
```

## Checks before trusting a cycle result

- Forgetting that pump work is small but not always zero in high-pressure cycles.
- Using turbine exit enthalpy without first determining whether the exit is wet or superheated.
- Assuming lowering condenser pressure always helps without checking exit quality.
- Applying a single mass flow rate through all turbine stages in regenerative cycles despite bleed flows.
- Confusing heat recovery in a combined cycle with perfect conversion of exhaust energy to work.
- Starting from a special-case equation before checking its assumptions. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

<div className="see-also">

See also: [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables) · [exergy and second-law efficiency](/physics/thermodynamics/exergy-and-second-law-efficiency) · [gas power cycles](/physics/thermodynamics/gas-power-cycles) · [microscopic foundations](/physics/statistical-mechanics/intro) · [basic thermal physics](/physics/general/intro) · [thermochemistry](/chemistry/general/thermochemistry) · [physical chemistry](/chemistry/physical-chemistry/intro) · [engineering mathematics](/math/engineering-math/intro) · [thermal systems control](/cs/control-engineering/intro)

</div>
