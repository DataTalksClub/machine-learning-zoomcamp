#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded, non-camera source crops used for the 06-trees
# imagegen redraws. Coordinates are ImageMagick's x,y,width,height format.
# The source JPGs and published PNGs are never modified by this script.

image_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

crop() {
    local source="$1"
    local destination="$2"
    local geometry="$3"
    convert "$image_dir/$source" -crop "$geometry" +repage -quality 100 "$image_dir/$destination"
}

crop "03-decision-trees-01-risk-rules-tree.jpg" \
     "03-decision-trees-01-risk-rules-tree-imagegen-crop.jpg" \
     "480x260+25+0"
crop "03-decision-trees-05-memorizing.jpg" \
     "03-decision-trees-05-memorizing-imagegen-crop.jpg" \
     "390x330+110+0"
crop "03-decision-trees-07-decision-stump.jpg" \
     "03-decision-trees-07-decision-stump-imagegen-crop.jpg" \
     "390x330+110+0"
crop "06-random-forest-01-board-of-experts.jpg" \
     "06-random-forest-01-board-of-experts-imagegen-crop.jpg" \
     "980x690+22+16"
crop "06-random-forest-02-random-forest.jpg" \
     "06-random-forest-02-random-forest-imagegen-crop.jpg" \
     "1024x724+0+0"
crop "07-boosting-01-boosting-vs-random-forest.jpg" \
     "07-boosting-01-boosting-vs-random-forest-imagegen-crop.jpg" \
     "980x690+22+16"
crop "07-boosting-02-gradient-boosting-trees.jpg" \
     "07-boosting-02-gradient-boosting-trees-imagegen-crop.jpg" \
     "980x690+22+16"

# These four source frames are notebook screenshots. The bounds retain the
# lesson-relevant title/bullets or parameter cell while excluding browser
# chrome, the webcam tile, and unrelated notebook cells.
crop "10-summary-01-summary-slide.jpg" \
     "10-summary-01-summary-slide-imagegen-crop.jpg" \
     "480x125+90+135"
crop "10-summary-04-random-forest.jpg" \
     "10-summary-04-random-forest-imagegen-crop.jpg" \
     "480x88+90+119"
crop "10-summary-05-gradient-boosting.jpg" \
     "10-summary-05-gradient-boosting-imagegen-crop.jpg" \
     "480x100+90+112"
crop "10-summary-06-xgb-parameters.jpg" \
     "10-summary-06-xgb-parameters-imagegen-crop.jpg" \
     "465x185+90+78"
