# ML Zoomcamp trees/deep-learning screenshot rollout: 05–08 scope

The delegated shorthand names do not exist in this checkout: there is no
`06-trees/05-xgboost.md` or standalone `08-deep-learning.md`. The four actual
lesson files in the owned numbered range are `06-trees/05-decision-tree-tuning.md`
through `06-trees/08-xgb-tuning.md`; this report covers those 19 references.

## 05 — decision tree parameter tuning, screenshot 01

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-01-parameters.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the exact
  `DecisionTreeClassifier` parameter names and values are notebook content, so
  imagegen was not used.
- Crop coordinates: source `598x360`; `470x285+25+55` (`x=25, y=55,
  width=470, height=285`). This removes the browser/recording strip, presenter
  webcam tile, right black bar, and frame edges while keeping the lesson title,
  parameter bullets, and classifier parameter list.
- Invariants: preserve `DecisionTreeClassifier()`, `criterion='gini'`,
  `splitter='best'`, `max_depth=None`, `min_samples_split=2`,
  `min_samples_leaf=1`, `min_weight_fraction_leaf=0.0`, and
  `max_features=None` exactly as visible in the source.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-01-parameters-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  exact notebook parameter text is fidelity-sensitive. One crop was accepted.
- QA: final `940x570` PNG inspected visually; the required title, labels, and
  values remain crisp, with no face, camera tile, browser/Zoom chrome, cursor,
  watermark, overlay, or black bar. The source itself truncates the dropdown
  below the visible lower edge; no missing lines were invented. Markdown
  reference resolves and `git diff --check` passes before commit.

## 05 — decision tree parameter tuning, screenshot 02

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-02-max-depth-scores.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the validation
  AUC values and notebook expression are exact numeric content, so imagegen was
  not used.
- Crop coordinates: source `598x360`; `310x195+90+140` (`x=90, y=140,
  width=310, height=195`). This focuses on the complete printed depth/AUC
  output and the instructor's blue highlight, removing the notebook chrome,
  presenter webcam tile, and lesson-frame material.
- Invariants: preserve depths `1, 2, 3, 4, 5, 6, 10, 15, 20, None`, values
  `0.606`, `0.669`, `0.739`, `0.761`, `0.766`, `0.762`, `0.683`, `0.672`,
  `0.667`, `0.664`, and the highlighted 4–6 range.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-02-max-depth-scores-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  guessing numeric output would be unsafe. One crop was accepted.
- QA: final `620x390` PNG inspected visually; all rows and values are readable,
  with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay,
  or black bar. Markdown reference resolves and `git diff --check` passes
  before commit.

## 05 — decision tree parameter tuning, screenshot 03

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-03-grid-search.jpg`.
- Disposition: `crop/replace` via deterministic raster export; this is an exact
  dataframe preview with numeric AUC values, so imagegen was not used.
- Crop coordinates: source `598x360`; `260x120+125+220` (`x=125, y=220,
  width=260, height=120`). This isolates the dataframe header and first five
  rows, removing the notebook code cell, presenter webcam tile, frame chrome,
  and cell borders.
- Invariants: preserve dataframe columns `0`, `1`, `2`; rows `(4, 1,
  0.761283)`, `(4, 2, 0.761283)`, `(4, 5, 0.761283)`, `(4, 10,
  0.761283)`, and `(4, 15, 0.763726)` exactly.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-03-grid-search-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  numeric dataframe content is fidelity-sensitive. The tighter second crop was
  accepted after rejecting a candidate with a clipped notebook border.
- QA: final `520x240` PNG inspected visually; all visible headers, indices, and
  values remain crisp, with no face, camera tile, browser/Zoom chrome, cursor,
  watermark, overlay, or border artifact. Markdown reference resolves and
  `git diff --check` passes before commit.

## 05 — decision tree parameter tuning, screenshot 04

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-04-pivot.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the pivot table
  and highlighted best AUC are exact numeric content, so imagegen was not used.
- Crop coordinates: source `598x360`; `350x235+125+75` (`x=125, y=75,
  width=350, height=235`). This focuses on the complete pivot table and blue
  highlight, removing the notebook chrome, presenter webcam tile, lower lesson
  heading, and recording frame.
- Invariants: preserve headers `max_depth`, `min_samples_leaf`, `auc`, depth
  columns `4`, `5`, `6`, all visible leaf-size rows `1`, `2`, `5`, `10`, `15`,
  `20`, `100`, `200`, `500`, every AUC value, and the highlighted `0.785695`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-04-pivot-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  changing a numeric pivot table would be unsafe. A tighter crop was accepted
  after removing the stray output-label fragment from the first candidate.
- QA: final `700x470` PNG inspected visually; the complete table and winner are
  crisp, with no face, camera tile, browser/Zoom chrome, cursor, watermark,
  overlay, or black bar. Markdown reference resolves and `git diff --check`
  passes before commit.

## 05 — decision tree parameter tuning, screenshot 05

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-05-heatmap.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the heatmap's
  exact AUC values, axes, and highlighted winner are source-of-truth content,
  so imagegen was not used.
- Crop coordinates: source `598x360`; `330x210+125+115` (`x=125, y=115,
  width=330, height=210`). This isolates the complete heatmap, legend, axes,
  and blue annotation while removing notebook output text, webcam, browser
  chrome, and frame borders.
- Invariants: preserve the `min_samples_leaf` rows, `auc-4`, `auc-5`, and
  `auc-6` columns, all annotated AUC values, the color scale `0.68`–`0.78`,
  and the highlighted `0.786` cell at leaf size `15`, depth `6`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-05-heatmap-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  numeric heatmap content must not be guessed. A candidate with clipped
  `AxesSubplot` text was rejected; the accepted crop begins below it.
- QA: final `660x420` PNG inspected visually; the complete heatmap and axes are
  crisp, with no face, camera tile, browser/Zoom chrome, cursor, watermark,
  output-text fragment, or black bar. Markdown reference resolves and
  `git diff --check` passes before commit.

## 05 — decision tree parameter tuning, screenshot 06

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-06-nan-warning.jpg`.
- Disposition: `crop/replace` via deterministic raster export; this is an exact
  sorted dataframe with a `NaN` value and validation AUCs, so imagegen was not
  used.
