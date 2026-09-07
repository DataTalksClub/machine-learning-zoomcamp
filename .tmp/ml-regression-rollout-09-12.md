# ML Zoomcamp regression screenshot rollout: lessons 09–12

Scope: every Markdown image reference in `09-rmse.md`,
`10-car-price-validation.md`, `11-feature-engineering.md`, and
`12-categorical-variables.md`.

Rubric order is instructional contribution / relevance / readability and focus /
complementarity / durability / caption and accessibility, scored 0–2 each.
Imagegen was available and read completely. It is reserved for bounded
explanatory illustrations; exact formulas, code, plots, numbers, notebook
outputs, and UI are handled deterministically.

## 09 — RMSE

### Screenshot 01 — RMSE formula

- Source: `cohorts/2026/02-regression/images/09-rmse-01-rmse-formula.jpg`.
- Caption/context: “Writing the RMSE formula”; the surrounding text introduces the formula and the first `rmse` function cell.
- Rubric: `1 / 2 / 2 / 1 / 2 / 2 = 10/12`; keep because the handwritten formula connects the metric to the implementation, while the plot and code provide useful notebook context.
- Disposition: `crop/replace` via deterministic raster export; formula and code are exact instructional content, so imagegen was not used.
- Crop: source `598x360`; `565x288+16+72`, then 2× Lanczos resize and light unsharp masking. This removes the browser header, webcam tile, recording marker, black frame edges, and controls while keeping the plot, formula, code cell, and section context.
- Invariants/QA: preserve the full `sqrt(1/m Σ(g(x_i)-y_i)^2)` notation, `def rmse(y, y_pred):`, and visible notebook context. Final `1130x576` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-01-rmse-formula-cropped.png`.

### Screenshot 02 — predictions and actual prices

- Source: `cohorts/2026/02-regression/images/09-rmse-02-predictions-vs-actual-prices.jpg`.
- Caption/context: “Predictions and actual values as two arrays”; the lesson introduces the four paired predictions and target prices before taking their differences.
- Rubric: `2 / 2 / 2 / 2 / 2 / 2 = 12/12`; keep because the aligned arrays make the pairing that drives every later error calculation immediately visible.
- Disposition: `crop/replace` via deterministic raster export; the exact values and handwritten notation are the source of truth, so imagegen was not used.
- Crop: source `598x360`; `482x343+23+0`, then 2× Lanczos resize and light unsharp masking. This removes the recording marker, webcam tile, black side frame, and bottom controls while retaining the complete diagram.
- Invariants/QA: preserve `g(x_i)-y_i`, `PRED`, `PRICE`, `y-pred`, `y-train`, values `10, 9, 11, …, 10` and `9, 9, 10.5, …, 11.5`, and their row alignment. Final `964x686` PNG inspected with no face, camera tile, browser/Zoom chrome, cursor, watermark, or black border; Markdown reference resolves and `git diff --check` passes before commit.
- Final: `cohorts/2026/02-regression/images/09-rmse-02-predictions-vs-actual-prices-cropped.png`.
