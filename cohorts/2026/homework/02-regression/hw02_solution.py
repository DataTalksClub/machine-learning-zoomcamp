#!/usr/bin/env python3
"""
Solución oficial y detallada: Homework 2 - Regresión Lineal
Machine Learning Zoomcamp (Cohorte 2026)
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

# Rutas de datos
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parents[1] / "data" / "car_fuel_efficiency_2026.csv"

print("=" * 60)
print("MACHINE LEARNING ZOOMCAMP 2026 - HOMEWORK 2")
print("=" * 60)

# Carga de datos
df = pd.read_csv(DATA_PATH)
CAR_COLUMNS = ["engine_displacement", "horsepower", "vehicle_weight", "model_year"]
TARGET = "fuel_efficiency_mpg"

# Filtrar columnas requeridas
data = df[CAR_COLUMNS + [TARGET]].copy()
print(f"Dataset filtrado con forma: {data.shape}")

# -------------------------------------------------------------
# Question 1: Columna con valores faltantes
# -------------------------------------------------------------
missing_series = data.isna().sum()
missing_col = missing_series[missing_series > 0].index[0]
print(f"\n[Q1] Columna con valores faltantes: '{missing_col}' (nulos: {missing_series[missing_col]})")
# Opciones: engine_displacement, horsepower, vehicle_weight, model_year -> Respuesta: horsepower

# -------------------------------------------------------------
# Question 2: Mediana de horsepower
# -------------------------------------------------------------
hp_median = data["horsepower"].median()
print(f"\n[Q2] Mediana de 'horsepower': {hp_median:.0f}")
# Opciones: 204, 254, 304, 354 -> Respuesta: 254

# -------------------------------------------------------------
# Función para split con shuffle de las clases
# -------------------------------------------------------------
def split_with_lecture_shuffle(dataframe: pd.DataFrame, seed: int):
    n = len(dataframe)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    indices = np.arange(n)
    np.random.RandomState(seed).shuffle(indices)

    df_train = dataframe.iloc[indices[:n_train]].copy()
    df_val = dataframe.iloc[indices[n_train : n_train + n_val]].copy()
    df_test = dataframe.iloc[indices[n_train + n_val :]].copy()

    return df_train, df_val, df_test

# -------------------------------------------------------------
# Funciones para entrenamiento de regresión lineal y RMSE
# -------------------------------------------------------------
def train_linear_regression(X_train: pd.DataFrame, y_train: pd.Series, r: float = 0.0):
    matrix = np.column_stack([np.ones(len(X_train)), X_train.to_numpy(dtype=float)])
    XTX = matrix.T @ matrix
    if r > 0:
        regularizer = r * np.eye(XTX.shape[0])
        regularizer[0, 0] = 0.0
        XTX = XTX + regularizer
    weights = np.linalg.solve(XTX, matrix.T @ y_train.to_numpy(dtype=float))
    return weights

def evaluate_linear_regression(X_val: pd.DataFrame, y_val: pd.Series, weights: np.ndarray) -> float:
    matrix = np.column_stack([np.ones(len(X_val)), X_val.to_numpy(dtype=float)])
    y_pred = matrix @ weights
    return float(np.sqrt(mean_squared_error(y_val, y_pred)))

def compute_rmse(df_train, df_val, fill_value, r=0.0):
    X_train = df_train[CAR_COLUMNS].fillna(fill_value)
    y_train = df_train[TARGET]
    X_val = df_val[CAR_COLUMNS].fillna(fill_value)
    y_val = df_val[TARGET]

    w = train_linear_regression(X_train, y_train, r=r)
    return evaluate_linear_regression(X_val, y_val, w)

# -------------------------------------------------------------
# Question 3: Imputación con 0 vs con la media
# -------------------------------------------------------------
train_42, val_42, test_42 = split_with_lecture_shuffle(data, seed=42)

rmse_zero = compute_rmse(train_42, val_42, fill_value=0.0)
mean_horsepower = train_42["horsepower"].mean()
rmse_mean = compute_rmse(train_42, val_42, fill_value=mean_horsepower)

print(f"\n[Q3] RMSE con 0:    {rmse_zero:.3f} (exacto: {rmse_zero:.5f})")
print(f"     RMSE con media: {rmse_mean:.3f} (exacto: {rmse_mean:.5f})")
if round(rmse_mean, 3) < round(rmse_zero, 3):
    q3_answer = "With mean"
elif round(rmse_zero, 3) < round(rmse_mean, 3):
    q3_answer = "With 0"
else:
    q3_answer = "Both are equally good"
print(f"     Mejor opción: {q3_answer}")
# Opciones: With 0, With mean, Both are equally good -> Respuesta: With mean

# -------------------------------------------------------------
# Question 4: Regresión lineal con regularización
# -------------------------------------------------------------
r_candidates = [0, 0.01, 0.1, 1, 5, 10, 100]
print("\n[Q4] Evaluando regularización (r) con NA=0:")
r_scores = {}
for r in r_candidates:
    score = compute_rmse(train_42, val_42, fill_value=0.0, r=r)
    r_scores[r] = round(score, 4)
    print(f"     r={r:<6}: RMSE = {score:.4f}")

best_r = min(r_candidates, key=lambda r: (r_scores[r], r))
print(f"     Mejor r (menor RMSE redondeado a 4 decimales): {best_r}")
# Opciones: 0, 0.01, 0.1, 1, 5, 10, 100 -> Respuesta: 0

# -------------------------------------------------------------
# Question 5: Estabilidad de semillas
# -------------------------------------------------------------
seeds = list(range(10))
seed_scores = []
for seed in seeds:
    tr, val, _ = split_with_lecture_shuffle(data, seed=seed)
    score = compute_rmse(tr, val, fill_value=0.0, r=0.0)
    seed_scores.append(score)

std_rmse = np.std(seed_scores)
print(f"\n[Q5] RMSE para semillas 0 a 9: {[round(s, 4) for s in seed_scores]}")
print(f"     Desviación estándar de los scores: {std_rmse:.3f} (redondeado: {round(std_rmse, 3)})")
# Opciones: 0.006, 0.016, 0.029, 0.036 -> Respuesta: 0.029

# -------------------------------------------------------------
# Question 6: Evaluación final en Test con semilla 9 y r=0.001
# -------------------------------------------------------------
train_9, val_9, test_9 = split_with_lecture_shuffle(data, seed=9)
combined_train = pd.concat([train_9, val_9])

X_comb = combined_train[CAR_COLUMNS].fillna(0.0)
y_comb = combined_train[TARGET]
X_test = test_9[CAR_COLUMNS].fillna(0.0)
y_test = test_9[TARGET]

w_final = train_linear_regression(X_comb, y_comb, r=0.001)
final_test_rmse = evaluate_linear_regression(X_test, y_test, w_final)
print(f"\n[Q6] RMSE final en Test (seed 9, r=0.001): {final_test_rmse:.3f}")
# Opciones: 0.236, 2.236, 22.10, 221.0 -> Respuesta: 2.236

print("\n" + "=" * 60)
print("FIN HOMEWORK 2")
print("=" * 60)

