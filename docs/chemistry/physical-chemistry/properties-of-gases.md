---
title: Properties of Gases
sidebar_position: 2
---

# Properties of Gases

Gases are unusually clean macroscopic systems because pressure, volume, temperature, and amount are tied together by equations of state. They provide a direct bridge between empirical gas laws, molecular motion, and thermodynamic derivatives.

The perfect gas is the reference model: molecules are treated as point particles with negligible intermolecular forces except during collisions. Real gases depart from that model when attractions, repulsions, and finite molecular size become important, especially at high pressure and near condensation.

## Describing a gas state

A **state variable** is a property that describes the present condition of the system. For a simple pure gas, the usual variables are pressure $p$, volume $V$, temperature $T$, and amount $n$. An **equation of state** relates them:

$$
p=f(T,V,n)
$$

The **perfect gas equation** is

$$
pV=nRT
$$

where $R=8.314462618\ \mathrm{J\ K^{-1}\ mol^{-1}}$. The molar volume is $V_m=V/n$, so the perfect gas law may also be written $pV_m=RT$.

For mixtures, the mole fraction and partial pressure of component $J$ are

$$
x_J=\frac{n_J}{\sum_K n_K},
\qquad
p_J=x_Jp
$$

when the mixture behaves perfectly. The **compressibility factor** measures deviations from perfect behavior:

$$
Z=\frac{pV_m}{RT}
$$

For a perfect gas, $Z=1$ at all pressures and temperatures. For a real gas, $Z$ may be smaller than 1 when attractions dominate and larger than 1 when repulsions dominate.

Two common real-gas equations are the virial equation and the van der Waals equation. The pressure virial form is

$$
Z=1+B'(T)p+C'(T)p^2+\cdots
$$

and the molar-volume form is

$$
Z=1+\frac{B(T)}{V_m}+\frac{C(T)}{V_m^2}+\cdots
$$

The van der Waals equation is

$$
p=\frac{RT}{V_m-b}-\frac{a}{V_m^2}
$$

where $a$ represents attractive interactions and $b$ represents excluded volume.

## The dilute-gas limit

Boyle's law, Charles's law, and Avogadro's principle combine into the perfect gas law in the low-pressure limit:

$$
pV=\mathrm{constant}\quad (n,T\ \mathrm{constant})
$$

$$
V\propto T\quad (n,p\ \mathrm{constant}),
\qquad
V\propto n\quad (p,T\ \mathrm{constant})
$$

The gas laws are limiting laws. They work well when the gas is dilute enough that the average separation between molecules is large compared with molecular dimensions and the potential energy of interaction is small compared with thermal energy.

The van der Waals equation gives a useful qualitative correction. The observed pressure is lower than the perfect-gas value because attractions reduce the impulse delivered to the walls. The accessible volume is lower than $V_m$ because molecules occupy finite space. Rearranging,

$$
\left(p+\frac{a}{V_m^2}\right)(V_m-b)=RT
$$

Critical constants follow from the inflection point of the critical isotherm:

$$
\left(\frac{\partial p}{\partial V_m}\right)_T=0,
\qquad
\left(\frac{\partial^2 p}{\partial V_m^2}\right)_T=0
$$

For the van der Waals model,

$$
V_{m,c}=3b,
\qquad
p_c=\frac{a}{27b^2},
\qquad
T_c=\frac{8a}{27Rb}
$$

Reduced variables compare a state with its critical point:

$$
p_r=\frac{p}{p_c},
\qquad
V_r=\frac{V_m}{V_{m,c}},
\qquad
T_r=\frac{T}{T_c}
$$

The principle of corresponding states says that many gases have similar reduced equations of state when expressed using these variables.

The pressure of a gas also has a mechanical interpretation that is useful throughout the subject. A gas exerts pressure because molecules transfer momentum to the container walls. Higher temperature increases the average kinetic energy and therefore increases the rate and severity of wall collisions. Larger volume lowers the collision frequency at the walls. This molecular picture is not needed to use the perfect gas equation, but it explains why the equation has the structure it does and why it fails when molecules are close enough for attractions and repulsions to matter.

Kinetic theory makes that picture quantitative. For $N$ molecules of mass $m$ in a cubic container, an elastic collision reverses the velocity component normal to a wall. Summing the momentum transfer over many randomly directed molecules gives

$$
pV=\frac{1}{3}Nm\langle c^2\rangle,
$$

where $\langle c^2\rangle$ is the mean squared molecular speed. Comparing this result with $pV=Nk_BT$ gives the mean translational kinetic energy

$$
\frac{1}{2}m\langle c^2\rangle=\frac{3}{2}k_BT.
$$

Temperature therefore fixes the average translational kinetic energy, not a single molecular speed. Molecules retain a broad Maxwell speed distribution. Three characteristic speeds are

