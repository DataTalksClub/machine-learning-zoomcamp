# ML intro screenshot rollout: 05–07

## 05-model-selection

### 01 — train-validation

- Source: `cohorts/2026/01-intro/images/05-model-selection-01-train-validation.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-01-train-validation-imagegen-pilot.png`
- Crop: `465×305+35+30` (deterministic crop before generation)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: `TRAIN` and `VAL` columns; `X`, `y`, `Xᵥ`, `yᵥ`; `g`; `g(Xᵥ)`; arrows from each split to its inputs and model notation; left/right order and training-versus-validation meaning
- Validation: passed visual review; crisp at lesson size; labels and subscripts are legible; no face, webcam tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, extra label, or extra metric

### 02 — multiple-comparisons

- Source: `cohorts/2026/01-intro/images/05-model-selection-02-multiple-comparisons.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-02-multiple-comparisons-imagegen-pilot.png`
- Crop: `500×250+0+90` (deterministic crop before generation)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: title `Multiple comparisons problem`; `20%` badge; exactly five email examples; exactly five coin models; same-validation-set versus multiple-coin-model teaching point
- Validation: final third iteration accepted after rejecting a first variant that kept a blue scribble/currency markings and a second variant with incomplete arrows; final is crisp and contains no face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, arrows, extra labels, currency text, or invented metrics

### 03 — train-valid-test

- Source: `cohorts/2026/01-intro/images/05-model-selection-03-train-valid-test.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-03-train-valid-test-imagegen-pilot.png`
- Crop: `500×300+0+30` (deterministic crop before generation; excludes the webcam tile and recording frame)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: title `Validation & Test`; contiguous `60%`, `20%`, `20%` split; downward mapping to `TRAIN`, `VALID`, `TEST`; `g`, `X`, `y`, `Xᵥ`, `yᵥ`, `NN`; test held out as the final partition
- Validation: passed visual review; all labels, percentages, order, arrows, and split meaning are legible and intact; no face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, clipped box, or extra metric

### 04 — select-and-test

- Source: `cohorts/2026/01-intro/images/05-model-selection-04-select-and-test.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-04-select-and-test-imagegen-pilot.png`
- Crop: `500×260+0+70` (deterministic crop before generation; removes the webcam tile and recording frame)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: candidate rows `LR / 66%`, `DT / 60%`, `RF / 67%`, selected `NN / 80%`, and final `TEST` check; selected row and arrow relationship
- Validation: accepted on the second generation after rejecting a faint handwritten artifact in the first table cell; final is crisp with exact labels/values, no scribbles, face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, clipped content, or extra metric

## 06-environment

### 01 — create-repo

- Source: `cohorts/2026/01-intro/images/06-environment-01-create-repo.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-01-create-repo-cropped.png`
- Crop: `500×314+0+46` (removes browser chrome and the webcam tile while retaining the GitHub repository form)
- Path: deterministic lossless PNG crop; imagegen not used because exact UI text and controls are the source of truth
- Invariants: GitHub `New repository` / `Create a new repository`; `No template`; `Owner`; `Repository name`; repository-form context
- Validation: passed visual review; exact UI text remains readable; no face, camera tile, browser tab/address chrome, cursor, watermark, recording overlay, or black border

### 02 — create-codespace

- Source: `cohorts/2026/01-intro/images/06-environment-02-create-codespace.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-02-create-codespace-cropped.png`
- Crop: `520×322+0+38` (removes browser chrome and the webcam tile while retaining the Codespaces menu and target button)
- Path: deterministic lossless PNG crop; imagegen not used because exact GitHub UI text and controls are the source of truth
- Invariants: repository page context; `Code` menu with `Codespaces`; `No codespaces`; `Create codespace on main`; visible repository navigation
- Validation: exact UI text and button are readable; face, camera tile, browser tab/address chrome, watermark, recording overlay, and black border are gone. Limitation: the original pointer remains over the required click target because removing it deterministically would damage the exact button label; it is retained as an instructional click cue.

### 03 — vscode-desktop

- Source: `cohorts/2026/01-intro/images/06-environment-03-vscode-desktop.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-03-vscode-desktop-cropped.png`
- Crop: `520×360+0+0` (removes the webcam tile at the right edge; VS Code chrome is retained because it is the demonstrated environment)
- Path: deterministic lossless PNG crop; imagegen not used because exact editor and terminal UI are the source of truth
- Invariants: VS Code desktop interface; `README.md` tab; `Hello world`; integrated terminal and Codespaces context
- Validation: passed visual review; editor text and terminal context remain readable; no face, camera tile, recording/browser overlay, cursor, watermark, or black border
