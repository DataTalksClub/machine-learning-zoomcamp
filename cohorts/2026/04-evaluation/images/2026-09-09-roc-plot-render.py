#!/usr/bin/env python3
"""Render the three evaluation ROC plots from the lesson's source data.

The lesson notebook was executed with the historical scikit-learn stack.  The
explicit versions in the provenance record are intentional: newer solvers can
produce a different validation curve even when the source CSV is unchanged.
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
from sklearn.metrics import roc_curve
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


def render(data_path: Path, output_dir: Path) -> None:
    y_val, y_pred = prepare_predictions(data_path)
    scores = threshold_frame(y_val, y_pred)

    num_neg = int((y_val == 0).sum())
    num_pos = int((y_val == 1).sum())
    y_ideal = np.repeat([0, 1], [num_neg, num_pos])
    y_ideal_pred = np.linspace(0, 1, len(y_val))
    ideal = threshold_frame(y_ideal, y_ideal_pred)

    figure, axes = plt.subplots(figsize=(8, 5.3333333333))
    axes.plot(scores.threshold, scores.tpr, label="TPR", color="black")
    axes.plot(scores.threshold, scores.fpr, label="FPR", color="blue")
    axes.plot(ideal.threshold, ideal.tpr, label="TPR ideal")
    axes.plot(ideal.threshold, ideal.fpr, label="FPR ideal")
    axes.legend()
    save_figure(
        figure,
        output_dir / "05-roc-04-model-vs-ideal-tpr-fpr-crisp.png",
    )

    figure, axes = plt.subplots(figsize=(6.5, 6.5))
    axes.plot(scores.fpr, scores.tpr, label="Model")
    axes.plot([0, 1], [0, 1], label="Random", linestyle="--")
    axes.set_xlabel("FPR")
    axes.set_ylabel("TPR")
    axes.legend()
    save_figure(
        figure,
        output_dir / "05-roc-05-roc-curve-manual-crisp.png",
    )

    fpr, tpr, _ = roc_curve(y_val, y_pred)
    figure, axes = plt.subplots(figsize=(6.5, 6.5))
    axes.plot(fpr, tpr, label="Model")
    axes.plot([0, 1], [0, 1], label="Random", linestyle="--")
    axes.set_xlabel("FPR")
    axes.set_ylabel("TPR")
    axes.legend()
    save_figure(
        figure,
        output_dir / "05-roc-06-roc-curve-sklearn-crisp.png",
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
