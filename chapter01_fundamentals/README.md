# 📘 Chapter 01 - Flask Fundamentals (Day 1–3)

##  Overview
This chapter builds a strong foundation in Flask by covering core backend concepts such as routing, modular structure, API design, and request handling.

By the end of this chapter, we move from a basic Flask app to a **structured, production-style backend service**.

---

##  What We Learned

### 🔹 Day 1: Flask Basics
- Flask App Initialization
- App Factory Pattern (`create_app`)
- Basic Routing
- JSON Responses using `jsonify`
- Dynamic Routes
- Config Separation (`config.py`)

---

### 🔹 Day 2: Modular Backend Structure
- Blueprints for route organization
- Clean folder structure
- Custom API response format
- Utility functions (`utils/response.py`)
- Input validation basics
- HTTP status codes

---

### 🔹 Day 3: Real API Behavior
- Query Parameters (`request.args`)
- Data type conversion (string → int/float)
- Advanced validation
- Error handling using `try-except`
- Building realistic API endpoints

---

##  Project Structure

chapter01_fundamentals/
│
├── app.py
├── config.py
├── routes/
│ ├── init.py
│ └── main_routes.py
├── utils/
│ └── response.py
├── requirements.txt
└── README.md


---

##  API Endpoints

| Method | Endpoint                          | Description                  |
|--------|----------------------------------|------------------------------|
| GET    | /                                | Home route                   |
| GET    | /health                          | Health check                 |
| GET    | /user/<name>                     | Dynamic greeting             |
| GET    | /about                           | Project information          |
| GET    | /search?name=sahil&age=20        | Query parameter example      |
| GET    | /calculate?num1=10&num2=5        | Addition API                 |

---

## Standard API Response Format

###  Success Response
```json
{
  "success": true,
  "message": "Request successful",
  "data": {}
}
 Error Response
{
  "success": false,
  "error": "Something went wrong"
}
▶ How to Run
pip install -r requirements.txt
python app.py
 Key Concepts Covered
Flask App Factory Pattern → Scalable app creation
Blueprints → Modular and maintainable routing
Custom Response Handling → Consistent API design
Query Parameters → Handling dynamic user input
Validation & Error Handling → Building robust APIs
Status Codes → Communicating API responses effectively
 Practice Tasks
1. Square API
GET /square/<int:number>
2. Multiply API
GET /multiply?num1=5&num2=3
