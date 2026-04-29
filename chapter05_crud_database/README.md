#  Chapter 05 — Database Setup with Flask SQLAlchemy (Day 15)

##  Overview
This chapter introduces database integration using Flask SQLAlchemy and SQLite to persist application data.

---

##  Concepts Covered

- Flask SQLAlchemy Setup
- SQLite Database Configuration
- ORM Concepts
- Creating Models
- Auto Table Creation

---

##  Project Structure

```bash
chapter05_crud_database/
│
├── app/
│   ├── models.py
│   ├── routes/
│   └── templates/
│
├── config.py
├── run.py
``` id="k4ho8v"

---

##  Learning Outcome

- Connect Flask to SQLite  
- Define ORM Models  
- Persist Data in Database  
- Build Real CRUD Foundations  

---

##  Progress

-  Day 15 Completed  
-  Day 16 Next (Read + Update + Delete Operations)

Theory / Explanation
 Why Database Instead of Python List?

Python list:

Resets every restart
Not scalable
Temporary only

Database:

Permanent storage
Real-world backend approach
Query / Filter / Update support
 What is SQLAlchemy?

ORM = Object Relational Mapper

Instead of writing SQL manually:

INSERT INTO users ...

You write Python:

User(name="Sahil")
 What is db.create_all()?

Creates all tables based on models automatically.

 What is a Model?
class User(db.Model)

Represents database table structure.