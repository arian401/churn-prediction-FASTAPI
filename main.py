# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize app
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn using a trained ML model",
    version="1.0"
)

# Load model and scaler
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Define expected input schema
class CustomerData(BaseModel):
    tenure_months: float
    total_spent: float
    avg_purchase_frequency: float
    is_active: int  # 0 or 1

@app.post("/predict/")
def predict_churn(data: CustomerData):
    try:
        # Convert to DataFrame
        df = pd.DataFrame([data.dict()])

        # Scale input
        scaled_input = scaler.transform(df)

        # Predict churn
        prediction = model.predict(scaled_input)[0]

        return {"churn_prediction": int(prediction)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
