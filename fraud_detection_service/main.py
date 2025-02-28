from fastapi import FastAPI
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import uvicorn

app = FastAPI()

model_name = "NousResearch/Llama-2-7b-chat-hf"

device = (
    "cuda" if torch.cuda.is_available() 
    else "mps" if torch.backends.mps.is_available() 
    else "cpu"
)

print(f"Using device: {device}")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto").to(device).eval()

@app.get("/")
def read_root():
    return {"Welcome": "fraud_detection_service is running!"}

@app.post("/detect_fraud")
def detect_fraud(transaction: dict):
    description = transaction.get("description", "No description provided")
    transaction_text = f"Transaction: {description}. Is it 'fraud' or 'not fraud'?"

    inputs = tokenizer(transaction_text, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=5)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip().lower()
    is_fraud = "fraud" in response

    return {"fraud": is_fraud, "response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)