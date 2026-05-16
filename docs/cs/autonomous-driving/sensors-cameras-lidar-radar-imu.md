---
title: Sensors, Cameras, LiDAR, Radar, and IMU
sidebar_position: 3
---

# Sensors, Cameras, LiDAR, Radar, and IMU

Autonomous driving is built on imperfect measurements. Cameras see texture and color, lidar gives accurate 3D range, radar detects velocity and survives some weather, IMUs measure short-term motion, GNSS anchors the vehicle globally, and ultrasonic sensors cover close-range parking distances. No single sensor solves the problem alone; each has blind spots, failure modes, timing issues, and calibration requirements that shape the rest of the stack.

This page is the sensor-level foundation for [perception](/cs/autonomous-driving/perception-object-detection-and-segmentation), [depth estimation](/cs/autonomous-driving/depth-estimation-and-stereo-vision), [sensor fusion](/cs/autonomous-driving/sensor-fusion), [localization](/cs/autonomous-driving/localization-and-hd-maps), and [safety analysis](/cs/autonomous-driving/safety-iso26262-sotif-scenario-testing). The practical lesson is that sensor choice is never just a bill-of-materials decision; it changes which algorithms are credible and which hazards must be mitigated.

## Definitions

A **camera** measures image irradiance on a pixel grid. Automotive cameras are usually monocular RGB or RCCB sensors with wide dynamic range. A **rolling shutter** exposes rows at slightly different times, which can bend fast-moving objects or distort images during vibration. A **global shutter** exposes all pixels at once, reducing motion distortion but often with cost or sensitivity trade-offs.

**LiDAR** stands for light detection and ranging. It estimates distance by measuring the time of flight, phase shift, or frequency difference of emitted light. Mechanical spinning lidar, MEMS lidar, flash lidar, optical phased-array lidar, and FMCW lidar differ in scanning pattern, range, velocity measurement, cost, and robustness.

**Radar** uses radio waves, usually frequency-modulated continuous-wave signals in automotive systems. FMCW radar estimates range from beat frequency, radial velocity from Doppler shift, and angle from antenna arrays. **MIMO radar** uses multiple transmit and receive antennas to synthesize a larger virtual aperture.

An **IMU** contains accelerometers and gyroscopes. It measures specific force and angular velocity at high rate, but bias and noise cause dead-reckoning drift. IMUs are powerful in the short term and weak in the long term unless fused with GNSS, wheel odometry, lidar, camera, or map constraints.

**GNSS** is the satellite navigation family that includes GPS, Galileo, GLONASS, BeiDou, and related augmentation systems. It provides global position but can be degraded by urban canyons, multipath, tunnels, foliage, spoofing, or jamming.

**Ultrasonic sensors** use acoustic time of flight at short range. They are cheap and useful for parking, curb detection, and near-field obstacle sensing, but they have low angular resolution and are sensitive to surface geometry.

**Extrinsic calibration** estimates the rigid transform between sensor coordinate frames. **Intrinsic calibration** models a sensor's internal geometry, such as camera focal length and distortion. **Time calibration** aligns timestamps. A technically good sensor suite can still fail if space and time alignment are poor.

## Key results

Range sensors often use time-of-flight reasoning. If a lidar pulse returns after round-trip time $\Delta t$, then range is approximately:

$$
r = \frac{c \Delta t}{2},
$$

where $c$ is the speed of light in air. The division by two appears because the light travels to the object and back.

FMCW radar and FMCW lidar use a frequency sweep. For a linear chirp with slope $S$ in hertz per second, the beat frequency $f_b$ is related to range:

$$
r \approx \frac{c f_b}{2S}.
$$

For radar radial velocity, the Doppler shift is approximately:

$$
v_r \approx \frac{\lambda f_D}{2},
$$

where $\lambda$ is wavelength and $f_D$ is Doppler frequency. The sign depends on convention. Radar measures radial velocity directly, which is one reason it remains valuable even when lidar and cameras are strong.

Camera geometry maps a 3D point $P = (X,Y,Z)$ into pixel coordinates through intrinsics:

$$
\begin{aligned}
u &= f_x \frac{X}{Z} + c_x, \\
v &= f_y \frac{Y}{Z} + c_y.
\end{aligned}
$$

This projection gives rich semantics but loses metric depth unless paired with stereo, motion, learned priors, lidar, or other constraints. Camera-only systems must therefore recover 3D structure indirectly.

