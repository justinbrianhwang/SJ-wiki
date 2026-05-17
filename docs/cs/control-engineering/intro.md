---
title: Control Engineering
sidebar_position: 1
---

# Control Engineering

These notes synthesize the standard undergraduate sequence in Norman S. Nise's *Control Systems Engineering*, 7th ed. The section begins with feedback configurations and the design process, then develops transfer-function and state-space models for electrical, mechanical, electromechanical, and sampled-data systems. The central analysis themes are transient response, steady-state error, and stability; the design themes are root locus, Bode/Nyquist frequency response, classical compensation, state feedback, observers, and digital implementation.

![An inverted pendulum on a cart shows the unstable plant used in many control examples.](https://commons.wikimedia.org/wiki/Special:FilePath/Cart-pendulum.svg)

*Figure: The cart-pendulum is a concrete plant for modeling, stabilization, and control design. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cart-pendulum.svg), Krishnavedala, CC0.*

![A historical centrifugal governor drawing shows rotating flyballs regulating engine speed.](https://commons.wikimedia.org/wiki/Special:FilePath/Centrifugal_governor.png)

*Figure: The centrifugal governor is an early mechanical feedback-control apparatus. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Centrifugal_governor.png), R. Routledge, public domain.*

![A feedback control block diagram shows compensators wrapped around a plant.](https://commons.wikimedia.org/wiki/Special:FilePath/Control_System.svg)

*Figure: The standard feedback loop keeps control pages tied to the plant-controller interface. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Control_System.svg), Inductiveload, public domain.*

The emphasis is practical: every model should state its assumptions, every controller should be checked for stability and error performance, and every elegant pole-zero calculation should survive simulation and implementation constraints. Nise's treatment is primarily linear and time-invariant, so the nonlinear page is included as a short bridge showing where saturation, dead zone, phase-plane thinking, describing functions, and Lyapunov ideas enter after the linear course.

The pages are written to be read in order, but they also work as references for specific tasks. If you are deriving a plant model, start with transfer functions, physical modeling, and state space. If you are checking a proposed design, use time response, Routh-Hurwitz, steady-state error, and margins. If you are implementing a controller, read the compensator, digital-control, and embedded connections carefully because sampling, saturation, and actuator limits often decide whether the textbook design survives contact with hardware.

## Pages

1. [Introduction to Feedback Control](/cs/control-engineering/introduction-to-feedback-control)
2. [Laplace Transfer Functions and Linearization](/cs/control-engineering/laplace-transfer-functions-and-linearization)
3. [Physical System Modeling in the Frequency Domain](/cs/control-engineering/physical-system-modeling-frequency-domain)
4. [State-Space Modeling and Conversions](/cs/control-engineering/state-space-modeling-and-conversions)
5. [Time Response of First- and Second-Order Systems](/cs/control-engineering/time-response-first-and-second-order)
6. [Block Diagrams, Signal Flow, and Mason Rule](/cs/control-engineering/block-diagrams-signal-flow-and-mason)
7. [Routh-Hurwitz Stability](/cs/control-engineering/routh-hurwitz-stability)
8. [Steady-State Errors and Sensitivity](/cs/control-engineering/steady-state-errors-and-sensitivity)
9. [Root Locus Sketching and Analysis](/cs/control-engineering/root-locus-sketching-and-analysis)
10. [Root Locus Design and Classical Compensation](/cs/control-engineering/root-locus-design-and-classical-compensation)
11. [PID, Lead, Lag, and Lag-Lead Compensators](/cs/control-engineering/pid-lead-lag-and-lag-lead-compensators)
12. [Bode Plots and Frequency Response](/cs/control-engineering/bode-plots-and-frequency-response)
13. [Nyquist and Frequency Stability Margins](/cs/control-engineering/nyquist-and-frequency-stability-margins)
14. [Frequency-Response Compensator Design](/cs/control-engineering/frequency-response-compensator-design)
15. [State-Space Controller and Observer Design](/cs/control-engineering/state-space-controller-observer-design)
16. [Digital Control, Sampling, and the z-Transform](/cs/control-engineering/digital-control-sampling-and-z-transform)
17. [z-Plane Design and Digital Compensators](/cs/control-engineering/z-plane-design-and-digital-compensators)
18. [Nonlinear Control Basics](/cs/control-engineering/nonlinear-control-basics)
