# 🎓 Student Grade Tracker

> A simple, clean system for storing and managing student grades — built as a backend API.

---

## 🧠 What Is This Project? (In Plain English)

Imagine you are a teacher or a school administrator. You have a list of students, and each student has:
- A **name**
- A **course** they are taking
- A **grade** (their score)
- An **email address**

Now, instead of writing all of this in a notebook or an Excel sheet, this project gives you a **smart digital system** where you can:

- ✅ **Add** a new student and their grade
- 📋 **View** all students at once
- 🔍 **Search** for a specific student by their ID number
- ✏️ **Update** a student's information (e.g., correct a grade or change their course)
- 🗑️ **Delete** a student's record when needed

Think of it like a **digital register** — but smarter, faster, and accessible from anywhere.

---

## 🏗️ How Does It Work? (The Big Picture)

This project is a **REST API**. Don't let that term scare you!

An API is simply a **messenger**. When you want to get student data, you send a request (like sending a text message), and the API replies back with the information you need.

Here is an analogy:
> 🍔 Think of a restaurant. You (the customer) don't go into the kitchen yourself. You tell the **waiter** (the API) what you want. The waiter goes to the **kitchen** (the database), gets your food (the data), and brings it back to you.

That is exactly what this project does — it acts as the waiter between **you** and the **student database**.

---

## 🗂️ What's Inside the Project? (File by File)

Here is a breakdown of every file in this project and what it does — in simple terms:

| File | What It Does |
|------|-------------|
| `main.py` | The **front door** of the app. This is where all the routes (web addresses) are defined — like `/students` to see all students. |
| `database.py` | Sets up the **connection to the database**. Think of it as plugging in the power cable to a storage system. |
| `models.py` | Describes the **shape of the data**. It tells the system: "A student has a name, a course, a grade, and an email." |
| `schemas.py` | Acts as a **gatekeeper**. It checks that the data coming in (and going out) is in the correct format — no missing fields, no wrong data types. |
| `crud.py` | Contains all the **actions** — Create, Read, Update, Delete. This is where the actual work happens. |
| `grades.db` | The actual **database file** where all student records are saved on your computer. |

---

## ⚙️ The Four Main Actions (CRUD)

CRUD stands for **Create, Read, Update, Delete**. These are the four basic things any data system needs to be able to do. Here's what each one means in this project:

### ➕ Create — Add a New Student
Send the student's name, course, grade, and email → the system saves them and gives them a unique ID number.

### 📖 Read — View Students
- Get the **full list** of all students at once.
- Or look up **one specific student** using their ID number.

### ✏️ Update — Edit Student Info
Already saved a student but their grade changed? No problem — send only the field you want to change and the system updates just that part.

### 🗑️ Delete — Remove a Student
If a student leaves or was added by mistake, you can permanently remove their record using their ID.

---

## 🌐 How to Use It (The Web Addresses / Endpoints)

Once the app is running, you can interact with it by visiting these addresses in a tool like [Postman](https://www.postman.com/) or the built-in docs page:

| Action | Method | Address | What It Does |
|--------|--------|---------|-------------|
| Add a student | `POST` | `/students` | Creates a new student record |
| Get all students | `GET` | `/students/` | Returns a list of every student |
| Get one student | `GET` | `/students/{id}` | Returns one student by their ID |
| Update a student | `PUT` | `/students/{id}` | Updates a student's information |
| Delete a student | `DELETE` | `/students/{id}` | Removes a student from the system |

> 💡 Replace `{id}` with the actual number, e.g. `/students/3` to get student number 3.

---

## 🧰 What Technologies Were Used?

You don't need to understand all of these deeply, but here's what powers this project:

| Technology | Role | Simple Explanation |
|------------|------|--------------------|
| **Python** | Programming Language | The language this entire project is written in |
| **FastAPI** | Web Framework | The tool that handles incoming requests and sends responses |
| **SQLAlchemy** | Database Connector | The bridge between Python code and the database |
| **SQLite** | Database | A lightweight database that stores all student data in a single file (`grades.db`) |
| **Pydantic** | Data Validator | Makes sure all data sent to the API is valid and complete |
| **Uvicorn** | Server | The engine that runs the app so it can receive requests |

---

## 🚀 How to Run This Project on Your Computer

Follow these steps one at a time. You will need **Python** installed on your computer.

### Step 1 — Download the project
```bash
git clone https://github.com/GithinjiVictor/student-grade-tracker.git
```

### Step 2 — Go into the project folder
```bash
cd student-grade-tracker
```

### Step 3 — Create a virtual environment
*(This is like a private workspace so the project's tools don't interfere with anything else on your computer)*
```bash
python -m venv myvenv
```

### Step 4 — Activate the virtual environment

On **Windows**:
```bash
myvenv\Scripts\activate
```

On **Mac/Linux**:
```bash
source myvenv/bin/activate
```

### Step 5 — Install the required tools
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### Step 6 — Start the app
```bash
uvicorn main:app --reload
```

### Step 7 — Open it in your browser
Visit 👉 **http://127.0.0.1:8000/docs**

You will see a beautiful, interactive page where you can test every feature of the API — no extra tools needed!

---

## 📸 What the Docs Page Looks Like

When you open `http://127.0.0.1:8000/docs`, you will see a page called **Swagger UI**. It lists all the available actions and lets you try them out directly in your browser — like a control panel for the API.

---

## 💡 What a Student Record Looks Like

When you add a student, you send data that looks like this:

```json
{
  "name": "Jane Doe",
  "course": "Mathematics",
  "grade": 87.5,
  "email": "jane.doe@example.com"
}
```

And the system will respond with:

```json
{
  "id": 1,
  "name": "Jane Doe",
  "course": "Mathematics",
  "grade": 87.5,
  "email": "jane.doe@example.com"
}
```

Notice the system automatically adds an **`id`** — a unique number to identify each student.

---

## ❗ What Happens If Something Goes Wrong?

The system is built to handle errors gracefully:

- If you try to **find a student that doesn't exist**, you'll get a clear message:
  `"Student not found"` with a `404` error code.
- If you try to **add a student with a duplicate email**, the database will reject it (since emails must be unique).
- If you send **incomplete or wrong data**, the system will tell you exactly what's missing.

---

## 🤝 Author

**Victor Githinji**
Built during the Lux-Dev Internship Program.

---

## 📄 License

This project is open source and free to use for learning purposes.
