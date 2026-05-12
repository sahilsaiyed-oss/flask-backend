# Chapter 11 - Flask Authentication System (Day 26)

## Overview

This chapter introduces authentication systems in Flask applications using user registration, login APIs, password hashing, and database validation.

---

## Concepts Covered

* User Authentication
* Registration APIs
* Login APIs
* Password Hashing with bcrypt
* Database Validation

---

## Folder Structure

```bash
chapter11_authentication/
│
├── app/
│   ├── routes/
│   │   └── auth_routes.py
│   ├── models.py
│   ├── __init__.py
│
├── config.py
├── run.py
└── README.md
```

---

## API Endpoints

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /auth/register | Register User |
| POST   | /auth/login    | Login User    |

---

## Run Project

```bash
python run.py
```

---

## Learning Outcome

* Build authentication APIs
* Hash passwords securely
* Validate users from database
* Create production-style login systems

---

## Progress

Completed:

* Day 26

Next:

* Day 27 - JWT Authentication and Protected Routes
