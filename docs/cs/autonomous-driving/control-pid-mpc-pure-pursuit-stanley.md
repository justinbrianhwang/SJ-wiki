---
title: Control, PID, MPC, Pure Pursuit, and Stanley
sidebar_position: 11
---

# Control, PID, MPC, Pure Pursuit, and Stanley

Control turns a planned trajectory into steering, throttle, and braking commands. It is where elegant trajectories meet tire friction, actuator delay, sensor noise, slopes, load transfer, and imperfect vehicle models. In autonomous driving, longitudinal control manages speed and headway, while lateral control manages path tracking. A good controller is stable, smooth, robust, and honest about the limits of the plan it is asked to follow.

This page introduces PID, pure pursuit, Stanley control, model predictive control, and the kinematic and dynamic bicycle models. It connects [motion planning](/cs/autonomous-driving/motion-planning) to [embedded implementation](/cs/embedded/) and [engineering math](/math/engineering-math/), because control is both mathematical and deeply physical.

## Definitions

**Longitudinal control** regulates speed, acceleration, and spacing using throttle and brakes. Adaptive cruise control and stop-and-go traffic control are longitudinal problems.

**Lateral control** regulates cross-track error and heading error using steering. Lane keeping, path following, and obstacle-avoidance tracking are lateral problems.

**PID control** uses proportional, integral, and derivative terms:

$$
u(t)=K_p e(t)+K_i\int_0^t e(\tau)d\tau+K_d\frac{de}{dt}.
$$

The proportional term reacts to current error, the integral term removes steady-state bias, and the derivative term damps fast changes.

**Pure pursuit** chooses a lookahead point on the reference path and steers toward it. For wheelbase $L$, lookahead distance $\ell_d$, and angle $\alpha$ to the lookahead point, a common steering law is:

$$
\delta = \arctan\left(\frac{2L\sin\alpha}{\ell_d}\right).
$$

**Stanley control** combines heading error and cross-track error:

$$
\delta = \psi_e + \arctan\left(\frac{k e_c}{v+\epsilon}\right),
$$

where $\psi_e$ is heading error, $e_c$ cross-track error, $v$ speed, $k$ gain, and $\epsilon$ prevents division by zero.

**MPC** solves a constrained control problem over a finite horizon, using a vehicle model and cost function. It can handle actuator limits and coupled lateral-longitudinal behavior.

The **kinematic bicycle model** assumes no tire slip and is useful at low to moderate speeds. The **dynamic bicycle model** includes tire forces and slip angles, which matter near handling limits, high speed, or low-friction surfaces.

## Key results

Ackermann steering geometry relates steering angle and turn radius:

$$
\tan\delta = \frac{L}{R},
\quad
\kappa = \frac{1}{R} = \frac{\tan\delta}{L}.
$$

This relation appears in planning and control. A planned path with curvature beyond $\tan(\delta_{\max})/L$ cannot be tracked by steering alone.

Pure pursuit is geometrically intuitive. Increasing lookahead distance smooths steering but cuts corners and reacts slowly. Decreasing lookahead improves tight tracking but can cause oscillation. A common heuristic is speed-dependent lookahead:

$$
\ell_d = \ell_0 + k_v v.
$$

Stanley control is attractive because it directly corrects cross-track error. The cross-track term weakens at high speed because the denominator includes $v$, reducing aggressive steering when fast.

MPC can be written:

$$
\begin{aligned}
\min_{x_{0:N},u_{0:N-1}}\quad
& \sum_{t=0}^{N}
\|x_t-x_t^{\mathrm{ref}}\|_Q^2
+ \sum_{t=0}^{N-1}\|u_t\|_R^2 \\
\mathrm{s.t.}\quad
& x_{t+1}=f(x_t,u_t), \\
& \delta_{\min}\leq \delta_t \leq \delta_{\max}, \\
& a_{\min}\leq a_t \leq a_{\max}.
\end{aligned}
$$

MPC is powerful but not magic. It depends on model fidelity, solver timing, horizon length, constraints, and warm starts. A late or infeasible MPC solution must be handled safely.

Control must account for delay. If steering actuator delay is 100 ms at 25 m/s, the vehicle moves 2.5 m before the commanded steering fully appears. Delay compensation, preview, and robust margins are essential.

Good tracking usually combines feedforward and feedback. Feedforward steering can be computed from planned curvature, for example $\delta_{\mathrm{ff}}=\arctan(L\kappa)$, while feedback corrects residual cross-track and heading errors. Feedforward alone fails when the model is wrong; feedback alone can lag and oscillate if the path curvature changes quickly. A production controller also needs command filtering, rate limits, saturation handling, and health checks for actuator response.

