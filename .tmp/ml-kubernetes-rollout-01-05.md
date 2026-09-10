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
- Output: `images/01-overview-01-tf-serving-inference-imagegen.jpg`.

### `01-overview-02-architecture.jpg`

- Lesson: `01-overview.md`; caption: Website, gateway and TensorFlow Serving.
- Disposition: imagegen replacement; the source is a bounded architecture diagram.
- Source inspection: `594x360`; camera tile, recording controls, and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-02-architecture-source.png`, coordinates `475x360+23+0`.
- Invariants checked: `WEBSITE` → `GATEWAY` → `TF-SERVING`, request labels `URL` and `X`, return arrows, `10 NUMBERS`, and the response notation `"pants": 9.88,...`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra service remains.
- Output: `images/01-overview-02-architecture-imagegen.jpg`.

### `01-overview-03-grpc.jpg`

- Lesson: `01-overview.md`; caption: The gateway talks to TensorFlow Serving over gRPC.
- Disposition: imagegen replacement; the source is a bounded protocol/architecture diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-03-grpc-source.png`, coordinates `475x360+23+0`.
- Invariants checked: website → gateway → TF-Serving flow, `URL`, `X`, `gRPC`, return arrows, `10 NUMBERS`, and the clothing model.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra component remains.
- Output: `images/01-overview-03-grpc-imagegen.jpg`.

### `01-overview-04-kubernetes.jpg`

- Lesson: `01-overview.md`; caption: Everything runs inside Kubernetes.
- Disposition: imagegen replacement; the source is a bounded deployment-boundary diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-04-kubernetes-source.png`, coordinates `475x360+23+0`.
- Invariants checked: website outside the boundary; gateway/Flask and TF-Serving/C++ inside `KUBERNETES`; `URL`, `X`, `gRPC`, return arrows, `10 NUMBERS`, and the clothing model.
- Prompt iteration: first generation was rejected because it omitted the gateway-to-website response arrow; one targeted imagegen correction restored that arrow without changing the other relationships.
- Output: `images/01-overview-04-kubernetes-imagegen.jpg`.

### `01-overview-05-cpu-gpu.jpg`

- Lesson: `01-overview.md`; caption: The gateway runs on CPU, TensorFlow Serving on GPU.
- Disposition: imagegen replacement; the source is a bounded CPU/GPU deployment diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-05-cpu-gpu-source.png`, coordinates `475x360+23+0`.
- Invariants checked: gateway/Flask/CPU assignment, TF-Serving/C++/GPU assignment, Kubernetes boundary, `URL`, `X`, `gRPC`, return arrows, `10 NUMBERS`, and `DOWNLOADING IMAGES RESIZING THEM`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra service remains.
- Output: `images/01-overview-05-cpu-gpu-imagegen.jpg`.

### `01-overview-06-plan.jpg`

- Lesson: `01-overview.md`; caption: The lesson plan for this module.
- Disposition: deterministic crop/prep; the exact lesson headings and bullet text are the source of truth.
- Source inspection: `594x360`; VS Code UI, webcam tile, and black right strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-06-plan-source-clean.png`, coordinates `500x360+0+0`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: exact headings and bullets for sections 10.5–10.7 remain readable; no generated text used.
- Limitation: the source is a screen capture, so the VS Code frame/status bar remains part of the exact UI context; the webcam tile and right strip are removed.
- Output: `images/01-overview-06-plan-cropped.jpg`.

### `02-tensorflow-serving-01-saved-model.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: The SavedModel directory: `saved_model.pb` and `variables`.
- Disposition: deterministic crop/prep; the terminal file tree and exact filenames are the source of truth.
- Source inspection: `594x360`; browser chrome, webcam tile, black side strip, and GitHub footer present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-01-saved-model-source-clean.png`, coordinates `460x255+20+38`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `clothing-model`, `assets`, `saved_model.pb`, `variables`, both variable files, and the final directory/file counts remain exact.
- Output: `images/02-tensorflow-serving-01-saved-model-cropped.jpg`.

### `02-tensorflow-serving-02-signature.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: The signature definition of the model.
- Disposition: deterministic focused crop/prep; exact signature names, dtype, shape, and method are the source of truth.
- Source inspection: `594x360`; Save As dialog, webcam tile, editor chrome, and status bar present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-02-signature-source-clean.png`, coordinates `500x165+0+78`; resized 2.5x with Lanczos and light unsharp masking.
- Invariants checked: `outputs['dense_7']`, `DT_FLOAT`, `(-1, 10)`, `StatefulPartitionedCall:0`, and `tensorflow/serving/predict` remain exact; the obstructing Save As dialog is excluded by the crop.
- Output: `images/02-tensorflow-serving-02-signature-cropped.jpg`.

### `02-tensorflow-serving-03-docker-run.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Volume mapping: the model name and the version.
- Disposition: deterministic crop/prep; exact Docker command, mount path, model name, and version are the source of truth.
- Source inspection: `594x360`; editor chrome, webcam tile, and black side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-03-docker-run-source-clean.png`, initial `460x265+20+30`, then top `8px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `docker run`, `8500:8500`, `./`, `clothing-model`, `clothing-model-v4.h5`, `/models/clothing-model`, and version `1` remain exact; handwritten `NAME`/`VERSION` annotations are preserved.
- Output: `images/02-tensorflow-serving-03-docker-run-cropped.jpg`.

