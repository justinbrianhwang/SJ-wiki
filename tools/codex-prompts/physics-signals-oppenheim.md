You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Alan V. Oppenheim, Alan S. Willsky, with S. Hamid - Signals and Systems -Prentice Hall (1996).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/physics/signals-systems/`
- **SUBJECT**: Signals and Systems (Oppenheim, Willsky, Nawab — *Signals and Systems*, 2nd ed)

## Produce

1. **`intro.md`** — overview + chapter list.

2. **12-18 detail pages** covering:
   - Signals (continuous- and discrete-time, transformations of time, periodicity, energy/power)
   - Systems (linearity, time-invariance, causality, memory, stability, invertibility)
   - LTI systems and convolution (CT and DT)
   - Fourier series (CT and DT periodic signals)
   - Continuous-time Fourier transform (CTFT)
   - Discrete-time Fourier transform (DTFT)
   - Sampling theorem (Nyquist), aliasing, reconstruction
   - Z-transform and its properties; ROC
   - Laplace transform and its properties; ROC
   - Frequency response, filtering (lowpass / highpass / bandpass)
   - Modulation (AM/FM/sampling as modulation)
   - State-space (introduction, if covered)

3. Per-page: definitions → key formulas (LaTeX) → properties table → worked example → MATLAB/Python (NumPy/SciPy) snippet.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` for TOC. 3. Iterate. 4. `intro.md` last.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate.

Begin now.
