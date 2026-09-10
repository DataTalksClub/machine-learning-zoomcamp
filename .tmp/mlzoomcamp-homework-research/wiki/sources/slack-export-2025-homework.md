# Slack export: 2025 homework questions and responses

<!-- Source page; evidence is summarized below with provenance markers. -->

## Source and method

- [FACT slack-export-2025-homework] The source is the user-supplied Slack export at `/home/alexey/.pocketshell/attachments/machine-learning-zoomcamp/main/20260910-123157-01-course-ml-zoomcamp.zip`, extracted into a temporary read-only analysis directory on 2026-09-10.
- [FACT slack-export-2025-homework] The review focused on messages dated 2025-09-15 through 2025-12-31 and searched for homework/module/question references, option mismatches, rounding, seeds, datasets, synthetic data, scaling, Docker image size, preprocessing, and reproducibility.
- [OPEN] Slack is an informal support channel. A student report is evidence that a symptom occurred, not proof of its root cause; community suggestions are not automatically official course guidance.

## Reports and what resolved them

### Homework 1: filter and wording confusion

- [FACT slack-export-2025-homework] In thread `1758211682.965849` on 2025-09-18, a student questioned whether the maximum-fuel-efficiency options were correct; later messages said the answer was not among the options until the dataframe was filtered to `origin == 'Asia'`. Another student noted that GitHub and the course homework page differed (`2025-09-21`).
- [FACT slack-export-2025-homework] In thread `1758213438.225589` on 2025-09-18, a student got `0.49` for the matrix question. The thread eventually found that the Asia filter had not been used when selecting the matrix rows; the corrected rows produced an available answer.
- [FACT slack-export-2025-homework] In thread `1759054167.651829` on 2025-09-28, a student used `X.dot(X.T)` instead of `X.T.dot(X)` and got a singular-matrix error. Alexey reposted the intended sequence: filter Asia, select weight/year, take the first seven rows, compute `X.T @ X`, and invert it.
- [INFERENCE slack-export-2025-homework, homework-2025-repo] The Q1 complaints combine a student implementation mistake with a real material-consistency hazard: the 2025 intro notebook says “Europe” in its explanatory cell while its executable code and markdown homework use “Asia.”

### Homework 2: lecture mismatch, transformation ambiguity, and collapsed numeric options

- [FACT slack-export-2025-homework] In thread `1759220184.998839` on 2025-09-30, students followed the car-price lecture and looked for `MSRP`, while HW2 actually uses `car_fuel_efficiency.csv` and predicts `fuel_efficiency_mpg`. The thread also identified ambiguity created by the phrase “follow the code in the lectures” because the lecture applies `log1p` to a different target.
- [FACT slack-export-2025-homework] In thread `1759232006.392029`, Alexey first said he normally looks at the data to decide whether to apply a log transform, then clarified on 2025-10-01: the homework does not instruct students to apply it to this dataset, so they should not.
- [FACT slack-export-2025-homework] In thread `1759478500.015639` on 2025-10-03, multiple students reported identical RMSE values for all listed regularization values after rounding to two decimals. Community explanations pointed to unscaled features and a very small regularization effect; some students tried flooring or printing more digits, neither of which was the stated homework procedure.
- [FACT slack-export-2025-homework] In the same thread and in `1759417893.132919`, students reported standard-deviation/test-RMSE results that did not exactly match the choices. One separate student later found a re-used shuffle index was the cause of their discrepancy, so not every mismatch was a course defect.
- [FACT slack-export-2025-homework] In thread `1759821119.680489` on 2025-10-07, a student questioned a positive horsepower/fuel-efficiency relationship. Alexey replied that the data was generated and that some correlations might not make sense, then linked `https://github.com/alexeygrigorev/datagen` as the generator.
- [FACT slack-export-2025-homework] In thread `1759855134.423779`, students reported all RMSE values near `0.038` when using a log-transformed target; another student advised removing the log transform, and a fresh notebook plus the specified NA handling resolved at least one report. Alexey also said in thread `1759846997.715189` that even correct code could land between options and advised selecting an option and moving on.
- [FACT slack-export-2025-homework] Alexey’s operational responses were mostly workarounds: follow the written instructions, do not use `log1p` unless instructed, select the closest/any option when the result is between options, and accept that exact reproducibility was a challenge.

