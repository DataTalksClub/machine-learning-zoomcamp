#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded reference crops used for the 2026-09-09
# classification illustration repairs. Run from this directory or pass an
# explicit output directory as the first argument.
output_dir="${1:-.}"
mkdir -p "$output_dir"
script_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$script_dir"

convert 05-risk-03-difference-vs-risk-ratio.jpg \
  -crop 490x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-risk-03-difference-vs-risk-ratio-imagegen-crop.jpg"

convert 06-mutual-info-01-mutual-information-wikipedia.jpg \
  -crop 440x270+105+65 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/06-mutual-info-01-mutual-information-wikipedia-imagegen-crop.jpg"

convert 11-log-reg-interpretation-06-second-example-slide.jpg \
  -crop 490x300+15+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/11-log-reg-interpretation-06-second-example-imagegen-crop.jpg"

convert 13-summary-01-churn-prediction-slide.jpg \
  -crop 520x340+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/13-summary-01-churn-prediction-imagegen-crop.jpg"