IMU integration illustrates drift. With acceleration bias $b_a$, even a small constant error accumulates quadratically in position:

$$
\Delta x(t) \approx \frac{1}{2} b_a t^2.
$$

That is why IMU-only navigation is not enough for road driving over long intervals, even though IMUs are essential for high-rate motion propagation.

Sensor failure modes must be treated as first-class design inputs. Cameras can saturate under glare, struggle at night, or lose contrast in fog. Lidar can degrade in heavy rain, snow, dust, or with low-reflectivity targets. Radar can produce ghost detections, multipath, and poor elevation discrimination. GNSS can jump or drift under multipath. IMUs drift silently. Ultrasonic sensors can miss soft or angled surfaces. The stack must know both what was measured and how much to trust it.

## Visual

```mermaid
flowchart TB
  subgraph Camera["Camera processing chain"]
    direction TB
    CamRaw["#quot;Raw frames: [H, W, RGB/RCCB, t"]"]
    CamISP["ISP + HDR merge + rectification"]
    CamCal["Intrinsic/extrinsic calibration: K, distortion, T_cam_vehicle"]
    CamFeat["#quot;Image CNN/ViT features: [C, H/stride, W/stride"]"]
    CamOut["Outputs: 2D boxes, masks, lanes, lights, bearings"]
    CamRaw --> CamISP --> CamCal --> CamFeat --> CamOut
  end

  subgraph Lidar["LiDAR processing chain"]
    direction TB
    LidarRaw["#quot;Packets/range image: [beam, azimuth, range, intensity, t"]"]
    LidarMotion["Motion compensation with IMU/odometry"]
    LidarCloud["#quot;Point cloud: [N, x, y, z, intensity"]"]
    LidarVoxel["#quot;Voxel/pillarization: [C, X, Y, Z"] or ["C, X, Y"]"]
    LidarOut["Outputs: 3D boxes, occupancy, freespace, landmarks"]
    LidarRaw --> LidarMotion --> LidarCloud --> LidarVoxel --> LidarOut
  end

  subgraph Radar["Radar processing chain"]
    direction TB
    RadarRaw["#quot;FMCW ADC samples: [chirp, antenna, sample"]"]
    FFT["Range FFT -> Doppler FFT -> angle estimation"]
    RadarCFAR["CFAR detection + clustering"]
    RadarTrack["Track filtering: range, bearing, radial velocity"]
    RadarOut["Outputs: long-range tracks, cut-in velocity cues"]
    RadarRaw --> FFT --> RadarCFAR --> RadarTrack --> RadarOut
  end

  subgraph Inertial["IMU, GNSS, odometry chain"]
    direction TB
    IMURaw["#quot;IMU: [a_x, a_y, a_z, gyro_x, gyro_y, gyro_z"] at high rate"]
    Wheel["Wheel ticks + steering angle"]
    GNSS["GNSS/RTK: position, time, covariance"]
    Prop["Dead-reckoning propagation: x_t, P_t"]
    Update["EKF/factor-graph update"]
    Pose["Outputs: ego pose, velocity, covariance, time base"]
    IMURaw --> Prop
    Wheel --> Prop
    GNSS --> Update
    Prop --> Update --> Pose
  end

  subgraph NearField["Ultrasonic / near-field chain"]
    direction TB
    UltraRaw["Time-of-flight echo: short-range distance"]
    UltraFilter["Echo filtering + mounting-angle compensation"]
    UltraGrid["Near-field occupancy cells around vehicle"]
    UltraRaw --> UltraFilter --> UltraGrid
  end

  CamOut -->|"semantics + bearing"| Fusion["Fusion-ready measurement set"]
  LidarOut -->|"metric geometry"| Fusion
  RadarOut -->|"range + Doppler"| Fusion
  Pose -->|"ego motion + timestamps"| Fusion
  UltraGrid -->|"parking/curb proximity"| Fusion
  Fusion --> Final(("Perception/localization inputs"))
```

This diagram compares each sensor as a processing chain rather than a flat list: cameras produce semantic image features, lidar produces metric geometry, radar adds Doppler-rich tracks, and inertial/GNSS signals stabilize pose and timing. The arrows into the fusion-ready set show why calibration and timestamps are part of the sensor architecture, not bookkeeping after the fact.

## Worked example 1: Computing lidar range from time of flight

