# ML intro screenshot rollout: 05–07

## 05-model-selection

### 01 — train-validation

- Source: `cohorts/2026/01-intro/images/05-model-selection-01-train-validation.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-01-train-validation-imagegen-pilot.jpg`
- Crop: `465×305+35+30` (deterministic crop before generation)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: `TRAIN` and `VAL` columns; `X`, `y`, `Xᵥ`, `yᵥ`; `g`; `g(Xᵥ)`; arrows from each split to its inputs and model notation; left/right order and training-versus-validation meaning
- Validation: passed visual review; crisp at lesson size; labels and subscripts are legible; no face, webcam tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, extra label, or extra metric

### 02 — multiple-comparisons

- Source: `cohorts/2026/01-intro/images/05-model-selection-02-multiple-comparisons.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-02-multiple-comparisons-imagegen-pilot.jpg`
- Crop: `500×250+0+90` (deterministic crop before generation)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: title `Multiple comparisons problem`; `20%` badge; exactly five email examples; exactly five coin models; same-validation-set versus multiple-coin-model teaching point
- Validation: final third iteration accepted after rejecting a first variant that kept a blue scribble/currency markings and a second variant with incomplete arrows; final is crisp and contains no face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, arrows, extra labels, currency text, or invented metrics

### 03 — train-valid-test

- Source: `cohorts/2026/01-intro/images/05-model-selection-03-train-valid-test.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-03-train-valid-test-imagegen-pilot.jpg`
- Crop: `500×300+0+30` (deterministic crop before generation; excludes the webcam tile and recording frame)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: title `Validation & Test`; contiguous `60%`, `20%`, `20%` split; downward mapping to `TRAIN`, `VALID`, `TEST`; `g`, `X`, `y`, `Xᵥ`, `yᵥ`, `NN`; test held out as the final partition
- Validation: passed visual review; all labels, percentages, order, arrows, and split meaning are legible and intact; no face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, clipped box, or extra metric

### 04 — select-and-test

- Source: `cohorts/2026/01-intro/images/05-model-selection-04-select-and-test.jpg` (598×360 JPEG)
- Disposition: accepted imagegen sibling `05-model-selection-04-select-and-test-imagegen-pilot.jpg`
- Crop: `500×260+0+70` (deterministic crop before generation; removes the webcam tile and recording frame)
- Path: built-in imagegen, `scientific-educational`; imagegen skill available and read
- Invariants: candidate rows `LR / 66%`, `DT / 60%`, `RF / 67%`, selected `NN / 80%`, and final `TEST` check; selected row and arrow relationship
- Validation: accepted on the second generation after rejecting a faint handwritten artifact in the first table cell; final is crisp with exact labels/values, no scribbles, face, camera tile, browser/Zoom chrome, cursor, watermark, recording overlay, black border, clipped content, or extra metric

## 06-environment

### 01 — create-repo

- Source: `cohorts/2026/01-intro/images/06-environment-01-create-repo.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-01-create-repo-cropped.jpg`
- Crop: `500×314+0+46` (removes browser chrome and the webcam tile while retaining the GitHub repository form)
- Path: deterministic lossless PNG crop; imagegen not used because exact UI text and controls are the source of truth
- Invariants: GitHub `New repository` / `Create a new repository`; `No template`; `Owner`; `Repository name`; repository-form context
- Validation: passed visual review; exact UI text remains readable; no face, camera tile, browser tab/address chrome, cursor, watermark, recording overlay, or black border

### 02 — create-codespace

- Source: `cohorts/2026/01-intro/images/06-environment-02-create-codespace.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-02-create-codespace-cropped.jpg`
- Crop: `520×322+0+38` (removes browser chrome and the webcam tile while retaining the Codespaces menu and target button)
- Path: deterministic lossless PNG crop; imagegen not used because exact GitHub UI text and controls are the source of truth
- Invariants: repository page context; `Code` menu with `Codespaces`; `No codespaces`; `Create codespace on main`; visible repository navigation
- Validation: exact UI text and button are readable; face, camera tile, browser tab/address chrome, watermark, recording overlay, and black border are gone. Limitation: the original pointer remains over the required click target because removing it deterministically would damage the exact button label; it is retained as an instructional click cue.

### 03 — vscode-desktop

- Source: `cohorts/2026/01-intro/images/06-environment-03-vscode-desktop.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-03-vscode-desktop-cropped.jpg`
- Crop: `520×360+0+0` (removes the webcam tile at the right edge; VS Code chrome is retained because it is the demonstrated environment)
- Path: deterministic lossless PNG crop; imagegen not used because exact editor and terminal UI are the source of truth
- Invariants: VS Code desktop interface; `README.md` tab; `Hello world`; integrated terminal and Codespaces context
- Validation: passed visual review; editor text and terminal context remain readable; no face, camera tile, recording/browser overlay, cursor, watermark, or black border

### 04 — push-pip-install

