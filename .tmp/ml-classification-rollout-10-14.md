# Classification screenshot rollout: lessons 10–14

Worker scope: every Markdown image reference in `10-training-log-reg.md`,
`11-log-reg-interpretation.md`, `12-using-log-reg.md`, `13-summary.md`, and
`14-explore-more.md`. The worker has the `imagegen` skill; exact notebook
code/output uses deterministic crops, while bounded explanatory illustrations
use the built-in imagegen workflow after source inspection.

## Accepted assets

- `10-training-log-reg-01-fit.jpg` → `10-training-log-reg-01-fit-cropped.png`
  — deterministic crop `(x=15, y=32, w=440, h=105)`, 2× Lanczos resize and
  light unsharp; preserved the import, model construction, and `fit` call;
  removed notebook/browser frame and camera tile.

- `10-training-log-reg-02-coefficients.jpg` →
  `10-training-log-reg-02-coefficients-cropped.png` — deterministic composite
  of the intercept crop `(15,32,440,52)` and coefficient crop
  `(15,82,505,115)`, 2× Lanczos resize and light unsharp; preserved the exact
  bias and 45-weight array and removed the handwritten annotation/camera tile.
