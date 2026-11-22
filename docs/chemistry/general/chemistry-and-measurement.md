---
title: Chemistry and Measurement
sidebar_position: 2
---

# Chemistry and Measurement

Chemistry connects molecular claims to observations that other people can repeat. A color change may suggest reaction, but mass, temperature, pressure, spectrum, or composition gives the observation a scale. Every reported number combines a magnitude, a unit, and some statement—explicit or implicit—about uncertainty.

Measurement is therefore part of the chemical argument. An answer with no units is incomplete; an answer with more digits than the experiment supports is misleading; an answer with correct arithmetic but an uncalibrated instrument may still be wrong.

## From observation to a testable claim

A qualitative observation describes a property without assigning a numerical value: a solid forms, the solution becomes blue, or gas bubbles appear. A quantitative observation includes a measurement, such as a $2.31\ \mathrm g$ mass increase or a $6.4\ ^\circ\mathrm C$ temperature rise.

A hypothesis is a testable proposed explanation. It should lead to predictions that could fail. Experiments compare those predictions with observations while controlling alternative causes. Repeated agreement strengthens support but does not turn a hypothesis into logical certainty.

A scientific law summarizes a reproducible relationship, often mathematically. A theory provides a broad explanatory framework. One does not mature into the other: a gas law describes a relationship among variables, while kinetic molecular theory explains that relationship using particle motion.

Models deliberately omit detail. The ideal-gas model works well under many conditions even though real molecules attract one another and occupy volume. A model is judged by the range and accuracy of its predictions, not by whether every part is literally exact.

## Classifying what is being measured

Matter is anything with mass and volume. A pure substance has a fixed chemical identity and composition; a mixture contains more than one substance with variable proportions. Elements cannot be decomposed into simpler substances by ordinary chemical means. Compounds contain elements in fixed ratios and can be chemically decomposed.

Homogeneous mixtures have uniform macroscopic composition and are called solutions. Heterogeneous mixtures contain distinct regions or phases. Classification depends on scale: milk looks uniform to the eye but is a colloidal dispersion under closer examination.

Physical properties can be observed without changing chemical identity: density, melting point, and electrical conductivity are examples. Chemical properties describe the ability to undergo chemical change, such as combustion or reaction with acid. A phase change is physical; electrolysis of water is chemical because new substances form.

An **intensive** property does not scale with sample amount, while an **extensive** property does. Temperature and density are intensive; mass and volume are extensive. Ratios of extensive properties can be intensive: doubling a uniform sample doubles both mass and volume but leaves $m/V$ unchanged.

## Units carry the physical meaning

The International System of Units provides a coherent base. Chemistry often uses convenient accepted units such as liters and degrees Celsius alongside SI units.

| Quantity | SI unit | Common chemistry units | Comment |
|---|---|---|---|
| mass | kilogram, kg | gram, milligram | balances commonly read in grams |
| length | meter, m | centimeter, nanometer | molecular dimensions are often nanometers |
| time | second, s | minute, hour | conversion may be needed in rate constants |
| temperature | kelvin, K | degree Celsius | proportional laws require kelvin |
| amount | mole, mol | millimole | counts entities through Avogadro's constant |
| volume | cubic meter, $\mathrm{m^3}$ | liter, milliliter | $1\ \mathrm{mL}=1\ \mathrm{cm^3}$ exactly |
| pressure | pascal, Pa | bar, atmosphere, torr | match the gas constant to the pressure unit |

Metric prefixes are powers of ten: kilo is $10^3$, centi is $10^{-2}$, milli is $10^{-3}$, micro is $10^{-6}$, and nano is $10^{-9}$. Prefixes attach to the unit before powers are applied. Thus

$$
1\ \mathrm{cm^3}=(10^{-2}\ \mathrm m)^3=10^{-6}\ \mathrm{m^3},
$$

not $10^{-2}\ \mathrm{m^3}$.

Temperature needs special care. Celsius and kelvin increments have the same size, but their zero points differ:

$$
T_K=T_{^\circ C}+273.15.
$$

