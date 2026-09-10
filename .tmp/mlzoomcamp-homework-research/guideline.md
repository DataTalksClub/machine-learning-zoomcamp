# 2026 homework data and assessment redesign guideline

Status: implemented in the sibling `datagen` project and in the 2026 course
data/homework release; verification is recorded in the implementation source
page and project log.

## Core decision

- [INFERENCE slack-export-2025-homework, datasets-2025-snapshot, datagen-generator-repo] Do not solve the 2025 problem by only widening answer options or adding “choose the closest.” Build homework around versioned, validated datasets and a deterministic reference pipeline. Use realistic relationships as an explicit acceptance criterion, not as a hope attached to an LLM prompt.

## Data strategy

### Preferred two-layer approach

1. Use a small, immutable real-world dataset where the goal is to notice genuine domain patterns. Store the exact release asset or commit and its SHA-256.
2. Use a controlled synthetic dataset when the lesson needs a particular missingness pattern, class balance, noise level, or relationship. Label it synthetic and ship a data card explaining the intended relationships.

This keeps the course honest: real data teaches that relationships are messy; controlled data makes a pedagogical experiment answerable.

### If using synthetic car data

- Model a generative story instead of independent columns: vehicle class/body type and model year influence engine displacement, cylinder count, horsepower, and weight; fuel efficiency depends negatively on weight/displacement/horsepower and positively on model year, with class/fuel/drivetrain effects and calibrated noise.
- Generate horsepower conditionally from displacement/vehicle class and weight. Enforce plausible ranges and monotonic/sign constraints after rounding.
- Treat missingness as a measurement process: for example, older records or particular sources may have missing horsepower. Keep the mechanism documented and avoid changing the target in a way that creates leakage.
- Use bounded, domain-specific outliers. Never inject generic `mean ± k*std` values into physical measurements without checking that they remain possible.
- If asking students to compare ridge values, standardize or rescale features in the stated pipeline, or choose `r` values that produce a validated, visible effect on the actual unscaled design matrix.

### If using synthetic lead-scoring data

- Generate a funnel: acquisition source influences opportunity and engagement; visits/courses/interactions are related counts; fit and engagement contribute to a latent conversion propensity.
- Generate `converted` by sampling Bernoulli probabilities from a calibrated logistic propensity, rather than hard-thresholding a score at zero. Tune class balance and signal-to-noise on reference splits.
- Make the intended feature-feature relationships explicit. If Q2 asks for a correlation ranking, include a robust relationship among the offered pairs; do not rely on the largest accidental sample correlation among near-zero values.
- Ensure `lead_score` is either a legitimate pre-conversion feature or clearly a derived score available at prediction time. If it is computed from engagement fields, explain that collinearity is part of the exercise and test how it affects the chosen model.

## Dataset data card

Ship a small JSON/Markdown data card with:

- dataset version, source/license, URL or release asset, SHA-256, row count, schema, units, and known bounds;
- generator repository commit/plan/seed if synthetic;
- target construction, noise model, class balance, and expected relationships/signs;
- missingness mechanism and whether any feature is derived from another or from the target;
- exact train/validation/test indices or the complete split algorithm;
- supported Python and library versions;
- a list of homework questions that consume the file.

## Answerability gate

Before publishing a homework, run the exact student-facing pipeline on the locked environment and at least 30–100 supported seeds where the question depends on a sample split.

- For a categorical choice, the same option must win under the declared reference procedure. If the answer is intentionally seed-dependent, ask for a distribution/interval instead.
- For a hyperparameter question, the winning metric must differ from the runner-up by more than the displayed rounding tolerance, or the question must explicitly test “same performance, prefer simpler model.” Verify that the model’s predictions/metric can actually respond over the listed range.
- For a numeric choice, generate options from the reference result, include a documented tolerance, and reject options that are equidistant or too close. Prefer a numeric answer with tolerance over forced nearest-option selection.
- For each question, check that the reference result equals one of the options after the stated rounding. Do not use post-hoc flooring, undocumented scaling, or “any option” as a reference method.
- Run every notebook from a clean kernel and compare its outputs, target name, dataset URL, hyperparameter lists, and wording against the markdown. Fail CI on stale names such as an old target or unrelated feature list.

