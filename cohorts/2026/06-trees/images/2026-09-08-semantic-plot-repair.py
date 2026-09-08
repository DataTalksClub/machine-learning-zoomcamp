"""Render the exact plot assets repaired on 2026-09-08.

The chart inputs follow the lesson notebook and the printed lesson values.  The
script intentionally renders native charts instead of using a screenshot or an
enlarged derivative as an image-generation input.

Run with the lesson's original dependencies, for example:

    uv run --python 3.11 --with numpy --with pandas \
      --with scikit-learn --with matplotlib --with seaborn --with xgboost \
      python 2026-09-08-semantic-plot-repair.py
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlopen

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score


OUT = Path(__file__).parent
DATA_URL = (
    "https://raw.githubusercontent.com/alexeygrigorev/"
    "mlbookcamp-code/master/chapter-06-trees/CreditScoring.csv"
)


def load_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Reproduce the notebook's cleaning, split, and one-hot encoding."""

    with urlopen(DATA_URL) as response:
        data = response.read()

    source = pd.read_csv(pd.io.common.BytesIO(data))
    source.columns = source.columns.str.lower()

    source.status = source.status.map({1: "ok", 2: "default", 0: "unk"})
    source.home = source.home.map(
        {1: "rent", 2: "owner", 3: "private", 4: "ignore", 5: "parents", 6: "other", 0: "unk"}
    )
    source.marital = source.marital.map(
        {1: "single", 2: "married", 3: "widow", 4: "separated", 5: "divorced", 0: "unk"}
    )
    source.records = source.records.map({1: "no", 2: "yes", 0: "unk"})
    source.job = source.job.map({1: "fixed", 2: "partime", 3: "freelance", 4: "others", 0: "unk"})

    for column in ["income", "assets", "debt"]:
        source[column] = source[column].replace(99999999, np.nan)

    source = source[source.status != "unk"].reset_index(drop=True)
    full_train, test = train_test_split(source, test_size=0.2, random_state=11)
    train, validation = train_test_split(full_train, test_size=0.25, random_state=11)

    train = train.reset_index(drop=True)
    validation = validation.reset_index(drop=True)
    test = test.reset_index(drop=True)

    y_train = (train.status == "default").astype("int").values
    y_validation = (validation.status == "default").astype("int").values

    train = train.drop(columns=["status"])
    validation = validation.drop(columns=["status"])
    test = test.drop(columns=["status"])

    vectorizer = DictVectorizer(sparse=False)
    x_train = vectorizer.fit_transform(train.fillna(0).to_dict(orient="records"))
    x_validation = vectorizer.transform(validation.fillna(0).to_dict(orient="records"))
    return x_train, y_train, x_validation, y_validation


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(OUT / filename, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def render_heatmaps() -> None:
    leaves = [1, 5, 10, 15, 20, 100, 200, 500]
    depths = [4, 5, 6]
    values = [
        [0.761, 0.767, 0.759],
        [0.761, 0.768, 0.759],
        [0.761, 0.762, 0.778],
        [0.764, 0.772, 0.785],
        [0.761, 0.774, 0.774],
        [0.756, 0.763, 0.776],
        [0.747, 0.759, 0.768],
        [0.680, 0.680, 0.680],
    ]
    table = pd.DataFrame(values, index=leaves, columns=depths)
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(table, annot=True, fmt=".3f", cmap="magma", ax=ax, cbar_kws={"label": "Validation AUC"})
    ax.set_title("Decision-tree validation AUC")
    ax.set_xlabel("max_depth")
    ax.set_ylabel("min_samples_leaf")
    save(fig, "05-decision-tree-tuning-05-heatmap-imagegen.png")

    wider_depths = ["None", "4", "5", "6", "7", "10", "15", "20"]
    wider_values = [
        [0.663, 0.761, 0.767, 0.749, 0.753, 0.693, 0.666, 0.654],
        [0.690, 0.761, 0.766, 0.755, 0.757, 0.720, 0.667, 0.666],
        [0.715, 0.761, 0.768, 0.762, 0.758, 0.727, 0.710, 0.720],
        [0.758, 0.761, 0.762, 0.778, 0.764, 0.766, 0.762, 0.764],
        [0.788, 0.764, 0.772, 0.785, 0.780, 0.790, 0.785, 0.788],
        [0.782, 0.761, 0.774, 0.774, 0.780, 0.786, 0.784, 0.783],
        [0.779, 0.756, 0.763, 0.776, 0.780, 0.779, 0.779, 0.780],
        [0.680, 0.680, 0.680, 0.680, 0.680, 0.680, 0.680, 0.680],
    ]
    wider_table = pd.DataFrame(wider_values, index=leaves, columns=wider_depths)
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.heatmap(
        wider_table,
        annot=True,
        fmt=".3f",
        cmap="magma",
        ax=ax,
        cbar_kws={"label": "Validation AUC"},
    )
    ax.set_title("Wider decision-tree parameter search")
    ax.set_xlabel("max_depth (None = unlimited)")
    ax.set_ylabel("min_samples_leaf")
    save(fig, "05-decision-tree-tuning-07-wider-search-imagegen.png")


def render_random_forest(x_train: np.ndarray, y_train: np.ndarray, x_validation: np.ndarray, y_validation: np.ndarray) -> None:
    estimator_counts = list(range(10, 201, 10))

    scores = []
    for n in estimator_counts:
        model = RandomForestClassifier(n_estimators=n, random_state=1)
        model.fit(x_train, y_train)
        score = roc_auc_score(y_validation, model.predict_proba(x_validation)[:, 1])
        scores.append(score)
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.plot(estimator_counts, scores)
    ax.set_title("Validation AUC versus number of trees")
    ax.set_xlabel("Number of trees (n_estimators)")
    ax.set_ylabel("Validation AUC")
    save(fig, "06-random-forest-03-auc-vs-trees-imagegen.png")

    scores_by_depth: dict[int, list[float]] = {}
    for depth in [5, 10, 15]:
        scores_by_depth[depth] = []
        for n in estimator_counts:
            model = RandomForestClassifier(n_estimators=n, max_depth=depth, random_state=1)
            model.fit(x_train, y_train)
            scores_by_depth[depth].append(
                roc_auc_score(y_validation, model.predict_proba(x_validation)[:, 1])
            )
    fig, ax = plt.subplots(figsize=(9, 7))
    for depth, scores in scores_by_depth.items():
        ax.plot(estimator_counts, scores, label=f"max_depth={depth}")
    ax.set_title("Random-forest validation AUC by max_depth")
    ax.set_xlabel("Number of trees (n_estimators)")
    ax.set_ylabel("Validation AUC")
    ax.legend(title="Parameter")
    save(fig, "06-random-forest-04-tuning-max-depth-imagegen.png")

    scores_by_leaf: dict[int, list[float]] = {}
    for leaf_size in [1, 3, 5, 10, 50]:
        scores_by_leaf[leaf_size] = []
        for n in estimator_counts:
            model = RandomForestClassifier(
                n_estimators=n,
                max_depth=10,
                min_samples_leaf=leaf_size,
                random_state=1,
            )
            model.fit(x_train, y_train)
            scores_by_leaf[leaf_size].append(
                roc_auc_score(y_validation, model.predict_proba(x_validation)[:, 1])
            )
    fig, ax = plt.subplots(figsize=(9, 7))
    colors = ["black", "blue", "orange", "red", "grey"]
    for leaf_size, color in zip(scores_by_leaf, colors):
        ax.plot(
            estimator_counts,
            scores_by_leaf[leaf_size],
            color=color,
            label=f"min_samples_leaf={leaf_size}",
        )
    ax.set_title("Random-forest validation AUC by leaf size")
    ax.set_xlabel("Number of trees (n_estimators)")
    ax.set_ylabel("Validation AUC")
    ax.legend(title="Parameter")
    save(fig, "06-random-forest-05-tuning-min-samples-leaf-imagegen.png")


def xgb_scores(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_validation: np.ndarray,
    y_validation: np.ndarray,
    *,
    eta: float,
    max_depth: int,
    min_child_weight: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    train_matrix = xgb.DMatrix(x_train, label=y_train)
    validation_matrix = xgb.DMatrix(x_validation, label=y_validation)
    evaluation: dict[str, dict[str, list[float]]] = {}
    params = {
        "eta": eta,
        "max_depth": max_depth,
        "min_child_weight": min_child_weight,
        "objective": "binary:logistic",
        "eval_metric": "auc",
        # One thread keeps the render reproducible and avoids OpenMP contention
        # when the full set of comparison curves is generated.
        "nthread": 1,
        "seed": 1,
        "verbosity": 0,
    }
    xgb.train(
        params,
        train_matrix,
        num_boost_round=200,
        evals=[(train_matrix, "train"), (validation_matrix, "val")],
        evals_result=evaluation,
        verbose_eval=False,
    )
    # XGBoost's verbose-eval output includes the closing round 200.  The
    # in-memory evaluation arrays are zero-based and end at index 199.
    iterations = np.arange(0, 201, 5)
    indexes = np.minimum(iterations, 199)
    return iterations, np.asarray(evaluation["train"]["auc"])[indexes], np.asarray(evaluation["val"]["auc"])[indexes]


def render_boosting_and_xgb(x_train: np.ndarray, y_train: np.ndarray, x_validation: np.ndarray, y_validation: np.ndarray) -> None:
    iterations, train_auc, val_auc = xgb_scores(
        x_train, y_train, x_validation, y_validation, eta=0.3, max_depth=6, min_child_weight=1
    )
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.plot(iterations, train_auc, label="train")
    ax.plot(iterations, val_auc, label="val")
    ax.set_title("Training and validation AUC during boosting")
    ax.set_xlabel("Boosting rounds")
    ax.set_ylabel("AUC")
    ax.legend()
    save(fig, "07-boosting-03-train-val-auc-imagegen.png")

    eta_values = [0.3, 1.0, 0.1, 0.05, 0.01]
    fig, ax = plt.subplots(figsize=(9, 7))
    for eta in eta_values:
        iterations, _, val_auc = xgb_scores(
            x_train, y_train, x_validation, y_validation, eta=eta, max_depth=6, min_child_weight=1
        )
        ax.plot(iterations, val_auc, label=f"eta={eta}")
    ax.set_title("XGBoost validation AUC by learning rate")
    ax.set_xlabel("Boosting rounds")
    ax.set_ylabel("Validation AUC")
    ax.set_ylim(0.8, 0.84)
    ax.legend(title="Parameter")
    save(fig, "08-xgb-tuning-02-tuning-eta-imagegen.png")

    fig, ax = plt.subplots(figsize=(9, 7))
    for depth in [6, 3, 4]:
        iterations, _, val_auc = xgb_scores(
            x_train, y_train, x_validation, y_validation, eta=0.1, max_depth=depth, min_child_weight=1
        )
        ax.plot(iterations, val_auc, label=f"max_depth={depth}")
    ax.set_title("XGBoost validation AUC by max_depth")
    ax.set_xlabel("Boosting rounds")
    ax.set_ylabel("Validation AUC")
    ax.set_ylim(0.8, 0.84)
    ax.legend(title="Parameter")
    save(fig, "08-xgb-tuning-03-max-depth-curves-imagegen.png")

    fig, ax = plt.subplots(figsize=(9, 7))
    for child_weight in [1, 10, 30]:
        iterations, _, val_auc = xgb_scores(
            x_train,
            y_train,
            x_validation,
            y_validation,
            eta=0.1,
            max_depth=3,
            min_child_weight=child_weight,
        )
        ax.plot(iterations, val_auc, label=f"min_child_weight={child_weight}")
    ax.set_title("XGBoost validation AUC by min_child_weight")
    ax.set_xlabel("Boosting rounds")
    ax.set_ylabel("Validation AUC")
    ax.set_ylim(0.82, 0.84)
    ax.legend(title="Parameter")
    save(fig, "08-xgb-tuning-04-min-child-weight-curves-imagegen.png")


def render_summary() -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    labels = ["train", "validation"]
    values = [1.0, 0.6548400377860302]
    bars = ax.bar(labels, values, color=["#2f6db0", "#d65b53"], width=0.6)
    ax.set_title("Overfitting in an unrestricted decision tree")
    ax.set_xlabel("Data split")
    ax.set_ylabel("AUC")
    ax.set_ylim(0, 1.1)
    labels = ["1.0", "0.6548400377860302"]
    for bar, value, label in zip(bars, values, labels):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.03, label, ha="center", weight="bold")
    save(fig, "10-summary-03-overfitting-auc-imagegen.png")


def main() -> None:
    render_heatmaps()
    x_train, y_train, x_validation, y_validation = load_data()
    render_random_forest(x_train, y_train, x_validation, y_validation)
    render_boosting_and_xgb(x_train, y_train, x_validation, y_validation)
    render_summary()


if __name__ == "__main__":
    main()
