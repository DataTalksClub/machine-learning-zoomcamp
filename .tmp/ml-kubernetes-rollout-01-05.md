# Kubernetes lessons 01–05 screenshot rollout

Scope: every Markdown image reference in `01-overview.md` through
`05-kubernetes-intro.md`. Originals remain in place; accepted replacements
are sibling assets. Imagegen is used only for bounded explanatory diagrams;
exact code, commands, URLs, plots, numeric output, and UI use deterministic
crops and upscaling.

## Acceptance records

### `01-overview-01-tf-serving-inference.jpg`

- Lesson: `01-overview.md`; caption: TensorFlow Serving: C++ inference with the clothes model.
- Disposition: imagegen replacement; the source is a bounded inference diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-01-tf-serving-inference-source.png`, coordinates `475x360+23+0`.
- Invariants checked: left-to-right image input, arrow label `X`, `INFERENCE`, `TF-SERVING`, `C++`, and `CLOTHING MODEL`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra component remains.
- Output: `images/01-overview-01-tf-serving-inference-imagegen.png`.

### `01-overview-02-architecture.jpg`

- Lesson: `01-overview.md`; caption: Website, gateway and TensorFlow Serving.
- Disposition: imagegen replacement; the source is a bounded architecture diagram.
- Source inspection: `594x360`; camera tile, recording controls, and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-02-architecture-source.png`, coordinates `475x360+23+0`.
- Invariants checked: `WEBSITE` → `GATEWAY` → `TF-SERVING`, request labels `URL` and `X`, return arrows, `10 NUMBERS`, and the response notation `"pants": 9.88,...`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra service remains.
- Output: `images/01-overview-02-architecture-imagegen.png`.

### `01-overview-03-grpc.jpg`

- Lesson: `01-overview.md`; caption: The gateway talks to TensorFlow Serving over gRPC.
- Disposition: imagegen replacement; the source is a bounded protocol/architecture diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-03-grpc-source.png`, coordinates `475x360+23+0`.
- Invariants checked: website → gateway → TF-Serving flow, `URL`, `X`, `gRPC`, return arrows, `10 NUMBERS`, and the clothing model.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra component remains.
- Output: `images/01-overview-03-grpc-imagegen.png`.

### `01-overview-04-kubernetes.jpg`

- Lesson: `01-overview.md`; caption: Everything runs inside Kubernetes.
- Disposition: imagegen replacement; the source is a bounded deployment-boundary diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-04-kubernetes-source.png`, coordinates `475x360+23+0`.
- Invariants checked: website outside the boundary; gateway/Flask and TF-Serving/C++ inside `KUBERNETES`; `URL`, `X`, `gRPC`, return arrows, `10 NUMBERS`, and the clothing model.
- Prompt iteration: first generation was rejected because it omitted the gateway-to-website response arrow; one targeted imagegen correction restored that arrow without changing the other relationships.
- Output: `images/01-overview-04-kubernetes-imagegen.png`.

### `01-overview-05-cpu-gpu.jpg`

- Lesson: `01-overview.md`; caption: The gateway runs on CPU, TensorFlow Serving on GPU.
- Disposition: imagegen replacement; the source is a bounded CPU/GPU deployment diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-05-cpu-gpu-source.png`, coordinates `475x360+23+0`.
- Invariants checked: gateway/Flask/CPU assignment, TF-Serving/C++/GPU assignment, Kubernetes boundary, `URL`, `X`, `gRPC`, return arrows, `10 NUMBERS`, and `DOWNLOADING IMAGES RESIZING THEM`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra service remains.
- Output: `images/01-overview-05-cpu-gpu-imagegen.png`.

### `01-overview-06-plan.jpg`

- Lesson: `01-overview.md`; caption: The lesson plan for this module.
- Disposition: deterministic crop/prep; the exact lesson headings and bullet text are the source of truth.
- Source inspection: `594x360`; VS Code UI, webcam tile, and black right strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-06-plan-source-clean.png`, coordinates `500x360+0+0`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: exact headings and bullets for sections 10.5–10.7 remain readable; no generated text used.
- Limitation: the source is a screen capture, so the VS Code frame/status bar remains part of the exact UI context; the webcam tile and right strip are removed.
- Output: `images/01-overview-06-plan-cropped.png`.

