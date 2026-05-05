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

# 📘 Chapter 05 — CRUD Validation & UX Improvements (Day 17)

## 📌 Overview
Enhanced the CRUD application with validation, flash messaging, and better user interaction patterns.

---

## 🚀 Concepts Covered

- Duplicate Email Validation
- Flash Success/Error Messages
- Delete Confirmation Popup
- Safe Update Validation

---

## 🎯 Learning Outcome

- Prevent duplicate DB entries  
- Improve CRUD user experience  
- Build production-like validation flow  

---

## 📅 Progress

- ✅ Day 17 Completed  
- ⏳ Day 18 Next (Search / Filter / Query Features)

📘 Theory / Explanation
🔥 Duplicate Validation
User.query.filter_by(email=email).first()

Checks if email already exists.

🔥 Excluding Current User in Update
User.id != user_id

Prevents false duplicate when user keeps same email.

🔥 Flash Messages

Used for:

Success feedback
Error notifications
Better UX
🔥 Delete Confirmation
onclick="return confirm(...)"

Browser popup before delete.


# 📘 Chapter 05 — Search & Filter Users (Day 18)

## 📌 Overview
Added search functionality to the CRUD dashboard for filtering users dynamically by name or email.

---

## 🚀 Concepts Covered

- Query Parameters
- Search Forms
- SQLAlchemy Filtering
- Case-Insensitive Search

---

## 🎯 Learning Outcome

- Read URL Query Parameters  
- Filter DB Results Dynamically  
- Build Searchable Admin Interfaces  

---

## 📅 Progress

- ✅ Day 18 Completed  
- ⏳ Day 19 Next (Sorting + Pagination)

🧪 3. Test Search

Try:

http://127.0.0.1:5000/?search=sahil
📘 Theory / Explanation
🔥 Query Parameters
request.args.get("search")

Reads URL params like:

/?search=sahil
🔥 SQL ILIKE
User.name.ilike(...)

Case-insensitive search.

🔥 Multi-Field Filter
(User.name.ilike(...)) | (User.email.ilike(...))

Searches across:

Name
Email
🔥 Why This Matters

Real dashboards need:

Search
Filters
Query params

This is standard admin panel functionality.

# 📘 Chapter 05 — Sorting & Pagination (Day 19)

## 📌 Overview
Enhanced the CRUD system with sorting and pagination to efficiently manage large datasets.

---

## 🚀 Concepts Covered

- Pagination using SQLAlchemy
- Sorting query results
- Query parameters (page, sort)
- Efficient data loading

---

## 🎯 Learning Outcome

- Implement pagination in Flask  
- Sort database results dynamically  
- Build scalable backend APIs  

---

## 📅 Progress

- ✅ Day 19 Completed  
- ⏳ Day 20 Next (API version of CRUD)

🧪 3. Test URLs
Pagination
/?page=2
Sorting
/?sort=desc
Combined
/?search=sahil&sort=asc&page=1
📘 Theory / Explanation
🔥 Pagination
query.paginate(page=page, per_page=3)

Returns:

items
page
pages
has_next
has_prev
🔥 Sorting
User.name.asc()
User.name.desc()

Controls order of results.

🔥 Query Parameters
request.args.get("page")

Reads from URL:

?page=2
🔥 Why This Matters

Real systems NEVER:
❌ load all data at once

They always:
✅ paginate
✅ filter
✅ sort