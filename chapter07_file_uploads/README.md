# Chapter 07 - File Uploads in Flask (Day 22)

## Overview

This chapter introduces file upload handling in Flask applications using multipart form data and secure file saving.

---

## Concepts Covered

* File Upload APIs
* Multipart Form Data
* request.files
* secure_filename()
* File Storage Handling

---

## Folder Structure

```bash
chapter07_file_uploads/
│
├── app/
│   ├── routes/
│   │   └── upload_routes.py
│
├── uploads/
├── run.py
└── README.md
```

---

## API Endpoint

| Method | Endpoint      | Description |
| ------ | ------------- | ----------- |
| POST   | /files/upload | Upload File |

---

## Run Project

```bash
python run.py
```

---

## Learning Outcome

* Handle file uploads in Flask
* Save files securely
* Process multipart form requests
* Build upload APIs for backend systems

---

## Progress

Completed:

* Day 22

Next:

* Day 23 - Static Files in Flask

# Day 22 Theory - File Uploads in Flask

## What is request.files

```python
request.files
```

Used to access uploaded files from incoming HTTP requests.

---

## Why secure_filename()

```python
secure_filename(file.filename)
```

Protects the server from malicious filenames and unsafe paths.

Example:

Unsafe:

```text
../../../system32/file.exe
```

Safe:

```text
file.exe
```

---

## Why File Uploads Matter

Used in:

* Profile image systems
* Resume upload portals
* Document management systems
* Admin dashboards

---

## Multipart Form Data

File uploads use:

```http
multipart/form-data
```

instead of JSON.

This allows binary files to be transferred through HTTP requests.

