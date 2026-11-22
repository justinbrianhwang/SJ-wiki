---
title: Acids, Bases, and pH
sidebar_position: 16
---

# Acids, Bases, and pH

Acid-base language has widened over time. Arrhenius described ions produced in water, Brønsted and Lowry followed proton transfer, and Lewis followed electron pairs. Each model keeps the useful part of the earlier one while covering reactions that the narrower definition misses.

pH belongs to the aqueous side of the subject. It compresses hydronium activity onto a logarithmic scale, so a change of one pH unit corresponds to a tenfold change in acidity. Before calculating it, identify what reacted and what remains in solution.

## Three models, three ranges of use

| Model | Acid | Base | Reaction it describes well |
|---|---|---|---|
| Arrhenius | increases hydronium in water | increases hydroxide in water | hydrochloric acid with sodium hydroxide |
| Brønsted–Lowry | proton donor | proton acceptor | ammonium transferring a proton to water |
| Lewis | electron-pair acceptor | electron-pair donor | boron trifluoride binding ammonia |

An Arrhenius acid need not literally contain an isolated $H^+$ ion. Hydrogen chloride transfers a proton to water:

$$
\mathrm{HCl+H_2O\rightarrow H_3O^+ + Cl^-}.
$$

Writing $H^+$ is often convenient bookkeeping, but bare protons do not persist in liquid water. Hydronium, $H_3O^+$, is itself a simplified formula for a hydrated proton distributed among water molecules.

The Brønsted–Lowry definition handles proton transfer outside the pattern “acid plus hydroxide.” For example,

$$
\mathrm{NH_3+H_2O\rightleftharpoons NH_4^+ + OH^-}.
$$

Ammonia accepts a proton and is the base; water donates one and is the acid. The products form the corresponding conjugates. $\mathrm{NH_4^+/NH_3}$ and $\mathrm{H_2O/OH^-}$ are conjugate acid-base pairs, with each pair differing by exactly one proton.

Water can donate or accept a proton, so it is amphiprotic. Bicarbonate, $\mathrm{HCO_3^-}$, is another amphiprotic species: it can become $\mathrm{H_2CO_3}$ by accepting a proton or $\mathrm{CO_3^{2-}}$ by donating one. Whether it acts as acid or base depends on its reaction partner.

Lewis theory removes the requirement for proton transfer. Ammonia donates its nitrogen lone pair to electron-deficient $\mathrm{BF_3}$:

$$
\mathrm{BF_3+NH_3\rightarrow F_3B\!\leftarrow\!NH_3}.
$$

$\mathrm{BF_3}$ is the Lewis acid and $\mathrm{NH_3}$ the Lewis base. Metal cations are Lewis acids when ligands donate electron pairs to them. Every Brønsted base uses an electron pair to bind a proton, but Lewis acid-base chemistry also includes coordination reactions with no proton at all.

## Strength, concentration, and amount are separate ideas

Acid strength describes the position of an equilibrium. A strong acid reacts essentially completely with water under the stated conditions; a weak acid establishes an appreciable equilibrium between ionized and unionized forms. Concentration instead reports how much solute occupies a volume. A $10^{-4}\ \mathrm M$ strong acid is dilute but still strong, while a $1.0\ \mathrm M$ weak acid is concentrated but still weak.

The strongest acid that can persist in water is effectively hydronium, because any acid much stronger than hydronium transfers its proton to water. This solvent leveling effect causes HCl, HBr, and several other strong acids to appear equally complete in dilute aqueous solution. A different solvent can distinguish strengths that water levels.

For bases, soluble group 1 hydroxides dissociate completely. Some group 2 hydroxides supply two hydroxide ions per formula unit when dissolved:

$$
\mathrm{Ca(OH)_2\rightarrow Ca^{2+}+2OH^-}.
$$

“Strong” does not mean “highly soluble.” Calcium hydroxide is treated as fully dissociated for the portion that dissolves, yet its solubility is limited. Strength concerns ionization or dissociation; solubility concerns how much enters solution.

Molecular structure helps explain relative acid strength. Within a row of the periodic table, greater electronegativity often stabilizes the conjugate base. Down a group, increasing bond length and polarizability can dominate, so hydrohalic acid strength rises from HF to HI. Oxyacid strength generally increases when electron-withdrawing oxygen atoms stabilize the conjugate base. Resonance also spreads negative charge: acetate is more stable than ethoxide, helping acetic acid donate a proton more readily than ethanol.

