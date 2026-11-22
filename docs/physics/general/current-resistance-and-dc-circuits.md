---
title: Current, Resistance, and DC Circuits
sidebar_position: 19
---

# Current, Resistance, and DC Circuits

DC circuit analysis rests on three ideas: charge is conserved at a junction, energy is conserved around a loop, and each component supplies a relation between its current and voltage. Ohm's law is one such component relation, not a universal definition of resistance.

## Current, resistance, and power

Current is the rate at which charge crosses a surface:

$$
I=\frac{dQ}{dt}.
$$

Conventional current points in the direction positive charge would move. In metals, the mobile electrons drift in the opposite direction.

For charge carriers of number density $n$, charge magnitude $q$, cross-sectional area $A$, and drift-speed magnitude $v_d$,

$$
I=nqAv_d.
$$

The random thermal speeds of conduction electrons are much larger than $v_d$, but random motion has no preferred direction and contributes no net current. When a circuit is closed, the electric field establishing the drift propagates through the circuit rapidly; electrons do not have to travel from the battery to the load before the load responds.

Current density records local flow:

$$
\vec J=\frac{dI}{dA}\hat n,
\qquad
\vec J=\sigma\vec E
$$

for an isotropic ohmic material. Conductivity is $\sigma=1/\rho$. The microscopic relation $\vec J=\sigma\vec E$ leads to $R=\rho L/A$ for a uniform straight wire with nearly uniform field.

An ohmic element obeys

$$
V=IR.
$$

For a uniform wire,

$$
R=\rho\frac{L}{A},
$$

where resistivity $\rho$ is a material property that generally depends on temperature. Electrical power delivered to a component is

$$
P=IV.
$$

For an ohmic resistor this becomes

$$
P=I^2R=\frac{V^2}{R}.
$$

The choice between these forms depends on which quantity is held fixed. At fixed voltage, increasing $R$ lowers the power; at fixed current, it raises the power.

Near a reference temperature $T_0$, a metal's resistance is often approximated by

$$
R(T)=R_0[1+\alpha(T-T_0)].
$$

This linear law works over a limited range. Filament lamps are visibly non-ohmic because heating changes their resistance as current rises. Diodes are non-ohmic for a different reason: their current-voltage relation is strongly asymmetric. Ohm's law should be tested as a model of a component, not used as the definition $R=V/I$ for every device.

The sign in $P=IV$ depends on terminal conventions. Under the passive sign convention, current enters the terminal labeled positive and $P\gt 0$ means the element absorbs energy. A discharging battery has current leaving its positive terminal, so it supplies power and its absorbed power is negative.

## Reducing resistor networks

Resistors in series carry the same current:

$$
R_{\mathrm{eq}}=R_1+R_2+\cdots.
$$

Resistors in parallel share the same potential difference:

$$
\frac{1}{R_{\mathrm{eq}}}
=\frac{1}{R_1}+\frac{1}{R_2}+\cdots.
$$

A $12\,\mathrm V$ battery connected to $100\,\Omega$ and $220\,\Omega$ in series has

$$
R_{\mathrm{eq}}=320\,\Omega,
\qquad
I=\frac{12}{320}=0.0375\,\mathrm A.
$$

The power in the $220\,\Omega$ resistor is

$$
P=I^2R=(0.0375)^2(220)=0.309\,\mathrm W.
$$

The voltage drops are

$$
V_{100}=3.75\,\mathrm V,
\qquad
V_{220}=8.25\,\mathrm V,
$$

which add to the battery's $12.0\,\mathrm V$. The source supplies $P=VI=0.450\,\mathrm W$. The resistors absorb $0.141\,\mathrm W$ and $0.309\,\mathrm W$, so power balances.

For parallel resistors, the equivalent resistance must be smaller than the smallest branch resistance. For example, $6\,\Omega$ and $3\,\Omega$ in parallel give

$$
R_{\mathrm{eq}}=\left(\frac16+\frac13\right)^{-1}=2\,\Omega.
$$

Across a $12\,\mathrm V$ source, the branch currents are $2\,\mathrm A$ and $4\,\mathrm A$. Their sum, $6\,\mathrm A$, equals $12\,\mathrm V/2\,\Omega$.

## Real sources and terminal voltage

An ideal source maintains its emf regardless of current. A simple real-battery model places internal resistance $r$ in series with an ideal emf $\mathcal E$. While the battery supplies current $I$,

