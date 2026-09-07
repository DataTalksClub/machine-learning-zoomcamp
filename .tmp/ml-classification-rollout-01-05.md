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

## 09 — data preparation: churn yes/no to booleans

- Source: `cohorts/2026/03-classification/images/02-data-preparation-06-churn-encoding.jpg` (598×360 JPEG).
- Context/caption: “Translating churn from yes/no to 1/0.” This image teaches that comparing `churn` with `'yes'` produces booleans before casting them to integer labels.
- Rubric/disposition: keep — deterministic crop plus targeted cursor cleanup and lossless PNG export. The notebook code and boolean outputs are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` in `.tmp/ml-classification-rollout-02-data-preparation-crops/06-candidate.png` removes the browser/notebook header, webcam tile, and right black capture bar. The source text caret and mouse I-beam were removed deterministically from the empty area after the visible expression using bounded rectangles `x=232..234, y=151..166` and `x=244..251, y=159..170` relative to the crop; the code text and output were not repainted.
- Invariants: `df.churn.head()` output remains `no`, `no`, `yes`, `no`, `yes` with `Name: churn, dtype: object`; the comparison expression `(df.churn == 'yes')` remains visible; boolean output remains `False`, `False`, `True`, `False`, `True` for indices `0`–`4`, followed by the source ellipsis and tail rows beginning at `7038`; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/02-data-preparation-06-churn-encoding-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size and zoomed code/output inspections; string values, comparison expression, boolean sequence, and tail-row context checked against the source; both cursors removed without changing instructional text; Markdown reference resolves.

## 10 — validation: train/validation/test split plan

- Source: `cohorts/2026/03-classification/images/03-validation-01-train-val-test-split.jpg` (598×360 JPEG).
- Context/caption: “The plan: first split off 20% for the test set, then split the remaining 80% into train and validation.” This image teaches the two-step 60/20/20 partition and the relationship between the full train, train, validation, and test sets.
- Rubric/disposition: keep — deterministic crop with bounded background cleanup. The diagram’s labels, percentages, boxes, and arrows are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `521×360+28+0` removes the left black bar, right black bar, and face tile. A deterministic background fill removes the face-tile rectangle at `x=478..520, y=0..57` and a small cursor in blank background at `x=450..463, y=222..237`, all relative to the cropped image; no instructional pixels are covered.
- Invariants: section marker `3.3`; top row `TRAIN`, `VAL`, `TEST` with `60%`, `20%`, and `20%`; `80%` arrow to `FULL TRAIN`; `20%` arrow to `TEST`; lower arrows to `TRAIN` and `VAL`; box order and arrow directions preserved; no face, camera tile, cursor, watermark, overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/03-validation-01-train-val-test-split-cropped.png` (521×360 PNG).
- QA: accepted after `view_image` inspection at lesson size; all labels, percentages, box relationships, and arrow directions checked against the original; face/capture framing and cursor are absent; Markdown reference resolves.

## 11 — validation: split sizes

- Source: `cohorts/2026/03-classification/images/03-validation-02-split-sizes.jpg` (598×360 JPEG).
- Context/caption: “The two splits and the sizes of the resulting sets.” This image teaches the exact two-step split code and confirms that train, validation, and test contain 4225, 1409, and 1409 rows.
- Rubric/disposition: keep — deterministic crop with bounded camera-tile cleanup. The notebook heading, code, output tuple, and UI text are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×320+26+40` removes the browser/Zoom header and right capture edge. A deterministic white fill removes the remaining webcam-tile rectangle at `x=478..549, y=0..20` relative to the cropped image; it covers only blank margin and does not touch the heading or notebook cells.
- Invariants: heading `3.3 Setting up the validation framework`; visible split calls remain `df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)` and `df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)` as captured; output remains `(4225, 1409, 1409)`; `3.4 EDA` and its visible bullets remain; source’s right-edge truncation is retained; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/03-validation-02-split-sizes-cropped.png` (550×320 PNG).
- QA: accepted after `view_image` inspection at lesson size; heading, code, output values, and EDA context checked against the source; camera/browser framing removed without changing instructional pixels; Markdown reference resolves.

## 12 — validation: resetting indexes

- Source: `cohorts/2026/03-classification/images/03-validation-03-reset-index.jpg` (598×360 JPEG).
- Context/caption: “Resetting the indexes after the shuffle.” This image teaches that each split dataframe receives a fresh zero-based index after `train_test_split` shuffles the rows.
- Rubric/disposition: keep — deterministic crop. The three dataframe reset commands are exact instructional content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×52+26+82` removes the browser/Zoom header, face tile, black capture edges, and the unrelated partially typed next-cell line/caret by cropping to the target cell only. No target code pixels are covered.
- Invariants: the complete three-line cell remains `df_train = df_train.reset_index(drop=True)`, `df_val = df_val.reset_index(drop=True)`, and `df_test = df_test.reset_index(drop=True)`; line order and `drop=True` arguments are unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/03-validation-03-reset-index-cropped.png` (550×52 PNG).
- QA: accepted after `view_image` inspection at lesson size; all three commands and their ordering checked against the original; capture framing, unrelated active-cell content, and caret are absent; Markdown reference resolves.

