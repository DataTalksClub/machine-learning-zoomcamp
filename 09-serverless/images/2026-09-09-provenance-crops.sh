#!/usr/bin/env bash
set -euo pipefail

root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

crop() {
  local source_name=$1
  local output_name=$2
  local geometry=$3
  convert "$root/$source_name" -crop "$geometry" +repage -quality 92 "$root/$output_name"
}

# Native crops for imagegen references: keep the lesson board and remove the
# camera/recorder frame. No resize, sharpen, or interpolation is performed.
crop 01-intro-01-clothes-classification-use-case.jpg 01-intro-01-clothes-classification-use-case-imagegen-crop.jpg 478x315+22+0
crop 01-intro-02-aws-lambda-deployment.jpg 01-intro-02-aws-lambda-deployment-imagegen-crop.jpg 478x315+22+0
crop 01-intro-03-lambda-uses-tf-lite.jpg 01-intro-03-lambda-uses-tf-lite-imagegen-crop.jpg 478x315+22+0
crop 02-aws-lambda-07-serverless-vs-serverful.jpg 02-aws-lambda-07-serverless-vs-serverful-imagegen-crop.jpg 478x315+22+0

# The active ref combines two exact code artifacts, so retain one native crop
# per source JPG as evidence for the deterministic replacement.
crop 03-tensorflow-lite-02-keras-predictions.jpg 03-tensorflow-lite-02-keras-predictions-native-crop.jpg 500x330+0+30
crop 03-tensorflow-lite-03-convert-to-tflite.jpg 03-tensorflow-lite-03-convert-to-tflite-native-crop.jpg 500x330+0+30

# Exact code/output artifact: render the source text and prediction values
# deterministically from the checked-in SVG. This is not an imagegen redraw
# and does not use a screenshot resize.
convert "$root/2026-09-09-tflite-artifact.svg" "$root/03-tensorflow-lite-02-03-predictions-to-tflite-crisp.png"
