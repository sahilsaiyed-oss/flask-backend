# 📘 Chapter 06 — REST API CRUD Endpoints (Day 20)

## 📌 Overview
Converted the Flask CRUD application into a RESTful JSON API by exposing CRUD operations through API endpoints.

---

## 🚀 Concepts Covered

- REST API Design
- JSON Responses with jsonify
- HTTP Methods (GET, POST, PUT, DELETE)
- API Blueprint Separation

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/users | Get All Users |
| GET | /api/users/<id> | Get Single User |
| POST | /api/users | Create User |
| PUT | /api/users/<id> | Update User |
| DELETE | /api/users/<id> | Delete User |

---

## 🎯 Learning Outcome

- Build REST APIs in Flask  
- Return JSON Responses  
- Structure Backend for Frontend Consumption  

---

## 📅 Progress

- ✅ Day 20 Completed  
- ⏳ Day 21 Next (API Validation + Error Handling)

🧪 3. Test Endpoints
Get All Users
GET /api/users
Get Single User
GET /api/users/1
Create User
POST /api/users
Content-Type: application/json

{
    "name": "Rahul",
    "email": "rahul@gmail.com"
}
Update User
PUT /api/users/1
Delete User
DELETE /api/users/1
📘 Theory / Explanation
🔥 What is REST API?

REST API = Backend endpoints returning JSON instead of HTML

Used by:

React Frontend
Mobile Apps
External Clients
Microservices
🔥 Why Separate API & Web Routes?

Professional apps often have:

web_routes.py → HTML Pages
api_routes.py → JSON APIs

This separation improves:

Maintainability
Scalability
Frontend/Backend decoupling
🔥 jsonify()
return jsonify({...})

Converts Python dict/list → JSON response.

🔥 HTTP Methods
Method	Purpose
GET	Fetch Data
POST	Create Data
PUT	Update Data
DELETE	Remove Data