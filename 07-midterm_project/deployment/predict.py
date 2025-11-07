import pickle
import uvicorn
from fastapi import FastAPI
from typing import Dict, Any
from pydantic import BaseModel
from sklearn.feature_extraction import DictVectorizer


app = FastAPI(title="Deployment midterm project app")

#read the model
with open("random_forest_model.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

with open('dict_vectorizer.bin', 'rb') as f:
    dv = pickle.load(f)

#function to predict single input
def predict_single(input_data):
    X = dv.transform([input_data])
    result = pipeline.predict_proba(X)[0, 1]
    return float(result)

class BacteriaSample(BaseModel):
    growth_rate: float
    peaks: int
    circularity: float
    eccentricity: float
    RGB_mean_1: float
    RGBt_mean_2: float
    RGBt_mean_3: float
    RGBt_std_1: float
    RGBt_std_2: float
    RGBt_std_3: float
    Lab_mean_1: float
    Lab_mean_2: float
    Lab_mean_3: float
    Lab_std_1: float
    Lab_std_2: float
    Lab_std_3: float
    Labt_mean_1: float
    Labt_mean_2: float
    Labt_mean_3: float
    Labt_std_1: float
    Labt_std_2: float
    Labt_std_3: float

@app.post("/predict")
def predict_endpoint(bacteria: BacteriaSample):
    activity = predict_single(bacteria.dict())
    return {
        "activity_probability": activity,
        "activity_predicted": int(activity >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)

