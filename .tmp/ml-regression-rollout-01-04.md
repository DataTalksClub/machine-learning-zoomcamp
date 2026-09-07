# Regression intro screenshot rollout

## 01 — select best price

- Disposition: `keep` via deterministic crop/export; the image teaches the user-facing price-entry problem that motivates the car-price model.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-01-select-best-price.jpg`; caption: “How can we help our user select the best price”.
- Crop coordinates: source `598x360`; `504x336+0+24` (`x=0, y=24, width=504, height=336`). The crop removes the DataTalks.Club watermark, top-left recording marker, webcam tile, right black bar, and keeps the slide content.
- Invariants: preserve the title “How can we help our user select the best price?”, the thinking figure with phone, the Price/Exchange control, the `$0000?` field, the `UAH` selector, and the red “Required field” state.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-01-select-best-price-cropped.jpg`.
- QA: source inspected in lesson context; exact UI/text preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `504x336`; lesson reference resolves; `git diff --check` passes before commit.

## 02 — Kaggle dataset

- Disposition: `crop/replace` via deterministic crop/export; the image teaches which Kaggle dataset supplies the car features and MSRP used in the project.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-02-kaggle-dataset.jpg`; caption: “Car Features and MSRP dataset on Kaggle”.
- Crop coordinates: source `598x360`; `539x246+18+58` (`x=18, y=58, width=539, height=246`). The crop removes the top watermark, webcam tile, recording frame, right black bar, bottom control strip, and presenter pointer while retaining the Kaggle page content.
- Invariants: preserve the exact Kaggle dataset banner “Car Features and MSRP”, feature description, author/version line, tabs, download/new-notebook controls, usability/tags row, “Context” heading and dataset description, and “Content” heading.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-02-kaggle-dataset-cropped.jpg`.
- QA: source and candidate crops inspected visually; exact UI/text preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, black border, or presenter pointer remains; final dimensions `539x246`; lesson reference resolves; `git diff --check` passes before commit.

## 03 — Kaggle data explorer

- Disposition: `crop/replace` via deterministic crop/export; the image teaches that the Kaggle data explorer exposes one row per car and multiple feature columns.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-03-kaggle-data-explorer.jpg`; caption: “Kaggle data explorer showing the car dataset columns”.
- Crop coordinates: source `598x360`; `576x283+0+58` (`x=0, y=58, width=576, height=283`). The crop removes browser chrome, the webcam tile/face, the right black bar, and the bottom recording strip.
- Invariants: preserve the Kaggle left navigation, `data.csv` explorer, Detail/Compact/Column tabs, “About this file”, feature-column headers and distributions, visible car rows, and the Summary showing 16 columns.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-03-kaggle-data-explorer-cropped.jpg`.
- QA: source and candidate crops inspected visually; exact UI, labels, row values, and column relationships preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `576x283`; lesson reference resolves; `git diff --check` passes before commit.

## 04 — MSRP column

- Disposition: `crop/replace` via deterministic crop/export; the image teaches that `MSRP` is the target price column in the car dataset.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-04-msrp-column.jpg`; caption: “The MSRP column contains the price of each car”.
- Crop coordinates: source `598x360`; `576x283+0+58` (`x=0, y=58, width=576, height=283`). The crop removes browser chrome, the webcam tile/face, the right black bar, and the bottom recording strip.
- Invariants: preserve the Kaggle Data Explorer, `data.csv (1.41 MB)`, visible feature headers and rows, the rightmost `MSRP` column, and its exact visible numeric prices.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-04-msrp-column-cropped.jpg`.
- QA: source and candidate crop inspected visually; exact UI, `MSRP` values, headers, and row relationships preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `576x283`; lesson reference resolves; `git diff --check` passes before commit.

## 05 — project plan

