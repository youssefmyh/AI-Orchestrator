from fastapi import FastAPI
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

model_name = "NousResearch/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto").eval()

@app.post("/detect_fraud")
def detect_fraud(transaction: dict):
    transaction_text = f"Transaction: {transaction['description']}. Is it 'fraud' or 'not fraud'?"

    inputs = tokenizer(transaction_text, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=5)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip().lower()
    is_fraud = "fraud" in response

    return {"fraud": is_fraud, "response": response}
