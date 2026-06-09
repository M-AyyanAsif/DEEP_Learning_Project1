<<<<<<< HEAD
---
title: Kidney Tumor Disease Classification
emoji: 🔬
colorFrom: red
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
---

=======
>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426
# DEEP_Learning_Project1
# 🧠 Kidney Disease Classification using Deep Learning

> An end-to-end production-grade Deep Learning project for Kidney Disease Classification using TensorFlow, MLflow, DVC, Docker, AWS, and CI/CD pipelines.

---

# 🚀 Project Overview

This project demonstrates how to build, track, version, and deploy a real-world Deep Learning application using modern MLOps practices. The system classifies Kidney Disease images using a Convolutional Neural Network (CNN) and provides a complete machine learning lifecycle pipeline from data ingestion to cloud deployment.

The project follows modular coding architecture and industry-standard engineering practices used in production AI systems.

---

# ✨ Key Features

- 🔬 Deep Learning based medical image classification
- 🧱 Modular and scalable project architecture
- 📊 Experiment tracking using MLflow
- 🔁 Reproducible ML pipelines using DVC
- 🐳 Dockerized application
<<<<<<< HEAD
- ☁️ Deployment with Hugging Face Spaces
=======
- ☁️ AWS deployment with EC2 & ECR
>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426
- 🔄 CI/CD automation using GitHub Actions
- 🌐 Flask web application for predictions
- 📁 Configuration-driven pipeline
- ⚙️ End-to-end MLOps workflow

---

# 🏗️ Complete System Workflow

```text
Data Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Base Model Preparation
      ↓
Model Training
      ↓
Model Evaluation
      ↓
MLflow Experiment Tracking
      ↓
DVC Pipeline Versioning
      ↓
Docker Containerization
      ↓
AWS Deployment
      ↓
Flask Prediction Web App
```

---

# 📁 Project Structure

```text
Kidney-Disease-Classification-MLflow-DVC/
│
├── .github/
│   └── workflows/
│       └── main.yaml
│
├── config/
│   └── config.yaml
│
├── research/
│
├── src/
│   └── cnnClassifier/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
│
├── templates/
├── static/
├── artifacts/
├── logs/
│
├── app.py
├── main.py
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

---

# ⚙️ Tech Stack

## 🔹 Machine Learning
- TensorFlow
- Keras
- Scikit-learn
- NumPy
- Pandas

## 🔹 MLOps Tools
- MLflow
- DVC
- Docker
- GitHub Actions

## 🔹 Backend & Deployment
- Flask
<<<<<<< HEAD
- Hugging Face Spaces
=======
- AWS EC2
- AWS ECR
>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426

## 🔹 Utilities
- YAML
- Logging
- Python Box
- Joblib

---

# 🧪 MLflow Experiment Tracking

MLflow is used to:
- Track experiments
- Compare models
- Log metrics & parameters
- Store artifacts
- Version models

## Start MLflow UI

```bash
mlflow ui
```

Open browser:

```text
http://localhost:5000
```

---

# 🔁 DVC Pipeline Management

DVC is used for:
- Data versioning
- Pipeline orchestration
- Reproducible workflows

## Initialize DVC

```bash
dvc init
```

## Run Pipeline

```bash
dvc repro
```

## Visualize Pipeline DAG

```bash
dvc dag
```

---

# 🔧 Project Workflow

## 1️⃣ Update `config.yaml`
Stores all project configurations and paths.

## 2️⃣ Update `params.yaml`
Stores hyperparameters:
- IMAGE_SIZE
- BATCH_SIZE
- EPOCHS
- LEARNING_RATE

## 3️⃣ Update `secrets.yaml` *(Optional)*
Stores API keys and credentials.

## 4️⃣ Update Entity
Defines configuration schemas and data classes.

## 5️⃣ Update Configuration Manager
Handles centralized configuration management.

## 6️⃣ Update Components
Contains:
- Data Ingestion
- Validation
- Base Model
- Training
- Evaluation

## 7️⃣ Update Pipeline
Creates training & inference pipelines.

## 8️⃣ Update `main.py`
Runs all pipeline stages sequentially.

## 9️⃣ Update `dvc.yaml`
Defines DVC stages and dependencies.

## 🔟 Update `app.py`
Flask application for predictions.

---

# 🚀 How To Run The Project

## STEP 1 — Clone Repository

```bash
git clone https://github.com/M-AyyanAsif/DEEP_Learning_Project1/tree/main
```

```bash
cd Kidney-Disease-Classification-Deep-Learning-Project
```

---

## STEP 2 — Create Conda Environment

```bash
 python -m venv myenv
```

```bash
myenv/scripts/activate
```

---

## STEP 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## STEP 4 — Run Application

```bash
python app.py
```

Open browser:

```text
http://localhost:8080
```

---

# 🔐 MLflow + DagsHub Integration

## Set Environment Variables

### Windows CMD

```bash
set MLFLOW_TRACKING_URI=https://dagshub.com/stopmold8290/DEEP_Learning_Project1.mlflow/#/.mlflow

set MLFLOW_TRACKING_USERNAME=entbappy

set MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0
```

---


# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t kidney-classifier .
```

## Run Docker Container

```bash
docker run -p 8080:8080 kidney-classifier
```

---

# ☁️ AWS Deployment with GitHub Actions

## AWS Services Used

### EC2
Virtual machine hosting application.

### ECR
Stores Docker images.

---

# 🔑 IAM Policies Required

Attach:
- AmazonEC2FullAccess
- AmazonEC2ContainerRegistryFullAccess

---

# 🗂️ Create ECR Repository

Example:

```text
566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
```

---

# 🖥️ Setup EC2 Instance

Install Docker:

```bash
sudo apt-get update -y
```

```bash
sudo apt-get upgrade -y
```

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

```bash
sudo sh get-docker.sh
```

```bash
sudo usermod -aG docker ubuntu
```

```bash
newgrp docker
```

---

# 🔄 Configure GitHub Self Hosted Runner

Go to:

```text
GitHub Repository
→ Settings
→ Actions
→ Runners
→ New Self Hosted Runner
```

Run all commands provided by GitHub inside EC2 terminal.

---

# 🔐 GitHub Secrets

Add these secrets:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```

---

# 📊 MLflow Benefits

- Production-grade experiment tracking
- Parameter logging
- Metrics comparison
- Model registry
- Artifact storage

---

# 📈 DVC Benefits

- Lightweight pipeline orchestration
- Data version control
- Reproducible ML workflows
- Pipeline dependency tracking

---

# 🌐 Flask Application

The Flask web app allows users to:
- Upload Kidney images
- Run predictions
- View classification results

---

# 📌 Business Use Cases

- Early disease detection
- AI-assisted diagnostics
- Healthcare automation
- Medical imaging systems

---

# 🔮 Future Improvements

- Kubernetes deployment
- FastAPI backend
- Real-time monitoring
- Model drift detection
- Automated retraining
- Multi-model serving
- Cloud scalability

---

# 👨‍💻 Author

Developed as a complete end-to-end MLOps Deep Learning project demonstrating production-level architecture, deployment, automation, and experiment tracking.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and support the project.
