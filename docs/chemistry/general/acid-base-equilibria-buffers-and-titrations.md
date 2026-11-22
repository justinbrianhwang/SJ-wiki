---
title: Acid-Base Equilibria, Buffers, and Titrations
sidebar_position: 17
---

# Acid-Base Equilibria, Buffers, and Titrations

A weak acid does not come with a fixed hydronium concentration. Its pH depends on both the equilibrium constant and the amount dissolved. Add its conjugate base and the same equilibrium becomes a buffer; add a measured amount of strong base and it becomes a titration. The chemistry is continuous even though the calculation method changes from one region to another.

The reliable order of work is always chemical before algebraic: list the species, complete any essentially quantitative reaction, and only then write the equilibrium that controls pH.

## What an acid dissociation constant measures

For a monoprotic weak acid,

$$
\mathrm{HA(aq)+H_2O(l)\rightleftharpoons H_3O^+(aq)+A^-(aq)},
$$

the acid dissociation constant is

$$
K_a=\frac{[H_3O^+][A^-]}{[HA]}.
$$

Liquid water is omitted because its activity is effectively constant in a dilute aqueous solution. A larger $K_a$ means that products are more strongly favored. The logarithmic form, $pK_a=-\log K_a$, reverses the ordering: a smaller $pK_a$ denotes a stronger acid.

A weak base is treated in the same way:

$$
\mathrm{B+H_2O\rightleftharpoons BH^+ + OH^-},
\qquad
K_b=\frac{[BH^+][OH^-]}{[B]}.
$$

For a conjugate pair, multiplying the acid and base equilibria cancels the conjugate species and leaves water autoionization. Therefore,

$$
K_a(\mathrm{BH^+})K_b(\mathrm{B})=K_w.
$$

At $25\ ^\circ\mathrm C$, $K_w=1.0\times10^{-14}$, so $pK_a+pK_b=14.00$. The numerical value changes with temperature; using 14.00 without a stated temperature is an approximation.

Percent ionization describes how much of an initial weak acid concentration $C_0$ has dissociated:

$$
\%\text{ ionization}=\frac{[H_3O^+]_{\mathrm{eq}}}{C_0}\times100\%.
$$

Dilution increases the *fraction* ionized even though it usually lowers $[H_3O^+]$. Le Châtelier's principle predicts the greater fraction, while the mass balance explains the lower absolute concentration.

### Worked example: solving without hiding the approximation

Find the pH and percent ionization of $0.100\ \mathrm M$ acetic acid with $K_a=1.8\times10^{-5}$.

Let $x$ molar acid dissociate. The equilibrium concentrations are $[HA]=0.100-x$ and $[H_3O^+]=[A^-]=x$, giving

$$
1.8\times10^{-5}=\frac{x^2}{0.100-x}.
$$

If $x$ is small compared with $0.100$, the denominator is approximately $0.100$:

$$
x\approx\sqrt{(1.8\times10^{-5})(0.100)}
=1.34\times10^{-3}\ \mathrm M.
$$

The neglected change is

$$
\frac{1.34\times10^{-3}}{0.100}\times100\%=1.34\%,
$$

comfortably below the usual five-percent check. Thus

$$
\mathrm{pH}=-\log(1.34\times10^{-3})=2.87.
$$

The exact quadratic gives essentially the same reported pH. The check matters more than the shortcut: when the change is not small, solve $x^2+K_ax-K_aC_0=0$ and keep the positive root.

## Polyprotic acids donate one proton at a time

A diprotic acid has two distinct equilibria,

$$
\begin{aligned}
\mathrm{H_2A+H_2O}&\rightleftharpoons\mathrm{H_3O^+ + HA^-} && K_{a1},\\
\mathrm{HA^-+H_2O}&\rightleftharpoons\mathrm{H_3O^+ + A^{2-}} && K_{a2}.
\end{aligned}
$$

Usually $K_{a1}\gt K_{a2}$. Removing a positive proton from an already negative ion is less favorable, and hydronium produced by the first step suppresses the second. When the constants differ by several orders of magnitude, the first dissociation determines the pH of an acid solution and the later step contributes little hydronium. That simplification fails when adjacent constants are close.

Amphiprotic intermediate ions such as $\mathrm{HA^-}$ can donate or accept a proton. For a solution of a salt containing only such an intermediate, a useful approximation is

$$
\mathrm{pH}\approx\frac{1}{2}(pK_{a1}+pK_{a2}),
$$

