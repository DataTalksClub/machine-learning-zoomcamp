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

### Screenshot 03 — train and validate

- Source: `cohorts/2026/02-regression/images/10-car-price-validation-03-train-and-validate.jpg`.
- Caption/context: “Training the model and computing the RMSE on the validation set”; the section contrasts preparation/training on `df_train` with prediction and RMSE on `df_val`.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because the consecutive notebook cells show the full train/validation handoff and its measured result.
- Disposition: `crop/replace` via deterministic raster export; exact code and numeric output are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x207+26+82`, then 2× Lanczos resize and light unsharp masking. This retains the complete helper/training/validation cells and result while removing browser/Zoom chrome, webcam tile, lesson heading, and recording frame.
- Invariants/QA: preserve `prepare_X`, `train_linear_regression`, `df_train`, `df_val`, `rmse(y_val, y_pred)`, and `0.7616530991301577`. Final `1066x414` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/10-car-price-validation-03-train-and-validate-cropped.png`.

### Screenshot 04 — training versus validation parts

- Source: `cohorts/2026/02-regression/images/10-car-price-validation-04-train-vs-validation-parts.jpg`.
- Caption/context: “The training part and the validation part of the code”; the bullets immediately below explain which dataset each block may touch.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the handwritten `TRAIN` and `VAL` annotations add a useful visual partition that the code alone does not provide.
- Disposition: `crop/replace` via deterministic raster export; exact code, output, and annotations are fidelity-sensitive, so imagegen was not used.
- Crop: source `598x360`; `533x207+26+82`, with a small notebook-background patch over the cursor (`local x=454..470, y=158..173`), then 2× Lanczos resize and light unsharp masking. This removes browser/Zoom chrome, webcam tile, lesson heading, and recording frame.
- Invariants/QA: preserve both code blocks, the `TRAIN` / `VAL` annotations and line, and result `0.7616530991301577`; the patch touches only blank cell background. Final `1066x414` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/10-car-price-validation-04-train-vs-validation-parts-cropped.png`.

## 11 — feature engineering

### Screenshot 01 — year column

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-01-year-column.jpg`.
- Caption/context: “The training dataset with the year column”; the lesson motivates transforming `year` into car age.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the selected `year` column and representative old/new rows make the raw feature concrete.
- Disposition: `crop/replace` via deterministic raster export; exact table values are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `165x215+135+145`, then 2× Lanczos resize and light unsharp masking. This focuses on the complete `make`, `model`, and selected `year` columns and removes browser/Zoom chrome, webcam tile, code-cell fragments, cursor, and clipped adjacent columns.
- Invariants/QA: preserve the `year` header, rows 0–4 and 7145–7148, and all visible make/model/year values. Final `330x430` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or partial adjacent column; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-01-year-column-cropped.png`.

### Screenshot 02 — car age calculation

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-02-car-age.jpg`.
- Caption/context: “Computing the age of each car as 2017 minus year”; the lesson defines age as `2017 - year` and shows the resulting series.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because the exact vector output demonstrates the transformation across the first and last rows.
- Disposition: `crop/replace` via deterministic raster export; exact expression and values must remain unchanged, so imagegen was not used.
- Crop: source `598x360`; `533x190+26+104`, then 2× Lanczos resize and light unsharp masking. This retains the complete expression and visible output while removing browser/Zoom chrome, webcam tile, headings, and recording frame.
- Invariants/QA: preserve `2017 - df_train.year`, rows 0–4 and 7145–7149, their age values, and `Name: year, Length: 7150, dtype: int64`. Final `1066x380` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-02-car-age-cropped.png`.

### Screenshot 03 — adding `age` to `prepare_X`

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-03-age-feature.jpg`.
- Caption/context: “The prepare_X function with the new age feature”; the section adds `df['age'] = 2017 - df.year` before selecting the numerical features.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because the focused cell shows exactly where the derived feature is created and then included in the matrix.
- Disposition: `crop/replace` via deterministic raster export; exact Python code is the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x130+26+230`, then 2× Lanczos resize and light unsharp masking. This retains the complete function and removes the browser/Zoom frame, webcam tile, clipped lesson heading, and following-cell material.
- Invariants/QA: preserve `df['age'] = 2017 - df.year`, `df[base]`, `fillna(0)`, `.values`, and `return X`. Final `1066x260` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-03-age-feature-cropped.png`.

### Screenshot 04 — modified dataframe

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-04-modified-dataframe.jpg`.
- Caption/context: “Running prepare_X added the age column to df_train”; the section uses this visible mutation to motivate copying the dataframe.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the added `age` row is concrete evidence of the unintended side effect discussed in the prose.
- Disposition: `crop/replace` via deterministic raster export; exact dtype output and selection highlight are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x245+26+72`, then 2× Lanczos resize and light unsharp masking. This retains the complete `df_train.dtypes` output, selected `age` row, and `dtype: object` while removing browser/Zoom chrome, webcam tile, headings, and recording frame.
- Invariants/QA: preserve all visible column/type pairs, especially `age int64`, the selection highlight, and the final dtype line. Final `1066x490` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-04-modified-dataframe-cropped.png`.

### Screenshot 05 — copying the dataframe

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-05-dataframe-copy.jpg`.
- Caption/context: “With df.copy() the original dataframe is no longer modified”; the lesson presents this function as the fix for the visible side effect.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because the focused code cell makes the non-mutating fix visible without the surrounding notebook clutter.
- Disposition: `crop/replace` via deterministic raster export; exact Python code is the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x175+26+72`, then 2× Lanczos resize and light unsharp masking. This keeps the complete `prepare_X` implementation with `df.copy()` and removes browser/Zoom chrome, webcam tile, headings, incomplete output, and recording frame.
- Invariants/QA: preserve `df = df.copy()`, age creation, feature selection, `fillna(0)`, `.values`, and `return X`; no clipped output is presented as evidence. Final `1066x350` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-05-dataframe-copy-cropped.png`.