- Crop coordinates: source `598x360`; `360x140+85+90` (`x=85, y=90,
  width=360, height=140`). This isolates the full five-row sorted table and
  removes the notebook code cells, presenter webcam tile, browser chrome, and
  lower frame material.
- Invariants: preserve headers `max_depth`, `min_samples_leaf`, `auc`; rows
  `40/10.0/15/0.790439`, `67/NaN/15/0.788356`, `58/20.0/15/0.788074`,
  `41/10.0/20/0.786370`, and `49/15.0/15/0.785389` exactly.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-06-nan-warning-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  exact numeric output and `NaN` must not be guessed. A shorter crop was
  rejected because it clipped the fifth row; the accepted crop keeps the full
  table and only the notebook cell border at the lower edge.
- QA: final `720x280` PNG inspected visually; headers, `NaN`, row order, and
  values remain crisp, with no face, camera tile, browser/Zoom chrome, cursor,
  watermark, or black bar. Markdown reference resolves and `git diff --check`
  passes before commit.

## 05 — decision tree parameter tuning, screenshot 07

- Source: `cohorts/2026/06-trees/images/05-decision-tree-tuning-07-wider-search.jpg`.
- Disposition: `crop/replace` via deterministic raster export; this wider
  heatmap contains exact AUC values and axes, so imagegen was not used.
- Crop coordinates: source `598x360`; `360x210+115+125` (`x=115, y=125,
  width=360, height=210`). This isolates the complete heatmap, legend, axes,
  and blue annotations, removing the notebook code/output text, presenter
  webcam tile, browser chrome, and frame borders.
- Invariants: preserve the wider `None`, `4`, `5`, `6`, `7`, `10`, `15`, and
  `20` max-depth columns; leaf-size rows; every visible annotated AUC value;
  the `0.788`, `0.785`, `0.790`, and `0.788` highlights; and the color scale
  `0.66`–`0.78`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/05-decision-tree-tuning-07-wider-search-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  numeric heatmap content must not be guessed. Candidates with clipped
  `AxesSubplot` output were rejected; the accepted crop begins at the plot.
- QA: final `720x420` PNG inspected visually; all cells, axes, annotations, and
  legend remain crisp, with no face, camera tile, browser/Zoom chrome, cursor,
  watermark, output-text fragment, or black bar. Markdown reference resolves
  and `git diff --check` passes before commit.

## 06 — random forest, screenshot 01

- Source: `cohorts/2026/06-trees/images/06-random-forest-01-board-of-experts.jpg`.
- Disposition: `replace` via built-in imagegen; this is a bounded conceptual
  ensemble diagram, not an exact code, UI, plot, or numeric-result source.
- Crop coordinates: source `1024x724`; deterministic preparation crop
  `980x690+22+16` (`x=22, y=16, width=980, height=690`) removed only the
  outer board edge before generation.
