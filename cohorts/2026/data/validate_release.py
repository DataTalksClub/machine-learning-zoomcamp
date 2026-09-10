"""Release-level checks for the ML Zoomcamp 2026 generated datasets."""

import json
from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent


def check_report(name: str) -> None:
    report = json.loads((DATA_DIR / f"{name}_report.json").read_text())
    violations = report["data_quality"]["bound_violations"]
    assert violations and all(value == 0 for value in violations.values()), violations


def main() -> None:
    car = pd.read_csv(DATA_DIR / "car_fuel_efficiency_2026.csv")
    lead = pd.read_csv(DATA_DIR / "course_lead_scoring_2026.csv")

    assert car.shape == (10_000, 11), car.shape
    assert lead.shape == (5_000, 9), lead.shape
    assert car.fuel_efficiency_mpg.notna().all()
    assert lead.converted.notna().all()

    # The car release has structured, non-trivial relationships and realistic
    # missingness rather than independent columns.
    assert car.horsepower.isna().mean() > 0.05
    assert car.acceleration.isna().mean() > 0.01
    numeric = car.select_dtypes("number")
    assert numeric.corr().loc["vehicle_weight", "fuel_efficiency_mpg"] < -0.3
    assert numeric.corr().loc["model_year", "fuel_efficiency_mpg"] > 0.1
    assert numeric.corr().loc["engine_displacement", "vehicle_weight"] > 0.60
    assert car.fuel_efficiency_mpg.between(10, 45).all()

    # The lead release has a funnel-shaped feature graph and probabilistic
    # labels. The strongest offered pair is deliberate and measurable.
    assert 0.45 < lead.converted.mean() < 0.70
    lead_numeric = lead.select_dtypes("number")
    assert lead_numeric.corr().loc["interaction_count", "lead_score"] > 0.85
    assert lead_numeric.corr().loc["interaction_count", "lead_score"] > lead_numeric.corr().loc[
        "number_of_courses_viewed", "lead_score"
    ]
    assert lead.annual_income.isna().mean() > 0.05
    student_income_missing = lead.loc[
        lead.employment_status == "student", "annual_income"
    ].isna().mean()
    employed_income_missing = lead.loc[
        lead.employment_status == "employed", "annual_income"
    ].isna().mean()
    assert student_income_missing > employed_income_missing + 0.20

    check_report("car_fuel_efficiency_2026")
    check_report("course_lead_scoring_2026")
    print("ML Zoomcamp 2026 data release: OK")


if __name__ == "__main__":
    main()