### Screenshot 06 — RMSE improvement

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-06-rmse-improvement.jpg`.
- Caption/context: “The RMSE dropped from 0.76 to 0.51 with the age feature”; the section compares the new validation result with the baseline.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the exact validation code and measured `0.5172055461058291` output provide evidence of the improvement.
- Disposition: `crop/replace` via deterministic raster export; exact code and numeric output are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x145+26+190`, then 2× Lanczos resize and light unsharp masking. This removes browser/Zoom chrome, webcam tile, preceding code, headings, and recording frame while retaining the complete validation cell and result.
- Invariants/QA: preserve the training/validation calls, `rmse(y_val, y_pred)`, and exact output `0.5172055461058291`. The source's small native selection highlight over the leading digits remains because removing it would damage the exact output; it is recorded as a limitation. Final `1066x290` PNG otherwise has no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-06-rmse-improvement-cropped.png`.

### Screenshot 07 — prediction/target distributions

- Source: `cohorts/2026/02-regression/images/11-feature-engineering-07-distribution-comparison.jpg`.
- Caption/context: “The distributions of predictions and actual values are now much closer”; the prose interprets the red/blue histogram overlap after adding age.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the plot supplies visual evidence of the distributional improvement and the handwritten arrows call out the remaining mismatch.
- Disposition: `crop/replace` via deterministic raster export; plot geometry, colors, and values are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x270+26+72`, then 2× Lanczos resize and light unsharp masking. This keeps the plotting code, output label, complete histogram, axes, and annotations while removing browser/Zoom chrome, webcam tile, headings, and recording frame.
- Invariants/QA: preserve both histogram calls, red/blue series, bins `50`, axes, bar heights/shape, and blue arrows. Final `1066x540` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/11-feature-engineering-07-distribution-comparison-cropped.png`.

## 12 — categorical variables

### Screenshot 01 — object columns

- Source: `cohorts/2026/02-regression/images/12-categorical-variables-01-object-columns.jpg`.
- Caption/context: “The columns with the object type are the categorical variables”; the lesson uses `df_train.dtypes` to identify string columns.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the complete dtype listing distinguishes categorical `object` columns from numeric columns.
- Disposition: `crop/replace` via deterministic raster export; exact labels and dtypes are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x268+26+72`, then 2× Lanczos resize and light unsharp masking. This retains the complete command and dtype output while removing browser/Zoom chrome, webcam tile, cursor, headings below the output, and recording frame.
- Invariants/QA: preserve every visible column/type pair and final `dtype: object`. Final `1066x536` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/12-categorical-variables-01-object-columns-cropped.png`.

### Screenshot 03 — number-of-doors loop

- Source: `cohorts/2026/02-regression/images/12-categorical-variables-03-doors-loop.jpg`.
- Caption/context: “The prepare_X function with the number-of-doors columns added”; the section introduces the loop that creates `num_doors_2`, `num_doors_3`, and `num_doors_4`.
- Rubric: `2 / 2 / 2 / 1 / 2 / 2 = 11/12`; keep because the focused code cell shows the categorical-to-binary loop and the exact generated column names.
- Disposition: `crop/replace` via deterministic raster export; exact Python code is the source of truth, so imagegen was not used.
- Crop: source `598x360`; `533x140+26+158`, then 2× Lanczos resize and light unsharp masking. This retains the complete function through the door-feature loop and removes browser/Zoom chrome, webcam tile, previous output fragment, cursor, and following incomplete lines.
- Invariants/QA: preserve `base.copy()`, age creation, loop values `[2, 3, 4]`, comparison expression, `astype('int')`, and both feature-name expressions. Final `1066x280` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or clipped next cell; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/12-categorical-variables-03-doors-loop-cropped.png`.

### Screenshot 02 — one-hot encoding diagram

- Source: `cohorts/2026/02-regression/images/12-categorical-variables-02-encoding-diagram.jpg`.
- Caption/context: “One categorical column with values 2, 3, 4, 2 represented as three binary columns”; the section explains the one-hot transformation row by row.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the diagram directly shows the original category and the resulting one-hot columns, values, and row alignment.
- Disposition: `keep` original; this is already a clean `1492x1054` explanatory diagram with no face, webcam tile, browser/Zoom chrome, cursor, watermark, or black border. Imagegen was not used because the existing exact labels and matrix values are already crisp.
- QA: source inspected with `view_image`; all required headers, rows, arrows, and 0/1 values are readable at lesson size, the Markdown reference resolves, and `git diff --check` passes. No replacement asset was created.