These are comparisons, not a substitute for measured equilibrium constants. Solvent, charge, and local structure can change which effect dominates.

## Water sets the reference scale

Water undergoes autoionization:

$$
\mathrm{2H_2O\rightleftharpoons H_3O^+ + OH^-}.
$$

Its equilibrium constant is written

$$
K_w=[H_3O^+][OH^-].
$$

At $25\ ^\circ\mathrm C$, $K_w=1.0\times10^{-14}$ in the usual introductory concentration treatment. In pure water the two ions form in equal amounts, hence

$$
[H_3O^+]=[OH^-]=\sqrt{K_w}=1.0\times10^{-7}\ \mathrm M.
$$

The logarithmic definitions are

$$
\mathrm{pH}=-\log a_{H_3O^+},
\qquad
\mathrm{pOH}=-\log a_{OH^-}.
$$

Strictly, pH uses the dimensionless activity $a$, not a concentration carrying units. In sufficiently dilute solutions, activity is approximated by molar concentration relative to the standard state, which yields the familiar calculation. Concentrated solutions may have pH values outside the nominal 0–14 interval and require activity corrections.

Taking the negative logarithm of $K_w$ gives

$$
\mathrm{pH+pOH}=pK_w.
$$

At $25\ ^\circ\mathrm C$, $pK_w=14.00$. Both $K_w$ and the neutral pH vary with temperature. Neutrality always means equal hydronium and hydroxide activities; it means pH 7.00 only when $pK_w=14.00$.

The logarithm changes how uncertainty and significant figures are reported. The number of digits after the decimal in pH corresponds roughly to the number of significant figures in the hydronium concentration. A concentration of $2.5\times10^{-3}\ \mathrm M$ supports pH $2.60$, not $2.60206$.

## Reading the logarithmic scale

```text
more acidic                              more basic
high hydronium                           high hydroxide
     0    2    4    6    7    8    10   12   14    pH at 25 °C
     |----|----|----|----|----|-----|----|----|
                         neutral
```

A solution at pH 3 has ten times the hydronium activity of one at pH 4 and one thousand times that of one at pH 6. It is incorrect to call the first solution “twice as acidic” as a pH 6 solution. The numerical pH values differ by a factor of two, but the underlying activities differ by $10^3$.

The inverse operation recovers concentration from pH:

$$
[H_3O^+]\approx10^{-\mathrm{pH}}.
$$

For pH $8.35$, the hydronium concentration is approximately $10^{-8.35}=4.5\times10^{-9}\ \mathrm M$. At $25\ ^\circ\mathrm C$, the hydroxide concentration is $K_w/[H_3O^+]=2.2\times10^{-6}\ \mathrm M$.

## Worked example: a strong diprotic base

Find the pH of $3.20\times10^{-3}\ \mathrm M$ barium hydroxide at $25\ ^\circ\mathrm C$, assuming complete dissociation.

First account for the formula stoichiometry:

$$
\mathrm{Ba(OH)_2\rightarrow Ba^{2+}+2OH^-}.
$$

Each mole supplies two moles of hydroxide, so

$$
[OH^-]=2(3.20\times10^{-3})=6.40\times10^{-3}\ \mathrm M.
$$

Then

$$
\mathrm{pOH}=-\log(6.40\times10^{-3})=2.194.
$$

Using $\mathrm{pH+pOH}=14.00$,

$$
\mathrm{pH}=14.00-2.194=11.806\approx11.81.
$$

The answer is basic and of the expected scale. Treating the hydroxide concentration as equal to the formula concentration would miss the factor of two and shift the pH by about $\log 2=0.301$ unit.

## Neutralization is a mole calculation first

When strong acid and strong base are mixed, hydronium and hydroxide react essentially to completion:

$$
\mathrm{H_3O^+ + OH^-\rightarrow2H_2O}.
$$

Concentrations cannot be subtracted directly when the solutions have different volumes. Convert each reagent to moles, determine the excess, and divide that excess by the combined volume.

### Worked example: mixing nitric acid and potassium hydroxide

Mix $40.0\ \mathrm{mL}$ of $0.100\ \mathrm M$ nitric acid with $25.0\ \mathrm{mL}$ of $0.120\ \mathrm M$ potassium hydroxide.

The initial acid amount is

$$
n_{H_3O^+}=(0.0400\ \mathrm L)(0.100\ \mathrm{mol\,L^{-1}})
=0.00400\ \mathrm{mol}.
$$

