# AGENT 5 — Motion planning & control (classical)

Create these 4 pages in `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`:

1. **`frenet-trajectory-generation.md`** — sidebar_position: 31
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Optimal Trajectory Generation Frenet Frame.pdf`
   - Technique: **Optimal Trajectory Generation in a Frenét Frame** (Werling, Ziegler, Kammel, Thrun, ICRA 2010). The classic Frenet-frame lateral/longitudinal quintic-polynomial sampling planner. Derive the jerk-optimal quintic polynomials and the combined cost functional with KaTeX. This is a foundational planning paper — full depth. Diagram the s–d (station–lateral) decomposition.

2. **`sampling-based-motion-planning.md`** — sidebar_position: 32
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Efficient Sampling-Based Motion Planning for On-Road Autonomous Driving.pdf`
   - Technique: **Efficient Sampling-Based Motion Planning for On-Road Driving** (Ma, Xue et al., IEEE T-ITS 2015). On-road sampling planner; contrast with RRT*/lattice; explain the road-aligned sampling and cost evaluation.

3. **`urban-path-planning.md`** — sidebar_position: 33
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Path Planning and Decision Making for Autonomous Vehicle in Urban Environment.pdf`
   - Topic: **Path Planning & Decision Making in Urban Environments** (Fu, Song, Yang, Wang, IEEE ITSC 2015). The planning + behavior decision layer for urban driving.

4. **`mpc-for-autonomous-driving.md`** — sidebar_position: 34
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Model Predictive Control for Autonomous Driving Vehicles.pdf`
   - Technique: **Model Predictive Control for Autonomous Driving** (Vu, Moezzi, Cyrus, Hlava, Electronics 2021). MPC for path tracking with a vehicle model. Derive the receding-horizon QP, the kinematic/dynamic bicycle model, and constraints with KaTeX. Full depth.

Cross-link generously to `/cs/autonomous-driving/motion-planning`,
`/cs/autonomous-driving/decision-making-and-behavior-planning`,
`/cs/autonomous-driving/control-pid-mpc-pure-pursuit-stanley`, and to math pages
(`/math/numerical-analysis/...` for optimization, `/math/engineering-math/...` for ODEs) where natural.
