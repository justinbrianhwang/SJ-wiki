## IMAGE POLICY for SJ Wiki

Add **CC-licensed / public-domain images** from Wikimedia Commons to improve visual richness of wiki pages.

### Hard rules

1. **Source restriction**: ONLY embed images from **Wikimedia Commons** (`https://upload.wikimedia.org/wikipedia/commons/...`). Do not embed from random websites, blogs, or commercial sources. Do not embed paper figures directly from arxiv PDFs (link to paper instead).

2. **Conservative embedding**: If you are NOT confident an image exists at a specific Wikimedia Commons URL, **do not include it**. A broken image is worse than no image. Prefer Mermaid diagrams or descriptive captions when uncertain.

3. **Quality over quantity**:
   - Most pages: **1-2 images** at most.
   - Some pages: **0 images** is fine (text + Mermaid is enough).
   - Total target: roughly 20-40% of pages in your section get an image. Don't force one onto every page.

4. **Required format** (markdown):

   ```markdown
   ![Bloch sphere diagram showing a qubit state as a vector on the unit sphere](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bloch_sphere.svg/400px-Bloch_sphere.svg.png)

   *Figure: Bloch sphere representation of a qubit. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Bloch_sphere.svg), Smite-Meister, CC BY-SA 3.0.*
   ```

   - `alt`: descriptive, full-sentence.
   - Caption below in italics: brief description + `[Wikimedia Commons](file-page-url)` + author + license.

5. **Width handling**: Use Wikimedia thumbnail URLs (`.../thumb/.../400px-Filename.ext`) to keep images reasonable size. Common widths: `400px`, `500px`, `600px`.

6. **Where to add images** — focus on pages where a real image dramatically helps over text:

   - **Math**: famous geometric figures (e.g., torus, Möbius strip), classic plots (sine wave, normal distribution).
   - **CS**: architecture diagrams (neural nets, CPU pipeline), conceptual illustrations (B-tree, sorting visualization). For papers without Commons images, skip and use Mermaid.
   - **Physics**: phenomena (double-slit interference, planetary orbits), apparatus (Stern-Gerlach, LIGO), portraits of scientists (Einstein, Feynman) at section intros.
   - **Chemistry**: molecular structures (water, benzene), apparatus (Bunsen burner, periodic table image).
   - **QIS**: Bloch sphere, quantum circuit symbol diagrams, IBM Q hardware photos, satellite QKD diagrams — where they exist on Commons.

7. **Do not** alter or recreate copyrighted text/equations — only embed images with clear public licenses.

8. **Update count**: at the end of your section run, print a short summary of how many images you added across how many pages.

### Skipping is the right call

If a topic doesn't have an obvious well-known Wikimedia Commons image, **leave the page alone**. Better to have selectively rich pages than uniformly mediocre ones with broken or low-quality embeds.

---

Section-specific instructions follow below.

---