### `02-tensorflow-serving-04-install-libraries.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Installing the libraries in the notebook.
- Disposition: deterministic crop/prep; exact package names and versions are the source of truth.
- Source inspection: `594x360`; notebook chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-04-install-libraries-source-clean.png`, coordinates `500x205+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `%autosave 0`, `grpcio==1.42.0`, `tensorflow-serving-api==2.7.0`, `keras-image-helper`, and the visible `import` cell remain exact.
- Output: `images/02-tensorflow-serving-04-install-libraries-cropped.jpg`.

### `02-tensorflow-serving-05-grpc-stub.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Connecting to TensorFlow Serving: host, channel and stub.
- Disposition: deterministic crop/prep; exact imports, host, and channel code are the source of truth.
- Source inspection: `594x360`; notebook chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-05-grpc-stub-source-clean.png`, coordinates `500x275+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: package installs, `import grpc`, TensorFlow Serving protobuf imports, `host = 'localhost:8500'`, and `grpc.insecure_channel` remain exact.
- Output: `images/02-tensorflow-serving-05-grpc-stub-cropped.jpg`.

### `02-tensorflow-serving-06-prepare-request.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Preparing the prediction request.
- Disposition: deterministic crop/prep; exact preprocessing, URL, protobuf, model, signature, and input names are the source of truth.
- Source inspection: `594x360`; notebook chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-06-prepare-request-source-clean.png`, coordinates `500x290+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `create_preprocessor`, `xception`, `(299, 299)`, the pants URL, `np_to_protobuf`, `clothing-model`, `serving_default`, and `input_8` remain exact.
- Output: `images/02-tensorflow-serving-06-prepare-request-cropped.jpg`.

### `02-tensorflow-serving-07-prediction.jpg`

