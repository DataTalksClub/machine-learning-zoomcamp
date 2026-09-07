# ML Zoomcamp trees screenshot rollout (lessons 01–04)

Scope in this checkout: `01-credit-risk.md`, `02-data-prep.md`,
`03-decision-trees.md`, and `04-decision-tree-learning.md` (the requested
filenames were not present). Every referenced screenshot in those lessons is
being inspected and assigned an imagegen or deterministic disposition.

## Accepted assets

- `01-credit-risk-01-loan-application.jpg` →
  `01-credit-risk-01-loan-application-imagegen.png`: imagegen regeneration.
  Source crop `(x=25, y=0, width=455, height=330)` removed the black frame,
  webcam tile, recorder controls, and color wheel before generation. The
  accepted correction removed an incorrect generated sign; checked labels
  `BANK`, `MONEY`, `YES / NO`, client-to-bank and bank-to-client arrows, and
  absence of people/camera/recording overlays.
- `01-credit-risk-02-historical-data.jpg` →
  `01-credit-risk-02-historical-data-imagegen.png`: imagegen regeneration.
  Source crop `(x=25, y=0, width=455, height=330)` removed the black frame,
  webcam tile, recorder controls, and color wheel. Checked five rows and exact
  outcome order `OK`, `OK`, `DEFAULT`, `DEFAULT`, `OK`; no extra rows or
  overlays remain.
- `01-credit-risk-03-probability-of-default.jpg` →
  `01-credit-risk-03-probability-of-default-imagegen.png`: imagegen
  regeneration. Source crop `(x=25, y=0, width=480, height=270)` removed the
  black frame, webcam tile, recorder controls, and color wheel. Checked the
  five target outcomes, `y ∈ {0, 1}`, mappings to `OK`/`DEFAULT`, and the
  statement `g(xᵢ) → probability of default`; no extra values or overlays.
- `01-credit-risk-04-dataset-columns.jpg` →
  `01-credit-risk-04-dataset-columns-cropped.png`: deterministic crop
  `(x=0, y=25, width=430, height=330)` retained the exact 14-row column
  reference and removed browser/camera chrome; exact text was not generated.
- `01-credit-risk-05-module-plan.jpg` →
  `01-credit-risk-05-module-plan-cropped.png`: deterministic crop
  `(x=0, y=35, width=500, height=320)` retained the exact notebook headings
  and bullets for sections 6.3 and 6.4 while removing browser/camera chrome.
- `02-data-prep-01-download-data.jpg` →
  `02-data-prep-01-download-data-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact download result,
  `head` command, and CSV rows; browser/camera chrome was removed.
- `02-data-prep-02-decode-status.jpg` →
  `02-data-prep-02-decode-status-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact `status_values`
  dictionary and `map` calls; browser/camera chrome was removed.
- `02-data-prep-03-encoded-missing-values.jpg` →
  `02-data-prep-03-encoded-missing-values-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact summary table and
  visible `99999999` encoded-missing values; browser/camera chrome was removed.
- `02-data-prep-04-replace-missing-with-nan.jpg` →
  `02-data-prep-04-replace-missing-with-nan-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact replacement code
  and post-replacement statistics; browser/camera chrome was removed.
- `02-data-prep-05-remove-unknown-status.jpg` →
  `02-data-prep-05-remove-unknown-status-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact filter result and
  `4454 rows × 14 columns` output; browser/camera chrome was removed.
- `02-data-prep-06-train-val-test-split.jpg` →
  `02-data-prep-06-train-val-test-split-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact two-step
  `train_test_split` and index-reset code; browser/camera chrome was removed.
- `02-data-prep-07-binary-target.jpg` →
  `02-data-prep-07-binary-target-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact binary-target
  expressions and array output; browser/camera chrome was removed.
- `03-decision-trees-01-risk-rules-tree.jpg` →
  `03-decision-trees-01-risk-rules-tree-imagegen.png`: imagegen regeneration.
  Source crop `(x=25, y=0, width=480, height=260)` removed the black frame,
  webcam tile, recorder controls, and color wheel. Checked root and nested
  conditions, TRUE/FALSE directions, and all four `OK`/`DEFAULT` leaves.
- `03-decision-trees-02-assess-risk.jpg` →
  `03-decision-trees-02-assess-risk-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact customer-dictionary,
  `assess_risk(xi)`, output, and classifier import cells while removing the
  webcam tile and browser top bar. A notebook autocomplete tooltip visible in
  the source is retained because this is exact code/UI content.
