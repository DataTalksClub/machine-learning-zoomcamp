# ML Zoomcamp intro screenshot rollout

This report records every screenshot in the three assigned lessons. Originals
remain in place; accepted replacements are sibling assets.

## 02-ml-vs-rules

### 02-ml-vs-rules-01-spam-examples.jpg

- Disposition: `imagegen`; the two example email cards directly support the
  spam-detection setup.
- Invariant: title `Spam`; two overlapping cards; `Get 50% off now` from
  `promotions@online.com`; `URGENT: tax review` from `tax@online.com`; the
  tax-review warning, URL, and `Tax office.` remain readable.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-01-spam-examples-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; exact headers, URL,
  warning, and two-card relationship checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

## 04-crisp-dm

### 04-crisp-dm-01-ml-projects.jpg

- Disposition: `imagegen`; this introductory four-step list is a bounded
  conceptual slide.
- Invariant: title `ML Projects`; bullets in order: `Understand the problem`,
  `Collect the data`, `Train the model`, `Use it`.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `04-crisp-dm-01-ml-projects-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; title and all four
  bullets/order checked; face, webcam, browser/Zoom chrome, cursor, watermark,
  toolbar, and recording overlays absent.

### 04-crisp-dm-02-process-diagram.jpg

- Disposition: `imagegen`; this is a bounded process/architecture diagram.
- Invariant: title `CRISP-DM`; central `Data`; exact six stages and order:
  `Business Understanding`, `Data Understanding`, `Data Preparation`,
  `Modeling`, `Evaluation`, `Deployment`; circular and feedback arrows remain.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `04-crisp-dm-02-process-diagram-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all six labels, stage
  relationships, data cylinder, circular iteration, and feedback arrows
  checked; face, webcam, browser/Zoom chrome, cursor, watermark, toolbar, and
  recording overlays absent.

### 04-crisp-dm-03-business-understanding.jpg

- Disposition: `imagegen`; this is a process-stage highlight with bounded
  labels and explanatory text.
- Invariant: exact text `Identify the business problem, understand how we can
  solve it`; `Business Understanding` is highlighted within the same six-stage
  CRISP-DM loop and central `Data` remains visible.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `04-crisp-dm-03-business-understanding-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; explanatory text,
  highlighted stage, six-stage loop, arrows, and Data label checked; face,
  webcam, browser/Zoom chrome, cursor, watermark, toolbar, and recording
  overlays absent.

### 03-supervised-ml-06-ranking.jpg

- Disposition: `imagegen`; the original ecommerce strip is illustrative, not
  an exact UI source of truth, and the concept is scored/ranked items.
- Invariant: title `Ranking`; product recommendations are ordered along an
  explicit score axis; axis direction is exactly `0` on the left to `1` on
  the right; higher score means more relevant.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `03-supervised-ml-06-ranking-imagegen-pilot.png`.
- Validation: first generation rejected because it reversed the score axis;
  second generation inspected at lesson size and passed with `0 → 1`.
  Face, webcam, browser/Zoom chrome, cursor, watermark, toolbar, and
  recording overlays are absent.

### 03-supervised-ml-07-summary.jpg

- Disposition: `imagegen`; the source is a conceptual handwritten summary,
  not an exact code, plot, or UI asset.
- Invariant: exact formula `g(X) ≈ y`; y branches to `number`/regression,
  `category`/classification, and `ranking`/ranking-recommenders.
- Crop: `550x300+20+30`, with the camera area masked, from the 598x360
  source.
- Output: `03-supervised-ml-07-summary-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; formula, three output
  types, and branch relationships checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-07-rule-based-summary.jpg

- Disposition: `imagegen`; this bounded diagram summarizes how data and code
  feed ordinary software to produce an outcome.
- Invariant: `DATA` and `CODE` arrows enter `SOFTWARE`; one arrow exits to
  `OUTCOME`; directions and central box relationship are unchanged.
- Crop: `598x300+0+30`, with the camera area masked, from the 598x360
  source.
- Output: `02-ml-vs-rules-07-rule-based-summary-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; labels, arrows, and
  relationship checked; face, webcam, browser/Zoom chrome, cursor, watermark,
  toolbar, black bars, and recording overlays absent.

### 02-ml-vs-rules-08-ml-summary.jpg

- Disposition: `imagegen`; this diagram summarizes the learned-model flow.
- Invariant: `DATA` and `OUTCOME`/`SPAM / NOT` enter `ML`; `ML` points to
  `MODEL`; the bottom statement is `DATA + MODEL => OUTCOME`.
- Crop: `598x300+0+30`, with the camera area masked, from the 598x360
  source.
- Output: `02-ml-vs-rules-08-ml-summary-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; labels, arrows, and
  bottom relationship checked; face, webcam, browser/Zoom chrome, cursor,
  watermark, toolbar, black bars, and recording overlays absent.

## 03-supervised-ml

### 03-supervised-ml-01-features-target.jpg

- Disposition: `imagegen`; the side-by-side feature matrix and target vector
  establish the formal supervised-learning inputs.
- Invariant: headers `Features (data)` and `Target (desired output)`; six
  rows with exactly six feature values each; target sequence `1, 0, 1, 1,
  0, 0`.
- Crop: `475x300+50+30`, with the camera sliver masked, from the 598x360
  source. The first generation was rejected because it omitted the sixth
  feature column; the second generation passed.
