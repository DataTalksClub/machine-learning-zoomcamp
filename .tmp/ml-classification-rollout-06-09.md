# Classification screenshot rollout: lessons 06–09

Scope: every Markdown image reference in `06-mutual-info.md`,
`07-correlation.md`, `08-ohe.md`, and `09-logistic-regression.md`.

Worker capability: `imagegen` skill available; built-in imagegen used only
for the bounded conceptual mutual-information illustration. Exact code,
numeric output, plots, formulas, and teaching diagrams use deterministic
crops. Original sources remain unchanged. Each accepted screenshot gets its
own focused commit; crops and rejected/intermediate files stay under `.tmp/`.

## Accepted assets

### 06-mutual-info.md

- `06-mutual-info-01-mutual-information-wikipedia.jpg` →
  `06-mutual-info-01-mutual-information-wikipedia-imagegen-pilot.png`
  - Disposition: imagegen conceptual replacement.
  - Prep: reference crop `.tmp/ml-classification-rollout-06-09-crops/06-mutual-info-01-reference.png`, coordinates `505x300+0+42`.
  - Invariants: clean overlap diagram; exact labels `X`, `Y`, and `Mutual information`; no people, camera, browser, or extra metrics.

### 07-correlation.md

- `07-correlation-01-correlation-coefficient.jpg` →
  `07-correlation-01-correlation-coefficient-imagegen-pilot.png`
  - Disposition: imagegen bounded explanatory replacement.
  - Prep: inspected/cropped source reference `.tmp/ml-classification-rollout-06-09-crops/07-correlation-01-correlation-coefficient-cropped.png`.
  - Invariants: `-1 ≤ r ≤ 1`; negative/positive direction; LOW `0–0.2`, MEDIUM `0.2–0.5`, and STRONG `0.5–1.0` ranges; no people, camera, browser, or extra metrics.

- `07-correlation-02-binary-target.jpg` →
  `07-correlation-02-binary-target-imagegen-pilot.png`
  - Disposition: imagegen bounded explanatory replacement.
  - Prep: inspected/cropped source reference `.tmp/ml-classification-rollout-06-09-crops/07-correlation-02-binary-target-cropped.png`.
  - Invariants: `x = tenure`, `y = churn`, `y ∈ {0, 1}`, `x ∈ ℝ`; positive means more tenure → higher churn and negative means more tenure → less churn; no people, camera, browser, or extra metrics.

- `07-correlation-03-corrwith-churn.jpg` →
  `07-correlation-03-corrwith-churn-cropped.png`
  - Disposition: deterministic crop; exact code and output retained.
  - Crop: `480x105+25+50`; removes notebook/recording chrome and camera tile.
  - Invariants: `corrwith` call and exact values `-0.351885`, `0.196805`, and `-0.196353` checked against the lesson.

- `07-correlation-04-churn-rate-tenure.jpg` →
  `07-correlation-04-churn-rate-tenure-clean.png`
  - Disposition: deterministic vector redraw; source control wheel overlapped the right edge, so a crop would damage the visual.
  - Invariants: tenure groups `0–2`, `2–12`, `12+`; exact churn rates `60%`, `40%`, `17%`; decreasing relationship preserved; no camera or recording chrome.

- `07-correlation-05-churn-rate-monthly-charges.jpg` →
  `07-correlation-05-churn-rate-monthly-charges-clean.png`
  - Disposition: deterministic vector redraw; source control wheel overlapped the right edge and clipped the monthly-charge labels.
  - Invariants: monthly-charge groups `≤20`, `20–50`, `>50`; exact churn rates `8%`, `18%`, `32%`; positive relationship preserved. The reference tenure panel is retained for context; no camera or recording chrome.

### 08-ohe.md

- `08-ohe-01-one-hot-table.jpg` →
  `08-ohe-01-one-hot-table-cropped.png`
  - Disposition: deterministic crop; exact hand-drawn category table and binary values retained.
  - Crop: `450x340+28+0`; removes camera/control edges while retaining the full table and row examples.
  - Invariants: gender/contract columns, row order, and every 0/1 entry checked visually; no face or recording chrome.

- `08-ohe-02-to-dict-records.jpg` →
  `08-ohe-02-to-dict-records-cropped.png`
  - Disposition: deterministic crop; exact `to_dict(orient='records')` output retained.
  - Crop: `480x175+25+70`; removes notebook chrome, the camera tile, and the following lesson heading.
  - Invariants: dictionary keys, row order, and displayed values checked against the source; the long input line remains source-edge truncated after `records` because the original frame clipped it at the camera boundary.

- `08-ohe-03-dictvectorizer-fit.jpg` →
  `08-ohe-03-dictvectorizer-fit-cropped.png`
  - Disposition: deterministic crop; exact DictVectorizer calls and shape `(4225, 45)` retained.
  - Crop: `480x225+25+35`; removes notebook/recording chrome and camera tile.
  - Invariants: import, fit/transform sequence, and displayed shape checked; long source lines remain clipped at the original frame edge rather than being guessed or regenerated.

- `08-ohe-04-feature-names.jpg` →
  `08-ohe-04-feature-names-cropped.png`
  - Disposition: deterministic crop; exact feature-name output retained.
  - Crop: `480x325+25+35`; removes notebook/recording chrome and camera tile.
  - Invariants: `get_feature_names()` call and visible ordered names checked; the list remains truncated at the original bottom edge, as in the source frame.

- `08-ohe-05-validation-transform.jpg` →
  `08-ohe-05-validation-transform-cropped.png`
  - Disposition: deterministic crop; exact validation `transform` sequence retained.
  - Crop: `480x225+25+35`; removes notebook/recording chrome and camera tile.
  - Invariants: fitted training vectorizer is reused for `val_dict` and `X_val`; no second fit is introduced. Long source lines remain clipped at the original frame edge.

### 09-logistic-regression.md

- `09-logistic-regression-01-binary-classification.jpg` →
  `09-logistic-regression-01-binary-classification-clean.png`
  - Disposition: deterministic vector redraw; exact binary-class labels and probability mapping retained.
  - Invariants: `y_i ∈ {0, 1}`, 0 = no churn/no spam, 1 = churn/spam, and `g(x_i) → 0–1` as probability of the positive class; no face or recording chrome.

- `09-logistic-regression-02-from-linear-to-logistic.jpg` →
  `09-logistic-regression-02-from-linear-to-logistic-clean.png`
  - Disposition: deterministic vector redraw; mathematical notation is kept exact rather than generated.
  - Invariants: `g(x_i) = Sigmoid(w_0 + w_1 x_1 + ... + w_n x_n)`; the real-valued weighted sum passes through sigmoid to `g(x_i) ∈ [0, 1]`; no face or recording chrome.
