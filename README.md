# Product Catalog Service

**Student Name:** Trhas Weldu  
**Project Title:** Product Catalog Service  -Complete CRUD API
**Deployment Platform:** Render  
**Course:** Advanced Software Engineering  

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [System Requirements](#2-system-requirements)
3. [Project Structure](#3-project-structure)
4. [Installation and Local Setup](#4-installation-and-local-setup)

5. [ API Endpoints](#5-API-Endpoint)

6. [Testing](#6-Testing)
7. [Docker Containerization](#7-docker-containerization)
8. [Deployment to Render](#8-deployment-to-render)
9. [Conclusion](#9-conclusion)
10. [References](#10-references)

---

## 1. Introduction

This project implements a **complete CRUD (Create, Read, Update, Delete) Product Catalog Web Service** using the Flask web framework in Python.  
The service provides RESTful API endpoints that allow users to:

- ✅ **Create** new products (POST)
- ✅ **Read** product information (GET) 
- ✅ **Update** existing products (PUT)
- ✅ **Delete** products (DELETE)
- Check system health status

This project demonstrates core concepts in REST API development, containerization, testing, and version control.

---

## 2. System Requirements

| Requirement | Version / Description |
|-------------|------------------------|
| Python | 3.9 |
| Flask | 2.3 |
| Requests | 2.31 (for testing) |
| Git | Latest version |
| Docker Desktop | Latest version |
| Operating System | Windows 10 |

---

## 3. Project Structure


product-catalog-project/

│

├── app.py # Main Flask application with CRUD endpoints

├── requirements.txt # Python dependencies

├── Dockerfile # Container configuration

├── test_basic.py # Comprehensive test suite

├── .dockerignore # Docker build exclusions

└── README.md # Project documentation


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


## 5. API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/` | GET | Returns service information |
| `/health` | GET | Returns service health check |
| `/products` | GET | Returns list of all products |
| `/products/<id>` | GET | Returns product details by ID |
| `/products` | POST | Creates a new product |
| `/products/<id>` | PUT | Update existing product|
| `/products/<id>` | DELETE | Delete product|

### Example Create Product Request
curl -X POST http://127.0.0.1:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Smartphone", "price":699.99, "category":"Electronics"}'
  ### Example Update Product (PUT)
curl -X PUT http://127.0.0.1:5000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Gaming Laptop", "price":1299.99}'
### Example Delete Product 
curl -X DELETE http://127.0.0.1:5000/products/1

---
## 6. Testing
### Run Comprehensive Test Suite

pip install requests

python test_basic.py

Test Output Includes:
✅ Health endpoint verification

✅ GET all products

✅ GET single product

✅ POST - Create new product

✅ PUT - Update product

✅ DELETE - Remove product

✅ Error handling (404, 400)

✅ Input validation

### Expected Test Result:

✅ ALL TESTS PASSED!
✅ POST, GET, PUT, DELETE all working perfectly!
✅ No crashes - All response formats match!
---
## 7. Docker Containerization

### Build Docker Image
docker build -t product-service .

### Run Docker Container
docker run -p 5000:5000 product-service

### Test Service
Open browser:
http://127.0.0.1:5000/health

http://127.0.0.1:5000/products

---


## 8. Deployment to Render

1. Push project to GitHub:

git add .

git commit -m "Complete CRUD implementation with testing"

git push origin main

2. Open https://render.com  
3. Select **New → Web Service**  
4. Connect GitHub repository  
5. Select **Docker** deployment  
6. Deploy service and wait for build completion  
7. Test using the live Render URL

---

## 9. Conclusion

This project successfully demonstrates:

✅ Complete CRUD Operations - All 4 HTTP methods implemented

✅ RESTful API Design - Proper endpoints and status codes

✅ Comprehensive Testing - Automated test suite with 100% pass rate

✅ Input Validation - Error handling for invalid requests

✅ Containerization - Docker deployment ready

✅ Version Control - GitHub repository management

The implementation proves all required HTTP methods (GET, POST, PUT, DELETE) are fully functional with proper error handling and validation.


---

## 10. References

- Flask Documentation: https://flask.palletsprojects.com/
- Docker Documentation: https://docs.docker.com/
- Render Deployment Guide: https://render.com/docs
