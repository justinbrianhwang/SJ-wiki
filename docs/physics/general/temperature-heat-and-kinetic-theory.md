---
title: Temperature, Heat, and Kinetic Theory
sidebar_position: 14
---

# Temperature, Heat, and Kinetic Theory

Temperature labels a thermal state. Heat labels energy crossing a system boundary because of a temperature difference. Internal energy belongs to the system; heat does not remain inside it as a stored substance. That distinction is old but still useful: once energy has entered a body, it contributes to microscopic kinetic and potential energies and is counted as internal energy.

Kinetic theory supplies a mechanical interpretation for an ideal gas. Pressure comes from molecular impacts on container walls, and absolute temperature measures the mean translational kinetic energy per molecule. Calorimetry works at the macroscopic level, without needing to follow any molecule.

## Thermal equilibrium and temperature scales

The zeroth law states that if systems $A$ and $B$ are each in thermal equilibrium with system $C$, then $A$ and $B$ are in thermal equilibrium with each other. It licenses the use of a thermometer: $C$ is the thermometer, and its reproducible property establishes a temperature reading.

For gas laws and microscopic formulas, temperature must be absolute. The Celsius and kelvin scales are related by

$$
T(\mathrm K)=T({}^\circ\mathrm C)+273.15.
$$

A temperature interval has the same numerical value on both scales, so a rise of $20{}^\circ\mathrm C$ is a rise of $20\,\mathrm K$. A ratio such as $T_2/T_1$ requires kelvins. Saying that $40{}^\circ\mathrm C$ is twice as hot as $20{}^\circ\mathrm C$ has no thermodynamic meaning; the corresponding absolute temperatures are $313.15\,\mathrm K$ and $293.15\,\mathrm K$.

Temperature changes also alter dimensions. For a homogeneous solid over a modest range,

$$
\Delta L=\alpha_L L_0\Delta T,
$$

where $\alpha_L$ is the coefficient of linear expansion. An isotropic solid has approximate volume coefficient $\beta\approx3\alpha_L$. Expansion joints and bimetallic strips exploit this effect. A hole in a uniformly heated plate expands as though it were made of the plate material; it does not shrink inward.

## Tracking energy through heating and phase changes

For a body that stays in one phase and has nearly constant specific heat $c$,

$$
Q=mc\Delta T.
$$

More generally,

$$
Q=m\int_{T_1}^{T_2}c(T)\,dT.
$$

Specific heat depends on the substance and, for gases, on the process constraint. The molar heat capacities of an ideal gas satisfy $C_P-C_V=R$. Heating at constant pressure requires more energy per kelvin because the expanding gas also does boundary work.

During a first-order phase change of a pure substance at fixed pressure, energy can enter while temperature stays at the saturation value:

$$
Q=mL.
$$

$L_f$ denotes latent heat of fusion and $L_v$ latent heat of vaporization. The energy changes molecular organization rather than the mean translational kinetic energy. A calculation that crosses a phase boundary must be split into stages.

| Stage | Energy term | What changes |
|---|---|---|
| One phase, no transition | $mc\Delta T$ | temperature |
| Melting or freezing | $mL_f$ | phase fraction |
| Vaporizing or condensing | $mL_v$ | phase fraction |
| Variable specific heat | $m\int c(T)dT$ | temperature |

In an isolated calorimeter, the algebraic sum of heat transfers is zero:

$$
\sum_i Q_i=0.
$$

Objects that cool have negative $Q$ under the convention that heat into an object is positive. The calorimeter itself may need a term $C_{cal}\Delta T$. Ignoring it amounts to assuming a perfectly insulating container with negligible heat capacity.

### Worked example: warm water and melting ice

Place $0.100\,\mathrm{kg}$ of ice at $0{}^\circ\mathrm C$ into $0.500\,\mathrm{kg}$ of water at $30{}^\circ\mathrm C$ in an ideal insulated container. Use $c_w=4186\,\mathrm{J/(kg\,K)}$ and $L_f=3.34\times10^5\,\mathrm{J/kg}$. Find the final state.

