# ML Zoomcamp 2026 deployment release

This directory contains the frozen lead-scoring artifact used by Homework 5
and Homework 10. It is trained from
`cohorts/2026/data/course_lead_scoring_2026.csv`, not from a prior cohort's
dataset.

The API accepts the eight observable fields in the release. Missing numeric
values are replaced with medians calculated from the training CSV and recorded
in `feature_defaults.json`; missing categories use `NA`.

## Local run

```bash
uv sync --locked
uv run python smoke_test.py
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

In another terminal:

```bash
python q6_test.py
```

## Container run

```bash
docker build -t zoomcamp-model:2026-hw10 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw10
```

The API exposes `GET /health` and `POST /predict`. The model artifact is
addressed by its checksum in `model_metadata.json`; the API health response
also reports the feature-default checksum. The Dockerfile pins the Python and
uv image digests and installs from the checked-in lockfile.
