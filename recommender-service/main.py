from fastapi import FastAPI, HTTPException
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import uvicorn

app = FastAPI()

# Device Selection: CUDA → MPS (Mac) → CPU
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# Load Tokenizer & Model
model_name = "NousResearch/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, device_map="auto").to(device).eval()

@app.get("/")
def read_root():
    return {"Welcome": "recommender-service is running!"}

@app.get("/recommend")
def recommend(user_id: int):
    try:
        user_input = f"User ID: {user_id}. Generate recommendations."

        # Ensure inputs are on the same device as the model
        inputs = tokenizer(user_input, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=50)

        recommendations = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {"user_id": user_id, "recommendations": recommendations}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)