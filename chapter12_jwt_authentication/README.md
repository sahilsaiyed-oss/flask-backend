# Chapter 12 - JWT Authentication and Protected Routes (Day 27)

## Overview

This chapter introduces JWT-based authentication systems in Flask applications for securing APIs and protecting backend routes.

---

## Concepts Covered

* JWT Authentication
* Access Tokens
* Protected Routes
* User Identity Verification
* Authorization Headers

---

## Folder Structure

```bash id="d8v6zy"
chapter12_jwt_authentication/
│
├── app/
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── protected_routes.py
│   ├── models.py
│   ├── __init__.py
│
├── config.py
├── run.py
└── README.md
```

---

## API Endpoints

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| POST   | /auth/register | Register User        |
| POST   | /auth/login    | Login User           |
| GET    | /api/profile   | Protected User Route |

---

## Run Project

```bash id="4vjlwm"
python run.py
```

---

## Learning Outcome

* Build JWT authentication systems
* Generate access tokens
* Protect backend routes
* Verify authenticated users
* Secure Flask APIs

---

## Progress

Completed:

* Day 27

Next:

* Day 28 - Role Based Authorization System

# Day 27 Theory - JWT Authentication and Protected Routes

## What is JWT

JWT stands for JSON Web Token.

It is used for:

* User authentication
* API security
* Protected backend systems

---

## Why JWT is Important

Traditional session-based authentication stores session data on the server.

JWT stores authentication data inside tokens.

Benefits:

* Stateless authentication
* Scalable APIs
* Faster backend systems
* Used in modern web applications

---

## What is create_access_token()

```python id="3z7upm"
create_access_token(identity=user.id)
```

Generates a secure JWT token containing user identity information.

---

## What is @jwt_required()

```python id="3f3ex8"
@jwt_required()
```

Protects routes from unauthorized access.

Only users with valid JWT tokens can access protected endpoints.

---

## What is get_jwt_identity()

```python id="qs1m7w"
get_jwt_identity()
```

Extracts logged-in user information from the JWT token.

---

## Authorization Header

Protected routes require:

```http id="m7e9zy"
Authorization: Bearer TOKEN
```

Without a valid token:

* Access is denied
* Server returns Unauthorized response

---

## Real World Usage

JWT authentication is used in:

* Banking applications
* E-commerce systems
* Admin dashboards
* Mobile applications
* REST APIs

It is one of the most important concepts in backend development.
