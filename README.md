# Training_FastAPI
Репозиторий для изучения и практики работы с библиотекой FastAPI.

Проект на базе FastAPI, который объединяет:

- **FastAPI** — современный и быстрый веб-фреймворк
- **Pydantic** — валидация и сериализация данных
- **Typer** — удобная CLI-обёртка (например, для запуска сервера)

---

## Что будет в проекте:

- `GET /users` — получить всех пользователей
- `POST /users` — создать нового пользователя
- Хранилище данных — в памяти
- CLI через Typer: `runserver`, `create-user`
- Использование `FastAPI` как ASGI-приложения

---

## Как использовать

### Установка

```bash
cd fastapi_project
pip install -r requirements.txt
```

---

### Запуск API сервера

```bash
python3 -m app.main runserver
```

Откроется FastAPI-приложение на:

- Документация OpenAPI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Альтернативная документация: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
    

---

### Добавление пользователя через CLI

```bash
python3 -m app.main create-user 1 Alice --age 25
```

---
### Создание пользователя через API:

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"id": 2, "name": "Bob", "age": 30}'
```