$$
V_{\mathrm{terminal}}=\mathcal E-Ir.
$$

With an external load $R$,

$$
I=\frac{\mathcal E}{R+r}.
$$

Take a $12.0\,\mathrm V$ battery with $r=0.50\,\Omega$ connected to $R=5.5\,\Omega$. Then

$$
\begin{aligned}
I&=\frac{12.0}{5.5+0.50}=2.00\,\mathrm A,\\
V_{\mathrm{terminal}}&=12.0-(2.00)(0.50)=11.0\,\mathrm V,\\
P_R&=I^2R=(2.00)^2(5.5)=22.0\,\mathrm W,\\
P_r&=I^2r=2.0\,\mathrm W.
\end{aligned}
$$

The chemical source supplies $\mathcal EI=24.0\,\mathrm W$, equal to the load power plus internal heating. During charging, current enters the battery's positive terminal and its terminal voltage exceeds the emf in this model.

## Kirchhoff equations for networks that do not reduce

The junction rule expresses charge conservation:

$$
\sum I_{\mathrm{in}}=\sum I_{\mathrm{out}}.
$$

The loop rule expresses energy conservation:

$$
\sum_{\mathrm{loop}}\Delta V=0.
$$

Choose current directions before writing equations. A solved current may be negative; that result means the physical current runs opposite the assumed arrow. When traversing a resistor in the assumed current direction, the potential change is $-IR$. Across an ideal source from its negative to positive terminal, it is $+\mathcal E$.

```mermaid
graph LR
  A[Label branch currents] --> B[Write junction equations]
  B --> C[Choose loop directions]
  C --> D[Write voltage changes]
  D --> E[Solve the simultaneous equations]
  E --> F[Interpret negative currents]
```

| Situation | Invariant | Useful relation |
|---|---|---|
| Series branch | same current | $R_{\mathrm{eq}}=\sum R_i$ |
| Parallel branches | same voltage | $1/R_{\mathrm{eq}}=\sum 1/R_i$ |
| Junction | charge flow balances | $\sum I_{\mathrm{in}}=\sum I_{\mathrm{out}}$ |
| Closed loop | net potential change is zero | $\sum\Delta V=0$ |

### Worked example: a two-loop network

Two meshes share a $4\,\Omega$ resistor. The left mesh contains a $10\,\mathrm V$ source and a separate $2\,\Omega$ resistor; the right mesh contains a $4\,\mathrm V$ source opposing the left source and a separate $3\,\Omega$ resistor. Assign clockwise mesh currents $I_1$ and $I_2$. The current through the shared resistor is $I_1-I_2$ in the left-loop direction.

The loop equations are

$$
\begin{aligned}
10-2I_1-4(I_1-I_2)&=0,\\
-4-3I_2-4(I_2-I_1)&=0.
\end{aligned}
$$

Rearranging,

$$
\begin{aligned}
6I_1-4I_2&=10,\\
-4I_1+7I_2&=-4.
\end{aligned}
$$

Multiply the first equation by $7$ and the second by $4$:

$$
\begin{aligned}
42I_1-28I_2&=70,\\
-16I_1+28I_2&=-16.
\end{aligned}
$$

Adding gives $26I_1=54$, so $I_1=2.08\,\mathrm A$. Substitution yields

$$
I_2=\frac{6I_1-10}{4}=0.615\,\mathrm A.
$$

The shared branch carries $I_1-I_2=1.46\,\mathrm A$ in the left-loop direction. Both solved mesh currents are positive, so the chosen clockwise directions were consistent with the result.

## The RC time scale

When a capacitor charges through a resistor from an ideal source $\mathcal E$,

$$
V_C(t)=\mathcal E\left(1-e^{-t/RC}\right),
\qquad
I(t)=\frac{\mathcal E}{R}e^{-t/RC}.
$$

The time constant is

$$
\tau=RC.
$$

The exponential comes from Kirchhoff's rule. With capacitor charge $q$,

$$
\mathcal E-IR-\frac qC=0,
\qquad I=\frac{dq}{dt}.
$$

Thus

$$
\frac{dq}{dt}=\frac{\mathcal E}{R}-\frac{q}{RC}.
$$

Solving with $q(0)=0$ gives $q=C\mathcal E(1-e^{-t/RC})$, from which the stated voltage and current follow. The product $RC$ has units of seconds: $\Omega\,\mathrm F=(\mathrm{V/A})(\mathrm{C/V})=\mathrm{C/A}=\mathrm s$.

