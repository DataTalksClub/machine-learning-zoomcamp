# Open questions

## Questions that should be resolved before implementation

- [OPEN] Which exact plan, generator commit, seed, dependency lock, and post-processing steps produced `car_fuel_efficiency.csv` and `course_lead_scoring.csv`? Preserve them, or explicitly classify the next files as a new version.
- [OPEN] Should the 2026 course use a real, immutable public dataset, a synthetic dataset calibrated from a real one, or both? A recommended answer is both: a small real dataset for domain intuition and a controlled synthetic fixture for exercises that require known relationships.
- [OPEN] Which questions are intended to teach an algorithmic procedure versus a domain observation? Questions based on accidental sample correlations or exact Docker display sizes should not be retained without changing their learning objective.
- [OPEN] What dependency matrix will the course officially support? The answer key should be produced with that lockfile and checked on at least CPU/Linux plus the most common student environment.
- [OPEN] Should notebooks remain answer-bearing companion artifacts? If yes, markdown and notebooks need a consistency test; if no, remove or clearly label them as optional reference notebooks.
- [OPEN] For HW8/HW9, what result is meant to be reproducible: model training, deterministic inference, or conceptual understanding? Random augmentation and local Docker measurements should not be graded as exact scalar answers.

## Recommended defaults if no further decision is made

- [INFERENCE datasets-2025-snapshot, datagen-generator-repo] Freeze a versioned dataset plus SHA-256 and data card; use a domain-constrained generator or a real snapshot rather than a one-shot LLM plan.
- [INFERENCE homework-2025-repo] Grade numeric answers with tolerances or code/output checks, and derive multiple-choice options from the verified reference result with a minimum separation test.
- [INFERENCE slack-export-2025-homework] Treat “choose closest” as an emergency grading tolerance, not as the normal contract presented to learners.