- Lesson: `02-tensorflow-serving.md`; caption: Turning the raw scores into class names.
- Disposition: deterministic crop/prep; this is an exact UI screenshot, but its visible content must not be reconstructed with imagegen.
- Source inspection: `594x360`; GitHub browser chrome, profile/contributor avatars, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/02-tensorflow-serving-07-prediction-source-clean.png`, coordinates `380x280+0+40`; resized 2x with Lanczos and light unsharp masking, excluding browser header/sidebar avatars.
- Invariants checked: the visible repository listing remains exact; no generated text or inferred prediction output was added.
- Limitation: the supplied source does not show raw scores or class names despite the caption; the crop removes unrelated avatars/chrome but cannot repair this source-content mismatch.
- Output: `images/02-tensorflow-serving-07-prediction-cropped.jpg`.

### `03-preprocessing-01-nbconvert.jpg`

- Lesson: `03-preprocessing.md`; caption: Converting the notebook with jupyter nbconvert.
- Disposition: deterministic crop/prep; exact terminal command and server output are the source of truth.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-01-nbconvert-source-clean.png`, coordinates `490x285+10+25`, then top `14px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: the notebook server output, model files, `jupyter nbconvert` command, and visible status lines remain exact.
- Limitation: the source itself truncates the first character of the directory path and the lower conversion output; no text was guessed or reconstructed.
- Output: `images/03-preprocessing-01-nbconvert-cropped.jpg`.

### `03-preprocessing-02-gateway-script.jpg`

- Lesson: `03-preprocessing.md`; caption: Preparing the request and invoking the model in the gateway script.
- Disposition: deterministic crop/prep; exact Python, URL, model, signature, and timeout code are the source of truth.
- Source inspection: `594x360`; editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-02-gateway-script-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `clothing-model`, `serving_default`, `input_8`, `np_to_protobuf`, the pants URL, and `timeout=20.0` remain exact.
- Output: `images/03-preprocessing-02-gateway-script-cropped.jpg`.

### `03-preprocessing-03-flask-app.jpg`

- Lesson: `03-preprocessing.md`; caption: The Flask app part of `gateway.py`.
- Disposition: deterministic crop/prep; the visible Python source is exact and must not be approximated with imagegen.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-03-flask-app-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: Flask imports, model loading, `/predict` route, request handling, churn threshold, JSON keys, and `jsonify` call remain unchanged.
- Limitation: the source screenshot is intrinsically low-resolution and text remains softer than the other crops; no generated approximation was used because code fidelity is required.
- Output: `images/03-preprocessing-03-flask-app-cropped.jpg`.

### `03-preprocessing-04-pipenv-install.jpg`

- Lesson: `03-preprocessing.md`; caption: Installing the dependencies with pipenv and testing the gateway.
- Disposition: deterministic crop/prep; exact shell output, package versions, and prediction values are the source of truth.
- Source inspection: `594x360`; editor/browser chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-04-pipenv-install-source-clean.png`, coordinates `460x300+20+30`, then top `8px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `grpcio==1.42.0`, Flask, gunicorn, `keras-image-helper`, Python `3.8.10`, virtualenv creation, and visible prediction values remain exact.
- Limitation: long terminal lines retain the source-edge truncation; no output was guessed or expanded.
- Output: `images/03-preprocessing-04-pipenv-install-cropped.jpg`.

### `03-preprocessing-05-tensorflow-protobuf.jpg`

- Lesson: `03-preprocessing.md`; caption: The tensorflow-protobuf README: the verbose version without the baggage.
- Disposition: deterministic crop/prep; exact protobuf Python code is the source of truth.
- Source inspection: `594x360`; browser chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-05-tensorflow-protobuf-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `make_tensor_proto`, shape/dims conversion, dtype conversion, `TensorProto`, `tensor_content`, and `np_to_protobuf` remain exact.
- Output: `images/03-preprocessing-05-tensorflow-protobuf-cropped.jpg`.

### `03-preprocessing-06-proto-py.jpg`

- Lesson: `03-preprocessing.md`; caption: The `proto.py` script with the protobuf conversion code.
- Disposition: deterministic crop/prep; exact Python conversion code is the source of truth.
- Source inspection: `594x360`; editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/03-preprocessing-06-proto-py-source-clean.png`, coordinates `500x320+0+20`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `dtypes_as_dtype`, `DT_FLOAT`, shape/dims conversion, `TensorShapeProto`, `TensorProto`, and `tensor_content` remain exact.
- Limitation: the source itself truncates long right-side code lines; the crop does not invent or reflow them.
- Output: `images/03-preprocessing-06-proto-py-cropped.jpg`.

### `04-docker-compose-01-model-image.jpg`

- Lesson: `04-docker-compose.md`; caption: Building the model image and running it: TensorFlow Serving loads the model successfully.
- Disposition: deterministic crop/prep; exact TensorFlow Serving logs and Docker build command are the source of truth.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/04-docker-compose-01-model-image-source-clean.png`, coordinates `500x320+0+20`, then top `20px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: model load success, gRPC/HTTP endpoints, event loop, and `docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .` remain exact.
- Output: `images/04-docker-compose-01-model-image-cropped.jpg`.

### `04-docker-compose-02-gateway-image.jpg`

