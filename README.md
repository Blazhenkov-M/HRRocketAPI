# HR-Rocket

## Описание

Тестовое задание на должность Python Developer

## Ответственные лица

* Архитектор - [Михаил] (https://t.me/Mishanya_B)

## Установка и запуск

### Зависимости

- Python 3.12
- FastAPI
- Uvicorn
- и другие (см. `pyproject.toml` и `poetry.lock`)

### Запуск приложения

Для запуска приложения используйте команду:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Конфигурация

В файле `.env` для локальной разработки должны быть указаны следующие переменные. Обратите внимание, что приведённые
ниже значения являются примерами, и вам следует установить свои собственные значения для каждой переменной:

```plaintext
DATABASE_URL=postgresql+asyncpg://postgres:pass@localhost:5432/postgres
HOST=0.0.0.0
PORT=8080
```

В этом разделе дается пример конфигурации для локальной разработки. Пожалуйста, адаптируйте эти настройки в соответствии
с вашей инфраструктурой и требованиями безопасности.

### Makefile

```bash

build:
	docker compose -f docker-compose-local.yaml build
up:
	make build
	docker compose -f docker-compose-local.yaml up -d
	make migrate
run:
	make build
	docker compose -f docker-compose-local.yaml up hr-rocket

down:
	docker compose -f docker-compose-local.yaml down

purge:
	docker compose -f docker-compose-local.yaml down -v && docker system prune --force --volumes
```