- Source: `cohorts/2026/01-intro/images/06-environment-04-push-pip-install.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-04-push-pip-install-cropped.jpg`
- Crop: `640×260+0+100` (removes the webcam tile and upper recording frame while retaining the terminal output and `pip install` command)
- Path: deterministic lossless PNG crop; imagegen not used because exact shell output and command text are the source of truth
- Invariants: VS Code terminal; `git push`; object-count/output lines; GitHub remote; visible `pip install` command; terminal context
- Validation: passed visual review; command/output text remains exact and readable; no face, camera tile, browser/recording chrome, watermark, or black border

### 05 — jupyter-notebook

- Source: `cohorts/2026/01-intro/images/06-environment-05-jupyter-notebook.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-05-jupyter-notebook-cropped.jpg`
- Crop: `510×270+0+90` (removes browser chrome and the webcam tile while retaining the Jupyter toolbar, `JupyterLab`, kernel context, and `import pandas as pd` cell)
- Path: deterministic lossless PNG crop; imagegen not used because exact notebook UI and code are the source of truth
- Invariants: Jupyter toolbar; `JupyterLab`; `Python 3 (ipykernel)` context; `import pandas as pd`; notebook cell area
- Validation: passed visual review; exact code and UI labels are readable; no face, camera tile, browser tab/address chrome, watermark, recording overlay, or black border

### 06 — homework-notebook

- Source: `cohorts/2026/01-intro/images/06-environment-06-homework-notebook.jpg` (640×360 JPEG)
- Disposition: accepted deterministic sibling `06-environment-06-homework-notebook-cropped.jpg`
- Crop: `510×360+0+0` (removes the webcam tile at the right edge; retains VS Code, notebook, code cell, and terminal)
- Path: deterministic lossless PNG crop; imagegen not used because exact notebook/terminal UI, code, URL, and output are the source of truth
- Invariants: `homework.ipynb`; `import pandas as pd`; `pd.read_csv(...)` cell; terminal with Jupyter server/token context; Codespaces/VS Code context
- Validation: passed visual review; exact code and terminal output remain readable; no face, camera tile, recording/browser overlay, watermark, or black border

### 07 — sample-jupyter-notebook

- Source: `cohorts/2026/01-intro/images/sample-jupyter-notebook.jpg` (1266×494 PNG)
- Disposition: accepted deterministic sibling `sample-jupyter-notebook-cropped.jpg`
- Crop: `560×374+20+120` (trims GitHub navigation while retaining the repository breadcrumb, notebook filename, context menu, and `Copy link address` target)
- Path: deterministic lossless PNG crop; imagegen not used because exact GitHub UI, filename, menu labels, and instructional annotation are the source of truth
- Invariants: `mlbookcamp-code / chapter-02-car-price`; `02-carprice.ipynb`; context menu; `Copy link address`; red instructional highlight
- Validation: passed visual review; exact UI text and annotation remain crisp; no face, camera tile, browser/recording overlay, watermark, cursor, or black border

### 10 — add-code-for-datafile-download

- Source: `cohorts/2026/01-intro/images/add-code-for-datafile-download.jpg` (1299×564 PNG)
- Disposition: accepted deterministic sibling `add-code-for-datafile-download-cropped.jpg`
- Crop: `1200×440+70+90` (trims outer notebook chrome while retaining the exact import cell, `wget` URL, `pd.read_csv('data.csv')`, output, and red instructional highlight)
- Path: deterministic lossless PNG crop; imagegen not used because exact Python, shell command, URL, output, and annotation are the source of truth
- Invariants: `!wget https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv`; `df = pd.read_csv('data.csv')`; `len(df)` output `11914`; red highlight
- Validation: passed visual review; exact code, URL, output, and annotation remain crisp; no face, camera tile, browser/recording overlay, watermark, cursor, or black border

## 07-numpy

### 01 — zeros-ones-full

- Source: `cohorts/2026/01-intro/images/07-numpy-01-zeros-ones-full.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-01-zeros-ones-full-cropped.jpg`
- Crop: `500×290+0+40` (removes the browser frame and webcam tile; retains the NumPy notebook toolbar, `np.ones(10)`, `np.full(10, 2.5)`, exact outputs, and section context)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code and numeric output are the source of truth
- Invariants: `np.ones(10)` and all ten `1.` values; `np.full(10, 2.5)` and all ten `2.5` values; visible zeros output; `Multi-dimensional arrays` context
- Validation: passed visual review; code and numeric output remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 02 — array-from-list

- Source: `cohorts/2026/01-intro/images/07-numpy-02-array-from-list.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-02-array-from-list-cropped.jpg`
- Crop: `500×240+0+90` (removes browser frame and webcam tile; retains the NumPy cells and outputs)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code and output are the source of truth
- Invariants: `a = np.array([1, 2, 3, 5, 7, 12])`; output `[1, 2, 3, 5, 7, 12]`; `a[2] = 10`; final output `[1, 2, 10, 5, 7, 12]`; blue instructional circle around index `2`
- Validation: passed visual review; code, values, and annotation remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 03 — two-d-arrays

