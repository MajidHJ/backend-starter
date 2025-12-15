# 📘 Day 02 --- Creating Project Scaffold

## 🎯 Goals for Today

A clean, reproducible virtual environment
Installing dependencies with pip inside the venv (FastAPI + Uvicorn)
Running the project in a real setup using:
uvicorn app.main:app --reload
A deep understanding of these (not rote memorization):
pip vs pipx
module vs package
The role of __init__.py
The import system and why it is critical in multi-layered projects


------------------------------------------------------------------------

### What I Learned (Week 1 – Day 2)

* I learned how to correctly create and activate a **Python virtual environment (venv)** and why each project must have its own isolated environment.
* I understand why the **virtual environment should be located at the root of the repository** and what kinds of problems occur if it is created elsewhere.
* I learned how `pip install` behaves **inside an active virtual environment** and how to verify that packages are not being installed globally.
* I now clearly understand the difference between **runtime dependencies** (such as `fastapi` and `uvicorn`) and **development tools** (such as formatters and linters).
* I understand the architectural difference between **FastAPI as an application framework** and **Uvicorn as an ASGI server that runs the application**.
* I learned what **ASGI** is and why FastAPI requires an ASGI server to handle HTTP requests.
* I learned the correct pronunciation and role of **Uvicorn** in a backend architecture.
* I understand what `pip freeze` does, what it actually **freezes**, and how `requirements.txt` is generated.
* I learned that `requirements.txt` does not need to exist beforehand and when freezing dependencies makes sense.
* I now understand how Python’s **import system** works and the order in which Python resolves imports.
* I learned the meaning of `.` and `./` in filesystem paths and why `./.venv/...` is used for explicit execution.
* I understand the difference between a **module** and a **package** in Python.
* I learned what `__init__.py` is, what problem it solves, and why explicitly defining packages matters in larger projects.
* I understand how `uvicorn app.main:app` relies on Python’s import system to locate and run the application object.
* I learned how to verify that a package is being imported **from the virtual environment** rather than from the global system.

---

------------------------------------------------------------------------