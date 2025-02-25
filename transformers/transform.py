import os
import torch
import onnx
import tensorflow as tf
from onnx2keras import onnx_to_keras
from transformers import AutoModel

def load_model(model_name: str):
    """Load a DeepSeek model from Hugging Face."""
    model = AutoModel.from_pretrained(model_name)
    return model

def save_as_pt(model, save_path: str):
    """Save model as PyTorch .pt format."""
    torch.save(model.state_dict(), save_path)
    print(f"Model saved to {save_path}")

def convert_to_onnx(model, dummy_input_shape, save_path: str):
    """Convert a PyTorch model to ONNX format."""
    dummy_input = torch.randn(*dummy_input_shape)
    torch.onnx.export(model, dummy_input, save_path, input_names=['input'], output_names=['output'])
    print(f"Model converted to ONNX at {save_path}")

def convert_to_h5(onnx_path: str, h5_path: str):
    """Convert an ONNX model to H5 format."""
    onnx_model = onnx.load(onnx_path)
    k_model = onnx_to_keras(onnx_model, ['input'])
    k_model.save(h5_path)
    print(f"Model saved to {h5_path}")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    model_name = "deepseek-ai/deepseek-llm-7b-base"
    model = load_model(model_name)
    save_as_pt(model, "models/deepseek_model.pt")
    convert_to_onnx(model, (1, 3, 224, 224), "models/deepseek_model.onnx")
    convert_to_h5("models/deepseek_model.onnx", "models/deepseek_model.h5")
