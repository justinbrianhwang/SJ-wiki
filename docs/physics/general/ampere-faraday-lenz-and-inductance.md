---
title: Ampere, Faraday, Lenz, and Inductance
sidebar_position: 21
---

# Ampere, Faraday, Lenz, and Inductance

Currents produce magnetic fields, and changing magnetic flux produces electric fields. Ampere's law is most useful when current geometry supplies enough symmetry; Faraday's law handles induction; Lenz's law fixes the direction required by energy conservation. Together they replace the electrostatic picture of conservative electric fields with a dynamical one in which electric and magnetic fields create each other.

## When Ampere's law determines the field

For steady currents,

$$
\oint \vec B\cdot d\vec l=\mu_0 I_{\mathrm{enc}}.
$$

The law is always valid in magnetostatics, but it yields $B$ directly only when symmetry makes $\vec B\cdot d\vec l$ simple along the chosen loop. The standard cases are an infinite straight wire, an ideal infinite solenoid, and a toroid.

For a long straight wire, cylindrical symmetry gives a tangential field of constant magnitude on a circle of radius $r$:

$$
B(2\pi r)=\mu_0 I,
\qquad
B=\frac{\mu_0 I}{2\pi r}.
$$

The right-hand rule gives the field direction. With $I=12\,\mathrm{A}$ and $r=0.050\,\mathrm{m}$,

$$
B=\frac{(4\pi\times10^{-7}\,\mathrm{T\,m/A})(12\,\mathrm{A})}
{2\pi(0.050\,\mathrm{m})}
=4.8\times10^{-5}\,\mathrm{T}.
$$

Choosing an arbitrary Amperian loop around an asymmetric current distribution does not remove the integral; in such cases Biot-Savart or numerical field calculation is usually more useful.

### Long solenoid and toroid

An ideal solenoid has $n$ turns per unit length carrying current $I$. Choose a rectangular Amperian loop with length $\ell$ inside the winding and its return side far outside, where the ideal field vanishes. The short sides contribute zero because they are perpendicular to $\vec B$. Ampere's law gives

$$
B\ell=\mu_0(n\ell)I,
\qquad
B=\mu_0nI.
$$

For a magnetic material in the linear regime, one often writes $B=\mu nI$ with $\mu=\mu_r\mu_0$. Saturation and hysteresis make the proportional law fail in real ferromagnetic cores.

A toroid bends a solenoid into a ring. A circular path of radius $r$ within the windings encloses all $N$ turns:

$$
B(2\pi r)=\mu_0NI,
\qquad
B(r)=\frac{\mu_0NI}{2\pi r}.
$$

The field varies across the toroid's thickness. Treating it as constant is an approximation valid when the cross-section is small compared with the mean radius. An Amperian loop through the central hole encloses zero net current and gives zero field for the ideal toroid.

Ampere's magnetostatic law must be extended when electric fields change with time:

$$
\oint\vec B\cdot d\vec l
=\mu_0I_{\mathrm{enc}}+mu_0\epsilon_0\frac{d\Phi_E}{dt}.
$$

The displacement-current term resolves the apparent contradiction near a charging capacitor: one surface bounded by an Amperian loop cuts the wire current, while another passes between the plates.

## Flux and induced emf

Magnetic flux through a surface is

$$
\Phi_B=\int \vec B\cdot d\vec A.
$$

For a uniform field through a flat loop, $\Phi_B=BA\cos\theta$, where $\theta$ is the angle between $\vec B$ and the surface normal. Faraday's law for an $N$-turn coil is

$$
\mathcal E=-N\frac{d\Phi_B}{dt}.
$$

Flux can change because the field strength, loop area, or orientation changes. The minus sign is Lenz's law: the induced current produces a magnetic effect that opposes the change in flux, not necessarily the original field.

Faraday's law in integral form is more general than a voltage source placed in a wire:

$$
\oint_C\vec E\cdot d\vec l
=-\frac{d}{dt}\int_S\vec B\cdot d\vec A.
$$

A changing magnetic field creates a circulating electric field even when no conductor is present. Unlike an electrostatic field, this induced field is nonconservative: its line integral around a closed path need not vanish, and a single-valued electric potential cannot describe it globally.

