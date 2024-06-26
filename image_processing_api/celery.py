from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Убедитесь, что используется правильный модуль настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_processing_api.settings')

app = Celery('image_processing_api')

# Загружает настройки из настроек Django с префиксом `CELERY_`
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживает задачи в файлах tasks.py каждого приложения Django
app.autodiscover_tasks()
