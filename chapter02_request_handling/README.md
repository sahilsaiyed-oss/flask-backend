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


### 🔹 Day 6
- Centralized Validation
- Reusable Utility Functions
- Error Handling Improvements
- Clean Backend Architecture

 1. Centralized Validation

Before:

validation inside route 

Now:

validate_user_data(data) 
 Cleaner + reusable

 2. Multiple Error Handling
errors = []
errors.append(...)

 Return all errors at once (real-world practice)

 3. Separation of Concerns
routes → API logic
utils → reusable logic

 THIS is what companies expect

 4. Update vs Create Validation
is_update=True

 Smart backend design

 5. GET Single Resource
GET /api/users/1

 Important REST concept

3. Test Important APIs
GET    /api/users/
GET    /api/users/1
POST   /api/users/
PUT    /api/users/1
DELETE /api/users/1