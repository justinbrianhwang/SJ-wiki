You are an autonomous content author for **SJ Wiki**. Generate **foundational** Markdown notes for the Autonomous Driving subtopic.

## Inputs

- **SOURCE_PDFs**: NONE for this run. The user is preparing source material in parallel. Write the foundational layer from general knowledge of the field — self-driving has stable definitions, standard stacks (sensing → perception → fusion → prediction → planning → control), industry-standard safety frameworks (ISO 26262, SOTIF, SAE levels), and well-known reference systems (Waymo, Tesla, Cruise, Mobileye, Aurora, Zoox).
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/autonomous-driving/`

## What to produce

A **foundational page set** covering the autonomous-driving stack from sensors up to safety / regulation, so later paper / textbook deep-dives can plug in.

The existing `intro.md` is a stub. **Rewrite it** with a real overview + numbered page list.

### Pages to create (target 12-16 pages)

| Position | Filename | Topic |
|---:|---|---|
| 1 | `intro.md` (rewrite) | Hub: scope, AV stack diagram, SAE levels, taxonomy of approaches, page list |
| 2 | `sae-levels-and-operational-design-domain.md` | SAE J3016 levels 0-5, ODD definitions, what each level means, regulatory mapping |
| 3 | `sensors-cameras-lidar-radar-imu.md` | Camera (rolling vs global shutter), LiDAR (mechanical / solid-state / FMCW), radar (FMCW, MIMO), IMU, GNSS/GPS, ultrasonic. Strengths, weaknesses, failure modes, weather sensitivity |
| 4 | `perception-object-detection-and-segmentation.md` | 2D/3D detection (YOLO/RetinaNet/DETR/PointPillars/CenterPoint), semantic / instance / panoptic segmentation, lane / drivable-area detection |
| 5 | `depth-estimation-and-stereo-vision.md` | Stereo geometry, monocular depth (MiDaS, DPT), self-supervised (Monodepth2), depth completion from LiDAR + camera |
| 6 | `sensor-fusion.md` | Early/mid/late fusion, BEV (bird's-eye view) representations, BEVFormer / BEVFusion, occupancy networks, multi-sensor calibration |
| 7 | `localization-and-hd-maps.md` | GPS + IMU dead reckoning, SLAM (LIO / VIO / GraphSLAM), HD map matching, vector / lanelet maps, localization without HD maps |
| 8 | `prediction-and-motion-forecasting.md` | Predicting other agents' motion: constant-velocity, social-LSTM, Trajectron++, multi-modal trajectory prediction, scene-level prediction, Argoverse / Waymo Open Motion |
| 9 | `motion-planning.md` | Search-based (A*, hybrid A*), sampling-based (RRT, RRT*, PRM), optimization-based (MPC, iLQR), trajectory optimization, lattice planners |
| 10 | `decision-making-and-behavior-planning.md` | Finite-state machines, behavior trees, POMDPs for AV, learning-based planners, rule-based vs ML hybrid |
| 11 | `control-pid-mpc-pure-pursuit-stanley.md` | Longitudinal (PID, MPC), lateral (pure pursuit, Stanley, MPC with vehicle dynamics models — kinematic bicycle, dynamic bicycle) |
| 12 | `end-to-end-driving.md` | Imitation learning (Bojarski/PilotNet), conditional imitation learning, world models (DreamerV3-like), Tesla FSD architecture, ALVINN historical context |
| 13 | `simulation-and-data.md` | CARLA, NVIDIA DRIVE Sim, AirSim, LGSVL/SVL, scenario generation, synthetic data, Sim2Real, log-replay |
| 14 | `safety-iso26262-sotif-scenario-testing.md` | Functional safety (ISO 26262, ASIL), SOTIF (ISO 21448), scenario-based testing, RSS (Mobileye), formal safety arguments, edge-case mining |
| 15 | `v2x-and-connected-vehicles.md` | DSRC vs C-V2X, V2V/V2I/V2P/V2N, cooperative perception, security & privacy, latency budgets |
| 16 | `adversarial-and-physical-attacks-on-av.md` | Cross-link to `/cs/adversarial-attacks/` — adversarial patches on signs, LiDAR spoofing, projector attacks, sensor jamming, defense considerations |

Adjust as needed; if you prefer fewer pages, group adjacent topics.

## Per-page format (depth addendum applies)

- Frontmatter: `title:`, `sidebar_position:` (per table)
- 1-paragraph elevator pitch
- **Definitions** — domain terms (ODD, ASIL, ego-vehicle, NPC, etc.)
- **Key concepts / formulas** — KaTeX math where relevant (e.g., Ackermann steering geometry $\tan\delta = L/R$, pure-pursuit lookahead $\delta = \arctan(2L\sin\alpha / \ell_d)$, MPC cost function, kinematic bicycle equations, EKF prediction/update)
- **Visual** (mandatory) — Mermaid pipeline diagram, sensor placement ASCII, or comparison table (sensor capabilities, planner trade-offs, level matrix)
- **Worked example** — concrete: trace Stanley control on a curve; design an MPC cost; size a lookahead distance from vehicle speed
- **PyTorch / Python sketch** — minimal code where appropriate (kinematic bicycle update, A* on a grid, EKF step, Hungarian assignment for multi-object tracking, BEV transformation)
- **Common pitfalls** — calibration drift, latency, weather, sensor occlusion, validation theater
- **Connections** — cross-links to other AV pages and `/cs/deep-learning/`, `/cs/reinforcement-learning/`, `/cs/embedded/`, `/cs/adversarial-attacks/`, `/math/engineering-math/` (ODEs / control), `/physics/signals-systems/`, `/physics/electromagnetics/` (radar / LiDAR EM)
- **Further reading** — name the canonical papers / books (Thrun's "Probabilistic Robotics", Pomerleau's ALVINN, Bojarski's "End-to-End Learning for Self-Driving Cars", Mobileye RSS, etc.) without writing deep-dives — those come when source material arrives

## Critical guidelines

- **Be concrete about real systems** where standard knowledge supports it: Waymo's stack, Tesla FSD evolution, Mobileye's REM/RSS, Cruise's incident history at a system-level — but only at facts that are public and stable. Don't speculate on internal architectures.
- **Honest scope**: this is foundational coverage. Don't deep-dive any single paper.
- **Math precision**: bicycle model, EKF equations, MPC formulation, IoU / mAP metrics.
- **Code precision**: PyTorch / NumPy / Python snippets must run mentally. Use `cv2`, `np`, `torch` consistently.

## Workflow

1. `ls` OUTPUT_DIR. Read existing `intro.md` to know the stub.
2. Plan the 12-16 pages (see table).
3. Write each detail page.
4. Rewrite `intro.md` last with a numbered list of every page you produced + a Mermaid diagram of the AV stack.
5. Print summary.

## Constraints

- Stay inside `f:/coding/SJ Wiki/docs/cs/autonomous-driving/`.
- Do not modify `_category_.json`, config files, `sidebars.ts`, `package.json`, or files outside OUTPUT_DIR.
- No `npm`. English. Precise. KaTeX math. Mermaid for visuals.
- Cross-doc links use absolute paths (`/cs/...`, `/math/...`, `/physics/...`).
- Mermaid labels with special characters (parens, equals, commas, slashes, braces, etc.) must be wrapped in `"..."`; internal `"` becomes `#quot;`.

Begin now.
