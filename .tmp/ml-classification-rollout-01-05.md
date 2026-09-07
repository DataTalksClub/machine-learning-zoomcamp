# ML classification screenshot rollout 01-05

## 01 — churn problem

- Source: `cohorts/2026/03-classification/images/01-churn-project-01-churn-problem.jpg` (598×360 JPEG).
- Context/caption: “Churn prediction: each customer gets a churn score, and the customers with the highest scores get a discount offer.” This image teaches that a telecom company scores individual customers and targets the highest-risk customers with an offer.
- Rubric/disposition: keep — deterministic native re-render. The source is a bounded conceptual diagram, but the visible labels, percentages, and scores are exact instructional content; imagegen was not used.
- Capture cleanup: preparation crop `470×360+28+0` in `.tmp/ml-classification-rollout-01-05/01-source-crop.png` removes the left black bar and avoids the webcam tile/color-wheel overlay. A crop alone was rejected because it clipped the right-side company/score context; the accepted final is a deterministic re-render from the inspected source.
- Invariants: title `CHURN PREDICTION`; company labels `TELCO` and `TELCO2`; green offer flow with `95%`, envelope, and `25%`; six customers with scores `0.2`, `0.3`, `0.35`, `0.40`, `0.45`, `0.85`; highest score `0.85` highlighted; customer/offer arrow relationships preserved; no faces, camera tile, Zoom controls, color-wheel overlay, cursor, watermark, or black border.
- Final: `cohorts/2026/03-classification/images/01-churn-project-01-churn-problem-cropped.png` (598×360 PNG).
- QA: accepted after `view_image` inspection at lesson size; exact labels/values and relationships checked; no capture overlays remain; Markdown reference resolves.

## 02 — binary classification

- Source: `cohorts/2026/03-classification/images/01-churn-project-02-binary-classification.jpg` (598×360 JPEG).
- Context/caption: “Binary classification: the model g approximates the target y for each customer.” This image teaches the per-customer model relationship and identifies `x_i` as the i-th customer.
- Rubric/disposition: keep — deterministic native re-render. The formula and labels are exact instructional content; imagegen was not used.
- Capture cleanup: preparation crop `400×337+90+0` in `.tmp/ml-classification-rollout-01-05/02-source-crop.png` removes the left black bar, bottom Zoom controls, webcam tile, and color-wheel overlay, but was rejected because the capture obscured/clipped the final `N` in the heading. The accepted final is a deterministic re-render from the inspected source and lesson formula.
- Invariants: heading `BINARY CLASSIFICATION`; formula `g(x_i) ≈ y_i`; `x_i` and `y_i` remain in the same order; blue arrow points to `x_i` with the `i-th customer` annotation; blue arrow points toward `y_i`; no faces, camera tile, Zoom controls, color-wheel overlay, cursor, watermark, or black border.
- Final: `cohorts/2026/03-classification/images/01-churn-project-02-binary-classification-cropped.png` (598×360 PNG).
- QA: accepted after `view_image` inspection at lesson size; heading, formula, subscripts, annotation, and arrow directions checked; no capture overlays remain; Markdown reference resolves.

## 03 — module plan

- Source: `cohorts/2026/03-classification/images/01-churn-project-03-module-plan.jpg` (598×360 JPEG).
- Context/caption: “The plan of the module in the course notebook.” This image teaches the sequence of the validation framework, EDA, and feature-importance sections in the notebook.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The notebook UI text is exact instructional content; imagegen was not used.
- Capture cleanup: crop `492×321+58+39` removes the browser toolbar, left margin, and black/capture framing. After cropping, a `45×14` white rectangle in the blank notebook margin removes the remaining bottom edge of the webcam tile; no instructional pixels are covered.
- Invariants: headings `3.3 Setting up the validation framework`, `3.4 EDA`, and `3.5 Feature importance: Churn rate and risk ratio`; visible bullets and notebook prompts remain verbatim, including the train/validation/test split, missing values, target variable, numerical and categorical variables, feature-importance sentence, `Churn rate`, and the visible `Risk ratio` line; order and UI hierarchy preserved; no face, camera tile, browser toolbar, cursor, watermark, or black bar.
- Final: `cohorts/2026/03-classification/images/01-churn-project-03-module-plan-cropped.png` (492×321 PNG).
- QA: accepted after `view_image` inspection at lesson size; exact visible UI text and ordering checked; webcam/browser framing removed; source’s bottom-edge truncation is retained rather than invented; Markdown reference resolves.

## 04 — data preparation: downloading and reading the data

