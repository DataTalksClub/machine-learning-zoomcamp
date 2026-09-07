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

## 05 — nested deployment environments

- Disposition: `crop/replace` via deterministic crop/export; this hand-drawn nesting diagram shows the service, Python dependencies, and system dependencies being wrapped layer by layer.
- Source/context: `cohorts/2026/05-deployment/images/01-intro-05-environments.jpg`; caption: “The web service wraps the model, Pipenv wraps the Python dependencies, Docker wraps everything”.
- Crop coordinates: source `540x360`; `432x312+24+12` (`x=24, y=12, width=432, height=312`). The crop removes the webcam tile, color-wheel overlay, recording controls, black borders, and unused frame area while keeping the complete nested drawing.
- Invariants: preserve the nesting and exact labels `DOCKER`, `PIPENV`, `FLASK`, `CHURN PREDICTION MODEL`, `WEB SERVICE`, `ENVIRONMENT FOR PYTHON DEPS`, and `ENVIRONMENT — SYSTEM DEPENDENCIES`, including the outer-to-inner dependency relationship.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/01-intro-05-environments-cropped.jpg`.
- QA: source and candidate inspected in lesson context; nested boxes, labels, and hierarchy preserved; no face, webcam, browser/Zoom chrome, cursor, color-wheel overlay, recording control, watermark, or black border remains; final dimensions `432x312`; lesson reference resolves; `git diff --check` passes before commit.

## Pickle lesson — 01 — module plan

- Disposition: `crop/replace` via deterministic crop/export; this exact VS Code plan frame shows where saving/loading the model fits in the deployment module.
- Source/context: `cohorts/2026/05-deployment/images/02-pickle-01-module-plan.jpg`; caption: “The plan of the module: saving and loading the model”.
- Crop coordinates: source `598x360`; `510x286+44+53` (`x=44, y=53, width=510, height=286`). The crop removes the VS Code activity bar, top tabs/breadcrumb chrome, right minimap, bottom status bar, webcam tile, and unused frame area. A deterministic background patch at source `x=85..86, y=229..244` removes the insertion cursor from the blank line without touching text.
- Invariants: preserve the exact visible lines `deploy it as a web service.`, `## 5.1 Intro / Session overview`, `* What we will cover this week`, the highlighted `## 5.2 Saving and loading the model` section and its three bullets, `## 5.3 Web services: introduction to Flask` and its two bullets, and `## 5.4 Serving the churn model with Flask`, including order, punctuation, and highlight hierarchy.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/02-pickle-01-module-plan-cropped.jpg`.
- QA: source inspected in lesson context at native `598x360`; candidate reviewed at lesson size; exact text, ordering, and highlight preserved; no face, webcam, browser/Zoom chrome, minimap, cursor, watermark, overlay, or black border remains; final dimensions `510x286`; image reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because this is exact editor text and the deterministic path is required.

## Pickle lesson — 02 — pickle dump

- Disposition: `crop/replace` via deterministic crop/export; this Jupyter frame shows the exact `pickle.dump((dv, model), f_out)` save sequence and resulting `model_C=1.0.bin` filename.
- Source/context: `cohorts/2026/05-deployment/images/02-pickle-02-pickle-dump.jpg`; caption: “Saving the vectorizer and the model as a tuple with pickle”.
- Crop coordinates: source `598x360`; `535x307+35+53` (`x=35, y=53, width=535, height=307`). The crop removes the browser URL/menu chrome, webcam tile, black right edge, and unused page margin while retaining the complete notebook cells.
- Invariants: preserve the exact notebook labels `In [14]`, `In [16]`, `Out[16]`, `In [17]`, the code `import pickle`, `output_file = f'model_C={C}.bin'`, `output_file`, `f_out = open(output_file, 'wb')`, `pickle.dump((dv, model), f_out)`, `f_out.close()`, and the output `'model_C=1.0.bin'`, plus the `Save the model` and `Load the model` headings and cell order.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/02-pickle-02-pickle-dump-cropped.jpg`.
- QA: source inspected in lesson context at native `598x360`; candidate reviewed at lesson size; exact code, labels, output value, ordering, and cell borders preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, or black border remains; final dimensions `535x307`; image reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because code and output values require deterministic fidelity.

## Pickle lesson — 03 — model filename

- Disposition: `crop/replace` via deterministic crop/export; this notebook frame demonstrates that the saved filename includes the tuned `C` value.
- Source/context: `cohorts/2026/05-deployment/images/02-pickle-03-model-filename.jpg`; caption: “The filename contains the value of C”.
- Crop coordinates: source `598x360`; `535x295+35+65` (`x=35, y=65, width=535, height=295`). The crop removes the browser URL/menu chrome, webcam tile, clipped preceding output, black right edge, and unused page margin. A deterministic background patch at source `x=285..286, y=207..220` removes the insertion cursor after `'w'` without touching the code or punctuation.
- Invariants: preserve the exact notebook labels `In [14]`, `In [16]`, `Out[16]`, `In [ ]`, the `Save the model` and `Load the model` headings, the code `import pickle`, `output_file = f'model_C={C}.bin'`, `output_file`, `f_out = open(output_file, 'w')`, and the output `'model_C=1.0.bin'`, including cell order and green active-cell border.
- Path: deterministic crop/export and blank-background cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/02-pickle-03-model-filename-cropped.jpg`.
- QA: source inspected in lesson context at native `598x360`; candidate reviewed at lesson size; exact code, filename value, labels, punctuation, and cell border preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, or black border remains; final dimensions `535x295`; image reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact code and output values require deterministic fidelity.

## Pickle lesson — 04 — loaded model

- Disposition: `crop/replace` via deterministic crop/export; this notebook frame shows loading the pickle tuple and unpacking it into `dv` and `model`.
- Source/context: `cohorts/2026/05-deployment/images/02-pickle-04-loaded-model.jpg`; caption: “Loading the model back: the tuple unpacks into the vectorizer and the model”.
- Crop coordinates: source `598x360`; `535x295+35+65` (`x=35, y=65, width=535, height=295`). The crop removes the browser URL/menu chrome, webcam tile, clipped preceding save cell, black right edge, and unused page margin. A deterministic background patch at source `x=215..218, y=115..124` removes the insertion cursor after `import pickle` without touching the code.
- Invariants: preserve the exact `Load the model` heading; notebook labels `In [1]`, `In [4]`, `In [5]`, `In [6]`, `Out[6]`, and `In [ ]`; code `import pickle`, `model_file = 'model_C=1.0.bin'`, `with open(model_file, 'rb') as f_in:`, `dv, model = pickle.load(f_in)`, and `dv, model`; preserve the exact output `(DictVectorizer(sparse=False), LogisticRegression(max_iter=1000))` and following customer dictionary order.
- Path: deterministic crop/export and blank-background cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/02-pickle-04-loaded-model-cropped.jpg`.
- QA: source inspected in lesson context at native `598x360`; candidate reviewed at lesson size; exact code, labels, filename, output representation, punctuation, and cell order preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, or black border remains; final dimensions `535x295`; image reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact code and output values require deterministic fidelity.