- Invariants: preserve the top-to-bottom flow, arrows, `YES/NO`, `PROB OF
  DEFAULT`, the random-subset explanation, the five model outputs, the
  probabilities `0.6`, `0.7`, `0.3`, `0.7`, `0.65`, and the average formula
  `1/n Σ pᵢ`; no extra model or metric may be introduced.
- Path: imagegen skill was available and read completely; built-in imagegen
  edit used the inspected crop as the reference. Final sibling
  `cohorts/2026/06-trees/images/06-random-forest-01-board-of-experts-imagegen.png`;
  original JPG preserved.
- Prompt/iteration: one structured `scientific-educational` generation with
  exact labels, values, relationships, and negative constraints. The accepted
  result replaces handwriting with crisp vector-like geometry and uses simple
  non-human model icons rather than faces.
- QA: final `1496x1052` PNG inspected visually; all required labels, five
  probabilities, arrows, and average formula are readable. No face, camera
  tile, browser/Zoom chrome, cursor, watermark, or unrelated overlay remains.
  Markdown reference resolves and `git diff --check` passes before commit.

## 06 — random forest, screenshot 02

- Source: `cohorts/2026/06-trees/images/06-random-forest-02-random-forest.jpg`.
- Disposition: `replace` via built-in imagegen; this is a bounded conceptual
  feature-subset diagram where crisp relationships matter more than source
  pixels.
- Crop coordinates: source `768x576`; the full frame was used as the clean
  reference because it already contains no camera or recording overlay. The
  first `738x548+15+12` prep crop was rejected after clipping the rightmost
  `DT #3` content; the full-source reference restored the complete layout.
- Invariants: preserve top headers `ASSETS`, `DEBT`, `PRICE`; lower pairs
  `ASSETS/DEBT`, `ASSETS/PRICE`, `DEBT/PRICE`; arrows from each top feature
  column; labels `DT #1`, `DT #2`, `DT #3`; quoted `BOARD OF EXPERTS`; and
  the averaging formula `1/3 (p₁ + p₂ + p₃)`.
- Path: imagegen skill was available and read completely; built-in imagegen
  edit used the inspected full source. Final sibling
  `cohorts/2026/06-trees/images/06-random-forest-02-random-forest-imagegen.png`;
  original JPG preserved.
- Prompt/iteration: one structured `scientific-educational` generation with
  exact labels, feature-pair order, arrows, formula, and negative constraints.
  The accepted result uses crisp vector-like tables and typography without
  inventing columns or people.
- QA: final `1492x1052` PNG inspected visually; all tables, labels, arrows,
  and formula are complete and readable, with no face, camera tile,
  browser/Zoom chrome, cursor, watermark, or unrelated overlay. Markdown
  reference resolves and `git diff --check` passes before commit.

## 06 — random forest, screenshot 03

- Source: `cohorts/2026/06-trees/images/06-random-forest-03-auc-vs-trees.jpg`.
- Disposition: `crop/replace` via deterministic raster export; this exact AUC
  curve is numeric plot content and was not sent to imagegen.
- Crop coordinates: source `768x576`; `680x500+35+35` (`x=35, y=35,
  width=680, height=500`). This keeps the complete axes, tick labels, and
  curve while removing excess white screenshot margin.
- Invariants: preserve the plotted validation-AUC curve, its `0.78`–`0.82`
  y-axis scale, `25`–`200` estimator ticks, and the rapid-growth-then-
  stabilization shape exactly.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/06-random-forest-03-auc-vs-trees-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  plot geometry and values are fidelity-sensitive. A first crop cut the left
  y-axis labels; the wider accepted crop restores them.
- QA: final `1360x1000` PNG inspected visually; curve, axes, and tick labels are
  crisp, with no face, camera tile, browser/Zoom chrome, cursor, watermark, or
  overlay. Markdown reference resolves and `git diff --check` passes before
  commit.

## 06 — random forest, screenshot 04

