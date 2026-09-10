# ML Zoomcamp intro imagegen pilot: assets 06–07

## Method

- Used the built-in `image_gen` tool with each local screenshot as a cropped reference.
- Inspected both original screenshots first with `view_image`.
- Cropped the instructional content deterministically before generation so the presenter tile, recording/browser overlays, cursor, and black side chrome were not supplied as reference content.
- Kept the original JPEGs unchanged and saved versioned PNG siblings for review.

## Asset 06: using a model

- Source: `cohorts/2026/01-intro/images/01-what-is-ml-06-using-model.jpg` (598×360)
- Crop: `500×255+25+82`
- Output: `cohorts/2026/01-intro/images/01-what-is-ml-06-using-model-imagegen-pilot.jpg` (1692×930)
- Prompt iteration: 2 total; the first pilot was rejected because it changed the faded Target values. The second was a targeted follow-up using the same deterministic crop.
- Prompt focus: crisp scientific-educational diagram with exact invariants: faded Target values `$1.1k`, `$0.6k`, `$23k`, `...`; Predictions values `$1.5k`, `$0.4k`, `$20k`, `...`; feature rows `1995/GAZ/200.000`, `1980/VAZ/100.000`, and `2016/BWM/5.000`.
- Validation: passed visual inspection after correction. Every required label and numeric value is readable and exact; the feature-to-target-to-model-to-predictions relationship is preserved. No extra numeric values, presenter, face, camera tile, browser/Zoom chrome, recording controls, cursor, watermark, black bars, or screenshot artifacts remain.

## Asset 07: suggest price

- Source: `cohorts/2026/01-intro/images/01-what-is-ml-07-suggest-price.jpg` (598×360)
- Crop: `220×285+15+30`
- Output: `cohorts/2026/01-intro/images/01-what-is-ml-07-suggest-price-imagegen-pilot.jpg` (1536×1024)
- Prompt iteration: 2 total; the first pilot was rejected because it changed the source text to `Toyota Prius`.
- Prompt focus: crisp educational car-ad form with the stick figure, exact source text `Toyota Hilux, almost new`, required labels `Describe in detail`, `Photo`, `Price`, `Required field`, and `UAH`, plus an allowed model-filled suggested price.
- Validation: passed visual inspection after correction. The form concept and teaching point are preserved, the required labels and `Toyota Hilux, almost new` are readable and exact, and the stick figure remains a neutral lesson illustration. No presenter, face, camera tile, browser/Zoom chrome, recording controls, cursor, watermark, black bars, screenshot artifacts, or unrelated UI remain.

## Limitations

The generated raster illustrations are faithful educational redraws, not pixel-preserving restorations. Commit `c84e26b` is superseded by the follow-up commit because its 06 Target values and 07 car-model text failed QA. The original source images remain available for comparison, and lesson Markdown was intentionally not edited in this pilot.
