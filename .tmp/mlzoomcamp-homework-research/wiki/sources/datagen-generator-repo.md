# datagen synthetic dataset generator

<!-- Source page; evidence is summarized below with provenance markers. -->

## Provenance and confidence

- [FACT datagen-generator-repo] Alexey linked `https://github.com/alexeygrigorev/datagen` in Slack thread `1759821119.680489` immediately after saying the HW2 data was generated.
- [FACT datagen-generator-repo] The repository was inspected at shallow commit `6a5e69b9d5a0d3bff8dad3f24c53e8374a9f906b`, dated 2025-10-07. The dataset repository contains no checked-in plan or provenance file tying these exact two homework CSVs to a specific generator commit.
- [OPEN] The following findings describe the linked generator’s implementation and are strong evidence about the generation approach, but they do not prove that the exact 2025 CSV bytes were produced by this exact commit or plan.

## What the generator actually does

- [FACT datagen-generator-repo] `DatasetGenerator.generate()` samples each feature independently from its declared distribution, creates a dataframe, rounds numeric features, then computes the target, applies missingness, applies global outliers, and shuffles rows (`datagen/generator.py:31-62`).
- [FACT datagen-generator-repo] `_apply_correlations()` only logs “Applying correlations (simplified)” and returns the dataframe unchanged (`datagen/generator.py:176-187`). The normal `generate()` path does not call this method. Therefore, feature-feature correlations are not implemented by this code path even though the README and generator prompt talk about realistic correlations.
- [FACT datagen-generator-repo] The LLM prompt asks for a “realistic” plan, meaningful features, a target formula, roughly balanced classification classes, and some missing rates, but does not require a domain reference distribution, a causal/conditional dependency graph, sign constraints, physical bounds, or validation across seeds (`datagen/llm_generator.py:55-115`).
- [FACT datagen-generator-repo] Classification targets produced from a valid formula are made by thresholding formula output at zero (`formula_output >= 0`), not by drawing a Bernoulli outcome from a calibrated probability (`datagen/generator.py:189-208`). The fallback is random. This can create a sharp, deterministic boundary and makes the result depend heavily on formula scale and feature distributions.
- [FACT datagen-generator-repo] Regression targets receive noise scaled to a fraction of the generated target standard deviation, while missing values are applied independently per feature at the declared rate (`datagen/generator.py:210-223`, `:353-365`). Neither mechanism is conditioned on domain events such as a measurement being unavailable for a particular customer or vehicle class.
- [FACT datagen-generator-repo] Outliers are injected into every numeric feature at a global rate using `mean ± (3 + exponential) * std` without domain-specific bounds (`datagen/generator.py:367-400`). This can produce statistical extremes that are not physically or operationally valid.
- [FACT datagen-generator-repo] Row counts are randomized around size presets from the seed, and the LLM is asked to choose distributions/rounding. The plan schema records feature names, distributions, missing rates, and a formula, but has no fields for expected correlations, causal parents, invariants, or validation thresholds (`datagen/schemas.py:12-32`, `:46-60`).

## Validation gap

- [FACT datagen-generator-repo] The README describes generated data as realistic and gives a car-fuel example, but the tests mainly check rounding, missingness, outlier mechanics, formula parsing, class balance, and a generic AUC threshold. The classification AUC test constructs probabilities with a sigmoid and samples Bernoulli labels (`tests/test_classification_auc.py:23-64`), which is different from production thresholding at zero.
- [FACT datagen-generator-repo] No reviewed test asserts domain sign relationships, realistic conditional distributions, plausible bounds after outlier injection, stable answer ordering across seeds, separation between multiple-choice options, or consistency between a generated answer key and the homework markdown/notebook.
- [INFERENCE datagen-generator-repo] The generator is suitable as a fast prototype or fixture generator, but an LLM-generated feature list plus independent marginals is not sufficient for a realistic educational dataset. The missing correlation hook and the production/test mismatch are especially relevant to the 2025 student complaints.
