# Tasks API

A simple REST API for managing a to-do list, built with **FastAPI** and **SQLite** (via SQLModel). Tasks are stored in a single database file that both the API and any SQLite browser can read directly.

## Why SQLite?

- **Single file** — the entire database is one `tasks.db` file on disk, no server process to install or manage.
- **Zero setup** — the file is created automatically on first run, so the project works out of the box after cloning.
- **Survives restarts** — data is persisted to disk, so your tasks are still there after stopping or restarting the API.

## Where the database file lives

- The database is `tasks.db`, located in the project root (same folder as `main.py`).
- It is **created automatically** the first time the app runs (`SQLModel.metadata.create_all`), and a few starter tasks are seeded if the table is empty.
<img width="810" height="171" alt="image" src="https://github.com/user-attachments/assets/ab3431c1-070d-4eaa-bd5e-3e9c08d38894" />

## Getting started

Install dependencies, then start the server with:

```bash
uvicorn main:app --reload
```

The API is then available at `http://127.0.0.1:8000` — interactive docs (Swagger UI) at `/docs`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | API name, version, and endpoint list |
| `GET` | `/health` | Health check (`{"status": "ok"}`) |
| `GET` | `/tasks` | List all tasks |
| `GET` | `/tasks/{id}` | Get one task (404 if not found) |
| `POST` | `/tasks` | Create a task (empty title → 400) |
| `PUT` | `/tasks/{id}` | Update a task's title and/or done |
| `DELETE` | `/task/{id}` | Delete a task |

## Example usage

```bash
# List tasks
curl http://127.0.0.1:8000/tasks

# Create a task
curl -X POST http://127.0.0.1:8000/tasks -H "Content-Type: application/json" -d '{"title": "read a book"}'

# Mark task 2 as done
curl -X PUT http://127.0.0.1:8000/tasks/2 -H "Content-Type: application/json" -d '{"title": "clean room", "done": true}'

# Delete task 3
curl -X DELETE http://127.0.0.1:8000/task/3
```

**Example query:**

```sql
SELECT * FROM tasks WHERE done = 1;
```

**Result:**

<img width="367" height="118" alt="image" src="https://github.com/user-attachments/assets/8976e431-d4c7-499b-8c78-a718818ab696" />