A temperature difference of $10\ ^\circ\mathrm C$ equals a difference of $10\ \mathrm K$, yet $20\ ^\circ\mathrm C$ is not twice as hot as $10\ ^\circ\mathrm C$. Ratios and reciprocal temperatures require an absolute scale.

## Dimensional analysis as equation checking

A conversion factor is a ratio of equal quantities and therefore has numerical value one. Orient each factor so unwanted units cancel. The remaining unit should match the requested quantity.

For example, convert $72.0\ \mathrm{km\,h^{-1}}$ to meters per second:

$$
72.0\ \frac{\mathrm{km}}{\mathrm h}
\left(\frac{1000\ \mathrm m}{1\ \mathrm{km}}\right)
\left(\frac{1\ \mathrm h}{3600\ \mathrm s}\right)
=20.0\ \mathrm{m\,s^{-1}}.
$$

Kilometers and hours cancel. A factor reversed by mistake leaves an obviously unsuitable compound unit. Dimensional consistency cannot prove that an equation is physically correct, but inconsistency proves that it is wrong.

Units also reveal missing powers. Area conversion requires squaring the length conversion; volume requires cubing it. A density conversion from $\mathrm{g\,mL^{-1}}$ to $\mathrm{kg\,m^{-3}}$ changes both numerator and denominator.

### Worked example: a concentration conversion chain

A solution contains $25.0\ \mathrm{mg}$ solute per $5.00\ \mathrm{mL}$. Express the concentration in $\mathrm{g\,L^{-1}}$.

Start with the measured ratio and choose factors that remove milligrams and milliliters:

$$
\frac{25.0\ \mathrm{mg}}{5.00\ \mathrm{mL}}
\left(\frac{1\ \mathrm g}{1000\ \mathrm{mg}}\right)
\left(\frac{1000\ \mathrm{mL}}{1\ \mathrm L}\right).
$$

Cancel the units:

$$
\frac{\cancel{\mathrm{mg}}}{\cancel{\mathrm{mL}}}
\frac{\mathrm g}{\cancel{\mathrm{mg}}}
\frac{\cancel{\mathrm{mL}}}{\mathrm L}
=\mathrm{g\,L^{-1}}.
$$

Numerically, the powers of 1000 cancel:

$$
\frac{25.0}{5.00}=5.00\ \mathrm{g\,L^{-1}}.
$$

Both measured values have three significant figures, so the result has three. The cancellation also gives a quick scale check: $1\ \mathrm{mg\,mL^{-1}}=1\ \mathrm{g\,L^{-1}}$.

## Precision, accuracy, and kinds of error

**Precision** describes agreement among repeated measurements. **Accuracy** describes agreement with an accepted or reference value. A set can be tightly clustered but shifted from the correct value, giving high precision and poor accuracy.

Random error changes unpredictably among trials and causes scatter. Repeating measurements and averaging can reduce its influence on the mean. Systematic error biases results in a consistent direction: a balance with a zero offset or a volumetric pipette calibrated incorrectly. Repetition does not remove systematic bias; calibration, blanks, standards, and method comparison are needed.

Percent error compares one measured result with an accepted value:

$$
\%\ \mathrm{error}
=\frac{|\mathrm{measured}-\mathrm{accepted}|}
{\mathrm{accepted}}\times100\%.
$$

Absolute value reports magnitude. If the direction of bias matters, signed relative error may be more informative. Percent difference is used when comparing two experimental values without treating either as accepted; it commonly divides their absolute difference by their average.

Uncertainty is not identical to error. Error is the unknowable exact difference from the true value; uncertainty estimates the plausible range associated with a result. A complete high-quality report may use notation such as $(10.42\pm0.03)\ \mathrm{mL}$ and state the confidence or method used to obtain the uncertainty.

### Worked example: accuracy and precision in a calibration check

Four measurements of a $10.00\ \mathrm g$ reference mass are $9.82$, $9.83$, $9.82$, and $9.83\ \mathrm g$.

Their mean is

$$
\bar x=\frac{9.82+9.83+9.82+9.83}{4}=9.825\ \mathrm g.
$$