- Source: `cohorts/2026/06-trees/images/06-random-forest-04-tuning-max-depth.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the three exact
  validation-AUC curves and legend values are plot source of truth, so imagegen
  was not used.
- Crop coordinates: source `768x576`; `680x520+35+10` (`x=35, y=10,
  width=680, height=520`). This keeps the full axes, curves, and legend while
  removing excess screenshot margin.
- Invariants: preserve the series labels `max_depth=5`, `max_depth=10`, and
  `max_depth=15`; their colors and curve ordering; the `0.790`–`0.825` y-axis
  scale; and the plotted validation-AUC relationships.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/06-random-forest-04-tuning-max-depth-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  plot values and curves must not be guessed. One crop was accepted after
  visual review.
- QA: final `1360x1040` PNG inspected visually; all curves, tick labels, and
  legend entries are crisp, with no face, camera tile, browser/Zoom chrome,
  cursor, watermark, or overlay. Markdown reference resolves and
  `git diff --check` passes before commit.

## 08 — XGBoost parameter tuning, screenshot 01

- Source: `cohorts/2026/06-trees/images/08-xgb-tuning-01-parameters.jpg`.
- Disposition: `replace` via built-in imagegen; this is a bounded conceptual
  parameter-and-sequential-boosting diagram, so generation is safe when all
  labels, stage order, and arrow relationships are explicitly locked.
- Crop coordinates: source `1024x724`; deterministic preparation crop
  `980x690+22+16` (`x=22, y=16, width=980, height=690`) removed only the
  outer board edge before generation.
- Invariants: preserve the exact title `6.8 XGBOOST PARAMETER TUNING`, the
  three numbered lines `ETA = LEARNING RATE = SIZE OF STEP`, `MAX_DEPTH`, and
  `MIN_CHILD_WEIGHT = MIN_SAMPLES_LEAF IN RF`; the stages `DATA`, `MODEL 1`,
  `PRED 1`, `ERRORS OF MODEL 1`, through `MODEL 4` and `PRED 4`; sequential
  error-feedback arrows; and the green annotation `0.3` beneath `PRED 2`.
- Path: imagegen skill was available and read completely; built-in imagegen
  edit used the inspected crop. Final sibling
  `cohorts/2026/06-trees/images/08-xgb-tuning-01-parameters-imagegen.png`;
  original JPG preserved.
- Prompt/iteration: one structured `scientific-educational` generation with
  exact labels, four-stage order, feedback arrows, and negative constraints.
  The accepted result removes handwriting texture and leaves a crisp,
  face-free diagram without UI or recording overlays.
- QA: final `1529x1029` PNG inspected visually; all parameter labels, model
  stages, predictions, error boxes, arrows, and the `0.3` annotation are
  complete and readable. No face, camera tile, browser/Zoom chrome, cursor,
  watermark, or unrelated overlay remains. Markdown reference resolves and
  `git diff --check` passes before commit.

## 08 — XGBoost parameter tuning, screenshot 02

- Source: `cohorts/2026/06-trees/images/08-xgb-tuning-02-tuning-eta.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the five exact
  validation-AUC curves, legend values, axes, and numeric ticks are fidelity-
  sensitive plot content, so imagegen was not used.
- Crop coordinates: source `768x576`; `680x500+35+35` (`x=35, y=35,
  width=680, height=500`). This keeps the complete plot, axes, legend, and
  x-axis labels while removing excess screenshot margin.
