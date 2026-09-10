# Log

2026-09-10T12:36:59+02:00 | init | created building project | seed
2026-09-10T12:37:20+02:00 | scope | froze seed | sha256:3e3c6337ff79832b2c6d11eb2d8365a7160b342d7638f26ec5682f8299e44b10
2026-09-10T13:00:00+02:00 | research | selected slack-export-2025-homework, homework-2025-repo, datasets-2025-snapshot, datagen-generator-repo, homework-2026-draft | triangulated reported symptoms, repository defects, dataset behavior, generator behavior, and 2026 carry-over status
2026-09-10T13:05:00+02:00 | research | reproduced HW2/HW3 reference calculations | verified rounded RMSE ties, missing/near options, and same-C validation accuracy on the downloaded CSV hashes
2026-09-10T13:10:00+02:00 | distilled | wrote overview, synthesis, open-questions, and guideline | converted evidence into a data-and-assessment redesign handoff
2026-09-10T13:11:00+02:00 | lint | passed | 0 errors, 0 warnings
2026-09-10T13:15:00+02:00 | distilled | added report.md | created a concise handoff linking the evidence pages and implementation guideline
2026-09-10T13:16:00+02:00 | distilled | expanded report with static HW6/HW4/HW1 defects | connected notebook inconsistencies to the Slack-reported symptoms
2026-09-10T12:59:37+02:00 | state | scoped -> researching | Selected and reviewed the Slack export, 2025 homework/history, dataset snapshots, linked generator, and 2026 drafts.
2026-09-10T12:59:42+02:00 | state | researching -> distilled | Evidence pages and quantitative synthesis are complete; open questions and design implications are documented.
2026-09-10T12:59:47+02:00 | state | distilled -> critiqued | Reflection and decision review completed; evidence limits and accepted risks are explicit.
2026-09-10T12:59:47+02:00 | state | critiqued -> ready | Guideline is distilled, critique is complete, and the research wiki passes lint.
2026-09-10T13:30:00+02:00 | audit | expanded Slack/repository evidence | Added HW1–HW10 release, wording, environment, framework, and deployment reports; separated student mistakes from course defects and recorded Alexey's documented remedies.
2026-09-10T15:15:00+02:00 | implementation | extended sibling datagen | Added dependency-aware derived features, bounds, conditional missingness, calibrated Bernoulli-logistic labels, target controls, and relationship/bound reporting while preserving legacy plans.
2026-09-10T15:16:00+02:00 | implementation | created 2026 data release | Generated car and lead CSVs from reviewed keyless plans with seed 20260910; stored plans, reports, data card, and release validation script in cohorts/2026/data.
2026-09-10T15:17:00+02:00 | implementation | rewrote answerable homework contracts | Updated HW1–HW4 and HW6 URLs, option sets, precision, split/metric wording, threshold policy, and tree sweep; removed closest-option fallback from the redesigned assignments.
2026-09-10T15:18:00+02:00 | verification | passed | datagen pytest: 48 passed; keyless regeneration byte-matched both release CSVs; release validator passed; HW1–HW4/HW6 reference replays and XGBoost eta comparison completed.
2026-09-10T15:20:14+02:00 | state | ready -> implemented | Implemented the reviewed keyless datagen plans, pinned 2026 data release, validation script, and redesigned HW1-HW4/HW6 contracts.
2026-09-10T15:32:39+02:00 | state | implemented -> verified | Release validator, deterministic keyless regeneration, generator tests, homework reference replays, XGBoost comparison, and research lint all pass.
2026-09-10T16:00:00+02:00 | verification | added homework contract replay | Recomputed HW1-HW4/HW6 answers from the current release using the procedures stated in each assignment; corrected stale HW1 row-count and HW2 seed-sensitivity/test-RMSE options; the new validator passes.