Friction limits connect control to physics. The available tire force must support braking, acceleration, and cornering. A simple lateral acceleration estimate is:

$$
a_y = v^2\kappa.
$$

At high speed, modest curvature can demand more lateral acceleration than the road can provide, especially in rain, snow, or on worn tires. A controller should not be blamed for failing to track a trajectory that violates the friction envelope; the planner and safety monitors must prevent such references.

Controller evaluation should separate steady-state accuracy, transient response, passenger comfort, and safety margin. A controller that minimizes cross-track error by using sharp steering may be uncomfortable or unstable on low-friction roads. A controller that is very smooth may cut corners or react too slowly to a suddenly changing reference. Typical metrics include RMS tracking error, maximum error, steering rate, jerk, acceleration, actuator saturation time, and recovery after disturbances.

Control handoff also matters. When a planner replans, cancels a lane change, or enters fallback, the controller should transition references smoothly. Discontinuous reference trajectories can create command spikes even when each individual trajectory is feasible.

## Visual

```mermaid
flowchart TB
  Ref["Planned trajectory: (t, x_ref, y_ref, yaw_ref, v_ref, kappa_ref"]"]
  State["Estimated vehicle state: (x, y, yaw, v, a, yaw_rate"]"]

  subgraph Error["Reference comparison"]
    direction TB
    Match["Nearest / preview point selection"]
    Errors["Tracking errors: e_speed, e_cross, e_heading, curvature"]
    Ref --> Match
    State --> Match
    Match --> Errors
  end

  subgraph PID["Longitudinal PID branch"]
    direction TB
    SpeedErr["Speed or spacing error e(t)"]
    P["P term: Kp * e"]
    I["I term: Ki * integral(e) with anti-windup"]
    D["D term: Kd * de/dt with filter"]
    SumPID(("sum"))
    LongSat["Throttle/brake saturation and jerk limit"]
    SpeedErr --> P --> SumPID
    SpeedErr --> I --> SumPID
    SpeedErr --> D --> SumPID
    SumPID --> LongSat
  end

  subgraph Lateral["Pure pursuit / Stanley lateral branch"]
    direction TB
    Lookahead["Pure pursuit lookahead point: l_d = l_0 + k_v v"]
    Alpha["Bearing alpha to lookahead"]
    PP["delta_pp = atan(2L sin(alpha) / l_d)"]
    Crosstrack["Stanley errors: e_cross, psi_e"]
    Stan["delta_st = psi_e + atan(k e_cross / (v + epsilon))"]
    Blend["Mode selection / blending / steering-rate limit"]
    Lookahead --> Alpha --> PP --> Blend
    Crosstrack --> Stan --> Blend
  end

  subgraph MPC["MPC tracking branch"]
    direction TB
    Model["Kinematic/dynamic bicycle model f(x,u)"]
    Horizon["Horizon variables: x_0..x_N, u_0..u_N-1"]
    Constraints["Constraints: tire friction, steering, accel, rate limits"]
    Objective["Objective: tracking error + control effort + comfort"]
    Solver["Real-time solver + warm start"]
    FirstU["First control u_0 = (delta, accel"]"]
    Model --> Horizon --> Constraints --> Objective --> Solver --> FirstU
  end

  Errors --> SpeedErr
  Errors --> Lookahead
  Errors --> Crosstrack
  Ref --> Model
  State --> Model
  LongSat --> Arb["Command arbitration and health checks"]
  Blend --> Arb
  FirstU --> Arb
  Arb --> Act["Actuators: steering rack, throttle, brakes"]
  Act --> Plant["Vehicle plant: tires, road grade, delay, saturation"]
  Plant --> Sensors["Sensors: IMU, wheel speed, steering angle, localization"]
  Sensors -. "feedback state estimate" .-> State
  Plant --> Output(("Tracked motion in road world"))
```

This diagram shows the control stack as a closed loop rather than a list of controller names. PID handles scalar longitudinal errors, pure pursuit and Stanley compute steering from geometric path errors, MPC solves a constrained horizon problem, and all branches pass through arbitration, actuator limits, vehicle dynamics, and sensor feedback.

## Worked example 1: Pure-pursuit steering

Problem: A vehicle has wheelbase $L=2.8$ m. The lookahead point is at distance $\ell_d=10$ m and angle $\alpha=8^\circ$ relative to the vehicle heading. Compute the pure-pursuit steering command.