provided concentration and water autoionization do not dominate. It comes from combining the two neighboring equilibria and the mass and charge balances, not from averaging pH values arbitrarily.

## Salt hydrolysis and the pH of ions

The ions of a soluble salt need not be spectators in acid-base chemistry. The conjugate base of a weak acid accepts a proton from water:

$$
\mathrm{A^-+H_2O\rightleftharpoons HA+OH^-},
\qquad K_b=\frac{K_w}{K_a}.
$$

Consequently, sodium acetate solution is basic. The conjugate acid of a weak base behaves oppositely, so ammonium chloride solution is acidic. Ions derived from strong acids or strong bases, such as $\mathrm{Cl^-}$ or $\mathrm{Na^+}$ in introductory calculations, have negligible acid-base action.

Small, highly charged metal cations can acidify water even though they contain no proton in their written formula. Coordinated water molecules are polarized by the metal ion, making an O–H bond easier to break. A rule based only on whether an ion contains hydrogen is therefore unreliable.

For a salt made from a weak acid and weak base, both ions react. Comparing $K_a$ of the cation with $K_b$ of the anion predicts the direction qualitatively. A full treatment may require simultaneous balances rather than two independent ICE tables.

## Buffers as a proton inventory

A buffer contains appreciable amounts of a weak acid and its conjugate base. Added strong base consumes the acid,

$$
\mathrm{HA+OH^-\rightarrow A^-+H_2O},
$$

while added strong acid consumes the conjugate base,

$$
\mathrm{H_3O^+ + A^-\rightarrow HA+H_2O}.
$$

The strong reagent is handled by mole stoichiometry because these reactions lie far toward products. The remaining conjugate pair then establishes equilibrium.

Rearranging the $K_a$ expression gives the Henderson–Hasselbalch equation:

$$
\begin{aligned}
K_a&=\frac{[H_3O^+][A^-]}{[HA]},\\
[H_3O^+]&=K_a\frac{[HA]}{[A^-]},\\
\mathrm{pH}&=pK_a+\log\frac{[A^-]}{[HA]}.
\end{aligned}
$$

It is an equilibrium relation, not a separate chemical law. Activities are replaced by concentrations, so accuracy declines in concentrated or high-ionic-strength solutions. When both species share a volume, their mole ratio equals their concentration ratio.

Buffer capacity is the amount of strong acid or base that can be absorbed for a specified pH change. Capacity grows with the total concentration $[HA]+[A^-]$ and is greatest near equal concentrations. The useful buffering range is often taken as $pK_a\pm1$, where the ratio lies between $0.1$ and $10$. A dilute buffer and a concentrated buffer can have the same pH but very different capacities.

### Worked example: acid added to a buffer

A solution contains $0.200$ mol acetic acid and $0.300$ mol acetate in $1.00\ \mathrm L$. Add $0.0500$ mol HCl and assume the volume change is negligible. Use $pK_a=4.74$.

First consume acetate with the strong acid. The mole changes are $-0.0500$ mol acetate and $+0.0500$ mol acetic acid:

$$
\begin{array}{c|cc}
&\mathrm{HA}&\mathrm{A^-}\\ \hline
\text{before}&0.200&0.300\\
\text{change}&+0.0500&-0.0500\\
\text{after}&0.250&0.250
\end{array}
$$

Both buffer components remain, so

$$
\mathrm{pH}=4.74+\log\frac{0.250}{0.250}=4.74.
$$

Had $0.350$ mol HCl been added, acetate would be exhausted and $0.050$ mol strong acid would remain. Henderson–Hasselbalch would then be invalid; excess hydronium would control the pH.

## A titration is several different calculations

During a titration, the dominant pH calculation changes with the composition. For a weak monoprotic acid titrated by strong base, the sequence is:

```mermaid
flowchart LR
  A["Initial weak acid"] --> B["Buffer region"]
  B --> C["Half-equivalence: pH = pKa"]
  C --> D["Equivalence: conjugate-base hydrolysis"]
  D --> E["After equivalence: excess OH-"]
```

| Region | Main species controlling pH | Method |
|---|---|---|
| Before any titrant | weak acid | acid ICE table |
| Before equivalence | acid and conjugate base | neutralization, then buffer equation |
| Half-equivalence | equal conjugate amounts | $\mathrm{pH}=pK_a$ |
| Equivalence | conjugate base | hydrolysis ICE table |
| Beyond equivalence | excess strong base | leftover $OH^-$ and total volume |

