# ML Zoomcamp imagegen pilot — intro/regression

## Selected pilot

- **Area:** `cohorts/2026/02-regression`
- **Lesson/unit:** `12-categorical-variables.md`, “Encoding categories as binary columns”
- **Source path:** `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/02-regression/images/12-categorical-variables-02-encoding-diagram.jpg`
- **Source dimensions:** 598×360 workshop frame
- **Crop before generation:** yes
- **Crop coordinates:** `x=0, y=0, width=510, height=360` (right-side webcam tile removed; the source’s left recording control remains in the crop reference but was excluded from the regenerated output)
- **Final output path:** `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/02-regression/images/12-categorical-variables-02-encoding-diagram.jpg`
- **Final dimensions:** 1492×1054 JPEG

The learner should notice that the categorical `ND` column with rows `2, 3, 4, 2` becomes three binary indicator columns, `ND2`, `ND3`, and `ND4`, with exactly one `1` in each row.

## Generation prompt

```text
Use case: scientific-educational
Asset type: lesson illustration for an introductory machine-learning regression lesson
Primary request: Recreate the referenced hand-drawn one-hot encoding diagram as a crisp, clean educational infographic. Preserve the instructional mapping exactly: a single categorical column labeled "ND" containing the values 2, 3, 4, 2 maps row-by-row to three binary indicator columns labeled "ND2", "ND3", and "ND4". The rows must remain:
ND: 2, 3, 4, 2
ND2: 1, 0, 0, 1
ND3: 0, 1, 0, 0
ND4: 0, 0, 1, 0
Input image: the cropped source is the edit target/reference; preserve its layout and exact data.
Scene/backdrop: clean warm off-white classroom diagram background, no screenshot framing
Subject: left categorical input column and three right one-hot encoded columns, aligned rows, with simple arrows from the input toward the encoded representation
Style/medium: polished flat educational infographic, crisp dark navy outlines and blue accent labels, high legibility, faithful to the original simple diagram
Composition/framing: landscape, centered with generous margins; left input column and three evenly spaced output columns; no webcam or browser/Zoom controls
Text (verbatim): "ND", "ND2", "ND3", "ND4", "2", "3", "4", "2", "1", "0", "0", "1", "0", "1", "0", "0", "0", "1", "0"
Constraints: preserve all exact labels, row order, and binary values; preserve the one-hot encoding relationship; no invented values; remove webcam tile, browser chrome, black borders, recording controls, cursor, watermarks, and unrelated marks; make every label and number readable.
Avoid: extra columns, changed numbers, swapped rows, realistic UI, code, charts, decorative icons, additional text, logos, watermark.
```

## QA notes

- Re-inspected the original with `view_image` before cropping and generation.
- Re-inspected the generated output and the installed final JPEG with `view_image`.
- Confirmed visible labels are `ND`, `ND2`, `ND3`, `ND4`.
- Confirmed visible rows are `2,3,4,2`; `1,0,0,1`; `0,1,0,0`; and `0,0,1,0`.
- Webcam tile, browser/Zoom chrome, black side border, cursor, recording controls, and source watermark are absent from the final asset.
- The clean output is substantially larger and more legible than the 598×360 source while retaining the lesson’s meaning.
- Generation used the built-in imagegen edit flow with the cropped source as the edit target/reference.
