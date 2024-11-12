from .celery_conf1 import app
from time import sleep

@app.task
def send_notification_task(user_id, message):
    sleep(2)
    print(f"Notification sent to user {user_id}: {message}")