Problem: A pulsed lidar emits light and receives a return after $\Delta t = 80$ ns. Estimate the object range. Use $c = 3.0 \times 10^8$ m/s.

1. Write the time-of-flight equation:

$$
r = \frac{c \Delta t}{2}.
$$

2. Convert nanoseconds to seconds:

$$
80\ \mathrm{ns} = 80 \times 10^{-9}\ \mathrm{s}.
$$

3. Substitute:

$$
\begin{aligned}
r &= \frac{(3.0 \times 10^8)(80 \times 10^{-9})}{2} \\
  &= \frac{24}{2} \\
  &= 12\ \mathrm{m}.
\end{aligned}
$$

Answer: the target is approximately 12 m away.

Check: Light travels 24 m in 80 ns. Because the path is out and back, the one-way distance is 12 m.

## Worked example 2: Estimating camera rolling-shutter displacement

Problem: A forward camera has a rolling-shutter readout time of 20 ms from top row to bottom row. During the readout, the vehicle yaws at $15^\circ$/s over a bumpy road. Estimate the yaw difference between the top and bottom rows.

1. Convert the yaw rate to degrees per millisecond:

$$
15^\circ / \mathrm{s} = 0.015^\circ / \mathrm{ms}.
$$

2. Multiply by readout time:

$$
\Delta \psi = 0.015^\circ/\mathrm{ms} \times 20\ \mathrm{ms} = 0.30^\circ.
$$

3. Interpret the result. A third of a degree may look small, but for long-range perception a tiny angular error can shift lane boundaries, signs, or vehicles by several pixels. The displacement grows with focal length and range.

Answer: the top and bottom rows can represent scene geometry under poses that differ by about $0.30^\circ$.

Check: If the yaw rate doubles or the readout time doubles, the distortion doubles. This linear dependence is why global shutter and motion compensation matter for fast motion and long-range detection.

## Code

```python
import numpy as np

def project_points(points_vehicle, K, T_cam_vehicle):
    """Project vehicle-frame 3D points into a camera image."""
    n = points_vehicle.shape[0]
    homog = np.hstack([points_vehicle, np.ones((n, 1))])
    points_cam = (T_cam_vehicle @ homog.T).T[:, :3]

    z = np.maximum(points_cam[:, 2], 1e-6)
    pixels_h = (K @ points_cam.T).T
    uv = pixels_h[:, :2] / z[:, None]
    return uv, points_cam[:, 2] > 0.0

K = np.array([[900.0, 0.0, 640.0],
              [0.0, 900.0, 360.0],
              [0.0, 0.0, 1.0]])
T_cam_vehicle = np.eye(4)
points = np.array([[5.0, 0.0, 20.0],
                   [2.0, -1.0, 10.0],
                   [1.0, 0.5, -3.0]])

uv, in_front = project_points(points, K, T_cam_vehicle)
print(uv)
print(in_front)
```

## Common pitfalls

- Comparing sensors by one headline range number. Field of view, angular resolution, latency, false positives, calibration stability, and failure modes matter as much as range.
- Ignoring timestamp alignment. A 50 ms timing error at 20 m/s is a 1 m spatial error before perception even begins.
- Treating radar as low-quality lidar. Radar provides Doppler velocity and has different noise statistics, so it should not be forced into a lidar-only mental model.
- Assuming GNSS is always globally accurate. Multipath can produce plausible but wrong positions, especially near tall buildings.
- Trusting calibration forever. Sensor mounts move under thermal cycling, vibration, impacts, maintenance, and manufacturing variation.
- Forgetting occlusion. A perfect sensor cannot see through a truck, building, hill crest, or parked vehicle without cooperative perception or prior map information.

## Connections

- [Perception object detection and segmentation](/cs/autonomous-driving/perception-object-detection-and-segmentation)
- [Depth estimation and stereo vision](/cs/autonomous-driving/depth-estimation-and-stereo-vision)
- [Sensor fusion](/cs/autonomous-driving/sensor-fusion)
- [Localization and HD maps](/cs/autonomous-driving/localization-and-hd-maps)
- [Physics of signals and systems](/physics/signals-systems/)
- [Electromagnetics for radar and lidar](/physics/electromagnetics/)
- Further reading: Thrun, Burgard, and Fox, *Probabilistic Robotics*; standard automotive radar texts; lidar sensor datasheets; camera calibration literature by Zhang and Hartley-Zisserman.
