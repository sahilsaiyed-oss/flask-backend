# 📘 Chapter 02 - Request Handling (Day 4–5)

##  Overview
This chapter focuses on handling client requests and building a complete CRUD API using Flask.

---

##  Concepts Covered

### 🔹 Day 4
- HTTP Methods (GET, POST)
- JSON Request Handling
- Input Validation
- Status Codes

### 🔹 Day 5
- PUT (Update Data)
- DELETE (Remove Data)
- In-memory Database
- CRUD Operations

---

##  Project Structure
chapter02_request_handling/
│
├── app.py
├── config.py
├── routes/
│ └── user_routes.py
├── utils/
│ └── response.py
└── README.md


---

##  API Endpoints

| Method | Endpoint              | Description        |
|--------|----------------------|--------------------|
| GET    | /api/users/          | Get all users      |
| POST   | /api/users/          | Create user        |
| PUT    | /api/users/<id>      | Update user        |
| DELETE | /api/users/<id>      | Delete user        |

---

##  Key Concepts

- CRUD Operations  
- REST API Design  
- Request Body Handling  
- Input Validation  
- Error Handling  

---

##  Run Project

```bash
pip install -r requirements.txt
python app.py

theory explanation 
1. PUT Method (Update)
methods=["PUT"]

 Used to update existing data

 2. DELETE Method
methods=["DELETE"]

 Used to remove data

 3. In-Memory Database
users = []

 Temporary storage (used before real DB)

 4. CRUD Operations (VERY IMPORTANT)
Operation	Method	Meaning
Create	POST	Add data
Read	GET	Fetch data
Update	PUT	Modify data
Delete	DELETE	Remove data

 Interview must-know concept

 5. Partial Update
data.get("name", user["name"])

 Only update if value provided

 6. 404 Handling
return error_response("User not found", 404)