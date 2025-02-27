# 🚀 Multi-Model AI Microservices Project

## 🌟 Overview

![Multi-Model Architecture](multimodel.webp)

Welcome to the **Multi-Model AI Microservices Project**! This project integrates three independent AI-powered services that can be deployed together seamlessly:

- **Recommender Service** – Suggests products based on user history.
- **Fraud Detection Service** – Detects suspicious transactions.
- **Chatbot Service** – Engages users in conversation.

Each service is built using **FastAPI** and is fully containerized with **Docker** for easy deployment. You can run everything locally using **Docker Compose** or deploy it to the cloud with **Kubernetes**.

---

## 🔧 Setup & Installation

### 1️⃣ Install Dependencies

Ensure **Python** is installed, then run:

```sh
pip install -r requirements.txt
```

### 2️⃣ Download Pre-trained Models

Run the following script to fetch the necessary AI models:

```sh
python scripts/download_models.py
```

This ensures that each service has the correct model files before running.

### 3️⃣ Start Services with Docker Compose

Launch all three services at once:

```sh
docker compose up --build
```

This will spin up the services on the following ports:

- **Recommender Service** → [http://localhost:8001](http://localhost:8001)
- **Fraud Detection Service** → [http://localhost:8002](http://localhost:8002)
- **Chatbot Service** → [http://localhost:8003](http://localhost:8003)

---

## 🔍 Testing the APIs

You can test each service using **cURL** or **Postman**.

### **Test Recommender Service**
```sh
curl "http://localhost:8001/recommend?user_id=123"
```

### **Test Fraud Detection Service**
```sh
curl -X POST "http://localhost:8002/detect_fraud" \
     -H "Content-Type: application/json" \
     -d '{"amount": 1000, "location": "NY"}'
```

### **Test Chatbot Service**
```sh
curl -X POST "http://localhost:8003/chat" \
     -H "Content-Type: application/json" \
     -d '{"user_input": "Hello!"}'
```

---

## ☁️ Deploying with Kubernetes

For cloud deployment, apply the Kubernetes configuration:

```sh
kubectl apply -f k8s/
```

---


## **Hardware Requirements**  

To run **AI-Orchestrator** efficiently, ensure your system meets the following hardware specifications:  

### **1. Processor (CPU/GPU)**  
- **CPU**: Multi-core processor (4+ cores, e.g., Intel i7/AMD Ryzen 7) for handling concurrent requests.  
- **GPU (Optional)**: Recommended for AI models requiring acceleration (e.g., deep learning). An **NVIDIA GPU with CUDA support (8GB+ VRAM)** is ideal.  

### **2. Memory (RAM)**  
- Minimum: **16GB RAM**  
- Recommended: **32GB RAM** for handling multiple AI services efficiently.  

### **3. Storage**  
- **Minimum**: 50GB free space  per model
- **Recommended**: **SSD (NVMe preferred)** for faster data access and improved system responsiveness.  

### **4. Networking**  
- **Stable high-speed internet** (especially if using cloud-based AI services or real-time processing).  

### **5. Operating System**  
- **Linux (Ubuntu 20.04+ recommended)** or **Windows 10/11** with **WSL2** for better compatibility with Docker and Kubernetes.  

### **6. Software Dependencies**  
Ensure the following are installed:  
- **Docker** (Latest version) for containerized deployments.  
- **Kubernetes** (Optional, for orchestration at scale).  
- **Python 3.8+** for AI model execution and service scripts.  
- **GPU Drivers & CUDA** (If using GPU for acceleration).  

### **7. Scalability Considerations**  
For production or large-scale deployments:  
- Consider **cloud-based solutions (AWS/GCP/Azure)** for dynamic scaling.  
- Use **load balancing** and **Kubernetes clusters** to optimize resource utilization.  

---
## ⚠️ Important Notes

- Ensure **Docker Desktop** is running before using `docker compose up`.
- Before downloading models, update `scripts/download_models.py` with the correct model URLs.
- You can modify the **Dockerfile** to match your specific requirements.

---
