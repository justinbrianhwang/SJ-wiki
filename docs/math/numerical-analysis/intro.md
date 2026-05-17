---
title: Numerical Analysis
sidebar_position: 1
---

# Numerical Analysis

These notes organize Burden and Faires, *Numerical Analysis*, 9th edition, into a practical wiki path for computation, analysis, and implementation. The emphasis is the central theme of the text: numerical algorithms are useful only when their approximation error, floating-point behavior, convergence, and stability are understood together.

![The bisection method repeatedly narrows an interval around a root.](https://commons.wikimedia.org/wiki/Special:FilePath/Bisection_method.svg)

*Figure: Bisection is a robust root-finding method built from the intermediate value theorem. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Bisection_method.svg), Tokuchan after Dake, CC BY-SA 3.0.*

![Newton iteration follows tangent lines toward a root of a curve.](https://commons.wikimedia.org/wiki/Special:FilePath/Newton_iteration.svg)

*Figure: Newton iteration uses local linearization to turn calculus into a fast root-finding algorithm. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Newton_iteration.svg), Oleg Alexandrov and Pbroks13, public domain.*

![Four Runge-Kutta slope samples are drawn along one ODE step.](https://commons.wikimedia.org/wiki/Special:FilePath/Runge-Kutta_slopes.svg)

*Figure: Runge-Kutta methods combine several slope estimates to advance an ODE solution more accurately. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Runge-Kutta_slopes.svg), HilberTraum, CC BY-SA 4.0.*

The sequence starts with calculus-based error estimates and machine arithmetic, then moves through nonlinear equations, interpolation, differentiation, integration, ordinary differential equations, numerical linear algebra, approximation theory, eigenvalue problems, nonlinear systems, boundary-value problems, and finite-difference methods for partial differential equations. Each topic page follows the same study pattern: intuition, algorithm, convergence or stability analysis, a worked example, and executable Python/NumPy/SciPy-style code.

Use the pages in order for a first pass; later, jump directly to the method family needed for a computation.

1. [Numerical Analysis](./intro.md)
2. [Mathematical Preliminaries and Error Analysis](./mathematical-preliminaries-error-analysis.md)
3. [Floating Point Conditioning and Stability](./floating-point-conditioning-stability.md)
4. [Bisection and Fixed Point Iteration](./bisection-fixed-point.md)
5. [Newton Secant and Polynomial Roots](./newton-secant-polynomial-roots.md)
6. [Lagrange Interpolation and Neville Method](./interpolation-lagrange-neville.md)
7. [Divided Differences and Hermite Interpolation](./divided-differences-hermite.md)
8. [Cubic Splines and Parametric Curves](./cubic-splines-parametric-curves.md)
9. [Numerical Differentiation and Richardson Extrapolation](./numerical-differentiation-richardson.md)
10. [Newton Cotes and Romberg Integration](./newton-cotes-romberg-integration.md)
11. [Adaptive and Gaussian Quadrature](./adaptive-gaussian-quadrature.md)
12. [Euler Taylor and Runge Kutta Methods](./euler-taylor-runge-kutta.md)
13. [Adaptive Runge Kutta and Multistep Methods](./adaptive-runge-kutta-multistep.md)
14. [ODE Stability Stiffness and Systems](./ode-stability-stiffness-systems.md)
15. [Gaussian Elimination Pivoting and LU](./gaussian-elimination-pivoting-lu.md)
16. [Matrix Factorizations and Special Systems](./matrix-factorizations-special-systems.md)
17. [Jacobi Gauss Seidel and SOR](./iterative-linear-systems.md)
18. [Conjugate Gradient and Iterative Refinement](./conjugate-gradient-iterative-refinement.md)
19. [Least Squares and Chebyshev Approximation](./least-squares-chebyshev-approximation.md)
20. [Rational Trigonometric Approximation and FFT](./rational-trigonometric-fft.md)
21. [Eigenvalue Methods](./eigenvalue-methods.md)
22. [Nonlinear Systems](./nonlinear-systems.md)
23. [Boundary Value Problems](./boundary-value-problems.md)
24. [Finite Difference Methods for PDEs](./finite-difference-pdes.md)
