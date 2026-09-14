## Homework 5: Deploying Machine Learning Models

This homework uses a frozen lead-scoring release for the 2026 cohort. The
artifact, dataset checksum, training script, API, and container definition are
in this directory. No prior-cohort model or generated answer set is used.

The model was trained from
[`course_lead_scoring_2026.csv`](../../data/course_lead_scoring_2026.csv) with
the following observable features:

| Feature | Type | Missing-value rule |
| --- | --- | --- |
| `lead_source` | categorical | `NA` |
| `industry` | categorical | `NA` |
| `employment_status` | categorical | `NA` |
| `location` | categorical | `NA` |
| `number_of_courses_viewed` | integer | training-set median |
| `annual_income` | number | training-set median |
| `interaction_count` | integer | training-set median |
| `lead_score` | number | training-set median |

We use a `DictVectorizer` followed by
`LogisticRegression(solver="liblinear", C=1.0)`. The training script records
the data checksum and imputation values in `model_metadata.json`.
`lead_score` is available before conversion and `converted` is the target.

## Setup

Use Python 3.11.15 and `uv`:

```bash
cd cohorts/2026/homework/05-deployment
uv sync --locked
uv run python smoke_test.py
```

The smoke test loads the checked-in model and verifies that inference is
deterministic. Check the artifact before using it:

```bash
sha256sum pipeline.bin
```

It must be:

```text
1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1  pipeline.bin
```

## Question 1 — environment check

Run `uv --version` and record the version in your notes. This is a setup check,
not a graded answer: your local `uv` version is not a property of the model.

## Question 2 — locked dependency

Open `pyproject.toml` and `uv.lock`. Which Scikit-Learn version is part of the
2026 reference environment?

- `1.6.1`
- `1.7.2`
- `1.8.0`
- `2.0.0`

Do not regenerate the lockfile for the graded run; use `uv sync --locked`.

## Question 3 — load the model

Write a Python script that loads `pipeline.bin` with `pickle` and calls
`predict_proba` for this lead:

```json
{
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}
```

Report the probability of conversion rounded to three decimal places. The
grader accepts an absolute error of at most `0.005`; do not choose the nearest
answer from a list.

## Question 4 — serve the model

Start the provided API:

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

The API has `GET /health` and `POST /predict`. Send this second lead:

```json
{
  "lead_source": "organic_search",
  "industry": "technology",
  "employment_status": "employed",
  "location": "europe",
  "number_of_courses_viewed": 4,
  "annual_income": 80304.0,
  "interaction_count": 7,
  "lead_score": 0.74
}
```

For example:

```bash
curl -s http://localhost:9696/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74
  }'
```

Report `conversion_probability` rounded to three decimal places. The same
`0.005` absolute tolerance applies. The response must contain a probability in
`[0, 1]` and a boolean `conversion` field.

## Container

The checked-in `Dockerfile` is the canonical 2026 container configuration. It uses
Python `3.11.15-slim-bookworm`, `uv 0.10.11`, and the checked-in `uv.lock`.
It copies the frozen artifact and starts the API on port `9696`.

Build and run it:

```bash
docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
```

## Question 5 — look at the container configuration

Which Python base-image tag is declared in the Dockerfile?

- `python:3.9-slim-bullseye`
- `python:3.11.15-slim-bookworm`
- `python:3.12-slim-bookworm`
- `python:3.13.10-slim-bookworm`

This question checks a version-controlled declaration. The displayed size of a
local Docker image is not graded because it varies by platform, architecture,
Docker version, and cached layers.

## Question 6 — run the container

Run the same request from Question 4 against the container. You can use the
provided smoke client:

```bash
python q6_test.py
```

Report `conversion_probability` rounded to three decimal places. The expected
result is the same reference inference as Question 4, with the same `0.005`
absolute tolerance. Also verify that:

```bash
curl -s http://localhost:9696/health
```

returns `{"status":"ok", ...}` and the model checksum recorded in
`model_metadata.json`.

## Submit the results

Submit the results here:
<https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw05>.

Submit numeric probabilities to three decimal places. The tolerance is part of
the grading policy, so numeric answers use the stated tolerance.
