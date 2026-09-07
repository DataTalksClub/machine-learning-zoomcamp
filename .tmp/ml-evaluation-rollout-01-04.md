# Evaluation overview screenshot rollout

## 01 — title slide

- Source: `cohorts/2026/04-evaluation/images/01-overview-01-title.jpg`
- Disposition: accepted deterministic crop; exact handwritten title retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=478, height=360` from the 598×360 source; removes both black side bars and the upper-right webcam tile.
- Invariants: `ML ZOOMCAMP`, `EVALUATION METRICS`, `FOR`, `CLASSIFICATION`, and `DATA TALKS.CLUB` remain unchanged and in the original layout.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-01-title-cropped.jpg`
- QA: accepted after visual inspection; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `478×360` output renders cleanly.

## 03 — metric definition notebook

- Source: `cohorts/2026/04-evaluation/images/01-overview-03-metric-definition.jpg`
- Disposition: accepted deterministic crop; exact notebook text, URLs, and code retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: the `4.1 Evaluation metrics: session overview` heading, both source links, the metric definition sentence, and the visible `pandas`, `numpy`, `matplotlib`, `train_test_split`, `DictVectorizer`, `LogisticRegression`, and `pd.read_csv('data-week-3.csv')` code remain unchanged.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-03-metric-definition-cropped.jpg`
- QA: accepted after visual inspection; exact text and code are legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 04 — load and split notebook

- Source: `cohorts/2026/04-evaluation/images/01-overview-04-load-split.jpg`
- Disposition: accepted deterministic crop; exact data-cleaning and train/validation/test split code retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: the visible `pd.read_csv('data-week-3.csv')`, lowercase/underscore normalization, categorical-column loop, `totalcharges` numeric coercion with `errors='coerce'`, `fillna(0)`, binary churn conversion, and `train_test_split` calls with `test_size=0.2`, `test_size=0.25`, and `random_state=1` remain unchanged.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-04-load-split-cropped.jpg`
- QA: accepted after visual inspection; exact code remains legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 05 — feature lists notebook

- Source: `cohorts/2026/04-evaluation/images/01-overview-05-features.jpg`
- Disposition: accepted deterministic crop; exact feature names and notebook output retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: the target-value cleanup lines remain visible, and the feature definitions preserve `numerical = ['tenure', 'monthlycharges', 'totalcharges']` plus the visible categorical order beginning with `gender`, `seniorcitizen`, `partner`, `dependents`, `phoneservice`, `multiplelines`, `internetservice`, `onlinesecurity`, `onlinebackup`, `deviceprotection`, and `techsupport`.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-05-features-cropped.jpg`
- QA: accepted after visual inspection; exact labels and ordering remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 06 — predictions and accuracy notebook

- Source: `cohorts/2026/04-evaluation/images/01-overview-06-predictions-accuracy.jpg`
- Disposition: accepted deterministic crop; exact prediction code and evaluation result retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: `DictVectorizer(sparse=False)`, the training transform, `LogisticRegression`, `predict_proba(X_val)[:, 1]`, threshold `0.5`, the agreement calculation, exact result `0.8034066713981547`, and the `4.2 Accuracy and dummy model` heading remain unchanged.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-06-predictions-accuracy-cropped.jpg`
- QA: accepted after visual inspection; the exact numeric result and code remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 07 — module outline notebook

- Source: `cohorts/2026/04-evaluation/images/01-overview-07-module-outline.jpg`
- Disposition: accepted deterministic crop plus a bounded background patch; exact notebook headings, bullets, and result retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar. Post-crop cursor cleanup: white rectangle `x=144..156, y=216..230` in the cropped image, limited to blank page background.
- Invariants: `0.8034066713981547`, `4.2 Accuracy and dummy model`, its two bullets, `4.3 Confusion table`, its two bullets, and `4.4 Precision and Recall` remain unchanged and in the original order.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-07-module-outline-cropped.jpg`
- QA: accepted after visual inspection; exact headings, bullets, and result remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 02 — churn prediction scenario

- Source: `cohorts/2026/04-evaluation/images/01-overview-02-churn-scenario.jpg`
- Disposition: accepted deterministic crop; exact whiteboard illustration and numeric labels retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=478, height=360` from the 598×360 source; removes both black side bars and the upper-right webcam tile.
- Invariants: `CHURN PREDICTION`, `TELCO`, the promo-mail arrow, `25%`, customer scores `0.2`, `0.3`, `0.35`, `0.40`, `0.45`, `0.85`, the highlighted customer, and `ACCURACY 80%` remain unchanged with the original relationships.
- Final path: `cohorts/2026/04-evaluation/images/01-overview-02-churn-scenario-cropped.jpg`
- QA: accepted after visual inspection; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `478×360` output renders cleanly.
