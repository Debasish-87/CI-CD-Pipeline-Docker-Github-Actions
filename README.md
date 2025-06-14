# 🚀 CI/CD Pipeline with GitHub Actions, Docker, and Minikube

This project demonstrates a complete CI/CD pipeline built with **GitHub Actions**, **Docker**, and **Minikube**, without using any cloud provider. The pipeline automatically builds, tests, and deploys a simple Node.js application locally using Kubernetes.

---

## 🧩 Project Overview

| Stage       | Tool/Platform     | Purpose                                     |
|-------------|-------------------|---------------------------------------------|
| CI          | GitHub Actions     | Automate build, test, and push to Docker Hub |
| Containerization | Docker          | Build and package the Node.js app           |
| Image Hosting | Docker Hub       | Store and retrieve Docker images            |
| CD / Deployment | Minikube + kubectl | Deploy app to local Kubernetes cluster     |

---

## 📁 Project Structure

```

CI-CD-Pipeline-Docker-Github-Actions/
├── .github/workflows/
│   └── main.yml               # GitHub Actions workflow
├── Dockerfile                 # Docker image definition
├── app.js                     # Simple Node.js application
├── package.json               # App dependencies
├── kubernetes.yaml            # Kubernetes deployment & service
├── README.md                  # Project documentation

````

---

## ⚙️ Tools & Technologies Used

- **GitHub Actions** – Continuous Integration & Automation
- **Docker** – Containerization
- **Docker Hub** – Image Registry (🔗 [`debasish8787/simple-node-app`](https://hub.docker.com/r/debasish8787/simple-node-app))
- **Minikube** – Local Kubernetes Cluster
- **kubectl** – Kubernetes CLI
- **Node.js** – Application Runtime

---

## 🔁 CI/CD Workflow

### ✅ GitHub Actions Flow

1. **Trigger**: On every push to `main` branch
2. **Steps**:
   - Checkout code
   - Set up Docker Buildx
   - Log in to Docker Hub
   - Build Docker image
   - Push image to Docker Hub

### 📜 Workflow File: `.github/workflows/main.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: debasish8787/simple-node-app:latest
````

---

## 🐳 Docker Build

```bash
docker build -t debasish8787/simple-node-app:latest .
docker push debasish8787/simple-node-app:latest
```

---

## ☸️ Kubernetes Deployment (Minikube)

### ✅ Steps:

```bash
# Load image into Minikube
minikube image load debasish8787/simple-node-app:latest

# Deploy the app
kubectl create deployment simple-node-app --image=debasish8787/simple-node-app:latest

# Expose via NodePort
kubectl expose deployment simple-node-app --type=NodePort --port=80

# Access the app
minikube service simple-node-app
```

### ✅ Output:

```
🚀 Hello from CI/CD Pipeline using GitHub Actions + Docker + Minikube!
```

---

## 🖼️ Screenshots

| 📌 Stage | Screenshot Proof |

| ✅ GitHub Actions Success 

![d03e1ef2-dc4a-45f7-b2be-3beb6cc9dbaa](https://github.com/user-attachments/assets/79a1a394-842d-45a2-8333-ba40568a2b36)

| ✅ Docker Hub Image  

![56c4795c-0418-47dc-be6a-8784e922571d](https://github.com/user-attachments/assets/d847e679-a5ff-4d00-91f7-670fa697d505)

| ✅ kubectl get pods & Pod Logs/Describe 

![Screenshot from 2025-06-15 03-03-24](https://github.com/user-attachments/assets/fc74b14f-aec1-4ac1-a67d-b8c13d3b1a0c)

| ✅ App Running in Browser 

![9a53ab26-6a6c-47e3-a8e6-e08bb96d131f](https://github.com/user-attachments/assets/3b7d4b18-f404-4ee5-b715-2ede137771bb)

---

## 🔗 Docker Hub Image

> [`https://hub.docker.com/r/debasish8787/simple-node-app`](https://hub.docker.com/r/debasish8787/simple-node-app)

---

## ✍️ Author

**Debasish Mohanty**
👨‍💻 DevOps & Cloud Intern
🔗 [GitHub](https://github.com/Debasish-87) | 🌐 [Docker Hub](https://hub.docker.com/u/debasish8787)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```

