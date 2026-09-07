# ML Zoomcamp deployment intro screenshot rollout

This report records the five screenshots referenced by `cohorts/2026/05-deployment/01-intro.md`. Originals remain in place; accepted replacements are sibling assets.

## 01 — deployment title

- Disposition: `crop/replace` via deterministic crop/export; the title frame introduces the deployment module and its exact title text.
- Source/context: `cohorts/2026/05-deployment/images/01-intro-01-title.jpg`; caption: “Deploying machine learning models”.
- Crop coordinates: source `540x360`; `432x336+24+12` (`x=24, y=12, width=432, height=336`). The crop removes the right webcam tile, color-wheel overlay, recording controls, black borders, and the source cursor was removed by copying a same-slide blank patch at the cursor's blank-area location.
- Invariants: preserve the exact title lines `ML ZOOMCAMP`, `DEPLOYING`, `MACHINE LEARNING`, `MODELS`, and `DATATALKS.CLUB`, including their order and color hierarchy.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/01-intro-01-title-cropped.jpg`.
- QA: source inspected in lesson context; exact title text and hierarchy preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, or black border remains; final dimensions `432x336`; lesson reference resolves; `git diff --check` passes before commit.