```mermaid
graph LR
  A[Current distribution] --> B[Magnetic field]
  B --> C[Flux through a loop]
  C --> D[Changing flux]
  D --> E[Induced emf]
  E --> F[Current opposing the change]
```

| Stage | Relation | Point to check |
|---|---|---|
| Field from current | $\oint\vec B\cdot d\vec l=\mu_0I_{\mathrm{enc}}$ | symmetry must simplify the loop integral |
| Flux through a loop | $\Phi_B=\int\vec B\cdot d\vec A$ | include the angle to the area normal |
| Induced emf | $\mathcal E=-N\,d\Phi_B/dt$ | the sign refers to the chosen loop orientation |
| Stored energy | $U_L=\tfrac12LI^2$ | inductance is a geometric response, not a resistance |

Consider a $200$-turn coil of area $0.010\,\mathrm{m^2}$ whose perpendicular field changes from $0.20\,\mathrm{T}$ to $0.050\,\mathrm{T}$ in $0.30\,\mathrm{s}$. The emf magnitude is

$$
\lvert\mathcal E\rvert
=NA\frac{\lvert\Delta B\rvert}{\Delta t}
=200(0.010)\frac{0.150}{0.30}
=1.0\,\mathrm{V}.
$$

Its direction still requires a choice of surface normal and the corresponding positive direction around the loop.

If the positive area normal points along the initial field, then $\Delta\Phi_B\lt 0$ and $\mathcal E=-N\Delta\Phi_B/\Delta t\gt 0$. The induced current follows the positive loop direction fixed by the right-hand rule. Its own field points along the chosen normal, trying to replace the flux that is disappearing.

### Worked example: a rotating generator coil

Let a coil with $N$ turns and area $A$ rotate at angular speed $\omega$ in a uniform magnetic field. If its area normal makes angle $\theta=\omega t$ with the field,

$$
\Phi_B(t)=BA\cos(\omega t).
$$

Faraday's law gives

$$
\begin{aligned}
\mathcal E(t)
&=-N\frac{d}{dt}[BA\cos(\omega t)]\\
&=NBA\omega\sin(\omega t).
\end{aligned}
$$

For $N=100$, $B=0.50\,\mathrm T$, $A=2.0\times10^{-2}\,\mathrm{m^2}$, and $f=60\,\mathrm{Hz}$,

$$
\begin{aligned}
\omega&=2\pi f=377\,\mathrm{rad/s},\\
\mathcal E_0&=(100)(0.50)(2.0\times10^{-2})(377)=377\,\mathrm V,\\
\mathcal E_{\mathrm{rms}}&=\frac{377}{\sqrt2}=267\,\mathrm V.
\end{aligned}
$$

The mechanical torque required to maintain rotation increases when the generator supplies current. Lenz's law accounts for that counter-torque and prevents electrical energy from appearing without mechanical work.

## Reading Lenz's law without guessing

Use the following sequence:

1. Decide whether the external flux in the chosen direction is increasing or decreasing.
2. Choose the induced field that opposes that change.
3. Use the right-hand rule to infer the induced current.

For example, if upward flux is increasing, the induced field points downward. If upward flux is decreasing, the induced field points upward. Saying only that the induced current “opposes the field” gives the wrong answer in the second case.

The sign can also be checked through energy. A magnet approaching a conducting loop induces a current whose field repels the approaching pole. If the induced field instead attracted the magnet, the magnet would accelerate while the growing current delivered electrical energy, with no compensating input.

## Motional emf and sliding conductors

Flux may change because a conductor moves through a static field. Charges in a rod of length $\ell$ moving with velocity $\vec v$ experience magnetic force $q\vec v\times\vec B$. When the rod, velocity, and field are mutually perpendicular, charge separation produces

$$
\mathcal E=B\ell v.
$$

Suppose the rod slides on conducting rails, closing a circuit of total resistance $R$. Then

$$
I=\frac{B\ell v}{R}.
$$

The magnetic force opposing the motion has magnitude

$$
F=I\ell B=\frac{B^2\ell^2v}{R}.
$$

