# ML Zoomcamp repository: 2025 homework and git history

<!-- Source page; evidence is summarized below with provenance markers. -->

## Scope

- [FACT homework-2025-repo] The 2025 cohort contains homework for modules 1, 2, 3, 4, 5, 6, 8, 9, and 10. The 2025 tabular assignments use two downloadable CSVs: `car_fuel_efficiency.csv` for modules 1, 2, and 6, and `course_lead_scoring.csv` for modules 3, 4, and 5.
- [FACT homework-2025-repo] The initial 2025 homework commit was `80e1809` on 2025-09-15. The next-day commits `8500a54` and `0aedbac` replaced the initial HW2/HW3 draft material with the car-fuel and lead-scoring datasets and changed their questions/options.
- [FACT homework-2025-repo] Important in-cohort edits were made after publication: `6c38123` added the smallest-`r` tie rule on 2025-10-04; `ba25a5e` restricted HW3 correlation answers to specified pairs on 2025-10-04; `2cf7cc1`, `771188a`, and `8b1f57f` continued HW4/HW3 updates; `a4519a9` added the generic closest/higher-midpoint wording on 2025-10-25.
- [INFERENCE homework-2025-repo] This chronology indicates a live, iterative release rather than a fully frozen and validated homework package. It explains why students could be working from different drafts, but it is not by itself evidence that every mismatch came from the release process.

## Concrete homework and notebook defects

### Intro and regression

- [FACT homework-2025-repo] The written HW1 says to select cars from Asia in the normal-equation question (`cohorts/2025/01-intro/homework.md:85`), but the shipped HW1 notebook’s explanatory cell says Europe while its executable selection uses Asia (`cohorts/2025/01-intro/homework_1.ipynb:875`, `:895`).
- [FACT homework-2025-repo] HW2 explicitly says the target is `fuel_efficiency_mpg`, says to use the five listed columns, instructs students to use the lecture split code, rounds Q4 RMSE to two decimals, and selects the smallest `r` on a rounded tie (`cohorts/2025/02-regression/homework.md:10`, `:67`, `:86`).
- [FACT homework-2025-repo] The HW2 notebook is a separately committed artifact (`771188a`) and should be treated as a second source of truth requiring consistency checks. Its code list for Q4 omits some values present in the markdown list, while the markdown Q3 asks students to compare zero versus training-mean imputation and the notebook’s narrative answer contains a different imputation wording.

### Classification and evaluation

- [FACT homework-2025-repo] HW3 fixes the target as `converted`, says the target must be excluded from `X`, restricts Q2 to the listed numeric feature pairs, pins the Q4 logistic-regression parameters, and tells students to choose the smallest `C` on a tie (`cohorts/2025/03-classification/homework.md:10`, `:53`, `:74`, `:114`). These restrictions were not all present in the initial published version.
- [FACT homework-2025-repo] The HW3 notebook has a history of target-name and question-text corrections; its Q6 narrative and code had differing candidate-`C` lists before later edits. This is a notebook/markdown synchronization risk even when the final markdown is clearer.
- [FACT homework-2025-repo] The HW4 notebook still contains old car-price-style references such as `above_average` and `engine_hp` in its Q1 text while loading the lead-scoring CSV (`cohorts/2025/04-evaluation/homework_4.ipynb:35`, `:110`, `:116`). Its Q6 text lists `[0.01, 0.1, 0.5, 10]`, whereas the final markdown lists `[0.000001, 0.001, 1]` (`cohorts/2025/04-evaluation/homework_4.ipynb:849`, `cohorts/2025/04-evaluation/homework.md:128`).

### Trees and later modules

- [FACT homework-2025-repo] The HW6 notebook loads the car-fuel data but its Q5 options refer to unrelated student-performance features (`study_hours_per_week`, `attendance_rate`, `distance_to_school`, `teacher_quality`), and its XGBoost-output parser labels regression values as `train_auc`/`val_auc` (`cohorts/2025/06-trees/homework.ipynb:28`, `:2008`, `:2121`). The written HW6 markdown uses car-specific feature names, so the notebook and markdown are materially inconsistent.
- [FACT homework-2025-repo] HW8 uses approximately 1,000 hair images, asks students to train a CNN with random augmentation, recommends seeds, and warns that exact results are not guaranteed (`cohorts/2025/08-deep-learning/homework.md:11`, `:40`, `:254`).
- [FACT homework-2025-repo] HW5 and HW9 ask students to select a fixed multiple-choice Docker image size based on `docker images` (`cohorts/2025/05-deployment/homework.md:128`, `:150`, `:159`; `cohorts/2025/09-serverless/homework.md:137`, `:146`). Local display size is a poor fixed-answer measurement unless the image reference, Docker version, platform, and measurement definition are controlled.

### Later-module release hazards

- [FACT homework-2025-repo] HW5’s 2025 instructions moved the environment from the older pip-based material to `uv`, while students were still finding the 2024 homework. The 2025 assignment also distinguishes the local `pipeline_v1.bin` exercise from the `pipeline_v2.bin` artifact already inside the Docker image. This is a valid deployment concept, but the artifact identity and working directory need to be made explicit before grading.
- [FACT homework-2025-repo] Commit `6a4918e` changed HW8 from TensorFlow/Keras to PyTorch on 2025-11-16, added PyTorch 2.8.0 and new training code, and removed the draft marker. The resulting homework says the data has train and test directories, but its sample loop refers to `validation_loader` and `validation_dataset` (`cohorts/2025/08-deep-learning/homework.md:22`, `:174`, `:186`). Commit `9df44dd` added an explicit train/test clarification on 2025-12-01, after the cohort had already started the assignment.
- [FACT homework-2025-repo] The current HW8 text simultaneously requires an output activation and lists `BCEWithLogitsLoss()` as a choice, while its sample accuracy calculation applies `torch.sigmoid` to the model output (`cohorts/2025/08-deep-learning/homework.md:75-92`, `:159-160`). That combination is answerable only if the intended model/loss contract is stated explicitly.
- [FACT homework-2025-repo] HW9 now names the 2025 model and explains that the base image contains a different model (`cohorts/2025/09-serverless/homework.md:127-158`), but the Slack history records that students initially saw 2024 references. The repository also contains a later Docker URL fix (`e9a84f4`) and a 2025-vs-2024 typo fix in the Kubernetes homework (`fb2c805`), confirming that deployment links and model references were corrected during the cohort.
- [FACT homework-2025-repo] HW10 still contains a stale `course-zoomcamp/...` path in its build instructions (`cohorts/2025/10-kubernetes/homework.md:17`), whereas the repository is cloned as `machine-learning-zoomcamp`. This was not the main Slack complaint, but it is the same class of copy/paste defect.

## 2026 carry-over risk

- [FACT homework-2026-draft] The 2026 homework files are explicitly marked `[DRAFT]` and say they are carried over from 2025 while questions, datasets, and models are to be updated before each module. The 2026 HW1, HW2, HW3, HW4, HW5, HW6, HW8, HW9, and HW10 drafts therefore cannot be treated as already redesigned.
- [FACT homework-2026-draft] In particular, the 2026 HW1 and HW2 drafts still point at the same `car_fuel_efficiency.csv`, and the 2026 HW3 and HW4 drafts still point at the same `course_lead_scoring.csv` (`cohorts/2026/homework/01-intro/homework.md:23`, `cohorts/2026/homework/02-regression/homework.md:13`, `cohorts/2026/homework/03-classification/homework.md:13`, `cohorts/2026/homework/04-evaluation/homework.md:12`).
