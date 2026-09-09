#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded reference crops used for the 2026-09-09 evaluation
# illustration repairs. Run from this directory or pass an output directory.
output_dir="${1:-.}"
mkdir -p "$output_dir"
script_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$script_dir"

convert 01-overview-02-churn-scenario.jpg \
  -crop 490x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/01-overview-02-churn-scenario-imagegen-crop.jpg"

convert 02-accuracy-08-class-imbalance.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/02-accuracy-08-class-imbalance-imagegen-crop.jpg"

convert 03-confusion-table-01-four-outcomes.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/03-confusion-table-01-four-outcomes-imagegen-crop.jpg"

convert 03-confusion-table-04-confusion-counts.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/03-confusion-table-04-confusion-counts-imagegen-crop.jpg"

convert 04-precision-recall-03-precision-pie.jpg \
  -crop 500x350+15+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/04-precision-recall-03-precision-pie-imagegen-crop.jpg"

convert 04-precision-recall-05-recall-example.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/04-precision-recall-05-recall-example-imagegen-crop.jpg"

convert 05-roc-01-tpr-fpr-vs-threshold.jpg \
  -crop 364x238+4+4 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-roc-01-tpr-fpr-vs-threshold-reference-crop.jpg"

convert 05-roc-02-random-model-tpr-fpr.jpg \
  -crop 364x238+4+4 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-roc-02-random-model-tpr-fpr-reference-crop.jpg"

convert 05-roc-03-ideal-model-tpr-fpr.jpg \
  -crop 364x238+4+4 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-roc-03-ideal-model-tpr-fpr-reference-crop.jpg"

convert 05-roc-04-model-vs-ideal-tpr-fpr.jpg \
  -crop 364x238+4+4 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-roc-04-model-vs-ideal-tpr-fpr-reference-crop.jpg"

convert 05-roc-05-roc-curve-manual.jpg \
  -crop 322x309+4+4 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-roc-05-roc-curve-manual-reference-crop.jpg"

convert 05-roc-06-roc-curve-sklearn.jpg \
  -crop 322x309+4+4 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-roc-06-roc-curve-sklearn-reference-crop.jpg"

convert 06-auc-02-auc-values.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/06-auc-02-auc-values-imagegen-crop.jpg"

convert 06-auc-05-auc-interpretation.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/06-auc-05-auc-interpretation-imagegen-crop.jpg"

convert 07-cross-validation-01-kfold-diagram.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/07-cross-validation-01-kfold-diagram-imagegen-crop.jpg"
