#!/usr/bin/env python3
"""
Solución oficial y detallada: Homework 1 - Introducción a Machine Learning
Machine Learning Zoomcamp (Cohorte 2026)
"""

from pathlib import Path
import numpy as np
import pandas as pd

# Rutas de datos
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parents[1] / "data" / "car_fuel_efficiency_2026.csv"

print("=" * 60)
print("MACHINE LEARNING ZOOMCAMP 2026 - HOMEWORK 1")
print("=" * 60)

# -------------------------------------------------------------
# Q1. Pandas version
# -------------------------------------------------------------
pandas_version = pd.__version__
print(f"\n[Q1] Versión de Pandas instalada: {pandas_version}")

# -------------------------------------------------------------
# Carga de datos
# -------------------------------------------------------------
print(f"\nCargando dataset desde: {DATA_PATH}...")
df = pd.read_csv(DATA_PATH)
print(f"Dataset cargado exitosamente. Forma: {df.shape}")

# -------------------------------------------------------------
# Q2. Records count
# -------------------------------------------------------------
n_records = len(df)
print(f"\n[Q2] Cantidad de registros en el dataset: {n_records}")
# Opciones: 5000, 9000, 10000, 15000 -> Respuesta: 10000

# -------------------------------------------------------------
# Q3. Fuel types
# -------------------------------------------------------------
n_fuel_types = df["fuel_type"].nunique()
fuel_types_list = df["fuel_type"].unique().tolist()
print(f"\n[Q3] Cantidad de tipos de combustible: {n_fuel_types} {fuel_types_list}")
# Opciones: 1, 2, 3, 4 -> Respuesta: 3

# -------------------------------------------------------------
# Q4. Missing values
# -------------------------------------------------------------
missing_per_col = df.isna().sum()
cols_with_missing = (missing_per_col > 0).sum()
print(f"\n[Q4] Columnas con valores faltantes: {cols_with_missing}")
print("Detalle de valores faltantes por columna:")
for col, count in missing_per_col.items():
    if count > 0:
        print(f"  - {col}: {count} nulos ({count / len(df) * 100:.2f}%)")
# Opciones: 0, 1, 2, 3, 4 -> Respuesta: 2

# -------------------------------------------------------------
# Q5. Max fuel efficiency (Asia)
# -------------------------------------------------------------
asia_cars = df[df["origin"] == "Asia"]
max_fuel_eff_asia = asia_cars["fuel_efficiency_mpg"].max()
print(f"\n[Q5] Máxima eficiencia de combustible para autos de Asia: {max_fuel_eff_asia:.1f}")
# Opciones: 21.2, 31.2, 41.2, 51.2 -> Respuesta: 41.2

# -------------------------------------------------------------
# Q6. Median value of horsepower
# -------------------------------------------------------------
horsepower_series = df["horsepower"]
median_before = horsepower_series.median()
mode_hp = horsepower_series.mode().iloc[0]
horsepower_filled = horsepower_series.fillna(mode_hp)
median_after = horsepower_filled.median()

if median_after > median_before:
    q6_answer = "Yes, it increased"
elif median_after < median_before:
    q6_answer = "Yes, it decreased"
else:
    q6_answer = "No"

print(f"\n[Q6] Mediana de horsepower antes: {median_before}")
print(f"     Moda de horsepower: {mode_hp}")
print(f"     Mediana de horsepower después: {median_after}")
print(f"     ¿Ha cambiado?: {q6_answer}")
# Opciones: Yes, it increased / Yes, it decreased / No -> Respuesta: Yes, it decreased

# -------------------------------------------------------------
# Q7. Sum of weights (Linear Regression)
# -------------------------------------------------------------
asia_subset = df.loc[df["origin"] == "Asia", ["vehicle_weight", "model_year"]].head(7)
X = asia_subset.to_numpy()
XTX = X.T @ X
XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
w = XTX_inv @ X.T @ y
w_sum = w.sum()

print(f"\n[Q7] Matriz X (primeras 7 filas de Asia):\n{X}")
print(f"     Vector y: {y}")
print(f"     Pesos w calculados: {w}")
print(f"     Suma de pesos: {w_sum:.3f} (redondeado: {round(w_sum, 3)})")
# Opciones: 0.0369, 0.369, 3.69, 36.9 -> Respuesta: 0.369

print("\n" + "=" * 60)
print("FIN HOMEWORK 1")
print("=" * 60)

