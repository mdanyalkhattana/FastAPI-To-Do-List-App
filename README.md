
# ✅ FastAPI To-Do List App

A clean and powerful **To-Do List REST API** built with **FastAPI**, **SQLAlchemy**, and **MySQL (XAMPP)**.  
This project demonstrates how to build a modern backend using FastAPI — including **CRUD operations**, **database models**, and **schema validation**.

---

## 🚀 Features

- ✨ Fast and asynchronous API built with **FastAPI**
- 🧠 Data modeling using **SQLAlchemy ORM**
- 🔐 Validation and serialization using **Pydantic**
- 💾 MySQL database (via XAMPP)
- ✅ Full CRUD operations (Create, Read, Update, Delete)
- 🕹️ Mark tasks as completed
- 🌐 CORS enabled — ready for frontend integration (React, Vue, etc.)
- ⚙️ Modular structure — clean, scalable, and easy to extend

---

## 📂 Project Structure

```

todo_list/
│
├── main.py                     # FastAPI entry point
├── database.py                 # MySQL connection engine + session setup
│
├── models/
│   └── task_model.py           # SQLAlchemy model (Task)
│
├── schemas/
│   └── task_schema.py          # Pydantic schemas (TaskBase, TaskCreate, TaskUpdate)
│
├── crud/
│   └── task_crud.py            # Database operations (CRUD logic)
│
├── routers/
│   └── tasks.py                # All /tasks endpoints (API routes)
│
└── requirements.txt            # All dependencies

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/todo-list-fastapi.git
cd todo-list-fastapi
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # (Windows)
# OR
source venv/bin/activate # (Mac/Linux)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database (XAMPP)

1. Start **Apache** and **MySQL** from XAMPP Control Panel.
2. Open **phpMyAdmin** → create a new database, e.g. `todo_db`.
3. Update your `database.py` connection string:

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/todo_db"
```

> ⚠️ If your MySQL has a password, update it accordingly.

### 5️⃣ Create Tables

Run this once to create tables in your MySQL database:

```bash
python
>>> from database import Base, engine
>>> from models.task_model import Task
>>> Base.metadata.create_all(bind=engine)
>>> exit()
```

### 6️⃣ Run the Server

```bash
uvicorn main:app --reload
```

Server will start at 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧭 API Endpoints

| Method     | Endpoint               | Description                               |
| :--------- | :--------------------- | :---------------------------------------- |
| **POST**   | `/tasks/`              | Create a new task                         |
| **GET**    | `/tasks/`              | Get all tasks                             |
| **GET**    | `/tasks/{id}`          | Get a task by ID                          |
| **PUT**    | `/tasks/{id}`          | Update task (title/description/completed) |
| **PATCH**  | `/tasks/{id}/complete` | Mark task as completed                    |
| **DELETE** | `/tasks/{id}`          | Delete task                               |

---

## 🧩 Example JSON Payloads

### ➕ Create Task

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

### 📝 Update Task

```json
{
  "title": "Buy groceries (updated)",
  "description": "Milk, eggs, bread, butter",
  "completed": true
}
```

---

## 🧠 Tech Stack

| Component      | Technology        |
| -------------- | ----------------- |
| **Backend**    | FastAPI           |
| **Database**   | MySQL (via XAMPP) |
| **ORM**        | SQLAlchemy        |
| **Validation** | Pydantic          |
| **Server**     | Uvicorn           |

---

## 🧪 Testing the API

You can test endpoints using:

* 🔹 **FastAPI Swagger UI:**
  Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* 🔹 **Postman or Thunder Client** (VS Code Extension)

---

## 📸 Screenshots (Optional)

> You can add screenshots of:
>
> * Your FastAPI Swagger UI
> * Database (phpMyAdmin)
> * Example request/response in Postman

---

## 🤝 Contribution Guide

Contributions are always welcome!

1. Fork the repository
2. Create a new branch (`feature/new-feature`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to your branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 💬 Contact

**Author:** [Your Name]
📧 **Email:** [your.email@example.com](mailto:your.email@example.com)
🌐 **GitHub:** [https://github.com/your-username](https://github.com/your-username)

---

## 🪄 License

This project is licensed under the **MIT License** — feel free to use and modify it.

---
 
Which one would you like next?
```
