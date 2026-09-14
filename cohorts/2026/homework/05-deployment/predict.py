from __future__ import annotations

import hashlib
import os
import pickle
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from model import DEFAULTS_PATH, normalize_record


MODEL_PATH = Path(os.getenv("MODEL_PATH", Path(__file__).with_name("pipeline.bin")))
with MODEL_PATH.open("rb") as model_file:
    pipeline = pickle.load(model_file)
MODEL_SHA256 = hashlib.sha256(MODEL_PATH.read_bytes()).hexdigest()
FEATURE_DEFAULTS_SHA256 = hashlib.sha256(DEFAULTS_PATH.read_bytes()).hexdigest()

app = FastAPI(title="ML Zoomcamp 2026 lead scoring")


class Lead(BaseModel):
    lead_source: str | None = None
    industry: str | None = None
    employment_status: str | None = None
    location: str | None = None
    number_of_courses_viewed: int | None = None
    annual_income: float | None = None
    interaction_count: int | None = None
    lead_score: float | None = None


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "model_sha256": MODEL_SHA256,
        "feature_defaults_sha256": FEATURE_DEFAULTS_SHA256,
    }


@app.post("/predict")
def predict(lead: Lead) -> dict[str, Any]:
    record = normalize_record(lead.model_dump())
    probability = float(pipeline.predict_proba([record])[0, 1])
    return {
        "conversion_probability": round(probability, 6),
        "conversion": probability >= 0.5,
    }
