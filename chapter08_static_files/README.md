# Chapter 08 - Static Files in Flask (Day 23)

## Overview

This chapter introduces serving static files in Flask applications such as text files, CSS, images, and JavaScript.

---

## Concepts Covered

* Static File Serving
* Flask Static Folder
* Public Asset Access
* Frontend Resource Handling

---

## Folder Structure

```bash
chapter08_static_files/
│
├── app/
│   ├── static/
│   │   └── sample.txt
│
├── run.py
└── README.md
```

---

## Static URL Example

```text
http://127.0.0.1:5000/static/sample.txt
```

---

## Run Project

```bash
python run.py
```

---

## Learning Outcome

* Serve static files in Flask
* Understand frontend asset management
* Work with public resource URLs

---

## Progress

Completed:

* Day 23

Next:

* Day 24 - HTML Templates in Flask

# Day 23 Theory - Static Files in Flask

## What are Static Files

Static files are resources served directly without backend processing.

Examples:

* CSS
* Images
* JavaScript
* Text Files

---

## Flask Static Folder

Flask automatically exposes:

```text
/static
```

directory to the browser.

---

## Why Static Files Matter

Frontend applications need:

* Styling
* Images
* Client-side scripts

Without static file support, frontend integration is incomplete.

---

## Real World Usage

Static folders are heavily used in:

* Portfolio websites
* Dashboards
* Admin panels
* Full stack applications
