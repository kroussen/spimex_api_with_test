from celery import Celery
from celery.schedules import crontab
import logging
import os


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

broker_url = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
result_backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

celery_app = Celery('spimex_api', broker=broker_url, backend=result_backend)

celery_app.conf.update(
    result_expires=3600,
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
)

celery_app.conf.timezone = "Europe/Moscow"


celery_app.conf.beat_schedule = {
    'check-task-execution-time': {
        'task': 'source.celery_tasks.tasks.check_execution_time',
        'schedule': crontab(minute="*", day_of_week='*'),
    },
}
