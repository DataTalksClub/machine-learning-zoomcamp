#!/usr/bin/env bash
set -euo pipefail

# Reproduce the bounded source crops for the remaining imagegen-backed
# evaluation diagrams in this worker scope.
output_dir="${1:-.}"
mkdir -p "$output_dir"

convert 03-confusion-table-04-confusion-counts.jpg \
  -crop 523x290+27+70 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/03-confusion-table-04-confusion-counts-imagegen-crop.jpg"

convert 04-precision-recall-03-precision-pie.jpg \
  -crop 523x295+27+65 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/04-precision-recall-03-precision-pie-imagegen-crop.jpg"

convert 04-precision-recall-05-recall-example.jpg \
  -crop 478x360+27+0 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/04-precision-recall-05-recall-example-imagegen-crop.jpg"
