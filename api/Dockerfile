FROM python:3.13-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libpq-dev \
       curl \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /var/www/app/

COPY pyproject.toml uv.lock ./
COPY . .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir uv \
    && uv sync --frozen --no-cache


EXPOSE 8000


CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]