import joblib
import pandas as pd

model = joblib.load("models/congestion_model.pkl")

sample_event = pd.DataFrame({
    "zone": ["East"],
    "junction": ["KR Puram"],
    "hour": [18],
    "day_of_week": [5],
    "month": [6],
    "year": [2026]
})

prediction = model.predict(sample_event)

print("\nPredicted Congestion Risk:")
print(prediction[0])