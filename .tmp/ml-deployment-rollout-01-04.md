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

## Pickle lesson — 05 — train.py validation loop

- Disposition: `crop/replace` via deterministic crop/export; this exact VS Code frame shows the `predict` return and the start of `KFold` validation in `train.py`.
- Source/context: `cohorts/2026/05-deployment/images/02-pickle-05-train-py.jpg`; caption: “The train.py script: the predict function and the cross-validation loop”.
- Crop coordinates: source `598x360`; `510x292+44+51` (`x=44, y=51, width=510, height=292`). The crop removes the VS Code activity bar, top tabs/breadcrumb chrome, right minimap, bottom status bar, webcam tile, unused frame area, and the source’s next partially clipped line. A deterministic background patch at source `x=160..163, y=159..176` removes the insertion cursor after `# validation` without touching code.
- Invariants: preserve the exact visible line numbers and code `X = dv.transform(dicts)`, `y_pred = model.predict_proba(X)[:, 1]`, `return y_pred`, `# validation`, `kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)`, `scores = []`, `for train_idx, val_idx in kfold.split(df_full_train):`, `df_train = df_full_train.iloc[train_idx]`, `df_val = df_full_train.iloc[val_idx]`, and `y_train = df_train.churn.values`, in their original order and indentation.
- Path: deterministic crop/export and blank-background cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/02-pickle-05-train-py-cropped.jpg`.
- QA: source inspected in lesson context at native `598x360`; candidate reviewed at lesson size; exact code, line numbers, syntax, indentation, and ordering preserved; no face, webcam, browser/Zoom chrome, minimap, cursor, watermark, overlay, black border, or partial next line remains; final dimensions `510x292`; image reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because this is exact source code and deterministic fidelity is required.

## Flask intro lesson — 01 — module overview

- Disposition: `crop/replace` via deterministic crop/export; this hand-drawn overview establishes the deployment flow and marks web services as the focus of the week, so the exact labels and arrow relationships are retained rather than regenerated.
- Source/context: `cohorts/2026/05-deployment/images/03-flask-intro-01-module-overview.jpg`; caption: “The plan of the module: web services are the focus of this week”.
- Crop coordinates: source `598x360`; `464x344+26+0` (`x=26, y=0, width=464, height=344`). The crop removes the left black border, upper-right webcam tile, lower-right color-wheel/recording overlay, and the source bottom edge; a deterministic blank-paper patch at source `x=285..294, y=104..117` removes the cursor from the empty area below the notebook-to-model arrow.
- Invariants: preserve the exact visible labels `5.1 OVERVIEW`, `JUPYTER NOTEBOOK`, `model`, `model.bin`, `MARKETING SERVICE`, `CHURN SERVICE`, `MODEL`, `25%`, and `FOCUS OF THIS WEEK`; preserve the notebook→`model.bin`, `model.bin`→churn, marketing→churn, and focus-arrow relationships and their original ordering.
- Path: deterministic crop/export and blank-area cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/03-flask-intro-01-module-overview-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; all instructional labels, boxes, arrows, people/envelope mark, `25%`, and focus note remain readable; no face, webcam, browser/Zoom chrome, cursor, watermark, color-wheel overlay, or black border remains; final dimensions `464x344`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because deterministic pixels and handwritten relationships are the source of truth.

## Flask intro lesson — 02 — request/response sketch

- Disposition: `crop/replace` via deterministic crop/export; this conceptual sketch explains the client request and web-service response, while its handwritten labels and arrow directions remain exact.
- Source/context: `cohorts/2026/05-deployment/images/03-flask-intro-02-request-response.jpg`; caption: “A client sends a request to the web service and gets a response back”.
- Crop coordinates: source `598x360`; `464x300+26+0` (`x=26, y=0, width=464, height=300`). The crop removes the left black border, upper-right webcam tile, lower-right color-wheel/recording overlay, and unused bottom frame; a deterministic blank-paper patch at source `x=278..289, y=10..25` removes the cursor from the empty area above the request arrow.
- Invariants: preserve the exact visible title `5.3 WEB SERVICES`, the client stick figure, `ml+zoomcamp`, `q=web-service`, the `WEB SERVICE` box, the rightward request arrow, leftward response arrow, and the green document sketch in their original positions and directions.
- Path: deterministic crop/export and blank-area cursor cleanup from the original; final asset `cohorts/2026/05-deployment/images/03-flask-intro-02-request-response-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; title, labels, arrows, service box, client figure, and document sketch remain readable and unchanged; no face, webcam, browser/Zoom chrome, cursor, watermark, color-wheel overlay, or black border remains; final dimensions `464x300`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because deterministic handwritten labels and arrow relationships are the source of truth.

## Flask intro lesson — 03 — ping.py editor