### `02-tensorflow-serving-01-saved-model.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: The SavedModel directory: `saved_model.pb` and `variables`.
- Disposition: deterministic crop/prep; the terminal file tree and exact filenames are the source of truth.
- Source inspection: `594x360`; browser chrome, webcam tile, black side strip, and GitHub footer present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-01-saved-model-source-clean.png`, coordinates `460x255+20+38`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `clothing-model`, `assets`, `saved_model.pb`, `variables`, both variable files, and the final directory/file counts remain exact.
- Output: `images/02-tensorflow-serving-01-saved-model-cropped.png`.

### `02-tensorflow-serving-02-signature.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: The signature definition of the model.
- Disposition: deterministic focused crop/prep; exact signature names, dtype, shape, and method are the source of truth.
- Source inspection: `594x360`; Save As dialog, webcam tile, editor chrome, and status bar present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-02-signature-source-clean.png`, coordinates `500x165+0+78`; resized 2.5x with Lanczos and light unsharp masking.
- Invariants checked: `outputs['dense_7']`, `DT_FLOAT`, `(-1, 10)`, `StatefulPartitionedCall:0`, and `tensorflow/serving/predict` remain exact; the obstructing Save As dialog is excluded by the crop.
- Output: `images/02-tensorflow-serving-02-signature-cropped.png`.

### `02-tensorflow-serving-03-docker-run.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Volume mapping: the model name and the version.
- Disposition: deterministic crop/prep; exact Docker command, mount path, model name, and version are the source of truth.
- Source inspection: `594x360`; editor chrome, webcam tile, and black side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-03-docker-run-source-clean.png`, initial `460x265+20+30`, then top `8px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `docker run`, `8500:8500`, `./`, `clothing-model`, `clothing-model-v4.h5`, `/models/clothing-model`, and version `1` remain exact; handwritten `NAME`/`VERSION` annotations are preserved.
- Output: `images/02-tensorflow-serving-03-docker-run-cropped.png`.

### `02-tensorflow-serving-04-install-libraries.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Installing the libraries in the notebook.
- Disposition: deterministic crop/prep; exact package names and versions are the source of truth.
- Source inspection: `594x360`; notebook chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-04-install-libraries-source-clean.png`, coordinates `500x205+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `%autosave 0`, `grpcio==1.42.0`, `tensorflow-serving-api==2.7.0`, `keras-image-helper`, and the visible `import` cell remain exact.
- Output: `images/02-tensorflow-serving-04-install-libraries-cropped.png`.

### `02-tensorflow-serving-05-grpc-stub.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Connecting to TensorFlow Serving: host, channel and stub.
- Disposition: deterministic crop/prep; exact imports, host, and channel code are the source of truth.
- Source inspection: `594x360`; notebook chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-05-grpc-stub-source-clean.png`, coordinates `500x275+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: package installs, `import grpc`, TensorFlow Serving protobuf imports, `host = 'localhost:8500'`, and `grpc.insecure_channel` remain exact.
- Output: `images/02-tensorflow-serving-05-grpc-stub-cropped.png`.

### `02-tensorflow-serving-06-prepare-request.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Preparing the prediction request.
- Disposition: deterministic crop/prep; exact preprocessing, URL, protobuf, model, signature, and input names are the source of truth.
- Source inspection: `594x360`; notebook chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-06-prepare-request-source-clean.png`, coordinates `500x290+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `create_preprocessor`, `xception`, `(299, 299)`, the pants URL, `np_to_protobuf`, `clothing-model`, `serving_default`, and `input_8` remain exact.
- Output: `images/02-tensorflow-serving-06-prepare-request-cropped.png`.

