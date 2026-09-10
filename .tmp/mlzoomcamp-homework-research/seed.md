# ML Zoomcamp 2025 homework reliability and realistic-data redesign

## Problem

Students in the 2025 ML Zoomcamp cohort reported homework results that did not match the multiple-choice options, ties where a hyperparameter should have mattered, confusing differences between the lecture dataset and the homework dataset, and results that felt implausible because the data was generated. The course author wants to understand the reports, the responses or fixes offered, and the underlying homework/data-design causes before preparing more realistic homework data for the 2026 cohort.

## Desired behavior

Produce an evidence-grounded diagnosis of the 2025 homework problems and a practical redesign direction for generated datasets and homework questions. The redesigned assignments should preserve the teaching objectives while making the data-generating relationships plausible, the expected results reproducible, and the answer options and instructions robust across supported environments.

## Acceptance criteria

- [ ] Identify the material homework complaints in the supplied Slack export for the 2025 cohort, with dates, homework/question references, and the reported symptom.
- [ ] Record the response, workaround, or fix offered by Alexey or the community where the thread contains one, distinguishing an actual fix from advice or speculation.
- [ ] Inspect the 2025 homework files and relevant repository history to connect each complaint to a concrete instruction, dataset, preprocessing choice, generated-data property, or environment dependency.
- [ ] Separate confirmed evidence from agent inference and unresolved uncertainty.
- [ ] Recommend a realistic-data and assessment design that addresses the observed failure modes, including reproducibility and option-generation safeguards.
- [ ] Do not modify the target course repository as part of this research pass.

## Constraints

The supplied Slack archive and the target repository are read-only research inputs. The report should focus on the 2025 cohort immediately preceding 2026, while noting if evidence comes from an earlier or later cohort. Recommendations should remain feasible for a free, self-paced course and should not require access to private student data. Preserve exact provenance to local source files, commits, and Slack-thread identifiers where possible.

## Current understanding

Initial signals suggest at least two interacting causes: synthetic/generated tabular data can contain implausible or weak relationships and can make regularization/hyperparameter comparisons collapse after rounding; separately, students followed lecture material built around a different car-price dataset, and some answer-option or environment issues were corrected after publication. The extent to which the synthetic data itself caused wrong answers versus exposing student implementation mistakes remains to be established.

## Comparison sources

The supplied Slack export; the 2025 homework markdown/notebooks and git history in the target repository; the data-generation repository linked in the relevant Slack thread; and the 2026 homework materials for any already-adopted changes.

## Non-goals

Do not grade or identify individual students, reconstruct every ordinary “how do I code this?” question, redesign the entire curriculum, or implement the 2026 homework changes during this research pass.
