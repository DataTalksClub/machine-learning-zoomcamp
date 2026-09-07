# ML Zoomcamp regression screenshot rollout: lessons 05–08

## 05 — simple regression, screenshot 01

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-01-one-car-one-price.jpg`.
- Disposition: `replace` via built-in imagegen; the source is a bounded educational chalkboard diagram showing that a model maps a car to its price.
- Crop coordinates: source `598x360`; deterministic preparation crop `470x340+25+0` (`x=25, y=0, width=470, height=340`). This removes the presenter webcam tile, right black bar, top-left recording marker, and bottom recording controls before generation.
- Invariants: preserve the formula `g(x_i) ≈ y_i`, the blue arrows and their directions, the labels `A CAR` and `ITS PRICE`, and the visible lower vector formula beginning `x_i = (x_i1` with the same instructional relationship and layout.
- Path: built-in imagegen edit from the inspected crop; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-01-one-car-one-price-imagegen-pilot.png`; original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely; one generation iteration was accepted. No rejected variant was staged.
- QA: final `1474x1067` PNG inspected visually; formula, labels, arrows, pale background, and relationship remain readable; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border remains. Markdown reference resolves and `git diff --check` passes before commit.
