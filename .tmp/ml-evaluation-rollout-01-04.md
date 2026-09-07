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

## 01 — accuracy versus threshold plot

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-01-accuracy-vs-threshold.jpg`
- Disposition: accepted deterministic re-export; the exact plot is already a clean frame, so no crop or imagegen was needed.
- Crop coordinates: `x=0, y=0, width=372, height=248` (full frame) from the 372×248 source; no recording frame, browser/Zoom chrome, face, camera tile, cursor, watermark, overlay, or black bar is present.
- Invariants: the blue accuracy curve, its rise from about `0.27` at threshold `0.0` to a peak around `0.80` near `0.5`, its decline to about `0.73`, and the visible x-axis ticks `0.0`, `0.2`, `0.4`, `0.6`, `0.8`, `1.0` plus y-axis ticks `0.3` through `0.8` remain unchanged.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-01-accuracy-vs-threshold-cropped.jpg`
- QA: accepted after visual inspection; the exact curve and axes remain crisp and readable at lesson size, with no non-teaching overlays; `372×248` output renders cleanly.

## 02 — toy accuracy example

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-02-accuracy-example.jpg`
- Disposition: accepted deterministic crop; the exact whiteboard teaching example is retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=451, height=340` from the 598×360 source; removes the black side bars, upper-right webcam tile, circular recording overlay, and bottom-left recording controls, while trimming only blank whiteboard margin at the bottom.
- Invariants: the handwritten `4.2 ACCURACY` title, six customer figures with their green checks/red crosses and probability annotations, the red/blue grouping, threshold note `>0.5`, and `3/6 = 50%` remain unchanged with the original relationships.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-02-accuracy-example-cropped.jpg`
- QA: accepted after visual inspection; all instructional handwriting, figures, threshold marking, and accuracy calculation remain legible; no face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, or black bar remains; `451×340` output renders cleanly.

## 03 — accuracy notebook result

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-03-accuracy-notebook.jpg`
- Disposition: accepted deterministic crop; exact notebook code and outputs are retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: the `4.2 Accuracy and dummy model` heading and bullets, `len(y_val)` with output `1409`, `(y_val == churn_decision).sum()` with output `1132`, `1132 / 1409`, and exact accuracy output `0.8034066713981547` remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-03-accuracy-notebook-cropped.jpg`
- QA: accepted after visual inspection; exact code, outputs, heading, and bullets remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 04 — threshold accuracy scores notebook

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-04-accuracy-score.jpg`
- Disposition: accepted deterministic crop; exact threshold-loop code and numeric output are retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: the visible `scores = []` initialization, threshold loop, `churn_decision = (y_pred >= t)`, `score = (y_val == churn_decision).mean()`, `scores.append(score)`, the plotting call beginning with `plt.plot(thresholds, ...)`, and the displayed scores array including the peak `0.8034066713981547` remain unchanged.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-04-accuracy-score-cropped.jpg`
- QA: accepted after visual inspection; exact code and numeric output remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 05 — dummy-model counter notebook

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-05-dummy-counter.jpg`
- Disposition: accepted deterministic tight crop; exact `Counter` code and output are retained, so imagegen was not used.
- Crop coordinates: `x=0, y=155, width=577, height=195` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, right black bar, preceding plot fragment, and blank lower frame margin.
- Invariants: `from collections import Counter`, `Counter(y_pred >= 1.0)`, exact output `Counter({False: 1409})`, and the `4.3 Confusion table` heading with both bullets remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-05-dummy-counter-cropped.jpg`
- QA: accepted after visual inspection; exact code, result, heading, and bullets remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×195` output renders cleanly.