An external agent maintaining constant speed supplies mechanical power

$$
Fv=\frac{B^2\ell^2v^2}{R}=I^2R,
$$

exactly the rate of Joule heating. The energy balance checks the Lenz's-law direction.

## Inductors as field-energy storage

Self-inductance relates the flux linkage of a circuit to its own current. With a fixed geometry and linear magnetic medium,

$$
N\Phi_B=LI,
\qquad
\mathcal E_L=-L\frac{dI}{dt}.
$$

An inductor resists changes in current by developing an emf; it does not act like a resistance that dissipates $I^2R$ continuously. The magnetic energy stored at current $I$ is

$$
U_L=\frac12LI^2.
$$

The formula follows from power. Building current against the back emf requires terminal voltage $v=L\,dI/dt$, so

$$
\begin{aligned}
U_L
&=\int p\,dt
=\int LI\frac{dI}{dt}\,dt\\
&=\int_0^I LI'\,dI'
=\frac12LI^2.
\end{aligned}
$$

For a long air-core solenoid of length $\ell$, cross-sectional area $A$, and $N$ turns,

$$
L=\mu_0\frac{N^2A}{\ell}.
$$

Combining this with $B=\mu_0(N/\ell)I$ shows that magnetic energy is stored throughout the field volume, with density

$$
u_B=\frac{B^2}{2\mu_0}.
$$

For an ideal RL circuit connected to a DC source, the time constant is $\tau=L/R$. The current cannot jump instantaneously because that would require an unbounded induced emf.

### Worked example: current growth and decay

Kirchhoff's loop equation after connecting a battery is

$$
L\frac{dI}{dt}+RI=V.
$$

With $I(0)=0$, separation or an integrating factor gives

$$
I(t)=\frac VR\left(1-e^{-t/\tau}\right),
\qquad \tau=\frac LR.
$$

Take $V=12\,\mathrm V$, $R=6.0\,\Omega$, and $L=3.0\,\mathrm H$. Then $\tau=0.50\,\mathrm s$ and the final current is $2.0\,\mathrm A$. At one time constant,

$$
I(0.50\,\mathrm s)=2.0(1-e^{-1})=1.26\,\mathrm A.
$$

The resistor voltage is $V_R=IR=7.59\,\mathrm V$, while

$$
V_L=V-V_R=4.41\,\mathrm V.
$$

Their sum remains $12\,\mathrm V$. If the source is removed and the inductor discharges through the resistor, $I(t)=I_0e^{-t/\tau}$. Interrupting the current path abruptly can produce a large switch voltage; a flyback diode provides a controlled decay path in a DC circuit.

## Mutual inductance and transformer action

Two nearby coils can share magnetic flux. If current $I_1$ in coil 1 produces flux linkage in coil 2, define

$$
N_2\Phi_{21}=MI_1,
\qquad
\mathcal E_2=-M\frac{dI_1}{dt}.
$$

For an ideal transformer, both windings link the same changing core flux. Faraday's law then gives

$$
\frac{V_2}{V_1}=\frac{N_2}{N_1}.
$$

Conservation of power in the lossless model gives $V_1I_1=V_2I_2$, hence $I_2/I_1=N_1/N_2$. A transformer changes voltage and current levels but does not create power. It needs changing flux; steady DC produces no sustained secondary emf after the switching transient.

## Sign and symmetry traps

- Ampere's law does not guarantee an easy field calculation; the current distribution must provide the needed symmetry.
- The flux angle is measured from the surface normal, not from the plane of the loop.
- Lenz's law opposes the change in flux. It can reinforce the existing external field while that field is decreasing.
- The sign of $\mathcal E$ depends on the paired choices of area normal and positive loop direction. Its magnitude does not.
- Inductance has units of henries and stores magnetic energy; resistance has units of ohms and converts electrical energy to thermal energy.
- The ideal relation $B=\mu_0nI$ ignores end effects. Near a finite solenoid's ends, the field spreads and weakens.
- A transformer turns ratio applies to induced winding voltages. Winding resistance, leakage flux, and core loss alter terminal values under load.

