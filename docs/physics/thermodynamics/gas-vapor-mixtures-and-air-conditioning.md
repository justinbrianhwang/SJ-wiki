---
title: Gas-Vapor Mixtures and Air Conditioning
sidebar_position: 14
---

# Gas-Vapor Mixtures and Air Conditioning

Moist air is a gas mixture in which one constituent, water, can condense at ordinary temperatures. Dry air and water vapor are both modeled nearly as ideal gases at atmospheric pressure, but the vapor partial pressure cannot exceed water's saturation pressure at the mixture temperature. That phase-equilibrium limit produces dew point, condensation on cooling coils, evaporative cooling, and the curved saturation boundary of a psychrometric chart.

HVAC calculations are usually normalized by kilograms of dry air. Dry air passes through a heater, humidifier, cooling coil, or mixing box without condensing, while water may enter as liquid or steam and leave as vapor or condensate. A dry-air basis keeps one conserved denominator throughout the equipment train.

## Humidity ratio from partial pressure

Let $m_a$ denote dry-air mass and $m_v$ water-vapor mass. The humidity ratio is

$$
\omega=\frac{m_v}{m_a}.
$$

Apply the ideal-gas equation separately to vapor and dry air in the same volume at the same absolute temperature:

$$
P_vV=m_vR_vT,
\qquad
P_aV=m_aR_aT.
$$

Taking the ratio and using $P_a=P-P_v$ gives

$$
\omega
=\frac{R_a}{R_v}\frac{P_v}{P-P_v}
=0.622\frac{P_v}{P-P_v}.
$$

The factor $0.622$ is the molar-mass ratio $M_v/M_a$, approximately $18.015/28.97$. Humidity ratio has units of kilograms of vapor per kilogram of dry air, though it is dimensionless as a mass ratio.

Meteorology also uses *specific humidity*,

$$
q=\frac{m_v}{m_a+m_v}
=\frac{\omega}{1+\omega}.
$$

The two numbers are close for ordinary atmospheric moisture levels but are not identical. A formula or chart labeled $\omega$ uses the dry-air denominator.

Relative humidity compares the actual vapor partial pressure with the saturation pressure of water at the dry-bulb temperature:

$$
\phi=\frac{P_v}{P_{\mathrm{sat}}(T)}.
$$

At saturation, $\phi=1$ and $P_v=P_{\mathrm{sat}}(T)$. Relative humidity can change when air is heated even though no water is added: $P_v$ and $\omega$ stay nearly constant at fixed total pressure, while $P_{\mathrm{sat}}(T)$ rises rapidly.

## Dew point and the onset of condensation

Cool an unsaturated moist-air sample at constant total pressure without adding or removing water. Its humidity ratio and vapor partial pressure remain constant until the saturation curve is reached. The dew-point temperature $T_{dp}$ satisfies

$$
P_{\mathrm{sat}}(T_{dp})=P_v.
$$

Further cooling cannot retain the original vapor mass in equilibrium. Water condenses, $\omega$ decreases, and the remaining air follows the saturation boundary. Dew point depends on the vapor partial pressure, not directly on the current dry-bulb temperature. Two air samples with different dry-bulb temperatures but the same $P_v$ have the same dew point.

### Worked example: humidity ratio and dew point

Atmospheric air is at $30{}^{\circ}\mathrm{C}$, $P=101.325\ \mathrm{kPa}$, and $60\%$ relative humidity. At $30{}^{\circ}\mathrm{C}$, $P_{\mathrm{sat}}=4.246\ \mathrm{kPa}$. Find its vapor pressure and humidity ratio.

The vapor partial pressure is

$$
P_v=\phi P_{\mathrm{sat}}
=0.60(4.246)
=2.548\ \mathrm{kPa}.
$$

Then

$$
\begin{aligned}
\omega
&=0.622\frac{2.548}{101.325-2.548}\\
&=0.01604\ \mathrm{kg_v/kg_{da}}.
\end{aligned}
$$

The dew point is the saturation temperature corresponding to $2.548\ \mathrm{kPa}$. A water saturation table places it at about $21.2{}^{\circ}\mathrm{C}$. Sensible cooling from $30{}^{\circ}\mathrm{C}$ to $25{}^{\circ}\mathrm{C}$ would leave $\omega$ unchanged; cooling below about $21.2{}^{\circ}\mathrm{C}$ would begin removing liquid water.

At the same temperature and relative humidity but a lower barometric pressure, $P_v$ is unchanged while $P-P_v$ decreases. The humidity ratio is therefore larger. Psychrometric charts belong to a specified total pressure, commonly one standard atmosphere.

## Enthalpy and volume on a dry-air basis

