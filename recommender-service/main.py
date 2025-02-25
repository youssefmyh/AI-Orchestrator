from fastapi import FastAPI
import torch
from transformers import AutoModel, AutoTokenizer

app = FastAPI()

model_name = "NousResearch/Llama-2-7b-chat-hf" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto").eval()

@app.get("/recommend")
def recommend(user_id: int):
    user_input = f"User ID: {user_id}. Generate recommendations."

    inputs = tokenizer(user_input, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        outputs = model(**inputs)

    recommendations = outputs.last_hidden_state.mean(dim=1).tolist()

    return {"user_id": user_id, "recommendations": recommendations}
