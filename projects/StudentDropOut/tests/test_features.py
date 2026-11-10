import pandas as pd
import pytest

from features import CATEGORICAL, MODEL_FEATURES, RAW_FEATURES, add_engineered_features, load_data, to_records


@pytest.fixture(scope="module")
def df() -> pd.DataFrame:
    return load_data()


def test_load_data_has_clean_columns_and_binary_target(df):
    assert df.shape == (4424, 38)
    assert set(RAW_FEATURES) <= set(df.columns)
    assert set(df["dropout"].unique()) == {0, 1}
    assert df["dropout"].sum() == (df["target"] == "Dropout").sum()


def test_approval_rate_handles_zero_enrolled_units():
    frame = pd.DataFrame({
        "sem1_approved": [0, 3], "sem1_enrolled": [0, 6],
        "sem2_approved": [2, 6], "sem2_enrolled": [4, 6],
        "sem1_grade": [0.0, 12.0], "sem2_grade": [10.0, 11.5],
    })

    result = add_engineered_features(frame)

    assert result["sem1_approval_rate"].tolist() == [0.0, 0.5]
    assert result["sem2_approval_rate"].tolist() == [0.5, 1.0]
    assert result["grade_change"].tolist() == [10.0, -0.5]
    assert "sem1_approval_rate" not in frame.columns  # input is not mutated


def test_to_records_turns_categorical_codes_into_strings(df):
    records = to_records(df.head(3))

    assert len(records) == 3
    assert list(records[0]) == MODEL_FEATURES
    assert all(isinstance(records[0][c], str) for c in CATEGORICAL)
    assert isinstance(records[0]["admission_grade"], float)
