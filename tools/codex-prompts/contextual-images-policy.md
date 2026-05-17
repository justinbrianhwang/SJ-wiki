## CONTEXTUAL IMAGES POLICY (broad pass)

The wiki currently has architecture diagrams (Mermaid) and a few CC images but lacks "situation/context" images that make a wiki feel real. Add many more images across the wiki to fix this.

### What kinds of images to add

Pick the kind that **best fits the content** of each page. Examples:

- **Real-world scenarios / applications**: a robot in a maze (RL); an autonomous vehicle on a road (AV); Alice/Bob figure for cryptography; a NV diamond crystal for quantum sensing.
- **Physical apparatus / equipment**: inverted pendulum cart, Watt governor, NMR magnet, Stern-Gerlach apparatus, transmon chip.
- **Famous data examples**: MNIST sample digits, ImageNet category samples, KITTI driving scene.
- **Historical context**: portraits of key scientists (Turing, Shannon, Curie, Newton, Mendeleev) at the start of relevant sections — only when CC-licensed.
- **Natural phenomena**: aurora (magnetic field), rainbow (dispersion), double-slit pattern, crystal structures.
- **Industrial / hardware**: IBM Q processor photo, LIGO mirror, MRI machine, semiconductor wafer.
- **Conceptual cartoons**: Alice/Bob/Eve characters (cryptography), agent-environment cartoon (RL), gridworld maze.

### Critical URL rule

**For Wikimedia Commons, ALWAYS use `Special:FilePath/` format**:

```
https://commons.wikimedia.org/wiki/Special:FilePath/<Filename>
```

Example:
- ✅ `https://commons.wikimedia.org/wiki/Special:FilePath/Bloch_sphere.svg`
- ❌ `https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bloch_sphere.svg/...` ← do NOT construct hash paths. They will be wrong and 400.

Wikimedia auto-redirects `Special:FilePath/<filename>` to the correct CDN URL. You do not need to know the hash directory.

Use exact filenames you remember as well-known on Commons. Famous examples that exist:
- `Bloch_sphere.svg`, `Standard_Model_of_Elementary_Particles.svg`, `Periodic_table.svg`, `Snells_law.svg`, `Double-slit.svg`, `Inverted_pendulum.svg`, `Alice_Bob_Eve_simple_diagram_(crypto).png`, `Mendeleev_Table_5th_II.jpg`, `Albert_Einstein_Head.jpg`, `Newton-WilliamBlake.jpg`, `Periodic_table_large.svg`, `Stern-Gerlach_experiment.svg`, `RSA_Algorithm.svg`, `MNIST_digits.png`, `CartPole-v1.gif`, `Lorenz_attractor_yb.svg`, etc.

If you're not confident a specific filename exists, **prefer a similar concept that does** or skip the image.

### Other allowed sources

- **arxiv ar5iv**: `https://ar5iv.labs.arxiv.org/html/<id>/x<N>.png` — use only when you're confident in the figure number for that paper.
- **NASA images**: `https://images-assets.nasa.gov/...` (public domain).
- **NIST / NIH / USGS / ESA / CERN**: typically public domain.
- **PyTorch / HuggingFace official tutorial figures**: open-source license.
- **GitHub raw figures from author repos**: only if the repo has a clear permissive license (MIT, Apache 2.0, CC-BY).

### Format

```markdown
![Descriptive alt text — full sentence.](IMAGE_URL)

*Figure: brief description. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:FILENAME), Author, CC BY-SA 4.0 (or appropriate license).*
```

### Quantity expectation

- **Most pages get 1-3 contextual images** beyond what's already there.
- Hub pages (intro.md) of each subtopic should have 2-5 images that set the scene.
- Don't force an image into every section header — pick where it really helps comprehension.
- Hot pages where readers want visual context (RL gridworld, crypto Alice-Bob, control inverted pendulum, NV magnetometry, etc.) get richer treatment.

### Skip when uncertain

If you cannot remember a specific Wikimedia filename or are unsure, leave the page alone. Better to have selectively rich pages than uniformly broken ones.

### Output

End-of-run summary: how many images added across how many pages, broken down by source.

---

Section-specific instructions follow.

---

