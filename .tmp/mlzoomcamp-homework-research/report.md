# ML Zoomcamp 2025 homework reliability review

Date: 2026-09-10  
Scope: 2025 cohort, with a check of the current 2026 drafts

## Executive conclusion

[INFERENCE slack-export-2025-homework, homework-2025-repo, datasets-2025-snapshot, datagen-generator-repo] The complaints came from four interacting problems:

1. generated tabular data did not reliably express the domain relationships students were expected to interpret;
2. the answer options were not always generated and checked from a locked reference run;
3. markdown, notebooks, lecture datasets, and live repository versions were not consistently synchronized;
4. some graded measurements depended on local libraries, Docker platforms, or random training/inference behavior.

The important distinction is that “more realistic data” addresses only the first problem. The 2026 homework also needs a reproducibility and answerability release gate.

## What students reported and what was offered

| Homework | Reported problem | Evidence and response | Diagnosis |
| --- | --- | --- | --- |
| HW1 | Max/normal-equation answers seemed absent from the options; Asia filter was unclear. | Threads `1758211682.965849` and `1758213438.225589` (Sep 18–21). Students eventually found the missing `origin == 'Asia'` filter; Alexey emphasized following the instructions and welcomed framing suggestions. | Mixed: student filter mistakes, plus a real Europe/Asia contradiction between the notebook and markdown. |
| HW2 | Students used `MSRP`/`log1p` from the car-price lecture; others got almost identical RMSEs or results between options. | Thread `1759220184.998839`; Alexey clarified on `1759232006.392029` that HW2 does not ask for `log1p`. In `1759478500.015639` he ultimately said to follow the instructions; in `1759846997.715189` he acknowledged that correct code could still land between options. | Confirmed content ambiguity and a poorly discriminating ridge question. The target is nearly symmetric and the regularization effect disappears after rounding. |
| HW2 | Horsepower had a weak positive relationship with fuel efficiency, contrary to the intended car intuition. | Thread `1759821119.680489` (Oct 7). Alexey explicitly said the data was generated and some correlations might not make sense, and linked `datagen`. | Confirmed synthetic-data realism issue; exact CSV-generation plan is not available. |
| HW3 | Validation accuracy was `0.70` while choices started at `0.64`/`0.74`; all listed `C` values sometimes returned exactly the same accuracy. | Threads `1760264156.083519`, `1760286271.009029`, `1760286485.938019`, `1760370872.456799`. Workaround: choose closest; choose smallest `C` on a tie. | Reproduced design issue: accuracy is a coarse hard-prediction metric and the feature-feature correlations are mostly accidental/weak. |
| HW4 | Students used stale/different material; solver/scaling choices changed answers and some results were between options. | Thread `1760739881.321829` (wrong draft dataset); thread `1760481314.348929` (scaling/solver/options). Alexey said his reference used no scaler, advised closest option, and called reproducibility a challenge. | Confirmed release/version problem and an under-specified reference pipeline. |
| HW6 | The supplied notebook loads car-fuel data but asks about unrelated student-performance features and labels regression outputs as AUC. | Found by comparing the 2025 notebook with its markdown; the markdown uses car-specific features. | Static notebook defect, even without a matching Slack complaint. |
| HW5 | Docker base-image size was not an option or exactly between options; one “higher” choice was later marked wrong. | Thread `1761394314.367929`; Alexey advised closest, then higher for a midpoint and added that wording in commit `a4519a9`. Thread `1762987392.558459` records the grading failure. | Local image-size display is not a stable exact-answer measurement. |
| HW5 | A rounded metric appeared to keep improving to 200 instead of the expected 80. | Thread `1762951557.779209`; Alexey reproduced/accepted 200. | Precision was too low for the decision boundary. |
| HW8/HW9 | Missing validation split, random augmentation, preprocessing ambiguity, and environment/GPU setup caused different results. | Alexey confirmed train/test only in `1764098862.897439`; HW9 preprocessing ambiguity is in `1765139344.098649`. | Stochastic training and random inference transforms were mixed with exact-answer grading. |

Detailed thread evidence is in [the Slack source page](wiki/sources/slack-export-2025-homework.md).

## Additional problems reported in 2025

The following issues should be tracked separately from the generated-data problem. They still affect whether students can tell a wrong implementation from a broken question.