### Homework 3: weakly discriminating classification questions

- [FACT slack-export-2025-homework] In threads `1760264156.083519`, `1760286271.009029`, and `1760286485.938019` on 2025-10-12, students reported that validation accuracy was between the choices or that every listed `C` value produced exactly the same accuracy, even without rounding.
- [FACT slack-export-2025-homework] The same discussion included one genuine student error: a participant initially used the wrong split seed and fixed one answer after changing it to `42`. This does not explain the repeated same-accuracy reports from other students.
- [FACT slack-export-2025-homework] A community explanation correctly noted that different logistic-regression coefficients can leave every validation class prediction unchanged, so accuracy can be identical across `C`; the thread also explicitly described the dataset as synthetic/generated.
- [FACT slack-export-2025-homework] In thread `1760370872.456799` on 2025-10-13, students repeatedly reported `0.70` for Q4 while the choices were `0.64`, `0.74`, `0.84`, and `0.94`; a student reported `0.70` for every `C` in Q6 as well. The practical response was to select the closest option (`0.74`) and use the smallest `C` on a tie.
- [FACT slack-export-2025-homework] In thread `1760273609.041829` and related messages, students asked whether the target should be included in the correlation matrix. The written homework was later clarified to exclude the target and to consider only the listed pairs; the repository records that change in commit `ba25a5e`.

### Homework 4: stale material and undocumented preprocessing

- [FACT slack-export-2025-homework] In thread `1760739881.321829` on 2025-10-17, a student realized they had not fetched the new repository and had worked on a draft using the wrong dataset. The reminder was to check that course material was updated.
- [FACT slack-export-2025-homework] In thread `1760481314.348929` from 2025-10-14 onward, students reported Q2 AUC values between or far from the options. Some found that changing the solver, increasing iterations, or applying `StandardScaler` produced an available choice, although scaling was not in the stated procedure. Alexey said his preparation used no scaler and advised using the closest option.
- [FACT slack-export-2025-homework] Alexey later summarized the issue in that thread as a reproducibility challenge, not a student mistake, and said the instructions had been updated. The thread still contains reports that different strategies produced different answers for later questions.

### Homework 5 and 9: environment-dependent Docker measurements

- [FACT slack-export-2025-homework] In thread `1761394314.367929` on 2025-10-25, students reported that the pulled base Docker image size was not any listed option; one was on Windows. Alexey said his value matched, advised choosing the closest value, then chose the higher option for an exact tie and said he would add that rule to the instructions.
- [FACT slack-export-2025-homework] The repository history shows the “choose the higher value if exactly between two options” wording was added across homework files in commit `a4519a9` on 2025-10-25, after these reports.
- [FACT slack-export-2025-homework] In thread `1762951557.779209` on 2025-11-12, several students got `200` rather than the expected `80` for a model-size/estimator question because the metric still appeared to improve when rounded to three decimals. Alexey said he would reproduce it and then accepted `200` as correct. In thread `1762869041.309119`, he later confirmed that `0.99` was correct for another disputed HW5 answer and said he would re-score.
- [FACT slack-export-2025-homework] In thread `1765198248.651289` in December, a Windows student still got a Docker size between choices even after trying WSL2; another student got the expected value in GitHub Codespaces. This is direct evidence that “closest” did not eliminate environment dependence.

### Homework 8 and 9: training/inference reproducibility

