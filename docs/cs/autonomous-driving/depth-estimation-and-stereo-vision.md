---
title: Depth Estimation and Stereo Vision
sidebar_position: 5
---

# Depth Estimation and Stereo Vision

Depth estimation asks how far scene points are from the vehicle. Lidar gives direct sparse range, but camera-based systems must infer depth from geometry, motion, stereo disparity, learned priors, or fusion. This is central to autonomous driving because planning needs metric distances: whether a pedestrian is 6 m or 60 m away changes braking, lane changes, and risk assessment.

This page covers stereo geometry, monocular depth, self-supervised depth learning, and depth completion. It connects the raw sensor discussion in [sensors](/cs/autonomous-driving/sensors-cameras-lidar-radar-imu) to [perception](/cs/autonomous-driving/perception-object-detection-and-segmentation), [sensor fusion](/cs/autonomous-driving/sensor-fusion), and [motion planning](/cs/autonomous-driving/motion-planning), where depth uncertainty becomes a safety-critical input.

## Definitions

**Depth** is distance along a camera's optical axis, often denoted $Z$. **Range** is Euclidean distance from the sensor origin to a point. They are equal only for points on the optical axis.

**Stereo vision** uses two cameras with known relative pose. For rectified stereo, corresponding points lie on the same image row, and depth is inversely proportional to disparity. **Disparity** is the horizontal pixel difference between the left and right image coordinates of the same 3D point.

The **baseline** $B$ is the distance between stereo camera centers. The **focal length** $f$ is the camera focal length in pixel units after calibration. For rectified stereo, depth is:

$$
Z = \frac{fB}{d},
$$

where $d$ is disparity in pixels.

**Monocular depth estimation** predicts depth from one image. Since a single image lacks metric scale by geometry alone, monocular methods use learned priors, known camera height, object sizes, temporal motion, or additional sensors.

**MiDaS** and **DPT** are influential monocular depth models that learn robust relative depth across diverse datasets. They are useful references, but automotive deployment requires metric scale, temporal consistency, calibration, and domain validation.

**Self-supervised monocular depth**, such as the Monodepth family, trains by predicting depth and camera motion such that one frame can be warped into another. It avoids dense ground-truth depth labels but depends on brightness constancy, static-scene assumptions, and careful handling of occlusion and moving objects.

**Depth completion** fills a dense or semi-dense depth map from sparse lidar or radar depth plus camera imagery. It can provide dense geometry while retaining metric anchors.

## Key results

The stereo depth equation has an important sensitivity property. Since $Z = fB/d$, a disparity error $\Delta d$ produces approximate depth error:

$$
\Delta Z \approx -\frac{fB}{d^2}\Delta d.
$$

Depth error grows quadratically with distance because distant objects have small disparity. A one-pixel disparity error near the vehicle may be modest; the same error far away can be many meters. This is why long-range camera depth is difficult and why radar or lidar can be valuable for far objects.

Rectification simplifies correspondence. If cameras are calibrated and rectified, corresponding points share the same vertical coordinate. Stereo matching becomes a one-dimensional search along horizontal scanlines instead of a two-dimensional search. But real systems must handle low texture, repetitive patterns, reflections, rain drops, dirt, exposure differences, and rolling-shutter motion.

Monocular depth is not pure geometry. A neural network can learn that lane markings converge, cars have typical sizes, and the road plane has structure. Those priors help, but they can fail on unusual objects, hills, trailers, construction equipment, or camera pitch changes. A planner must treat monocular depth as uncertain, especially under distribution shift.

Self-supervised photometric losses typically compare a target image $I_t$ with a source image $I_s$ warped using predicted depth $\hat{D}_t$ and relative pose $\hat{T}_{t \to s}$:

$$
\mathcal{L}_{\mathrm{photo}} =
\sum_p
\rho \left(
I_t(p) -
I_s\left(\pi\left(\hat{T}_{t \to s}\ \hat{D}_t(p)\ K^{-1}p\right)\right)
\right),
$$

where $K$ is the camera intrinsic matrix, $\pi$ is projection, and $\rho$ is a robust penalty. This loss is elegant, but it is invalid where pixels are occluded, non-Lambertian, independently moving, saturated, or outside the image after warping.