Choose liquid water at $0{}^{\circ}\mathrm{C}$ as a common approximate enthalpy reference. Per kilogram of dry air, the moist-air enthalpy is the dry-air contribution plus $\omega$ times the water-vapor contribution:

$$
h=h_a+\omega h_v.
$$

For ordinary HVAC temperatures,

$$
h\approx1.005T+\omega(2500+1.88T),
$$

where $T$ is in degrees Celsius and $h$ is in $\mathrm{kJ/kg_{da}}$. The $2500\ \mathrm{kJ/kg}$ term is the approximate vaporization enthalpy at the reference temperature. Because $h$ is quoted per kilogram of dry air, it must be multiplied by dry-air mass flow, not total moist-air mass flow.

The specific volume per kilogram of dry air is obtained from the dry-air partial pressure:

$$
v=\frac{R_aT_K}{P-P_v}.
$$

Using the humidity-ratio relation, an equivalent form is

$$
v=\frac{R_aT_K}{P}(1+1.608\omega).
$$

This volume includes both constituents but uses only dry-air mass in its denominator. Thus a volumetric flow rate converts to dry-air mass flow as $\dot m_a=\dot V/v$.

## What the psychrometric chart encodes

A psychrometric chart is a graphical property table at fixed pressure. Dry-bulb temperature lies on the horizontal axis and humidity ratio on the vertical axis. The upper curved boundary is saturated air. Curves below it mark constant relative humidity; oblique lines usually represent nearly constant wet-bulb temperature and enthalpy; another family gives specific volume.

```text
humidity ratio
omega
|                    saturation, phi = 100%
|                ___/
|            ___/      relative-humidity curves
|        ___/
|    ___/
|___/________________________________ dry-bulb temperature
```

Any two independent properties usually locate a state once total pressure is fixed. Relative humidity and dew point are not independent if dry-bulb temperature is already given because all three determine the same $P_v$. Values read from different chart families should agree only within graphical resolution and the property correlations used to draw the chart.

| Process | Idealized chart direction | Main balance consequence |
|---|---|---|
| Sensible heating | right at constant $\omega$ | heat added, no water added |
| Sensible cooling above dew point | left at constant $\omega$ | heat removed, no condensate |
| Cooling and dehumidification | down and left | condensate leaves |
| Steam humidification | up and usually right | vapor mass and enthalpy added |
| Evaporative cooling | up and left near constant $h$ | liquid evaporates into air |
| Mixing two air streams | state lies on joining line | dry-air, water, and energy balances |

The apparent straight paths assume negligible pressure change and steady operation. A real cooling coil can have a pressure drop and may not produce a spatially uniform outlet state.

## Cooling coils and condensate bookkeeping

For a steady cooling coil with one moist-air inlet, one moist-air outlet, and liquid condensate outlet, dry air is conserved:

$$
\dot m_{a,1}=\dot m_{a,2}=\dot m_a.
$$

The water balance is

$$
\dot m_a\omega_1
=\dot m_a\omega_2+\dot m_w,
$$

so

$$
\dot m_w=\dot m_a(\omega_1-\omega_2).
$$

Neglecting fan work and kinetic and potential changes, with heat into the control volume positive,

$$
\dot Q
=\dot m_a(h_2-h_1)+\dot m_wh_f(T_w).
$$

The condensate enthalpy term follows from the chosen water reference. It is often small relative to the moist-air enthalpy change, but including it keeps the balance explicit.

### Worked example: coil load with dehumidification

Moist air enters a coil at $30{}^{\circ}\mathrm{C}$ and $50\%$ relative humidity and leaves at $15{}^{\circ}\mathrm{C}$ saturated. The dry-air flow is $1.0\ \mathrm{kg_{da}/s}$ and $P=101.325\ \mathrm{kPa}$. Use $P_{\mathrm{sat}}(30{}^{\circ}\mathrm{C})=4.246\ \mathrm{kPa}$ and $P_{\mathrm{sat}}(15{}^{\circ}\mathrm{C})=1.705\ \mathrm{kPa}$.

At the inlet,

$$
P_{v1}=0.50(4.246)=2.123\ \mathrm{kPa},
$$

$$
\omega_1=0.622\frac{2.123}{101.325-2.123}
=0.01331.
$$

The saturated outlet has

$$
\omega_2=0.622\frac{1.705}{101.325-1.705}
=0.01065.
$$

Therefore the condensate rate is

$$
\dot m_w=1.0(0.01331-0.01065)
=0.00266\ \mathrm{kg/s}.
$$

Using the moist-air enthalpy correlation,

$$
\begin{aligned}
h_1
&=1.005(30)+0.01331[2500+1.88(30)]\\
&=64.17\ \mathrm{kJ/kg_{da}},
\end{aligned}
$$