## 06 — dummy-model accuracy notebook

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-06-dummy-accuracy.jpg`
- Disposition: accepted deterministic crop with a bounded background patch; exact notebook code and numeric result are retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar. Post-crop cursor cleanup: white rectangle `x=105..119, y=162..181`, limited to blank page background left of the `4.3 Confusion table` bullets.
- Invariants: `Counter(y_pred >= 1.0)` with `Counter({False: 1409})`, `1 - y_val.mean()`, exact output `0.7260468417317246`, the `4.3 Confusion table` heading and bullets, and the `4.4 Precision and Recall` heading remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-06-dummy-accuracy-cropped.jpg`
- QA: accepted after visual inspection; exact code, outputs, headings, and bullets remain legible; the cursor is absent; no face, camera tile, browser/Zoom chrome, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 07 — threshold endpoint annotations

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-07-thresholds-endpoints.jpg`
- Disposition: accepted deterministic crop; exact notebook plot, output, and hand-drawn teaching annotations are retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black bar.
- Invariants: `plt.plot(thresholds, scores)`, the visible `Line2D` output, the accuracy curve and axes, the blue hand-drawn circles at the threshold `0` and `1` endpoints, the blue vertical marker at `1`, and the `4.3 Confusion table` heading remain unchanged. The hand-drawn marks are instructional content and were preserved.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-07-thresholds-endpoints-cropped.jpg`
- QA: accepted after visual inspection; the curve, endpoint marks, axes, exact code, and output remain legible; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains; `577×292` output renders cleanly.

## 08 — class-imbalance whiteboard

- Source: `cohorts/2026/04-evaluation/images/02-accuracy-08-class-imbalance.jpg`
- Disposition: accepted deterministic crop; the exact whiteboard class-imbalance illustration and numeric annotations are retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=451, height=340` from the 598×360 source; removes the black side bars, upper-right webcam tile, circular recording overlay, and blank lower frame margin.
- Invariants: `YOUR MODEL`, `DUMMY MODEL`, `80%`, `73%`, `7%`, the `PRED` and `ACTUAL` rows with their F/T markings, the red/green row boxes, the `27%` arrow annotation, and boxed `73%` remain unchanged with their original relationships.
- Final path: `cohorts/2026/04-evaluation/images/02-accuracy-08-class-imbalance-cropped.jpg`
- QA: accepted after visual inspection; all instructional handwriting, percentages, row labels, markers, arrows, and box remain legible; no face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, or black bar remains; `451×340` output renders cleanly.

## 01 — confusion-table four outcomes

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-01-four-outcomes.jpg`
- Disposition: accepted deterministic crop plus bounded blank-board cleanup; exact handwritten outcome labels and relationships retained, so imagegen was not used.
- Crop coordinates: `x=31, y=0, width=518, height=360` from the 598×360 source; removes the left/right black bars and keeps the full four-outcome board. Post-crop cleanup fills only blank board space: `x=474..517, y=0..53` for the webcam tile, `x=466..517, y=75..204` for the partial recording-wheel overlay, and `x=326..339, y=55..72` for the cursor, all with the sampled pale board background `srgb(246,246,220)`.
- Invariants: `4.3 CONFUSION TABLE`, `g(x_i)`, the `< t`/`≥ t` branches, `NEGATIVE`, `POSITIVE`, `NO CHURN`, `CHURN`, the four customer boxes, and `TRUE NEGATIVE`, `FALSE NEGATIVE`, `FALSE POSITIVE`, and `TRUE POSITIVE` remain unchanged and in their original relationships.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-01-four-outcomes-cropped.jpg`
- QA: accepted after `view_image` inspection; all exact handwritten labels, arrows, boxes, and the green mail icon remain legible; no face, camera tile, recording overlay, cursor, watermark, browser/Zoom chrome, or black bar remains; `518×360` output renders cleanly.

## 02 — prediction conditions notebook

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-02-prediction-conditions.jpg`
- Disposition: accepted deterministic crop; exact notebook code, threshold, array values, and teaching annotation retained, so imagegen was not used.
- Crop coordinates: `x=0, y=54, width=577, height=306` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black strip with no post-crop content edits.
- Invariants: `actual_positive = (y_val == 1)`, `actual_negative = (y_val == 0)`, `t = 0.5`, `predict_positive = (y_pred >= t)`, `predict_negative = (y_pred < t)`, both sample arrays, the handwritten `TRUE`/`FALSE` grouping, and the final `predict_positive & actual_positive` output remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-02-prediction-conditions-cropped.jpg`
- QA: accepted after `view_image` inspection; exact code, values, and annotation remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black strip remains; `577×306` output renders cleanly.

## 03 — element-wise AND notebook

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-03-and-operator.jpg`
- Disposition: accepted deterministic crop plus bounded blank-cell cursor cleanup; exact AND expressions and visible output retained, so imagegen was not used.
- Crop coordinates: `x=0, y=54, width=577, height=306` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black strip. Post-crop cleanup fills only blank notebook-cell space with `srgb(254,254,254)`: `x=149..160, y=183..199`, `x=143..152, y=220..243`, and `x=150..162, y=216..236` remove the I-beam/text caret artifacts without touching code glyphs.
- Invariants: the actual-positive/actual-negative definitions, threshold `t = 0.5`, `predict_positive`/`predict_negative`, `tp = (predict_positive & actual_positive).sum()`, `tn = (predict_negative & actual_negative).sum()`, the visible `fp`/`fn` cell, output `922`, and the `4.4 Precision and Recall` heading remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-03-and-operator-cropped.jpg`
- QA: accepted after `view_image` inspection; exact code, ampersands, output, and cell structure remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black strip remains; `577×306` output renders cleanly.

## 04 — confusion counts whiteboard

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-04-confusion-counts.jpg`
- Disposition: accepted deterministic crop plus bounded blank-board cleanup; exact handwritten counts, regions, labels, and conditions retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=522, height=340` from the 598×360 source; removes the left/right black frame bars and bottom-left recording controls. Post-crop cleanup fills only blank board space with `srgb(246,246,220)`: `x=0..76, y=0..101` removes the partial recording wheel, `x=478..521, y=0..54` removes the webcam tile, `x=390..403, y=288..305` removes the cursor, and `x=0..3, y=102..339` removes the residual black frame edge.
- Invariants: the green/red TN/FP/FN/TP regions, counts `922`, `101`, `176`, and `210`, and all four condition annotations `g(x_i)<t & y=0`, `g(x_i)>=t & y=0`, `g(x_i)>=t & y=1`, and `g(x_i)<t & y=1` remain unchanged and in their original relationships.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-04-confusion-counts-cropped.jpg`
- QA: accepted after `view_image` inspection; all exact counts, labels, arrows, regions, and conditions remain legible, and no face, camera tile, recording overlay, cursor, watermark, browser/Zoom chrome, or black frame bar remains; `522×340` output renders cleanly.

