# AGENT 1 — BEV LiDAR-Camera fusion (core systems)

Create these 4 pages in `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`:

1. **`bevfusion-mit.md`** — sidebar_position: 21
   - PDF: `f:/coding/Web/SJ Wiki/tmp/BEVFusion Multi-Task Multi-Sensor Unified BEV.pdf`
   - System: **BEVFusion** (Liu, Tang, Amini, Han et al., MIT, ICRA 2023). Unified BEV representation; camera-to-BEV view transform + optimized BEV pooling; multi-task (detection + map segmentation). Emphasize the efficient BEV pooling kernel and the shared BEV space.

2. **`bevfusion-robust.md`** — sidebar_position: 22
   - PDF: `f:/coding/Web/SJ Wiki/tmp/BEVFusion, A Simple and Robust LiDAR-Camera Fusion Framework.pdf`
   - System: **BEVFusion** (Liang et al., Peking University, NeurIPS 2022). Two independent streams fused in BEV so it stays robust when one modality fails. Contrast it clearly with the MIT BEVFusion (same name, different design) — add a short "Note: name collision" paragraph and cross-link `bevfusion-mit`.

3. **`bevdilation.md`** — sidebar_position: 23
   - PDF: `f:/coding/Web/SJ Wiki/tmp/BEVDilation, LiDAR-Centric Multi-Modal Fusion for 3D Object Detection.pdf`
   - System: **BEVDilation** (Zhang et al., HK PolyU). LiDAR-centric multi-modal fusion; explain the dilation mechanism and why LiDAR-centric.

4. **`fusion4ca.md`** — sidebar_position: 24
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Fusion4CA, Boosting 3D Object Detection via Comprehensive Image Exploitation.pdf`
   - System: **Fusion4CA** (Luo et al., SJTU). Comprehensive image exploitation for BEV LiDAR-camera 3D detection.

Cross-link all four to each other and to `/cs/autonomous-driving/sensor-fusion`,
`/cs/autonomous-driving/perception-object-detection-and-segmentation`,
`/cs/autonomous-driving/sensors-cameras-lidar-radar-imu`, and `/cs/deep-learning/` where relevant.
Datasets here are mostly nuScenes (mAP, NDS) and KITTI — quote conservatively.
