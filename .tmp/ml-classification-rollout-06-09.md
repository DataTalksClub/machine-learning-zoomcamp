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
