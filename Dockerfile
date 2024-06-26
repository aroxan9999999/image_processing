# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Экспортируем переменные окружения
ENV DB_HOST=db \
    DB_PORT=5432 \
    REDIS_URL=redis://redis:6379/1

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
