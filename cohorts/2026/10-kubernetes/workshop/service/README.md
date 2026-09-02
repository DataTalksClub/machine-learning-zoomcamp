# Kubernetes Workshop for ML Model Deployment

FastAPI service for clothing classification using ONNX Runtime.

## Setup

Download the ONNX model:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing_classifier_mobilenet_v2_latest.onnx -O clothing-model.onnx
```

Initialize the project:

```bash
uv sync
```

## Run Locally

```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

## Test

```bash
uv run python test.py
```

## Docker

Build:

```bash
docker build -t clothing-classifier:v1 .
```

Run:

```bash
docker run -it --rm -p 8080:8080 clothing-classifier:v1
```
