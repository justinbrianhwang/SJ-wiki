## Domain: Physics + Math + Chemistry

- **TARGET_DIRS**:
  - `f:/coding/SJ Wiki/docs/physics/`
  - `f:/coding/SJ Wiki/docs/math/`
  - `f:/coding/SJ Wiki/docs/chemistry/`

### Guidance

Most math/physics/chemistry pages don't need "architecture" diagrams as such, but several have **system / apparatus / protocol** diagrams worth detailing in Mermaid:

- **Physics**
  - `physics/quantum-mechanics/intro.md`: postulates as a flowchart linking state → operator → measurement → Born rule → time evolution.
  - `physics/quantum-mechanics/scattering-theory.md`: partial-wave expansion + Born series structure.
  - `physics/signals-systems/*`: LTI block diagrams (impulse response, convolution, Laplace/z-domain).
  - `physics/simulation/*`: simulation loop (model → numerical integrator → state update → measurement → control input) — already arch-flavored.
  - `physics/electromagnetics/*`: transmission-line equivalent circuit, antenna feed system, Smith chart matching circuit, waveguide mode structure.
  - `physics/quantum-field-theory/perturbation-and-feynman-diagrams.md`: Feynman rule lookup as a flowchart (vertex / propagator / external leg → integrand factor).
  - `physics/mechanics/*`: free-body workflow (identify body → enumerate forces → choose axes → write balance → solve).

- **Math**
  - `math/engineering-math/laplace-transform.md`: Laplace transform pipeline (time signal → integral → s-domain → algebraic manipulation → inverse → time).
  - `math/engineering-math/fourier-series.md`, `fourier-integrals-and-transforms.md`: signal → analysis equation → spectrum → synthesis equation.
  - `math/numerical-analysis/*`: each algorithm as a flowchart (initialize → loop → convergence test → return).
  - `math/graph-theory/*`: algorithm flowcharts (BFS, DFS, Dijkstra, MST) plus example graph structures.
  - `math/probability-and-random-variables/markov-chains.md`: state machine diagrams for canonical MCs (random walk, birth-death, queueing M/M/1).

- **Chemistry**
  - `chemistry/general/electrochemistry.md`: galvanic cell diagram (anode / cathode / salt bridge / external circuit + standard potential annotations).
  - `chemistry/general/chemical-kinetics.md`: reaction-coordinate diagram (energy vs progress with activation energy + transition state).
  - `chemistry/general/chemical-equilibrium.md`: ICE table workflow as a flowchart.
  - `chemistry/physical-chemistry/phase-transitions-and-phase-diagrams.md`: water phase diagram annotated; Clausius-Clapeyron derivation flow.
  - `chemistry/physical-chemistry/rate-laws-and-reaction-mechanisms.md`: steady-state approximation derivation steps.

### Hard rule

If a math/physics/chemistry page is mostly about a theorem or proof (e.g., "proof of Cauchy's theorem"), do NOT shoehorn an architecture-style diagram in. Skip those pages. Only enhance pages where a system/apparatus/protocol/algorithm diagram genuinely helps.

Apply the policy. Begin now.
