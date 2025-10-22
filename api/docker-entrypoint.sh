#!/bin/bash
set -e

source /var/www/app/api/.venv/bin/activate

cd ..

alembic -c api/alembic.ini upgrade head

echo "Запускаем FastAPI..."
exec uv run fastapi dev --host 0.0.0.0 --port 8000
