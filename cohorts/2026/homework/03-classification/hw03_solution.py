#!/usr/bin/env python3
"""
Solución oficial y detallada: Homework 3 - Clasificación y Regresión Logística
Machine Learning Zoomcamp (Cohorte 2026)
"""

from pathlib import Path
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mutual_info_score

# Filtrar warnings de compatibilidad de pandas si fuera necesario
warnings.filterwarnings("ignore")

# Rutas de datos
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parents[1] / "data" / "course_lead_scoring_2026.csv"

print("=" * 60)
print("MACHINE LEARNING ZOOMCAMP 2026 - HOMEWORK 3")
print("=" * 60)

# Carga de datos
df = pd.read_csv(DATA_PATH)
TARGET = "converted"
print(f"Dataset cargado con forma: {df.shape}")

# -------------------------------------------------------------
# Preparación de datos
# - Categóricos nulos -> 'NA'
# - Numéricos nulos -> 0.0
# -------------------------------------------------------------
features = df.drop(columns=[TARGET]).copy()

# Identificar tipos de columnas de forma robusta y compatible
numerical = [c for c in features.columns if pd.api.types.is_numeric_dtype(features[c])]
categorical = [c for c in features.columns if c not in numerical]

features[categorical] = features[categorical].fillna("NA")
features[numerical] = features[numerical].fillna(0.0)

# -------------------------------------------------------------
# Question 1: Moda de 'industry'
# -------------------------------------------------------------
industry_mode = df["industry"].mode().iloc[0]
print(f"\n[Q1] Moda de la columna 'industry': {industry_mode}")
# Opciones: NA, technology, healthcare, retail -> Respuesta: technology

# -------------------------------------------------------------
# Question 2: Matriz de correlación para variables numéricas
# -------------------------------------------------------------
corr_matrix = features[numerical].corr().abs()
candidate_pairs = [
    ("interaction_count", "lead_score"),
    ("number_of_courses_viewed", "lead_score"),
    ("number_of_courses_viewed", "interaction_count"),
    ("annual_income", "interaction_count"),
]

print("\n[Q2] Correlación entre los pares candidatos:")
for col1, col2 in candidate_pairs:
    print(f"     {col1} y {col2}: {corr_matrix.loc[col1, col2]:.4f}")

best_pair = max(candidate_pairs, key=lambda pair: corr_matrix.loc[pair[0], pair[1]])
print(f"     Par con mayor correlación: '{best_pair[0]}' y '{best_pair[1]}'")
# Opciones:
# - interaction_count and lead_score
# - number_of_courses_viewed and lead_score
# - number_of_courses_viewed and interaction_count
# - annual_income and interaction_count
# Respuesta: interaction_count and lead_score

# -------------------------------------------------------------
# Split de datos (60% train, 20% val, 20% test)
# -------------------------------------------------------------
prepared_df = features.assign(**{TARGET: df[TARGET]})
df_full_train, df_test = train_test_split(prepared_df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

y_train = df_train.pop(TARGET).values
y_val = df_val.pop(TARGET).values
y_test = df_test.pop(TARGET).values

# -------------------------------------------------------------
# Question 3: Mutual Information con 'converted'
# -------------------------------------------------------------
mi_scores = {}
for col in categorical:
    score = mutual_info_score(y_train, df_train[col])
    mi_scores[col] = round(score, 2)

print("\n[Q3] Mutual Information con el target 'converted':")
for col, score in mi_scores.items():
    print(f"     {col}: {score:.2f}")

highest_mi_col = max(mi_scores, key=mi_scores.get)
print(f"     Variable con mayor MI: '{highest_mi_col}' ({mi_scores[highest_mi_col]})")
# Opciones: industry, location, lead_source, employment_status -> Respuesta: lead_source

# -------------------------------------------------------------
# Función auxiliar para entrenar Regresión Logística con One-Hot Encoding
# -------------------------------------------------------------
def train_and_eval_logistic(train_features, val_features, c=1.0):
    dv = DictVectorizer(sparse=False)
    X_train_dict = train_features.to_dict(orient="records")
    X_val_dict = val_features.to_dict(orient="records")

    X_train = dv.fit_transform(X_train_dict)
    X_val = dv.transform(X_val_dict)

    model = LogisticRegression(solver="liblinear", C=c, max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    val_preds = model.predict(X_val)
    acc = accuracy_score(y_val, val_preds)
    return model, dv, acc

# -------------------------------------------------------------
# Question 4: Accuracy del modelo completo
# -------------------------------------------------------------
base_model, dv, original_acc = train_and_eval_logistic(df_train, df_val, c=1.0)
print(f"\n[Q4] Accuracy en validación (modelo completo): {original_acc:.2f} (exacto: {original_acc:.4f})")
# Opciones: 0.55, 0.65, 0.75, 0.85 -> Respuesta: 0.65

# -------------------------------------------------------------
# Question 5: Eliminación de características (Feature Elimination)
# -------------------------------------------------------------
target_features = ["lead_source", "number_of_courses_viewed", "interaction_count"]
acc_diffs = {}

print("\n[Q5] Feature elimination:")
for feat in target_features:
    train_sub = df_train.drop(columns=[feat])
    val_sub = df_val.drop(columns=[feat])
    _, _, acc_without = train_and_eval_logistic(train_sub, val_sub, c=1.0)
    diff = abs(original_acc - acc_without)
    acc_diffs[feat] = diff
    print(f"     Sin '{feat}': Accuracy = {acc_without:.4f} | Diferencia = {diff:.4f}")

least_useful = min(acc_diffs, key=acc_diffs.get)
print(f"     Característica con menor diferencia: '{least_useful}' (diff = {acc_diffs[least_useful]:.4f})")
# Opciones: 'lead_source', 'number_of_courses_viewed', 'interaction_count' -> Respuesta: 'number_of_courses_viewed'

# -------------------------------------------------------------
# Question 6: Regularización C
# -------------------------------------------------------------
c_list = [0.000001, 0.00001, 0.0001, 0.001]
c_scores = {}

print("\n[Q6] Regularización variando C:")
for c in c_list:
    _, _, acc = train_and_eval_logistic(df_train, df_val, c=c)
    c_scores[c] = round(acc, 3)
    print(f"     C={c:<8}: Accuracy = {acc:.4f} (redondeado a 3 dec: {round(acc, 3)})")

best_c = max(c_list, key=lambda c: (c_scores[c], -c))
print(f"     Mejor C: {best_c}")
# Opciones: 0.000001, 0.00001, 0.0001, 0.001 -> Respuesta: 0.001

print("\n" + "=" * 60)
print("FIN HOMEWORK 3")
print("=" * 60)

