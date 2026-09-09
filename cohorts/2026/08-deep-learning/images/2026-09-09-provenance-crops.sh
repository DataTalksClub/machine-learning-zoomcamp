#!/usr/bin/env bash
set -euo pipefail

root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

crop() {
  local source_name=$1
  local output_name=$2
  local geometry=$3
  convert "$root/$source_name" -crop "$geometry" +repage -quality 92 "$root/$output_name"
}

# Conceptual diagrams: preserve the lesson board while excluding the camera,
# recorder controls, and the black frame on the right. These are native crops;
# this script deliberately has no resize, sharpen, or interpolation operation.
crop 01-fashion-classification-01-tabular-vs-images.jpg 01-fashion-classification-01-tabular-vs-images-imagegen-crop.jpg 478x360+22+0
crop 01-fashion-classification-02-upload-service.jpg 01-fashion-classification-02-upload-service-imagegen-crop.jpg 478x360+22+0
crop 02-tensorflow-keras-01-keras-inside-tensorflow.jpg 02-tensorflow-keras-01-keras-inside-tensorflow-imagegen-crop.jpg 478x360+22+0
crop 02-tensorflow-keras-05-image-sizes.jpg 02-tensorflow-keras-05-image-sizes-imagegen-crop.jpg 478x360+22+0
crop 02-tensorflow-keras-07-rgb-channels.jpg 02-tensorflow-keras-07-rgb-channels-imagegen-crop.jpg 478x360+22+0
crop 04-conv-neural-nets-01-cnn-overview.jpg 04-conv-neural-nets-01-cnn-overview-imagegen-crop.jpg 456x360+44+0
crop 04-conv-neural-nets-02-feature-map.jpg 04-conv-neural-nets-02-feature-map-imagegen-crop.jpg 456x360+44+0
crop 04-conv-neural-nets-03-one-feature-map-per-filter.jpg 04-conv-neural-nets-03-one-feature-map-per-filter-imagegen-crop.jpg 456x360+44+0
crop 04-conv-neural-nets-04-chained-conv-layers.jpg 04-conv-neural-nets-04-chained-conv-layers-imagegen-crop.jpg 456x360+44+0
crop 04-conv-neural-nets-05-vector-representation.jpg 04-conv-neural-nets-05-vector-representation-imagegen-crop.jpg 456x360+44+0
crop 04-conv-neural-nets-07-dense-layer.jpg 04-conv-neural-nets-07-dense-layer-imagegen-crop.jpg 456x360+44+0
crop 04-conv-neural-nets-08-summary.jpg 04-conv-neural-nets-08-summary-imagegen-crop.jpg 456x360+44+0
crop 05-transfer-learning-01-transfer-learning-idea.jpg 05-transfer-learning-01-transfer-learning-idea-imagegen-crop.jpg 456x360+44+0
crop 06-learning-rate-01-book-analogy.jpg 06-learning-rate-01-book-analogy-imagegen-crop.jpg 478x360+22+0
crop 07-checkpointing-02-callbacks.jpg 07-checkpointing-02-callbacks-imagegen-crop.jpg 478x315+22+0
crop 07-checkpointing-04-save-best-only.jpg 07-checkpointing-04-save-best-only-imagegen-crop.jpg 478x315+22+0
crop 08-more-layers-01-inner-layer-diagram.jpg 08-more-layers-01-inner-layer-diagram-imagegen-crop.jpg 478x360+22+0
crop 09-dropout-01-motivation-logo.jpg 09-dropout-01-motivation-logo-imagegen-crop.jpg 478x315+22+0
crop 09-dropout-02-hiding-input.jpg 09-dropout-02-hiding-input-imagegen-crop.jpg 478x315+22+0
crop 09-dropout-04-v3-diagram.jpg 09-dropout-04-v3-diagram-imagegen-crop.jpg 478x315+22+0
crop 10-augmentation-01-generate-more-images.jpg 10-augmentation-01-generate-more-images-imagegen-crop.jpg 478x315+22+0
crop 13-summary-01-use-case-diagram.jpg 13-summary-01-use-case-diagram-imagegen-crop.jpg 478x315+22+0

