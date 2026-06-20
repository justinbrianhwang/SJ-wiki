# AGENT 4 — V2X cooperative perception

Create these 2 pages in `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`:

1. **`tumtraf-v2x-dataset.md`** — sidebar_position: 29
   - PDF: `f:/coding/Web/SJ Wiki/tmp/TUMTraf V2X Cooperative Perception Dataset.pdf`
   - Dataset: **TUMTraf V2X Cooperative Perception Dataset** (Zimmer et al., TU Munich, CVPR 2024). A roadside + vehicle cooperative perception dataset. Cover: sensor setup (infrastructure + vehicle, camera + LiDAR), labeling, classes, scenarios, the cooperative 3D detection benchmark and the baseline fusion model (CoopDet3D if present). Use a table of dataset statistics. This is a dataset page — frame accordingly (still follow the format, but "Method" becomes the dataset construction + benchmark protocol).

2. **`cooperative-bev-fusion.md`** — sidebar_position: 30
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Camera and LiDAR BEV Fusion for Cooperative 3D Object Detection on TUMTraf V2X.pdf`
   - System: **Cooperative Camera-LiDAR BEV Fusion** (Shahbaz & Agarwal, Univ. Central Florida, 2026). Cooperative (infrastructure↔vehicle) BEV fusion 3D detection evaluated on TUMTraf V2X. Explain how cooperative/early-vs-late fusion across agents works in BEV, and communication considerations.

Cross-link the two pages to each other and to `/cs/autonomous-driving/v2x-and-connected-vehicles`,
`/cs/autonomous-driving/sensor-fusion`, `/cs/autonomous-driving/perception-object-detection-and-segmentation`,
`/cs/autonomous-driving/simulation-and-data` (dataset), and the BEVFusion pages
(`/cs/autonomous-driving/bevfusion-mit`).
