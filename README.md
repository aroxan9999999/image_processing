
# API для обработки изображений

## Обзор

Этот проект представляет собой API для обработки изображений, поддерживающий высокую загрузку изображений. Он построен с использованием Django, Celery, Redis и AWS S3 для хранения. API обрабатывает загрузку, обработку и хранение изображений в различных размерах.

## Функциональность

- Загрузка оригинальных изображений.
- Генерация нескольких версий изображений:
  - Миниатюра (150x120)
  - Большая миниатюра (700x700)
  - Большое изображение (1920x1080)
  - D2500 (2500x2500)
- Хранение изображений в AWS S3.
- Использование Celery для фоновой обработки.
- Docker для легкого развертывания.

## Установка

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/aroxan9999999/image_processing/
   cd image_processing_api
   ```

2. **Создание и заполнение файла .env**:

   ```plaintext
   # Django secret key
   SECRET_KEY=ваш_секретный_ключ

   # Режим отладки
   DEBUG=True

   # Разрешенные хосты
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Конфигурация базы данных
   DB_NAME=image_processing_db
   DB_USER=ваш_пользователь_базы_данных
   DB_PASSWORD=ваш_пароль_базы_данных
   DB_HOST=localhost
   DB_PORT=5432

   # Конфигурация Redis
   REDIS_URL=redis://localhost:6379/1

   # Конфигурация Celery
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=django-db

   # Конфигурация AWS S3
   AWS_ACCESS_KEY_ID=ваш_ключ
   AWS_SECRET_ACCESS_KEY=ваш_секретный_ключ
   AWS_STORAGE_BUCKET_NAME=ваше_имя_бакета
   AWS_REGION=ваш_регион
   ```

3. **Запуск Docker Compose**:

   ```bash
   docker-compose up --build
   ```

## Использование

### Загрузка изображения

```bash
curl -X POST http://127.0.0.1:8000/api/images/upload/     -F "original=@/путь/к/вашему/изображению.jpg"     -F "project_id=111"
```

### Получение списка изображений для проекта

```bash
curl -X GET http://127.0.0.1:8000/projects/111/images/
```
