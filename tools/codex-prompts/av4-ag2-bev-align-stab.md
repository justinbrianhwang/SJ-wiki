# AGENT 2 — BEV fusion: alignment, stabilization, attention

Create these 3 pages in `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`:

1. **`contrastalign.md`** — sidebar_position: 25
   - PDF: `f:/coding/Web/SJ Wiki/tmp/ContrastAlign, Toward Robust BEV Feature Alignment via Contrastive Learning for Multi-Modal 3D Object Detection.pdf`
   - System: **ContrastAlign** (Song et al., 2024). Contrastive learning to align LiDAR and camera BEV features robustly under calibration/projection noise. Explain the contrastive objective with KaTeX (positive/negative pairs, InfoNCE-style loss).

2. **`post-fusion-bev-stabilization.md`** — sidebar_position: 26
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Post Fusion BEV Feature Stabilization.pdf`
   - System/technique: **Post-Fusion BEV Feature Stabilization** (Dong et al., 2026). Stabilizing BEV features after fusion for robust multimodal 3D detection (temporal/feature stability). Explain what "stabilization" means here and why post-fusion.

3. **`hybrid-attention-fusion.md`** — sidebar_position: 27
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Multi-Modal Sensor Fusion using Hybrid Attention for Autonomous Driving.pdf`
   - Technique: **Hybrid-Attention Multi-Modal Fusion** (Mayank et al., Mercedes-Benz AG + Univ. Freiburg). Hybrid (self + cross) attention to fuse modalities. Explain the attention blocks with KaTeX (Q/K/V, cross-modal attention).

Cross-link to each other and to `/cs/autonomous-driving/sensor-fusion`,
`/cs/autonomous-driving/perception-object-detection-and-segmentation`,
the BEVFusion pages (`/cs/autonomous-driving/bevfusion-mit`, `/cs/autonomous-driving/bevfusion-robust`),
`/cs/deep-learning/attention-transformers` (attention background), and `/cs/deep-learning/` as relevant.
Datasets: nuScenes / KITTI — conservative quoting.
