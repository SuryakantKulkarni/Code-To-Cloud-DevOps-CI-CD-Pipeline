<!-- ================= HEADER ================= -->

<h1 align="center">🚀 DevOps CI/CD Pipeline Project</h1>

<p align="center">
  <b>Automated Build • Containerized Deployment • Cloud Hosting</b><br>
  <i>End-to-End DevOps workflow simulating real production systems</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CI/CD-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white"/>
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cloud-AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
</p>

---

## 🌟 Overview

This project demonstrates a **complete DevOps pipeline** that automates:

* Code integration
* Docker image build
* Image storage in registry
* Cloud deployment

It replicates how modern applications are delivered in production environments.

---

## 🧠 Architecture

```text
Developer → GitHub → GitHub Actions (CI/CD)
           ↓
      Docker Image Build
           ↓
      Docker Hub (Registry)
           ↓
        AWS EC2 Instance
           ↓
     Running Container (Live App)
```

---

## ⚙️ Tech Stack

| Category         | Tools          |
| ---------------- | -------------- |
| Version Control  | GitHub         |
| CI/CD            | GitHub Actions |
| Containerization | Docker         |
| Registry         | Docker Hub     |
| Cloud            | AWS EC2        |
| Backend          | Flask (Python) |
| UI               | HTML, CSS      |

---

## 🔄 Workflow

```text
1. Code pushed to GitHub
2. CI/CD pipeline triggered
3. Docker image built
4. Image pushed to Docker Hub
5. EC2 pulls latest image
6. Container runs application
```

---

## 🌍 Live Application

👉 http://YOUR_EC2_PUBLIC_IP:5000

---

## 📸 Screenshots

### 🚀 Application UI

<p align="center">
  <img src="screenshots/app.png" width="700"/>
</p>

---

### ⚙️ CI/CD Pipeline

<p align="center">
  <img src="screenshots/github-actions.png" width="700"/>
</p>

---

### 🐳 Docker Build

<p align="center">
  <img src="screenshots/docker.png" width="700"/>
</p>

---

### ☁️ Deployed Application

<p align="center">
  <img src="screenshots/ec2-live.png" width="700"/>
</p>

---

## 📂 Project Structure

```text
DevOps-Project/
│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── docker/
│   └── Dockerfile
│
├── .github/workflows/
│   └── docker.yml
│
├── requirements.txt
├── screenshots/
└── README.md
```

---

## 🐳 Docker Usage

```bash
docker build -t devops-app -f docker/Dockerfile .
docker run -d -p 5000:5000 devops-app
```

---

## 🛠️ Implementation Steps (Quick Guide)

1. Create Flask application
2. Push code to GitHub
3. Create Dockerfile
4. Setup GitHub Actions CI/CD
5. Push Docker image to Docker Hub
6. Deploy container on AWS EC2

---

## 🎯 Key Features

* 🚀 Automated CI/CD pipeline
* 🐳 Dockerized application
* ☁️ Cloud deployment
* 🔄 End-to-end workflow automation
* 🎨 Clean UI interface

---

## 🧠 Key Learnings

* CI/CD pipeline design
* Docker containerization
* Cloud deployment using AWS
* Debugging real-world issues
* DevOps project structuring

---

## 🚀 Future Improvements

* Kubernetes deployment
* Auto-deployment using SSH
* Load balancing
* HTTPS + domain
* Monitoring integration

---

## 👨‍💻 Author

**Suryakant Kulkarni**
🔗 https://www.linkedin.com/in/suryakantkulkarni

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
