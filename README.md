# Task API

A small task-tracker API built with **FastAPI** + **SQLModel**, containerized with **Docker Compose**.

## Quickstart

Requires Docker + Docker Compose. Nothing else — no local Python, no manual database setup.

```bash
cp .env.example .env
docker compose up --build
```

Then:

- API root: <http://localhost:8000>
- Interactive docs: <http://localhost:8000/docs>
- `GET /tasks` returns the three seeded tasks

Stop with `docker compose down` (keeps data).

## Endpoints

| Method | Path | Input | Success | Errors |
| ------ | ---- | ----- | ------- | ------ |
| `GET` | `/` | — | `200` | — |
| `GET` | `/health` | — | `200` | — |
| `GET` | `/tasks` | — | `200` list of tasks | — |
| `GET` | `/tasks/{id}` | path: `id` (int) | `200` | `404` item not found |
| `POST` | `/tasks` | body: `{"title": "..."}`; optional query `?done=true` | `201` created task | `400` empty or missing title |
| `PUT` | `/tasks/{id}` | query: `title` and/or `done` (at least one) | `200` updated task | `400` no fields given · `404` not found |
| `DELETE` | `/tasks/{id}` | path: `id` (int) | `204` | `404` not found |

## Example request

```console
$ curl -i http://localhost:8000/tasks
HTTP/1.1 200 OK
date: Fri, 20 Nov 2026 10:14:02 GMT
server: uvicorn
content-length: 154
content-type: application/json

[{"id":1,"title":"untitled 1","done":false},
 {"id":2,"title":"untitled 2","done":false},
 {"id":3,"title":"untitled 3","done":false}]
```

Create a task:

```console
$ curl -i -X POST http://localhost:8000/tasks \
    -H 'content-type: application/json' \
    -d '{"title":"buy milk"}'
HTTP/1.1 201 Created
date: Fri, 20 Nov 2026 10:14:31 GMT
server: uvicorn
content-length: 41
content-type: application/json

{"id":4,"title":"buy milk","done":false}
```

## Data in the database

**Example in AGAdmin**


<img width="428" height="381" alt="image" src="https://github.com/user-attachments/assets/0dbcba41-0f4a-4ef6-91da-2d7d030bc583" />
