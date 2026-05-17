---
title: Gas-Vapor Mixtures and Air Conditioning
sidebar_position: 14
---

# Gas-Vapor Mixtures and Air Conditioning

Air-conditioning analysis treats atmospheric air as a mixture of dry air and water vapor. The dry-air component behaves nearly as an ideal gas, while the water vapor amount is limited by saturation pressure at the mixture temperature. This coupling creates humidity, dew point, wet-bulb behavior, cooling with dehumidification, evaporative cooling, and cooling-tower performance.

Cengel's psychrometric chapter is highly practical. The psychrometric chart is a graphical property table for moist air at a specified pressure. It organizes dry-bulb temperature, humidity ratio, relative humidity, enthalpy, specific volume, dew-point temperature, and wet-bulb temperature so that HVAC processes can be solved by mass and energy balances.

## Definitions

- **Dry air** is the mixture of noncondensing gases in atmospheric air, treated as one ideal gas.
- **Atmospheric air** or **moist air** is dry air plus water vapor.
- **Humidity ratio** is $\omega=m_v/m_a$, the mass of water vapor per mass of dry air.
- **Relative humidity** is $\phi=P_v/P_g$, the ratio of water-vapor partial pressure to saturation pressure at the same temperature.
- **Dew-point temperature** is the temperature at which water vapor begins to condense when moist air is cooled at constant pressure and humidity ratio.
- **Specific humidity** and **humidity ratio** are often used in similar ways in HVAC contexts, but Cengel's psychrometric formulas typically use $\omega$.
- **Dry-bulb temperature** is the ordinary air temperature. **Wet-bulb temperature** includes evaporative cooling effects at a wetted thermometer.
- **Adiabatic saturation** is a process in which unsaturated air contacts liquid water in an insulated device and approaches saturation.
- **Cooling and dehumidification** occurs when moist air is cooled below its dew point and water condenses out.
- **Evaporative cooling** lowers dry-bulb temperature by evaporating water into air, approximately at constant enthalpy for simple idealized devices.

Balances are usually written per kg of dry air because dry air is conserved through humidification, cooling, and dehumidification devices while water vapor may be added or removed. This convention prevents moving denominators as condensation changes the water-vapor mass.
For this topic, a complete engineering model should state the boundary, the time basis, the property model, and the sign convention before any numbers are substituted. In gas-vapor mixtures and air conditioning, that habit is especially important because several formulas look similar while answering different physical questions. A closed-system expression, a steady-flow expression, an ideal-gas relation, and a property-table interpolation may all contain pressure, temperature, or enthalpy, but they do not have the same assumptions. The safest workflow is to write the general balance or defining relation first, cancel terms with a written reason, and only then insert table values or constants.

The second modeling habit is to keep the basis visible. Some calculations are per unit mass, some per mole, some per kg dry air, and some per unit time. A correct formula on the wrong basis is a common source of errors that look numerically plausible. When a table gives $\mathrm{kJ/kg}$, multiply by $\dot m$ to get $\mathrm{kW}$; when a reaction is balanced in kmol, convert to mass only after the element balance is complete; when a mixture property uses mole fraction, do not substitute mass fraction without conversion.

## Key results

For ideal-gas dry air and water vapor,

$$
\omega=0.622\frac{P_v}{P-P_v}.
$$

Relative humidity gives

$$
P_v=\phi P_g(T),
$$

where $P_g(T)$ is the saturation pressure of water at the dry-bulb temperature. The moist-air enthalpy per kg dry air is commonly approximated by

$$
h \approx 1.005T + \omega(2500+1.88T)
$$

with $T$ in $^{\circ}C$ and $h$ in $\mathrm{kJ/kg_{dry\ air}}$.

Specific volume per kg dry air can be estimated by

$$
v=\frac{R_aT_K}{P-P_v}.
$$

For a steady-flow air-conditioning device with condensate leaving as liquid water,

$$
\dot m_a\omega_1=\dot m_a\omega_2+\dot m_w,
$$

and an energy balance, neglecting fan work and kinetic-potential changes, is

$$
\dot Q=\dot m_a(h_2-h_1)+\dot m_w h_w
$$

with sign depending on whether heat is added to or removed from the air stream. Psychrometric charts encode these formulas graphically and are often faster than repeated table lookup.
These results should be read as a hierarchy rather than a list of isolated equations. Conservation of mass and energy set the allowed accounting; property relations supply the missing state data; the second law or equilibrium criterion decides direction, limits, and losses. A numerical answer is not finished until it passes three checks: the units reduce to the requested quantity, the sign matches the stated energy or entropy transfer direction, and the magnitude is reasonable compared with a limiting case. Useful limiting cases include zero heat transfer, reversible operation, incompressible behavior, ideal-gas behavior, saturated-liquid or saturated-vapor endpoints, and equal reservoir temperatures.

Because the textbook often moves between exact laws and engineering approximations, the approximation should be named in the solution. Examples include constant specific heats, negligible kinetic energy, negligible pump work, adiabatic devices, isentropic turbomachinery, ideal-gas mixtures, dry-air approximations, and linear interpolation. Naming the approximation makes later refinement straightforward: replace the approximate property model or restore the neglected term without rebuilding the whole analysis.

## Visual

ASCII sketch of a psychrometric chart:

```text
humidity ratio
omega
|                 saturation curve phi = 100%
|             ___/
|         ___/     curved relative humidity lines
|     ___/
| ___/________________________ dry-bulb temperature
       dew point moves horizontally at constant omega
```

