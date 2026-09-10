# Datasets repository and raw 2025 homework CSV snapshot

<!-- Source page; evidence is summarized below with provenance markers. -->

## Provenance

- [FACT datasets-2025-snapshot] The datasets repository was inspected at shallow commit `8aa02f8bd20f565eed700cc3da31d8de292556c2`, dated 2025-09-16, which contains `car_fuel_efficiency.csv` and `course_lead_scoring.csv`.
- [FACT datasets-2025-snapshot] The raw URLs used by the homework were downloaded on 2026-09-10. SHA-256 hashes were `89fb42d0b81d82a3e6d89c0069c1c876cc97cc516e627846e600ba4438829d86` for `car_fuel_efficiency.csv` and `03bd91b6c43f784d4d31aa0c9c81744eb752c2f929e5bf74676f11433c95d756` for `course_lead_scoring.csv`.
- [OPEN] The public raw URL is mutable from the learner’s point of view. A future redesign should publish an immutable release asset or include a checksum in the homework.

## Car fuel efficiency data

- [FACT datasets-2025-snapshot] The file has 9,704 rows and 11 columns. Missingness is concentrated in `num_cylinders` (482, 4.97%), `horsepower` (708, 7.30%), `acceleration` (930, 9.58%), and `num_doors` (502, 5.17%). HW2 filters to five columns, leaving `horsepower` as the missing feature.
- [FACT datasets-2025-snapshot] `fuel_efficiency_mpg` ranges from 6.20 to 25.97, has median 15.006, and has skewness approximately `-0.012`. It is not a right-tailed target that naturally motivates the `log1p` transformation used in the car-price lecture.
- [FACT datasets-2025-snapshot] In the full numeric data, the target correlation with `vehicle_weight` is approximately `-0.977`, with `horsepower` approximately `+0.122`, and with `engine_displacement` approximately `+0.001`. The negative weight relationship is intuitive; the positive horsepower relationship is weak and counterintuitive for the teaching context, matching the Slack report.

## Reproduction of the most disputed HW2 questions

- [FACT datasets-2025-snapshot] Using the HW2 five-column filter, `np.random.seed(42)`, shuffle-then-slice 60/20/20 split, zero imputation, and ordinary least squares/ridge as specified, the validation RMSEs for `r = [0, .01, .1, 1, 5, 10, 100]` were approximately `[.517378, .517112, .518753, .522235, .522892, .522981, .523064]`.
- [FACT datasets-2025-snapshot] Every one of those RMSEs rounds to `.52` at the homework’s requested precision. The smallest full-precision value is at `r=.01`, while the written rounded-tie rule selects `r=0`. Thus the exercise cannot demonstrate a unique regularization choice at the displayed precision.
- [FACT datasets-2025-snapshot] For seeds 0 through 9, the corresponding validation RMSE standard deviation is approximately `.006989`, which rounds to `.007`, while the choices are `.001`, `.006`, `.060`, and `.600`. The nearest option is `.006`, not the rounded result.
- [FACT datasets-2025-snapshot] With seed 9, train+validation refit, `r=.001`, and zero imputation, test RMSE is approximately `.515626`, close to but not equal to the `.515` option.
- [INFERENCE datasets-2025-snapshot] The data explains why the reported problem felt fragile: the target is nearly symmetric, so the lecture’s log branch is a poor default; feature scales are large and heterogeneous, making small ridge values almost invisible; and the options appear to have been manually spaced rather than generated from a checked reference run.

## Lead-scoring data

- [FACT datasets-2025-snapshot] The file has 1,462 rows and 9 columns. Missingness is 4.31% in `location`, 6.84% in `employment_status`, 8.75% in `lead_source`, 9.17% in `industry`, and 12.38% in `annual_income`; the target `converted` has no missing values and a positive rate of approximately 61.9%.
- [FACT datasets-2025-snapshot] Pairwise correlations among the three numeric predictors and `lead_score` are all weak in the downloaded data. The largest absolute pairwise value among HW3’s four choices is approximately `.0486` for `annual_income`/`interaction_count`; the other candidates are around `.032`, `.024`, and `.010` in absolute value.
- [FACT datasets-2025-snapshot] The target has useful marginal signal: correlations with `number_of_courses_viewed`, `interaction_count`, and `lead_score` are approximately `.436`, `.375`, and `.194`. This means the data can support a basic classifier while still failing to provide robust feature-feature relationships for a correlation-ranking question.
- [FACT datasets-2025-snapshot] Reproducing the final HW3 procedure with seed 42, target excluded, categorical missing values replaced by `NA`, numeric missing values by zero, and one-hot logistic regression gives validation accuracy approximately `.699659` for `C=1`. Rounded to two decimals this is `.70`, absent from choices `.64`, `.74`, `.84`, `.94`.
- [FACT datasets-2025-snapshot] Under that same split and preprocessing, validation accuracy is exactly `.699659` for every `C` in `[.01, .1, 1, 10, 100]` in the reference run. Different coefficients/probabilities can therefore produce the same hard predictions and accuracy.
- [INFERENCE datasets-2025-snapshot] HW3’s “biggest correlation” and “best C” questions are unstable teaching signals on this snapshot: one is based on small accidental sample correlations, and the other measures a coarse metric that is insensitive to the hyperparameter range.

## Reproduction environment

- [FACT datasets-2025-snapshot] The quick reference calculations were run on 2026-09-10 with a current NumPy/pandas/scikit-learn environment; the exact package versions and implementation are recorded in the analysis log, and the results agree with the Slack-reported `.70`/same-`C` symptom.
- [OPEN] A final answer key should be generated and checked under the exact supported dependency lockfile, not inferred from a later library stack.