## 05 — confusion matrix NumPy output

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-05-confusion-matrix-output.jpg`
- Disposition: accepted deterministic crop plus bounded blank-cell cursor cleanup; exact matrix code, values, and promo-email annotation retained, so imagegen was not used.
- Crop coordinates: `x=0, y=54, width=577, height=306` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black strip. Post-crop cleanup fills only blank notebook-cell space: `x=344..364, y=136..158` with `srgb(247,247,247)` removes the gray cursor without touching the code or handwritten annotation.
- Invariants: `confusion_matrix = np.array([[tn, fp], [fn, tp]])`, the displayed `array([[922, 101], [176, 210]])`, the blue envelope sketch and `25%` note, and the `4.4 Precision and Recall` heading remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-05-confusion-matrix-output-cropped.jpg`
- QA: accepted after `view_image` inspection; exact code, matrix values, annotation, and heading remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black strip remains; `577×306` output renders cleanly.

## 06 — normalized confusion matrix notebook

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-06-normalized-confusion-matrix.jpg`
- Disposition: accepted deterministic crop; exact matrix construction, count matrix, normalized fractions, and headings retained, so imagegen was not used.
- Crop coordinates: `x=0, y=54, width=577, height=306` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black strip with no post-crop content edits.
- Invariants: the `confusion_matrix` array with `922`, `101`, `176`, and `210`, the division by `confusion_matrix.sum()`, exact output values `0.6543648`, `0.07168204`, `0.12491128`, and `0.14904187`, plus the `4.4 Precision and Recall` and `4.5 ROC Curves` headings remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-06-normalized-confusion-matrix-cropped.jpg`
- QA: accepted after `view_image` inspection; exact code, numeric values, matrix context, and headings remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black strip remains; `577×306` output renders cleanly.

## 07 — accuracy from confusion table whiteboard