The range is only

$$
9.83-9.82=0.01\ \mathrm g,
$$

so the readings are closely grouped. The mean percent error is

$$
\frac{|9.825-10.00|}{10.00}\times100\%=1.75\%.
$$

The measurements are precise relative to their spread but inaccurate relative to the reference. A persistent calibration or tare error is more plausible than random scatter. Averaging hundreds of similarly biased readings would give a more precise estimate of the wrong value.

## Significant figures are a reporting convention

Digits known from the instrument plus one estimated digit are recorded in an analog reading. A digital instrument reports to its displayed resolution, though the true uncertainty may be larger than the last digit. Significant figures communicate resolution compactly when a full uncertainty analysis is unavailable.

The main counting conventions are:

- Nonzero digits are significant.
- Zeros between nonzero digits are significant.
- Leading zeros locate the decimal and are not significant.
- Trailing zeros after a decimal point are significant.
- Trailing zeros in an integer without a decimal marker are ambiguous; scientific notation resolves the ambiguity.

Thus $0.00450$ has three significant figures. Writing $1.20\times10^3$ states three significant figures, whereas $1.2\times10^3$ states two.

For multiplication and division, the result is normally rounded to the fewest significant figures among measured inputs. For addition and subtraction, it is rounded to the least precise decimal place. These different rules reflect the operations: addition combines absolute place resolution, while multiplication combines relative resolution.

Exact counts and defined conversions do not limit significant figures. There are exactly three samples if they were counted, and $1\ \mathrm m=100\ \mathrm{cm}$ by definition. A measured “3 m” length, however, may have only one significant figure; context determines whether a number is counted, defined, or measured.

Keep guard digits through intermediate steps and round once at the end. Repeated rounding can shift the final answer. When the discarded digits begin with exactly 5 and nothing else, different rounding conventions exist; scientific software may use round-to-even to reduce aggregate bias.

### Worked example: mixed arithmetic and reporting

Suppose a mass is found by difference:

$$
m=18.462\ \mathrm g-12.1\ \mathrm g.
$$

The unrounded difference is $6.362\ \mathrm g$, but subtraction is limited to the tenths place by $12.1\ \mathrm g$, so the report is

$$
m=6.4\ \mathrm g.
$$

If that mass is divided by a measured volume of $2.35\ \mathrm{mL}$, use the unrounded difference as a guard value:

$$
d=\frac{6.362\ \mathrm g}{2.35\ \mathrm{mL}}
=2.707\ldots\ \mathrm{g\,mL^{-1}}.
$$

The mass difference is effectively known only to about two significant figures after the subtraction rule, so a conservative final report is

$$
d=2.7\ \mathrm{g\,mL^{-1}}.
$$

Writing $2.70723\ \mathrm{g\,mL^{-1}}$ would preserve calculator output rather than experimental information.

## Density combines two measurements

Density is

$$
d=\frac{m}{V}.
$$

It is temperature dependent because volume changes with temperature. The density of a pure substance under stated conditions can help identify it, but a match alone is not conclusive when several materials have similar values.

### Worked example: volume by displacement

A metal sample has mass $37.50\ \mathrm g$. In a graduated cylinder, water rises from $21.30\ \mathrm{mL}$ to $26.06\ \mathrm{mL}$ when the sample is fully submerged.

The sample volume is the displacement:

$$
V=26.06-21.30=4.76\ \mathrm{mL}.
$$

Both cylinder readings extend to the hundredths place, so their difference does too. Density is

$$
d=\frac{37.50\ \mathrm g}{4.76\ \mathrm{mL}}
=7.878\ldots\ \mathrm{g\,mL^{-1}}.
$$

The volume has three significant figures and limits the division:

$$
d=7.88\ \mathrm{g\,mL^{-1}}.
$$

The result is plausible for a dense metal and predicts sinking in water. Air bubbles attached to the sample would increase apparent displaced volume and bias the calculated density low. Dissolution or reaction with water would invalidate the method altogether.

## Calibration and experimental records

