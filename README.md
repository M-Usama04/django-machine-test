# Django Machine Test – Client & Project Management API (PostgreSQL)

## 🚀 Project Overview

This is a Django REST Framework (DRF) based backend system for managing **Users**, **Clients**, and **Projects** as part of a machine test. The application is powered by **PostgreSQL** and demonstrates clean architecture, token-based authentication, and modular design.

> 📊 **Review Purpose**: This README serves as a technical brief for the reviewing team to evaluate API structure, functionality, and codebase.

---

## ✨ Core Functionalities Implemented

| # | Feature Description                            | Endpoint                           | Status |
| - | ---------------------------------------------- | ---------------------------------- | ------ |
| 1 | Create a new client                            | `POST /api/clients/`               | ✅      |
| 2 | Fetch all clients                              | `GET /api/clients/`                | ✅      |
| 3 | Retrieve client details + associated projects  | `GET /api/clients/<id>/`           | ✅      |
| 4 | Update client info                             | `PATCH /api/clients/<id>/`         | ✅      |
| 5 | Delete a client                                | `DELETE /api/clients/<id>/`        | ✅      |
| 6 | Create a project for a client and assign users | `POST /api/clients/<id>/projects/` | ✅      |
| 7 | Fetch projects assigned to logged-in user      | `GET /api/projects/`               | ✅      |

### Relationships

* One Client ➔ Many Projects
* One Project ➔ Many Users (M2M)
* One User ➔ Many Assigned Projects

---

## 📊 Database Used

**PostgreSQL** (production-ready setup)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'machine_test',
        'USER': 'machine_test',
        'PASSWORD': 'usama123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🛠️ Setup Instructions (Local Development)

```bash
# Clone repository
https://github.com/M-Usama04/django-machine-test.git
cd django-machine-test

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Superuser Credentials (used for testing):

```
Username: Machine_test
Password: Usama@123
```

---

## 🔑 Authentication (Token-Based)

**Login Endpoint:** `POST /api-token-auth/`

**Request Body:**

```json
{
  "username": "testuser",
  "password": "testpass"
}
```

**Use Token in Header:**

```
Authorization: Token your_token_here
```

---

## 🔄 API Endpoints Summary

### Clients

| Method | Endpoint           | Description                          |
| ------ | ------------------ | ------------------------------------ |
| GET    | /api/clients/      | List all clients                     |
| POST   | /api/clients/      | Create new client                    |
| GET    | /api/clients/<id>/ | Retrieve a client and their projects |
| PATCH  | /api/clients/<id>/ | Update client details                |
| DELETE | /api/clients/<id>/ | Delete client                        |

### Projects under Client

| Method | Endpoint                    | Description                            |
| ------ | --------------------------- | -------------------------------------- |
| POST   | /api/clients/<id>/projects/ | Add project to a client + assign users |

### Logged-in User's Projects

| Method | Endpoint       | Description                              |
| ------ | -------------- | ---------------------------------------- |
| GET    | /api/projects/ | List projects assigned to logged-in user |

---

## 🔢 Sample Request/Response

### Create Client

```http
POST /api/clients/
{
  "client_name": "Infotech"
}
```

**Response**:

```json
{
  "status": "success",
  "message": "Client created successfully",
  "data": {
    "id": 1,
    "client_name": "Infotech",
    "created_by": "Machine_test",
    "created_at": "2025-07-12T13:23:00",
    "updated_at": null,
    "projects": []
  }
}
```

### Create Project

```http
POST /api/clients/1/projects/
{
  "project_name": "Project A",
  "users": [1]
}
```

**Response**:

```json
{
  "status": "success",
  "message": "Project created successfully",
  "data": {
    "id": 3,
    "project_name": "Project A",
    "client": "Infotech",
    "users": [
      {
        "id": 1,
        "username": "testuser"
      }
    ],
    "created_by": "Machine_test",
    "created_at": "2025-07-12T13:23:00",
    "updated_at": null
  }
}
```

---

## 📈 Test Cases (DRF API Test Coverage)

All unit tests are located in `core/tests.py` and validate:

* ✅ Client creation (201)
* ✅ Get all clients (200)
* ✅ Client update (PATCH)
* ✅ Project creation under client
* ✅ Get user-assigned projects

**Run all tests:**

```bash
python manage.py test
```

---

## 🔹 Admin Panel Access

```
http://127.0.0.1:8000/admin/
```

Login with superuser to:

* Manage Users
* View Clients/Projects
* Tokens and related models

---

## 🔹 Contribution & Feedback

* This repo is **public** but write access is limited to the owner.
* Others may **Fork** or **Open Issues** for suggestions.

---

## 🙌 Author

**Usama Mulla**

Built for machine test submission. Feedback & collaboration welcome.

---

## 🚨 Important Notes

* No frontend UI included. API-only backend.
* Use Postman/cURL for testing.
* Project follows best practices with token auth and PostgreSQL.

---

## 🎯 Future Work (Optional)

* Swagger/OpenAPI docs
* Pagination, Filtering, Search
* Dockerization & CI
* Rate limiting & permissions