Half-equivalence means half the original acid has been converted to conjugate base. Equal amounts make the logarithm zero, so the measured pH gives $pK_a$. Equivalence instead means stoichiometric equality between acid originally present and base delivered. It does not generally mean pH 7.

### Worked example: four points on one titration

Titrate $50.0\ \mathrm{mL}$ of $0.100\ \mathrm M$ acetic acid with $0.100\ \mathrm M$ NaOH. Take $K_a=1.8\times10^{-5}$ and $pK_a=4.74$. Initially there are

$$
n_{HA}=(0.0500\ \mathrm L)(0.100\ \mathrm{mol\,L^{-1}})=0.00500\ \mathrm{mol}.
$$

**Initial point.** The weak-acid calculation from the earlier example scales directly because the concentration is also $0.100\ \mathrm M$; $[H_3O^+]\approx1.34\times10^{-3}\ \mathrm M$ and $\mathrm{pH}=2.87$.

**After $25.0\ \mathrm{mL}$ base.** Added hydroxide is $0.00250$ mol. It converts that amount of acid to acetate, leaving $0.00250$ mol of each. This is half-equivalence:

$$
\mathrm{pH}=4.74+\log(1)=4.74.
$$

**At $50.0\ \mathrm{mL}$ base.** All $0.00500$ mol acid has become acetate. Its concentration in the $0.1000\ \mathrm L$ total volume is $0.0500\ \mathrm M$. Now

$$
K_b=\frac{1.0\times10^{-14}}{1.8\times10^{-5}}=5.6\times10^{-10}.
$$

For acetate hydrolysis, $[OH^-]\approx\sqrt{K_bC}$:

$$
[OH^-]\approx\sqrt{(5.6\times10^{-10})(0.0500)}=5.3\times10^{-6}\ \mathrm M.
$$

Thus $\mathrm{pOH}=5.28$ and $\mathrm{pH}=8.72$. The basic equivalence point follows from acetate hydrolysis.

**After $60.0\ \mathrm{mL}$ base.** Hydroxide added is $0.00600$ mol, so $0.00100$ mol remains after neutralization. The total volume is $0.1100\ \mathrm L$:

$$
[OH^-]=\frac{0.00100}{0.1100}=9.09\times10^{-3}\ \mathrm M.
$$

Therefore $\mathrm{pOH}=2.04$ and $\mathrm{pH}=11.96$. Acetate hydrolysis is negligible beside this much excess strong base.

## Choosing an indicator and reading the endpoint

An equivalence point is theoretical; an endpoint is an observed color change or instrument response. An indicator is itself a weak acid-base pair whose two forms have different colors. Its transition range is centered roughly on its $pK_a$ and usually spans about two pH units. The chosen range should lie within the steep portion of the titration curve.

For a weak-acid/strong-base titration, the equivalence region is above pH 7, so an indicator changing on the basic side is suitable. For strong acid with strong base, several indicators work because the pH jump is broad. Weak-acid/weak-base titrations have a shallow change near equivalence; a pH meter is usually more reliable than a visual indicator.

## Failure modes worth checking

- A concentration ICE table cannot replace the initial mole calculation when solutions are mixed. Reaction stoichiometry uses moles; equilibrium uses concentrations in the final volume.
- The buffer equation needs both members of a conjugate pair. At equivalence one member has been consumed, so hydrolysis replaces the buffer calculation.
- The five-percent guideline checks an approximation; it does not determine whether an acid is weak. A very dilute weak acid can violate the approximation.
- At concentrations near $10^{-7}\ \mathrm M$, water autoionization can no longer be ignored. A naive acid-only calculation may even predict a pH above 7 for an acid solution.
- Successive $K_a$ values must remain attached to their individual dissociation steps. Combining them by addition has no equilibrium meaning; the overall constant is their product.
- Formal concentration and equilibrium concentration are different. Labels on prepared solutions normally give the analytical amount before dissociation.

## Designing a buffer rather than merely calculating one

Buffer preparation begins with a target pH and a conjugate pair whose $pK_a$ lies nearby. Henderson–Hasselbalch then supplies the required ratio, while the expected acid or base load determines the total concentration. Those are separate design choices. Raising both component concentrations by the same factor leaves the calculated pH unchanged but raises capacity.

Suppose a pH 5.00 acetate buffer is needed and $pK_a=4.74$. The required ratio follows from

$$
5.00=4.74+\log\frac{[A^-]}{[HA]}.
$$

Therefore,

$$
\frac{[A^-]}{[HA]}=10^{0.26}=1.82.
$$