Calibration compares an instrument response with standards traceable to known values. A calibration curve should cover the sample range; extrapolating far beyond the standards assumes response behavior that has not been tested. A blank measures background from solvents, reagents, and the container so it can be separated from the analyte signal.

Glassware is chosen by the required task. A beaker gives rough volume, a graduated cylinder gives moderate precision, a volumetric pipette delivers one calibrated volume accurately, and a burette measures variable delivered volume from the difference of two readings. More digits written from inappropriate glassware do not create more information.

Record raw observations, units, instrument identity, calibration state, temperature where relevant, and any deviations while the experiment is running. Reconstructing details later invites selective memory. Unexpected results should be retained and investigated rather than silently deleted; excluding a value needs a stated technical reason.

## Final checks on a numerical result

- Carry units through every line. Correct cancellation is an independent check on setup.
- Estimate the order of magnitude before calculating. Prefix mistakes often shift an answer by factors of $10^3$ or more.
- Separate random scatter from systematic bias. Replication addresses the former more readily than the latter.
- Do not infer uncertainty solely from the number of displayed digits. Resolution, calibration, and method variability all contribute.
- Use kelvin in ratios, reciprocal temperatures, gas laws, and thermodynamic equations. Celsius is suitable for many reported conditions and temperature differences.
- Round at the end and preserve guard digits internally. The reported precision should follow the least informative measurement, not the calculator display.

## Combining uncertainties

Significant-figure rules are a compact classroom convention. When numerical uncertainties are available, propagation gives a clearer result. For independent quantities added or subtracted, absolute variances add approximately:

$$
u_z=\sqrt{u_x^2+u_y^2}.
$$

For multiplication or division, relative variances add approximately:

$$
\left(\frac{u_z}{z}\right)^2
=
\left(\frac{u_x}{x}\right)^2
+
\left(\frac{u_y}{y}\right)^2.
$$

Suppose mass is $(12.50\pm0.01)\ \mathrm g$ and volume is $(5.00\pm0.02)\ \mathrm{mL}$. Density is $2.500\ \mathrm{g\,mL^{-1}}$. Its relative uncertainty is

$$
\sqrt{(0.01/12.50)^2+(0.02/5.00)^2}=0.00408.
$$

The absolute uncertainty is

$$
u_d=(2.500)(0.00408)=0.0102\ \mathrm{g\,mL^{-1}}.
$$

A sensible report is $(2.50\pm0.01)\ \mathrm{g\,mL^{-1}}$. Correlated inputs require covariance terms; the independent-error formula cannot be used blindly when the same calibration affects both quantities.

## Separating a signal from a detection claim

Analytical measurements include background noise and blanks. A small positive response does not automatically prove that analyte is present. A detection limit concerns whether a signal can be distinguished from background with a stated error rate; a quantitation limit is higher and concerns whether an amount can be estimated with acceptable precision.

Replicate blanks characterize background variation. Calibration standards establish sensitivity. Samples outside the calibrated range should be diluted or measured with a suitable range rather than extrapolated casually. Reporting “zero” when a signal is below detection is also inaccurate; the defensible statement is that the analyte was not detected above the method limit.

Reference materials and spiked samples test different failure modes. A reference material checks the full method against a known composition. A spike adds a known amount to the actual sample and reveals matrix suppression or enhancement. Good agreement on clean standards alone does not show that a complex sample behaves the same way.

## Reproducibility in the notebook

A result can be repeated only if the record preserves sample identity, reagent lots or concentrations, instrument settings, calibration data, environmental conditions that matter, and the calculation path from raw signal to reported value. Units and unrounded values should remain in the record even when the final report is rounded.

Corrections should leave the original entry readable and state why it changed. Selective removal of inconvenient trials biases the record. If a trial is excluded because of a spill, bubble, instrument fault, or failed control, note that reason before looking at whether exclusion improves the desired result.

<div className="see-also">

See also: [atoms, molecules, and ions](/chemistry/general/atoms-molecules-and-ions) · [stoichiometry](/chemistry/general/stoichiometry) · [gases](/chemistry/general/gases) · [thermochemistry](/chemistry/general/thermochemistry)

</div>
