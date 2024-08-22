# Builder stage
FROM python:3.12-slim AS builder

RUN set -ex \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Create a virtual environment
RUN python3 -m venv /venv

# Workdir
WORKDIR /app

# Install dependencies using poetry
# Copy migrations
COPY ./migrations /app/migrations
COPY pyproject.toml poetry.lock alembic.ini /app/
RUN set -ex \
    && . /venv/bin/activate \
    && ~/.local/bin/poetry install

# Copy app
COPY ./app /app/app