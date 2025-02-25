from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/detect_fraud")
def detect_fraud(transaction: dict):
    features = np.array([list(transaction.values())])
    prediction = model.predict(features)[0]
    return {"fraud": bool(prediction)}