The initial hydroxide amount is

$$
n_{OH^-}=(0.0250\ \mathrm L)(0.120\ \mathrm{mol\,L^{-1}})
=0.00300\ \mathrm{mol}.
$$

The reaction is one-to-one, leaving

$$
n_{H_3O^+,\,excess}=0.00400-0.00300=0.00100\ \mathrm{mol}.
$$

Assuming additive volumes, the final volume is

$$
V_{\mathrm{total}}=0.0400+0.0250=0.0650\ \mathrm L.
$$

Therefore,

$$
[H_3O^+]=\frac{0.00100}{0.0650}=1.54\times10^{-2}\ \mathrm M,
$$

and

$$
\mathrm{pH}=-\log(1.54\times10^{-2})=1.81.
$$

Nitrate and potassium remain as spectator ions. If the acid and base moles had been equal, the neutral result would follow only because both reagents are strong and their salt does not appreciably react with water.

## The very dilute limit

Ignoring water works well when the strong acid or base contributes far more than $10^{-7}\ \mathrm M$ of its characteristic ion. It fails near that scale. For example, treating $1.0\times10^{-8}\ \mathrm M$ HCl as the sole hydronium source gives pH 8, falsely predicting that an acid makes water basic.

Let $C$ be the analytical HCl concentration. Charge balance gives $[H_3O^+]=[OH^-]+C$, and water gives $[H_3O^+][OH^-]=K_w$. Substitution produces

$$
[H_3O^+]^2-C[H_3O^+]-K_w=0.
$$

The physically meaningful root is

$$
[H_3O^+]=\frac{C+\sqrt{C^2+4K_w}}{2}.
$$

For $C=1.0\times10^{-8}\ \mathrm M$ at $25\ ^\circ\mathrm C$,

$$
[H_3O^+]=\frac{1.0\times10^{-8}+\sqrt{(1.0\times10^{-8})^2+4.0\times10^{-14}}}{2}
=1.05\times10^{-7}\ \mathrm M,
$$

so $\mathrm{pH}=6.98$. The acid lowers the pH slightly below 7, as chemical reasoning requires.

## Checks before accepting a result

- Conjugate partners must differ by one $H^+$ and their charges must differ by one unit. $\mathrm{H_2SO_4/HSO_4^-}$ is a pair; $\mathrm{H_2SO_4/SO_4^{2-}}$ is not an adjacent pair.
- A negative excess amount signals that the limiting reagent assignment was reversed. Recalculate the remainder using the larger amount minus the smaller one.
- Strong acid does not mean concentrated, and weak acid does not mean harmless. The labels describe equilibrium behavior, not dose or corrosiveness.
- Polyprotic formulas require stoichiometric care. Complete dissociation of one formula unit may produce more than one acidic proton or hydroxide ion, but later ionizations of weak polyprotic acids are equilibria rather than automatic multiples.
- A calculator accepts the logarithm of a bare number. Chemically, the pH definition uses activity; the concentration shorthand is an approximation tied to a standard state.
- Litmus or universal indicator supplies an interval, not a precise pH. Electrode calibration, temperature, and ionic strength matter when numerical accuracy is needed.

## Acid-base reactions favor the weaker pair

A proton-transfer reaction can be predicted by comparing the acids on opposite sides. For

$$
\mathrm{HA+B\rightleftharpoons A^-+BH^+},
$$

the equilibrium constant is obtained by dividing the acid constants:

$$
K=\frac{K_a(HA)}{K_a(BH^+)}
=10^{pK_a(BH^+)-pK_a(HA)}.
$$

If $HA$ is the stronger acid, it has the smaller $pK_a$, making $K$ large and favoring products. The favored side contains the weaker acid and weaker base. This comparison replaces vague claims that a proton “wants” to move; equilibrium favors the lower-free-energy acid-base pair under the stated solvent conditions.

Consider acetate reacting with ammonium:

$$
\mathrm{CH_3COO^-+NH_4^+\rightleftharpoons CH_3COOH+NH_3}.
$$

Using approximate $pK_a$ values 4.74 for acetic acid and 9.25 for ammonium, the reaction as written forms the stronger acid, acetic acid. Its equilibrium constant is

$$
K=10^{4.74-9.25}=3.1\times10^{-5}.
$$

Reactants are favored. Reversing the equation gives a large constant: acetic acid readily protonates ammonia. The calculation also shows why acid-base equilibria require conjugate-pair labels on both sides.