| Area | What students reported | What was offered or changed | 2026 implication |
| --- | --- | --- | --- |
| Release/access | 2025 links initially opened 2024/draft work, one HW1 submission URL pointed to HW2, GitHub login returned 500, and scores were not immediately visible. | Alexey updated the link, merged PR #655, students used Google login, and the community explained post-deadline scoring. | Publish one canonical cohort URL and run link/status checks before opening submissions. |
| HW2 preprocessing | Students were unsure whether to impute validation/test and whether to standardize; changing these choices changed answers. | Community converged on training-derived imputation; Alexey clarified no `log1p`; students were often told to choose the closest answer. | Put the complete preprocessing pipeline in the question and grade numeric values with tolerance. |
| HW3/HW4 wording | Feature elimination before/after one-hot encoding, class threshold `0.5`, validation versus test, AUC versus “mean score,” and threshold precision were unclear. | Community supplied conventions; Alexey said instructions would be edited and later advised closest/any option. | Define each operation, metric, split, precision, and threshold in executable reference code. |
| HW5 deployment | `uv` versus old pip material, old sklearn dependencies, `pipeline_v1` versus `pipeline_v2`, model paths/workdirs, and Docker platform differences caused setup failures. | Students were directed to updated material/`uv`, to use the image’s model, and to use Codespaces/WSL2; disputed answers were re-scored. | Ship a lockfile, a smoke-test command, a fully specified image, and artifact paths; avoid platform-sensitive exact size questions. |
| HW6 lesson scope | The lesson covered a classifier while the homework used a regressor; students also asked what to do with the unused test split. | Alexey said the regressor was part of the homework discovery and confirmed the test-set handling. | Add a short prerequisite or make the extension explicitly conceptual rather than an unexplained implementation jump. |
| HW8/HW9/HW10 | PyTorch replaced TensorFlow late; output activation/loss and validation naming were ambiguous; Saturn Cloud was unavailable for some; HW9 had a 2024/2025 model typo and HWC/NCHW confusion; an old Keras model failed under Keras 3. | Alexey redirected students to Colab/local, confirmed train/test, accepted the typo fix, and pointed to newer model material. | Freeze framework/model versions before release, provide deterministic inference code, and test every deployment path on a clean machine. |

Some reports in this table were caused by student mistakes—wrong split, wrong filter, copying the local model, or an unset workdir. They belong in the review because the material did not make those mistakes easy to diagnose, but they should not be counted as evidence that every answer key was wrong.

[FACT homework-2025-repo] Static inspection also found HW1’s Europe/Asia notebook contradiction and old car-price references plus a different hyperparameter list in the HW4 notebook. These were not all reported in a single Slack thread, but they are independently actionable defects in the homework package.

## Reproduction on the 2025 CSVs

The raw URLs were downloaded on 2026-09-10. Hashes:

- `car_fuel_efficiency.csv`: `89fb42d0b81d82a3e6d89c0069c1c876cc97cc516e627846e600ba4438829d86`
- `course_lead_scoring.csv`: `03bd91b6c43f784d4d31aa0c9c81744eb752c2f929e5bf74676f11433c95d756`

[FACT datasets-2025-snapshot] On the car data, HW2’s specified five-column filter leaves 708 missing horsepower values (7.30%). The target has skewness approximately `-0.012`, so it does not resemble the right-tailed target from the car-price lecture. Target correlation is approximately `-0.977` with weight, but only `+0.122` with horsepower and `+0.001` with engine displacement.

[FACT datasets-2025-snapshot] With seed 42, zero imputation, and the stated shuffle/split, HW2 Q4 RMSEs for `r = [0, .01, .1, 1, 5, 10, 100]` are approximately:

```text
[.517378, .517112, .518753, .522235, .522892, .522981, .523064]
```

All become `.52` after the required two-decimal rounding. Full precision prefers `.01`; the added tie rule selects `0`. This is exactly the kind of result that makes a correct student doubt their code.

[FACT datasets-2025-snapshot] HW2 Q5 gives a standard deviation around `.006989`, which rounds to `.007`; `.007` is not an option. HW2 Q6 gives test RMSE around `.515626`, close to `.515` but not equal.

[FACT datasets-2025-snapshot] On the lead-scoring data, validation accuracy under the final HW3 procedure is approximately `.699659` (`.70` rounded), absent from the choices. The validation accuracy is exactly the same in the reference run for every listed `C` in `[.01, .1, 1, 10, 100]`. The coefficients can change while the thresholded class predictions do not.

The reproducibility calculations and limitations are in [the dataset source page](wiki/sources/datasets-2025-snapshot.md).

## What the linked generator reveals

[FACT datagen-generator-repo] The linked generator creates each feature independently from its declared distribution, then computes the target. Its `_apply_correlations()` method only logs a message and returns the dataframe unchanged, and the normal generation path does not call it. The generator therefore does not implement feature-feature relationships despite describing the output as realistic.

[FACT datagen-generator-repo] Valid classification formulas are thresholded at zero rather than converted to calibrated probabilities and sampled. Missingness is independently applied per feature, and generic outliers are injected as `mean ± (3 + exponential) * std` without domain bounds.

[FACT datagen-generator-repo] The prompt asks an LLM for realistic features/formulas and missing rates but does not require reference marginals, causal dependencies, domain bounds, expected correlation signs, or multi-seed answer validation. The tests do not check those properties or multiple-choice separation.