If the desired total analytical concentration is $0.200\ \mathrm M$, let $[HA]=x$ and $[A^-]=1.82x$. The material balance gives

$$
x+1.82x=0.200,
$$

so $[HA]=0.0709\ \mathrm M$ and $[A^-]=0.129\ \mathrm M$. These values specify composition before activity corrections. One may prepare the pair from acetic acid and sodium acetate, or partially neutralize a known amount of acetic acid with strong base. Partial neutralization is often convenient because the neutralization stoichiometry fixes the mole ratio directly.

The calculated recipe is only a starting point for precise work. Temperature changes $K_a$, concentrated solutions depart from the concentration approximation, and added salts change activity coefficients. A calibrated pH electrode is used for final adjustment when the target tolerance is narrow. Adding strong acid or base blindly to the final volume can alter both composition and volume; prepare near the desired composition, measure, adjust carefully, and dilute to the final mark.

The buffer components should also be chemically compatible with the system. A phosphate buffer may precipitate some metal ions. Ammonia can coordinate transition metals. Acetate may participate in reactions that a nominally inert pH medium should not. Buffer selection includes chemical side reactions, temperature range, and measurement method in addition to $pK_a$.

## Distribution of protonation states

For a monoprotic acid, the fraction present as acid or conjugate base can be obtained without solving separate concentrations. Let the total analytical concentration be

$$
C_T=[HA]+[A^-].
$$

Combining this balance with

$$
K_a=\frac{[H_3O^+][A^-]}{[HA]}
$$

gives the fractional compositions

$$
\alpha_{HA}=\frac{[H_3O^+]}{[H_3O^+]+K_a},
\qquad
\alpha_{A^-}=\frac{K_a}{[H_3O^+]+K_a}.
$$

At pH equal to $pK_a$, $[H_3O^+]=K_a$ and both fractions are one half. One pH unit below $pK_a$, the protonated form is about $91\%$; one unit above, the deprotonated form is about $91\%$. This distribution view is useful for amino acids, indicators, drug ionization, and separations because charge state often controls solubility or mobility.

Polyprotic systems have several overlapping distributions. A diprotic acid can be mostly $\mathrm{H_2A}$ at low pH, mostly $\mathrm{HA^-}$ between its two $pK_a$ values, and mostly $\mathrm{A^{2-}}$ at high pH. If the two constants are close, no wide pH interval contains only the intermediate form and the simple “one step at a time” picture becomes less accurate.

## Titration data as analytical evidence

A titration curve contains more information than the unknown concentration. The equivalence volume determines the initial analyte amount through stoichiometry. The half-equivalence pH estimates $pK_a$ for a monoprotic weak acid. Multiple equivalence regions can reveal multiple ionizable groups when their stepwise constants are sufficiently separated.

Curve shape also exposes experimental problems. An equivalence volume that changes with indicator choice may indicate a poorly matched transition range or a shallow endpoint. Drift before titrant addition can signal electrode equilibration or carbon dioxide absorption. A strong base solution gradually absorbs atmospheric carbon dioxide, lowering its effective hydroxide concentration; standardization against a suitable primary standard corrects the concentration before analysis.

Gran plots and derivative plots are sometimes used to estimate equivalence more objectively, but they still rely on valid electrode response and appropriate chemical models. No numerical endpoint method repairs an unbalanced reaction, an unstandardized titrant, or an interfering reaction in the sample.

Dilution during titration affects every concentration but not the stoichiometric mole ratio. In the buffer region, the common total volume cancels from the conjugate-pair ratio. At equivalence and beyond it does not cancel from hydrolysis or excess-reagent concentrations, so the combined volume must be used. Treating all titration regions with one formula hides this change in what controls pH.

Polyprotic titrations may show separate equivalence points only when successive proton transfers differ enough in strength. Overlapping steps merge into a broad curve, and an indicator may not isolate each endpoint. The number of visible jumps is therefore not automatically the number of acidic hydrogens in the formula.

Replicate titrations should agree in delivered volume within the method's precision. Concordant endpoints reveal repeatability, while a correct concentration also requires standardized titrant and unbiased endpoint detection.

<div className="see-also">

See also: [acids, bases, and pH](/chemistry/general/acids-bases-and-ph) · [chemical equilibrium](/chemistry/general/chemical-equilibrium) · [aqueous reactions and solution stoichiometry](/chemistry/general/aqueous-reactions-and-solution-stoichiometry) · [solubility and complex-ion equilibria](/chemistry/general/solubility-and-complex-ion-equilibria)

</div>
