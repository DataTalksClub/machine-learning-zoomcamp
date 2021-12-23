import joblib

import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

url = 'https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv?raw=true'
df = pd.read_csv(url)

df.columns = df.columns.str.lower().str.replace(' ', '_')

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)

df.churn = (df.churn == 'yes').astype(int)


numerical = ['tenure', 'monthlycharges']
categorical = ['contract']


dicts = df[categorical + numerical].to_dict(orient='records')

pipeline = Pipeline([
    ('vectorizer', DictVectorizer(sparse=False)),
    ('model', LogisticRegression(C=1.0, solver='liblinear'))
])

pipeline.fit(dicts, df.churn.values)

joblib.dump(pipeline, 'model.joblib')

