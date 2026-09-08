# Regression screenshot rollout: lessons 13–17

Scope: every Markdown image reference in `13-regularization.md` through
`17-explore-more.md`. The rubric cutoff is 4/12: scores 0–3 are removed,
4–6 are reviewed for crop/replace, and 7–12 are kept when no hard gate is
violated. One caption-mismatched source is removed below the cutoff and one
useful source is remapped to the correct summary caption; `17-explore-more.md`
has no image references.

Capability: this worker has the `imagegen` skill. Exact code, commands, URLs,
plots, numeric output, and notebook UI use deterministic crops. The one
bounded website-to-model sketch is being evaluated for imagegen separately.

## Decisions

| Lesson | Source | Decision | Score | Preparation and invariants |
| --- | --- | --- | ---: | --- |
| 13 | `13-regularization-01-normal-equation.jpg` | keep/crop | 10/12 | Crop `(x=95,y=55,w=230,h=170)`; retain the exact handwritten `XᵀX` teaching fragment; remove camera tile, controls, and black frame. |
| 13 | `13-regularization-02-duplicate-columns.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the feature and Gram-matrix values; remove browser/camera frame. A native notebook caret remains in the code cell without obscuring the values. |
| 13 | `13-regularization-03-noisy-gram-matrix.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the noisy Gram matrix and large inverse values exactly; remove browser/camera frame. The source itself begins mid-cell, so that source-edge truncation remains. |
| 13 | `13-regularization-04-huge-weights.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the inverse and million-scale weight values plus the next singular-matrix setup; remove browser/camera frame. |
| 13 | `13-regularization-05-singular-matrix.jpg` | keep/crop | 9/12 | Crop `(x=25,y=40,w=480,h=315)`; preserve the duplicate-column input and visible `LinAlgError` traceback; remove browser/camera frame. The original frame cuts off the final exception text, so that source-edge limitation remains. |
| 13 | `13-regularization-06-eye-diagonal.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the exact `XTX + np.eye(3)` result and diagonal change; remove browser/camera frame. A native selection highlight remains over two numeric glyphs but does not change their values. |
| 13 | `13-regularization-07-regularized-training.jpg` | keep/crop | 11/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the complete `train_linear_regression_reg` function and the preceding controlled inverse; remove browser/camera frame. |
| 13 | `13-regularization-08-rmse-result.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the exact `r=0.01` validation cell and RMSE `0.4608208286209523`; remove browser/camera frame. |
| 14 | `14-tuning-model-01-r-values-loop.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the exact loop over `r` values and validation-cell code; remove browser/camera frame. |
| 14 | `14-tuning-model-02-rmse-per-r.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve every printed `r`, bias, and RMSE value; remove browser/camera frame. The source's native blue selection highlight remains over the first RMSE value without changing the text. |
| 14 | `14-tuning-model-03-choosing-r.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the full comparison table used to justify choosing `r=0.001`; remove browser/camera frame. |
| 14 | `14-tuning-model-04-final-model.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve the selected `r=0.001` training cell and validation RMSE `0.46081585838957173`; remove browser/camera frame. |
| 16 | `16-summary-01-data-cleaning.jpg` | replace/remap | 9/12 | The original file was a categorical-variable frame and failed the caption-match hard gate, so it was removed. The useful data-cleaning capture from `16-summary-02-log-transformation.jpg` was deterministically cropped `(x=20,y=65,w=550,h=290)` into `16-summary-01-data-cleaning-cropped.png`; exact `str.lower().str.replace` code and output are preserved. |
| 16 | `16-summary-02-log-transformation.jpg` | remove/reassign | 2/12 | The source is the same data-cleaning cell reused above, not a log-transformation plot; the caption-match hard gate fails. Its original file is retained only as the source for the corrected data-cleaning crop, and the misleading Markdown reference is removed. |
| 16 | `16-summary-03-linear-regression-loop.jpg` | keep/crop | 10/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the exact single-example weights, loop, and `linear_regression` implementation; remove browser/camera frame. |
| 16 | `16-summary-04-vector-form.jpg` | keep/crop | 10/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the `dot`, vector-form regression, and resulting weight vector; remove browser/camera frame. |
| 16 | `16-summary-05-normal-equation.jpg` | keep/crop | 10/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the exact Gram-matrix inverse implementation and resulting weights; remove browser/camera frame. |
| 16 | `16-summary-06-baseline-model.jpg` | keep/crop | 9/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the baseline section, five base-feature list, and training setup; remove browser/camera frame. The source ends before the later baseline result, so that source-edge limitation remains. |
| 15 | `15-using-model-01-full-train-concat.jpg` | keep/crop | 10/12 | Crop `(x=20,y=210,w=540,h=145)`; focus on the `pd.concat` cell and resulting combined dataframe; remove browser/camera frame and unrelated preceding cells. |
| 15 | `15-using-model-02-full-train-prepare-x.jpg` | keep/crop | 10/12 | Crop `(x=25,y=50,w=480,h=300)`; preserve `concat`, `reset_index`, `prepare_X`, and the resulting feature matrix; remove browser/camera frame. |
| 15 | `15-using-model-03-final-model-weights.jpg` | keep/crop | 9/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the final-model training cell and printed weights with a wider content area; remove browser/camera frame. The source cuts off the final weight row at the bottom, so that source-edge limitation remains. |
| 15 | `15-using-model-04-test-rmse.jpg` | keep/crop | 10/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the full test-set preparation cell and exact RMSE `0.4600753970266562`; remove browser/camera frame. |
| 15 | `15-using-model-05-website-request-diagram.jpg` | keep/imagegen | 11/12 | Deterministic source crop `(x=20,y=5,w=485,h=330)` removed the face, cursor, controls, and black frame before generation. Built-in imagegen preserved the left form → right dictionary relationship and exact labels `TOYOTA`/`SIENNA`; generated output contains no people, camera, chrome, or extra labels. |
| 15 | `15-using-model-06-car-dictionary.jpg` | keep/crop | 9/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the exact Toyota Sienna dictionary fields and values visible in the source; remove browser/camera frame. The source cuts off the remaining dictionary fields at the bottom, so that limitation remains. |
| 15 | `15-using-model-07-single-car-prediction.jpg` | keep/crop | 10/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the one-row dataframe, `prepare_X`/prediction cells, and exact logarithmic prediction `10.63249251`; remove browser/camera frame. |
| 15 | `15-using-model-08-prediction-vs-actual.jpg` | keep/crop | 10/12 | Crop `(x=20,y=65,w=550,h=290)`; preserve the exact log prediction, exponentiated prediction `41459.336786653585`, and actual `35000.00000000001`; remove browser/camera frame. |