## 13 — validation: isolating the target

- Source: `cohorts/2026/03-classification/images/03-validation-04-isolate-target.jpg` (598×360 JPEG).
- Context/caption: “Taking the target out of the dataframes and into y vectors.” This image teaches extracting `churn` into the three target arrays before deleting the target column from each split dataframe.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The notebook commands and exact `churn` references are instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` removes the browser/notebook header, webcam tile, and right capture edge while retaining the reset context, target-extraction cell, delete cell, and visible `3.4 EDA` context. The source’s lower-edge truncation is retained rather than inventing content beyond the capture.
- Invariants: target cell remains `y_train = df_train.churn.values`, `y_val = df_val.churn.values`, and `y_test = df_test.churn.values`; delete cell remains `del df_train['churn']`, `del df_val['churn']`, and `del df_test['churn']`; line order, dataframe names, `churn`, and `.values` are unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/03-validation-04-isolate-target-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size and zoomed code-cell inspection; all six exact commands and their order checked against the source, capture framing removed, and Markdown reference resolves.

## 14 — EDA: missing values

- Source: `cohorts/2026/03-classification/images/04-eda-01-missing-values.jpg` (598×360 JPEG).
- Context/caption: “Checking for missing values: everything is 0.” This image teaches that the dataframe-wide `isnull().sum()` result contains zero missing values for every column.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The pandas output and exact column names/counts are instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` removes the browser/notebook header, webcam tile, and black capture framing. The native blue selection highlight on `totalcharges` is retained because its white glyphs are exact output content and repainting it would risk altering the result.
- Invariants: all visible column names remain in source order from `customerid` through `churn`; every visible count remains `0`; `dtype: int64` remains; selected `totalcharges` row and output alignment are unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, or black capture bar.
- Final: `cohorts/2026/03-classification/images/04-eda-01-missing-values-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size; column order, zero counts, dtype, and selection state checked against the source; recording framing removed and the Markdown reference resolves.

## 15 — EDA: churn-rate source frame

- Source: `cohorts/2026/03-classification/images/04-eda-02-churn-rate.jpg` (598×360 JPEG).
- Context/caption: “The distribution of the target: 73% stayed, 27% churned.” The inspected frame itself shows the `3.4 EDA` heading, reset-index cells, and a transposed-looking dataframe preview rather than the later churn-rate output; that source/caption mismatch is preserved and called out here.
- Rubric/disposition: keep — deterministic crop with bounded cursor cleanup and lossless PNG export. The visible notebook heading, commands, dataframe labels, and values are exact instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` removes the browser/notebook header, webcam tile, and black capture framing. A deterministic white fill removes the small cursor in blank inter-cell space at `x=204..224, y=108..121` relative to the crop; no code or dataframe pixels are covered.
- Invariants: heading `3.4 EDA` and its three bullets remain; reset-index and dataframe cells remain in order; visible headers, sample rows, and source-truncated right/lower edges remain unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, or black capture bar.
- Final: `cohorts/2026/03-classification/images/04-eda-02-churn-rate-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size and an enlarged cursor-area check; exact visible notebook text/table content checked against the source, cursor and recording framing removed, caption/frame mismatch documented, and Markdown reference resolves.

## 16 — EDA: churn rate and binary mean

- Source: `cohorts/2026/03-classification/images/04-eda-03-churn-rate-mean.jpg` (598×360 JPEG).
- Context/caption: “The mean of the binary churn column is the churn rate.” This image teaches that `value_counts(normalize=True)` and `churn.mean()` produce the same churn-rate value.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The code, exact proportions, dtype, and numeric result are instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×132+26+96` removes the browser/notebook header, webcam tile, empty active-cell area, and black capture framing. A small source cursor remains over the exact mean-output glyph area because removing it safely would require repainting numeric pixels; no attempt was made to guess or alter the value.
- Invariants: `df_full_train.churn.value_counts(normalize=True)` remains visible; proportions remain `0.730032` and `0.269968`; `Name: churn, dtype: float64` remains; `df_full_train.churn.mean()` and `0.26996805111821087` remain verbatim and in order; no face, camera tile, browser/Zoom chrome, watermark, or black capture bar.
- Final: `cohorts/2026/03-classification/images/04-eda-03-churn-rate-mean-cropped.png` (550×132 PNG).
- QA: accepted after `view_image` inspection at lesson size and enlarged numeric-output inspection; exact code, proportions, dtype, and mean value checked against the source, framing removed, cursor limitation documented, and Markdown reference resolves.

