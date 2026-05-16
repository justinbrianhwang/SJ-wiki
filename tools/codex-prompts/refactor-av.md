## Section: Autonomous Driving

- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/autonomous-driving/`

### Foundation pages (preserve and enrich)

```
intro.md
sae-levels-and-operational-design-domain.md
sensors-cameras-lidar-radar-imu.md
perception-object-detection-and-segmentation.md
depth-estimation-and-stereo-vision.md
sensor-fusion.md
localization-and-hd-maps.md
prediction-and-motion-forecasting.md
motion-planning.md
decision-making-and-behavior-planning.md
control-pid-mpc-pure-pursuit-stanley.md
end-to-end-driving.md
simulation-and-data.md
safety-iso26262-sotif-scenario-testing.md
v2x-and-connected-vehicles.md
adversarial-and-physical-attacks-on-av.md
```

### Paper-named pages to merge then delete

Run `ls docs/cs/autonomous-driving/` to enumerate. Approximate mapping:

```
pointpillars.md, centerpoint.md, mv3d-sonar.md          → perception-object-detection-and-segmentation.md (or sensor-fusion.md)
vectornet.md, hivt.md, lanegcn.md, pnpnet.md            → prediction-and-motion-forecasting.md
chauffeurnet.md, dynamic-conditional-imitation-learning.md,
learning-by-cheating.md, darpa-urban-challenge.md       → end-to-end-driving.md (or new "Imitation learning for driving")
transfuser.md, interfuser.md, uniad.md,
diffusion-planning-for-driving.md, world-models-for-driving.md → end-to-end-driving.md (modern E2E sub-section)
autovla.md, drivevlm.md, limsim.md,
vla-for-driving-survey.md, mllm-for-driving-survey.md   → end-to-end-driving.md or new "Foundation models for driving"
```

### Recommended new topical chapter (optional)

If `end-to-end-driving.md` becomes too long after merging, split off a new foundation page:

- `foundation-models-for-driving.md` at a reasonable sidebar_position, for VLA / MLLM / LLM-based driving systems

Use your judgment. Don't split unnecessarily.

### Notes

- DARPA Urban Challenge is historical — it can be a sub-section "Classical pipelines and the DARPA Urban Challenge" in `end-to-end-driving.md` (because it predates and motivates learned E2E).
- Section headings should be topical:
  - ✅ `### Pillar-based 3D detection` (covers PointPillars [1])
  - ✅ `### Center-based 3D detection and tracking` (covers CenterPoint [2])
  - ✅ `### Vectorized scene representations` (covers VectorNet [3], LaneGCN [4])
  - ✅ `### Hierarchical motion forecasting with transformers` (covers HiVT [5])

Apply the refactor policy above. Begin now.
