# Backend Starter Kit (Python + FastAPI)

## Goal

This repository is the starting point of a **production-minded backend project** built step by step over several months.

The goal is not just to make the application run, but to:
- understand *why* each file exists
- build a clean, scalable structure
- develop the correct architectural mindset for real-world backend systems

---

## Tech Stack (Target)

- Python 3.x
- FastAPI
- (Later) PostgreSQL
- (Later) Redis
- (Later) pytest
- (Later) Docker & CI

> Not all tools are used yet.  
> They will be introduced gradually, with clear reasoning.

---

## Current Status (End of Week 1 – Day 5)

At this stage:

- The repository is initialized and clean
- FastAPI application runs successfully
- A basic `/health` endpoint is implemented
- Python typing is introduced for clarity and correctness
- Project structure is intentionally minimal
- Path handling is based on `pathlib` to ensure future stability

The focus so far has been:
- correctness over shortcuts
- understanding over speed
- foundations over features

---

## Project Philosophy

This project follows these principles:

- **Separation of concerns**  
  Code will be organized by responsibility, not convenience.

- **Growth-aware design**  
  Decisions are made with future scaling in mind.

- **Explicit over implicit**  
  Nothing is added “because it works” — every part must be explainable.

- **Production mindset from day one**  
  Even simple code should not create future traps.

---

## Project Structure (Current)

```text
backend-starter/
├── app/
│   └── main.py        # FastAPI entrypoint
├── README.md
├── .gitignore
````

> More layers (api, domain, application, infrastructure)
> will be added progressively when their purpose is clear.

---

## How to Run (Development)

```bash
uvicorn app.main:app --reload
```

Then open:

```
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status": "ok"}
```

---

## Notes

This repository is intentionally simple at the beginning.

Complexity will be introduced **only when it becomes necessary**,
and always with a clear explanation of *why*.

---

## Progress Log

* [x] Project initialization
* [x] Git repository setup
* [x] Virtual environment
* [x] FastAPI basic app
* [x] `/health` endpoint
* [x] Python typing basics
* [x] Path handling with `pathlib`

---

## Disclaimer

This project is part of a structured learning path.
Refactoring and changes are expected as understanding deepens.

```

---