- Source: `cohorts/2026/03-classification/images/02-data-preparation-01-download-data.jpg` (598×360 JPEG).
- Context/caption: “Downloading the dataset with wget.” This image teaches that the notebook download completed successfully and saved the dataset as `data-week-3.csv`.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The terminal output and notebook cell are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` in `.tmp/ml-classification-rollout-02-data-preparation-crops/01-candidate-y58.png` removes the browser/notebook header, webcam tile, and right black capture bar. The crop keeps the HTTP `200 OK` result, `Length: 977501 (955K)`, saved filename, transfer result, `pd.read_csv` cell, and surrounding notebook context.
- Invariants: visible download completion output includes `HTTP request sent, awaiting response... 200 OK`, `Saving to: ‘data-week-3.csv’`, `data-week-3.csv`, `954.59K`, and `[977501/977501]`; notebook cell shows `pd.read_csv(...)`; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/02-data-preparation-01-download-data-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size; exact output values, filename, and notebook code checked; capture overlays removed; Markdown reference resolves.

## 05 — data preparation: first look at the transposed dataframe

- Source: `cohorts/2026/03-classification/images/02-data-preparation-02-first-look.jpg` (598×360 JPEG).
- Context/caption: “Looking at the data with head().T to see all the columns.” This image teaches how transposing the dataframe exposes the feature rows and their values across five sample customers.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The dataframe labels and values are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` in `.tmp/ml-classification-rollout-02-data-preparation-crops/02-candidate.png` removes the browser/notebook header, webcam tile, and right black capture bar. The visible transposed dataframe rows and five sample columns are retained; the source’s cropped lower edge is retained.
- Invariants: row order and labels remain `customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, and `StreamingMovies`; visible sample IDs remain `7590-VHVEG`, `5575-GNVDE`, `3668-QPYBK`, `7795-CFOCW`, and `9237-HQITU`; values retain source capitalization and spaces, including `No phone service`, `DSL`, and `Fiber optic`; no face, camera tile, browser/Zoom chrome, cursor, watermark, overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/02-data-preparation-02-first-look-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size; row ordering, labels, sample IDs, and visible values checked against the source; capture overlays removed; Markdown reference resolves.

## 06 — data preparation: normalized dataframe

- Source: `cohorts/2026/03-classification/images/02-data-preparation-03-normalized.jpg` (598×360 JPEG).
- Context/caption: “The same dataframe after making the names and values uniform.” This image teaches that both column names and string values have been lowercased and spaces replaced with underscores.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The dataframe labels and values are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×308+26+52` in `.tmp/ml-classification-rollout-02-data-preparation-crops/03-candidate-y52.png` removes the browser/notebook header, webcam tile, and right black capture bar while preserving the top `customerid` row and the visible dataframe through `contract`.
- Invariants: row order remains `customerid`, `gender`, `seniorcitizen`, `partner`, `dependents`, `tenure`, `phoneservice`, `multiplelines`, `internetservice`, `onlinesecurity`, `onlinebackup`, `deviceprotection`, `techsupport`, `streamingtv`, `streamingmovies`, and `contract`; visible values remain normalized, including `no_phone_service`, `fiber_optic`, and `month-to-month`; source’s native dataframe row highlighting/selection is retained without capture framing; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/02-data-preparation-03-normalized-cropped.png` (550×308 PNG).
- QA: accepted after `view_image` inspection at lesson size; lowercase labels, underscore substitutions, visible values, and row ordering checked against the source; capture framing removed; Markdown reference resolves.

## 07 — data preparation: totalcharges conversion error

- Source: `cohorts/2026/03-classification/images/02-data-preparation-04-totalcharges-error.jpg` (598×360 JPEG).
- Context/caption: “Converting totalcharges to numbers fails because of the `_` values.” This image teaches that `pd.to_numeric(df.totalcharges)` fails when normalized missing values are represented by the underscore string.
- Rubric/disposition: keep — deterministic crop plus targeted cursor cleanup and lossless PNG export. The code, exception text, and stack trace are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` in `.tmp/ml-classification-rollout-02-data-preparation-crops/04-candidate.png` removes the browser/notebook header, webcam tile, and right black capture bar. A source cursor over the underscore in the error string was removed deterministically in the bounded crop rectangle `x=306..313, y=143..156` relative to the crop, and the exact underscore glyph was restored; the correction candidate is `.tmp/ml-classification-rollout-02-data-preparation-crops/04-cursor-clean-candidate.png`.
- Invariants: code cell remains `pd.to_numeric(df.totalcharges)`; the error remains `ValueError: Unable to parse string "_" at position 488`; the visible pandas traceback and error hierarchy remain in place; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/02-data-preparation-04-totalcharges-error-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size and a zoomed cursor-area inspection; exact code and error message checked, restored underscore is legible, capture overlays removed, and Markdown reference resolves.

## 08 — data preparation: missing total charges after coercion

- Source: `cohorts/2026/03-classification/images/02-data-preparation-05-coerce-missing.jpg` (598×360 JPEG).
- Context/caption: “The 11 customers with missing total charges.” This image teaches that `errors='coerce'` exposes the customers whose normalized underscore values became missing numeric values.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The notebook commands and customer output are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` in `.tmp/ml-classification-rollout-02-data-preparation-crops/05-candidate.png` removes the browser/notebook header, webcam tile, and right black capture bar. The source’s visible lower-edge truncation is retained rather than inventing rows beyond the captured output.
- Invariants: visible commands remain `tc = pd.to_numeric(df.totalcharges, errors='coerce')`, `df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')`, and `df[tc.isnull()][['customerid', 'totalcharges']]`; output headers remain `customerid` and `totalcharges`; visible missing values remain `_`; row indices remain `488`, `753`, `936`, `1082`, `1340`, `3331`, `3826`, `4380`, and `5218`, with their source customer IDs unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/02-data-preparation-05-coerce-missing-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size and a zoomed table inspection; commands, headers, missing-value markers, visible row indices, and customer IDs checked against the source; capture framing removed; Markdown reference resolves.