- Source: `cohorts/2026/01-intro/images/07-numpy-03-two-d-arrays.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-03-two-d-arrays-cropped.jpg`
- Crop: `500×290+0+70` (removes browser frame and webcam tile; retains the matrix construction, index assignment, outputs, and notebook toolbar)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code, matrix values, and output are the source of truth
- Invariants: `n = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`; `n[0, 1] = 20`; output begins `[[1, 20, 3], [4, 5, 6], [7, 8, 9]]`; blue instructional marks
- Validation: passed visual review; code, values, and annotations remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 04 — columns

- Source: `cohorts/2026/01-intro/images/07-numpy-04-columns.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-04-columns-cropped.jpg`
- Crop: `500×250+0+85` (removes browser frame and webcam tile; retains the matrix, column assignment, outputs, and section context)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code and matrix output are the source of truth
- Invariants: matrix `n`; `n[:, 2] = [0, 1, 2]`; final output `[[1, 20, 0], [4, 5, 1], [1, 1, 2]]`; `Randomly generated arrays` context
- Validation: passed visual review; code and matrix values remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 05 — random-seed

- Source: `cohorts/2026/01-intro/images/07-numpy-05-random-seed.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-05-random-seed-cropped.jpg`
- Crop: `500×220+0+100` (removes browser frame and webcam tile; retains the section heading, seed commands, exact 5×2 output, and next-section context)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy commands and numeric output are the source of truth
- Invariants: `np.random.seed(2)`; `np.random.rand(5, 2)`; all five rows and two columns of output; `Randomly generated arrays` / `Element-wise operations` headings
- Validation: passed visual review; code and all numeric values remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 06 — element-wise

- Source: `cohorts/2026/01-intro/images/07-numpy-06-element-wise.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-06-element-wise-cropped.jpg`
- Crop: `500×200+0+100` (removes browser frame and webcam tile; retains the element-wise heading, array construction, multiplication, exact outputs, and next-section context)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code and numeric output are the source of truth
- Invariants: `a = np.arange(5)`; output `[0, 1, 2, 3, 4]`; `a * 2`; output `[0, 2, 4, 6, 8]`; `Element-wise operations` / `Comparison operations` headings
- Validation: passed visual review; code and values remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 07 — comparison

- Source: `cohorts/2026/01-intro/images/07-numpy-07-comparison.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-07-comparison-cropped.jpg`
- Crop: `500×185+0+135` (removes browser frame and webcam tile; retains the comparison heading, `a`, `a >= 2`, exact Boolean output, and next-section context)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code and Boolean values are the source of truth
- Invariants: `a` output `[0, 1, 2, 3, 4]`; `a >= 2`; output `[False, False, True, True, True]`; `Comparison operations` / `Summarizing operations` headings
- Validation: passed visual review; code and Boolean output remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 08 — summarizing

- Source: `cohorts/2026/01-intro/images/07-numpy-08-summarizing.jpg` (598×360 JPEG)
- Disposition: accepted deterministic sibling `07-numpy-08-summarizing-cropped.jpg`
- Crop: `500×230+0+100` (removes browser frame and webcam tile; retains the summarizing heading, `a`, exact array output, `a.mean()`, `2.0`, and next-lesson context)
- Path: deterministic lossless PNG crop; imagegen not used because exact NumPy code and numeric output are the source of truth
- Invariants: `a` output `[0, 1, 2, 3, 4]`; `a.mean()`; output `2.0`; `Summarizing operations`; `Next` / `Linear algebra refresher`
- Validation: passed visual review; code and numeric output remain exact and readable; no face, camera tile, browser/recording chrome, watermark, cursor, or black border

### 08 — sample-code

- Source: `cohorts/2026/01-intro/images/sample-code.jpg` (1299×550 PNG)
- Disposition: accepted deterministic sibling `sample-code-cropped.jpg`
- Crop: `930×450+70+100` (trims notebook navigation/sidebar while retaining the code cells, output, and red instructional highlight)
- Path: deterministic lossless PNG crop; imagegen not used because exact Python code, output, and UI annotation are the source of truth
- Invariants: `import pandas as pd`; `import numpy as np`; `import seaborn as sns`; `df = pd.read_csv('data.csv')`; `len(df)` output `11914`; red highlight around the CSV read
- Validation: passed visual review; exact code, output, and annotation remain crisp; no face, camera tile, browser/recording overlay, watermark, cursor, or black border

### 09 — sample-data-file

- Source: `cohorts/2026/01-intro/images/sample-data-file.jpg` (1296×529 PNG)
- Disposition: accepted deterministic sibling `sample-data-file-cropped.jpg`
- Crop: `500×409+20+120` (trims GitHub navigation while retaining the repository file list, `data.csv`, context menu, `Copy link address`, and red instructional highlight)
- Path: deterministic lossless PNG crop; imagegen not used because exact GitHub UI, filename, menu labels, and annotation are the source of truth
- Invariants: `mlbookcamp-code / chapter-02-car-price`; `data.csv`; context menu; `Copy link address`; red instructional arrow/highlight
- Validation: passed visual review; exact UI text and annotation remain crisp; no face, camera tile, browser/recording overlay, watermark, cursor, or black border