$$
c_{mp}=\sqrt{\frac{2RT}{M}},
\qquad
\bar c=\sqrt{\frac{8RT}{\pi M}},
\qquad
c_{rms}=\sqrt{\frac{3RT}{M}},
$$

with $c_{mp}\lt \bar c\lt c_{rms}$. Here $M$ must be in $\mathrm{kg\,mol^{-1}}$ when SI units are used. Raising $T$ shifts the distribution toward higher speeds and broadens it; increasing molar mass shifts it toward lower speeds.

### Worked example: comparing molecular speeds

For nitrogen at $300\ \mathrm{K}$, take $M=28.0\ \mathrm{g\,mol^{-1}}=0.0280\ \mathrm{kg\,mol^{-1}}$. The root-mean-square speed is

$$
\begin{aligned}
c_{rms}
&=\sqrt{\frac{3RT}{M}}\\
&=\sqrt{\frac{3(8.314)(300)}{0.0280}}\\
&=517\ \mathrm{m\,s^{-1}}.
\end{aligned}
$$

For helium at the same temperature, $M=0.00400\ \mathrm{kg\,mol^{-1}}$:

$$
c_{rms}=\sqrt{\frac{3(8.314)(300)}{0.00400}}=1.37\times10^3\ \mathrm{m\,s^{-1}}.
$$

The ratio can be checked without repeating the constants:

$$
\frac{c_{rms}(\mathrm{He})}{c_{rms}(\mathrm{N_2})}
=\sqrt{\frac{M_{N_2}}{M_{He}}}
=\sqrt{7}=2.65.
$$

At equal temperature both gases have the same mean translational kinetic energy per molecule. Helium moves faster because the same average energy is carried by less mass.

## Collisions, mean free path, and transport

Molecules in a gas do not normally fly from one wall to the opposite wall without interruption. They collide with other molecules after a **mean free path**, the average distance between successive collisions. In a simple hard-sphere model, mean free path grows as pressure falls because number density falls. It also depends on collision diameter: larger molecules sweep out more collision area and collide more often.

Collision frequency links microscopic motion to chemical rate and transport. A reaction between two gas molecules requires encounters, although only a fraction have a suitable energy and orientation. Diffusion carries molecules down concentration gradients through many collisions. Viscosity carries momentum between neighboring layers. Thermal conductivity carries molecular energy. These transport processes need nonequilibrium gradients and are not determined by the equilibrium equation of state alone.

**Effusion** is escape through a hole small compared with the mean free path, so molecules pass through without a flow pattern developing in the aperture. For ideal gases at the same temperature, Graham's law gives an effusion rate inversely proportional to the square root of molar mass. The result follows because molecular flux to the hole is proportional to number density times mean speed, and mean speed varies as the inverse square root of mass.

Consider equal-pressure samples of methane and sulfur hexafluoride at the same temperature. Their molar masses are approximately 16.0 and 146.1 grams per mole. The rate ratio is

$$
\frac{r_{CH_4}}{r_{SF_6}}
=\sqrt{\frac{M_{SF_6}}{M_{CH_4}}}
=\sqrt{\frac{146.1}{16.0}}
=3.02.
$$

Methane effuses about three times as fast under the model. The calculation compares initial rates at equal pressure and temperature. It does not say that a methane sample takes exactly one third as long to empty, because pressure and rate change as a finite container empties.

Diffusion through another gas is more complicated than effusion into a vacuum. The diffusing molecule repeatedly collides with the background, and both molecular sizes and interaction forces matter. Applying Graham's square-root rule indiscriminately to liquid diffusion or high-pressure flow discards the assumptions that produced it.

## Partial pressure is a molecular count

In an ideal mixture, each species contributes pressure according to how many of its molecules occupy the common volume. Summing the species equations gives Dalton's law. The mole fraction relation then follows by dividing a component equation by the total equation. Partial pressure is therefore more than a bookkeeping definition; it is the pressure that component would exert alone at the mixture temperature and volume under ideal behavior.

Suppose a dry gas contains 2.0 moles of nitrogen, 0.50 moles of oxygen, and 0.10 moles of carbon dioxide at a total pressure of 1.04 bar. The total amount is 2.60 moles. Carbon dioxide has mole fraction $0.10/2.60=0.0385$, so its partial pressure is $0.0385\times1.04=0.0400$ bar. Nitrogen and oxygen partial pressures are found the same way, and all three must sum to 1.04 bar.

Gas collected over water needs another component in that sum. The measured total pressure contains water vapor at its equilibrium vapor pressure, so the dry gas pressure is total pressure minus water vapor pressure at the collection temperature. Forgetting that subtraction makes the inferred dry-gas amount too large.

