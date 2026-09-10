# ML Zoomcamp intro imagegen pilot: assets 03–05

## Scope

Regenerated the three blurry screenshot illustrations for the 2026 Intro lesson as versioned sibling PNGs. The original JPEGs and lesson Markdown were left unchanged.

The built-in `image_gen` tool was used. Each source was inspected first, cropped deterministically to the meaningful lesson content, and supplied as the reference image. The prompts explicitly required removal of webcam/face tiles, browser and recording overlays, cursors, watermarks, black bars, and screenshot margins.

## Crops

All source screenshots are 598×360 pixels. Crop coordinates use ImageMagick geometry `WIDTHxHEIGHT+X+Y`:

| Asset | Crop | Input crop |
| --- | --- | --- |
| Expert or model | `500x240+40+80` | `/tmp/ml-intro-imagegen-03-05/expert-or-model-crop.png` |
| Features and target | `550x285+15+35` | `/tmp/ml-intro-imagegen-03-05/features-target-crop.png` |
| Model training | `490x275+15+30` | `/tmp/ml-intro-imagegen-03-05/model-training-crop.png` |

The right edge of the features/target and model-training crops intersects the original screenshot overlay because the overlay overlaps the source content boundary. The generation prompts explicitly required its removal; the generated outputs contain no overlay remnants.

## Generation and validation

Each asset required one imagegen prompt and one accepted generation. Outputs were inspected at high detail after generation.

- `01-what-is-ml-03-expert-or-model-imagegen-pilot.jpg` — 1672×941. Both DATA→expert/person→PATTERNS and DATA→ML→PATTERNS rows are present, arrows point right, and the caption `If an expert can, so can a model!` is legible. The person is a neutral educational symbol, not a webcam portrait.
- `01-what-is-ml-04-features-target-imagegen-pilot.jpg` — 1690×931. The feature table preserves `1995 / GAZ / 200.000`, `1980 / VAZ / 100.000`, and `2016 / BWM / 5.000`; the separate Price column preserves `$1.1k`, `$0.6k`, and `$23k`. `Features`, `what we know about cars`, `Target`, and `what we want to predict` are legible.
- `01-what-is-ml-05-model-training-imagegen-pilot.jpg` — 1536×1024. The exact title `Model training`, feature table, Price column, two inputs into `ML`, and one `ML`→`Model` output are present and readable.

No output contains a face/camera tile, browser or recording controls, cursor, watermark, black side chrome, or other screenshot overlay. No source JPEG or lesson Markdown was modified.

## Limitations

These are regenerated raster illustrations, not pixel-preserving edits. Car thumbnails were redrawn as clean neutral illustrations, and the expert symbol was redrawn as a simple neutral worker icon. The exact instructional labels, values, layout relationships, and arrows were preserved; visual details inside the thumbnails are illustrative.
