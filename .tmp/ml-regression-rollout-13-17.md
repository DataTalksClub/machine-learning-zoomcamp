# Regression screenshot rollout: lessons 13–17

Scope: every Markdown image reference in `13-regularization.md` through
`17-explore-more.md`. The rubric cutoff is 4/12: scores 0–3 are removed,
4–6 are reviewed for crop/replace, and 7–12 are kept when no hard gate is
violated. No image in this batch scored below the cutoff; `17-explore-more.md`
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
| 15 | `15-using-model-01-full-train-concat.jpg` | keep/crop | 10/12 | Crop `(x=20,y=210,w=540,h=145)`; focus on the `pd.concat` cell and resulting combined dataframe; remove browser/camera frame and unrelated preceding cells. |
