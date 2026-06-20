# AGENT 6 — Safety & runtime enforcement

Create these 2 pages in `f:/coding/Web/SJ Wiki/docs/cs/autonomous-driving/`:

1. **`sensor-failure-safety-simulation.md`** — sidebar_position: 35
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Simulating the Effects of Sensor Failures on Autonomous Vehicles for Safety Evaluation.pdf`
   - Topic: **Simulating Sensor Failures for AV Safety Evaluation** (Matos, Durães, Cunha, Polytechnic Univ. Coimbra). Fault-injection / simulation of sensor failures (camera, LiDAR, GPS, IMU) to evaluate AV safety. Cover the failure taxonomy, the simulation/injection setup (likely CARLA), and the safety metrics. Use a failure-mode table.

2. **`shield-synthesis-runtime-enforcement.md`** — sidebar_position: 36
   - PDF: `f:/coding/Web/SJ Wiki/tmp/Shield Synthsis, Rntime Enforcement for Reactive Systems.pdf`
   - Topic: **Shield Synthesis: Runtime Enforcement for Reactive Systems** (Bloem, B. Könighofer, R. Könighofer, Wang, CAV 2015). A formal-methods paper: a "shield" is synthesized from a safety specification and attached to a reactive system/controller to correct its outputs at runtime with minimal deviation. Explain the automata-theoretic / safety-game synthesis with KaTeX/notation, and frame its relevance to AV runtime safety (a learned planner wrapped by a verified shield). Diagram the system → shield → actuator pipeline.

Cross-link to `/cs/autonomous-driving/safety-iso26262-sotif-scenario-testing`,
`/cs/autonomous-driving/simulation-and-data`,
`/cs/autonomous-driving/sensors-cameras-lidar-radar-imu`,
`/cs/autonomous-driving/decision-making-and-behavior-planning`, and
`/cs/adversarial-attacks/` (robustness) where relevant. The shield page may also link to any
formal-methods / theory pages if they exist.
