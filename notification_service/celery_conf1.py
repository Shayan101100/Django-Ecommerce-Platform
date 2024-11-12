
import os
from celery import Celery

#Set the default Django setting modual for the celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','charsu.settings')
app = Celery('notification_service.celery_conf1')
#apply config from Canfig class 
app.config_from_object('notification_service.config_redis.Config')

#Auto-discover tasks from task.py
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
