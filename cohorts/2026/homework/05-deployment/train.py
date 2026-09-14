from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pickle
from pathlib import Path
from typing import Any

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

from model import FEATURES, NUMERICAL_FEATURES, normalize_record


DEFAULT_DATA = Path(__file__).resolve().parents[2] / "data" / "course_lead_scoring_2026.csv"
DEFAULT_MODEL = Path(__file__).resolve().parent / "pipeline.bin"


def read_training_rows(
    path: Path,
) -> tuple[list[dict[str, Any]], list[int], dict[str, float]]:
    raw_rows: list[dict[str, str]] = []
    targets: list[int] = []

    with path.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            raw_rows.append(row)
            targets.append(int(row["converted"]))

    defaults = {}
    for feature in NUMERICAL_FEATURES:
        values = sorted(
            float(row[feature])
            for row in raw_rows
            if row[feature] != ""
        )
        middle = len(values) // 2
        if len(values) % 2:
            defaults[feature] = values[middle]
        else:
            defaults[feature] = (values[middle - 1] + values[middle]) / 2

    records = [normalize_record(row, defaults) for row in raw_rows]
    return records, targets, defaults


def build_pipeline():
    return make_pipeline(
        DictVectorizer(),
        LogisticRegression(
            solver="liblinear",
            C=1.0,
            max_iter=1000,
            random_state=42,
        ),
    )


def train(data_path: Path, model_path: Path) -> None:
    records, targets, defaults = read_training_rows(data_path)
    pipeline = build_pipeline()
    pipeline.fit(records, targets)

    with model_path.open("wb") as model_file:
        pickle.dump(pipeline, model_file, protocol=pickle.HIGHEST_PROTOCOL)

    model_hash = hashlib.sha256(model_path.read_bytes()).hexdigest()
    data_hash = hashlib.sha256(data_path.read_bytes()).hexdigest()
    defaults_path = model_path.with_name("feature_defaults.json")
    defaults_path.write_text(json.dumps(defaults, indent=2) + "\n", encoding="utf-8")
    defaults_hash = hashlib.sha256(defaults_path.read_bytes()).hexdigest()
    metadata = {
        "dataset": data_path.name,
        "dataset_sha256": data_hash,
        "rows": len(records),
        "features": list(FEATURES),
        "target": "converted",
        "model": "DictVectorizer + LogisticRegression(solver=liblinear, C=1.0)",
        "random_state": 42,
        "scikit_learn": "1.7.2",
        "numeric_imputation": "training-set median",
        "numeric_defaults": defaults,
        "model_sha256": model_hash,
        "feature_defaults_sha256": defaults_hash,
    }
    metadata_path = model_path.with_name("model_metadata.json")
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train the ML Zoomcamp 2026 lead model")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    args = parser.parse_args()
    train(args.data, args.model)
