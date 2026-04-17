# 📘 Chapter 02 - Request Handling (Day 4)

##  Overview
This chapter focuses on handling client requests in Flask, especially working with POST requests and JSON data.

---

##  Concepts Covered

###  1. HTTP Methods
- GET → Fetch data
- POST → Send data
- PUT → Update data
- DELETE → Remove data

---

###  2. Request Body (JSON)
Flask allows reading JSON data sent by client using:

```python
request.get_json()