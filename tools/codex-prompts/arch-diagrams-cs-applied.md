## Domain: CS Applied (Autonomous Driving, Adversarial, Cryptography, Control, Software Engineering)

- **TARGET_DIRS**:
  - `f:/coding/SJ Wiki/docs/cs/autonomous-driving/`
  - `f:/coding/SJ Wiki/docs/cs/adversarial-attacks/`
  - `f:/coding/SJ Wiki/docs/cs/cryptography/`
  - `f:/coding/SJ Wiki/docs/cs/control-engineering/`
  - `f:/coding/SJ Wiki/docs/cs/software-engineering/`

### Guidance

- **Autonomous Driving**:
  - `intro.md` / `sae-levels-and-operational-design-domain.md`: full AV stack pipeline (sensors → perception → fusion → localization → prediction → planning → control → actuators) with real data flow types annotated on arrows (point cloud, images, BEV grid, object list, future-trajectory set, motion command).
  - `sensors-cameras-lidar-radar-imu.md`: comparison block diagram of each sensor's processing chain.
  - `perception-object-detection-and-segmentation.md`: PointPillars / CenterPoint / VoxelNet architectures (detailed: voxelization → backbone → detection head).
  - `prediction-and-motion-forecasting.md`: VectorNet vectorization + graph encoder; HiVT hierarchical attention.
  - `sensor-fusion.md`: early/mid/late fusion variants; BEV fusion architecture (BEVFormer-style spatial cross attention).
  - `motion-planning.md`: A*/Hybrid A* search expansion, MPC receding horizon loop.
  - `control-pid-mpc-pure-pursuit-stanley.md`: closed-loop PID with plant; MPC optimization loop with horizon shift.
  - `end-to-end-driving.md`: ChauffeurNet / TransFuser / UniAD / world-model / VLA pipelines as block diagrams.
  - `safety-iso26262-sotif-scenario-testing.md`: V-model + ISO 26262 lifecycle phases; SOTIF flow.

- **Adversarial Attacks**:
  - `white-box-attacks.md`: PGD iteration loop with projection step explicit (gradient step → project to $\epsilon$-ball → clip to valid range); C&W optimization loop with logit-difference objective.
  - `adversarial-training.md`: min-max training loop with inner PGD and outer SGD; TRADES dual objective.
  - `certified-defenses-and-randomized-smoothing.md`: randomized smoothing decision boundary; IBP bound propagation through a small net.
  - `physical-world-and-patch-attacks.md`: patch optimization pipeline (image + patch placement → physical transformations → classifier → loss → gradient back to patch).
  - `evaluation-and-benchmarks.md`: AutoAttack ensemble; adaptive evaluation flow.

- **Cryptography**:
  - `symmetric-encryption-modes.md`: ECB / CBC / CTR / GCM mode block diagrams with IV/nonce flow.
  - `message-authentication-codes.md`: HMAC inner/outer hash structure; CBC-MAC chain.
  - `authenticated-encryption-gcm.md`: GHASH + CTR composition.
  - `rsa-and-oaep.md`: OAEP padding feistel-like structure.
  - `discrete-log-diffie-hellman.md`: DH exchange protocol diagram.
  - `tls-protocol-overview.md`: TLS 1.3 handshake message sequence (ClientHello / ServerHello / EncryptedExtensions / Certificate / Finished).
  - `zero-knowledge-proofs.md`: Schnorr Sigma protocol three-move structure.

- **Control Engineering**:
  - `introduction-to-feedback-control.md`: classical feedback loop with R / E / C / G / H / Y blocks.
  - `block-diagrams-signal-flow-and-mason.md`: full block algebra examples.
  - `state-space-controller-observer-design.md`: separation principle diagram (plant + observer + controller).
  - `pid-lead-lag-and-lag-lead-compensators.md`: each compensator's pole-zero location and frequency response shape.
  - `digital-control-sampling-and-z-transform.md`: ZOH + sampler + digital controller in closed loop.

- **Software Engineering**:
  - `software-life-cycle-models.md`: waterfall / V / spiral / agile lifecycles.
  - `software-design.md`: layered / MVC / microservices / event-driven architecture diagrams.
  - `software-testing.md`: V-model with test levels aligned to dev phases.

Apply the policy. Begin now.
