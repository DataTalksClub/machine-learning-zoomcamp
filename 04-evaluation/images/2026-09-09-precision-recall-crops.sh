#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded instructional regions from the unchanged 598x360
# video-frame JPEGs. The retained crop files in this directory were copied
# byte-for-byte from the worker's verified temporary crops. ImageMagick's
# crop command below reproduces those exact JPEG bytes, including the source
# JPEG comment and quality/sampling settings.
#
# Usage:
#   ./2026-09-09-precision-recall-crops.sh [output-directory]
#
# The output directory defaults to a disposable directory under /tmp so that
# rerunning the script cannot overwrite the retained audit artifacts.

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
OUTPUT_DIR=${1:-"$(mktemp -d /tmp/precision-recall-crops.XXXXXX)"}
mkdir -p -- "$OUTPUT_DIR"

convert "$SCRIPT_DIR/04-precision-recall-01-precision-definition.jpg" \
  -crop 470x355+18+0 +repage -quality 90 \
  -sampling-factor 2x2,1x1,1x1 \
  "$OUTPUT_DIR/04-precision-recall-01-precision-definition-imagegen-crop.jpg"

convert "$SCRIPT_DIR/04-precision-recall-06-precision-recall-table.jpg" \
  -crop 490x350+15+0 +repage -quality 90 \
  -sampling-factor 2x2,1x1,1x1 \
  "$OUTPUT_DIR/04-precision-recall-06-precision-recall-table-imagegen-crop.jpg"

sha256sum \
  "$OUTPUT_DIR/04-precision-recall-01-precision-definition-imagegen-crop.jpg" \
  "$OUTPUT_DIR/04-precision-recall-06-precision-recall-table-imagegen-crop.jpg"
