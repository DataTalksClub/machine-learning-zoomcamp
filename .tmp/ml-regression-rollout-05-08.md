# ML Zoomcamp regression screenshot rollout: lessons 05–08

## 05 — simple regression, screenshot 01

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-01-one-car-one-price.jpg`.
- Disposition: `replace` via built-in imagegen; the source is a bounded educational chalkboard diagram showing that a model maps a car to its price.
- Crop coordinates: source `598x360`; deterministic preparation crop `470x340+25+0` (`x=25, y=0, width=470, height=340`). This removes the presenter webcam tile, right black bar, top-left recording marker, and bottom recording controls before generation.
- Invariants: preserve the formula `g(x_i) ≈ y_i`, the blue arrows and their directions, the labels `A CAR` and `ITS PRICE`, and the visible lower vector formula beginning `x_i = (x_i1` with the same instructional relationship and layout.
- Path: built-in imagegen edit from the inspected crop; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-01-one-car-one-price-imagegen-pilot.jpg`; original JPG preserved.
- Iteration/capability: imagegen skill was available and read completely; one generation iteration was accepted. No rejected variant was staged.
- QA: final `1474x1067` PNG inspected visually; formula, labels, arrows, pale background, and relationship remain readable; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border remains. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 02

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-02-car-10-features.jpg`.
- Disposition: `crop/replace` via deterministic raster export; this is an exact notebook/table screenshot whose car feature values must remain unchanged.
- Crop coordinates: source `598x360`; `485x235+15+70` (`x=15, y=70, width=485, height=235`). The crop removes browser chrome, the presenter webcam tile, the right black bar, the lower lesson heading, and recording-frame material.
- Invariants: preserve `df_train.iloc[10]`, the Rolls-Royce Phantom Drophead Coupe row, year `2015`, `engine_hp` `453.0`, `city_mpg` `11`, `popularity` `86`, every visible feature label/value, row order, and table relationships.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-02-car-10-features-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact notebook UI and numeric values are the source of truth; one crop correction removed a clipped heading fragment before acceptance.
- QA: final `970x470` PNG inspected visually; exact code, labels, values, and table ordering remain readable; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar remains. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 03

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-03-regression-formula.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the handwritten vector and regression formula are exact instructional content, so imagegen was not used.
- Crop coordinates: source `598x360`; content crop `532x340+17+0` (`x=17, y=0, width=532, height=340`) assembled from a clean top strip (`488x55+17+0`) plus a lower strip (`532x285+17+55`), with the top-right webcam area replaced by the adjacent blank board strip (`44x55+460+0`). This removes the recording marker, webcam tile, right black bar, and bottom controls while retaining the full formula.
- Invariants: preserve `x_i = [453, 11, 86]`, `i=10`, `g(x_i) ≈ y_i`, and the complete lower expression `g(x_i) = w_0 + w_1·x_i1 + w_2·x_i2 + w_3·x_i3`.
- Path: deterministic crop/composite followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-03-regression-formula-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact handwritten formula content is the source of truth. An initial single rectangle was rejected because it clipped the lower formula; the accepted stepped crop restored the complete expression without the webcam tile.
- QA: final `1064x680` PNG inspected visually; all numeric values, symbols, and formula terms remain readable, with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 04

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-04-sum-notation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the summation notation is exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x170+30+135` (`x=30, y=135, width=450, height=170`). This focuses on the clean lower equation and removes the recorder marker, webcam tile, partially covered upper expansion, black bar, and recording controls.
- Invariants: preserve the complete equation `g(x_i) = w_0 + \sum_{j=1}^{3} w_j · x_{ij}`, including the upper limit `3`, lower limit `j=1`, all subscripts, and the plus sign.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-04-sum-notation-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact mathematical notation is the source of truth. One tighter candidate was rejected because it retained a clipped blue fragment from the upper formula; the accepted crop starts at `y=135`.
- QA: final `900x340` PNG inspected visually; the full summation equation is crisp and centered with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, clipped source fragment, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 05

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-05-implementation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; notebook code and the handwritten summation are exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `532x220+17+100` (`x=17, y=100, width=532, height=220`). This removes browser chrome, the presenter webcam tile, the right black bar, and the lower output fragment while retaining the feature vector, weight setup, complete `linear_regression` function, and annotated sum.
- Invariants: preserve `xi = [453, 11, 86]`, `w0 = 0`, `w = [1, 1, 1]`, the exact loop and `return pred`, plus the visible annotated `w_0 + \sum w_j·x_{ij}` relationship.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-05-implementation-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code and mathematical notation are the source of truth. An initial narrow crop clipped the right side of the annotated formula; the accepted `width=532` crop restores it.
- QA: final `1064x440` PNG inspected visually; code, values, formula, and annotation remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 06

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-06-weights-interpretation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the exact numeric prediction expression is source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `532x130+17+55` (`x=17, y=55, width=532, height=130`). This keeps the equation and removes the recording marker, webcam tile, right black bar, selected annotation box, bottom editor controls, and other blank canvas.
- Invariants: preserve `7.17 + 453·0.01 + 11·0.04 + 86·0.002 =` exactly, including decimal points, multiplication dots, and the terminal equals sign.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-06-weights-interpretation-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because guessing numeric values would be unsafe; one deterministic crop was accepted after visual inspection.
- QA: final `1064x260` PNG inspected visually; the full expression is crisp and readable with no face, camera tile, browser/Zoom chrome, cursor, watermark, selection box, editor controls, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 05 — simple regression, screenshot 07

- Source: `cohorts/2026/02-regression/images/05-linear-regression-simple-07-prediction-undo-log.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact notebook commands, values, and outputs are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x200+15+70` (`x=15, y=70, width=480, height=200`). This removes browser chrome, the presenter webcam tile, the right black bar, the clipped preceding function line, the lower lesson heading, and the empty notebook cell.
- Invariants: preserve `xi = [453, 11, 86]`, `w0 = 7.17`, `w = [0.01, 0.04, 0.002]`, `linear_regression(xi)`, output `12.312`, `np.log(12.312)`, `g(xi)`, and output `10000`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/05-linear-regression-simple-07-prediction-undo-log-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact notebook content and numeric outputs must not be guessed. A first crop retained a clipped `return pred` fragment and an empty cell; the accepted crop starts at `y=70` and ends at `y=270`.
- QA: final `960x400` PNG inspected visually; all commands, values, and outputs remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, clipped source fragment, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 01

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-01-g-x-approx-y.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; this bounded chalkboard diagram contains the exact lesson notation and labels, so the source pixels were retained rather than guessed with imagegen.
- Crop coordinates: source `598x360`; `415x340+90+0` (`x=90, y=0, width=415, height=340`). This removes the recording marker, presenter webcam tile, right black bar, bottom controls, and the cursor in the blank left margin.
- Invariants: preserve `g(X) ≈ y`, the arrows and labels `model`, `feature matrix (TRAIN)`, `target`, `PRICE`, and `LINEAR REGRESSION`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-01-g-x-approx-y-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because the equation, labels, and arrow relationships are exact instructional content. Two crop adjustments removed the cursor while keeping `LINEAR REGRESSION` uncropped.
- QA: final `830x680` PNG inspected visually; formula, labels, arrows, and relationships remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 02

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-02-dot-product-notation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the exact handwritten formulas are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x300+50+20` (`x=50, y=20, width=450, height=300`). This removes the recording marker, presenter webcam tile, right black bar, bottom controls, and unused frame edges while preserving both formula lines and the blue summation box.
- Invariants: preserve `g(x_i) = w_0 + \sum_{j=1}^{n} x_{ij}·w_j` and the equivalent `= w_0 + x_i^T w`, including all limits, subscripts, superscript `T`, and equality signs.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-02-dot-product-notation-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact mathematical notation is the source of truth; one crop was accepted after visual inspection.
- QA: final `900x600` PNG inspected visually; both equations and the explanatory blue box are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 03

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-03-dot-function.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact Python code is source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x170+15+65` (`x=15, y=65, width=480, height=170`). This removes browser chrome, the lesson headings, presenter webcam tile, right black bar, cursor/controls, and the selected next cell while retaining the complete `dot` and simplified `linear_regression` functions.
- Invariants: preserve the exact definitions, loop bounds, `res = res + xi[j] * w[j]`, `return res`, and `return w0 + dot(xi, w)` lines.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-03-dot-function-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code must not be guessed. A wider candidate was rejected because it retained the selected green-bordered next cell; the accepted crop ends before it.
- QA: final `960x340` PNG inspected visually; both functions and all code tokens remain crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 04

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-04-fake-feature.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the handwritten vectors and added `1` are exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x300+50+20` (`x=50, y=20, width=450, height=300`). This removes the recording marker, presenter webcam tile, the partially covered dimension note, right black bar, and bottom controls while preserving both vectors and the dot-product line.
- Invariants: preserve `w = [w_0, w_1, w_2, …, w_n]`, `x_i = [1, x_{i1}, x_{i2}, …, x_{in}]` with the blue added `1`, and `w^T x_i = x_i^T w`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-04-fake-feature-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact vector notation is the source of truth. Two crop widths were tested; the accepted `width=450` keeps the closing feature-vector bracket complete and excludes a stray edge artifact.
- QA: final `900x600` PNG inspected visually; vectors, indices, added `1`, transpose marks, and equality are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 05

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-05-prepend-one.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact notebook code and numeric output are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; primary code crop `480x125+15+120` (`x=15, y=120, width=480, height=125`) plus the selected-cell code crop `360x50+125+251` (`x=125, y=251, width=360, height=50`) aligned below it. This removes browser chrome, presenter webcam tile, lesson heading, green selected-cell border, cursor, and other UI frame material.
- Invariants: preserve the simplified `linear_regression` cell, `w_new = [w0] + w`, displayed vector `[7.17, 0.01, 0.04, 0.002]`, and the exact fictional-feature implementation `xi = [1] + xi; return dot(xi, w)`.
- Path: deterministic crop/composite followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-05-prepend-one-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code and values must not be guessed. A simple rectangle retained a green selected-cell border and clipped preceding code; the accepted two-region export removes those artifacts while preserving both code sections.
- QA: final `960x350` PNG inspected visually; all code tokens and values are crisp, with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 06

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-06-matrix-vector-multiplication.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the matrix/vector symbols and row structure are exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `470x300+35+0` (`x=35, y=0, width=470, height=300`). This removes the recording marker, presenter webcam tile, right black bar, bottom controls, and left frame edge while preserving `X`, the matrix rows beginning with `1`, and the weight vector.
- Invariants: preserve the `X` label and `m×(n+1)` annotation, matrix entries `1`, `x_{i1}`, `x_{i2}`, `…`, `x_{in}`, row labels/ellipsis, and weight vector entries `w_0`, `w_1`, `…`, `w_n`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-06-matrix-vector-multiplication-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact matrix notation is the source of truth. A wider crop retained a black frame edge; the accepted crop starts at `x=35` while keeping the row labels visible.
- QA: final `940x600` PNG inspected visually; matrix and weight vector are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black frame edge. Markdown reference resolves and `git diff --check` passes before commit.

## 06 — vector form, screenshot 07

- Source: `cohorts/2026/02-regression/images/06-linear-regression-vector-07-x-dot-w-new.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact matrix code, values, and predictions are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; matrix/output crop `480x150+15+90` (`x=15, y=90, width=480, height=150`) plus selected-cell code/output crop `360x53+125+252` (`x=125, y=252, width=360, height=53`) aligned below it. This removes browser chrome, presenter webcam tile, lesson heading, selected-cell border, right black bar, and frame controls.
- Invariants: preserve `x1`, `x2`, `x10`, the matrix construction `X = [x1, x2, x10]; X = np.array(X)`, the displayed matrix values, `def linear_regression(X): return X.dot(w_new)`, and `array([12.38, 13.552, 12.312])`.
- Path: deterministic crop/composite followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/06-linear-regression-vector-07-x-dot-w-new-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code, matrix values, and predictions must not be guessed. A single crop retained the selected green border and clipped preceding code; the accepted two-region export removes the border and keeps all required matrix/prediction content.
- QA: final `960x406` PNG inspected visually; code, matrix, and prediction array remain crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 01

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-01-inverse-solution.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the handwritten inverse derivation is exact lesson content, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x300+50+20` (`x=50, y=20, width=450, height=300`). This removes the recording marker, presenter webcam tile, right black bar, and bottom controls; a tiny cursor in blank board space was removed with a matching board-color patch.
- Invariants: preserve the crossed inverse-matrix cancellation, boxed `w`, identity `I`, `X⁻¹y`, and the final `w = X⁻¹y` relationship.
- Path: deterministic crop plus blank-space cursor cleanup followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-01-inverse-solution-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact mathematical notation and the instructor’s derivation are source of truth; one cursor-cleanup pass was accepted without touching diagram strokes.
- QA: final `900x600` PNG inspected visually; derivation remains crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 02

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-02-gram-matrix.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact normal-equation notation and dimensions are source of truth, so imagegen was not used.
- Crop coordinates: formula crop `300x170+200+45` (`x=200, y=45, width=300, height=170`) with blank-space cleanup for the crossed-out material/cursor, plus dimension-label crop `360x120+80+180` (`x=80, y=180, width=360, height=120`), vertically composed with a clean board gap. This removes the webcam, recording marker, black bar, controls, crossed-out clutter, and cursor while preserving the normal equation and `GRAM MATRIX (n+1)×(n+1)` label.
- Invariants: preserve `w = (XᵀX)⁻¹Xᵀy` and the complete `GRAM MATRIX (n+1)×(n+1)` annotation.
- Path: deterministic crop/composite with matching board-color cleanup followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-02-gram-matrix-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact formula symbols and dimensions must not be guessed. A broad crop retained partially clipped crossed-out material and a cursor; the accepted focused/composed crop removes them and restores a clean equation/label presentation.
- QA: final `720x610` PNG inspected visually; equation and dimensions are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, crossed-out clutter, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 03

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-03-normal-equation.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact normal-equation notation is source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `465x280+35+20` (`x=35, y=20, width=465, height=280`). This removes the recording marker, presenter webcam tile, right black bar, left frame edge, and bottom controls while preserving the main equation and `Iw = w` identity line.
- Invariants: preserve `w = (XᵀX)⁻¹Xᵀy`, the underlined `w`, and the identity simplification `Iw = w`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-03-normal-equation-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact formula symbols are the source of truth; one crop was accepted after visual inspection.
- QA: final `930x560` PNG inspected visually; equation and identity remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 04

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-04-gram-matrix-code.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact matrix values, code, and annotated formula are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `550x155+15+85` (`x=15, y=85, width=550, height=155`). This removes browser chrome, presenter webcam tile, right black bar, lesson headings, and bottom controls while preserving the matrix output, `w = (XᵀX)⁻¹Xᵀy`, and `XTX = X.T.dot(X)`.
- Invariants: preserve all nine matrix rows and their values, the exact `XTX` code, and the complete annotated normal-equation formula.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-04-gram-matrix-code-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact numeric matrix/code content must not be guessed. Narrow candidates clipped the right-hand `y`; the accepted width restores it while ending before the lower heading.
- QA: final `1100x310` PNG inspected visually; matrix values, code, and formula are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, heading overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 05

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-05-inverse-check.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact NumPy code, identity output, and annotated equation are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `550x155+15+100` (`x=15, y=100, width=550, height=155`). A white notebook-background cleanup removes the clipped preceding matrix fragment from the top-left strip. The crop removes browser chrome, presenter webcam tile, the lower lesson headings, right black bar, and controls.
- Invariants: preserve `XTX = X.T.dot(X)`, `XTX_inv = np.linalg.inv(XTX)`, `XTX.dot(XTX_inv).round(1)`, the complete identity array, and `w = (XᵀX)⁻¹Xᵀy`.
- Path: deterministic crop with blank-space cleanup followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-05-inverse-check-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code, floating-point output, and formula are source of truth. A first crop clipped the identity output and retained a previous-cell fragment; the accepted crop starts earlier and masks only the blank top-left fragment.
- QA: final `1100x310` PNG inspected visually; code, identity matrix, and equation remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, clipped source fragment, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 06

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-06-ones-column-stack.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact Python code and target values are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; setup crop `480x70+15+165` (`x=15, y=165, width=480, height=70`), plus code-line crops `365x18+125+246` and `365x18+125+276`, aligned below with clean notebook gaps. This removes browser chrome, presenter webcam tile, the selected-cell green border, lesson headings, right black bar, and controls.
- Invariants: preserve `ones = np.ones(X.shape[0])`, the nine-element ones output, `np.column_stack()`, and `y = [100, 200, 150, 250, 100, 200, 150, 250, 120]` exactly.
- Path: deterministic crop/composite followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-06-ones-column-stack-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code and numeric targets must not be guessed. A single crop retained a green selected-cell border; the accepted multi-region export removes it while keeping both code lines.
- QA: final `960x252` PNG inspected visually; setup, ones output, `column_stack`, and target vector remain crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 07 — normal equation, screenshot 07

- Source: `cohorts/2026/02-regression/images/07-linear-regression-training-07-train-function.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact NumPy assignments and floating-point output are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `550x90+15+55` (`x=15, y=55, width=550, height=90`). This focuses on the split-weight cells, removes browser chrome, presenter webcam tile, selected unfinished function cell, lesson headings, right black bar, and controls, and keeps the full output array.
- Invariants: preserve `w0 = w_full[0]`, `w = w_full[1:]`, `w0, w`, and the complete displayed tuple/weight array values.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/07-linear-regression-training-07-train-function-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact assignments and numeric output must not be guessed; one crop was accepted after widening the right edge to retain the final output value.
- QA: final `1100x180` PNG inspected visually; assignments and all displayed values remain crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 08 — baseline model, screenshot 01

- Source: `cohorts/2026/02-regression/images/08-baseline-model-01-numerical-columns.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the dataframe column names and dtypes are exact notebook output, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x205+50+105` (`x=50, y=105, width=480, height=205`). This focuses on the complete `df_train.columns` output and removes browser chrome, presenter webcam tile, selected-cell border, cursor, right black bar, controls, and the following `base` cell.
- Invariants: preserve every visible column/type pair, including `engine_hp`, `engine_cylinders`, `highway_mpg`, `city_mpg`, `popularity`, and `dtype: object`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/08-baseline-model-01-numerical-columns-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact dataframe output is source of truth. A wider crop retained an incomplete/cursor-obscured input command; the accepted output-only crop keeps the useful complete table and removes that artifact.
- QA: final `960x410` PNG inspected visually; all visible labels and dtypes are crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 08 — baseline model, screenshot 02

- Source: `cohorts/2026/02-regression/images/08-baseline-model-02-base-features.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; exact feature names and code are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x42+15+75` (`x=15, y=75, width=480, height=42`). This keeps the complete two-line `base` assignment and removes browser chrome, presenter webcam tile, previous-cell fragment, selected-cell border/cursor, headings, right black bar, and controls.
- Invariants: preserve `engine_hp`, `engine_cylinders`, `highway_mpg`, `city_mpg`, `popularity`, list punctuation, and line continuation exactly.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/08-baseline-model-02-base-features-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code/token content must not be guessed. A taller crop retained a previous-cell fragment and green border; the accepted crop isolates the code cell.
- QA: final `960x84` PNG inspected visually; all five feature names and syntax remain crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 08 — baseline model, screenshot 03

- Source: `cohorts/2026/02-regression/images/08-baseline-model-03-nan-weights.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the exact failed training call and `nan` output are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x55+50+180` (`x=50, y=180, width=480, height=55`). This isolates the training call/result and removes the prior-cell fragment, browser chrome, presenter webcam tile, lesson headings, selected-cell frame, right black bar, and controls.
- Invariants: preserve `train_linear_regression(X_train, y_train)` and the complete output `(nan, array([nan, nan, nan, nan, nan]))`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/08-baseline-model-03-nan-weights-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact code and failure values must not be guessed; one crop was accepted after removing the preceding `isnull` fragment.
- QA: final `960x110` PNG inspected visually; command and all `nan` values are crisp with no face, camera tile, browser/Zoom chrome, cursor, clipped source fragment, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 08 — baseline model, screenshot 04

- Source: `cohorts/2026/02-regression/images/08-baseline-model-04-fillna-zero.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the filled dataframe values and column labels are exact notebook output, so imagegen was not used.
- Crop coordinates: source `598x360`; `520x160+50+180` (`x=50, y=180, width=520, height=160`). This focuses on the complete output table and removes browser chrome, presenter webcam tile, input cursor, selected-cell frame, right black bar, and surrounding notebook cells.
- Invariants: preserve the headers `engine_hp`, `engine_cylinders`, `highway_mpg`, `city_mpg`, `popularity`, all visible row values, ellipses, and row `7145`.
- Path: deterministic output-table crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/08-baseline-model-04-fillna-zero-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact table values are source of truth. A crop including the input cursor required masking over code; the accepted output-only crop removes that cursor without touching any table value.
- QA: final `1040x320` PNG inspected visually; headers and every visible value are crisp with no face, camera tile, browser/Zoom chrome, cursor, selected-cell border, watermark, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 08 — baseline model, screenshot 05

- Source: `cohorts/2026/02-regression/images/08-baseline-model-05-missing-feature-ignored.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; the exact formula and missing-feature annotation are source of truth, so imagegen was not used.
- Crop coordinates: source `598x360`; `450x300+50+20` (`x=50, y=20, width=450, height=300`). This removes the recording marker, presenter webcam tile, right black bar, and bottom controls while preserving both equation lines and the `missing` annotation.
- Invariants: preserve `g(x_i) = w_0 + x_{i1}·w_1 + x_{i2}·w_2`, the crossed/zeroed missing `x_{i1}` term, the `missing` label, and `= w_0 + x_{i2}·w_2`.
- Path: deterministic crop followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/08-baseline-model-05-missing-feature-ignored-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact formula symbols and annotation are source of truth; one crop was accepted after visual inspection.
- QA: final `900x600` PNG inspected visually; both equations and the missing-feature explanation are crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.

## 08 — baseline model, screenshot 06

- Source: `cohorts/2026/02-regression/images/08-baseline-model-06-prediction-histogram.jpg`.
- Disposition: `crop/replace` via deterministic native raster export; notebook code and the plotted distributions are exact source content, so imagegen was not used.
- Crop coordinates: source `598x360`; `480x310+15+45` (`x=15, y=45, width=480, height=310`). This preserves all three plotting cells, the `Out[90]` line, and the complete histogram while removing browser chrome, presenter webcam tile, right black bar, and surrounding frame material.
- Invariants: preserve the `train_linear_regression`/`y_pred`/`histplot` commands, red-vs-blue distribution, y-axis `Count`, x-axis values, and complete chart extent.
- Path: deterministic crop plus localized `5x5` median cleanup over the cursor coordinates (crop-relative `+224+172`, `28x34`) followed by 2x Lanczos export with light unsharp masking; final sibling `cohorts/2026/02-regression/images/08-baseline-model-06-prediction-histogram-cropped.jpg`; original JPG preserved.
- Iteration/capability: imagegen was not used because exact plotted values and code are source of truth. A plain crop left a white cursor over the bars; a localized median cleanup removed only that small cursor region while retaining the histogram structure.
- QA: final `960x620` PNG inspected visually; code and complete red/blue histogram remain crisp with no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black border. Markdown reference resolves and `git diff --check` passes before commit.