[OPEN] The exact plan and generator commit used to produce the two 2025 CSVs are not stored with the files. These implementation findings explain a credible mechanism, but should not be presented as byte-for-byte provenance.

See [the generator source page](wiki/sources/datagen-generator-repo.md).

## Recommended 2026 design

### Data

- Use a small immutable real dataset for domain intuition, or a synthetic dataset calibrated from one. Publish a data card with source/license, hash, schema/units/bounds, split indices, target construction, missingness mechanism, generator plan/commit/seed, and supported dependency lock.
- For car data, generate a structural story: class/year influence engine size, cylinders, horsepower, and weight; MPG decreases with weight/displacement/horsepower and improves with model year. Enforce signs and physical bounds after rounding.
- For lead data, generate a funnel: source influences engagement, engagement counts are related, and conversion is sampled from a calibrated logistic propensity. Make any intended correlations explicit and robust across seeds.
- Use domain-specific missingness and bounded outliers. Do not use independent missingness or generic extreme values merely to make a file look realistic.

### Assessment

- State the immutable dataset version/hash, target, preprocessing, split algorithm/order, seed, estimator/solver, metric, precision, and tie rule in one canonical homework file.
- Generate the answer key and options programmatically from the same locked reference pipeline. Do not manually guess option spacing.
- Run 30–100 seeds when an answer depends on a random split. Reject questions where the winner changes unexpectedly, the runner-up is within the rounding tolerance, or the correct value is not an option.
- Prefer tolerance-based numeric grading over “choose closest.” If multiple-choice is required, reject equidistant/nearby choices and publish the midpoint rule before the cohort starts.
- For hyperparameters, use a metric that can show the effect (e.g. log-loss/AUC where appropriate) or explicitly make “same metric, prefer simpler model” the lesson.
- Do not grade local Docker image display size or random GPU training output as an exact scalar. Grade an image digest/config, provide a locked container, or use a deterministic checkpoint and inference transform.

### Release process

1. Freeze data, plan, hashes, and dependency lock.
2. Generate answer keys/options by code.
3. Execute every notebook from a clean kernel.
4. Compare markdown and notebook URLs, targets, feature names, options, and outputs in CI.
5. Have a second person complete the homework from a clean checkout.
6. Publish the data card, lockfile, reference code, and correction policy together.

The full implementation-oriented plan is in [guideline.md](guideline.md). The repository evidence is in [the 2025 homework source page](wiki/sources/homework-2025-repo.md), and the current carry-over risk is in [the 2026 draft source page](wiki/sources/homework-2026-draft.md).

## Bottom line

[INFERENCE homework-2026-draft, datasets-2025-snapshot] The current 2026 drafts still carry the 2025 car/lead datasets and closest-option patterns. Before using them, either replace them with validated releases or convert the fragile questions to tolerance-based/reference-output assessments. The most urgent fixes are HW2, HW3, HW4, and the Docker/image-size questions.

The practical diagnosis is therefore two-layered: redesign the car/lead data so the intended domain relationships are real and documented, and introduce a release gate that catches stale material, ambiguous preprocessing, platform-dependent measurements, and answers that do not land on a validated option. Alexey’s 2025 responses were useful emergency repairs—clarifications, closest-option rules, accepted alternatives, and re-scoring—but they were mostly compensating for defects discovered after publication.

## What was implemented for 2026

[FACT mlzoomcamp-2026-data-release] The sibling `datagen` project now supports
reviewed plan inputs with dependency-aware numerical features, physical/business
bounds, conditional missingness, target rounding/noise controls, and calibrated
Bernoulli-logistic classification. Existing legacy plans remain supported.

[FACT mlzoomcamp-2026-data-release] Two keyless, deterministic releases were
generated from reviewed plans: a 10,000-row car dataset and a 5,000-row lead
dataset. Their plans, reports, data card, hashes, and validation script live in
`cohorts/2026/data/`. The data reflects a structural car story and a marketing
funnel story instead of independent feature marginals and a hard classification
threshold.

[FACT mlzoomcamp-2026-data-release] HW1–HW4 and HW6 were updated to use the
release and to state exact preprocessing, metrics, precision, split behavior,
and non-degenerate threshold handling. The answer options were replayed from
the generated data; keyless regeneration matched the release byte-for-byte,
the release validator passed, `datagen` tests passed 48/48, and the XGBoost
comparison was rerun. The release now also includes `validate_homework.py`,
which replays the HW1–HW4/HW6 answer calculations and checks that every
computed answer appears in the corresponding Markdown options. That check
found and corrected one stale HW1 row-count option and two HW2 options before
this release was considered verified.

[OPEN] Deployment image-size questions and stochastic deep-learning/environment
issues remain outside this tabular data release and should be handled in a
separate environment/artifact pass before the cohort opens.
