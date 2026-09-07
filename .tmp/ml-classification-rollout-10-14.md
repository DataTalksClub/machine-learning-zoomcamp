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

- `11-log-reg-interpretation-02-coefficients.jpg` →
  `11-log-reg-interpretation-02-coefficients-cropped.png` — deterministic crop
  `(15,82,505,200)`, 2× Lanczos resize and light unsharp; preserved the exact
  visible feature/weight pairs and their signs while removing camera, browser
  chrome, and the unrelated following lesson heading. The source frame itself
  begins partway through the long dictionary and that source-edge truncation
  remains documented.

- `11-log-reg-interpretation-03-small-features.jpg` →
  `11-log-reg-interpretation-03-small-features-cropped.png` — deterministic
  crop `(15,32,490,235)`, 2× Lanczos resize and light unsharp; preserved the
  five feature names, vectorizer fit, transform, and small-model setup while
  removing the camera tile and notebook/browser frame.

- `11-log-reg-interpretation-04-small-model-weights.jpg` →
  `11-log-reg-interpretation-04-small-model-weights-cropped.png` —
  deterministic crop `(15,45,490,220)`, 2× Lanczos resize and light unsharp;
  preserved the bias and five exact weights plus the training output while
  removing the camera/browser chrome. The first training cell is source-edge
  clipped, so that limitation remains visible rather than being invented.

- `11-log-reg-interpretation-05-first-example.jpg` →
  `11-log-reg-interpretation-05-first-example-rendered.png` — deterministic
  notebook-style render from the exact lesson code/output: `-3.473` and
  `0.030090303318277657`. The source screenshot was rejected because it
  showed the later month-to-month example (`0.418...`) instead of the
  surrounding two-year-customer example; no generated approximation was used.

- `11-log-reg-interpretation-06-second-example-slide.jpg` →
  `11-log-reg-interpretation-06-second-example-imagegen.png` — built-in
  imagegen replacement from inspected/cropped source `(0,8,508,285)`.
  Preserved the exact score equation, `1Y`/`2Y` zeroed contract terms,
  monthly-charge and tenure terms, and `-0.33` result; removed the presenter,
  camera/recording controls, and color wheel. Output visually checked at
  lesson size.