The perfect gas law is approached as $p\to0$ because the average separation between molecules grows large. Potential-energy contributions from intermolecular forces then become negligible compared with translational kinetic energy. A real gas at ordinary laboratory pressure may be close enough to ideal for rough stoichiometry, but precision thermodynamics uses fugacity or measured equations of state. The virial equation is especially valuable because each coefficient carries information about molecular interactions: the second virial coefficient reflects pair interactions, the third includes three-body effects, and so on.

The sign of the second virial coefficient is physically meaningful. If attractions dominate at a given temperature, $B(T)$ is negative and $Z\lt 1$ at sufficiently low density: the gas pressure is lower than the perfect-gas value because molecules are pulled slightly back from the wall by neighboring molecules. If repulsions dominate, $B(T)$ is positive and $Z\gt 1$: finite molecular size and short-range repulsion raise the pressure. The Boyle temperature is the temperature at which $B(T)=0$, so a real gas obeys the perfect gas law unusually well over a wider low-pressure range, even though higher virial terms still remain.

The van der Waals equation should be read as a model rather than a high-accuracy correlation. Its attraction parameter $a$ lowers pressure by an amount proportional to concentration squared, because attractions depend on pair encounters. Its excluded-volume parameter $b$ reduces the volume available for molecular translation. These two corrections are enough to predict liquid-vapor loops and a critical point, which the perfect gas law cannot do. However, near the critical point real fluids show fluctuation behavior that the simple mean-field van der Waals model cannot capture quantitatively.

Critical phenomena matter because above $T_c$ a gas cannot be liquefied by pressure alone. Below $T_c$, compression can produce a two-phase liquid-vapor region; at $T_c$, the distinction between liquid and gas disappears. Supercritical fluids combine high density with transport properties closer to gases, which is why they are useful in extraction and materials processing. In the language of phase diagrams, the critical point is the endpoint of a coexistence curve; in the language of equations of state, it is the point where an isotherm has a horizontal inflection.

Gas mixtures introduce another layer of idealization. Dalton's law assumes each gas contributes to the total pressure as if it occupied the container alone at the same temperature. This is reliable for low-pressure mixtures because molecular identity barely affects translational pressure. In real mixtures, unlike interactions can be different from like interactions, so activity or fugacity replaces partial pressure in accurate equilibrium work. Even then, the perfect-gas partial pressure remains the reference concept for defining standard states and reaction quotients.

The same equation can look different depending on whether $R$ is expressed in $\mathrm{J\ K^{-1}\ mol^{-1}}$, $\mathrm{L\ bar\ K^{-1}\ mol^{-1}}$, or $\mathrm{L\ atm\ K^{-1}\ mol^{-1}}$. Real-gas constants $a$ and $b$ are also unit-dependent. Many numerical errors are unit mismatches, especially when pressure is converted between pascals, bar, atmospheres, torr, and millimeters of mercury.

## Choosing an equation of state

| Model or quantity | Main equation | Best use | Limitation |
|---|---:|---|---|
| Perfect gas | $pV=nRT$ | Dilute gases, reference states | Ignores attractions and molecular size |
| Dalton mixture | $p_J=x_Jp$ | Gas mixtures at low pressure | Fails when mixture nonideality is strong |
| Compressibility factor | $Z=pV_m/RT$ | Measures real-gas deviation | Descriptive unless paired with model/data |
| Virial equation | $Z=1+B/V_m+C/V_m^2+\cdots$ | Accurate empirical corrections | Coefficients depend on $T$ and gas identity |
| van der Waals | $p=RT/(V_m-b)-a/V_m^2$ | Qualitative real-gas physics, criticality | Quantitatively rough near critical point |

```mermaid
graph LR
  A["Gas state variables"] --> B["Perfect gas law"]
  B --> C["Partial pressures"]
  B --> D["Reference for real gases"]
  D --> E["Compressibility factor Z"]
  E --> F["Virial equation"]
  E --> G["van der Waals model"]
  G --> H["Critical constants"]
  H --> I["Reduced variables"]
```

## Worked example: pressure from a liquid column

A mercury barometer has a column of height $760.0\ \mathrm{mm}$ at a place where $g=9.80665\ \mathrm{m\ s^{-2}}$. Mercury has density $13.595\ \mathrm{g\ cm^{-3}}$. Calculate the pressure in pascals and atmospheres.

The pressure at the base of a liquid column is its weight per area:

$$
p=\rho gh
$$

1. Convert density:

$$
\rho=13.595\ \mathrm{g\ cm^{-3}}
=13.595\times 10^3\ \mathrm{kg\ m^{-3}}
$$

2. Convert height:

$$
h=760.0\ \mathrm{mm}=0.7600\ \mathrm{m}
$$