## Assessment wording

- State the dataset file/version/hash and exact target at the top of every homework.
- State all preprocessing: missing-value policy, categorical encoding, scaling, split order, seed, estimator, solver, `random_state`, metric, and rounding.
- Distinguish lecture examples from homework data with a visible warning when the dataset changes. Do not say “follow the lecture code” when the target/data-generating process differs.
- For feature elimination, say whether the original column is removed before encoding or whether all derived encoded columns are removed. Name the evaluation split and classification threshold in the same place.
- Put tie-breaking in the question before students submit. For a real tie, prefer the simpler model only when that is the intended lesson; otherwise accept all tied choices.
- Replace “closest option” with tolerance-based grading wherever possible. If multiple-choice is required, validate the spacing and publish the midpoint rule in advance.

## Specific changes to 2025-style questions

- HW1: make the filter/query appear once in the canonical markdown and generate the notebook from it; add a test that Asia/Europe wording, code, and expected row count agree.
- HW2: either make the target visibly right-skewed and explicitly ask for `log1p`, or keep the near-symmetric target and remove all lecture-log ambiguity. Rescale features or redesign the ridge range so the regularization comparison is observable. Store exact expected RMSEs and accept a small numeric tolerance.
- HW3: replace “largest correlation among weak accidental pairs” with a named domain relationship or a supplied correlation target. For `C`, use log-loss/AUC or a deliberately controlled dataset where the listed values produce different results; if all accuracies tie, make that the explicit concept question.
- HW4: remove stale notebook content and make solver/scaling choices canonical. Run Q2–Q6 from a clean reference notebook before release.
- HW5/HW9: do not ask for a local Docker image’s displayed size as an exact fact. Ask for image digest, Dockerfile base tag, layer count/config, or grade an output from a provided locked container. If size is pedagogically necessary, publish the exact measurement definition and accept a range.
- HW8/HW9: separate deterministic inference from stochastic training. Use `model.eval()`, fixed non-random validation/inference transforms, a supplied checkpoint, and CPU reference outputs. Grade architecture/training concepts rather than a number produced by random augmentation on a student GPU.
- HW5–HW10: freeze the framework, model artifact, image tag/digest, paths, working directory, and dependency versions before the cohort starts. Include a one-command smoke test for every Docker/Lambda/Kubernetes exercise and avoid references to prior-cohort files.

## Release process

1. Freeze the data and environment.
2. Generate answer keys programmatically from the same code students receive.
3. Generate options from those keys and run the answerability gate.
4. Execute markdown/notebook consistency checks.
5. Have a second person complete the homework from a clean checkout.
6. Publish the immutable data release, data card, lockfile, and correction policy together.
7. Test all supported execution paths (at minimum the published CPU reference environment and the documented Docker platform) and run a link/reference scan for old cohort names, targets, model tags, and paths.
8. Keep a regression list from the 2025 Slack threads: dataset mismatch, log-transform ambiguity, rounded ties, same-`C` accuracy, stale notebook, Docker-size mismatch, missing validation contract, loss/activation mismatch, and random inference preprocessing.

## Minimum viable 2026 fix

- [INFERENCE homework-2026-draft, datasets-2025-snapshot] Before the 2026 cohort starts, do not reuse the current car/lead CSVs for exact multiple-choice questions without rerunning the gate. At minimum freeze hashes, rewrite the canonical instructions, regenerate all options from a locked pipeline, remove stale notebooks, and convert fragile exact-value questions to tolerance-based grading.

## Implementation result

[FACT mlzoomcamp-2026-data-release] The minimum viable fix was implemented for
the tabular homework path. The sibling generator now accepts explicit derived
feature dependencies, domain bounds, conditional missingness, calibrated
probabilistic classification, target controls, and relationship/bound reports.
The course repository contains reviewed car and lead plans, generated CSVs,
reports, a data card with SHA-256 hashes, and a release validator.

[FACT mlzoomcamp-2026-data-release] HW1–HW4 and HW6 now point to the 2026
release and state their metric, split, precision, and tie behavior. Fragile
“choose the closest” wording was removed from those redesigned assignments;
option sets were regenerated from the reference replay. Deployment/image-size
and deep-learning stochastic-environment issues remain separate follow-up work.