- Disposition: `crop/replace` via deterministic crop/export; the image teaches the sequence of work planned for the car-price project.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-05-project-plan.jpg`; caption: “Project plan slide”.
- Crop coordinates: source `598x360`; `485x317+20+23` (`x=20, y=23, width=485, height=317`). The crop removes the top watermark/recording marker, webcam tile, right black bar, cursor in the blank area, and bottom controls.
- Invariants: preserve the exact title “Project plan” and all seven bullets: EDA, linear regression, internals of linear regression, RMSE evaluation, feature engineering, regularization, and using the model.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-05-project-plan-cropped.jpg`.
- QA: source and candidate crop inspected visually; exact slide text and ordering preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `485x317`; lesson reference resolves; `git diff --check` passes before commit.

## 06 — GitHub repository

- Disposition: `crop/replace` via deterministic crop/export; the image teaches where the `chapter-02-car-price` project directory lives in the `mlbookcamp-code` repository.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-06-github-repo.jpg`; caption: “The mlbookcamp-code repository with chapter-02-car-price”.
- Crop coordinates: source `598x360`; `530x283+47+57` (`x=47, y=57, width=530, height=283`). The crop removes the watermark, top recording/webcam area, captured avatar/commit strip, left recording controls, right black bar, and bottom recording strip.
- Invariants: preserve the GitHub repository file list, the first `chapter-02-car-price` folder row, neighboring chapter folders, commit messages, timestamps, and the repository’s exact folder/file labels.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-06-github-repo-cropped.jpg`.
- QA: source and candidate crop inspected visually; exact GitHub UI labels and folder ordering preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `530x283`; lesson reference resolves; `git diff --check` passes before commit.

## 07 — chapter files

- Disposition: `crop/replace` via deterministic crop/export; the image teaches that the project folder contains the notebook and the `data.csv` dataset.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-07-chapter-files.jpg`; caption: “The notebook and the data file in chapter-02-car-price”.
- Crop coordinates: source `598x360`; `546x68+15+215` (`x=15, y=215, width=546, height=68`). The crop removes browser chrome, the webcam/face, native avatar and commit/navigation rows, footer, and other recording-frame material.
- Invariants: preserve the exact file rows `02-carprice.ipynb` and `data.csv`, their visible commit messages (`chapter 02 update` and `chapter 2 code`), and their timestamps.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-07-chapter-files-cropped.jpg`.
- QA: source and candidate crops inspected visually; exact filenames, row order, labels, and timestamps preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `546x68`; lesson reference resolves; `git diff --check` passes before commit.

## 08 — download data

- Disposition: `keep` via deterministic crop/export; the screenshot teaches that `wget` downloads the CSV from the raw GitHub URL and saves it locally as `data.csv`.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-01-download-data.jpg`; caption: “Downloading data.csv with wget”.
- Crop coordinates: source `598x360`; `577x306+0+54` (`x=0, y=54, width=577, height=306`). The crop removes the notebook/browser header, webcam tile, right black strip, and recording-frame area while retaining the data URL cell, `!wget $data`, download URL/output, `200 OK`, progress line, and saved-file line.
- Invariants: preserve the exact `!wget $data` command, raw GitHub URL/output, HTTP 200 result, `data.csv` filename, byte count, progress result, and the relationship that the command writes the local CSV.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-01-download-data-cropped.jpg`.
- QA: source inspected in lesson context; exact command, URL, output, values, and order preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `577x306`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 09 — read_csv and df.head()

- Disposition: `keep` via deterministic crop/export with a deterministic blank-gap pointer cleanup; the screenshot teaches that pandas loads `data.csv` and `df.head()` displays the first five rows.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-02-read-csv.jpg`; caption: “read_csv and df.head() show the first five rows”.
- Crop coordinates: source `598x360`; `577x290+0+54` (`x=0, y=54, width=577, height=290`). The crop removes the notebook/browser header, webcam tile, right black strip, and horizontal scrollbar; the source pointer in the blank gap above the table rule was removed by copying the adjacent blank `14x14` source patch from `x=232, y=132` to `x=218, y=132`.
- Invariants: preserve `df = pd.read_csv('data.csv')`, `df.head()`, the visible column labels, row indices `0` through `4`, every visible value, and the table's original column/row relationships.
- Path: deterministic crop/export and blank-gap source patch from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-02-read-csv-cropped.jpg`.
- QA: source inspected in lesson context; exact code, labels, values, ordering, and table relationships preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, black border, or scrollbar remains; final dimensions `577x290`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 10 — lowercase columns

