# AGENT 3 — 3D detection backbone + weather robustness

Create these 2 pages in `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`:

1. **`centerpoint.md`** — sidebar_position: 20
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Center-based 3D Object Detection and Tracking.pdf`
   - System: **CenterPoint** (Yin, Zhou, Krähenbühl, UT Austin, CVPR 2021). Center-based (anchor-free) 3D detection + tracking on point clouds; two-stage refinement; velocity head enabling greedy closest-point tracking. This is a landmark detector — give it full depth. Explain the keypoint heatmap formulation with KaTeX. Datasets: nuScenes (NDS, AMOTA), Waymo Open.

2. **`weather-occlusion-robustness.md`** — sidebar_position: 28
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Evaluating the Impact of Weather-Induced Sensor Occlusion on BEVFusion for 3D Object Detection.pdf`
   - Topic: **Weather-induced sensor occlusion robustness of BEVFusion** (Kumar et al., 2025). An evaluation/analysis paper (not a new architecture) — frame it as a robustness study: how rain/fog/snow occlusion on camera and/or LiDAR degrades BEVFusion 3D detection, the occlusion modeling, and the measured degradation. Title can be topical, e.g. "Weather-Induced Sensor Occlusion Robustness (Kumar et al., 2025)". Use a comparison table of degradation under conditions.

Cross-link: centerpoint ↔ `/cs/autonomous-driving/perception-object-detection-and-segmentation`,
`/cs/autonomous-driving/prediction-and-motion-forecasting` (tracking → prediction);
weather page ↔ `/cs/autonomous-driving/sensor-fusion`, `/cs/autonomous-driving/sensors-cameras-lidar-radar-imu`,
`/cs/autonomous-driving/safety-iso26262-sotif-scenario-testing`, and the BEVFusion pages
(`/cs/autonomous-driving/bevfusion-mit`).
