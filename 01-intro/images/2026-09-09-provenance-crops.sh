#!/usr/bin/env bash
set -euo pipefail

# Recreate the bounded native reference crops for the 20 strict-audit assets.
# Coordinates use ImageMagick's x,y,width,height notation. This script only
# crops decoded source JPG pixels: it does not resize, sharpen, Lanczos-scale,
# or otherwise enhance any image. The previous published PNGs are not inputs.

image_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

crop() {
    local source="$1"
    local destination="$2"
    local geometry="$3"
    convert "$image_dir/$source" \
        -crop "$geometry" +repage -strip \
        "$image_dir/$destination"
}

crop "01-what-is-ml-01-price-field.jpg" \
     "01-what-is-ml-01-price-field-cropped.png" \
     "380x190+115+100"
crop "01-what-is-ml-03-expert-or-model.jpg" \
     "01-what-is-ml-03-expert-or-model-cropped.png" \
     "530x243+35+82"

crop "02-ml-vs-rules-01-spam-examples.jpg" \
     "02-ml-vs-rules-01-spam-examples-cropped.png" \
     "530x243+35+82"
crop "02-ml-vs-rules-03-more-spam.jpg" \
     "02-ml-vs-rules-03-more-spam-cropped.png" \
     "530x243+35+82"
crop "02-ml-vs-rules-05-encode-email.jpg" \
     "02-ml-vs-rules-05-encode-email-cropped.png" \
     "520x243+45+82"
crop "02-ml-vs-rules-07-rule-based-summary.jpg" \
     "02-ml-vs-rules-07-rule-based-summary-cropped.png" \
     "510x243+55+82"
crop "02-ml-vs-rules-08-ml-summary.jpg" \
     "02-ml-vs-rules-08-ml-summary-cropped.png" \
     "540x243+25+82"

crop "03-supervised-ml-04-regression.jpg" \
     "03-supervised-ml-04-regression-cropped.png" \
     "545x243+20+82"
crop "03-supervised-ml-06-ranking.jpg" \
     "03-supervised-ml-06-ranking-cropped.png" \
     "555x243+10+82"
crop "03-supervised-ml-07-summary.jpg" \
     "03-supervised-ml-07-summary-cropped.png" \
     "545x243+20+82"

crop "04-crisp-dm-02-process-diagram.jpg" \
     "04-crisp-dm-02-process-diagram-cropped.png" \
     "545x243+20+82"
crop "04-crisp-dm-03-business-understanding.jpg" \
     "04-crisp-dm-03-business-understanding-cropped.png" \
     "545x243+20+82"
crop "04-crisp-dm-04-data-preparation.jpg" \
     "04-crisp-dm-04-data-preparation-cropped.png" \
     "555x243+10+82"

crop "05-model-selection-01-train-validation.jpg" \
     "05-model-selection-01-train-validation-cropped.png" \
     "530x243+35+82"
crop "05-model-selection-03-train-valid-test.jpg" \
     "05-model-selection-03-train-valid-test-cropped.png" \
     "545x243+20+82"
crop "05-model-selection-04-select-and-test.jpg" \
     "05-model-selection-04-select-and-test-cropped.png" \
     "545x243+20+82"

# This crop already exists as a reviewed, bounded native reference from the
# original 640x360 JPG. Keep it byte-for-byte unchanged.
test -f "$image_dir/06-environment-03-vscode-desktop-cropped.png"

crop "10-summary-04-supervised-g-x-y.jpg" \
     "10-summary-04-supervised-g-x-y-cropped.png" \
     "545x243+20+82"
crop "10-summary-05-crisp-dm-bigger-picture.jpg" \
     "10-summary-05-crisp-dm-bigger-picture-cropped.png" \
     "545x243+20+82"
crop "10-summary-06-model-selection-split.jpg" \
     "10-summary-06-model-selection-split-cropped.png" \
     "545x243+20+82"
