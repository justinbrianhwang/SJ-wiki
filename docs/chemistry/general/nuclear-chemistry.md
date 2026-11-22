---
title: Nuclear Chemistry
sidebar_position: 21
---

# Nuclear Chemistry

Chemical reactions rearrange valence electrons while leaving nuclei intact. Nuclear reactions change proton or neutron counts and can turn one element into another. Their energy scale is much larger because nuclear binding changes a measurable amount of rest mass. The governing bookkeeping is still compact: conserve charge, nucleon number, energy, and momentum.

## Nuclides and the valley of stability

A nuclide is written $^A_Z\mathrm{X}$, where $Z$ is the proton count and identifies the element, $A$ is the mass number, and $A-Z$ is the neutron count. Isotopes have the same $Z$ but different $A$. The notation records the nucleus; an ionic charge, if relevant, belongs at the upper right and does not alter $A$ or $Z$.

Nuclear stability reflects a competition. The strong nuclear force attracts nearby nucleons over a short range, while electrostatic repulsion acts between every pair of protons. Light stable nuclei tend to have roughly equal proton and neutron counts. Heavier stable nuclei need a growing neutron excess: neutrons contribute strong-force attraction without adding proton–proton repulsion. Very large nuclei remain vulnerable despite that excess.

Even–even nuclei are especially common among stable nuclides, while odd–odd stable combinations are rare. Such patterns guide expectations but do not replace measured nuclear data. “Stable” also means no decay has been observed on the relevant timescale, not that a nucleus has no internal energy.

## Decay modes repair different imbalances

| Process | Emitted or captured particle | Change in $A$ | Change in $Z$ |
|---|---|---:|---:|
| alpha emission | $^4_2\mathrm{He}$ | $-4$ | $-2$ |
| beta-minus emission | $^0_{-1}\mathrm{e}$ | $0$ | $+1$ |
| positron emission | $^0_{+1}\mathrm{e}$ | $0$ | $-1$ |
| electron capture | $^0_{-1}\mathrm{e}$ on reactant side | $0$ | $-1$ |
| gamma emission | $\gamma$ | $0$ | $0$ |

Alpha decay is common for very heavy nuclei. It reduces both nuclear size and charge, producing a daughter two places to the left in the periodic table. In beta-minus decay, a neutron becomes a proton while an electron and antineutrino are emitted. The daughter therefore has the same mass number and atomic number one larger. Positron emission converts a proton to a neutron and emits a positron plus a neutrino. Electron capture has the same effect on $A$ and $Z$: a nuclear proton captures an inner electron and becomes a neutron.

Gamma emission changes neither proton nor neutron count. An excited nucleus releases a high-energy photon and moves to a lower nuclear energy level. Gamma radiation often follows another decay that leaves the daughter excited.

Neutrinos are needed for energy, momentum, and angular-momentum conservation in beta processes, even though elementary balancing exercises often omit them. Nuclear equations that balance only $A$ and $Z$ are necessary bookkeeping, not a complete reaction description.

### Worked example: identifying a decay product

Suppose $^{238}_{92}\mathrm{U}$ undergoes alpha decay. Subtract the alpha particle's mass and atomic numbers:

$$
A_d=238-4=234,
$$

$$
Z_d=92-2=90.
$$

Element 90 is thorium, so

$$
^{238}_{92}\mathrm{U}\rightarrow{}^{234}_{90}\mathrm{Th}+{}^4_2\mathrm{He}.
$$

Both sides total 238 nucleons and charge number 92. If the thorium nucleus is produced excited, a later gamma photon may appear without changing its nuclide label.

### Worked example: completing a bombardment equation

Consider

$$
^{14}_7\mathrm{N}+{}^4_2\mathrm{He}\rightarrow{}^{17}_8\mathrm{O}+{}^A_Z\mathrm{X}.
$$

The reactants total $A=18$ and $Z=9$. The known oxygen product accounts for 17 and 8, leaving

$$
A=18-17=1,\qquad Z=9-8=1.
$$

The missing particle is a proton:

