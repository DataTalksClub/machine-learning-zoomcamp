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

- `10-training-log-reg-03-soft-predictions.jpg` →
  `10-training-log-reg-03-soft-predictions-cropped.png` — deterministic crop
  `(15,190,300,100)`, 2× Lanczos resize and light unsharp; preserved the
  `predict_proba` matrix and removed the handwritten “SOFT PREDICTIONS”
  annotation and camera tile.

- `10-training-log-reg-04-churn-decision.jpg` →
  `10-training-log-reg-04-churn-decision-cropped.png` — deterministic crop
  `(15,160,505,110)`, with a pixel-level repair restoring the selected
  `True` glyph from the adjacent unselected output, then 2× Lanczos resize
  and light unsharp; preserved `y_pred >= 0.5` and the exact boolean output,
  removed the camera tile and selection highlight.

- `10-training-log-reg-05-selected-customers.jpg` →
  `10-training-log-reg-05-selected-customers-cropped.png` — deterministic crop
  `(15,82,505,220)`, 2× Lanczos resize and light unsharp; preserved the mask,
  representative customer IDs, and exact `Length: 311` output while removing
  the camera tile and notebook frame.

- `10-training-log-reg-06-accuracy.jpg` →
  `10-training-log-reg-06-accuracy-cropped.png` — deterministic crop
  `(15,82,505,220)`, 2× Lanczos resize and light unsharp; preserved both
  `0.8034066713981547` calculations and the dataframe construction while
  removing the camera tile and notebook frame.

- `11-log-reg-interpretation-01-zip.jpg` →
  `11-log-reg-interpretation-01-zip-cropped.png` — deterministic composite of
  the simple `zip` example crop `(15,32,490,48)` and model-output crop
  `(15,82,505,255)`, 2× Lanczos resize and light unsharp; preserved the exact
  dictionary output and coefficient names/values while removing the camera
  tile and browser frame.
