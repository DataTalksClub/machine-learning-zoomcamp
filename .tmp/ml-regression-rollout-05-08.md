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

## 05 — simple regression, screenshot 05

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-05-implementation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; notebook code and the handwritten summation are exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `532x220+17+100` (`x=17, y=100, width=532, height=220`). This removes browser chrome, the presenter webcam tile, the right black bar, and the lower output fragment while retaining the feature vector, weight setup, complete `linear_regression` function, and annotated sum.
- Invariants: preserve `xi = [453, 11, 86]`, `w0 = 0`, `w = [1, 1, 1]`, the exact loop and `return pred`, plus the visible annotated `w_0 + \sum w_j·x_{ij}` relationship.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-05-implementation-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code and mathematical notation are the source of truth. An initial narrow crop clipped the right side of the annotated formula; the accepted `width=532` crop restores it.
- QA: final `1064x440` PNG inspected visually; code, values, formula, and annotation remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 06

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-06-weights-interpretation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the exact numeric prediction expression is source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `532x130+17+55` (`x=17, y=55, width=532, height=130`). This keeps the equation and removes the recording marker, webcam tile, right black bar, selected annotation box, bottom editor controls, and other blank canvas.
- Invariants: preserve `7.17 + 453·0.01 + 11·0.04 + 86·0.002 =` exactly, including decimal points, multiplication dots, and the terminal equals sign.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-06-weights-interpretation-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because guessing numeric values would be unsafe; one deterministic crop was accepted after visual inspection.
- QA: final `1064x260` PNG inspected visually; the full expression is crisp and readable with no face, camera tile, browser/Zoom chrome, cursor, watermark, selection box, editor controls, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 07

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-07-prediction-undo-log.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact notebook commands, values, and outputs are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x200+15+70` (`x=15, y=70, width=480, height=200`). This removes browser chrome, the presenter webcam tile, the right black bar, the clipped preceding function line, the lower lesson heading, and the empty notebook cell.
- Invariants: preserve `xi = [453, 11, 86]`, `w0 = 7.17`, `w = [0.01, 0.04, 0.002]`, `linear_regression(xi)`, output `12.312`, `np.log(12.312)`, `g(xi)`, and output `10000`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-07-prediction-undo-log-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact notebook content and numeric outputs must not be guessed. A first crop retained a clipped `return pred` fragment and an empty cell; the accepted crop starts at `y=70` and ends at `y=270`.
- QA: final `960x400` PNG inspected visually; all commands, values, and outputs remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, clipped source fragment, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 01

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-01-g-x-approx-y.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; this bounded chalkboard diagram contains the exact lesson notation and labels, so the source pixels were retained rather than guessed with imagegen.
- Crop coordinates: source `598x360`; `415x340+90+0` (`x=90, y=0, width=415, height=340`). This removes the recording marker, presenter webcam tile, right black bar, bottom controls, and the cursor in the blank left margin.
- Invariants: preserve `g(X) ≈ y`, the arrows and labels `model`, `feature matrix (TRAIN)`, `target`, `PRICE`, and `LINEAR REGRESSION`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-01-g-x-approx-y-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because the equation, labels, and arrow relationships are exact instructional content. Two crop adjustments removed the cursor while keeping `LINEAR REGRESSION` uncropped.
- QA: final `830x680` PNG inspected visually; formula, labels, arrows, and relationships remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 02

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-02-dot-product-notation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the exact handwritten formulas are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x300+50+20` (`x=50, y=20, width=450, height=300`). This removes the recording marker, presenter webcam tile, right black bar, bottom controls, and unused frame edges while preserving both formula lines and the blue summation box.
- Invariants: preserve `g(x_i) = w_0 + \sum_{j=1}^{n} x_{ij}·w_j` and the equivalent `= w_0 + x_i^T w`, including all limits, subscripts, superscript `T`, and equality signs.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-02-dot-product-notation-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact mathematical notation is the source of truth; one crop was accepted after visual inspection.
- QA: final `900x600` PNG inspected visually; both equations and the explanatory blue box are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 03

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-03-dot-function.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact Python code is source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x170+15+65` (`x=15, y=65, width=480, height=170`). This removes browser chrome, the lesson headings, presenter webcam tile, right black bar, cursor/controls, and the selected next cell while retaining the complete `dot` and simplified `linear_regression` functions.
- Invariants: preserve the exact definitions, loop bounds, `res = res + xi[j] * w[j]`, `return res`, and `return w0 + dot(xi, w)` lines.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-03-dot-function-cropped.png`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code must not be guessed. A wider candidate was rejected because it retained the selected green-bordered next cell; the accepted crop ends before it.
- QA: final `960x340` PNG inspected visually; both functions and all code tokens remain crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.