- Source: `cohorts/2026/04-evaluation/images/03-confusion-table-07-accuracy-from-table.jpg`
- Disposition: accepted deterministic crop plus bounded blank-board cleanup; exact table labels, counts, percentages, and accuracy relationship retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=522, height=340` from the 598×360 source; removes the left/right black frame bars and blank lower frame margin. Post-crop cleanup fills only blank board space with `srgb(246,246,220)`: `x=0..76, y=0..101` removes the partial recording wheel, `x=478..521, y=0..54` removes the webcam tile, and `x=0..3, y=102..339` removes the residual black frame edge.
- Invariants: `PREDICTIONS`, `ACTUAL`, the negative/positive row and column labels, `TN 922`, `FP 101`, `FN 176`, `TP 210`, visible cell percentages `65%`, `8%`, `12%`, and `15%`, condition annotations, and `ACCURACY=80%=65%+15%` remain unchanged and in their original relationships.
- Final path: `cohorts/2026/04-evaluation/images/03-confusion-table-07-accuracy-from-table-cropped.jpg`
- QA: accepted after `view_image` inspection; exact table structure, labels, counts, percentages, arrows, and accuracy equation remain legible, and no face, camera tile, recording overlay, cursor, watermark, browser/Zoom chrome, or black frame bar remains; `522×340` output renders cleanly.

## 08 — confusion matrix reference diagram

- Source: `cohorts/2026/04-evaluation/images/confusion_matrix.png`
- Disposition: accepted deterministic full-frame native PNG re-export with metadata stripped; exact diagram labels and geometry retained, so imagegen was not used.
- Crop coordinates: `x=0, y=0, width=1380, height=562` from the 1380×562 source; full frame retained because no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar is present.
- Invariants: `XY`, both outgoing arrows, `True/False Prediction status`, `Positive/Negative Predict Label`, `Predict Positive`, `Predict Negative`, `Actual Positive`, `Actual Negative`, `TP`, `FN`, `FP`, `TN`, the diagonal true/false prediction lines, and `False Prediction`/`True Prediction` remain unchanged in their original positions.
- Final path: `cohorts/2026/04-evaluation/images/confusion_matrix-cropped.png`
- QA: accepted after `view_image` inspection; exact labels, colors, cell geometry, arrows, and diagonal relationships remain crisp and readable; no non-teaching frame artifacts are present; `1380×562` output renders cleanly.

## 04.01 — precision definition

- Source: `cohorts/2026/04-evaluation/images/04-precision-recall-01-precision-definition.jpg`
- Disposition: accepted deterministic crop; the exact handwritten precision definition and ellipse illustration were retained, so imagegen was not used.
- Crop coordinates: `x=27, y=0, width=468, height=340` from the 598×360 source; removes the black side bars, upper-right webcam tile, lower-right recording wheel, and lower-left recording controls by trimming only the outer blank frame margin.
- Invariants: `4.4. PRECISION & RECALL`, `PRECISION`, the red/blue definition text, the oval `PREDICT` illustration, the internal divider, and the `PREDICT` arrow remain unchanged and in their original relationships.
- Final path: `cohorts/2026/04-evaluation/images/04-precision-recall-01-precision-definition-cropped.jpg`
- QA: accepted after `view_image` inspection; all exact handwritten labels and the oval remain legible, and no face, camera tile, browser/Zoom chrome, cursor, recording control, watermark, overlay, or black bar remains; `468×340` output renders cleanly.

## 04.02 — precision notebook

- Source: `cohorts/2026/04-evaluation/images/04-precision-recall-02-precision-notebook.jpg`
- Disposition: accepted deterministic crop; exact notebook code, outputs, and section headings were retained, so imagegen was not used.
- Crop coordinates: `x=0, y=68, width=577, height=292` from the 598×360 source; removes the browser/Notebook chrome, upper-right webcam tile, and right black strip with no post-crop content edits.
- Invariants: the visible normalized confusion output, `4.4 Precision and Recall`, `(tp + tn) / (tp + tn + fp + fn)`, output `0.8034066713981547`, `p = tp / (tp + fp)`, output `0.6752411575562701`, `tp + fp`, output `311`, and `4.5 ROC Curves` remain unchanged and in order.
- Final path: `cohorts/2026/04-evaluation/images/04-precision-recall-02-precision-notebook-cropped.jpg`
- QA: accepted after `view_image` inspection; exact code, numeric outputs, and headings remain legible, and no face, camera tile, browser/Zoom chrome, cursor, watermark, recording control, overlay, or black strip remains; `577×292` output renders cleanly.
