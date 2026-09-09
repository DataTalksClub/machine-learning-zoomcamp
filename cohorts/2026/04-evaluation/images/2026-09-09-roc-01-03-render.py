#!/usr/bin/env python3
"""Render ROC lesson plots 01/02/03 from the exact notebook data path.

This renderer deliberately writes only the three threshold plots owned by the
current repair task. ROC 04/05/06 have a separate renderer and are not touched.
"""

from __future__ import annotations

import argparse
import hashlib
import tempfile
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


DATA_URL = (
    "https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/"
    "master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)
DATA_SHA256 = "88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a"

NUMERICAL = ["tenure", "monthlycharges", "totalcharges"]
CATEGORICAL = [
    "gender",
    "seniorcitizen",
    "partner",
    "dependents",
    "phoneservice",
    "multiplelines",
    "internetservice",
    "onlinesecurity",
    "onlinebackup",
    "deviceprotection",
    "techsupport",
    "streamingtv",
    "streamingmovies",
    "contract",
    "paperlessbilling",
    "paymentmethod",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def prepare_predictions(data_path: Path) -> tuple[np.ndarray, np.ndarray]:
    if sha256(data_path) != DATA_SHA256:
        raise ValueError(
            f"unexpected source hash for {data_path}; expected {DATA_SHA256}"
        )

    df = pd.read_csv(data_path)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    categorical_columns = list(df.dtypes[df.dtypes == "object"].index)
    for column in categorical_columns:
        df[column] = df[column].str.lower().str.replace(" ", "_")

    df.totalcharges = pd.to_numeric(df.totalcharges, errors="coerce")
    df.totalcharges = df.totalcharges.fillna(0)
    df.churn = (df.churn == "yes").astype(int)

    df_full_train, _ = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(
        df_full_train, test_size=0.25, random_state=1
    )
    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)

    y_train = df_train.pop("churn").values
    y_val = df_val.pop("churn").values

    vectorizer = DictVectorizer(sparse=False)
    train_dict = df_train[CATEGORICAL + NUMERICAL].to_dict(orient="records")
    val_dict = df_val[CATEGORICAL + NUMERICAL].to_dict(orient="records")
    x_train = vectorizer.fit_transform(train_dict)
    x_val = vectorizer.transform(val_dict)

    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict_proba(x_val)[:, 1]
    return y_val, y_pred


def threshold_frame(y_val: np.ndarray, y_pred: np.ndarray) -> pd.DataFrame:
    rows = []
    for threshold in np.linspace(0, 1, 101):
        actual_positive = y_val == 1
        actual_negative = y_val == 0
        predict_positive = y_pred >= threshold
        predict_negative = y_pred < threshold
        tp = int((predict_positive & actual_positive).sum())
        tn = int((predict_negative & actual_negative).sum())
        fp = int((predict_positive & actual_negative).sum())
        fn = int((predict_negative & actual_positive).sum())
        rows.append(
            {
                "threshold": threshold,
                "tpr": tp / (tp + fn),
                "fpr": fp / (fp + tn),
            }
        )
    return pd.DataFrame(rows)


def save_figure(figure: plt.Figure, path: Path) -> None:
    figure.savefig(
        path,
        dpi=220,
        facecolor="white",
        bbox_inches="tight",
        pad_inches=0.08,
    )
    plt.close(figure)


def render_plot(scores: pd.DataFrame, path: Path) -> None:
    figure, axes = plt.subplots(figsize=(8, 5.3333333333))
    axes.plot(scores.threshold, scores.tpr, label="TPR")
    axes.plot(scores.threshold, scores.fpr, label="FPR")
    axes.set_xlabel("Threshold")
    axes.set_ylabel("Rate")
    axes.legend()
    save_figure(figure, path)


def render(data_path: Path, output_dir: Path) -> None:
    y_val, y_pred = prepare_predictions(data_path)

    # These assertions are lesson facts and protect against silently using a
    # different dataset, split, or model runtime.
    assert len(y_val) == 1409
    assert int((y_val == 0).sum()) == 1023
    assert int((y_val == 1).sum()) == 386
    model_at_half = threshold_frame(y_val, y_pred)
    half = model_at_half.iloc[50]
    assert tuple(
        int(value)
        for value in (
            ((y_pred >= 0.5) & (y_val == 1)).sum(),
            ((y_pred >= 0.5) & (y_val == 0)).sum(),
            ((y_pred < 0.5) & (y_val == 1)).sum(),
            ((y_pred < 0.5) & (y_val == 0)).sum(),
        )
    ) == (210, 101, 176, 922)
    assert round(float(half.tpr), 12) == round(210 / 386, 12)
    assert round(float(half.fpr), 12) == round(101 / 1023, 12)

    np.random.seed(1)
    y_rand = np.random.uniform(0, 1, size=len(y_val))
    random_scores = threshold_frame(y_val, y_rand)

    num_neg = int((y_val == 0).sum())
    num_pos = int((y_val == 1).sum())
    y_ideal = np.repeat([0, 1], [num_neg, num_pos])
    y_ideal_pred = np.linspace(0, 1, len(y_val))
    ideal_scores = threshold_frame(y_ideal, y_ideal_pred)

    render_plot(
        model_at_half,
        output_dir / "05-roc-01-tpr-fpr-vs-threshold-crisp.png",
    )
    render_plot(
        random_scores,
        output_dir / "05-roc-02-random-model-tpr-fpr-crisp.png",
    )
    render_plot(
        ideal_scores,
        output_dir / "05-roc-03-ideal-model-tpr-fpr-crisp.png",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-path", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.data_path:
        render(args.data_path, args.output_dir)
        return

    with tempfile.TemporaryDirectory() as directory:
        data_path = Path(directory) / "data-week-3.csv"
        urllib.request.urlretrieve(DATA_URL, data_path)
        render(data_path, args.output_dir)


if __name__ == "__main__":
    main()
