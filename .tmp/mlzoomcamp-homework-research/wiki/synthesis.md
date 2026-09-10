# Synthesis

## Thesis

- [INFERENCE slack-export-2025-homework, homework-2025-repo, datasets-2025-snapshot, datagen-generator-repo] The core problem was not simply “students made mistakes” or simply “the data was synthetic.” A fast-generated dataset, weakly validated answer choices, live edits, inconsistent notebooks, and environment-dependent measurements combined to turn ordinary learning uncertainty into grading uncertainty.

## Evidence chain

1. [FACT slack-export-2025-homework] Students repeatedly reported values missing from the choices, identical values across regularization settings, and plausible-looking but unexpected relationships.
2. [FACT homework-2025-repo] The written material contains concrete contradictions: Asia versus Europe in HW1, old `above_average`/`engine_hp` text in the HW4 notebook, different HW4 C lists between notebook and markdown, and unrelated HW6 notebook features/metric labels.
3. [FACT datasets-2025-snapshot] Reproduction on the downloaded 2025 CSVs recreates the high-signal failures: all HW2 Q4 RMSEs round to `.52`; HW2 Q5 produces `.007` against choices centered on `.006`; HW3 Q4 produces `.70` against choices starting at `.64`/`.74`; and all HW3 Q6 accuracies are identical for the listed C values.
4. [FACT datagen-generator-repo] The linked generator samples declared feature marginals independently, does not implement its correlation hook, thresholds valid classification formulas at zero, and lacks tests for domain relationships or answer-option stability.

## What is confirmed versus inferred

### Confirmed

- [FACT slack-export-2025-homework] Alexey explicitly acknowledged that the HW2 data was generated and linked `datagen`.
- [FACT slack-export-2025-homework] Alexey clarified that HW2 did not require `log1p`, advised closest/any choices when answers fell between options, added tie guidance, and accepted/re-scored disputed answers when reproduction showed a problem.
- [FACT datasets-2025-snapshot] The supplied/current CSV snapshot has weak or counterintuitive relationships for some questions and reproduces the most prominent HW2/HW3 symptoms.
- [FACT homework-2025-repo] Material and answer-rule edits happened after the cohort started, and the 2026 drafts still carry over the same files.

### Inferred

- [INFERENCE datasets-2025-snapshot, datagen-generator-repo] Independent feature generation is a likely reason the car data has a nearly zero displacement/MPG relationship and weak/positive horsepower/MPG relationship, but the exact CSV-generation plan is not available to prove causality.
- [INFERENCE datasets-2025-snapshot] The options were not robustly synthesized from a locked reference pipeline: several are merely close, and some correct rounded results are absent.
- [INFERENCE slack-export-2025-homework] Students sometimes had genuine implementation mistakes (wrong filter, wrong matrix multiplication, wrong seed, log transform, reused index), but the course’s ambiguous materials made those mistakes harder to distinguish from assignment defects.

## Design implication

- [INFERENCE slack-export-2025-homework, datasets-2025-snapshot, datagen-generator-repo] “Make the data more realistic” is necessary for domain intuition but insufficient. Every homework question must also pass a reproducibility/answerability gate: the exact pipeline, expected result, option spacing, tie behavior, and supported environment should be tested before release.

## Secondary failure modes

- [FACT slack-export-2025-homework, homework-2025-repo] A second cluster was caused by moving or inconsistent course artifacts: 2024 versus 2025 links, notebook/markdown disagreement, the late TensorFlow-to-PyTorch HW8 change, old deployment dependencies, and model/image path confusion.
- [FACT slack-export-2025-homework] A third cluster was instructional-contract ambiguity: imputation scope, scaling, one-hot feature elimination, validation versus test, classification thresholds, loss/output activation, and deterministic versus augmented inference.
- [INFERENCE slack-export-2025-homework, homework-2025-repo] The reliable fix is to treat each homework as a versioned release with one executable specification, rather than as a markdown file plus independently edited notebook and ad hoc answer choices.