- [FACT slack-export-2025-homework] HW8 questions generated confusion about the absence of a separate validation set; in thread `1764098862.897439` Alexey confirmed that the assignment was intended to use only train/test.
- [FACT slack-export-2025-homework] The 2025 HW8 instructions themselves recommend setting random seeds and warn that exact results cannot be guaranteed. Students also asked about changing environments, GPU availability, PyTorch setup, and augmentation behavior.
- [FACT slack-export-2025-homework] In thread `1765139344.098649` on 2025-12-07, a student reported different HW9 predictions depending on whether the deterministic preprocessing or the random augmentation pipeline from HW8 was used. The first pipeline was the sensible inference interpretation, but the question wording invited the ambiguity.

## Additional reports: specification, release, and environment problems

These reports are important for the 2026 redesign, but they are not all caused by the generated tabular data.

### HW1 and course access

- [FACT slack-export-2025-homework] In thread `1757986117.988419`, students found that the 2025 homework entry initially still pointed to 2024 material, the assignment was not ready, and submission appeared closed. In thread `1758090195.114639`, the HW1 submission link pointed to HW2; Alexey updated it, and a student fix PR (`#655`) was merged.
- [FACT slack-export-2025-homework] In thread `1758628798.289319`, a student understood the matrix operations incorrectly and also found the Q7 wording confusing; the student suggested splitting “transpose” and “multiply” into separate steps, and Alexey welcomed a PR with wording improvements.
- [FACT slack-export-2025-homework] GitHub login failures were reported in `1758917406.019119` and `1758984780.561219`; students were advised to use Google login. Another thread (`1758345135.981859`) shows that students expected an immediate score, while the community clarified that scores would appear after the deadline. These are access/expectation issues rather than data issues.

### HW2: under-specified preprocessing

- [FACT slack-export-2025-homework] In `1759692752.258669`, a student asked whether validation and test missing values should be filled and which mean to use, reporting significantly different results. Community guidance settled on applying the training-set mean to all splits, or zero to all splits for the zero-imputation branch; this was not obvious enough from the question wording.
- [FACT slack-export-2025-homework] In `1759754094.341379`, students asked whether standardization was allowed even though it was not stated. A bot recommended `StandardScaler`, and students reported that scaling changed the answers. This is an assessment-contract problem because ridge values depend on feature scale.
- [FACT slack-export-2025-homework] Some HW2 mismatches were ordinary implementation errors: `1759774426.212589` identifies reusing `X_val` instead of `X_test` and using the wrong split as common causes. The later tie-rule reports (`1760111814.927439` and `1760621683.479969`) show that students could still be graded wrong when all rounded RMSEs looked identical.

### HW3: procedure ambiguity beyond the synthetic signal

- [FACT slack-export-2025-homework] In `1760201213.969009`, students disagreed about whether feature elimination should drop a categorical source column before one-hot encoding or drop its derived one-hot columns afterward. Different interpretations changed the answer.
- [FACT slack-export-2025-homework] In `1760392107.098229`, students asked which probability threshold to use for converting predictions to classes; a participant cited earlier guidance from Alexey to use `0.5`, but that threshold was not clearly stated in the assignment.
- [FACT slack-export-2025-homework] In `1760093955.003239`, students asked whether Q5 accuracy belonged to validation or test. The surrounding convention suggested validation, but the need to ask indicates the split contract was not explicit enough.
- [FACT slack-export-2025-homework] The same-C problem was still being reported in `1765451658.296069` on 2025-12-11, nearly two months after the first reports. This shows that “choose the smallest C” handled grading but did not make the question pedagogically informative.

### HW4: stale names, metric wording, and precision

- [FACT slack-export-2025-homework] In `1760949459.353179`, HW4 was described as Bank Marketing while the link and features were for `course_lead_scoring.csv`; students also saw FAQ references to `bank-full.csv` and `balance`. Alexey replied, “I'll edit it.”
- [FACT slack-export-2025-homework] In `1760994954.744669`, a student found Q1’s instruction to use each numeric variable as a prediction and compute AUC confusing because the variables themselves were not binary. In `1760588443.321539`, another student asked whether “mean score” meant accuracy or AUC; the community inferred AUC from the surrounding questions.
- [FACT slack-export-2025-homework] In `1760830082.890739`, a student noticed that Q3 answer choices had three decimal places while the threshold search advanced in steps of `0.01`. Threads `1761077483.804179` and `1761209432.653979` add validation/test confusion and multiple reports that results did not match the choices.

