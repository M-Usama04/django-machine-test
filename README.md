# Django REST API – Machine Test Solution

## 🚀 Project: Client, Project & User Management API

This Django REST API project is a complete solution for the machine test problem involving the management of Users, Clients, and Projects. The system is built using Django and Django REST Framework (DRF), following best practices and secure token authentication.

---

## 📌 Features Implemented (As per Requirements)

| Feature # | Requirement                                  | Status                               |
| --------- | -------------------------------------------- | ------------------------------------ |
| 1         | Register a client                            | ✅ `POST /api/clients/`               |
| 2         | Fetch all client info                        | ✅ `GET /api/clients/`                |
| 3         | Edit/Delete client info                      | ✅ `PATCH / DELETE /clients/<id>/`    |
| 4         | Add projects under client & assign users     | ✅ `POST /api/clients/<id>/projects/` |
| 5         | Retrieve projects assigned to logged-in user | ✅ `GET /api/projects/`               |

Additional Considerations:

- ✅ Many Users
- ✅ Many Clients
- ✅ One Client → Many Projects
- ✅ One Project → Many Users (Many-to-Many)

---

## ⚙️ Technology Stack

- Python 3.11+
- Django 5.0+
- Django REST Framework
- Token Authentication (DRF AuthToken)
- SQLite3 (default DB)

---

## 🗂️ Folder Structure

```
├── machine_test/              # Django project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # Root URLs (includes core app)
│   └── ...
├── core/                      # Core app
│   ├── models.py              # Client, Project models
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # ViewSets and logic
│   ├── urls.py                # API routes
│   └── admin.py               # Admin registrations
├── manage.py
└── README.md                  # This documentation file
```

---

## 📦 Setup Instructions

```bash
# Step 1: Clone and navigate
cd django-machine-test

# Step 2: Create virtual env
python3 -m venv venv
source venv/bin/activate  # Mac/Linux

# Step 3: Install requirements
pip install -r requirements.txt

# Step 4: Run migrations
python manage.py makemigrations
python manage.py migrate

# Step 5: Create superuser
python manage.py createsuperuser

# Step 6: Run the server
python manage.py runserver
```

---

##  Authentication (Token-Based)

### Endpoint

`POST /api-token-auth/`

### Request Body

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Response

```json
{
  "token": "abc123..."
}
```

### Use in Headers

```
Authorization: Token abc123...
```

---

##  API Endpoints Summary

###  Clients

| Method | URL            | Description                          |
| ------ | -------------- | ------------------------------------ |
| GET    | /api/clients/  | List all clients                     |
| POST   | /api/clients/  | Create new client                    |
| GET    | /api/clients// | Retrieve client detail with projects |
| PATCH  | /api/clients// | Update client info                   |
| DELETE | /api/clients// | Delete a client                      |

###  Projects (Under Client)

| Method | URL                     | Description                                  |
| ------ | ----------------------- | -------------------------------------------- |
| POST   | /api/clients//projects/ | Create project under a client + assign users |

### 📂 Logged-in User Projects

| Method | URL            | Description                            |
| ------ | -------------- | -------------------------------------- |
| GET    | /api/projects/ | List all projects assigned to the user |

---

## ✅ Sample Inputs/Outputs

### Create Client

```json
POST /api/clients/
{
  "client_name": "Infotech"
}
```

**Response:**

```json
{
  "id": 1,
  "client_name": "Infotech",
  "created_by": "rohit",
  "created_at": "2025-07-12T13:23:00",
  "updated_at": null
}
```

### Create Project for Client

```json
POST /api/clients/1/projects/
{
  "project_name": "Project A",
  "users": [1]
}
```

**Response:**

```json
{
  "id": 1,
  "project_name": "Project A",
  "client": "Infotech",
  "created_by": "ganesh",
  "users": [
    {
      "id": 1,
      "name": "Rohit"
    }
  ],
  "created_at": "2025-07-12T13:25:00"
}
```

---

## 🧪 Postman API Testing

1. First, generate token: `POST /api-token-auth/`
2. Add token in header: `Authorization: Token <your_token>`
3. Test each endpoint with required body and method

---

## 📁 Admin Panel

URL: `http://127.0.0.1:8000/admin`

Use superuser credentials to:

- Manage Users
- View Clients & Projects
- View DRF Auth Tokens

---

## ✨ Notes

- DRF ViewSets + Routers used
- Full modular structure
- Fully authenticated and protected endpoints
- Easy to extend

---

## 👨‍💻 Author

**Usama Mulla**\
Built on MacBook Pro 15" using VS Code, Python 3.13, Django 5, and DRF.

---

## 🧭 Future Enhancements

- ✅ Swagger/OpenAPI Docs (DRF Yasg)
- ✅ Pagination and Filtering
- ✅ Role-based Authorization
- ✅ Email Notifications

## Note
> ⚠️ This is a backend-only project built with Django REST Framework.
> No frontend UI is included. Use tools like Postman or cURL to test APIs.
