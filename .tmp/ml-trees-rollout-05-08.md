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
