from __future__ import annotations

import pickle
from pathlib import Path

from model import normalize_record


MODEL_PATH = Path(__file__).with_name("pipeline.bin")
CLIENT = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74,
}

with MODEL_PATH.open("rb") as model_file:
    pipeline = pickle.load(model_file)

record = normalize_record(CLIENT)
first = float(pipeline.predict_proba([record])[0, 1])
second = float(pipeline.predict_proba([record])[0, 1])

assert 0 < first < 1
assert first == second
print({"conversion_probability": round(first, 6), "conversion": first >= 0.5})
