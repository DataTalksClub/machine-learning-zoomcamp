# ML Zoomcamp trees screenshot rollout (lessons 01–04)

Scope in this checkout: `01-credit-risk.md`, `02-data-prep.md`,
`03-decision-trees.md`, and `04-decision-tree-learning.md` (the requested
filenames were not present). Every referenced screenshot in those lessons is
being inspected and assigned an imagegen or deterministic disposition.

## Accepted assets

- `01-credit-risk-01-loan-application.jpg` →
  `01-credit-risk-01-loan-application-imagegen.png`: imagegen regeneration.
  Source crop `(x=25, y=0, width=455, height=330)` removed the black frame,
  webcam tile, recorder controls, and color wheel before generation. The
  accepted correction removed an incorrect generated sign; checked labels
  `BANK`, `MONEY`, `YES / NO`, client-to-bank and bank-to-client arrows, and
  absence of people/camera/recording overlays.
- `01-credit-risk-02-historical-data.jpg` →
  `01-credit-risk-02-historical-data-imagegen.png`: imagegen regeneration.
  Source crop `(x=25, y=0, width=455, height=330)` removed the black frame,
  webcam tile, recorder controls, and color wheel. Checked five rows and exact
  outcome order `OK`, `OK`, `DEFAULT`, `DEFAULT`, `OK`; no extra rows or
  overlays remain.
- `01-credit-risk-03-probability-of-default.jpg` →
  `01-credit-risk-03-probability-of-default-imagegen.png`: imagegen
  regeneration. Source crop `(x=25, y=0, width=480, height=270)` removed the
  black frame, webcam tile, recorder controls, and color wheel. Checked the
  five target outcomes, `y ∈ {0, 1}`, mappings to `OK`/`DEFAULT`, and the
  statement `g(xᵢ) → probability of default`; no extra values or overlays.
- `01-credit-risk-04-dataset-columns.jpg` →
  `01-credit-risk-04-dataset-columns-cropped.png`: deterministic crop
  `(x=0, y=25, width=430, height=330)` retained the exact 14-row column
  reference and removed browser/camera chrome; exact text was not generated.
