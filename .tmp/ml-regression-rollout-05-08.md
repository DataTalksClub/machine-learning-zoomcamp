# ML Zoomcamp regression screenshot rollout: lessons 05–08

## 05 — simple regression, screenshot 01

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-01-one-car-one-price.jpg`.
- Disposition: `replace` via built-in imagegen; the source is a bounded educational chalkboard diagram showing that a model maps a car to its price.
- Crop coordinates: source `598x360`; deterministic preparation crop `470x340+25+0` (`x=25, y=0, width=470, height=340`). This removes the presenter webcam tile, right black bar, top-left recording marker, and bottom recording controls before generation.
- Invariants: preserve the formula `g(x_i) ≈ y_i`, the blue arrows and their directions, the labels `A CAR` and `ITS PRICE`, and the visible lower vector formula beginning `x_i = (x_i1` with the same instructional relationship and layout.
- Path: built-in imagegen edit from the inspected crop; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-01-one-car-one-price-imagegen-pilot.png`; original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely; one generation iteration was accepted. No rejected variant was staged.
- QA: final `1474x1067` PNG inspected visually; formula, labels, arrows, pale background, and relationship remain readable; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border remains. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 02

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-02-car-10-features.jpg`.
- Disposition: `crop/replace` via deterministic raster export; this is an exact notebook/table screenshot whose car feature values must remain unchanged.
- Crop coordinates: source `598x360`; `485x235+15+70` (`x=15, y=70, width=485, height=235`). The crop removes browser chrome, the presenter webcam tile, the right black bar, the lower lesson heading, and recording-frame material.
- Invariants: preserve `df_train.iloc[10]`, the Rolls-Royce Phantom Drophead Coupe row, year `2015`, `engine_hp` `453.0`, `city_mpg` `11`, `popularity` `86`, every visible feature label/value, row order, and table relationships.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-02-car-10-features-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact notebook UI and numeric values are the source of truth; one crop correction removed a clipped heading fragment before acceptance.
- QA: final `970x470` PNG inspected visually; exact code, labels, values, and table ordering remain readable; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 03

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-03-regression-formula.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the handwritten vector and regression formula are exact instructional content, so imagegen was not used.
- Crop coordinates: source `598x360`; content crop `532x340+17+0` (`x=17, y=0, width=532, height=340`) assembled from a clean top strip (`488x55+17+0`) plus a lower strip (`532x285+17+55`), with the top-right webcam area replaced by the adjacent blank board strip (`44x55+460+0`). This removes the recording marker, webcam tile, right black bar, and bottom controls while retaining the full formula.
- Invariants: preserve `x_i = [453, 11, 86]`, `i=10`, `g(x_i) ≈ y_i`, and the complete lower expression `g(x_i) = w_0 + w_1·x_i1 + w_2·x_i2 + w_3·x_i3`.
- Path: deterministic crop/composite followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-03-regression-formula-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact handwritten formula content is the source of truth. An initial single rectangle was rejected because it clipped the lower formula; the accepted stepped crop restored the complete expression without the webcam tile.
- QA: final `1064x680` PNG inspected visually; all numeric values, symbols, and formula terms remain readable, with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 04

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-04-sum-notation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the summation notation is exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x170+30+135` (`x=30, y=135, width=450, height=170`). This focuses on the clean lower equation and removes the recorder marker, webcam tile, partially covered upper expansion, black bar, and recording controls.
- Invariants: preserve the complete equation `g(x_i) = w_0 + \sum_{j=1}^{3} w_j · x_{ij}`, including the upper limit `3`, lower limit `j=1`, all subscripts, and the plus sign.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-04-sum-notation-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact mathematical notation is the source of truth. One tighter candidate was rejected because it retained a clipped blue fragment from the upper formula; the accepted crop starts at `y=135`.
- QA: final `900x340` PNG inspected visually; the full summation equation is crisp and centered with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, clipped source fragment, or black border. Markdown reference resolves and `git diff --check` passes before commit.
