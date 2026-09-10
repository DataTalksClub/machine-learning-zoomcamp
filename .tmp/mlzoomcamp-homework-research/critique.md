# Critique

## Reflection

- [FACT slack-export-2025-homework] The strongest evidence is not a single complaint but a repeated pattern: students independently observed rounded ties, missing options, stale material, and generated-data relationships that did not support the intended intuition.
- [FACT datasets-2025-snapshot] Reproducing HW2/HW3 on the downloaded files materially strengthened the diagnosis; it prevents treating every Slack report as a student coding error.
- [OPEN] Exact CSV-to-generator provenance remains the largest evidence gap. The report deliberately distinguishes the linked generator’s implementation from proof that this exact commit generated the two files.

## Decision review

- [INFERENCE slack-export-2025-homework, datasets-2025-snapshot, datagen-generator-repo] The recommended decision is a combined data-and-assessment redesign: domain-constrained/versioned data plus an automated answerability gate. Choosing only more realistic marginals would leave the release and grading failures intact.
- [INFERENCE homework-2026-draft] The 2026 drafts should be treated as migration input, not as evidence that fixes are already implemented.

## Accepted risks

- [OPEN] The Slack export may omit private conversations and does not quantify how many students experienced each issue.
- [OPEN] Raw URLs may change in the future; the measured hashes identify this analysis snapshot but do not create a public immutable release.
- [OPEN] The generator repository was reviewed at one shallow commit and may have changed since; recommendations should be rechecked against the exact generator version selected for 2026.
- [INFERENCE slack-export-2025-homework] The report intentionally leaves deep-learning conceptual difficulty separate from the generated-tabular-data diagnosis; those modules need their own reproducibility review.

## Implementation review

- [FACT mlzoomcamp-2026-data-release] The implementation follows the combined
  data-and-assessment recommendation: the plans express relationships directly,
  the generator enforces bounds and calibrated labels, and the course release
  includes hashes, reports, and a validator.
- [INFERENCE mlzoomcamp-2026-data-release] The largest deliberate deviation from
  the guideline is retaining multiple-choice questions for this pass. They now
  use validated options and explicit precision, but tolerance-based grading is
  still preferable for the eventual course platform.
- [FACT mlzoomcamp-2026-data-release] HW2 keeps the lecture's unscaled normal
  equation so it remains compatible with the lesson. Instead of inventing a
  new scaling convention, the reference release uses four-decimal RMSE for
  regularization and three-decimal RMSE for imputation; both comparisons are
  now separated on the actual data.
- [OPEN] The generator modifications are not yet tagged in the sibling git
  repository. Before public publication, tag or vendor that exact revision and
  rerun the checksum gate from a clean checkout.
