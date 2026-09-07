# Classification screenshot rollout: lessons 06–09

Scope: every Markdown image reference in `06-mutual-info.md`,
`07-correlation.md`, `08-ohe.md`, and `09-logistic-regression.md`.

Worker capability: `imagegen` skill available; built-in imagegen used only
for the bounded conceptual mutual-information illustration. Exact code,
numeric output, plots, formulas, and teaching diagrams use deterministic
crops. Original sources remain unchanged. Each accepted screenshot gets its
own focused commit; crops and rejected/intermediate files stay under `.tmp/`.

## Accepted assets

### 06-mutual-info.md

- `06-mutual-info-01-mutual-information-wikipedia.jpg` →
  `06-mutual-info-01-mutual-information-wikipedia-imagegen-pilot.png`
  - Disposition: imagegen conceptual replacement.
  - Prep: reference crop `.tmp/ml-classification-rollout-06-09-crops/06-mutual-info-01-reference.png`, coordinates `505x300+0+42`.
  - Invariants: clean overlap diagram; exact labels `X`, `Y`, and `Mutual information`; no people, camera, browser, or extra metrics.

### 07-correlation.md

- `07-correlation-01-correlation-coefficient.jpg` →
  `07-correlation-01-correlation-coefficient-imagegen-pilot.png`
  - Disposition: imagegen bounded explanatory replacement.
  - Prep: inspected/cropped source reference `.tmp/ml-classification-rollout-06-09-crops/07-correlation-01-correlation-coefficient-cropped.png`.
  - Invariants: `-1 ≤ r ≤ 1`; negative/positive direction; LOW `0–0.2`, MEDIUM `0.2–0.5`, and STRONG `0.5–1.0` ranges; no people, camera, browser, or extra metrics.

- `07-correlation-02-binary-target.jpg` →
  `07-correlation-02-binary-target-imagegen-pilot.png`
  - Disposition: imagegen bounded explanatory replacement.
  - Prep: inspected/cropped source reference `.tmp/ml-classification-rollout-06-09-crops/07-correlation-02-binary-target-cropped.png`.
  - Invariants: `x = tenure`, `y = churn`, `y ∈ {0, 1}`, `x ∈ ℝ`; positive means more tenure → higher churn and negative means more tenure → less churn; no people, camera, browser, or extra metrics.
