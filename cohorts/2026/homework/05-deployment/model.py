from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CATEGORICAL_FEATURES = (
    "lead_source",
    "industry",
    "employment_status",
    "location",
)
NUMERICAL_FEATURES = (
    "number_of_courses_viewed",
    "annual_income",
    "interaction_count",
    "lead_score",
)
FEATURES = CATEGORICAL_FEATURES + NUMERICAL_FEATURES
DEFAULTS_PATH = Path(__file__).with_name("feature_defaults.json")


def load_feature_defaults(path: Path = DEFAULTS_PATH) -> dict[str, float]:
    if not path.exists():
        return {feature: 0.0 for feature in NUMERICAL_FEATURES}
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_record(
    raw: dict[str, Any], numeric_defaults: dict[str, float] | None = None
) -> dict[str, Any]:
    """Apply the training-time missing-value policy to one lead."""

    if numeric_defaults is None:
        numeric_defaults = load_feature_defaults()

    record: dict[str, Any] = {}
    for feature in CATEGORICAL_FEATURES:
        value = raw.get(feature)
        record[feature] = value or "NA"

    for feature in NUMERICAL_FEATURES:
        value = raw.get(feature)
        if value is None or value == "":
            record[feature] = numeric_defaults[feature]
        elif feature == "number_of_courses_viewed" or feature == "interaction_count":
            record[feature] = int(value)
        else:
            record[feature] = float(value)

    return record