At $t=0^+$ an initially uncharged capacitor behaves like a short circuit: its voltage cannot jump, while the current can. As $t\to\infty$ it behaves like an open circuit under DC conditions.

For $C=10\,\mu\mathrm F$, $R=200\,\mathrm{k\Omega}$, and $\mathcal E=9.0\,\mathrm V$,

$$
\tau=(200\times10^3)(10\times10^{-6})=2.0\,\mathrm s,
$$

and after one time constant,

$$
V_C(\tau)=9.0(1-e^{-1})=5.69\,\mathrm V.
$$

Thus the capacitor reaches about $63.2\%$ of its final voltage in one $\tau$; it is not fully charged after one time constant.

At $t=5\tau$ it has reached $1-e^{-5}\approx99.33\%$ of the final voltage. “Fully charged” is therefore an engineering tolerance, not a finite mathematical time.

Energy reveals another feature of charging. The battery supplies

$$
E_{\mathrm{source}}=\mathcal E Q=C\mathcal E^2.
$$

The final capacitor energy is

$$
U_C=\frac12C\mathcal E^2.
$$

The remaining half is dissipated in the resistor, independent of $R$; changing $R$ changes the charging time but not the total heat in this ideal circuit. During discharge through a resistor,

$$
V_C(t)=V_0e^{-t/RC},
\qquad
I(t)=-\frac{V_0}{R}e^{-t/RC},
$$

where the minus sign refers to a current reference direction chosen for charging.

## Measuring without changing the circuit too much

An ammeter is placed in series and should have very small internal resistance. A voltmeter is placed in parallel and should have very large internal resistance. Reversing those connections can badly disturb the circuit; placing a low-resistance ammeter directly across a source may create a damaging current.

A meter's finite resistance causes loading. If a voltmeter of resistance $R_V$ measures a resistor $R$, the branch actually becomes $R\parallel R_V$. The error is small only when $R_V\gg R$. Likewise, an ammeter's resistance adds to the measured branch and should be much smaller than the branch resistance.

## Checks at switching instants

- Do not swap the resistor and capacitor combination rules: capacitors combine oppositely to resistors.
- A capacitor is neither always open nor always short. Its voltage is continuous through an ideal switching instant, and its long-time DC current is zero.
- Keep one traversal direction for each loop equation. Changing direction halfway through changes signs without changing the physics.
- A negative branch current corrects an assumed direction; it does not invalidate the equations.
- Check power conservation by comparing total power supplied with total power absorbed.
- Kirchhoff's lumped-circuit model assumes component dimensions are small compared with the electromagnetic wavelength and that stray capacitance and inductance can be neglected.

The limits of an RC solution should be read before trusting intermediate values. For charging, $V_C(0)=0$ and $V_C(\infty)=\mathcal E$; the current starts at $\mathcal E/R$ and decays to zero.

## Node voltage and equivalent-source methods

Kirchhoff equations can be organized without tracing many loops. In node-voltage analysis, choose one node as zero potential and assign unknown voltages to the others. The current through a resistor between nodes $a$ and $b$ is $(V_a-V_b)/R$. Applying current conservation at each nonreference node produces one equation per unknown node voltage.

For example, a node $V$ connects through $2\,\mathrm{k\Omega}$ to a $10\,\mathrm V$ node, through $3\,\mathrm{k\Omega}$ to ground, and through $6\,\mathrm{k\Omega}$ to a $4\,\mathrm V$ node. Taking currents leaving $V$,

$$
\frac{V-10}{2000}+\frac V{3000}+\frac{V-4}{6000}=0.
$$

Multiply by $6000$:

$$
3(V-10)+2V+(V-4)=0.
$$

Thus $6V-34=0$ and $V=5.67\,\mathrm V$. The branch currents then follow from their voltage differences. This method makes junction conservation automatic and scales better than guessing many branch currents.

Any linear two-terminal network of sources and resistors can be replaced, as seen by a load, by a Thevenin source $V_{\mathrm{th}}$ in series with $R_{\mathrm{th}}$. Find $V_{\mathrm{th}}$ as the open-circuit terminal voltage. Find $R_{\mathrm{th}}$ by turning off independent sources—short ideal voltage sources and open ideal current sources—and calculating resistance seen from the terminals. A Norton equivalent uses current $I_N=V_{\mathrm{th}}/R_{\mathrm{th}}$ in parallel with the same resistance.

