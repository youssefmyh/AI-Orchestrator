import requests

models = {
    "recommender_service/model.onnx": "https://huggingface.co/microsoft/resnet-50/resolve/main/model.onnx",
    "fraud_detection_service/model.onnx": "https://huggingface.co/mistralai/Mistral-7B-v0.1/resolve/main/model.onnx",
    "chatbot_service/model.onnx": "https://huggingface.co/deepset/roberta-base-squad2/resolve/main/model.onnx",
}

for path, url in models.items():
    print(f"Downloading {path}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"✅ {path} downloaded!")
    else:
        print(f"❌ Failed to download {path}")