## 17 — EDA: numerical variables

- Source: `cohorts/2026/03-classification/images/04-eda-04-numerical-variables.jpg` (598×360 JPEG).
- Context/caption: “The three numerical variables.” This image teaches the exact `numerical` feature list used for the classification dataset: `tenure`, `monthlycharges`, and `totalcharges`.
- Rubric/disposition: keep — deterministic crop with bounded background cleanup and lossless PNG export. The Python assignment is exact instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×32+26+40` isolates the complete numerical-variable assignment and removes the browser/notebook header, webcam tile, unrelated active-cell content/caret, and capture framing. A white fill at `x=452..549, y=0..18` relative to the crop removes the residual camera-tile strip in blank margin.
- Invariants: the complete assignment remains `numerical = ['tenure', 'monthlycharges', 'totalcharges']`; list order, spelling, punctuation, and syntax coloring are unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated cell, or black capture bar.
- Final: `cohorts/2026/03-classification/images/04-eda-04-numerical-variables-cropped.png` (550×32 PNG).
- QA: accepted after `view_image` inspection at lesson size; exact assignment text and ordering checked against the source, camera strip and unrelated active-cell content removed, and Markdown reference resolves.

## 18 — EDA: categorical variables

- Source: `cohorts/2026/03-classification/images/04-eda-05-categorical-variables.jpg` (598×360 JPEG).
- Context/caption: “The list of categorical variables.” This image teaches the exact 16 categorical feature names used after excluding the identifier, numerical variables, and target.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The Python list is exact instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×82+26+124` isolates the complete categorical-variable assignment and removes the browser/notebook header, webcam tile, unrelated dataframe output, active-cell content/caret, and capture framing.
- Invariants: all 16 labels remain verbatim and in source order: `gender`, `seniorcitizen`, `partner`, `dependents`, `phoneservice`, `multiplelines`, `internetservice`, `onlinesecurity`, `onlinebackup`, `deviceprotection`, `techsupport`, `streamingtv`, `streamingmovies`, `contract`, `paperlessbilling`, and `paymentmethod`; punctuation, line wrapping, and syntax coloring remain; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated cell, or black capture bar.
- Final: `cohorts/2026/03-classification/images/04-eda-05-categorical-variables-cropped.png` (550×82 PNG).
- QA: accepted after `view_image` inspection at lesson size; all 16 labels, order, and list syntax checked against the source, unrelated capture content removed, and Markdown reference resolves.

## 19 — risk: churn rate by gender

- Source: `cohorts/2026/03-classification/images/05-risk-01-churn-rate-gender.jpg` (598×360 JPEG).
- Context/caption: “Computing the churn rate for each gender and the global churn rate.” This image teaches comparing the female and male churn rates with the global churn rate; the differences are small.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The notebook code and exact churn-rate values are instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×294+26+66` removes the browser/notebook header, horizontal scrollbar, webcam tile, left capture margin, and right capture edge while retaining the three churn-rate cells and the following `Risk ratio` heading.
- Invariants: visible code remains the female, male, and global churn calculations; outputs remain `0.27682403433476394`, `0.2632135306553911`, and `0.26996805111821087`; cell order and notebook hierarchy remain unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/05-risk-01-churn-rate-gender-cropped.png` (550×294 PNG).
- QA: accepted after `view_image` inspection at lesson size; code, exact values, ordering, and retained `Risk ratio` context checked against the source; capture framing is absent and the Markdown reference resolves.

## 20 — risk: churn rate by partner status

- Source: `cohorts/2026/03-classification/images/05-risk-02-churn-rate-partner.jpg` (598×360 JPEG).
- Context/caption: “The churn rate for customers with and without a partner.” This image teaches that the partner groups have materially different churn rates and that the partner-group difference from the global rate is positive for customers with a partner.
- Rubric/disposition: keep — deterministic crop and lossless PNG export. The notebook code, counts, and exact churn-rate values are instructional source content; imagegen was not used despite the capability being available.
- Capture cleanup: accepted crop `550×302+26+58` removes the browser/notebook header, webcam tile, left capture margin, and right capture edge while retaining the partner counts, group churn-rate cells, global-rate subtraction, and following `Risk ratio` heading.
- Invariants: visible partner counts remain `no 2932` and `yes 2702`; outputs remain `0.20503330866025166`, `0.06493474245795922`, and `0.3298090040927694`; code and cell order remain unchanged; no face, camera tile, browser/Zoom chrome, cursor, watermark, unrelated overlay, or black bar.
- Final: `cohorts/2026/03-classification/images/05-risk-02-churn-rate-partner-cropped.png` (550×302 PNG).
- QA: accepted after `view_image` inspection at lesson size; counts, exact outputs, cell order, and retained `Risk ratio` context checked against the source; capture framing is absent and the Markdown reference resolves.
