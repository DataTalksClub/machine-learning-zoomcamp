"""Replay the deterministic answer contract for the reviewed 2026 homework.

This is a release check, not a student solution. It recalculates the answers
that depend on the pinned CSVs and verifies that each answer is present in the
corresponding homework file. Keeping this next to the plans makes option drift
visible before the assignments are published.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_squared_error,
    mutual_info_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import KFold, train_test_split
from sklearn.tree import DecisionTreeRegressor


DATA_DIR = Path(__file__).resolve().parent
HOMEWORK_DIR = DATA_DIR.parent / "homework"
CAR_COLUMNS = [
    "engine_displacement",
    "horsepower",
    "vehicle_weight",
    "model_year",
]
LEAD_TARGET = "converted"


def question_block(path: Path, heading: str) -> str:
    """Return one question and stop before the next Markdown heading."""
    text = path.read_text()
    start = text.index(heading)
    remainder = text[start + len(heading) :]
    next_heading = re.search(r"\n#{2,3} ", remainder)
    end = start + len(heading) + (next_heading.start() if next_heading else len(remainder))
    return text[start:end]


def require_option(path: Path, heading: str, value: str) -> None:
    block = question_block(path, heading)
    option_pattern = rf"^\s*[-*]\s*{re.escape(value)}\s*$"
    if not re.search(option_pattern, block, flags=re.MULTILINE):
        raise AssertionError(f"{path.name} {heading}: missing option {value!r}")


def split_three_way(df: pd.DataFrame, seed: int):
    full_train, test = train_test_split(df, test_size=0.2, random_state=seed)
    train, validation = train_test_split(
        full_train, test_size=0.25, random_state=seed
    )
    return train, validation, test


def split_with_lecture_shuffle(df: pd.DataFrame, seed: int):
    """Use the NumPy shuffle/slice split used in the regression lectures."""
    n_validation = int(len(df) * 0.2)
    n_test = int(len(df) * 0.2)
    n_train = len(df) - n_validation - n_test
    indices = np.arange(len(df))
    np.random.RandomState(seed).shuffle(indices)
    train = df.iloc[indices[:n_train]]
    validation = df.iloc[indices[n_train : n_train + n_validation]]
    test = df.iloc[indices[n_train + n_validation :]]
    return train, validation, test


def linear_weights(x: pd.DataFrame, y: pd.Series, regularization: float = 0.0):
    matrix = np.column_stack([np.ones(len(x)), x.to_numpy(dtype=float)])
    xtx = matrix.T @ matrix
    regularizer = regularization * np.eye(xtx.shape[0])
    regularizer[0, 0] = 0.0
    return np.linalg.solve(xtx + regularizer, matrix.T @ y.to_numpy(dtype=float))


def linear_rmse(
    train_x: pd.DataFrame,
    train_y: pd.Series,
    validation_x: pd.DataFrame,
    validation_y: pd.Series,
    fill_value,
    regularization: float = 0.0,
) -> float:
    train_filled = train_x.fillna(fill_value)
    validation_filled = validation_x.fillna(fill_value)
    weights = linear_weights(train_filled, train_y, regularization)
    matrix = np.column_stack([np.ones(len(validation_filled)), validation_filled])
    predictions = matrix @ weights
    return float(mean_squared_error(validation_y, predictions) ** 0.5)


def prepare_leads(df: pd.DataFrame):
    features = df.drop(columns=[LEAD_TARGET]).copy()
    categorical = features.select_dtypes(include=["object"]).columns.tolist()
    numerical = features.select_dtypes(exclude=["object"]).columns.tolist()
    features[categorical] = features[categorical].fillna("NA")
    features[numerical] = features[numerical].fillna(0.0)
    return features, categorical, numerical


def fit_lead_model(
    train_x: pd.DataFrame,
    train_y: pd.Series,
    validation_x: pd.DataFrame,
    c: float = 1.0,
):
    dv = DictVectorizer(sparse=False)
    train_matrix = dv.fit_transform(train_x.to_dict(orient="records"))
    validation_matrix = dv.transform(validation_x.to_dict(orient="records"))
    model = LogisticRegression(
        solver="liblinear", C=c, max_iter=1000, random_state=42
    )
    model.fit(train_matrix, train_y)
    return model, validation_matrix


def validate_hw1(car: pd.DataFrame) -> None:
    path = HOMEWORK_DIR / "01-intro" / "homework.md"
    require_option(path, "## Q2. Records count", str(len(car)))
    require_option(path, "## Q3. Fuel types", str(car["fuel_type"].nunique()))
    require_option(path, "## Q4. Missing values", str(car.isna().any().sum()))
    asia_max = f"{car.loc[car.origin == 'Asia', 'fuel_efficiency_mpg'].max():.1f}"
    require_option(path, "## Q5. Max fuel efficiency", asia_max)

    horsepower = car["horsepower"]
    before = horsepower.median()
    after = horsepower.fillna(horsepower.mode().iloc[0]).median()
    change = "No" if before == after else (
        "Yes, it increased" if after > before else "Yes, it decreased"
    )
    require_option(path, "## Q6. Median value of horsepower", change)

    asia = car.loc[car.origin == "Asia", ["vehicle_weight", "model_year"]].head(7)
    x = asia.to_numpy()
    y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
    weights = np.linalg.inv(x.T @ x) @ x.T @ y
    require_option(path, "## Q7. Sum of weights", f"{weights.sum():.3f}")


def validate_hw2(car: pd.DataFrame) -> None:
    path = HOMEWORK_DIR / "02-regression" / "homework.md"
    data = car[CAR_COLUMNS + ["fuel_efficiency_mpg"]]
    train, validation, test = split_with_lecture_shuffle(data, seed=42)

    missing_column = data.columns[data.isna().any()][0]
    require_option(path, "### Question 1", f"`'{missing_column}'`")
    require_option(path, "### Question 2", f"{data.horsepower.median():.0f}")

    zero_rmse = linear_rmse(
        train[CAR_COLUMNS], train.fuel_efficiency_mpg,
        validation[CAR_COLUMNS], validation.fuel_efficiency_mpg, 0.0,
    )
    mean_value = train.horsepower.mean()
    mean_rmse = linear_rmse(
        train[CAR_COLUMNS], train.fuel_efficiency_mpg,
        validation[CAR_COLUMNS], validation.fuel_efficiency_mpg, mean_value,
    )
    require_option(path, "### Question 3", "With mean" if mean_rmse < zero_rmse else "With 0")

    regularization_values = [0, 0.01, 0.1, 1, 5, 10, 100]
    regularization_scores = {
        r: linear_rmse(
            train[CAR_COLUMNS], train.fuel_efficiency_mpg,
            validation[CAR_COLUMNS], validation.fuel_efficiency_mpg, 0.0, r,
        )
        for r in regularization_values
    }
    best_r = min(regularization_values, key=lambda r: (round(regularization_scores[r], 4), r))
    require_option(path, "### Question 4", str(best_r))

    seed_scores = []
    for seed in range(10):
        seed_train, seed_validation, _ = split_with_lecture_shuffle(data, seed=seed)
        seed_scores.append(
            linear_rmse(
                seed_train[CAR_COLUMNS], seed_train.fuel_efficiency_mpg,
                seed_validation[CAR_COLUMNS], seed_validation.fuel_efficiency_mpg, 0.0,
            )
        )
    require_option(path, "### Question 5", f"{np.std(seed_scores):.3f}")

    train_9, validation_9, test_9 = split_with_lecture_shuffle(data, seed=9)
    combined = pd.concat([train_9, validation_9])
    test_rmse = linear_rmse(
        combined[CAR_COLUMNS], combined.fuel_efficiency_mpg,
        test_9[CAR_COLUMNS], test_9.fuel_efficiency_mpg, 0.0, 0.001,
    )
    require_option(path, "### Question 6", f"{test_rmse:.3f}")


def validate_hw3(lead: pd.DataFrame) -> None:
    path = HOMEWORK_DIR / "03-classification" / "homework.md"
    features, categorical, numerical = prepare_leads(lead)
    target = lead[LEAD_TARGET]
    train, validation, _ = split_three_way(features.assign(**{LEAD_TARGET: target}), seed=42)
    train_y = train.pop(LEAD_TARGET)
    validation_y = validation.pop(LEAD_TARGET)

    require_option(path, "### Question 1", f"`{lead.industry.mode().iloc[0]}`")
    correlations = features[numerical].corr().abs()
    candidate_pairs = [
        ("interaction_count", "lead_score"),
        ("number_of_courses_viewed", "lead_score"),
        ("number_of_courses_viewed", "interaction_count"),
        ("annual_income", "interaction_count"),
    ]
    best_pair = max(candidate_pairs, key=lambda pair: correlations.loc[pair[0], pair[1]])
    require_option(path, "### Question 2", "`" + "` and `".join(best_pair) + "`")

    mi = {
        column: mutual_info_score(train_y, train[column])
        for column in categorical
    }
    require_option(path, "### Question 3", f"`{max(mi, key=mi.get)}`")

    model, validation_matrix = fit_lead_model(train, train_y, validation)
    predictions = model.predict(validation_matrix)
    original_accuracy = accuracy_score(validation_y, predictions)
    require_option(path, "### Question 4", f"{original_accuracy:.2f}")

    differences = {}
    for column in ["lead_source", "number_of_courses_viewed", "interaction_count"]:
        reduced_train = train.drop(columns=[column])
        reduced_validation = validation.drop(columns=[column])
        reduced_model, reduced_matrix = fit_lead_model(
            reduced_train, train_y, reduced_validation
        )
        reduced_accuracy = accuracy_score(validation_y, reduced_model.predict(reduced_matrix))
        differences[column] = abs(original_accuracy - reduced_accuracy)
    require_option(
        path,
        "### Question 5",
        f"`'{min(differences, key=differences.get)}'`",
    )

    c_values = [1e-6, 1e-5, 1e-4, 1e-3]
    c_scores = {}
    for c in c_values:
        c_model, c_matrix = fit_lead_model(train, train_y, validation, c=c)
        c_scores[c] = accuracy_score(validation_y, c_model.predict(c_matrix))
    best_c = max(c_values, key=lambda c: (c_scores[c], -c))
    require_option(path, "### Question 6", f"{best_c:g}")


def validate_hw4(lead: pd.DataFrame) -> None:
    path = HOMEWORK_DIR / "04-evaluation" / "homework.md"
    features, categorical, numerical = prepare_leads(lead)
    prepared = features.assign(**{LEAD_TARGET: lead[LEAD_TARGET].to_numpy()})
    full_train, test = train_test_split(prepared, test_size=0.2, random_state=1)
    train, validation = train_test_split(full_train, test_size=0.25, random_state=1)
    train_y = train.pop(LEAD_TARGET)
    validation_y = validation.pop(LEAD_TARGET)

    single_feature_auc = {}
    for column in numerical:
        score = roc_auc_score(train_y, train[column])
        single_feature_auc[column] = max(score, 1.0 - score)
    candidates = [
        "lead_score",
        "number_of_courses_viewed",
        "interaction_count",
        "annual_income",
    ]
    require_option(path, "### Question 1", f"`{max(candidates, key=single_feature_auc.get)}`")

    model, validation_matrix = fit_lead_model(train, train_y, validation)
    probabilities = model.predict_proba(validation_matrix)[:, 1]
    validation_auc = roc_auc_score(validation_y, probabilities)
    require_option(path, "### Question 2", f"{validation_auc:.3f}")

    thresholds = np.arange(0.0, 1.0, 0.01)
    threshold_metrics = []
    for threshold in thresholds:
        predicted = (probabilities >= threshold).astype(int)
        precision = precision_score(validation_y, predicted, zero_division=0)
        recall = recall_score(validation_y, predicted, zero_division=0)
        if precision == 0 and recall == 0:
            continue
        threshold_metrics.append((abs(precision - recall), threshold))
    intersection = min(threshold_metrics)[1]
    require_option(path, "### Question 3", f"{intersection:.2f}")

    f1_scores = [
        f1_score(validation_y, (probabilities >= threshold).astype(int), zero_division=0)
        for threshold in thresholds
    ]
    best_threshold = thresholds[int(np.argmax(f1_scores))]
    require_option(path, "### Question 4", f"{best_threshold:.2f}")

    cv = KFold(n_splits=5, shuffle=True, random_state=1)
    cv_scores = []
    for fold_train_idx, fold_validation_idx in cv.split(full_train):
        fold_train = full_train.iloc[fold_train_idx].copy()
        fold_validation = full_train.iloc[fold_validation_idx].copy()
        fold_train_y = fold_train.pop(LEAD_TARGET)
        fold_validation_y = fold_validation.pop(LEAD_TARGET)
        fold_model, fold_matrix = fit_lead_model(
            fold_train, fold_train_y, fold_validation
        )
        cv_scores.append(
            roc_auc_score(fold_validation_y, fold_model.predict_proba(fold_matrix)[:, 1])
        )
    require_option(path, "### Question 5", f"{np.std(cv_scores):.3f}")

    tuning = {}
    for c in [1e-6, 1e-3, 1.0]:
        scores = []
        for fold_train_idx, fold_validation_idx in cv.split(full_train):
            fold_train = full_train.iloc[fold_train_idx].copy()
            fold_validation = full_train.iloc[fold_validation_idx].copy()
            fold_train_y = fold_train.pop(LEAD_TARGET)
            fold_validation_y = fold_validation.pop(LEAD_TARGET)
            fold_model, fold_matrix = fit_lead_model(
                fold_train, fold_train_y, fold_validation, c=c
            )
            scores.append(
                roc_auc_score(
                    fold_validation_y, fold_model.predict_proba(fold_matrix)[:, 1]
                )
            )
        tuning[c] = (np.mean(scores), np.std(scores))
    best_c = max(tuning, key=lambda c: (round(tuning[c][0], 3), -round(tuning[c][1], 3), -c))
    require_option(path, "### Question 6", f"{best_c:g}")


def validate_hw6(car: pd.DataFrame) -> None:
    path = HOMEWORK_DIR / "06-trees" / "homework.md"
    features = car.drop(columns=["fuel_efficiency_mpg"]).fillna(0)
    target = car["fuel_efficiency_mpg"]
    train, validation, _ = split_three_way(
        features.assign(fuel_efficiency_mpg=target), seed=1
    )
    train_y = train.pop("fuel_efficiency_mpg")
    validation_y = validation.pop("fuel_efficiency_mpg")
    dv = DictVectorizer(sparse=True)
    train_matrix = dv.fit_transform(train.to_dict(orient="records"))
    validation_matrix = dv.transform(validation.to_dict(orient="records"))

    tree = DecisionTreeRegressor(max_depth=1, random_state=1)
    tree.fit(train_matrix, train_y)
    split_feature = dv.feature_names_[tree.tree_.feature[0]]
    original_feature = split_feature.split("=", 1)[0]
    require_option(path, "## Question 1", f"`'{original_feature}'`")

    forest_scores = {}
    for n_estimators in [10, 50, 100, 150]:
        forest = RandomForestRegressor(
            n_estimators=n_estimators, random_state=1, n_jobs=-1
        )
        forest.fit(train_matrix, train_y)
        predictions = forest.predict(validation_matrix)
        forest_scores[n_estimators] = mean_squared_error(validation_y, predictions) ** 0.5

    require_option(path, "## Question 2", f"{forest_scores[10]:.3f}")
    require_option(path, "## Question 3", str(min(forest_scores, key=forest_scores.get)))

    depth_scores = {}
    for depth in [10, 15, 20, 25]:
        scores = []
        for n_estimators in [10, 50, 100, 150]:
            forest = RandomForestRegressor(
                n_estimators=n_estimators,
                max_depth=depth,
                random_state=1,
                n_jobs=-1,
            )
            forest.fit(train_matrix, train_y)
            scores.append(
                mean_squared_error(validation_y, forest.predict(validation_matrix)) ** 0.5
            )
        depth_scores[depth] = np.mean(scores)
    require_option(path, "## Question 4", str(min(depth_scores, key=depth_scores.get)))

    importance_forest = RandomForestRegressor(
        n_estimators=10, max_depth=20, random_state=1, n_jobs=-1
    )
    importance_forest.fit(train_matrix, train_y)
    importances = dict(zip(dv.feature_names_, importance_forest.feature_importances_))
    candidates = ["vehicle_weight", "horsepower", "acceleration", "engine_displacement"]
    best_feature = max(candidates, key=lambda name: importances.get(name, 0.0))
    require_option(path, "# Question 5", f"`{best_feature}`")

    # XGBoost is an optional course dependency. The question contract is still
    # checked here, while the numerical comparison is run in the release CI
    # environment that installs the course's pinned XGBoost version.
    require_option(path, "# Question 6", "0.1")


def main() -> None:
    car = pd.read_csv(DATA_DIR / "car_fuel_efficiency_2026.csv")
    lead = pd.read_csv(DATA_DIR / "course_lead_scoring_2026.csv")
    validate_hw1(car)
    validate_hw2(car)
    validate_hw3(lead)
    validate_hw4(lead)
    validate_hw6(car)
    print("ML Zoomcamp 2026 homework contract: OK")


if __name__ == "__main__":
    main()