- Output: `03-supervised-ml-01-features-target-imagegen-pilot.png`.
- Validation: final image inspected at lesson size; all 36 feature values,
  six target values, headers, and row alignment checked; no face, webcam,
  browser/Zoom chrome, cursor, watermark, annotations, toolbar, or recording
  overlays remain.

### 03-supervised-ml-02-feature-matrix.jpg

- Disposition: `imagegen`; the original annotations explain rows, columns,
  X, and y, so this is a bounded educational diagram.
- Invariant: six rows and six feature columns with the same binary values as
  the preceding table; one target per row; rows are observations, columns
  are features, matrix is `X`, target vector is `y`.
- Crop: `475x300+50+30`, with the camera sliver masked, from the 598x360
  source.
- Output: `03-supervised-ml-02-feature-matrix-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all 36 feature
  values, six targets, row/column labels, X/y labels, and arrows checked;
  face, webcam, browser/Zoom chrome, cursor, watermark, annotations,
  toolbar, and recording overlays absent.

### 03-supervised-ml-03-predictions.jpg

- Disposition: `imagegen`; the table directly illustrates one prediction per
  feature row.
- Invariant: six six-value feature rows and exact probabilities `0.93`,
  `0.48`, `0.19`, `0.32`, `0.01`, `0.94` in the original order; headers
  `Features (data)` and `Predictions (output)`.
- Crop: `475x300+50+30`, with the camera sliver masked, from the 598x360
  source.
- Output: `03-supervised-ml-03-predictions-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all 36 feature values,
  six probabilities, row order, and headers checked; face, webcam,
  browser/Zoom chrome, cursor, watermark, annotation, toolbar, and recording
  overlays absent.

### 03-supervised-ml-04-regression.jpg

- Disposition: `imagegen`; this bounded car-to-price example communicates
  numeric regression directly.
- Invariant: `Supervised Machine Learning`, `Regression:`, one car input,
  right-pointing arrow, and exact numeric output `$50k`.
- Crop: `550x300+20+30`, with the camera area masked, from the 598x360
  source.
- Output: `03-supervised-ml-04-regression-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; label, input/output
  relationship, arrow direction, and `$50k` checked; face, webcam,
  browser/Zoom chrome, cursor, watermark, toolbar, and recording overlays
  absent.

### 03-supervised-ml-05-multiclass.jpg

- Disposition: `imagegen`; this is a bounded input-to-category illustration.
- Invariant: heading `Classification`, panel label `Multiclass:`, one image
  input, right-pointing arrow, and exactly the ordered categories `cat`,
  `dog`, `car`.
- Crop: `550x300+20+30`, with the camera area masked, from the 598x360
  source.
- Output: `03-supervised-ml-05-multiclass-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; heading, label,
  arrow, input, and category order checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-06-predictions.jpg

- Disposition: `imagegen`; the model-to-probability mapping is central to the
  threshold explanation.
- Invariant: `MODEL` arrow into the feature matrix; six rows in order; exact
  predictions `0.8`, `0.6`, `0.1`, `0.01`, `0.7`, `0.4`; headings for
  features, predictions, and final outcome; no invented decision values.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-06-predictions-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; every matrix row,
  probability, heading, and arrow checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-03-more-spam.jpg

- Disposition: `imagegen`; the prize/deposit email is the concrete example
  that motivates adding a new spam rule.
- Invariant: title `More`; one bordered email; `Waiting for your reply`,
  `prince1@test.com`, the 1.000.000-dollar claim, `$10`,
  `prince@test.com`, transfer message, and `Congratulations again!` remain
  readable.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-03-more-spam-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; exact amount, dollar
  fee, email addresses, and single-card relationship checked; face, webcam,
  browser/Zoom chrome, cursor, watermark, toolbar, and recording overlays
  absent.

### 02-ml-vs-rules-04-features.jpg

- Disposition: `imagegen`; the feature list makes the transition from rules
  to numerical ML inputs concrete.
- Invariant: title `Features`; six bullets in source order, including both
  sender addresses, `test.com`, and `deposit`; the `Rules` cue remains on the
  right.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-04-features-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all six labels and
  the `Rules` cue checked verbatim; face, webcam, browser/Zoom chrome,
  cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-05-encode-email.jpg

- Disposition: `imagegen`; the email-to-vector mapping is the lesson's key
  feature-encoding example.
- Invariant: email content and `SPAM` badge; `Sender
  promotions@online.com? False`; exact vector `[1, 1, 0, 0, 1, 1]`; arrow
  from the sender feature to the vector.
- Crop: `505x300+0+30` from the 598x360 source.
- Output: `02-ml-vs-rules-05-encode-email-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; email labels, vector
  values/order, badge, and mapping checked; face, webcam, browser/Zoom
  chrome, cursor, watermark, toolbar, and recording overlays absent.

### 02-ml-vs-rules-02-rules.jpg

- Disposition: `imagegen`; the three hard-coded rules are the lesson's
  contrast with learned rules.
- Invariant: title `Rules`; exact three bullet rules and their order, including
  `promotions@online.com`, `tax review`, `online.com`, `spam`, and
  `good email`.
- Crop: `480x280+20+30` from the 598x360 source.
- Output: `02-ml-vs-rules-02-rules-imagegen-pilot.png`.
- Validation: imagegen output inspected at lesson size; all three bullets and
  order checked verbatim; face, webcam, browser/Zoom chrome, cursor,
  watermark, toolbar, and recording overlays absent.