| Process | Approximate chart path | What changes |
|---|---|---|
| Sensible heating | horizontal right | $T$ rises, $\omega$ constant |
| Sensible cooling above dew point | horizontal left | $T$ falls, $\omega$ constant |
| Cooling with dehumidification | left and downward | $T$ falls, water condenses |
| Humidification with steam | upward and right | $\omega$ and enthalpy rise |
| Evaporative cooling | up and left near constant $h$ | $T$ falls, $\omega$ rises |

## Worked example 1: humidity ratio from relative humidity

**Problem.** Atmospheric air is at $30{}^{\circ}C$, $P=101.325\ \mathrm{kPa}$, and $60\%$ relative humidity. The saturation pressure of water at $30{}^{\circ}C$ is $4.246\ \mathrm{kPa}$. Find the humidity ratio.

**Method.**

1. Compute water-vapor partial pressure:

$$
P_v=\phi P_g=0.60(4.246)=2.548\ \mathrm{kPa}.
$$

2. Use the humidity-ratio formula:

$$
\omega=0.622\frac{P_v}{P-P_v}.
$$

3. Substitute:

$$
\omega=0.622\frac{2.548}{101.325-2.548}
=0.0160\ \mathrm{kg_v/kg_{da}}.
$$

**Checked answer.** The humidity ratio is about $0.016\ \mathrm{kg}$ water vapor per kg dry air. It is below the saturated value at $30{}^{\circ}C$, as expected for $60\%$ relative humidity.

## Worked example 2: cooling and dehumidification load

**Problem.** Moist air flows at $1.0\ \mathrm{kg_{dry\ air}/s}$ from $30{}^{\circ}C$, $50\%$ relative humidity to $15{}^{\circ}C$ saturated air. Use $P=101.325\ \mathrm{kPa}$, $P_g(30{}^{\circ}C)=4.246\ \mathrm{kPa}$, and $P_g(15{}^{\circ}C)=1.705\ \mathrm{kPa}$. Estimate condensate rate and cooling load using $h=1.005T+\omega(2500+1.88T)$.

**Method.**

1. Inlet vapor pressure:

$$
P_{v1}=0.50(4.246)=2.123\ \mathrm{kPa}.
$$

2. Inlet humidity ratio:

$$
\omega_1=0.622\frac{2.123}{101.325-2.123}=0.0133.
$$

3. Exit saturated vapor pressure is $P_{v2}=1.705\ \mathrm{kPa}$:

$$
\omega_2=0.622\frac{1.705}{101.325-1.705}=0.01065.
$$

4. Condensate rate:

$$
\dot m_w=\dot m_a(\omega_1-\omega_2)=1.0(0.0133-0.01065)=0.00265\ \mathrm{kg/s}.
$$

5. Enthalpies:

$$
h_1=1.005(30)+0.0133[2500+1.88(30)]=64.2\ \mathrm{kJ/kg_{da}},
$$

$$
h_2=1.005(15)+0.01065[2500+1.88(15)]=42.0\ \mathrm{kJ/kg_{da}}.
$$

6. Cooling load, neglecting condensate liquid enthalpy correction:

$$
\dot Q_{out}=\dot m_a(h_1-h_2)=22.2\ \mathrm{kW}.
$$

**Checked answer.** The coil removes about $22\ \mathrm{kW}$ and condenses $0.00265\ \mathrm{kg/s}$ of water.

## Code

```python
def humidity_ratio(Pv, P=101.325):
    return 0.622 * Pv / (P - Pv)

def moist_air_h(T_C, omega):
    return 1.005 * T_C + omega * (2500.0 + 1.88 * T_C)

w1 = humidity_ratio(0.50 * 4.246)
w2 = humidity_ratio(1.705)
h1 = moist_air_h(30.0, w1)
h2 = moist_air_h(15.0, w2)
print(w1, w2, w1 - w2)
print(h1, h2, h1 - h2)
```

## Common pitfalls

- Using total air mass instead of dry-air mass as the basis for humidity ratio.
- Confusing relative humidity with humidity ratio.
- Assuming cooling always dehumidifies; condensation begins only below the dew point.
- Reading a psychrometric chart at the wrong barometric pressure.
- Ignoring condensate mass and enthalpy when dehumidification is large.
- Starting from a special-case equation before checking that its assumptions actually hold. Write the general balance or definition first, then reduce it.
- Leaving property-table values unlabeled. Record the substance, phase region, pressure or temperature row, interpolation fraction, and units so the result can be audited.
- Rounding intermediate states too aggressively. Keep extra digits through property lookup, quality calculation, and efficiency ratios, then round the final answer to justified precision.
- Skipping a limiting-case check. Test the result against reversible operation, zero pressure drop, saturated endpoints, ideal-gas behavior, or equal-temperature reservoirs when those limits are meaningful.
- Treating a numerical solver or chart as a substitute for physical reasoning. Software can return a precise-looking number even when the selected phase, reference state, or boundary model is wrong.
- Forgetting to state whether the reported answer is specific, total, or rate based.

## Connections

- [gas mixtures](/physics/thermodynamics/gas-mixtures)
- [refrigeration cycles](/physics/thermodynamics/refrigeration-cycles)
- [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis)
- [microscopic foundations](/physics/statistical-mechanics/)
- [basic thermal physics](/physics/general/)
- [thermochemistry](/chemistry/general/thermochemistry)
- [physical chemistry](/chemistry/physical-chemistry/)
- [engineering mathematics](/math/engineering-math/)
- [thermal systems control](/cs/control-engineering/)