### HW5 and HW6: deployment and lesson-contract problems

- [FACT slack-export-2025-homework] In `1761179635.146459`, students discovered that the current 2025 deployment homework used `uv` while the easily found 2024 material still used `pip`; the updated 2025 link had been shared in Telegram. In `1761495998.645299`, installing the old `scikit-learn==0.24.2` on a modern Codespaces/Python environment failed, followed by `numpy._core` pickle errors. The eventual workarounds were to use an older environment or `uv`, not to change the assignment.
- [FACT slack-export-2025-homework] In `1761398394.458069`, Q4 and Q6 produced the same client probability for some students, who were unsure whether the Docker exercise used the same model. Alexey said to use the model in the Docker image and explained that he included it to reduce confusion; students then discovered that Q6 used `pipeline_v2.bin`, not the local `pipeline_v1.bin`. A later `1761866119.061349` report shows that the model path/workdir (`/code`) was also easy to get wrong.
- [FACT slack-export-2025-homework] In `1762118406.383309`, a student asked what to do with the unused test split in HW6; Alexey confirmed that using it that way was acceptable. In `1762499989.844489`, a student noted that the lessons covered `DecisionTreeClassifier` while HW6 required `DecisionTreeRegressor`; Alexey said students would figure it out as part of the homework. This is a deliberate extension, but it was experienced as a missing prerequisite.

### HW8–HW10: moving targets and framework/deployment ambiguity

- [FACT slack-export-2025-homework] In `1763528191.606659`, Saturn Cloud’s interface and availability differed from the video, including a regional `403`; Alexey directed students to Colab or local execution and said the models were light enough to run with patience.
- [FACT slack-export-2025-homework] In `1764099786.708559` and `1764445575.010709`, students reported that the HW8 output-activation instruction conflicted with the listed loss functions and the provided `torch.sigmoid` accuracy code. Students were unsure whether to remove the output sigmoid or use a loss not listed in the choices.
- [FACT slack-export-2025-homework] Alexey confirmed in `1764098862.897439` that HW8 intentionally used only train and test, but students still encountered `validation_loader`/`validation_dataset` names in the provided code and asked whether they should create another split (`1764543910.206599`). Random augmentation, CPU/GPU differences, and the explicit warning that exact results were not guaranteed made exact multiple-choice outputs especially fragile.
- [FACT slack-export-2025-homework] In `1765143730.975559`, HW9 referred to the 2024 hairstyle image/model even though the cohort needed the 2025 v1 image. Alexey confirmed on `1765184113.263199` that it was a copy-paste error and accepted the correction PR. Students also needed help with the expected NCHW tensor shape versus HWC (`1765218922.102599`) and whether to extend or merely run the supplied Docker image (`1765249440.904589`).
- [FACT slack-export-2025-homework] In `1765643360.679809`, the HW10 homework link was still announced as TBA. In `1765256928.082999`, the old Keras model failed under Keras 3; Alexey directed students to the newer model in the serverless workshop. These are stale-material/dependency problems, not generated-data problems.

## What students and staff were effectively offered

- [FACT slack-export-2025-homework] The recurring remedies were: re-fetch the current repository, use the dataset named in the homework, follow the written preprocessing and seed, print more precision while diagnosing, select the closest answer, use the smallest hyperparameter on a tie, use the higher option for an exact midpoint, and ask for re-scoring when many students saw the same result.
- [FACT slack-export-2025-homework] These remedies improved grading tolerance but did not repair the underlying assessment design. No Slack thread found in this review documents a systematic re-generation or statistical validation of the car/lead datasets after the synthetic-data complaints.
