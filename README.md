# Backend Starter Kit (Python + FastAPI)

## Goal

This repository is part of a step-by-step learning journey to build a **production-minded backend starter kit** using Python and FastAPI.

The goal is not just to make the app work, but to understand:
- why the structure exists
- how the environment is managed
- how imports, dependencies, and execution really work

This project will gradually evolve into a clean, testable, and deployable backend foundation.

---

## Current Stage

**Month 1 – Week 1 – Day 2**  
**Focus:** Python Environment & Import System

At this stage, the focus is on setting up a **correct and reproducible development environment** and understanding how Python resolves imports in a real project.

The application logic is intentionally minimal.

---

## What Has Been Done So Far

### Environment
- A dedicated Python **virtual environment (`.venv`)** has been created at the root of the repository.
- All dependencies are installed **inside the virtual environment**, not globally.
- Dependency versions have been frozen for reproducibility.

### Dependencies
Installed runtime dependencies:
- FastAPI
- Uvicorn (with standard extras)

Current dependency snapshot is stored in:
```

requirements.txt

```

---

## Project Structure (Current)

```

backend-starter/
├── app/
│   ├── **init**.py
│   └── main.py
├── .venv/
├── requirements.txt
├── .gitignore
└── README.md

````

### Notes
- `app` is an explicit Python package (via `__init__.py`)
- `main.py` contains the minimal FastAPI application object
- No endpoints are implemented yet by design

---

## Running the Application

Activate the virtual environment first:

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
````

**macOS / Linux:**

```bash
source ./.venv/bin/activate
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

If successful, the application starts and FastAPI’s interactive docs are available at:

```
http://127.0.0.1:8000/docs
```

---

## What This Stage Is About

At Day 2, the project intentionally focuses on fundamentals:

* Why each project needs its own virtual environment
* How `pip` installs dependencies inside that environment
* The difference between modules and packages
* Why `__init__.py` matters in real-world projects
* How `uvicorn app.main:app` uses Python’s import system

No business logic or endpoints are added yet on purpose.

---

## Next Step

**Day 3 – FastAPI Basics & First Endpoint**

* Add the first real endpoint (`/health`)
* Understand how FastAPI routes work
* Confirm the application is truly “alive”

---

## Status

✅ Environment set up correctly
✅ Dependencies isolated and reproducible
✅ Application runs successfully
🟡 Business logic and API endpoints coming next

```

---