1. Convert angle:

$$
8^\circ = 8\frac{\pi}{180}\approx 0.1396\ \mathrm{rad}.
$$

2. Use the steering law:

$$
\delta = \arctan\left(\frac{2L\sin\alpha}{\ell_d}\right).
$$

3. Compute numerator:

$$
2L\sin\alpha = 2(2.8)\sin(0.1396)
\approx 5.6(0.1392)
\approx 0.7795.
$$

4. Divide by lookahead:

$$
\frac{0.7795}{10}=0.07795.
$$

5. Take arctangent:

$$
\delta=\arctan(0.07795)\approx 0.0778\ \mathrm{rad}.
$$

6. Convert to degrees:

$$
0.0778 \times \frac{180}{\pi}\approx 4.46^\circ.
$$

Answer: pure pursuit commands about $4.5^\circ$ of steering.

Check: The lookahead angle is 8 degrees, but steering is smaller because the lookahead point is 10 m away and the wheelbase is 2.8 m.

## Worked example 2: Stanley steering on a curve

Problem: A vehicle travels at $v=12$ m/s. Heading error to the path is $\psi_e=2^\circ$. Cross-track error is $e_c=0.5$ m to the left of the path, gain $k=1.2$, and $\epsilon=0.1$. Compute the Stanley steering correction assuming positive error requires positive steering.

1. Convert heading error:

$$
2^\circ = 0.0349\ \mathrm{rad}.
$$

2. Compute cross-track term:

$$
\arctan\left(\frac{k e_c}{v+\epsilon}\right)
= \arctan\left(\frac{1.2(0.5)}{12.1}\right)
= \arctan(0.0496).
$$

3. Approximate arctangent:

$$
\arctan(0.0496)\approx 0.0496\ \mathrm{rad}.
$$

4. Sum terms:

$$
\delta = 0.0349 + 0.0496 = 0.0845\ \mathrm{rad}.
$$

5. Convert to degrees:

$$
0.0845 \times \frac{180}{\pi}\approx 4.84^\circ.
$$

Answer: Stanley control commands about $4.8^\circ$.

Check: At higher speed, the cross-track term would shrink. At lower speed, the same lateral error would produce stronger steering, which is why $\epsilon$ and saturation matter.

## Code

```python
import numpy as np

def pure_pursuit_delta(wheelbase, lookahead_dist, alpha_rad):
    return np.arctan2(2.0 * wheelbase * np.sin(alpha_rad), lookahead_dist)

def stanley_delta(heading_error, cross_track_error, speed, gain=1.0, eps=0.1):
    return heading_error + np.arctan2(gain * cross_track_error, speed + eps)

def pid_step(error, prev_error, integral, dt, kp, ki, kd):
    integral += error * dt
    derivative = (error - prev_error) / dt
    command = kp * error + ki * integral + kd * derivative
    return command, integral

delta_pp = pure_pursuit_delta(2.8, 10.0, np.deg2rad(8.0))
delta_st = stanley_delta(np.deg2rad(2.0), 0.5, 12.0, gain=1.2)
print("pure pursuit deg:", np.rad2deg(delta_pp))
print("stanley deg:", np.rad2deg(delta_st))
```

## Common pitfalls

- Mixing sign conventions for cross-track error. A controller can steer away from the path if the coordinate convention is inconsistent.
- Tuning at one speed and deploying at another. Lookahead, gains, and delay effects all change with speed.
- Ignoring actuator saturation and rate limits. A controller that asks for impossible steering produces tracking errors and instability.
- Letting PID integral wind up during saturation. Anti-windup logic is needed for braking and throttle loops.
- Using a kinematic model near tire limits. Wet roads, snow, high curvature, and high speed require stronger dynamic awareness.
- Validating only in open-loop logs. Control must be tested closed-loop because small tracking errors change future states.

## Connections

- [Motion planning](/cs/autonomous-driving/motion-planning)
- [Decision making and behavior planning](/cs/autonomous-driving/decision-making-and-behavior-planning)
- [Simulation and data](/cs/autonomous-driving/simulation-and-data)
- [Embedded systems](/cs/embedded/)
- [Engineering math for controls and ODEs](/math/engineering-math/)
- [Physics of signals and systems](/physics/signals-systems/)
- Further reading: Stanley controller from the DARPA Grand Challenge, pure pursuit robotics literature, Rajamani's vehicle dynamics, MPC texts, and PID control references.