First ask whether the warm water can melt all the ice. If it cools to $0{}^\circ\mathrm C$, it releases

$$
|Q_w|=m_wc_w(30-0)
=(0.500)(4186)(30)
=62{,}790\,\mathrm J.
$$

Melting all the ice requires

$$
Q_m=m_iL_f
=(0.100)(3.34\times10^5)
=33{,}400\,\mathrm J.
$$

There is enough energy to melt all the ice, leaving

$$
Q_{left}=62{,}790-33{,}400=29{,}390\,\mathrm J
$$

to warm the resulting $0.600\,\mathrm{kg}$ of liquid water. Its final temperature satisfies

$$
29{,}390=(0.600)(4186)(T_f-0),
$$

so

$$
T_f=\frac{29{,}390}{2511.6}=11.7{}^\circ\mathrm C.
$$

The intermediate energy check matters. If the warm water had released less than $33.4\,\mathrm{kJ}$ on reaching zero, the final state would have contained both ice and water at $0{}^\circ\mathrm C$ rather than liquid at a negative or positive temperature.

## How heat crosses a boundary

Conduction transfers energy through microscopic interactions. For steady one-dimensional conduction through a slab,

$$
\frac{Q}{\Delta t}=kA\frac{T_h-T_c}{L},
$$

where $k$ is thermal conductivity. The minus sign in Fourier's vector law, $\mathbf q=-k\nabla T$, says that heat flux points down the temperature gradient.

Convection is transfer between a surface and a moving fluid. A common empirical model is

$$
\frac{Q}{\Delta t}=hA(T_s-T_\infty),
$$

with $h$ dependent on geometry and flow. Thermal radiation requires no material medium. An idealized surface exchanges net radiative power

$$
P=\epsilon\sigma A(T_s^4-T_{sur}^4).
$$

Absolute temperatures are essential in the fourth-power law. Real cooling problems often involve all three mechanisms, so the slowest thermal resistance can dominate the overall rate.

## From molecular impacts to the ideal-gas law

Consider $N$ molecules of mass $m$ in a cube of side $L$. A molecule with velocity component $v_x$ reverses that component in an elastic collision with the wall, transferring momentum $2mv_x$. It returns to the same wall after time $2L/\vert v_x\vert $, so its average force contribution is $mv_x^2/L$. Summing molecules and dividing by wall area $L^2$ gives

$$
P=\frac{m}{V}\sum_i v_{x,i}^2.
$$

For an isotropic equilibrium gas,

$$
\langle v_x^2\rangle=\langle v_y^2\rangle=\langle v_z^2\rangle
=\frac13\langle v^2\rangle.
$$

Hence

$$
PV=\frac13Nm\langle v^2\rangle.
$$

Comparing this result with $PV=Nk_BT$ yields

$$
\frac12m\langle v^2\rangle=\frac32k_BT.
$$

The left side is the mean translational kinetic energy per molecule. It depends only on temperature, not molecular mass. The root-mean-square speed is

$$
v_{rms}=\sqrt{\langle v^2\rangle}=\sqrt{\frac{3k_BT}{m}}
=\sqrt{\frac{3RT}{M}},
$$

where $M$ is molar mass in kilograms per mole. At equal temperature, lighter molecules have greater rms speed even though both gases have the same mean translational energy.

The ideal-gas equation

$$
PV=nRT
$$

describes dilute gases whose intermolecular forces and molecular volumes are negligible for the question at hand. For a fixed amount between equilibrium states,

$$
\frac{P_1V_1}{T_1}=\frac{P_2V_2}{T_2}.
$$

It is an equation of state, not a process law. It connects properties at each state but does not specify heat, work, or the path between them.

### Worked example: simultaneous compression and heating

An ideal gas starts at $P_1=1.0\,\mathrm{atm}$, $V_1=3.0\,\mathrm L$, and $T_1=300\,\mathrm K$. It ends at $V_2=1.5\,\mathrm L$ and $T_2=360\,\mathrm K$. For fixed $n$,

