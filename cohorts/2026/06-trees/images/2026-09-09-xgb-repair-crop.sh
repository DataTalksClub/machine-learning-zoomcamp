#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded reference crop used for the XGBoost semantic repair.
# The original JPG is the only source; the old published PNG is not read.
image_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
convert "$image_dir/08-xgb-tuning-01-parameters.jpg" \
  -crop 980x690+22+16 +repage -quality 100 \
  "$image_dir/08-xgb-tuning-01-parameters-imagegen-crop.jpg"
