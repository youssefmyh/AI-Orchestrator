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

## ⚠️ Important Notes

- Ensure **Docker Desktop** is running before using `docker compose up`.
- Before downloading models, update `scripts/download_models.py` with the correct model URLs.
- You can modify the **Dockerfile** to match your specific requirements.

---