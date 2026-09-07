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
