# Chapter 04 - Templates & Frontend Integration (Day 10)

##  Overview
This chapter introduces Flask templates and frontend integration, allowing backend data to be displayed in HTML pages.

---

##  Concepts Covered

- Flask Templates (Jinja2)
- Rendering HTML pages
- Passing data from backend to frontend
- Basic UI integration

---


---

## Routes

| Route        | Description        |
|--------------|--------------------|
| /            | Home page          |
| /users       | User list (HTML)   |
| /api/users   | JSON API           |

---

##  Run Project

```bash
python run.py

1. Templates (Jinja2)
render_template("index.html")

 Flask renders HTML files from /templates

 2. Passing Data to HTML
render_template("users.html", users=users)

 Sends Python data → HTML

 3. Jinja Loop
{% for user in users %}

 Loop through backend data

 4. Separation of API & UI
/api/users → JSON API
/users → HTML UI

 This is real architecture

 5. Blueprints
user_bp → API
web_bp → frontend routes

 Clean separation


  (Day 11)

##  Overview
This chapter extends frontend integration by adding HTML forms and handling POST requests from the browser.

---

##  Concepts Covered

- HTML Forms
- POST requests from frontend
- Handling form data in Flask
- Redirect after form submission

---

##  Routes

| Route       | Description        |
|-------------|--------------------|
| /           | Home page          |
| /users      | User list          |
| /add-user   | Add user form      |

---

##  Run Project

```bash
python run.py
 Learning Outcome
Build forms in HTML
Send POST requests from frontend
Handle form data in Flask
Understand full request-response cycle