- Disposition: `crop/replace` via deterministic crop/export; this is an exact source-code frame, so no generated approximation is permitted.
- Source/context: `cohorts/2026/05-deployment/images/03-flask-intro-03-ping-app.jpg`; caption: “The ping.py service in the editor”.
- Crop coordinates: source `598x360`; `460x292+44+51` (`x=44, y=51, width=460, height=292`). The crop removes the VS Code activity/sidebar and top chrome, the upper-right webcam tile, the bottom status/control strip, and unused frame area; a deterministic dark-editor patch at source `x=83..85, y=51..75` removes the insertion caret immediately before `from` without changing the code glyphs.
- Invariants: preserve the exact visible line numbers 1–10 and code `from flask import Flask`, `app = Flask('ping')`, `@app.route('/ping', methods=['GET'])`, `def ping():`, `return "PONG"`, `if __name__ == "__main__":`, and `app.run(debug=True, host='0.0.0.0', port=9696)`, including indentation, quote style, punctuation, and ordering.
- Path: deterministic crop/export and dark-background caret cleanup from the original; final asset `cohorts/2026/05-deployment/images/03-flask-intro-03-ping-app-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; line numbers, code text, punctuation, indentation, and syntax coloring remain unchanged and readable; no face, webcam, browser/Zoom chrome, cursor/caret, watermark, overlay, activity bar, or black border remains; final dimensions `460x292`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact code is the source of truth.

## Flask deployment lesson — 01 — module plan

- Disposition: `crop/replace` via deterministic crop/export; this exact editor frame shows the Flask serving, gunicorn, waitress, and Pipenv sequence used in the lesson.
- Source/context: `cohorts/2026/05-deployment/images/04-flask-deployment-01-module-plan.jpg`; caption: “The plan of the module: serving the churn model with Flask”.
- Crop coordinates: source `598x360`; `460x286+44+52` (`x=44, y=52, width=460, height=286`). The crop removes the VS Code activity bar, tabs/breadcrumb chrome, webcam tile, bottom status/control strip, black frame edge, and the source's clipped `5.6` heading; no instructional text is painted over.
- Invariants: preserve the exact visible lines `* Writing a simple ping/pong app`, `* Querying it with \`curl\` and browser`, `## 5.4 Serving the churn model with Flask`, all four bullets under that heading, `## 5.5 Dependency and environment management: Pipenv`, and its four bullets, in their original order and punctuation.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/04-flask-deployment-01-module-plan-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; exact editor text, syntax colors, ordering, and indentation remain readable; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, sidebar, black border, or bottom status bar remains; final dimensions `460x286`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact editor text is the source of truth.

## Flask deployment lesson — 02 — predict.py editor

- Disposition: `crop/replace` via deterministic crop/export; this exact source-code frame shows the POST route, vectorizer transform, probability threshold, native-type casts, JSON response, and Flask entry point.
- Source/context: `cohorts/2026/05-deployment/images/04-flask-deployment-02-predict-py.jpg`; caption: “The predict.py service in the editor”.
- Crop coordinates: source `598x360`; `460x292+44+51` (`x=44, y=51, width=460, height=292`). The crop removes the VS Code activity bar, tabs/breadcrumb chrome, webcam tile, bottom status/control strip, and unused frame area; no code pixels are painted over.
- Invariants: preserve visible lines 15–32 exactly, including `@app.route('/predict', methods=['POST'])`, `customer = request.get_json()`, `X = dv.transform([customer])`, `y_pred = model.predict_proba(X)[0, 1]`, `churn = y_pred >= 0.5`, the `result` dictionary with `float(y_pred)` and `bool(churn)`, `return jsonify(result)`, and `app.run(debug=True, host='0.0.0.0', port=9696)`, with original indentation, punctuation, and syntax coloring.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/04-flask-deployment-02-predict-py-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; exact code, line numbers, values, quote style, indentation, and ordering remain readable; no face, webcam, browser/Zoom chrome, cursor/caret, watermark, overlay, sidebar, black border, or bottom status bar remains; final dimensions `460x292`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact source code is the source of truth.

## Flask deployment lesson — 03 — customer dictionary

- Disposition: `crop/replace` via deterministic crop/export; this Jupyter frame shows the exact customer record sent to the prediction endpoint before the JSON response is serialized.
- Source/context: `cohorts/2026/05-deployment/images/04-flask-deployment-03-json-serializable-error.jpg`; caption: “Flask cannot serialize NumPy types to JSON, so we cast to native Python types”.
- Crop coordinates: source `598x360`; `480x273+20+39` (`x=20, y=39, width=480, height=273`). The crop removes the browser/menu chrome, webcam tile, black right frame edge, bottom browser strip, and following blank input cell; the active cell border and code are retained without painting.
- Invariants: preserve the exact `In [4]` cell and customer dictionary, including keys and values `gender: "female"`, `seniorcitizen: 0`, `partner: "yes"`, `dependents: "no"`, `phoneservice: "no"`, `multiplelines: "no_phone_service"`, `internetservice: "dsl"`, `onlinesecurity: "no"`, `onlinebackup: "yes"`, `deviceprotection: "no"`, `techsupport: "no"`, `streamingtv: "no"`, `streamingmovies: "no"`, `contract: "month-to-month"`, `paperlessbilling: "yes"`, `paymentmethod: "electronic_check"`, `tenure: 1`, `monthlycharges: 29.85`, and `totalcharges: 29.85`, in their original order and syntax.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/04-flask-deployment-03-json-serializable-error-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; all visible labels, keys, values, punctuation, colors, and cell framing remain readable; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, black border, or trailing blank cell remains; final dimensions `480x273`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact notebook text and values are the source of truth.

