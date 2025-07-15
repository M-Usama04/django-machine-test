# Django Machine Test - REST API

##  Overview

This Django REST API project is designed to manage **Users**, **Clients**, and **Projects** as part of a Machine Test submission. It demonstrates full CRUD operations, token-based authentication, user-project assignment, and PostgreSQL integration using Django REST Framework.

---

## 🔧 Features Implemented

| Feature # | Requirement                             | Endpoint                              | Status |
| --------- | --------------------------------------- | ------------------------------------- | ------ |
| 1         | Register a new client                   | `POST /api/clients/`                  | ✅ Done |
| 2         | Fetch all clients                       | `GET /api/clients/`                   | ✅ Done |
| 3         | Retrieve/Edit/Delete client             | `GET/PATCH/DELETE /api/clients/<id>/` | ✅ Done |
| 4         | Add projects to client and assign users | `POST /api/clients/<id>/projects/`    | ✅ Done |
| 5         | Fetch logged-in user projects           | `GET /api/projects/`                  | ✅ Done |

**Relationships:**

* A client can have multiple projects.
* A project can be assigned to multiple users.

---

## Technology Stack

* Python 3.11+
* Django 5.0+
* Django REST Framework
* PostgreSQL (fully integrated)
* Token Authentication

---

## How Things Are Implemented

### Clients:

* Model: `core/models.py -> Client`
* API Logic: `core/views.py -> ClientViewSet`
* Serialization: `core/serializers.py -> ClientSerializer, ClientCreateSerializer`

### Projects:

* Model: `core/models.py -> Project`
* API Logic: `core/views.py -> ProjectCreateView, UserProjectsView`
* Serialization: `core/serializers.py -> ProjectDetailSerializer, ProjectCreateSerializer`

### Authentication:

* DRF Token Authentication used.
* Token generation endpoint: `POST /api-token-auth/`

### Testing:

* Tests written using `APITestCase` in `core/tests.py`
* 100% of major flows tested: create client, update, fetch, assign project, user project retrieval.

---

## 📁 PostgreSQL Configuration

**Location:** `machine_test/settings.py`

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

> ⚠️ Note: Do **not** expose credentials in public. Move to `.env` file in production.

---

## 🔢 How to Run & Test the App

```bash
# Clone the repo
$ git clone https://github.com/your-username/django-machine-test.git
$ cd django-machine-test

# Create and activate virtualenv
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Create superuser
$ python manage.py createsuperuser

# Run server
$ python manage.py runserver
```

## Testing API Endpoints

Use **Postman** or **cURL**:

* Get token: `POST /api-token-auth/`
* Add token to headers: `Authorization: Token <your_token>`
* Test endpoints (`/api/clients/`, `/api/projects/` etc.)

---

##  Test Cases Included

* Located in: `core/tests.py`
* Tests covered:

  * Client creation
  * Client retrieval
  * Client update
  * Project creation with user assignment
  * Logged-in user's project list

Run all tests:

```bash
$ python manage.py test
```

---

## ⚠️ Notes for Reviewers

* Credentials are **not** included in this repo. Please create a superuser to test.
* For demonstration, PostgreSQL database is used instead of SQLite.
* App has passed all test cases and mimics real-world relational structure.

---

##  Built With

* MacBook Pro 15"
* Python 3.13
* Django 5
* PostgreSQL 15
* DRF 3.x
* VS Code

---

##  License

This project is intended for educational and machine test evaluation purposes only.

---

*Developed by Usama Mulla*
