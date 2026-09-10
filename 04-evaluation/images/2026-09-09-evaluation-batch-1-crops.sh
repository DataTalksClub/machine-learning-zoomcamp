#!/usr/bin/env bash
set -euo pipefail

# Reproduce the bounded source crops used for the first evaluation redraw batch.
# Run from this directory, optionally passing an output directory.
output_dir="${1:-.}"
mkdir -p "$output_dir"

convert 01-overview-02-churn-scenario.jpg \
  -crop 478x360+27+0 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/01-overview-02-churn-scenario-imagegen-crop.jpg"

convert 02-accuracy-08-class-imbalance.jpg \
  -crop 478x360+27+0 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/02-accuracy-08-class-imbalance-imagegen-crop.jpg"

convert 03-confusion-table-01-four-outcomes.jpg \
  -crop 523x280+27+80 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/03-confusion-table-01-four-outcomes-imagegen-crop.jpg"
