"""Shared data loading and feature engineering.

The same functions are used by the notebook, train.py and predict.py so the
model always sees features prepared in exactly the same way.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "data.csv"
TARGET = "dropout"

# Original UCI column names -> clean snake_case names.
# The raw file has a stray tab in one header and a typo ("Nacionality").
COLUMN_MAP = {
    "Marital status": "marital_status",
    "Application mode": "application_mode",
    "Application order": "application_order",
    "Course": "course",
    "Daytime/evening attendance\t": "daytime_attendance",
    "Previous qualification": "previous_qualification",
    "Previous qualification (grade)": "previous_qualification_grade",
    "Nacionality": "nationality",
    "Mother's qualification": "mothers_qualification",
    "Father's qualification": "fathers_qualification",
    "Mother's occupation": "mothers_occupation",
    "Father's occupation": "fathers_occupation",
    "Admission grade": "admission_grade",
    "Displaced": "displaced",
    "Educational special needs": "special_needs",
    "Debtor": "debtor",
    "Tuition fees up to date": "tuition_up_to_date",
    "Gender": "gender",
    "Scholarship holder": "scholarship_holder",
    "Age at enrollment": "age_at_enrollment",
    "International": "international",
    "Curricular units 1st sem (credited)": "sem1_credited",
    "Curricular units 1st sem (enrolled)": "sem1_enrolled",
    "Curricular units 1st sem (evaluations)": "sem1_evaluations",
    "Curricular units 1st sem (approved)": "sem1_approved",
    "Curricular units 1st sem (grade)": "sem1_grade",
    "Curricular units 1st sem (without evaluations)": "sem1_without_evaluations",
    "Curricular units 2nd sem (credited)": "sem2_credited",
    "Curricular units 2nd sem (enrolled)": "sem2_enrolled",
    "Curricular units 2nd sem (evaluations)": "sem2_evaluations",
    "Curricular units 2nd sem (approved)": "sem2_approved",
    "Curricular units 2nd sem (grade)": "sem2_grade",
    "Curricular units 2nd sem (without evaluations)": "sem2_without_evaluations",
    "Unemployment rate": "unemployment_rate",
    "Inflation rate": "inflation_rate",
    "GDP": "gdp",
    "Target": "target",
}

# Integer codes that stand for categories (course id, nationality id, ...).
# They have no numeric order, so they are one-hot encoded.
CATEGORICAL = [
    "marital_status",
    "application_mode",
    "course",
    "previous_qualification",
    "nationality",
    "mothers_qualification",
    "fathers_qualification",
    "mothers_occupation",
    "fathers_occupation",
]

NUMERICAL = [
    "application_order",
    "daytime_attendance",
    "previous_qualification_grade",
    "admission_grade",
    "displaced",
    "special_needs",
    "debtor",
    "tuition_up_to_date",
    "gender",
    "scholarship_holder",
    "age_at_enrollment",
    "international",
    "sem1_credited",
    "sem1_enrolled",
    "sem1_evaluations",
    "sem1_approved",
    "sem1_grade",
    "sem1_without_evaluations",
    "sem2_credited",
    "sem2_enrolled",
    "sem2_evaluations",
    "sem2_approved",
    "sem2_grade",
    "sem2_without_evaluations",
    "unemployment_rate",
    "inflation_rate",
    "gdp",
]

ENGINEERED = ["sem1_approval_rate", "sem2_approval_rate", "grade_change"]

RAW_FEATURES = CATEGORICAL + NUMERICAL
MODEL_FEATURES = CATEGORICAL + NUMERICAL + ENGINEERED


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Read the raw UCI file, rename columns and add the binary target."""
    raw = pd.read_csv(path, sep=";", encoding="utf-8-sig")
    missing = set(COLUMN_MAP) - set(raw.columns)
    if missing:
        raise ValueError(f"Dataset is missing expected columns: {sorted(missing)}")

    df = raw.rename(columns=COLUMN_MAP)
    return df.assign(**{TARGET: (df["target"] == "Dropout").astype(int)})


def _safe_rate(approved: pd.Series, enrolled: pd.Series) -> pd.Series:
    """approved / enrolled, with 0 when the student enrolled in nothing."""
    rate = approved / enrolled.where(enrolled > 0)
    return rate.fillna(0.0).clip(0.0, 1.0)


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of df with the three engineered features added."""
    return df.assign(
        sem1_approval_rate=_safe_rate(df["sem1_approved"], df["sem1_enrolled"]),
        sem2_approval_rate=_safe_rate(df["sem2_approved"], df["sem2_enrolled"]),
        grade_change=df["sem2_grade"] - df["sem1_grade"],
    )


def to_records(df: pd.DataFrame) -> list[dict]:
    """Turn a frame of raw features into DictVectorizer-ready records.

    Categorical codes become strings so DictVectorizer one-hot encodes them.
    """
    prepared = add_engineered_features(df[RAW_FEATURES])
    prepared = prepared.assign(**{c: prepared[c].astype(str) for c in CATEGORICAL})
    return prepared[MODEL_FEATURES].to_dict(orient="records")