Equivalent sources do not reproduce internal voltages and currents, only terminal behavior. Dependent sources cannot be turned off; a test source is then used to determine the input resistance.

## Maximum power and efficiency

A Thevenin source driving load $R_L$ delivers

$$
P_L=\frac{V_{\mathrm{th}}^2R_L}{(R_{\mathrm{th}}+R_L)^2}.
$$

Differentiation shows maximum load power at $R_L=R_{\mathrm{th}}$. At that point half the source power is dissipated inside the Thevenin resistance, so efficiency is only fifty percent. Maximum power transfer is useful in signal and communication settings; power-distribution systems usually prefer $R_L\gg R_{\mathrm{th}}$ to reduce source loss.

If $V_{\mathrm{th}}=12\,\mathrm V$ and $R_{\mathrm{th}}=4\,\Omega$, the matched load is $4\,\Omega$. Current is $12/8=1.5\,\mathrm A$, and load power is $(1.5)^2(4)=9.0\,\mathrm W$. A $20\,\Omega$ load receives less power, but the fraction of supplied power reaching it is much higher.

## Energy delivery and electrical safety

Household energy billing uses kilowatt-hours, a unit of energy:

$$
1\,\mathrm{kWh}=3.6\times10^6\,\mathrm J.
$$

A $1.5\,\mathrm{kW}$ heater operating for three hours consumes $4.5\,\mathrm{kWh}$, or $16.2\,\mathrm{MJ}$. Power describes rate; energy also depends on duration.

Fuses and circuit breakers respond to excessive current because wiring heat scales roughly as $I^2R$. A short circuit removes most load resistance and can produce dangerous current limited mainly by source and wire resistance. Ground-fault protection instead compares outgoing and returning currents and disconnects when some current takes an unintended path.

The physiological hazard of electricity depends on current path, duration, frequency, skin condition, and contact area, not voltage alone. High voltage can drive dangerous current through the body's resistance, while wet skin lowers that resistance. Circuit calculations involving mains or high-energy capacitors should remain analytical unless proper isolation, discharge procedures, and rated equipment are available.

## Model boundaries

Ideal wires are equipotential and have no resistance. Real wires develop voltage drop and heat, especially at high current. Contacts add resistance; batteries have chemistry-dependent voltage and capacity; capacitors leak; switches arc. A lumped DC model is valuable when these effects are either included as components or small relative to the desired accuracy.

Kirchhoff's loop rule assumes changing magnetic flux through the loop is negligible. In rapidly changing circuits, induced emf must be included. At sufficiently high frequency, propagation delay makes voltage position-dependent along a wire and transmission-line analysis replaces the instantaneous lumped picture.

## Reading component ratings

A resistor's resistance value does not state how much power it can safely dissipate. If a $1.0\,\mathrm{k\Omega}$ resistor carries $30\,\mathrm{mA}$, its power is

$$
P=I^2R=(0.030)^2(1000)=0.90\,\mathrm W.
$$

That exceeds the rating of a common quarter-watt part even though Ohm's law is satisfied. Voltage rating can impose another limit, especially for physically small or high-value resistors.

Capacitors have voltage ratings and polarity constraints. Exceeding the dielectric rating can cause breakdown; reversing a polarized electrolytic capacitor can damage it. Batteries specify capacity in ampere-hours, which measures charge, while stored energy also depends on voltage. A $2\,\mathrm{Ah}$ battery at nominal $12\,\mathrm V$ corresponds ideally to about $24\,\mathrm{Wh}$, but usable energy depends on discharge rate, temperature, cutoff voltage, and aging.

Wire gauge affects both resistance and allowable current. A thinner or longer wire has larger resistance, creating more voltage drop and heat at the same current. Connections can dominate resistance when contacts are loose or corroded. These effects are modeled with ordinary series resistances before invoking more elaborate circuit theory.

When reporting a solved circuit, include current directions, node-voltage reference, source polarity, and whether voltages are terminal or emf values. A bare negative number is ambiguous without the reference arrow that made it negative.

Sign conventions are part of the answer, not disposable scratch work.

<div className="see-also">

See also: [Electric Potential and Capacitance](/physics/general/electric-potential-and-capacitance) · [AC Circuits and EM Waves](/physics/general/ac-circuits-and-electromagnetic-waves)

</div>