- Lesson: `04-docker-compose.md`; caption: Building the gateway image.
- Disposition: deterministic crop/prep; exact file list, prediction output, and Docker build command are the source of truth.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/04-docker-compose-02-gateway-image-source-clean.png`, coordinates `500x320+0+20`, then top `20px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `gateway.py`, `image-gateway.dockerfile`, prediction keys/values, and `docker build -t zoomcamp-10-gateway:001 -f image-gateway.dockerfile .` remain exact.
- Output: `images/04-docker-compose-02-gateway-image-cropped.jpg`.

### `04-docker-compose-03-isolated-containers.jpg`

- Lesson: `04-docker-compose.md`; caption: Two isolated containers: each maps its port to the host, but they cannot reach each other.
- Disposition: imagegen replacement; the source is a bounded Docker networking diagram.
- Source inspection: `594x360`; camera tile, playback controls, and a green edge overlay present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/04-docker-compose-03-isolated-containers-source-clean.png`, coordinates `450x320+50+20`; overlays removed before generation.
- Invariants checked: outer `UBUNTU - HOST`, separate `GATEWAY`/`FLASK` and `TF-SERVING`/`TFSERVING` areas, ports `9696` and `8500`, host mappings, and `TEST.PY` connections.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra container remains.
- Output: `images/04-docker-compose-03-isolated-containers-imagegen.jpg`.

### `04-docker-compose-04-compose-file.jpg`

- Lesson: `04-docker-compose.md`; caption: The docker-compose file with the two services.
- Disposition: deterministic focused crop/prep; the YAML values are exact and must not be regenerated.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, terminal panel, and native text-selection highlights present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/04-docker-compose-04-compose-file-source-clean.png`, coordinates `500x215+0+20`, then top `20px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: Compose version `3.9`, both service names/images, `TF_SERVING_HOST=clothing-model:8500`, and `9696:9696` remain exact.
- Limitation: native editor selection highlights remain because removing pixels from exact YAML text would risk damaging the code; unrelated terminal output and webcam/chrome are cropped away.
- Output: `images/04-docker-compose-04-compose-file-cropped.jpg`.

### `04-docker-compose-05-compose-up.jpg`

- Lesson: `04-docker-compose.md`; caption: docker-compose up: both services start.
- Disposition: deterministic crop/prep; exact container logs and successful model-load status are the source of truth.
- Source inspection: `594x360`; browser/editor chrome, webcam tile, and right-side strip present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/04-docker-compose-05-compose-up-source-clean.png`, coordinates `500x320+0+20`, then top `20px` shaved; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: gateway/gunicorn startup, `localhost:9696`, TensorFlow Serving model load, `clothing-model` version `1`, and `Status: success: OK` remain exact.
- Limitation: the source itself truncates some long log lines at both edges; no log text was guessed or expanded.
- Output: `images/04-docker-compose-05-compose-up-cropped.jpg`.

### `05-kubernetes-intro-01-cluster-nodes-pods.jpg`

- Lesson: `05-kubernetes-intro.md`; caption: A cluster with two nodes, each running pods.
- Disposition: imagegen replacement; the source is a bounded Kubernetes cluster diagram.
- Source inspection: `596x360`; webcam sliver and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/05-kubernetes-intro-01-cluster-nodes-pods-source-clean.png`, coordinates `475x360+23+0`.
- Invariants checked: one `CLUSTER`, exactly two stacked `NODE` regions, pods inside each node, and the labels `10.5 INTRODUCTION TO KUBERNETES`, `CLUSTER`, `NODE`, and `POD`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or unrelated Kubernetes component remains.
- Output: `images/05-kubernetes-intro-01-cluster-nodes-pods-imagegen.jpg`.

### `05-kubernetes-intro-02-deployments.jpg`

- Lesson: `05-kubernetes-intro.md`; caption: Two deployments: gateway pods and TF-Serving pods, each with the same image and config.
- Disposition: imagegen replacement; the source is a bounded Kubernetes deployment diagram.
- Source inspection: `596x360`; webcam tile, recording controls, and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/05-kubernetes-intro-02-deployments-source-clean.png`, coordinates `475x360+23+0`; resized 2x with Lanczos and light unsharp masking before generation.
- Invariants checked: one `CLUSTER` boundary, exactly two stacked `NODE` regions, a gateway deployment and a TF-Serving deployment spanning both nodes, exactly one gateway pod and one TF-Serving pod in each node, and same-image/config relationships.
- Prompt iteration: first generation was rejected because it duplicated pods within each node and changed the topology; a targeted correction restored exactly four pods distributed one per deployment per node.
- Output: `images/05-kubernetes-intro-02-deployments-imagegen.jpg`.

