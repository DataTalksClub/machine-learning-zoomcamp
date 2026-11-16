"""FastAPI web service that serves the dropout model.

Run locally:  uvicorn predict:app --host 0.0.0.0 --port 9696
"""

import logging
import os
import pickle
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

from features import RAW_FEATURES, to_records

MODEL_PATH = Path(os.getenv("MODEL_PATH", Path(__file__).parent / "model.bin"))
HIGH_RISK_MARGIN = 0.2  # probability >= threshold + margin is labelled "high"

logger = logging.getLogger("dropout-service")
logging.basicConfig(level=logging.INFO)


class Student(BaseModel):
    """One student's data at the end of their first year.

    Categorical fields use the integer codes from the UCI dataset documentation.
    """

    model_config = ConfigDict(extra="forbid")

    marital_status: int = Field(ge=1, le=6)
    application_mode: int = Field(ge=1, le=57)
    application_order: int = Field(ge=0, le=9)
    course: int = Field(ge=1, le=9999)
    daytime_attendance: int = Field(ge=0, le=1, description="1 = daytime, 0 = evening")
    previous_qualification: int = Field(ge=1, le=43)
    previous_qualification_grade: float = Field(ge=0, le=200)
    nationality: int = Field(ge=1, le=109)
    mothers_qualification: int = Field(ge=1, le=44)
    fathers_qualification: int = Field(ge=1, le=44)
    mothers_occupation: int = Field(ge=0, le=194)
    fathers_occupation: int = Field(ge=0, le=195)
    admission_grade: float = Field(ge=0, le=200)
    displaced: int = Field(ge=0, le=1)
    special_needs: int = Field(ge=0, le=1)
    debtor: int = Field(ge=0, le=1)
    tuition_up_to_date: int = Field(ge=0, le=1)
    gender: int = Field(ge=0, le=1, description="1 = male, 0 = female")
    scholarship_holder: int = Field(ge=0, le=1)
    age_at_enrollment: int = Field(ge=15, le=100)
    international: int = Field(ge=0, le=1)
    sem1_credited: int = Field(ge=0, le=60)
    sem1_enrolled: int = Field(ge=0, le=60)
    sem1_evaluations: int = Field(ge=0, le=100)
    sem1_approved: int = Field(ge=0, le=60)
    sem1_grade: float = Field(ge=0, le=20)
    sem1_without_evaluations: int = Field(ge=0, le=60)
    sem2_credited: int = Field(ge=0, le=60)
    sem2_enrolled: int = Field(ge=0, le=60)
    sem2_evaluations: int = Field(ge=0, le=100)
    sem2_approved: int = Field(ge=0, le=60)
    sem2_grade: float = Field(ge=0, le=20)
    sem2_without_evaluations: int = Field(ge=0, le=60)
    unemployment_rate: float = Field(ge=0, le=100)
    inflation_rate: float = Field(ge=-50, le=100)
    gdp: float = Field(ge=-50, le=50)


class Prediction(BaseModel):
    dropout_probability: float
    dropout_risk: bool
    risk_level: Literal["low", "medium", "high"]
    threshold: float


def load_artifact(path: Path) -> dict:
    """Load the pickled {'model', 'threshold', ...} artifact written by train.py."""
    if not path.exists():
        raise FileNotFoundError(f"Model file not found at {path}. Run `python train.py` first.")
    with path.open("rb") as f:
        artifact = pickle.load(f)  # trusted file produced by our own train.py
    if "model" not in artifact or "threshold" not in artifact:
        raise ValueError(f"{path} is not a valid model artifact")
    return artifact


def risk_level(probability: float, threshold: float) -> str:
    if probability >= threshold + HIGH_RISK_MARGIN:
        return "high"
    if probability >= threshold:
        return "medium"
    return "low"


def score(student: Student, artifact: dict) -> Prediction:
    frame = pd.DataFrame([student.model_dump()])[RAW_FEATURES]
    probability = float(artifact["model"].predict_proba(to_records(frame))[0, 1])
    threshold = float(artifact["threshold"])
    return Prediction(
        dropout_probability=round(probability, 4),
        dropout_risk=probability >= threshold,
        risk_level=risk_level(probability, threshold),
        threshold=round(threshold, 4),
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.artifact = load_artifact(MODEL_PATH)
    logger.info("Loaded model from %s", MODEL_PATH)
    yield


app = FastAPI(
    title="Student Dropout Risk API",
    description="Predicts the probability that a student drops out, from their first-year data.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict", response_model=Prediction)
def predict(student: Student) -> Prediction:
    try:
        return score(student, app.state.artifact)
    except Exception as exc:  # pragma: no cover - defensive, logged for debugging
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail="Prediction failed") from exc
