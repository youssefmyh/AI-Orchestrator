from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/chat")
def chat(user_input: str):
    response = model.predict([user_input])[0]
    return {"response": response}