### `05-kubernetes-intro-03-services.jpg`

- Lesson: `05-kubernetes-intro.md`; caption: The user talks to the gateway service; the gateway talks to the model service.
- Disposition: deterministic crop/prep; the diagram's exact arrows, labels, and pod placement are the source of truth.
- Source inspection: `596x360`; webcam tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/05-kubernetes-intro-03-services-source-clean.png`, coordinates `475x360+23+0`; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: client, gateway service, model service, cluster, two nodes, gateway and TF-Serving pods, and the handwritten same-image/config annotations remain visible; recording overlays are excluded.
- Limitation: deterministic preparation preserves the source's hand-drawn lettering and source-edge composition; no text or topology was reconstructed.
- Output: `images/05-kubernetes-intro-03-services-cropped.jpg`.

### `05-kubernetes-intro-04-external-internal-ingress.jpg`

- Lesson: `05-kubernetes-intro.md`; caption: External and internal services, with ingress in front of the cluster.
- Disposition: imagegen replacement; this is a bounded Kubernetes service/ingress diagram.
- Source inspection: `950x720` prepared source-clean crop; webcam face and black side bars are excluded.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/05-kubernetes-intro-04-external-internal-ingress-source-clean.png`, full prepared crop; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: `INGRESS`, `EXTERNAL`, `INTERNAL`, gateway/model services, two nodes, both deployments, pod placement, request arrows, and same-image/config annotations remain unchanged.
- Prompt constraint: preserve the exact service boundaries, arrows, labels, pod placement, and Kubernetes relationships while removing the recording UI and face/camera artifacts.
- Output: `images/05-kubernetes-intro-04-external-internal-ingress-imagegen.jpg`.

### `05-kubernetes-intro-05-definitions.jpg`

- Lesson: `05-kubernetes-intro.md`; caption: The whiteboard definitions: node, pod, deployment, service, ingress.
- Disposition: imagegen replacement; this is a bounded Kubernetes definitions whiteboard.
- Source inspection: `950x720` prepared source-clean crop; webcam face and black side bars are excluded.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/05-kubernetes-intro-05-definitions-source-clean.png`, full prepared crop; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: the definitions of `NODE`, `POD`, `DEPLOYMENT`, `SERVICE`, `EXTERNAL`, `INTERNAL`, and `INGRESS` remain exact and readable.
- Prompt constraint: preserve every handwritten definition and line break while removing the recording UI and face/camera artifacts.
- Output: `images/05-kubernetes-intro-05-definitions-imagegen.jpg`.

### `05-kubernetes-intro-06-scaling.jpg`

- Lesson: `05-kubernetes-intro.md`; caption: More users, more pods: Kubernetes scales the deployments up.
- Disposition: imagegen replacement; this is a bounded Kubernetes scaling diagram.
- Source inspection: `950x720` prepared source-clean crop; webcam face and black side bars are excluded.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/05-kubernetes-intro-06-scaling-source-clean.png`, full prepared crop; resized 2x with Lanczos and light unsharp masking.
- Invariants checked: multiple users, ingress, external/internal services, gateway and model deployments, additional gateway pods, and the two-node cluster remain unchanged.
- Prompt constraint: preserve the users, arrows, added pods, deployment boundaries, labels, and scaling relationship while removing recording UI and face/camera artifacts.
- Output: `images/05-kubernetes-intro-06-scaling-imagegen.jpg`.

## Lesson 05 validation

- Six lesson-05 image references resolve: `01-cluster-nodes-pods-imagegen.png`, `02-deployments-imagegen.png`, `03-services-cropped.png`, `04-external-internal-ingress-imagegen.png`, `05-definitions-imagegen.png`, and `06-scaling-imagegen.png`.
- All six original `.jpg` assets remain in `cohorts/2026/10-kubernetes/images/`.
- The services asset uses deterministic crop/prep; the ingress, definitions, and scaling assets use imagegen after source inspection and prompt constraints.
- `git diff --check` passes.
