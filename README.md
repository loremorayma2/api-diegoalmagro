# 🏪 Diego de Almagro Marketplace API

**A modern RESTful API built with FastAPI to empower local entrepreneurs in Chile.**  
This backend system enables users to authenticate, manage their products, and handle orders in a scalable and secure way.

---

## 🚀 Features

- JWT-based authentication
- CRUD operations for products
- Order creation with basic stock validation
- Role-based user management (optional)
- Clean modular architecture using FastAPI + SQLAlchemy
- Auto-generated interactive documentation (Swagger & Redoc)
- Documentation API with markdown web page
  → Available at: [https://api-diegoalmagro.up.railway.app/docs/api](https://api-diegoalmagro.up.railway.app/docs/api)

---

## 📌 Main Endpoints

| Method | Endpoint                 | Description                            |
|--------|--------------------------|----------------------------------------|
| POST   | `/api/v1/auth/login`     | Login and retrieve JWT token           |
| GET    | `/api/v1/users/me`       | Get current authenticated user info    |
| GET    | `/api/v1/products`      | List all products                      |
| POST   | `/api/v1/products`      | Create a new product                   |
| POST   | `/api/v1/orders`        | Create a new order                     |

---

## 📚 Interactive API Docs

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Markdown API Reference**: [https://api-diegoalmagro.up.railway.app/docs/api](https://api-diegoalmagro.up.railway.app/docs/api)  
  (Web-accessible API documentation written in Markdown for developers)

---

## 🧱 Technology Stack

- **Python 3.13+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **JWT (JSON Web Tokens)**
- **PostgreSQL / SQLite (configurable)**
- **Uvicorn** (ASGI server)
- **pytest** (for testing)

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-org/diegodealmagro-api.git
cd diegodealmagro-api
```
### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Create and activate a virtual environment

```bash
pip install -r requirements.txt
```

### 4. Run the API locally

```bash
uvicorn app.main:app --reload
```

---

## 🛠️ Project Structure

```text
app/
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── routers/             # Route definitions (auth, users, products, orders)
├── core/                # Security, configs, dependencies
├── database/            # DB connection setup
└── tests/               # Unit tests
.gitignore               # Git ignored files config
.env                     # Environment variables
requirements.txt         # Python dependencies
runtime.txt              # Python version for production (optional)
README.md                # Project summary
main.py                  # App entry point
```

---

## 🔐 Authentication

* Uses OAuth2 with JWT Bearer tokens

* Pass the token in the Authorization header:

```http
Authorization: Bearer <your_token_here>
```

---

## 🧪 Testing

* To run tests (if added):

```bash
pytest
```
---

## 📄 License

This project is proprietary and owned by Diego de Almagro.
All rights reserved. Unauthorized use, reproduction, or distribution is prohibited unless explicitly permitted by the project owners.

---