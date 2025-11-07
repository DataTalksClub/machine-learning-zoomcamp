#!/usr/bin/env python
# coding: utf-8

# # Midterm Project: Predicting Antibiotic-Producing Bacteria Using Morphological Features
# 
# ## Project Goal
# 
# Build a classification model to predict whether a bacterial strain will exhibit antimicrobial activity based solely on its morphological features, achieving the best possible **AUC score** on validation data.
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import pickle

# ### Data preparation
print('preparing data...')
df_all = pd.read_csv("data_allrounds_activitybinary.csv", sep=";")

df_all.columns = df_all.columns.str.lower().str.replace(' ', '_')

# ### Split data into train, val, test
df = df_all.iloc[:,5:28].copy()

df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.activity_total.astype('int').values
y_test = df_test.activity_total.astype('int').values

del df_train['activity_total']
del df_test['activity_total']

def train(df_train, y_train, max_depth, min_samples_leaf, max_features):
    train_dicts = df_train.to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dicts)

    model= RandomForestClassifier(n_estimators=200,
                                max_depth=max_depth,
                                min_samples_leaf=min_samples_leaf,
                                max_features=max_features,
                                random_state=1)
    model.fit(X_train, y_train)
    return dv, model

def predict(df, dv, model):
    dicts = df.to_dict(orient='records')
    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred

# ### Training
print('training ...')
dv, model = train(df_train, y_train, max_depth=5, min_samples_leaf=10, max_features=0.2)
y_pred = predict(df_test, dv, model)
roc_auc = roc_auc_score(y_test, y_pred)
print(f'ROC AUC: {roc_auc}')


# ### Save the model
print('saving model...')

# Save model
with open('random_forest_model.bin', 'wb') as f:
    pickle.dump(model, f)

# Save the DictVectorizer
with open('dict_vectorizer.bin', 'wb') as f_out:
    pickle.dump(dv, f_out)
