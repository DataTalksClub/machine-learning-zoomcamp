# ML imagegen pilot: classification/evaluation

## Pilot asset

- Source: `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/04-evaluation/images/07-cross-validation-01-kfold-diagram.jpg`
- Output: `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/04-evaluation/images/07-cross-validation-01-kfold-diagram-pilot.png`
- Lesson/unit: `04-evaluation/07-cross-validation.md`, section “K-fold cross-validation”.
- Learner should notice: with `K=3`, each run trains on two folds and validates on the remaining fold; the validation fold rotates through 3, 2, and 1, and the resulting AUCs are summarized with a mean and standard deviation.
- Crop: source crop `(x=35, y=25, width=470, height=305)` from the 598x360 JPEG. This removes the webcam tile and most browser/Zoom framing; the generator also removed the residual calibration wheel.
- Prompt: exact cleanup of the cropped whiteboard diagram into a crisp digital educational illustration; preserve `K=3`, top folds `1 2 3`, the three train pairings `1+2`, `1+3`, `2+3`, validation outputs `3`, `2`, `1`, `g(x)`, and `AUC_1, AUC_2, AUC_3 -> MEAN AUC, STD AUC`; remove workshop artifacts; add no labels, percentages, or numeric results.
- QA: inspected the source with `view_image` before cropping and inspected the crop. The first generation was rejected because it hallucinated `ND` labels and changed the diagram. The second generation was inspected and accepted: it preserves the fold relationships, labels, row order, validation outputs, and AUC summary, with no webcam, browser chrome, person, gauge, watermark, or fabricated metric values.
- Why this is a good pilot: it has high instructional contribution and complementarity, is a diagram rather than exact code/output, and the visual structure remains useful after the workshop capture is removed. It is also easy to compare against the source and has a bounded set of invariants.

## Not regenerated

- `03-classification/images/12-using-log-reg-04-production-diagram.jpg`: despite its filename, the inspected frame is a dataframe/code screenshot with customer fields and exact values; imagegen could corrupt the values and it does not show the promised production diagram.
- `04-evaluation/images/07-cross-validation-05-tuning-results.jpg`: the plot/result contains exact AUC values and parameter labels that must remain numerically faithful; a generated redraw risks changing those values, so it should use a deterministic crop or source plot instead.
