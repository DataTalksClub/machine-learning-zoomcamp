# ML Zoomcamp deployment intro screenshot rollout

This report records the five screenshots referenced by `cohorts/2026/05-deployment/01-intro.md`. Originals remain in place; accepted replacements are sibling assets.

## 01 — deployment title

- Disposition: `crop/replace` via deterministic crop/export; the title frame introduces the deployment module and its exact title text.
- Source/context: `cohorts/2026/05-deployment/images/01-intro-01-title.jpg`; caption: “Deploying machine learning models”.
- Crop coordinates: source `540x360`; `432x336+24+12` (`x=24, y=12, width=432, height=336`). The crop removes the right webcam tile, color-wheel overlay, recording controls, black borders, and the source cursor was removed by copying a same-slide blank patch at the cursor's blank-area location.
- Invariants: preserve the exact title lines `ML ZOOMCAMP`, `DEPLOYING`, `MACHINE LEARNING`, `MODELS`, and `DATATALKS.CLUB`, including their order and color hierarchy.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/01-intro-01-title-cropped.jpg`.
- QA: source inspected in lesson context; exact title text and hierarchy preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, or black border remains; final dimensions `432x336`; lesson reference resolves; `git diff --check` passes before commit.

## 02 — model deployment architecture

- Disposition: `keep` the existing `imagegen-pilot`; this bounded architecture diagram shows how the notebook model becomes a service that the marketing service can call.
- Source/context: original workshop source `cohorts/2026/05-deployment/images/01-intro-02-model-deployment-diagram.jpg`; current lesson reference `01-intro-02-model-deployment-diagram-imagegen-pilot.png`; caption: “The marketing service asks the churn service, which uses the model, for predictions”.
- Crop coordinates: original source `540x360`; `465x250+25+10` (`x=25, y=10, width=465, height=250`) was the deterministic pre-generation crop used for the pilot. The final `1536x1024` pilot is already framed without webcam, Zoom controls, color-wheel overlay, cursor, watermark, or black borders; no additional crop is needed.
- Invariants: preserve the exact labels `5.1 OVERVIEW`, `JUPYTER NOTEBOOK`, `model`, `model.bin`, `MARKETING SERVICE`, `CHURN SERVICE`, and `MODEL`; preserve notebook→`model.bin` and marketing→churn arrow directions and the model inside the churn service.
- Path: existing imagegen pilot, losslessly re-encoded with pixel identity preserved; final asset `cohorts/2026/05-deployment/images/01-intro-02-model-deployment-diagram-imagegen-pilot.png`.
- QA: source and current output inspected at lesson size; all labels, boxes, and arrow relationships remain readable; a pixel comparison of the lossless re-encode reports zero differing pixels; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, or black border remains; lesson reference resolves; `git diff --check` passes before commit.

## 03 — later module plan

- Disposition: `crop/replace` via deterministic crop/export; this editor capture gives the exact Pipenv and Docker session sequence that the surrounding prose summarizes.
- Source/context: `cohorts/2026/05-deployment/images/01-intro-03-module-plan.jpg`; caption: “The plan of the module, from the lesson notes”.
- Crop coordinates: source `540x360`; `455x300+0+42` (`x=0, y=42, width=455, height=300`). The crop removes the webcam tile, right recording strip, bottom status/control bar, and black border; a deterministic blank-source patch at `x=300, y=104, width=20, height=26` removes the editor cursor without touching text.
- Invariants: preserve the visible exact bullets `Wrapping the predict script into a Flask app`, `Querying it with 'requests'`, `Preparing for production: gunicorn`, and `Running it on Windows with waitress`; preserve the `5.5 Dependency and environment management: Pipenv` and `5.6 Environment management: Docker` headings and every bullet under each heading in its original order.
- Path: deterministic crop/export and blank-gap cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/01-intro-03-module-plan-cropped.jpg`.
- QA: source and candidate inspected in lesson context; exact editor text, punctuation, capitalization, and ordering preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, recording overlay, black border, or bottom status bar remains; final dimensions `455x300`; lesson reference resolves; `git diff --check` passes before commit.

## 04 — first module plan

- Disposition: `crop/replace` via deterministic crop/export; this editor capture gives the exact opening sequence from the deployment overview through the first Flask exercise.
- Source/context: `cohorts/2026/05-deployment/images/01-intro-04-module-plan-continued.jpg`; caption: “The second half of the plan: Pipenv, Docker and AWS”.
- Crop coordinates: source `540x360`; `455x300+0+42` (`x=0, y=42, width=455, height=300`). The crop removes the webcam tile, right recording strip, bottom status/control bar, and black border; a deterministic blank-source patch at `x=300, y=104, width=20, height=26` removes the editor cursor without touching text.
- Invariants: preserve the exact heading `5. Deploying Machine Learning models`; the prose about using the trained churn model as a web service; the `5.1 Intro / Session overview`, `5.2 Saving and loading the model`, and `5.3 Web services: introduction to Flask` headings; and every visible bullet in its original order.
- Path: deterministic crop/export and blank-gap cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/01-intro-04-module-plan-continued-cropped.jpg`.
- QA: source and candidate inspected in lesson context; exact editor text, apostrophes, punctuation, capitalization, and ordering preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, recording overlay, black border, or bottom status bar remains; final dimensions `455x300`; lesson reference resolves; `git diff --check` passes before commit.
