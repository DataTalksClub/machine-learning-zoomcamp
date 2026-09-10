# ML Zoomcamp 2026 data release

These datasets support the 2026 regression, classification, evaluation, and
trees homeworks. We generate them from reviewed JSON plans with the sibling
`datagen` project. This release needs no OpenAI API key.

The reproducible command is:

```bash
cd ../datagen
env -u OPENAI_API_KEY uv run python datagen.py \
  --plan ../machine-learning-zoomcamp/cohorts/2026/data/plans/car_fuel_efficiency_2026_plan.json \
  --accept \
  --outdir ../machine-learning-zoomcamp/cohorts/2026/data
```

Replace the plan filename in that command with
`course_lead_scoring_2026_plan.json` to generate the lead dataset. We edit the
plans directly. The reports record relationships, missingness, class balance,
and bound checks.

The reference replay used Python 3.11.15, NumPy 2.3.3, Pandas 2.3.2, and
Scikit-Learn 1.7.2. The XGBoost check used XGBoost 3.2.0. A public release
should pin these versions (or grade the numeric questions with a tolerance)
before opening submissions.

Run the release checks from the course repository root:

```bash
python cohorts/2026/data/validate_release.py
python cohorts/2026/data/validate_homework.py
```

The second command recomputes the answers for HW1-HW4 and HW6, then checks
that every result is present in the corresponding homework options.

## Files

The release contains these files:

- `car_fuel_efficiency_2026.csv`: 10,000 automotive regression rows.
- `course_lead_scoring_2026.csv`: 5,000 marketing classification rows.
- `plans/`: reviewed generator inputs.
- `*_report.json`: generation and data-quality reports.
- `validate_homework.py`: reference answer and option consistency check.

The car data uses physically connected vehicle measurements, and we derive each
measurement in dependency order. MPG has plausible directions and bounded
values. Missing horsepower is more common for older vehicles, while acceleration
has a modest origin-dependent missingness mechanism.

The lead data follows a funnel. Acquisition source and employment influence
engagement, and engagement influences interactions and lead score. We sample
conversion from a calibrated logistic probability. That gives the
classification homeworks genuine correlations and non-deterministic labels.
It also gives them conditional missingness instead of independent columns and
a hard threshold.

## Release checksums

SHA-256 checksums for the generated release:

```text
00a5cab178a8b7cd6e9157ee71dabc236ba7f20b1832336d358b07af14ba431f  car_fuel_efficiency_2026.csv
2d9da196bdefd2a45aa0a17ca21c19f06a5d9d56af628be1f04bbb3531cc12e9  course_lead_scoring_2026.csv
de4f1bc9f72ea77f9a18a5a8fe12ca6eec8bc66440ab42bedb09617bf6b9866d  plans/car_fuel_efficiency_2026_plan.json
3d096b4288eb794718191a0a9933f72fafe9f910d864b1144a95b4c6ee198ae9  plans/course_lead_scoring_2026_plan.json
```

The reports include a measured generation-time field, so their JSON hashes can
vary by a few hundredths of a second between runs. Run `validate_release.py` to
check their relationship, missingness, and bound values. The CSVs and plans
above are the immutable release files.