- Invariants: preserve legend entries `eta=0.3`, `eta=1.0`, `eta=0.1`,
  `eta=0.05`, and `eta=0.01`; their colors and curve geometry; the
  `0.800`–`0.840` y-axis scale; and the `0`–`200` boosting-round x-axis.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling
  `cohorts/2026/06-trees/images/08-xgb-tuning-02-tuning-eta-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  exact plot geometry and values must not be guessed. One crop was accepted
  after visual review.
- QA: final `1360x1000` PNG inspected visually; all five curves, axes, tick
  labels, and legend entries are crisp, with no face, camera tile,
  browser/Zoom chrome, cursor, watermark, or overlay. Markdown reference
  resolves and `git diff --check` passes before commit.

## 07 — gradient boosting and XGBoost, screenshot 01

- Source: `cohorts/2026/06-trees/images/07-boosting-01-boosting-vs-random-forest.jpg`.
- Disposition: `replace` via built-in imagegen; this is a bounded conceptual
  comparison diagram, so generation is safe when the workflows and labels are
  explicitly locked.
- Crop coordinates: source `1024x724`; deterministic preparation crop
  `980x690+22+16` (`x=22, y=16, width=980, height=690`) removed only the
  outer board edge before generation.
- Invariants: preserve the top RF parallel workflow with `DATA`, `DT 1`,
  `DT 2`, `DT 3`, `1/n Σ pᵢ`, `PREDICTION`; the bottom boosting sequential
  workflow with `ERRORS OF MODEL 1/2/3`, `MODEL 1/2/3/4`, `PRED 1/2/3/4`;
  labels `RF`, `PARALLEL`, `BOOSTING`, `SEQUENTIAL`; and `FINAL PREDICTION`.
- Path: imagegen skill was available and read completely; built-in imagegen
  edit used the inspected crop. Final sibling
  `cohorts/2026/06-trees/images/07-boosting-01-boosting-vs-random-forest-imagegen.png`;
  original JPG preserved.
- Prompt/iteration: one structured `scientific-educational` generation with
  exact labels, arrow directions, average formula, stage count, and negative
  constraints. The accepted result removes handwriting texture and uses crisp
  boxed workflows without people or UI overlays.
- QA: final `1494x1054` PNG inspected visually; parallel versus sequential
  relationships, all stages, formula, and labels are complete and readable.
  No face, camera tile, browser/Zoom chrome, cursor, watermark, or unrelated
  overlay remains. Markdown reference resolves and `git diff --check` passes
  before commit.

## 07 — gradient boosting and XGBoost, screenshot 02

- Source: `cohorts/2026/06-trees/images/07-boosting-02-gradient-boosting-trees.jpg`.
- Disposition: `replace` via built-in imagegen; this is a bounded conceptual
  four-stage error-correction diagram.
- Crop coordinates: source `1024x724`; deterministic preparation crop
  `980x690+22+16` (`x=22, y=16, width=980, height=690`) removed only the
  outer board edge before generation.
- Invariants: preserve title `GRADIENT BOOSTING TREES / XGBOOST`; stage order
  `DATA`, `TREE 1`, `PRED 1`, `ERRORS OF MODEL 1`, `TREE 2`, `PRED 2`,
  `ERRORS OF MODEL 2`, `TREE 3`, `PRED 3`, `ERRORS OF MODEL 3`, `TREE 4`,
  `PRED 4`; every arrow direction; and `FINAL PREDICTION`.
- Path: imagegen skill was available and read completely; built-in imagegen
  edit used the inspected crop. Final sibling
  `cohorts/2026/06-trees/images/07-boosting-02-gradient-boosting-trees-imagegen.png`;
  original JPG preserved.
- Prompt/iteration: one structured `scientific-educational` generation with
  exact labels, four-stage order, curved error-feedback arrows, and negative
  constraints. The accepted result removes handwriting texture and leaves a
  crisp, face-free diagram.
- QA: final `1496x1051` PNG inspected visually; all stages, labels, arrows,
  and the final connector are complete and readable. No face, camera tile,
  browser/Zoom chrome, cursor, watermark, or unrelated overlay remains.
  Markdown reference resolves and `git diff --check` passes before commit.

## 07 — gradient boosting and XGBoost, screenshot 03

- Source: `cohorts/2026/06-trees/images/07-boosting-03-train-val-auc.jpg`.
- Disposition: `crop/replace` via deterministic raster export; train/validation
  AUC curves and their numeric axes are exact plot content, so imagegen was not
  used.
- Crop coordinates: source `768x576`; `680x500+35+35` (`x=35, y=35,
  width=680, height=500`). This keeps the complete plot, axes, and legend while
  removing excess white screenshot margin.
- Invariants: preserve `train` and `val` series, their colors and curve
  geometry, the `0.80`–`1.00` y-axis scale, and the `0`–`200` boosting-round
  x-axis ticks exactly.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/07-boosting-03-train-val-auc-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  plot values and curves must not be guessed. One crop was accepted after
  visual review.
- QA: final `1360x1000` PNG inspected visually; both curves, axes, tick labels,
  and legend are crisp, with no face, camera tile, browser/Zoom chrome, cursor,
  watermark, or overlay. Markdown reference resolves and `git diff --check`
  passes before commit.

## 06 — random forest, screenshot 05

- Source: `cohorts/2026/06-trees/images/06-random-forest-05-tuning-min-samples-leaf.jpg`.
- Disposition: `crop/replace` via deterministic raster export; the five exact
  validation-AUC curves and legend values are plot source of truth, so imagegen
  was not used.
- Crop coordinates: source `768x576`; `680x520+35+10` (`x=35, y=10,
  width=680, height=520`). This keeps the full axes, curves, and legend while
  removing excess screenshot margin.
- Invariants: preserve legend labels `min_samples_leaf=1`, `3`, `5`, `10`,
  `50`; their colors and curve ordering; the `0.790`–`0.825` y-axis scale;
  and every plotted relationship.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp
  masking; final sibling `cohorts/2026/06-trees/images/06-random-forest-05-tuning-min-samples-leaf-cropped.png`;
  original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely, but
  plot geometry and values must not be guessed. One crop was accepted after
  visual review.
- QA: final `1360x1040` PNG inspected visually; all curves, tick labels, and
  legend entries are crisp, with no face, camera tile, browser/Zoom chrome,
  cursor, watermark, or overlay. Markdown reference resolves and
  `git diff --check` passes before commit.
