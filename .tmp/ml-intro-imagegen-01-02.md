# ML intro imagegen pilot: assets 01–02

## Scope

Regenerated only these two versioned siblings; the original JPEG screenshots were not modified and lesson Markdown was not edited:

- `cohorts/2026/01-intro/images/01-what-is-ml-01-price-field-imagegen-pilot.jpg`
- `cohorts/2026/01-intro/images/01-what-is-ml-02-known-about-cars-imagegen-pilot.jpg`

Used the built-in `image_gen` tool with the cropped image as the reference/edit target. No CLI fallback was used.

## Deterministic crops

Both source files are 598×360 JPEG screenshots.

- Price form: `x=105, y=125, width=390, height=145` → `/tmp/ml-intro-imagegen-01-02/price-crop.png`. This keeps the seller icon and form while excluding the top attribution, webcam tile, recording control, cursor, and black right chrome.
- Car table: `x=15, y=35, width=480, height=275` → `/tmp/ml-intro-imagegen-01-02/cars-crop.png`. This keeps the title, thumbnails, feature grid, and price values while stopping before the webcam artifact at the right edge and excluding the screenshot border/controls.

Crop command used:

```bash
convert <source> -crop <width>x<height>+<x>+<y> +repage <crop>
```

## Generation prompts and iterations

### Price form

One generation iteration. Prompt requirements: recreate the cropped reference as a crisp scientific-educational raster illustration; preserve the seller icon and form hierarchy; render the exact text `Price`, `Exchange`, `Price`, `Required field`, and `UAH`; use a clean white layout; and avoid faces, camera feeds, browser/recording UI, watermark, cursor, social handles, black bars, and extra labels.

Output: 1816×866 PNG. Visual QA passed.

### Known-about-cars table

One generation iteration. Prompt requirements: recreate the cropped reference as a crisp educational table; render the exact title `What do we know about cars?`, header `Year`, years `1995`, `1980`, `2016`, separate rightmost header `Price`, and prices `$1.1k`, `$0.6k`, `$23k`; keep three rows, paired year/price values, and mostly blank feature cells; and avoid faces, camera feeds, browser/recording UI, watermark, cursor, black bars, extra labels, extra rows, invented values, or conclusions.

Output: 1659×948 PNG. Visual QA passed.

## Validation

- Opened both final PNGs with `view_image` at high detail.
- Confirmed all required labels and numeric values are readable and exact.
- Confirmed the price form still communicates a required UAH price field.
- Confirmed the car table preserves the three year/price pairings and separate Price column.
- Confirmed no webcam tile, face, browser chrome, recording controls, cursor, watermark, social handles, or black side bars remain.
- Confirmed only the two requested image outputs and this report are in the focused commit; no lesson Markdown or source JPEG was changed.