$$
\begin{aligned}
h_2
&=1.005(15)+0.01065[2500+1.88(15)]\\
&=42.00\ \mathrm{kJ/kg_{da}}.
\end{aligned}
$$

If condensate leaves at $15{}^{\circ}\mathrm{C}$, take $h_f\approx4.18(15)=62.7\ \mathrm{kJ/kg}$. Then

$$
\begin{aligned}
\dot Q
&=1.0(42.00-64.17)+0.00266(62.7)\\
&=-22.00\ \mathrm{kW}.
\end{aligned}
$$

The negative sign means heat leaves the control volume; the required cooling capacity is about $22.0\ \mathrm{kW}$. Neglecting condensate enthalpy would give $22.17\ \mathrm{kW}$, close here but not algebraically identical.

A coil surface below the inlet dew point can be partly dry and partly wet. The outlet may be unsaturated because some air effectively bypasses intimate contact with the cold surface. HVAC models often describe this with a bypass factor and an apparatus dew point rather than assuming a saturated outlet.

## Mixing two moist-air streams

For an adiabatic mixing chamber with no condensation, dry-air conservation, water conservation, and energy conservation give

$$
\dot m_{a3}=\dot m_{a1}+\dot m_{a2},
$$

$$
\dot m_{a3}\omega_3
=\dot m_{a1}\omega_1+\dot m_{a2}\omega_2,
$$

$$
\dot m_{a3}h_3
=\dot m_{a1}h_1+\dot m_{a2}h_2.
$$

Thus both $\omega_3$ and $h_3$ are dry-air-flow-weighted averages. On a chart, state 3 lies on the straight line joining states 1 and 2, and its position divides the line in the inverse ratio of the dry-air flow rates.

### Worked example: outdoor and return air

Mix $1\ \mathrm{kg_{da}/s}$ of outdoor air with $\omega_1=0.012$ and $h_1=58\ \mathrm{kJ/kg_{da}}$ with $3\ \mathrm{kg_{da}/s}$ of return air at $\omega_2=0.008$ and $h_2=42\ \mathrm{kJ/kg_{da}}$.

The total dry-air flow is

$$
\dot m_{a3}=1+3=4\ \mathrm{kg_{da}/s}.
$$

Water balance gives

$$
\omega_3
=\frac{1(0.012)+3(0.008)}{4}
=0.0090\ \mathrm{kg_v/kg_{da}}.
$$

Energy balance gives

$$
h_3
=\frac{1(58)+3(42)}{4}
=46.0\ \mathrm{kJ/kg_{da}}.
$$

The dry-bulb temperature can be recovered from the enthalpy correlation:

$$
46.0=1.005T_3+0.0090(2500+1.88T_3).
$$

Collecting terms,

$$
46.0-22.5=(1.005+0.01692)T_3,
$$

$$
T_3=\frac{23.5}{1.02192}=23.0{}^{\circ}\mathrm{C}.
$$

The result must still be checked against saturation at $23{}^{\circ}\mathrm{C}$. If the averaged state lies beyond the saturation boundary, condensation occurs and the simple no-condensation balances need a liquid-water outlet term.

## Sensible and latent loads in an HVAC process

Room loads are often divided into a sensible part associated mainly with temperature change and a latent part associated with water removal. The split is useful for equipment selection because a coil that supplies enough total cooling may still leave a space too humid if its surface temperature is too high.

For a moist-air stream whose humidity ratio remains fixed, the sensible enthalpy change is approximately

$$
\Delta h_s\approx(c_{p,a}+\omega c_{p,v})\Delta T.
$$

At ordinary humidity levels, the coefficient is close to $1.02\ \mathrm{kJ/(kg_{da}\,K)}$. A change in humidity ratio carries a much larger latent contribution, approximately

$$
\Delta h_l\approx h_{fg}\Delta\omega.
$$

Because $h_{fg}$ is around $2500\ \mathrm{kJ/kg}$ near room conditions, removing only $0.001\ \mathrm{kg}$ of vapor per kilogram of dry air requires roughly $2.5\ \mathrm{kJ/kg_{da}}$ beyond the sensible load.

The sensible heat factor is commonly defined as

$$
\mathrm{SHF}=\frac{\dot Q_s}{\dot Q_s+\dot Q_l}.
$$

It corresponds to a process-line slope on a psychrometric chart. A value near one indicates mostly temperature control; a lower value requires more dehumidification. Exact definitions vary with whether fan heat, ventilation air, and equipment gains are counted, so the boundary should accompany a reported SHF.

