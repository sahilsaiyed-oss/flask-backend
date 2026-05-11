# Chapter 09 - HTML Templates in Flask (Day 24)

## Overview

This chapter introduces HTML template rendering in Flask using Jinja2 templates.

---

## Concepts Covered

* Jinja2 Templates
* render_template()
* Dynamic HTML Rendering
* Backend to Frontend Data Passing

---

## Folder Structure

```bash
chapter09_templates/
│
├── app/
│   ├── templates/
│   │   └── index.html
│
├── run.py
└── README.md
```

---

## Route

| Route | Description          |
| ----- | -------------------- |
| /     | Render HTML Template |

---

## Run Project

```bash
python run.py
```

---

## Learning Outcome

* Render HTML pages from Flask
* Pass dynamic data to frontend
* Build backend-driven UI systems

---

## Progress

Completed:

* Day 24

Next:

* Day 25 - Custom Error Handlers
# Day 24 Theory - HTML Templates in Flask

## What is render_template()

```python
render_template("index.html")
```

Used to render HTML files from the templates folder.

---

## What is Jinja2

Jinja2 is Flask’s template engine.

Allows:

* Variables
* Loops
* Conditions
* Dynamic HTML rendering

Example:

```html
{{ name }}
```

---

## Passing Backend Data to HTML

```python
return render_template(
    "index.html",
    name="Sahil"
)
```

Backend data becomes accessible inside HTML templates.

---

## Why Templates Matter

Templates allow Flask to:

* Build frontend pages
* Create dashboards
* Render dynamic UI content

This is foundational for full stack development.
