import pickle
import uvicorn
from fastapi import FastAPI


app = FastAPI(title='lead-scoring')

with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


@app.post('/predict')
def predict(lead: dict) -> dict:
    y_pred = pipeline.predict_proba(lead)[0, 1]
    conversion = y_pred >= 0.5

    result = {
        'conversion_probability': float(y_pred),
        'conversion': bool(conversion)
    }

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)