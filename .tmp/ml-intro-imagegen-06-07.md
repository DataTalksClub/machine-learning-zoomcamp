# ML Zoomcamp intro imagegen pilot: assets 06–07

## Method

- Used the built-in `image_gen` tool with each local screenshot as a cropped reference.
- Inspected both original screenshots first with `view_image`.
- Cropped the instructional content deterministically before generation so the presenter tile, recording/browser overlays, cursor, and black side chrome were not supplied as reference content.
- Kept the original JPEGs unchanged and saved versioned PNG siblings for review.

## Asset 06: using a model

- Source: `cohorts/2026/01-intro/images/01-what-is-ml-06-using-model.jpg` (598×360)
- Crop: `500×255+25+82`
- Output: `cohorts/2026/01-intro/images/01-what-is-ml-06-using-model-imagegen-pilot.png` (1692×930)
- Prompt iteration: 1
- Prompt focus: crisp scientific-educational diagram; exact title, feature-table labels and values, faded target column, `model` box, `predict` arrow, and prediction values `$1.5k`, `$0.4k`, `$20k`.
- Validation: passed visual inspection. All required labels and values are readable; the feature-to-model-to-predictions relationship is preserved. No presenter, face, camera tile, browser/Zoom chrome, recording controls, cursor, watermark, black bars, or screenshot artifacts remain.

## Asset 07: suggest price

- Source: `cohorts/2026/01-intro/images/01-what-is-ml-07-suggest-price.jpg` (598×360)
- Crop: `220×285+15+30`
- Output: `cohorts/2026/01-intro/images/01-what-is-ml-07-suggest-price-imagegen-pilot.png` (1536×1024)
- Prompt iteration: 1
- Prompt focus: crisp educational car-ad form with the stick figure, exact labels `Describe in detail`, `Photo`, `Price`, `Required field`, and `UAH`, plus a filled price marked `Suggested by model`.
- Validation: passed visual inspection. The form concept and teaching point are preserved, the required labels are readable, and the stick figure remains a neutral lesson illustration. No presenter, face, camera tile, browser/Zoom chrome, recording controls, cursor, watermark, black bars, or screenshot artifacts remain.

## Limitations

The generated raster illustrations are faithful educational redraws, not pixel-preserving restorations. The original source images remain available for comparison, and lesson Markdown was intentionally not edited in this pilot.
