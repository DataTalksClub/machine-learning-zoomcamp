#!/usr/bin/env bash
set -euo pipefail

# Reproduce the bounded native crop used for the remaining evaluation redraw.
# The original JPG and the published PNG are never modified by this script.

output_dir="${1:-.}"
mkdir -p "$output_dir"

convert 02-accuracy-02-accuracy-example.jpg \
  -crop 450x330+27+0 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/02-accuracy-02-accuracy-example-imagegen-crop.jpg"