## Flask deployment lesson — 04 — test request

- Disposition: `crop/replace` via deterministic crop/export; this Jupyter frame shows the exact `requests` call, returned churn decision, probability, and follow-up branch.
- Source/context: `cohorts/2026/05-deployment/images/04-flask-deployment-04-test-request.jpg`; caption: “Sending a test request with the requests library”.
- Crop coordinates: source `598x360`; `480x100+20+253` (`x=20, y=253, width=480, height=100`). The crop keeps the complete request/response cells and removes the browser/menu chrome, webcam tile, preceding partial customer dictionary, bottom browser strip, and unused frame area.
- Invariants: preserve the exact `In [15]` code `response = requests.post(url, json=customer).json()` followed by `response`; the `Out[15]` value `{'churn': False, 'churn_probability': 0.3257561103397851}`; and the visible `In [16]` condition `if response['churn'] == True:`, including labels, punctuation, spacing, and syntax colors.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/04-flask-deployment-04-test-request-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; exact request code, response keys, Boolean value, numeric probability, cell labels, and ordering remain readable; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, black border, or unrelated partial cell remains; final dimensions `480x100`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact code and output values are the source of truth.

## Flask deployment lesson — 05 — development-server warning

- Disposition: `crop/replace` via deterministic crop/export; this terminal frame retains the exact Flask development-server warning and the surrounding debug-mode context.
- Source/context: `cohorts/2026/05-deployment/images/04-flask-deployment-05-dev-server-warning.jpg`; caption: “Flask warns that the development server is not for production”.
- Crop coordinates: source `598x360`; `461x187+71+54` (`x=71, y=54, width=461, height=187`). The crop isolates the terminal content, removing VS Code/browser chrome, webcam tile, terminal frame border, bottom controls, and the URL line whose hover tooltip obscures exact text; no pixels are painted over.
- Invariants: preserve the exact terminal lines `$ python predict.py`, `* Serving Flask app 'churn' (lazy loading)`, `* Environment: production`, both complete `WARNING: This is a development server. Do not use it in a production deployment.` lines, `* Use a production WSGI server instead.`, `* Debug mode: on`, and `* Running on all addresses.`, plus the visible directory listing and syntax colors.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/05-deployment/images/04-flask-deployment-05-dev-server-warning-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size; warning text, debug/environment labels, command prompt output, line wrapping, and colors remain exact and readable; no face, webcam, browser/Zoom chrome, cursor, hover tooltip, watermark, overlay, terminal scrollbar, or black/white frame border remains; final dimensions `461x187`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact terminal text is the source of truth; the obscured URL was excluded by crop rather than guessed or regenerated.

## Flask deployment lesson — 06 — Windows command prompt

- Disposition: `crop/replace` via deterministic crop/export plus a background-patch cleanup; this exact Windows command-prompt frame preserves the directory context for the Windows deployment alternative.
- Source/context: `cohorts/2026/05-deployment/images/04-flask-deployment-06-waitress-windows.jpg`; caption: “gunicorn fails on Windows because of the fcntl module; waitress is the alternative”.
- Crop coordinates: source `598x360`; `450x190+72+57` (`x=72, y=57, width=450, height=190`). The crop removes browser/Jupyter chrome, command-prompt title bar, webcam tile, notebook underneath, right scrollbar, and the clipped `pycache` rows. Deterministic cleanup copies the blank command-prompt background from cropped `x=220..225, y=38..53` to `x=214..219, y=38..53` (source destination `x=286..291, y=95..110`) to remove the mouse pointer immediately after `zoomcamp`, leaving the path text unchanged.
- Invariants: preserve the exact visible `Volume in drive C is Local Disk`, `Volume Serial Number is 6C3B-24E8`, `Directory of C:\Users\alexey\zoomcamp`, and every complete directory row through `train.py`, including dates, times, `<DIR>` markers, filenames, sizes, and column order.
- Path: deterministic crop/export and same-background pointer cleanup from the original; final asset `cohorts/2026/05-deployment/images/04-flask-deployment-06-waitress-windows-cropped.jpg`.
- QA: source inspected at native `598x360` in lesson context; candidate reviewed at lesson size and enlarged for pointer cleanup; path, directory rows, values, alignment, and text remain readable; no face, webcam, browser/Zoom chrome, cursor, watermark, overlay, title bar, scrollbar, black border, or clipped row remains; final dimensions `450x190`; lesson reference resolves; `git diff --check` passes before commit. Imagegen skill was available but not used because exact Windows UI text is the source of truth.