Depth completion can be framed as sensor fusion at the pixel or BEV level. Sparse lidar points projected into the image give accurate depth samples. A model uses image edges and semantics to propagate those samples while preserving discontinuities at object boundaries.

### Multi-view acoustic depth reconstruction

Depth estimation is not only a camera problem. Forward-looking sonar in underwater autonomy measures range and bearing but compresses elevation, so a single 2D sonar image can correspond to many possible 3D surfaces. MV3D [1] uses a batch of sonar views from a linear scan to predict multiple depth maps, then back-projects and fuses them into a 3D reconstruction.

For a sonar return with range $r$, bearing $\theta$, and inferred elevation $\phi$, a simple back-projection is:

$$
x=r\cos\phi\cos\theta,\qquad
y=r\cos\phi\sin\theta,\qquad
z=r\sin\phi.
$$

The learning problem is to infer the missing elevation and surface geometry from multi-view acoustic appearance, shadows, and motion. MV3D [1] trains on synthetic sonar-depth pairs, uses style transfer to reduce the synthetic-to-real gap, and evaluates geometry with Chamfer distance:

$$
d_{\mathrm{CD}}(P,Q)=
\frac{1}{|P|}\sum_{p\in P}\min_{q\in Q}\|p-q\|_2^2+
\frac{1}{|Q|}\sum_{q\in Q}\min_{p\in P}\|q-p\|_2^2.
$$

Pseudo-code for the reconstruction interface:

```python
depth_maps = sonar_depth_model(scan_batch)
clouds = []
for depth, pose in zip(depth_maps, virtual_camera_poses):
    local_cloud = backproject_sonar_depth(depth)
    clouds.append(transform(local_cloud, pose))
reconstruction = fuse_point_clouds(clouds)
```

Worked example: if $r=4$ m, $\theta=30^\circ$, and $\phi=10^\circ$, then $x\approx4(0.985)(0.866)=3.41$ m, $y\approx4(0.985)(0.5)=1.97$ m, and $z\approx4(0.174)=0.70$ m. The example is underwater rather than road driving, but the lesson transfers: each sensor has its own projection ambiguity, and the depth model must respect that physics.

Temporal depth adds another source of geometry. If the camera moves and a scene point is static, multiple frames provide parallax, much like a virtual stereo baseline. This is useful for monocular video, but it depends on accurate ego motion and static-scene assumptions. Moving vehicles, pedestrians, shadows, reflections, and rolling-shutter effects break the simple geometry. AV systems often separate static structure from dynamic agents before trusting temporal depth.

Road-plane assumptions are helpful but dangerous. If the camera height and pitch are known, pixels below the horizon can be intersected with an estimated ground plane to get approximate distance. This works for flat roads and lane markings, but hills, banked curves, speed bumps, dips, and camera pitch changes can create large errors. A robust system treats the road plane as a hypothesis with uncertainty, not as a universal truth.

Depth should be evaluated where it affects driving. Average pixel depth error can be dominated by background regions that do not matter for near-term safety. More useful slices include obstacle depth in the ego lane, curb and barrier range, crossing-pedestrian distance, long-range lead-vehicle range, and depth discontinuities near object boundaries. A depth map that is visually smooth may still be unsafe if it rounds off a curb or places a pedestrian behind the true location.

Scale monitoring is essential for learned monocular systems. If camera pitch, focal length, crop, or image resizing changes, a model can keep plausible relative depth while drifting in metric scale. Calibration checks and sensor-fusion anchors help catch this failure.

## Visual

```text
Rectified stereo geometry

Left camera                          Right camera
    o-------------------------------------o
    |<------------- baseline B ---------->|
     \                                   /
      \                                 /
       \                               /
        \                             /
          point at depth Z

Image relation after rectification:
left pixel u_L, right pixel u_R
disparity d = u_L - u_R
depth Z = fB / d
```

## Worked example 1: Stereo depth from disparity

Problem: A stereo rig has focal length $f = 900$ pixels and baseline $B = 0.30$ m. A car feature has disparity $d = 45$ pixels. Estimate its depth.

