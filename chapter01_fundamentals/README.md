#  Chapter 01 - Flask Fundamentals (Day 1)

##  Overview
This chapter introduces the basics of Flask and setting up a simple backend application.

---

##  Concepts Covered
- Flask App Initialization
- Routing
- JSON Responses
- Dynamic Routes
- Basic Config Setup

---

##  API Endpoints

| Method | Endpoint       | Description        |
|--------|--------------|--------------------|
| GET    | /            | Home route         |
| GET    | /health      | Health check       |
| GET    | /user/<name> | Dynamic greeting   |

---

## How to Run

```bash
pip install -r requirements.txt
python app.py

### 🔹 Day 2
- Blueprints (Modular Routing)
- Clean Project Structure
- Standard API Response Format
- Input Validation
- HTTP Status Codes


---

## 🔗 API Endpoints

| Method | Endpoint              | Description              |
|--------|----------------------|--------------------------|
| GET    | /                    | Home route               |
| GET    | /health              | Health check             |
| GET    | /user/<name>         | Dynamic greeting         |
| GET    | /about               | Project information      |

---

## 📤 Response Format (Standardized)

### ✅ Success Response
```json
{
  "success": true,
  "message": "Request successful",
  "data": {}
}

pip install -r requirements.txt
python app.py