# This is an exact plot, so publish the bounded native crop rather than a
# redraw. It contains the source curve, tick marks, labels, and annotations;
# the camera and recorder controls are outside this bound.
convert "$root/07-checkpointing-04-save-best-only.jpg" -crop 438x305+22+0 +repage -quality 92 "$root/07-checkpointing-04-save-best-only-native-crop.jpg"
convert "$root/07-checkpointing-04-save-best-only.jpg" -crop 438x305+22+0 +repage "$root/07-checkpointing-04-save-best-only-imagegen.png"

# Exact visual artifacts use native source crops as evidence. The published
# replacements are made separately from these crops and are never resized.
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

# Recompose the three exact augmentation grids from bounded source regions;
# this removes notebook controls and the hand-drawn annotation while keeping
# every source pixel in each grid. The fifth zoom-x tile is then cleaned with
# a local vertical sample for only blue annotation pixels.
convert "$root/10-augmentation-02-flip-rotation-shift-grids.jpg" -crop 410x88+35+15 +repage "$work/flip.png"
convert "$root/10-augmentation-02-flip-rotation-shift-grids.jpg" -crop 410x92+35+145 +repage "$work/rotation.png"
convert "$root/10-augmentation-02-flip-rotation-shift-grids.jpg" -crop 410x82+35+278 +repage "$work/shift.png"
convert "$work/flip.png" "$work/rotation.png" "$work/shift.png" -append "$root/10-augmentation-02-flip-rotation-shift-grids-native-crop.png"
convert "$root/10-augmentation-02-flip-rotation-shift-grids-native-crop.png" -quality 92 "$root/10-augmentation-02-flip-rotation-shift-grids-native-crop.jpg"
cp "$root/10-augmentation-02-flip-rotation-shift-grids-native-crop.png" "$root/10-augmentation-02-flip-rotation-shift-grids-imagegen.png"

convert "$root/10-augmentation-03-zoom-grid.jpg" -crop 410x78+35+100 +repage "$work/zoom-x.png"
convert "$root/10-augmentation-03-zoom-grid.jpg" -crop 410x78+35+225 +repage "$work/zoom-y.png"
convert "$work/zoom-x.png" -fx '((u.b-u.r)>0.08) ? p{i,j+12} : u' "$work/zoom-x-clean.png"
convert "$work/zoom-y.png" -fx '((u.b-u.r)>0.08) ? p{i,j+12} : u' "$work/zoom-y-clean.png"
convert "$work/zoom-x-clean.png" "$work/zoom-y-clean.png" -append "$root/10-augmentation-03-zoom-grid-native-crop.png"
convert "$root/10-augmentation-03-zoom-grid-native-crop.png" -quality 92 "$root/10-augmentation-03-zoom-grid-native-crop.jpg"
cp "$root/10-augmentation-03-zoom-grid-native-crop.png" "$root/10-augmentation-03-zoom-grid-imagegen.png"

convert "$root/10-augmentation-06-val-stuck-077.jpg" -crop 300x185+90+100 +repage "$root/10-augmentation-06-val-stuck-077-native-crop.jpg"
convert "$root/10-augmentation-06-val-stuck-077.jpg" -crop 300x185+90+100 +repage "$root/10-augmentation-06-val-stuck-077-imagegen.png"
convert "$root/12-using-model-03-load-img-pants.jpg" -crop 290x220+105+125 +repage "$root/12-using-model-03-load-img-pants-native-crop.jpg"
convert "$root/12-using-model-03-load-img-pants.jpg" -crop 290x220+105+125 +repage "$root/12-using-model-03-load-img-pants-imagegen.png"