3. Substitute:

$$
\begin{aligned}
p&=(13.595\times 10^3\ \mathrm{kg\ m^{-3}})
(9.80665\ \mathrm{m\ s^{-2}})
(0.7600\ \mathrm{m})\\
&=1.0132\times 10^5\ \mathrm{Pa}
\end{aligned}
$$

4. Convert to atmospheres:

$$
\frac{1.0132\times 10^5\ \mathrm{Pa}}{101325\ \mathrm{Pa\ atm^{-1}}}
=0.9999\ \mathrm{atm}
$$

The pressure is essentially $1.013\times 10^5\ \mathrm{Pa}=1.000\ \mathrm{atm}$. This agrees with the conventional relation between $760\ \mathrm{mmHg}$ and one atmosphere; the small numerical difference comes from the stated mercury density.

## Worked example: real-gas pressure with van der Waals corrections

Estimate the pressure of $1.000\ \mathrm{mol}$ of $\mathrm{CO_2}$ in a $1.000\ \mathrm{L}$ vessel at $300.0\ \mathrm{K}$ using the perfect gas equation and the van der Waals equation. Use $a=3.592\ \mathrm{L^2\ bar\ mol^{-2}}$ and $b=0.04267\ \mathrm{L\ mol^{-1}}$.

For $n=1$, $V_m=1.000\ \mathrm{L\ mol^{-1}}$. Use $R=0.08314\ \mathrm{L\ bar\ K^{-1}\ mol^{-1}}$.

1. Perfect gas pressure:

$$
\begin{aligned}
p_{\mathrm{ideal}}
&=\frac{RT}{V_m}\\
&=\frac{(0.08314)(300.0)}{1.000}\\
&=24.94\ \mathrm{bar}
\end{aligned}
$$

2. Excluded-volume term:

$$
\frac{RT}{V_m-b}
=\frac{(0.08314)(300.0)}{1.000-0.04267}
=\frac{24.94}{0.95733}
=26.05\ \mathrm{bar}
$$

3. Attraction correction:

$$
\frac{a}{V_m^2}
=\frac{3.592}{(1.000)^2}
=3.592\ \mathrm{bar}
$$

4. van der Waals pressure:

$$
p=26.05-3.592=22.46\ \mathrm{bar}
$$

5. Compressibility factor:

$$
Z=\frac{pV_m}{RT}
=\frac{(22.46)(1.000)}{24.94}
=0.901
$$

The real-gas estimate is $22.5\ \mathrm{bar}$, lower than the ideal value because attractions dominate at this state. The result $Z\lt 1$ confirms that interpretation. At still smaller volume, the excluded-volume term grows sharply and can instead make $Z\gt 1$.

## Sampling an isotherm numerically

The van der Waals terms compete as volume changes, so a short calculation is more informative than evaluating only one state. Values near or below $b$ are excluded because the model's available volume vanishes there.

```python
import numpy as np

R = 0.08314  # L bar K^-1 mol^-1
a = 3.592   # CO2, L^2 bar mol^-2
b = 0.04267 # CO2, L mol^-1
T = 300.0

Vm = np.linspace(0.08, 5.0, 200)
p_ideal = R * T / Vm
p_vdw = R * T / (Vm - b) - a / Vm**2
Z_vdw = p_vdw * Vm / (R * T)

for volume in [0.5, 1.0, 2.0, 5.0]:
    p = R * T / (volume - b) - a / volume**2
    z = p * volume / (R * T)
    print(f"Vm={volume:4.1f} L/mol  p={p:7.2f} bar  Z={z:6.3f}")
```

## Limits and unit checks

- Treating $pV=nRT$ as exact for all gases. It is a limiting model; check pressure, temperature, and phase proximity.
- Forgetting that $V_m$ in van der Waals equations is molar volume. If using total volume, use the $n$-dependent form.
- Mixing pressure units inside $R$. Use $8.314\ \mathrm{J\ K^{-1}\ mol^{-1}}$ with pascals and cubic meters, or $0.08314\ \mathrm{L\ bar\ K^{-1}\ mol^{-1}}$ with liters and bar.
- Interpreting $a$ and $b$ as universal constants. They depend on the gas.
- Assuming $Z\lt 1$ always means a gas is "more ideal." It means attractions reduce pressure relative to the perfect-gas value at that state.

<div className="see-also">

See also: [General chemistry gases](/chemistry/general/gases) · [First law and thermochemistry](/chemistry/physical-chemistry/first-law-and-thermochemistry) · [Phase transitions and phase diagrams](/chemistry/physical-chemistry/phase-transitions-and-phase-diagrams) · [molecular interactions and transport](/chemistry/physical-chemistry/molecular-interactions-and-transport)

</div>