- Disposition: `keep` via deterministic crop/export; the screenshot teaches the column-name string operation and shows the resulting pandas `Index`.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-03-lowercase-columns.jpg`; caption: “Lowercasing column names and replacing spaces”.
- Crop coordinates: source `598x360`; `577x145+0+54` (`x=0, y=54, width=577, height=145`). The crop removes the notebook/browser header, webcam tile, right black strip, later exploratory-section cells, and recording-frame material while retaining the `df.columns.str.lower()` cell and complete `Index` output.
- Invariants: preserve the exact code, all sixteen visible column labels and their order, spaces in the pre-replacement labels, and the exact `dtype='object'` result.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-03-lowercase-columns-cropped.jpg`.
- QA: source inspected in lesson context; exact code, labels, values, order, and dtype preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `577x145`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 11 — dtypes

- Disposition: `keep` via deterministic crop/export; the screenshot teaches that `df.dtypes` identifies the string (`object`) and numeric types for every column.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-04-dtypes.jpg`; caption: “df.dtypes shows the type of every column”.
- Crop coordinates: source `598x360`; `577x280+0+54` (`x=0, y=54, width=577, height=280`). The crop removes the notebook/browser header, webcam tile, right black strip, later-section heading, and recording-frame material while retaining the code cell and complete dtype output.
- Invariants: preserve `df.dtypes`, all sixteen column/type pairs in their original order (`object`, `int64`, and `float64` values), and the final `dtype: object` line.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-04-dtypes-cropped.jpg`.
- QA: source inspected in lesson context; exact code, labels, type values, order, and final dtype preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `577x280`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 12 — string columns

- Disposition: `keep` via deterministic crop/export; the screenshot teaches that comparing `df.dtypes` with `object` identifies the string columns, with the original handwritten `VALUES` annotation retained.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-05-string-columns.jpg`; caption: “Selecting the columns of type object”.
- Crop coordinates: source `598x360`; `577x190+0+54` (`x=0, y=54, width=577, height=190`). The crop removes the notebook/browser header, webcam tile, right black strip, later-section heading, and recording-frame material while retaining the code, complete object-column output, blue bracket/arrows, and `VALUES` annotation.
- Invariants: preserve `df.dtypes[df.dtypes == 'object']`, the eight exact column names in their original order, every visible `object` value, `dtype: object`, and the handwritten `VALUES` teaching annotation and its pointers.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-05-string-columns-cropped.jpg`.
- QA: source inspected in lesson context; exact code, labels, values, order, and annotation preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `577x190`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 13 — strings list

- Disposition: `keep` via deterministic crop/export; the screenshot teaches the Python list of object-column names that will drive the normalization loop.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-06-strings-list.jpg`; caption: “The list of column names that contain strings”.
- Crop coordinates: source `598x360`; `577x230+0+54` (`x=0, y=54, width=577, height=230`). The crop removes the notebook/browser header, webcam tile, right black strip, later-section heading, and recording-frame material while retaining the list output and the following loop cell.
- Invariants: preserve `strings = list(df.dtypes[df.dtypes == 'object'].index)`, the second `strings` expression, all eight exact list entries and their order, and the visible `for col in strings` / `df[col] =` setup cell.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-06-strings-list-cropped.jpg`.
- QA: source inspected in lesson context; exact code, labels, values, order, and loop setup preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `577x230`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 14 — normalize values

