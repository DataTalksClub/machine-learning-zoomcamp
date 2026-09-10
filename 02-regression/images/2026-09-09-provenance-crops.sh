#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded native reference crops for the 2026-09-09
# regression imagegen provenance audit. Run from this directory or pass an
# explicit output directory as the first argument.
output_dir="${1:-.}"
mkdir -p "$output_dir"
output_dir="$(cd "$output_dir" && pwd)"
script_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$script_dir"

convert 05-linear-regression-simple-01-one-car-one-price.jpg \
  -crop 470x340+25+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/05-linear-regression-simple-01-one-car-one-price-imagegen-crop.jpg"

convert 11-feature-engineering-01-year-column.jpg \
  -crop 480x260+15+80 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/11-feature-engineering-01-feature-engineering-imagegen-crop.jpg"

convert 15-using-model-05-website-request-diagram.jpg \
  -crop 485x330+20+5 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/15-using-model-05-website-request-diagram-imagegen-crop.jpg"
