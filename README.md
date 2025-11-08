# Product Catalog Service

**Student Name:** Trhas Weldu  
**Project Title:** Product Catalog Service  
**Deployment Platform:** Render  
**Course:** Advanced Software Engineering  

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [System Requirements](#2-system-requirements)
3. [Project Structure](#3-project-structure)
4. [Installation and Local Setup](#4-installation-and-local-setup)
5. [API Endpoints](#5-api-endpoints)
6. [Docker Containerization](#6-docker-containerization)
7. [Deployment to Render](#7-deployment-to-render)
8. [Conclusion](#8-conclusion)
9. [References](#9-references)

---

## 1. Introduction

This project implements a Product Catalog Web Service using the Flask web framework in Python.  
The service provides RESTful API endpoints that allow users to:

- Retrieve information about the service
- Check system health status
- View all available products
- Retrieve details for a specific product
- Add a new product entry

This project demonstrates core concepts in web service development, containerization, and cloud deployment.

---

## 2. System Requirements

| Requirement | Version / Description |
|------------|------------------------|
| Python | 3.9  |
| Flask | 2.3+ |
| Git | Latest version |
| Docker Desktop | Latest version |
| Render Account | For cloud deployment |
| Operating System | Windows 10|

---

## 3. Project Structure

project-folder/
│
├── app.py
├── requirements.txt
├── Dockerfile
├──test_basic.py
├── .dockerignore
└── README.md

---

## 4. Installation and Local Setup

### Step 1: Create Virtual Environment
python -m venv venv

### Step 2: Activate Environment
**Windows**
venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Run Application
python app.py

### Step 5: Open in Browser
http://127.0.0.1:5000/health

---
### step 6: Test Simple Test Script

pip install requests

python test_basic.py

## 5. API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/` | GET | Returns service information |
| `/health` | GET | Returns service health check |
| `/products` | GET | Returns list of all products |
| `/products/<id>` | GET | Returns product details by ID |
| `/products` | POST | Creates a new product |

### Example Create Product Request
curl -X POST http://127.0.0.1:5000/products
 ^
-H "Content-Type: application/json" ^
-d "{"name":"Phone","price":499.99}"

---

## 6. Docker Containerization

### Build Docker Image
docker build -t product-service .

### Run Docker Container
docker run -p 5000:5000 product-service

### Test Service
Open browser:
http://127.0.0.1:5000/products

---


## 7. Deployment to Render

1. Push project to GitHub:
git add .
git commit -m "Initial Commit"
git branch -M main
git push -u origin main

2. Open https://render.com  
3. Select **New → Web Service**  
4. Connect GitHub repository  
5. Select **Docker** deployment  
6. Deploy service and wait for build completion  
7. Test using the live Render URL

---

## 8. Conclusion

This project enabled practical learning in REST API development, Python application setup, containerization with Docker, and deployment using Render. It demonstrates the essential skills required to develop and deploy modern cloud-based backend services.

---

## 9. References

- Flask Documentation: https://flask.palletsprojects.com/
- Docker Documentation: https://docs.docker.com/
- Render Deployment Guide: https://render.com/docs
