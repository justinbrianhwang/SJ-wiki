---
title: First-Order ODEs
sidebar_position: 2
---

# First-Order ODEs

A first-order ordinary differential equation relates an unknown function to its first derivative. In models, that derivative is usually a rate: heat leaving a body, charge changing in a circuit, material entering a tank, or a population responding to crowding. Solving the algebra is only part of the job. The initial condition, domain, units, and maximal interval determine what the formula actually represents.

## Recognize the structure before manipulating it

An equation may be implicit,

$$
F(x,y,y')=0,
$$

or explicit,

$$
y'=f(x,y).
$$

An initial condition $y(x_0)=y_0$ selects a curve from a family when existence and uniqueness apply. Recognition determines the useful first move:

| Form | Recognition cue | Main move |
|---|---|---|
| separable | $y'=g(x)h(y)$ | place $y$ terms with $dy$ and $x$ terms with $dx$ |
| linear | $y'+p(x)y=r(x)$ | multiply by an integrating factor |
| exact | $M(x,y)\,dx+N(x,y)\,dy=0$ with $M_y=N_x$ | recover a potential function |
| Bernoulli | $y'+p(x)y=g(x)y^a$ | substitute $v=y^{1-a}$ |
| homogeneous ratio | $y'=F(y/x)$ | set $y=vx$ |
| autonomous | $y'=f(y)$ | locate equilibria and use separation or a phase line |

These classes overlap. An equation can be both separable and linear; use whichever path has less algebra. If no pattern fits, qualitative analysis or a numerical solver is a legitimate method rather than a last-resort symbolic failure.

Before dividing by an expression involving $y$, record its zeros. Before taking logarithms or roots, record sign restrictions. After finding a formula, substitute it into the original equation and apply the initial condition. These checks catch most missing branches and sign errors.

## Separation preserves a balance of differentials

For

$$
\frac{dy}{dx}=g(x)h(y),
$$

and on a region where $h(y)\ne0$, rearrange and integrate:

$$
\frac{1}{h(y)}\,dy=g(x)\,dx,
$$

$$
\int\frac{1}{h(y)}\,dy
=\int g(x)\,dx+C.
$$

The resulting relation may stay implicit. Solving explicitly for $y$ is useful only when it is possible and does not obscure branches.

Division by $h(y)$ discards any constant solution satisfying $h(y_*)=0$. These equilibria must be checked separately. They often carry the most important long-term behavior in an autonomous model.

### Worked example: logistic growth

Solve

$$
y'=0.3y\left(1-\frac{y}{12}\right),
\qquad y(0)=3.
$$

The equilibrium solutions are $y=0$ and $y=12$. The initial value is neither, so separation is allowed near the solution:

$$
\frac{dy}{y(1-y/12)}=0.3\,dt.
$$

Since $1-y/12=(12-y)/12$,

$$
\frac{1}{y(1-y/12)}
=\frac{12}{y(12-y)}
=\frac1y+\frac{1}{12-y}.
$$

Integrating requires the minus sign from $d(12-y)=-dy$:

$$
\ln|y|-\ln|12-y|=0.3t+C.
$$

Combine logarithms and exponentiate:

$$
\frac{y}{12-y}=Ce^{0.3t}.
$$

The solution stays between $0$ and $12$, so no absolute-value branch change occurs. Solve for $y$:

$$
y=\frac{12Ce^{0.3t}}{1+Ce^{0.3t}}
=\frac{12}{1+C^{-1}e^{-0.3t}}.
$$

Use $y(0)=3$:

$$
3=\frac{12}{1+C^{-1}}
\quad\Longrightarrow\quad
C^{-1}=3.
$$

Thus

$$
y(t)=\frac{12}{1+3e^{-0.3t}}.
$$

At $t=0$, the formula gives $3$. As $t\to\infty$, the exponential vanishes and $y\to12$, matching the stable carrying capacity seen from the sign of the right side. The discarded equilibria $y=0$ and $y=12$ remain additional solutions for their own initial data.

## The integrating factor for linear equations

A first-order linear equation has normalized form

$$
y'+p(x)y=r(x).
$$

Seek a multiplier $\mu(x)$ that turns the left side into $(\mu y)'$. Expanding,

$$
(\mu y)'=\mu y'+\mu'y.
$$

After multiplying the ODE by $\mu$, the coefficient of $y$ is $\mu p$. Therefore require

$$
\mu'=p\mu.
$$

Its nonzero solutions are constant multiples of

$$
\mu(x)=e^{\int p(x)\,dx}.
$$

The constant multiple is irrelevant. Then

$$
(\mu y)'=\mu r,
$$

so

$$
y(x)=\frac{1}{\mu(x)}
\left(\int\mu(x)r(x)\,dx+C\right).
$$

Normalize first if the coefficient of $y'$ is not $1$. The interval must avoid points where that division or the coefficients fail.

### Worked example: salt in a mixing tank

A $100$ L tank initially contains $20$ g of salt. Brine containing $0.5$ g/L enters at $4$ L/min, and well-mixed liquid leaves at the same rate. Let $A(t)$ be the salt amount in grams.

Equal flow rates keep volume at $100$ L. The inflow rate of salt is

$$
0.5\frac{\mathrm g}{\mathrm L}
\cdot4\frac{\mathrm L}{\mathrm{min}}
=2\frac{\mathrm g}{\mathrm{min}}.
$$

The tank concentration is $A/100$ g/L, so outflow removes

$$
\frac{A}{100}\frac{\mathrm g}{\mathrm L}
\cdot4\frac{\mathrm L}{\mathrm{min}}
=\frac{A}{25}\frac{\mathrm g}{\mathrm{min}}.
$$

Rate in minus rate out gives

$$
A'+\frac1{25}A=2,
\qquad A(0)=20.
$$

The integrating factor is

$$
\mu(t)=e^{t/25}.
$$

Multiplication produces

$$
(e^{t/25}A)'=2e^{t/25}.
$$

Integrate:

$$
e^{t/25}A=50e^{t/25}+C,
$$

$$
A=50+Ce^{-t/25}.
$$

The initial condition gives $20=50+C$, so

$$
A(t)=50-30e^{-t/25}.
$$

The steady amount is $50$ g, equal to $100$ L times the incoming concentration. The solution rises from $20$ toward $50$ without overshoot, consistent with the balance law. Units also check: every term in the ODE is grams per minute.

### Shifting by the steady state

Constant-forcing linear equations become especially clear after subtracting equilibrium. If

$$
y'+ky=b,
\qquad k\ne0,
$$

the constant steady value is $y_*=b/k$. Set $u=y-y_*$. Since $y_*'=0$ and $ky_*=b$, substitution gives

$$
u'+ku=0.
$$

Thus

$$
y(x)=y_*+Ce^{-kx}.
$$

This derivation separates the long-term level from the transient. For the tank, $A_*=2/(1/25)=50$ and $A-50=-30e^{-t/25}$. The time constant is $25$ minutes: after one time constant, the displacement from equilibrium is multiplied by $e^{-1}$.

Newton cooling has the same structure. If a body at temperature $T$ sits in constant ambient temperature $T_a$ and obeys

$$
T'=-k(T-T_a),
$$

then $u=T-T_a$ satisfies $u'=-ku$. Hence

$$
T(t)=T_a+(T_0-T_a)e^{-kt}.
$$

For $k\gt 0$, the sign of $T-T_a$ never changes in the ideal model: an initially hotter body approaches ambient from above, while a colder one approaches from below. If ambient temperature varies with time, the equation remains linear but the steady-state shift is no longer constant; the integrating-factor method handles the forcing $kT_a(t)$.

## Exact equations recover a hidden potential

Write an implicit first-order equation as

$$
M(x,y)\,dx+N(x,y)\,dy=0.
$$

It is exact on a suitable region if a function $U$ exists with

$$
U_x=M,
\qquad U_y=N.
$$

Then along a solution,

$$
\frac{d}{dx}U(x,y(x))
=U_x+U_yy'=0,
$$

and the solution curves are level sets $U(x,y)=C$.

With continuous first partial derivatives on a simply connected region, the test is

$$
M_y=N_x.
$$

To construct $U$, integrate one component while treating the other variable as constant, then recover the missing single-variable term from the other derivative.

For example, solve

$$
(2xy+3)\,dx+(x^2+4y)\,dy=0.
$$

Here

$$
M_y=2x,
\qquad N_x=2x,
$$

so the equation is exact on $\mathbb R^2$. Integrate $M$ with respect to $x$:

$$
U=x^2y+3x+g(y).
$$

Differentiate with respect to $y$ and compare with $N$:

$$
U_y=x^2+g'(y)=x^2+4y.
$$

Thus $g'(y)=4y$ and $g(y)=2y^2$. The implicit family is

$$
x^2y+3x+2y^2=C.
$$

For an initial condition $y(0)=1$, $C=2$. Leaving the answer implicit avoids an unnecessary quadratic formula and keeps both possible local branches apparent. The implicit-function theorem determines where a branch can be solved locally for $y$.

Some nonexact equations become exact after multiplication by an integrating factor. If $(M_y-N_x)/N$ depends only on $x$, then an $x$-dependent factor may be found by exponentiating its integral. A similar criterion using $(N_x-M_y)/M$ applies to a factor depending only on $y$. These tests cover special cases, not every nonexact equation.

## Bernoulli equations become linear after a power change

A Bernoulli equation has form

$$
y'+p(x)y=g(x)y^a,
\qquad a\ne0,1.
$$

Set $v=y^{1-a}$. Since

$$
v'=(1-a)y^{-a}y',
$$

division by $y^a$ and multiplication by $1-a$ gives the linear equation

$$
v'+(1-a)p(x)v=(1-a)g(x).
$$

For

$$
y'+\frac2x y=x^2y^2,
\qquad x>0,
$$

take $v=y^{-1}$. Dividing by $y^2$ for nonzero solutions gives

$$
-v'+\frac2xv=x^2,
$$

or

$$
v'-\frac2xv=-x^2.
$$

The integrating factor is

$$
e^{\int-2/x\,dx}=x^{-2}
$$

on $x\gt 0$. Therefore

$$
(x^{-2}v)'=-1,
$$

$$
x^{-2}v=-x+C,
$$

$$
v=Cx^2-x^3.
$$

Returning to $y$,

$$
y(x)=\frac{1}{x^2(C-x)}.
$$

Division by $y^2$ omitted $y=0$, which is also a solution. The formula's interval cannot cross $x=0$ or $x=C$ and must be restricted to the connected interval containing any specified initial point.

## Homogeneous ratio substitutions

An equation of the form

$$
y'=F(y/x)
$$

is called homogeneous in this first-order sense; it is unrelated to the use of “homogeneous” for a linear equation with zero forcing. Set

$$
y=vx,
\qquad y'=v+xv'.
$$

Then

$$
v+xv'=F(v),
$$

which is separable if $F(v)-v$ can be handled. Lines $y=vx$ for roots of $F(v)=v$ may be lost during division and should be restored.

Translated ratios such as $(y-b)/(x-a)$ suggest shifting coordinates first. The substitution works only on intervals that avoid $x=0$ in the original ratio, or $x=a$ after translation.

## Solution intervals and singular behavior

An algebraic expression without an interval is incomplete. The initial point selects one connected interval on which the formula and the original equation are defined. For

$$
y'=y^2,
\qquad y(0)=1,
$$

the solution $y=1/(1-x)$ has maximal interval $(-\infty,1)$, not merely “$x\ne1$.” The disconnected interval $(1,\infty)$ does not contain the initial point.

Finite endpoints can arise from a coefficient singularity, a boundary of the domain of $f$, or blow-up of the solution. The local existence theorem does not promise a global solution. A numerical solver also cannot be trusted past such a boundary merely because it returns numbers.

When symbolic recognition fails, a solver should report its interval, tolerances, and event conditions. Known invariants and equilibria make good numerical checks. For the tank model, for example, a computed solution should remain between $20$ and $50$ and approach $50$ monotonically.

## A compact verification routine

After solving, run these checks in order:

- Differentiate the candidate and substitute into the original equation, before any divided form.
- Apply the initial condition to the final expression.
- Restore equilibrium or zero solutions lost by division.
- State the maximal connected interval containing the initial point.
- Check units in modeled equations and signs in rate-in-minus-rate-out balances.
- Compare limiting behavior with equilibria or the direction field.
- For implicit solutions, differentiate implicitly rather than forcing an explicit branch.

These checks are method-independent. They also catch solutions introduced by squaring, exponentiating, or choosing an incompatible logarithm branch.

## Modeling starts before the differential equation

A state variable should contain enough information to determine its rate under the model. In a mixing tank, amount is a better state than concentration when volume changes, because amount obeys a direct conservation balance. In cooling, temperature difference from ambient isolates the decaying part. In a circuit, charge or current may be natural depending on the element law and the measured output.

Every rate term needs a sign convention and units. “Rate in minus rate out” is reliable only after each stream has been converted to amount per unit time. A concentration cannot be subtracted from a mass flow. If the volume varies, the outflow concentration uses the current volume, and the time interval ends if the tank empties or overflows under the stated physical setup.

Parameters also encode assumptions. A constant cooling coefficient assumes the heat-transfer regime and surrounding conditions remain suitable. Logistic growth assumes a fixed carrying capacity and an instantaneous density effect. A good solution distinguishes what follows from the differential equation from what was assumed when selecting it.

Steady states provide an early plausibility check. Set the rate to zero before solving. Their units and signs should fit the system, and the vector field should point toward or away from them as the modeled mechanism suggests. If a tank solution approaches an amount inconsistent with incoming concentration and volume, the balance law was probably assembled incorrectly.

## Implicit solutions and branch selection

An implicit relation can describe several branches at once. The initial condition selects a point, and local uniqueness selects the branch through it. Solving algebraically for the dependent variable may introduce plus-or-minus choices; only a branch satisfying the initial value and differentiability requirements belongs to the initial value problem.

The implicit-function condition also identifies where an explicit graph can fail. If the derivative of the implicit relation with respect to the dependent variable vanishes, solving locally for that variable may become impossible even though the level curve continues. Such points deserve direct substitution into the original differential equation rather than blind differentiation of a chosen branch.

Logarithmic implicit answers carry hidden sign intervals. An equation involving the logarithm of an absolute value is valid on components that avoid its zeros. Exponentiating introduces a nonzero constant whose sign may distinguish solution regions. Absorbing every sign into an unnamed constant is convenient, but the initial condition must still place the solution in the correct region.

## Long-time behavior without a closed form

For an autonomous scalar equation, the phase line often determines the limit. A bounded monotone solution has a finite limit. Under continuity, substituting that limiting behavior into the field shows that the limit must be an equilibrium; otherwise the derivative would retain a sign bounded away from zero and the solution could not settle.

This argument needs boundedness and continued existence. A monotonically increasing solution can instead blow up in finite time, as the quadratic growth example shows. An equilibrium barrier and uniqueness can supply the needed bound. When no such barrier exists, comparison with a simpler equation can reveal growth or blow-up.

Linear equations separate transient and forced response. With positive decay coefficient, the memory of initial data is multiplied by a decaying exponential. The forcing contributes a weighted history, with recent values often receiving more weight than distant ones. This interpretation remains useful even when the forcing integral has no elementary antiderivative.

Periodic forcing does not automatically produce a periodic total solution. A decaying transient may accompany a periodic steady response; only after the transient dies out does the observed motion approach periodic behavior. Initial conditions determine the transient amplitude, while the equation and forcing determine the steady response.

## Comparing symbolic and numerical answers

A symbolic expression should be evaluated near the initial point and near suspected singularities. Cancellation can hide loss of precision, while a mathematically equivalent form may behave better numerically. Exponentials with large opposite terms and differences of nearly equal quantities need particular care.

Numerical solvers estimate local error and adjust step size, but tolerances are not guarantees of model accuracy. Event detection should stop integration at empty-tank times, impacts, or singular boundaries. A solver that steps past such an event is computing an extension of the equations, not necessarily an extension of the physical system.

When an exact solution is available, compare numerical error across several tolerances or step sizes. When it is not, compare independent methods, monitor conserved or bounded quantities, and inspect residuals obtained by substituting an interpolated numerical solution into the equation. Agreement of a single plotted curve with intuition is weak evidence.

<div className="see-also">

See also: [Direction fields and existence](/math/engineering-math/direction-fields-and-existence) · [Second-order linear ODEs](/math/engineering-math/second-order-linear-odes) · [Systems of ODEs and phase planes](/math/engineering-math/systems-of-odes-and-phase-plane) · [Laplace transform](/math/engineering-math/laplace-transform) · [Numerical methods overview](/math/engineering-math/numerical-methods-overview)

</div>
