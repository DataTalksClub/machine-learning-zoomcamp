# ML Zoomcamp regression screenshot rollout: lessons 09–12

Scope: every Markdown image reference in `09-rmse.md`,
`10-car-price-validation.md`, `11-feature-engineering.md`, and
`12-categorical-variables.md`.

Rubric order is instructional contribution / relevance / readability and focus /
complementarity / durability / caption and accessibility, scored 0–2 each.
Imagegen was available and read completely. It is reserved for bounded
explanatory illustrations; exact formulas, code, plots, numbers, notebook
outputs, and UI are handled deterministically.

## 09 — RMSE

### Screenshot 01 — RMSE formula

- Source: `cohorts/2026/02-regression/images/09-rmse-01-rmse-formula.jpg`.
- Caption/context: “Writing the RMSE formula”; the surrounding text introduces the formula and the first `rmse` function cell.
- Rubric: `1 / 2 / 2 / 1 / 2 / 2 = 10/12`; keep because the handwritten formula connects the metric to the implementation, while the plot and code provide useful notebook context.
- Disposition: `crop/replace` via deterministic raster export; formula and code are exact instructional content, so imagegen was not used.
- Crop: source `598x360`; `565x288+16+72`, then 2× Lanczos resize and light unsharp masking. This removes the browser header, webcam tile, recording marker, black frame edges, and controls while keeping the plot, formula, code cell, and section context.
- Invariants/QA: preserve the full `sqrt(1/m Σ(g(x_i)-y_i)^2)` notation, `def rmse(y, y_pred):`, and visible notebook context. Final `1130x576` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-01-rmse-formula-cropped.png`.

### Screenshot 02 — predictions and actual prices

- Source: `cohorts/2026/02-regression/images/09-rmse-02-predictions-vs-actual-prices.jpg`.
- Caption/context: “Predictions and actual values as two arrays”; the lesson introduces the four paired predictions and target prices before taking their differences.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the aligned arrays make the pairing that drives every later error calculation immediately visible.
- Disposition: `crop/replace` via deterministic raster export; the exact values and handwritten notation are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `482x343+23+0`, then 2× Lanczos resize and light unsharp masking. This removes the recording marker, webcam tile, black side frame, and bottom controls while retaining the complete diagram.
- Invariants/QA: preserve `g(x_i)-y_i`, `PRED`, `PRICE`, `y-pred`, `y-train`, values `10, 9, 11, …, 10` and `9, 9, 10.5, …, 11.5`, and their row alignment. Final `964x686` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-02-predictions-vs-actual-prices-cropped.png`.

### Screenshot 03 — differences

- Source: `cohorts/2026/02-regression/images/09-rmse-03-differences.jpg`.
- Caption/context: “Taking the differences between predictions and actual values”; the next worked-example step turns the paired rows into four errors.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the third row of values and the resulting error row make the elementwise subtraction concrete.
- Disposition: `crop/replace` via deterministic raster export; exact notation and values must remain unchanged, so imagegen was not used.
- Crop: source `598x360`; `525x343+23+0`, then a deterministic blank-board mask over only the webcam rectangle (`local x=482..524, y=0..70`), 2× Lanczos resize, and light unsharp masking. The wider crop is needed to keep the final `-1.5` cell complete.
- Invariants/QA: preserve the formula, both input rows, the error row `1, 0, 0.5, …, -1.5`, and row alignment. Final `1050x686` PNG inspected; the mask touches only blank board behind the camera, and no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border remains. Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-03-differences-cropped.png`.

### Screenshot 04 — squared errors and mean

- Source: `cohorts/2026/02-regression/images/09-rmse-04-squared-errors-mean.jpg`.
- Caption/context: “Squaring the differences and taking the mean”; the prose explains why squaring avoids cancellation and then calculates MSE as `0.875`.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the visual calculation shows both the squared-error values and their mean in one step.
- Disposition: `crop/replace` via deterministic raster export; the handwritten arithmetic is exact source content, so imagegen was not used.
- Crop: source `598x360`; `525x290+23+0`, with the webcam area replaced only over blank board (`local x=482..524, y=0..70`), then 2× Lanczos resize and light unsharp masking. The crop also removes the partial next-step square-root fragment at the source bottom.
- Invariants/QA: preserve `1, 0, 0.25, 2.25`, `(1+0+0.25+2.25)/4`, `= 0.875`, and the `SQUARED ERROR` / `MEAN SE` annotations. Final `1050x580` PNG inspected; no face, camera tile, browser/Zoom chrome, cursor, watermark, black border, or partial next-step fragment remains. Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-04-squared-errors-mean-cropped.png`.