Solvent matters in such comparisons. A $pK_a$ table measured in water should not be transferred uncritically to another solvent. Solvation stabilizes charged and neutral species differently, changing acid strength and sometimes reversing familiar orderings.

## Lewis acids beyond proton transfer

Lewis theory is especially useful for metal ions and electron-deficient compounds. When $\mathrm{Al^{3+}}$ binds six water molecules, oxygen lone pairs donate into the metal center. The highly charged metal polarizes the coordinated O–H bonds, allowing a bound water molecule to donate a proton:

$$
\mathrm{[Al(H_2O)_6]^{3+}+H_2O
\rightleftharpoons
[Al(H_2O)_5(OH)]^{2+}+H_3O^+}.
$$

The first event is Lewis acid-base coordination; the resulting polarization produces Brønsted acidity. The models describe different aspects of one system rather than competing labels.

Lewis acidity also explains why $\mathrm{BF_3}$ reacts with donors despite containing no hydrogen and producing no hydronium. In organic mechanisms, carbocations and polarized carbonyl carbons behave as electron-pair acceptors, while lone pairs and pi bonds act as donors. The broader definition connects introductory acid-base chemistry with coordination and organic chemistry.

## Measuring pH with an electrode

A glass pH electrode responds to a potential difference related to hydrogen-ion activity. It does not count hydronium ions directly. The ideal response is Nernstian, so potential changes linearly with pH at a given temperature. A reference electrode supplies a stable comparison potential.

Calibration normally uses at least two standard buffers that bracket the expected sample pH. The slope and offset reveal whether the electrode response is reasonable. Rinsing prevents carryover, while gentle blotting avoids creating static charge or wiping the hydrated glass layer aggressively. Temperature affects both electrode slope and the sample's acid-base equilibria; automatic temperature compensation corrects the former but cannot convert the sample chemistry to what it would be at another temperature.

Very low ionic strength causes unstable junction potentials and slow readings. Concentrated acids and bases depart strongly from the dilute activity model. Samples containing proteins, oils, or precipitates can foul the glass or junction. A displayed value with two decimals is not automatically accurate to two decimals.

Indicators provide a different measurement. For an indicator equilibrium

$$
\mathrm{HIn+H_2O\rightleftharpoons H_3O^++In^-},
$$

the two forms have different colors. The observed transition occurs over a ratio range rather than at one exact pH. Human color perception, sample color, lighting, and indicator concentration limit precision. Indicators are well suited to a sharp titration endpoint but poor substitutes for an electrode when a reliable continuous pH value is required.

## Acid-base chemistry outside ideal dilute water

The familiar pH equations assume dilute aqueous behavior. In seawater, concentrated electrolytes, or biological media, ions interact and activity coefficients differ from one. Charge balance and mass balance still hold, but replacing every activity by molarity can produce noticeable error.

Carbon dioxide exchange is another common complication. Dissolved carbon dioxide participates in a set of equilibria involving hydrated carbon dioxide, bicarbonate, and carbonate. Water left open to air does not remain chemically isolated, and freshly boiled or deionized water can change pH during handling. The observed pH of “pure water” is therefore sensitive to gas exchange and contamination even before instrumental limitations are considered.

At extreme acid or base concentrations, the nominal 0–14 classroom range is not a hard boundary. Activity-based pH can be negative or greater than 14. Such values do not violate the definition; they expose the limits of treating molarity as activity and of using dilute-solution intuition.

Acid-base equilibria also control solubility. Protonating the anion of a weak acid removes that ion from a dissolution equilibrium, so many carbonates and sulfides dissolve more readily at low pH. Conversely, raising pH can precipitate metal hydroxides. A pH change therefore alters more than the hydronium number; it can change charge state, complexation, and which solid phases are stable.

When several proton-accepting sites are present, the most basic site is protonated preferentially, but neighboring groups can shift one another's strength. Tabulated constants belong to a specified molecule and step rather than to a functional group in isolation.

<div className="see-also">

See also: [acid-base equilibria, buffers, and titrations](/chemistry/general/acid-base-equilibria-buffers-and-titrations) · [aqueous reactions and solution stoichiometry](/chemistry/general/aqueous-reactions-and-solution-stoichiometry) · [chemical equilibrium](/chemistry/general/chemical-equilibrium) · [ionic and covalent bonding](/chemistry/general/ionic-and-covalent-bonding)

</div>