Useful limiting cases expose setup errors. A static flux gives zero induced emf. Doubling the number of turns doubles the emf for the same flux change per turn. For the straight-wire field, doubling the distance halves $B$.

## Local forms and the geometry behind the loops

Stokes' theorem converts the circulation laws into local differential equations. Magnetostatic Ampere's law becomes

$$
\nabla\times\vec B=\mu_0\vec J,
$$

while Faraday's law becomes

$$
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}.
$$

The curl describes local circulation. A current density creates curling magnetic field, and a changing magnetic field creates curling electric field. The integral form is usually more direct for symmetric apparatus; the differential form is the starting point for field equations in arbitrary geometry.

Orientation is encoded systematically. Choose a surface normal. The positive direction around its boundary is then fixed by the right-hand rule. Reversing the normal reverses both the flux sign and the positive loop direction, leaving the physical law unchanged. Many apparent Lenz-law contradictions come from reversing only one member of this pair.

The surface spanning a loop is not unique, but Maxwell's equations make the result independent of that choice when all relevant terms are included. For magnetic flux, $\nabla\cdot\vec B=0$ means two surfaces with the same boundary enclose no net magnetic charge between them. For Ampere-Maxwell law, conduction and displacement current together satisfy continuity.

## Eddy currents, braking, and heating

A changing flux through a bulk conductor drives circulating currents within the material. These eddy currents create fields opposing the change and dissipate energy through resistance. They are useful in induction cooktops, contactless braking, damping of instrument needles, and metal detection. They are unwanted in transformer cores and electric machines when they waste power as heat.

Laminating a transformer core into thin insulated sheets interrupts large current loops and increases their resistance. Ferrites have high electrical resistivity and are useful at higher frequencies. The magnetic material still guides flux, but the conductive loss path is reduced.

Consider a conducting plate moving into a magnetic-field region. The increasing flux induces currents whose magnetic force opposes entry. Once the plate is fully inside a perfectly uniform field and moves without changing orientation, the linked flux of a co-moving loop no longer changes, so that particular braking contribution vanishes. At the exit edge, the flux decreases and the induced current reverses, yet the force again opposes motion. “Opposes the change” predicts both cases without memorizing current directions.

## Inductance as a circuit coefficient

For multiple coupled circuits, flux linkages are linear combinations of currents in a linear medium:

$$
\begin{aligned}
\Lambda_1&=L_1I_1+MI_2,\\
\Lambda_2&=MI_1+L_2I_2.
\end{aligned}
$$

The sign of the mutual terms depends on winding orientation and reference-current choices; circuit diagrams record it with the dot convention. The magnitude obeys

$$
|M|\leq\sqrt{L_1L_2}.
$$

Defining coupling coefficient $k=\vert M\vert /\sqrt{L_1L_2}$ gives $0\leq k\leq1$. Leakage flux makes $k\lt 1$ in real transformers.

The stored energy for two coupled coils is

$$
U=\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2
$$

with signs consistent with the chosen references. Positivity of field energy leads to the bound on $M$. This is one place where treating mutual inductance as an arbitrary signed number would produce an unphysical circuit.

Inductance may depend on current when the core is nonlinear. Near magnetic saturation, incremental inductance decreases because additional current produces less additional flux. The simple relation $\mathcal E=-L\,dI/dt$ assumes constant $L$; more generally the induced voltage follows $-d\Lambda/dt$. If geometry moves, both current and inductance can vary, and expanding that derivative adds a term involving $dL/dt$.

## Historical thread

Faraday formulated induction through experiments with coils, magnets, and changing currents, emphasizing lines of force before the modern field equations existed. Maxwell later expressed the linked electric and magnetic laws mathematically and added displacement current. Lenz's rule supplies the sign consistent with energy conservation, while inductance packages a device's geometry and material response into a circuit parameter. The sequence mirrors the useful reasoning order: determine the field, determine linked flux, then determine the induced circuit response.

<div className="see-also">

See also: [Magnetic Fields and Forces](/physics/general/magnetic-fields-and-forces) · [AC Circuits and EM Waves](/physics/general/ac-circuits-and-electromagnetic-waves)

</div>
