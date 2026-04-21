# 📘 Chapter 03 - Project Structure (Day 7–8)

##  Overview
This chapter focuses on building scalable Flask applications with proper project structure and environment-based configuration.

---

##  Concepts Covered

### 🔹 Day 7
- App Factory Pattern
- Modular folder structure
- Blueprint organization

### 🔹 Day 8
- Environment variables
- `.env` file usage
- Config classes (dev/prod)
- Secure configuration handling


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
pip install -r requirements.txt
python run.py

1. Environment Variables
SECRET_KEY=...

Used to store sensitive data

2. .env File
Keeps secrets outside code
Used in real production apps
3. Config Classes
DevelopmentConfig
ProductionConfig

Different settings for different environments

4. python-dotenv
load_dotenv()

Loads .env variables

5. Environment Switching
FLASK_ENV=development

Controls behavior of app

7. Run Project
python run.py