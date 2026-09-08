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
