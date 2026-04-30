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


# 📘 Chapter 05 — Full CRUD Operations (Day 16)

## 📌 Overview
This chapter extends the Flask SQLAlchemy app by implementing full CRUD functionality including Update and Delete operations.

---

## 🚀 Concepts Covered

- Fetching records by ID
- Updating database rows
- Deleting records
- Edit forms with pre-filled data
- 404 handling with get_or_404

---

## 📁 New Files

```bash
templates/edit_user.html
``` id="t1sy3r"

---

## 🎯 Learning Outcome

- Perform full CRUD in Flask  
- Edit records via HTML forms  
- Delete database entries  
- Handle missing records safely  

---

## 📅 Progress

- ✅ Day 16 Completed  
- ⏳ Day 17 Next (Validation + Flash + Better CRUD UX)


📘 Theory / Explanation
🔥 Update Operation
user.name = request.form.get("name")

Updates DB row fields.

🔥 Delete Operation
db.session.delete(user)

Marks record for deletion.

🔥 Commit Changes
db.session.commit()

Persists DB modifications.

🔥 get_or_404()
User.query.get_or_404(user_id)

Automatically returns 404 page if record not found.