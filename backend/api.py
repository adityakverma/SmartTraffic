from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/congestion_model.pkl")


@app.get("/")
def home():
    return {"message": "SmartTraffic API Running"}


@app.post("/predict")
def predict():

    sample = pd.DataFrame({
        "zone": ["East"],
        "junction": ["KR Puram"],
        "hour": [18],
        "day_of_week": [5],
        "month": [6],
        "year": [2026]
    })

    risk = model.predict(sample)[0]

    return {
        "risk": risk
    }
@app.get("/recommendation")
def recommendation():

    risk = "High"

    return {
        "police_units": 5,
        "barricades": 12,
        "message": "Deploy maximum traffic control resources."
    }