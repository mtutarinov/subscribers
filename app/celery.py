from celery import Celery
from app.core.config import settings

app = Celery(settings.APP_NAME, broker=settings.CELERY_BROKER_URL, backend=settings.DB_URL)
app.autodiscover_tasks()