### `02-tensorflow-serving-07-prediction.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Turning the raw scores into class names.
- Disposition: deterministic crop/prep; this is an exact UI screenshot, but its visible content must not be reconstructed with imagegen.
- Source inspection: `594x360`; GitHub browser chrome, profile/contributor avatars, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-07-prediction-source-clean.png`, coordinates `380x280+0+40`; resized 2x with Lanczos and light unsharp masking, excluding browser header/sidebar avatars.
- Invariants checked: the visible repository listing remains exact; no generated text or inferred prediction output was added.
- Limitation: the supplied source does not show raw scores or class names despite the caption; the crop removes unrelated avatars/chrome but cannot repair this source-content mismatch.
- Output: `images/02-tensorflow-serving-07-prediction-cropped.png`.

### `03-preprocessing-01-nbconvert.jpg`

- Lesson: `03-preprocessing.md`; caption: Converting the notebook with jupyter nbconvert.
- Disposition: deterministic crop/prep; exact terminal command and server output are the source of truth.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-01-nbconvert-source-clean.png`, coordinates `490x285+10+25`, then top `14px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: the notebook server output, model files, `jupyter nbconvert` command, and visible status lines remain exact.
- Limitation: the source itself truncates the first character of the directory path and the lower conversion output; no text was guessed or reconstructed.
- Output: `images/03-preprocessing-01-nbconvert-cropped.png`.

### `03-preprocessing-02-gateway-script.jpg`

- Lesson: `03-preprocessing.md`; caption: Preparing the request and invoking the model in the gateway script.
- Disposition: deterministic crop/prep; exact Python, URL, model, signature, and timeout code are the source of truth.
- Source inspection: `594x360`; editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-02-gateway-script-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `clothing-model`, `serving_default`, `input_8`, `np_to_protobuf`, the pants URL, and `timeout=20.0` remain exact.
- Output: `images/03-preprocessing-02-gateway-script-cropped.png`.

### `03-preprocessing-03-flask-app.jpg`

- Lesson: `03-preprocessing.md`; caption: The Flask app part of `gateway.py`.
- Disposition: deterministic crop/prep; the visible Python source is exact and must not be approximated with imagegen.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-03-flask-app-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: Flask imports, model loading, `/predict` route, request handling, churn threshold, JSON keys, and `jsonify` call remain unchanged.
- Limitation: the source screenshot is intrinsically low-resolution and text remains softer than the other crops; no generated approximation was used because code fidelity is required.
- Output: `images/03-preprocessing-03-flask-app-cropped.png`.

### `03-preprocessing-04-pipenv-install.jpg`

- Lesson: `03-preprocessing.md`; caption: Installing the dependencies with pipenv and testing the gateway.
- Disposition: deterministic crop/prep; exact shell output, package versions, and prediction values are the source of truth.
- Source inspection: `594x360`; editor/browser chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-04-pipenv-install-source-clean.png`, coordinates `460x300+20+30`, then top `8px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `grpcio==1.42.0`, Flask, gunicorn, `keras-image-helper`, Python `3.8.10`, virtualenv creation, and visible prediction values remain exact.
- Limitation: long terminal lines retain the source-edge truncation; no output was guessed or expanded.
- Output: `images/03-preprocessing-04-pipenv-install-cropped.png`.

### `03-preprocessing-05-tensorflow-protobuf.jpg`

- Lesson: `03-preprocessing.md`; caption: The tensorflow-protobuf README: the verbose version without the baggage.
- Disposition: deterministic crop/prep; exact protobuf Python code is the source of truth.
- Source inspection: `594x360`; browser chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-05-tensorflow-protobuf-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `make_tensor_proto`, shape/dims conversion, dtype conversion, `TensorProto`, `tensor_content`, and `np_to_protobuf` remain exact.
- Output: `images/03-preprocessing-05-tensorflow-protobuf-cropped.png`.