### Screenshot 05 — mean calculator

- Source: `cohorts/2026/02-regression/images/09-rmse-05-mean-calculator.jpg`.
- Caption/context: “Computing the mean of the squared errors”; the surrounding prose and code already show `(1 + 0 + 0.25 + 2.25) / 4 = 0.875`.
- Rubric: `1 / 2 / 1 / 1 / 0 / 1 = 6/12`; remove because the transient Google calculator adds no durable evidence beyond the written arithmetic and the source UI is low-resolution.
- Disposition: `remove`; the original JPG remains in the repository but is no longer referenced. A crop candidate was reviewed and rejected for the same redundancy/readability reasons.
- QA: source and context inspected; the Markdown reference was removed, no other lesson content changed, and `git diff --check` passes before commit.

### Screenshot 06 — RMSE implementation

- Source: `cohorts/2026/02-regression/images/09-rmse-06-rmse-implementation.jpg`.
- Caption/context: “Implementing rmse and evaluating the baseline model”; the section explains the function and shows the baseline result `0.7554192603920132`.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because it links the handwritten formula, exact NumPy implementation, and observed baseline score in one view.
- Disposition: `crop/replace` via deterministic raster export; exact code and numeric output are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `565x288+16+72`, then 2× Lanczos resize and light unsharp masking. This removes the browser header, webcam tile, recording marker, black frame edges, and controls.
- Invariants/QA: preserve the formula, complete `rmse` function, call `rmse(y_train, y_pred)`, and output `0.7554192603920132`. Final `1130x576` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-06-rmse-implementation-cropped.png`.

## 10 — validation data

### Screenshot 01 — train/validation/test split

- Source: `cohorts/2026/02-regression/images/10-car-price-validation-01-split-diagram.jpg`.
- Caption/context: “Train, validation and test sets: the model g is trained on train and applied to validation”; the opening section explains why validation must use unseen data.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the arrows show the training/validation relationship more directly than prose alone.
- Disposition: `crop/replace` via deterministic raster export; the exact labels and arrow directions are fidelity-sensitive, so imagegen was not used.
- Crop: source `598x360`; `380x260+126+31`, then a small blank-board mask over the cursor (`local x=52..70, y=141..158`), 2× Lanczos resize, and light unsharp masking. This removes the recording marker, webcam tile, black frame, controls, and cursor.
- Invariants/QA: preserve the `TRAIN`, `VAL`, and `TEST` partitions, model `g`, and both arrow directions. Final `760x520` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/10-car-price-validation-01-split-diagram-cropped.png`.

### Screenshot 02 — `prepare_X` function

- Source: `cohorts/2026/02-regression/images/10-car-price-validation-02-prepare-x-function.jpg`.
- Caption/context: “The prepare_X function in the notebook”; the section breaks one-line feature preparation into selection, filling missing values, and extracting `.values`.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because the focused notebook cell shows the exact three-step transformation and its order.
- Disposition: `crop/replace` via deterministic raster export; exact Python code is the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x90+26+176`, then 2× Lanczos resize and light unsharp masking. This keeps only the complete `prepare_X` cell and removes browser/Zoom chrome, webcam tile, lesson headings, cursor, and recording frame.
- Invariants/QA: preserve `def prepare_X(df)`, `df[base]`, `fillna(0)`, `.values`, and `return X` exactly. Final `1066x180` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/10-car-price-validation-02-prepare-x-function-cropped.png`.
