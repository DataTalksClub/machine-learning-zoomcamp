#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded reference crop used for the eta-plot repair.
# The original JPG is the only source; the previous published PNG is never
# read by this script.
image_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

convert "$image_dir/08-xgb-tuning-02-tuning-eta.jpg" \
    -crop 680x500+35+35 +repage -quality 100 \
    "$image_dir/08-xgb-tuning-02-tuning-eta-imagegen-crop.jpg"