$$
P_2=P_1\frac{V_1}{V_2}\frac{T_2}{T_1}.
$$

Substitution gives

$$
P_2=(1.0)\left(\frac{3.0}{1.5}\right)
\left(\frac{360}{300}\right)
=2.4\,\mathrm{atm}.
$$

Compression alone would double the pressure at constant temperature; heating multiplies it by another factor of $1.2$.

### Worked example: comparing molecular speeds

Find $v_{rms}$ for nitrogen at $300\,\mathrm K$, taking $M=0.0280\,\mathrm{kg/mol}$ and $R=8.314\,\mathrm{J/(mol\,K)}$.

$$
v_{rms}=\sqrt{\frac{3RT}{M}}
=\sqrt{\frac{3(8.314)(300)}{0.0280}}.
$$

The quantity under the square root is

$$
\frac{7482.6}{0.0280}=2.672\times10^5\,\mathrm{m^2/s^2},
$$

so

$$
v_{rms}=517\,\mathrm{m/s}.
$$

This is not the mean speed or the most probable speed; the Maxwell distribution assigns different values to each. It is the square root of the mean squared speed, the quantity that appears naturally in the pressure derivation.

## Internal energy and degrees of freedom

Equipartition assigns an average energy $\frac12k_BT$ to each independent quadratic term in the classical molecular energy. A monatomic ideal gas has three translational quadratic terms, giving

$$
U=\frac32Nk_BT=\frac32nRT.
$$

A rotating diatomic molecule can acquire two additional active rotational degrees of freedom, leading over a suitable temperature range to $U\approx\frac52nRT$. Vibrational modes contribute only when thermal energy is high enough to excite them appreciably; quantum energy spacing suppresses them at lower temperature. Therefore $U=\frac32nRT$ is specific to a monatomic ideal gas, not to every ideal gas.

Temperature is intensive while internal energy is extensive. Two equal samples at the same temperature have the same temperature but twice the combined internal energy of either sample. Likewise, an object can have a higher temperature yet less total internal energy than a cooler, much larger object.

## Molecular distributions, not a single molecular speed

The rms speed does not mean every molecule travels at that speed. Equilibrium gas molecules occupy a broad Maxwell speed distribution. Collisions continually exchange energy, leaving some molecules slow and a smaller population much faster than the mean. The distribution becomes broader and shifts toward higher speed as temperature rises.

Three characteristic speeds are commonly distinguished. The most probable speed lies at the peak of the speed distribution, the mean speed is the arithmetic average of molecular speed, and the rms speed weights fast molecules more strongly because speed is squared before averaging. For a classical ideal gas they satisfy

$$
v_{mp}=\sqrt{\frac{2RT}{M}},\qquad
\bar v=\sqrt{\frac{8RT}{\pi M}},\qquad
v_{rms}=\sqrt{\frac{3RT}{M}}.
$$

Their order is $v_{mp}\lt\bar v\lt v_{rms}$. Pressure involves the mean of $v^2$, so rms speed is the natural quantity in the kinetic-theory derivation. Effusion through a tiny hole samples the faster molecules preferentially because they strike the opening more often.

Diffusion and effusion also show why equal temperature does not erase mass differences. In the idealized effusion limit, the rate scales approximately as $1/\sqrt M$. A lighter gas escapes faster than a heavier gas at the same temperature. This relation assumes a hole smaller than the mean free path and negligible collisions within the opening; bulk flow through a pipe is a different regime.

The mean free path is the typical distance between molecular collisions. Dilute gases have long mean free paths compared with molecular size, supporting the point-particle idealization. At high pressure the path shortens, molecular volume matters, and attractive interactions influence pressure. Condensation is a direct failure of a model that neglects attraction.

## Thermal response depends on the path

An ideal gas has internal energy depending only on temperature, but heat supplied is not determined by temperature change alone. The first law,

$$
\Delta U=Q-W,
$$

