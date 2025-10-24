import pickle
import uvicorn
from fastapi import FastAPI
from typing import Dict, Any
from pydantic import BaseModel

app = FastAPI(title="homework prediction app")

#read the model
with open("pipeline_v1.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

#function to predict single input
def predict_single(input_data):
    result = pipeline.predict_proba(input_data)[0, 1]
    return float(result)

class Customer(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict_endpoint(costumer: Customer):
    probability = predict_single(costumer.dict())
    return {
        "predicted_probability": probability
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)

