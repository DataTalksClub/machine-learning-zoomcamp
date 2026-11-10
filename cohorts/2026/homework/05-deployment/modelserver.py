import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Define the input data schema matching your lead features
class LeadInput(BaseModel):
    lead_source: str
    industry: str
    employment_status: str
    location: str
    number_of_courses_viewed: int
    annual_income: float
    interaction_count: int
    lead_score: float

# Define the expected output structure
class PredictionOutput(BaseModel):
    conversion_probability: float
    conversion: bool

# Initialize FastAPI application
app = FastAPI()

# Load the model pipeline at startup
# (DictVectorizer expects a dictionary/list of dicts, which Pydantic's .model_dump() provides)
MODEL_FILE = "pipeline.bin"
with open(MODEL_FILE, "rb") as f_in:
    pipeline = pickle.load(f_in)

@app.get("/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionOutput)
def predict(lead: LeadInput):
    """Predict the conversion probability for an incoming lead."""
    # Convert Pydantic model to a standard Python dictionary
    lead_dict = lead.model_dump()
    
    # Extract the probability for the positive class (conversion)
    # Wrap in a list because DictVectorizer expects a collection of records
    prob = float(pipeline.predict_proba([lead_dict])[0, 1])
    
    # Determine the boolean outcome using a standard 0.5 threshold
    conversion_outcome = prob >= 0.5
    
    return {
        "conversion_probability": round(prob, 3),
        "conversion": conversion_outcome
    }
