import os
import requests
from transformers import AutoModel

def load_model(model_name: str, save_path: str):
    model = AutoModel.from_pretrained(model_name)
    model.save_pretrained(save_path)
    model_path = os.path.join(save_path, "model.pt")
    model.save_pretrained(model_path)
    print(f"✅ Model saved as {model_path}")

# Define microservice model paths
microservices = ["recommender_service", "fraud_detection_service", "chatbot_service"]
model_name = "deepseek-ai/deepseek-llm-7b-base"

for service in microservices:
    save_path = os.path.join(service, "model")
    os.makedirs(save_path, exist_ok=True)
    print(f"Downloading model for {service}...")
    load_model(model_name, save_path)

# ONNX model URLs
#models = {
#    "recommender_service/model.onnx": "https://huggingface.co/microsoft/resnet-50/resolve/main/model.onnx",
#    "fraud_detection_service/model.onnx": "https://huggingface.co/mistralai/Mistral-7B-v0.1/resolve/main/model.onnx",
#    "chatbot_service/model.onnx": "https://huggingface.co/deepset/roberta-base-squad2/resolve/main/model.onnx",
#}

# Download ONNX models
#for path, url in models.items():
#    print(f"Downloading {path}...")
#    response = requests.get(url)
#    if response.status_code == 200:
#        with open(path, "wb") as f:
#            f.write(response.content)
#        print(f"✅ {path} downloaded!")
#    else:
#        print(f"❌ Failed to download {path}")