- Disposition: `keep` via deterministic crop/export; the screenshot teaches that the loop lowercases string values and replaces spaces with underscores before `df.head()` is inspected.
- Source/context: `cohorts/2026/02-regression/images/02-data-preparation-07-normalize-values.jpg`; caption: “The normalized string values”.
- Crop coordinates: source `598x360`; `577x196+0+54` (`x=0, y=54, width=577, height=196`). The crop removes the notebook/browser header, webcam tile, right black strip, horizontal scrollbar/pointer, later-section heading, and recording-frame material while retaining the loop, `df.head()`, and the complete visible five-row output.
- Invariants: preserve `for col in strings`, the exact lowercase/space-replacement expression, `df.head()`, every visible normalized header and value, all five visible row relationships, and the original horizontal viewport/truncation.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/02-data-preparation-07-normalize-values-cropped.jpg`.
- QA: source inspected in lesson context; exact code, labels, values, row order, relationships, and visible viewport preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, black border, or scrollbar remains; final dimensions `577x196`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 15 — explore columns

- Disposition: `keep` via deterministic crop/export; the screenshot teaches the loop that prints each column, sample unique values, and the unique-value count.
- Source/context: `cohorts/2026/02-regression/images/03-eda-01-explore-columns.jpg`; caption: “The loop that prints unique values and their counts for every column”.
- Crop coordinates: source `598x360`; `577x306+0+54` (`x=0, y=54, width=577, height=306`). The crop removes the notebook/browser header, webcam tile/face, right black strip, and recording-frame material while retaining the complete visible code cell and output through the `engine_hp` sample.
- Invariants: preserve the exact `for col in df.columns` loop, the `unique()[:5]` and `nunique()` calls, the visible column names, unique-value samples, counts, ordering, and the partial `engine_hp` output at the source bottom edge.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/03-eda-01-explore-columns-cropped.jpg`.
- QA: source inspected in lesson context and candidate crop inspected visually; exact code, labels, values, ordering, and output relationships preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `577x306`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 16 — import plotting libraries

- Disposition: `keep` via deterministic crop/export; the screenshot teaches the imports for matplotlib and seaborn and the notebook's inline plotting directive.
- Source/context: `cohorts/2026/02-regression/images/03-eda-02-import-plotting-libraries.jpg`; caption: “Importing matplotlib and seaborn”.
- Crop coordinates: source `598x360`; `577x136+0+183` (`x=0, y=183, width=577, height=136`). The crop removes the notebook/browser header, webcam tile/face, right black strip, preceding table/scrollbar, and following unrelated section while retaining the `Distribution of price` heading, import cell, and blank prompt immediately below it.
- Invariants: preserve the exact `import matplotlib.pyplot as plt`, `import seaborn as sns`, and `%matplotlib inline` lines, their order, notebook cell styling, and the `Distribution of price` context heading.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/03-eda-02-import-plotting-libraries-cropped.jpg`.
- QA: source inspected in lesson context and candidate crop inspected visually; exact heading, code, ordering, and notebook context preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, black border, or unrelated table remains; final dimensions `577x136`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.

## 17 — long-tail distribution

- Disposition: `keep` via deterministic crop/export; the screenshot teaches the exact price histogram's long right tail and why `1e6` means one million.
- Source/context: `cohorts/2026/02-regression/images/03-eda-03-long-tail-distribution.jpg`; caption: “The histogram of prices has a long tail”.
- Crop coordinates: source `598x360`; `577x255+0+90` (`x=0, y=90, width=577, height=255`). The crop removes the notebook/browser header, webcam tile/face, right black strip, preceding unrelated cell, and following-cell border while retaining the plotting code, output, full visible histogram, axes, and handwritten scientific-notation annotation.
- Invariants: preserve the exact `sns.histplot(df.msrp, bins=50)` call and output label, the histogram bars and long-tail shape, the `msrp`/`Count` axes, scientific-notation tick, and the handwritten `1e6 = 10^6` / `1,000,000` explanation.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/03-eda-03-long-tail-distribution-cropped.jpg`.
- QA: source inspected in lesson context and candidate crop inspected visually; exact code, plot geometry, axes, values, annotation, and teaching relationship preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, black border, or following-cell border remains; final dimensions `577x255`; lesson reference resolves; `git diff --check` and missing-reference check pass before commit.
