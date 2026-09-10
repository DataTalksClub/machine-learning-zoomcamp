# Overview

## Research question

- [FACT homework-2025-repo] “Last year” was interpreted as the 2025 cohort immediately preceding the current 2026 work. The review covers the supplied Slack export, 2025 homework markdown/notebooks/history, the two linked CSVs, the linked `datagen` repository, and the 2026 draft copies.
- [FACT slack-export-2025-homework] The material complaints cluster around HW1–HW4 tabular questions, with additional environment/reproducibility complaints in HW5, HW8, and HW9.

## Source map

| Source | What it establishes |
| --- | --- |
| `slack-export-2025-homework` | Student symptoms, dates, informal explanations, and Alexey’s workarounds/fixes. |
| `homework-2025-repo` | Exact instructions, notebook/markdown inconsistencies, and the sequence of in-cohort edits. |
| `datasets-2025-snapshot` | Dataset shape, missingness, correlations, and reproduced answer-option failures. |
| `datagen-generator-repo` | The linked generator’s independent feature sampling, thresholded classification, and validation gaps. |
| `homework-2026-draft` | Whether the known materials are already replaced for 2026. |

## Initial landscape

- [FACT homework-2025-repo] The 2025 package combined a live GitHub repository, separate notebooks, downloadable raw URLs, and answer-option forms. Several artifacts changed during the cohort.
- [FACT homework-2026-draft] The 2026 files currently inspected are drafts carried over from 2025, not a completed redesign.
- [INFERENCE slack-export-2025-homework, homework-2025-repo, datasets-2025-snapshot] There are three interacting failure classes: (1) content/version ambiguity, (2) answer options that are too close or not generated from a verified reference run, and (3) synthetic data whose statistical/domain relationships do not reliably support the intended lesson.

## Boundaries

- [FACT slack-export-2025-homework] The Slack review records reported symptoms, not a complete population survey; students often posted partial code or informal hypotheses.
- [OPEN] The exact generator plan/commit for the two CSVs is not stored with the datasets, so the generator-code findings should be treated as mechanism evidence, not a byte-for-byte provenance claim.
