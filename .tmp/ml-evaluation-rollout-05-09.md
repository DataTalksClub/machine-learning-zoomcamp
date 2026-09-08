# Evaluation lessons 05–09 screenshot rollout

Worker scope: `cohorts/2026/04-evaluation/05-roc.md` through
`09-explore-more.md`.

The rubric cutoff is 7/12, with the hard gates from
`zoomcamp-ops/template/illustration-rubric.md`: an image must add a specific
learning point, match its caption, and remain readable. Exact plots, code,
commands, URLs, numbers, and notebook/UI states use deterministic crops or
exports. Conceptual diagrams may use imagegen only after source inspection;
all originals are preserved. Duplicate `TPR_FPR.png` references share one
disposition.

Capability: this worker has the built-in `imagegen` skill and used it only for
bounded conceptual illustrations after deterministic crop/source inspection.

## Dispositions

- `06-auc-02-auc-values.jpg` — **crop/replace**, score 11/12. The five ROC/AUC comparisons teach how curve shape maps to 0.5, 0.6, 0.8, 0.9, and 1.0; the original had a color-wheel overlay, camera tile, handwriting, and low readability. Cropped at `(x=110, y=0, w=394, h=350)` for source inspection, then regenerated with imagegen as `06-auc-02-auc-values-imagegen.png`; all five curves, values, and GOOD/GREAT/POOR labels were checked. Original preserved.
- `06-auc-05-auc-interpretation.jpg` — **crop/replace**, score 10/12. The score-ranking example explains the positive-vs-negative comparison behind AUC, but the source was a blurry whiteboard frame with a camera tile, color-wheel overlay, black border, and handwritten text. Cropped at `(x=14, y=0, w=476, h=350)` for source inspection, then regenerated with imagegen as `06-auc-05-auc-interpretation-imagegen.png`; NO CHURN/CHURN, NEGATIVE/POSITIVE groups, source scores, selected 0.50/0.60 pair, and callout were checked. Original preserved.
- `05-roc-01-tpr-fpr-vs-threshold.jpg` — **crop/replace**, score 12/12. The plot uniquely shows how both TPR and FPR fall as the classification threshold increases. The 372×248 source was already a clean plot with no overlays, so it was deterministically re-exported at 2× with Lanczos scaling and light sharpening as `05-roc-01-tpr-fpr-vs-threshold-cropped.png`; curve geometry, axes, ticks, and legend were checked. Original preserved.
- `05-roc-02-random-model-tpr-fpr.jpg` — **crop/replace**, score 11/12. The nearly overlapping descending TPR/FPR lines show that a random model cannot distinguish churners from non-churners. The 372×248 source was already a clean plot, so it was deterministically re-exported at 2× with Lanczos scaling and light sharpening as `05-roc-02-random-model-tpr-fpr-cropped.png`; both curves and axes were checked. Original preserved.
- `05-roc-03-ideal-model-tpr-fpr.jpg` — **crop/replace**, score 12/12. The plot uniquely shows the ideal model keeping TPR at 1.0 until the separating threshold while FPR falls to zero. The 372×248 source was already a clean plot, so it was deterministically re-exported at 2× with Lanczos scaling and light sharpening as `05-roc-03-ideal-model-tpr-fpr-cropped.png`; both curves, the threshold shape, axes, and legend were checked. Original preserved.
- `05-roc-04-model-vs-ideal-tpr-fpr.jpg` — **crop/replace**, score 12/12. The overlaid curves make the gap between the learned model and ideal reference explicit. The 372×248 source was deterministically re-exported at 2× with a small white border, Lanczos scaling, and light sharpening as `05-roc-04-model-vs-ideal-tpr-fpr-cropped.png`; all four curves, legend, and axes were checked. Original preserved.
- `05-roc-05-roc-curve-manual.jpg` — **crop/replace**, score 12/12. This plot is the lesson’s central visual evidence for comparing the model ROC curve with the random diagonal baseline. The 330×317 source was deterministically re-exported at 2× with a small white border, Lanczos scaling, and light sharpening as `05-roc-05-roc-curve-manual-cropped.png`; model/random lines, FPR/TPR axes, and legend were checked. Original preserved.