$$
^{14}_7\mathrm{N}+{}^4_2\mathrm{He}\rightarrow{}^{17}_8\mathrm{O}+{}^1_1\mathrm{p}.
$$

Matching only mass numbers would not distinguish a proton from a neutron; charge balance supplies the identity.

## Why radioactive decay is exponential

An unstable nucleus has a constant probability per unit time of decaying. For a large population, the expected rate of loss is proportional to the number still present:

$$
\frac{dN}{dt}=-\lambda N.
$$

Separating variables and integrating from $N_0$ at time zero to $N$ at time $t$ gives

$$
\int_{N_0}^{N}\frac{dN'}{N'}=-\lambda\int_0^t dt',
$$

and hence

$$
N=N_0e^{-\lambda t}.
$$

At the half-life, $N/N_0=1/2$:

$$
t_{1/2}=\frac{\ln 2}{\lambda}.
$$

Equal time intervals remove equal fractions, not equal numbers. Individual nuclear decays remain unpredictable; the exponential law describes a population.

Activity is the decay rate magnitude,

$$
\mathcal A=\lambda N.
$$

Its SI unit, the becquerel, is one decay per second. Because $\lambda$ is constant for a given nuclide, activity and number of parent nuclei fall by the same fractional factor. Count rate from a detector is related to activity but also depends on geometry, detection efficiency, shielding, and background.

### Worked example: elapsed time from a remaining fraction

A sample has half-life $12.0\ \mathrm{h}$. After $36.0\ \mathrm{h}$, three half-lives have passed, so

$$
\frac{N}{N_0}=\left(\frac12\right)^3=0.125.
$$

Thus 12.5 percent remains. For a noninteger number of half-lives, use logarithms. If 30.0 percent remains,

$$
\lambda=\frac{0.693}{12.0\ \mathrm{h}}=0.0578\ \mathrm{h^{-1}},
$$

then

$$
t=-\frac{\ln(0.300)}{0.0578\ \mathrm{h^{-1}}}=20.8\ \mathrm{h}.
$$

The half-life is independent of starting mass. A larger sample has greater initial activity because it contains more nuclei, not because its nuclei decay faster.

## Mass defect and binding energy

A bound nucleus has less mass than its separated protons and neutrons. Define the mass defect as

$$
\Delta m=Zm_p+(A-Z)m_n-m_{\text{nucleus}}.
$$

The corresponding binding energy is

$$
E_b=\Delta mc^2.
$$

When atomic masses are used, electron masses must be handled consistently. A convenient conversion is that one atomic mass unit of mass difference corresponds to about $931.5\ \mathrm{MeV}$ of energy. Binding energy per nucleon, $E_b/A$, allows nuclei of different sizes to be compared.

The curve of binding energy per nucleon rises steeply among light nuclei, reaches a broad maximum near the iron–nickel region, and then declines slowly for heavy nuclei. Reactions release energy when products are more tightly bound overall. Light nuclei can move upward by fusion; very heavy nuclei can move upward by fission.

For any nuclear reaction, one may calculate a $Q$ value:

$$
Q=(m_{\text{reactants}}-m_{\text{products}})c^2.
$$

A positive $Q$ means rest-mass energy is released as kinetic energy or radiation. A negative $Q$ means at least that much energy must be supplied, with momentum conservation sometimes raising the projectile threshold above $\vert Q\vert $.

## Fission, fusion, and chain behavior

Fission splits a heavy nucleus into medium-mass fragments, usually with neutrons and gamma radiation. Neutron-induced fission can release additional neutrons, producing a chain reaction. Whether the neutron population shrinks, remains steady, or grows depends on leakage and absorption as well as neutron production. A reactor maintains controlled criticality; a rapidly supercritical assembly behaves very differently.

Fusion joins light nuclei. The products may be more tightly bound, but positively charged reactants must approach closely enough for the strong force to act. Their Coulomb repulsion creates a large barrier. High temperature supplies kinetic energy, while quantum tunneling allows some collisions to react even below the classical barrier. Favorable reaction energy does not imply an easy laboratory rate.

Chemical combustion and nuclear energy both obey energy conservation, but their sources differ. Combustion changes electronic binding. Fission and fusion change nuclear binding and thus release far more energy per reacting particle.

