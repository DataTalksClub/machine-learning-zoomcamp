"""Train the final dropout model and save it to model.bin.

Hyperparameters come from the tuning done in notebook.ipynb.
Usage:  python train.py [--output model.bin]
"""

import argparse
import logging
import os
import pickle
from pathlib import Path

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import f1_score, precision_recall_curve, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from xgboost import XGBClassifier

from features import MODEL_FEATURES, TARGET, load_data, to_records

SEED = 42
TEST_SIZE = 0.2
N_FOLDS = 5
N_JOBS = min(8, os.cpu_count() or 1)

# Best parameters from the grid search in notebook.ipynb (section 4.4)
XGB_PARAMS = {
    "n_estimators": 400,
    "learning_rate": 0.03,
    "max_depth": 4,
    "min_child_weight": 1,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
}

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("train")


def build_model() -> Pipeline:
    xgb = XGBClassifier(**XGB_PARAMS, eval_metric="auc", random_state=SEED, n_jobs=1)
    return make_pipeline(DictVectorizer(sparse=False), xgb)


def pick_threshold(model: Pipeline, X: list[dict], y: np.ndarray) -> float:
    """F1-optimal threshold from out-of-fold predictions (never touches the test set)."""
    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    oof = cross_val_predict(model, X, y, cv=cv, method="predict_proba", n_jobs=N_JOBS)[:, 1]
    precision, recall, thresholds = precision_recall_curve(y, oof)
    f1 = 2 * precision * recall / (precision + recall + 1e-12)
    return float(thresholds[int(np.argmax(f1[:-1]))])


def main(output: Path) -> None:
    df = load_data()
    df_train, df_test = train_test_split(df, test_size=TEST_SIZE, random_state=SEED, stratify=df[TARGET])
    X_train, y_train = to_records(df_train), df_train[TARGET].values
    X_test, y_test = to_records(df_test), df_test[TARGET].values
    log.info("train rows: %d | test rows: %d", len(X_train), len(X_test))

    threshold = pick_threshold(build_model(), X_train, y_train)
    model = build_model().fit(X_train, y_train)

    y_proba = model.predict_proba(X_test)[:, 1]
    test_auc = roc_auc_score(y_test, y_proba)
    test_f1 = f1_score(y_test, (y_proba >= threshold).astype(int))
    log.info("threshold: %.4f | test ROC AUC: %.4f | test F1: %.4f", threshold, test_auc, test_f1)

    # Final model is refit on all the data so the service uses every example we have
    final_model = build_model().fit(to_records(df), df[TARGET].values)
    artifact = {
        "model": final_model,
        "threshold": threshold,
        "features": MODEL_FEATURES,
        "metrics": {"test_roc_auc": round(test_auc, 4), "test_f1": round(test_f1, 4)},
        "params": XGB_PARAMS,
    }
    with output.open("wb") as f:
        pickle.dump(artifact, f)
    log.info("saved model to %s", output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "model.bin")
    main(parser.parse_args().output)
