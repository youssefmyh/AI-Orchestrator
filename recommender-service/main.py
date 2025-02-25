from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/recommend")
def recommend(user_id: int):
    recommendations = model.predict(np.array([[user_id]])).tolist()
    return {"user_id": user_id, "recommendations": recommendations}