1. Write the stereo formula:

$$
Z=\frac{fB}{d}.
$$

2. Substitute:

$$
\begin{aligned}
Z &= \frac{900 \times 0.30}{45} \\
  &= \frac{270}{45} \\
  &= 6\ \mathrm{m}.
\end{aligned}
$$

Answer: the feature is approximately 6 m away along the optical axis.

Check: If the disparity were half as large, $22.5$ pixels, the estimated depth would double to 12 m. This inverse relationship is the core intuition of stereo.

## Worked example 2: Depth uncertainty from a one-pixel disparity error

Problem: Use the same stereo rig, $f=900$ pixels and $B=0.30$ m. Estimate the depth error from a one-pixel disparity error at $d=45$ pixels and at $d=9$ pixels.

1. Use the derivative magnitude:

$$
|\Delta Z| \approx \frac{fB}{d^2}|\Delta d|.
$$

2. Near case with $d=45$ and $\vert \Delta d\vert =1$:

$$
|\Delta Z| \approx \frac{270}{45^2}
= \frac{270}{2025}
\approx 0.133\ \mathrm{m}.
$$

3. Far case with $d=9$:

$$
|\Delta Z| \approx \frac{270}{9^2}
= \frac{270}{81}
\approx 3.33\ \mathrm{m}.
$$

Answer: a one-pixel disparity error is about 13 cm at 6 m, but about 3.3 m at 30 m.

Check: The far object has one fifth the disparity, so the sensitivity is $5^2 = 25$ times worse. That matches $0.133 \times 25 \approx 3.33$.

## Code

```python
import numpy as np

def stereo_depth(disparity_px, focal_px, baseline_m, min_disparity=0.1):
    disparity = np.maximum(disparity_px.astype(float), min_disparity)
    return focal_px * baseline_m / disparity

def depth_uncertainty(disparity_px, focal_px, baseline_m, sigma_disparity_px):
    disparity = np.maximum(disparity_px.astype(float), 0.1)
    return (focal_px * baseline_m / disparity**2) * sigma_disparity_px

disparities = np.array([45.0, 18.0, 9.0])
depths = stereo_depth(disparities, focal_px=900.0, baseline_m=0.30)
sigmas = depth_uncertainty(disparities, 900.0, 0.30, sigma_disparity_px=1.0)

for d, z, s in zip(disparities, depths, sigmas):
    print(f"disparity={d:4.1f}px depth={z:5.2f}m sigma≈{s:5.2f}m")
```

## Common pitfalls

- Treating monocular depth as metric without checking scale. A model trained for relative depth may preserve ordering but not absolute distance.
- Forgetting that stereo depth worsens rapidly at long range. Small disparity errors dominate far-away estimates.
- Assuming rectification is perfect forever. Camera mounts, temperature, vibration, and repairs can invalidate calibration.
- Ignoring moving objects in self-supervised training. Photometric warping from ego motion does not explain independently moving cars or pedestrians.
- Over-smoothing depth completion across object boundaries. This can merge a pedestrian with the background or smear a curb into the road surface.
- Evaluating depth with average error only. Tail errors near the driving corridor matter more than small errors on sky, buildings, or distant background.

## Connections

- [Sensors, cameras, lidar, radar, and IMU](/cs/autonomous-driving/sensors-cameras-lidar-radar-imu)
- [Perception, object detection, and segmentation](/cs/autonomous-driving/perception-object-detection-and-segmentation)
- [Sensor fusion](/cs/autonomous-driving/sensor-fusion)
- [Motion planning](/cs/autonomous-driving/motion-planning)
- [Deep learning](/cs/deep-learning/)
- [Engineering math and projective geometry](/math/engineering-math/)
- Further reading: Hartley and Zisserman, *Multiple View Geometry*; Monodepth2; MiDaS; DPT; KITTI stereo and depth completion benchmarks.

## References

[1] N. Jaber, M. Wehbe, A. Christensen, F. Kirchner. *MV3D: Multi-View 3D Reconstruction of Objects Using Forward-Looking Sonar*. IEEE Robotics and Automation Letters, 2025.
