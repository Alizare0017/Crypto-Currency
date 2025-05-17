import os
from celery import Celery
from django.conf import settings
import redis

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Tehran')
app.config_from_object(settings, namespace='CELERY')
app.conf.accept_content = ['application/json', 'application/x-python-serialize', 'pickle']


# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