- `03-decision-trees-03-training.jpg` →
  `03-decision-trees-03-training-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact imports,
  `DictVectorizer`, training-dictionary conversion, and classifier fit cells
  while removing the webcam tile and browser top bar. The source's notebook
  autocomplete tooltip is retained for code fidelity.
- `03-decision-trees-04-overfit-auc.jpg` →
  `03-decision-trees-04-overfit-auc-cropped.png`: deterministic crop
  `(x=0, y=65, width=576, height=285)` retained the exact validation AUC,
  customer dictionary, probability prediction, and training AUC output while
  removing the webcam tile and browser top bar.
- `03-decision-trees-05-memorizing.jpg` →
  `03-decision-trees-05-memorizing-imagegen.png`: imagegen regeneration from
  the viewed source crop `(x=110, y=0, width=390, height=330)`, which removed
  the camera sliver and recording gauge. Checked exact title/subtitles
  `OVERFITTING`, `MEMORIZING THE DATA`, `BUT FAILING TO GENERALIZE`, the
  example-tree labels `HOME = "OWNER"`, `AGE > 35`, `AGE < 37`,
  `JOB = "FREELANCE"`, `DEBT > 0.0`, and red class `1`; no people, camera,
  browser, cursor, watermark, or extra labels remain.
- `03-decision-trees-06-learned-rules.jpg` →
  `03-decision-trees-06-learned-rules-imagegen.png`: imagegen regeneration
  from the viewed source crop `(x=110, y=0, width=390, height=330)`, removing
  the camera sliver and recording gauge. Checked the exact labels
  `RECORDS = NO` and `JOB = 1`, the two-step branching structure, and absence
  of people, camera, browser, cursor, watermark, or extra labels.
- `03-decision-trees-07-decision-stump.jpg` →
  `03-decision-trees-07-decision-stump-imagegen.png`: imagegen regeneration
  from the viewed source crop `(x=110, y=0, width=390, height=330)`, removing
  the camera sliver and recording gauge. Checked `DEPTH=3`, the deep-tree
  labels `HOME = "OWNER"`, `AGE > 35`, `RECORDS = "YES"`, the stump label
  `RECORDS = "NO"`, caption `DECISION STUMP`, and leaves `DEFAULT`/`OK`; no
  people, camera, browser, cursor, watermark, or extra labels remain.
- `04-decision-tree-learning-01-best-threshold.jpg` →
  `04-decision-tree-learning-01-best-threshold-cropped.png`: deterministic
  crop `(x=0, y=65, width=500, height=285)` retained the exact toy dataset
  array, `df_example`, and lesson heading while removing the webcam tile and
  browser top bar.
- `04-decision-tree-learning-02-candidate-thresholds.jpg` →
  `04-decision-tree-learning-02-candidate-thresholds-cropped.png`:
  deterministic crop `(x=0, y=65, width=500, height=285)` retained the exact
  sorted assets/status table, threshold annotations, and output while removing
  the webcam tile and browser top bar.
- `04-decision-tree-learning-03-split-t4000.jpg` →
  `04-decision-tree-learning-03-split-t4000-cropped.png`: deterministic crop
  `(x=0, y=65, width=500, height=285)` retained the exact `T = 4000` split
  code and both resulting status tables while removing the webcam tile and
  browser top bar.
- `04-decision-tree-learning-04-misclassification-rate.jpg` →
  `04-decision-tree-learning-04-misclassification-rate-cropped.png`:
  deterministic crop `(x=0, y=65, width=500, height=285)` retained the exact
  left/right status tables and 25% misclassification evidence while removing
  the webcam tile and browser top bar.
- `04-decision-tree-learning-05-impurity-table.jpg` →
  `04-decision-tree-learning-05-impurity-table-prepared.png`: deterministic
  crop `(x=25, y=0, width=550, height=360)` retained the full handwritten
  impurity table and exact numeric values. A deterministic background mask over
  relative rectangles `(0,0)-(80,95)` and `(480,0)-(549,95)` removed the
  source gauge and webcam tile; no generated text was used.
- `04-decision-tree-learning-06-split-algorithm.jpg` →
  `04-decision-tree-learning-06-split-algorithm-cropped.png`: deterministic
  crop `(x=25, y=0, width=455, height=330)` retained the exact handwritten
  split-finding pseudocode while removing the camera tile, recording gauge,
  and bottom-left controls.
- `04-decision-tree-learning-07-impurity-criteria.jpg` →
  `04-decision-tree-learning-07-impurity-criteria-cropped.png`: deterministic
  crop `(x=0, y=0, width=500, height=360)` retained the exact scikit-learn
  documentation page, formulas, and sidebar while removing the webcam tile at
  the right edge.
