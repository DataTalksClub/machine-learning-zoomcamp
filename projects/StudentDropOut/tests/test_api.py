import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import predict

EXAMPLES = Path(__file__).parent.parent / "examples"


@pytest.fixture(scope="module")
def client():
    if not predict.MODEL_PATH.exists():
        pytest.skip("model.bin not found - run `python train.py` first")
    with TestClient(predict.app) as test_client:
        yield test_client


def load_example(name: str) -> dict:
    return json.loads((EXAMPLES / name).read_text())


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_at_risk_student_is_flagged(client):
    body = client.post("/predict", json=load_example("student_at_risk.json")).json()
    assert body["dropout_risk"] is True
    assert body["dropout_probability"] > body["threshold"]


def test_on_track_student_is_not_flagged(client):
    body = client.post("/predict", json=load_example("student_on_track.json")).json()
    assert body["dropout_risk"] is False
    assert body["risk_level"] == "low"


def test_rejects_out_of_range_values(client):
    student = {**load_example("student_on_track.json"), "sem1_grade": 35}
    assert client.post("/predict", json=student).status_code == 422


def test_rejects_missing_and_unknown_fields(client):
    student = load_example("student_on_track.json")
    missing = {k: v for k, v in student.items() if k != "course"}
    assert client.post("/predict", json=missing).status_code == 422
    assert client.post("/predict", json={**student, "hacker": 1}).status_code == 422


@pytest.mark.parametrize("probability, expected", [(0.1, "low"), (0.45, "medium"), (0.9, "high")])
def test_risk_level_bands(probability, expected):
    assert predict.risk_level(probability, threshold=0.4) == expected
