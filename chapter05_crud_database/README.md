# Chapter 05 - CRUD Operations and Database Integration

## Overview

This chapter focuses on building a production-style CRUD application in Flask using SQLite and Flask SQLAlchemy.
Across Day 15 to Day 19, the application evolves from basic database integration into a feature-rich admin dashboard with validation, search, sorting, and pagination.

---

## Project Structure

```bash
chapter05_crud_database/
│
├── app/
│   ├── models.py
│   ├── routes/
│   │   └── user_routes.py
│   ├── templates/
│   │   ├── users.html
│   │   └── edit_user.html
│
├── config.py
├── run.py
└── README.md
```

---

## Day 15 - Database Setup with Flask SQLAlchemy

### Work Completed

* Configured SQLite database connection
* Integrated Flask SQLAlchemy
* Created User model
* Implemented automatic table creation
* Replaced temporary Python list storage with database persistence

### Concepts Covered

* Flask SQLAlchemy Setup
* SQLite Configuration
* ORM Basics
* Models and Tables
* Database Initialization

### Code Explanation

#### Why Database Instead of Python List

Python lists:

* Reset on every server restart
* Store temporary data only
* Not suitable for real applications

Databases:

* Persist data permanently
* Support filtering and querying
* Used in real-world backend systems

#### What is SQLAlchemy

SQLAlchemy is an ORM (Object Relational Mapper).

Instead of writing raw SQL:

```sql
INSERT INTO users VALUES (...)
```

You write Python:

```python
User(name="Sahil", email="sahil@gmail.com")
```

#### What is db.create_all()

```python
db.create_all()
```

Automatically creates database tables based on defined models.

#### What is a Model

```python
class User(db.Model)
```

Represents a database table structure in Python.

---

## Day 16 - Full CRUD Operations

### Work Completed

* Added Update User functionality
* Added Delete User functionality
* Built Edit User Form
* Implemented record fetching by ID
* Added 404 handling for invalid records

### Concepts Covered

* Read Single Record
* Update Operation
* Delete Operation
* Edit Forms
* get_or_404()

### Code Explanation

#### Update Operation

```python
user.name = request.form.get("name")
```

Updates existing database record values.

#### Delete Operation

```python
db.session.delete(user)
```

Marks the record for deletion.

#### Commit Changes

```python
db.session.commit()
```

Persists all pending database modifications.

#### get_or_404()

```python
User.query.get_or_404(user_id)
```

Returns the requested record or automatically raises 404 if not found.

---

## Day 17 - Validation and User Experience Improvements

### Work Completed

* Added duplicate email validation
* Added flash success/error messages
* Added delete confirmation popup
* Improved update validation logic

### Concepts Covered

* Duplicate Data Prevention
* Flash Messaging
* Validation Logic
* Confirmation Dialogs

### Code Explanation

#### Duplicate Validation

```python
User.query.filter_by(email=email).first()
```

Checks whether the email already exists before insertion.

#### Excluding Current User During Update

```python
User.id != user_id
```

Prevents duplicate validation from matching the current user record.

#### Flash Messages

Used to display temporary:

* Success notifications
* Error messages
* Validation feedback

#### Delete Confirmation

```html
onclick="return confirm(...)"
```

Shows browser confirmation before deleting a record.

---

## Day 18 - Search and Filter Functionality

### Work Completed

* Added search form to dashboard
* Implemented filtering by name/email
* Added dynamic query parameter support
* Built searchable admin panel behavior

### Concepts Covered

* Query Parameters
* Search Forms
* SQLAlchemy Filtering
* Case-Insensitive Search

### Code Explanation

#### Query Parameters

```python
request.args.get("search")
```

Reads values from URL query string:

```bash
/?search=sahil
```

#### Case-Insensitive Search

```python
User.name.ilike(...)
```

Allows matching regardless of uppercase/lowercase.

#### Multi-Field Filtering

```python
(User.name.ilike(...)) | (User.email.ilike(...))
```

Searches across multiple database columns.

#### Why This Matters

Search/filtering is essential in:

* Admin dashboards
* CMS systems
* Internal management tools

---

## Day 19 - Sorting and Pagination

### Work Completed

* Added sorting by name (A-Z / Z-A)
* Implemented pagination system
* Added page navigation controls
* Combined search, sort, and pagination together

### Concepts Covered

* Pagination
* Sorting
* Query Parameter Handling
* Efficient Data Loading

### Code Explanation

#### Pagination

```python
query.paginate(page=page, per_page=3)
```

Splits results into manageable pages.

Provides:

* items
* page
* pages
* has_next
* has_prev

#### Sorting

```python
User.name.asc()
User.name.desc()
```

Orders query results alphabetically.

#### Page Query Parameter

```python
request.args.get("page")
```

Reads page number from URL:

```bash
/?page=2
```

#### Why Pagination Matters

Large datasets should never load all records at once.

Production systems always:

* Paginate
* Filter
* Sort

---

## Overall Learning Outcomes

After completing Chapter 05, I can:

* Integrate Flask with SQLite database
* Build complete CRUD applications
* Validate and protect database integrity
* Implement search and filtering systems
* Add sorting and pagination for scalability
* Structure admin-style dashboards

---

## Progress

Completed:

* Day 15
* Day 16
* Day 17
* Day 18
* Day 19

Next:

* Chapter 06 - REST API Development