uses $W$ as work done by the gas. At constant volume, boundary work vanishes, so heating gives $Q_V=\Delta U=nC_V\Delta T$. At constant pressure, the gas expands and does work $P\Delta V=nR\Delta T$, giving

$$
Q_P=nC_P\Delta T=n(C_V+R)\Delta T.
$$

The same initial and final temperatures therefore produce the same internal-energy change but can require different heat transfers. Heat capacity is partly a statement about the process constraint.

For a monatomic ideal gas, equipartition gives $C_V=\frac32R$ and $C_P=\frac52R$. The ratio $\gamma=C_P/C_V=5/3$ enters adiabatic gas relations and sound speed. A diatomic gas over an ordinary temperature range has active rotational modes and an approximate ratio closer to $7/5$. These values change when vibrational modes become populated or when the gas ceases to behave ideally.

### Worked comparison: constant volume and constant pressure

One mole of a monatomic ideal gas is heated from $300$ K to $400$ K. At constant volume,

$$
Q_V=nC_V\Delta T
=(1)\left(\frac32R\right)(100)
=1.25\ \text{kJ}.
$$

The work is zero and $\Delta U=1.25$ kJ. At constant pressure,

$$
Q_P=nC_P\Delta T
=(1)\left(\frac52R\right)(100)
=2.08\ \text{kJ}.
$$

The internal-energy change remains $1.25$ kJ. The difference is boundary work:

$$
W=Q_P-\Delta U=0.831\ \text{kJ},
$$

equal to $nR\Delta T$. Temperature alone fixes $\Delta U$ for the ideal gas, while the mechanical constraint fixes how the energy crosses the boundary.

## Thermal time scales and lumped models

Calorimetry equations compare equilibrium states and contain no rate. A metal block may eventually reach the surrounding temperature, but conduction within it and convection at its surface determine how long that takes. Treating the whole block as having one uniform temperature is a lumped-capacitance approximation. It works when internal conduction is fast relative to surface heat transfer; otherwise a temperature field develops inside the body.

Newton's cooling model writes

$$
mc\frac{dT}{dt}=-hA(T-T_\infty).
$$

With constant properties and surroundings, integration gives exponential approach:

$$
T(t)-T_\infty=(T_0-T_\infty)e^{-hAt/(mc)}.
$$

The object never crosses the surrounding temperature under this simple model. Radiation, changing convection, phase changes, and spatial gradients can all spoil the single exponential. The formula is a rate model, unlike $Q=mc\Delta T$, which is an endpoint energy relation.

Thermal equilibrium is also local before it is global. A rapidly heated solid can have a hot surface and cool interior, so assigning one temperature to the entire object is an approximation. Thermometers have their own response time and perturb small systems by exchanging energy with them. A reported temperature therefore presumes both a calibration scale and sufficient equilibration at the measurement location.

## Model limits and sign checks

- Use kelvins in gas-law ratios, rms-speed formulas, and radiation laws. Celsius intervals are safe only for differences.
- Before applying $Q=mc\Delta T$, check whether the path crosses a phase boundary and whether $c$ varies enough to require integration.
- Latent heat may be released as well as absorbed. Freezing and condensation have negative $Q$ for the substance under the heat-in-positive convention.
- A calorimetry result outside the assumed phase range signals a missing stage rather than an exotic final temperature.
- The ideal-gas law becomes inaccurate at high density and near condensation, where molecular size and attraction matter.
- Equal molecular kinetic energy at equal temperature does not mean equal molecular speed.
- Heat and temperature are not interchangeable units or concepts: heat is measured in joules, temperature in kelvins.

<div className="see-also">

See also: [First Law, Entropy, and Second Law](/physics/general/first-law-entropy-and-second-law) · [Fluids: Statics, Dynamics, and Bernoulli](/physics/general/fluids-statics-dynamics-and-bernoulli) · [Pure Substances and Property Tables](/physics/thermodynamics/pure-substances-and-property-tables) · [Classical Ideal Gas and Maxwell Distribution](/physics/statistical-mechanics/classical-ideal-gas-and-maxwell-distribution)

</div>