## Radiation, shielding, and dose

Activity alone is not a hazard measure. Alpha particles lose energy over short distances and are stopped by outer dead skin, yet an alpha emitter taken into the body can deposit energy intensely in nearby tissue. Beta particles travel farther and may require low-atomic-number shielding to limit secondary radiation. Gamma rays are penetrating photons and require substantial dense shielding. Neutrons are uncharged and are slowed effectively by collisions with light nuclei, often using hydrogen-rich materials.

Absorbed dose measures energy deposited per unit mass; equivalent and effective dose apply weighting for radiation type and tissue sensitivity. Exposure time, distance, shielding, chemical form, and biological retention all matter. A short half-life can mean high activity for a fixed number of atoms, but it may also mean the material disappears rapidly. No single half-life ranking gives total risk.

## Common bookkeeping failures

- Balance $A$ and $Z$ independently. Chemical coefficients or ionic charges cannot substitute for either nuclear total.
- Put electron capture on the reactant side. Beta-minus and positron particles belong on the product side.
- Do not interpret half-life as the time when every atom has decayed. Exponential decay approaches zero continuously in the population model.
- Keep mass units consistent before applying $E=mc^2$. Atomic mass units pair naturally with the MeV conversion; kilograms give joules.
- Separate thermodynamic permission from reaction rate. Fusion can release energy while still requiring extreme conditions to overcome its kinetic barrier.

## Decay chains and secular equilibrium

A radioactive daughter may itself be unstable, producing a decay chain rather than one isolated step. Each link has its own decay constant. The daughter population initially grows from parent decay while simultaneously being depleted by its own decay. If the parent half-life is much longer than the daughter's, the daughter can approach secular equilibrium: its activity becomes approximately equal to the parent's even though their atom counts differ greatly. Removing the daughter breaks that balance; it grows back as the parent continues to decay.

Branching complicates the chain when one nuclide has several decay modes. Branching fractions specify the probability of each route and sum to one. A partial half-life for a branch is not the same as the nuclide's total half-life; decay constants for independent routes add. These ideas matter when predicting daughter yields or radiation spectra.

Radioactive dating compares a parent, a daughter, or an isotope ratio with an assumed initial condition. The clock starts when the system becomes closed to the relevant species. Heating, weathering, or biological exchange can reset or disturb it. The exponential calculation may be precise while the age is wrong if closure and initial composition are poorly justified.

Nuclear reactions must also conserve momentum. A single excited nucleus cannot generally emit all its energy as one massive particle without recoil. Gamma emission gives the daughter a small recoil momentum, so photon energy is slightly below the full level spacing. Such corrections are usually negligible in introductory bookkeeping but explain why energy conservation involves the complete set of products.

Artificial transmutation uses projectiles to create nuclides absent or rare in nature. Charged projectiles face a Coulomb barrier, while neutrons can enter nuclei without electrostatic repulsion. The product may immediately emit particles or gamma rays, and its identity follows from the same $A$ and $Z$ balances. Cross section describes reaction probability for a specified projectile energy; it is an effective area, not a geometric nuclear size. Resonances can make the probability vary sharply with energy.

## Interpreting nuclear data

Atomic masses already include electron masses, whereas nuclear masses do not. Reaction calculations must use one convention consistently. When neutral atomic masses are used for beta decay, electron bookkeeping is often implicitly included; mixing them with bare-particle masses can add or omit an electron mass. Significant figures matter because the energy comes from subtracting nearly equal masses.

Nuclear stability and chemical toxicity are separate. An isotope's chemistry controls where it travels in an organism or environment, while its nuclear properties control radiation and decay rate. Isotopes of one element undergo nearly identical ordinary chemistry but can differ greatly in radiological behavior.

<div className="see-also">

See also: [quantum theory of atoms](/chemistry/general/quantum-theory-of-atoms) · [chemical kinetics](/chemistry/general/chemical-kinetics) · [thermodynamics and free energy](/chemistry/general/thermodynamics-and-free-energy) · [main-group elements](/chemistry/general/main-group-elements)

</div>
