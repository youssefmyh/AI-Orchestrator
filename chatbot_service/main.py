import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

model_name = "NousResearch/Llama-2-7b-chat-hf"

device = (
    "cuda" if torch.cuda.is_available() 
    else "mps" if torch.backends.mps.is_available() 
    else "cpu"
)

# Load tokenizer and model
print(f"Using device: {device}")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto").to(device).eval()

class ChatRequest(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"Welcome": "Chatbot Service is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    inputs = tokenizer(request.user_input, return_tensors="pt").to(device)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=100)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)