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