Summer conditioning often follows a sequence rather than one direct path. Outdoor air is mixed with return air, the mixture is cooled below its dew point to remove moisture, and the supply may then be reheated at constant humidity ratio. Reheat raises dry-bulb temperature without undoing dehumidification. It consumes energy if no recovered heat source is available, but it can be required when the latent load calls for a cold coil and the sensible load does not permit equally cold supply air.

Winter conditioning may sensibly heat cold air and then humidify it. Heating alone lowers relative humidity because saturation pressure rises while $\omega$ stays fixed. Injecting steam raises both humidity ratio and enthalpy; spraying liquid water can raise humidity while cooling the air through evaporation. Treating both methods as the same vertical chart move ignores the very different enthalpy carried by steam and liquid water.

## Wet-bulb temperature and evaporative cooling

A wetted thermometer reaches a temperature below the dry-bulb temperature when water evaporates into unsaturated air. The exact thermodynamic wet-bulb temperature is associated with adiabatic saturation: air contacts liquid water in an insulated device long enough to leave saturated, while the makeup water enters at the final temperature.

An adiabatic saturator obeys

$$
h_1+(\omega_2-\omega_1)h_f(T_2)=h_2,
$$

where state 2 is saturated. At ordinary HVAC conditions the liquid-water correction is modest, so constant wet-bulb lines lie close to constant-enthalpy lines on the chart. They are not mathematically identical. Sling-psychrometer readings also depend on ventilation, radiation, and wick condition.

Direct evaporative cooling adds water and lowers dry-bulb temperature with little change in moist-air enthalpy under the ideal adiabatic model. It cannot cool below the entering wet-bulb temperature, and it works best in dry climates. Cooling with dehumidification instead requires a surface below the dew point and removes both sensible and latent heat.

## Cooling towers as coupled air-water devices

A cooling tower exposes warm circulating water to an air stream. A small part of the water evaporates, taking energy from the remaining liquid; the air leaves warmer and more humid. The process is governed by separate dry-air, total-water, and energy balances.

Let liquid water enter at rate $\dot m_{w,in}$ and leave at $\dot m_{w,out}$, while dry air flows at $\dot m_a$. Neglecting drift droplets for the moment, the evaporated water rate is

$$
\dot m_{\mathrm{evap}}
=\dot m_a(\omega_2-\omega_1)
=\dot m_{w,in}-\dot m_{w,out}.
$$

An approximately adiabatic tower satisfies

$$
\dot m_{w,in}h_{f,in}+\dot m_a h_1
=\dot m_{w,out}h_{f,out}+\dot m_a h_2.
$$

Makeup water replaces evaporation, deliberate blowdown, and drift losses. Blowdown controls dissolved-solids concentration because evaporation removes nearly pure water while leaving salts behind. It should not be confused with the evaporation rate in the psychrometric balance.

The lowest plausible cold-water temperature is tied to the entering-air wet-bulb temperature, not its dry-bulb temperature. Tower *range* is the hot-water inlet temperature minus cold-water outlet temperature. Tower *approach* is the cold-water outlet temperature minus entering-air wet-bulb temperature. A smaller approach demands more transfer area and airflow; a zero approach would require a reversible limiting device of unbounded size.

Evaporative cooling towers may release visible plumes when warm moist exhaust mixes with colder ambient air and becomes supersaturated. The plume is condensed water droplets formed after discharge, not smoke and not necessarily tower drift. Its appearance depends on ambient state and mixing, which can be checked on a psychrometric chart by following the mixture line between exhaust and outdoor air.

## Checks before trusting a chart result

- State the total pressure. Elevation changes the relation among vapor pressure, humidity ratio, and chart position.
- Keep all moist-air enthalpies and volumes on the dry-air basis. Total moist-air mass flow is $(1+\omega)\dot m_a$.
- Sensible cooling does not remove moisture until the dew point is reached. Relative humidity rises along that constant-$\omega$ cooling path.
- Every equilibrium state must lie on or below the saturation curve. An algebraic result above it implies condensation was omitted.
- Steam injection and liquid-water evaporation have different inlet enthalpies. A water mass balance alone cannot determine their outlet temperatures.
- Chart readings, saturation tables, and empirical correlations may differ slightly. Carrying more digits than the source property data does not increase accuracy.

<div className="see-also">

See also: [gas mixtures](/physics/thermodynamics/gas-mixtures) · [refrigeration cycles](/physics/thermodynamics/refrigeration-cycles) · [control-volume mass and energy analysis](/physics/thermodynamics/control-volume-mass-and-energy-analysis) · [pure substances and property tables](/physics/thermodynamics/pure-substances-and-property-tables) · [entropy and entropy balance](/physics/thermodynamics/entropy-and-entropy-balance)

</div>
