#  Chapter 03 - Project Structure (Day 7–9)

##  Overview
This chapter focuses on building scalable Flask applications with clean architecture, environment configuration, and production-ready practices.

---

## Concepts Covered

### 🔹 Day 7
- App Factory Pattern
- Modular folder structure
- Blueprint organization

### 🔹 Day 8
- Environment variables
- `.env` usage
- Config management

### 🔹 Day 9
- Global error handling
- Logging system
- Middleware (request lifecycle hooks)

---

##  Project Structure


---

##  API Endpoints

| Method | Endpoint        | Description      |
|--------|----------------|------------------|
| GET    | /health        | Health check     |
| GET    | /api/users/    | Get users        |
| POST   | /api/users/    | Create user      |

---

##  Run Project

```bash
python run.py

1. Global Error Handling
@app.errorhandler(404)

Handles errors centrally

2. Logging
logger.info(...)

Tracks requests & responses
Used in debugging & monitoring

3. Middleware Concept
@app.before_request
@app.after_request

Runs before/after every request
Used for:

Logging
Auth
Tracking
4. Clean Error Responses

Instead of crash:

{
  "success": false,
  "error": "Route not found"
}
6. Test

Try invalid route:

http://127.0.0.1:5000/invalid

 You should get clean 404 response