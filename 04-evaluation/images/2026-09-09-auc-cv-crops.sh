#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded reference crops for the AUC and cross-validation
# illustrations. Run from this directory or pass an output directory.
output_dir="${1:-.}"
mkdir -p "$output_dir"
script_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$script_dir"

# Keep these ImageMagick options unchanged: they reproduce the tracked
# reference JPEGs byte-for-byte on the current source files.
convert 06-auc-02-auc-values.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/06-auc-02-auc-values-imagegen-crop.jpg"

convert 06-auc-05-auc-interpretation.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/06-auc-05-auc-interpretation-imagegen-crop.jpg"

convert 07-cross-validation-01-kfold-diagram.jpg \
  -crop 500x350+10+0 +repage -sampling-factor 2x2 -quality 90 \
  "$output_dir/07-cross-validation-01-kfold-diagram-imagegen-crop.jpg"
